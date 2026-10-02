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
    AbortStatement,
    AbortablePart,
    AccessSpecification,
    Aggregate,
    AncestorPart,
    ArrayAggregate,
    ArrayIndexes,
    BasicDeclaration,
    BasicDeclarativeItem,
    Body,
    BodyStub,
    ComponentItem,
    CompositeConstraint,
    CompoundStatement,
    ContextItem,
    DeclarativeBlock,
    DeclarativeItem,
    DiscreteChoice,
    DiscreteRange,
    DiscreteSubtypeDefinition,
    DiscriminantPart,
    EntryIndex,
    ExplicitGenericActualParameter,
    FormalTypeDefinition,
    FullTypeDeclaration,
    GenericFormalParameterDeclaration,
    GenericItem,
    HandledSequenceOfStatements,
    IntegerTypeDefinition,
    Interval,
    LibrarySpecification,
    LibraryUnitSpecification,
    NewTypeDeclaration,
    NotNullAccessDefinition,
    ObjectDeclaration,
    PackageDeclaration,
    ParameterEffectiveValue,
    ParenthesizedExpression,
    Primary,
    ProperBody,
    ProtectedElementDeclaration,
    ProtectedOperationDeclaration,
    ProtectedOperationItem,
    Qualifier,
    Range,
    RangeConstraint,
    RealTypeDefinition,
    RecordAggregate,
    RecordComponentAssociation,
    ReturnSubtypeIndication,
    ScalarConstraint,
    SelectAlternative,
    SelectStatement,
    SimpleStatement,
    Statement,
    SubprogramSpecification,
    TaskItem,
    TriggeringStatement,
    TypeDeclaration,
    TypeDefinition,
    Unit,
    UseClause,
    adb_AbortStatement,
    adb_AbortablePart,
    adb_AcceptAlternative,
    adb_AcceptStatement,
    adb_AccessSpecification,
    adb_AccessToDataDefinition,
    adb_AccessToDataInstance,
    adb_AccessToSubprogramDefinition,
    adb_AccessTypeDefinition,
    adb_Aggregate,
    adb_Allocator,
    adb_AncestorPart,
    adb_AnonymousAccessDefinition,
    adb_ArrayAggregate,
    adb_ArrayComponentAssociation,
    adb_ArrayIndexes,
    adb_ArrayTypeDefinition,
    adb_AspectClause,
    adb_AssignmentStatement,
    adb_AsynchronousSelect,
    adb_AttributeDesignator,
    adb_BasicDeclaration,
    adb_BasicDeclarativeItem,
    adb_BlockStatement,
    adb_Body,
    adb_BodyStub,
    adb_CaseStatement,
    adb_CaseStatementAlternative,
    adb_Compilation,
    adb_CompilationUnit,
    adb_ComponentChoiceList,
    adb_ComponentClause,
    adb_ComponentDeclaration,
    adb_ComponentDefinition,
    adb_ComponentItem,
    adb_ComponentList,
    adb_CompositeConstraint,
    adb_CompoundStatement,
    adb_ConditionalEntryCall,
    adb_ConstrainedIndexes,
    adb_ContextClause,
    adb_ContextItem,
    adb_DataInstanceDeclaration,
    adb_DeclarativeBlock,
    adb_DeclarativeItem,
    adb_DefiningIdentifierList,
    adb_DelayAlternative,
    adb_DelayStatement,
    adb_DeltaConstraint,
    adb_DerivedTypeDefinition,
    adb_DigitsConstraint,
    adb_DiscreteChoice,
    adb_DiscreteChoiceList,
    adb_DiscreteRange,
    adb_DiscreteSubtypeDefinition,
    adb_DiscriminantAssociation,
    adb_DiscriminantConstraint,
    adb_DiscriminantPart,
    adb_DiscriminantSelectors,
    adb_DiscriminantSpecification,
    adb_EObject,
    adb_EntityRange,
    adb_EntryBarrier,
    adb_EntryBody,
    adb_EntryBodyFormalPart,
    adb_EntryCallAlternative,
    adb_EntryDeclaration,
    adb_EntryIndex,
    adb_EntryIndexSpecification,
    adb_EnumerationTypeDefinition,
    adb_ExceptionChoice,
    adb_ExceptionDeclaration,
    adb_ExceptionHandler,
    adb_ExitStatement,
    adb_ExplicitGenericActualParameter,
    adb_ExplicitRange,
    adb_Expression,
    adb_ExtendedReturnStatement,
    adb_ExtensionAggregate,
    adb_Factor,
    adb_FixedPointDefinition,
    adb_FloatingPointDefinition,
    adb_FormalDerivedTypeDefinition,
    adb_FormalObjectDeclaration,
    adb_FormalPackageActualPart,
    adb_FormalPackageAssociation,
    adb_FormalPackageDeclaration,
    adb_FormalPart,
    adb_FormalPrivateTypeDefinition,
    adb_FormalSubprogramDeclaration,
    adb_FormalTypeDeclaration,
    adb_FormalTypeDefinition,
    adb_FullDataTypeDeclaration,
    adb_FullTypeDeclaration,
    adb_FunctionSpecification,
    adb_GenericActualPart,
    adb_GenericAssociation,
    adb_GenericDeclaration,
    adb_GenericFormalParameterDeclaration,
    adb_GenericInstantiation,
    adb_GenericItem,
    adb_GenericItems,
    adb_GotoStatement,
    adb_Guard,
    adb_GuardedAlternative,
    adb_HandledSequenceOfStatements,
    adb_IfStatement,
    adb_IncompleteTypeDeclaration,
    adb_IndexConstraint,
    adb_InitializedComponents,
    adb_IntegerTypeDefinition,
    adb_InterfaceList,
    adb_InterfaceTypeDefinition,
    adb_Interval,
    adb_IterationScheme,
    adb_KnownDiscriminantPart,
    adb_Label,
    adb_LabelisableStatement,
    adb_LibrarySpecification,
    adb_LibraryUnitDeclaration,
    adb_LibraryUnitSpecification,
    adb_LoopParameterSpecification,
    adb_LoopStatement,
    adb_Membership,
    adb_ModClause,
    adb_Mode,
    adb_ModularTypeDefinition,
    adb_Name,
    adb_NamedArrayAggregate,
    adb_NewTypeDeclaration,
    adb_NotNullAccessDefinition,
    adb_Null,
    adb_NullStatement,
    adb_NumberDeclaration,
    adb_NumericLiteral,
    adb_ObjectDeclaration,
    adb_OptConstraint,
    adb_OptNullExclusion,
    adb_OptVariantPart,
    adb_OverridingIndicator,
    adb_PackageBody,
    adb_PackageBodyStub,
    adb_PackageDeclaration,
    adb_PackageDefinition,
    adb_PackageSpecification,
    adb_ParameterAndResultProfile,
    adb_ParameterAssociation,
    adb_ParameterEffectiveValue,
    adb_ParameterSpecification,
    adb_ParenthesizedExpression,
    adb_PositionalArrayAggregate,
    adb_Pragma,
    adb_PragmaArgumentAssociation,
    adb_Primary,
    adb_PrimaryName,
    adb_PrivateExtensionDeclaration,
    adb_PrivateTypeDeclaration,
    adb_ProcedureOrEntryCallStatement,
    adb_ProcedureSpecification,
    adb_ProperBody,
    adb_ProtectedBody,
    adb_ProtectedBodyStub,
    adb_ProtectedDefinition,
    adb_ProtectedElementDeclaration,
    adb_ProtectedOperationDeclaration,
    adb_ProtectedOperationItem,
    adb_ProtectedTypeDeclaration,
    adb_QualifiedName,
    adb_Qualifier,
    adb_RaiseStatement,
    adb_Range,
    adb_RangeConstraint,
    adb_RealRangeSpecification,
    adb_RealTypeDefinition,
    adb_RecordAggregate,
    adb_RecordComponentAssociation,
    adb_RecordComponentAssociationList,
    adb_RecordDefinition,
    adb_RecordExtensionPart,
    adb_RecordTypeDefinition,
    adb_Relation,
    adb_Renaming,
    adb_RequeueStatement,
    adb_ReturnSubtypeIndication,
    adb_ScalarConstraint,
    adb_SelectAlternative,
    adb_SelectStatement,
    adb_SelectiveAccept,
    adb_SeparateSubunit,
    adb_SequenceOfStatements,
    adb_SignedIntegerTypeDefinition,
    adb_SimpleExpression,
    adb_SimpleReturnStatement,
    adb_SimpleStatement,
    adb_SingleProtectedDeclaration,
    adb_Statement,
    adb_StringLiteral,
    adb_SubprogramBody,
    adb_SubprogramDeclaration,
    adb_SubprogramDefault,
    adb_SubprogramSpecification,
    adb_SubtypeDeclaration,
    adb_SubtypeIndication,
    adb_TaskBody,
    adb_TaskBodyStub,
    adb_TaskDeclaration,
    adb_TaskDefinition,
    adb_TaskItem,
    adb_TaskNames,
    adb_Term,
    adb_TimedEntryCall,
    adb_TriggeringAlternative,
    adb_TriggeringStatement,
    adb_TypeDeclaration,
    adb_TypeDefinition,
    adb_UnconstrainedIndexes,
    adb_UninitializedComponents,
    adb_Unit,
    adb_UnknownDiscriminantPart,
    adb_UseClause,
    adb_UsePackageClause,
    adb_UseTypeClause,
    adb_Variant,
    adb_VariantPart,
    adb_WithClause,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.adb_ExitStatement()
    var_1 = python_code_.GenericFormalParameterDeclaration()
    var_2 = python_code_.adb_BlockStatement(blockStatementIdentifier=var_0)
    assert isinstance(var_2, python_code_.adb_BlockStatement)
    var_4 = python_code_.adb_DiscriminantPart()
    var_6 = python_code_.adb_EntryDeclaration(name=var_4, adb_EntryDeclaration54=var_1)
    assert isinstance(var_6, python_code_.adb_EntryDeclaration)
    var_7 = '6$&f-";'
    var_8 = python_code_.DiscreteChoice
    var_9 = True
    var_10 = python_code_.adb_InterfaceList()
    var_11 = python_code_.adb_FormalDerivedTypeDefinition(
        absract=var_7,
        limited=var_8,
        synchronized=var_9,
        adb_FormalDerivedTypeDefinition="P0x\rcSwO]8h",
        adb_FormalDerivedTypeDefinition106=var_10,
    )
    assert isinstance(var_11, python_code_.adb_FormalDerivedTypeDefinition)
    python_code_.adb_RecordDefinition(null=var_7)
    var_16 = python_code_.adb_PositionalArrayAggregate(othersBox=True)
    assert isinstance(var_16, python_code_.adb_PositionalArrayAggregate)
    var_17 = "adb_ComponentDeclaration434:_adb_SubtypeIndication__adb_SubtypeIndication:adb_GenericActualPart115"
    python_code_.adb_GenericAssociation(selectorName=var_17)
    var_25 = "X\\8M:4Uu"
    var_26 = python_code_.adb_AccessToDataInstance(constant=var_25)
    assert isinstance(var_26, python_code_.adb_AccessToDataInstance)


