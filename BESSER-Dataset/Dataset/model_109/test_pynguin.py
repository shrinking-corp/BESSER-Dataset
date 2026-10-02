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
    ASTNode,
    AbstractTypeDeclaration,
    Annotation,
    AssignmentOperatorKind,
    BodyDeclaration,
    Comment,
    Enum,
    Expression,
    ExtendedModifier,
    IJavaElement,
    IMember,
    IPackageFragmentRoot,
    ISourceReference,
    ITypeRoot,
    InfixExpressionOperatorKind,
    JDTAST_AST,
    JDTAST_ASTNode,
    JDTAST_AbstractTypeDeclaration,
    JDTAST_Annotation,
    JDTAST_AnnotationTypeDeclaration,
    JDTAST_AnnotationTypeMemberDeclaration,
    JDTAST_AnonymousClassDeclaration,
    JDTAST_ArrayAccess,
    JDTAST_ArrayCreation,
    JDTAST_ArrayInitializer,
    JDTAST_ArrayType,
    JDTAST_AssertStatement,
    JDTAST_Assignment,
    JDTAST_BinaryPackageFragmentRoot,
    JDTAST_Block,
    JDTAST_BlockComment,
    JDTAST_BodyDeclaration,
    JDTAST_BooleanLiteral,
    JDTAST_BreakStatement,
    JDTAST_CastExpression,
    JDTAST_CatchClause,
    JDTAST_CharacterLiteral,
    JDTAST_ClassInstanceCreation,
    JDTAST_Comment,
    JDTAST_CompilationUnit,
    JDTAST_ConditionalExpression,
    JDTAST_ConstructorInvocation,
    JDTAST_ContinueStatement,
    JDTAST_DoStatement,
    JDTAST_EmptyStatement,
    JDTAST_EnhancedForStatement,
    JDTAST_EnumConstantDeclaration,
    JDTAST_EnumDeclaration,
    JDTAST_Expression,
    JDTAST_ExpressionStatement,
    JDTAST_ExtendedModifier,
    JDTAST_FieldAccess,
    JDTAST_FieldDeclaration,
    JDTAST_ForStatement,
    JDTAST_IClassFile,
    JDTAST_ICompilationUnit,
    JDTAST_IField,
    JDTAST_IImportDeclaration,
    JDTAST_IInitializer,
    JDTAST_IJavaElement,
    JDTAST_IJavaModel,
    JDTAST_IJavaProject,
    JDTAST_IMember,
    JDTAST_IMethod,
    JDTAST_IPackageFragment,
    JDTAST_IPackageFragmentRoot,
    JDTAST_ISourceRange,
    JDTAST_ISourceReference,
    JDTAST_IType,
    JDTAST_ITypeParameter,
    JDTAST_ITypeRoot,
    JDTAST_IfStatement,
    JDTAST_ImportDeclaration,
    JDTAST_InfixExpression,
    JDTAST_Initializer,
    JDTAST_InstanceofExpression,
    JDTAST_Javadoc,
    JDTAST_LabeledStatement,
    JDTAST_LineComment,
    JDTAST_MarkerAnnotation,
    JDTAST_MemberRef,
    JDTAST_MemberValuePair,
    JDTAST_MethodDeclaration,
    JDTAST_MethodInvocation,
    JDTAST_MethodRef,
    JDTAST_MethodRefParameter,
    JDTAST_Modifier,
    JDTAST_Name,
    JDTAST_NormalAnnotation,
    JDTAST_NullLiteral,
    JDTAST_NumberLiteral,
    JDTAST_PackageDeclaration,
    JDTAST_Parameter,
    JDTAST_ParameterizedType,
    JDTAST_ParenthesizedExpression,
    JDTAST_PhysicalElement,
    JDTAST_PostfixExpression,
    JDTAST_PrefixExpression,
    JDTAST_PrimitiveType,
    JDTAST_QualifiedName,
    JDTAST_QualifiedType,
    JDTAST_ReturnStatement,
    JDTAST_SimpleName,
    JDTAST_SimpleType,
    JDTAST_SingleMemberAnnotation,
    JDTAST_SingleVariableDeclaration,
    JDTAST_SourcePackageFragmentRoot,
    JDTAST_Statement,
    JDTAST_StringLiteral,
    JDTAST_SuperConstructorInvocation,
    JDTAST_SuperFieldAccess,
    JDTAST_SuperMethodInvocation,
    JDTAST_SwitchCase,
    JDTAST_SwitchStatement,
    JDTAST_SynchronizedStatement,
    JDTAST_TagElement,
    JDTAST_TextElement,
    JDTAST_ThisExpression,
    JDTAST_ThrowStatement,
    JDTAST_TryStatement,
    JDTAST_Type,
    JDTAST_TypeDeclaration,
    JDTAST_TypeDeclarationStatement,
    JDTAST_TypeLiteral,
    JDTAST_TypeParameter,
    JDTAST_VariableDeclaration,
    JDTAST_VariableDeclarationExpression,
    JDTAST_VariableDeclarationFragment,
    JDTAST_VariableDeclarationStatement,
    JDTAST_WhileStatement,
    JDTAST_WildcardType,
    Modifiers,
    Name,
    PhysicalElement,
    PostfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
    Statement,
    Type,
    VariableDeclaration,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.AssignmentOperatorKind.minus_assign
    var_1 = python_code_.JDTAST_PrimitiveType(code=var_0)
    assert isinstance(var_1, python_code_.JDTAST_PrimitiveType)
    var_9 = "JDTAST_CatchClause59,JDTAST_SuperMethodInvocation,JDTAST_BreakStatement"
    var_10 = python_code_.JDTAST_WildcardType(upperBound=var_9)
    assert isinstance(var_10, python_code_.JDTAST_WildcardType)


