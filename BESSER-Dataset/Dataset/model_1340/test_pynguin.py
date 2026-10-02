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
    AnnotationElementCS,
    ClassifierCS,
    ElementCS,
    ElementRefCS,
    Enum,
    FeatureCS,
    IteratorKind,
    ModelElementCS,
    MultiplicityCS,
    Nameable,
    NamedElementCS,
    NamespaceCS,
    PackageOwnerCS,
    PathElementCS,
    Pivotable,
    PivotableElementCS,
    RootCS,
    StructuralFeatureCS,
    TemplateParameterCS,
    TemplateableElementCS,
    TypeCS,
    TypeRefCS,
    TypedElementCS,
    TypedRefCS,
    VisitableCS,
    abstractmethod,
    basecs_AnnotationCS,
    basecs_AnnotationElementCS,
    basecs_AttributeCS,
    basecs_ClassCS,
    basecs_ClassifierCS,
    basecs_ConstraintCS,
    basecs_DataTypeCS,
    basecs_DetailCS,
    basecs_DocumentationCS,
    basecs_EClassifier,
    basecs_Element,
    basecs_ElementCS,
    basecs_ElementRefCS,
    basecs_EnumerationCS,
    basecs_EnumerationLiteralCS,
    basecs_FeatureCS,
    basecs_ImportCS,
    basecs_LambdaTypeCS,
    basecs_LibraryCS,
    basecs_ModelElementCS,
    basecs_ModelElementRefCS,
    basecs_MultiplicityBoundsCS,
    basecs_MultiplicityCS,
    basecs_MultiplicityStringCS,
    basecs_NamedElementCS,
    basecs_Namespace,
    basecs_NamespaceCS,
    basecs_OperationCS,
    basecs_PackageCS,
    basecs_PackageOwnerCS,
    basecs_ParameterCS,
    basecs_PathElementCS,
    basecs_PathElementWithURICS,
    basecs_PathNameCS,
    basecs_PivotableElementCS,
    basecs_PrimitiveTypeRefCS,
    basecs_Property,
    basecs_ReferenceCS,
    basecs_RootCS,
    basecs_RootPackageCS,
    basecs_SpecificationCS,
    basecs_StructuralFeatureCS,
    basecs_TemplateBindingCS,
    basecs_TemplateParameterCS,
    basecs_TemplateParameterSubstitutionCS,
    basecs_TemplateSignatureCS,
    basecs_TemplateableElementCS,
    basecs_TuplePartCS,
    basecs_TupleTypeCS,
    basecs_Type,
    basecs_TypeCS,
    basecs_TypeParameterCS,
    basecs_TypeRefCS,
    basecs_TypedElementCS,
    basecs_TypedRefCS,
    basecs_TypedTypeRefCS,
    basecs_VisitableCS,
    basecs_WildcardTypeRefCS,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.PivotableElementCS()
    var_1 = python_code_.TemplateParameterCS()
    var_3 = python_code_.basecs_ParameterCS(ParameterCS=None, ownedParameter=var_0)
    assert isinstance(var_3, python_code_.basecs_ParameterCS)
    var_3.ast()
    python_code_.basecs_OperationCS(
        owner45=set(),
        basecs_OperationCS=set(),
        basecs_OperationCS49={-55.84, -2487.61, var_1},
        OperationCS61=var_3,
    )


def test_1():
    python_code_.basecs_ParameterCS()


def test_2():
    var_0 = 1857.19
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName="/",
        qualifier="basecs_TypedTypeRefCS,_basecs_OperationCS__owner45,_basecs_LambdaTypeCS__basecs_LambdaTypeCS28,basecs_ParameterCS",
        ownedType=var_0,
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_20 = python_code_.basecs_ParameterCS(ownedParameter=-1544)
    assert isinstance(var_20, python_code_.basecs_ParameterCS)
    var_21 = "QCqb"
    var_22 = python_code_.basecs_ConstraintCS(stereotype=var_21)
    assert isinstance(var_22, python_code_.basecs_ConstraintCS)
    var_50 = 1727
    var_51 = python_code_.basecs_EnumerationCS()
    var_52 = python_code_.basecs_EnumerationLiteralCS(
        value=var_50,
        basecs_EnumerationLiteralCS=complex(1920.3941, 635.68),
        basecs_EnumerationLiteralCS21=var_51,
    )
    assert isinstance(var_52, python_code_.basecs_EnumerationLiteralCS)


def test_3():
    python_code_.basecs_EnumerationCS()
    var_39 = python_code_.basecs_MultiplicityCS()
    var_39.getLower()