def test_1():
    var_2 = python_code_.adb_OptConstraint()
    var_3 = python_code_.adb_Pragma(name=[], adb_Pragma=var_2)
    assert isinstance(var_3, python_code_.adb_Pragma)
    python_code_.adb_SubprogramDefault(defaultName=-1907)
    var_21 = "adb_PrimaryName_adb_SubprogramDefault__adb_SubprogramDefault_adb_Name__adb_Name363_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration140"
    var_22 = python_code_.adb_Term(multiplyingOperators=var_21)
    var_24 = "z!7(t\t"
    var_25 = python_code_.adb_BlockStatement(blockStatementIdentifier=var_24)
    assert isinstance(var_25, python_code_.adb_BlockStatement)
    var_27 = True
    var_28 = python_code_.adb_PrivateExtensionDeclaration(
        abstract=var_27,
        limited=var_27,
        synchronized=var_22,
        adb_PrivateExtensionDeclaration47=var_24,
    )
    assert isinstance(var_28, python_code_.adb_PrivateExtensionDeclaration)
    var_29 = python_code_.adb_BodyStub(name=True)
    assert isinstance(var_29, python_code_.adb_BodyStub)
    var_31 = python_code_.adb_DelayAlternative()
    var_32 = python_code_.adb_DelayStatement(until=var_24, adb_DelayStatement280=var_31)
    assert isinstance(var_32, python_code_.adb_DelayStatement)
    var_33 = True
    var_34 = lambda *args, **kwargs: -1055
    python_code_.adb_ComponentDefinition(
        aliased=var_33, adb_ComponentDefinition367=var_34
    )
    var_40 = python_code_.adb_NumericLiteral(value=var_24)
    assert isinstance(var_40, python_code_.adb_NumericLiteral)
    var_41 = "L.5xA2R~-j`$=j3/0Q"
    python_code_.adb_RecordDefinition(null=var_41, adb_RecordDefinition421=var_34)


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "$(g{%#dNn "
    var_1 = python_code_.adb_SequenceOfStatements()
    python_code_.adb_ExceptionHandler(
        name=var_0,
        adb_ExceptionHandler=("adb_DerivedTypeDefinition",),
        adb_ExceptionHandler75=var_1,
    )
    var_3 = python_code_.adb_StringLiteral(value=var_0)
    assert isinstance(var_3, python_code_.adb_StringLiteral)
    var_5 = python_code_.adb_SubprogramBody(endname=var_0)
    assert isinstance(var_5, python_code_.adb_SubprogramBody)
    var_8 = python_code_.adb_AccessToDataInstance(constant=var_0)
    assert isinstance(var_8, python_code_.adb_AccessToDataInstance)
    var_11 = abs
    var_12 = False
    var_13 = python_code_.adb_FormalPrivateTypeDefinition(
        abstract=var_8, tagged=var_11, limited=var_12
    )
    assert isinstance(var_13, python_code_.adb_FormalPrivateTypeDefinition)
    var_14 = python_code_.adb_AcceptAlternative()
    var_15 = python_code_.adb_AcceptStatement(
        entryidentifier=var_11, adb_AcceptStatement278=var_14
    )
    assert isinstance(var_15, python_code_.adb_AcceptStatement)
    var_20 = lambda *args, **kwargs: "adb_DiscreteSubtypeDefinition252"
    python_code_.adb_ComponentChoiceList(componentSelectorName=var_15, others=var_20)
    var_24 = python_code_.adb_AnonymousAccessDefinition()
    var_25 = python_code_.adb_DataInstanceDeclaration(
        aliased=var_12, constant=var_20, adb_DataInstanceDeclaration137=var_24
    )
    assert isinstance(var_25, python_code_.adb_DataInstanceDeclaration)
    python_code_.adb_DefiningIdentifierList(
        name=var_11, adb_DefiningIdentifierList126=var_25
    )


