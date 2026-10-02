#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AuthenticationFlows,
    AuthenticationTypes,
    CollectionRealizationEnum,
    CollectionRealizationLevelEnum,
    ConstrainableType,
    Constraint,
    DataExample,
    DataType,
    Documentable,
    Element,
    Enum,
    Example,
    Extensible,
    Feature,
    HTTPMethods,
    HasSecurityValue,
    HasStringValue,
    HasTitle,
    HttpMessageParameterLocation,
    Inheritable,
    ObjectRealization,
    Parameter,
    RESTElement,
    RealizationContainer,
    ReferenceElement,
    ReferenceRealizationEnum,
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
    abstractmethod,
    date,
    datetime,
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
    time,
)


def test_0():
    var_0 = python_code_.rapidml_RESTElement
    var_1 = python_code_.rapidml_SingleValueType(rapidml_SingleValueType=var_0)
    assert isinstance(var_1, python_code_.rapidml_SingleValueType)
    var_2 = var_1.getPrimitiveType()
    var_3 = True
    var_4 = python_code_.rapidml_Feature(
        name=var_2, restriction=b"\x0c\xc9\x01\x04\xbb", readOnly=var_3, key=-1011.39
    )
    assert isinstance(var_4, python_code_.rapidml_Feature)
    var_5 = python_code_.rapidml_NamedLinkDescriptor(name=var_0, default=var_1)
    assert isinstance(var_5, python_code_.rapidml_NamedLinkDescriptor)
    var_6 = '/DQRM*i"'
    var_7 = "9"
    var_8 = python_code_.rapidml_LinkRelationsLibrary(
        name=var_7, rapidml_LinkRelationsLibrary=var_7
    )
    var_9 = python_code_.rapidml_LinkRelation(
        specURL=var_4, name=var_6, rapidml_LinkRelation130=var_8
    )
    assert isinstance(var_9, python_code_.rapidml_LinkRelation)
    var_10 = python_code_.rapidml_TypedMessage(useParentTypeReference=-405.06)
    assert isinstance(var_10, python_code_.rapidml_TypedMessage)


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "k\\ZP&y~\\{4'Y!\t0MT"
    var_1 = python_code_.rapidml_Element(cardinality=var_0)
    assert isinstance(var_1, python_code_.rapidml_Element)
    var_2 = var_1.getMinOccurs()
    var_3 = False
    var_4 = python_code_.rapidml_ReferenceProperty(containment=var_3, container=var_3)
    assert isinstance(var_4, python_code_.rapidml_ReferenceProperty)
    var_5 = dict
    var_6 = python_code_.rapidml_Example
    var_7 = '"\x0bl; '
    var_8 = python_code_.rapidml_Parameter(
        name=var_5, required=var_2, default=var_6, fixed=var_7
    )
    assert isinstance(var_8, python_code_.rapidml_Parameter)
    var_9 = python_code_.rapidml_AuthenticationMethod()
    var_10 = python_code_.rapidml_SecurityScope(
        name=var_0, rapidml_SecurityScope112=var_9
    )
    assert isinstance(var_10, python_code_.rapidml_SecurityScope)
    var_12 = python_code_.rapidml_PathSegment()
    var_13 = python_code_.rapidml_ReferenceElement(rapidml_ReferenceElement80=var_12)
    assert isinstance(var_13, python_code_.rapidml_ReferenceElement)
    python_code_.rapidml_Structure(
        containingDataType=var_6, rapidml_Structure163=var_13
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "k\\ZP&y~\\{4'Y!\t0MT"
    var_1 = python_code_.rapidml_Element(cardinality=var_0)
    assert isinstance(var_1, python_code_.rapidml_Element)
    var_2 = var_1.getMinOccurs()
    var_3 = False
    var_4 = python_code_.rapidml_ReferenceProperty(containment=var_3, container=var_3)
    assert isinstance(var_4, python_code_.rapidml_ReferenceProperty)
    var_5 = dict
    var_6 = python_code_.rapidml_Example
    var_7 = '"\x0bl; '
    var_8 = python_code_.rapidml_Parameter(
        name=var_5, required=var_2, default=var_6, fixed=var_7
    )
    assert isinstance(var_8, python_code_.rapidml_Parameter)
    var_11 = python_code_.rapidml_SecuritySchemeLibrary(
        name=var_1, rapidml_SecuritySchemeLibrary=var_5
    )
    assert isinstance(var_11, python_code_.rapidml_SecuritySchemeLibrary)
    var_12 = python_code_.rapidml_PathSegment()
    var_13 = python_code_.rapidml_ReferenceElement(rapidml_ReferenceElement80=var_12)
    assert isinstance(var_13, python_code_.rapidml_ReferenceElement)
    var_15 = python_code_.rapidml_RegExConstraint(pattern=var_7)
    assert isinstance(var_15, python_code_.rapidml_RegExConstraint)
    var_1.isMultiValued()
    python_code_.rapidml_ObjectRealization(
        rapidml_ObjectRealization=var_3, ObjectRealization=2697
    )


def test_3():
    var_0 = "\x0c NVqla2p~M)igK"
    var_1 = python_code_.rapidml_MediaType(
        name="361;dtf",
        specURL=var_0,
        rapidml_MediaType59=None,
        rapidml_MediaType4=None,
        rapidml_MediaType12=var_0,
        rapidml_MediaType19=set(),
    )
    assert isinstance(var_1, python_code_.rapidml_MediaType)
    var_2 = python_code_.rapidml_ObjectRealization
    var_1.equals(rapidml_other=var_2)
    var_15 = {True, 527.91, 141}
    var_16 = python_code_.rapidml_PropertyRealization(cardinality=var_15)
    assert isinstance(var_16, python_code_.rapidml_PropertyRealization)
    var_16.getPrimitiveType()
    var_19 = python_code_.rapidml_ReferenceTreatment(rapidml_ReferenceTreatment=set())
    assert isinstance(var_19, python_code_.rapidml_ReferenceTreatment)
    var_19.getLinkDescriptor()
    python_code_.rapidml_ReferenceElement()


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = "rapidml_ReferenceElementDELETE_rapidml_URIParameter__uriParameters"
    var_1 = True
    var_2 = "rapidml_ZenModel41:_rapidml_DataType__rapidml_DataType:rapidml_WithExamples:rapidml_ResourceDefinition50"
    var_3 = python_code_.rapidml_PrimitiveTypesLibrary(name=var_2)
    var_4 = python_code_.rapidml_PrimitiveType(rapidml_PrimitiveType133=var_3)
    assert isinstance(var_4, python_code_.rapidml_PrimitiveType)
    var_5 = var_4.getPrimitiveType()
    var_6 = python_code_.rapidml_ObjectRealization(rapidml_ObjectRealization93=var_5)
    assert isinstance(var_6, python_code_.rapidml_ObjectRealization)
    var_7 = python_code_.rapidml_PropertyRealization(
        cardinality=var_0,
        rapidml_PropertyRealization91=var_6,
        rapidml_PropertyRealization94=var_6,
    )
    assert isinstance(var_7, python_code_.rapidml_PropertyRealization)
    python_code_.rapidml_Feature(
        name=var_0, restriction=var_1, readOnly=var_0, key=False, rapidml_Feature=var_7
    )


def test_5():
    var_0 = python_code_.rapidml_InlineDataExample(body={False, -309})
    assert isinstance(var_0, python_code_.rapidml_InlineDataExample)
    var_10 = False
    var_11 = python_code_.rapidml_URISegment
    var_12 = python_code_.rapidml_TypedMessage(
        useParentTypeReference=var_10, rapidml_TypedMessage=var_11
    )
    assert isinstance(var_12, python_code_.rapidml_TypedMessage)
    var_35 = '\x0c"cD6?'
    var_36 = python_code_.rapidml_PropertyRealization(
        cardinality=var_35, rapidml_PropertyRealization=var_11
    )
    assert isinstance(var_36, python_code_.rapidml_PropertyRealization)
    var_14 = ""
    python_code_.rapidml_ObjectRealization()
    var_22 = python_code_.rapidml_Element(cardinality=None)
    assert isinstance(var_22, python_code_.rapidml_Element)
    var_22.getMinOccurs()
    var_25 = python_code_.rapidml_ReferenceRealization(
        realizationType=var_14, multiValued=(), rapidml_ReferenceRealization73=var_11
    )
    assert isinstance(var_25, python_code_.rapidml_ReferenceRealization)
    var_28 = python_code_.rapidml_SourceReference(
        SourceReference=var_11, sourceReference={-5207, True, False}
    )
    assert isinstance(var_28, python_code_.rapidml_SourceReference)
    var_28.getPrimitiveType()


@pytest.mark.xfail(strict=True)
def test_6():
    var_5 = python_code_.rapidml_HasStringValue()
    python_code_.rapidml_ReferenceElement()
    var_8 = python_code_.rapidml_PrimitiveType(rapidml_PrimitiveType={883})
    assert isinstance(var_8, python_code_.rapidml_PrimitiveType)
    python_code_.rapidml_ServiceDataResource(
        default=var_5, rapidml_ServiceDataResource=var_8
    )


def test_7():
    var_3 = "u\x0cc<acVsXP"
    var_4 = True
    var_5 = python_code_.rapidml_ReferenceRealization(
        realizationType=var_3, multiValued=var_4, rapidml_ReferenceRealization=-1
    )
    assert isinstance(var_5, python_code_.rapidml_ReferenceRealization)
    var_23 = python_code_.rapidml_TypedResponse(statusCode=var_4)
    assert isinstance(var_23, python_code_.rapidml_TypedResponse)
    python_code_.rapidml_SourceReference()
    var_26 = python_code_.rapidml_ReferenceElement(rapidml_ReferenceElement80=set())
    assert isinstance(var_26, python_code_.rapidml_ReferenceElement)
    var_26.getName()


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = lambda *args, **kwargs: True
    var_1 = python_code_.rapidml_LinkRelationsLibrary(name=var_0)
    python_code_.rapidml_ZenModel(
        name={2252.5},
        namespace={},
        rapidml_ZenModel37=-827.54,
        rapidml_ZenModel39=None,
        rapidml_ZenModel41=var_1,
    )


def test_9():
    var_1 = True
    var_2 = python_code_.rapidml_TypedMessage(useParentTypeReference=var_1)
    assert isinstance(var_2, python_code_.rapidml_TypedMessage)
    var_3 = python_code_.rapidml_RESTElement()
    var_5 = python_code_.rapidml_SecuritySchemeLibrary(
        name=var_3, rapidml_SecuritySchemeLibrary={}
    )
    assert isinstance(var_5, python_code_.rapidml_SecuritySchemeLibrary)
    python_code_.rapidml_ReferenceEmbed()
    python_code_.rapidml_ObjectRealization()
    var_18 = python_code_.rapidml_Element(cardinality=None)
    assert isinstance(var_18, python_code_.rapidml_Element)
    var_18.getMinOccurs()


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = ":Sh-Rn`#T9CKl5rk"
    var_1 = python_code_.rapidml_MediaType(
        name=(1432.33,),
        specURL=var_0,
        rapidml_MediaType56=-2816.83,
        rapidml_MediaType59=b"\xc0\xdeX\xfd\x04\x90\x12\xe1\x85",
    )
    assert isinstance(var_1, python_code_.rapidml_MediaType)
    var_2 = python_code_.rapidml_ObjectRealization
    var_1.equals(rapidml_other=var_2)
    var_4 = True
    var_5 = python_code_.rapidml_ReferenceTreatment(
        rapidml_ReferenceTreatment72=["XQ", 1364.49]
    )
    assert isinstance(var_5, python_code_.rapidml_ReferenceTreatment)
    python_code_.rapidml_ReferenceRealization(
        realizationType=-401,
        multiValued=var_4,
        rapidml_ReferenceRealization70=var_5,
        rapidml_ReferenceRealization75=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = python_code_.rapidml_InlineDataExample(body={False, -309})
    assert isinstance(var_0, python_code_.rapidml_InlineDataExample)
    var_3 = "U]:}, fhTz>z"
    var_4 = True
    var_5 = python_code_.rapidml_ReferenceRealization(
        realizationType=var_3, multiValued=var_4, rapidml_ReferenceRealization73=var_4
    )
    assert isinstance(var_5, python_code_.rapidml_ReferenceRealization)
    python_code_.rapidml_ReferenceTreatment(rapidml_ReferenceTreatment72=var_5)


@pytest.mark.xfail(strict=True)
def test_12():
    var_2 = python_code_.rapidml_WithDataExamples()
    var_3 = "u\x0cc<acVsXP"
    var_4 = True
    var_5 = python_code_.rapidml_ReferenceRealization(
        realizationType=var_3, multiValued=var_4, rapidml_ReferenceRealization=-1
    )
    assert isinstance(var_5, python_code_.rapidml_ReferenceRealization)
    var_6 = "I7siV4Mi~"
    var_7 = python_code_.rapidml_PropertyRealization(cardinality=var_6)
    assert isinstance(var_7, python_code_.rapidml_PropertyRealization)
    var_7.getPrimitiveType()
    var_9 = python_code_.URIParameter
    var_10 = python_code_.rapidml_RealizationContainer(
        withDefaultRealization=var_4,
        realizationName=var_2,
        effectiveRealization=var_6,
        rapidml_RealizationContainer=var_9,
    )
    assert isinstance(var_10, python_code_.rapidml_RealizationContainer)
    python_code_.rapidml_ObjectRealization(ObjectRealization=var_10)


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = python_code_.rapidml_RESTElement
    var_1 = python_code_.rapidml_SingleValueType(rapidml_SingleValueType=var_0)
    assert isinstance(var_1, python_code_.rapidml_SingleValueType)
    var_2 = var_1.getPrimitiveType()
    var_3 = True
    var_4 = python_code_.rapidml_Feature(
        name=var_2, restriction=b"\x0c\xc9\x01\x04\xbb", readOnly=var_3, key=-1011.39
    )
    assert isinstance(var_4, python_code_.rapidml_Feature)
    var_5 = python_code_.rapidml_NamedLinkDescriptor(name=var_0, default=var_1)
    assert isinstance(var_5, python_code_.rapidml_NamedLinkDescriptor)
    var_6 = '/DQRM*i"'
    var_7 = "P"
    var_8 = python_code_.rapidml_LinkRelationsLibrary(
        name=var_7, rapidml_LinkRelationsLibrary=var_7
    )
    var_9 = python_code_.rapidml_LinkRelation(
        specURL=var_4, name=var_6, rapidml_LinkRelation130=var_8
    )
    assert isinstance(var_9, python_code_.rapidml_LinkRelation)
    var_10 = python_code_.rapidml_TypedMessage(useParentTypeReference=-405.06)
    assert isinstance(var_10, python_code_.rapidml_TypedMessage)
    var_11 = var_1.getPrimitiveType()
    var_12 = "`yjxx\"y0Ca$+8%'"
    var_13 = python_code_.rapidml_RealizationContainer(
        withDefaultRealization=-1395,
        realizationName={"rapidml_SecuritySchemeLibrary114", True},
        effectiveRealization=var_12,
        RealizationContainer=var_0,
    )
    assert isinstance(var_13, python_code_.rapidml_RealizationContainer)
    python_code_.rapidml_ObjectRealization(
        rapidml_ObjectRealization=var_11, rapidml_ObjectRealization118=var_13
    )


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = python_code_.rapidml_TemplateParameter()
    var_1 = False
    var_2 = True
    var_3 = python_code_.rapidml_Feature(
        name=var_0, restriction=var_0, readOnly=var_1, key=var_2, rapidml_Feature=()
    )
    assert isinstance(var_3, python_code_.rapidml_Feature)
    var_4 = python_code_.rapidml_Method
    var_5 = python_code_.rapidml_TypedRequest()
    python_code_.rapidml_Method(
        id=var_4, httpMethod=True, containingMethod=var_5, containingMethod15=var_1
    )


def test_15():
    var_1 = True
    var_2 = python_code_.rapidml_TypedMessage(useParentTypeReference=var_1)
    assert isinstance(var_2, python_code_.rapidml_TypedMessage)
    var_3 = python_code_.rapidml_RESTElement()
    var_5 = python_code_.rapidml_SecuritySchemeLibrary(
        name=var_3, rapidml_SecuritySchemeLibrary={}
    )
    assert isinstance(var_5, python_code_.rapidml_SecuritySchemeLibrary)
    var_6 = python_code_.rapidml_ReferenceEmbed()
    var_6.getNestedReferenceTreatments()


def test_16():
    var_1 = "?%]p:c\tn:"
    var_2 = python_code_.rapidml_Element(cardinality=var_1)
    assert isinstance(var_2, python_code_.rapidml_Element)
    var_2.getDataType()