@pytest.mark.xfail(strict=True)
def test_1():
    var_3 = python_code_.JDTAST_ITypeRoot()
    var_5 = "Df5Di52yO"
    var_6 = python_code_.JDTAST_ImportDeclaration(onDemand=var_5, static=var_3)
    assert isinstance(var_6, python_code_.JDTAST_ImportDeclaration)
    var_10 = "right_shift_signed and_ _JDTAST_IImportDeclaration__JDTAST_IImportDeclaration _JDTAST_TagElement__JDTAST_TagElement182"
    var_11 = python_code_.JDTAST_NumberLiteral(token=var_10)
    assert isinstance(var_11, python_code_.JDTAST_NumberLiteral)
    var_14 = 'w=fM$G[""XlX ^dl^V'
    var_15 = "JDTAST_SingleVariableDeclaration"
    var_16 = python_code_.JDTAST_StringLiteral(escapedValue=var_14, literalValue=var_15)
    assert isinstance(var_16, python_code_.JDTAST_StringLiteral)
    var_19 = python_code_.JDTAST_WildcardType(upperBound=[], JDTAST_WildcardType=var_5)
    assert isinstance(var_19, python_code_.JDTAST_WildcardType)
    var_21 = python_code_.JDTAST_SimpleName
    var_22 = "JDTAST_MemberRef"
    var_23 = "|4&xMS"
    var_24 = "_JDTAST_Expression__JDTAST_Expression231 JDTAST_EnumConstantDeclaration139 right_shift_signed _JDTAST_IType__JDTAST_IType44"
    var_25 = python_code_.JDTAST_IField(
        constant=var_21,
        isEnumConstant=var_22,
        typeSignature=var_23,
        isVolatile=var_24,
        isTransient=[2],
    )
    assert isinstance(var_25, python_code_.JDTAST_IField)
    var_30 = python_code_.JDTAST_Name(
        fullyQualifiedName='"Q%Tk&.b',
        JDTAST_Name160=None,
        JDTAST_Name185=None,
        JDTAST_Name430=var_21,
    )
    assert isinstance(var_30, python_code_.JDTAST_Name)
    python_code_.JDTAST_InfixExpression(
        operator=var_15, JDTAST_InfixExpression=var_21, JDTAST_InfixExpression240=[]
    )


def test_2():
    var_5 = "@2>"
    var_6 = python_code_.JDTAST_PrimitiveType(code=var_5)
    assert isinstance(var_6, python_code_.JDTAST_PrimitiveType)
    var_9 = python_code_.JDTAST_IJavaElement
    var_10 = "O_~"
    var_11 = python_code_.JDTAST_ImportDeclaration(onDemand=var_9, static=var_10)
    assert isinstance(var_11, python_code_.JDTAST_ImportDeclaration)
    var_15 = ':/F4qt:\x0c; x"y=q{?<Z'
    var_16 = python_code_.JDTAST_SwitchCase(default=var_15)
    assert isinstance(var_16, python_code_.JDTAST_SwitchCase)


