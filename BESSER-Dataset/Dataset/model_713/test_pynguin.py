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
    AssociativityKind,
    Behavior,
    CallExp,
    Class,
    CollectionKind,
    CollectionLiteralPart,
    CollectionType,
    DataType,
    DynamicElement,
    Element,
    Enum,
    Feature,
    FeatureCallExp,
    LiteralExp,
    LoopExp,
    Nameable,
    NamedElement,
    Namespace,
    NavigationCallExp,
    NumericLiteralExp,
    OCLExpression,
    OpaqueExpression,
    Operation,
    Package,
    ParameterableElement,
    PrimitiveLiteralExp,
    PseudostateKind,
    ReferringElement,
    State,
    TemplateParameter,
    TemplateableElement,
    TransitionKind,
    Type,
    TypedElement,
    TypedMultiplicityElement,
    ValueSpecification,
    VariableDeclaration,
    Vertex,
    Visitable,
    abstractmethod,
    date,
    datetime,
    pivot_Annotation,
    pivot_AnyType,
    pivot_AssociationClass,
    pivot_AssociationClassCallExp,
    pivot_BagType,
    pivot_Behavior,
    pivot_BooleanLiteralExp,
    pivot_CallExp,
    pivot_CallOperationAction,
    pivot_Class,
    pivot_CollectionItem,
    pivot_CollectionLiteralExp,
    pivot_CollectionLiteralPart,
    pivot_CollectionRange,
    pivot_CollectionType,
    pivot_Comment,
    pivot_ConnectionPointReference,
    pivot_Constraint,
    pivot_ConstructorExp,
    pivot_ConstructorPart,
    pivot_DataType,
    pivot_Detail,
    pivot_DynamicElement,
    pivot_DynamicProperty,
    pivot_DynamicType,
    pivot_Element,
    pivot_ElementExtension,
    pivot_EnumLiteralExp,
    pivot_Enumeration,
    pivot_EnumerationLiteral,
    pivot_ExpressionInOCL,
    pivot_Feature,
    pivot_FeatureCallExp,
    pivot_FinalState,
    pivot_IfExp,
    pivot_Import,
    pivot_IntegerLiteralExp,
    pivot_InvalidLiteralExp,
    pivot_InvalidType,
    pivot_IterateExp,
    pivot_Iteration,
    pivot_IteratorExp,
    pivot_LambdaType,
    pivot_LetExp,
    pivot_Library,
    pivot_LiteralExp,
    pivot_LoopExp,
    pivot_MessageExp,
    pivot_MessageType,
    pivot_Metaclass,
    pivot_MorePivotable,
    pivot_Nameable,
    pivot_NamedElement,
    pivot_Namespace,
    pivot_NavigationCallExp,
    pivot_NullLiteralExp,
    pivot_NumericLiteralExp,
    pivot_OCLExpression,
    pivot_OpaqueExpression,
    pivot_Operation,
    pivot_OperationCallExp,
    pivot_OperationTemplateParameter,
    pivot_OppositePropertyCallExp,
    pivot_OrderedSetType,
    pivot_Package,
    pivot_PackageableElement,
    pivot_Parameter,
    pivot_ParameterableElement,
    pivot_Pivotable,
    pivot_Precedence,
    pivot_PrimitiveLiteralExp,
    pivot_PrimitiveType,
    pivot_Profile,
    pivot_ProfileApplication,
    pivot_Property,
    pivot_PropertyCallExp,
    pivot_Pseudostate,
    pivot_RealLiteralExp,
    pivot_ReferringElement,
    pivot_Region,
    pivot_Root,
    pivot_SelfType,
    pivot_SendSignalAction,
    pivot_SequenceType,
    pivot_SetType,
    pivot_Signal,
    pivot_State,
    pivot_StateExp,
    pivot_StateMachine,
    pivot_Stereotype,
    pivot_StringLiteralExp,
    pivot_TemplateBinding,
    pivot_TemplateParameter,
    pivot_TemplateParameterSubstitution,
    pivot_TemplateParameterType,
    pivot_TemplateSignature,
    pivot_TemplateableElement,
    pivot_Transition,
    pivot_Trigger,
    pivot_TupleLiteralExp,
    pivot_TupleLiteralPart,
    pivot_TupleType,
    pivot_Type,
    pivot_TypeExp,
    pivot_TypeExtension,
    pivot_TypeTemplateParameter,
    pivot_TypedElement,
    pivot_TypedMultiplicityElement,
    pivot_UnlimitedNaturalLiteralExp,
    pivot_UnspecifiedType,
    pivot_UnspecifiedValueExp,
    pivot_ValueSpecification,
    pivot_Variable,
    pivot_VariableDeclaration,
    pivot_VariableExp,
    pivot_Vertex,
    pivot_Visitable,
    pivot_Visitor,
    pivot_VoidType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.pivot_IteratorExp()
    var_0.RejectOrSelectTypeIsBoolean(pivot_context=None, pivot_diagnostics=var_0)
    var_3 = python_code_.pivot_Package
    var_9 = "]lZ_8slfHoG|"
    var_12 = python_code_.pivot_NavigationCallExp()
    var_18 = python_code_.pivot_CollectionType(lower=None, upper=var_9)
    assert isinstance(var_18, python_code_.pivot_CollectionType)
    var_19 = var_0.SortedByElementTypeIsSourceElementType(
        pivot_context=1, pivot_diagnostics=var_0
    )
    python_code_.pivot_Type(
        instanceClassName=var_3,
        pivot_Type=var_18,
        pivot_Type133=None,
        Type183={},
        pivot_Type100=var_12,
        type=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_1 = python_code_.pivot_ValueSpecification()
    var_1.integerValue()
    var_5 = python_code_.pivot_OCLExpression()
    var_6 = python_code_.pivot_LoopExp(pivot_LoopExp=var_5)
    assert isinstance(var_6, python_code_.pivot_LoopExp)
    var_7 = python_code_.pivot_Iteration()
    var_8 = "q.\\%r.,5n+\x0c9h\tu(<R!"
    var_9 = python_code_.pivot_EnumerationLiteral(value=var_8)
    assert isinstance(var_9, python_code_.pivot_EnumerationLiteral)
    var_10 = python_code_.pivot_ConstructorPart()
    var_12 = python_code_.pivot_Stereotype()
    var_13 = python_code_.pivot_TypeExtension(
        isRequired={"3 9(s": "X1oQuKcc", "rDZ": "=newpVM\nem]i)b+("},
        TypeExtension=var_12,
        extensionOfs=var_12,
        TypeExtension331=var_7,
    )
    assert isinstance(var_13, python_code_.pivot_TypeExtension)
    var_14 = python_code_.pivot_IteratorExp()
    var_15 = lambda *args, **kwargs: False
    var_14.SortedByIsOrderedIfSourceIsOrdered(
        pivot_diagnostics=var_8, pivot_context=var_15
    )
    var_17 = "_pivot_Class__pivot_ClassRegionpivot_Property211"
    var_18 = "cQth8F^x;t\\ P?V"
    python_code_.pivot_Class(
        isInterface=var_17,
        isAbstract=set(),
        isActive=var_18,
        pivot_Class11=True,
        pivot_Class14=var_7,
        pivot_Class197=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "FZ*eH]yBGH\n,RHg"
    var_1 = python_code_.pivot_Namespace()
    var_2 = "%G8C"
    var_3 = python_code_.pivot_TypeExtension
    var_4 = python_code_.pivot_Vertex()
    var_5 = python_code_.pivot_Transition(
        kind=var_2,
        Transition=set(),
        transition320=None,
        Transition371=var_3,
        Transition369=var_4,
    )
    assert isinstance(var_5, python_code_.pivot_Transition)
    python_code_.pivot_Constraint(
        isCallable=var_0,
        pivot_Constraint41=(),
        pivot_Constraint="skm`E)G.UO@l>PhV`]",
        pivot_Constraint136=var_1,
        Constraint=var_1,
        Constraint314=var_5,
    )


def test_3():
    var_1 = python_code_.pivot_DataType(isSerializable={3119.94, '*JU&$7j?I~mr"nEz=S'})
    assert isinstance(var_1, python_code_.pivot_DataType)
    var_2 = python_code_.pivot_ValueSpecification()
    var_2.unlimitedValue()


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = "l_~MK#)4H"
    var_3 = "f$Xw\x0bd-cAf16&O6V"
    var_4 = -3226
    var_5 = python_code_.pivot_Precedence(associativity=var_3, order=var_4)
    assert isinstance(var_5, python_code_.pivot_Precedence)
    var_6 = lambda *args, **kwargs: "EHy_-mLu<\ns#1J"
    var_7 = python_code_.pivot_OperationCallExp(pivot_OperationCallExp=var_3)
    assert isinstance(var_7, python_code_.pivot_OperationCallExp)
    var_8 = python_code_.pivot_IteratorExp()
    var_8.IsUniqueHasOneIterator(pivot_diagnostics=(), pivot_context=var_8)
    var_10 = "ZTrPBv.$R#:J]s%[L="
    var_11 = python_code_.pivot_PropertyCallExp()
    var_12 = var_11.getSpecializedReferredPropertyType()
    var_13 = python_code_.pivot_Operation(
        isInvalidating=var_10, isValidating=var_5, operation=var_12, Operation339={}
    )
    assert isinstance(var_13, python_code_.pivot_Operation)
    var_14 = var_8.RejectOrSelectTypeIsSourceType(
        pivot_diagnostics=True, pivot_context=-76.34
    )
    python_code_.pivot_Type(
        instanceClassName=var_6,
        pivot_Type51=var_1,
        pivot_Type=var_7,
        Type=var_13,
        owningType338=var_14,
    )


def test_5():
    var_3 = python_code_.pivot_CollectionRange()
    var_5 = python_code_.pivot_ValueSpecification()
    var_6 = var_5.isComputable()
    var_9 = python_code_.pivot_PropertyCallExp()
    var_9.CompatibleResultType(pivot_context=(), pivot_diagnostics=var_5)
    var_11 = "nOA\rY%"
    var_12 = python_code_.pivot_Operation(
        isInvalidating=var_11,
        isValidating=("_pivot_PropertyCallExp__pivot_PropertyCallExp",),
        pivot_Operation=var_6,
        pivot_Operation157=-568,
        pivot_Operation172=complex(338.4784, 1100.808),
        ownedOperation="_pivot_Precedence__pivot_Precedence158 extension _pivot_State__state pivot_Comment64",
    )
    assert isinstance(var_12, python_code_.pivot_Operation)
    var_12.UniquePreconditionName(
        pivot_context=complex(2047.815047, -594.586119), pivot_diagnostics=var_3
    )


@pytest.mark.xfail(strict=True)
def test_6():
    python_code_.pivot_MessageExp(
        pivot_MessageExp=complex(805.1020479, 1487.510441), pivot_MessageExp126=()
    )


def test_7():
    var_0 = python_code_.pivot_ValueSpecification()
    var_3 = python_code_.pivot_OperationCallExp()
    var_4 = python_code_.pivot_Region
    var_3.ArgumentCount(pivot_diagnostics=var_4, pivot_context={-1763.27, -139.13})
    var_0.stringValue()


def test_8():
    python_code_.pivot_ValueSpecification()


def test_9():
    var_0 = python_code_.pivot_TemplateSignature()
    var_1 = python_code_.pivot_IteratorExp()
    var_1.ClosureElementTypeIsSourceElementType(
        pivot_diagnostics=var_0, pivot_context=()
    )
