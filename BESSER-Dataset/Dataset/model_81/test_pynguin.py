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
    AbstractMethodDeclaration,
    AbstractMethodInvocation,
    AbstractTypeDeclaration,
    AbstractTypeQualifiedExpression,
    AbstractVariablesContainer,
    AnnotationTypeDeclaration,
    AnnotationTypeMemberDeclaration,
    AssignmentKind,
    BodyDeclaration,
    ClassDeclaration,
    Comment,
    Enum,
    EnumDeclaration,
    Expression,
    InfixExpressionKind,
    InheritanceKind,
    InterfaceDeclaration,
    LabeledStatement,
    MethodDeclaration,
    NamedElement,
    NamespaceAccess,
    PostfixExpressionKind,
    PrefixExpressionKind,
    PrimitiveType,
    SingleVariableDeclaration,
    Statement,
    Type,
    TypeDeclaration,
    UnresolvedItem,
    VariableDeclaration,
    VariableDeclarationFragment,
    VisibilityKind,
    abstractmethod,
    date,
    datetime,
    java__ASTNode,
    java__AbstractMethodDeclaration,
    java__AbstractMethodInvocation,
    java__AbstractTypeDeclaration,
    java__AbstractTypeQualifiedExpression,
    java__AbstractVariablesContainer,
    java__Annotation,
    java__AnnotationMemberValuePair,
    java__AnnotationTypeDeclaration,
    java__AnnotationTypeMemberDeclaration,
    java__AnonymousClassDeclaration,
    java__Archive,
    java__ArrayAccess,
    java__ArrayCreation,
    java__ArrayInitializer,
    java__ArrayLengthAccess,
    java__ArrayType,
    java__AssertStatement,
    java__Assignment,
    java__Block,
    java__BlockComment,
    java__BodyDeclaration,
    java__BooleanLiteral,
    java__BreakStatement,
    java__CastExpression,
    java__CatchClause,
    java__CharacterLiteral,
    java__ClassDeclaration,
    java__ClassFile,
    java__ClassInstanceCreation,
    java__Comment,
    java__CompilationUnit,
    java__ConditionalExpression,
    java__ConstructorDeclaration,
    java__ConstructorInvocation,
    java__ContinueStatement,
    java__DoStatement,
    java__EmptyStatement,
    java__EnhancedForStatement,
    java__EnumConstantDeclaration,
    java__EnumDeclaration,
    java__Expression,
    java__ExpressionStatement,
    java__FieldAccess,
    java__FieldDeclaration,
    java__ForStatement,
    java__IfStatement,
    java__ImportDeclaration,
    java__InfixExpression,
    java__Initializer,
    java__InstanceofExpression,
    java__InterfaceDeclaration,
    java__Javadoc,
    java__LabeledStatement,
    java__LineComment,
    java__Manifest,
    java__ManifestAttribute,
    java__ManifestEntry,
    java__MemberRef,
    java__MethodDeclaration,
    java__MethodInvocation,
    java__MethodRef,
    java__MethodRefParameter,
    java__Model,
    java__Modifier,
    java__NamedElement,
    java__NamespaceAccess,
    java__NullLiteral,
    java__NumberLiteral,
    java__Package,
    java__PackageAccess,
    java__ParameterizedType,
    java__ParenthesizedExpression,
    java__PostfixExpression,
    java__PrefixExpression,
    java__PrimitiveType,
    java__PrimitiveTypeBoolean,
    java__PrimitiveTypeByte,
    java__PrimitiveTypeChar,
    java__PrimitiveTypeDouble,
    java__PrimitiveTypeFloat,
    java__PrimitiveTypeInt,
    java__PrimitiveTypeLong,
    java__PrimitiveTypeShort,
    java__PrimitiveTypeVoid,
    java__QueryCollection,
    java__ReturnStatement,
    java__SingleVariableAccess,
    java__SingleVariableDeclaration,
    java__Statement,
    java__StringLiteral,
    java__SuperConstructorInvocation,
    java__SuperFieldAccess,
    java__SuperMethodInvocation,
    java__SwitchCase,
    java__SwitchStatement,
    java__SynchronizedStatement,
    java__TagElement,
    java__TextElement,
    java__ThisExpression,
    java__ThrowStatement,
    java__TryStatement,
    java__Type,
    java__TypeAccess,
    java__TypeDeclaration,
    java__TypeDeclarationStatement,
    java__TypeLiteral,
    java__TypeParameter,
    java__UnresolvedAnnotationDeclaration,
    java__UnresolvedAnnotationTypeMemberDeclaration,
    java__UnresolvedClassDeclaration,
    java__UnresolvedEnumDeclaration,
    java__UnresolvedInterfaceDeclaration,
    java__UnresolvedItem,
    java__UnresolvedItemAccess,
    java__UnresolvedLabeledStatement,
    java__UnresolvedMethodDeclaration,
    java__UnresolvedSingleVariableDeclaration,
    java__UnresolvedType,
    java__UnresolvedTypeDeclaration,
    java__UnresolvedVariableDeclarationFragment,
    java__VariableDeclaration,
    java__VariableDeclarationExpression,
    java__VariableDeclarationFragment,
    java__VariableDeclarationStatement,
    java__WhileStatement,
    java__WildCardType,
    time,
)