def test_3():
    var_0 = python_code_.adb_Pragma
    var_1 = python_code_.adb_WithClause(limited=var_0, private=var_0)
    assert isinstance(var_1, python_code_.adb_WithClause)
    var_2 = python_code_.adb_ProtectedBody(
        identifier=-109, idTask=var_0, adb_ProtectedBody="WwNZca<*0+i2"
    )
    assert isinstance(var_2, python_code_.adb_ProtectedBody)
    var_3 = python_code_.adb_LabelisableStatement()
    var_5 = python_code_.adb_UninitializedComponents(box=var_0)
    assert isinstance(var_5, python_code_.adb_UninitializedComponents)
    var_6 = False
    var_7 = python_code_.adb_DataInstanceDeclaration(aliased=var_3, constant=var_6)
    assert isinstance(var_7, python_code_.adb_DataInstanceDeclaration)
    var_8 = python_code_.adb_SubtypeIndication(
        subtypeMark=var_0, adb_SubtypeIndication=var_2
    )
    assert isinstance(var_8, python_code_.adb_SubtypeIndication)
    var_11 = "JVm:\x0c.kwZVR6s/W-ui"
    var_12 = python_code_.adb_BodyStub(name=var_11)
    assert isinstance(var_12, python_code_.adb_BodyStub)
    var_13 = python_code_.adb_ConditionalEntryCall()
    var_15 = python_code_.adb_FormalTypeDefinition()
    var_16 = python_code_.adb_FormalTypeDeclaration(
        identifier=var_13, adb_FormalTypeDeclaration102=var_15
    )
    assert isinstance(var_16, python_code_.adb_FormalTypeDeclaration)
    var_25 = python_code_.adb_TypeDeclaration(name=var_11)
    assert isinstance(var_25, python_code_.adb_TypeDeclaration)
    var_30 = python_code_.adb_CompilationUnit()
    var_31 = python_code_.adb_Pragma(name=None, adb_Pragma=var_30)
    assert isinstance(var_31, python_code_.adb_Pragma)
    var_41 = python_code_.adb_NumericLiteral(value=var_0)
    assert isinstance(var_41, python_code_.adb_NumericLiteral)