def test_4():
    var_6 = python_code_.basecs_OperationCS(
        owner45=set(),
        basecs_OperationCS49=set(),
        basecs_OperationCS52=set(),
        OperationCS61=None,
        ownedOperation=None,
    )
    assert isinstance(var_6, python_code_.basecs_OperationCS)


def test_5():
    var_9 = python_code_.basecs_ClassCS()
    var_10 = python_code_.basecs_OperationCS(
        OperationCS=var_9,
        basecs_OperationCS55="basecs_ClassifierCS:_basecs_SpecificationCS__basecs_SpecificationCS16:_basecs_ClassifierCS__ownedType",
        OperationCS61=var_9,
    )
    assert isinstance(var_10, python_code_.basecs_OperationCS)


def test_6():
    var_39 = python_code_.basecs_SpecificationCS(
        exprString=-1398, basecs_SpecificationCS16=None
    )
    assert isinstance(var_39, python_code_.basecs_SpecificationCS)
    var_41 = python_code_.basecs_OperationCS(
        owner45={False},
        basecs_OperationCS49={-1090, -587.44},
        basecs_OperationCS52=set(),
        basecs_OperationCS55=set(),
    )
    assert isinstance(var_41, python_code_.basecs_OperationCS)


def test_7():
    var_38 = python_code_.basecs_EnumerationCS(
        basecs_EnumerationCS={"\x0c]Trb\nXon\\p$WFw}kP"}
    )
    assert isinstance(var_38, python_code_.basecs_EnumerationCS)
    var_39 = python_code_.FeatureCS
    var_40 = "basecs_SpecificationCS16"
    var_41 = python_code_.basecs_PackageCS(nsPrefix=var_38, nsURI=var_40, owner58=[])
    assert isinstance(var_41, python_code_.basecs_PackageCS)
    var_42 = python_code_.basecs_ClassifierCS(
        instanceClassName=var_38, qualifier=var_39, ClassifierCS=var_41
    )
    assert isinstance(var_42, python_code_.basecs_ClassifierCS)
    var_42.ast()


def test_8():
    var_8 = python_code_.basecs_PackageCS(
        nsPrefix=".uV,\tj", nsURI="[d]", PackageCS=None, basecs_PackageCS=None
    )
    assert isinstance(var_8, python_code_.basecs_PackageCS)


def test_9():
    var_9 = "_basecs_PathNameCS__PathNameCS"
    var_10 = lambda *args, **kwargs: True
    var_11 = python_code_.basecs_PackageCS(
        nsPrefix=var_9, nsURI=-375.64, basecs_PackageCS=var_10
    )
    assert isinstance(var_11, python_code_.basecs_PackageCS)
    var_11.ast()


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=var_0, qualifier="H:Pq5#-B"
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    python_code_.basecs_PackageCS(
        nsPrefix="basecs_TypedRefCS107", nsURI=var_0, PackageCS=var_1
    )


def test_11():
    var_0 = python_code_.basecs_DataTypeCS()
    var_55 = "Pa^>q"
    var_56 = python_code_.basecs_PackageCS(
        nsPrefix=var_0, nsURI=var_55, PackageCS=False, basecs_PackageCS=var_55
    )
    assert isinstance(var_56, python_code_.basecs_PackageCS)


def test_12():
    python_code_.basecs_EnumerationCS()
    var_55 = "basecs_TypedRefCS32"
    var_57 = python_code_.basecs_ImportCS(all=True)
    assert isinstance(var_57, python_code_.basecs_ImportCS)
    var_58 = python_code_.basecs_PackageCS(
        nsPrefix=var_55,
        nsURI=var_55,
        basecs_PackageCS={
            "_basecs_ElementCS__basecs_ElementCS:_basecs_ParameterCS__ownedParameter",
            False,
            0,
        },
    )
    assert isinstance(var_58, python_code_.basecs_PackageCS)
    var_58.getClassifier(basecs_name=True)
    var_65 = python_code_.basecs_MultiplicityStringCS(
        stringBounds="_basecs_ImportCS__basecs_ImportCS24"
    )
    assert isinstance(var_65, python_code_.basecs_MultiplicityStringCS)