def test_0():
    var_0 = python_code_.java__SwitchCase(default=("#P _\tRAA\r1O@\x0b\n%",))
    assert isinstance(var_0, python_code_.java__SwitchCase)
    var_22 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_28 = python_code_.java__QueryCollection()
    var_28.textElementInJavadoc(java__self_=var_22)


def test_1():
    var_19 = "ImportDeclaration"
    var_25 = True
    var_26 = python_code_.java__MethodRefParameter(
        name=var_19,
        varargs=var_25,
        java__MethodRefParameter233=b"\xda*\xeb\x1c\xf5\xf3\xd3\x13\x1b\xe8\xc5/\xbd\xb7\xc5\xb7\t\xe3\xd0",
    )
    assert isinstance(var_26, python_code_.java__MethodRefParameter)
    var_32 = python_code_.java__TypeAccess()
    var_33 = python_code_.java__ArrayType(dimensions=var_25, java__ArrayType=var_32)
    assert isinstance(var_33, python_code_.java__ArrayType)


def test_2():
    var_2 = True
    var_3 = python_code_.java__WildCardType(upperBound=var_2, java__WildCardType=False)
    assert isinstance(var_3, python_code_.java__WildCardType)
    var_7 = python_code_.java__Expression()
    var_8 = python_code_.java__PostfixExpression(
        operator="java__Package", java__PostfixExpression=var_7
    )
    assert isinstance(var_8, python_code_.java__PostfixExpression)
    var_69 = True
    var_73 = python_code_.java__ImportDeclaration(static=var_69)
    assert isinstance(var_73, python_code_.java__ImportDeclaration)
    var_74 = python_code_.java__StringLiteral(
        escapedValue=b"\\+\xca\xb3;_k\xf1\x8e\xc50"
    )
    assert isinstance(var_74, python_code_.java__StringLiteral)


def test_3():
    var_0 = python_code_.java__ArrayInitializer()
    var_1 = python_code_.java__BooleanLiteral(value=(-343, 993.56, False))
    assert isinstance(var_1, python_code_.java__BooleanLiteral)
    var_2 = python_code_.PostfixExpressionKind
    var_3 = True
    var_4 = python_code_.java__ASTNode()
    var_5 = python_code_.java__Comment(
        content=var_2,
        enclosedByParent=var_1,
        prefixOfParent=var_3,
        java__Comment41=var_4,
        java__Comment=var_0,
        java__Comment18=False,
    )
    assert isinstance(var_5, python_code_.java__Comment)
    var_10 = python_code_.java__TypeLiteral()
    var_11 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_12 = python_code_.java__CharacterLiteral(escapedValue=var_11)
    assert isinstance(var_12, python_code_.java__CharacterLiteral)
    var_13 = "java__AbstractTypeDeclaration17"
    var_14 = python_code_.java__StringLiteral(escapedValue=var_13)
    assert isinstance(var_14, python_code_.java__StringLiteral)
    var_26 = python_code_.java__CompilationUnit(
        originalFilePath=var_10,
        java__CompilationUnit108=False,
        java__CompilationUnit134=var_2,
    )
    assert isinstance(var_26, python_code_.java__CompilationUnit)
    var_28 = python_code_.java__QueryCollection()
    var_28.textElementInJavadoc(java__self_=var_11)


