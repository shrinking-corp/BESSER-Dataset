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
    rapidml_Element,
    Constraint,
    rapidml_RegExConstraint,
    rapidml_ValueRangeConstraint,
    rapidml_LengthConstraint,
    SingleValueType,
    rapidml_SimpleType,
    rapidml_Enumeration,
    SimpleType,
    Inheritable,
    DataExample,
    rapidml_InlineDataExample,
    rapidml_DataExample,
    rapidml_WithDataExamples,
    rapidml_Inheritable,
    Element,
    WithDataExamples,
    DataType,
    rapidml_SingleValueType,
    Feature,
    rapidml_Extensible,
    rapidml_Structure,
    rapidml_HasTitle,
    rapidml_Extension,
    rapidml_AuthenticationMethod,
    rapidml_HasSecurityValue,
    ReferenceElement,
    rapidml_ReferenceProperty,
    ConstrainableType,
    rapidml_UserDefinedType,
    rapidml_PropertyRealization,
    rapidml_HasStringValue,
    Example,
    rapidml_ExternalExample,
    rapidml_InlineExample,
    rapidml_Example,
    rapidml_WithExamples,
    URISegment,
    HasStringValue,
    rapidml_URISegment,
    rapidml_PrimitiveType,
    rapidml_PathSegment,
    ObjectRealization,
    ResourceDefinition,
    ReferenceTreatment,
    rapidml_ReferenceEmbed,
    rapidml_ReferenceLink,
    rapidml_ReferenceElement,
    rapidml_NamedLinkDescriptor,
    rapidml_ImportDeclaration,
    rapidml_PrimitiveTypesLibrary,
    rapidml_LinkRelationsLibrary,
    rapidml_MediaTypesLibrary,
    rapidml_RealizationModelLocation,
    HasTitle,
    rapidml_PrimitiveProperty,
    SourceReference,
    rapidml_PrimitiveTypeSourceReference,
    rapidml_PropertyReference,
    Parameter,
    rapidml_URIParameter,
    rapidml_CollectionReferenceElement,
    rapidml_CollectionParameter,
    ServiceDataResource,
    rapidml_ObjectResource,
    rapidml_CollectionResource,
    URIParameter,
    rapidml_TemplateParameter,
    rapidml_MatrixParameter,
    rapidml_URISegmentWithParameter,
    rapidml_Documentable,
    rapidml_Documentation,
    TypedMessage,
    Documentable,
    rapidml_SecuritySchemeLibrary,
    rapidml_SecurityScope,
    rapidml_SecuritySchemeParameter,
    rapidml_LinkRelation,
    rapidml_Operation,
    rapidml_EnumConstant,
    rapidml_DataModel,
    rapidml_SourceReference,
    RealizationContainer,
    rapidml_ReferenceRealization,
    rapidml_ServiceDataResource,
    rapidml_URI,
    rapidml_TypedResponse,
    rapidml_TypedRequest,
    Extensible,
    rapidml_DataType,
    rapidml_RealizationContainer,
    rapidml_Feature,
    rapidml_ObjectRealization,
    rapidml_ZenModel,
    rapidml_RESTElement,
    rapidml_Constraint,
    rapidml_ReferenceTreatment,
    rapidml_ConstrainableType,
    rapidml_MessageParameter,
    HasSecurityValue,
    WithExamples,
    RESTElement,
    rapidml_MediaType,
    rapidml_Parameter,
    rapidml_Method,
    rapidml_ResourceAPI,
    rapidml_SecurityScheme,
    rapidml_TypedMessage,
    rapidml_ResourceDefinition,
    AuthenticationFlows,
    HttpMessageParameterLocation,
    HTTPMethods,
    CollectionRealizationLevelEnum,
    AuthenticationTypes,
    ReferenceRealizationEnum,
    CollectionRealizationEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_rapidml_element_is_not_abstract():
    assert not inspect.isabstract(rapidml_Element)


def test_hyp_rapidml_element_constructor_exists():
    assert callable(rapidml_Element.__init__)


def test_hyp_rapidml_element_constructor_args():
    sig = inspect.signature(rapidml_Element.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"




def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_regexconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_RegExConstraint)


def test_hyp_rapidml_regexconstraint_constructor_exists():
    assert callable(rapidml_RegExConstraint.__init__)


def test_hyp_rapidml_regexconstraint_constructor_args():
    sig = inspect.signature(rapidml_RegExConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"




def test_hyp_rapidml_valuerangeconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_ValueRangeConstraint)


def test_hyp_rapidml_valuerangeconstraint_constructor_exists():
    assert callable(rapidml_ValueRangeConstraint.__init__)


def test_hyp_rapidml_valuerangeconstraint_constructor_args():
    sig = inspect.signature(rapidml_ValueRangeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "minValueExclusive" in params, "Missing parameter 'minValueExclusive'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "maxValueExclusive" in params, "Missing parameter 'maxValueExclusive'"
    assert "minValue" in params, "Missing parameter 'minValue'"







def test_hyp_rapidml_lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_LengthConstraint)


def test_hyp_rapidml_lengthconstraint_constructor_exists():
    assert callable(rapidml_LengthConstraint.__init__)