@pytest.mark.xfail(strict=True)
def test_13():
    var_1 = python_code_.basecs_ElementCS()
    var_2 = var_1.getDescription()
    var_4 = "basecs_TypedRefCS32"
    var_5 = python_code_.basecs_PrimitiveTypeRefCS(name=var_4)
    assert isinstance(var_5, python_code_.basecs_PrimitiveTypeRefCS)
    var_7 = python_code_.basecs_ImportCS(all=True)
    assert isinstance(var_7, python_code_.basecs_ImportCS)
    var_8 = python_code_.basecs_PackageCS(
        nsPrefix="](SJmsL7N\t",
        nsURI=var_4,
        owner58={"b.\x0bz.?q28S/ ^8F"},
        basecs_PackageCS=var_2,
    )
    assert isinstance(var_8, python_code_.basecs_PackageCS)
    var_9 = var_8.ast()
    var_10 = python_code_.basecs_TypedTypeRefCS()
    python_code_.basecs_PathNameCS(
        scopeFilter=(283.38, False),
        basecs_PathNameCS=var_7,
        pathName=var_9,
        basecs_PathNameCS109=var_10,
    )


def test_14():
    var_38 = python_code_.basecs_EnumerationCS(
        basecs_EnumerationCS={"\x0c]Trb\nXon\\p$WFw}kP"}
    )
    assert isinstance(var_38, python_code_.basecs_EnumerationCS)


def test_15():
    var_10 = "hTN*M\r<J[DGs\x0b#g=[&~"
    var_11 = python_code_.basecs_AnnotationElementCS()
    var_12 = python_code_.basecs_DetailCS(value=var_10, basecs_DetailCS=var_11)
    assert isinstance(var_12, python_code_.basecs_DetailCS)


def test_16():
    var_0 = 1857.19
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName="\n\x0b`U0Ibb)[g!LrywkC",
        qualifier="Parameter",
        basecs_ClassifierCS=set(),
        ownedType=var_0,
        ClassifierCS=var_0,
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_16 = python_code_.basecs_AttributeCS()
    var_17 = python_code_.basecs_TemplateSignatureCS()
    var_20 = python_code_.basecs_ParameterCS(ownedParameter=-1544)
    assert isinstance(var_20, python_code_.basecs_ParameterCS)
    var_21 = "owner58,_basecs_ParameterCS__ownedParameter"
    var_22 = python_code_.basecs_ConstraintCS(stereotype=var_21)
    assert isinstance(var_22, python_code_.basecs_ConstraintCS)
    var_28 = python_code_.basecs_ClassifierCS(instanceClassName=[], qualifier=var_16)
    var_34 = python_code_.basecs_MultiplicityCS()
    var_37 = python_code_.basecs_DocumentationCS(value=var_21)
    assert isinstance(var_37, python_code_.basecs_DocumentationCS)
    var_38 = python_code_.basecs_ClassCS()
    var_39 = var_28.ast()
    var_40 = var_34.getUpper()
    var_41 = python_code_.basecs_OperationCS(
        OperationCS=var_38,
        owner45=var_39,
        basecs_OperationCS52=var_40,
        ownedOperation=var_17,
    )
    assert isinstance(var_41, python_code_.basecs_OperationCS)
    var_41.ast()
    var_46 = python_code_.basecs_ElementCS(basecs_ElementCS18=var_17)
    assert isinstance(var_46, python_code_.basecs_ElementCS)


def test_17():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)


def test_18():
    var_2 = ">B}.)"
    var_4 = python_code_.basecs_ParameterCS(ParameterCS=var_2)
    assert isinstance(var_4, python_code_.basecs_ParameterCS)
    var_12 = python_code_.basecs_ModelElementCS(originalXmiId=var_2, csi=var_2)
    assert isinstance(var_12, python_code_.basecs_ModelElementCS)
    var_19 = lambda *args, **kwargs: 580
    var_20 = python_code_.basecs_EnumerationLiteralCS(
        value=b"a\xdb\xcd\x9c\xa0\x84\xb0\xe1\x12\xd2Z\x1bw6E\x8a",
        basecs_EnumerationLiteralCS21=var_19,
    )
    assert isinstance(var_20, python_code_.basecs_EnumerationLiteralCS)
    var_21 = ""
    var_22 = python_code_.basecs_ClassifierCS(instanceClassName=var_2, qualifier=var_21)
    assert isinstance(var_22, python_code_.basecs_ClassifierCS)


