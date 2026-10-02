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
    Access,
    BaseAccess,
    BasePath,
    BlockStatement,
    Branch,
    BranchStatement,
    CatchBlock,
    CatchParameter,
    Clone,
    CloneInstance,
    CompositeAccess,
    Constructor,
    DeclarationTypeAccess,
    Delegate,
    Destructor,
    Directory,
    Enum,
    Exit,
    Field,
    File,
    FormalParameter,
    Function,
    FunctionAccess,
    GASTClass,
    GASTExpression,
    GASTType,
    GlobalFunction,
    GlobalFunctionKind,
    GlobalVariable,
    Identifier,
    InheritanceTypeAccess,
    JumpStatementKind,
    LocalVariable,
    LoopStatement,
    LoopStatementKind,
    Member,
    Method,
    ModelAnnotation,
    ModelElement,
    NamedModelElement,
    Package,
    Position,
    Property,
    Root,
    SourceEntity,
    Statement,
    Status,
    StructuralAbstraction,
    ThrowTypeAccess,
    TypeAccess,
    TypeAlias,
    TypeDecorator,
    TypeParameterClass,
    Variable,
    VariableAccess,
    Visibilities,
    abstractmethod,
    annotations_ModelAnnotation,
    core_GenericEntity,
    core_ModelElement,
    core_NamedModelElement,
    core_SourceEntity,
    date,
    datetime,
    functions_Constructor,
    functions_Function,
    functions_GlobalFunction,
    functions_Method,
    gast_accesses_Access,
    gast_accesses_BaseAccess,
    gast_accesses_CastTypeAccess,
    gast_accesses_CompositeAccess,
    gast_accesses_DeclarationTypeAccess,
    gast_accesses_DelegateAccess,
    gast_accesses_FunctionAccess,
    gast_accesses_InheritanceTypeAccess,
    gast_accesses_ParameterInstantiationTypeAccess,
    gast_accesses_PropertyAccess,
    gast_accesses_RunTimeTypeAccess,
    gast_accesses_SelfAccess,
    gast_accesses_StaticTypeAccess,
    gast_accesses_ThrowTypeAccess,
    gast_accesses_TypeAccess,
    gast_accesses_VariableAccess,
    gast_annotations_Attribute,
    gast_annotations_Clone,
    gast_annotations_CloneInstance,
    gast_annotations_Comment,
    gast_annotations_Layer,
    gast_annotations_ModelAnnotation,
    gast_annotations_StructuralAbstraction,
    gast_annotations_Subsystem,
    gast_core_BasePath,
    gast_core_Directory,
    gast_core_File,
    gast_core_GenericEntity,
    gast_core_Identifier,
    gast_core_ModelElement,
    gast_core_NamedModelElement,
    gast_core_Package,
    gast_core_PackageAlias,
    gast_core_Position,
    gast_core_Root,
    gast_core_SourceEntity,
    gast_functions_Constructor,
    gast_functions_Delegate,
    gast_functions_Destructor,
    gast_functions_Function,
    gast_functions_GenericConstructor,
    gast_functions_GenericFunction,
    gast_functions_GenericMethod,
    gast_functions_GlobalFunction,
    gast_functions_Method,
    gast_statements_BlockStatement,
    gast_statements_Branch,
    gast_statements_BranchStatement,
    gast_statements_CatchBlock,
    gast_statements_ExceptionHandler,
    gast_statements_Exit,
    gast_statements_GASTBehaviour,
    gast_statements_GASTExpression,
    gast_statements_JumpStatement,
    gast_statements_LoopStatement,
    gast_statements_Methods,
    gast_statements_SimpleStatement,
    gast_statements_Statement,
    gast_types_GASTArray,
    gast_types_GASTClass,
    gast_types_GASTEnumeration,
    gast_types_GASTStruct,
    gast_types_GASTType,
    gast_types_GASTUnion,
    gast_types_GenericClass,
    gast_types_Member,
    gast_types_Reference,
    gast_types_TypeAlias,
    gast_types_TypeDecorator,
    gast_types_TypeParameterClass,
    gast_variables_CatchParameter,
    gast_variables_Field,
    gast_variables_FormalParameter,
    gast_variables_GlobalVariable,
    gast_variables_LocalVariable,
    gast_variables_Property,
    gast_variables_Variable,
    time,
    types_GASTClass,
    types_GASTType,
    types_Member,
    types_TypeDecorator,
    variables_Field,
    variables_Variable,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.Package()
    var_1 = python_code_.gast_types_TypeAlias(innerTypeAlias=(), typeAliases=var_0)
    assert isinstance(var_1, python_code_.gast_types_TypeAlias)
    var_2 = python_code_.Variable()
    var_3 = python_code_.gast_annotations_ModelAnnotation()
    var_4 = 2
    python_code_.gast_core_Position(
        endColumn=var_3, endLine=1036.72, startLine=var_4, startColumn=var_2
    )
    python_code_.gast_core_ModelElement(
        status=None, sissyId=var_2, gast_core_ModelElement=var_0
    )