def test_4():
    var_32 = python_code_.java__BooleanLiteral(value=(-343, 993.56, False))
    assert isinstance(var_32, python_code_.java__BooleanLiteral)
    var_39 = python_code_.ASTNode
    var_40 = "_java__MethodDeclaration__redefinedMethodDeclaration"
    var_58 = python_code_.java__CompilationUnit(
        originalFilePath=var_40,
        java__CompilationUnit=var_39,
        java__CompilationUnit134=[False, 1529, 1924],
    )
    assert isinstance(var_58, python_code_.java__CompilationUnit)
    var_60 = python_code_.java__ArrayType(
        dimensions="!P", java__ArrayType=b"\x94i\xc1\xae\t\x9f\xd70\x9a\x9c\x1e"
    )
    assert isinstance(var_60, python_code_.java__ArrayType)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.java__UnresolvedSingleVariableDeclaration()
    var_2 = True
    var_3 = python_code_.java__WildCardType(upperBound=var_2, java__WildCardType=False)
    assert isinstance(var_3, python_code_.java__WildCardType)
    var_4 = python_code_.java__LineComment()
    var_7 = python_code_.java__Expression()
    var_8 = python_code_.java__PostfixExpression(
        operator=var_2, java__PostfixExpression=var_7
    )
    assert isinstance(var_8, python_code_.java__PostfixExpression)
    var_13 = python_code_.ASTNode
    var_14 = "_java__MethodDeclaration__redefinedMethodDeclaration"
    var_15 = True
    var_16 = python_code_.java__Modifier(
        visibility=var_13,
        inheritance=var_14,
        static=var_13,
        transient=-2486,
        volatile=var_15,
        native=var_0,
        strictfp=var_13,
        synchronized=var_3,
    )
    assert isinstance(var_16, python_code_.java__Modifier)
    var_27 = python_code_.java__UnresolvedItemAccess()
    var_36 = python_code_.java__CompilationUnit(
        originalFilePath=var_14,
        java__CompilationUnit=var_13,
        java__CompilationUnit134=[False, 1529, 1924],
    )
    assert isinstance(var_36, python_code_.java__CompilationUnit)
    python_code_.java__ClassFile(
        originalFilePath=var_27,
        java__ClassFile104=var_13,
        java__ClassFile107=var_36,
        java__ClassFile110=var_4,
    )


def test_6():
    var_4 = True
    var_5 = python_code_.java__SwitchCase(default=var_4)
    assert isinstance(var_5, python_code_.java__SwitchCase)
    var_8 = python_code_.java__ASTNode()
    var_9 = python_code_.java__ClassFile(
        originalFilePath="_java__ClassFile__java__ClassFile245._java__Comment__java__Comment130._java__ManifestAttribute__java__ManifestAttribute.java__NamedElement",
        java__ClassFile46=var_8,
    )
    assert isinstance(var_9, python_code_.java__ClassFile)
    var_15 = ""
    var_16 = python_code_.java__CharacterLiteral(escapedValue=var_15)
    assert isinstance(var_16, python_code_.java__CharacterLiteral)