def test_19():
    var_2 = ">B}.)"
    var_3 = python_code_.TypedRefCS
    var_4 = python_code_.basecs_ParameterCS(ParameterCS=var_2)
    assert isinstance(var_4, python_code_.basecs_ParameterCS)
    var_5 = var_4.ast()
    var_6 = python_code_.basecs_ClassifierCS(
        instanceClassName=var_2,
        qualifier=var_3,
        basecs_ClassifierCS=var_5,
        ownedType=var_4,
    )
    assert isinstance(var_6, python_code_.basecs_ClassifierCS)
    var_8 = python_code_.basecs_StructuralFeatureCS(
        default=var_6, basecs_StructuralFeatureCS=b"\xc0"
    )
    assert isinstance(var_8, python_code_.basecs_StructuralFeatureCS)
    var_9 = python_code_.basecs_SpecificationCS(
        exprString=var_4,
        basecs_SpecificationCS=-1480.42,
        basecs_SpecificationCS88=var_8,
    )
    assert isinstance(var_9, python_code_.basecs_SpecificationCS)
    var_12 = python_code_.basecs_ModelElementCS(originalXmiId=var_2, csi=var_2)
    assert isinstance(var_12, python_code_.basecs_ModelElementCS)
    var_17 = -3132
    var_18 = python_code_.basecs_EnumerationLiteralCS(value=var_17)
    assert isinstance(var_18, python_code_.basecs_EnumerationLiteralCS)


def test_20():
    var_5 = python_code_.basecs_ParameterCS()
    var_5.ast()


def test_21():
    python_code_.basecs_EnumerationCS()
    python_code_.basecs_MultiplicityCS()
    var_42 = python_code_.basecs_PathElementCS()
    var_43 = python_code_.basecs_ParameterCS()
    var_43.ast()
    var_45 = python_code_.basecs_PathNameCS(
        scopeFilter=b"\xe0\xd5.W", PathNameCS=var_42
    )
    assert isinstance(var_45, python_code_.basecs_PathNameCS)
    var_48 = python_code_.basecs_MultiplicityStringCS(stringBounds=var_42)
    assert isinstance(var_48, python_code_.basecs_MultiplicityStringCS)


def test_22():
    var_43 = python_code_.basecs_MultiplicityBoundsCS(
        lowerBound=2666, upperBound="c||+w{"
    )
    assert isinstance(var_43, python_code_.basecs_MultiplicityBoundsCS)
    var_46 = lambda *args, **kwargs: "&Pbx zm`\ty8XB'Z"
    var_47 = "\rY"
    var_48 = python_code_.basecs_TypedElementCS(
        optional=var_46, qualifier=var_47, basecs_TypedElementCS=var_43
    )
    assert isinstance(var_48, python_code_.basecs_TypedElementCS)


def test_23():
    python_code_.basecs_EnumerationCS()
    var_38 = "u2cPcT-\\a"
    var_39 = python_code_.basecs_NamedElementCS(name=var_38)
    assert isinstance(var_39, python_code_.basecs_NamedElementCS)
    var_59 = python_code_.basecs_ParameterCS(ownedParameter=b"\x81\xc7\x1a")
    assert isinstance(var_59, python_code_.basecs_ParameterCS)
    var_59.ast()


def test_24():
    python_code_.basecs_ElementCS()
    var_61 = python_code_.basecs_TypedRefCS()
    var_62 = python_code_.basecs_MultiplicityCS(basecs_MultiplicityCS=var_61)
    assert isinstance(var_62, python_code_.basecs_MultiplicityCS)
    var_66 = python_code_.basecs_PrimitiveTypeRefCS(name={"lcKz"})
    assert isinstance(var_66, python_code_.basecs_PrimitiveTypeRefCS)
    var_69 = 1745
    var_70 = python_code_.basecs_EnumerationLiteralCS(value=var_69)
    assert isinstance(var_70, python_code_.basecs_EnumerationLiteralCS)
    var_70.ast()


def test_25():
    var_8 = python_code_.basecs_PackageCS(
        nsPrefix=904.6, nsURI={"owner45": True, "_": -26.5, "I-": True}
    )
    assert isinstance(var_8, python_code_.basecs_PackageCS)
    var_9 = python_code_.basecs_ClassCS()
    var_10 = python_code_.basecs_OperationCS(
        OperationCS=var_9,
        basecs_OperationCS55="basecs_ClassifierCS:_basecs_SpecificationCS__basecs_SpecificationCS16:_basecs_ClassifierCS__ownedType",
        OperationCS61=var_9,
    )
    assert isinstance(var_10, python_code_.basecs_OperationCS)
    var_10.ast()


def test_26():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_4 = python_code_.basecs_PackageCS(nsPrefix=var_0, nsURI=var_0)
    assert isinstance(var_4, python_code_.basecs_PackageCS)
    var_4.getClassifier(basecs_name=True)


def test_27():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_1.ast()
    python_code_.basecs_ElementCS()