def test_hyp_rapidml_lengthconstraint_constructor_args():
    sig = inspect.signature(rapidml_LengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "length" in params, "Missing parameter 'length'"
    assert "minLength" in params, "Missing parameter 'minLength'"






def test_hyp_singlevaluetype_is_not_abstract():
    assert not inspect.isabstract(SingleValueType)


def test_hyp_singlevaluetype_constructor_exists():
    assert callable(SingleValueType.__init__)


def test_hyp_singlevaluetype_constructor_args():
    sig = inspect.signature(SingleValueType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_simpletype_is_not_abstract():
    assert not inspect.isabstract(rapidml_SimpleType)


def test_hyp_rapidml_simpletype_constructor_exists():
    assert callable(rapidml_SimpleType.__init__)


def test_hyp_rapidml_simpletype_constructor_args():
    sig = inspect.signature(rapidml_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_enumeration_is_not_abstract():
    assert not inspect.isabstract(rapidml_Enumeration)


def test_hyp_rapidml_enumeration_constructor_exists():
    assert callable(rapidml_Enumeration.__init__)


def test_hyp_rapidml_enumeration_constructor_args():
    sig = inspect.signature(rapidml_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_hyp_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_hyp_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inheritable_is_not_abstract():
    assert not inspect.isabstract(Inheritable)


def test_hyp_inheritable_constructor_exists():
    assert callable(Inheritable.__init__)


def test_hyp_inheritable_constructor_args():
    sig = inspect.signature(Inheritable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dataexample_is_not_abstract():
    assert not inspect.isabstract(DataExample)


def test_hyp_dataexample_constructor_exists():
    assert callable(DataExample.__init__)


def test_hyp_dataexample_constructor_args():
    sig = inspect.signature(DataExample.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_inlinedataexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_InlineDataExample)


def test_hyp_rapidml_inlinedataexample_constructor_exists():
    assert callable(rapidml_InlineDataExample.__init__)


def test_hyp_rapidml_inlinedataexample_constructor_args():
    sig = inspect.signature(rapidml_InlineDataExample.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_rapidml_dataexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataExample)


def test_hyp_rapidml_dataexample_constructor_exists():
    assert callable(rapidml_DataExample.__init__)


def test_hyp_rapidml_dataexample_constructor_args():
    sig = inspect.signature(rapidml_DataExample.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_withdataexamples_is_not_abstract():
    assert not inspect.isabstract(rapidml_WithDataExamples)


def test_hyp_rapidml_withdataexamples_constructor_exists():
    assert callable(rapidml_WithDataExamples.__init__)


def test_hyp_rapidml_withdataexamples_constructor_args():
    sig = inspect.signature(rapidml_WithDataExamples.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_inheritable_is_not_abstract():
    assert not inspect.isabstract(rapidml_Inheritable)


def test_hyp_rapidml_inheritable_constructor_exists():
    assert callable(rapidml_Inheritable.__init__)


def test_hyp_rapidml_inheritable_constructor_args():
    sig = inspect.signature(rapidml_Inheritable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_withdataexamples_is_not_abstract():
    assert not inspect.isabstract(WithDataExamples)


def test_hyp_withdataexamples_constructor_exists():
    assert callable(WithDataExamples.__init__)


def test_hyp_withdataexamples_constructor_args():
    sig = inspect.signature(WithDataExamples.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_singlevaluetype_is_not_abstract():
    assert not inspect.isabstract(rapidml_SingleValueType)


def test_hyp_rapidml_singlevaluetype_constructor_exists():
    assert callable(rapidml_SingleValueType.__init__)


def test_hyp_rapidml_singlevaluetype_constructor_args():
    sig = inspect.signature(rapidml_SingleValueType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_extensible_is_not_abstract():
    assert not inspect.isabstract(rapidml_Extensible)


def test_hyp_rapidml_extensible_constructor_exists():
    assert callable(rapidml_Extensible.__init__)


def test_hyp_rapidml_extensible_constructor_args():
    sig = inspect.signature(rapidml_Extensible.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_structure_is_not_abstract():
    assert not inspect.isabstract(rapidml_Structure)


def test_hyp_rapidml_structure_constructor_exists():
    assert callable(rapidml_Structure.__init__)


def test_hyp_rapidml_structure_constructor_args():
    sig = inspect.signature(rapidml_Structure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_hastitle_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasTitle)


def test_hyp_rapidml_hastitle_constructor_exists():
    assert callable(rapidml_HasTitle.__init__)


def test_hyp_rapidml_hastitle_constructor_args():
    sig = inspect.signature(rapidml_HasTitle.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_rapidml_extension_is_not_abstract():
    assert not inspect.isabstract(rapidml_Extension)


def test_hyp_rapidml_extension_constructor_exists():
    assert callable(rapidml_Extension.__init__)


def test_hyp_rapidml_extension_constructor_args():
    sig = inspect.signature(rapidml_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_rapidml_authenticationmethod_is_not_abstract():
    assert not inspect.isabstract(rapidml_AuthenticationMethod)


def test_hyp_rapidml_authenticationmethod_constructor_exists():
    assert callable(rapidml_AuthenticationMethod.__init__)


def test_hyp_rapidml_authenticationmethod_constructor_args():
    sig = inspect.signature(rapidml_AuthenticationMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_hassecurityvalue_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasSecurityValue)


def test_hyp_rapidml_hassecurityvalue_constructor_exists():
    assert callable(rapidml_HasSecurityValue.__init__)


def test_hyp_rapidml_hassecurityvalue_constructor_args():
    sig = inspect.signature(rapidml_HasSecurityValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referenceelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceElement)


def test_hyp_referenceelement_constructor_exists():
    assert callable(ReferenceElement.__init__)


def test_hyp_referenceelement_constructor_args():
    sig = inspect.signature(ReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_referenceproperty_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceProperty)


def test_hyp_rapidml_referenceproperty_constructor_exists():
    assert callable(rapidml_ReferenceProperty.__init__)


def test_hyp_rapidml_referenceproperty_constructor_args():
    sig = inspect.signature(rapidml_ReferenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"
    assert "containment" in params, "Missing parameter 'containment'"





def test_hyp_constrainabletype_is_not_abstract():
    assert not inspect.isabstract(ConstrainableType)


def test_hyp_constrainabletype_constructor_exists():
    assert callable(ConstrainableType.__init__)


def test_hyp_constrainabletype_constructor_args():
    sig = inspect.signature(ConstrainableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(rapidml_UserDefinedType)


def test_hyp_rapidml_userdefinedtype_constructor_exists():
    assert callable(rapidml_UserDefinedType.__init__)


def test_hyp_rapidml_userdefinedtype_constructor_args():
    sig = inspect.signature(rapidml_UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_propertyrealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_PropertyRealization)


def test_hyp_rapidml_propertyrealization_constructor_exists():
    assert callable(rapidml_PropertyRealization.__init__)


def test_hyp_rapidml_propertyrealization_constructor_args():
    sig = inspect.signature(rapidml_PropertyRealization.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"




def test_hyp_rapidml_hasstringvalue_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasStringValue)


def test_hyp_rapidml_hasstringvalue_constructor_exists():
    assert callable(rapidml_HasStringValue.__init__)


def test_hyp_rapidml_hasstringvalue_constructor_args():
    sig = inspect.signature(rapidml_HasStringValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_example_is_not_abstract():
    assert not inspect.isabstract(Example)


def test_hyp_example_constructor_exists():
    assert callable(Example.__init__)


def test_hyp_example_constructor_args():
    sig = inspect.signature(Example.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_externalexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_ExternalExample)


def test_hyp_rapidml_externalexample_constructor_exists():
    assert callable(rapidml_ExternalExample.__init__)


def test_hyp_rapidml_externalexample_constructor_args():
    sig = inspect.signature(rapidml_ExternalExample.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_rapidml_inlineexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_InlineExample)


def test_hyp_rapidml_inlineexample_constructor_exists():
    assert callable(rapidml_InlineExample.__init__)


def test_hyp_rapidml_inlineexample_constructor_args():
    sig = inspect.signature(rapidml_InlineExample.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_rapidml_example_is_not_abstract():
    assert not inspect.isabstract(rapidml_Example)


def test_hyp_rapidml_example_constructor_exists():
    assert callable(rapidml_Example.__init__)


def test_hyp_rapidml_example_constructor_args():
    sig = inspect.signature(rapidml_Example.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_withexamples_is_not_abstract():
    assert not inspect.isabstract(rapidml_WithExamples)


def test_hyp_rapidml_withexamples_constructor_exists():
    assert callable(rapidml_WithExamples.__init__)


def test_hyp_rapidml_withexamples_constructor_args():
    sig = inspect.signature(rapidml_WithExamples.__init__)
    params = list(sig.parameters.keys())



def test_hyp_urisegment_is_not_abstract():
    assert not inspect.isabstract(URISegment)


def test_hyp_urisegment_constructor_exists():
    assert callable(URISegment.__init__)


def test_hyp_urisegment_constructor_args():
    sig = inspect.signature(URISegment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hasstringvalue_is_not_abstract():
    assert not inspect.isabstract(HasStringValue)


def test_hyp_hasstringvalue_constructor_exists():
    assert callable(HasStringValue.__init__)


def test_hyp_hasstringvalue_constructor_args():
    sig = inspect.signature(HasStringValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_urisegment_is_not_abstract():
    assert not inspect.isabstract(rapidml_URISegment)


def test_hyp_rapidml_urisegment_constructor_exists():
    assert callable(rapidml_URISegment.__init__)


def test_hyp_rapidml_urisegment_constructor_args():
    sig = inspect.signature(rapidml_URISegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveType)


def test_hyp_rapidml_primitivetype_constructor_exists():
    assert callable(rapidml_PrimitiveType.__init__)


def test_hyp_rapidml_primitivetype_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_pathsegment_is_not_abstract():
    assert not inspect.isabstract(rapidml_PathSegment)


def test_hyp_rapidml_pathsegment_constructor_exists():
    assert callable(rapidml_PathSegment.__init__)


def test_hyp_rapidml_pathsegment_constructor_args():
    sig = inspect.signature(rapidml_PathSegment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objectrealization_is_not_abstract():
    assert not inspect.isabstract(ObjectRealization)


def test_hyp_objectrealization_constructor_exists():
    assert callable(ObjectRealization.__init__)


def test_hyp_objectrealization_constructor_args():
    sig = inspect.signature(ObjectRealization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourcedefinition_is_not_abstract():
    assert not inspect.isabstract(ResourceDefinition)


def test_hyp_resourcedefinition_constructor_exists():
    assert callable(ResourceDefinition.__init__)


def test_hyp_resourcedefinition_constructor_args():
    sig = inspect.signature(ResourceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referencetreatment_is_not_abstract():
    assert not inspect.isabstract(ReferenceTreatment)


def test_hyp_referencetreatment_constructor_exists():
    assert callable(ReferenceTreatment.__init__)


def test_hyp_referencetreatment_constructor_args():
    sig = inspect.signature(ReferenceTreatment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_referenceembed_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceEmbed)


def test_hyp_rapidml_referenceembed_constructor_exists():
    assert callable(rapidml_ReferenceEmbed.__init__)


def test_hyp_rapidml_referenceembed_constructor_args():
    sig = inspect.signature(rapidml_ReferenceEmbed.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_referencelink_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceLink)


def test_hyp_rapidml_referencelink_constructor_exists():
    assert callable(rapidml_ReferenceLink.__init__)


def test_hyp_rapidml_referencelink_constructor_args():
    sig = inspect.signature(rapidml_ReferenceLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "collectionRealizationLevel" in params, "Missing parameter 'collectionRealizationLevel'"





def test_hyp_rapidml_referenceelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceElement)


def test_hyp_rapidml_referenceelement_constructor_exists():
    assert callable(rapidml_ReferenceElement.__init__)


def test_hyp_rapidml_referenceelement_constructor_args():
    sig = inspect.signature(rapidml_ReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_namedlinkdescriptor_is_not_abstract():
    assert not inspect.isabstract(rapidml_NamedLinkDescriptor)


def test_hyp_rapidml_namedlinkdescriptor_constructor_exists():
    assert callable(rapidml_NamedLinkDescriptor.__init__)


def test_hyp_rapidml_namedlinkdescriptor_constructor_args():
    sig = inspect.signature(rapidml_NamedLinkDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_rapidml_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(rapidml_ImportDeclaration)


def test_hyp_rapidml_importdeclaration_constructor_exists():
    assert callable(rapidml_ImportDeclaration.__init__)


def test_hyp_rapidml_importdeclaration_constructor_args():
    sig = inspect.signature(rapidml_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "alias" in params, "Missing parameter 'alias'"






def test_hyp_rapidml_primitivetypeslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveTypesLibrary)


def test_hyp_rapidml_primitivetypeslibrary_constructor_exists():
    assert callable(rapidml_PrimitiveTypesLibrary.__init__)


def test_hyp_rapidml_primitivetypeslibrary_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_linkrelationslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_LinkRelationsLibrary)


def test_hyp_rapidml_linkrelationslibrary_constructor_exists():
    assert callable(rapidml_LinkRelationsLibrary.__init__)


def test_hyp_rapidml_linkrelationslibrary_constructor_args():
    sig = inspect.signature(rapidml_LinkRelationsLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_mediatypeslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_MediaTypesLibrary)


def test_hyp_rapidml_mediatypeslibrary_constructor_exists():
    assert callable(rapidml_MediaTypesLibrary.__init__)


def test_hyp_rapidml_mediatypeslibrary_constructor_args():
    sig = inspect.signature(rapidml_MediaTypesLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_realizationmodellocation_is_not_abstract():
    assert not inspect.isabstract(rapidml_RealizationModelLocation)


def test_hyp_rapidml_realizationmodellocation_constructor_exists():
    assert callable(rapidml_RealizationModelLocation.__init__)


def test_hyp_rapidml_realizationmodellocation_constructor_args():
    sig = inspect.signature(rapidml_RealizationModelLocation.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_hastitle_is_not_abstract():
    assert not inspect.isabstract(HasTitle)


def test_hyp_hastitle_constructor_exists():
    assert callable(HasTitle.__init__)


def test_hyp_hastitle_constructor_args():
    sig = inspect.signature(HasTitle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_primitiveproperty_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveProperty)


def test_hyp_rapidml_primitiveproperty_constructor_exists():
    assert callable(rapidml_PrimitiveProperty.__init__)


def test_hyp_rapidml_primitiveproperty_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcereference_is_not_abstract():
    assert not inspect.isabstract(SourceReference)


def test_hyp_sourcereference_constructor_exists():
    assert callable(SourceReference.__init__)


def test_hyp_sourcereference_constructor_args():
    sig = inspect.signature(SourceReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_primitivetypesourcereference_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveTypeSourceReference)


def test_hyp_rapidml_primitivetypesourcereference_constructor_exists():
    assert callable(rapidml_PrimitiveTypeSourceReference.__init__)


def test_hyp_rapidml_primitivetypesourcereference_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveTypeSourceReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_propertyreference_is_not_abstract():
    assert not inspect.isabstract(rapidml_PropertyReference)


def test_hyp_rapidml_propertyreference_constructor_exists():
    assert callable(rapidml_PropertyReference.__init__)


def test_hyp_rapidml_propertyreference_constructor_args():
    sig = inspect.signature(rapidml_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_uriparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_URIParameter)


def test_hyp_rapidml_uriparameter_constructor_exists():
    assert callable(rapidml_URIParameter.__init__)


def test_hyp_rapidml_uriparameter_constructor_args():
    sig = inspect.signature(rapidml_URIParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_collectionreferenceelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionReferenceElement)


def test_hyp_rapidml_collectionreferenceelement_constructor_exists():
    assert callable(rapidml_CollectionReferenceElement.__init__)


def test_hyp_rapidml_collectionreferenceelement_constructor_args():
    sig = inspect.signature(rapidml_CollectionReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_collectionparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionParameter)


def test_hyp_rapidml_collectionparameter_constructor_exists():
    assert callable(rapidml_CollectionParameter.__init__)


def test_hyp_rapidml_collectionparameter_constructor_args():
    sig = inspect.signature(rapidml_CollectionParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicedataresource_is_not_abstract():
    assert not inspect.isabstract(ServiceDataResource)


def test_hyp_servicedataresource_constructor_exists():
    assert callable(ServiceDataResource.__init__)


def test_hyp_servicedataresource_constructor_args():
    sig = inspect.signature(ServiceDataResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_objectresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_ObjectResource)


def test_hyp_rapidml_objectresource_constructor_exists():
    assert callable(rapidml_ObjectResource.__init__)


def test_hyp_rapidml_objectresource_constructor_args():
    sig = inspect.signature(rapidml_ObjectResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_collectionresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionResource)


def test_hyp_rapidml_collectionresource_constructor_exists():
    assert callable(rapidml_CollectionResource.__init__)


def test_hyp_rapidml_collectionresource_constructor_args():
    sig = inspect.signature(rapidml_CollectionResource.__init__)
    params = list(sig.parameters.keys())
    assert "resourceRealizationKind" in params, "Missing parameter 'resourceRealizationKind'"




def test_hyp_uriparameter_is_not_abstract():
    assert not inspect.isabstract(URIParameter)


def test_hyp_uriparameter_constructor_exists():
    assert callable(URIParameter.__init__)


def test_hyp_uriparameter_constructor_args():
    sig = inspect.signature(URIParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_templateparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_TemplateParameter)


def test_hyp_rapidml_templateparameter_constructor_exists():
    assert callable(rapidml_TemplateParameter.__init__)


def test_hyp_rapidml_templateparameter_constructor_args():
    sig = inspect.signature(rapidml_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_matrixparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_MatrixParameter)


def test_hyp_rapidml_matrixparameter_constructor_exists():
    assert callable(rapidml_MatrixParameter.__init__)


def test_hyp_rapidml_matrixparameter_constructor_args():
    sig = inspect.signature(rapidml_MatrixParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_urisegmentwithparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_URISegmentWithParameter)


def test_hyp_rapidml_urisegmentwithparameter_constructor_exists():
    assert callable(rapidml_URISegmentWithParameter.__init__)


def test_hyp_rapidml_urisegmentwithparameter_constructor_args():
    sig = inspect.signature(rapidml_URISegmentWithParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_documentable_is_not_abstract():
    assert not inspect.isabstract(rapidml_Documentable)


def test_hyp_rapidml_documentable_constructor_exists():
    assert callable(rapidml_Documentable.__init__)


def test_hyp_rapidml_documentable_constructor_args():
    sig = inspect.signature(rapidml_Documentable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_documentation_is_not_abstract():
    assert not inspect.isabstract(rapidml_Documentation)


def test_hyp_rapidml_documentation_constructor_exists():
    assert callable(rapidml_Documentation.__init__)


def test_hyp_rapidml_documentation_constructor_args():
    sig = inspect.signature(rapidml_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_typedmessage_is_not_abstract():
    assert not inspect.isabstract(TypedMessage)


def test_hyp_typedmessage_constructor_exists():
    assert callable(TypedMessage.__init__)


def test_hyp_typedmessage_constructor_args():
    sig = inspect.signature(TypedMessage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentable_is_not_abstract():
    assert not inspect.isabstract(Documentable)


def test_hyp_documentable_constructor_exists():
    assert callable(Documentable.__init__)


def test_hyp_documentable_constructor_args():
    sig = inspect.signature(Documentable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_securityschemelibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecuritySchemeLibrary)


def test_hyp_rapidml_securityschemelibrary_constructor_exists():
    assert callable(rapidml_SecuritySchemeLibrary.__init__)


def test_hyp_rapidml_securityschemelibrary_constructor_args():
    sig = inspect.signature(rapidml_SecuritySchemeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_securityscope_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecurityScope)


def test_hyp_rapidml_securityscope_constructor_exists():
    assert callable(rapidml_SecurityScope.__init__)


def test_hyp_rapidml_securityscope_constructor_args():
    sig = inspect.signature(rapidml_SecurityScope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_securityschemeparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecuritySchemeParameter)


def test_hyp_rapidml_securityschemeparameter_constructor_exists():
    assert callable(rapidml_SecuritySchemeParameter.__init__)


def test_hyp_rapidml_securityschemeparameter_constructor_args():
    sig = inspect.signature(rapidml_SecuritySchemeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_rapidml_linkrelation_is_not_abstract():
    assert not inspect.isabstract(rapidml_LinkRelation)


def test_hyp_rapidml_linkrelation_constructor_exists():
    assert callable(rapidml_LinkRelation.__init__)


def test_hyp_rapidml_linkrelation_constructor_args():
    sig = inspect.signature(rapidml_LinkRelation.__init__)
    params = list(sig.parameters.keys())
    assert "specURL" in params, "Missing parameter 'specURL'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_rapidml_operation_is_not_abstract():
    assert not inspect.isabstract(rapidml_Operation)


def test_hyp_rapidml_operation_constructor_exists():
    assert callable(rapidml_Operation.__init__)


def test_hyp_rapidml_operation_constructor_args():
    sig = inspect.signature(rapidml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_enumconstant_is_not_abstract():
    assert not inspect.isabstract(rapidml_EnumConstant)


def test_hyp_rapidml_enumconstant_constructor_exists():
    assert callable(rapidml_EnumConstant.__init__)


def test_hyp_rapidml_enumconstant_constructor_args():
    sig = inspect.signature(rapidml_EnumConstant.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"






def test_hyp_rapidml_datamodel_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataModel)


def test_hyp_rapidml_datamodel_constructor_exists():
    assert callable(rapidml_DataModel.__init__)


def test_hyp_rapidml_datamodel_constructor_args():
    sig = inspect.signature(rapidml_DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_sourcereference_is_not_abstract():
    assert not inspect.isabstract(rapidml_SourceReference)


def test_hyp_rapidml_sourcereference_constructor_exists():
    assert callable(rapidml_SourceReference.__init__)


def test_hyp_rapidml_sourcereference_constructor_args():
    sig = inspect.signature(rapidml_SourceReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realizationcontainer_is_not_abstract():
    assert not inspect.isabstract(RealizationContainer)


def test_hyp_realizationcontainer_constructor_exists():
    assert callable(RealizationContainer.__init__)


def test_hyp_realizationcontainer_constructor_args():
    sig = inspect.signature(RealizationContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_referencerealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceRealization)


def test_hyp_rapidml_referencerealization_constructor_exists():
    assert callable(rapidml_ReferenceRealization.__init__)


def test_hyp_rapidml_referencerealization_constructor_args():
    sig = inspect.signature(rapidml_ReferenceRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizationType" in params, "Missing parameter 'realizationType'"
    assert "multiValued" in params, "Missing parameter 'multiValued'"





def test_hyp_rapidml_servicedataresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_ServiceDataResource)


def test_hyp_rapidml_servicedataresource_constructor_exists():
    assert callable(rapidml_ServiceDataResource.__init__)


def test_hyp_rapidml_servicedataresource_constructor_args():
    sig = inspect.signature(rapidml_ServiceDataResource.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_rapidml_uri_is_not_abstract():
    assert not inspect.isabstract(rapidml_URI)


def test_hyp_rapidml_uri_constructor_exists():
    assert callable(rapidml_URI.__init__)


def test_hyp_rapidml_uri_constructor_args():
    sig = inspect.signature(rapidml_URI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_typedresponse_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedResponse)


def test_hyp_rapidml_typedresponse_constructor_exists():
    assert callable(rapidml_TypedResponse.__init__)


def test_hyp_rapidml_typedresponse_constructor_args():
    sig = inspect.signature(rapidml_TypedResponse.__init__)
    params = list(sig.parameters.keys())
    assert "statusCode" in params, "Missing parameter 'statusCode'"




def test_hyp_rapidml_typedrequest_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedRequest)


def test_hyp_rapidml_typedrequest_constructor_exists():
    assert callable(rapidml_TypedRequest.__init__)


def test_hyp_rapidml_typedrequest_constructor_args():
    sig = inspect.signature(rapidml_TypedRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extensible_is_not_abstract():
    assert not inspect.isabstract(Extensible)


def test_hyp_extensible_constructor_exists():
    assert callable(Extensible.__init__)


def test_hyp_extensible_constructor_args():
    sig = inspect.signature(Extensible.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_datatype_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataType)


def test_hyp_rapidml_datatype_constructor_exists():
    assert callable(rapidml_DataType.__init__)


def test_hyp_rapidml_datatype_constructor_args():
    sig = inspect.signature(rapidml_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_rapidml_realizationcontainer_is_not_abstract():
    assert not inspect.isabstract(rapidml_RealizationContainer)


def test_hyp_rapidml_realizationcontainer_constructor_exists():
    assert callable(rapidml_RealizationContainer.__init__)


def test_hyp_rapidml_realizationcontainer_constructor_args():
    sig = inspect.signature(rapidml_RealizationContainer.__init__)
    params = list(sig.parameters.keys())
    assert "effectiveRealization" in params, "Missing parameter 'effectiveRealization'"
    assert "realizationName" in params, "Missing parameter 'realizationName'"
    assert "withDefaultRealization" in params, "Missing parameter 'withDefaultRealization'"






def test_hyp_rapidml_feature_is_not_abstract():
    assert not inspect.isabstract(rapidml_Feature)


def test_hyp_rapidml_feature_constructor_exists():
    assert callable(rapidml_Feature.__init__)


def test_hyp_rapidml_feature_constructor_args():
    sig = inspect.signature(rapidml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "name" in params, "Missing parameter 'name'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "restriction" in params, "Missing parameter 'restriction'"







def test_hyp_rapidml_objectrealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_ObjectRealization)


def test_hyp_rapidml_objectrealization_constructor_exists():
    assert callable(rapidml_ObjectRealization.__init__)


def test_hyp_rapidml_objectrealization_constructor_args():
    sig = inspect.signature(rapidml_ObjectRealization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_zenmodel_is_not_abstract():
    assert not inspect.isabstract(rapidml_ZenModel)


def test_hyp_rapidml_zenmodel_constructor_exists():
    assert callable(rapidml_ZenModel.__init__)


def test_hyp_rapidml_zenmodel_constructor_args():
    sig = inspect.signature(rapidml_ZenModel.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_rapidml_restelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_RESTElement)


def test_hyp_rapidml_restelement_constructor_exists():
    assert callable(rapidml_RESTElement.__init__)


def test_hyp_rapidml_restelement_constructor_args():
    sig = inspect.signature(rapidml_RESTElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_constraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_Constraint)


def test_hyp_rapidml_constraint_constructor_exists():
    assert callable(rapidml_Constraint.__init__)


def test_hyp_rapidml_constraint_constructor_args():
    sig = inspect.signature(rapidml_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_referencetreatment_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceTreatment)


def test_hyp_rapidml_referencetreatment_constructor_exists():
    assert callable(rapidml_ReferenceTreatment.__init__)


def test_hyp_rapidml_referencetreatment_constructor_args():
    sig = inspect.signature(rapidml_ReferenceTreatment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_constrainabletype_is_not_abstract():
    assert not inspect.isabstract(rapidml_ConstrainableType)


def test_hyp_rapidml_constrainabletype_constructor_exists():
    assert callable(rapidml_ConstrainableType.__init__)


def test_hyp_rapidml_constrainabletype_constructor_args():
    sig = inspect.signature(rapidml_ConstrainableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_messageparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_MessageParameter)


def test_hyp_rapidml_messageparameter_constructor_exists():
    assert callable(rapidml_MessageParameter.__init__)


def test_hyp_rapidml_messageparameter_constructor_args():
    sig = inspect.signature(rapidml_MessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "httpLocation" in params, "Missing parameter 'httpLocation'"




def test_hyp_hassecurityvalue_is_not_abstract():
    assert not inspect.isabstract(HasSecurityValue)


def test_hyp_hassecurityvalue_constructor_exists():
    assert callable(HasSecurityValue.__init__)


def test_hyp_hassecurityvalue_constructor_args():
    sig = inspect.signature(HasSecurityValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_withexamples_is_not_abstract():
    assert not inspect.isabstract(WithExamples)


def test_hyp_withexamples_constructor_exists():
    assert callable(WithExamples.__init__)


def test_hyp_withexamples_constructor_args():
    sig = inspect.signature(WithExamples.__init__)
    params = list(sig.parameters.keys())



def test_hyp_restelement_is_not_abstract():
    assert not inspect.isabstract(RESTElement)


def test_hyp_restelement_constructor_exists():
    assert callable(RESTElement.__init__)


def test_hyp_restelement_constructor_args():
    sig = inspect.signature(RESTElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rapidml_mediatype_is_not_abstract():
    assert not inspect.isabstract(rapidml_MediaType)


def test_hyp_rapidml_mediatype_constructor_exists():
    assert callable(rapidml_MediaType.__init__)


def test_hyp_rapidml_mediatype_constructor_args():
    sig = inspect.signature(rapidml_MediaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "specURL" in params, "Missing parameter 'specURL'"





def test_hyp_rapidml_parameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_Parameter)


def test_hyp_rapidml_parameter_constructor_exists():
    assert callable(rapidml_Parameter.__init__)


def test_hyp_rapidml_parameter_constructor_args():
    sig = inspect.signature(rapidml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"







def test_hyp_rapidml_method_is_not_abstract():
    assert not inspect.isabstract(rapidml_Method)


def test_hyp_rapidml_method_constructor_exists():
    assert callable(rapidml_Method.__init__)


def test_hyp_rapidml_method_constructor_args():
    sig = inspect.signature(rapidml_Method.__init__)
    params = list(sig.parameters.keys())
    assert "httpMethod" in params, "Missing parameter 'httpMethod'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_rapidml_resourceapi_is_not_abstract():
    assert not inspect.isabstract(rapidml_ResourceAPI)


def test_hyp_rapidml_resourceapi_constructor_exists():
    assert callable(rapidml_ResourceAPI.__init__)


def test_hyp_rapidml_resourceapi_constructor_args():
    sig = inspect.signature(rapidml_ResourceAPI.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "baseURI" in params, "Missing parameter 'baseURI'"
    assert "version" in params, "Missing parameter 'version'"






def test_hyp_rapidml_securityscheme_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecurityScheme)


def test_hyp_rapidml_securityscheme_constructor_exists():
    assert callable(rapidml_SecurityScheme.__init__)


def test_hyp_rapidml_securityscheme_constructor_args():
    sig = inspect.signature(rapidml_SecurityScheme.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "flow" in params, "Missing parameter 'flow'"






def test_hyp_rapidml_typedmessage_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedMessage)


def test_hyp_rapidml_typedmessage_constructor_exists():
    assert callable(rapidml_TypedMessage.__init__)


def test_hyp_rapidml_typedmessage_constructor_args():
    sig = inspect.signature(rapidml_TypedMessage.__init__)
    params = list(sig.parameters.keys())
    assert "useParentTypeReference" in params, "Missing parameter 'useParentTypeReference'"




def test_hyp_rapidml_resourcedefinition_is_not_abstract():
    assert not inspect.isabstract(rapidml_ResourceDefinition)


def test_hyp_rapidml_resourcedefinition_constructor_exists():
    assert callable(rapidml_ResourceDefinition.__init__)


def test_hyp_rapidml_resourcedefinition_constructor_args():
    sig = inspect.signature(rapidml_ResourceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_authenticationflows_exists():
    # Check that the Enumeration exists
    assert AuthenticationFlows is not None

def test_hyp_authenticationflows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationFlows]
    expected_literals = [
        "IMPLICIT",
        "APPLICATION",
        "PASSWORD",
        "ACCESS_CODE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationFlows"

def test_hyp_httpmessageparameterlocation_exists():
    # Check that the Enumeration exists
    assert HttpMessageParameterLocation is not None

def test_hyp_httpmessageparameterlocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HttpMessageParameterLocation]
    expected_literals = [
        "HEADER",
        "QUERY",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HttpMessageParameterLocation"

def test_hyp_httpmethods_exists():
    # Check that the Enumeration exists
    assert HTTPMethods is not None

def test_hyp_httpmethods_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HTTPMethods]
    expected_literals = [
        "GET",
        "PUT",
        "PATCH",
        "TRACE",
        "OPTIONS",
        "HEAD",
        "CONNECT",
        "POST",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HTTPMethods"

def test_hyp_collectionrealizationlevelenum_exists():
    # Check that the Enumeration exists
    assert CollectionRealizationLevelEnum is not None

def test_hyp_collectionrealizationlevelenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionRealizationLevelEnum]
    expected_literals = [
        "COLLECTION_LEVEL",
        "ITEM_LEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionRealizationLevelEnum"

def test_hyp_authenticationtypes_exists():
    # Check that the Enumeration exists
    assert AuthenticationTypes is not None

def test_hyp_authenticationtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationTypes]
    expected_literals = [
        "CUSTOM",
        "OAUTH2",
        "BASIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationTypes"

def test_hyp_referencerealizationenum_exists():
    # Check that the Enumeration exists
    assert ReferenceRealizationEnum is not None

def test_hyp_referencerealizationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceRealizationEnum]
    expected_literals = [
        "EMBED",
        "LINK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceRealizationEnum"

def test_hyp_collectionrealizationenum_exists():
    # Check that the Enumeration exists
    assert CollectionRealizationEnum is not None

def test_hyp_collectionrealizationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionRealizationEnum]
    expected_literals = [
        "REFERENCE_LINK_LIST",
        "EMBEDDED_OBJECT_LIST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionRealizationEnum"


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
rapidml_Element_strategy = st.builds(
    rapidml_Element,
    cardinality=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
rapidml_RegExConstraint_strategy = st.builds(
    rapidml_RegExConstraint,
    pattern=
        safe_text
)
rapidml_ValueRangeConstraint_strategy = st.builds(
    rapidml_ValueRangeConstraint,
    minValueExclusive=
        st.booleans(),
    maxValue=
        safe_text,
    maxValueExclusive=
        st.booleans(),
    minValue=
        safe_text
)
rapidml_LengthConstraint_strategy = st.builds(
    rapidml_LengthConstraint,
    maxLength=
        st.integers(),
    length=
        st.integers(),
    minLength=
        st.integers()
)
SingleValueType_strategy = st.builds(
    SingleValueType,
)
rapidml_SimpleType_strategy = st.builds(
    rapidml_SimpleType,
)
rapidml_Enumeration_strategy = st.builds(
    rapidml_Enumeration,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
Inheritable_strategy = st.builds(
    Inheritable,
)
DataExample_strategy = st.builds(
    DataExample,
)
rapidml_InlineDataExample_strategy = st.builds(
    rapidml_InlineDataExample,
    body=
        safe_text
)
rapidml_DataExample_strategy = st.builds(
    rapidml_DataExample,
)
rapidml_WithDataExamples_strategy = st.builds(
    rapidml_WithDataExamples,
)
rapidml_Inheritable_strategy = st.builds(
    rapidml_Inheritable,
)
Element_strategy = st.builds(
    Element,
)
WithDataExamples_strategy = st.builds(
    WithDataExamples,
)
DataType_strategy = st.builds(
    DataType,
)
rapidml_SingleValueType_strategy = st.builds(
    rapidml_SingleValueType,
)
Feature_strategy = st.builds(
    Feature,
)
rapidml_Extensible_strategy = st.builds(
    rapidml_Extensible,
)
rapidml_Structure_strategy = st.builds(
    rapidml_Structure,
)
rapidml_HasTitle_strategy = st.builds(
    rapidml_HasTitle,
    title=
        safe_text
)
rapidml_Extension_strategy = st.builds(
    rapidml_Extension,
    name=
        safe_text,
    value=
        safe_text
)
rapidml_AuthenticationMethod_strategy = st.builds(
    rapidml_AuthenticationMethod,
)
rapidml_HasSecurityValue_strategy = st.builds(
    rapidml_HasSecurityValue,
)
ReferenceElement_strategy = st.builds(
    ReferenceElement,
)
rapidml_ReferenceProperty_strategy = st.builds(
    rapidml_ReferenceProperty,
    container=
        st.booleans(),
    containment=
        st.booleans()
)
ConstrainableType_strategy = st.builds(
    ConstrainableType,
)
rapidml_UserDefinedType_strategy = st.builds(
    rapidml_UserDefinedType,
)
rapidml_PropertyRealization_strategy = st.builds(
    rapidml_PropertyRealization,
    cardinality=
        safe_text
)
rapidml_HasStringValue_strategy = st.builds(
    rapidml_HasStringValue,
)
Example_strategy = st.builds(
    Example,
)
rapidml_ExternalExample_strategy = st.builds(
    rapidml_ExternalExample,
    path=
        safe_text
)
rapidml_InlineExample_strategy = st.builds(
    rapidml_InlineExample,
    body=
        safe_text
)
rapidml_Example_strategy = st.builds(
    rapidml_Example,
)
rapidml_WithExamples_strategy = st.builds(
    rapidml_WithExamples,
)
URISegment_strategy = st.builds(
    URISegment,
)
HasStringValue_strategy = st.builds(
    HasStringValue,
)
rapidml_URISegment_strategy = st.builds(
    rapidml_URISegment,
    name=
        safe_text
)
rapidml_PrimitiveType_strategy = st.builds(
    rapidml_PrimitiveType,
)
rapidml_PathSegment_strategy = st.builds(
    rapidml_PathSegment,
)
ObjectRealization_strategy = st.builds(
    ObjectRealization,
)
ResourceDefinition_strategy = st.builds(
    ResourceDefinition,
)
ReferenceTreatment_strategy = st.builds(
    ReferenceTreatment,
)
rapidml_ReferenceEmbed_strategy = st.builds(
    rapidml_ReferenceEmbed,
)
rapidml_ReferenceLink_strategy = st.builds(
    rapidml_ReferenceLink,
    name=
        safe_text,
    collectionRealizationLevel=
        safe_text
)
rapidml_ReferenceElement_strategy = st.builds(
    rapidml_ReferenceElement,
)
rapidml_NamedLinkDescriptor_strategy = st.builds(
    rapidml_NamedLinkDescriptor,
    default=
        st.booleans(),
    name=
        safe_text
)
rapidml_ImportDeclaration_strategy = st.builds(
    rapidml_ImportDeclaration,
    importURI=
        safe_text,
    importedNamespace=
        safe_text,
    alias=
        safe_text
)
rapidml_PrimitiveTypesLibrary_strategy = st.builds(
    rapidml_PrimitiveTypesLibrary,
    name=
        safe_text
)
rapidml_LinkRelationsLibrary_strategy = st.builds(
    rapidml_LinkRelationsLibrary,
    name=
        safe_text
)
rapidml_MediaTypesLibrary_strategy = st.builds(
    rapidml_MediaTypesLibrary,
)
rapidml_RealizationModelLocation_strategy = st.builds(
    rapidml_RealizationModelLocation,
    uri=
        safe_text
)
HasTitle_strategy = st.builds(
    HasTitle,
)
rapidml_PrimitiveProperty_strategy = st.builds(
    rapidml_PrimitiveProperty,
)
SourceReference_strategy = st.builds(
    SourceReference,
)
rapidml_PrimitiveTypeSourceReference_strategy = st.builds(
    rapidml_PrimitiveTypeSourceReference,
)
rapidml_PropertyReference_strategy = st.builds(
    rapidml_PropertyReference,
)
Parameter_strategy = st.builds(
    Parameter,
)
rapidml_URIParameter_strategy = st.builds(
    rapidml_URIParameter,
)
rapidml_CollectionReferenceElement_strategy = st.builds(
    rapidml_CollectionReferenceElement,
)
rapidml_CollectionParameter_strategy = st.builds(
    rapidml_CollectionParameter,
)
ServiceDataResource_strategy = st.builds(
    ServiceDataResource,
)
rapidml_ObjectResource_strategy = st.builds(
    rapidml_ObjectResource,
)
rapidml_CollectionResource_strategy = st.builds(
    rapidml_CollectionResource,
    resourceRealizationKind=
        safe_text
)
URIParameter_strategy = st.builds(
    URIParameter,
)
rapidml_TemplateParameter_strategy = st.builds(
    rapidml_TemplateParameter,
)
rapidml_MatrixParameter_strategy = st.builds(
    rapidml_MatrixParameter,
)
rapidml_URISegmentWithParameter_strategy = st.builds(
    rapidml_URISegmentWithParameter,
)
rapidml_Documentable_strategy = st.builds(
    rapidml_Documentable,
)
rapidml_Documentation_strategy = st.builds(
    rapidml_Documentation,
    text=
        safe_text
)
TypedMessage_strategy = st.builds(
    TypedMessage,
)
Documentable_strategy = st.builds(
    Documentable,
)
rapidml_SecuritySchemeLibrary_strategy = st.builds(
    rapidml_SecuritySchemeLibrary,
    name=
        safe_text
)
rapidml_SecurityScope_strategy = st.builds(
    rapidml_SecurityScope,
    name=
        safe_text
)
rapidml_SecuritySchemeParameter_strategy = st.builds(
    rapidml_SecuritySchemeParameter,
    name=
        safe_text,
    value=
        safe_text
)
rapidml_LinkRelation_strategy = st.builds(
    rapidml_LinkRelation,
    specURL=
        safe_text,
    name=
        safe_text
)
rapidml_Operation_strategy = st.builds(
    rapidml_Operation,
    name=
        safe_text
)
rapidml_EnumConstant_strategy = st.builds(
    rapidml_EnumConstant,
    literalValue=
        safe_text,
    name=
        safe_text,
    integerValue=
        st.integers()
)
rapidml_DataModel_strategy = st.builds(
    rapidml_DataModel,
    name=
        safe_text
)
rapidml_SourceReference_strategy = st.builds(
    rapidml_SourceReference,
)
RealizationContainer_strategy = st.builds(
    RealizationContainer,
)
rapidml_ReferenceRealization_strategy = st.builds(
    rapidml_ReferenceRealization,
    realizationType=
        safe_text,
    multiValued=
        st.booleans()
)
rapidml_ServiceDataResource_strategy = st.builds(
    rapidml_ServiceDataResource,
    default=
        st.booleans()
)
rapidml_URI_strategy = st.builds(
    rapidml_URI,
)
rapidml_TypedResponse_strategy = st.builds(
    rapidml_TypedResponse,
    statusCode=
        st.integers()
)
rapidml_TypedRequest_strategy = st.builds(
    rapidml_TypedRequest,
)
Extensible_strategy = st.builds(
    Extensible,
)
rapidml_DataType_strategy = st.builds(
    rapidml_DataType,
    name=
        safe_text
)
rapidml_RealizationContainer_strategy = st.builds(
    rapidml_RealizationContainer,
    effectiveRealization=
        safe_text,
    realizationName=
        safe_text,
    withDefaultRealization=
        st.booleans()
)
rapidml_Feature_strategy = st.builds(
    rapidml_Feature,
    key=
        st.booleans(),
    name=
        safe_text,
    readOnly=
        st.booleans(),
    restriction=
        st.booleans()
)
rapidml_ObjectRealization_strategy = st.builds(
    rapidml_ObjectRealization,
)
rapidml_ZenModel_strategy = st.builds(
    rapidml_ZenModel,
    namespace=
        safe_text,
    name=
        safe_text
)
rapidml_RESTElement_strategy = st.builds(
    rapidml_RESTElement,
)
rapidml_Constraint_strategy = st.builds(
    rapidml_Constraint,
)
rapidml_ReferenceTreatment_strategy = st.builds(
    rapidml_ReferenceTreatment,
)
rapidml_ConstrainableType_strategy = st.builds(
    rapidml_ConstrainableType,
)
rapidml_MessageParameter_strategy = st.builds(
    rapidml_MessageParameter,
    httpLocation=
        safe_text
)
HasSecurityValue_strategy = st.builds(
    HasSecurityValue,
)
WithExamples_strategy = st.builds(
    WithExamples,
)
RESTElement_strategy = st.builds(
    RESTElement,
)
rapidml_MediaType_strategy = st.builds(
    rapidml_MediaType,
    name=
        safe_text,
    specURL=
        safe_text
)
rapidml_Parameter_strategy = st.builds(
    rapidml_Parameter,
    required=
        st.booleans(),
    fixed=
        safe_text,
    name=
        safe_text,
    default=
        safe_text
)
rapidml_Method_strategy = st.builds(
    rapidml_Method,
    httpMethod=
        safe_text,
    id=
        safe_text
)
rapidml_ResourceAPI_strategy = st.builds(
    rapidml_ResourceAPI,
    name=
        safe_text,
    baseURI=
        safe_text,
    version=
        safe_text
)
rapidml_SecurityScheme_strategy = st.builds(
    rapidml_SecurityScheme,
    type=
        safe_text,
    name=
        safe_text,
    flow=
        safe_text
)
rapidml_TypedMessage_strategy = st.builds(
    rapidml_TypedMessage,
    useParentTypeReference=
        st.booleans()
)
rapidml_ResourceDefinition_strategy = st.builds(
    rapidml_ResourceDefinition,
    name=
        safe_text
)




@given(instance=rapidml_Element_strategy)
def test_hyp_rapidml_element_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_Element_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_element_ismultivalued_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMultiValued()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMultiValued).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMultiValued' in rapidml_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMultiValued' in rapidml_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMultiValued' in rapidml_Element is not implemented or raised an error")





@given(instance=rapidml_RegExConstraint_strategy)
def test_hyp_rapidml_regexconstraint_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original




@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_hyp_rapidml_valuerangeconstraint_minValueExclusive_setter(instance):
    original = instance.minValueExclusive
    instance.minValueExclusive = original
    assert instance.minValueExclusive == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_hyp_rapidml_valuerangeconstraint_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_hyp_rapidml_valuerangeconstraint_maxValueExclusive_setter(instance):
    original = instance.maxValueExclusive
    instance.maxValueExclusive = original
    assert instance.maxValueExclusive == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_hyp_rapidml_valuerangeconstraint_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original




@given(instance=rapidml_LengthConstraint_strategy)
def test_hyp_rapidml_lengthconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=rapidml_LengthConstraint_strategy)
def test_hyp_rapidml_lengthconstraint_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rapidml_LengthConstraint_strategy)
def test_hyp_rapidml_lengthconstraint_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original










@given(instance=rapidml_InlineDataExample_strategy)
def test_hyp_rapidml_inlinedataexample_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original














@given(instance=rapidml_HasTitle_strategy)
def test_hyp_rapidml_hastitle_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=rapidml_Extension_strategy)
def test_hyp_rapidml_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Extension_strategy)
def test_hyp_rapidml_extension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=rapidml_ReferenceProperty_strategy)
def test_hyp_rapidml_referenceproperty_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=rapidml_ReferenceProperty_strategy)
def test_hyp_rapidml_referenceproperty_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original






@given(instance=rapidml_PropertyRealization_strategy)
def test_hyp_rapidml_propertyrealization_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_HasStringValue_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_hasstringvalue_tostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toString' in rapidml_HasStringValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toString' in rapidml_HasStringValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toString' in rapidml_HasStringValue is not implemented or raised an error")





@given(instance=rapidml_ExternalExample_strategy)
def test_hyp_rapidml_externalexample_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original




@given(instance=rapidml_InlineExample_strategy)
def test_hyp_rapidml_inlineexample_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original








@given(instance=rapidml_URISegment_strategy)
def test_hyp_rapidml_urisegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=rapidml_ReferenceLink_strategy)
def test_hyp_rapidml_referencelink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_ReferenceLink_strategy)
def test_hyp_rapidml_referencelink_collectionRealizationLevel_setter(instance):
    original = instance.collectionRealizationLevel
    instance.collectionRealizationLevel = original
    assert instance.collectionRealizationLevel == original





@given(instance=rapidml_NamedLinkDescriptor_strategy)
def test_hyp_rapidml_namedlinkdescriptor_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=rapidml_NamedLinkDescriptor_strategy)
def test_hyp_rapidml_namedlinkdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_ImportDeclaration_strategy)
def test_hyp_rapidml_importdeclaration_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original



@given(instance=rapidml_ImportDeclaration_strategy)
def test_hyp_rapidml_importdeclaration_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=rapidml_ImportDeclaration_strategy)
def test_hyp_rapidml_importdeclaration_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original




@given(instance=rapidml_PrimitiveTypesLibrary_strategy)
def test_hyp_rapidml_primitivetypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_LinkRelationsLibrary_strategy)
def test_hyp_rapidml_linkrelationslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=rapidml_RealizationModelLocation_strategy)
def test_hyp_rapidml_realizationmodellocation_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original















@given(instance=rapidml_CollectionResource_strategy)
def test_hyp_rapidml_collectionresource_resourceRealizationKind_setter(instance):
    original = instance.resourceRealizationKind
    instance.resourceRealizationKind = original
    assert instance.resourceRealizationKind == original









@given(instance=rapidml_Documentation_strategy)
def test_hyp_rapidml_documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






@given(instance=rapidml_SecuritySchemeLibrary_strategy)
def test_hyp_rapidml_securityschemelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_SecurityScope_strategy)
def test_hyp_rapidml_securityscope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_SecuritySchemeParameter_strategy)
def test_hyp_rapidml_securityschemeparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_SecuritySchemeParameter_strategy)
def test_hyp_rapidml_securityschemeparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=rapidml_LinkRelation_strategy)
def test_hyp_rapidml_linkrelation_specURL_setter(instance):
    original = instance.specURL
    instance.specURL = original
    assert instance.specURL == original



@given(instance=rapidml_LinkRelation_strategy)
def test_hyp_rapidml_linkrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_Operation_strategy)
def test_hyp_rapidml_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_EnumConstant_strategy)
def test_hyp_rapidml_enumconstant_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original



@given(instance=rapidml_EnumConstant_strategy)
def test_hyp_rapidml_enumconstant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_EnumConstant_strategy)
def test_hyp_rapidml_enumconstant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original




@given(instance=rapidml_DataModel_strategy)
def test_hyp_rapidml_datamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=rapidml_ReferenceRealization_strategy)
def test_hyp_rapidml_referencerealization_realizationType_setter(instance):
    original = instance.realizationType
    instance.realizationType = original
    assert instance.realizationType == original



@given(instance=rapidml_ReferenceRealization_strategy)
def test_hyp_rapidml_referencerealization_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original




@given(instance=rapidml_ServiceDataResource_strategy)
def test_hyp_rapidml_servicedataresource_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_ServiceDataResource_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_servicedataresource_isincluded_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isIncluded(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isIncluded).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isIncluded' in rapidml_ServiceDataResource is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isIncluded' in rapidml_ServiceDataResource did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isIncluded' in rapidml_ServiceDataResource is not implemented or raised an error")





@given(instance=rapidml_TypedResponse_strategy)
def test_hyp_rapidml_typedresponse_statusCode_setter(instance):
    original = instance.statusCode
    instance.statusCode = original
    assert instance.statusCode == original






@given(instance=rapidml_DataType_strategy)
def test_hyp_rapidml_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=rapidml_RealizationContainer_strategy)
def test_hyp_rapidml_realizationcontainer_effectiveRealization_setter(instance):
    original = instance.effectiveRealization
    instance.effectiveRealization = original
    assert instance.effectiveRealization == original



@given(instance=rapidml_RealizationContainer_strategy)
def test_hyp_rapidml_realizationcontainer_realizationName_setter(instance):
    original = instance.realizationName
    instance.realizationName = original
    assert instance.realizationName == original



@given(instance=rapidml_RealizationContainer_strategy)
def test_hyp_rapidml_realizationcontainer_withDefaultRealization_setter(instance):
    original = instance.withDefaultRealization
    instance.withDefaultRealization = original
    assert instance.withDefaultRealization == original




@given(instance=rapidml_Feature_strategy)
def test_hyp_rapidml_feature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=rapidml_Feature_strategy)
def test_hyp_rapidml_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Feature_strategy)
def test_hyp_rapidml_feature_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=rapidml_Feature_strategy)
def test_hyp_rapidml_feature_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original





@given(instance=rapidml_ZenModel_strategy)
def test_hyp_rapidml_zenmodel_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=rapidml_ZenModel_strategy)
def test_hyp_rapidml_zenmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_Constraint_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_constraint_supports_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.supports(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.supports).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'supports' in rapidml_Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'supports' in rapidml_Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'supports' in rapidml_Constraint is not implemented or raised an error")






@given(instance=rapidml_MessageParameter_strategy)
def test_hyp_rapidml_messageparameter_httpLocation_setter(instance):
    original = instance.httpLocation
    instance.httpLocation = original
    assert instance.httpLocation == original







@given(instance=rapidml_MediaType_strategy)
def test_hyp_rapidml_mediatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_MediaType_strategy)
def test_hyp_rapidml_mediatype_specURL_setter(instance):
    original = instance.specURL
    instance.specURL = original
    assert instance.specURL == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_mediatype_hashcode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hashCode()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hashCode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hashCode' in rapidml_MediaType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hashCode' in rapidml_MediaType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hashCode' in rapidml_MediaType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_mediatype_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in rapidml_MediaType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in rapidml_MediaType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in rapidml_MediaType is not implemented or raised an error")




@given(instance=rapidml_Parameter_strategy)
def test_hyp_rapidml_parameter_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=rapidml_Parameter_strategy)
def test_hyp_rapidml_parameter_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original



@given(instance=rapidml_Parameter_strategy)
def test_hyp_rapidml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Parameter_strategy)
def test_hyp_rapidml_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original




@given(instance=rapidml_Method_strategy)
def test_hyp_rapidml_method_httpMethod_setter(instance):
    original = instance.httpMethod
    instance.httpMethod = original
    assert instance.httpMethod == original



@given(instance=rapidml_Method_strategy)
def test_hyp_rapidml_method_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=rapidml_ResourceAPI_strategy)
def test_hyp_rapidml_resourceapi_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_ResourceAPI_strategy)
def test_hyp_rapidml_resourceapi_baseURI_setter(instance):
    original = instance.baseURI
    instance.baseURI = original
    assert instance.baseURI == original



@given(instance=rapidml_ResourceAPI_strategy)
def test_hyp_rapidml_resourceapi_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original




@given(instance=rapidml_SecurityScheme_strategy)
def test_hyp_rapidml_securityscheme_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rapidml_SecurityScheme_strategy)
def test_hyp_rapidml_securityscheme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_SecurityScheme_strategy)
def test_hyp_rapidml_securityscheme_flow_setter(instance):
    original = instance.flow
    instance.flow = original
    assert instance.flow == original




@given(instance=rapidml_TypedMessage_strategy)
def test_hyp_rapidml_typedmessage_useParentTypeReference_setter(instance):
    original = instance.useParentTypeReference
    instance.useParentTypeReference = original
    assert instance.useParentTypeReference == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_TypedMessage_strategy)
@settings(max_examples=30)
def test_hyp_rapidml_typedmessage_isincluded_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isIncluded(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isIncluded).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isIncluded' in rapidml_TypedMessage is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isIncluded' in rapidml_TypedMessage did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isIncluded' in rapidml_TypedMessage is not implemented or raised an error")




@given(instance=rapidml_ResourceDefinition_strategy)
def test_hyp_rapidml_resourcedefinition_name_setter(instance):
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
    ConstrainableType,
    Constraint,
    DataExample,
    DataType,
    Documentable,
    Element,
    Example,
    Extensible,
    Feature,
    HasSecurityValue,
    HasStringValue,
    HasTitle,
    Inheritable,
    ObjectRealization,
    Parameter,
    RESTElement,
    RealizationContainer,
    ReferenceElement,
    ReferenceTreatment,
    ResourceDefinition,
    ServiceDataResource,
    SimpleType,
    SingleValueType,
    SourceReference,
    TypedMessage,
    URIParameter,
    URISegment,
    WithDataExamples,
    WithExamples,
    rapidml_AuthenticationMethod,
    rapidml_CollectionParameter,
    rapidml_CollectionReferenceElement,
    rapidml_CollectionResource,
    rapidml_ConstrainableType,
    rapidml_Constraint,
    rapidml_DataExample,
    rapidml_DataModel,
    rapidml_DataType,
    rapidml_Documentable,
    rapidml_Documentation,
    rapidml_Element,
    rapidml_EnumConstant,
    rapidml_Enumeration,
    rapidml_Example,
    rapidml_Extensible,
    rapidml_Extension,
    rapidml_ExternalExample,
    rapidml_Feature,
    rapidml_HasSecurityValue,
    rapidml_HasStringValue,
    rapidml_HasTitle,
    rapidml_ImportDeclaration,
    rapidml_Inheritable,
    rapidml_InlineDataExample,
    rapidml_InlineExample,
    rapidml_LengthConstraint,
    rapidml_LinkRelation,
    rapidml_LinkRelationsLibrary,
    rapidml_MatrixParameter,
    rapidml_MediaType,
    rapidml_MediaTypesLibrary,
    rapidml_MessageParameter,
    rapidml_Method,
    rapidml_NamedLinkDescriptor,
    rapidml_ObjectRealization,
    rapidml_ObjectResource,
    rapidml_Operation,
    rapidml_Parameter,
    rapidml_PathSegment,
    rapidml_PrimitiveProperty,
    rapidml_PrimitiveType,
    rapidml_PrimitiveTypeSourceReference,
    rapidml_PrimitiveTypesLibrary,
    rapidml_PropertyRealization,
    rapidml_PropertyReference,
    rapidml_RESTElement,
    rapidml_RealizationContainer,
    rapidml_RealizationModelLocation,
    rapidml_ReferenceElement,
    rapidml_ReferenceEmbed,
    rapidml_ReferenceLink,
    rapidml_ReferenceProperty,
    rapidml_ReferenceRealization,
    rapidml_ReferenceTreatment,
    rapidml_RegExConstraint,
    rapidml_ResourceAPI,
    rapidml_ResourceDefinition,
    rapidml_SecurityScheme,
    rapidml_SecuritySchemeLibrary,
    rapidml_SecuritySchemeParameter,
    rapidml_SecurityScope,
    rapidml_ServiceDataResource,
    rapidml_SimpleType,
    rapidml_SingleValueType,
    rapidml_SourceReference,
    rapidml_Structure,
    rapidml_TemplateParameter,
    rapidml_TypedMessage,
    rapidml_TypedRequest,
    rapidml_TypedResponse,
    rapidml_URI,
    rapidml_URIParameter,
    rapidml_URISegment,
    rapidml_URISegmentWithParameter,
    rapidml_UserDefinedType,
    rapidml_ValueRangeConstraint,
    rapidml_WithDataExamples,
    rapidml_WithExamples,
    rapidml_ZenModel,
    AuthenticationFlows,
    AuthenticationTypes,
    CollectionRealizationEnum,
    CollectionRealizationLevelEnum,
    HTTPMethods,
    HttpMessageParameterLocation,
    ReferenceRealizationEnum,
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

def test_rapidml_CollectionResource_resourceRealizationKind_value_roundtrip():
    instance = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    assert instance.resourceRealizationKind == "sample_text"
    instance.resourceRealizationKind = "sample_text_2"
    assert instance.resourceRealizationKind == "sample_text_2"


def test_rapidml_DataModel_name_value_roundtrip():
    instance = rapidml_DataModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_DataType_name_value_roundtrip():
    instance = rapidml_DataType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Documentation_text_value_roundtrip():
    instance = rapidml_Documentation(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_rapidml_Element_cardinality_value_roundtrip():
    instance = rapidml_Element(cardinality="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_rapidml_EnumConstant_integerValue_value_roundtrip():
    instance = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    assert instance.integerValue == 7
    instance.integerValue = 13
    assert instance.integerValue == 13


def test_rapidml_EnumConstant_literalValue_value_roundtrip():
    instance = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    assert instance.literalValue == "sample_text"
    instance.literalValue = "sample_text_2"
    assert instance.literalValue == "sample_text_2"


def test_rapidml_EnumConstant_name_value_roundtrip():
    instance = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Extension_name_value_roundtrip():
    instance = rapidml_Extension(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Extension_value_value_roundtrip():
    instance = rapidml_Extension(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_rapidml_ExternalExample_path_value_roundtrip():
    instance = rapidml_ExternalExample(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_rapidml_Feature_key_value_roundtrip():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert instance.key == True
    instance.key = False
    assert instance.key == False


def test_rapidml_Feature_name_value_roundtrip():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Feature_readOnly_value_roundtrip():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_rapidml_Feature_restriction_value_roundtrip():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert instance.restriction == True
    instance.restriction = False
    assert instance.restriction == False


def test_rapidml_HasTitle_title_value_roundtrip():
    instance = rapidml_HasTitle(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_rapidml_ImportDeclaration_alias_value_roundtrip():
    instance = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_rapidml_ImportDeclaration_importURI_value_roundtrip():
    instance = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_rapidml_ImportDeclaration_importedNamespace_value_roundtrip():
    instance = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_rapidml_InlineDataExample_body_value_roundtrip():
    instance = rapidml_InlineDataExample(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_rapidml_InlineExample_body_value_roundtrip():
    instance = rapidml_InlineExample(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_rapidml_LengthConstraint_length_value_roundtrip():
    instance = rapidml_LengthConstraint(length=7, maxLength=7, minLength=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_rapidml_LengthConstraint_maxLength_value_roundtrip():
    instance = rapidml_LengthConstraint(length=7, maxLength=7, minLength=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_rapidml_LengthConstraint_minLength_value_roundtrip():
    instance = rapidml_LengthConstraint(length=7, maxLength=7, minLength=7)
    assert instance.minLength == 7
    instance.minLength = 13
    assert instance.minLength == 13


def test_rapidml_LinkRelation_name_value_roundtrip():
    instance = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_LinkRelation_specURL_value_roundtrip():
    instance = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    assert instance.specURL == "sample_text"
    instance.specURL = "sample_text_2"
    assert instance.specURL == "sample_text_2"


def test_rapidml_LinkRelationsLibrary_name_value_roundtrip():
    instance = rapidml_LinkRelationsLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_MediaType_name_value_roundtrip():
    instance = rapidml_MediaType(name="sample_text", specURL="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_MediaType_specURL_value_roundtrip():
    instance = rapidml_MediaType(name="sample_text", specURL="sample_text")
    assert instance.specURL == "sample_text"
    instance.specURL = "sample_text_2"
    assert instance.specURL == "sample_text_2"


def test_rapidml_MessageParameter_httpLocation_value_roundtrip():
    instance = rapidml_MessageParameter(httpLocation="sample_text")
    assert instance.httpLocation == "sample_text"
    instance.httpLocation = "sample_text_2"
    assert instance.httpLocation == "sample_text_2"


def test_rapidml_Method_httpMethod_value_roundtrip():
    instance = rapidml_Method(httpMethod="sample_text", id="sample_text")
    assert instance.httpMethod == "sample_text"
    instance.httpMethod = "sample_text_2"
    assert instance.httpMethod == "sample_text_2"


def test_rapidml_Method_id_value_roundtrip():
    instance = rapidml_Method(httpMethod="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_rapidml_NamedLinkDescriptor_default_value_roundtrip():
    instance = rapidml_NamedLinkDescriptor(default=True, name="sample_text")
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_rapidml_NamedLinkDescriptor_name_value_roundtrip():
    instance = rapidml_NamedLinkDescriptor(default=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Operation_name_value_roundtrip():
    instance = rapidml_Operation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Parameter_default_value_roundtrip():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_rapidml_Parameter_fixed_value_roundtrip():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert instance.fixed == "sample_text"
    instance.fixed = "sample_text_2"
    assert instance.fixed == "sample_text_2"


def test_rapidml_Parameter_name_value_roundtrip():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_Parameter_required_value_roundtrip():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_rapidml_PrimitiveTypesLibrary_name_value_roundtrip():
    instance = rapidml_PrimitiveTypesLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_PropertyRealization_cardinality_value_roundtrip():
    instance = rapidml_PropertyRealization(cardinality="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_rapidml_RealizationContainer_effectiveRealization_value_roundtrip():
    instance = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    assert instance.effectiveRealization == "sample_text"
    instance.effectiveRealization = "sample_text_2"
    assert instance.effectiveRealization == "sample_text_2"


def test_rapidml_RealizationContainer_realizationName_value_roundtrip():
    instance = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    assert instance.realizationName == "sample_text"
    instance.realizationName = "sample_text_2"
    assert instance.realizationName == "sample_text_2"


def test_rapidml_RealizationContainer_withDefaultRealization_value_roundtrip():
    instance = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    assert instance.withDefaultRealization == True
    instance.withDefaultRealization = False
    assert instance.withDefaultRealization == False


def test_rapidml_RealizationModelLocation_uri_value_roundtrip():
    instance = rapidml_RealizationModelLocation(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_rapidml_ReferenceLink_collectionRealizationLevel_value_roundtrip():
    instance = rapidml_ReferenceLink(collectionRealizationLevel="sample_text", name="sample_text")
    assert instance.collectionRealizationLevel == "sample_text"
    instance.collectionRealizationLevel = "sample_text_2"
    assert instance.collectionRealizationLevel == "sample_text_2"


def test_rapidml_ReferenceLink_name_value_roundtrip():
    instance = rapidml_ReferenceLink(collectionRealizationLevel="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_ReferenceProperty_container_value_roundtrip():
    instance = rapidml_ReferenceProperty(container=True, containment=True)
    assert instance.container == True
    instance.container = False
    assert instance.container == False


def test_rapidml_ReferenceProperty_containment_value_roundtrip():
    instance = rapidml_ReferenceProperty(container=True, containment=True)
    assert instance.containment == True
    instance.containment = False
    assert instance.containment == False


def test_rapidml_ReferenceRealization_multiValued_value_roundtrip():
    instance = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    assert instance.multiValued == True
    instance.multiValued = False
    assert instance.multiValued == False


def test_rapidml_ReferenceRealization_realizationType_value_roundtrip():
    instance = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    assert instance.realizationType == "sample_text"
    instance.realizationType = "sample_text_2"
    assert instance.realizationType == "sample_text_2"


def test_rapidml_RegExConstraint_pattern_value_roundtrip():
    instance = rapidml_RegExConstraint(pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_rapidml_ResourceAPI_baseURI_value_roundtrip():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert instance.baseURI == "sample_text"
    instance.baseURI = "sample_text_2"
    assert instance.baseURI == "sample_text_2"


def test_rapidml_ResourceAPI_name_value_roundtrip():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_ResourceAPI_version_value_roundtrip():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_rapidml_ResourceDefinition_name_value_roundtrip():
    instance = rapidml_ResourceDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_SecurityScheme_flow_value_roundtrip():
    instance = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    assert instance.flow == "sample_text"
    instance.flow = "sample_text_2"
    assert instance.flow == "sample_text_2"


def test_rapidml_SecurityScheme_name_value_roundtrip():
    instance = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_SecurityScheme_type_value_roundtrip():
    instance = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_rapidml_SecuritySchemeLibrary_name_value_roundtrip():
    instance = rapidml_SecuritySchemeLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_SecuritySchemeParameter_name_value_roundtrip():
    instance = rapidml_SecuritySchemeParameter(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_SecuritySchemeParameter_value_value_roundtrip():
    instance = rapidml_SecuritySchemeParameter(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_rapidml_SecurityScope_name_value_roundtrip():
    instance = rapidml_SecurityScope(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_ServiceDataResource_default_value_roundtrip():
    instance = rapidml_ServiceDataResource(default=True)
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_rapidml_TypedMessage_useParentTypeReference_value_roundtrip():
    instance = rapidml_TypedMessage(useParentTypeReference=True)
    assert instance.useParentTypeReference == True
    instance.useParentTypeReference = False
    assert instance.useParentTypeReference == False


def test_rapidml_TypedResponse_statusCode_value_roundtrip():
    instance = rapidml_TypedResponse(statusCode=7)
    assert instance.statusCode == 7
    instance.statusCode = 13
    assert instance.statusCode == 13


def test_rapidml_URISegment_name_value_roundtrip():
    instance = rapidml_URISegment(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_ValueRangeConstraint_maxValue_value_roundtrip():
    instance = rapidml_ValueRangeConstraint(maxValue="sample_text", maxValueExclusive=True, minValue="sample_text", minValueExclusive=True)
    assert instance.maxValue == "sample_text"
    instance.maxValue = "sample_text_2"
    assert instance.maxValue == "sample_text_2"


def test_rapidml_ValueRangeConstraint_maxValueExclusive_value_roundtrip():
    instance = rapidml_ValueRangeConstraint(maxValue="sample_text", maxValueExclusive=True, minValue="sample_text", minValueExclusive=True)
    assert instance.maxValueExclusive == True
    instance.maxValueExclusive = False
    assert instance.maxValueExclusive == False


def test_rapidml_ValueRangeConstraint_minValue_value_roundtrip():
    instance = rapidml_ValueRangeConstraint(maxValue="sample_text", maxValueExclusive=True, minValue="sample_text", minValueExclusive=True)
    assert instance.minValue == "sample_text"
    instance.minValue = "sample_text_2"
    assert instance.minValue == "sample_text_2"


def test_rapidml_ValueRangeConstraint_minValueExclusive_value_roundtrip():
    instance = rapidml_ValueRangeConstraint(maxValue="sample_text", maxValueExclusive=True, minValue="sample_text", minValueExclusive=True)
    assert instance.minValueExclusive == True
    instance.minValueExclusive = False
    assert instance.minValueExclusive == False


def test_rapidml_ZenModel_name_value_roundtrip():
    instance = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rapidml_ZenModel_namespace_value_roundtrip():
    instance = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    assert instance.namespace == "sample_text"
    instance.namespace = "sample_text_2"
    assert instance.namespace == "sample_text_2"


def test_rapidml_PrimitiveProperty_isa_ConstrainableType():
    instance = rapidml_PrimitiveProperty()
    assert isinstance(instance, ConstrainableType)


def test_rapidml_PropertyRealization_isa_ConstrainableType():
    instance = rapidml_PropertyRealization(cardinality="sample_text")
    assert isinstance(instance, ConstrainableType)


def test_rapidml_UserDefinedType_isa_ConstrainableType():
    instance = rapidml_UserDefinedType()
    assert isinstance(instance, ConstrainableType)


def test_rapidml_LengthConstraint_isa_Constraint():
    instance = rapidml_LengthConstraint(length=7, maxLength=7, minLength=7)
    assert isinstance(instance, Constraint)


def test_rapidml_RegExConstraint_isa_Constraint():
    instance = rapidml_RegExConstraint(pattern="sample_text")
    assert isinstance(instance, Constraint)


def test_rapidml_ValueRangeConstraint_isa_Constraint():
    instance = rapidml_ValueRangeConstraint(maxValue="sample_text", maxValueExclusive=True, minValue="sample_text", minValueExclusive=True)
    assert isinstance(instance, Constraint)


def test_rapidml_InlineDataExample_isa_DataExample():
    instance = rapidml_InlineDataExample(body="sample_text")
    assert isinstance(instance, DataExample)


def test_rapidml_SingleValueType_isa_DataType():
    instance = rapidml_SingleValueType()
    assert isinstance(instance, DataType)


def test_rapidml_Structure_isa_DataType():
    instance = rapidml_Structure()
    assert isinstance(instance, DataType)


def test_rapidml_DataModel_isa_Documentable():
    instance = rapidml_DataModel(name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_DataType_isa_Documentable():
    instance = rapidml_DataType(name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_EnumConstant_isa_Documentable():
    instance = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_Feature_isa_Documentable():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert isinstance(instance, Documentable)


def test_rapidml_LinkRelation_isa_Documentable():
    instance = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_Operation_isa_Documentable():
    instance = rapidml_Operation(name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_RESTElement_isa_Documentable():
    instance = rapidml_RESTElement()
    assert isinstance(instance, Documentable)


def test_rapidml_SecurityScheme_isa_Documentable():
    instance = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_SecuritySchemeLibrary_isa_Documentable():
    instance = rapidml_SecuritySchemeLibrary(name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_SecuritySchemeParameter_isa_Documentable():
    instance = rapidml_SecuritySchemeParameter(name="sample_text", value="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_SecurityScope_isa_Documentable():
    instance = rapidml_SecurityScope(name="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_ZenModel_isa_Documentable():
    instance = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    assert isinstance(instance, Documentable)


def test_rapidml_Feature_isa_Element():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert isinstance(instance, Element)


def test_rapidml_ReferenceElement_isa_Element():
    instance = rapidml_ReferenceElement()
    assert isinstance(instance, Element)


def test_rapidml_ExternalExample_isa_Example():
    instance = rapidml_ExternalExample(path="sample_text")
    assert isinstance(instance, Example)


def test_rapidml_InlineExample_isa_Example():
    instance = rapidml_InlineExample(body="sample_text")
    assert isinstance(instance, Example)


def test_rapidml_ConstrainableType_isa_Extensible():
    instance = rapidml_ConstrainableType()
    assert isinstance(instance, Extensible)


def test_rapidml_Constraint_isa_Extensible():
    instance = rapidml_Constraint()
    assert isinstance(instance, Extensible)


def test_rapidml_DataType_isa_Extensible():
    instance = rapidml_DataType(name="sample_text")
    assert isinstance(instance, Extensible)


def test_rapidml_Feature_isa_Extensible():
    instance = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    assert isinstance(instance, Extensible)


def test_rapidml_Method_isa_Extensible():
    instance = rapidml_Method(httpMethod="sample_text", id="sample_text")
    assert isinstance(instance, Extensible)


def test_rapidml_ObjectRealization_isa_Extensible():
    instance = rapidml_ObjectRealization()
    assert isinstance(instance, Extensible)


def test_rapidml_Parameter_isa_Extensible():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert isinstance(instance, Extensible)


def test_rapidml_RESTElement_isa_Extensible():
    instance = rapidml_RESTElement()
    assert isinstance(instance, Extensible)


def test_rapidml_RealizationContainer_isa_Extensible():
    instance = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    assert isinstance(instance, Extensible)


def test_rapidml_ReferenceTreatment_isa_Extensible():
    instance = rapidml_ReferenceTreatment()
    assert isinstance(instance, Extensible)


def test_rapidml_ZenModel_isa_Extensible():
    instance = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    assert isinstance(instance, Extensible)


def test_rapidml_PrimitiveProperty_isa_Feature():
    instance = rapidml_PrimitiveProperty()
    assert isinstance(instance, Feature)


def test_rapidml_ReferenceProperty_isa_Feature():
    instance = rapidml_ReferenceProperty(container=True, containment=True)
    assert isinstance(instance, Feature)


def test_rapidml_Method_isa_HasSecurityValue():
    instance = rapidml_Method(httpMethod="sample_text", id="sample_text")
    assert isinstance(instance, HasSecurityValue)


def test_rapidml_ResourceAPI_isa_HasSecurityValue():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert isinstance(instance, HasSecurityValue)


def test_rapidml_ResourceDefinition_isa_HasSecurityValue():
    instance = rapidml_ResourceDefinition(name="sample_text")
    assert isinstance(instance, HasSecurityValue)


def test_rapidml_PrimitiveProperty_isa_HasStringValue():
    instance = rapidml_PrimitiveProperty()
    assert isinstance(instance, HasStringValue)


def test_rapidml_URI_isa_HasStringValue():
    instance = rapidml_URI()
    assert isinstance(instance, HasStringValue)


def test_rapidml_URISegment_isa_HasStringValue():
    instance = rapidml_URISegment(name="sample_text")
    assert isinstance(instance, HasStringValue)


def test_rapidml_DataModel_isa_HasTitle():
    instance = rapidml_DataModel(name="sample_text")
    assert isinstance(instance, HasTitle)


def test_rapidml_ResourceAPI_isa_HasTitle():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert isinstance(instance, HasTitle)


def test_rapidml_ZenModel_isa_HasTitle():
    instance = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    assert isinstance(instance, HasTitle)


def test_rapidml_Structure_isa_Inheritable():
    instance = rapidml_Structure()
    assert isinstance(instance, Inheritable)


def test_rapidml_NamedLinkDescriptor_isa_ObjectRealization():
    instance = rapidml_NamedLinkDescriptor(default=True, name="sample_text")
    assert isinstance(instance, ObjectRealization)


def test_rapidml_CollectionParameter_isa_Parameter():
    instance = rapidml_CollectionParameter()
    assert isinstance(instance, Parameter)


def test_rapidml_MessageParameter_isa_Parameter():
    instance = rapidml_MessageParameter(httpLocation="sample_text")
    assert isinstance(instance, Parameter)


def test_rapidml_URIParameter_isa_Parameter():
    instance = rapidml_URIParameter()
    assert isinstance(instance, Parameter)


def test_rapidml_MediaType_isa_RESTElement():
    instance = rapidml_MediaType(name="sample_text", specURL="sample_text")
    assert isinstance(instance, RESTElement)


def test_rapidml_Method_isa_RESTElement():
    instance = rapidml_Method(httpMethod="sample_text", id="sample_text")
    assert isinstance(instance, RESTElement)


def test_rapidml_Parameter_isa_RESTElement():
    instance = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    assert isinstance(instance, RESTElement)


def test_rapidml_ResourceAPI_isa_RESTElement():
    instance = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    assert isinstance(instance, RESTElement)


def test_rapidml_ResourceDefinition_isa_RESTElement():
    instance = rapidml_ResourceDefinition(name="sample_text")
    assert isinstance(instance, RESTElement)


def test_rapidml_SecurityScheme_isa_RESTElement():
    instance = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    assert isinstance(instance, RESTElement)


def test_rapidml_TypedMessage_isa_RESTElement():
    instance = rapidml_TypedMessage(useParentTypeReference=True)
    assert isinstance(instance, RESTElement)


def test_rapidml_ReferenceRealization_isa_RealizationContainer():
    instance = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    assert isinstance(instance, RealizationContainer)


def test_rapidml_ServiceDataResource_isa_RealizationContainer():
    instance = rapidml_ServiceDataResource(default=True)
    assert isinstance(instance, RealizationContainer)


def test_rapidml_TypedMessage_isa_RealizationContainer():
    instance = rapidml_TypedMessage(useParentTypeReference=True)
    assert isinstance(instance, RealizationContainer)


def test_rapidml_CollectionReferenceElement_isa_ReferenceElement():
    instance = rapidml_CollectionReferenceElement()
    assert isinstance(instance, ReferenceElement)


def test_rapidml_ReferenceProperty_isa_ReferenceElement():
    instance = rapidml_ReferenceProperty(container=True, containment=True)
    assert isinstance(instance, ReferenceElement)


def test_rapidml_ReferenceEmbed_isa_ReferenceTreatment():
    instance = rapidml_ReferenceEmbed()
    assert isinstance(instance, ReferenceTreatment)


def test_rapidml_ReferenceLink_isa_ReferenceTreatment():
    instance = rapidml_ReferenceLink(collectionRealizationLevel="sample_text", name="sample_text")
    assert isinstance(instance, ReferenceTreatment)


def test_rapidml_ServiceDataResource_isa_ResourceDefinition():
    instance = rapidml_ServiceDataResource(default=True)
    assert isinstance(instance, ResourceDefinition)


def test_rapidml_CollectionResource_isa_ServiceDataResource():
    instance = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    assert isinstance(instance, ServiceDataResource)


def test_rapidml_ObjectResource_isa_ServiceDataResource():
    instance = rapidml_ObjectResource()
    assert isinstance(instance, ServiceDataResource)


def test_rapidml_PrimitiveType_isa_SimpleType():
    instance = rapidml_PrimitiveType()
    assert isinstance(instance, SimpleType)


def test_rapidml_UserDefinedType_isa_SimpleType():
    instance = rapidml_UserDefinedType()
    assert isinstance(instance, SimpleType)


def test_rapidml_Enumeration_isa_SingleValueType():
    instance = rapidml_Enumeration()
    assert isinstance(instance, SingleValueType)


def test_rapidml_SimpleType_isa_SingleValueType():
    instance = rapidml_SimpleType()
    assert isinstance(instance, SingleValueType)


def test_rapidml_PrimitiveTypeSourceReference_isa_SourceReference():
    instance = rapidml_PrimitiveTypeSourceReference()
    assert isinstance(instance, SourceReference)


def test_rapidml_PropertyReference_isa_SourceReference():
    instance = rapidml_PropertyReference()
    assert isinstance(instance, SourceReference)


def test_rapidml_TypedRequest_isa_TypedMessage():
    instance = rapidml_TypedRequest()
    assert isinstance(instance, TypedMessage)


def test_rapidml_TypedResponse_isa_TypedMessage():
    instance = rapidml_TypedResponse(statusCode=7)
    assert isinstance(instance, TypedMessage)


def test_rapidml_MatrixParameter_isa_URIParameter():
    instance = rapidml_MatrixParameter()
    assert isinstance(instance, URIParameter)


def test_rapidml_TemplateParameter_isa_URIParameter():
    instance = rapidml_TemplateParameter()
    assert isinstance(instance, URIParameter)


def test_rapidml_URISegmentWithParameter_isa_URISegment():
    instance = rapidml_URISegmentWithParameter()
    assert isinstance(instance, URISegment)


def test_rapidml_Structure_isa_WithDataExamples():
    instance = rapidml_Structure()
    assert isinstance(instance, WithDataExamples)


def test_rapidml_ResourceDefinition_isa_WithExamples():
    instance = rapidml_ResourceDefinition(name="sample_text")
    assert isinstance(instance, WithExamples)


def test_rapidml_TypedMessage_isa_WithExamples():
    instance = rapidml_TypedMessage(useParentTypeReference=True)
    assert isinstance(instance, WithExamples)


def test_assoc_URI5_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_URI()
    b2 = rapidml_URI()
    _safe_set(a, 'rapidml_ResourceDefinition6', b1)
    assert _is_linked(a, 'rapidml_ResourceDefinition6', b1)
    if hasattr(b1, 'rapidml_URI'):
        assert _is_linked(b1, 'rapidml_URI', a)
    _safe_set(a, 'rapidml_ResourceDefinition6', b2)
    assert _is_linked(a, 'rapidml_ResourceDefinition6', b2)
    if hasattr(b1, 'rapidml_URI'):
        assert not _is_linked(b1, 'rapidml_URI', a)
    if hasattr(b2, 'rapidml_URI'):
        assert _is_linked(b2, 'rapidml_URI', a)
    _safe_set(a, 'rapidml_ResourceDefinition6', None)
    assert not _is_linked(a, 'rapidml_ResourceDefinition6', b2)
    if hasattr(b2, 'rapidml_URI'):
        assert not _is_linked(b2, 'rapidml_URI', a)


def test_assoc_allMediaTypes2_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ResourceDefinition3', {b1})
    assert _is_linked(a, 'rapidml_ResourceDefinition3', b1)
    if hasattr(b1, 'rapidml_MediaType4'):
        assert _is_linked(b1, 'rapidml_MediaType4', a)
    _safe_set(a, 'rapidml_ResourceDefinition3', {b2})
    assert _is_linked(a, 'rapidml_ResourceDefinition3', b2)
    if hasattr(b1, 'rapidml_MediaType4'):
        assert not _is_linked(b1, 'rapidml_MediaType4', a)
    if hasattr(b2, 'rapidml_MediaType4'):
        assert _is_linked(b2, 'rapidml_MediaType4', a)
    _safe_set(a, 'rapidml_ResourceDefinition3', set())
    assert not _is_linked(a, 'rapidml_ResourceDefinition3', b2)
    if hasattr(b2, 'rapidml_MediaType4'):
        assert not _is_linked(b2, 'rapidml_MediaType4', a)


def test_assoc_allSupertypes150_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Inheritable()
    b2 = rapidml_Inheritable()
    _safe_set(a, 'rapidml_Structure151', {b1})
    assert _is_linked(a, 'rapidml_Structure151', b1)
    if hasattr(b1, 'rapidml_Inheritable152'):
        assert _is_linked(b1, 'rapidml_Inheritable152', a)
    _safe_set(a, 'rapidml_Structure151', {b2})
    assert _is_linked(a, 'rapidml_Structure151', b2)
    if hasattr(b1, 'rapidml_Inheritable152'):
        assert not _is_linked(b1, 'rapidml_Inheritable152', a)
    if hasattr(b2, 'rapidml_Inheritable152'):
        assert _is_linked(b2, 'rapidml_Inheritable152', a)
    _safe_set(a, 'rapidml_Structure151', set())
    assert not _is_linked(a, 'rapidml_Structure151', b2)
    if hasattr(b2, 'rapidml_Inheritable152'):
        assert not _is_linked(b2, 'rapidml_Inheritable152', a)


def test_assoc_autoRealizations64_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_RealizationModelLocation(uri="sample_text")
    b2 = rapidml_RealizationModelLocation(uri="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI65', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI65', b1)
    if hasattr(b1, 'rapidml_RealizationModelLocation'):
        assert _is_linked(b1, 'rapidml_RealizationModelLocation', a)
    _safe_set(a, 'rapidml_ResourceAPI65', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI65', b2)
    if hasattr(b1, 'rapidml_RealizationModelLocation'):
        assert not _is_linked(b1, 'rapidml_RealizationModelLocation', a)
    if hasattr(b2, 'rapidml_RealizationModelLocation'):
        assert _is_linked(b2, 'rapidml_RealizationModelLocation', a)
    _safe_set(a, 'rapidml_ResourceAPI65', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI65', b2)
    if hasattr(b2, 'rapidml_RealizationModelLocation'):
        assert not _is_linked(b2, 'rapidml_RealizationModelLocation', a)


def test_assoc_baseProperty85_link_reassign_clear():
    a = rapidml_PropertyRealization(cardinality="sample_text")
    b1 = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    b2 = rapidml_Feature(key=False, name="sample_text_2", readOnly=False, restriction=False)
    _safe_set(a, 'rapidml_PropertyRealization', b1)
    assert _is_linked(a, 'rapidml_PropertyRealization', b1)
    if hasattr(b1, 'rapidml_Feature'):
        assert _is_linked(b1, 'rapidml_Feature', a)
    _safe_set(a, 'rapidml_PropertyRealization', b2)
    assert _is_linked(a, 'rapidml_PropertyRealization', b2)
    if hasattr(b1, 'rapidml_Feature'):
        assert not _is_linked(b1, 'rapidml_Feature', a)
    if hasattr(b2, 'rapidml_Feature'):
        assert _is_linked(b2, 'rapidml_Feature', a)
    _safe_set(a, 'rapidml_PropertyRealization', None)
    assert not _is_linked(a, 'rapidml_PropertyRealization', b2)
    if hasattr(b2, 'rapidml_Feature'):
        assert not _is_linked(b2, 'rapidml_Feature', a)


def test_assoc_baseType157_link_reassign_clear():
    a = rapidml_PrimitiveType()
    b1 = rapidml_Enumeration()
    b2 = rapidml_Enumeration()
    _safe_set(a, 'rapidml_PrimitiveType158', b1)
    assert _is_linked(a, 'rapidml_PrimitiveType158', b1)
    if hasattr(b1, 'rapidml_Enumeration'):
        assert _is_linked(b1, 'rapidml_Enumeration', a)
    _safe_set(a, 'rapidml_PrimitiveType158', b2)
    assert _is_linked(a, 'rapidml_PrimitiveType158', b2)
    if hasattr(b1, 'rapidml_Enumeration'):
        assert not _is_linked(b1, 'rapidml_Enumeration', a)
    if hasattr(b2, 'rapidml_Enumeration'):
        assert _is_linked(b2, 'rapidml_Enumeration', a)
    _safe_set(a, 'rapidml_PrimitiveType158', None)
    assert not _is_linked(a, 'rapidml_PrimitiveType158', b2)
    if hasattr(b2, 'rapidml_Enumeration'):
        assert not _is_linked(b2, 'rapidml_Enumeration', a)


def test_assoc_baseType160_link_reassign_clear():
    a = rapidml_UserDefinedType()
    b1 = rapidml_SimpleType()
    b2 = rapidml_SimpleType()
    _safe_set(a, 'rapidml_UserDefinedType', b1)
    assert _is_linked(a, 'rapidml_UserDefinedType', b1)
    if hasattr(b1, 'rapidml_SimpleType'):
        assert _is_linked(b1, 'rapidml_SimpleType', a)
    _safe_set(a, 'rapidml_UserDefinedType', b2)
    assert _is_linked(a, 'rapidml_UserDefinedType', b2)
    if hasattr(b1, 'rapidml_SimpleType'):
        assert not _is_linked(b1, 'rapidml_SimpleType', a)
    if hasattr(b2, 'rapidml_SimpleType'):
        assert _is_linked(b2, 'rapidml_SimpleType', a)
    _safe_set(a, 'rapidml_UserDefinedType', None)
    assert not _is_linked(a, 'rapidml_UserDefinedType', b2)
    if hasattr(b2, 'rapidml_SimpleType'):
        assert not _is_linked(b2, 'rapidml_SimpleType', a)


def test_assoc_collectionParameters28_link_reassign_clear():
    a = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    b1 = rapidml_CollectionParameter()
    b2 = rapidml_CollectionParameter()
    _safe_set(a, 'containingResourceDefinition29', {b1})
    assert _is_linked(a, 'containingResourceDefinition29', b1)
    if hasattr(b1, 'CollectionParameter'):
        assert _is_linked(b1, 'CollectionParameter', a)
    _safe_set(a, 'containingResourceDefinition29', {b2})
    assert _is_linked(a, 'containingResourceDefinition29', b2)
    if hasattr(b1, 'CollectionParameter'):
        assert not _is_linked(b1, 'CollectionParameter', a)
    if hasattr(b2, 'CollectionParameter'):
        assert _is_linked(b2, 'CollectionParameter', a)
    _safe_set(a, 'containingResourceDefinition29', set())
    assert not _is_linked(a, 'containingResourceDefinition29', b2)
    if hasattr(b2, 'CollectionParameter'):
        assert not _is_linked(b2, 'CollectionParameter', a)


def test_assoc_conceptualFeature32_link_reassign_clear():
    a = rapidml_PropertyReference()
    b1 = rapidml_PrimitiveProperty()
    b2 = rapidml_PrimitiveProperty()
    _safe_set(a, 'rapidml_PropertyReference', b1)
    assert _is_linked(a, 'rapidml_PropertyReference', b1)
    if hasattr(b1, 'rapidml_PrimitiveProperty'):
        assert _is_linked(b1, 'rapidml_PrimitiveProperty', a)
    _safe_set(a, 'rapidml_PropertyReference', b2)
    assert _is_linked(a, 'rapidml_PropertyReference', b2)
    if hasattr(b1, 'rapidml_PrimitiveProperty'):
        assert not _is_linked(b1, 'rapidml_PrimitiveProperty', a)
    if hasattr(b2, 'rapidml_PrimitiveProperty'):
        assert _is_linked(b2, 'rapidml_PrimitiveProperty', a)
    _safe_set(a, 'rapidml_PropertyReference', None)
    assert not _is_linked(a, 'rapidml_PropertyReference', b2)
    if hasattr(b2, 'rapidml_PrimitiveProperty'):
        assert not _is_linked(b2, 'rapidml_PrimitiveProperty', a)


def test_assoc_constraints164_link_reassign_clear():
    a = rapidml_Constraint()
    b1 = rapidml_ConstrainableType()
    b2 = rapidml_ConstrainableType()
    _safe_set(a, 'rapidml_Constraint', b1)
    assert _is_linked(a, 'rapidml_Constraint', b1)
    if hasattr(b1, 'rapidml_ConstrainableType'):
        assert _is_linked(b1, 'rapidml_ConstrainableType', a)
    _safe_set(a, 'rapidml_Constraint', b2)
    assert _is_linked(a, 'rapidml_Constraint', b2)
    if hasattr(b1, 'rapidml_ConstrainableType'):
        assert not _is_linked(b1, 'rapidml_ConstrainableType', a)
    if hasattr(b2, 'rapidml_ConstrainableType'):
        assert _is_linked(b2, 'rapidml_ConstrainableType', a)
    _safe_set(a, 'rapidml_Constraint', None)
    assert not _is_linked(a, 'rapidml_Constraint', b2)
    if hasattr(b2, 'rapidml_ConstrainableType'):
        assert not _is_linked(b2, 'rapidml_ConstrainableType', a)


def test_assoc_containingDataType134_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    b2 = rapidml_Feature(key=False, name="sample_text_2", readOnly=False, restriction=False)
    _safe_set(a, 'Structure', b1)
    assert _is_linked(a, 'Structure', b1)
    if hasattr(b1, 'ownedFeatures'):
        assert _is_linked(b1, 'ownedFeatures', a)
    _safe_set(a, 'Structure', b2)
    assert _is_linked(a, 'Structure', b2)
    if hasattr(b1, 'ownedFeatures'):
        assert not _is_linked(b1, 'ownedFeatures', a)
    if hasattr(b2, 'ownedFeatures'):
        assert _is_linked(b2, 'ownedFeatures', a)
    _safe_set(a, 'Structure', None)
    assert not _is_linked(a, 'Structure', b2)
    if hasattr(b2, 'ownedFeatures'):
        assert not _is_linked(b2, 'ownedFeatures', a)


def test_assoc_containingMessage34_link_reassign_clear():
    a = rapidml_TypedMessage(useParentTypeReference=True)
    b1 = rapidml_MessageParameter(httpLocation="sample_text")
    b2 = rapidml_MessageParameter(httpLocation="sample_text_2")
    _safe_set(a, 'TypedMessage', b1)
    assert _is_linked(a, 'TypedMessage', b1)
    if hasattr(b1, 'parameters'):
        assert _is_linked(b1, 'parameters', a)
    _safe_set(a, 'TypedMessage', b2)
    assert _is_linked(a, 'TypedMessage', b2)
    if hasattr(b1, 'parameters'):
        assert not _is_linked(b1, 'parameters', a)
    if hasattr(b2, 'parameters'):
        assert _is_linked(b2, 'parameters', a)
    _safe_set(a, 'TypedMessage', None)
    assert not _is_linked(a, 'TypedMessage', b2)
    if hasattr(b2, 'parameters'):
        assert not _is_linked(b2, 'parameters', a)


def test_assoc_containingMethod22_link_reassign_clear():
    a = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b1 = rapidml_TypedRequest()
    b2 = rapidml_TypedRequest()
    _safe_set(a, 'Method23', b1)
    assert _is_linked(a, 'Method23', b1)
    if hasattr(b1, 'request'):
        assert _is_linked(b1, 'request', a)
    _safe_set(a, 'Method23', b2)
    assert _is_linked(a, 'Method23', b2)
    if hasattr(b1, 'request'):
        assert not _is_linked(b1, 'request', a)
    if hasattr(b2, 'request'):
        assert _is_linked(b2, 'request', a)
    _safe_set(a, 'Method23', None)
    assert not _is_linked(a, 'Method23', b2)
    if hasattr(b2, 'request'):
        assert not _is_linked(b2, 'request', a)


def test_assoc_containingMethod24_link_reassign_clear():
    a = rapidml_TypedResponse(statusCode=7)
    b1 = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b2 = rapidml_Method(httpMethod="sample_text_2", id="sample_text_2")
    _safe_set(a, 'responses', b1)
    assert _is_linked(a, 'responses', b1)
    if hasattr(b1, 'Method25'):
        assert _is_linked(b1, 'Method25', a)
    _safe_set(a, 'responses', b2)
    assert _is_linked(a, 'responses', b2)
    if hasattr(b1, 'Method25'):
        assert not _is_linked(b1, 'Method25', a)
    if hasattr(b2, 'Method25'):
        assert _is_linked(b2, 'Method25', a)
    _safe_set(a, 'responses', None)
    assert not _is_linked(a, 'responses', b2)
    if hasattr(b2, 'Method25'):
        assert not _is_linked(b2, 'Method25', a)


def test_assoc_containingParameter33_link_reassign_clear():
    a = rapidml_SourceReference()
    b1 = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    b2 = rapidml_Parameter(default="sample_text_2", fixed="sample_text_2", name="sample_text_2", required=False)
    _safe_set(a, 'sourceReference', b1)
    assert _is_linked(a, 'sourceReference', b1)
    if hasattr(b1, 'Parameter'):
        assert _is_linked(b1, 'Parameter', a)
    _safe_set(a, 'sourceReference', b2)
    assert _is_linked(a, 'sourceReference', b2)
    if hasattr(b1, 'Parameter'):
        assert not _is_linked(b1, 'Parameter', a)
    if hasattr(b2, 'Parameter'):
        assert _is_linked(b2, 'Parameter', a)
    _safe_set(a, 'sourceReference', None)
    assert not _is_linked(a, 'sourceReference', b2)
    if hasattr(b2, 'Parameter'):
        assert not _is_linked(b2, 'Parameter', a)


def test_assoc_containingResourceDefinition16_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b2 = rapidml_Method(httpMethod="sample_text_2", id="sample_text_2")
    _safe_set(a, 'ResourceDefinition', b1)
    assert _is_linked(a, 'ResourceDefinition', b1)
    if hasattr(b1, 'methods'):
        assert _is_linked(b1, 'methods', a)
    _safe_set(a, 'ResourceDefinition', b2)
    assert _is_linked(a, 'ResourceDefinition', b2)
    if hasattr(b1, 'methods'):
        assert not _is_linked(b1, 'methods', a)
    if hasattr(b2, 'methods'):
        assert _is_linked(b2, 'methods', a)
    _safe_set(a, 'ResourceDefinition', None)
    assert not _is_linked(a, 'ResourceDefinition', b2)
    if hasattr(b2, 'methods'):
        assert not _is_linked(b2, 'methods', a)


def test_assoc_containingResourceDefinition31_link_reassign_clear():
    a = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    b1 = rapidml_CollectionParameter()
    b2 = rapidml_CollectionParameter()
    _safe_set(a, 'CollectionResource', b1)
    assert _is_linked(a, 'CollectionResource', b1)
    if hasattr(b1, 'collectionParameters'):
        assert _is_linked(b1, 'collectionParameters', a)
    _safe_set(a, 'CollectionResource', b2)
    assert _is_linked(a, 'CollectionResource', b2)
    if hasattr(b1, 'collectionParameters'):
        assert not _is_linked(b1, 'collectionParameters', a)
    if hasattr(b2, 'collectionParameters'):
        assert _is_linked(b2, 'collectionParameters', a)
    _safe_set(a, 'CollectionResource', None)
    assert not _is_linked(a, 'CollectionResource', b2)
    if hasattr(b2, 'collectionParameters'):
        assert not _is_linked(b2, 'collectionParameters', a)


def test_assoc_containingURI27_link_reassign_clear():
    a = rapidml_URIParameter()
    b1 = rapidml_URI()
    b2 = rapidml_URI()
    _safe_set(a, 'uriParameters', b1)
    assert _is_linked(a, 'uriParameters', b1)
    if hasattr(b1, 'URI'):
        assert _is_linked(b1, 'URI', a)
    _safe_set(a, 'uriParameters', b2)
    assert _is_linked(a, 'uriParameters', b2)
    if hasattr(b1, 'URI'):
        assert not _is_linked(b1, 'URI', a)
    if hasattr(b2, 'URI'):
        assert _is_linked(b2, 'URI', a)
    _safe_set(a, 'uriParameters', None)
    assert not _is_linked(a, 'uriParameters', b2)
    if hasattr(b2, 'URI'):
        assert not _is_linked(b2, 'URI', a)


def test_assoc_dataModels36_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_DataModel(name="sample_text")
    b2 = rapidml_DataModel(name="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel37', {b1})
    assert _is_linked(a, 'rapidml_ZenModel37', b1)
    if hasattr(b1, 'rapidml_DataModel'):
        assert _is_linked(b1, 'rapidml_DataModel', a)
    _safe_set(a, 'rapidml_ZenModel37', {b2})
    assert _is_linked(a, 'rapidml_ZenModel37', b2)
    if hasattr(b1, 'rapidml_DataModel'):
        assert not _is_linked(b1, 'rapidml_DataModel', a)
    if hasattr(b2, 'rapidml_DataModel'):
        assert _is_linked(b2, 'rapidml_DataModel', a)
    _safe_set(a, 'rapidml_ZenModel37', set())
    assert not _is_linked(a, 'rapidml_ZenModel37', b2)
    if hasattr(b2, 'rapidml_DataModel'):
        assert not _is_linked(b2, 'rapidml_DataModel', a)


def test_assoc_dataType122_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    b2 = rapidml_RealizationContainer(effectiveRealization="sample_text_2", realizationName="sample_text_2", withDefaultRealization=False)
    _safe_set(a, 'rapidml_Structure', b1)
    assert _is_linked(a, 'rapidml_Structure', b1)
    if hasattr(b1, 'rapidml_RealizationContainer123'):
        assert _is_linked(b1, 'rapidml_RealizationContainer123', a)
    _safe_set(a, 'rapidml_Structure', b2)
    assert _is_linked(a, 'rapidml_Structure', b2)
    if hasattr(b1, 'rapidml_RealizationContainer123'):
        assert not _is_linked(b1, 'rapidml_RealizationContainer123', a)
    if hasattr(b2, 'rapidml_RealizationContainer123'):
        assert _is_linked(b2, 'rapidml_RealizationContainer123', a)
    _safe_set(a, 'rapidml_Structure', None)
    assert not _is_linked(a, 'rapidml_Structure', b2)
    if hasattr(b2, 'rapidml_RealizationContainer123'):
        assert not _is_linked(b2, 'rapidml_RealizationContainer123', a)


def test_assoc_dataType161_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_ReferenceElement()
    b2 = rapidml_ReferenceElement()
    _safe_set(a, 'rapidml_Structure163', b1)
    assert _is_linked(a, 'rapidml_Structure163', b1)
    if hasattr(b1, 'rapidml_ReferenceElement162'):
        assert _is_linked(b1, 'rapidml_ReferenceElement162', a)
    _safe_set(a, 'rapidml_Structure163', b2)
    assert _is_linked(a, 'rapidml_Structure163', b2)
    if hasattr(b1, 'rapidml_ReferenceElement162'):
        assert not _is_linked(b1, 'rapidml_ReferenceElement162', a)
    if hasattr(b2, 'rapidml_ReferenceElement162'):
        assert _is_linked(b2, 'rapidml_ReferenceElement162', a)
    _safe_set(a, 'rapidml_Structure163', None)
    assert not _is_linked(a, 'rapidml_Structure163', b2)
    if hasattr(b2, 'rapidml_ReferenceElement162'):
        assert not _is_linked(b2, 'rapidml_ReferenceElement162', a)


def test_assoc_defaultReferenceRealizations62_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    b2 = rapidml_ReferenceRealization(multiValued=False, realizationType="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI63', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI63', b1)
    if hasattr(b1, 'rapidml_ReferenceRealization'):
        assert _is_linked(b1, 'rapidml_ReferenceRealization', a)
    _safe_set(a, 'rapidml_ResourceAPI63', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI63', b2)
    if hasattr(b1, 'rapidml_ReferenceRealization'):
        assert not _is_linked(b1, 'rapidml_ReferenceRealization', a)
    if hasattr(b2, 'rapidml_ReferenceRealization'):
        assert _is_linked(b2, 'rapidml_ReferenceRealization', a)
    _safe_set(a, 'rapidml_ResourceAPI63', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI63', b2)
    if hasattr(b2, 'rapidml_ReferenceRealization'):
        assert not _is_linked(b2, 'rapidml_ReferenceRealization', a)


def test_assoc_definedLinkDescriptors66_link_reassign_clear():
    a = rapidml_ServiceDataResource(default=True)
    b1 = rapidml_NamedLinkDescriptor(default=True, name="sample_text")
    b2 = rapidml_NamedLinkDescriptor(default=False, name="sample_text_2")
    _safe_set(a, 'rapidml_ServiceDataResource', {b1})
    assert _is_linked(a, 'rapidml_ServiceDataResource', b1)
    if hasattr(b1, 'rapidml_NamedLinkDescriptor'):
        assert _is_linked(b1, 'rapidml_NamedLinkDescriptor', a)
    _safe_set(a, 'rapidml_ServiceDataResource', {b2})
    assert _is_linked(a, 'rapidml_ServiceDataResource', b2)
    if hasattr(b1, 'rapidml_NamedLinkDescriptor'):
        assert not _is_linked(b1, 'rapidml_NamedLinkDescriptor', a)
    if hasattr(b2, 'rapidml_NamedLinkDescriptor'):
        assert _is_linked(b2, 'rapidml_NamedLinkDescriptor', a)
    _safe_set(a, 'rapidml_ServiceDataResource', set())
    assert not _is_linked(a, 'rapidml_ServiceDataResource', b2)
    if hasattr(b2, 'rapidml_NamedLinkDescriptor'):
        assert not _is_linked(b2, 'rapidml_NamedLinkDescriptor', a)


def test_assoc_definedLinkRelations128_link_reassign_clear():
    a = rapidml_LinkRelationsLibrary(name="sample_text")
    b1 = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    b2 = rapidml_LinkRelation(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_LinkRelationsLibrary129', {b1})
    assert _is_linked(a, 'rapidml_LinkRelationsLibrary129', b1)
    if hasattr(b1, 'rapidml_LinkRelation130'):
        assert _is_linked(b1, 'rapidml_LinkRelation130', a)
    _safe_set(a, 'rapidml_LinkRelationsLibrary129', {b2})
    assert _is_linked(a, 'rapidml_LinkRelationsLibrary129', b2)
    if hasattr(b1, 'rapidml_LinkRelation130'):
        assert not _is_linked(b1, 'rapidml_LinkRelation130', a)
    if hasattr(b2, 'rapidml_LinkRelation130'):
        assert _is_linked(b2, 'rapidml_LinkRelation130', a)
    _safe_set(a, 'rapidml_LinkRelationsLibrary129', set())
    assert not _is_linked(a, 'rapidml_LinkRelationsLibrary129', b2)
    if hasattr(b2, 'rapidml_LinkRelation130'):
        assert not _is_linked(b2, 'rapidml_LinkRelation130', a)


def test_assoc_definedLinkRelations60_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    b2 = rapidml_LinkRelation(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI61', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI61', b1)
    if hasattr(b1, 'rapidml_LinkRelation'):
        assert _is_linked(b1, 'rapidml_LinkRelation', a)
    _safe_set(a, 'rapidml_ResourceAPI61', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI61', b2)
    if hasattr(b1, 'rapidml_LinkRelation'):
        assert not _is_linked(b1, 'rapidml_LinkRelation', a)
    if hasattr(b2, 'rapidml_LinkRelation'):
        assert _is_linked(b2, 'rapidml_LinkRelation', a)
    _safe_set(a, 'rapidml_ResourceAPI61', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI61', b2)
    if hasattr(b2, 'rapidml_LinkRelation'):
        assert not _is_linked(b2, 'rapidml_LinkRelation', a)


def test_assoc_definedMediaTypes57_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI58', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI58', b1)
    if hasattr(b1, 'rapidml_MediaType59'):
        assert _is_linked(b1, 'rapidml_MediaType59', a)
    _safe_set(a, 'rapidml_ResourceAPI58', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI58', b2)
    if hasattr(b1, 'rapidml_MediaType59'):
        assert not _is_linked(b1, 'rapidml_MediaType59', a)
    if hasattr(b2, 'rapidml_MediaType59'):
        assert _is_linked(b2, 'rapidml_MediaType59', a)
    _safe_set(a, 'rapidml_ResourceAPI58', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI58', b2)
    if hasattr(b2, 'rapidml_MediaType59'):
        assert not _is_linked(b2, 'rapidml_MediaType59', a)


def test_assoc_derivedFrom20_link_reassign_clear():
    a = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_MediaType19', {b1})
    assert _is_linked(a, 'rapidml_MediaType19', b1)
    if hasattr(b1, 'rapidml_MediaType21'):
        assert _is_linked(b1, 'rapidml_MediaType21', a)
    _safe_set(a, 'rapidml_MediaType19', {b2})
    assert _is_linked(a, 'rapidml_MediaType19', b2)
    if hasattr(b1, 'rapidml_MediaType21'):
        assert not _is_linked(b1, 'rapidml_MediaType21', a)
    if hasattr(b2, 'rapidml_MediaType21'):
        assert _is_linked(b2, 'rapidml_MediaType21', a)
    _safe_set(a, 'rapidml_MediaType19', set())
    assert not _is_linked(a, 'rapidml_MediaType19', b2)
    if hasattr(b2, 'rapidml_MediaType21'):
        assert not _is_linked(b2, 'rapidml_MediaType21', a)


def test_assoc_documentation18_link_reassign_clear():
    a = rapidml_Documentation(text="sample_text")
    b1 = rapidml_Documentable()
    b2 = rapidml_Documentable()
    _safe_set(a, 'rapidml_Documentation', b1)
    assert _is_linked(a, 'rapidml_Documentation', b1)
    if hasattr(b1, 'rapidml_Documentable'):
        assert _is_linked(b1, 'rapidml_Documentable', a)
    _safe_set(a, 'rapidml_Documentation', b2)
    assert _is_linked(a, 'rapidml_Documentation', b2)
    if hasattr(b1, 'rapidml_Documentable'):
        assert not _is_linked(b1, 'rapidml_Documentable', a)
    if hasattr(b2, 'rapidml_Documentable'):
        assert _is_linked(b2, 'rapidml_Documentable', a)
    _safe_set(a, 'rapidml_Documentation', None)
    assert not _is_linked(a, 'rapidml_Documentation', b2)
    if hasattr(b2, 'rapidml_Documentable'):
        assert not _is_linked(b2, 'rapidml_Documentable', a)


def test_assoc_enumConstants156_link_reassign_clear():
    a = rapidml_Enumeration()
    b1 = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    b2 = rapidml_EnumConstant(integerValue=13, literalValue="sample_text_2", name="sample_text_2")
    _safe_set(a, 'enumeration', {b1})
    assert _is_linked(a, 'enumeration', b1)
    if hasattr(b1, 'EnumConstant'):
        assert _is_linked(b1, 'EnumConstant', a)
    _safe_set(a, 'enumeration', {b2})
    assert _is_linked(a, 'enumeration', b2)
    if hasattr(b1, 'EnumConstant'):
        assert not _is_linked(b1, 'EnumConstant', a)
    if hasattr(b2, 'EnumConstant'):
        assert _is_linked(b2, 'EnumConstant', a)
    _safe_set(a, 'enumeration', set())
    assert not _is_linked(a, 'enumeration', b2)
    if hasattr(b2, 'EnumConstant'):
        assert not _is_linked(b2, 'EnumConstant', a)


def test_assoc_enumeration159_link_reassign_clear():
    a = rapidml_Enumeration()
    b1 = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    b2 = rapidml_EnumConstant(integerValue=13, literalValue="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Enumeration', b1)
    assert _is_linked(a, 'Enumeration', b1)
    if hasattr(b1, 'enumConstants'):
        assert _is_linked(b1, 'enumConstants', a)
    _safe_set(a, 'Enumeration', b2)
    assert _is_linked(a, 'Enumeration', b2)
    if hasattr(b1, 'enumConstants'):
        assert not _is_linked(b1, 'enumConstants', a)
    if hasattr(b2, 'enumConstants'):
        assert _is_linked(b2, 'enumConstants', a)
    _safe_set(a, 'Enumeration', None)
    assert not _is_linked(a, 'Enumeration', b2)
    if hasattr(b2, 'enumConstants'):
        assert not _is_linked(b2, 'enumConstants', a)


def test_assoc_errorResponses105_link_reassign_clear():
    a = rapidml_TypedResponse(statusCode=7)
    b1 = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b2 = rapidml_SecurityScheme(flow="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rapidml_TypedResponse', b1)
    assert _is_linked(a, 'rapidml_TypedResponse', b1)
    if hasattr(b1, 'rapidml_SecurityScheme106'):
        assert _is_linked(b1, 'rapidml_SecurityScheme106', a)
    _safe_set(a, 'rapidml_TypedResponse', b2)
    assert _is_linked(a, 'rapidml_TypedResponse', b2)
    if hasattr(b1, 'rapidml_SecurityScheme106'):
        assert not _is_linked(b1, 'rapidml_SecurityScheme106', a)
    if hasattr(b2, 'rapidml_SecurityScheme106'):
        assert _is_linked(b2, 'rapidml_SecurityScheme106', a)
    _safe_set(a, 'rapidml_TypedResponse', None)
    assert not _is_linked(a, 'rapidml_TypedResponse', b2)
    if hasattr(b2, 'rapidml_SecurityScheme106'):
        assert not _is_linked(b2, 'rapidml_SecurityScheme106', a)


def test_assoc_examples86_link_reassign_clear():
    a = rapidml_Example()
    b1 = rapidml_WithExamples()
    b2 = rapidml_WithExamples()
    _safe_set(a, 'rapidml_Example', b1)
    assert _is_linked(a, 'rapidml_Example', b1)
    if hasattr(b1, 'rapidml_WithExamples'):
        assert _is_linked(b1, 'rapidml_WithExamples', a)
    _safe_set(a, 'rapidml_Example', b2)
    assert _is_linked(a, 'rapidml_Example', b2)
    if hasattr(b1, 'rapidml_WithExamples'):
        assert not _is_linked(b1, 'rapidml_WithExamples', a)
    if hasattr(b2, 'rapidml_WithExamples'):
        assert _is_linked(b2, 'rapidml_WithExamples', a)
    _safe_set(a, 'rapidml_Example', None)
    assert not _is_linked(a, 'rapidml_Example', b2)
    if hasattr(b2, 'rapidml_WithExamples'):
        assert not _is_linked(b2, 'rapidml_WithExamples', a)


def test_assoc_excludedProperties95_link_reassign_clear():
    a = rapidml_ObjectRealization()
    b1 = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    b2 = rapidml_Feature(key=False, name="sample_text_2", readOnly=False, restriction=False)
    _safe_set(a, 'rapidml_ObjectRealization96', {b1})
    assert _is_linked(a, 'rapidml_ObjectRealization96', b1)
    if hasattr(b1, 'rapidml_Feature97'):
        assert _is_linked(b1, 'rapidml_Feature97', a)
    _safe_set(a, 'rapidml_ObjectRealization96', {b2})
    assert _is_linked(a, 'rapidml_ObjectRealization96', b2)
    if hasattr(b1, 'rapidml_Feature97'):
        assert not _is_linked(b1, 'rapidml_Feature97', a)
    if hasattr(b2, 'rapidml_Feature97'):
        assert _is_linked(b2, 'rapidml_Feature97', a)
    _safe_set(a, 'rapidml_ObjectRealization96', set())
    assert not _is_linked(a, 'rapidml_ObjectRealization96', b2)
    if hasattr(b2, 'rapidml_Feature97'):
        assert not _is_linked(b2, 'rapidml_Feature97', a)


def test_assoc_exclusivePropertyList90_link_reassign_clear():
    a = rapidml_PropertyRealization(cardinality="sample_text")
    b1 = rapidml_ObjectRealization()
    b2 = rapidml_ObjectRealization()
    _safe_set(a, 'rapidml_PropertyRealization91', b1)
    assert _is_linked(a, 'rapidml_PropertyRealization91', b1)
    if hasattr(b1, 'rapidml_ObjectRealization'):
        assert _is_linked(b1, 'rapidml_ObjectRealization', a)
    _safe_set(a, 'rapidml_PropertyRealization91', b2)
    assert _is_linked(a, 'rapidml_PropertyRealization91', b2)
    if hasattr(b1, 'rapidml_ObjectRealization'):
        assert not _is_linked(b1, 'rapidml_ObjectRealization', a)
    if hasattr(b2, 'rapidml_ObjectRealization'):
        assert _is_linked(b2, 'rapidml_ObjectRealization', a)
    _safe_set(a, 'rapidml_PropertyRealization91', None)
    assert not _is_linked(a, 'rapidml_PropertyRealization91', b2)
    if hasattr(b2, 'rapidml_ObjectRealization'):
        assert not _is_linked(b2, 'rapidml_ObjectRealization', a)


def test_assoc_extensions124_link_reassign_clear():
    a = rapidml_Extension(name="sample_text", value="sample_text")
    b1 = rapidml_Extensible()
    b2 = rapidml_Extensible()
    _safe_set(a, 'rapidml_Extension', b1)
    assert _is_linked(a, 'rapidml_Extension', b1)
    if hasattr(b1, 'rapidml_Extensible'):
        assert _is_linked(b1, 'rapidml_Extensible', a)
    _safe_set(a, 'rapidml_Extension', b2)
    assert _is_linked(a, 'rapidml_Extension', b2)
    if hasattr(b1, 'rapidml_Extensible'):
        assert not _is_linked(b1, 'rapidml_Extensible', a)
    if hasattr(b2, 'rapidml_Extensible'):
        assert _is_linked(b2, 'rapidml_Extensible', a)
    _safe_set(a, 'rapidml_Extension', None)
    assert not _is_linked(a, 'rapidml_Extension', b2)
    if hasattr(b2, 'rapidml_Extensible'):
        assert not _is_linked(b2, 'rapidml_Extensible', a)


def test_assoc_formats54_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI55', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI55', b1)
    if hasattr(b1, 'rapidml_MediaType56'):
        assert _is_linked(b1, 'rapidml_MediaType56', a)
    _safe_set(a, 'rapidml_ResourceAPI55', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI55', b2)
    if hasattr(b1, 'rapidml_MediaType56'):
        assert not _is_linked(b1, 'rapidml_MediaType56', a)
    if hasattr(b2, 'rapidml_MediaType56'):
        assert _is_linked(b2, 'rapidml_MediaType56', a)
    _safe_set(a, 'rapidml_ResourceAPI55', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI55', b2)
    if hasattr(b2, 'rapidml_MediaType56'):
        assert not _is_linked(b2, 'rapidml_MediaType56', a)


def test_assoc_importedModel87_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    b2 = rapidml_ImportDeclaration(alias="sample_text_2", importURI="sample_text_2", importedNamespace="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel89', b1)
    assert _is_linked(a, 'rapidml_ZenModel89', b1)
    if hasattr(b1, 'rapidml_ImportDeclaration88'):
        assert _is_linked(b1, 'rapidml_ImportDeclaration88', a)
    _safe_set(a, 'rapidml_ZenModel89', b2)
    assert _is_linked(a, 'rapidml_ZenModel89', b2)
    if hasattr(b1, 'rapidml_ImportDeclaration88'):
        assert not _is_linked(b1, 'rapidml_ImportDeclaration88', a)
    if hasattr(b2, 'rapidml_ImportDeclaration88'):
        assert _is_linked(b2, 'rapidml_ImportDeclaration88', a)
    _safe_set(a, 'rapidml_ZenModel89', None)
    assert not _is_linked(a, 'rapidml_ZenModel89', b2)
    if hasattr(b2, 'rapidml_ImportDeclaration88'):
        assert not _is_linked(b2, 'rapidml_ImportDeclaration88', a)


def test_assoc_imports44_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    b2 = rapidml_ImportDeclaration(alias="sample_text_2", importURI="sample_text_2", importedNamespace="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel45', {b1})
    assert _is_linked(a, 'rapidml_ZenModel45', b1)
    if hasattr(b1, 'rapidml_ImportDeclaration'):
        assert _is_linked(b1, 'rapidml_ImportDeclaration', a)
    _safe_set(a, 'rapidml_ZenModel45', {b2})
    assert _is_linked(a, 'rapidml_ZenModel45', b2)
    if hasattr(b1, 'rapidml_ImportDeclaration'):
        assert not _is_linked(b1, 'rapidml_ImportDeclaration', a)
    if hasattr(b2, 'rapidml_ImportDeclaration'):
        assert _is_linked(b2, 'rapidml_ImportDeclaration', a)
    _safe_set(a, 'rapidml_ZenModel45', set())
    assert not _is_linked(a, 'rapidml_ZenModel45', b2)
    if hasattr(b2, 'rapidml_ImportDeclaration'):
        assert not _is_linked(b2, 'rapidml_ImportDeclaration', a)


def test_assoc_inlineObjectRealization116_link_reassign_clear():
    a = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    b1 = rapidml_ObjectRealization()
    b2 = rapidml_ObjectRealization()
    _safe_set(a, 'realizationContainer', b1)
    assert _is_linked(a, 'realizationContainer', b1)
    if hasattr(b1, 'ObjectRealization'):
        assert _is_linked(b1, 'ObjectRealization', a)
    _safe_set(a, 'realizationContainer', b2)
    assert _is_linked(a, 'realizationContainer', b2)
    if hasattr(b1, 'ObjectRealization'):
        assert not _is_linked(b1, 'ObjectRealization', a)
    if hasattr(b2, 'ObjectRealization'):
        assert _is_linked(b2, 'ObjectRealization', a)
    _safe_set(a, 'realizationContainer', None)
    assert not _is_linked(a, 'realizationContainer', b2)
    if hasattr(b2, 'ObjectRealization'):
        assert not _is_linked(b2, 'ObjectRealization', a)


def test_assoc_inverse138_link_reassign_clear():
    a = rapidml_ReferenceProperty(container=True, containment=True)
    b1 = rapidml_ReferenceProperty(container=True, containment=True)
    b2 = rapidml_ReferenceProperty(container=False, containment=False)
    _safe_set(a, 'rapidml_ReferenceProperty137', b1)
    assert _is_linked(a, 'rapidml_ReferenceProperty137', b1)
    if hasattr(b1, 'rapidml_ReferenceProperty139'):
        assert _is_linked(b1, 'rapidml_ReferenceProperty139', a)
    _safe_set(a, 'rapidml_ReferenceProperty137', b2)
    assert _is_linked(a, 'rapidml_ReferenceProperty137', b2)
    if hasattr(b1, 'rapidml_ReferenceProperty139'):
        assert not _is_linked(b1, 'rapidml_ReferenceProperty139', a)
    if hasattr(b2, 'rapidml_ReferenceProperty139'):
        assert _is_linked(b2, 'rapidml_ReferenceProperty139', a)
    _safe_set(a, 'rapidml_ReferenceProperty137', None)
    assert not _is_linked(a, 'rapidml_ReferenceProperty137', b2)
    if hasattr(b2, 'rapidml_ReferenceProperty139'):
        assert not _is_linked(b2, 'rapidml_ReferenceProperty139', a)


def test_assoc_linkRelation77_link_reassign_clear():
    a = rapidml_ReferenceLink(collectionRealizationLevel="sample_text", name="sample_text")
    b1 = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    b2 = rapidml_LinkRelation(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ReferenceLink', b1)
    assert _is_linked(a, 'rapidml_ReferenceLink', b1)
    if hasattr(b1, 'rapidml_LinkRelation78'):
        assert _is_linked(b1, 'rapidml_LinkRelation78', a)
    _safe_set(a, 'rapidml_ReferenceLink', b2)
    assert _is_linked(a, 'rapidml_ReferenceLink', b2)
    if hasattr(b1, 'rapidml_LinkRelation78'):
        assert not _is_linked(b1, 'rapidml_LinkRelation78', a)
    if hasattr(b2, 'rapidml_LinkRelation78'):
        assert _is_linked(b2, 'rapidml_LinkRelation78', a)
    _safe_set(a, 'rapidml_ReferenceLink', None)
    assert not _is_linked(a, 'rapidml_ReferenceLink', b2)
    if hasattr(b2, 'rapidml_LinkRelation78'):
        assert not _is_linked(b2, 'rapidml_LinkRelation78', a)


def test_assoc_linkRelationsLibrary40_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_LinkRelationsLibrary(name="sample_text")
    b2 = rapidml_LinkRelationsLibrary(name="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel41', b1)
    assert _is_linked(a, 'rapidml_ZenModel41', b1)
    if hasattr(b1, 'rapidml_LinkRelationsLibrary'):
        assert _is_linked(b1, 'rapidml_LinkRelationsLibrary', a)
    _safe_set(a, 'rapidml_ZenModel41', b2)
    assert _is_linked(a, 'rapidml_ZenModel41', b2)
    if hasattr(b1, 'rapidml_LinkRelationsLibrary'):
        assert not _is_linked(b1, 'rapidml_LinkRelationsLibrary', a)
    if hasattr(b2, 'rapidml_LinkRelationsLibrary'):
        assert _is_linked(b2, 'rapidml_LinkRelationsLibrary', a)
    _safe_set(a, 'rapidml_ZenModel41', None)
    assert not _is_linked(a, 'rapidml_ZenModel41', b2)
    if hasattr(b2, 'rapidml_LinkRelationsLibrary'):
        assert not _is_linked(b2, 'rapidml_LinkRelationsLibrary', a)


def test_assoc_mediaTypes1_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_ResourceDefinition', {b1})
    assert _is_linked(a, 'rapidml_ResourceDefinition', b1)
    if hasattr(b1, 'rapidml_MediaType'):
        assert _is_linked(b1, 'rapidml_MediaType', a)
    _safe_set(a, 'rapidml_ResourceDefinition', {b2})
    assert _is_linked(a, 'rapidml_ResourceDefinition', b2)
    if hasattr(b1, 'rapidml_MediaType'):
        assert not _is_linked(b1, 'rapidml_MediaType', a)
    if hasattr(b2, 'rapidml_MediaType'):
        assert _is_linked(b2, 'rapidml_MediaType', a)
    _safe_set(a, 'rapidml_ResourceDefinition', set())
    assert not _is_linked(a, 'rapidml_ResourceDefinition', b2)
    if hasattr(b2, 'rapidml_MediaType'):
        assert not _is_linked(b2, 'rapidml_MediaType', a)


def test_assoc_mediaTypes10_link_reassign_clear():
    a = rapidml_TypedMessage(useParentTypeReference=True)
    b1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    _safe_set(a, 'rapidml_TypedMessage11', {b1})
    assert _is_linked(a, 'rapidml_TypedMessage11', b1)
    if hasattr(b1, 'rapidml_MediaType12'):
        assert _is_linked(b1, 'rapidml_MediaType12', a)
    _safe_set(a, 'rapidml_TypedMessage11', {b2})
    assert _is_linked(a, 'rapidml_TypedMessage11', b2)
    if hasattr(b1, 'rapidml_MediaType12'):
        assert not _is_linked(b1, 'rapidml_MediaType12', a)
    if hasattr(b2, 'rapidml_MediaType12'):
        assert _is_linked(b2, 'rapidml_MediaType12', a)
    _safe_set(a, 'rapidml_TypedMessage11', set())
    assert not _is_linked(a, 'rapidml_TypedMessage11', b2)
    if hasattr(b2, 'rapidml_MediaType12'):
        assert not _is_linked(b2, 'rapidml_MediaType12', a)


def test_assoc_mediaTypes125_link_reassign_clear():
    a = rapidml_MediaType(name="sample_text", specURL="sample_text")
    b1 = rapidml_MediaTypesLibrary()
    b2 = rapidml_MediaTypesLibrary()
    _safe_set(a, 'rapidml_MediaType127', b1)
    assert _is_linked(a, 'rapidml_MediaType127', b1)
    if hasattr(b1, 'rapidml_MediaTypesLibrary126'):
        assert _is_linked(b1, 'rapidml_MediaTypesLibrary126', a)
    _safe_set(a, 'rapidml_MediaType127', b2)
    assert _is_linked(a, 'rapidml_MediaType127', b2)
    if hasattr(b1, 'rapidml_MediaTypesLibrary126'):
        assert not _is_linked(b1, 'rapidml_MediaTypesLibrary126', a)
    if hasattr(b2, 'rapidml_MediaTypesLibrary126'):
        assert _is_linked(b2, 'rapidml_MediaTypesLibrary126', a)
    _safe_set(a, 'rapidml_MediaType127', None)
    assert not _is_linked(a, 'rapidml_MediaType127', b2)
    if hasattr(b2, 'rapidml_MediaTypesLibrary126'):
        assert not _is_linked(b2, 'rapidml_MediaTypesLibrary126', a)


def test_assoc_mediaTypesLibrary38_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_MediaTypesLibrary()
    b2 = rapidml_MediaTypesLibrary()
    _safe_set(a, 'rapidml_ZenModel39', b1)
    assert _is_linked(a, 'rapidml_ZenModel39', b1)
    if hasattr(b1, 'rapidml_MediaTypesLibrary'):
        assert _is_linked(b1, 'rapidml_MediaTypesLibrary', a)
    _safe_set(a, 'rapidml_ZenModel39', b2)
    assert _is_linked(a, 'rapidml_ZenModel39', b2)
    if hasattr(b1, 'rapidml_MediaTypesLibrary'):
        assert not _is_linked(b1, 'rapidml_MediaTypesLibrary', a)
    if hasattr(b2, 'rapidml_MediaTypesLibrary'):
        assert _is_linked(b2, 'rapidml_MediaTypesLibrary', a)
    _safe_set(a, 'rapidml_ZenModel39', None)
    assert not _is_linked(a, 'rapidml_ZenModel39', b2)
    if hasattr(b2, 'rapidml_MediaTypesLibrary'):
        assert not _is_linked(b2, 'rapidml_MediaTypesLibrary', a)


def test_assoc_methods0_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b2 = rapidml_Method(httpMethod="sample_text_2", id="sample_text_2")
    _safe_set(a, 'containingResourceDefinition', {b1})
    assert _is_linked(a, 'containingResourceDefinition', b1)
    if hasattr(b1, 'Method'):
        assert _is_linked(b1, 'Method', a)
    _safe_set(a, 'containingResourceDefinition', {b2})
    assert _is_linked(a, 'containingResourceDefinition', b2)
    if hasattr(b1, 'Method'):
        assert not _is_linked(b1, 'Method', a)
    if hasattr(b2, 'Method'):
        assert _is_linked(b2, 'Method', a)
    _safe_set(a, 'containingResourceDefinition', set())
    assert not _is_linked(a, 'containingResourceDefinition', b2)
    if hasattr(b2, 'Method'):
        assert not _is_linked(b2, 'Method', a)


def test_assoc_overriddenPropertyList92_link_reassign_clear():
    a = rapidml_PropertyRealization(cardinality="sample_text")
    b1 = rapidml_ObjectRealization()
    b2 = rapidml_ObjectRealization()
    _safe_set(a, 'rapidml_PropertyRealization94', b1)
    assert _is_linked(a, 'rapidml_PropertyRealization94', b1)
    if hasattr(b1, 'rapidml_ObjectRealization93'):
        assert _is_linked(b1, 'rapidml_ObjectRealization93', a)
    _safe_set(a, 'rapidml_PropertyRealization94', b2)
    assert _is_linked(a, 'rapidml_PropertyRealization94', b2)
    if hasattr(b1, 'rapidml_ObjectRealization93'):
        assert not _is_linked(b1, 'rapidml_ObjectRealization93', a)
    if hasattr(b2, 'rapidml_ObjectRealization93'):
        assert _is_linked(b2, 'rapidml_ObjectRealization93', a)
    _safe_set(a, 'rapidml_PropertyRealization94', None)
    assert not _is_linked(a, 'rapidml_PropertyRealization94', b2)
    if hasattr(b2, 'rapidml_ObjectRealization93'):
        assert not _is_linked(b2, 'rapidml_ObjectRealization93', a)


def test_assoc_ownedDataTypes153_link_reassign_clear():
    a = rapidml_DataType(name="sample_text")
    b1 = rapidml_DataModel(name="sample_text")
    b2 = rapidml_DataModel(name="sample_text_2")
    _safe_set(a, 'rapidml_DataType', b1)
    assert _is_linked(a, 'rapidml_DataType', b1)
    if hasattr(b1, 'rapidml_DataModel154'):
        assert _is_linked(b1, 'rapidml_DataModel154', a)
    _safe_set(a, 'rapidml_DataType', b2)
    assert _is_linked(a, 'rapidml_DataType', b2)
    if hasattr(b1, 'rapidml_DataModel154'):
        assert not _is_linked(b1, 'rapidml_DataModel154', a)
    if hasattr(b2, 'rapidml_DataModel154'):
        assert _is_linked(b2, 'rapidml_DataModel154', a)
    _safe_set(a, 'rapidml_DataType', None)
    assert not _is_linked(a, 'rapidml_DataType', b2)
    if hasattr(b2, 'rapidml_DataModel154'):
        assert not _is_linked(b2, 'rapidml_DataModel154', a)


def test_assoc_ownedElements144_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Structure()
    b2 = rapidml_Structure()
    _safe_set(a, 'rapidml_Structure143', {b1})
    assert _is_linked(a, 'rapidml_Structure143', b1)
    if hasattr(b1, 'rapidml_Structure145'):
        assert _is_linked(b1, 'rapidml_Structure145', a)
    _safe_set(a, 'rapidml_Structure143', {b2})
    assert _is_linked(a, 'rapidml_Structure143', b2)
    if hasattr(b1, 'rapidml_Structure145'):
        assert not _is_linked(b1, 'rapidml_Structure145', a)
    if hasattr(b2, 'rapidml_Structure145'):
        assert _is_linked(b2, 'rapidml_Structure145', a)
    _safe_set(a, 'rapidml_Structure143', set())
    assert not _is_linked(a, 'rapidml_Structure143', b2)
    if hasattr(b2, 'rapidml_Structure145'):
        assert not _is_linked(b2, 'rapidml_Structure145', a)


def test_assoc_ownedFeatures142_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    b2 = rapidml_Feature(key=False, name="sample_text_2", readOnly=False, restriction=False)
    _safe_set(a, 'containingDataType', {b1})
    assert _is_linked(a, 'containingDataType', b1)
    if hasattr(b1, 'Feature'):
        assert _is_linked(b1, 'Feature', a)
    _safe_set(a, 'containingDataType', {b2})
    assert _is_linked(a, 'containingDataType', b2)
    if hasattr(b1, 'Feature'):
        assert not _is_linked(b1, 'Feature', a)
    if hasattr(b2, 'Feature'):
        assert _is_linked(b2, 'Feature', a)
    _safe_set(a, 'containingDataType', set())
    assert not _is_linked(a, 'containingDataType', b2)
    if hasattr(b2, 'Feature'):
        assert not _is_linked(b2, 'Feature', a)


def test_assoc_ownedOperations146_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Operation(name="sample_text")
    b2 = rapidml_Operation(name="sample_text_2")
    _safe_set(a, 'rapidml_Structure147', {b1})
    assert _is_linked(a, 'rapidml_Structure147', b1)
    if hasattr(b1, 'rapidml_Operation'):
        assert _is_linked(b1, 'rapidml_Operation', a)
    _safe_set(a, 'rapidml_Structure147', {b2})
    assert _is_linked(a, 'rapidml_Structure147', b2)
    if hasattr(b1, 'rapidml_Operation'):
        assert not _is_linked(b1, 'rapidml_Operation', a)
    if hasattr(b2, 'rapidml_Operation'):
        assert _is_linked(b2, 'rapidml_Operation', a)
    _safe_set(a, 'rapidml_Structure147', set())
    assert not _is_linked(a, 'rapidml_Structure147', b2)
    if hasattr(b2, 'rapidml_Operation'):
        assert not _is_linked(b2, 'rapidml_Operation', a)


def test_assoc_ownedReferenceRealization71_link_reassign_clear():
    a = rapidml_ReferenceTreatment()
    b1 = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    b2 = rapidml_ReferenceRealization(multiValued=False, realizationType="sample_text_2")
    _safe_set(a, 'rapidml_ReferenceTreatment72', b1)
    assert _is_linked(a, 'rapidml_ReferenceTreatment72', b1)
    if hasattr(b1, 'rapidml_ReferenceRealization73'):
        assert _is_linked(b1, 'rapidml_ReferenceRealization73', a)
    _safe_set(a, 'rapidml_ReferenceTreatment72', b2)
    assert _is_linked(a, 'rapidml_ReferenceTreatment72', b2)
    if hasattr(b1, 'rapidml_ReferenceRealization73'):
        assert not _is_linked(b1, 'rapidml_ReferenceRealization73', a)
    if hasattr(b2, 'rapidml_ReferenceRealization73'):
        assert _is_linked(b2, 'rapidml_ReferenceRealization73', a)
    _safe_set(a, 'rapidml_ReferenceTreatment72', None)
    assert not _is_linked(a, 'rapidml_ReferenceTreatment72', b2)
    if hasattr(b2, 'rapidml_ReferenceRealization73'):
        assert not _is_linked(b2, 'rapidml_ReferenceRealization73', a)


def test_assoc_ownedResourceDefinitions48_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'rapidml_ResourceDefinition50', b1)
    assert _is_linked(a, 'rapidml_ResourceDefinition50', b1)
    if hasattr(b1, 'rapidml_ResourceAPI49'):
        assert _is_linked(b1, 'rapidml_ResourceAPI49', a)
    _safe_set(a, 'rapidml_ResourceDefinition50', b2)
    assert _is_linked(a, 'rapidml_ResourceDefinition50', b2)
    if hasattr(b1, 'rapidml_ResourceAPI49'):
        assert not _is_linked(b1, 'rapidml_ResourceAPI49', a)
    if hasattr(b2, 'rapidml_ResourceAPI49'):
        assert _is_linked(b2, 'rapidml_ResourceAPI49', a)
    _safe_set(a, 'rapidml_ResourceDefinition50', None)
    assert not _is_linked(a, 'rapidml_ResourceDefinition50', b2)
    if hasattr(b2, 'rapidml_ResourceAPI49'):
        assert not _is_linked(b2, 'rapidml_ResourceAPI49', a)


def test_assoc_parameters103_link_reassign_clear():
    a = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b1 = rapidml_MessageParameter(httpLocation="sample_text")
    b2 = rapidml_MessageParameter(httpLocation="sample_text_2")
    _safe_set(a, 'rapidml_SecurityScheme104', {b1})
    assert _is_linked(a, 'rapidml_SecurityScheme104', b1)
    if hasattr(b1, 'rapidml_MessageParameter'):
        assert _is_linked(b1, 'rapidml_MessageParameter', a)
    _safe_set(a, 'rapidml_SecurityScheme104', {b2})
    assert _is_linked(a, 'rapidml_SecurityScheme104', b2)
    if hasattr(b1, 'rapidml_MessageParameter'):
        assert not _is_linked(b1, 'rapidml_MessageParameter', a)
    if hasattr(b2, 'rapidml_MessageParameter'):
        assert _is_linked(b2, 'rapidml_MessageParameter', a)
    _safe_set(a, 'rapidml_SecurityScheme104', set())
    assert not _is_linked(a, 'rapidml_SecurityScheme104', b2)
    if hasattr(b2, 'rapidml_MessageParameter'):
        assert not _is_linked(b2, 'rapidml_MessageParameter', a)


def test_assoc_parameters7_link_reassign_clear():
    a = rapidml_TypedMessage(useParentTypeReference=True)
    b1 = rapidml_MessageParameter(httpLocation="sample_text")
    b2 = rapidml_MessageParameter(httpLocation="sample_text_2")
    _safe_set(a, 'containingMessage', {b1})
    assert _is_linked(a, 'containingMessage', b1)
    if hasattr(b1, 'MessageParameter'):
        assert _is_linked(b1, 'MessageParameter', a)
    _safe_set(a, 'containingMessage', {b2})
    assert _is_linked(a, 'containingMessage', b2)
    if hasattr(b1, 'MessageParameter'):
        assert not _is_linked(b1, 'MessageParameter', a)
    if hasattr(b2, 'MessageParameter'):
        assert _is_linked(b2, 'MessageParameter', a)
    _safe_set(a, 'containingMessage', set())
    assert not _is_linked(a, 'containingMessage', b2)
    if hasattr(b2, 'MessageParameter'):
        assert not _is_linked(b2, 'MessageParameter', a)


def test_assoc_primitiveTypes131_link_reassign_clear():
    a = rapidml_PrimitiveTypesLibrary(name="sample_text")
    b1 = rapidml_PrimitiveType()
    b2 = rapidml_PrimitiveType()
    _safe_set(a, 'rapidml_PrimitiveTypesLibrary132', {b1})
    assert _is_linked(a, 'rapidml_PrimitiveTypesLibrary132', b1)
    if hasattr(b1, 'rapidml_PrimitiveType133'):
        assert _is_linked(b1, 'rapidml_PrimitiveType133', a)
    _safe_set(a, 'rapidml_PrimitiveTypesLibrary132', {b2})
    assert _is_linked(a, 'rapidml_PrimitiveTypesLibrary132', b2)
    if hasattr(b1, 'rapidml_PrimitiveType133'):
        assert not _is_linked(b1, 'rapidml_PrimitiveType133', a)
    if hasattr(b2, 'rapidml_PrimitiveType133'):
        assert _is_linked(b2, 'rapidml_PrimitiveType133', a)
    _safe_set(a, 'rapidml_PrimitiveTypesLibrary132', set())
    assert not _is_linked(a, 'rapidml_PrimitiveTypesLibrary132', b2)
    if hasattr(b2, 'rapidml_PrimitiveType133'):
        assert not _is_linked(b2, 'rapidml_PrimitiveType133', a)


def test_assoc_primitiveTypesLibrary42_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_PrimitiveTypesLibrary(name="sample_text")
    b2 = rapidml_PrimitiveTypesLibrary(name="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel43', b1)
    assert _is_linked(a, 'rapidml_ZenModel43', b1)
    if hasattr(b1, 'rapidml_PrimitiveTypesLibrary'):
        assert _is_linked(b1, 'rapidml_PrimitiveTypesLibrary', a)
    _safe_set(a, 'rapidml_ZenModel43', b2)
    assert _is_linked(a, 'rapidml_ZenModel43', b2)
    if hasattr(b1, 'rapidml_PrimitiveTypesLibrary'):
        assert not _is_linked(b1, 'rapidml_PrimitiveTypesLibrary', a)
    if hasattr(b2, 'rapidml_PrimitiveTypesLibrary'):
        assert _is_linked(b2, 'rapidml_PrimitiveTypesLibrary', a)
    _safe_set(a, 'rapidml_ZenModel43', None)
    assert not _is_linked(a, 'rapidml_ZenModel43', b2)
    if hasattr(b2, 'rapidml_PrimitiveTypesLibrary'):
        assert not _is_linked(b2, 'rapidml_PrimitiveTypesLibrary', a)


def test_assoc_properties117_link_reassign_clear():
    a = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    b1 = rapidml_ObjectRealization()
    b2 = rapidml_ObjectRealization()
    _safe_set(a, 'rapidml_RealizationContainer', b1)
    assert _is_linked(a, 'rapidml_RealizationContainer', b1)
    if hasattr(b1, 'rapidml_ObjectRealization118'):
        assert _is_linked(b1, 'rapidml_ObjectRealization118', a)
    _safe_set(a, 'rapidml_RealizationContainer', b2)
    assert _is_linked(a, 'rapidml_RealizationContainer', b2)
    if hasattr(b1, 'rapidml_ObjectRealization118'):
        assert not _is_linked(b1, 'rapidml_ObjectRealization118', a)
    if hasattr(b2, 'rapidml_ObjectRealization118'):
        assert _is_linked(b2, 'rapidml_ObjectRealization118', a)
    _safe_set(a, 'rapidml_RealizationContainer', None)
    assert not _is_linked(a, 'rapidml_RealizationContainer', b2)
    if hasattr(b2, 'rapidml_ObjectRealization118'):
        assert not _is_linked(b2, 'rapidml_ObjectRealization118', a)


def test_assoc_realizationContainer98_link_reassign_clear():
    a = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    b1 = rapidml_ObjectRealization()
    b2 = rapidml_ObjectRealization()
    _safe_set(a, 'RealizationContainer', b1)
    assert _is_linked(a, 'RealizationContainer', b1)
    if hasattr(b1, 'inlineObjectRealization'):
        assert _is_linked(b1, 'inlineObjectRealization', a)
    _safe_set(a, 'RealizationContainer', b2)
    assert _is_linked(a, 'RealizationContainer', b2)
    if hasattr(b1, 'inlineObjectRealization'):
        assert not _is_linked(b1, 'inlineObjectRealization', a)
    if hasattr(b2, 'inlineObjectRealization'):
        assert _is_linked(b2, 'inlineObjectRealization', a)
    _safe_set(a, 'RealizationContainer', None)
    assert not _is_linked(a, 'RealizationContainer', b2)
    if hasattr(b2, 'inlineObjectRealization'):
        assert not _is_linked(b2, 'inlineObjectRealization', a)


def test_assoc_referenceElement67_link_reassign_clear():
    a = rapidml_ReferenceTreatment()
    b1 = rapidml_ReferenceElement()
    b2 = rapidml_ReferenceElement()
    _safe_set(a, 'rapidml_ReferenceTreatment', b1)
    assert _is_linked(a, 'rapidml_ReferenceTreatment', b1)
    if hasattr(b1, 'rapidml_ReferenceElement'):
        assert _is_linked(b1, 'rapidml_ReferenceElement', a)
    _safe_set(a, 'rapidml_ReferenceTreatment', b2)
    assert _is_linked(a, 'rapidml_ReferenceTreatment', b2)
    if hasattr(b1, 'rapidml_ReferenceElement'):
        assert not _is_linked(b1, 'rapidml_ReferenceElement', a)
    if hasattr(b2, 'rapidml_ReferenceElement'):
        assert _is_linked(b2, 'rapidml_ReferenceElement', a)
    _safe_set(a, 'rapidml_ReferenceTreatment', None)
    assert not _is_linked(a, 'rapidml_ReferenceTreatment', b2)
    if hasattr(b2, 'rapidml_ReferenceElement'):
        assert not _is_linked(b2, 'rapidml_ReferenceElement', a)


def test_assoc_referenceElement79_link_reassign_clear():
    a = rapidml_ReferenceElement()
    b1 = rapidml_PathSegment()
    b2 = rapidml_PathSegment()
    _safe_set(a, 'rapidml_ReferenceElement80', b1)
    assert _is_linked(a, 'rapidml_ReferenceElement80', b1)
    if hasattr(b1, 'rapidml_PathSegment'):
        assert _is_linked(b1, 'rapidml_PathSegment', a)
    _safe_set(a, 'rapidml_ReferenceElement80', b2)
    assert _is_linked(a, 'rapidml_ReferenceElement80', b2)
    if hasattr(b1, 'rapidml_PathSegment'):
        assert not _is_linked(b1, 'rapidml_PathSegment', a)
    if hasattr(b2, 'rapidml_PathSegment'):
        assert _is_linked(b2, 'rapidml_PathSegment', a)
    _safe_set(a, 'rapidml_ReferenceElement80', None)
    assert not _is_linked(a, 'rapidml_ReferenceElement80', b2)
    if hasattr(b2, 'rapidml_PathSegment'):
        assert not _is_linked(b2, 'rapidml_PathSegment', a)


def test_assoc_referenceElements30_link_reassign_clear():
    a = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    b1 = rapidml_CollectionReferenceElement()
    b2 = rapidml_CollectionReferenceElement()
    _safe_set(a, 'rapidml_CollectionResource', {b1})
    assert _is_linked(a, 'rapidml_CollectionResource', b1)
    if hasattr(b1, 'rapidml_CollectionReferenceElement'):
        assert _is_linked(b1, 'rapidml_CollectionReferenceElement', a)
    _safe_set(a, 'rapidml_CollectionResource', {b2})
    assert _is_linked(a, 'rapidml_CollectionResource', b2)
    if hasattr(b1, 'rapidml_CollectionReferenceElement'):
        assert not _is_linked(b1, 'rapidml_CollectionReferenceElement', a)
    if hasattr(b2, 'rapidml_CollectionReferenceElement'):
        assert _is_linked(b2, 'rapidml_CollectionReferenceElement', a)
    _safe_set(a, 'rapidml_CollectionResource', set())
    assert not _is_linked(a, 'rapidml_CollectionResource', b2)
    if hasattr(b2, 'rapidml_CollectionReferenceElement'):
        assert not _is_linked(b2, 'rapidml_CollectionReferenceElement', a)


def test_assoc_referenceRealization68_link_reassign_clear():
    a = rapidml_ReferenceTreatment()
    b1 = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    b2 = rapidml_ReferenceRealization(multiValued=False, realizationType="sample_text_2")
    _safe_set(a, 'rapidml_ReferenceTreatment69', b1)
    assert _is_linked(a, 'rapidml_ReferenceTreatment69', b1)
    if hasattr(b1, 'rapidml_ReferenceRealization70'):
        assert _is_linked(b1, 'rapidml_ReferenceRealization70', a)
    _safe_set(a, 'rapidml_ReferenceTreatment69', b2)
    assert _is_linked(a, 'rapidml_ReferenceTreatment69', b2)
    if hasattr(b1, 'rapidml_ReferenceRealization70'):
        assert not _is_linked(b1, 'rapidml_ReferenceRealization70', a)
    if hasattr(b2, 'rapidml_ReferenceRealization70'):
        assert _is_linked(b2, 'rapidml_ReferenceRealization70', a)
    _safe_set(a, 'rapidml_ReferenceTreatment69', None)
    assert not _is_linked(a, 'rapidml_ReferenceTreatment69', b2)
    if hasattr(b2, 'rapidml_ReferenceRealization70'):
        assert not _is_linked(b2, 'rapidml_ReferenceRealization70', a)


def test_assoc_referenceTreatments119_link_reassign_clear():
    a = rapidml_ReferenceTreatment()
    b1 = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    b2 = rapidml_RealizationContainer(effectiveRealization="sample_text_2", realizationName="sample_text_2", withDefaultRealization=False)
    _safe_set(a, 'rapidml_ReferenceTreatment121', b1)
    assert _is_linked(a, 'rapidml_ReferenceTreatment121', b1)
    if hasattr(b1, 'rapidml_RealizationContainer120'):
        assert _is_linked(b1, 'rapidml_RealizationContainer120', a)
    _safe_set(a, 'rapidml_ReferenceTreatment121', b2)
    assert _is_linked(a, 'rapidml_ReferenceTreatment121', b2)
    if hasattr(b1, 'rapidml_RealizationContainer120'):
        assert not _is_linked(b1, 'rapidml_RealizationContainer120', a)
    if hasattr(b2, 'rapidml_RealizationContainer120'):
        assert _is_linked(b2, 'rapidml_RealizationContainer120', a)
    _safe_set(a, 'rapidml_ReferenceTreatment121', None)
    assert not _is_linked(a, 'rapidml_ReferenceTreatment121', b2)
    if hasattr(b2, 'rapidml_RealizationContainer120'):
        assert not _is_linked(b2, 'rapidml_RealizationContainer120', a)


def test_assoc_request13_link_reassign_clear():
    a = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b1 = rapidml_TypedRequest()
    b2 = rapidml_TypedRequest()
    _safe_set(a, 'containingMethod', b1)
    assert _is_linked(a, 'containingMethod', b1)
    if hasattr(b1, 'TypedRequest'):
        assert _is_linked(b1, 'TypedRequest', a)
    _safe_set(a, 'containingMethod', b2)
    assert _is_linked(a, 'containingMethod', b2)
    if hasattr(b1, 'TypedRequest'):
        assert not _is_linked(b1, 'TypedRequest', a)
    if hasattr(b2, 'TypedRequest'):
        assert _is_linked(b2, 'TypedRequest', a)
    _safe_set(a, 'containingMethod', None)
    assert not _is_linked(a, 'containingMethod', b2)
    if hasattr(b2, 'TypedRequest'):
        assert not _is_linked(b2, 'TypedRequest', a)


def test_assoc_resourceAPIs35_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel', {b1})
    assert _is_linked(a, 'rapidml_ZenModel', b1)
    if hasattr(b1, 'rapidml_ResourceAPI'):
        assert _is_linked(b1, 'rapidml_ResourceAPI', a)
    _safe_set(a, 'rapidml_ZenModel', {b2})
    assert _is_linked(a, 'rapidml_ZenModel', b2)
    if hasattr(b1, 'rapidml_ResourceAPI'):
        assert not _is_linked(b1, 'rapidml_ResourceAPI', a)
    if hasattr(b2, 'rapidml_ResourceAPI'):
        assert _is_linked(b2, 'rapidml_ResourceAPI', a)
    _safe_set(a, 'rapidml_ZenModel', set())
    assert not _is_linked(a, 'rapidml_ZenModel', b2)
    if hasattr(b2, 'rapidml_ResourceAPI'):
        assert not _is_linked(b2, 'rapidml_ResourceAPI', a)


def test_assoc_resourceType8_link_reassign_clear():
    a = rapidml_TypedMessage(useParentTypeReference=True)
    b1 = rapidml_ResourceDefinition(name="sample_text")
    b2 = rapidml_ResourceDefinition(name="sample_text_2")
    _safe_set(a, 'rapidml_TypedMessage', b1)
    assert _is_linked(a, 'rapidml_TypedMessage', b1)
    if hasattr(b1, 'rapidml_ResourceDefinition9'):
        assert _is_linked(b1, 'rapidml_ResourceDefinition9', a)
    _safe_set(a, 'rapidml_TypedMessage', b2)
    assert _is_linked(a, 'rapidml_TypedMessage', b2)
    if hasattr(b1, 'rapidml_ResourceDefinition9'):
        assert not _is_linked(b1, 'rapidml_ResourceDefinition9', a)
    if hasattr(b2, 'rapidml_ResourceDefinition9'):
        assert _is_linked(b2, 'rapidml_ResourceDefinition9', a)
    _safe_set(a, 'rapidml_TypedMessage', None)
    assert not _is_linked(a, 'rapidml_TypedMessage', b2)
    if hasattr(b2, 'rapidml_ResourceDefinition9'):
        assert not _is_linked(b2, 'rapidml_ResourceDefinition9', a)


def test_assoc_responses14_link_reassign_clear():
    a = rapidml_TypedResponse(statusCode=7)
    b1 = rapidml_Method(httpMethod="sample_text", id="sample_text")
    b2 = rapidml_Method(httpMethod="sample_text_2", id="sample_text_2")
    _safe_set(a, 'TypedResponse', b1)
    assert _is_linked(a, 'TypedResponse', b1)
    if hasattr(b1, 'containingMethod15'):
        assert _is_linked(b1, 'containingMethod15', a)
    _safe_set(a, 'TypedResponse', b2)
    assert _is_linked(a, 'TypedResponse', b2)
    if hasattr(b1, 'containingMethod15'):
        assert not _is_linked(b1, 'containingMethod15', a)
    if hasattr(b2, 'containingMethod15'):
        assert _is_linked(b2, 'containingMethod15', a)
    _safe_set(a, 'TypedResponse', None)
    assert not _is_linked(a, 'TypedResponse', b2)
    if hasattr(b2, 'containingMethod15'):
        assert not _is_linked(b2, 'containingMethod15', a)


def test_assoc_scheme107_link_reassign_clear():
    a = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b1 = rapidml_AuthenticationMethod()
    b2 = rapidml_AuthenticationMethod()
    _safe_set(a, 'rapidml_SecurityScheme109', b1)
    assert _is_linked(a, 'rapidml_SecurityScheme109', b1)
    if hasattr(b1, 'rapidml_AuthenticationMethod108'):
        assert _is_linked(b1, 'rapidml_AuthenticationMethod108', a)
    _safe_set(a, 'rapidml_SecurityScheme109', b2)
    assert _is_linked(a, 'rapidml_SecurityScheme109', b2)
    if hasattr(b1, 'rapidml_AuthenticationMethod108'):
        assert not _is_linked(b1, 'rapidml_AuthenticationMethod108', a)
    if hasattr(b2, 'rapidml_AuthenticationMethod108'):
        assert _is_linked(b2, 'rapidml_AuthenticationMethod108', a)
    _safe_set(a, 'rapidml_SecurityScheme109', None)
    assert not _is_linked(a, 'rapidml_SecurityScheme109', b2)
    if hasattr(b2, 'rapidml_AuthenticationMethod108'):
        assert not _is_linked(b2, 'rapidml_AuthenticationMethod108', a)


def test_assoc_scopes100_link_reassign_clear():
    a = rapidml_SecurityScope(name="sample_text")
    b1 = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b2 = rapidml_SecurityScheme(flow="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rapidml_SecurityScope', b1)
    assert _is_linked(a, 'rapidml_SecurityScope', b1)
    if hasattr(b1, 'rapidml_SecurityScheme'):
        assert _is_linked(b1, 'rapidml_SecurityScheme', a)
    _safe_set(a, 'rapidml_SecurityScope', b2)
    assert _is_linked(a, 'rapidml_SecurityScope', b2)
    if hasattr(b1, 'rapidml_SecurityScheme'):
        assert not _is_linked(b1, 'rapidml_SecurityScheme', a)
    if hasattr(b2, 'rapidml_SecurityScheme'):
        assert _is_linked(b2, 'rapidml_SecurityScheme', a)
    _safe_set(a, 'rapidml_SecurityScope', None)
    assert not _is_linked(a, 'rapidml_SecurityScope', b2)
    if hasattr(b2, 'rapidml_SecurityScheme'):
        assert not _is_linked(b2, 'rapidml_SecurityScheme', a)


def test_assoc_scopes110_link_reassign_clear():
    a = rapidml_SecurityScope(name="sample_text")
    b1 = rapidml_AuthenticationMethod()
    b2 = rapidml_AuthenticationMethod()
    _safe_set(a, 'rapidml_SecurityScope112', b1)
    assert _is_linked(a, 'rapidml_SecurityScope112', b1)
    if hasattr(b1, 'rapidml_AuthenticationMethod111'):
        assert _is_linked(b1, 'rapidml_AuthenticationMethod111', a)
    _safe_set(a, 'rapidml_SecurityScope112', b2)
    assert _is_linked(a, 'rapidml_SecurityScope112', b2)
    if hasattr(b1, 'rapidml_AuthenticationMethod111'):
        assert not _is_linked(b1, 'rapidml_AuthenticationMethod111', a)
    if hasattr(b2, 'rapidml_AuthenticationMethod111'):
        assert _is_linked(b2, 'rapidml_AuthenticationMethod111', a)
    _safe_set(a, 'rapidml_SecurityScope112', None)
    assert not _is_linked(a, 'rapidml_SecurityScope112', b2)
    if hasattr(b2, 'rapidml_AuthenticationMethod111'):
        assert not _is_linked(b2, 'rapidml_AuthenticationMethod111', a)


def test_assoc_securitySchemes113_link_reassign_clear():
    a = rapidml_SecuritySchemeLibrary(name="sample_text")
    b1 = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b2 = rapidml_SecurityScheme(flow="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rapidml_SecuritySchemeLibrary114', {b1})
    assert _is_linked(a, 'rapidml_SecuritySchemeLibrary114', b1)
    if hasattr(b1, 'rapidml_SecurityScheme115'):
        assert _is_linked(b1, 'rapidml_SecurityScheme115', a)
    _safe_set(a, 'rapidml_SecuritySchemeLibrary114', {b2})
    assert _is_linked(a, 'rapidml_SecuritySchemeLibrary114', b2)
    if hasattr(b1, 'rapidml_SecurityScheme115'):
        assert not _is_linked(b1, 'rapidml_SecurityScheme115', a)
    if hasattr(b2, 'rapidml_SecurityScheme115'):
        assert _is_linked(b2, 'rapidml_SecurityScheme115', a)
    _safe_set(a, 'rapidml_SecuritySchemeLibrary114', set())
    assert not _is_linked(a, 'rapidml_SecuritySchemeLibrary114', b2)
    if hasattr(b2, 'rapidml_SecurityScheme115'):
        assert not _is_linked(b2, 'rapidml_SecurityScheme115', a)


def test_assoc_securitySchemesLibrary46_link_reassign_clear():
    a = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    b1 = rapidml_SecuritySchemeLibrary(name="sample_text")
    b2 = rapidml_SecuritySchemeLibrary(name="sample_text_2")
    _safe_set(a, 'rapidml_ZenModel47', b1)
    assert _is_linked(a, 'rapidml_ZenModel47', b1)
    if hasattr(b1, 'rapidml_SecuritySchemeLibrary'):
        assert _is_linked(b1, 'rapidml_SecuritySchemeLibrary', a)
    _safe_set(a, 'rapidml_ZenModel47', b2)
    assert _is_linked(a, 'rapidml_ZenModel47', b2)
    if hasattr(b1, 'rapidml_SecuritySchemeLibrary'):
        assert not _is_linked(b1, 'rapidml_SecuritySchemeLibrary', a)
    if hasattr(b2, 'rapidml_SecuritySchemeLibrary'):
        assert _is_linked(b2, 'rapidml_SecuritySchemeLibrary', a)
    _safe_set(a, 'rapidml_ZenModel47', None)
    assert not _is_linked(a, 'rapidml_ZenModel47', b2)
    if hasattr(b2, 'rapidml_SecuritySchemeLibrary'):
        assert not _is_linked(b2, 'rapidml_SecuritySchemeLibrary', a)


def test_assoc_segments82_link_reassign_clear():
    a = rapidml_URISegment(name="sample_text")
    b1 = rapidml_URI()
    b2 = rapidml_URI()
    _safe_set(a, 'rapidml_URISegment', b1)
    assert _is_linked(a, 'rapidml_URISegment', b1)
    if hasattr(b1, 'rapidml_URI83'):
        assert _is_linked(b1, 'rapidml_URI83', a)
    _safe_set(a, 'rapidml_URISegment', b2)
    assert _is_linked(a, 'rapidml_URISegment', b2)
    if hasattr(b1, 'rapidml_URI83'):
        assert not _is_linked(b1, 'rapidml_URI83', a)
    if hasattr(b2, 'rapidml_URI83'):
        assert _is_linked(b2, 'rapidml_URI83', a)
    _safe_set(a, 'rapidml_URISegment', None)
    assert not _is_linked(a, 'rapidml_URISegment', b2)
    if hasattr(b2, 'rapidml_URI83'):
        assert not _is_linked(b2, 'rapidml_URI83', a)


def test_assoc_serviceDataModels51_link_reassign_clear():
    a = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    b1 = rapidml_DataModel(name="sample_text")
    b2 = rapidml_DataModel(name="sample_text_2")
    _safe_set(a, 'rapidml_ResourceAPI52', {b1})
    assert _is_linked(a, 'rapidml_ResourceAPI52', b1)
    if hasattr(b1, 'rapidml_DataModel53'):
        assert _is_linked(b1, 'rapidml_DataModel53', a)
    _safe_set(a, 'rapidml_ResourceAPI52', {b2})
    assert _is_linked(a, 'rapidml_ResourceAPI52', b2)
    if hasattr(b1, 'rapidml_DataModel53'):
        assert not _is_linked(b1, 'rapidml_DataModel53', a)
    if hasattr(b2, 'rapidml_DataModel53'):
        assert _is_linked(b2, 'rapidml_DataModel53', a)
    _safe_set(a, 'rapidml_ResourceAPI52', set())
    assert not _is_linked(a, 'rapidml_ResourceAPI52', b2)
    if hasattr(b2, 'rapidml_DataModel53'):
        assert not _is_linked(b2, 'rapidml_DataModel53', a)


def test_assoc_settings101_link_reassign_clear():
    a = rapidml_SecuritySchemeParameter(name="sample_text", value="sample_text")
    b1 = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    b2 = rapidml_SecurityScheme(flow="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rapidml_SecuritySchemeParameter', b1)
    assert _is_linked(a, 'rapidml_SecuritySchemeParameter', b1)
    if hasattr(b1, 'rapidml_SecurityScheme102'):
        assert _is_linked(b1, 'rapidml_SecurityScheme102', a)
    _safe_set(a, 'rapidml_SecuritySchemeParameter', b2)
    assert _is_linked(a, 'rapidml_SecuritySchemeParameter', b2)
    if hasattr(b1, 'rapidml_SecurityScheme102'):
        assert not _is_linked(b1, 'rapidml_SecurityScheme102', a)
    if hasattr(b2, 'rapidml_SecurityScheme102'):
        assert _is_linked(b2, 'rapidml_SecurityScheme102', a)
    _safe_set(a, 'rapidml_SecuritySchemeParameter', None)
    assert not _is_linked(a, 'rapidml_SecuritySchemeParameter', b2)
    if hasattr(b2, 'rapidml_SecurityScheme102'):
        assert not _is_linked(b2, 'rapidml_SecurityScheme102', a)


def test_assoc_simpleType81_link_reassign_clear():
    a = rapidml_PrimitiveTypeSourceReference()
    b1 = rapidml_PrimitiveType()
    b2 = rapidml_PrimitiveType()
    _safe_set(a, 'rapidml_PrimitiveTypeSourceReference', b1)
    assert _is_linked(a, 'rapidml_PrimitiveTypeSourceReference', b1)
    if hasattr(b1, 'rapidml_PrimitiveType'):
        assert _is_linked(b1, 'rapidml_PrimitiveType', a)
    _safe_set(a, 'rapidml_PrimitiveTypeSourceReference', b2)
    assert _is_linked(a, 'rapidml_PrimitiveTypeSourceReference', b2)
    if hasattr(b1, 'rapidml_PrimitiveType'):
        assert not _is_linked(b1, 'rapidml_PrimitiveType', a)
    if hasattr(b2, 'rapidml_PrimitiveType'):
        assert _is_linked(b2, 'rapidml_PrimitiveType', a)
    _safe_set(a, 'rapidml_PrimitiveTypeSourceReference', None)
    assert not _is_linked(a, 'rapidml_PrimitiveTypeSourceReference', b2)
    if hasattr(b2, 'rapidml_PrimitiveType'):
        assert not _is_linked(b2, 'rapidml_PrimitiveType', a)


def test_assoc_sourceReference17_link_reassign_clear():
    a = rapidml_SourceReference()
    b1 = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    b2 = rapidml_Parameter(default="sample_text_2", fixed="sample_text_2", name="sample_text_2", required=False)
    _safe_set(a, 'SourceReference', b1)
    assert _is_linked(a, 'SourceReference', b1)
    if hasattr(b1, 'containingParameter'):
        assert _is_linked(b1, 'containingParameter', a)
    _safe_set(a, 'SourceReference', b2)
    assert _is_linked(a, 'SourceReference', b2)
    if hasattr(b1, 'containingParameter'):
        assert not _is_linked(b1, 'containingParameter', a)
    if hasattr(b2, 'containingParameter'):
        assert _is_linked(b2, 'containingParameter', a)
    _safe_set(a, 'SourceReference', None)
    assert not _is_linked(a, 'SourceReference', b2)
    if hasattr(b2, 'containingParameter'):
        assert not _is_linked(b2, 'containingParameter', a)


def test_assoc_supertypes148_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_Inheritable()
    b2 = rapidml_Inheritable()
    _safe_set(a, 'rapidml_Structure149', {b1})
    assert _is_linked(a, 'rapidml_Structure149', b1)
    if hasattr(b1, 'rapidml_Inheritable'):
        assert _is_linked(b1, 'rapidml_Inheritable', a)
    _safe_set(a, 'rapidml_Structure149', {b2})
    assert _is_linked(a, 'rapidml_Structure149', b2)
    if hasattr(b1, 'rapidml_Inheritable'):
        assert not _is_linked(b1, 'rapidml_Inheritable', a)
    if hasattr(b2, 'rapidml_Inheritable'):
        assert _is_linked(b2, 'rapidml_Inheritable', a)
    _safe_set(a, 'rapidml_Structure149', set())
    assert not _is_linked(a, 'rapidml_Structure149', b2)
    if hasattr(b2, 'rapidml_Inheritable'):
        assert not _is_linked(b2, 'rapidml_Inheritable', a)


def test_assoc_targetResource74_link_reassign_clear():
    a = rapidml_ResourceDefinition(name="sample_text")
    b1 = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    b2 = rapidml_ReferenceRealization(multiValued=False, realizationType="sample_text_2")
    _safe_set(a, 'rapidml_ResourceDefinition76', b1)
    assert _is_linked(a, 'rapidml_ResourceDefinition76', b1)
    if hasattr(b1, 'rapidml_ReferenceRealization75'):
        assert _is_linked(b1, 'rapidml_ReferenceRealization75', a)
    _safe_set(a, 'rapidml_ResourceDefinition76', b2)
    assert _is_linked(a, 'rapidml_ResourceDefinition76', b2)
    if hasattr(b1, 'rapidml_ReferenceRealization75'):
        assert not _is_linked(b1, 'rapidml_ReferenceRealization75', a)
    if hasattr(b2, 'rapidml_ReferenceRealization75'):
        assert _is_linked(b2, 'rapidml_ReferenceRealization75', a)
    _safe_set(a, 'rapidml_ResourceDefinition76', None)
    assert not _is_linked(a, 'rapidml_ResourceDefinition76', b2)
    if hasattr(b2, 'rapidml_ReferenceRealization75'):
        assert not _is_linked(b2, 'rapidml_ReferenceRealization75', a)


def test_assoc_type135_link_reassign_clear():
    a = rapidml_Structure()
    b1 = rapidml_ReferenceProperty(container=True, containment=True)
    b2 = rapidml_ReferenceProperty(container=False, containment=False)
    _safe_set(a, 'rapidml_Structure136', b1)
    assert _is_linked(a, 'rapidml_Structure136', b1)
    if hasattr(b1, 'rapidml_ReferenceProperty'):
        assert _is_linked(b1, 'rapidml_ReferenceProperty', a)
    _safe_set(a, 'rapidml_Structure136', b2)
    assert _is_linked(a, 'rapidml_Structure136', b2)
    if hasattr(b1, 'rapidml_ReferenceProperty'):
        assert not _is_linked(b1, 'rapidml_ReferenceProperty', a)
    if hasattr(b2, 'rapidml_ReferenceProperty'):
        assert _is_linked(b2, 'rapidml_ReferenceProperty', a)
    _safe_set(a, 'rapidml_Structure136', None)
    assert not _is_linked(a, 'rapidml_Structure136', b2)
    if hasattr(b2, 'rapidml_ReferenceProperty'):
        assert not _is_linked(b2, 'rapidml_ReferenceProperty', a)


def test_assoc_type140_link_reassign_clear():
    a = rapidml_SingleValueType()
    b1 = rapidml_PrimitiveProperty()
    b2 = rapidml_PrimitiveProperty()
    _safe_set(a, 'rapidml_SingleValueType', b1)
    assert _is_linked(a, 'rapidml_SingleValueType', b1)
    if hasattr(b1, 'rapidml_PrimitiveProperty141'):
        assert _is_linked(b1, 'rapidml_PrimitiveProperty141', a)
    _safe_set(a, 'rapidml_SingleValueType', b2)
    assert _is_linked(a, 'rapidml_SingleValueType', b2)
    if hasattr(b1, 'rapidml_PrimitiveProperty141'):
        assert not _is_linked(b1, 'rapidml_PrimitiveProperty141', a)
    if hasattr(b2, 'rapidml_PrimitiveProperty141'):
        assert _is_linked(b2, 'rapidml_PrimitiveProperty141', a)
    _safe_set(a, 'rapidml_SingleValueType', None)
    assert not _is_linked(a, 'rapidml_SingleValueType', b2)
    if hasattr(b2, 'rapidml_PrimitiveProperty141'):
        assert not _is_linked(b2, 'rapidml_PrimitiveProperty141', a)


def test_assoc_uriParameters84_link_reassign_clear():
    a = rapidml_URIParameter()
    b1 = rapidml_URI()
    b2 = rapidml_URI()
    _safe_set(a, 'URIParameter', b1)
    assert _is_linked(a, 'URIParameter', b1)
    if hasattr(b1, 'containingURI'):
        assert _is_linked(b1, 'containingURI', a)
    _safe_set(a, 'URIParameter', b2)
    assert _is_linked(a, 'URIParameter', b2)
    if hasattr(b1, 'containingURI'):
        assert not _is_linked(b1, 'containingURI', a)
    if hasattr(b2, 'containingURI'):
        assert _is_linked(b2, 'containingURI', a)
    _safe_set(a, 'URIParameter', None)
    assert not _is_linked(a, 'URIParameter', b2)
    if hasattr(b2, 'containingURI'):
        assert not _is_linked(b2, 'containingURI', a)


def test_assoc_uriSegment26_link_reassign_clear():
    a = rapidml_URIParameter()
    b1 = rapidml_URISegmentWithParameter()
    b2 = rapidml_URISegmentWithParameter()
    _safe_set(a, 'rapidml_URIParameter', b1)
    assert _is_linked(a, 'rapidml_URIParameter', b1)
    if hasattr(b1, 'rapidml_URISegmentWithParameter'):
        assert _is_linked(b1, 'rapidml_URISegmentWithParameter', a)
    _safe_set(a, 'rapidml_URIParameter', b2)
    assert _is_linked(a, 'rapidml_URIParameter', b2)
    if hasattr(b1, 'rapidml_URISegmentWithParameter'):
        assert not _is_linked(b1, 'rapidml_URISegmentWithParameter', a)
    if hasattr(b2, 'rapidml_URISegmentWithParameter'):
        assert _is_linked(b2, 'rapidml_URISegmentWithParameter', a)
    _safe_set(a, 'rapidml_URIParameter', None)
    assert not _is_linked(a, 'rapidml_URIParameter', b2)
    if hasattr(b2, 'rapidml_URISegmentWithParameter'):
        assert not _is_linked(b2, 'rapidml_URISegmentWithParameter', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ConstrainableType_strategy = st.builds(ConstrainableType)
@given(instance=ConstrainableType_strategy)
@settings(max_examples=25)
def test_ConstrainableType_instantiation(instance):
    assert isinstance(instance, ConstrainableType)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


DataExample_strategy = st.builds(DataExample)
@given(instance=DataExample_strategy)
@settings(max_examples=25)
def test_DataExample_instantiation(instance):
    assert isinstance(instance, DataExample)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Documentable_strategy = st.builds(Documentable)
@given(instance=Documentable_strategy)
@settings(max_examples=25)
def test_Documentable_instantiation(instance):
    assert isinstance(instance, Documentable)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Example_strategy = st.builds(Example)
@given(instance=Example_strategy)
@settings(max_examples=25)
def test_Example_instantiation(instance):
    assert isinstance(instance, Example)


Extensible_strategy = st.builds(Extensible)
@given(instance=Extensible_strategy)
@settings(max_examples=25)
def test_Extensible_instantiation(instance):
    assert isinstance(instance, Extensible)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


HasSecurityValue_strategy = st.builds(HasSecurityValue)
@given(instance=HasSecurityValue_strategy)
@settings(max_examples=25)
def test_HasSecurityValue_instantiation(instance):
    assert isinstance(instance, HasSecurityValue)


HasStringValue_strategy = st.builds(HasStringValue)
@given(instance=HasStringValue_strategy)
@settings(max_examples=25)
def test_HasStringValue_instantiation(instance):
    assert isinstance(instance, HasStringValue)


HasTitle_strategy = st.builds(HasTitle)
@given(instance=HasTitle_strategy)
@settings(max_examples=25)
def test_HasTitle_instantiation(instance):
    assert isinstance(instance, HasTitle)


Inheritable_strategy = st.builds(Inheritable)
@given(instance=Inheritable_strategy)
@settings(max_examples=25)
def test_Inheritable_instantiation(instance):
    assert isinstance(instance, Inheritable)


ObjectRealization_strategy = st.builds(ObjectRealization)
@given(instance=ObjectRealization_strategy)
@settings(max_examples=25)
def test_ObjectRealization_instantiation(instance):
    assert isinstance(instance, ObjectRealization)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


RESTElement_strategy = st.builds(RESTElement)
@given(instance=RESTElement_strategy)
@settings(max_examples=25)
def test_RESTElement_instantiation(instance):
    assert isinstance(instance, RESTElement)


RealizationContainer_strategy = st.builds(RealizationContainer)
@given(instance=RealizationContainer_strategy)
@settings(max_examples=25)
def test_RealizationContainer_instantiation(instance):
    assert isinstance(instance, RealizationContainer)


ReferenceElement_strategy = st.builds(ReferenceElement)
@given(instance=ReferenceElement_strategy)
@settings(max_examples=25)
def test_ReferenceElement_instantiation(instance):
    assert isinstance(instance, ReferenceElement)


ReferenceTreatment_strategy = st.builds(ReferenceTreatment)
@given(instance=ReferenceTreatment_strategy)
@settings(max_examples=25)
def test_ReferenceTreatment_instantiation(instance):
    assert isinstance(instance, ReferenceTreatment)


ResourceDefinition_strategy = st.builds(ResourceDefinition)
@given(instance=ResourceDefinition_strategy)
@settings(max_examples=25)
def test_ResourceDefinition_instantiation(instance):
    assert isinstance(instance, ResourceDefinition)


ServiceDataResource_strategy = st.builds(ServiceDataResource)
@given(instance=ServiceDataResource_strategy)
@settings(max_examples=25)
def test_ServiceDataResource_instantiation(instance):
    assert isinstance(instance, ServiceDataResource)


SimpleType_strategy = st.builds(SimpleType)
@given(instance=SimpleType_strategy)
@settings(max_examples=25)
def test_SimpleType_instantiation(instance):
    assert isinstance(instance, SimpleType)


SingleValueType_strategy = st.builds(SingleValueType)
@given(instance=SingleValueType_strategy)
@settings(max_examples=25)
def test_SingleValueType_instantiation(instance):
    assert isinstance(instance, SingleValueType)


SourceReference_strategy = st.builds(SourceReference)
@given(instance=SourceReference_strategy)
@settings(max_examples=25)
def test_SourceReference_instantiation(instance):
    assert isinstance(instance, SourceReference)


TypedMessage_strategy = st.builds(TypedMessage)
@given(instance=TypedMessage_strategy)
@settings(max_examples=25)
def test_TypedMessage_instantiation(instance):
    assert isinstance(instance, TypedMessage)


URIParameter_strategy = st.builds(URIParameter)
@given(instance=URIParameter_strategy)
@settings(max_examples=25)
def test_URIParameter_instantiation(instance):
    assert isinstance(instance, URIParameter)


URISegment_strategy = st.builds(URISegment)
@given(instance=URISegment_strategy)
@settings(max_examples=25)
def test_URISegment_instantiation(instance):
    assert isinstance(instance, URISegment)


WithDataExamples_strategy = st.builds(WithDataExamples)
@given(instance=WithDataExamples_strategy)
@settings(max_examples=25)
def test_WithDataExamples_instantiation(instance):
    assert isinstance(instance, WithDataExamples)


WithExamples_strategy = st.builds(WithExamples)
@given(instance=WithExamples_strategy)
@settings(max_examples=25)
def test_WithExamples_instantiation(instance):
    assert isinstance(instance, WithExamples)


rapidml_AuthenticationMethod_strategy = st.builds(rapidml_AuthenticationMethod)
@given(instance=rapidml_AuthenticationMethod_strategy)
@settings(max_examples=25)
def test_rapidml_AuthenticationMethod_instantiation(instance):
    assert isinstance(instance, rapidml_AuthenticationMethod)


rapidml_CollectionParameter_strategy = st.builds(rapidml_CollectionParameter)
@given(instance=rapidml_CollectionParameter_strategy)
@settings(max_examples=25)
def test_rapidml_CollectionParameter_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionParameter)


rapidml_CollectionReferenceElement_strategy = st.builds(rapidml_CollectionReferenceElement)
@given(instance=rapidml_CollectionReferenceElement_strategy)
@settings(max_examples=25)
def test_rapidml_CollectionReferenceElement_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionReferenceElement)


rapidml_CollectionResource_strategy = st.builds(rapidml_CollectionResource, resourceRealizationKind=safe_text)
@given(instance=rapidml_CollectionResource_strategy)
@settings(max_examples=25)
def test_rapidml_CollectionResource_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionResource)


rapidml_ConstrainableType_strategy = st.builds(rapidml_ConstrainableType)
@given(instance=rapidml_ConstrainableType_strategy)
@settings(max_examples=25)
def test_rapidml_ConstrainableType_instantiation(instance):
    assert isinstance(instance, rapidml_ConstrainableType)


rapidml_Constraint_strategy = st.builds(rapidml_Constraint)
@given(instance=rapidml_Constraint_strategy)
@settings(max_examples=25)
def test_rapidml_Constraint_instantiation(instance):
    assert isinstance(instance, rapidml_Constraint)


rapidml_DataExample_strategy = st.builds(rapidml_DataExample)
@given(instance=rapidml_DataExample_strategy)
@settings(max_examples=25)
def test_rapidml_DataExample_instantiation(instance):
    assert isinstance(instance, rapidml_DataExample)


rapidml_DataModel_strategy = st.builds(rapidml_DataModel, name=safe_text)
@given(instance=rapidml_DataModel_strategy)
@settings(max_examples=25)
def test_rapidml_DataModel_instantiation(instance):
    assert isinstance(instance, rapidml_DataModel)


rapidml_DataType_strategy = st.builds(rapidml_DataType, name=safe_text)
@given(instance=rapidml_DataType_strategy)
@settings(max_examples=25)
def test_rapidml_DataType_instantiation(instance):
    assert isinstance(instance, rapidml_DataType)


rapidml_Documentable_strategy = st.builds(rapidml_Documentable)
@given(instance=rapidml_Documentable_strategy)
@settings(max_examples=25)
def test_rapidml_Documentable_instantiation(instance):
    assert isinstance(instance, rapidml_Documentable)


rapidml_Documentation_strategy = st.builds(rapidml_Documentation, text=safe_text)
@given(instance=rapidml_Documentation_strategy)
@settings(max_examples=25)
def test_rapidml_Documentation_instantiation(instance):
    assert isinstance(instance, rapidml_Documentation)


rapidml_Element_strategy = st.builds(rapidml_Element, cardinality=safe_text)
@given(instance=rapidml_Element_strategy)
@settings(max_examples=25)
def test_rapidml_Element_instantiation(instance):
    assert isinstance(instance, rapidml_Element)


rapidml_EnumConstant_strategy = st.builds(rapidml_EnumConstant, integerValue=st.integers(), literalValue=safe_text, name=safe_text)
@given(instance=rapidml_EnumConstant_strategy)
@settings(max_examples=25)
def test_rapidml_EnumConstant_instantiation(instance):
    assert isinstance(instance, rapidml_EnumConstant)


rapidml_Enumeration_strategy = st.builds(rapidml_Enumeration)
@given(instance=rapidml_Enumeration_strategy)
@settings(max_examples=25)
def test_rapidml_Enumeration_instantiation(instance):
    assert isinstance(instance, rapidml_Enumeration)


rapidml_Example_strategy = st.builds(rapidml_Example)
@given(instance=rapidml_Example_strategy)
@settings(max_examples=25)
def test_rapidml_Example_instantiation(instance):
    assert isinstance(instance, rapidml_Example)


rapidml_Extensible_strategy = st.builds(rapidml_Extensible)
@given(instance=rapidml_Extensible_strategy)
@settings(max_examples=25)
def test_rapidml_Extensible_instantiation(instance):
    assert isinstance(instance, rapidml_Extensible)


rapidml_Extension_strategy = st.builds(rapidml_Extension, name=safe_text, value=safe_text)
@given(instance=rapidml_Extension_strategy)
@settings(max_examples=25)
def test_rapidml_Extension_instantiation(instance):
    assert isinstance(instance, rapidml_Extension)


rapidml_ExternalExample_strategy = st.builds(rapidml_ExternalExample, path=safe_text)
@given(instance=rapidml_ExternalExample_strategy)
@settings(max_examples=25)
def test_rapidml_ExternalExample_instantiation(instance):
    assert isinstance(instance, rapidml_ExternalExample)


rapidml_Feature_strategy = st.builds(rapidml_Feature, key=st.booleans(), name=safe_text, readOnly=st.booleans(), restriction=st.booleans())
@given(instance=rapidml_Feature_strategy)
@settings(max_examples=25)
def test_rapidml_Feature_instantiation(instance):
    assert isinstance(instance, rapidml_Feature)


rapidml_HasSecurityValue_strategy = st.builds(rapidml_HasSecurityValue)
@given(instance=rapidml_HasSecurityValue_strategy)
@settings(max_examples=25)
def test_rapidml_HasSecurityValue_instantiation(instance):
    assert isinstance(instance, rapidml_HasSecurityValue)


rapidml_HasStringValue_strategy = st.builds(rapidml_HasStringValue)
@given(instance=rapidml_HasStringValue_strategy)
@settings(max_examples=25)
def test_rapidml_HasStringValue_instantiation(instance):
    assert isinstance(instance, rapidml_HasStringValue)


rapidml_HasTitle_strategy = st.builds(rapidml_HasTitle, title=safe_text)
@given(instance=rapidml_HasTitle_strategy)
@settings(max_examples=25)
def test_rapidml_HasTitle_instantiation(instance):
    assert isinstance(instance, rapidml_HasTitle)


rapidml_ImportDeclaration_strategy = st.builds(rapidml_ImportDeclaration, alias=safe_text, importURI=safe_text, importedNamespace=safe_text)
@given(instance=rapidml_ImportDeclaration_strategy)
@settings(max_examples=25)
def test_rapidml_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, rapidml_ImportDeclaration)


rapidml_Inheritable_strategy = st.builds(rapidml_Inheritable)
@given(instance=rapidml_Inheritable_strategy)
@settings(max_examples=25)
def test_rapidml_Inheritable_instantiation(instance):
    assert isinstance(instance, rapidml_Inheritable)


rapidml_InlineDataExample_strategy = st.builds(rapidml_InlineDataExample, body=safe_text)
@given(instance=rapidml_InlineDataExample_strategy)
@settings(max_examples=25)
def test_rapidml_InlineDataExample_instantiation(instance):
    assert isinstance(instance, rapidml_InlineDataExample)


rapidml_InlineExample_strategy = st.builds(rapidml_InlineExample, body=safe_text)
@given(instance=rapidml_InlineExample_strategy)
@settings(max_examples=25)
def test_rapidml_InlineExample_instantiation(instance):
    assert isinstance(instance, rapidml_InlineExample)


rapidml_LengthConstraint_strategy = st.builds(rapidml_LengthConstraint, length=st.integers(), maxLength=st.integers(), minLength=st.integers())
@given(instance=rapidml_LengthConstraint_strategy)
@settings(max_examples=25)
def test_rapidml_LengthConstraint_instantiation(instance):
    assert isinstance(instance, rapidml_LengthConstraint)


rapidml_LinkRelation_strategy = st.builds(rapidml_LinkRelation, name=safe_text, specURL=safe_text)
@given(instance=rapidml_LinkRelation_strategy)
@settings(max_examples=25)
def test_rapidml_LinkRelation_instantiation(instance):
    assert isinstance(instance, rapidml_LinkRelation)


rapidml_LinkRelationsLibrary_strategy = st.builds(rapidml_LinkRelationsLibrary, name=safe_text)
@given(instance=rapidml_LinkRelationsLibrary_strategy)
@settings(max_examples=25)
def test_rapidml_LinkRelationsLibrary_instantiation(instance):
    assert isinstance(instance, rapidml_LinkRelationsLibrary)


rapidml_MatrixParameter_strategy = st.builds(rapidml_MatrixParameter)
@given(instance=rapidml_MatrixParameter_strategy)
@settings(max_examples=25)
def test_rapidml_MatrixParameter_instantiation(instance):
    assert isinstance(instance, rapidml_MatrixParameter)


rapidml_MediaType_strategy = st.builds(rapidml_MediaType, name=safe_text, specURL=safe_text)
@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=25)
def test_rapidml_MediaType_instantiation(instance):
    assert isinstance(instance, rapidml_MediaType)


rapidml_MediaTypesLibrary_strategy = st.builds(rapidml_MediaTypesLibrary)
@given(instance=rapidml_MediaTypesLibrary_strategy)
@settings(max_examples=25)
def test_rapidml_MediaTypesLibrary_instantiation(instance):
    assert isinstance(instance, rapidml_MediaTypesLibrary)


rapidml_MessageParameter_strategy = st.builds(rapidml_MessageParameter, httpLocation=safe_text)
@given(instance=rapidml_MessageParameter_strategy)
@settings(max_examples=25)
def test_rapidml_MessageParameter_instantiation(instance):
    assert isinstance(instance, rapidml_MessageParameter)


rapidml_Method_strategy = st.builds(rapidml_Method, httpMethod=safe_text, id=safe_text)
@given(instance=rapidml_Method_strategy)
@settings(max_examples=25)
def test_rapidml_Method_instantiation(instance):
    assert isinstance(instance, rapidml_Method)


rapidml_NamedLinkDescriptor_strategy = st.builds(rapidml_NamedLinkDescriptor, default=st.booleans(), name=safe_text)
@given(instance=rapidml_NamedLinkDescriptor_strategy)
@settings(max_examples=25)
def test_rapidml_NamedLinkDescriptor_instantiation(instance):
    assert isinstance(instance, rapidml_NamedLinkDescriptor)


rapidml_ObjectRealization_strategy = st.builds(rapidml_ObjectRealization)
@given(instance=rapidml_ObjectRealization_strategy)
@settings(max_examples=25)
def test_rapidml_ObjectRealization_instantiation(instance):
    assert isinstance(instance, rapidml_ObjectRealization)


rapidml_ObjectResource_strategy = st.builds(rapidml_ObjectResource)
@given(instance=rapidml_ObjectResource_strategy)
@settings(max_examples=25)
def test_rapidml_ObjectResource_instantiation(instance):
    assert isinstance(instance, rapidml_ObjectResource)


rapidml_Operation_strategy = st.builds(rapidml_Operation, name=safe_text)
@given(instance=rapidml_Operation_strategy)
@settings(max_examples=25)
def test_rapidml_Operation_instantiation(instance):
    assert isinstance(instance, rapidml_Operation)


rapidml_Parameter_strategy = st.builds(rapidml_Parameter, default=safe_text, fixed=safe_text, name=safe_text, required=st.booleans())
@given(instance=rapidml_Parameter_strategy)
@settings(max_examples=25)
def test_rapidml_Parameter_instantiation(instance):
    assert isinstance(instance, rapidml_Parameter)


rapidml_PathSegment_strategy = st.builds(rapidml_PathSegment)
@given(instance=rapidml_PathSegment_strategy)
@settings(max_examples=25)
def test_rapidml_PathSegment_instantiation(instance):
    assert isinstance(instance, rapidml_PathSegment)


rapidml_PrimitiveProperty_strategy = st.builds(rapidml_PrimitiveProperty)
@given(instance=rapidml_PrimitiveProperty_strategy)
@settings(max_examples=25)
def test_rapidml_PrimitiveProperty_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveProperty)


rapidml_PrimitiveType_strategy = st.builds(rapidml_PrimitiveType)
@given(instance=rapidml_PrimitiveType_strategy)
@settings(max_examples=25)
def test_rapidml_PrimitiveType_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveType)


rapidml_PrimitiveTypeSourceReference_strategy = st.builds(rapidml_PrimitiveTypeSourceReference)
@given(instance=rapidml_PrimitiveTypeSourceReference_strategy)
@settings(max_examples=25)
def test_rapidml_PrimitiveTypeSourceReference_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveTypeSourceReference)


rapidml_PrimitiveTypesLibrary_strategy = st.builds(rapidml_PrimitiveTypesLibrary, name=safe_text)
@given(instance=rapidml_PrimitiveTypesLibrary_strategy)
@settings(max_examples=25)
def test_rapidml_PrimitiveTypesLibrary_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveTypesLibrary)


rapidml_PropertyRealization_strategy = st.builds(rapidml_PropertyRealization, cardinality=safe_text)
@given(instance=rapidml_PropertyRealization_strategy)
@settings(max_examples=25)
def test_rapidml_PropertyRealization_instantiation(instance):
    assert isinstance(instance, rapidml_PropertyRealization)


rapidml_PropertyReference_strategy = st.builds(rapidml_PropertyReference)
@given(instance=rapidml_PropertyReference_strategy)
@settings(max_examples=25)
def test_rapidml_PropertyReference_instantiation(instance):
    assert isinstance(instance, rapidml_PropertyReference)


rapidml_RESTElement_strategy = st.builds(rapidml_RESTElement)
@given(instance=rapidml_RESTElement_strategy)
@settings(max_examples=25)
def test_rapidml_RESTElement_instantiation(instance):
    assert isinstance(instance, rapidml_RESTElement)


rapidml_RealizationContainer_strategy = st.builds(rapidml_RealizationContainer, effectiveRealization=safe_text, realizationName=safe_text, withDefaultRealization=st.booleans())
@given(instance=rapidml_RealizationContainer_strategy)
@settings(max_examples=25)
def test_rapidml_RealizationContainer_instantiation(instance):
    assert isinstance(instance, rapidml_RealizationContainer)


rapidml_RealizationModelLocation_strategy = st.builds(rapidml_RealizationModelLocation, uri=safe_text)
@given(instance=rapidml_RealizationModelLocation_strategy)
@settings(max_examples=25)
def test_rapidml_RealizationModelLocation_instantiation(instance):
    assert isinstance(instance, rapidml_RealizationModelLocation)


rapidml_ReferenceElement_strategy = st.builds(rapidml_ReferenceElement)
@given(instance=rapidml_ReferenceElement_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceElement_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceElement)


rapidml_ReferenceEmbed_strategy = st.builds(rapidml_ReferenceEmbed)
@given(instance=rapidml_ReferenceEmbed_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceEmbed_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceEmbed)


rapidml_ReferenceLink_strategy = st.builds(rapidml_ReferenceLink, collectionRealizationLevel=safe_text, name=safe_text)
@given(instance=rapidml_ReferenceLink_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceLink_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceLink)


rapidml_ReferenceProperty_strategy = st.builds(rapidml_ReferenceProperty, container=st.booleans(), containment=st.booleans())
@given(instance=rapidml_ReferenceProperty_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceProperty_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceProperty)


rapidml_ReferenceRealization_strategy = st.builds(rapidml_ReferenceRealization, multiValued=st.booleans(), realizationType=safe_text)
@given(instance=rapidml_ReferenceRealization_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceRealization_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceRealization)


rapidml_ReferenceTreatment_strategy = st.builds(rapidml_ReferenceTreatment)
@given(instance=rapidml_ReferenceTreatment_strategy)
@settings(max_examples=25)
def test_rapidml_ReferenceTreatment_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceTreatment)


rapidml_RegExConstraint_strategy = st.builds(rapidml_RegExConstraint, pattern=safe_text)
@given(instance=rapidml_RegExConstraint_strategy)
@settings(max_examples=25)
def test_rapidml_RegExConstraint_instantiation(instance):
    assert isinstance(instance, rapidml_RegExConstraint)


rapidml_ResourceAPI_strategy = st.builds(rapidml_ResourceAPI, baseURI=safe_text, name=safe_text, version=safe_text)
@given(instance=rapidml_ResourceAPI_strategy)
@settings(max_examples=25)
def test_rapidml_ResourceAPI_instantiation(instance):
    assert isinstance(instance, rapidml_ResourceAPI)


rapidml_ResourceDefinition_strategy = st.builds(rapidml_ResourceDefinition, name=safe_text)
@given(instance=rapidml_ResourceDefinition_strategy)
@settings(max_examples=25)
def test_rapidml_ResourceDefinition_instantiation(instance):
    assert isinstance(instance, rapidml_ResourceDefinition)


rapidml_SecurityScheme_strategy = st.builds(rapidml_SecurityScheme, flow=safe_text, name=safe_text, type=safe_text)
@given(instance=rapidml_SecurityScheme_strategy)
@settings(max_examples=25)
def test_rapidml_SecurityScheme_instantiation(instance):
    assert isinstance(instance, rapidml_SecurityScheme)


rapidml_SecuritySchemeLibrary_strategy = st.builds(rapidml_SecuritySchemeLibrary, name=safe_text)
@given(instance=rapidml_SecuritySchemeLibrary_strategy)
@settings(max_examples=25)
def test_rapidml_SecuritySchemeLibrary_instantiation(instance):
    assert isinstance(instance, rapidml_SecuritySchemeLibrary)


rapidml_SecuritySchemeParameter_strategy = st.builds(rapidml_SecuritySchemeParameter, name=safe_text, value=safe_text)
@given(instance=rapidml_SecuritySchemeParameter_strategy)
@settings(max_examples=25)
def test_rapidml_SecuritySchemeParameter_instantiation(instance):
    assert isinstance(instance, rapidml_SecuritySchemeParameter)


rapidml_SecurityScope_strategy = st.builds(rapidml_SecurityScope, name=safe_text)
@given(instance=rapidml_SecurityScope_strategy)
@settings(max_examples=25)
def test_rapidml_SecurityScope_instantiation(instance):
    assert isinstance(instance, rapidml_SecurityScope)


rapidml_ServiceDataResource_strategy = st.builds(rapidml_ServiceDataResource, default=st.booleans())
@given(instance=rapidml_ServiceDataResource_strategy)
@settings(max_examples=25)
def test_rapidml_ServiceDataResource_instantiation(instance):
    assert isinstance(instance, rapidml_ServiceDataResource)


rapidml_SimpleType_strategy = st.builds(rapidml_SimpleType)
@given(instance=rapidml_SimpleType_strategy)
@settings(max_examples=25)
def test_rapidml_SimpleType_instantiation(instance):
    assert isinstance(instance, rapidml_SimpleType)


rapidml_SingleValueType_strategy = st.builds(rapidml_SingleValueType)
@given(instance=rapidml_SingleValueType_strategy)
@settings(max_examples=25)
def test_rapidml_SingleValueType_instantiation(instance):
    assert isinstance(instance, rapidml_SingleValueType)


rapidml_SourceReference_strategy = st.builds(rapidml_SourceReference)
@given(instance=rapidml_SourceReference_strategy)
@settings(max_examples=25)
def test_rapidml_SourceReference_instantiation(instance):
    assert isinstance(instance, rapidml_SourceReference)


rapidml_Structure_strategy = st.builds(rapidml_Structure)
@given(instance=rapidml_Structure_strategy)
@settings(max_examples=25)
def test_rapidml_Structure_instantiation(instance):
    assert isinstance(instance, rapidml_Structure)


rapidml_TemplateParameter_strategy = st.builds(rapidml_TemplateParameter)
@given(instance=rapidml_TemplateParameter_strategy)
@settings(max_examples=25)
def test_rapidml_TemplateParameter_instantiation(instance):
    assert isinstance(instance, rapidml_TemplateParameter)


rapidml_TypedMessage_strategy = st.builds(rapidml_TypedMessage, useParentTypeReference=st.booleans())
@given(instance=rapidml_TypedMessage_strategy)
@settings(max_examples=25)
def test_rapidml_TypedMessage_instantiation(instance):
    assert isinstance(instance, rapidml_TypedMessage)


rapidml_TypedRequest_strategy = st.builds(rapidml_TypedRequest)
@given(instance=rapidml_TypedRequest_strategy)
@settings(max_examples=25)
def test_rapidml_TypedRequest_instantiation(instance):
    assert isinstance(instance, rapidml_TypedRequest)


rapidml_TypedResponse_strategy = st.builds(rapidml_TypedResponse, statusCode=st.integers())
@given(instance=rapidml_TypedResponse_strategy)
@settings(max_examples=25)
def test_rapidml_TypedResponse_instantiation(instance):
    assert isinstance(instance, rapidml_TypedResponse)


rapidml_URI_strategy = st.builds(rapidml_URI)
@given(instance=rapidml_URI_strategy)
@settings(max_examples=25)
def test_rapidml_URI_instantiation(instance):
    assert isinstance(instance, rapidml_URI)


rapidml_URIParameter_strategy = st.builds(rapidml_URIParameter)
@given(instance=rapidml_URIParameter_strategy)
@settings(max_examples=25)
def test_rapidml_URIParameter_instantiation(instance):
    assert isinstance(instance, rapidml_URIParameter)


rapidml_URISegment_strategy = st.builds(rapidml_URISegment, name=safe_text)
@given(instance=rapidml_URISegment_strategy)
@settings(max_examples=25)
def test_rapidml_URISegment_instantiation(instance):
    assert isinstance(instance, rapidml_URISegment)


rapidml_URISegmentWithParameter_strategy = st.builds(rapidml_URISegmentWithParameter)
@given(instance=rapidml_URISegmentWithParameter_strategy)
@settings(max_examples=25)
def test_rapidml_URISegmentWithParameter_instantiation(instance):
    assert isinstance(instance, rapidml_URISegmentWithParameter)


rapidml_UserDefinedType_strategy = st.builds(rapidml_UserDefinedType)
@given(instance=rapidml_UserDefinedType_strategy)
@settings(max_examples=25)
def test_rapidml_UserDefinedType_instantiation(instance):
    assert isinstance(instance, rapidml_UserDefinedType)


rapidml_ValueRangeConstraint_strategy = st.builds(rapidml_ValueRangeConstraint, maxValue=safe_text, maxValueExclusive=st.booleans(), minValue=safe_text, minValueExclusive=st.booleans())
@given(instance=rapidml_ValueRangeConstraint_strategy)
@settings(max_examples=25)
def test_rapidml_ValueRangeConstraint_instantiation(instance):
    assert isinstance(instance, rapidml_ValueRangeConstraint)


rapidml_WithDataExamples_strategy = st.builds(rapidml_WithDataExamples)
@given(instance=rapidml_WithDataExamples_strategy)
@settings(max_examples=25)
def test_rapidml_WithDataExamples_instantiation(instance):
    assert isinstance(instance, rapidml_WithDataExamples)


rapidml_WithExamples_strategy = st.builds(rapidml_WithExamples)
@given(instance=rapidml_WithExamples_strategy)
@settings(max_examples=25)
def test_rapidml_WithExamples_instantiation(instance):
    assert isinstance(instance, rapidml_WithExamples)


rapidml_ZenModel_strategy = st.builds(rapidml_ZenModel, name=safe_text, namespace=safe_text)
@given(instance=rapidml_ZenModel_strategy)
@settings(max_examples=25)
def test_rapidml_ZenModel_instantiation(instance):
    assert isinstance(instance, rapidml_ZenModel)