def test_7():
    var_0 = python_code_.java__ArrayInitializer()
    var_1 = python_code_.java__BooleanLiteral(value=(-343, 993.56, False))
    assert isinstance(var_1, python_code_.java__BooleanLiteral)
    var_2 = python_code_.PostfixExpressionKind
    var_3 = True
    var_4 = python_code_.java__ASTNode()
    var_5 = python_code_.java__Comment(
        content=var_2,
        enclosedByParent=var_1,
        prefixOfParent=var_3,
        java__Comment41=var_4,
        java__Comment=var_0,
        java__Comment18=False,
    )
    assert isinstance(var_5, python_code_.java__Comment)
    var_8 = python_code_.java__PrimitiveTypeInt()
    var_9 = python_code_.java__Initializer()
    var_13 = "java__AbstractTypeDeclaration17"
    var_14 = python_code_.java__StringLiteral(escapedValue=var_13)
    assert isinstance(var_14, python_code_.java__StringLiteral)
    var_15 = python_code_.java__Package()
    var_24 = python_code_.java__ClassFile(
        originalFilePath=", HY\\gh]iQ||4]u[Q\r",
        java__ClassFile107=var_9,
        java__ClassFile110=var_15,
        java__ClassFile245=var_8,
    )
    assert isinstance(var_24, python_code_.java__ClassFile)
    python_code_.java__QueryCollection()


def test_8():
    var_1 = python_code_.java__Archive(originalFilePath=None)
    assert isinstance(var_1, python_code_.java__Archive)
    var_45 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_46 = python_code_.java__CharacterLiteral(escapedValue=var_45)
    assert isinstance(var_46, python_code_.java__CharacterLiteral)
    var_47 = "java__AbstractTypeDeclaration17"
    var_48 = python_code_.java__StringLiteral(escapedValue=var_47)
    assert isinstance(var_48, python_code_.java__StringLiteral)
    var_49 = python_code_.java__Package()
    var_50 = python_code_.java__ClassFile(
        originalFilePath=-1709.46, java__ClassFile110=var_49
    )
    assert isinstance(var_50, python_code_.java__ClassFile)
    var_53 = python_code_.java__QueryCollection()
    var_53.textElementInJavadoc(java__self_=var_45)


def test_9():
    var_0 = python_code_.java__AbstractTypeDeclaration()
    var_1 = python_code_.java__Comment(
        content=1663.22,
        enclosedByParent=-374,
        prefixOfParent={True, 5506.05, True},
        java__Comment=var_0,
    )
    assert isinstance(var_1, python_code_.java__Comment)


def test_10():
    var_0 = python_code_.java__SwitchCase(default=("#P _\tRAA\r1O@\x0b\n%",))
    assert isinstance(var_0, python_code_.java__SwitchCase)
    var_6 = python_code_.java__NamespaceAccess()
    var_8 = python_code_.java__EmptyStatement
    var_9 = "m4Lxj~QN"
    var_10 = False
    var_11 = False
    var_12 = python_code_.java__BodyDeclaration()
    var_13 = python_code_.java__Modifier(
        visibility=var_8,
        inheritance=var_9,
        static=var_10,
        transient=var_10,
        volatile=[],
        native="_=K~LwjM~Ub\x0bC",
        strictfp=False,
        synchronized=var_11,
        modifier257=var_6,
        modifier=var_12,
    )
    assert isinstance(var_13, python_code_.java__Modifier)


def test_11():
    var_3 = python_code_.java__SuperMethodInvocation()
    var_4 = python_code_.java__PrimitiveTypeLong()
    var_9 = python_code_.java__PrefixExpression(
        operator=None, java__PrefixExpression=[]
    )
    assert isinstance(var_9, python_code_.java__PrefixExpression)
    var_11 = "K`#\n[vqU0PN}zE-"
    var_12 = lambda *args, **kwargs: True
    python_code_.java__ManifestAttribute(
        key=var_11, value=var_12, java__ManifestAttribute212=var_4
    )
    var_14 = python_code_.PrefixExpressionKind.PLUS
    var_15 = 'l<$STzb^TUb"Aj?[Z]|'
    var_16 = "_java__SwitchCase__java__SwitchCase java__Model244"
    var_17 = True
    var_18 = True
    var_19 = python_code_.java__VariableDeclarationExpression()
    var_20 = python_code_.java__Modifier(
        visibility=var_15,
        inheritance=var_16,
        static=None,
        transient=[],
        volatile=var_17,
        native=var_17,
        strictfp=var_12,
        synchronized=var_18,
        modifier257=var_19,
    )
    assert isinstance(var_20, python_code_.java__Modifier)
    var_27 = python_code_.java__MethodRef()
    var_29 = python_code_.AbstractMethodInvocation()
    var_31 = python_code_.java__NumberLiteral(tokenValue=var_16)
    assert isinstance(var_31, python_code_.java__NumberLiteral)
    var_32 = ";"
    var_33 = python_code_.java__TagElement(tagName=var_32)
    assert isinstance(var_33, python_code_.java__TagElement)
    var_34 = True
    var_35 = True
    python_code_.java__Modifier(
        visibility=var_14,
        inheritance=var_3,
        static=var_18,
        transient=var_29,
        volatile=var_34,
        native=var_35,
        strictfp=var_35,
        synchronized=var_27,
        Modifier=var_4,
        modifier257=var_19,
    )