def test_28():
    var_48 = python_code_.basecs_PathElementCS()
    var_51 = python_code_.basecs_PathNameCS(
        scopeFilter=b"\xe0\xd5.W", PathNameCS=var_48
    )
    assert isinstance(var_51, python_code_.basecs_PathNameCS)


def test_29():
    python_code_.basecs_ElementCS()


def test_30():
    python_code_.basecs_ElementCS()
    var_36 = '=ne"?\x0b&+k9<I'
    var_37 = python_code_.basecs_StructuralFeatureCS(default=var_36)
    assert isinstance(var_37, python_code_.basecs_StructuralFeatureCS)


def test_31():
    var_0 = python_code_.basecs_EClassifier()
    var_1 = python_code_.basecs_ElementCS(
        basecs_ElementCS=var_0, basecs_ElementCS18=var_0
    )
    assert isinstance(var_1, python_code_.basecs_ElementCS)
    var_2 = var_1.getDescription()
    var_3 = python_code_.basecs_StructuralFeatureCS(
        default=var_0,
        StructuralFeatureCS={
            "basecs_EnumerationCS-basecs_Element-_basecs_ConstraintCS__basecs_ConstraintCS13-_basecs_ParameterCS__ownedParameter",
            -2120.72,
        },
        basecs_StructuralFeatureCS=var_2,
    )
    assert isinstance(var_3, python_code_.basecs_StructuralFeatureCS)
    var_48 = python_code_.basecs_PathElementCS()
    var_49 = python_code_.basecs_ParameterCS()
    var_49.ast()
    var_51 = python_code_.basecs_PathNameCS(
        scopeFilter=b"\xe0\xd5.W", PathNameCS=var_48
    )
    assert isinstance(var_51, python_code_.basecs_PathNameCS)


def test_32():
    var_0 = python_code_.basecs_EClassifier()
    var_1 = python_code_.basecs_ElementCS()
    var_1.getDescription()
    var_3 = python_code_.basecs_StructuralFeatureCS(default="RAJal4\x0b")
    assert isinstance(var_3, python_code_.basecs_StructuralFeatureCS)
    var_4 = "basecs_TypedRefS32"
    var_5 = python_code_.basecs_PrimitiveTypeRefCS(name=var_4)
    assert isinstance(var_5, python_code_.basecs_PrimitiveTypeRefCS)
    var_6 = python_code_.basecs_Namespace
    var_7 = python_code_.basecs_ImportCS(all=var_0, basecs_ImportCS24=var_6)
    assert isinstance(var_7, python_code_.basecs_ImportCS)
    var_8 = python_code_.basecs_PackageCS(
        nsPrefix=var_4,
        nsURI=var_4,
        basecs_PackageCS={
            "_basecs_ElementCS__basecs_ElementCS:_basecs_ParameterCS__ownedParameter",
            False,
            0,
        },
    )
    assert isinstance(var_8, python_code_.basecs_PackageCS)
    var_35 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_4, ClassifierCS=()
    )
    assert isinstance(var_35, python_code_.basecs_ClassifierCS)


def test_33():
    var_10 = "hTN*M\r<J[DGs\x0b#g=[&~"
    var_12 = python_code_.basecs_DetailCS(value=var_10)
    assert isinstance(var_12, python_code_.basecs_DetailCS)


@pytest.mark.xfail(strict=True)
def test_34():
    var_2 = python_code_.basecs_TypedTypeRefCS
    var_34 = python_code_.basecs_DetailCS(value=var_2)
    assert isinstance(var_34, python_code_.basecs_DetailCS)
    var_12 = python_code_.basecs_ClassCS()
    var_16 = "basecs_PackageCS"
    python_code_.basecs_ModelElementCS(
        originalXmiId=var_16, csi=var_2, basecs_ModelElementCS36=var_12
    )


def test_35():
    var_55 = python_code_.basecs_EnumerationCS(basecs_EnumerationCS=())
    assert isinstance(var_55, python_code_.basecs_EnumerationCS)
    var_57 = python_code_.basecs_ModelElementCS(
        originalXmiId="_basecs_ElementCS__basecs_ElementCS73:basecs_SpecificationCS16",
        csi="cF*3",
    )
    assert isinstance(var_57, python_code_.basecs_ModelElementCS)


def test_36():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_12 = python_code_.basecs_ElementCS(
        basecs_ElementCS18=complex(1746.0627131, 1414.1291)
    )
    assert isinstance(var_12, python_code_.basecs_ElementCS)
    var_12.getDescription()
    var_15 = python_code_.basecs_PathElementWithURICS(uri=var_0)
    assert isinstance(var_15, python_code_.basecs_PathElementWithURICS)