def test_4():
    var_12 = lambda *args, **kwargs: 127
    var_13 = python_code_.adb_UninitializedComponents(box=var_12)
    assert isinstance(var_13, python_code_.adb_UninitializedComponents)
    var_14 = "adb_PragmaArgumentAssociation.adb_Expression549"
    var_15 = python_code_.adb_FormalSubprogramDeclaration(abstract=var_14)
    assert isinstance(var_15, python_code_.adb_FormalSubprogramDeclaration)


@pytest.mark.xfail(strict=True)
def test_5():
    var_6 = python_code_.adb_EntryBodyFormalPart()
    var_7 = python_code_.adb_EntryBarrier()
    var_8 = python_code_.adb_EntryBody(
        endid=(False,), adb_EntryBody239=var_6, adb_EntryBody241=var_7
    )
    assert isinstance(var_8, python_code_.adb_EntryBody)
    var_12 = python_code_.adb_RecordDefinition
    python_code_.adb_PackageSpecification(endname=var_12)
    var_16 = python_code_.adb_CaseStatement()
    var_17 = python_code_.adb_IfStatement()
    var_18 = python_code_.BasicDeclarativeItem
    var_19 = python_code_.adb_Expression(
        booleanOperator=complex(2281.0, -684.954388),
        adb_Expression249=var_12,
        adb_Expression178=var_16,
        adb_Expression162=var_12,
        adb_Expression=set(),
        adb_Expression170=var_17,
        adb_Expression192=None,
        adb_Expression417=[],
        adb_Expression542=var_17,
        adb_Expression549=var_18,
    )
    assert isinstance(var_19, python_code_.adb_Expression)
    var_21 = True
    python_code_.adb_PositionalArrayAggregate(
        othersBox=var_21, adb_PositionalArrayAggregate=var_18
    )