def test_12():
    var_1 = python_code_.java__QueryCollection()
    var_2 = python_code_.java__PackageAccess
    var_3 = python_code_.java__SingleVariableDeclaration(
        varargs={}, singleVariableDeclaration=var_1, parameters=-1, exception=var_2
    )
    assert isinstance(var_3, python_code_.java__SingleVariableDeclaration)
    var_4 = python_code_.java__ClassDeclaration()
    var_5 = python_code_.java__ExpressionStatement()
    var_8 = "ImportDeclaration"
    var_9 = False
    var_10 = python_code_.java__Modifier(
        visibility=var_5,
        inheritance=var_8,
        static=var_9,
        transient=var_2,
        volatile=var_4,
        native=(),
        strictfp=var_2,
        synchronized=var_9,
    )
    assert isinstance(var_10, python_code_.java__Modifier)
    var_15 = True
    var_16 = python_code_.java__MethodRefParameter(
        name=var_8,
        varargs=var_15,
        java__MethodRefParameter233=b"\xda*\xeb\x1c\xf5\xf3\xd3\x13\x1b\xe8\xc5/\xbd\xb7\xc5\xb7\t\xe3\xd0",
    )
    assert isinstance(var_16, python_code_.java__MethodRefParameter)
    python_code_.java__ManifestEntry(name=var_2)
    var_1.grabats09()
    var_24 = python_code_.java__TypeAccess()
    var_25 = python_code_.java__ArrayType(dimensions=var_15, java__ArrayType=var_24)
    assert isinstance(var_25, python_code_.java__ArrayType)


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = True
    var_1 = python_code_.java__WildCardType(upperBound=var_0)
    assert isinstance(var_1, python_code_.java__WildCardType)
    var_2 = python_code_.java__IfStatement()
    var_6 = python_code_.java__VariableDeclarationExpression()
    var_7 = python_code_.java__ImportDeclaration(static=var_2)
    assert isinstance(var_7, python_code_.java__ImportDeclaration)
    var_8 = True
    var_9 = python_code_.java__WhileStatement
    var_10 = True
    var_11 = python_code_.java__Modifier(
        visibility={'~3\tkWl3cJpqa"V&j', 214},
        inheritance=var_7,
        static=var_8,
        transient=var_9,
        volatile=var_10,
        native=None,
        strictfp=var_8,
        synchronized=var_8,
        modifier255=None,
        modifier257=var_6,
        Modifier360=var_9,
    )
    assert isinstance(var_11, python_code_.java__Modifier)
    var_16 = python_code_.java__QueryCollection()
    var_17 = var_16.grabats09()
    python_code_.java__Model(
        name=var_8, java__Model=var_6, java__Model239=var_17, Model=var_17
    )


def test_14():
    var_11 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_26 = python_code_.java__PostfixExpression(operator=var_11)
    assert isinstance(var_26, python_code_.java__PostfixExpression)
    var_34 = python_code_.Type
    var_35 = python_code_.java__ImportDeclaration(static=set(), usagesInImports=var_34)
    assert isinstance(var_35, python_code_.java__ImportDeclaration)