def test_37():
    var_5 = python_code_.basecs_EnumerationCS(basecs_EnumerationCS=())
    assert isinstance(var_5, python_code_.basecs_EnumerationCS)
    var_5.ast()


@pytest.mark.xfail(strict=True)
def test_38():
    var_17 = True
    var_18 = ""
    var_19 = python_code_.basecs_TypedElementCS(optional=var_17, qualifier=var_18)
    assert isinstance(var_19, python_code_.basecs_TypedElementCS)
    var_20 = python_code_.basecs_MultiplicityStringCS(stringBounds=1399.33)
    assert isinstance(var_20, python_code_.basecs_MultiplicityStringCS)
    python_code_.basecs_MultiplicityCS()
    var_26 = "basecs_PathElementCS-_basecs_EnumerationCS__basecs_EnumerationCS"
    var_27 = lambda *args, **kwargs: True
    var_28 = python_code_.basecs_ClassifierCS(
        instanceClassName=var_26, qualifier=var_26, ownedType=112.35
    )
    assert isinstance(var_28, python_code_.basecs_ClassifierCS)
    python_code_.basecs_PackageCS(
        nsPrefix=var_26, nsURI=var_27, PackageCS=var_28, owner58=var_20
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_0 = python_code_.basecs_ParameterCS()
    var_5 = True
    var_6 = python_code_.basecs_ImportCS(all=var_5, basecs_ImportCS={})
    assert isinstance(var_6, python_code_.basecs_ImportCS)
    var_8 = lambda *args, **kwargs: []
    var_9 = "ClassCS86 basecs_Element70"
    var_10 = var_0.ast()
    var_11 = python_code_.basecs_PackageOwnerCS()
    var_12 = python_code_.basecs_PackageCS(
        nsPrefix=var_8, nsURI=var_9, owner58=var_10, basecs_PackageCS=var_11
    )
    assert isinstance(var_12, python_code_.basecs_PackageCS)
    var_15 = python_code_.AnnotationElementCS
    var_16 = python_code_.basecs_ClassifierCS(instanceClassName=set(), qualifier=var_12)
    assert isinstance(var_16, python_code_.basecs_ClassifierCS)
    python_code_.basecs_PackageCS(
        nsPrefix=var_15, nsURI=None, PackageCS=var_16, basecs_PackageCS=var_11
    )


def test_40():
    var_48 = python_code_.basecs_ElementCS(basecs_ElementCS73=None)
    assert isinstance(var_48, python_code_.basecs_ElementCS)
    var_61 = python_code_.basecs_TypedRefCS()
    var_62 = python_code_.basecs_MultiplicityCS(basecs_MultiplicityCS=var_61)
    assert isinstance(var_62, python_code_.basecs_MultiplicityCS)


def test_41():
    var_4 = python_code_.basecs_ElementCS(basecs_ElementCS=None)
    assert isinstance(var_4, python_code_.basecs_ElementCS)
    python_code_.basecs_ElementCS(basecs_ElementCS18=complex(1746.0627131, 1414.1291))


def test_42():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_1 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_1, python_code_.basecs_ClassifierCS)
    var_1.ast()
    python_code_.basecs_ElementCS()
    var_5 = '=ne"?\x0b&+k9<I'
    var_7 = python_code_.StructuralFeatureCS()
    var_11 = python_code_.basecs_EnumerationCS(basecs_EnumerationCS=())
    assert isinstance(var_11, python_code_.basecs_EnumerationCS)
    var_12 = var_11.ast()
    var_13 = python_code_.basecs_ModelElementCS(
        originalXmiId=set(),
        csi=var_5,
        basecs_ModelElementCS=var_7,
        basecs_ModelElementCS36=var_12,
    )
    assert isinstance(var_13, python_code_.basecs_ModelElementCS)