def test_6():
    var_2 = python_code_.adb_DiscriminantAssociation()
    var_3 = "2F:m,[I"
    var_4 = python_code_.adb_SeparateSubunit(parentUnitName=var_3)
    assert isinstance(var_4, python_code_.adb_SeparateSubunit)
    var_6 = python_code_.adb_ComponentDeclaration()
    var_7 = python_code_.adb_ComponentDefinition(
        aliased=(),
        adb_ComponentDefinition367=[True, False, "c5,CL=$At8M"],
        adb_ComponentDefinition432=var_6,
    )
    var_8 = False
    var_9 = python_code_.adb_ComponentClause
    var_10 = python_code_.adb_InterfaceTypeDefinition(
        limited=var_7,
        task=var_8,
        protected=var_9,
        synchro=var_3,
        adb_InterfaceTypeDefinition=var_7,
    )
    assert isinstance(var_10, python_code_.adb_InterfaceTypeDefinition)
    var_12 = python_code_.adb_RealTypeDefinition()
    var_14 = "QNu_]8"
    var_15 = python_code_.adb_BodyStub(name=var_14)
    assert isinstance(var_15, python_code_.adb_BodyStub)
    var_16 = python_code_.adb_Interval()
    var_19 = python_code_.adb_DerivedTypeDefinition(
        limited=var_3,
        abstract=var_3,
        adb_DerivedTypeDefinition=complex(2645.6544, 1755.0),
    )
    assert isinstance(var_19, python_code_.adb_DerivedTypeDefinition)
    var_20 = python_code_.Primary()
    var_22 = False
    var_23 = python_code_.adb_LibraryUnitDeclaration(
        private=var_8, adb_LibraryUnitDeclaration13=var_9
    )
    assert isinstance(var_23, python_code_.adb_LibraryUnitDeclaration)
    var_24 = python_code_.adb_LibraryUnitDeclaration(
        private=var_8, adb_LibraryUnitDeclaration13=var_9
    )
    var_25 = python_code_.adb_WithClause(
        limited=var_22, private="adb_ParameterAndResultProfile387"
    )
    assert isinstance(var_25, python_code_.adb_WithClause)
    var_26 = python_code_.adb_LibraryUnitDeclaration(
        private=var_2,
        adb_LibraryUnitDeclaration13=var_16,
        adb_LibraryUnitDeclaration=var_25,
    )
    var_27 = {var_23, var_23, var_23, var_24, var_26}
    python_code_.adb_WithClause(limited=var_3, private=var_22, adb_WithClause=var_27)
    var_30 = "nXlS\x0cK"
    var_31 = python_code_.adb_EntryDeclaration(name=var_30)
    assert isinstance(var_31, python_code_.adb_EntryDeclaration)
    python_code_.adb_VariantPart(name=var_30)
    python_code_.adb_Term(multiplyingOperators=var_23, adb_Term=var_20)
    var_43 = python_code_.adb_EntryBarrier()
    var_44 = python_code_.adb_NumberDeclaration()
    var_45 = python_code_.adb_IfStatement()
    var_46 = python_code_.adb_ModClause()
    var_47 = python_code_.adb_EntityRange()
    var_48 = python_code_.adb_Expression(
        booleanOperator=var_3,
        adb_Expression249=var_43,
        adb_Expression157=var_44,
        adb_Expression170=var_45,
        adb_Expression202=1593,
        adb_Expression311="'|2^~#t3;[",
        adb_Expression332=var_9,
        adb_Expression437=-1131.97,
        adb_Expression444=var_46,
        adb_Expression465=var_12,
        adb_Expression549=var_15,
        adb_Expression570=var_47,
    )
    assert isinstance(var_48, python_code_.adb_Expression)


def test_7():
    var_6 = python_code_.adb_IncompleteTypeDeclaration(tagged=False)
    assert isinstance(var_6, python_code_.adb_IncompleteTypeDeclaration)


@pytest.mark.xfail(strict=True)
def test_8():
    var_3 = python_code_.RecordAggregate
    var_4 = python_code_.adb_Renaming(renamed=var_3)
    assert isinstance(var_4, python_code_.adb_Renaming)
    python_code_.adb_Pragma(name=-4013, adb_Pragma147=var_3)


def test_9():
    var_0 = python_code_.DiscreteChoice()
    var_1 = python_code_.adb_UnknownDiscriminantPart(box=var_0)
    assert isinstance(var_1, python_code_.adb_UnknownDiscriminantPart)