@pytest.mark.xfail(strict=True)
def test_15():
    var_1 = python_code_.java__Archive(originalFilePath=None)
    assert isinstance(var_1, python_code_.java__Archive)
    var_2 = python_code_.java__AnonymousClassDeclaration()
    var_10 = python_code_.java__UnresolvedClassDeclaration()
    var_12 = python_code_.java__ImportDeclaration(static=var_2)
    assert isinstance(var_12, python_code_.java__ImportDeclaration)
    python_code_.java__MethodDeclaration(
        extraArrayDimensions=var_12,
        redefinitions=var_10,
        redefinedMethodDeclaration=var_12,
    )


def test_16():
    var_3 = python_code_.java__SuperMethodInvocation()
    var_4 = python_code_.java__PrimitiveTypeLong()
    var_9 = python_code_.java__PrefixExpression(
        operator=None, java__PrefixExpression=[]
    )
    assert isinstance(var_9, python_code_.java__PrefixExpression)
    var_11 = "K`#\n[vqU0PN}zE-"
    var_12 = lambda *args, **kwargs: True
    python_code_.java__ManifestAttribute(
        key=var_11, value=var_12, java__ManifestAttribute212=var_4
    )
    var_14 = python_code_.PrefixExpressionKind.PLUS
    var_15 = 'l<$STzb^TUb"Aj?[Z]|'
    var_16 = "_java__SwitchCase__java__SwitchCase java__Model244"
    var_17 = True
    var_18 = True
    var_19 = python_code_.java__VariableDeclarationExpression()
    var_20 = python_code_.java__Modifier(
        visibility=var_15,
        inheritance=var_16,
        static=None,
        transient=[],
        volatile=var_17,
        native=var_17,
        strictfp=var_12,
        synchronized=var_18,
        modifier257=var_19,
    )
    assert isinstance(var_20, python_code_.java__Modifier)
    var_27 = python_code_.java__MethodRef()
    var_29 = python_code_.AbstractMethodInvocation()
    var_31 = python_code_.java__NumberLiteral(tokenValue=var_16)
    assert isinstance(var_31, python_code_.java__NumberLiteral)
    var_32 = ";"
    var_33 = python_code_.java__TagElement(tagName=var_32)
    assert isinstance(var_33, python_code_.java__TagElement)
    var_34 = True
    var_35 = True
    python_code_.java__Modifier(
        visibility=var_14,
        inheritance=var_3,
        static=var_18,
        transient=var_29,
        volatile=var_34,
        native=var_35,
        strictfp=var_35,
        synchronized=var_27,
        Modifier=var_4,
        modifier257=var_19,
    )
    python_code_.java__ManifestAttribute(key=var_16, value=var_12)
    var_38 = python_code_.java__SwitchCase(default=var_17)
    assert isinstance(var_38, python_code_.java__SwitchCase)


def test_17():
    var_1 = python_code_.java__SuperFieldAccess
    var_2 = python_code_.java__ImportDeclaration(static=var_1, usagesInImports=var_1)
    assert isinstance(var_2, python_code_.java__ImportDeclaration)


def test_18():
    var_11 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_26 = python_code_.java__PostfixExpression(operator=var_11)
    assert isinstance(var_26, python_code_.java__PostfixExpression)
    var_47 = True
    var_51 = python_code_.java__ImportDeclaration(static=var_47)
    assert isinstance(var_51, python_code_.java__ImportDeclaration)


def test_19():
    var_1 = python_code_.java__QueryCollection()
    var_2 = python_code_.java__PackageAccess
    var_3 = python_code_.java__SingleVariableDeclaration(
        varargs={}, singleVariableDeclaration=var_1, parameters=-1, exception=var_2
    )
    assert isinstance(var_3, python_code_.java__SingleVariableDeclaration)


def test_20():
    python_code_.java__UnresolvedSingleVariableDeclaration()