def test_43():
    var_48 = python_code_.basecs_ElementCS()
    var_50 = python_code_.basecs_StructuralFeatureCS(
        default='Sl"$d}/(B2%+P', ownedProperty=var_48
    )
    assert isinstance(var_50, python_code_.basecs_StructuralFeatureCS)
    var_55 = python_code_.basecs_EnumerationCS(basecs_EnumerationCS=())
    assert isinstance(var_55, python_code_.basecs_EnumerationCS)
    var_55.ast()
    var_57 = python_code_.basecs_ModelElementCS(
        originalXmiId="_basecs_ElementCS__basecs_ElementCS73:basecs_SpecificationCS16",
        csi="cF*3",
    )
    assert isinstance(var_57, python_code_.basecs_ModelElementCS)


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = python_code_.basecs_PathElementCS()
    var_1 = python_code_.basecs_ClassCS()
    var_3 = python_code_.basecs_NamedElementCS
    var_7 = python_code_.basecs_AnnotationElementCS()
    var_9 = python_code_.basecs_StructuralFeatureCS(default=var_3)
    assert isinstance(var_9, python_code_.basecs_StructuralFeatureCS)
    var_10 = var_9.ast()
    python_code_.basecs_OperationCS(
        owner45=var_10,
        basecs_OperationCS=var_0,
        basecs_OperationCS49=var_7,
        basecs_OperationCS52=(2968, 1954.9),
        basecs_OperationCS55=var_10,
        ownedOperation=var_1,
    )


def test_45():
    var_45 = True
    var_46 = ""
    var_47 = python_code_.basecs_TypedElementCS(optional=var_45, qualifier=var_46)
    assert isinstance(var_47, python_code_.basecs_TypedElementCS)
    var_7 = python_code_.basecs_MultiplicityStringCS(stringBounds=1399.33)
    assert isinstance(var_7, python_code_.basecs_MultiplicityStringCS)
    var_51 = python_code_.basecs_PackageCS(
        nsPrefix=var_46,
        nsURI=var_46,
        basecs_PackageCS={
            "_basecs_ElementCS__basecs_ElementCS:_basecs_ParameterCS__ownedParameter",
            False,
            0,
        },
    )
    assert isinstance(var_51, python_code_.basecs_PackageCS)
    var_54 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_46, ClassifierCS=()
    )
    assert isinstance(var_54, python_code_.basecs_ClassifierCS)
    var_55 = ', <>]4L"\rEc]~\t/Qe'
    var_56 = python_code_.basecs_ModelElementCS(originalXmiId=var_55, csi=[])
    assert isinstance(var_56, python_code_.basecs_ModelElementCS)


@pytest.mark.xfail(strict=True)
def test_46():
    python_code_.basecs_TupleTypeCS(name=[], basecs_TupleTypeCS=complex(699.3, -2146.0))


def test_47():
    var_30 = ""
    var_31 = python_code_.basecs_TupleTypeCS(name=var_30)
    assert isinstance(var_31, python_code_.basecs_TupleTypeCS)


@pytest.mark.xfail(strict=True)
def test_48():
    var_2 = python_code_.basecs_AttributeCS()
    var_4 = python_code_.basecs_LibraryCS()
    var_7 = python_code_.basecs_EnumerationCS()
    var_8 = python_code_.TypedElementCS()
    var_10 = "lz.\x0bq\\]z6;amp6"
    var_11 = python_code_.basecs_TypedRefCS()
    var_12 = python_code_.basecs_MultiplicityCS(basecs_MultiplicityCS=var_11)
    assert isinstance(var_12, python_code_.basecs_MultiplicityCS)
    var_13 = var_12.getLower()
    var_14 = python_code_.basecs_PackageCS(nsPrefix=var_4, nsURI=var_7)
    assert isinstance(var_14, python_code_.basecs_PackageCS)
    var_15 = python_code_.basecs_ClassifierCS(
        instanceClassName=var_8,
        qualifier=var_2,
        basecs_ClassifierCS=var_13,
        ClassifierCS=var_14,
    )
    assert isinstance(var_15, python_code_.basecs_ClassifierCS)
    python_code_.basecs_PackageCS(nsPrefix=var_10, nsURI=var_10, PackageCS=var_15)


@pytest.mark.xfail(strict=True)
def test_49():
    var_5 = python_code_.TypeCS()
    var_6 = lambda *args, **kwargs: []
    var_7 = python_code_.basecs_ElementCS(
        basecs_ElementCS18=None, basecs_ElementCS73=var_5
    )
    assert isinstance(var_7, python_code_.basecs_ElementCS)
    var_8 = python_code_.basecs_TypedTypeRefCS()
    python_code_.basecs_PathNameCS(
        scopeFilter=var_6, basecs_PathNameCS72=var_7, basecs_PathNameCS109=var_8
    )