def test_1():
    var_0 = python_code_.CatchBlock()
    var_3 = python_code_.gast_variables_Field(propertyField=var_0)
    assert isinstance(var_3, python_code_.gast_variables_Field)
    var_4 = python_code_.gast_functions_Destructor()
    var_5 = python_code_.gast_core_Identifier(id=var_3)
    assert isinstance(var_5, python_code_.gast_core_Identifier)
    var_6 = int
    var_5.idHasToBeUnique(gast_context=var_4, gast_diagnostics=var_6)
    var_9 = python_code_.ModelElement()
    var_15 = False
    var_16 = python_code_.gast_variables_FormalParameter(passedByReference=var_15)
    assert isinstance(var_16, python_code_.gast_variables_FormalParameter)
    var_23 = python_code_.types_TypeDecorator()
    var_24 = -3127
    var_26 = python_code_.gast_annotations_Comment(
        todo=var_24, formal=var_15, todoCount=var_9, texts=None
    )
    assert isinstance(var_26, python_code_.gast_annotations_Comment)
    var_26.OCLtodo(gast_context=var_6, gast_diagnostics=var_26)
    var_34 = python_code_.gast_core_Root(
        linesOfComments=-355,
        linesOfCode=-2687,
        gast_core_Root86=set(),
        root114={
            True,
            "Function311._gast_variables_FormalParameter__formalParameters._gast_functions_Function__gast_functions_Function",
        },
        ModelElement270=None,
        ModelElement=var_3,
    )
    assert isinstance(var_34, python_code_.gast_core_Root)
    var_35 = python_code_.gast_accesses_VariableAccess(write={}, Access84=var_34)
    assert isinstance(var_35, python_code_.gast_accesses_VariableAccess)
    var_39 = False
    python_code_.gast_variables_FormalParameter(
        passedByReference=var_39,
        formalParameters=var_23,
        Variable=[403.99, False, "GASTClass281"],
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.LocalVariable()
    var_2 = False
    var_3 = dict
    var_4 = python_code_.gast_annotations_Comment(
        todo=var_2, formal=var_3, todoCount=var_1, texts=var_1
    )
    assert isinstance(var_4, python_code_.gast_annotations_Comment)
    var_4.OCLtodo(gast_context=0, gast_diagnostics=var_4)
    var_6 = python_code_.gast_functions_GenericMethod()
    var_7 = python_code_.Clone()
    var_8 = 923
    var_9 = python_code_.gast_accesses_BaseAccess
    var_10 = python_code_.gast_core_Position(
        endColumn=var_3, endLine=None, startLine=var_7, startColumn=var_9, position=-128
    )
    var_11 = var_10.EitherAssemblyFileOrSourceFileSet(
        gast_context=var_6, gast_diagnostics=4378
    )
    python_code_.gast_core_Root(
        linesOfComments=var_8,
        linesOfCode=var_2,
        gast_core_Root=var_11,
        gast_core_Root111=var_6,
        ModelElement270=var_4,
        ModelElement=complex(-788.722551, 534.9801603),
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = python_code_.gast_accesses_CompositeAccess()
    var_2 = python_code_.gast_accesses_StaticTypeAccess()
    var_3 = python_code_.JumpStatementKind.JUMP
    var_5 = False
    var_6 = python_code_.gast_functions_Delegate(innerDelegate=var_5, delegates=var_0)
    assert isinstance(var_6, python_code_.gast_functions_Delegate)
    var_7 = python_code_.gast_functions_Constructor(
        initializer=var_3, constructors=var_5
    )
    assert isinstance(var_7, python_code_.gast_functions_Constructor)
    var_8 = 39
    var_9 = -615
    var_10 = lambda *args, **kwargs: ';U"\t8TD>N#3EGs'
    var_11 = python_code_.gast_core_Identifier(id="X$b\x0c1")
    assert isinstance(var_11, python_code_.gast_core_Identifier)
    var_12 = var_11.idHasToBeUnique(gast_context=var_10, gast_diagnostics=var_10)
    var_13 = True
    var_14 = False
    var_15 = -2311
    var_16 = python_code_.gast_core_Position(
        endColumn={},
        endLine=var_6,
        startLine=var_0,
        startColumn=var_15,
        gast_core_Position156=var_10,
    )
    var_17 = python_code_.gast_types_Member(
        visibility=var_3,
        abstract=var_12,
        extern="Directory119",
        introspectable=var_5,
        override=var_5,
        static=var_13,
        typeParameterClassMember=var_14,
        virtual=var_11,
        final=var_2,
        internal=333,
        SourceEntity=var_16,
    )
    assert isinstance(var_17, python_code_.gast_types_Member)
    var_18 = var_17.getSurroundingClass()
    var_19 = var_11.idHasToBeUnique(gast_context=var_2, gast_diagnostics=var_10)
    python_code_.gast_core_Root(
        linesOfComments=var_8,
        linesOfCode=var_9,
        gast_core_Root89=var_10,
        gast_core_Root92=var_10,
        gast_core_Root95=var_12,
        root105=var_18,
        gast_core_Root98=var_19,
        root116=var_13,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = "FVl\x0bDi+9J<D/(<+q;"
    python_code_.gast_statements_Exit(name=var_1)
    var_5 = python_code_.gast_variables_Property()
    var_11 = False
    var_12 = python_code_.gast_types_Reference(explicit=var_11)
    assert isinstance(var_12, python_code_.gast_types_Reference)
    var_13 = python_code_.BranchStatement()
    var_16 = True
    var_17 = python_code_.gast_types_Reference(explicit=var_16)
    var_20 = python_code_.Function
    var_21 = True
    var_22 = True
    var_23 = python_code_.gast_annotations_Comment(
        todo=var_21, formal=var_22, todoCount=var_5, texts=var_1
    )
    assert isinstance(var_23, python_code_.gast_annotations_Comment)
    var_23.OCLtodo(gast_context=complex(4104.41, 1281.73), gast_diagnostics="")
    var_25 = "_gast_types_TypeAlias__innerTypeAliases._gast_functions_Function__surroundingFunction308._gast_core_Package__gast_core_Package59"
    var_26 = python_code_.gast_core_Identifier(id=var_25)
    assert isinstance(var_26, python_code_.gast_core_Identifier)
    var_28 = 0
    var_29 = python_code_.gast_core_Position(
        endColumn=var_20,
        endLine=var_28,
        startLine=var_13,
        startColumn="kC \x0c*Oz",
        gast_core_Position=var_20,
    )
    var_30 = var_29.EitherAssemblyFileOrSourceFileSet(
        gast_context="~#!x", gast_diagnostics=None
    )
    var_31 = var_26.idHasToBeUnique(gast_context=var_20, gast_diagnostics=-780)
    python_code_.gast_core_Root(
        linesOfComments=var_20,
        linesOfCode=var_28,
        gast_core_Root92=var_20,
        gast_core_Root109=403.8,
        gast_core_Root111=var_30,
        root114=var_31,
        root116=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.gast_types_TypeDecorator()
    var_3 = "_gast_statements_Methods__gast_statements_Methods.VISIBILITYPROTECTED.gast_statements_Statement"
    var_4 = False
    var_5 = False
    var_6 = True
    var_7 = False
    var_8 = bytes
    var_9 = python_code_.Member()
    var_10 = python_code_.gast_types_Member(
        visibility=var_3,
        abstract={},
        extern=var_4,
        introspectable=var_5,
        override=var_3,
        static=var_6,
        typeParameterClassMember=var_6,
        virtual=var_7,
        final=var_8,
        internal=var_0,
        gast_types_Member=var_9,
    )
    assert isinstance(var_10, python_code_.gast_types_Member)
    var_11 = var_10.getSurroundingClass()
    var_12 = 3
    var_13 = python_code_.gast_core_Identifier(id={})
    assert isinstance(var_13, python_code_.gast_core_Identifier)
    var_14 = python_code_.core_SourceEntity
    var_15 = var_13.idHasToBeUnique(gast_context=var_14, gast_diagnostics=var_11)
    python_code_.gast_core_Root(
        linesOfComments=var_12,
        linesOfCode=complex(3691.18105, 1379.2),
        gast_core_Root100=var_0,
        root=var_12,
        gast_core_Root107=var_9,
        gast_core_Root109=var_15,
        gast_core_Root98=var_6,
        ModelElement=-615.99,
    )


def test_6():
    var_1 = python_code_.VariableAccess
    var_2 = python_code_.gast_accesses_VariableAccess(
        write=var_1,
        gast_accesses_VariableAccess=True,
        Access={
            "#HgHs5k'M3\n/7;": "",
            "_gast_functions_Function__surroundingFunction FOR _gast_core_Root__gast_core_Root98 gast_statements_GASTBehaviour": 1675,
            "gast_statements_LoopStatement.gast_functions_Delegate": ".`5\x0b) tS#\ti+",
        },
    )
    assert isinstance(var_2, python_code_.gast_accesses_VariableAccess)


def test_7():
    var_2 = python_code_.Variable()
    var_3 = python_code_.gast_annotations_ModelAnnotation()
    var_4 = 2
    var_5 = python_code_.gast_core_Position(
        endColumn=var_3, endLine=1036.72, startLine=var_4, startColumn=var_2
    )
    var_5.EitherAssemblyFileOrSourceFileSet(gast_context=-2442.9, gast_diagnostics=None)
    var_22 = python_code_.gast_variables_FormalParameter(
        passedByReference={
            433.99,
            2796.37,
            "Access303,Directory152,_gast_core_Directory__parentDirectory,Statement298",
        }
    )
    assert isinstance(var_22, python_code_.gast_variables_FormalParameter)


def test_8():
    var_0 = python_code_.gast_accesses_CompositeAccess()
    var_4 = python_code_.FormalParameter()
    var_5 = False
    var_6 = python_code_.gast_functions_Delegate(innerDelegate=var_5, delegates=var_0)
    assert isinstance(var_6, python_code_.gast_functions_Delegate)
    var_10 = lambda *args, **kwargs: ';U"\t8TD>N#3EGs'
    var_11 = python_code_.gast_core_Identifier(id="X$b\x0c1")
    assert isinstance(var_11, python_code_.gast_core_Identifier)
    var_11.idHasToBeUnique(gast_context=var_10, gast_diagnostics=var_10)
    var_13 = True
    var_27 = "_gast_statements_Statement__gast_statements_Statement15-_gast_core_Package__subPackages-_gast_core_Directory__subDirectory-gast_variables_LocalVariable"
    var_28 = 14
    var_29 = -2035
    var_39 = python_code_.gast_core_Directory(
        fullQualifiedPath=var_27, fileSystemPath=var_27, subDirectory=var_4
    )
    assert isinstance(var_39, python_code_.gast_core_Directory)
    var_30 = 0
    var_31 = 3420
    var_32 = True
    var_33 = python_code_.DeclarationTypeAccess()
    var_34 = python_code_.gast_functions_Function(
        numberOfStatements=var_28,
        maximumNestingLevel=var_29,
        linesOfComments=var_10,
        linesOfCode=var_30,
        numberOfEdgesInCFG=var_13,
        numberOfNodesInCFG=var_31,
        operator=var_32,
        function=var_33,
        gast_functions_Function302={},
        surroundingFunction305={
            3967,
            True,
            "_gast_functions_Function__gast_functions_Function302",
        },
    )
    assert isinstance(var_34, python_code_.gast_functions_Function)


def test_9():
    var_0 = python_code_.CatchBlock()
    var_3 = python_code_.gast_variables_Field(propertyField=var_0)
    assert isinstance(var_3, python_code_.gast_variables_Field)
    var_5 = python_code_.gast_core_Identifier(id=var_3)
    assert isinstance(var_5, python_code_.gast_core_Identifier)
    var_6 = int
    var_15 = False
    var_16 = python_code_.gast_variables_FormalParameter(passedByReference=var_15)
    assert isinstance(var_16, python_code_.gast_variables_FormalParameter)
    var_25 = -1679
    var_32 = var_5.idHasToBeUnique(gast_context=136, gast_diagnostics=var_6)
    var_33 = python_code_.gast_accesses_Access()
    var_34 = python_code_.gast_core_Root(
        linesOfComments=var_25,
        linesOfCode=var_6,
        gast_core_Root86=var_32,
        root114={
            "GASTClass96,_gast_core_Package__packages,_gast_core_Package__gast_core_Package53,_gast_core_Root__gast_core_Root": 1964,
            "qu9@\r\nC]~<bb": -2625,
        },
        ModelElement270=var_33,
    )
    assert isinstance(var_34, python_code_.gast_core_Root)
    var_35 = python_code_.gast_accesses_VariableAccess(write={}, Access84=var_34)
    assert isinstance(var_35, python_code_.gast_accesses_VariableAccess)


def test_10():
    var_9 = python_code_.gast_functions_Method(propertyMethod=1011.0)
    assert isinstance(var_9, python_code_.gast_functions_Method)
    var_10 = python_code_.gast_types_GASTEnumeration()
    var_12 = False
    var_13 = python_code_.gast_functions_Constructor(
        initializer=var_12, constructors=var_10
    )
    assert isinstance(var_13, python_code_.gast_functions_Constructor)


def test_11():
    var_0 = True
    var_1 = False
    var_2 = True
    var_3 = False
    var_4 = python_code_.gast_types_Member(
        visibility=True,
        abstract=var_0,
        extern=var_1,
        introspectable=var_1,
        override=var_0,
        static=var_0,
        typeParameterClassMember=[False, -3418],
        virtual=var_2,
        final=var_3,
        internal=var_0,
        SourceEntity=[-1036, "G9.=~^^uV\tC", "_gast_core_File__gast_core_File134"],
    )
    assert isinstance(var_4, python_code_.gast_types_Member)
    var_9 = "}}Ig$ak^XaZO1m<ic"
    var_10 = python_code_.gast_accesses_StaticTypeAccess
    var_11 = python_code_.gast_core_NamedModelElement(
        simpleName=var_9, ModelElement112=var_10
    )
    assert isinstance(var_11, python_code_.gast_core_NamedModelElement)
    var_18 = python_code_.gast_functions_Constructor(initializer=var_1)
    assert isinstance(var_18, python_code_.gast_functions_Constructor)
    var_19 = python_code_.gast_types_TypeDecorator()
    var_21 = python_code_.gast_accesses_SelfAccess(super=var_1)
    assert isinstance(var_21, python_code_.gast_accesses_SelfAccess)
    var_23 = python_code_.gast_accesses_DeclarationTypeAccess()
    var_24 = python_code_.gast_variables_CatchParameter(
        rethrown=var_19, Variable=var_23
    )
    assert isinstance(var_24, python_code_.gast_variables_CatchParameter)
    var_25 = python_code_.gast_types_GASTEnumeration()
    var_26 = python_code_.gast_types_TypeAlias(
        innerTypeAlias=complex(2422.9454349, 1492.234572), innerTypeAliases=var_25
    )
    assert isinstance(var_26, python_code_.gast_types_TypeAlias)


def test_12():
    var_2 = python_code_.functions_Method
    var_3 = python_code_.gast_types_Reference(explicit=var_2)
    assert isinstance(var_3, python_code_.gast_types_Reference)
    var_4 = python_code_.gast_accesses_SelfAccess(super=var_2)
    assert isinstance(var_4, python_code_.gast_accesses_SelfAccess)
    var_7 = python_code_.gast_types_GenericClass()
    var_13 = python_code_.gast_core_Identifier(id=var_7)
    assert isinstance(var_13, python_code_.gast_core_Identifier)
    var_13.idHasToBeUnique(gast_context=var_7, gast_diagnostics=[])


def test_13():
    var_1 = python_code_.gast_accesses_RunTimeTypeAccess()
    var_2 = python_code_.functions_Method
    var_3 = python_code_.gast_types_Reference(explicit=var_2)
    assert isinstance(var_3, python_code_.gast_types_Reference)
    var_4 = python_code_.gast_accesses_SelfAccess(super=var_2)
    assert isinstance(var_4, python_code_.gast_accesses_SelfAccess)
    var_7 = python_code_.gast_types_GenericClass()
    var_10 = -598
    var_11 = 1
    var_12 = python_code_.DeclarationTypeAccess()
    var_13 = python_code_.gast_core_Identifier(id=var_7)
    assert isinstance(var_13, python_code_.gast_core_Identifier)
    var_14 = var_13.idHasToBeUnique(gast_context=var_7, gast_diagnostics=[])
    var_15 = python_code_.gast_functions_Function(
        numberOfStatements=var_10,
        maximumNestingLevel=var_1,
        linesOfComments=var_10,
        linesOfCode=var_7,
        numberOfEdgesInCFG=var_11,
        numberOfNodesInCFG=var_2,
        operator=[False],
        function=var_12,
        surroundingFunction308=["OG?|oEc*", True, True],
        surroundingFunction=var_14,
    )
    assert isinstance(var_15, python_code_.gast_functions_Function)


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = python_code_.CatchBlock()
    var_3 = python_code_.gast_variables_Field(propertyField=var_0)
    assert isinstance(var_3, python_code_.gast_variables_Field)
    var_4 = python_code_.gast_functions_Destructor()
    var_5 = python_code_.gast_core_Identifier(id=var_3)
    assert isinstance(var_5, python_code_.gast_core_Identifier)
    var_6 = int
    var_5.idHasToBeUnique(gast_context=var_4, gast_diagnostics=var_6)
    var_8 = python_code_.types_GASTType()
    var_9 = python_code_.ModelElement()
    var_13 = python_code_.gast_statements_GASTBehaviour()
    var_15 = False
    var_16 = python_code_.gast_variables_FormalParameter(passedByReference=var_15)
    assert isinstance(var_16, python_code_.gast_variables_FormalParameter)
    var_24 = -3127
    var_25 = -1679
    var_26 = python_code_.gast_annotations_Comment(
        todo=var_24, formal=var_15, todoCount=var_9, texts=None
    )
    assert isinstance(var_26, python_code_.gast_annotations_Comment)
    var_27 = var_26.OCLtodo(gast_context=var_6, gast_diagnostics=var_26)
    python_code_.gast_functions_Function(
        numberOfStatements=var_13,
        maximumNestingLevel=var_5,
        linesOfComments=var_24,
        linesOfCode=var_25,
        numberOfEdgesInCFG=var_8,
        numberOfNodesInCFG=var_24,
        operator=var_15,
        gast_functions_Function300=var_8,
        surroundingFunction308=var_27,
    )


def test_15():
    var_20 = True
    var_21 = python_code_.gast_accesses_InheritanceTypeAccess(
        implementationInheritance=var_20
    )
    assert isinstance(var_21, python_code_.gast_accesses_InheritanceTypeAccess)
    python_code_.gast_core_Position(
        endColumn=-820,
        endLine=14,
        startLine=var_20,
        startColumn=1,
        gast_core_Position=var_21,
        position=None,
    )


def test_16():
    var_1 = python_code_.LocalVariable()
    var_2 = False
    var_3 = dict
    var_4 = python_code_.gast_annotations_Comment(
        todo=var_2, formal=var_3, todoCount=var_1, texts=var_1
    )
    assert isinstance(var_4, python_code_.gast_annotations_Comment)
    var_4.OCLtodo(gast_context=0, gast_diagnostics=var_4)
    var_6 = python_code_.gast_functions_GenericMethod()
    var_7 = python_code_.Clone()
    var_9 = python_code_.gast_accesses_BaseAccess
    var_10 = python_code_.gast_core_Position(
        endColumn=var_3, endLine=None, startLine=var_7, startColumn=var_9, position=-128
    )
    var_10.EitherAssemblyFileOrSourceFileSet(gast_context=var_6, gast_diagnostics=4378)


def test_17():
    var_0 = python_code_.gast_accesses_DelegateAccess()
    var_1 = python_code_.Member()
    var_2 = python_code_.gast_statements_Statement
    var_3 = python_code_.gast_accesses_BaseAccess()
    var_4 = python_code_.gast_statements_LoopStatement(
        kind=var_0,
        gast_statements_LoopStatement=var_0,
        loopstatement=-1058.43,
        Statement16=var_2,
        Statement240=var_3,
        Statement19=var_1,
        Statement242=var_0,
    )
    assert isinstance(var_4, python_code_.gast_statements_LoopStatement)
    var_10 = "FaU+`k|!JOTqB"
    var_11 = python_code_.gast_statements_Branch()
    python_code_.gast_statements_LoopStatement(
        kind=var_10,
        gast_statements_LoopStatement=var_2,
        Statement27=var_11,
        Statement298=b"\xce\x04 \x80\x95\x9el\xee\xbd\xef \x8a\xdc",
        Statement19=var_2,
    )


def test_18():
    var_0 = python_code_.gast_accesses_CompositeAccess()
    var_4 = python_code_.FormalParameter()
    var_5 = False
    var_6 = python_code_.gast_functions_Delegate(innerDelegate=var_5, delegates=var_0)
    assert isinstance(var_6, python_code_.gast_functions_Delegate)
    var_10 = lambda *args, **kwargs: ';U"\t8TD>N#3EGs'
    var_11 = python_code_.gast_core_Identifier(id="X$b\x0c1")
    assert isinstance(var_11, python_code_.gast_core_Identifier)
    var_11.idHasToBeUnique(gast_context=var_10, gast_diagnostics=var_10)
    var_13 = True
    var_27 = "_gast_statements_Statement__gast_statements_Statement15-_gast_core_Package__subPackages-_gast_core_Directory__subDirectory-gast_variables_LocalVariable"
    var_28 = 14
    var_29 = -2035
    var_39 = python_code_.gast_core_Directory(
        fullQualifiedPath=var_27, fileSystemPath=var_27, subDirectory=var_4
    )
    assert isinstance(var_39, python_code_.gast_core_Directory)
    var_30 = 0
    var_31 = 3420
    var_32 = True
    var_33 = python_code_.DeclarationTypeAccess()
    var_34 = python_code_.gast_functions_Function(
        numberOfStatements=var_28,
        maximumNestingLevel=var_29,
        linesOfComments=var_10,
        linesOfCode=var_30,
        numberOfEdgesInCFG=var_13,
        numberOfNodesInCFG=var_31,
        operator=var_32,
        function=var_33,
        gast_functions_Function302={},
        surroundingFunction305={
            3967,
            True,
            "_gast_functions_Function__gast_functions_Function302",
        },
    )
    assert isinstance(var_34, python_code_.gast_functions_Function)
    var_35 = 1077
    var_36 = 1657
    var_37 = python_code_.gast_statements_Statement(
        numberOfComments=var_35,
        linesOfCode=var_10,
        numberOfEdgesInCFG=var_36,
        numberOfStatements=1574.64,
        maximumNestingLevel=var_28,
        numberOfNodesInCFG=var_10,
        gast_statements_Statement="_gast_core_Root__gast_core_Root",
        gast_statements_Statement15=(True, True, -2885.97),
        SourceEntity=var_10,
    )
    assert isinstance(var_37, python_code_.gast_statements_Statement)
    var_38 = python_code_.gast_statements_JumpStatement(
        kind=var_27,
        Statement298=var_34,
        Statement=var_34,
        Statement16=var_37,
        Statement167=var_29,
    )
    assert isinstance(var_38, python_code_.gast_statements_JumpStatement)


def test_19():
    var_1 = python_code_.VariableAccess
    var_2 = python_code_.gast_accesses_VariableAccess(
        write=var_1,
        gast_accesses_VariableAccess=True,
        Access={
            "#HgHs5k'M3\n/7;": "",
            "_gast_functions_Function__surroundingFunction FOR _gast_core_Root__gast_core_Root98 gast_statements_GASTBehaviour": 1675,
            "gast_statements_LoopStatement.gast_functions_Delegate": ".`5\x0b) tS#\ti+",
        },
    )
    assert isinstance(var_2, python_code_.gast_accesses_VariableAccess)
    var_11 = False
    var_12 = python_code_.gast_accesses_ThrowTypeAccess(declared=var_11)
    assert isinstance(var_12, python_code_.gast_accesses_ThrowTypeAccess)