def test_3():
    var_0 = python_code_.JDTAST_VariableDeclaration(
        extraDimensions=b"C\x1e5\xb1\x93\xf5\xffP\xe248J\xa0\xd8\x8c\xfe\x0f"
    )
    assert isinstance(var_0, python_code_.JDTAST_VariableDeclaration)
    var_1 = python_code_.JDTAST_ASTNode()
    var_4 = "_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration120JDTAST_IType48JDTAST_MemberValuePair82"
    var_7 = python_code_.JDTAST_AnnotationTypeMemberDeclaration()
    var_8 = python_code_.JDTAST_SwitchCase(
        default=var_7, JDTAST_SwitchCase="(bKST:Jv_uPk_"
    )
    assert isinstance(var_8, python_code_.JDTAST_SwitchCase)
    var_15 = python_code_.JDTAST_Assignment(operator=var_1)
    assert isinstance(var_15, python_code_.JDTAST_Assignment)
    var_33 = python_code_.JDTAST_IPackageFragmentRoot()
    var_34 = python_code_.JDTAST_IPackageFragment(
        isDefaultPackage=var_4,
        JDTAST_IPackageFragment=None,
        IPackageFragment=var_33,
        JDTAST_IPackageFragment106=[],
    )
    assert isinstance(var_34, python_code_.JDTAST_IPackageFragment)
    var_35 = python_code_.JDTAST_IfStatement()
    var_38 = python_code_.JDTAST_ArrayType(dimensions=var_4)
    assert isinstance(var_38, python_code_.JDTAST_ArrayType)
    var_40 = python_code_.JDTAST_BooleanLiteral(booleanValue=var_35)
    assert isinstance(var_40, python_code_.JDTAST_BooleanLiteral)


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = "JDTAST_MethodDeclaration156 JDTAST_ClassInstanceCreation216 JDTAST_SimpleName124 JDTAST_MethodRefParameter92"
    var_2 = python_code_.JDTAST_ITypeParameter(bounds=var_1)
    assert isinstance(var_2, python_code_.JDTAST_ITypeParameter)
    var_3 = "JDTAST_PackageDeclaration105,JDTAST_IPackageFragment,_JDTAST_Expression__JDTAST_Expression374"
    var_4 = "gWt.'1?}N.h}}"
    var_5 = lambda *args, **kwargs: "\x0c"
    var_6 = python_code_.JDTAST_Modifier(
        abstract=var_3,
        final=var_2,
        native=var_4,
        none=var_1,
        private=var_1,
        protected=var_1,
        public=var_1,
        static=var_3,
        strictfp=var_4,
        synchronized=var_2,
        transient=var_5,
        volatile="J{Xn?;1Sy",
    )
    assert isinstance(var_6, python_code_.JDTAST_Modifier)
    var_40 = python_code_.JDTAST_IMethod(
        returnType=var_4,
        isConstructor=None,
        isMainMethod=var_5,
        exceptionTypes="_JDTAST_IType__JDTAST_IType23",
        JDTAST_IMethod=None,
    )
    assert isinstance(var_40, python_code_.JDTAST_IMethod)
    var_41 = python_code_.JDTAST_TypeParameter()
    var_42 = python_code_.AbstractTypeDeclaration()
    var_43 = "~n ps[Dz3"
    var_44 = {var_41}
    var_45 = python_code_.JDTAST_TypeDeclaration(
        interface=var_43, JDTAST_TypeDeclaration178=var_44
    )
    assert isinstance(var_45, python_code_.JDTAST_TypeDeclaration)
    var_47 = python_code_.JDTAST_VariableDeclaration(
        extraDimensions=complex(2041.585634, -2534.997)
    )
    assert isinstance(var_47, python_code_.JDTAST_VariableDeclaration)
    var_49 = "Lp&bEtN9X[MP"
    var_50 = python_code_.JDTAST_IField(
        constant=var_44,
        isEnumConstant=var_49,
        typeSignature=var_5,
        isVolatile=True,
        isTransient={
            "JDTAST_PackageDeclaration102.JDTAST_IClassFile.super": "#WOj'uXF\\!eWp_~\\L!"
        },
    )
    assert isinstance(var_50, python_code_.JDTAST_IField)
    var_51 = python_code_.JDTAST_Type()
    var_52 = python_code_.JDTAST_ArrayType(
        dimensions=var_43, JDTAST_ArrayType401=var_51, JDTAST_ArrayType404=var_51
    )
    assert isinstance(var_52, python_code_.JDTAST_ArrayType)
    var_53 = python_code_.JDTAST_FieldAccess()
    var_54 = python_code_.JDTAST_InfixExpression(
        operator="JDTAST_Assignment203._JDTAST_SimpleName__JDTAST_SimpleName352.JDTAST_IMember._JDTAST_Expression__JDTAST_Expression115"
    )
    assert isinstance(var_54, python_code_.JDTAST_InfixExpression)
    var_55 = python_code_.JDTAST_BreakStatement
    var_56 = python_code_.JDTAST_MethodInvocation()
    var_57 = python_code_.JDTAST_ParenthesizedExpression()
    var_58 = python_code_.JDTAST_ForStatement()
    var_59 = python_code_.JDTAST_SuperConstructorInvocation()
    var_60 = python_code_.JDTAST_SingleMemberAnnotation()
    var_61 = python_code_.JDTAST_Expression(
        resolveBoxing=var_4,
        resolveUnboxing=var_51,
        JDTAST_Expression192="~X;IwVr('[\x0bCiQl7\r0",
        JDTAST_Expression187=var_5,
        JDTAST_Expression336=True,
        JDTAST_Expression225=var_42,
        JDTAST_Expression228=None,
        JDTAST_Expression231=set(),
        JDTAST_Expression233=var_53,
        JDTAST_Expression238=var_54,
        JDTAST_Expression251=var_55,
        JDTAST_Expression254=var_56,
        JDTAST_Expression265=var_57,
        JDTAST_Expression339=var_58,
        JDTAST_Expression356=var_59,
        JDTAST_Expression359=var_59,
        JDTAST_Expression434=var_60,
    )
    assert isinstance(var_61, python_code_.JDTAST_Expression)
    python_code_.JDTAST_Assignment(
        operator=var_5, JDTAST_Assignment=var_61, JDTAST_Assignment203=var_61
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = 'V|MMHJ"K?l'
    var_2 = "remainder_assign JDTAST_ContinueStatement"
    var_9 = python_code_.JDTAST_IJavaElement(elementName=var_2)
    assert isinstance(var_9, python_code_.JDTAST_IJavaElement)
    var_19 = python_code_.JDTAST_PostfixExpression(operator=var_1)
    assert isinstance(var_19, python_code_.JDTAST_PostfixExpression)
    var_26 = python_code_.JDTAST_SingleVariableDeclaration
    python_code_.JDTAST_SingleVariableDeclaration(
        varargs=var_1, JDTAST_SingleVariableDeclaration424=var_26
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_5 = "@2>"
    var_6 = python_code_.JDTAST_PrimitiveType(code=var_5)
    assert isinstance(var_6, python_code_.JDTAST_PrimitiveType)
    var_9 = python_code_.JDTAST_IJavaElement
    var_10 = "O_~"
    var_11 = python_code_.JDTAST_ImportDeclaration(onDemand=var_9, static=var_10)
    assert isinstance(var_11, python_code_.JDTAST_ImportDeclaration)
    var_12 = python_code_.JDTAST_SwitchStatement()
    var_15 = ':/F4qt:\x0c; x"y=q{?<Z'
    var_16 = python_code_.JDTAST_SwitchCase(default=var_15)
    assert isinstance(var_16, python_code_.JDTAST_SwitchCase)
    var_18 = python_code_.JDTAST_ConditionalExpression()
    var_19 = python_code_.JDTAST_ConditionalExpression()
    var_20 = python_code_.JDTAST_PrefixExpression(operator=1563.45)
    assert isinstance(var_20, python_code_.JDTAST_PrefixExpression)
    python_code_.JDTAST_Expression(
        resolveBoxing=var_12,
        resolveUnboxing=[],
        JDTAST_Expression225=var_18,
        JDTAST_Expression231=var_19,
        JDTAST_Expression269=var_20,
        JDTAST_Expression267=var_9,
        JDTAST_Expression323=None,
        JDTAST_Expression364=var_16,
        JDTAST_Expression356=var_16,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.JDTAST_VariableDeclaration(
        extraDimensions=b"C\x1e5\xb1\x93\xf5\xffP\xe248J\xa0\xd8\x8c\xfe\x0f"
    )
    assert isinstance(var_0, python_code_.JDTAST_VariableDeclaration)
    var_1 = python_code_.JDTAST_ASTNode()
    var_3 = python_code_.JDTAST_IInitializer()
    var_4 = "_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration120JDTAST_IType48JDTAST_MemberValuePair82"
    var_5 = "_JDTAST_IMethod__JDTAST_IMethod50conditional_or_JDTAST_IType__JDTAST_IType23JDTAST_Expression204"
    var_6 = python_code_.JDTAST_IField(
        constant=var_0,
        isEnumConstant=var_4,
        typeSignature=var_1,
        isVolatile=var_5,
        isTransient=var_5,
    )
    assert isinstance(var_6, python_code_.JDTAST_IField)
    var_7 = python_code_.JDTAST_AnnotationTypeMemberDeclaration()
    var_8 = python_code_.JDTAST_SwitchCase(
        default=var_7, JDTAST_SwitchCase="(bKST:Jv_uPk_"
    )
    assert isinstance(var_8, python_code_.JDTAST_SwitchCase)
    var_9 = python_code_.JDTAST_ICompilationUnit()
    var_10 = python_code_.JDTAST_IImportDeclaration(
        isOnDemand=True, isStatic=var_5, JDTAST_IImportDeclaration=var_9
    )
    assert isinstance(var_10, python_code_.JDTAST_IImportDeclaration)
    var_13 = python_code_.JDTAST_BreakStatement()
    var_15 = python_code_.JDTAST_Assignment(operator=var_1)
    assert isinstance(var_15, python_code_.JDTAST_Assignment)
    var_16 = python_code_.JDTAST_EnumConstantDeclaration()
    var_17 = python_code_.JDTAST_ForStatement()
    var_18 = bool
    var_19 = python_code_.JDTAST_PrefixExpression(
        operator=var_18, JDTAST_PrefixExpression=var_3
    )
    assert isinstance(var_19, python_code_.JDTAST_PrefixExpression)
    var_20 = python_code_.JDTAST_PostfixExpression(operator=var_4)
    assert isinstance(var_20, python_code_.JDTAST_PostfixExpression)
    var_21 = python_code_.JDTAST_ExpressionStatement()
    var_22 = python_code_.JDTAST_SuperConstructorInvocation()
    var_23 = python_code_.JDTAST_SingleMemberAnnotation()
    python_code_.JDTAST_Expression(
        resolveBoxing=var_4,
        resolveUnboxing=None,
        JDTAST_Expression201=var_15,
        JDTAST_Expression134=var_16,
        JDTAST_Expression190=1026,
        JDTAST_Expression217=var_13,
        JDTAST_Expression336=var_17,
        JDTAST_Expression228=var_18,
        JDTAST_Expression233=[-765, ";$`J3J<zIf!VQ{d$", 1],
        JDTAST_Expression269=var_19,
        JDTAST_Expression267=var_20,
        JDTAST_Expression276=var_9,
        JDTAST_Expression376=None,
        JDTAST_Expression328=var_21,
        JDTAST_Expression344=var_5,
        JDTAST_Expression359=var_22,
        JDTAST_Expression434=var_23,
    )


def test_8():
    var_1 = 'V|MMHJ"K?l'
    var_2 = "remainder_assign JDTAST_ContinueStatement"
    var_3 = "$\r\nWm@x3'dH"
    var_4 = python_code_.JDTAST_IMethod(
        returnType=var_2, isConstructor=var_1, isMainMethod=var_3, exceptionTypes=var_3
    )
    assert isinstance(var_4, python_code_.JDTAST_IMethod)
    var_5 = python_code_.JDTAST_Parameter(name=var_1, type=True, JDTAST_Parameter=var_4)
    var_6 = python_code_.JDTAST_BreakStatement()
    var_7 = python_code_.JDTAST_LabeledStatement()
    var_8 = python_code_.JDTAST_SimpleName(
        declaration=var_5,
        identifier=var_2,
        JDTAST_SimpleName306=var_6,
        JDTAST_SimpleName352=var_7,
    )
    assert isinstance(var_8, python_code_.JDTAST_SimpleName)
    var_9 = python_code_.JDTAST_IJavaElement(elementName=var_2)
    assert isinstance(var_9, python_code_.JDTAST_IJavaElement)
    var_10 = python_code_.JDTAST_IImportDeclaration(isOnDemand=var_3, isStatic=None)
    assert isinstance(var_10, python_code_.JDTAST_IImportDeclaration)
    var_11 = python_code_.JDTAST_IPackageFragmentRoot()
    var_12 = python_code_.JDTAST_IPackageFragment(
        isDefaultPackage=var_1,
        JDTAST_IPackageFragment=None,
        IPackageFragment=var_11,
        JDTAST_IPackageFragment106=[],
    )
    assert isinstance(var_12, python_code_.JDTAST_IPackageFragment)
    var_13 = python_code_.JDTAST_IfStatement()
    var_16 = python_code_.JDTAST_ArrayType(dimensions=var_1)
    assert isinstance(var_16, python_code_.JDTAST_ArrayType)
    var_18 = python_code_.JDTAST_BooleanLiteral(booleanValue=var_13)
    assert isinstance(var_18, python_code_.JDTAST_BooleanLiteral)


def test_9():
    var_1 = "JDTAST_MethodDeclaration156 JDTAST_ClassInstanceCreation216 JDTAST_SimpleName124 JDTAST_MethodRefParameter92"
    var_2 = python_code_.JDTAST_ITypeParameter(bounds=var_1)
    assert isinstance(var_2, python_code_.JDTAST_ITypeParameter)
    var_3 = "JDTAST_PackageDeclaration105,JDTAST_IPackageFragment,_JDTAST_Expression__JDTAST_Expression374"
    var_4 = "gWt.'1?}N.h}}"
    var_5 = lambda *args, **kwargs: "\x0c"
    var_6 = python_code_.JDTAST_Modifier(
        abstract=var_3,
        final=var_2,
        native=var_4,
        none=var_1,
        private=var_1,
        protected=var_1,
        public=var_1,
        static=var_3,
        strictfp=var_4,
        synchronized=var_2,
        transient=var_5,
        volatile="J{Xn?;1Sy",
    )
    assert isinstance(var_6, python_code_.JDTAST_Modifier)
    var_8 = python_code_.JDTAST_BreakStatement()
    var_10 = python_code_.Type()
    python_code_.JDTAST_Parameter(name=var_6, type=var_10)
    var_13 = "_JDTAST_IType__JDTAST_IType48"
    var_14 = python_code_.JDTAST_IMethod(
        returnType=var_1,
        isConstructor=var_13,
        isMainMethod=var_4,
        exceptionTypes=var_6,
        JDTAST_IMethod263=var_13,
    )
    assert isinstance(var_14, python_code_.JDTAST_IMethod)
    var_16 = python_code_.JDTAST_Initializer()
    var_20 = python_code_.JDTAST_PhysicalElement(
        path=(-1, True, 1241), isReadOnly=var_5
    )
    assert isinstance(var_20, python_code_.JDTAST_PhysicalElement)
    var_23 = python_code_.JDTAST_BlockComment()
    var_26 = python_code_.JDTAST_VariableDeclarationFragment()
    var_27 = python_code_.JDTAST_IType(
        fullyQualifiedParametrizedName=var_4, fullyQualifiedName=[487.13, 599.28]
    )
    assert isinstance(var_27, python_code_.JDTAST_IType)
    var_28 = {var_27, var_27, var_27, var_27, var_27}
    python_code_.JDTAST_IType(
        fullyQualifiedParametrizedName=var_5,
        fullyQualifiedName=var_5,
        JDTAST_IType=var_23,
        JDTAST_IType44=var_28,
        JDTAST_IType43=var_28,
    )
    python_code_.JDTAST_IMethod(
        returnType=var_4,
        isConstructor=var_5,
        isMainMethod=var_26,
        exceptionTypes=var_8,
        JDTAST_IMethod=var_27,
    )
    var_32 = python_code_.JDTAST_ArrayType(
        dimensions=var_16, JDTAST_ArrayType404=var_14
    )
    assert isinstance(var_32, python_code_.JDTAST_ArrayType)


def test_10():
    var_0 = python_code_.JDTAST_TypeLiteral()
    var_2 = python_code_.JDTAST_DoStatement
    var_3 = python_code_.JDTAST_Type()
    var_4 = python_code_.JDTAST_SingleVariableDeclaration(
        varargs=var_2,
        JDTAST_SingleVariableDeclaration157=True,
        JDTAST_SingleVariableDeclaration421=var_3,
    )
    assert isinstance(var_4, python_code_.JDTAST_SingleVariableDeclaration)
    var_6 = python_code_.JDTAST_StringLiteral(escapedValue=True, literalValue=var_3)
    assert isinstance(var_6, python_code_.JDTAST_StringLiteral)
    var_7 = python_code_.JDTAST_ArrayInitializer()
    var_9 = python_code_.JDTAST_TextElement(text=var_0)
    assert isinstance(var_9, python_code_.JDTAST_TextElement)
    var_12 = "JDTAST_MethodInvocation262,equals,_JDTAST_MethodRefParameter__JDTAST_MethodRefParameter92,JDTAST_MemberValuePair82"
    var_13 = python_code_.JDTAST_CompilationUnit()
    var_14 = python_code_.JDTAST_AbstractTypeDeclaration(
        localTypeDeclaration=[],
        memberTypeDeclaration=var_12,
        packageMemberTypeDeclaration=var_2,
        JDTAST_AbstractTypeDeclaration=var_13,
        JDTAST_AbstractTypeDeclaration386=var_2,
    )
    assert isinstance(var_14, python_code_.JDTAST_AbstractTypeDeclaration)
    var_15 = python_code_.JDTAST_IField(
        constant=var_7,
        isEnumConstant=var_12,
        typeSignature=2,
        isVolatile=1050,
        isTransient=var_6,
    )
    assert isinstance(var_15, python_code_.JDTAST_IField)
    var_20 = python_code_.JDTAST_VariableDeclaration(
        extraDimensions={"7B~", "a@,D{wgq?{nv9|JSd"}
    )
    assert isinstance(var_20, python_code_.JDTAST_VariableDeclaration)
    var_26 = python_code_.ITypeRoot()
    var_27 = "!2"
    var_28 = python_code_.JDTAST_CatchClause()
    var_29 = ""
    var_30 = "JDTAST_MemberRef77,JDTAST_IType43,JDTAST_IClassFile,_JDTAST_IType__JDTAST_IType48"
    var_31 = python_code_.JDTAST_MethodDeclaration(
        constructor=var_29, varargs=var_30, extraDimensions=var_2
    )
    assert isinstance(var_31, python_code_.JDTAST_MethodDeclaration)
    var_32 = python_code_.JDTAST_SingleVariableDeclaration(
        varargs=var_27,
        JDTAST_SingleVariableDeclaration=var_28,
        JDTAST_SingleVariableDeclaration157=var_31,
        JDTAST_SingleVariableDeclaration421=var_26,
    )
    assert isinstance(var_32, python_code_.JDTAST_SingleVariableDeclaration)


@pytest.mark.xfail(strict=True)
def test_11():
    var_2 = python_code_.JDTAST_NumberLiteral(token=[False, False])
    assert isinstance(var_2, python_code_.JDTAST_NumberLiteral)
    var_3 = python_code_.JDTAST_LineComment()
    var_4 = ""
    var_5 = python_code_.JDTAST_ICompilationUnit()
    var_6 = python_code_.JDTAST_IImportDeclaration(
        isOnDemand=True, isStatic=var_4, JDTAST_IImportDeclaration=var_5
    )
    assert isinstance(var_6, python_code_.JDTAST_IImportDeclaration)
    var_7 = "aMAb83"
    var_8 = python_code_.JDTAST_ISourceReference(source=var_7)
    assert isinstance(var_8, python_code_.JDTAST_ISourceReference)
    var_9 = "_JDTAST_IType__JDTAST_IType48"
    var_10 = "U0e"
    var_11 = (
        lambda *args, **kwargs: "JDTAST_MethodDeclaration150 JDTAST_Type154 JDTAST_EnhancedForStatement"
    )
    var_12 = python_code_.JDTAST_IMethod(
        returnType=var_10,
        isConstructor=None,
        isMainMethod=var_11,
        exceptionTypes="_JDTAST_IType__JDTAST_IType23",
        JDTAST_IMethod=None,
    )
    assert isinstance(var_12, python_code_.JDTAST_IMethod)
    python_code_.JDTAST_MethodDeclaration(
        constructor=var_9,
        varargs=var_9,
        extraDimensions=var_3,
        JDTAST_MethodDeclaration159=1561,
        JDTAST_MethodDeclaration150=0,
        JDTAST_MethodDeclaration165=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_1 = python_code_.JDTAST_LineComment()
    var_2 = python_code_.JDTAST_NormalAnnotation()
    var_3 = python_code_.Expression
    var_4 = python_code_.JDTAST_EnumConstantDeclaration()
    var_5 = python_code_.JDTAST_ArrayAccess()
    var_6 = python_code_.JDTAST_DoStatement()
    var_7 = python_code_.JDTAST_SuperConstructorInvocation()
    var_8 = python_code_.JDTAST_SynchronizedStatement()
    var_9 = python_code_.JDTAST_Expression(
        resolveBoxing=var_1,
        resolveUnboxing={},
        JDTAST_Expression83=var_2,
        JDTAST_Expression204=var_3,
        JDTAST_Expression211=b"\xc9\x85\xbd\xcb\x91F ,0\xd7\xe9\xbc\x05\xca\x0e/e\xe3#",
        JDTAST_Expression134=var_4,
        JDTAST_Expression187=var_5,
        JDTAST_Expression225="JDTAST_SuperConstructorInvocation",
        JDTAST_Expression318=var_6,
        JDTAST_Expression323=var_3,
        JDTAST_Expression356=var_7,
        JDTAST_Expression374=var_8,
    )
    assert isinstance(var_9, python_code_.JDTAST_Expression)
    var_12 = set()
    var_13 = python_code_.JDTAST_ICompilationUnit()
    var_14 = {var_13}
    var_15 = python_code_.JDTAST_IPackageFragment(
        isDefaultPackage=(),
        JDTAST_IPackageFragment=var_12,
        JDTAST_IPackageFragment16=var_14,
    )
    assert isinstance(var_15, python_code_.JDTAST_IPackageFragment)
    var_19 = "JDTAST_PrefixExpression,bit_xor_assign,_JDTAST_IImportDeclaration__JDTAST_IImportDeclaration"
    var_20 = python_code_.JDTAST_SimpleName(
        declaration=complex(-1786.66, 76.6375443),
        identifier={"rx\to:$a@~'\n-|\r": True},
        JDTAST_SimpleName129=3180.94,
        JDTAST_SimpleName306=True,
        JDTAST_SimpleName236=var_14,
    )
    assert isinstance(var_20, python_code_.JDTAST_SimpleName)
    python_code_.JDTAST_VariableDeclaration(
        extraDimensions=var_19, JDTAST_VariableDeclaration117=var_20
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_3 = python_code_.JDTAST_ITypeRoot()
    var_5 = "Df5Di52yO"
    var_6 = python_code_.JDTAST_ImportDeclaration(onDemand=var_5, static=var_3)
    assert isinstance(var_6, python_code_.JDTAST_ImportDeclaration)
    var_7 = python_code_.JDTAST_NumberLiteral(token=[])
    assert isinstance(var_7, python_code_.JDTAST_NumberLiteral)
    var_14 = 'w=fM$G[""XlX ^dl^V'
    var_15 = "JDTAST_SingleVariableDeclaration"
    var_16 = python_code_.JDTAST_StringLiteral(escapedValue=var_14, literalValue=var_15)
    assert isinstance(var_16, python_code_.JDTAST_StringLiteral)
    var_19 = python_code_.JDTAST_WildcardType(upperBound=[], JDTAST_WildcardType=var_5)
    assert isinstance(var_19, python_code_.JDTAST_WildcardType)
    var_21 = python_code_.JDTAST_SimpleName
    var_22 = "JDTAST_MemberRef"
    var_23 = "|4&xMS"
    var_24 = "_JDTAST_Expression__JDTAST_Expression231 JDTAST_EnumConstantDeclaration139 right_shift_signed _JDTAST_IType__JDTAST_IType44"
    var_25 = python_code_.JDTAST_IField(
        constant=var_21,
        isEnumConstant=var_22,
        typeSignature=var_23,
        isVolatile=var_24,
        isTransient=[2],
    )
    assert isinstance(var_25, python_code_.JDTAST_IField)
    var_27 = python_code_.JDTAST_Annotation()
    var_28 = python_code_.JDTAST_SuperFieldAccess()
    var_29 = python_code_.JDTAST_ThisExpression()
    var_30 = python_code_.JDTAST_Name(
        fullyQualifiedName="@/6gz=`eH&X>m>t#\t",
        JDTAST_Name185=var_27,
        JDTAST_Name274=var_28,
        JDTAST_Name279=var_25,
        JDTAST_Name287=var_29,
    )
    assert isinstance(var_30, python_code_.JDTAST_Name)
    python_code_.JDTAST_InfixExpression(
        operator=var_15, JDTAST_InfixExpression=var_21, JDTAST_InfixExpression240=[]
    )


def test_14():
    var_1 = "JDTAST_MethodDeclaration156 JDTAST_ClassInstanceCreation216 JDTAST_SimpleName124 JDTAST_MethodRefParameter92"
    var_2 = python_code_.JDTAST_ITypeParameter(bounds=var_1)
    assert isinstance(var_2, python_code_.JDTAST_ITypeParameter)
    var_3 = "JDTAST_PackageDeclaration105,JDTAST_IPackageFragment,_JDTAST_Expression__JDTAST_Expression374"
    var_4 = "gWt.'1?}N.h}}"
    var_5 = lambda *args, **kwargs: "\x0c"
    var_6 = python_code_.JDTAST_Modifier(
        abstract=var_3,
        final=var_2,
        native=var_4,
        none=var_1,
        private=var_1,
        protected=var_1,
        public=var_1,
        static=var_3,
        strictfp=var_4,
        synchronized=var_2,
        transient=var_5,
        volatile="J{Xn?;1Sy",
    )
    assert isinstance(var_6, python_code_.JDTAST_Modifier)
    var_10 = python_code_.Type()
    python_code_.JDTAST_Parameter(name=var_6, type=var_10)
    var_13 = "_JDTAST_IType__JDTAST_IType48"
    var_14 = python_code_.JDTAST_IMethod(
        returnType=var_1,
        isConstructor=var_13,
        isMainMethod=var_4,
        exceptionTypes=var_6,
        JDTAST_IMethod263=var_13,
    )
    assert isinstance(var_14, python_code_.JDTAST_IMethod)
    var_20 = python_code_.JDTAST_PhysicalElement(
        path=(-1, True, 1241), isReadOnly=var_5
    )
    assert isinstance(var_20, python_code_.JDTAST_PhysicalElement)
    var_47 = "JDTAST_ArrayCreation196_JDTAST_IType__JDTAST_IType72"
    var_48 = "L\tuFF$p$TedoHSV*"
    var_49 = python_code_.JDTAST_TagElement(tagName=var_47, nested=var_48)
    assert isinstance(var_49, python_code_.JDTAST_TagElement)


@pytest.mark.xfail(strict=True)
def test_15():
    var_1 = python_code_.JDTAST_QualifiedType()
    var_2 = python_code_.InfixExpressionOperatorKind.right_shift_unsigned
    var_4 = python_code_.ASTNode()
    var_7 = "\\\t}9I6HF0|KV#s"
    var_8 = python_code_.JDTAST_IMethod(
        returnType=var_7, isConstructor=var_2, isMainMethod=var_7, exceptionTypes=var_4
    )
    assert isinstance(var_8, python_code_.JDTAST_IMethod)
    var_9 = python_code_.JDTAST_Parameter(
        name=var_7, type={"": "_SQGPU*J2d{"}, JDTAST_Parameter=var_8
    )
    var_15 = python_code_.JDTAST_ArrayType(dimensions=var_7)
    assert isinstance(var_15, python_code_.JDTAST_ArrayType)
    var_16 = python_code_.IMember
    python_code_.JDTAST_ISourceRange(
        length=var_16,
        offset=b"\x1b\x0b\x158\n\x8e.\xe4_\x92f_\xb5a\xa4E\x17",
        JDTAST_ISourceRange34=var_9,
    )
    var_29 = python_code_.JDTAST_ITypeParameter(
        bounds=var_7, JDTAST_ITypeParameter=var_16
    )
    assert isinstance(var_29, python_code_.JDTAST_ITypeParameter)
    var_31 = set()
    python_code_.JDTAST_IType(
        fullyQualifiedParametrizedName=var_16,
        fullyQualifiedName=var_7,
        JDTAST_IType=var_1,
        JDTAST_IType48=var_16,
        JDTAST_IType31=[],
        JDTAST_IType39=var_31,
    )


def test_16():
    var_2 = python_code_.JDTAST_NumberLiteral(token=[False, False])
    assert isinstance(var_2, python_code_.JDTAST_NumberLiteral)
    var_4 = ""
    var_5 = python_code_.JDTAST_ICompilationUnit()
    var_6 = python_code_.JDTAST_IImportDeclaration(
        isOnDemand=True, isStatic=var_4, JDTAST_IImportDeclaration=var_5
    )
    assert isinstance(var_6, python_code_.JDTAST_IImportDeclaration)
    var_7 = "aMAb83"
    var_8 = python_code_.JDTAST_ISourceReference(source=var_7)
    assert isinstance(var_8, python_code_.JDTAST_ISourceReference)
    var_10 = "U0e"
    var_11 = (
        lambda *args, **kwargs: "JDTAST_MethodDeclaration150 JDTAST_Type154 JDTAST_EnhancedForStatement"
    )
    var_53 = python_code_.JDTAST_PhysicalElement(
        path=(-1, True, 1241), isReadOnly=var_11
    )
    assert isinstance(var_53, python_code_.JDTAST_PhysicalElement)
    var_56 = python_code_.JDTAST_BlockComment()
    var_57 = python_code_.ASTNode()
    var_60 = python_code_.JDTAST_IType(
        fullyQualifiedParametrizedName=var_10, fullyQualifiedName=[487.13, 599.28]
    )
    assert isinstance(var_60, python_code_.JDTAST_IType)
    var_61 = {var_60, var_60, var_60, var_60, var_60}
    python_code_.JDTAST_IType(
        fullyQualifiedParametrizedName=var_11,
        fullyQualifiedName=var_11,
        JDTAST_IType=var_56,
        JDTAST_IType44=var_61,
        JDTAST_IType43=var_61,
    )
    var_68 = python_code_.JDTAST_ITypeParameter(bounds=var_57)
    assert isinstance(var_68, python_code_.JDTAST_ITypeParameter)


def test_17():
    var_5 = "@2>"
    var_32 = python_code_.JDTAST_ArrayType(dimensions=var_5)
    assert isinstance(var_32, python_code_.JDTAST_ArrayType)
    var_33 = python_code_.IMember
    var_45 = python_code_.JDTAST_ITypeParameter(
        bounds=var_5, JDTAST_ITypeParameter=var_33
    )
    assert isinstance(var_45, python_code_.JDTAST_ITypeParameter)
    var_49 = python_code_.JDTAST_BooleanLiteral(booleanValue="%Oo")
    assert isinstance(var_49, python_code_.JDTAST_BooleanLiteral)


def test_18():
    var_1 = "JDTAST_MethodDeclaration156 JDTAST_ClassInstanceCreation216 JDTAST_SimpleName124 JDTAST_MethodRefParameter92"
    var_2 = python_code_.JDTAST_ITypeParameter(bounds=var_1)
    assert isinstance(var_2, python_code_.JDTAST_ITypeParameter)
    var_5 = lambda *args, **kwargs: "\x0c"
    var_20 = python_code_.JDTAST_PhysicalElement(
        path=(-1, True, 1241), isReadOnly=var_5
    )
    assert isinstance(var_20, python_code_.JDTAST_PhysicalElement)
    var_47 = "JDTAST_ArrayCreation196_JDTAST_IType__JDTAST_IType72"
    var_48 = "L\tuFF$p$TedoHSV*"
    var_49 = python_code_.JDTAST_TagElement(tagName=var_47, nested=var_48)
    assert isinstance(var_49, python_code_.JDTAST_TagElement)