def test_50():
    var_1 = python_code_.basecs_ElementCS()
    var_2 = var_1.getDescription()
    var_3 = python_code_.basecs_StructuralFeatureCS(
        default="XP|G(^3L\txDqv[(+", basecs_StructuralFeatureCS={var_2}
    )
    assert isinstance(var_3, python_code_.basecs_StructuralFeatureCS)
    var_4 = "basecs_TypedRefCS32"
    var_7 = python_code_.basecs_ImportCS(all=True)
    assert isinstance(var_7, python_code_.basecs_ImportCS)
    var_8 = python_code_.basecs_PackageCS(
        nsPrefix=var_4,
        nsURI=var_4,
        basecs_PackageCS={
            "_basecs_ElementCS__basecs_ElementCS:_basecs_ParameterCS__ownedParameter",
            False,
            0,
        },
    )
    assert isinstance(var_8, python_code_.basecs_PackageCS)
    var_8.getClassifier(basecs_name=True)


def test_51():
    var_41 = python_code_.basecs_OperationCS(
        owner45={False},
        basecs_OperationCS49={-1090, -587.44},
        basecs_OperationCS52=set(),
        basecs_OperationCS55=set(),
    )
    assert isinstance(var_41, python_code_.basecs_OperationCS)
    var_43 = 1727
    var_44 = python_code_.basecs_EnumerationCS()
    var_45 = python_code_.basecs_EnumerationLiteralCS(
        value=var_43,
        basecs_EnumerationLiteralCS=complex(1920.3941, 635.68),
        basecs_EnumerationLiteralCS21=var_44,
    )
    assert isinstance(var_45, python_code_.basecs_EnumerationLiteralCS)


def test_52():
    var_53 = python_code_.basecs_DataTypeCS()
    var_55 = python_code_.basecs_EnumerationCS(basecs_EnumerationCS={var_53})
    assert isinstance(var_55, python_code_.basecs_EnumerationCS)
    var_55.ast()
    var_59 = lambda *args, **kwargs: 580
    var_60 = python_code_.basecs_EnumerationLiteralCS(
        value=b"a\xdb\xcd\x9c\xa0\x84\xb0\xe1\x12\xd2Z\x1bw6E\x8a",
        basecs_EnumerationLiteralCS21=var_59,
    )
    assert isinstance(var_60, python_code_.basecs_EnumerationLiteralCS)


@pytest.mark.xfail(strict=True)
def test_53():
    var_15 = python_code_.basecs_NamedElementCS
    var_16 = python_code_.basecs_ElementCS(basecs_ElementCS18=var_15)
    assert isinstance(var_16, python_code_.basecs_ElementCS)
    python_code_.basecs_ElementCS(basecs_ElementCS=var_16)


@pytest.mark.xfail(strict=True)
def test_54():
    var_9 = "_basecs2PathNameCS__PathNameCS"
    var_13 = python_code_.basecs_StructuralFeatureCS(default=var_9)
    assert isinstance(var_13, python_code_.basecs_StructuralFeatureCS)
    var_17 = int
    python_code_.basecs_PathNameCS(
        scopeFilter=var_13,
        basecs_PathNameCS40=var_9,
        PathNameCS="_basecs_OperationCS__basecs_OperationCS49",
        pathName=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_55():
    var_1 = python_code_.basecs_ModelElementRefCS()
    var_4 = python_code_.basecs_MultiplicityCS()
    var_4.getLower()
    var_7 = python_code_.basecs_TemplateableElementCS()
    var_9 = "ownedParameter"
    var_10 = python_code_.basecs_Property
    var_11 = python_code_.basecs_ConstraintCS(
        stereotype=var_9, basecs_ConstraintCS=var_1, basecs_ConstraintCS15=var_10
    )
    assert isinstance(var_11, python_code_.basecs_ConstraintCS)
    var_12 = python_code_.basecs_TypedRefCS()
    python_code_.basecs_LambdaTypeCS(
        name=var_10, basecs_LambdaTypeCS28=var_7, basecs_LambdaTypeCS31=var_12
    )


def test_56():
    var_0 = (
        "_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCSbasecs_TuplePartCS"
    )
    var_4 = python_code_.basecs_ClassifierCS(
        instanceClassName=None, qualifier=var_0, ClassifierCS=()
    )
    assert isinstance(var_4, python_code_.basecs_ClassifierCS)
    var_6 = python_code_.basecs_RootPackageCS()
    var_7 = python_code_.basecs_LambdaTypeCS(name=var_0, basecs_LambdaTypeCS31=var_6)
    assert isinstance(var_7, python_code_.basecs_LambdaTypeCS)


def test_57():
    python_code_.basecs_EnumerationCS()
    var_45 = "-\\j}!v\\o8RDXw"
    var_46 = python_code_.basecs_TypedRefCS()
    var_47 = python_code_.basecs_LambdaTypeCS(name=var_45, basecs_LambdaTypeCS=var_46)
    assert isinstance(var_47, python_code_.basecs_LambdaTypeCS)