def test_21():
    var_0 = True
    var_1 = python_code_.java__WildCardType(upperBound=var_0)
    assert isinstance(var_1, python_code_.java__WildCardType)
    var_3 = python_code_.java__VariableDeclarationExpression()
    var_7 = python_code_.java__ImportDeclaration(
        static=True, java__ImportDeclaration=var_0
    )
    assert isinstance(var_7, python_code_.java__ImportDeclaration)
    var_16 = python_code_.java__QueryCollection()
    var_16.grabats09()
    var_19 = python_code_.AnnotationTypeMemberDeclaration()
    var_20 = python_code_.java__NamedElement(
        name=var_19, proxy={1451.47, True}, java__NamedElement=var_3
    )
    assert isinstance(var_20, python_code_.java__NamedElement)
    var_37 = ""
    var_38 = python_code_.java__CharacterLiteral(escapedValue=var_37)
    assert isinstance(var_38, python_code_.java__CharacterLiteral)


def test_22():
    var_3 = python_code_.java__BooleanLiteral(value=2)
    assert isinstance(var_3, python_code_.java__BooleanLiteral)


def test_23():
    var_19 = "ImportDeclaration"
    var_25 = False
    var_26 = python_code_.java__MethodRefParameter(
        name=var_19,
        varargs=var_25,
        java__MethodRefParameter233=b"\xda*\xeb\x1c\xf5\xf3\xd3\x13\x1b\xe8\xc5/\xbd\xb7\xc5\xb7\t\xe3\xd0",
    )
    assert isinstance(var_26, python_code_.java__MethodRefParameter)
    var_32 = python_code_.java__TypeAccess()
    var_33 = python_code_.java__ArrayType(dimensions=var_25, java__ArrayType=var_32)
    assert isinstance(var_33, python_code_.java__ArrayType)
    var_44 = "java__ASTNode43"
    var_45 = True
    var_46 = python_code_.java__Comment(
        content=var_44,
        enclosedByParent=[],
        prefixOfParent=var_45,
        java__Comment130={
            "java__Expression81_java__VariableDeclaration__java__VariableDeclaration": 1933,
            "w[mZrz:>XMD": 1,
            "_java__Comment__java__Comment41 java__TypeAccess79 RIGHT_SHIFT_SIGNED": 1447.26,
        },
    )
    assert isinstance(var_46, python_code_.java__Comment)
    var_47 = python_code_.java__SwitchCase(default=var_45)
    assert isinstance(var_47, python_code_.java__SwitchCase)


def test_24():
    var_0 = python_code_.java__ArrayInitializer()
    var_1 = python_code_.java__BooleanLiteral(value=(-343, 993.56, False))
    assert isinstance(var_1, python_code_.java__BooleanLiteral)
    var_2 = python_code_.PostfixExpressionKind
    var_3 = True
    var_4 = python_code_.java__ASTNode()
    var_5 = python_code_.java__Comment(
        content=var_2,
        enclosedByParent=var_1,
        prefixOfParent=var_3,
        java__Comment41=var_4,
        java__Comment=var_0,
        java__Comment18=False,
    )
    assert isinstance(var_5, python_code_.java__Comment)
    var_37 = (
        "abstractjava__ASTNode322_java__VariableDeclaration__VariableDeclarationprivate"
    )
    var_38 = python_code_.java__CharacterLiteral(escapedValue=var_37)
    assert isinstance(var_38, python_code_.java__CharacterLiteral)
    var_39 = "java__AbstractTypeDeclaration17"
    var_40 = python_code_.java__StringLiteral(escapedValue=var_39)
    assert isinstance(var_40, python_code_.java__StringLiteral)
    var_41 = python_code_.java__Package()
    var_42 = python_code_.java__ClassFile(
        originalFilePath=-1709.46, java__ClassFile110=var_41
    )
    assert isinstance(var_42, python_code_.java__ClassFile)
    var_45 = python_code_.java__QueryCollection()
    var_45.textElementInJavadoc(java__self_=var_39)
    var_49 = python_code_.java__VariableDeclarationStatement(extraArrayDimensions=var_2)
    assert isinstance(var_49, python_code_.java__VariableDeclarationStatement)
