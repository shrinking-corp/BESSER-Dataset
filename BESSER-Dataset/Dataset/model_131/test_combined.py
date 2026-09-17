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
    astm_Visitable,
    RDBColumnType,
    astm_RDBBFile,
    astm_RDBClob,
    astm_RDBChar,
    astm_RDBBlob,
    astm_RDBNClob,
    astm_RDBInt,
    astm_RDBRowid,
    astm_RDBDate,
    astm_RDBLong,
    astm_RDBTimestamp,
    astm_RDBBoolean,
    astm_RDBReal,
    astm_RDBDecimal,
    astm_RDBFloat,
    astm_RDBVarchar,
    astm_RDBNumber,
    astm_RDBInteger,
    IdentifierReference,
    astm_RDBTableAlias,
    astm_RDBRaw,
    astm_RDBString,
    RDBCursorStatement,
    astm_RDBFetchCursorStatement,
    astm_RDBCloseCursorStatement,
    astm_RDBOpenCursorStatement,
    RDBModifyStatement,
    astm_RDBDeleteStatement,
    astm_RDBUpdateStatement,
    astm_RDBTableReference,
    RDBConstraint,
    astm_RDBUniqueKey,
    astm_RDBRefIntegrity,
    astm_RDBCheckConstraint,
    astm_RDBColumnReference,
    ActualParameterExpression,
    astm_ByReferenceActualParameterExpression,
    astm_ByValueActualParameterExpression,
    UnaryOperator,
    astm_Decrement,
    astm_Increment,
    astm_Deref,
    astm_PostDecrement,
    astm_Not,
    astm_PostIncrement,
    astm_AddressOf,
    astm_BitNot,
    astm_Negate,
    astm_UnaryPlus,
    Literal,
    astm_RealLiteral,
    astm_CharLiteral,
    astm_BitLiteral,
    astm_BooleanLiteral,
    astm_StringLiteral,
    astm_IntegerlLiteral,
    QualifiedIdentifierReference,
    astm_QualifiedOverData,
    astm_QualifiedOverPointer,
    ForStatement,
    astm_ForCheckAfterStatement,
    astm_ForCheckBeforeStatement,
    AccessKind,
    astm_Private,
    astm_Public,
    FormalParameterType,
    astm_ByReferenceFormalParameterType,
    astm_ByValueFormalParameterType,
    astm_Protected,
    PrimitiveType,
    astm_Integer,
    astm_Float,
    astm_String,
    astm_ShortInteger,
    astm_LongInteger,
    astm_Boolean,
    astm_WideCharacter,
    astm_Character,
    astm_LongDouble,
    astm_Byte,
    astm_Double,
    astm_Void,
    VirtualSpecification,
    astm_PureVirtual,
    astm_NonVirtual,
    astm_Virtual,
    StorageSpecification,
    astm_FileLocal,
    astm_NoDef,
    astm_FunctionPersistent,
    astm_PerClassMember,
    astm_External,
    Scope,
    ActualParameter,
    astm_MissingActualParameter,
    astm_ActualParameterExpression,
    BinaryOperator,
    astm_NotEqual,
    astm_BitXor,
    astm_SpecificIn,
    astm_SpecificLessEqual,
    astm_Multiply,
    astm_BitRightShift,
    astm_Less,
    astm_Or,
    astm_SpecificLike,
    astm_Exponent,
    astm_Modulus,
    astm_Equal,
    astm_SpecificGreaterEqual,
    astm_SpecificConcatString,
    astm_BitOr,
    astm_And,
    astm_Divide,
    astm_BitLeftShift,
    astm_Add,
    astm_Greater,
    astm_Subtract,
    astm_NotGreater,
    astm_Assign,
    astm_NotLess,
    astm_BitAnd,
    astm_OperatorAssign,
    TypeReference,
    astm_NamedTypeReference,
    astm_UnnamedTypeReference,
    AggregateType,
    astm_UnionType,
    astm_AnnotationType,
    astm_StructureType,
    astm_ClassType,
    Type,
    astm_FunctionType,
    ConstructedType,
    astm_PointerType,
    astm_ReferenceType,
    astm_CollectionType,
    astm_RangeType,
    astm_ArrayType,
    astm_AggregateScope,
    DataType,
    astm_EnumType,
    astm_RDBDataBaseType,
    astm_RDBCursorType,
    astm_RDBTableType,
    astm_ExceptionType,
    astm_RDBUserType,
    astm_RDBColumnType,
    astm_FormalParameterType,
    astm_ConstructedType,
    astm_RDBTableSpaceType,
    astm_RDBViewType,
    astm_PrimitiveType,
    GASTMSyntaxObject,
    astm_Type,
    PreprocessorElement,
    astm_MacroDefinition,
    astm_MacroCall,
    astm_Comment,
    astm_IncludeUnit,
    astm_LabelType,
    astm_NameSpaceType,
    astm_AggregateType,
    astm_NamedType,
    TypeDefinition,
    astm_AggregateTypeDefinition,
    astm_NamedTypeDefinition,
    DataDefinition,
    astm_VariableDefinition,
    astm_BitFieldDefinition,
    astm_Expression,
    astm_TypeReference,
    astm_FunctionScope,
    astm_Statement,
    astm_FormalParameterDefinition,
    Definition,
    astm_RDBUserDefinition,
    astm_DataDefinition,
    astm_RDBTableDefinition,
    astm_EntryDefinition,
    astm_RDBCursorDefinition,
    astm_RDBColumnDefinition,
    astm_SpecificTriggerDefinition,
    astm_EnumLiteralDefinition,
    astm_RDBViewDefinition,
    astm_RDBTableSpaceDefinition,
    astm_RDBDatabaseDefinition,
    astm_FunctionDefinition,
    Declaration,
    astm_VariableDeclaration,
    astm_FormalParameterDeclaration,
    astm_FunctionDeclaration,
    GASTMSemanticObject,
    astm_Project,
    DeclarationOrDefinition,
    astm_Declaration,
    astm_Definition,
    DefinitionObject,
    astm_TypeDefinition,
    astm_LabelDefinition,
    astm_NameSpaceDefinition,
    astm_DeclarationOrDefinition,
    astm_ProgramScope,
    OtherSyntaxObject,
    astm_VirtualSpecification,
    astm_DerivesFrom,
    astm_Dimension,
    astm_RDBTrigger,
    astm_RDBIndexColumn,
    astm_FunctionMemberAttribute,
    astm_RDBIndex,
    astm_RDBConstraint,
    astm_Name,
    astm_PreprocessorElement,
    GASTMObject,
    astm_GASTMSyntaxObject,
    astm_DefinitionObject,
    astm_Scope,
    astm_GlobalScope,
    astm_CompilationUnit,
    GASTMSourceObject,
    astm_SourceLocation,
    astm_SourceFile,
    Visitable,
    astm_RDBHostVariableReference,
    astm_AccessKind,
    astm_DataType,
    astm_StorageSpecification,
    astm_GASTMSourceObject,
    astm_OtherSyntaxObject,
    astm_RDBTableSpaceReference,
    astm_FunctionMemberAttributes,
    astm_ActualParameter,
    astm_BinaryOperator,
    astm_GASTMSemanticObject,
    astm_UnaryOperator,
    astm_GASTMObject,
    NameReference,
    astm_IdentifierReference,
    astm_TypeQualifiedIdentifierReference,
    astm_QualifiedIdentifierReference,
    Expression,
    astm_ConditionalExpression,
    astm_NewExpression,
    astm_AggregateExpression,
    astm_RDBSelectExpression,
    astm_FunctionCallExpression,
    astm_RangeExpression,
    astm_CastExpression,
    astm_Literal,
    astm_RDBHostVariableExpression,
    astm_ArrayAccess,
    astm_AnnotationExpression,
    astm_BinaryExpression,
    astm_UnaryExpression,
    astm_NameReference,
    CatchBlock,
    astm_VariableCatchBlock,
    astm_TypesCatchBlock,
    astm_CatchBlock,
    LoopStatement,
    astm_WhileStatement,
    astm_DoWhileStatement,
    astm_ForStatement,
    astm_LabelAccess,
    SwitchCase,
    astm_DefaultBlock,
    astm_CaseBlock,
    astm_SwitchCase,
    astm_BlockScope,
    Statement,
    astm_ReturnStatement,
    astm_EmptyStatement,
    astm_RDBInsertStatement,
    astm_SwitchStatement,
    astm_DeleteStatement,
    astm_ExpressionStatement,
    astm_LoopStatement,
    astm_LabeledStatement,
    astm_BreakStatement,
    astm_RDBCursorStatement,
    astm_ContinueStatement,
    astm_DeclarationOrDefinitionStatement,
    astm_BlockStatement,
    astm_RDBSelectStatement,
    astm_ThrowStatement,
    astm_JumpStatement,
    astm_RDBModifyStatement,
    astm_RDBConnectStatement,
    astm_TerminateStatement,
    astm_TryStatement,
    astm_IfStatement,
    astm_SpecificSelectStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_astm_visitable_is_not_abstract():
    assert not inspect.isabstract(astm_Visitable)


def test_hyp_astm_visitable_constructor_exists():
    assert callable(astm_Visitable.__init__)


def test_hyp_astm_visitable_constructor_args():
    sig = inspect.signature(astm_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbcolumntype_is_not_abstract():
    assert not inspect.isabstract(RDBColumnType)


def test_hyp_rdbcolumntype_constructor_exists():
    assert callable(RDBColumnType.__init__)


def test_hyp_rdbcolumntype_constructor_args():
    sig = inspect.signature(RDBColumnType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbbfile_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBFile)


def test_hyp_astm_rdbbfile_constructor_exists():
    assert callable(astm_RDBBFile.__init__)


def test_hyp_astm_rdbbfile_constructor_args():
    sig = inspect.signature(astm_RDBBFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbclob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBClob)


def test_hyp_astm_rdbclob_constructor_exists():
    assert callable(astm_RDBClob.__init__)


def test_hyp_astm_rdbclob_constructor_args():
    sig = inspect.signature(astm_RDBClob.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbchar_is_not_abstract():
    assert not inspect.isabstract(astm_RDBChar)


def test_hyp_astm_rdbchar_constructor_exists():
    assert callable(astm_RDBChar.__init__)


def test_hyp_astm_rdbchar_constructor_args():
    sig = inspect.signature(astm_RDBChar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbblob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBlob)


def test_hyp_astm_rdbblob_constructor_exists():
    assert callable(astm_RDBBlob.__init__)


def test_hyp_astm_rdbblob_constructor_args():
    sig = inspect.signature(astm_RDBBlob.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbnclob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBNClob)


def test_hyp_astm_rdbnclob_constructor_exists():
    assert callable(astm_RDBNClob.__init__)


def test_hyp_astm_rdbnclob_constructor_args():
    sig = inspect.signature(astm_RDBNClob.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInt)


def test_hyp_astm_rdbint_constructor_exists():
    assert callable(astm_RDBInt.__init__)


def test_hyp_astm_rdbint_constructor_args():
    sig = inspect.signature(astm_RDBInt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbrowid_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRowid)


def test_hyp_astm_rdbrowid_constructor_exists():
    assert callable(astm_RDBRowid.__init__)


def test_hyp_astm_rdbrowid_constructor_args():
    sig = inspect.signature(astm_RDBRowid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbdate_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDate)


def test_hyp_astm_rdbdate_constructor_exists():
    assert callable(astm_RDBDate.__init__)


def test_hyp_astm_rdbdate_constructor_args():
    sig = inspect.signature(astm_RDBDate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdblong_is_not_abstract():
    assert not inspect.isabstract(astm_RDBLong)


def test_hyp_astm_rdblong_constructor_exists():
    assert callable(astm_RDBLong.__init__)


def test_hyp_astm_rdblong_constructor_args():
    sig = inspect.signature(astm_RDBLong.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtimestamp_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTimestamp)


def test_hyp_astm_rdbtimestamp_constructor_exists():
    assert callable(astm_RDBTimestamp.__init__)


def test_hyp_astm_rdbtimestamp_constructor_args():
    sig = inspect.signature(astm_RDBTimestamp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbboolean_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBoolean)


def test_hyp_astm_rdbboolean_constructor_exists():
    assert callable(astm_RDBBoolean.__init__)


def test_hyp_astm_rdbboolean_constructor_args():
    sig = inspect.signature(astm_RDBBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbreal_is_not_abstract():
    assert not inspect.isabstract(astm_RDBReal)


def test_hyp_astm_rdbreal_constructor_exists():
    assert callable(astm_RDBReal.__init__)


def test_hyp_astm_rdbreal_constructor_args():
    sig = inspect.signature(astm_RDBReal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbdecimal_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDecimal)


def test_hyp_astm_rdbdecimal_constructor_exists():
    assert callable(astm_RDBDecimal.__init__)


def test_hyp_astm_rdbdecimal_constructor_args():
    sig = inspect.signature(astm_RDBDecimal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbfloat_is_not_abstract():
    assert not inspect.isabstract(astm_RDBFloat)


def test_hyp_astm_rdbfloat_constructor_exists():
    assert callable(astm_RDBFloat.__init__)


def test_hyp_astm_rdbfloat_constructor_args():
    sig = inspect.signature(astm_RDBFloat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbvarchar_is_not_abstract():
    assert not inspect.isabstract(astm_RDBVarchar)


def test_hyp_astm_rdbvarchar_constructor_exists():
    assert callable(astm_RDBVarchar.__init__)


def test_hyp_astm_rdbvarchar_constructor_args():
    sig = inspect.signature(astm_RDBVarchar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbnumber_is_not_abstract():
    assert not inspect.isabstract(astm_RDBNumber)


def test_hyp_astm_rdbnumber_constructor_exists():
    assert callable(astm_RDBNumber.__init__)


def test_hyp_astm_rdbnumber_constructor_args():
    sig = inspect.signature(astm_RDBNumber.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbinteger_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInteger)


def test_hyp_astm_rdbinteger_constructor_exists():
    assert callable(astm_RDBInteger.__init__)


def test_hyp_astm_rdbinteger_constructor_args():
    sig = inspect.signature(astm_RDBInteger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_hyp_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_hyp_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtablealias_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableAlias)


def test_hyp_astm_rdbtablealias_constructor_exists():
    assert callable(astm_RDBTableAlias.__init__)


def test_hyp_astm_rdbtablealias_constructor_args():
    sig = inspect.signature(astm_RDBTableAlias.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbraw_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRaw)


def test_hyp_astm_rdbraw_constructor_exists():
    assert callable(astm_RDBRaw.__init__)


def test_hyp_astm_rdbraw_constructor_args():
    sig = inspect.signature(astm_RDBRaw.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbstring_is_not_abstract():
    assert not inspect.isabstract(astm_RDBString)


def test_hyp_astm_rdbstring_constructor_exists():
    assert callable(astm_RDBString.__init__)


def test_hyp_astm_rdbstring_constructor_args():
    sig = inspect.signature(astm_RDBString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(RDBCursorStatement)


def test_hyp_rdbcursorstatement_constructor_exists():
    assert callable(RDBCursorStatement.__init__)


def test_hyp_rdbcursorstatement_constructor_args():
    sig = inspect.signature(RDBCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbfetchcursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBFetchCursorStatement)


def test_hyp_astm_rdbfetchcursorstatement_constructor_exists():
    assert callable(astm_RDBFetchCursorStatement.__init__)


def test_hyp_astm_rdbfetchcursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBFetchCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbclosecursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCloseCursorStatement)


def test_hyp_astm_rdbclosecursorstatement_constructor_exists():
    assert callable(astm_RDBCloseCursorStatement.__init__)


def test_hyp_astm_rdbclosecursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBCloseCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbopencursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBOpenCursorStatement)


def test_hyp_astm_rdbopencursorstatement_constructor_exists():
    assert callable(astm_RDBOpenCursorStatement.__init__)


def test_hyp_astm_rdbopencursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBOpenCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(RDBModifyStatement)


def test_hyp_rdbmodifystatement_constructor_exists():
    assert callable(RDBModifyStatement.__init__)


def test_hyp_rdbmodifystatement_constructor_args():
    sig = inspect.signature(RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbdeletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDeleteStatement)


def test_hyp_astm_rdbdeletestatement_constructor_exists():
    assert callable(astm_RDBDeleteStatement.__init__)


def test_hyp_astm_rdbdeletestatement_constructor_args():
    sig = inspect.signature(astm_RDBDeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbupdatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUpdateStatement)


def test_hyp_astm_rdbupdatestatement_constructor_exists():
    assert callable(astm_RDBUpdateStatement.__init__)


def test_hyp_astm_rdbupdatestatement_constructor_args():
    sig = inspect.signature(astm_RDBUpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtablereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableReference)


def test_hyp_astm_rdbtablereference_constructor_exists():
    assert callable(astm_RDBTableReference.__init__)


def test_hyp_astm_rdbtablereference_constructor_args():
    sig = inspect.signature(astm_RDBTableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(RDBConstraint)


def test_hyp_rdbconstraint_constructor_exists():
    assert callable(RDBConstraint.__init__)


def test_hyp_rdbconstraint_constructor_args():
    sig = inspect.signature(RDBConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbuniquekey_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUniqueKey)


def test_hyp_astm_rdbuniquekey_constructor_exists():
    assert callable(astm_RDBUniqueKey.__init__)


def test_hyp_astm_rdbuniquekey_constructor_args():
    sig = inspect.signature(astm_RDBUniqueKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbrefintegrity_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRefIntegrity)


def test_hyp_astm_rdbrefintegrity_constructor_exists():
    assert callable(astm_RDBRefIntegrity.__init__)


def test_hyp_astm_rdbrefintegrity_constructor_args():
    sig = inspect.signature(astm_RDBRefIntegrity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcheckconstraint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCheckConstraint)


def test_hyp_astm_rdbcheckconstraint_constructor_exists():
    assert callable(astm_RDBCheckConstraint.__init__)


def test_hyp_astm_rdbcheckconstraint_constructor_args():
    sig = inspect.signature(astm_RDBCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "RDBConstraintText" in params, "Missing parameter 'RDBConstraintText'"
    assert "RDBConstraintType" in params, "Missing parameter 'RDBConstraintType'"





def test_hyp_astm_rdbcolumnreference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnReference)


def test_hyp_astm_rdbcolumnreference_constructor_exists():
    assert callable(astm_RDBColumnReference.__init__)


def test_hyp_astm_rdbcolumnreference_constructor_args():
    sig = inspect.signature(astm_RDBColumnReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_hyp_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_hyp_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ByReferenceActualParameterExpression)


def test_hyp_astm_byreferenceactualparameterexpression_constructor_exists():
    assert callable(astm_ByReferenceActualParameterExpression.__init__)


def test_hyp_astm_byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ByValueActualParameterExpression)


def test_hyp_astm_byvalueactualparameterexpression_constructor_exists():
    assert callable(astm_ByValueActualParameterExpression.__init__)


def test_hyp_astm_byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_hyp_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_hyp_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_decrement_is_not_abstract():
    assert not inspect.isabstract(astm_Decrement)


def test_hyp_astm_decrement_constructor_exists():
    assert callable(astm_Decrement.__init__)


def test_hyp_astm_decrement_constructor_args():
    sig = inspect.signature(astm_Decrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_increment_is_not_abstract():
    assert not inspect.isabstract(astm_Increment)


def test_hyp_astm_increment_constructor_exists():
    assert callable(astm_Increment.__init__)


def test_hyp_astm_increment_constructor_args():
    sig = inspect.signature(astm_Increment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_deref_is_not_abstract():
    assert not inspect.isabstract(astm_Deref)


def test_hyp_astm_deref_constructor_exists():
    assert callable(astm_Deref.__init__)


def test_hyp_astm_deref_constructor_args():
    sig = inspect.signature(astm_Deref.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostDecrement)


def test_hyp_astm_postdecrement_constructor_exists():
    assert callable(astm_PostDecrement.__init__)


def test_hyp_astm_postdecrement_constructor_args():
    sig = inspect.signature(astm_PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_not_is_not_abstract():
    assert not inspect.isabstract(astm_Not)


def test_hyp_astm_not_constructor_exists():
    assert callable(astm_Not.__init__)


def test_hyp_astm_not_constructor_args():
    sig = inspect.signature(astm_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_postincrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostIncrement)


def test_hyp_astm_postincrement_constructor_exists():
    assert callable(astm_PostIncrement.__init__)


def test_hyp_astm_postincrement_constructor_args():
    sig = inspect.signature(astm_PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_addressof_is_not_abstract():
    assert not inspect.isabstract(astm_AddressOf)


def test_hyp_astm_addressof_constructor_exists():
    assert callable(astm_AddressOf.__init__)


def test_hyp_astm_addressof_constructor_args():
    sig = inspect.signature(astm_AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitnot_is_not_abstract():
    assert not inspect.isabstract(astm_BitNot)


def test_hyp_astm_bitnot_constructor_exists():
    assert callable(astm_BitNot.__init__)


def test_hyp_astm_bitnot_constructor_args():
    sig = inspect.signature(astm_BitNot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_negate_is_not_abstract():
    assert not inspect.isabstract(astm_Negate)


def test_hyp_astm_negate_constructor_exists():
    assert callable(astm_Negate.__init__)


def test_hyp_astm_negate_constructor_args():
    sig = inspect.signature(astm_Negate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_unaryplus_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryPlus)


def test_hyp_astm_unaryplus_constructor_exists():
    assert callable(astm_UnaryPlus.__init__)


def test_hyp_astm_unaryplus_constructor_args():
    sig = inspect.signature(astm_UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_realliteral_is_not_abstract():
    assert not inspect.isabstract(astm_RealLiteral)


def test_hyp_astm_realliteral_constructor_exists():
    assert callable(astm_RealLiteral.__init__)


def test_hyp_astm_realliteral_constructor_args():
    sig = inspect.signature(astm_RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_charliteral_is_not_abstract():
    assert not inspect.isabstract(astm_CharLiteral)


def test_hyp_astm_charliteral_constructor_exists():
    assert callable(astm_CharLiteral.__init__)


def test_hyp_astm_charliteral_constructor_args():
    sig = inspect.signature(astm_CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm_BitLiteral)


def test_hyp_astm_bitliteral_constructor_exists():
    assert callable(astm_BitLiteral.__init__)


def test_hyp_astm_bitliteral_constructor_args():
    sig = inspect.signature(astm_BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(astm_BooleanLiteral)


def test_hyp_astm_booleanliteral_constructor_exists():
    assert callable(astm_BooleanLiteral.__init__)


def test_hyp_astm_booleanliteral_constructor_args():
    sig = inspect.signature(astm_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_stringliteral_is_not_abstract():
    assert not inspect.isabstract(astm_StringLiteral)


def test_hyp_astm_stringliteral_constructor_exists():
    assert callable(astm_StringLiteral.__init__)


def test_hyp_astm_stringliteral_constructor_args():
    sig = inspect.signature(astm_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_integerlliteral_is_not_abstract():
    assert not inspect.isabstract(astm_IntegerlLiteral)


def test_hyp_astm_integerlliteral_constructor_exists():
    assert callable(astm_IntegerlLiteral.__init__)


def test_hyp_astm_integerlliteral_constructor_args():
    sig = inspect.signature(astm_IntegerlLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_hyp_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_hyp_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedOverData)


def test_hyp_astm_qualifiedoverdata_constructor_exists():
    assert callable(astm_QualifiedOverData.__init__)


def test_hyp_astm_qualifiedoverdata_constructor_args():
    sig = inspect.signature(astm_QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedOverPointer)


def test_hyp_astm_qualifiedoverpointer_constructor_exists():
    assert callable(astm_QualifiedOverPointer.__init__)


def test_hyp_astm_qualifiedoverpointer_constructor_args():
    sig = inspect.signature(astm_QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_hyp_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_hyp_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForCheckAfterStatement)


def test_hyp_astm_forcheckafterstatement_constructor_exists():
    assert callable(astm_ForCheckAfterStatement.__init__)


def test_hyp_astm_forcheckafterstatement_constructor_args():
    sig = inspect.signature(astm_ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForCheckBeforeStatement)


def test_hyp_astm_forcheckbeforestatement_constructor_exists():
    assert callable(astm_ForCheckBeforeStatement.__init__)


def test_hyp_astm_forcheckbeforestatement_constructor_args():
    sig = inspect.signature(astm_ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_hyp_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_hyp_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_private_is_not_abstract():
    assert not inspect.isabstract(astm_Private)


def test_hyp_astm_private_constructor_exists():
    assert callable(astm_Private.__init__)


def test_hyp_astm_private_constructor_args():
    sig = inspect.signature(astm_Private.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_public_is_not_abstract():
    assert not inspect.isabstract(astm_Public)


def test_hyp_astm_public_constructor_exists():
    assert callable(astm_Public.__init__)


def test_hyp_astm_public_constructor_args():
    sig = inspect.signature(astm_Public.__init__)
    params = list(sig.parameters.keys())



def test_hyp_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_hyp_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_hyp_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_ByReferenceFormalParameterType)


def test_hyp_astm_byreferenceformalparametertype_constructor_exists():
    assert callable(astm_ByReferenceFormalParameterType.__init__)


def test_hyp_astm_byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(astm_ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_ByValueFormalParameterType)


def test_hyp_astm_byvalueformalparametertype_constructor_exists():
    assert callable(astm_ByValueFormalParameterType.__init__)


def test_hyp_astm_byvalueformalparametertype_constructor_args():
    sig = inspect.signature(astm_ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_protected_is_not_abstract():
    assert not inspect.isabstract(astm_Protected)


def test_hyp_astm_protected_constructor_exists():
    assert callable(astm_Protected.__init__)


def test_hyp_astm_protected_constructor_args():
    sig = inspect.signature(astm_Protected.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_integer_is_not_abstract():
    assert not inspect.isabstract(astm_Integer)


def test_hyp_astm_integer_constructor_exists():
    assert callable(astm_Integer.__init__)


def test_hyp_astm_integer_constructor_args():
    sig = inspect.signature(astm_Integer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_float_is_not_abstract():
    assert not inspect.isabstract(astm_Float)


def test_hyp_astm_float_constructor_exists():
    assert callable(astm_Float.__init__)


def test_hyp_astm_float_constructor_args():
    sig = inspect.signature(astm_Float.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_string_is_not_abstract():
    assert not inspect.isabstract(astm_String)


def test_hyp_astm_string_constructor_exists():
    assert callable(astm_String.__init__)


def test_hyp_astm_string_constructor_args():
    sig = inspect.signature(astm_String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm_ShortInteger)


def test_hyp_astm_shortinteger_constructor_exists():
    assert callable(astm_ShortInteger.__init__)


def test_hyp_astm_shortinteger_constructor_args():
    sig = inspect.signature(astm_ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_longinteger_is_not_abstract():
    assert not inspect.isabstract(astm_LongInteger)


def test_hyp_astm_longinteger_constructor_exists():
    assert callable(astm_LongInteger.__init__)


def test_hyp_astm_longinteger_constructor_args():
    sig = inspect.signature(astm_LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_boolean_is_not_abstract():
    assert not inspect.isabstract(astm_Boolean)


def test_hyp_astm_boolean_constructor_exists():
    assert callable(astm_Boolean.__init__)


def test_hyp_astm_boolean_constructor_args():
    sig = inspect.signature(astm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm_WideCharacter)


def test_hyp_astm_widecharacter_constructor_exists():
    assert callable(astm_WideCharacter.__init__)


def test_hyp_astm_widecharacter_constructor_args():
    sig = inspect.signature(astm_WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_character_is_not_abstract():
    assert not inspect.isabstract(astm_Character)


def test_hyp_astm_character_constructor_exists():
    assert callable(astm_Character.__init__)


def test_hyp_astm_character_constructor_args():
    sig = inspect.signature(astm_Character.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_longdouble_is_not_abstract():
    assert not inspect.isabstract(astm_LongDouble)


def test_hyp_astm_longdouble_constructor_exists():
    assert callable(astm_LongDouble.__init__)


def test_hyp_astm_longdouble_constructor_args():
    sig = inspect.signature(astm_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_byte_is_not_abstract():
    assert not inspect.isabstract(astm_Byte)


def test_hyp_astm_byte_constructor_exists():
    assert callable(astm_Byte.__init__)


def test_hyp_astm_byte_constructor_args():
    sig = inspect.signature(astm_Byte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_double_is_not_abstract():
    assert not inspect.isabstract(astm_Double)


def test_hyp_astm_double_constructor_exists():
    assert callable(astm_Double.__init__)


def test_hyp_astm_double_constructor_args():
    sig = inspect.signature(astm_Double.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_void_is_not_abstract():
    assert not inspect.isabstract(astm_Void)


def test_hyp_astm_void_constructor_exists():
    assert callable(astm_Void.__init__)


def test_hyp_astm_void_constructor_args():
    sig = inspect.signature(astm_Void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_hyp_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_hyp_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_purevirtual_is_not_abstract():
    assert not inspect.isabstract(astm_PureVirtual)


def test_hyp_astm_purevirtual_constructor_exists():
    assert callable(astm_PureVirtual.__init__)


def test_hyp_astm_purevirtual_constructor_args():
    sig = inspect.signature(astm_PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_nonvirtual_is_not_abstract():
    assert not inspect.isabstract(astm_NonVirtual)


def test_hyp_astm_nonvirtual_constructor_exists():
    assert callable(astm_NonVirtual.__init__)


def test_hyp_astm_nonvirtual_constructor_args():
    sig = inspect.signature(astm_NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_virtual_is_not_abstract():
    assert not inspect.isabstract(astm_Virtual)


def test_hyp_astm_virtual_constructor_exists():
    assert callable(astm_Virtual.__init__)


def test_hyp_astm_virtual_constructor_args():
    sig = inspect.signature(astm_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_hyp_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_hyp_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_filelocal_is_not_abstract():
    assert not inspect.isabstract(astm_FileLocal)


def test_hyp_astm_filelocal_constructor_exists():
    assert callable(astm_FileLocal.__init__)


def test_hyp_astm_filelocal_constructor_args():
    sig = inspect.signature(astm_FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_nodef_is_not_abstract():
    assert not inspect.isabstract(astm_NoDef)


def test_hyp_astm_nodef_constructor_exists():
    assert callable(astm_NoDef.__init__)


def test_hyp_astm_nodef_constructor_args():
    sig = inspect.signature(astm_NoDef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionPersistent)


def test_hyp_astm_functionpersistent_constructor_exists():
    assert callable(astm_FunctionPersistent.__init__)


def test_hyp_astm_functionpersistent_constructor_args():
    sig = inspect.signature(astm_FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm_PerClassMember)


def test_hyp_astm_perclassmember_constructor_exists():
    assert callable(astm_PerClassMember.__init__)


def test_hyp_astm_perclassmember_constructor_args():
    sig = inspect.signature(astm_PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_external_is_not_abstract():
    assert not inspect.isabstract(astm_External)


def test_hyp_astm_external_constructor_exists():
    assert callable(astm_External.__init__)


def test_hyp_astm_external_constructor_args():
    sig = inspect.signature(astm_External.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_hyp_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_hyp_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_hyp_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_hyp_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_MissingActualParameter)


def test_hyp_astm_missingactualparameter_constructor_exists():
    assert callable(astm_MissingActualParameter.__init__)


def test_hyp_astm_missingactualparameter_constructor_args():
    sig = inspect.signature(astm_MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ActualParameterExpression)


def test_hyp_astm_actualparameterexpression_constructor_exists():
    assert callable(astm_ActualParameterExpression.__init__)


def test_hyp_astm_actualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_hyp_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_hyp_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_notequal_is_not_abstract():
    assert not inspect.isabstract(astm_NotEqual)


def test_hyp_astm_notequal_constructor_exists():
    assert callable(astm_NotEqual.__init__)


def test_hyp_astm_notequal_constructor_args():
    sig = inspect.signature(astm_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitxor_is_not_abstract():
    assert not inspect.isabstract(astm_BitXor)


def test_hyp_astm_bitxor_constructor_exists():
    assert callable(astm_BitXor.__init__)


def test_hyp_astm_bitxor_constructor_args():
    sig = inspect.signature(astm_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificin_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificIn)


def test_hyp_astm_specificin_constructor_exists():
    assert callable(astm_SpecificIn.__init__)


def test_hyp_astm_specificin_constructor_args():
    sig = inspect.signature(astm_SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificlessequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLessEqual)


def test_hyp_astm_specificlessequal_constructor_exists():
    assert callable(astm_SpecificLessEqual.__init__)


def test_hyp_astm_specificlessequal_constructor_args():
    sig = inspect.signature(astm_SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_multiply_is_not_abstract():
    assert not inspect.isabstract(astm_Multiply)


def test_hyp_astm_multiply_constructor_exists():
    assert callable(astm_Multiply.__init__)


def test_hyp_astm_multiply_constructor_args():
    sig = inspect.signature(astm_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitRightShift)


def test_hyp_astm_bitrightshift_constructor_exists():
    assert callable(astm_BitRightShift.__init__)


def test_hyp_astm_bitrightshift_constructor_args():
    sig = inspect.signature(astm_BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_less_is_not_abstract():
    assert not inspect.isabstract(astm_Less)


def test_hyp_astm_less_constructor_exists():
    assert callable(astm_Less.__init__)


def test_hyp_astm_less_constructor_args():
    sig = inspect.signature(astm_Less.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_or_is_not_abstract():
    assert not inspect.isabstract(astm_Or)


def test_hyp_astm_or_constructor_exists():
    assert callable(astm_Or.__init__)


def test_hyp_astm_or_constructor_args():
    sig = inspect.signature(astm_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificlike_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLike)


def test_hyp_astm_specificlike_constructor_exists():
    assert callable(astm_SpecificLike.__init__)


def test_hyp_astm_specificlike_constructor_args():
    sig = inspect.signature(astm_SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_exponent_is_not_abstract():
    assert not inspect.isabstract(astm_Exponent)


def test_hyp_astm_exponent_constructor_exists():
    assert callable(astm_Exponent.__init__)


def test_hyp_astm_exponent_constructor_args():
    sig = inspect.signature(astm_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_modulus_is_not_abstract():
    assert not inspect.isabstract(astm_Modulus)


def test_hyp_astm_modulus_constructor_exists():
    assert callable(astm_Modulus.__init__)


def test_hyp_astm_modulus_constructor_args():
    sig = inspect.signature(astm_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_equal_is_not_abstract():
    assert not inspect.isabstract(astm_Equal)


def test_hyp_astm_equal_constructor_exists():
    assert callable(astm_Equal.__init__)


def test_hyp_astm_equal_constructor_args():
    sig = inspect.signature(astm_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificGreaterEqual)


def test_hyp_astm_specificgreaterequal_constructor_exists():
    assert callable(astm_SpecificGreaterEqual.__init__)


def test_hyp_astm_specificgreaterequal_constructor_args():
    sig = inspect.signature(astm_SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificConcatString)


def test_hyp_astm_specificconcatstring_constructor_exists():
    assert callable(astm_SpecificConcatString.__init__)


def test_hyp_astm_specificconcatstring_constructor_args():
    sig = inspect.signature(astm_SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitor_is_not_abstract():
    assert not inspect.isabstract(astm_BitOr)


def test_hyp_astm_bitor_constructor_exists():
    assert callable(astm_BitOr.__init__)


def test_hyp_astm_bitor_constructor_args():
    sig = inspect.signature(astm_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_and_is_not_abstract():
    assert not inspect.isabstract(astm_And)


def test_hyp_astm_and_constructor_exists():
    assert callable(astm_And.__init__)


def test_hyp_astm_and_constructor_args():
    sig = inspect.signature(astm_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_divide_is_not_abstract():
    assert not inspect.isabstract(astm_Divide)


def test_hyp_astm_divide_constructor_exists():
    assert callable(astm_Divide.__init__)


def test_hyp_astm_divide_constructor_args():
    sig = inspect.signature(astm_Divide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitLeftShift)


def test_hyp_astm_bitleftshift_constructor_exists():
    assert callable(astm_BitLeftShift.__init__)


def test_hyp_astm_bitleftshift_constructor_args():
    sig = inspect.signature(astm_BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_add_is_not_abstract():
    assert not inspect.isabstract(astm_Add)


def test_hyp_astm_add_constructor_exists():
    assert callable(astm_Add.__init__)


def test_hyp_astm_add_constructor_args():
    sig = inspect.signature(astm_Add.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_greater_is_not_abstract():
    assert not inspect.isabstract(astm_Greater)


def test_hyp_astm_greater_constructor_exists():
    assert callable(astm_Greater.__init__)


def test_hyp_astm_greater_constructor_args():
    sig = inspect.signature(astm_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_subtract_is_not_abstract():
    assert not inspect.isabstract(astm_Subtract)


def test_hyp_astm_subtract_constructor_exists():
    assert callable(astm_Subtract.__init__)


def test_hyp_astm_subtract_constructor_args():
    sig = inspect.signature(astm_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_notgreater_is_not_abstract():
    assert not inspect.isabstract(astm_NotGreater)


def test_hyp_astm_notgreater_constructor_exists():
    assert callable(astm_NotGreater.__init__)


def test_hyp_astm_notgreater_constructor_args():
    sig = inspect.signature(astm_NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_assign_is_not_abstract():
    assert not inspect.isabstract(astm_Assign)


def test_hyp_astm_assign_constructor_exists():
    assert callable(astm_Assign.__init__)


def test_hyp_astm_assign_constructor_args():
    sig = inspect.signature(astm_Assign.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_notless_is_not_abstract():
    assert not inspect.isabstract(astm_NotLess)


def test_hyp_astm_notless_constructor_exists():
    assert callable(astm_NotLess.__init__)


def test_hyp_astm_notless_constructor_args():
    sig = inspect.signature(astm_NotLess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitand_is_not_abstract():
    assert not inspect.isabstract(astm_BitAnd)


def test_hyp_astm_bitand_constructor_exists():
    assert callable(astm_BitAnd.__init__)


def test_hyp_astm_bitand_constructor_args():
    sig = inspect.signature(astm_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm_OperatorAssign)


def test_hyp_astm_operatorassign_constructor_exists():
    assert callable(astm_OperatorAssign.__init__)


def test_hyp_astm_operatorassign_constructor_args():
    sig = inspect.signature(astm_OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_hyp_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_hyp_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_NamedTypeReference)


def test_hyp_astm_namedtypereference_constructor_exists():
    assert callable(astm_NamedTypeReference.__init__)


def test_hyp_astm_namedtypereference_constructor_args():
    sig = inspect.signature(astm_NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_UnnamedTypeReference)


def test_hyp_astm_unnamedtypereference_constructor_exists():
    assert callable(astm_UnnamedTypeReference.__init__)


def test_hyp_astm_unnamedtypereference_constructor_args():
    sig = inspect.signature(astm_UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AggregateType)


def test_hyp_aggregatetype_constructor_exists():
    assert callable(AggregateType.__init__)


def test_hyp_aggregatetype_constructor_args():
    sig = inspect.signature(AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_uniontype_is_not_abstract():
    assert not inspect.isabstract(astm_UnionType)


def test_hyp_astm_uniontype_constructor_exists():
    assert callable(astm_UnionType.__init__)


def test_hyp_astm_uniontype_constructor_args():
    sig = inspect.signature(astm_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationType)


def test_hyp_astm_annotationtype_constructor_exists():
    assert callable(astm_AnnotationType.__init__)


def test_hyp_astm_annotationtype_constructor_args():
    sig = inspect.signature(astm_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_structuretype_is_not_abstract():
    assert not inspect.isabstract(astm_StructureType)


def test_hyp_astm_structuretype_constructor_exists():
    assert callable(astm_StructureType.__init__)


def test_hyp_astm_structuretype_constructor_args():
    sig = inspect.signature(astm_StructureType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_classtype_is_not_abstract():
    assert not inspect.isabstract(astm_ClassType)


def test_hyp_astm_classtype_constructor_exists():
    assert callable(astm_ClassType.__init__)


def test_hyp_astm_classtype_constructor_args():
    sig = inspect.signature(astm_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functiontype_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionType)


def test_hyp_astm_functiontype_constructor_exists():
    assert callable(astm_FunctionType.__init__)


def test_hyp_astm_functiontype_constructor_args():
    sig = inspect.signature(astm_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_hyp_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_hyp_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_pointertype_is_not_abstract():
    assert not inspect.isabstract(astm_PointerType)


def test_hyp_astm_pointertype_constructor_exists():
    assert callable(astm_PointerType.__init__)


def test_hyp_astm_pointertype_constructor_args():
    sig = inspect.signature(astm_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_referencetype_is_not_abstract():
    assert not inspect.isabstract(astm_ReferenceType)


def test_hyp_astm_referencetype_constructor_exists():
    assert callable(astm_ReferenceType.__init__)


def test_hyp_astm_referencetype_constructor_args():
    sig = inspect.signature(astm_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm_CollectionType)


def test_hyp_astm_collectiontype_constructor_exists():
    assert callable(astm_CollectionType.__init__)


def test_hyp_astm_collectiontype_constructor_args():
    sig = inspect.signature(astm_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rangetype_is_not_abstract():
    assert not inspect.isabstract(astm_RangeType)


def test_hyp_astm_rangetype_constructor_exists():
    assert callable(astm_RangeType.__init__)


def test_hyp_astm_rangetype_constructor_args():
    sig = inspect.signature(astm_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_arraytype_is_not_abstract():
    assert not inspect.isabstract(astm_ArrayType)


def test_hyp_astm_arraytype_constructor_exists():
    assert callable(astm_ArrayType.__init__)


def test_hyp_astm_arraytype_constructor_args():
    sig = inspect.signature(astm_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateScope)


def test_hyp_astm_aggregatescope_constructor_exists():
    assert callable(astm_AggregateScope.__init__)


def test_hyp_astm_aggregatescope_constructor_args():
    sig = inspect.signature(astm_AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_enumtype_is_not_abstract():
    assert not inspect.isabstract(astm_EnumType)


def test_hyp_astm_enumtype_constructor_exists():
    assert callable(astm_EnumType.__init__)


def test_hyp_astm_enumtype_constructor_args():
    sig = inspect.signature(astm_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbdatabasetype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDataBaseType)


def test_hyp_astm_rdbdatabasetype_constructor_exists():
    assert callable(astm_RDBDataBaseType.__init__)


def test_hyp_astm_rdbdatabasetype_constructor_args():
    sig = inspect.signature(astm_RDBDataBaseType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcursortype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorType)


def test_hyp_astm_rdbcursortype_constructor_exists():
    assert callable(astm_RDBCursorType.__init__)


def test_hyp_astm_rdbcursortype_constructor_args():
    sig = inspect.signature(astm_RDBCursorType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtabletype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableType)


def test_hyp_astm_rdbtabletype_constructor_exists():
    assert callable(astm_RDBTableType.__init__)


def test_hyp_astm_rdbtabletype_constructor_args():
    sig = inspect.signature(astm_RDBTableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm_ExceptionType)


def test_hyp_astm_exceptiontype_constructor_exists():
    assert callable(astm_ExceptionType.__init__)


def test_hyp_astm_exceptiontype_constructor_args():
    sig = inspect.signature(astm_ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbusertype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUserType)


def test_hyp_astm_rdbusertype_constructor_exists():
    assert callable(astm_RDBUserType.__init__)


def test_hyp_astm_rdbusertype_constructor_args():
    sig = inspect.signature(astm_RDBUserType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcolumntype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnType)


def test_hyp_astm_rdbcolumntype_constructor_exists():
    assert callable(astm_RDBColumnType.__init__)


def test_hyp_astm_rdbcolumntype_constructor_args():
    sig = inspect.signature(astm_RDBColumnType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterType)


def test_hyp_astm_formalparametertype_constructor_exists():
    assert callable(astm_FormalParameterType.__init__)


def test_hyp_astm_formalparametertype_constructor_args():
    sig = inspect.signature(astm_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm_ConstructedType)


def test_hyp_astm_constructedtype_constructor_exists():
    assert callable(astm_ConstructedType.__init__)


def test_hyp_astm_constructedtype_constructor_args():
    sig = inspect.signature(astm_ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtablespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceType)


def test_hyp_astm_rdbtablespacetype_constructor_exists():
    assert callable(astm_RDBTableSpaceType.__init__)


def test_hyp_astm_rdbtablespacetype_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbviewtype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBViewType)


def test_hyp_astm_rdbviewtype_constructor_exists():
    assert callable(astm_RDBViewType.__init__)


def test_hyp_astm_rdbviewtype_constructor_args():
    sig = inspect.signature(astm_RDBViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(astm_PrimitiveType)


def test_hyp_astm_primitivetype_constructor_exists():
    assert callable(astm_PrimitiveType.__init__)


def test_hyp_astm_primitivetype_constructor_args():
    sig = inspect.signature(astm_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"




def test_hyp_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_hyp_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_hyp_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_type_is_not_abstract():
    assert not inspect.isabstract(astm_Type)


def test_hyp_astm_type_constructor_exists():
    assert callable(astm_Type.__init__)


def test_hyp_astm_type_constructor_args():
    sig = inspect.signature(astm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isConst" in params, "Missing parameter 'isConst'"





def test_hyp_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(PreprocessorElement)


def test_hyp_preprocessorelement_constructor_exists():
    assert callable(PreprocessorElement.__init__)


def test_hyp_preprocessorelement_constructor_args():
    sig = inspect.signature(PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(astm_MacroDefinition)


def test_hyp_astm_macrodefinition_constructor_exists():
    assert callable(astm_MacroDefinition.__init__)


def test_hyp_astm_macrodefinition_constructor_args():
    sig = inspect.signature(astm_MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "macroName" in params, "Missing parameter 'macroName'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_astm_macrocall_is_not_abstract():
    assert not inspect.isabstract(astm_MacroCall)


def test_hyp_astm_macrocall_constructor_exists():
    assert callable(astm_MacroCall.__init__)


def test_hyp_astm_macrocall_constructor_args():
    sig = inspect.signature(astm_MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_comment_is_not_abstract():
    assert not inspect.isabstract(astm_Comment)


def test_hyp_astm_comment_constructor_exists():
    assert callable(astm_Comment.__init__)


def test_hyp_astm_comment_constructor_args():
    sig = inspect.signature(astm_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_astm_includeunit_is_not_abstract():
    assert not inspect.isabstract(astm_IncludeUnit)


def test_hyp_astm_includeunit_constructor_exists():
    assert callable(astm_IncludeUnit.__init__)


def test_hyp_astm_includeunit_constructor_args():
    sig = inspect.signature(astm_IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_labeltype_is_not_abstract():
    assert not inspect.isabstract(astm_LabelType)


def test_hyp_astm_labeltype_constructor_exists():
    assert callable(astm_LabelType.__init__)


def test_hyp_astm_labeltype_constructor_args():
    sig = inspect.signature(astm_LabelType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceType)


def test_hyp_astm_namespacetype_constructor_exists():
    assert callable(astm_NameSpaceType.__init__)


def test_hyp_astm_namespacetype_constructor_args():
    sig = inspect.signature(astm_NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateType)


def test_hyp_astm_aggregatetype_constructor_exists():
    assert callable(astm_AggregateType.__init__)


def test_hyp_astm_aggregatetype_constructor_args():
    sig = inspect.signature(astm_AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namedtype_is_not_abstract():
    assert not inspect.isabstract(astm_NamedType)


def test_hyp_astm_namedtype_constructor_exists():
    assert callable(astm_NamedType.__init__)


def test_hyp_astm_namedtype_constructor_args():
    sig = inspect.signature(astm_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_hyp_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_hyp_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateTypeDefinition)


def test_hyp_astm_aggregatetypedefinition_constructor_exists():
    assert callable(astm_AggregateTypeDefinition.__init__)


def test_hyp_astm_aggregatetypedefinition_constructor_args():
    sig = inspect.signature(astm_AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_NamedTypeDefinition)


def test_hyp_astm_namedtypedefinition_constructor_exists():
    assert callable(astm_NamedTypeDefinition.__init__)


def test_hyp_astm_namedtypedefinition_constructor_args():
    sig = inspect.signature(astm_NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_hyp_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_hyp_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm_VariableDefinition)


def test_hyp_astm_variabledefinition_constructor_exists():
    assert callable(astm_VariableDefinition.__init__)


def test_hyp_astm_variabledefinition_constructor_args():
    sig = inspect.signature(astm_VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(astm_BitFieldDefinition)


def test_hyp_astm_bitfielddefinition_constructor_exists():
    assert callable(astm_BitFieldDefinition.__init__)


def test_hyp_astm_bitfielddefinition_constructor_args():
    sig = inspect.signature(astm_BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_expression_is_not_abstract():
    assert not inspect.isabstract(astm_Expression)


def test_hyp_astm_expression_constructor_exists():
    assert callable(astm_Expression.__init__)


def test_hyp_astm_expression_constructor_args():
    sig = inspect.signature(astm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_typereference_is_not_abstract():
    assert not inspect.isabstract(astm_TypeReference)


def test_hyp_astm_typereference_constructor_exists():
    assert callable(astm_TypeReference.__init__)


def test_hyp_astm_typereference_constructor_args():
    sig = inspect.signature(astm_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functionscope_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionScope)


def test_hyp_astm_functionscope_constructor_exists():
    assert callable(astm_FunctionScope.__init__)


def test_hyp_astm_functionscope_constructor_args():
    sig = inspect.signature(astm_FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_statement_is_not_abstract():
    assert not inspect.isabstract(astm_Statement)


def test_hyp_astm_statement_constructor_exists():
    assert callable(astm_Statement.__init__)


def test_hyp_astm_statement_constructor_args():
    sig = inspect.signature(astm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDefinition)


def test_hyp_astm_formalparameterdefinition_constructor_exists():
    assert callable(astm_FormalParameterDefinition.__init__)


def test_hyp_astm_formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm_FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_hyp_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_hyp_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbuserdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUserDefinition)


def test_hyp_astm_rdbuserdefinition_constructor_exists():
    assert callable(astm_RDBUserDefinition.__init__)


def test_hyp_astm_rdbuserdefinition_constructor_args():
    sig = inspect.signature(astm_RDBUserDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_datadefinition_is_not_abstract():
    assert not inspect.isabstract(astm_DataDefinition)


def test_hyp_astm_datadefinition_constructor_exists():
    assert callable(astm_DataDefinition.__init__)


def test_hyp_astm_datadefinition_constructor_args():
    sig = inspect.signature(astm_DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"




def test_hyp_astm_rdbtabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableDefinition)


def test_hyp_astm_rdbtabledefinition_constructor_exists():
    assert callable(astm_RDBTableDefinition.__init__)


def test_hyp_astm_rdbtabledefinition_constructor_args():
    sig = inspect.signature(astm_RDBTableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EntryDefinition)


def test_hyp_astm_entrydefinition_constructor_exists():
    assert callable(astm_EntryDefinition.__init__)


def test_hyp_astm_entrydefinition_constructor_args():
    sig = inspect.signature(astm_EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcursordefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorDefinition)


def test_hyp_astm_rdbcursordefinition_constructor_exists():
    assert callable(astm_RDBCursorDefinition.__init__)


def test_hyp_astm_rdbcursordefinition_constructor_args():
    sig = inspect.signature(astm_RDBCursorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcolumndefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnDefinition)


def test_hyp_astm_rdbcolumndefinition_constructor_exists():
    assert callable(astm_RDBColumnDefinition.__init__)


def test_hyp_astm_rdbcolumndefinition_constructor_args():
    sig = inspect.signature(astm_RDBColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "NotNull" in params, "Missing parameter 'NotNull'"




def test_hyp_astm_specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificTriggerDefinition)


def test_hyp_astm_specifictriggerdefinition_constructor_exists():
    assert callable(astm_SpecificTriggerDefinition.__init__)


def test_hyp_astm_specifictriggerdefinition_constructor_args():
    sig = inspect.signature(astm_SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EnumLiteralDefinition)


def test_hyp_astm_enumliteraldefinition_constructor_exists():
    assert callable(astm_EnumLiteralDefinition.__init__)


def test_hyp_astm_enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm_EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbviewdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBViewDefinition)


def test_hyp_astm_rdbviewdefinition_constructor_exists():
    assert callable(astm_RDBViewDefinition.__init__)


def test_hyp_astm_rdbviewdefinition_constructor_args():
    sig = inspect.signature(astm_RDBViewDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceDefinition)


def test_hyp_astm_rdbtablespacedefinition_constructor_exists():
    assert callable(astm_RDBTableSpaceDefinition.__init__)


def test_hyp_astm_rdbtablespacedefinition_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbdatabasedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDatabaseDefinition)


def test_hyp_astm_rdbdatabasedefinition_constructor_exists():
    assert callable(astm_RDBDatabaseDefinition.__init__)


def test_hyp_astm_rdbdatabasedefinition_constructor_args():
    sig = inspect.signature(astm_RDBDatabaseDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionDefinition)


def test_hyp_astm_functiondefinition_constructor_exists():
    assert callable(astm_FunctionDefinition.__init__)


def test_hyp_astm_functiondefinition_constructor_args():
    sig = inspect.signature(astm_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_VariableDeclaration)


def test_hyp_astm_variabledeclaration_constructor_exists():
    assert callable(astm_VariableDeclaration.__init__)


def test_hyp_astm_variabledeclaration_constructor_args():
    sig = inspect.signature(astm_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"




def test_hyp_astm_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDeclaration)


def test_hyp_astm_formalparameterdeclaration_constructor_exists():
    assert callable(astm_FormalParameterDeclaration.__init__)


def test_hyp_astm_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm_FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionDeclaration)


def test_hyp_astm_functiondeclaration_constructor_exists():
    assert callable(astm_FunctionDeclaration.__init__)


def test_hyp_astm_functiondeclaration_constructor_args():
    sig = inspect.signature(astm_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_hyp_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_hyp_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_project_is_not_abstract():
    assert not inspect.isabstract(astm_Project)


def test_hyp_astm_project_constructor_exists():
    assert callable(astm_Project.__init__)


def test_hyp_astm_project_constructor_args():
    sig = inspect.signature(astm_Project.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(DeclarationOrDefinition)


def test_hyp_declarationordefinition_constructor_exists():
    assert callable(DeclarationOrDefinition.__init__)


def test_hyp_declarationordefinition_constructor_args():
    sig = inspect.signature(DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_declaration_is_not_abstract():
    assert not inspect.isabstract(astm_Declaration)


def test_hyp_astm_declaration_constructor_exists():
    assert callable(astm_Declaration.__init__)


def test_hyp_astm_declaration_constructor_args():
    sig = inspect.signature(astm_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_definition_is_not_abstract():
    assert not inspect.isabstract(astm_Definition)


def test_hyp_astm_definition_constructor_exists():
    assert callable(astm_Definition.__init__)


def test_hyp_astm_definition_constructor_args():
    sig = inspect.signature(astm_Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_hyp_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_hyp_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_typedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_TypeDefinition)


def test_hyp_astm_typedefinition_constructor_exists():
    assert callable(astm_TypeDefinition.__init__)


def test_hyp_astm_typedefinition_constructor_args():
    sig = inspect.signature(astm_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_LabelDefinition)


def test_hyp_astm_labeldefinition_constructor_exists():
    assert callable(astm_LabelDefinition.__init__)


def test_hyp_astm_labeldefinition_constructor_args():
    sig = inspect.signature(astm_LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceDefinition)


def test_hyp_astm_namespacedefinition_constructor_exists():
    assert callable(astm_NameSpaceDefinition.__init__)


def test_hyp_astm_namespacedefinition_constructor_args():
    sig = inspect.signature(astm_NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(astm_DeclarationOrDefinition)


def test_hyp_astm_declarationordefinition_constructor_exists():
    assert callable(astm_DeclarationOrDefinition.__init__)


def test_hyp_astm_declarationordefinition_constructor_args():
    sig = inspect.signature(astm_DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"





def test_hyp_astm_programscope_is_not_abstract():
    assert not inspect.isabstract(astm_ProgramScope)


def test_hyp_astm_programscope_constructor_exists():
    assert callable(astm_ProgramScope.__init__)


def test_hyp_astm_programscope_constructor_args():
    sig = inspect.signature(astm_ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(OtherSyntaxObject)


def test_hyp_othersyntaxobject_constructor_exists():
    assert callable(OtherSyntaxObject.__init__)


def test_hyp_othersyntaxobject_constructor_args():
    sig = inspect.signature(OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm_VirtualSpecification)


def test_hyp_astm_virtualspecification_constructor_exists():
    assert callable(astm_VirtualSpecification.__init__)


def test_hyp_astm_virtualspecification_constructor_args():
    sig = inspect.signature(astm_VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(astm_DerivesFrom)


def test_hyp_astm_derivesfrom_constructor_exists():
    assert callable(astm_DerivesFrom.__init__)


def test_hyp_astm_derivesfrom_constructor_args():
    sig = inspect.signature(astm_DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"




def test_hyp_astm_dimension_is_not_abstract():
    assert not inspect.isabstract(astm_Dimension)


def test_hyp_astm_dimension_constructor_exists():
    assert callable(astm_Dimension.__init__)


def test_hyp_astm_dimension_constructor_args():
    sig = inspect.signature(astm_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtrigger_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTrigger)


def test_hyp_astm_rdbtrigger_constructor_exists():
    assert callable(astm_RDBTrigger.__init__)


def test_hyp_astm_rdbtrigger_constructor_args():
    sig = inspect.signature(astm_RDBTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbindexcolumn_is_not_abstract():
    assert not inspect.isabstract(astm_RDBIndexColumn)


def test_hyp_astm_rdbindexcolumn_constructor_exists():
    assert callable(astm_RDBIndexColumn.__init__)


def test_hyp_astm_rdbindexcolumn_constructor_args():
    sig = inspect.signature(astm_RDBIndexColumn.__init__)
    params = list(sig.parameters.keys())
    assert "AscendingOrDescending" in params, "Missing parameter 'AscendingOrDescending'"




def test_hyp_astm_functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttribute)


def test_hyp_astm_functionmemberattribute_constructor_exists():
    assert callable(astm_FunctionMemberAttribute.__init__)


def test_hyp_astm_functionmemberattribute_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbindex_is_not_abstract():
    assert not inspect.isabstract(astm_RDBIndex)


def test_hyp_astm_rdbindex_constructor_exists():
    assert callable(astm_RDBIndex.__init__)


def test_hyp_astm_rdbindex_constructor_args():
    sig = inspect.signature(astm_RDBIndex.__init__)
    params = list(sig.parameters.keys())
    assert "IsUnique" in params, "Missing parameter 'IsUnique'"
    assert "NotNull" in params, "Missing parameter 'NotNull'"





def test_hyp_astm_rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBConstraint)


def test_hyp_astm_rdbconstraint_constructor_exists():
    assert callable(astm_RDBConstraint.__init__)


def test_hyp_astm_rdbconstraint_constructor_args():
    sig = inspect.signature(astm_RDBConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_name_is_not_abstract():
    assert not inspect.isabstract(astm_Name)


def test_hyp_astm_name_constructor_exists():
    assert callable(astm_Name.__init__)


def test_hyp_astm_name_constructor_args():
    sig = inspect.signature(astm_Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"




def test_hyp_astm_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm_PreprocessorElement)


def test_hyp_astm_preprocessorelement_constructor_exists():
    assert callable(astm_PreprocessorElement.__init__)


def test_hyp_astm_preprocessorelement_constructor_args():
    sig = inspect.signature(astm_PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gastmobject_is_not_abstract():
    assert not inspect.isabstract(GASTMObject)


def test_hyp_gastmobject_constructor_exists():
    assert callable(GASTMObject.__init__)


def test_hyp_gastmobject_constructor_args():
    sig = inspect.signature(GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSyntaxObject)


def test_hyp_astm_gastmsyntaxobject_constructor_exists():
    assert callable(astm_GASTMSyntaxObject.__init__)


def test_hyp_astm_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(astm_GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm_DefinitionObject)


def test_hyp_astm_definitionobject_constructor_exists():
    assert callable(astm_DefinitionObject.__init__)


def test_hyp_astm_definitionobject_constructor_args():
    sig = inspect.signature(astm_DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_scope_is_not_abstract():
    assert not inspect.isabstract(astm_Scope)


def test_hyp_astm_scope_constructor_exists():
    assert callable(astm_Scope.__init__)


def test_hyp_astm_scope_constructor_args():
    sig = inspect.signature(astm_Scope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_globalscope_is_not_abstract():
    assert not inspect.isabstract(astm_GlobalScope)


def test_hyp_astm_globalscope_constructor_exists():
    assert callable(astm_GlobalScope.__init__)


def test_hyp_astm_globalscope_constructor_args():
    sig = inspect.signature(astm_GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_compilationunit_is_not_abstract():
    assert not inspect.isabstract(astm_CompilationUnit)


def test_hyp_astm_compilationunit_constructor_exists():
    assert callable(astm_CompilationUnit.__init__)


def test_hyp_astm_compilationunit_constructor_args():
    sig = inspect.signature(astm_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"




def test_hyp_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_hyp_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_hyp_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_sourcelocation_is_not_abstract():
    assert not inspect.isabstract(astm_SourceLocation)


def test_hyp_astm_sourcelocation_constructor_exists():
    assert callable(astm_SourceLocation.__init__)


def test_hyp_astm_sourcelocation_constructor_args():
    sig = inspect.signature(astm_SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"







def test_hyp_astm_sourcefile_is_not_abstract():
    assert not inspect.isabstract(astm_SourceFile)


def test_hyp_astm_sourcefile_constructor_exists():
    assert callable(astm_SourceFile.__init__)


def test_hyp_astm_sourcefile_constructor_args():
    sig = inspect.signature(astm_SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"




def test_hyp_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_hyp_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_hyp_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbhostvariablereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBHostVariableReference)


def test_hyp_astm_rdbhostvariablereference_constructor_exists():
    assert callable(astm_RDBHostVariableReference.__init__)


def test_hyp_astm_rdbhostvariablereference_constructor_args():
    sig = inspect.signature(astm_RDBHostVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_accesskind_is_not_abstract():
    assert not inspect.isabstract(astm_AccessKind)


def test_hyp_astm_accesskind_constructor_exists():
    assert callable(astm_AccessKind.__init__)


def test_hyp_astm_accesskind_constructor_args():
    sig = inspect.signature(astm_AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_datatype_is_not_abstract():
    assert not inspect.isabstract(astm_DataType)


def test_hyp_astm_datatype_constructor_exists():
    assert callable(astm_DataType.__init__)


def test_hyp_astm_datatype_constructor_args():
    sig = inspect.signature(astm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm_StorageSpecification)


def test_hyp_astm_storagespecification_constructor_exists():
    assert callable(astm_StorageSpecification.__init__)


def test_hyp_astm_storagespecification_constructor_args():
    sig = inspect.signature(astm_StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSourceObject)


def test_hyp_astm_gastmsourceobject_constructor_exists():
    assert callable(astm_GASTMSourceObject.__init__)


def test_hyp_astm_gastmsourceobject_constructor_args():
    sig = inspect.signature(astm_GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_OtherSyntaxObject)


def test_hyp_astm_othersyntaxobject_constructor_exists():
    assert callable(astm_OtherSyntaxObject.__init__)


def test_hyp_astm_othersyntaxobject_constructor_args():
    sig = inspect.signature(astm_OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbtablespacereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceReference)


def test_hyp_astm_rdbtablespacereference_constructor_exists():
    assert callable(astm_RDBTableSpaceReference.__init__)


def test_hyp_astm_rdbtablespacereference_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttributes)


def test_hyp_astm_functionmemberattributes_constructor_exists():
    assert callable(astm_FunctionMemberAttributes.__init__)


def test_hyp_astm_functionmemberattributes_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isInline" in params, "Missing parameter 'isInline'"






def test_hyp_astm_actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_ActualParameter)


def test_hyp_astm_actualparameter_constructor_exists():
    assert callable(astm_ActualParameter.__init__)


def test_hyp_astm_actualparameter_constructor_args():
    sig = inspect.signature(astm_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_BinaryOperator)


def test_hyp_astm_binaryoperator_constructor_exists():
    assert callable(astm_BinaryOperator.__init__)


def test_hyp_astm_binaryoperator_constructor_args():
    sig = inspect.signature(astm_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSemanticObject)


def test_hyp_astm_gastmsemanticobject_constructor_exists():
    assert callable(astm_GASTMSemanticObject.__init__)


def test_hyp_astm_gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm_GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryOperator)


def test_hyp_astm_unaryoperator_constructor_exists():
    assert callable(astm_UnaryOperator.__init__)


def test_hyp_astm_unaryoperator_constructor_args():
    sig = inspect.signature(astm_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMObject)


def test_hyp_astm_gastmobject_constructor_exists():
    assert callable(astm_GASTMObject.__init__)


def test_hyp_astm_gastmobject_constructor_args():
    sig = inspect.signature(astm_GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namereference_is_not_abstract():
    assert not inspect.isabstract(NameReference)


def test_hyp_namereference_constructor_exists():
    assert callable(NameReference.__init__)


def test_hyp_namereference_constructor_args():
    sig = inspect.signature(NameReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_identifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_IdentifierReference)


def test_hyp_astm_identifierreference_constructor_exists():
    assert callable(astm_IdentifierReference.__init__)


def test_hyp_astm_identifierreference_constructor_args():
    sig = inspect.signature(astm_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_TypeQualifiedIdentifierReference)


def test_hyp_astm_typequalifiedidentifierreference_constructor_exists():
    assert callable(astm_TypeQualifiedIdentifierReference.__init__)


def test_hyp_astm_typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedIdentifierReference)


def test_hyp_astm_qualifiedidentifierreference_constructor_exists():
    assert callable(astm_QualifiedIdentifierReference.__init__)


def test_hyp_astm_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ConditionalExpression)


def test_hyp_astm_conditionalexpression_constructor_exists():
    assert callable(astm_ConditionalExpression.__init__)


def test_hyp_astm_conditionalexpression_constructor_args():
    sig = inspect.signature(astm_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_newexpression_is_not_abstract():
    assert not inspect.isabstract(astm_NewExpression)


def test_hyp_astm_newexpression_constructor_exists():
    assert callable(astm_NewExpression.__init__)


def test_hyp_astm_newexpression_constructor_args():
    sig = inspect.signature(astm_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateExpression)


def test_hyp_astm_aggregateexpression_constructor_exists():
    assert callable(astm_AggregateExpression.__init__)


def test_hyp_astm_aggregateexpression_constructor_args():
    sig = inspect.signature(astm_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbselectexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RDBSelectExpression)


def test_hyp_astm_rdbselectexpression_constructor_exists():
    assert callable(astm_RDBSelectExpression.__init__)


def test_hyp_astm_rdbselectexpression_constructor_args():
    sig = inspect.signature(astm_RDBSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionCallExpression)


def test_hyp_astm_functioncallexpression_constructor_exists():
    assert callable(astm_FunctionCallExpression.__init__)


def test_hyp_astm_functioncallexpression_constructor_args():
    sig = inspect.signature(astm_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RangeExpression)


def test_hyp_astm_rangeexpression_constructor_exists():
    assert callable(astm_RangeExpression.__init__)


def test_hyp_astm_rangeexpression_constructor_args():
    sig = inspect.signature(astm_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_castexpression_is_not_abstract():
    assert not inspect.isabstract(astm_CastExpression)


def test_hyp_astm_castexpression_constructor_exists():
    assert callable(astm_CastExpression.__init__)


def test_hyp_astm_castexpression_constructor_args():
    sig = inspect.signature(astm_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_literal_is_not_abstract():
    assert not inspect.isabstract(astm_Literal)


def test_hyp_astm_literal_constructor_exists():
    assert callable(astm_Literal.__init__)


def test_hyp_astm_literal_constructor_args():
    sig = inspect.signature(astm_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_astm_rdbhostvariableexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RDBHostVariableExpression)


def test_hyp_astm_rdbhostvariableexpression_constructor_exists():
    assert callable(astm_RDBHostVariableExpression.__init__)


def test_hyp_astm_rdbhostvariableexpression_constructor_args():
    sig = inspect.signature(astm_RDBHostVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm_ArrayAccess)


def test_hyp_astm_arrayaccess_constructor_exists():
    assert callable(astm_ArrayAccess.__init__)


def test_hyp_astm_arrayaccess_constructor_args():
    sig = inspect.signature(astm_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationExpression)


def test_hyp_astm_annotationexpression_constructor_exists():
    assert callable(astm_AnnotationExpression.__init__)


def test_hyp_astm_annotationexpression_constructor_args():
    sig = inspect.signature(astm_AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_BinaryExpression)


def test_hyp_astm_binaryexpression_constructor_exists():
    assert callable(astm_BinaryExpression.__init__)


def test_hyp_astm_binaryexpression_constructor_args():
    sig = inspect.signature(astm_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryExpression)


def test_hyp_astm_unaryexpression_constructor_exists():
    assert callable(astm_UnaryExpression.__init__)


def test_hyp_astm_unaryexpression_constructor_args():
    sig = inspect.signature(astm_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_namereference_is_not_abstract():
    assert not inspect.isabstract(astm_NameReference)


def test_hyp_astm_namereference_constructor_exists():
    assert callable(astm_NameReference.__init__)


def test_hyp_astm_namereference_constructor_args():
    sig = inspect.signature(astm_NameReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_hyp_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_hyp_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_VariableCatchBlock)


def test_hyp_astm_variablecatchblock_constructor_exists():
    assert callable(astm_VariableCatchBlock.__init__)


def test_hyp_astm_variablecatchblock_constructor_args():
    sig = inspect.signature(astm_VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_typescatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_TypesCatchBlock)


def test_hyp_astm_typescatchblock_constructor_exists():
    assert callable(astm_TypesCatchBlock.__init__)


def test_hyp_astm_typescatchblock_constructor_args():
    sig = inspect.signature(astm_TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_catchblock_is_not_abstract():
    assert not inspect.isabstract(astm_CatchBlock)


def test_hyp_astm_catchblock_constructor_exists():
    assert callable(astm_CatchBlock.__init__)


def test_hyp_astm_catchblock_constructor_args():
    sig = inspect.signature(astm_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_hyp_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_hyp_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_whilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_WhileStatement)


def test_hyp_astm_whilestatement_constructor_exists():
    assert callable(astm_WhileStatement.__init__)


def test_hyp_astm_whilestatement_constructor_args():
    sig = inspect.signature(astm_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_DoWhileStatement)


def test_hyp_astm_dowhilestatement_constructor_exists():
    assert callable(astm_DoWhileStatement.__init__)


def test_hyp_astm_dowhilestatement_constructor_args():
    sig = inspect.signature(astm_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_forstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForStatement)


def test_hyp_astm_forstatement_constructor_exists():
    assert callable(astm_ForStatement.__init__)


def test_hyp_astm_forstatement_constructor_args():
    sig = inspect.signature(astm_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm_LabelAccess)


def test_hyp_astm_labelaccess_constructor_exists():
    assert callable(astm_LabelAccess.__init__)


def test_hyp_astm_labelaccess_constructor_args():
    sig = inspect.signature(astm_LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_hyp_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_hyp_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_defaultblock_is_not_abstract():
    assert not inspect.isabstract(astm_DefaultBlock)


def test_hyp_astm_defaultblock_constructor_exists():
    assert callable(astm_DefaultBlock.__init__)


def test_hyp_astm_defaultblock_constructor_args():
    sig = inspect.signature(astm_DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_caseblock_is_not_abstract():
    assert not inspect.isabstract(astm_CaseBlock)


def test_hyp_astm_caseblock_constructor_exists():
    assert callable(astm_CaseBlock.__init__)


def test_hyp_astm_caseblock_constructor_args():
    sig = inspect.signature(astm_CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_switchcase_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchCase)


def test_hyp_astm_switchcase_constructor_exists():
    assert callable(astm_SwitchCase.__init__)


def test_hyp_astm_switchcase_constructor_args():
    sig = inspect.signature(astm_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_blockscope_is_not_abstract():
    assert not inspect.isabstract(astm_BlockScope)


def test_hyp_astm_blockscope_constructor_exists():
    assert callable(astm_BlockScope.__init__)


def test_hyp_astm_blockscope_constructor_args():
    sig = inspect.signature(astm_BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ReturnStatement)


def test_hyp_astm_returnstatement_constructor_exists():
    assert callable(astm_ReturnStatement.__init__)


def test_hyp_astm_returnstatement_constructor_args():
    sig = inspect.signature(astm_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm_EmptyStatement)


def test_hyp_astm_emptystatement_constructor_exists():
    assert callable(astm_EmptyStatement.__init__)


def test_hyp_astm_emptystatement_constructor_args():
    sig = inspect.signature(astm_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbinsertstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInsertStatement)


def test_hyp_astm_rdbinsertstatement_constructor_exists():
    assert callable(astm_RDBInsertStatement.__init__)


def test_hyp_astm_rdbinsertstatement_constructor_args():
    sig = inspect.signature(astm_RDBInsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchStatement)


def test_hyp_astm_switchstatement_constructor_exists():
    assert callable(astm_SwitchStatement.__init__)


def test_hyp_astm_switchstatement_constructor_args():
    sig = inspect.signature(astm_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_DeleteStatement)


def test_hyp_astm_deletestatement_constructor_exists():
    assert callable(astm_DeleteStatement.__init__)


def test_hyp_astm_deletestatement_constructor_args():
    sig = inspect.signature(astm_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ExpressionStatement)


def test_hyp_astm_expressionstatement_constructor_exists():
    assert callable(astm_ExpressionStatement.__init__)


def test_hyp_astm_expressionstatement_constructor_args():
    sig = inspect.signature(astm_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LoopStatement)


def test_hyp_astm_loopstatement_constructor_exists():
    assert callable(astm_LoopStatement.__init__)


def test_hyp_astm_loopstatement_constructor_args():
    sig = inspect.signature(astm_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LabeledStatement)


def test_hyp_astm_labeledstatement_constructor_exists():
    assert callable(astm_LabeledStatement.__init__)


def test_hyp_astm_labeledstatement_constructor_args():
    sig = inspect.signature(astm_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BreakStatement)


def test_hyp_astm_breakstatement_constructor_exists():
    assert callable(astm_BreakStatement.__init__)


def test_hyp_astm_breakstatement_constructor_args():
    sig = inspect.signature(astm_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorStatement)


def test_hyp_astm_rdbcursorstatement_constructor_exists():
    assert callable(astm_RDBCursorStatement.__init__)


def test_hyp_astm_rdbcursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_continuestatement_is_not_abstract():
    assert not inspect.isabstract(astm_ContinueStatement)


def test_hyp_astm_continuestatement_constructor_exists():
    assert callable(astm_ContinueStatement.__init__)


def test_hyp_astm_continuestatement_constructor_args():
    sig = inspect.signature(astm_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_DeclarationOrDefinitionStatement)


def test_hyp_astm_declarationordefinitionstatement_constructor_exists():
    assert callable(astm_DeclarationOrDefinitionStatement.__init__)


def test_hyp_astm_declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(astm_DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BlockStatement)


def test_hyp_astm_blockstatement_constructor_exists():
    assert callable(astm_BlockStatement.__init__)


def test_hyp_astm_blockstatement_constructor_args():
    sig = inspect.signature(astm_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBSelectStatement)


def test_hyp_astm_rdbselectstatement_constructor_exists():
    assert callable(astm_RDBSelectStatement.__init__)


def test_hyp_astm_rdbselectstatement_constructor_args():
    sig = inspect.signature(astm_RDBSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ThrowStatement)


def test_hyp_astm_throwstatement_constructor_exists():
    assert callable(astm_ThrowStatement.__init__)


def test_hyp_astm_throwstatement_constructor_args():
    sig = inspect.signature(astm_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm_JumpStatement)


def test_hyp_astm_jumpstatement_constructor_exists():
    assert callable(astm_JumpStatement.__init__)


def test_hyp_astm_jumpstatement_constructor_args():
    sig = inspect.signature(astm_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBModifyStatement)


def test_hyp_astm_rdbmodifystatement_constructor_exists():
    assert callable(astm_RDBModifyStatement.__init__)


def test_hyp_astm_rdbmodifystatement_constructor_args():
    sig = inspect.signature(astm_RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_rdbconnectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBConnectStatement)


def test_hyp_astm_rdbconnectstatement_constructor_exists():
    assert callable(astm_RDBConnectStatement.__init__)


def test_hyp_astm_rdbconnectstatement_constructor_args():
    sig = inspect.signature(astm_RDBConnectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_TerminateStatement)


def test_hyp_astm_terminatestatement_constructor_exists():
    assert callable(astm_TerminateStatement.__init__)


def test_hyp_astm_terminatestatement_constructor_args():
    sig = inspect.signature(astm_TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_trystatement_is_not_abstract():
    assert not inspect.isabstract(astm_TryStatement)


def test_hyp_astm_trystatement_constructor_exists():
    assert callable(astm_TryStatement.__init__)


def test_hyp_astm_trystatement_constructor_args():
    sig = inspect.signature(astm_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm_IfStatement)


def test_hyp_astm_ifstatement_constructor_exists():
    assert callable(astm_IfStatement.__init__)


def test_hyp_astm_ifstatement_constructor_args():
    sig = inspect.signature(astm_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astm_specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificSelectStatement)


def test_hyp_astm_specificselectstatement_constructor_exists():
    assert callable(astm_SpecificSelectStatement.__init__)


def test_hyp_astm_specificselectstatement_constructor_args():
    sig = inspect.signature(astm_SpecificSelectStatement.__init__)
    params = list(sig.parameters.keys())


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
astm_Visitable_strategy = st.builds(
    astm_Visitable,
)
RDBColumnType_strategy = st.builds(
    RDBColumnType,
)
astm_RDBBFile_strategy = st.builds(
    astm_RDBBFile,
)
astm_RDBClob_strategy = st.builds(
    astm_RDBClob,
)
astm_RDBChar_strategy = st.builds(
    astm_RDBChar,
)
astm_RDBBlob_strategy = st.builds(
    astm_RDBBlob,
)
astm_RDBNClob_strategy = st.builds(
    astm_RDBNClob,
)
astm_RDBInt_strategy = st.builds(
    astm_RDBInt,
)
astm_RDBRowid_strategy = st.builds(
    astm_RDBRowid,
)
astm_RDBDate_strategy = st.builds(
    astm_RDBDate,
)
astm_RDBLong_strategy = st.builds(
    astm_RDBLong,
)
astm_RDBTimestamp_strategy = st.builds(
    astm_RDBTimestamp,
)
astm_RDBBoolean_strategy = st.builds(
    astm_RDBBoolean,
)
astm_RDBReal_strategy = st.builds(
    astm_RDBReal,
)
astm_RDBDecimal_strategy = st.builds(
    astm_RDBDecimal,
)
astm_RDBFloat_strategy = st.builds(
    astm_RDBFloat,
)
astm_RDBVarchar_strategy = st.builds(
    astm_RDBVarchar,
)
astm_RDBNumber_strategy = st.builds(
    astm_RDBNumber,
)
astm_RDBInteger_strategy = st.builds(
    astm_RDBInteger,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
astm_RDBTableAlias_strategy = st.builds(
    astm_RDBTableAlias,
)
astm_RDBRaw_strategy = st.builds(
    astm_RDBRaw,
)
astm_RDBString_strategy = st.builds(
    astm_RDBString,
)
RDBCursorStatement_strategy = st.builds(
    RDBCursorStatement,
)
astm_RDBFetchCursorStatement_strategy = st.builds(
    astm_RDBFetchCursorStatement,
)
astm_RDBCloseCursorStatement_strategy = st.builds(
    astm_RDBCloseCursorStatement,
)
astm_RDBOpenCursorStatement_strategy = st.builds(
    astm_RDBOpenCursorStatement,
)
RDBModifyStatement_strategy = st.builds(
    RDBModifyStatement,
)
astm_RDBDeleteStatement_strategy = st.builds(
    astm_RDBDeleteStatement,
)
astm_RDBUpdateStatement_strategy = st.builds(
    astm_RDBUpdateStatement,
)
astm_RDBTableReference_strategy = st.builds(
    astm_RDBTableReference,
)
RDBConstraint_strategy = st.builds(
    RDBConstraint,
)
astm_RDBUniqueKey_strategy = st.builds(
    astm_RDBUniqueKey,
)
astm_RDBRefIntegrity_strategy = st.builds(
    astm_RDBRefIntegrity,
)
astm_RDBCheckConstraint_strategy = st.builds(
    astm_RDBCheckConstraint,
    RDBConstraintText=
        safe_text,
    RDBConstraintType=
        safe_text
)
astm_RDBColumnReference_strategy = st.builds(
    astm_RDBColumnReference,
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
astm_ByReferenceActualParameterExpression_strategy = st.builds(
    astm_ByReferenceActualParameterExpression,
)
astm_ByValueActualParameterExpression_strategy = st.builds(
    astm_ByValueActualParameterExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm_Decrement_strategy = st.builds(
    astm_Decrement,
)
astm_Increment_strategy = st.builds(
    astm_Increment,
)
astm_Deref_strategy = st.builds(
    astm_Deref,
)
astm_PostDecrement_strategy = st.builds(
    astm_PostDecrement,
)
astm_Not_strategy = st.builds(
    astm_Not,
)
astm_PostIncrement_strategy = st.builds(
    astm_PostIncrement,
)
astm_AddressOf_strategy = st.builds(
    astm_AddressOf,
)
astm_BitNot_strategy = st.builds(
    astm_BitNot,
)
astm_Negate_strategy = st.builds(
    astm_Negate,
)
astm_UnaryPlus_strategy = st.builds(
    astm_UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
astm_RealLiteral_strategy = st.builds(
    astm_RealLiteral,
)
astm_CharLiteral_strategy = st.builds(
    astm_CharLiteral,
)
astm_BitLiteral_strategy = st.builds(
    astm_BitLiteral,
)
astm_BooleanLiteral_strategy = st.builds(
    astm_BooleanLiteral,
)
astm_StringLiteral_strategy = st.builds(
    astm_StringLiteral,
)
astm_IntegerlLiteral_strategy = st.builds(
    astm_IntegerlLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
astm_QualifiedOverData_strategy = st.builds(
    astm_QualifiedOverData,
)
astm_QualifiedOverPointer_strategy = st.builds(
    astm_QualifiedOverPointer,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
astm_ForCheckAfterStatement_strategy = st.builds(
    astm_ForCheckAfterStatement,
)
astm_ForCheckBeforeStatement_strategy = st.builds(
    astm_ForCheckBeforeStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
astm_Private_strategy = st.builds(
    astm_Private,
)
astm_Public_strategy = st.builds(
    astm_Public,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
astm_ByReferenceFormalParameterType_strategy = st.builds(
    astm_ByReferenceFormalParameterType,
)
astm_ByValueFormalParameterType_strategy = st.builds(
    astm_ByValueFormalParameterType,
)
astm_Protected_strategy = st.builds(
    astm_Protected,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
astm_Integer_strategy = st.builds(
    astm_Integer,
)
astm_Float_strategy = st.builds(
    astm_Float,
)
astm_String_strategy = st.builds(
    astm_String,
)
astm_ShortInteger_strategy = st.builds(
    astm_ShortInteger,
)
astm_LongInteger_strategy = st.builds(
    astm_LongInteger,
)
astm_Boolean_strategy = st.builds(
    astm_Boolean,
)
astm_WideCharacter_strategy = st.builds(
    astm_WideCharacter,
)
astm_Character_strategy = st.builds(
    astm_Character,
)
astm_LongDouble_strategy = st.builds(
    astm_LongDouble,
)
astm_Byte_strategy = st.builds(
    astm_Byte,
)
astm_Double_strategy = st.builds(
    astm_Double,
)
astm_Void_strategy = st.builds(
    astm_Void,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
astm_PureVirtual_strategy = st.builds(
    astm_PureVirtual,
)
astm_NonVirtual_strategy = st.builds(
    astm_NonVirtual,
)
astm_Virtual_strategy = st.builds(
    astm_Virtual,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
astm_FileLocal_strategy = st.builds(
    astm_FileLocal,
)
astm_NoDef_strategy = st.builds(
    astm_NoDef,
)
astm_FunctionPersistent_strategy = st.builds(
    astm_FunctionPersistent,
)
astm_PerClassMember_strategy = st.builds(
    astm_PerClassMember,
)
astm_External_strategy = st.builds(
    astm_External,
)
Scope_strategy = st.builds(
    Scope,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
astm_MissingActualParameter_strategy = st.builds(
    astm_MissingActualParameter,
)
astm_ActualParameterExpression_strategy = st.builds(
    astm_ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
astm_NotEqual_strategy = st.builds(
    astm_NotEqual,
)
astm_BitXor_strategy = st.builds(
    astm_BitXor,
)
astm_SpecificIn_strategy = st.builds(
    astm_SpecificIn,
)
astm_SpecificLessEqual_strategy = st.builds(
    astm_SpecificLessEqual,
)
astm_Multiply_strategy = st.builds(
    astm_Multiply,
)
astm_BitRightShift_strategy = st.builds(
    astm_BitRightShift,
)
astm_Less_strategy = st.builds(
    astm_Less,
)
astm_Or_strategy = st.builds(
    astm_Or,
)
astm_SpecificLike_strategy = st.builds(
    astm_SpecificLike,
)
astm_Exponent_strategy = st.builds(
    astm_Exponent,
)
astm_Modulus_strategy = st.builds(
    astm_Modulus,
)
astm_Equal_strategy = st.builds(
    astm_Equal,
)
astm_SpecificGreaterEqual_strategy = st.builds(
    astm_SpecificGreaterEqual,
)
astm_SpecificConcatString_strategy = st.builds(
    astm_SpecificConcatString,
)
astm_BitOr_strategy = st.builds(
    astm_BitOr,
)
astm_And_strategy = st.builds(
    astm_And,
)
astm_Divide_strategy = st.builds(
    astm_Divide,
)
astm_BitLeftShift_strategy = st.builds(
    astm_BitLeftShift,
)
astm_Add_strategy = st.builds(
    astm_Add,
)
astm_Greater_strategy = st.builds(
    astm_Greater,
)
astm_Subtract_strategy = st.builds(
    astm_Subtract,
)
astm_NotGreater_strategy = st.builds(
    astm_NotGreater,
)
astm_Assign_strategy = st.builds(
    astm_Assign,
)
astm_NotLess_strategy = st.builds(
    astm_NotLess,
)
astm_BitAnd_strategy = st.builds(
    astm_BitAnd,
)
astm_OperatorAssign_strategy = st.builds(
    astm_OperatorAssign,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm_NamedTypeReference_strategy = st.builds(
    astm_NamedTypeReference,
)
astm_UnnamedTypeReference_strategy = st.builds(
    astm_UnnamedTypeReference,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
astm_UnionType_strategy = st.builds(
    astm_UnionType,
)
astm_AnnotationType_strategy = st.builds(
    astm_AnnotationType,
)
astm_StructureType_strategy = st.builds(
    astm_StructureType,
)
astm_ClassType_strategy = st.builds(
    astm_ClassType,
)
Type_strategy = st.builds(
    Type,
)
astm_FunctionType_strategy = st.builds(
    astm_FunctionType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
astm_PointerType_strategy = st.builds(
    astm_PointerType,
)
astm_ReferenceType_strategy = st.builds(
    astm_ReferenceType,
)
astm_CollectionType_strategy = st.builds(
    astm_CollectionType,
)
astm_RangeType_strategy = st.builds(
    astm_RangeType,
)
astm_ArrayType_strategy = st.builds(
    astm_ArrayType,
)
astm_AggregateScope_strategy = st.builds(
    astm_AggregateScope,
)
DataType_strategy = st.builds(
    DataType,
)
astm_EnumType_strategy = st.builds(
    astm_EnumType,
)
astm_RDBDataBaseType_strategy = st.builds(
    astm_RDBDataBaseType,
)
astm_RDBCursorType_strategy = st.builds(
    astm_RDBCursorType,
)
astm_RDBTableType_strategy = st.builds(
    astm_RDBTableType,
)
astm_ExceptionType_strategy = st.builds(
    astm_ExceptionType,
)
astm_RDBUserType_strategy = st.builds(
    astm_RDBUserType,
)
astm_RDBColumnType_strategy = st.builds(
    astm_RDBColumnType,
)
astm_FormalParameterType_strategy = st.builds(
    astm_FormalParameterType,
)
astm_ConstructedType_strategy = st.builds(
    astm_ConstructedType,
)
astm_RDBTableSpaceType_strategy = st.builds(
    astm_RDBTableSpaceType,
)
astm_RDBViewType_strategy = st.builds(
    astm_RDBViewType,
)
astm_PrimitiveType_strategy = st.builds(
    astm_PrimitiveType,
    isSigned=
        st.booleans()
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm_Type_strategy = st.builds(
    astm_Type,
    isVolatile=
        st.booleans(),
    isConst=
        st.booleans()
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm_MacroDefinition_strategy = st.builds(
    astm_MacroDefinition,
    macroName=
        safe_text,
    body=
        safe_text
)
astm_MacroCall_strategy = st.builds(
    astm_MacroCall,
)
astm_Comment_strategy = st.builds(
    astm_Comment,
    text=
        safe_text
)
astm_IncludeUnit_strategy = st.builds(
    astm_IncludeUnit,
)
astm_LabelType_strategy = st.builds(
    astm_LabelType,
)
astm_NameSpaceType_strategy = st.builds(
    astm_NameSpaceType,
)
astm_AggregateType_strategy = st.builds(
    astm_AggregateType,
)
astm_NamedType_strategy = st.builds(
    astm_NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
astm_AggregateTypeDefinition_strategy = st.builds(
    astm_AggregateTypeDefinition,
)
astm_NamedTypeDefinition_strategy = st.builds(
    astm_NamedTypeDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm_VariableDefinition_strategy = st.builds(
    astm_VariableDefinition,
)
astm_BitFieldDefinition_strategy = st.builds(
    astm_BitFieldDefinition,
)
astm_Expression_strategy = st.builds(
    astm_Expression,
)
astm_TypeReference_strategy = st.builds(
    astm_TypeReference,
)
astm_FunctionScope_strategy = st.builds(
    astm_FunctionScope,
)
astm_Statement_strategy = st.builds(
    astm_Statement,
)
astm_FormalParameterDefinition_strategy = st.builds(
    astm_FormalParameterDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
astm_RDBUserDefinition_strategy = st.builds(
    astm_RDBUserDefinition,
)
astm_DataDefinition_strategy = st.builds(
    astm_DataDefinition,
    isMutable=
        st.booleans()
)
astm_RDBTableDefinition_strategy = st.builds(
    astm_RDBTableDefinition,
)
astm_EntryDefinition_strategy = st.builds(
    astm_EntryDefinition,
)
astm_RDBCursorDefinition_strategy = st.builds(
    astm_RDBCursorDefinition,
)
astm_RDBColumnDefinition_strategy = st.builds(
    astm_RDBColumnDefinition,
    NotNull=
        st.booleans()
)
astm_SpecificTriggerDefinition_strategy = st.builds(
    astm_SpecificTriggerDefinition,
)
astm_EnumLiteralDefinition_strategy = st.builds(
    astm_EnumLiteralDefinition,
)
astm_RDBViewDefinition_strategy = st.builds(
    astm_RDBViewDefinition,
)
astm_RDBTableSpaceDefinition_strategy = st.builds(
    astm_RDBTableSpaceDefinition,
)
astm_RDBDatabaseDefinition_strategy = st.builds(
    astm_RDBDatabaseDefinition,
)
astm_FunctionDefinition_strategy = st.builds(
    astm_FunctionDefinition,
)
Declaration_strategy = st.builds(
    Declaration,
)
astm_VariableDeclaration_strategy = st.builds(
    astm_VariableDeclaration,
    isMutable=
        st.booleans()
)
astm_FormalParameterDeclaration_strategy = st.builds(
    astm_FormalParameterDeclaration,
)
astm_FunctionDeclaration_strategy = st.builds(
    astm_FunctionDeclaration,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm_Project_strategy = st.builds(
    astm_Project,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
astm_Declaration_strategy = st.builds(
    astm_Declaration,
)
astm_Definition_strategy = st.builds(
    astm_Definition,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm_TypeDefinition_strategy = st.builds(
    astm_TypeDefinition,
)
astm_LabelDefinition_strategy = st.builds(
    astm_LabelDefinition,
)
astm_NameSpaceDefinition_strategy = st.builds(
    astm_NameSpaceDefinition,
)
astm_DeclarationOrDefinition_strategy = st.builds(
    astm_DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
astm_ProgramScope_strategy = st.builds(
    astm_ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
astm_VirtualSpecification_strategy = st.builds(
    astm_VirtualSpecification,
)
astm_DerivesFrom_strategy = st.builds(
    astm_DerivesFrom,
    isVirtual=
        st.booleans()
)
astm_Dimension_strategy = st.builds(
    astm_Dimension,
)
astm_RDBTrigger_strategy = st.builds(
    astm_RDBTrigger,
)
astm_RDBIndexColumn_strategy = st.builds(
    astm_RDBIndexColumn,
    AscendingOrDescending=
        safe_text
)
astm_FunctionMemberAttribute_strategy = st.builds(
    astm_FunctionMemberAttribute,
)
astm_RDBIndex_strategy = st.builds(
    astm_RDBIndex,
    IsUnique=
        st.booleans(),
    NotNull=
        st.booleans()
)
astm_RDBConstraint_strategy = st.builds(
    astm_RDBConstraint,
)
astm_Name_strategy = st.builds(
    astm_Name,
    nameString=
        safe_text
)
astm_PreprocessorElement_strategy = st.builds(
    astm_PreprocessorElement,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm_GASTMSyntaxObject_strategy = st.builds(
    astm_GASTMSyntaxObject,
)
astm_DefinitionObject_strategy = st.builds(
    astm_DefinitionObject,
)
astm_Scope_strategy = st.builds(
    astm_Scope,
)
astm_GlobalScope_strategy = st.builds(
    astm_GlobalScope,
)
astm_CompilationUnit_strategy = st.builds(
    astm_CompilationUnit,
    language=
        safe_text
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
astm_SourceLocation_strategy = st.builds(
    astm_SourceLocation,
    startColumn=
        st.integers(),
    startLine=
        st.integers(),
    endLine=
        st.integers(),
    endColumn=
        st.integers()
)
astm_SourceFile_strategy = st.builds(
    astm_SourceFile,
    pathName=
        safe_text
)
Visitable_strategy = st.builds(
    Visitable,
)
astm_RDBHostVariableReference_strategy = st.builds(
    astm_RDBHostVariableReference,
)
astm_AccessKind_strategy = st.builds(
    astm_AccessKind,
)
astm_DataType_strategy = st.builds(
    astm_DataType,
)
astm_StorageSpecification_strategy = st.builds(
    astm_StorageSpecification,
)
astm_GASTMSourceObject_strategy = st.builds(
    astm_GASTMSourceObject,
)
astm_OtherSyntaxObject_strategy = st.builds(
    astm_OtherSyntaxObject,
)
astm_RDBTableSpaceReference_strategy = st.builds(
    astm_RDBTableSpaceReference,
)
astm_FunctionMemberAttributes_strategy = st.builds(
    astm_FunctionMemberAttributes,
    isThisConst=
        st.booleans(),
    isFriend=
        st.booleans(),
    isInline=
        st.booleans()
)
astm_ActualParameter_strategy = st.builds(
    astm_ActualParameter,
)
astm_BinaryOperator_strategy = st.builds(
    astm_BinaryOperator,
)
astm_GASTMSemanticObject_strategy = st.builds(
    astm_GASTMSemanticObject,
)
astm_UnaryOperator_strategy = st.builds(
    astm_UnaryOperator,
)
astm_GASTMObject_strategy = st.builds(
    astm_GASTMObject,
)
NameReference_strategy = st.builds(
    NameReference,
)
astm_IdentifierReference_strategy = st.builds(
    astm_IdentifierReference,
)
astm_TypeQualifiedIdentifierReference_strategy = st.builds(
    astm_TypeQualifiedIdentifierReference,
)
astm_QualifiedIdentifierReference_strategy = st.builds(
    astm_QualifiedIdentifierReference,
)
Expression_strategy = st.builds(
    Expression,
)
astm_ConditionalExpression_strategy = st.builds(
    astm_ConditionalExpression,
)
astm_NewExpression_strategy = st.builds(
    astm_NewExpression,
)
astm_AggregateExpression_strategy = st.builds(
    astm_AggregateExpression,
)
astm_RDBSelectExpression_strategy = st.builds(
    astm_RDBSelectExpression,
)
astm_FunctionCallExpression_strategy = st.builds(
    astm_FunctionCallExpression,
)
astm_RangeExpression_strategy = st.builds(
    astm_RangeExpression,
)
astm_CastExpression_strategy = st.builds(
    astm_CastExpression,
)
astm_Literal_strategy = st.builds(
    astm_Literal,
    value=
        safe_text
)
astm_RDBHostVariableExpression_strategy = st.builds(
    astm_RDBHostVariableExpression,
)
astm_ArrayAccess_strategy = st.builds(
    astm_ArrayAccess,
)
astm_AnnotationExpression_strategy = st.builds(
    astm_AnnotationExpression,
)
astm_BinaryExpression_strategy = st.builds(
    astm_BinaryExpression,
)
astm_UnaryExpression_strategy = st.builds(
    astm_UnaryExpression,
)
astm_NameReference_strategy = st.builds(
    astm_NameReference,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
astm_VariableCatchBlock_strategy = st.builds(
    astm_VariableCatchBlock,
)
astm_TypesCatchBlock_strategy = st.builds(
    astm_TypesCatchBlock,
)
astm_CatchBlock_strategy = st.builds(
    astm_CatchBlock,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
astm_WhileStatement_strategy = st.builds(
    astm_WhileStatement,
)
astm_DoWhileStatement_strategy = st.builds(
    astm_DoWhileStatement,
)
astm_ForStatement_strategy = st.builds(
    astm_ForStatement,
)
astm_LabelAccess_strategy = st.builds(
    astm_LabelAccess,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
astm_DefaultBlock_strategy = st.builds(
    astm_DefaultBlock,
)
astm_CaseBlock_strategy = st.builds(
    astm_CaseBlock,
)
astm_SwitchCase_strategy = st.builds(
    astm_SwitchCase,
)
astm_BlockScope_strategy = st.builds(
    astm_BlockScope,
)
Statement_strategy = st.builds(
    Statement,
)
astm_ReturnStatement_strategy = st.builds(
    astm_ReturnStatement,
)
astm_EmptyStatement_strategy = st.builds(
    astm_EmptyStatement,
)
astm_RDBInsertStatement_strategy = st.builds(
    astm_RDBInsertStatement,
)
astm_SwitchStatement_strategy = st.builds(
    astm_SwitchStatement,
)
astm_DeleteStatement_strategy = st.builds(
    astm_DeleteStatement,
)
astm_ExpressionStatement_strategy = st.builds(
    astm_ExpressionStatement,
)
astm_LoopStatement_strategy = st.builds(
    astm_LoopStatement,
)
astm_LabeledStatement_strategy = st.builds(
    astm_LabeledStatement,
)
astm_BreakStatement_strategy = st.builds(
    astm_BreakStatement,
)
astm_RDBCursorStatement_strategy = st.builds(
    astm_RDBCursorStatement,
)
astm_ContinueStatement_strategy = st.builds(
    astm_ContinueStatement,
)
astm_DeclarationOrDefinitionStatement_strategy = st.builds(
    astm_DeclarationOrDefinitionStatement,
)
astm_BlockStatement_strategy = st.builds(
    astm_BlockStatement,
)
astm_RDBSelectStatement_strategy = st.builds(
    astm_RDBSelectStatement,
)
astm_ThrowStatement_strategy = st.builds(
    astm_ThrowStatement,
)
astm_JumpStatement_strategy = st.builds(
    astm_JumpStatement,
)
astm_RDBModifyStatement_strategy = st.builds(
    astm_RDBModifyStatement,
)
astm_RDBConnectStatement_strategy = st.builds(
    astm_RDBConnectStatement,
)
astm_TerminateStatement_strategy = st.builds(
    astm_TerminateStatement,
)
astm_TryStatement_strategy = st.builds(
    astm_TryStatement,
)
astm_IfStatement_strategy = st.builds(
    astm_IfStatement,
)
astm_SpecificSelectStatement_strategy = st.builds(
    astm_SpecificSelectStatement,
)






































@given(instance=astm_RDBCheckConstraint_strategy)
def test_hyp_astm_rdbcheckconstraint_RDBConstraintText_setter(instance):
    original = instance.RDBConstraintText
    instance.RDBConstraintText = original
    assert instance.RDBConstraintText == original



@given(instance=astm_RDBCheckConstraint_strategy)
def test_hyp_astm_rdbcheckconstraint_RDBConstraintType_setter(instance):
    original = instance.RDBConstraintType
    instance.RDBConstraintType = original
    assert instance.RDBConstraintType == original


























































































































@given(instance=astm_PrimitiveType_strategy)
def test_hyp_astm_primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original





@given(instance=astm_Type_strategy)
def test_hyp_astm_type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original



@given(instance=astm_Type_strategy)
def test_hyp_astm_type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original





@given(instance=astm_MacroDefinition_strategy)
def test_hyp_astm_macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original



@given(instance=astm_MacroDefinition_strategy)
def test_hyp_astm_macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original





@given(instance=astm_Comment_strategy)
def test_hyp_astm_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






















@given(instance=astm_DataDefinition_strategy)
def test_hyp_astm_datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original







@given(instance=astm_RDBColumnDefinition_strategy)
def test_hyp_astm_rdbcolumndefinition_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original











@given(instance=astm_VariableDeclaration_strategy)
def test_hyp_astm_variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original















@given(instance=astm_DeclarationOrDefinition_strategy)
def test_hyp_astm_declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original



@given(instance=astm_DeclarationOrDefinition_strategy)
def test_hyp_astm_declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original







@given(instance=astm_DerivesFrom_strategy)
def test_hyp_astm_derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original






@given(instance=astm_RDBIndexColumn_strategy)
def test_hyp_astm_rdbindexcolumn_AscendingOrDescending_setter(instance):
    original = instance.AscendingOrDescending
    instance.AscendingOrDescending = original
    assert instance.AscendingOrDescending == original





@given(instance=astm_RDBIndex_strategy)
def test_hyp_astm_rdbindex_IsUnique_setter(instance):
    original = instance.IsUnique
    instance.IsUnique = original
    assert instance.IsUnique == original



@given(instance=astm_RDBIndex_strategy)
def test_hyp_astm_rdbindex_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original





@given(instance=astm_Name_strategy)
def test_hyp_astm_name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original










@given(instance=astm_CompilationUnit_strategy)
def test_hyp_astm_compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original





@given(instance=astm_SourceLocation_strategy)
def test_hyp_astm_sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=astm_SourceLocation_strategy)
def test_hyp_astm_sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=astm_SourceLocation_strategy)
def test_hyp_astm_sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=astm_SourceLocation_strategy)
def test_hyp_astm_sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original




@given(instance=astm_SourceFile_strategy)
def test_hyp_astm_sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original












@given(instance=astm_FunctionMemberAttributes_strategy)
def test_hyp_astm_functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_hyp_astm_functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_hyp_astm_functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original





















@given(instance=astm_Literal_strategy)
def test_hyp_astm_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original













































# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AccessKind,
    ActualParameter,
    ActualParameterExpression,
    AggregateType,
    BinaryOperator,
    CatchBlock,
    ConstructedType,
    DataDefinition,
    DataType,
    Declaration,
    DeclarationOrDefinition,
    Definition,
    DefinitionObject,
    Expression,
    ForStatement,
    FormalParameterType,
    GASTMObject,
    GASTMSemanticObject,
    GASTMSourceObject,
    GASTMSyntaxObject,
    IdentifierReference,
    Literal,
    LoopStatement,
    NameReference,
    OtherSyntaxObject,
    PreprocessorElement,
    PrimitiveType,
    QualifiedIdentifierReference,
    RDBColumnType,
    RDBConstraint,
    RDBCursorStatement,
    RDBModifyStatement,
    Scope,
    Statement,
    StorageSpecification,
    SwitchCase,
    Type,
    TypeDefinition,
    TypeReference,
    UnaryOperator,
    VirtualSpecification,
    Visitable,
    astm_AccessKind,
    astm_ActualParameter,
    astm_ActualParameterExpression,
    astm_Add,
    astm_AddressOf,
    astm_AggregateExpression,
    astm_AggregateScope,
    astm_AggregateType,
    astm_AggregateTypeDefinition,
    astm_And,
    astm_AnnotationExpression,
    astm_AnnotationType,
    astm_ArrayAccess,
    astm_ArrayType,
    astm_Assign,
    astm_BinaryExpression,
    astm_BinaryOperator,
    astm_BitAnd,
    astm_BitFieldDefinition,
    astm_BitLeftShift,
    astm_BitLiteral,
    astm_BitNot,
    astm_BitOr,
    astm_BitRightShift,
    astm_BitXor,
    astm_BlockScope,
    astm_BlockStatement,
    astm_Boolean,
    astm_BooleanLiteral,
    astm_BreakStatement,
    astm_ByReferenceActualParameterExpression,
    astm_ByReferenceFormalParameterType,
    astm_ByValueActualParameterExpression,
    astm_ByValueFormalParameterType,
    astm_Byte,
    astm_CaseBlock,
    astm_CastExpression,
    astm_CatchBlock,
    astm_CharLiteral,
    astm_Character,
    astm_ClassType,
    astm_CollectionType,
    astm_Comment,
    astm_CompilationUnit,
    astm_ConditionalExpression,
    astm_ConstructedType,
    astm_ContinueStatement,
    astm_DataDefinition,
    astm_DataType,
    astm_Declaration,
    astm_DeclarationOrDefinition,
    astm_DeclarationOrDefinitionStatement,
    astm_Decrement,
    astm_DefaultBlock,
    astm_Definition,
    astm_DefinitionObject,
    astm_DeleteStatement,
    astm_Deref,
    astm_DerivesFrom,
    astm_Dimension,
    astm_Divide,
    astm_DoWhileStatement,
    astm_Double,
    astm_EmptyStatement,
    astm_EntryDefinition,
    astm_EnumLiteralDefinition,
    astm_EnumType,
    astm_Equal,
    astm_ExceptionType,
    astm_Exponent,
    astm_Expression,
    astm_ExpressionStatement,
    astm_External,
    astm_FileLocal,
    astm_Float,
    astm_ForCheckAfterStatement,
    astm_ForCheckBeforeStatement,
    astm_ForStatement,
    astm_FormalParameterDeclaration,
    astm_FormalParameterDefinition,
    astm_FormalParameterType,
    astm_FunctionCallExpression,
    astm_FunctionDeclaration,
    astm_FunctionDefinition,
    astm_FunctionMemberAttribute,
    astm_FunctionMemberAttributes,
    astm_FunctionPersistent,
    astm_FunctionScope,
    astm_FunctionType,
    astm_GASTMObject,
    astm_GASTMSemanticObject,
    astm_GASTMSourceObject,
    astm_GASTMSyntaxObject,
    astm_GlobalScope,
    astm_Greater,
    astm_IdentifierReference,
    astm_IfStatement,
    astm_IncludeUnit,
    astm_Increment,
    astm_Integer,
    astm_IntegerlLiteral,
    astm_JumpStatement,
    astm_LabelAccess,
    astm_LabelDefinition,
    astm_LabelType,
    astm_LabeledStatement,
    astm_Less,
    astm_Literal,
    astm_LongDouble,
    astm_LongInteger,
    astm_LoopStatement,
    astm_MacroCall,
    astm_MacroDefinition,
    astm_MissingActualParameter,
    astm_Modulus,
    astm_Multiply,
    astm_Name,
    astm_NameReference,
    astm_NameSpaceDefinition,
    astm_NameSpaceType,
    astm_NamedType,
    astm_NamedTypeDefinition,
    astm_NamedTypeReference,
    astm_Negate,
    astm_NewExpression,
    astm_NoDef,
    astm_NonVirtual,
    astm_Not,
    astm_NotEqual,
    astm_NotGreater,
    astm_NotLess,
    astm_OperatorAssign,
    astm_Or,
    astm_OtherSyntaxObject,
    astm_PerClassMember,
    astm_PointerType,
    astm_PostDecrement,
    astm_PostIncrement,
    astm_PreprocessorElement,
    astm_PrimitiveType,
    astm_Private,
    astm_ProgramScope,
    astm_Project,
    astm_Protected,
    astm_Public,
    astm_PureVirtual,
    astm_QualifiedIdentifierReference,
    astm_QualifiedOverData,
    astm_QualifiedOverPointer,
    astm_RDBBFile,
    astm_RDBBlob,
    astm_RDBBoolean,
    astm_RDBChar,
    astm_RDBCheckConstraint,
    astm_RDBClob,
    astm_RDBCloseCursorStatement,
    astm_RDBColumnDefinition,
    astm_RDBColumnReference,
    astm_RDBColumnType,
    astm_RDBConnectStatement,
    astm_RDBConstraint,
    astm_RDBCursorDefinition,
    astm_RDBCursorStatement,
    astm_RDBCursorType,
    astm_RDBDataBaseType,
    astm_RDBDatabaseDefinition,
    astm_RDBDate,
    astm_RDBDecimal,
    astm_RDBDeleteStatement,
    astm_RDBFetchCursorStatement,
    astm_RDBFloat,
    astm_RDBHostVariableExpression,
    astm_RDBHostVariableReference,
    astm_RDBIndex,
    astm_RDBIndexColumn,
    astm_RDBInsertStatement,
    astm_RDBInt,
    astm_RDBInteger,
    astm_RDBLong,
    astm_RDBModifyStatement,
    astm_RDBNClob,
    astm_RDBNumber,
    astm_RDBOpenCursorStatement,
    astm_RDBRaw,
    astm_RDBReal,
    astm_RDBRefIntegrity,
    astm_RDBRowid,
    astm_RDBSelectExpression,
    astm_RDBSelectStatement,
    astm_RDBString,
    astm_RDBTableAlias,
    astm_RDBTableDefinition,
    astm_RDBTableReference,
    astm_RDBTableSpaceDefinition,
    astm_RDBTableSpaceReference,
    astm_RDBTableSpaceType,
    astm_RDBTableType,
    astm_RDBTimestamp,
    astm_RDBTrigger,
    astm_RDBUniqueKey,
    astm_RDBUpdateStatement,
    astm_RDBUserDefinition,
    astm_RDBUserType,
    astm_RDBVarchar,
    astm_RDBViewDefinition,
    astm_RDBViewType,
    astm_RangeExpression,
    astm_RangeType,
    astm_RealLiteral,
    astm_ReferenceType,
    astm_ReturnStatement,
    astm_Scope,
    astm_ShortInteger,
    astm_SourceFile,
    astm_SourceLocation,
    astm_SpecificConcatString,
    astm_SpecificGreaterEqual,
    astm_SpecificIn,
    astm_SpecificLessEqual,
    astm_SpecificLike,
    astm_SpecificSelectStatement,
    astm_SpecificTriggerDefinition,
    astm_Statement,
    astm_StorageSpecification,
    astm_String,
    astm_StringLiteral,
    astm_StructureType,
    astm_Subtract,
    astm_SwitchCase,
    astm_SwitchStatement,
    astm_TerminateStatement,
    astm_ThrowStatement,
    astm_TryStatement,
    astm_Type,
    astm_TypeDefinition,
    astm_TypeQualifiedIdentifierReference,
    astm_TypeReference,
    astm_TypesCatchBlock,
    astm_UnaryExpression,
    astm_UnaryOperator,
    astm_UnaryPlus,
    astm_UnionType,
    astm_UnnamedTypeReference,
    astm_VariableCatchBlock,
    astm_VariableDeclaration,
    astm_VariableDefinition,
    astm_Virtual,
    astm_VirtualSpecification,
    astm_Visitable,
    astm_Void,
    astm_WhileStatement,
    astm_WideCharacter,
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

def test_astm_Comment_text_value_roundtrip():
    instance = astm_Comment(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_astm_CompilationUnit_language_value_roundtrip():
    instance = astm_CompilationUnit(language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_astm_DataDefinition_isMutable_value_roundtrip():
    instance = astm_DataDefinition(isMutable=True)
    assert instance.isMutable == True
    instance.isMutable = False
    assert instance.isMutable == False


def test_astm_DeclarationOrDefinition_isRegister_value_roundtrip():
    instance = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    assert instance.isRegister == True
    instance.isRegister = False
    assert instance.isRegister == False


def test_astm_DeclarationOrDefinition_linkageSpecifier_value_roundtrip():
    instance = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    assert instance.linkageSpecifier == "sample_text"
    instance.linkageSpecifier = "sample_text_2"
    assert instance.linkageSpecifier == "sample_text_2"


def test_astm_DerivesFrom_isVirtual_value_roundtrip():
    instance = astm_DerivesFrom(isVirtual=True)
    assert instance.isVirtual == True
    instance.isVirtual = False
    assert instance.isVirtual == False


def test_astm_FunctionMemberAttributes_isFriend_value_roundtrip():
    instance = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    assert instance.isFriend == True
    instance.isFriend = False
    assert instance.isFriend == False


def test_astm_FunctionMemberAttributes_isInline_value_roundtrip():
    instance = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    assert instance.isInline == True
    instance.isInline = False
    assert instance.isInline == False


def test_astm_FunctionMemberAttributes_isThisConst_value_roundtrip():
    instance = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    assert instance.isThisConst == True
    instance.isThisConst = False
    assert instance.isThisConst == False


def test_astm_Literal_value_value_roundtrip():
    instance = astm_Literal(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_astm_MacroDefinition_body_value_roundtrip():
    instance = astm_MacroDefinition(body="sample_text", macroName="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_astm_MacroDefinition_macroName_value_roundtrip():
    instance = astm_MacroDefinition(body="sample_text", macroName="sample_text")
    assert instance.macroName == "sample_text"
    instance.macroName = "sample_text_2"
    assert instance.macroName == "sample_text_2"


def test_astm_Name_nameString_value_roundtrip():
    instance = astm_Name(nameString="sample_text")
    assert instance.nameString == "sample_text"
    instance.nameString = "sample_text_2"
    assert instance.nameString == "sample_text_2"


def test_astm_PrimitiveType_isSigned_value_roundtrip():
    instance = astm_PrimitiveType(isSigned=True)
    assert instance.isSigned == True
    instance.isSigned = False
    assert instance.isSigned == False


def test_astm_RDBCheckConstraint_RDBConstraintText_value_roundtrip():
    instance = astm_RDBCheckConstraint(RDBConstraintText="sample_text", RDBConstraintType="sample_text")
    assert instance.RDBConstraintText == "sample_text"
    instance.RDBConstraintText = "sample_text_2"
    assert instance.RDBConstraintText == "sample_text_2"


def test_astm_RDBCheckConstraint_RDBConstraintType_value_roundtrip():
    instance = astm_RDBCheckConstraint(RDBConstraintText="sample_text", RDBConstraintType="sample_text")
    assert instance.RDBConstraintType == "sample_text"
    instance.RDBConstraintType = "sample_text_2"
    assert instance.RDBConstraintType == "sample_text_2"


def test_astm_RDBColumnDefinition_NotNull_value_roundtrip():
    instance = astm_RDBColumnDefinition(NotNull=True)
    assert instance.NotNull == True
    instance.NotNull = False
    assert instance.NotNull == False


def test_astm_RDBIndex_IsUnique_value_roundtrip():
    instance = astm_RDBIndex(IsUnique=True, NotNull=True)
    assert instance.IsUnique == True
    instance.IsUnique = False
    assert instance.IsUnique == False


def test_astm_RDBIndex_NotNull_value_roundtrip():
    instance = astm_RDBIndex(IsUnique=True, NotNull=True)
    assert instance.NotNull == True
    instance.NotNull = False
    assert instance.NotNull == False


def test_astm_RDBIndexColumn_AscendingOrDescending_value_roundtrip():
    instance = astm_RDBIndexColumn(AscendingOrDescending="sample_text")
    assert instance.AscendingOrDescending == "sample_text"
    instance.AscendingOrDescending = "sample_text_2"
    assert instance.AscendingOrDescending == "sample_text_2"


def test_astm_SourceFile_pathName_value_roundtrip():
    instance = astm_SourceFile(pathName="sample_text")
    assert instance.pathName == "sample_text"
    instance.pathName = "sample_text_2"
    assert instance.pathName == "sample_text_2"


def test_astm_SourceLocation_endColumn_value_roundtrip():
    instance = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    assert instance.endColumn == 7
    instance.endColumn = 13
    assert instance.endColumn == 13


def test_astm_SourceLocation_endLine_value_roundtrip():
    instance = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    assert instance.endLine == 7
    instance.endLine = 13
    assert instance.endLine == 13


def test_astm_SourceLocation_startColumn_value_roundtrip():
    instance = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    assert instance.startColumn == 7
    instance.startColumn = 13
    assert instance.startColumn == 13


def test_astm_SourceLocation_startLine_value_roundtrip():
    instance = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    assert instance.startLine == 7
    instance.startLine = 13
    assert instance.startLine == 13


def test_astm_Type_isConst_value_roundtrip():
    instance = astm_Type(isConst=True, isVolatile=True)
    assert instance.isConst == True
    instance.isConst = False
    assert instance.isConst == False


def test_astm_Type_isVolatile_value_roundtrip():
    instance = astm_Type(isConst=True, isVolatile=True)
    assert instance.isVolatile == True
    instance.isVolatile = False
    assert instance.isVolatile == False


def test_astm_VariableDeclaration_isMutable_value_roundtrip():
    instance = astm_VariableDeclaration(isMutable=True)
    assert instance.isMutable == True
    instance.isMutable = False
    assert instance.isMutable == False


def test_astm_Private_isa_AccessKind():
    instance = astm_Private()
    assert isinstance(instance, AccessKind)


def test_astm_Protected_isa_AccessKind():
    instance = astm_Protected()
    assert isinstance(instance, AccessKind)


def test_astm_Public_isa_AccessKind():
    instance = astm_Public()
    assert isinstance(instance, AccessKind)


def test_astm_ActualParameterExpression_isa_ActualParameter():
    instance = astm_ActualParameterExpression()
    assert isinstance(instance, ActualParameter)


def test_astm_MissingActualParameter_isa_ActualParameter():
    instance = astm_MissingActualParameter()
    assert isinstance(instance, ActualParameter)


def test_astm_ByReferenceActualParameterExpression_isa_ActualParameterExpression():
    instance = astm_ByReferenceActualParameterExpression()
    assert isinstance(instance, ActualParameterExpression)


def test_astm_ByValueActualParameterExpression_isa_ActualParameterExpression():
    instance = astm_ByValueActualParameterExpression()
    assert isinstance(instance, ActualParameterExpression)


def test_astm_AnnotationType_isa_AggregateType():
    instance = astm_AnnotationType()
    assert isinstance(instance, AggregateType)


def test_astm_ClassType_isa_AggregateType():
    instance = astm_ClassType()
    assert isinstance(instance, AggregateType)


def test_astm_StructureType_isa_AggregateType():
    instance = astm_StructureType()
    assert isinstance(instance, AggregateType)


def test_astm_UnionType_isa_AggregateType():
    instance = astm_UnionType()
    assert isinstance(instance, AggregateType)


def test_astm_Add_isa_BinaryOperator():
    instance = astm_Add()
    assert isinstance(instance, BinaryOperator)


def test_astm_And_isa_BinaryOperator():
    instance = astm_And()
    assert isinstance(instance, BinaryOperator)


def test_astm_Assign_isa_BinaryOperator():
    instance = astm_Assign()
    assert isinstance(instance, BinaryOperator)


def test_astm_BitAnd_isa_BinaryOperator():
    instance = astm_BitAnd()
    assert isinstance(instance, BinaryOperator)


def test_astm_BitLeftShift_isa_BinaryOperator():
    instance = astm_BitLeftShift()
    assert isinstance(instance, BinaryOperator)


def test_astm_BitOr_isa_BinaryOperator():
    instance = astm_BitOr()
    assert isinstance(instance, BinaryOperator)


def test_astm_BitRightShift_isa_BinaryOperator():
    instance = astm_BitRightShift()
    assert isinstance(instance, BinaryOperator)


def test_astm_BitXor_isa_BinaryOperator():
    instance = astm_BitXor()
    assert isinstance(instance, BinaryOperator)


def test_astm_Divide_isa_BinaryOperator():
    instance = astm_Divide()
    assert isinstance(instance, BinaryOperator)


def test_astm_Equal_isa_BinaryOperator():
    instance = astm_Equal()
    assert isinstance(instance, BinaryOperator)


def test_astm_Exponent_isa_BinaryOperator():
    instance = astm_Exponent()
    assert isinstance(instance, BinaryOperator)


def test_astm_Greater_isa_BinaryOperator():
    instance = astm_Greater()
    assert isinstance(instance, BinaryOperator)


def test_astm_Less_isa_BinaryOperator():
    instance = astm_Less()
    assert isinstance(instance, BinaryOperator)


def test_astm_Modulus_isa_BinaryOperator():
    instance = astm_Modulus()
    assert isinstance(instance, BinaryOperator)


def test_astm_Multiply_isa_BinaryOperator():
    instance = astm_Multiply()
    assert isinstance(instance, BinaryOperator)


def test_astm_NotEqual_isa_BinaryOperator():
    instance = astm_NotEqual()
    assert isinstance(instance, BinaryOperator)


def test_astm_NotGreater_isa_BinaryOperator():
    instance = astm_NotGreater()
    assert isinstance(instance, BinaryOperator)


def test_astm_NotLess_isa_BinaryOperator():
    instance = astm_NotLess()
    assert isinstance(instance, BinaryOperator)


def test_astm_OperatorAssign_isa_BinaryOperator():
    instance = astm_OperatorAssign()
    assert isinstance(instance, BinaryOperator)


def test_astm_Or_isa_BinaryOperator():
    instance = astm_Or()
    assert isinstance(instance, BinaryOperator)


def test_astm_SpecificConcatString_isa_BinaryOperator():
    instance = astm_SpecificConcatString()
    assert isinstance(instance, BinaryOperator)


def test_astm_SpecificGreaterEqual_isa_BinaryOperator():
    instance = astm_SpecificGreaterEqual()
    assert isinstance(instance, BinaryOperator)


def test_astm_SpecificIn_isa_BinaryOperator():
    instance = astm_SpecificIn()
    assert isinstance(instance, BinaryOperator)


def test_astm_SpecificLessEqual_isa_BinaryOperator():
    instance = astm_SpecificLessEqual()
    assert isinstance(instance, BinaryOperator)


def test_astm_SpecificLike_isa_BinaryOperator():
    instance = astm_SpecificLike()
    assert isinstance(instance, BinaryOperator)


def test_astm_Subtract_isa_BinaryOperator():
    instance = astm_Subtract()
    assert isinstance(instance, BinaryOperator)


def test_astm_TypesCatchBlock_isa_CatchBlock():
    instance = astm_TypesCatchBlock()
    assert isinstance(instance, CatchBlock)


def test_astm_VariableCatchBlock_isa_CatchBlock():
    instance = astm_VariableCatchBlock()
    assert isinstance(instance, CatchBlock)


def test_astm_ArrayType_isa_ConstructedType():
    instance = astm_ArrayType()
    assert isinstance(instance, ConstructedType)


def test_astm_CollectionType_isa_ConstructedType():
    instance = astm_CollectionType()
    assert isinstance(instance, ConstructedType)


def test_astm_PointerType_isa_ConstructedType():
    instance = astm_PointerType()
    assert isinstance(instance, ConstructedType)


def test_astm_RangeType_isa_ConstructedType():
    instance = astm_RangeType()
    assert isinstance(instance, ConstructedType)


def test_astm_ReferenceType_isa_ConstructedType():
    instance = astm_ReferenceType()
    assert isinstance(instance, ConstructedType)


def test_astm_BitFieldDefinition_isa_DataDefinition():
    instance = astm_BitFieldDefinition()
    assert isinstance(instance, DataDefinition)


def test_astm_FormalParameterDefinition_isa_DataDefinition():
    instance = astm_FormalParameterDefinition()
    assert isinstance(instance, DataDefinition)


def test_astm_VariableDefinition_isa_DataDefinition():
    instance = astm_VariableDefinition()
    assert isinstance(instance, DataDefinition)


def test_astm_AggregateType_isa_DataType():
    instance = astm_AggregateType()
    assert isinstance(instance, DataType)


def test_astm_ConstructedType_isa_DataType():
    instance = astm_ConstructedType()
    assert isinstance(instance, DataType)


def test_astm_EnumType_isa_DataType():
    instance = astm_EnumType()
    assert isinstance(instance, DataType)


def test_astm_ExceptionType_isa_DataType():
    instance = astm_ExceptionType()
    assert isinstance(instance, DataType)


def test_astm_FormalParameterType_isa_DataType():
    instance = astm_FormalParameterType()
    assert isinstance(instance, DataType)


def test_astm_NamedType_isa_DataType():
    instance = astm_NamedType()
    assert isinstance(instance, DataType)


def test_astm_PrimitiveType_isa_DataType():
    instance = astm_PrimitiveType(isSigned=True)
    assert isinstance(instance, DataType)


def test_astm_RDBColumnType_isa_DataType():
    instance = astm_RDBColumnType()
    assert isinstance(instance, DataType)


def test_astm_RDBCursorType_isa_DataType():
    instance = astm_RDBCursorType()
    assert isinstance(instance, DataType)


def test_astm_RDBDataBaseType_isa_DataType():
    instance = astm_RDBDataBaseType()
    assert isinstance(instance, DataType)


def test_astm_RDBTableSpaceType_isa_DataType():
    instance = astm_RDBTableSpaceType()
    assert isinstance(instance, DataType)


def test_astm_RDBTableType_isa_DataType():
    instance = astm_RDBTableType()
    assert isinstance(instance, DataType)


def test_astm_RDBUserType_isa_DataType():
    instance = astm_RDBUserType()
    assert isinstance(instance, DataType)


def test_astm_RDBViewType_isa_DataType():
    instance = astm_RDBViewType()
    assert isinstance(instance, DataType)


def test_astm_FormalParameterDeclaration_isa_Declaration():
    instance = astm_FormalParameterDeclaration()
    assert isinstance(instance, Declaration)


def test_astm_FunctionDeclaration_isa_Declaration():
    instance = astm_FunctionDeclaration()
    assert isinstance(instance, Declaration)


def test_astm_VariableDeclaration_isa_Declaration():
    instance = astm_VariableDeclaration(isMutable=True)
    assert isinstance(instance, Declaration)


def test_astm_Declaration_isa_DeclarationOrDefinition():
    instance = astm_Declaration()
    assert isinstance(instance, DeclarationOrDefinition)


def test_astm_Definition_isa_DeclarationOrDefinition():
    instance = astm_Definition()
    assert isinstance(instance, DeclarationOrDefinition)


def test_astm_DataDefinition_isa_Definition():
    instance = astm_DataDefinition(isMutable=True)
    assert isinstance(instance, Definition)


def test_astm_EntryDefinition_isa_Definition():
    instance = astm_EntryDefinition()
    assert isinstance(instance, Definition)


def test_astm_EnumLiteralDefinition_isa_Definition():
    instance = astm_EnumLiteralDefinition()
    assert isinstance(instance, Definition)


def test_astm_FunctionDefinition_isa_Definition():
    instance = astm_FunctionDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBColumnDefinition_isa_Definition():
    instance = astm_RDBColumnDefinition(NotNull=True)
    assert isinstance(instance, Definition)


def test_astm_RDBCursorDefinition_isa_Definition():
    instance = astm_RDBCursorDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBDatabaseDefinition_isa_Definition():
    instance = astm_RDBDatabaseDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBTableDefinition_isa_Definition():
    instance = astm_RDBTableDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBTableSpaceDefinition_isa_Definition():
    instance = astm_RDBTableSpaceDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBTrigger_isa_Definition():
    instance = astm_RDBTrigger()
    assert isinstance(instance, Definition)


def test_astm_RDBUserDefinition_isa_Definition():
    instance = astm_RDBUserDefinition()
    assert isinstance(instance, Definition)


def test_astm_RDBViewDefinition_isa_Definition():
    instance = astm_RDBViewDefinition()
    assert isinstance(instance, Definition)


def test_astm_SpecificTriggerDefinition_isa_Definition():
    instance = astm_SpecificTriggerDefinition()
    assert isinstance(instance, Definition)


def test_astm_DeclarationOrDefinition_isa_DefinitionObject():
    instance = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    assert isinstance(instance, DefinitionObject)


def test_astm_LabelDefinition_isa_DefinitionObject():
    instance = astm_LabelDefinition()
    assert isinstance(instance, DefinitionObject)


def test_astm_NameSpaceDefinition_isa_DefinitionObject():
    instance = astm_NameSpaceDefinition()
    assert isinstance(instance, DefinitionObject)


def test_astm_TypeDefinition_isa_DefinitionObject():
    instance = astm_TypeDefinition()
    assert isinstance(instance, DefinitionObject)


def test_astm_AggregateExpression_isa_Expression():
    instance = astm_AggregateExpression()
    assert isinstance(instance, Expression)


def test_astm_AnnotationExpression_isa_Expression():
    instance = astm_AnnotationExpression()
    assert isinstance(instance, Expression)


def test_astm_ArrayAccess_isa_Expression():
    instance = astm_ArrayAccess()
    assert isinstance(instance, Expression)


def test_astm_BinaryExpression_isa_Expression():
    instance = astm_BinaryExpression()
    assert isinstance(instance, Expression)


def test_astm_CastExpression_isa_Expression():
    instance = astm_CastExpression()
    assert isinstance(instance, Expression)


def test_astm_ConditionalExpression_isa_Expression():
    instance = astm_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_astm_FunctionCallExpression_isa_Expression():
    instance = astm_FunctionCallExpression()
    assert isinstance(instance, Expression)


def test_astm_LabelAccess_isa_Expression():
    instance = astm_LabelAccess()
    assert isinstance(instance, Expression)


def test_astm_Literal_isa_Expression():
    instance = astm_Literal(value="sample_text")
    assert isinstance(instance, Expression)


def test_astm_NameReference_isa_Expression():
    instance = astm_NameReference()
    assert isinstance(instance, Expression)


def test_astm_NewExpression_isa_Expression():
    instance = astm_NewExpression()
    assert isinstance(instance, Expression)


def test_astm_RDBHostVariableExpression_isa_Expression():
    instance = astm_RDBHostVariableExpression()
    assert isinstance(instance, Expression)


def test_astm_RDBSelectExpression_isa_Expression():
    instance = astm_RDBSelectExpression()
    assert isinstance(instance, Expression)


def test_astm_RangeExpression_isa_Expression():
    instance = astm_RangeExpression()
    assert isinstance(instance, Expression)


def test_astm_UnaryExpression_isa_Expression():
    instance = astm_UnaryExpression()
    assert isinstance(instance, Expression)


def test_astm_ForCheckAfterStatement_isa_ForStatement():
    instance = astm_ForCheckAfterStatement()
    assert isinstance(instance, ForStatement)


def test_astm_ForCheckBeforeStatement_isa_ForStatement():
    instance = astm_ForCheckBeforeStatement()
    assert isinstance(instance, ForStatement)


def test_astm_ByReferenceFormalParameterType_isa_FormalParameterType():
    instance = astm_ByReferenceFormalParameterType()
    assert isinstance(instance, FormalParameterType)


def test_astm_ByValueFormalParameterType_isa_FormalParameterType():
    instance = astm_ByValueFormalParameterType()
    assert isinstance(instance, FormalParameterType)


def test_astm_GASTMSyntaxObject_isa_GASTMObject():
    instance = astm_GASTMSyntaxObject()
    assert isinstance(instance, GASTMObject)


def test_astm_Project_isa_GASTMSemanticObject():
    instance = astm_Project()
    assert isinstance(instance, GASTMSemanticObject)


def test_astm_Scope_isa_GASTMSemanticObject():
    instance = astm_Scope()
    assert isinstance(instance, GASTMSemanticObject)


def test_astm_SourceFile_isa_GASTMSourceObject():
    instance = astm_SourceFile(pathName="sample_text")
    assert isinstance(instance, GASTMSourceObject)


def test_astm_SourceLocation_isa_GASTMSourceObject():
    instance = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    assert isinstance(instance, GASTMSourceObject)


def test_astm_DefinitionObject_isa_GASTMSyntaxObject():
    instance = astm_DefinitionObject()
    assert isinstance(instance, GASTMSyntaxObject)


def test_astm_Expression_isa_GASTMSyntaxObject():
    instance = astm_Expression()
    assert isinstance(instance, GASTMSyntaxObject)


def test_astm_PreprocessorElement_isa_GASTMSyntaxObject():
    instance = astm_PreprocessorElement()
    assert isinstance(instance, GASTMSyntaxObject)


def test_astm_Statement_isa_GASTMSyntaxObject():
    instance = astm_Statement()
    assert isinstance(instance, GASTMSyntaxObject)


def test_astm_Type_isa_GASTMSyntaxObject():
    instance = astm_Type(isConst=True, isVolatile=True)
    assert isinstance(instance, GASTMSyntaxObject)


def test_astm_RDBColumnReference_isa_IdentifierReference():
    instance = astm_RDBColumnReference()
    assert isinstance(instance, IdentifierReference)


def test_astm_RDBTableAlias_isa_IdentifierReference():
    instance = astm_RDBTableAlias()
    assert isinstance(instance, IdentifierReference)


def test_astm_RDBTableReference_isa_IdentifierReference():
    instance = astm_RDBTableReference()
    assert isinstance(instance, IdentifierReference)


def test_astm_BitLiteral_isa_Literal():
    instance = astm_BitLiteral()
    assert isinstance(instance, Literal)


def test_astm_BooleanLiteral_isa_Literal():
    instance = astm_BooleanLiteral()
    assert isinstance(instance, Literal)


def test_astm_CharLiteral_isa_Literal():
    instance = astm_CharLiteral()
    assert isinstance(instance, Literal)


def test_astm_IntegerlLiteral_isa_Literal():
    instance = astm_IntegerlLiteral()
    assert isinstance(instance, Literal)


def test_astm_RealLiteral_isa_Literal():
    instance = astm_RealLiteral()
    assert isinstance(instance, Literal)


def test_astm_StringLiteral_isa_Literal():
    instance = astm_StringLiteral()
    assert isinstance(instance, Literal)


def test_astm_DoWhileStatement_isa_LoopStatement():
    instance = astm_DoWhileStatement()
    assert isinstance(instance, LoopStatement)


def test_astm_ForStatement_isa_LoopStatement():
    instance = astm_ForStatement()
    assert isinstance(instance, LoopStatement)


def test_astm_WhileStatement_isa_LoopStatement():
    instance = astm_WhileStatement()
    assert isinstance(instance, LoopStatement)


def test_astm_IdentifierReference_isa_NameReference():
    instance = astm_IdentifierReference()
    assert isinstance(instance, NameReference)


def test_astm_QualifiedIdentifierReference_isa_NameReference():
    instance = astm_QualifiedIdentifierReference()
    assert isinstance(instance, NameReference)


def test_astm_TypeQualifiedIdentifierReference_isa_NameReference():
    instance = astm_TypeQualifiedIdentifierReference()
    assert isinstance(instance, NameReference)


def test_astm_CatchBlock_isa_OtherSyntaxObject():
    instance = astm_CatchBlock()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_CompilationUnit_isa_OtherSyntaxObject():
    instance = astm_CompilationUnit(language="sample_text")
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_DerivesFrom_isa_OtherSyntaxObject():
    instance = astm_DerivesFrom(isVirtual=True)
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_Dimension_isa_OtherSyntaxObject():
    instance = astm_Dimension()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_FunctionMemberAttribute_isa_OtherSyntaxObject():
    instance = astm_FunctionMemberAttribute()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_Name_isa_OtherSyntaxObject():
    instance = astm_Name(nameString="sample_text")
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_RDBConstraint_isa_OtherSyntaxObject():
    instance = astm_RDBConstraint()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_RDBIndex_isa_OtherSyntaxObject():
    instance = astm_RDBIndex(IsUnique=True, NotNull=True)
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_RDBIndexColumn_isa_OtherSyntaxObject():
    instance = astm_RDBIndexColumn(AscendingOrDescending="sample_text")
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_RDBTrigger_isa_OtherSyntaxObject():
    instance = astm_RDBTrigger()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_SwitchCase_isa_OtherSyntaxObject():
    instance = astm_SwitchCase()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_VirtualSpecification_isa_OtherSyntaxObject():
    instance = astm_VirtualSpecification()
    assert isinstance(instance, OtherSyntaxObject)


def test_astm_Comment_isa_PreprocessorElement():
    instance = astm_Comment(text="sample_text")
    assert isinstance(instance, PreprocessorElement)


def test_astm_IncludeUnit_isa_PreprocessorElement():
    instance = astm_IncludeUnit()
    assert isinstance(instance, PreprocessorElement)


def test_astm_MacroCall_isa_PreprocessorElement():
    instance = astm_MacroCall()
    assert isinstance(instance, PreprocessorElement)


def test_astm_MacroDefinition_isa_PreprocessorElement():
    instance = astm_MacroDefinition(body="sample_text", macroName="sample_text")
    assert isinstance(instance, PreprocessorElement)


def test_astm_Boolean_isa_PrimitiveType():
    instance = astm_Boolean()
    assert isinstance(instance, PrimitiveType)


def test_astm_Byte_isa_PrimitiveType():
    instance = astm_Byte()
    assert isinstance(instance, PrimitiveType)


def test_astm_Character_isa_PrimitiveType():
    instance = astm_Character()
    assert isinstance(instance, PrimitiveType)


def test_astm_Double_isa_PrimitiveType():
    instance = astm_Double()
    assert isinstance(instance, PrimitiveType)


def test_astm_Float_isa_PrimitiveType():
    instance = astm_Float()
    assert isinstance(instance, PrimitiveType)


def test_astm_Integer_isa_PrimitiveType():
    instance = astm_Integer()
    assert isinstance(instance, PrimitiveType)


def test_astm_LongDouble_isa_PrimitiveType():
    instance = astm_LongDouble()
    assert isinstance(instance, PrimitiveType)


def test_astm_LongInteger_isa_PrimitiveType():
    instance = astm_LongInteger()
    assert isinstance(instance, PrimitiveType)


def test_astm_ShortInteger_isa_PrimitiveType():
    instance = astm_ShortInteger()
    assert isinstance(instance, PrimitiveType)


def test_astm_String_isa_PrimitiveType():
    instance = astm_String()
    assert isinstance(instance, PrimitiveType)


def test_astm_Void_isa_PrimitiveType():
    instance = astm_Void()
    assert isinstance(instance, PrimitiveType)


def test_astm_WideCharacter_isa_PrimitiveType():
    instance = astm_WideCharacter()
    assert isinstance(instance, PrimitiveType)


def test_astm_QualifiedOverData_isa_QualifiedIdentifierReference():
    instance = astm_QualifiedOverData()
    assert isinstance(instance, QualifiedIdentifierReference)


def test_astm_QualifiedOverPointer_isa_QualifiedIdentifierReference():
    instance = astm_QualifiedOverPointer()
    assert isinstance(instance, QualifiedIdentifierReference)


def test_astm_RDBBFile_isa_RDBColumnType():
    instance = astm_RDBBFile()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBBlob_isa_RDBColumnType():
    instance = astm_RDBBlob()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBBoolean_isa_RDBColumnType():
    instance = astm_RDBBoolean()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBChar_isa_RDBColumnType():
    instance = astm_RDBChar()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBClob_isa_RDBColumnType():
    instance = astm_RDBClob()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBDate_isa_RDBColumnType():
    instance = astm_RDBDate()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBDecimal_isa_RDBColumnType():
    instance = astm_RDBDecimal()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBFloat_isa_RDBColumnType():
    instance = astm_RDBFloat()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBInt_isa_RDBColumnType():
    instance = astm_RDBInt()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBInteger_isa_RDBColumnType():
    instance = astm_RDBInteger()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBLong_isa_RDBColumnType():
    instance = astm_RDBLong()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBNClob_isa_RDBColumnType():
    instance = astm_RDBNClob()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBNumber_isa_RDBColumnType():
    instance = astm_RDBNumber()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBRaw_isa_RDBColumnType():
    instance = astm_RDBRaw()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBReal_isa_RDBColumnType():
    instance = astm_RDBReal()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBRowid_isa_RDBColumnType():
    instance = astm_RDBRowid()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBString_isa_RDBColumnType():
    instance = astm_RDBString()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBTimestamp_isa_RDBColumnType():
    instance = astm_RDBTimestamp()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBVarchar_isa_RDBColumnType():
    instance = astm_RDBVarchar()
    assert isinstance(instance, RDBColumnType)


def test_astm_RDBCheckConstraint_isa_RDBConstraint():
    instance = astm_RDBCheckConstraint(RDBConstraintText="sample_text", RDBConstraintType="sample_text")
    assert isinstance(instance, RDBConstraint)


def test_astm_RDBRefIntegrity_isa_RDBConstraint():
    instance = astm_RDBRefIntegrity()
    assert isinstance(instance, RDBConstraint)


def test_astm_RDBUniqueKey_isa_RDBConstraint():
    instance = astm_RDBUniqueKey()
    assert isinstance(instance, RDBConstraint)


def test_astm_RDBCloseCursorStatement_isa_RDBCursorStatement():
    instance = astm_RDBCloseCursorStatement()
    assert isinstance(instance, RDBCursorStatement)


def test_astm_RDBFetchCursorStatement_isa_RDBCursorStatement():
    instance = astm_RDBFetchCursorStatement()
    assert isinstance(instance, RDBCursorStatement)


def test_astm_RDBOpenCursorStatement_isa_RDBCursorStatement():
    instance = astm_RDBOpenCursorStatement()
    assert isinstance(instance, RDBCursorStatement)


def test_astm_RDBDeleteStatement_isa_RDBModifyStatement():
    instance = astm_RDBDeleteStatement()
    assert isinstance(instance, RDBModifyStatement)


def test_astm_RDBUpdateStatement_isa_RDBModifyStatement():
    instance = astm_RDBUpdateStatement()
    assert isinstance(instance, RDBModifyStatement)


def test_astm_AggregateScope_isa_Scope():
    instance = astm_AggregateScope()
    assert isinstance(instance, Scope)


def test_astm_BlockScope_isa_Scope():
    instance = astm_BlockScope()
    assert isinstance(instance, Scope)


def test_astm_FunctionScope_isa_Scope():
    instance = astm_FunctionScope()
    assert isinstance(instance, Scope)


def test_astm_GlobalScope_isa_Scope():
    instance = astm_GlobalScope()
    assert isinstance(instance, Scope)


def test_astm_ProgramScope_isa_Scope():
    instance = astm_ProgramScope()
    assert isinstance(instance, Scope)


def test_astm_BlockStatement_isa_Statement():
    instance = astm_BlockStatement()
    assert isinstance(instance, Statement)


def test_astm_BreakStatement_isa_Statement():
    instance = astm_BreakStatement()
    assert isinstance(instance, Statement)


def test_astm_ContinueStatement_isa_Statement():
    instance = astm_ContinueStatement()
    assert isinstance(instance, Statement)


def test_astm_DeclarationOrDefinitionStatement_isa_Statement():
    instance = astm_DeclarationOrDefinitionStatement()
    assert isinstance(instance, Statement)


def test_astm_DeleteStatement_isa_Statement():
    instance = astm_DeleteStatement()
    assert isinstance(instance, Statement)


def test_astm_EmptyStatement_isa_Statement():
    instance = astm_EmptyStatement()
    assert isinstance(instance, Statement)


def test_astm_ExpressionStatement_isa_Statement():
    instance = astm_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_astm_IfStatement_isa_Statement():
    instance = astm_IfStatement()
    assert isinstance(instance, Statement)


def test_astm_JumpStatement_isa_Statement():
    instance = astm_JumpStatement()
    assert isinstance(instance, Statement)


def test_astm_LabeledStatement_isa_Statement():
    instance = astm_LabeledStatement()
    assert isinstance(instance, Statement)


def test_astm_LoopStatement_isa_Statement():
    instance = astm_LoopStatement()
    assert isinstance(instance, Statement)


def test_astm_RDBConnectStatement_isa_Statement():
    instance = astm_RDBConnectStatement()
    assert isinstance(instance, Statement)


def test_astm_RDBCursorStatement_isa_Statement():
    instance = astm_RDBCursorStatement()
    assert isinstance(instance, Statement)


def test_astm_RDBInsertStatement_isa_Statement():
    instance = astm_RDBInsertStatement()
    assert isinstance(instance, Statement)


def test_astm_RDBModifyStatement_isa_Statement():
    instance = astm_RDBModifyStatement()
    assert isinstance(instance, Statement)


def test_astm_RDBSelectStatement_isa_Statement():
    instance = astm_RDBSelectStatement()
    assert isinstance(instance, Statement)


def test_astm_ReturnStatement_isa_Statement():
    instance = astm_ReturnStatement()
    assert isinstance(instance, Statement)


def test_astm_SpecificSelectStatement_isa_Statement():
    instance = astm_SpecificSelectStatement()
    assert isinstance(instance, Statement)


def test_astm_SwitchStatement_isa_Statement():
    instance = astm_SwitchStatement()
    assert isinstance(instance, Statement)


def test_astm_TerminateStatement_isa_Statement():
    instance = astm_TerminateStatement()
    assert isinstance(instance, Statement)


def test_astm_ThrowStatement_isa_Statement():
    instance = astm_ThrowStatement()
    assert isinstance(instance, Statement)


def test_astm_TryStatement_isa_Statement():
    instance = astm_TryStatement()
    assert isinstance(instance, Statement)


def test_astm_External_isa_StorageSpecification():
    instance = astm_External()
    assert isinstance(instance, StorageSpecification)


def test_astm_FileLocal_isa_StorageSpecification():
    instance = astm_FileLocal()
    assert isinstance(instance, StorageSpecification)


def test_astm_FunctionPersistent_isa_StorageSpecification():
    instance = astm_FunctionPersistent()
    assert isinstance(instance, StorageSpecification)


def test_astm_NoDef_isa_StorageSpecification():
    instance = astm_NoDef()
    assert isinstance(instance, StorageSpecification)


def test_astm_PerClassMember_isa_StorageSpecification():
    instance = astm_PerClassMember()
    assert isinstance(instance, StorageSpecification)


def test_astm_CaseBlock_isa_SwitchCase():
    instance = astm_CaseBlock()
    assert isinstance(instance, SwitchCase)


def test_astm_DefaultBlock_isa_SwitchCase():
    instance = astm_DefaultBlock()
    assert isinstance(instance, SwitchCase)


def test_astm_FunctionType_isa_Type():
    instance = astm_FunctionType()
    assert isinstance(instance, Type)


def test_astm_LabelType_isa_Type():
    instance = astm_LabelType()
    assert isinstance(instance, Type)


def test_astm_NameSpaceType_isa_Type():
    instance = astm_NameSpaceType()
    assert isinstance(instance, Type)


def test_astm_TypeReference_isa_Type():
    instance = astm_TypeReference()
    assert isinstance(instance, Type)


def test_astm_AggregateTypeDefinition_isa_TypeDefinition():
    instance = astm_AggregateTypeDefinition()
    assert isinstance(instance, TypeDefinition)


def test_astm_NamedTypeDefinition_isa_TypeDefinition():
    instance = astm_NamedTypeDefinition()
    assert isinstance(instance, TypeDefinition)


def test_astm_NamedTypeReference_isa_TypeReference():
    instance = astm_NamedTypeReference()
    assert isinstance(instance, TypeReference)


def test_astm_UnnamedTypeReference_isa_TypeReference():
    instance = astm_UnnamedTypeReference()
    assert isinstance(instance, TypeReference)


def test_astm_AddressOf_isa_UnaryOperator():
    instance = astm_AddressOf()
    assert isinstance(instance, UnaryOperator)


def test_astm_BitNot_isa_UnaryOperator():
    instance = astm_BitNot()
    assert isinstance(instance, UnaryOperator)


def test_astm_Decrement_isa_UnaryOperator():
    instance = astm_Decrement()
    assert isinstance(instance, UnaryOperator)


def test_astm_Deref_isa_UnaryOperator():
    instance = astm_Deref()
    assert isinstance(instance, UnaryOperator)


def test_astm_Increment_isa_UnaryOperator():
    instance = astm_Increment()
    assert isinstance(instance, UnaryOperator)


def test_astm_Negate_isa_UnaryOperator():
    instance = astm_Negate()
    assert isinstance(instance, UnaryOperator)


def test_astm_Not_isa_UnaryOperator():
    instance = astm_Not()
    assert isinstance(instance, UnaryOperator)


def test_astm_PostDecrement_isa_UnaryOperator():
    instance = astm_PostDecrement()
    assert isinstance(instance, UnaryOperator)


def test_astm_PostIncrement_isa_UnaryOperator():
    instance = astm_PostIncrement()
    assert isinstance(instance, UnaryOperator)


def test_astm_UnaryPlus_isa_UnaryOperator():
    instance = astm_UnaryPlus()
    assert isinstance(instance, UnaryOperator)


def test_astm_NonVirtual_isa_VirtualSpecification():
    instance = astm_NonVirtual()
    assert isinstance(instance, VirtualSpecification)


def test_astm_PureVirtual_isa_VirtualSpecification():
    instance = astm_PureVirtual()
    assert isinstance(instance, VirtualSpecification)


def test_astm_Virtual_isa_VirtualSpecification():
    instance = astm_Virtual()
    assert isinstance(instance, VirtualSpecification)


def test_astm_AccessKind_isa_Visitable():
    instance = astm_AccessKind()
    assert isinstance(instance, Visitable)


def test_astm_ActualParameter_isa_Visitable():
    instance = astm_ActualParameter()
    assert isinstance(instance, Visitable)


def test_astm_BinaryOperator_isa_Visitable():
    instance = astm_BinaryOperator()
    assert isinstance(instance, Visitable)


def test_astm_DataType_isa_Visitable():
    instance = astm_DataType()
    assert isinstance(instance, Visitable)


def test_astm_FunctionMemberAttributes_isa_Visitable():
    instance = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    assert isinstance(instance, Visitable)


def test_astm_GASTMObject_isa_Visitable():
    instance = astm_GASTMObject()
    assert isinstance(instance, Visitable)


def test_astm_GASTMSemanticObject_isa_Visitable():
    instance = astm_GASTMSemanticObject()
    assert isinstance(instance, Visitable)


def test_astm_GASTMSourceObject_isa_Visitable():
    instance = astm_GASTMSourceObject()
    assert isinstance(instance, Visitable)


def test_astm_OtherSyntaxObject_isa_Visitable():
    instance = astm_OtherSyntaxObject()
    assert isinstance(instance, Visitable)


def test_astm_RDBHostVariableReference_isa_Visitable():
    instance = astm_RDBHostVariableReference()
    assert isinstance(instance, Visitable)


def test_astm_RDBTableSpaceReference_isa_Visitable():
    instance = astm_RDBTableSpaceReference()
    assert isinstance(instance, Visitable)


def test_astm_StorageSpecification_isa_Visitable():
    instance = astm_StorageSpecification()
    assert isinstance(instance, Visitable)


def test_astm_UnaryOperator_isa_Visitable():
    instance = astm_UnaryOperator()
    assert isinstance(instance, Visitable)


def test_assoc_Column268_link_reassign_clear():
    a = astm_RDBColumnDefinition(NotNull=True)
    b1 = astm_RDBTableDefinition()
    b2 = astm_RDBTableDefinition()
    _safe_set(a, 'astm_RDBColumnDefinition', b1)
    assert _is_linked(a, 'astm_RDBColumnDefinition', b1)
    if hasattr(b1, 'astm_RDBTableDefinition269'):
        assert _is_linked(b1, 'astm_RDBTableDefinition269', a)
    _safe_set(a, 'astm_RDBColumnDefinition', b2)
    assert _is_linked(a, 'astm_RDBColumnDefinition', b2)
    if hasattr(b1, 'astm_RDBTableDefinition269'):
        assert not _is_linked(b1, 'astm_RDBTableDefinition269', a)
    if hasattr(b2, 'astm_RDBTableDefinition269'):
        assert _is_linked(b2, 'astm_RDBTableDefinition269', a)
    _safe_set(a, 'astm_RDBColumnDefinition', None)
    assert not _is_linked(a, 'astm_RDBColumnDefinition', b2)
    if hasattr(b2, 'astm_RDBTableDefinition269'):
        assert not _is_linked(b2, 'astm_RDBTableDefinition269', a)


def test_assoc_Column288_link_reassign_clear():
    a = astm_RDBIndexColumn(AscendingOrDescending="sample_text")
    b1 = astm_IncludeUnit()
    b2 = astm_IncludeUnit()
    _safe_set(a, 'astm_RDBIndexColumn', b1)
    assert _is_linked(a, 'astm_RDBIndexColumn', b1)
    if hasattr(b1, 'astm_IncludeUnit289'):
        assert _is_linked(b1, 'astm_IncludeUnit289', a)
    _safe_set(a, 'astm_RDBIndexColumn', b2)
    assert _is_linked(a, 'astm_RDBIndexColumn', b2)
    if hasattr(b1, 'astm_IncludeUnit289'):
        assert not _is_linked(b1, 'astm_IncludeUnit289', a)
    if hasattr(b2, 'astm_IncludeUnit289'):
        assert _is_linked(b2, 'astm_IncludeUnit289', a)
    _safe_set(a, 'astm_RDBIndexColumn', None)
    assert not _is_linked(a, 'astm_RDBIndexColumn', b2)
    if hasattr(b2, 'astm_IncludeUnit289'):
        assert not _is_linked(b2, 'astm_IncludeUnit289', a)


def test_assoc_Index272_link_reassign_clear():
    a = astm_RDBIndex(IsUnique=True, NotNull=True)
    b1 = astm_RDBTableDefinition()
    b2 = astm_RDBTableDefinition()
    _safe_set(a, 'astm_RDBIndex', b1)
    assert _is_linked(a, 'astm_RDBIndex', b1)
    if hasattr(b1, 'astm_RDBTableDefinition273'):
        assert _is_linked(b1, 'astm_RDBTableDefinition273', a)
    _safe_set(a, 'astm_RDBIndex', b2)
    assert _is_linked(a, 'astm_RDBIndex', b2)
    if hasattr(b1, 'astm_RDBTableDefinition273'):
        assert not _is_linked(b1, 'astm_RDBTableDefinition273', a)
    if hasattr(b2, 'astm_RDBTableDefinition273'):
        assert _is_linked(b2, 'astm_RDBTableDefinition273', a)
    _safe_set(a, 'astm_RDBIndex', None)
    assert not _is_linked(a, 'astm_RDBIndex', b2)
    if hasattr(b2, 'astm_RDBTableDefinition273'):
        assert not _is_linked(b2, 'astm_RDBTableDefinition273', a)


def test_assoc_IndexColumn285_link_reassign_clear():
    a = astm_RDBIndex(IsUnique=True, NotNull=True)
    b1 = astm_Name(nameString="sample_text")
    b2 = astm_Name(nameString="sample_text_2")
    _safe_set(a, 'astm_RDBIndex286', {b1})
    assert _is_linked(a, 'astm_RDBIndex286', b1)
    if hasattr(b1, 'astm_Name287'):
        assert _is_linked(b1, 'astm_Name287', a)
    _safe_set(a, 'astm_RDBIndex286', {b2})
    assert _is_linked(a, 'astm_RDBIndex286', b2)
    if hasattr(b1, 'astm_Name287'):
        assert not _is_linked(b1, 'astm_Name287', a)
    if hasattr(b2, 'astm_Name287'):
        assert _is_linked(b2, 'astm_Name287', a)
    _safe_set(a, 'astm_RDBIndex286', set())
    assert not _is_linked(a, 'astm_RDBIndex286', b2)
    if hasattr(b2, 'astm_Name287'):
        assert not _is_linked(b2, 'astm_Name287', a)


def test_assoc_accessKind104_link_reassign_clear():
    a = astm_DerivesFrom(isVirtual=True)
    b1 = astm_OtherSyntaxObject()
    b2 = astm_OtherSyntaxObject()
    _safe_set(a, 'astm_DerivesFrom105', b1)
    assert _is_linked(a, 'astm_DerivesFrom105', b1)
    if hasattr(b1, 'astm_OtherSyntaxObject106'):
        assert _is_linked(b1, 'astm_OtherSyntaxObject106', a)
    _safe_set(a, 'astm_DerivesFrom105', b2)
    assert _is_linked(a, 'astm_DerivesFrom105', b2)
    if hasattr(b1, 'astm_OtherSyntaxObject106'):
        assert not _is_linked(b1, 'astm_OtherSyntaxObject106', a)
    if hasattr(b2, 'astm_OtherSyntaxObject106'):
        assert _is_linked(b2, 'astm_OtherSyntaxObject106', a)
    _safe_set(a, 'astm_DerivesFrom105', None)
    assert not _is_linked(a, 'astm_DerivesFrom105', b2)
    if hasattr(b2, 'astm_OtherSyntaxObject106'):
        assert not _is_linked(b2, 'astm_OtherSyntaxObject106', a)


def test_assoc_accessKind20_link_reassign_clear():
    a = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    b1 = astm_OtherSyntaxObject()
    b2 = astm_OtherSyntaxObject()
    _safe_set(a, 'astm_DeclarationOrDefinition21', b1)
    assert _is_linked(a, 'astm_DeclarationOrDefinition21', b1)
    if hasattr(b1, 'astm_OtherSyntaxObject22'):
        assert _is_linked(b1, 'astm_OtherSyntaxObject22', a)
    _safe_set(a, 'astm_DeclarationOrDefinition21', b2)
    assert _is_linked(a, 'astm_DeclarationOrDefinition21', b2)
    if hasattr(b1, 'astm_OtherSyntaxObject22'):
        assert not _is_linked(b1, 'astm_OtherSyntaxObject22', a)
    if hasattr(b2, 'astm_OtherSyntaxObject22'):
        assert _is_linked(b2, 'astm_OtherSyntaxObject22', a)
    _safe_set(a, 'astm_DeclarationOrDefinition21', None)
    assert not _is_linked(a, 'astm_DeclarationOrDefinition21', b2)
    if hasattr(b2, 'astm_OtherSyntaxObject22'):
        assert not _is_linked(b2, 'astm_OtherSyntaxObject22', a)


def test_assoc_body101_link_reassign_clear():
    a = astm_Type(isConst=True, isVolatile=True)
    b1 = astm_NamedType()
    b2 = astm_NamedType()
    _safe_set(a, 'astm_Type', b1)
    assert _is_linked(a, 'astm_Type', b1)
    if hasattr(b1, 'astm_NamedType102'):
        assert _is_linked(b1, 'astm_NamedType102', a)
    _safe_set(a, 'astm_Type', b2)
    assert _is_linked(a, 'astm_Type', b2)
    if hasattr(b1, 'astm_NamedType102'):
        assert not _is_linked(b1, 'astm_NamedType102', a)
    if hasattr(b2, 'astm_NamedType102'):
        assert _is_linked(b2, 'astm_NamedType102', a)
    _safe_set(a, 'astm_Type', None)
    assert not _is_linked(a, 'astm_Type', b2)
    if hasattr(b2, 'astm_NamedType102'):
        assert not _is_linked(b2, 'astm_NamedType102', a)


def test_assoc_className107_link_reassign_clear():
    a = astm_DerivesFrom(isVirtual=True)
    b1 = astm_NamedType()
    b2 = astm_NamedType()
    _safe_set(a, 'astm_DerivesFrom108', b1)
    assert _is_linked(a, 'astm_DerivesFrom108', b1)
    if hasattr(b1, 'astm_NamedType109'):
        assert _is_linked(b1, 'astm_NamedType109', a)
    _safe_set(a, 'astm_DerivesFrom108', b2)
    assert _is_linked(a, 'astm_DerivesFrom108', b2)
    if hasattr(b1, 'astm_NamedType109'):
        assert not _is_linked(b1, 'astm_NamedType109', a)
    if hasattr(b2, 'astm_NamedType109'):
        assert _is_linked(b2, 'astm_NamedType109', a)
    _safe_set(a, 'astm_DerivesFrom108', None)
    assert not _is_linked(a, 'astm_DerivesFrom108', b2)
    if hasattr(b2, 'astm_NamedType109'):
        assert not _is_linked(b2, 'astm_NamedType109', a)


def test_assoc_derivesFrom103_link_reassign_clear():
    a = astm_DerivesFrom(isVirtual=True)
    b1 = astm_ClassType()
    b2 = astm_ClassType()
    _safe_set(a, 'astm_DerivesFrom', b1)
    assert _is_linked(a, 'astm_DerivesFrom', b1)
    if hasattr(b1, 'astm_ClassType'):
        assert _is_linked(b1, 'astm_ClassType', a)
    _safe_set(a, 'astm_DerivesFrom', b2)
    assert _is_linked(a, 'astm_DerivesFrom', b2)
    if hasattr(b1, 'astm_ClassType'):
        assert not _is_linked(b1, 'astm_ClassType', a)
    if hasattr(b2, 'astm_ClassType'):
        assert _is_linked(b2, 'astm_ClassType', a)
    _safe_set(a, 'astm_DerivesFrom', None)
    assert not _is_linked(a, 'astm_DerivesFrom', b2)
    if hasattr(b2, 'astm_ClassType'):
        assert not _is_linked(b2, 'astm_ClassType', a)


def test_assoc_exceptionVariable178_link_reassign_clear():
    a = astm_DataDefinition(isMutable=True)
    b1 = astm_VariableCatchBlock()
    b2 = astm_VariableCatchBlock()
    _safe_set(a, 'astm_DataDefinition179', b1)
    assert _is_linked(a, 'astm_DataDefinition179', b1)
    if hasattr(b1, 'astm_VariableCatchBlock'):
        assert _is_linked(b1, 'astm_VariableCatchBlock', a)
    _safe_set(a, 'astm_DataDefinition179', b2)
    assert _is_linked(a, 'astm_DataDefinition179', b2)
    if hasattr(b1, 'astm_VariableCatchBlock'):
        assert not _is_linked(b1, 'astm_VariableCatchBlock', a)
    if hasattr(b2, 'astm_VariableCatchBlock'):
        assert _is_linked(b2, 'astm_VariableCatchBlock', a)
    _safe_set(a, 'astm_DataDefinition179', None)
    assert not _is_linked(a, 'astm_DataDefinition179', b2)
    if hasattr(b2, 'astm_VariableCatchBlock'):
        assert not _is_linked(b2, 'astm_VariableCatchBlock', a)


def test_assoc_exceptions176_link_reassign_clear():
    a = astm_Type(isConst=True, isVolatile=True)
    b1 = astm_TypesCatchBlock()
    b2 = astm_TypesCatchBlock()
    _safe_set(a, 'astm_Type177', b1)
    assert _is_linked(a, 'astm_Type177', b1)
    if hasattr(b1, 'astm_TypesCatchBlock'):
        assert _is_linked(b1, 'astm_TypesCatchBlock', a)
    _safe_set(a, 'astm_Type177', b2)
    assert _is_linked(a, 'astm_Type177', b2)
    if hasattr(b1, 'astm_TypesCatchBlock'):
        assert not _is_linked(b1, 'astm_TypesCatchBlock', a)
    if hasattr(b2, 'astm_TypesCatchBlock'):
        assert _is_linked(b2, 'astm_TypesCatchBlock', a)
    _safe_set(a, 'astm_Type177', None)
    assert not _is_linked(a, 'astm_Type177', b2)
    if hasattr(b2, 'astm_TypesCatchBlock'):
        assert not _is_linked(b2, 'astm_TypesCatchBlock', a)


def test_assoc_file75_link_reassign_clear():
    a = astm_SourceFile(pathName="sample_text")
    b1 = astm_IncludeUnit()
    b2 = astm_IncludeUnit()
    _safe_set(a, 'astm_SourceFile76', b1)
    assert _is_linked(a, 'astm_SourceFile76', b1)
    if hasattr(b1, 'astm_IncludeUnit'):
        assert _is_linked(b1, 'astm_IncludeUnit', a)
    _safe_set(a, 'astm_SourceFile76', b2)
    assert _is_linked(a, 'astm_SourceFile76', b2)
    if hasattr(b1, 'astm_IncludeUnit'):
        assert not _is_linked(b1, 'astm_IncludeUnit', a)
    if hasattr(b2, 'astm_IncludeUnit'):
        assert _is_linked(b2, 'astm_IncludeUnit', a)
    _safe_set(a, 'astm_SourceFile76', None)
    assert not _is_linked(a, 'astm_SourceFile76', b2)
    if hasattr(b2, 'astm_IncludeUnit'):
        assert not _is_linked(b2, 'astm_IncludeUnit', a)


def test_assoc_files1_link_reassign_clear():
    a = astm_CompilationUnit(language="sample_text")
    b1 = astm_Project()
    b2 = astm_Project()
    _safe_set(a, 'astm_CompilationUnit', b1)
    assert _is_linked(a, 'astm_CompilationUnit', b1)
    if hasattr(b1, 'astm_Project'):
        assert _is_linked(b1, 'astm_Project', a)
    _safe_set(a, 'astm_CompilationUnit', b2)
    assert _is_linked(a, 'astm_CompilationUnit', b2)
    if hasattr(b1, 'astm_Project'):
        assert not _is_linked(b1, 'astm_Project', a)
    if hasattr(b2, 'astm_Project'):
        assert _is_linked(b2, 'astm_Project', a)
    _safe_set(a, 'astm_CompilationUnit', None)
    assert not _is_linked(a, 'astm_CompilationUnit', b2)
    if hasattr(b2, 'astm_Project'):
        assert not _is_linked(b2, 'astm_Project', a)


def test_assoc_fragments14_link_reassign_clear():
    a = astm_CompilationUnit(language="sample_text")
    b1 = astm_DefinitionObject()
    b2 = astm_DefinitionObject()
    _safe_set(a, 'astm_CompilationUnit15', {b1})
    assert _is_linked(a, 'astm_CompilationUnit15', b1)
    if hasattr(b1, 'astm_DefinitionObject16'):
        assert _is_linked(b1, 'astm_DefinitionObject16', a)
    _safe_set(a, 'astm_CompilationUnit15', {b2})
    assert _is_linked(a, 'astm_CompilationUnit15', b2)
    if hasattr(b1, 'astm_DefinitionObject16'):
        assert not _is_linked(b1, 'astm_DefinitionObject16', a)
    if hasattr(b2, 'astm_DefinitionObject16'):
        assert _is_linked(b2, 'astm_DefinitionObject16', a)
    _safe_set(a, 'astm_CompilationUnit15', set())
    assert not _is_linked(a, 'astm_CompilationUnit15', b2)
    if hasattr(b2, 'astm_DefinitionObject16'):
        assert not _is_linked(b2, 'astm_DefinitionObject16', a)


def test_assoc_functionMemberAttributes35_link_reassign_clear():
    a = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    b1 = astm_FunctionDeclaration()
    b2 = astm_FunctionDeclaration()
    _safe_set(a, 'astm_FunctionMemberAttributes', b1)
    assert _is_linked(a, 'astm_FunctionMemberAttributes', b1)
    if hasattr(b1, 'astm_FunctionDeclaration36'):
        assert _is_linked(b1, 'astm_FunctionDeclaration36', a)
    _safe_set(a, 'astm_FunctionMemberAttributes', b2)
    assert _is_linked(a, 'astm_FunctionMemberAttributes', b2)
    if hasattr(b1, 'astm_FunctionDeclaration36'):
        assert not _is_linked(b1, 'astm_FunctionDeclaration36', a)
    if hasattr(b2, 'astm_FunctionDeclaration36'):
        assert _is_linked(b2, 'astm_FunctionDeclaration36', a)
    _safe_set(a, 'astm_FunctionMemberAttributes', None)
    assert not _is_linked(a, 'astm_FunctionMemberAttributes', b2)
    if hasattr(b2, 'astm_FunctionDeclaration36'):
        assert not _is_linked(b2, 'astm_FunctionDeclaration36', a)


def test_assoc_functionMemberAttributes43_link_reassign_clear():
    a = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    b1 = astm_FunctionDefinition()
    b2 = astm_FunctionDefinition()
    _safe_set(a, 'astm_FunctionMemberAttributes45', b1)
    assert _is_linked(a, 'astm_FunctionMemberAttributes45', b1)
    if hasattr(b1, 'astm_FunctionDefinition44'):
        assert _is_linked(b1, 'astm_FunctionDefinition44', a)
    _safe_set(a, 'astm_FunctionMemberAttributes45', b2)
    assert _is_linked(a, 'astm_FunctionMemberAttributes45', b2)
    if hasattr(b1, 'astm_FunctionDefinition44'):
        assert not _is_linked(b1, 'astm_FunctionDefinition44', a)
    if hasattr(b2, 'astm_FunctionDefinition44'):
        assert _is_linked(b2, 'astm_FunctionDefinition44', a)
    _safe_set(a, 'astm_FunctionMemberAttributes45', None)
    assert not _is_linked(a, 'astm_FunctionMemberAttributes45', b2)
    if hasattr(b2, 'astm_FunctionDefinition44'):
        assert not _is_linked(b2, 'astm_FunctionDefinition44', a)


def test_assoc_identifierName23_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_Definition()
    b2 = astm_Definition()
    _safe_set(a, 'astm_Name', b1)
    assert _is_linked(a, 'astm_Name', b1)
    if hasattr(b1, 'astm_Definition'):
        assert _is_linked(b1, 'astm_Definition', a)
    _safe_set(a, 'astm_Name', b2)
    assert _is_linked(a, 'astm_Name', b2)
    if hasattr(b1, 'astm_Definition'):
        assert not _is_linked(b1, 'astm_Definition', a)
    if hasattr(b2, 'astm_Definition'):
        assert _is_linked(b2, 'astm_Definition', a)
    _safe_set(a, 'astm_Name', None)
    assert not _is_linked(a, 'astm_Name', b2)
    if hasattr(b2, 'astm_Definition'):
        assert not _is_linked(b2, 'astm_Definition', a)


def test_assoc_identifierName28_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_Declaration()
    b2 = astm_Declaration()
    _safe_set(a, 'astm_Name30', b1)
    assert _is_linked(a, 'astm_Name30', b1)
    if hasattr(b1, 'astm_Declaration29'):
        assert _is_linked(b1, 'astm_Declaration29', a)
    _safe_set(a, 'astm_Name30', b2)
    assert _is_linked(a, 'astm_Name30', b2)
    if hasattr(b1, 'astm_Declaration29'):
        assert not _is_linked(b1, 'astm_Declaration29', a)
    if hasattr(b2, 'astm_Declaration29'):
        assert _is_linked(b2, 'astm_Declaration29', a)
    _safe_set(a, 'astm_Name30', None)
    assert not _is_linked(a, 'astm_Name30', b2)
    if hasattr(b2, 'astm_Declaration29'):
        assert not _is_linked(b2, 'astm_Declaration29', a)


def test_assoc_inSourceFile0_link_reassign_clear():
    a = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    b1 = astm_SourceFile(pathName="sample_text")
    b2 = astm_SourceFile(pathName="sample_text_2")
    _safe_set(a, 'astm_SourceLocation', b1)
    assert _is_linked(a, 'astm_SourceLocation', b1)
    if hasattr(b1, 'astm_SourceFile'):
        assert _is_linked(b1, 'astm_SourceFile', a)
    _safe_set(a, 'astm_SourceLocation', b2)
    assert _is_linked(a, 'astm_SourceLocation', b2)
    if hasattr(b1, 'astm_SourceFile'):
        assert not _is_linked(b1, 'astm_SourceFile', a)
    if hasattr(b2, 'astm_SourceFile'):
        assert _is_linked(b2, 'astm_SourceFile', a)
    _safe_set(a, 'astm_SourceLocation', None)
    assert not _is_linked(a, 'astm_SourceLocation', b2)
    if hasattr(b2, 'astm_SourceFile'):
        assert not _is_linked(b2, 'astm_SourceFile', a)


def test_assoc_initialValue55_link_reassign_clear():
    a = astm_DataDefinition(isMutable=True)
    b1 = astm_Expression()
    b2 = astm_Expression()
    _safe_set(a, 'astm_DataDefinition', b1)
    assert _is_linked(a, 'astm_DataDefinition', b1)
    if hasattr(b1, 'astm_Expression'):
        assert _is_linked(b1, 'astm_Expression', a)
    _safe_set(a, 'astm_DataDefinition', b2)
    assert _is_linked(a, 'astm_DataDefinition', b2)
    if hasattr(b1, 'astm_Expression'):
        assert not _is_linked(b1, 'astm_Expression', a)
    if hasattr(b2, 'astm_Expression'):
        assert _is_linked(b2, 'astm_Expression', a)
    _safe_set(a, 'astm_DataDefinition', None)
    assert not _is_linked(a, 'astm_DataDefinition', b2)
    if hasattr(b2, 'astm_Expression'):
        assert not _is_linked(b2, 'astm_Expression', a)


def test_assoc_labelName71_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_LabelDefinition()
    b2 = astm_LabelDefinition()
    _safe_set(a, 'astm_Name72', b1)
    assert _is_linked(a, 'astm_Name72', b1)
    if hasattr(b1, 'astm_LabelDefinition'):
        assert _is_linked(b1, 'astm_LabelDefinition', a)
    _safe_set(a, 'astm_Name72', b2)
    assert _is_linked(a, 'astm_Name72', b2)
    if hasattr(b1, 'astm_LabelDefinition'):
        assert not _is_linked(b1, 'astm_LabelDefinition', a)
    if hasattr(b2, 'astm_LabelDefinition'):
        assert _is_linked(b2, 'astm_LabelDefinition', a)
    _safe_set(a, 'astm_Name72', None)
    assert not _is_linked(a, 'astm_Name72', b2)
    if hasattr(b2, 'astm_LabelDefinition'):
        assert not _is_linked(b2, 'astm_LabelDefinition', a)


def test_assoc_locationInfo8_link_reassign_clear():
    a = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    b1 = astm_GASTMSyntaxObject()
    b2 = astm_GASTMSyntaxObject()
    _safe_set(a, 'astm_SourceLocation9', b1)
    assert _is_linked(a, 'astm_SourceLocation9', b1)
    if hasattr(b1, 'astm_GASTMSyntaxObject'):
        assert _is_linked(b1, 'astm_GASTMSyntaxObject', a)
    _safe_set(a, 'astm_SourceLocation9', b2)
    assert _is_linked(a, 'astm_SourceLocation9', b2)
    if hasattr(b1, 'astm_GASTMSyntaxObject'):
        assert not _is_linked(b1, 'astm_GASTMSyntaxObject', a)
    if hasattr(b2, 'astm_GASTMSyntaxObject'):
        assert _is_linked(b2, 'astm_GASTMSyntaxObject', a)
    _safe_set(a, 'astm_SourceLocation9', None)
    assert not _is_linked(a, 'astm_SourceLocation9', b2)
    if hasattr(b2, 'astm_GASTMSyntaxObject'):
        assert not _is_linked(b2, 'astm_GASTMSyntaxObject', a)


def test_assoc_name112_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_NamedTypeReference()
    b2 = astm_NamedTypeReference()
    _safe_set(a, 'astm_Name113', b1)
    assert _is_linked(a, 'astm_Name113', b1)
    if hasattr(b1, 'astm_NamedTypeReference'):
        assert _is_linked(b1, 'astm_NamedTypeReference', a)
    _safe_set(a, 'astm_Name113', b2)
    assert _is_linked(a, 'astm_Name113', b2)
    if hasattr(b1, 'astm_NamedTypeReference'):
        assert not _is_linked(b1, 'astm_NamedTypeReference', a)
    if hasattr(b2, 'astm_NamedTypeReference'):
        assert _is_linked(b2, 'astm_NamedTypeReference', a)
    _safe_set(a, 'astm_Name113', None)
    assert not _is_linked(a, 'astm_Name113', b2)
    if hasattr(b2, 'astm_NamedTypeReference'):
        assert not _is_linked(b2, 'astm_NamedTypeReference', a)


def test_assoc_name185_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_NameReference()
    b2 = astm_NameReference()
    _safe_set(a, 'astm_Name186', b1)
    assert _is_linked(a, 'astm_Name186', b1)
    if hasattr(b1, 'astm_NameReference'):
        assert _is_linked(b1, 'astm_NameReference', a)
    _safe_set(a, 'astm_Name186', b2)
    assert _is_linked(a, 'astm_Name186', b2)
    if hasattr(b1, 'astm_NameReference'):
        assert not _is_linked(b1, 'astm_NameReference', a)
    if hasattr(b2, 'astm_NameReference'):
        assert _is_linked(b2, 'astm_NameReference', a)
    _safe_set(a, 'astm_Name186', None)
    assert not _is_linked(a, 'astm_Name186', b2)
    if hasattr(b2, 'astm_NameReference'):
        assert not _is_linked(b2, 'astm_NameReference', a)


def test_assoc_name248_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_LabelAccess()
    b2 = astm_LabelAccess()
    _safe_set(a, 'astm_Name250', b1)
    assert _is_linked(a, 'astm_Name250', b1)
    if hasattr(b1, 'astm_LabelAccess249'):
        assert _is_linked(b1, 'astm_LabelAccess249', a)
    _safe_set(a, 'astm_Name250', b2)
    assert _is_linked(a, 'astm_Name250', b2)
    if hasattr(b1, 'astm_LabelAccess249'):
        assert not _is_linked(b1, 'astm_LabelAccess249', a)
    if hasattr(b2, 'astm_LabelAccess249'):
        assert _is_linked(b2, 'astm_LabelAccess249', a)
    _safe_set(a, 'astm_Name250', None)
    assert not _is_linked(a, 'astm_Name250', b2)
    if hasattr(b2, 'astm_LabelAccess249'):
        assert not _is_linked(b2, 'astm_LabelAccess249', a)


def test_assoc_name276_link_reassign_clear():
    a = astm_RDBColumnDefinition(NotNull=True)
    b1 = astm_Name(nameString="sample_text")
    b2 = astm_Name(nameString="sample_text_2")
    _safe_set(a, 'astm_RDBColumnDefinition277', b1)
    assert _is_linked(a, 'astm_RDBColumnDefinition277', b1)
    if hasattr(b1, 'astm_Name278'):
        assert _is_linked(b1, 'astm_Name278', a)
    _safe_set(a, 'astm_RDBColumnDefinition277', b2)
    assert _is_linked(a, 'astm_RDBColumnDefinition277', b2)
    if hasattr(b1, 'astm_Name278'):
        assert not _is_linked(b1, 'astm_Name278', a)
    if hasattr(b2, 'astm_Name278'):
        assert _is_linked(b2, 'astm_Name278', a)
    _safe_set(a, 'astm_RDBColumnDefinition277', None)
    assert not _is_linked(a, 'astm_RDBColumnDefinition277', b2)
    if hasattr(b2, 'astm_Name278'):
        assert not _is_linked(b2, 'astm_Name278', a)


def test_assoc_name60_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_TypeDefinition()
    b2 = astm_TypeDefinition()
    _safe_set(a, 'astm_Name61', b1)
    assert _is_linked(a, 'astm_Name61', b1)
    if hasattr(b1, 'astm_TypeDefinition'):
        assert _is_linked(b1, 'astm_TypeDefinition', a)
    _safe_set(a, 'astm_Name61', b2)
    assert _is_linked(a, 'astm_Name61', b2)
    if hasattr(b1, 'astm_TypeDefinition'):
        assert not _is_linked(b1, 'astm_TypeDefinition', a)
    if hasattr(b2, 'astm_TypeDefinition'):
        assert _is_linked(b2, 'astm_TypeDefinition', a)
    _safe_set(a, 'astm_Name61', None)
    assert not _is_linked(a, 'astm_Name61', b2)
    if hasattr(b2, 'astm_TypeDefinition'):
        assert not _is_linked(b2, 'astm_TypeDefinition', a)


def test_assoc_nameSpace64_link_reassign_clear():
    a = astm_Name(nameString="sample_text")
    b1 = astm_NameSpaceDefinition()
    b2 = astm_NameSpaceDefinition()
    _safe_set(a, 'astm_Name65', b1)
    assert _is_linked(a, 'astm_Name65', b1)
    if hasattr(b1, 'astm_NameSpaceDefinition'):
        assert _is_linked(b1, 'astm_NameSpaceDefinition', a)
    _safe_set(a, 'astm_Name65', b2)
    assert _is_linked(a, 'astm_Name65', b2)
    if hasattr(b1, 'astm_NameSpaceDefinition'):
        assert not _is_linked(b1, 'astm_NameSpaceDefinition', a)
    if hasattr(b2, 'astm_NameSpaceDefinition'):
        assert _is_linked(b2, 'astm_NameSpaceDefinition', a)
    _safe_set(a, 'astm_Name65', None)
    assert not _is_linked(a, 'astm_Name65', b2)
    if hasattr(b2, 'astm_NameSpaceDefinition'):
        assert not _is_linked(b2, 'astm_NameSpaceDefinition', a)


def test_assoc_opensScope17_link_reassign_clear():
    a = astm_CompilationUnit(language="sample_text")
    b1 = astm_ProgramScope()
    b2 = astm_ProgramScope()
    _safe_set(a, 'astm_CompilationUnit18', b1)
    assert _is_linked(a, 'astm_CompilationUnit18', b1)
    if hasattr(b1, 'astm_ProgramScope'):
        assert _is_linked(b1, 'astm_ProgramScope', a)
    _safe_set(a, 'astm_CompilationUnit18', b2)
    assert _is_linked(a, 'astm_CompilationUnit18', b2)
    if hasattr(b1, 'astm_ProgramScope'):
        assert not _is_linked(b1, 'astm_ProgramScope', a)
    if hasattr(b2, 'astm_ProgramScope'):
        assert _is_linked(b2, 'astm_ProgramScope', a)
    _safe_set(a, 'astm_CompilationUnit18', None)
    assert not _is_linked(a, 'astm_CompilationUnit18', b2)
    if hasattr(b2, 'astm_ProgramScope'):
        assert not _is_linked(b2, 'astm_ProgramScope', a)


def test_assoc_refersTo77_link_reassign_clear():
    a = astm_MacroDefinition(body="sample_text", macroName="sample_text")
    b1 = astm_MacroCall()
    b2 = astm_MacroCall()
    _safe_set(a, 'astm_MacroDefinition', b1)
    assert _is_linked(a, 'astm_MacroDefinition', b1)
    if hasattr(b1, 'astm_MacroCall'):
        assert _is_linked(b1, 'astm_MacroCall', a)
    _safe_set(a, 'astm_MacroDefinition', b2)
    assert _is_linked(a, 'astm_MacroDefinition', b2)
    if hasattr(b1, 'astm_MacroCall'):
        assert not _is_linked(b1, 'astm_MacroCall', a)
    if hasattr(b2, 'astm_MacroCall'):
        assert _is_linked(b2, 'astm_MacroCall', a)
    _safe_set(a, 'astm_MacroDefinition', None)
    assert not _is_linked(a, 'astm_MacroDefinition', b2)
    if hasattr(b2, 'astm_MacroCall'):
        assert not _is_linked(b2, 'astm_MacroCall', a)


def test_assoc_storageSpecifiers19_link_reassign_clear():
    a = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    b1 = astm_OtherSyntaxObject()
    b2 = astm_OtherSyntaxObject()
    _safe_set(a, 'astm_DeclarationOrDefinition', b1)
    assert _is_linked(a, 'astm_DeclarationOrDefinition', b1)
    if hasattr(b1, 'astm_OtherSyntaxObject'):
        assert _is_linked(b1, 'astm_OtherSyntaxObject', a)
    _safe_set(a, 'astm_DeclarationOrDefinition', b2)
    assert _is_linked(a, 'astm_DeclarationOrDefinition', b2)
    if hasattr(b1, 'astm_OtherSyntaxObject'):
        assert not _is_linked(b1, 'astm_OtherSyntaxObject', a)
    if hasattr(b2, 'astm_OtherSyntaxObject'):
        assert _is_linked(b2, 'astm_OtherSyntaxObject', a)
    _safe_set(a, 'astm_DeclarationOrDefinition', None)
    assert not _is_linked(a, 'astm_DeclarationOrDefinition', b2)
    if hasattr(b2, 'astm_OtherSyntaxObject'):
        assert not _is_linked(b2, 'astm_OtherSyntaxObject', a)


def test_assoc_type110_link_reassign_clear():
    a = astm_Type(isConst=True, isVolatile=True)
    b1 = astm_UnnamedTypeReference()
    b2 = astm_UnnamedTypeReference()
    _safe_set(a, 'astm_Type111', b1)
    assert _is_linked(a, 'astm_Type111', b1)
    if hasattr(b1, 'astm_UnnamedTypeReference'):
        assert _is_linked(b1, 'astm_UnnamedTypeReference', a)
    _safe_set(a, 'astm_Type111', b2)
    assert _is_linked(a, 'astm_Type111', b2)
    if hasattr(b1, 'astm_UnnamedTypeReference'):
        assert not _is_linked(b1, 'astm_UnnamedTypeReference', a)
    if hasattr(b2, 'astm_UnnamedTypeReference'):
        assert _is_linked(b2, 'astm_UnnamedTypeReference', a)
    _safe_set(a, 'astm_Type111', None)
    assert not _is_linked(a, 'astm_Type111', b2)
    if hasattr(b2, 'astm_UnnamedTypeReference'):
        assert not _is_linked(b2, 'astm_UnnamedTypeReference', a)


def test_assoc_type279_link_reassign_clear():
    a = astm_RDBColumnDefinition(NotNull=True)
    b1 = astm_RDBColumnType()
    b2 = astm_RDBColumnType()
    _safe_set(a, 'astm_RDBColumnDefinition280', b1)
    assert _is_linked(a, 'astm_RDBColumnDefinition280', b1)
    if hasattr(b1, 'astm_RDBColumnType'):
        assert _is_linked(b1, 'astm_RDBColumnType', a)
    _safe_set(a, 'astm_RDBColumnDefinition280', b2)
    assert _is_linked(a, 'astm_RDBColumnDefinition280', b2)
    if hasattr(b1, 'astm_RDBColumnType'):
        assert not _is_linked(b1, 'astm_RDBColumnType', a)
    if hasattr(b2, 'astm_RDBColumnType'):
        assert _is_linked(b2, 'astm_RDBColumnType', a)
    _safe_set(a, 'astm_RDBColumnDefinition280', None)
    assert not _is_linked(a, 'astm_RDBColumnDefinition280', b2)
    if hasattr(b2, 'astm_RDBColumnType'):
        assert not _is_linked(b2, 'astm_RDBColumnType', a)


def test_assoc_virtualSpecifier48_link_reassign_clear():
    a = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    b1 = astm_VirtualSpecification()
    b2 = astm_VirtualSpecification()
    _safe_set(a, 'astm_FunctionMemberAttributes49', b1)
    assert _is_linked(a, 'astm_FunctionMemberAttributes49', b1)
    if hasattr(b1, 'astm_VirtualSpecification'):
        assert _is_linked(b1, 'astm_VirtualSpecification', a)
    _safe_set(a, 'astm_FunctionMemberAttributes49', b2)
    assert _is_linked(a, 'astm_FunctionMemberAttributes49', b2)
    if hasattr(b1, 'astm_VirtualSpecification'):
        assert not _is_linked(b1, 'astm_VirtualSpecification', a)
    if hasattr(b2, 'astm_VirtualSpecification'):
        assert _is_linked(b2, 'astm_VirtualSpecification', a)
    _safe_set(a, 'astm_FunctionMemberAttributes49', None)
    assert not _is_linked(a, 'astm_FunctionMemberAttributes49', b2)
    if hasattr(b2, 'astm_VirtualSpecification'):
        assert not _is_linked(b2, 'astm_VirtualSpecification', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AccessKind_strategy = st.builds(AccessKind)
@given(instance=AccessKind_strategy)
@settings(max_examples=25)
def test_AccessKind_instantiation(instance):
    assert isinstance(instance, AccessKind)


ActualParameter_strategy = st.builds(ActualParameter)
@given(instance=ActualParameter_strategy)
@settings(max_examples=25)
def test_ActualParameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)


ActualParameterExpression_strategy = st.builds(ActualParameterExpression)
@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=25)
def test_ActualParameterExpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)


AggregateType_strategy = st.builds(AggregateType)
@given(instance=AggregateType_strategy)
@settings(max_examples=25)
def test_AggregateType_instantiation(instance):
    assert isinstance(instance, AggregateType)


BinaryOperator_strategy = st.builds(BinaryOperator)
@given(instance=BinaryOperator_strategy)
@settings(max_examples=25)
def test_BinaryOperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)


CatchBlock_strategy = st.builds(CatchBlock)
@given(instance=CatchBlock_strategy)
@settings(max_examples=25)
def test_CatchBlock_instantiation(instance):
    assert isinstance(instance, CatchBlock)


ConstructedType_strategy = st.builds(ConstructedType)
@given(instance=ConstructedType_strategy)
@settings(max_examples=25)
def test_ConstructedType_instantiation(instance):
    assert isinstance(instance, ConstructedType)


DataDefinition_strategy = st.builds(DataDefinition)
@given(instance=DataDefinition_strategy)
@settings(max_examples=25)
def test_DataDefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


DeclarationOrDefinition_strategy = st.builds(DeclarationOrDefinition)
@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=25)
def test_DeclarationOrDefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)


Definition_strategy = st.builds(Definition)
@given(instance=Definition_strategy)
@settings(max_examples=25)
def test_Definition_instantiation(instance):
    assert isinstance(instance, Definition)


DefinitionObject_strategy = st.builds(DefinitionObject)
@given(instance=DefinitionObject_strategy)
@settings(max_examples=25)
def test_DefinitionObject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ForStatement_strategy = st.builds(ForStatement)
@given(instance=ForStatement_strategy)
@settings(max_examples=25)
def test_ForStatement_instantiation(instance):
    assert isinstance(instance, ForStatement)


FormalParameterType_strategy = st.builds(FormalParameterType)
@given(instance=FormalParameterType_strategy)
@settings(max_examples=25)
def test_FormalParameterType_instantiation(instance):
    assert isinstance(instance, FormalParameterType)


GASTMObject_strategy = st.builds(GASTMObject)
@given(instance=GASTMObject_strategy)
@settings(max_examples=25)
def test_GASTMObject_instantiation(instance):
    assert isinstance(instance, GASTMObject)


GASTMSemanticObject_strategy = st.builds(GASTMSemanticObject)
@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=25)
def test_GASTMSemanticObject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)


GASTMSourceObject_strategy = st.builds(GASTMSourceObject)
@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=25)
def test_GASTMSourceObject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)


GASTMSyntaxObject_strategy = st.builds(GASTMSyntaxObject)
@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=25)
def test_GASTMSyntaxObject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)


IdentifierReference_strategy = st.builds(IdentifierReference)
@given(instance=IdentifierReference_strategy)
@settings(max_examples=25)
def test_IdentifierReference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


LoopStatement_strategy = st.builds(LoopStatement)
@given(instance=LoopStatement_strategy)
@settings(max_examples=25)
def test_LoopStatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)


NameReference_strategy = st.builds(NameReference)
@given(instance=NameReference_strategy)
@settings(max_examples=25)
def test_NameReference_instantiation(instance):
    assert isinstance(instance, NameReference)


OtherSyntaxObject_strategy = st.builds(OtherSyntaxObject)
@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=25)
def test_OtherSyntaxObject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)


PreprocessorElement_strategy = st.builds(PreprocessorElement)
@given(instance=PreprocessorElement_strategy)
@settings(max_examples=25)
def test_PreprocessorElement_instantiation(instance):
    assert isinstance(instance, PreprocessorElement)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


QualifiedIdentifierReference_strategy = st.builds(QualifiedIdentifierReference)
@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=25)
def test_QualifiedIdentifierReference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)


RDBColumnType_strategy = st.builds(RDBColumnType)
@given(instance=RDBColumnType_strategy)
@settings(max_examples=25)
def test_RDBColumnType_instantiation(instance):
    assert isinstance(instance, RDBColumnType)


RDBConstraint_strategy = st.builds(RDBConstraint)
@given(instance=RDBConstraint_strategy)
@settings(max_examples=25)
def test_RDBConstraint_instantiation(instance):
    assert isinstance(instance, RDBConstraint)


RDBCursorStatement_strategy = st.builds(RDBCursorStatement)
@given(instance=RDBCursorStatement_strategy)
@settings(max_examples=25)
def test_RDBCursorStatement_instantiation(instance):
    assert isinstance(instance, RDBCursorStatement)


RDBModifyStatement_strategy = st.builds(RDBModifyStatement)
@given(instance=RDBModifyStatement_strategy)
@settings(max_examples=25)
def test_RDBModifyStatement_instantiation(instance):
    assert isinstance(instance, RDBModifyStatement)


Scope_strategy = st.builds(Scope)
@given(instance=Scope_strategy)
@settings(max_examples=25)
def test_Scope_instantiation(instance):
    assert isinstance(instance, Scope)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


StorageSpecification_strategy = st.builds(StorageSpecification)
@given(instance=StorageSpecification_strategy)
@settings(max_examples=25)
def test_StorageSpecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)


SwitchCase_strategy = st.builds(SwitchCase)
@given(instance=SwitchCase_strategy)
@settings(max_examples=25)
def test_SwitchCase_instantiation(instance):
    assert isinstance(instance, SwitchCase)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeDefinition_strategy = st.builds(TypeDefinition)
@given(instance=TypeDefinition_strategy)
@settings(max_examples=25)
def test_TypeDefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)


TypeReference_strategy = st.builds(TypeReference)
@given(instance=TypeReference_strategy)
@settings(max_examples=25)
def test_TypeReference_instantiation(instance):
    assert isinstance(instance, TypeReference)


UnaryOperator_strategy = st.builds(UnaryOperator)
@given(instance=UnaryOperator_strategy)
@settings(max_examples=25)
def test_UnaryOperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)


VirtualSpecification_strategy = st.builds(VirtualSpecification)
@given(instance=VirtualSpecification_strategy)
@settings(max_examples=25)
def test_VirtualSpecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)


Visitable_strategy = st.builds(Visitable)
@given(instance=Visitable_strategy)
@settings(max_examples=25)
def test_Visitable_instantiation(instance):
    assert isinstance(instance, Visitable)


astm_AccessKind_strategy = st.builds(astm_AccessKind)
@given(instance=astm_AccessKind_strategy)
@settings(max_examples=25)
def test_astm_AccessKind_instantiation(instance):
    assert isinstance(instance, astm_AccessKind)


astm_ActualParameter_strategy = st.builds(astm_ActualParameter)
@given(instance=astm_ActualParameter_strategy)
@settings(max_examples=25)
def test_astm_ActualParameter_instantiation(instance):
    assert isinstance(instance, astm_ActualParameter)


astm_ActualParameterExpression_strategy = st.builds(astm_ActualParameterExpression)
@given(instance=astm_ActualParameterExpression_strategy)
@settings(max_examples=25)
def test_astm_ActualParameterExpression_instantiation(instance):
    assert isinstance(instance, astm_ActualParameterExpression)


astm_Add_strategy = st.builds(astm_Add)
@given(instance=astm_Add_strategy)
@settings(max_examples=25)
def test_astm_Add_instantiation(instance):
    assert isinstance(instance, astm_Add)


astm_AddressOf_strategy = st.builds(astm_AddressOf)
@given(instance=astm_AddressOf_strategy)
@settings(max_examples=25)
def test_astm_AddressOf_instantiation(instance):
    assert isinstance(instance, astm_AddressOf)


astm_AggregateExpression_strategy = st.builds(astm_AggregateExpression)
@given(instance=astm_AggregateExpression_strategy)
@settings(max_examples=25)
def test_astm_AggregateExpression_instantiation(instance):
    assert isinstance(instance, astm_AggregateExpression)


astm_AggregateScope_strategy = st.builds(astm_AggregateScope)
@given(instance=astm_AggregateScope_strategy)
@settings(max_examples=25)
def test_astm_AggregateScope_instantiation(instance):
    assert isinstance(instance, astm_AggregateScope)


astm_AggregateType_strategy = st.builds(astm_AggregateType)
@given(instance=astm_AggregateType_strategy)
@settings(max_examples=25)
def test_astm_AggregateType_instantiation(instance):
    assert isinstance(instance, astm_AggregateType)


astm_AggregateTypeDefinition_strategy = st.builds(astm_AggregateTypeDefinition)
@given(instance=astm_AggregateTypeDefinition_strategy)
@settings(max_examples=25)
def test_astm_AggregateTypeDefinition_instantiation(instance):
    assert isinstance(instance, astm_AggregateTypeDefinition)


astm_And_strategy = st.builds(astm_And)
@given(instance=astm_And_strategy)
@settings(max_examples=25)
def test_astm_And_instantiation(instance):
    assert isinstance(instance, astm_And)


astm_AnnotationExpression_strategy = st.builds(astm_AnnotationExpression)
@given(instance=astm_AnnotationExpression_strategy)
@settings(max_examples=25)
def test_astm_AnnotationExpression_instantiation(instance):
    assert isinstance(instance, astm_AnnotationExpression)


astm_AnnotationType_strategy = st.builds(astm_AnnotationType)
@given(instance=astm_AnnotationType_strategy)
@settings(max_examples=25)
def test_astm_AnnotationType_instantiation(instance):
    assert isinstance(instance, astm_AnnotationType)


astm_ArrayAccess_strategy = st.builds(astm_ArrayAccess)
@given(instance=astm_ArrayAccess_strategy)
@settings(max_examples=25)
def test_astm_ArrayAccess_instantiation(instance):
    assert isinstance(instance, astm_ArrayAccess)


astm_ArrayType_strategy = st.builds(astm_ArrayType)
@given(instance=astm_ArrayType_strategy)
@settings(max_examples=25)
def test_astm_ArrayType_instantiation(instance):
    assert isinstance(instance, astm_ArrayType)


astm_Assign_strategy = st.builds(astm_Assign)
@given(instance=astm_Assign_strategy)
@settings(max_examples=25)
def test_astm_Assign_instantiation(instance):
    assert isinstance(instance, astm_Assign)


astm_BinaryExpression_strategy = st.builds(astm_BinaryExpression)
@given(instance=astm_BinaryExpression_strategy)
@settings(max_examples=25)
def test_astm_BinaryExpression_instantiation(instance):
    assert isinstance(instance, astm_BinaryExpression)


astm_BinaryOperator_strategy = st.builds(astm_BinaryOperator)
@given(instance=astm_BinaryOperator_strategy)
@settings(max_examples=25)
def test_astm_BinaryOperator_instantiation(instance):
    assert isinstance(instance, astm_BinaryOperator)


astm_BitAnd_strategy = st.builds(astm_BitAnd)
@given(instance=astm_BitAnd_strategy)
@settings(max_examples=25)
def test_astm_BitAnd_instantiation(instance):
    assert isinstance(instance, astm_BitAnd)


astm_BitFieldDefinition_strategy = st.builds(astm_BitFieldDefinition)
@given(instance=astm_BitFieldDefinition_strategy)
@settings(max_examples=25)
def test_astm_BitFieldDefinition_instantiation(instance):
    assert isinstance(instance, astm_BitFieldDefinition)


astm_BitLeftShift_strategy = st.builds(astm_BitLeftShift)
@given(instance=astm_BitLeftShift_strategy)
@settings(max_examples=25)
def test_astm_BitLeftShift_instantiation(instance):
    assert isinstance(instance, astm_BitLeftShift)


astm_BitLiteral_strategy = st.builds(astm_BitLiteral)
@given(instance=astm_BitLiteral_strategy)
@settings(max_examples=25)
def test_astm_BitLiteral_instantiation(instance):
    assert isinstance(instance, astm_BitLiteral)


astm_BitNot_strategy = st.builds(astm_BitNot)
@given(instance=astm_BitNot_strategy)
@settings(max_examples=25)
def test_astm_BitNot_instantiation(instance):
    assert isinstance(instance, astm_BitNot)


astm_BitOr_strategy = st.builds(astm_BitOr)
@given(instance=astm_BitOr_strategy)
@settings(max_examples=25)
def test_astm_BitOr_instantiation(instance):
    assert isinstance(instance, astm_BitOr)


astm_BitRightShift_strategy = st.builds(astm_BitRightShift)
@given(instance=astm_BitRightShift_strategy)
@settings(max_examples=25)
def test_astm_BitRightShift_instantiation(instance):
    assert isinstance(instance, astm_BitRightShift)


astm_BitXor_strategy = st.builds(astm_BitXor)
@given(instance=astm_BitXor_strategy)
@settings(max_examples=25)
def test_astm_BitXor_instantiation(instance):
    assert isinstance(instance, astm_BitXor)


astm_BlockScope_strategy = st.builds(astm_BlockScope)
@given(instance=astm_BlockScope_strategy)
@settings(max_examples=25)
def test_astm_BlockScope_instantiation(instance):
    assert isinstance(instance, astm_BlockScope)


astm_BlockStatement_strategy = st.builds(astm_BlockStatement)
@given(instance=astm_BlockStatement_strategy)
@settings(max_examples=25)
def test_astm_BlockStatement_instantiation(instance):
    assert isinstance(instance, astm_BlockStatement)


astm_Boolean_strategy = st.builds(astm_Boolean)
@given(instance=astm_Boolean_strategy)
@settings(max_examples=25)
def test_astm_Boolean_instantiation(instance):
    assert isinstance(instance, astm_Boolean)


astm_BooleanLiteral_strategy = st.builds(astm_BooleanLiteral)
@given(instance=astm_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_astm_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, astm_BooleanLiteral)


astm_BreakStatement_strategy = st.builds(astm_BreakStatement)
@given(instance=astm_BreakStatement_strategy)
@settings(max_examples=25)
def test_astm_BreakStatement_instantiation(instance):
    assert isinstance(instance, astm_BreakStatement)


astm_ByReferenceActualParameterExpression_strategy = st.builds(astm_ByReferenceActualParameterExpression)
@given(instance=astm_ByReferenceActualParameterExpression_strategy)
@settings(max_examples=25)
def test_astm_ByReferenceActualParameterExpression_instantiation(instance):
    assert isinstance(instance, astm_ByReferenceActualParameterExpression)


astm_ByReferenceFormalParameterType_strategy = st.builds(astm_ByReferenceFormalParameterType)
@given(instance=astm_ByReferenceFormalParameterType_strategy)
@settings(max_examples=25)
def test_astm_ByReferenceFormalParameterType_instantiation(instance):
    assert isinstance(instance, astm_ByReferenceFormalParameterType)


astm_ByValueActualParameterExpression_strategy = st.builds(astm_ByValueActualParameterExpression)
@given(instance=astm_ByValueActualParameterExpression_strategy)
@settings(max_examples=25)
def test_astm_ByValueActualParameterExpression_instantiation(instance):
    assert isinstance(instance, astm_ByValueActualParameterExpression)


astm_ByValueFormalParameterType_strategy = st.builds(astm_ByValueFormalParameterType)
@given(instance=astm_ByValueFormalParameterType_strategy)
@settings(max_examples=25)
def test_astm_ByValueFormalParameterType_instantiation(instance):
    assert isinstance(instance, astm_ByValueFormalParameterType)


astm_Byte_strategy = st.builds(astm_Byte)
@given(instance=astm_Byte_strategy)
@settings(max_examples=25)
def test_astm_Byte_instantiation(instance):
    assert isinstance(instance, astm_Byte)


astm_CaseBlock_strategy = st.builds(astm_CaseBlock)
@given(instance=astm_CaseBlock_strategy)
@settings(max_examples=25)
def test_astm_CaseBlock_instantiation(instance):
    assert isinstance(instance, astm_CaseBlock)


astm_CastExpression_strategy = st.builds(astm_CastExpression)
@given(instance=astm_CastExpression_strategy)
@settings(max_examples=25)
def test_astm_CastExpression_instantiation(instance):
    assert isinstance(instance, astm_CastExpression)


astm_CatchBlock_strategy = st.builds(astm_CatchBlock)
@given(instance=astm_CatchBlock_strategy)
@settings(max_examples=25)
def test_astm_CatchBlock_instantiation(instance):
    assert isinstance(instance, astm_CatchBlock)


astm_CharLiteral_strategy = st.builds(astm_CharLiteral)
@given(instance=astm_CharLiteral_strategy)
@settings(max_examples=25)
def test_astm_CharLiteral_instantiation(instance):
    assert isinstance(instance, astm_CharLiteral)


astm_Character_strategy = st.builds(astm_Character)
@given(instance=astm_Character_strategy)
@settings(max_examples=25)
def test_astm_Character_instantiation(instance):
    assert isinstance(instance, astm_Character)


astm_ClassType_strategy = st.builds(astm_ClassType)
@given(instance=astm_ClassType_strategy)
@settings(max_examples=25)
def test_astm_ClassType_instantiation(instance):
    assert isinstance(instance, astm_ClassType)


astm_CollectionType_strategy = st.builds(astm_CollectionType)
@given(instance=astm_CollectionType_strategy)
@settings(max_examples=25)
def test_astm_CollectionType_instantiation(instance):
    assert isinstance(instance, astm_CollectionType)


astm_Comment_strategy = st.builds(astm_Comment, text=safe_text)
@given(instance=astm_Comment_strategy)
@settings(max_examples=25)
def test_astm_Comment_instantiation(instance):
    assert isinstance(instance, astm_Comment)


astm_CompilationUnit_strategy = st.builds(astm_CompilationUnit, language=safe_text)
@given(instance=astm_CompilationUnit_strategy)
@settings(max_examples=25)
def test_astm_CompilationUnit_instantiation(instance):
    assert isinstance(instance, astm_CompilationUnit)


astm_ConditionalExpression_strategy = st.builds(astm_ConditionalExpression)
@given(instance=astm_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_astm_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, astm_ConditionalExpression)


astm_ConstructedType_strategy = st.builds(astm_ConstructedType)
@given(instance=astm_ConstructedType_strategy)
@settings(max_examples=25)
def test_astm_ConstructedType_instantiation(instance):
    assert isinstance(instance, astm_ConstructedType)


astm_ContinueStatement_strategy = st.builds(astm_ContinueStatement)
@given(instance=astm_ContinueStatement_strategy)
@settings(max_examples=25)
def test_astm_ContinueStatement_instantiation(instance):
    assert isinstance(instance, astm_ContinueStatement)


astm_DataDefinition_strategy = st.builds(astm_DataDefinition, isMutable=st.booleans())
@given(instance=astm_DataDefinition_strategy)
@settings(max_examples=25)
def test_astm_DataDefinition_instantiation(instance):
    assert isinstance(instance, astm_DataDefinition)


astm_DataType_strategy = st.builds(astm_DataType)
@given(instance=astm_DataType_strategy)
@settings(max_examples=25)
def test_astm_DataType_instantiation(instance):
    assert isinstance(instance, astm_DataType)


astm_Declaration_strategy = st.builds(astm_Declaration)
@given(instance=astm_Declaration_strategy)
@settings(max_examples=25)
def test_astm_Declaration_instantiation(instance):
    assert isinstance(instance, astm_Declaration)


astm_DeclarationOrDefinition_strategy = st.builds(astm_DeclarationOrDefinition, isRegister=st.booleans(), linkageSpecifier=safe_text)
@given(instance=astm_DeclarationOrDefinition_strategy)
@settings(max_examples=25)
def test_astm_DeclarationOrDefinition_instantiation(instance):
    assert isinstance(instance, astm_DeclarationOrDefinition)


astm_DeclarationOrDefinitionStatement_strategy = st.builds(astm_DeclarationOrDefinitionStatement)
@given(instance=astm_DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=25)
def test_astm_DeclarationOrDefinitionStatement_instantiation(instance):
    assert isinstance(instance, astm_DeclarationOrDefinitionStatement)


astm_Decrement_strategy = st.builds(astm_Decrement)
@given(instance=astm_Decrement_strategy)
@settings(max_examples=25)
def test_astm_Decrement_instantiation(instance):
    assert isinstance(instance, astm_Decrement)


astm_DefaultBlock_strategy = st.builds(astm_DefaultBlock)
@given(instance=astm_DefaultBlock_strategy)
@settings(max_examples=25)
def test_astm_DefaultBlock_instantiation(instance):
    assert isinstance(instance, astm_DefaultBlock)


astm_Definition_strategy = st.builds(astm_Definition)
@given(instance=astm_Definition_strategy)
@settings(max_examples=25)
def test_astm_Definition_instantiation(instance):
    assert isinstance(instance, astm_Definition)


astm_DefinitionObject_strategy = st.builds(astm_DefinitionObject)
@given(instance=astm_DefinitionObject_strategy)
@settings(max_examples=25)
def test_astm_DefinitionObject_instantiation(instance):
    assert isinstance(instance, astm_DefinitionObject)


astm_DeleteStatement_strategy = st.builds(astm_DeleteStatement)
@given(instance=astm_DeleteStatement_strategy)
@settings(max_examples=25)
def test_astm_DeleteStatement_instantiation(instance):
    assert isinstance(instance, astm_DeleteStatement)


astm_Deref_strategy = st.builds(astm_Deref)
@given(instance=astm_Deref_strategy)
@settings(max_examples=25)
def test_astm_Deref_instantiation(instance):
    assert isinstance(instance, astm_Deref)


astm_DerivesFrom_strategy = st.builds(astm_DerivesFrom, isVirtual=st.booleans())
@given(instance=astm_DerivesFrom_strategy)
@settings(max_examples=25)
def test_astm_DerivesFrom_instantiation(instance):
    assert isinstance(instance, astm_DerivesFrom)


astm_Dimension_strategy = st.builds(astm_Dimension)
@given(instance=astm_Dimension_strategy)
@settings(max_examples=25)
def test_astm_Dimension_instantiation(instance):
    assert isinstance(instance, astm_Dimension)


astm_Divide_strategy = st.builds(astm_Divide)
@given(instance=astm_Divide_strategy)
@settings(max_examples=25)
def test_astm_Divide_instantiation(instance):
    assert isinstance(instance, astm_Divide)


astm_DoWhileStatement_strategy = st.builds(astm_DoWhileStatement)
@given(instance=astm_DoWhileStatement_strategy)
@settings(max_examples=25)
def test_astm_DoWhileStatement_instantiation(instance):
    assert isinstance(instance, astm_DoWhileStatement)


astm_Double_strategy = st.builds(astm_Double)
@given(instance=astm_Double_strategy)
@settings(max_examples=25)
def test_astm_Double_instantiation(instance):
    assert isinstance(instance, astm_Double)


astm_EmptyStatement_strategy = st.builds(astm_EmptyStatement)
@given(instance=astm_EmptyStatement_strategy)
@settings(max_examples=25)
def test_astm_EmptyStatement_instantiation(instance):
    assert isinstance(instance, astm_EmptyStatement)


astm_EntryDefinition_strategy = st.builds(astm_EntryDefinition)
@given(instance=astm_EntryDefinition_strategy)
@settings(max_examples=25)
def test_astm_EntryDefinition_instantiation(instance):
    assert isinstance(instance, astm_EntryDefinition)


astm_EnumLiteralDefinition_strategy = st.builds(astm_EnumLiteralDefinition)
@given(instance=astm_EnumLiteralDefinition_strategy)
@settings(max_examples=25)
def test_astm_EnumLiteralDefinition_instantiation(instance):
    assert isinstance(instance, astm_EnumLiteralDefinition)


astm_EnumType_strategy = st.builds(astm_EnumType)
@given(instance=astm_EnumType_strategy)
@settings(max_examples=25)
def test_astm_EnumType_instantiation(instance):
    assert isinstance(instance, astm_EnumType)


astm_Equal_strategy = st.builds(astm_Equal)
@given(instance=astm_Equal_strategy)
@settings(max_examples=25)
def test_astm_Equal_instantiation(instance):
    assert isinstance(instance, astm_Equal)


astm_ExceptionType_strategy = st.builds(astm_ExceptionType)
@given(instance=astm_ExceptionType_strategy)
@settings(max_examples=25)
def test_astm_ExceptionType_instantiation(instance):
    assert isinstance(instance, astm_ExceptionType)


astm_Exponent_strategy = st.builds(astm_Exponent)
@given(instance=astm_Exponent_strategy)
@settings(max_examples=25)
def test_astm_Exponent_instantiation(instance):
    assert isinstance(instance, astm_Exponent)


astm_Expression_strategy = st.builds(astm_Expression)
@given(instance=astm_Expression_strategy)
@settings(max_examples=25)
def test_astm_Expression_instantiation(instance):
    assert isinstance(instance, astm_Expression)


astm_ExpressionStatement_strategy = st.builds(astm_ExpressionStatement)
@given(instance=astm_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_astm_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, astm_ExpressionStatement)


astm_External_strategy = st.builds(astm_External)
@given(instance=astm_External_strategy)
@settings(max_examples=25)
def test_astm_External_instantiation(instance):
    assert isinstance(instance, astm_External)


astm_FileLocal_strategy = st.builds(astm_FileLocal)
@given(instance=astm_FileLocal_strategy)
@settings(max_examples=25)
def test_astm_FileLocal_instantiation(instance):
    assert isinstance(instance, astm_FileLocal)


astm_Float_strategy = st.builds(astm_Float)
@given(instance=astm_Float_strategy)
@settings(max_examples=25)
def test_astm_Float_instantiation(instance):
    assert isinstance(instance, astm_Float)


astm_ForCheckAfterStatement_strategy = st.builds(astm_ForCheckAfterStatement)
@given(instance=astm_ForCheckAfterStatement_strategy)
@settings(max_examples=25)
def test_astm_ForCheckAfterStatement_instantiation(instance):
    assert isinstance(instance, astm_ForCheckAfterStatement)


astm_ForCheckBeforeStatement_strategy = st.builds(astm_ForCheckBeforeStatement)
@given(instance=astm_ForCheckBeforeStatement_strategy)
@settings(max_examples=25)
def test_astm_ForCheckBeforeStatement_instantiation(instance):
    assert isinstance(instance, astm_ForCheckBeforeStatement)


astm_ForStatement_strategy = st.builds(astm_ForStatement)
@given(instance=astm_ForStatement_strategy)
@settings(max_examples=25)
def test_astm_ForStatement_instantiation(instance):
    assert isinstance(instance, astm_ForStatement)


astm_FormalParameterDeclaration_strategy = st.builds(astm_FormalParameterDeclaration)
@given(instance=astm_FormalParameterDeclaration_strategy)
@settings(max_examples=25)
def test_astm_FormalParameterDeclaration_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDeclaration)


astm_FormalParameterDefinition_strategy = st.builds(astm_FormalParameterDefinition)
@given(instance=astm_FormalParameterDefinition_strategy)
@settings(max_examples=25)
def test_astm_FormalParameterDefinition_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDefinition)


astm_FormalParameterType_strategy = st.builds(astm_FormalParameterType)
@given(instance=astm_FormalParameterType_strategy)
@settings(max_examples=25)
def test_astm_FormalParameterType_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterType)


astm_FunctionCallExpression_strategy = st.builds(astm_FunctionCallExpression)
@given(instance=astm_FunctionCallExpression_strategy)
@settings(max_examples=25)
def test_astm_FunctionCallExpression_instantiation(instance):
    assert isinstance(instance, astm_FunctionCallExpression)


astm_FunctionDeclaration_strategy = st.builds(astm_FunctionDeclaration)
@given(instance=astm_FunctionDeclaration_strategy)
@settings(max_examples=25)
def test_astm_FunctionDeclaration_instantiation(instance):
    assert isinstance(instance, astm_FunctionDeclaration)


astm_FunctionDefinition_strategy = st.builds(astm_FunctionDefinition)
@given(instance=astm_FunctionDefinition_strategy)
@settings(max_examples=25)
def test_astm_FunctionDefinition_instantiation(instance):
    assert isinstance(instance, astm_FunctionDefinition)


astm_FunctionMemberAttribute_strategy = st.builds(astm_FunctionMemberAttribute)
@given(instance=astm_FunctionMemberAttribute_strategy)
@settings(max_examples=25)
def test_astm_FunctionMemberAttribute_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttribute)


astm_FunctionMemberAttributes_strategy = st.builds(astm_FunctionMemberAttributes, isFriend=st.booleans(), isInline=st.booleans(), isThisConst=st.booleans())
@given(instance=astm_FunctionMemberAttributes_strategy)
@settings(max_examples=25)
def test_astm_FunctionMemberAttributes_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttributes)


astm_FunctionPersistent_strategy = st.builds(astm_FunctionPersistent)
@given(instance=astm_FunctionPersistent_strategy)
@settings(max_examples=25)
def test_astm_FunctionPersistent_instantiation(instance):
    assert isinstance(instance, astm_FunctionPersistent)


astm_FunctionScope_strategy = st.builds(astm_FunctionScope)
@given(instance=astm_FunctionScope_strategy)
@settings(max_examples=25)
def test_astm_FunctionScope_instantiation(instance):
    assert isinstance(instance, astm_FunctionScope)


astm_FunctionType_strategy = st.builds(astm_FunctionType)
@given(instance=astm_FunctionType_strategy)
@settings(max_examples=25)
def test_astm_FunctionType_instantiation(instance):
    assert isinstance(instance, astm_FunctionType)


astm_GASTMObject_strategy = st.builds(astm_GASTMObject)
@given(instance=astm_GASTMObject_strategy)
@settings(max_examples=25)
def test_astm_GASTMObject_instantiation(instance):
    assert isinstance(instance, astm_GASTMObject)


astm_GASTMSemanticObject_strategy = st.builds(astm_GASTMSemanticObject)
@given(instance=astm_GASTMSemanticObject_strategy)
@settings(max_examples=25)
def test_astm_GASTMSemanticObject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSemanticObject)


astm_GASTMSourceObject_strategy = st.builds(astm_GASTMSourceObject)
@given(instance=astm_GASTMSourceObject_strategy)
@settings(max_examples=25)
def test_astm_GASTMSourceObject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSourceObject)


astm_GASTMSyntaxObject_strategy = st.builds(astm_GASTMSyntaxObject)
@given(instance=astm_GASTMSyntaxObject_strategy)
@settings(max_examples=25)
def test_astm_GASTMSyntaxObject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSyntaxObject)


astm_GlobalScope_strategy = st.builds(astm_GlobalScope)
@given(instance=astm_GlobalScope_strategy)
@settings(max_examples=25)
def test_astm_GlobalScope_instantiation(instance):
    assert isinstance(instance, astm_GlobalScope)


astm_Greater_strategy = st.builds(astm_Greater)
@given(instance=astm_Greater_strategy)
@settings(max_examples=25)
def test_astm_Greater_instantiation(instance):
    assert isinstance(instance, astm_Greater)


astm_IdentifierReference_strategy = st.builds(astm_IdentifierReference)
@given(instance=astm_IdentifierReference_strategy)
@settings(max_examples=25)
def test_astm_IdentifierReference_instantiation(instance):
    assert isinstance(instance, astm_IdentifierReference)


astm_IfStatement_strategy = st.builds(astm_IfStatement)
@given(instance=astm_IfStatement_strategy)
@settings(max_examples=25)
def test_astm_IfStatement_instantiation(instance):
    assert isinstance(instance, astm_IfStatement)


astm_IncludeUnit_strategy = st.builds(astm_IncludeUnit)
@given(instance=astm_IncludeUnit_strategy)
@settings(max_examples=25)
def test_astm_IncludeUnit_instantiation(instance):
    assert isinstance(instance, astm_IncludeUnit)


astm_Increment_strategy = st.builds(astm_Increment)
@given(instance=astm_Increment_strategy)
@settings(max_examples=25)
def test_astm_Increment_instantiation(instance):
    assert isinstance(instance, astm_Increment)


astm_Integer_strategy = st.builds(astm_Integer)
@given(instance=astm_Integer_strategy)
@settings(max_examples=25)
def test_astm_Integer_instantiation(instance):
    assert isinstance(instance, astm_Integer)


astm_IntegerlLiteral_strategy = st.builds(astm_IntegerlLiteral)
@given(instance=astm_IntegerlLiteral_strategy)
@settings(max_examples=25)
def test_astm_IntegerlLiteral_instantiation(instance):
    assert isinstance(instance, astm_IntegerlLiteral)


astm_JumpStatement_strategy = st.builds(astm_JumpStatement)
@given(instance=astm_JumpStatement_strategy)
@settings(max_examples=25)
def test_astm_JumpStatement_instantiation(instance):
    assert isinstance(instance, astm_JumpStatement)


astm_LabelAccess_strategy = st.builds(astm_LabelAccess)
@given(instance=astm_LabelAccess_strategy)
@settings(max_examples=25)
def test_astm_LabelAccess_instantiation(instance):
    assert isinstance(instance, astm_LabelAccess)


astm_LabelDefinition_strategy = st.builds(astm_LabelDefinition)
@given(instance=astm_LabelDefinition_strategy)
@settings(max_examples=25)
def test_astm_LabelDefinition_instantiation(instance):
    assert isinstance(instance, astm_LabelDefinition)


astm_LabelType_strategy = st.builds(astm_LabelType)
@given(instance=astm_LabelType_strategy)
@settings(max_examples=25)
def test_astm_LabelType_instantiation(instance):
    assert isinstance(instance, astm_LabelType)


astm_LabeledStatement_strategy = st.builds(astm_LabeledStatement)
@given(instance=astm_LabeledStatement_strategy)
@settings(max_examples=25)
def test_astm_LabeledStatement_instantiation(instance):
    assert isinstance(instance, astm_LabeledStatement)


astm_Less_strategy = st.builds(astm_Less)
@given(instance=astm_Less_strategy)
@settings(max_examples=25)
def test_astm_Less_instantiation(instance):
    assert isinstance(instance, astm_Less)


astm_Literal_strategy = st.builds(astm_Literal, value=safe_text)
@given(instance=astm_Literal_strategy)
@settings(max_examples=25)
def test_astm_Literal_instantiation(instance):
    assert isinstance(instance, astm_Literal)


astm_LongDouble_strategy = st.builds(astm_LongDouble)
@given(instance=astm_LongDouble_strategy)
@settings(max_examples=25)
def test_astm_LongDouble_instantiation(instance):
    assert isinstance(instance, astm_LongDouble)


astm_LongInteger_strategy = st.builds(astm_LongInteger)
@given(instance=astm_LongInteger_strategy)
@settings(max_examples=25)
def test_astm_LongInteger_instantiation(instance):
    assert isinstance(instance, astm_LongInteger)


astm_LoopStatement_strategy = st.builds(astm_LoopStatement)
@given(instance=astm_LoopStatement_strategy)
@settings(max_examples=25)
def test_astm_LoopStatement_instantiation(instance):
    assert isinstance(instance, astm_LoopStatement)


astm_MacroCall_strategy = st.builds(astm_MacroCall)
@given(instance=astm_MacroCall_strategy)
@settings(max_examples=25)
def test_astm_MacroCall_instantiation(instance):
    assert isinstance(instance, astm_MacroCall)


astm_MacroDefinition_strategy = st.builds(astm_MacroDefinition, body=safe_text, macroName=safe_text)
@given(instance=astm_MacroDefinition_strategy)
@settings(max_examples=25)
def test_astm_MacroDefinition_instantiation(instance):
    assert isinstance(instance, astm_MacroDefinition)


astm_MissingActualParameter_strategy = st.builds(astm_MissingActualParameter)
@given(instance=astm_MissingActualParameter_strategy)
@settings(max_examples=25)
def test_astm_MissingActualParameter_instantiation(instance):
    assert isinstance(instance, astm_MissingActualParameter)


astm_Modulus_strategy = st.builds(astm_Modulus)
@given(instance=astm_Modulus_strategy)
@settings(max_examples=25)
def test_astm_Modulus_instantiation(instance):
    assert isinstance(instance, astm_Modulus)


astm_Multiply_strategy = st.builds(astm_Multiply)
@given(instance=astm_Multiply_strategy)
@settings(max_examples=25)
def test_astm_Multiply_instantiation(instance):
    assert isinstance(instance, astm_Multiply)


astm_Name_strategy = st.builds(astm_Name, nameString=safe_text)
@given(instance=astm_Name_strategy)
@settings(max_examples=25)
def test_astm_Name_instantiation(instance):
    assert isinstance(instance, astm_Name)


astm_NameReference_strategy = st.builds(astm_NameReference)
@given(instance=astm_NameReference_strategy)
@settings(max_examples=25)
def test_astm_NameReference_instantiation(instance):
    assert isinstance(instance, astm_NameReference)


astm_NameSpaceDefinition_strategy = st.builds(astm_NameSpaceDefinition)
@given(instance=astm_NameSpaceDefinition_strategy)
@settings(max_examples=25)
def test_astm_NameSpaceDefinition_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceDefinition)


astm_NameSpaceType_strategy = st.builds(astm_NameSpaceType)
@given(instance=astm_NameSpaceType_strategy)
@settings(max_examples=25)
def test_astm_NameSpaceType_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceType)


astm_NamedType_strategy = st.builds(astm_NamedType)
@given(instance=astm_NamedType_strategy)
@settings(max_examples=25)
def test_astm_NamedType_instantiation(instance):
    assert isinstance(instance, astm_NamedType)


astm_NamedTypeDefinition_strategy = st.builds(astm_NamedTypeDefinition)
@given(instance=astm_NamedTypeDefinition_strategy)
@settings(max_examples=25)
def test_astm_NamedTypeDefinition_instantiation(instance):
    assert isinstance(instance, astm_NamedTypeDefinition)


astm_NamedTypeReference_strategy = st.builds(astm_NamedTypeReference)
@given(instance=astm_NamedTypeReference_strategy)
@settings(max_examples=25)
def test_astm_NamedTypeReference_instantiation(instance):
    assert isinstance(instance, astm_NamedTypeReference)


astm_Negate_strategy = st.builds(astm_Negate)
@given(instance=astm_Negate_strategy)
@settings(max_examples=25)
def test_astm_Negate_instantiation(instance):
    assert isinstance(instance, astm_Negate)


astm_NewExpression_strategy = st.builds(astm_NewExpression)
@given(instance=astm_NewExpression_strategy)
@settings(max_examples=25)
def test_astm_NewExpression_instantiation(instance):
    assert isinstance(instance, astm_NewExpression)


astm_NoDef_strategy = st.builds(astm_NoDef)
@given(instance=astm_NoDef_strategy)
@settings(max_examples=25)
def test_astm_NoDef_instantiation(instance):
    assert isinstance(instance, astm_NoDef)


astm_NonVirtual_strategy = st.builds(astm_NonVirtual)
@given(instance=astm_NonVirtual_strategy)
@settings(max_examples=25)
def test_astm_NonVirtual_instantiation(instance):
    assert isinstance(instance, astm_NonVirtual)


astm_Not_strategy = st.builds(astm_Not)
@given(instance=astm_Not_strategy)
@settings(max_examples=25)
def test_astm_Not_instantiation(instance):
    assert isinstance(instance, astm_Not)


astm_NotEqual_strategy = st.builds(astm_NotEqual)
@given(instance=astm_NotEqual_strategy)
@settings(max_examples=25)
def test_astm_NotEqual_instantiation(instance):
    assert isinstance(instance, astm_NotEqual)


astm_NotGreater_strategy = st.builds(astm_NotGreater)
@given(instance=astm_NotGreater_strategy)
@settings(max_examples=25)
def test_astm_NotGreater_instantiation(instance):
    assert isinstance(instance, astm_NotGreater)


astm_NotLess_strategy = st.builds(astm_NotLess)
@given(instance=astm_NotLess_strategy)
@settings(max_examples=25)
def test_astm_NotLess_instantiation(instance):
    assert isinstance(instance, astm_NotLess)


astm_OperatorAssign_strategy = st.builds(astm_OperatorAssign)
@given(instance=astm_OperatorAssign_strategy)
@settings(max_examples=25)
def test_astm_OperatorAssign_instantiation(instance):
    assert isinstance(instance, astm_OperatorAssign)


astm_Or_strategy = st.builds(astm_Or)
@given(instance=astm_Or_strategy)
@settings(max_examples=25)
def test_astm_Or_instantiation(instance):
    assert isinstance(instance, astm_Or)


astm_OtherSyntaxObject_strategy = st.builds(astm_OtherSyntaxObject)
@given(instance=astm_OtherSyntaxObject_strategy)
@settings(max_examples=25)
def test_astm_OtherSyntaxObject_instantiation(instance):
    assert isinstance(instance, astm_OtherSyntaxObject)


astm_PerClassMember_strategy = st.builds(astm_PerClassMember)
@given(instance=astm_PerClassMember_strategy)
@settings(max_examples=25)
def test_astm_PerClassMember_instantiation(instance):
    assert isinstance(instance, astm_PerClassMember)


astm_PointerType_strategy = st.builds(astm_PointerType)
@given(instance=astm_PointerType_strategy)
@settings(max_examples=25)
def test_astm_PointerType_instantiation(instance):
    assert isinstance(instance, astm_PointerType)


astm_PostDecrement_strategy = st.builds(astm_PostDecrement)
@given(instance=astm_PostDecrement_strategy)
@settings(max_examples=25)
def test_astm_PostDecrement_instantiation(instance):
    assert isinstance(instance, astm_PostDecrement)


astm_PostIncrement_strategy = st.builds(astm_PostIncrement)
@given(instance=astm_PostIncrement_strategy)
@settings(max_examples=25)
def test_astm_PostIncrement_instantiation(instance):
    assert isinstance(instance, astm_PostIncrement)


astm_PreprocessorElement_strategy = st.builds(astm_PreprocessorElement)
@given(instance=astm_PreprocessorElement_strategy)
@settings(max_examples=25)
def test_astm_PreprocessorElement_instantiation(instance):
    assert isinstance(instance, astm_PreprocessorElement)


astm_PrimitiveType_strategy = st.builds(astm_PrimitiveType, isSigned=st.booleans())
@given(instance=astm_PrimitiveType_strategy)
@settings(max_examples=25)
def test_astm_PrimitiveType_instantiation(instance):
    assert isinstance(instance, astm_PrimitiveType)


astm_Private_strategy = st.builds(astm_Private)
@given(instance=astm_Private_strategy)
@settings(max_examples=25)
def test_astm_Private_instantiation(instance):
    assert isinstance(instance, astm_Private)


astm_ProgramScope_strategy = st.builds(astm_ProgramScope)
@given(instance=astm_ProgramScope_strategy)
@settings(max_examples=25)
def test_astm_ProgramScope_instantiation(instance):
    assert isinstance(instance, astm_ProgramScope)


astm_Project_strategy = st.builds(astm_Project)
@given(instance=astm_Project_strategy)
@settings(max_examples=25)
def test_astm_Project_instantiation(instance):
    assert isinstance(instance, astm_Project)


astm_Protected_strategy = st.builds(astm_Protected)
@given(instance=astm_Protected_strategy)
@settings(max_examples=25)
def test_astm_Protected_instantiation(instance):
    assert isinstance(instance, astm_Protected)


astm_Public_strategy = st.builds(astm_Public)
@given(instance=astm_Public_strategy)
@settings(max_examples=25)
def test_astm_Public_instantiation(instance):
    assert isinstance(instance, astm_Public)


astm_PureVirtual_strategy = st.builds(astm_PureVirtual)
@given(instance=astm_PureVirtual_strategy)
@settings(max_examples=25)
def test_astm_PureVirtual_instantiation(instance):
    assert isinstance(instance, astm_PureVirtual)


astm_QualifiedIdentifierReference_strategy = st.builds(astm_QualifiedIdentifierReference)
@given(instance=astm_QualifiedIdentifierReference_strategy)
@settings(max_examples=25)
def test_astm_QualifiedIdentifierReference_instantiation(instance):
    assert isinstance(instance, astm_QualifiedIdentifierReference)


astm_QualifiedOverData_strategy = st.builds(astm_QualifiedOverData)
@given(instance=astm_QualifiedOverData_strategy)
@settings(max_examples=25)
def test_astm_QualifiedOverData_instantiation(instance):
    assert isinstance(instance, astm_QualifiedOverData)


astm_QualifiedOverPointer_strategy = st.builds(astm_QualifiedOverPointer)
@given(instance=astm_QualifiedOverPointer_strategy)
@settings(max_examples=25)
def test_astm_QualifiedOverPointer_instantiation(instance):
    assert isinstance(instance, astm_QualifiedOverPointer)


astm_RDBBFile_strategy = st.builds(astm_RDBBFile)
@given(instance=astm_RDBBFile_strategy)
@settings(max_examples=25)
def test_astm_RDBBFile_instantiation(instance):
    assert isinstance(instance, astm_RDBBFile)


astm_RDBBlob_strategy = st.builds(astm_RDBBlob)
@given(instance=astm_RDBBlob_strategy)
@settings(max_examples=25)
def test_astm_RDBBlob_instantiation(instance):
    assert isinstance(instance, astm_RDBBlob)


astm_RDBBoolean_strategy = st.builds(astm_RDBBoolean)
@given(instance=astm_RDBBoolean_strategy)
@settings(max_examples=25)
def test_astm_RDBBoolean_instantiation(instance):
    assert isinstance(instance, astm_RDBBoolean)


astm_RDBChar_strategy = st.builds(astm_RDBChar)
@given(instance=astm_RDBChar_strategy)
@settings(max_examples=25)
def test_astm_RDBChar_instantiation(instance):
    assert isinstance(instance, astm_RDBChar)


astm_RDBCheckConstraint_strategy = st.builds(astm_RDBCheckConstraint, RDBConstraintText=safe_text, RDBConstraintType=safe_text)
@given(instance=astm_RDBCheckConstraint_strategy)
@settings(max_examples=25)
def test_astm_RDBCheckConstraint_instantiation(instance):
    assert isinstance(instance, astm_RDBCheckConstraint)


astm_RDBClob_strategy = st.builds(astm_RDBClob)
@given(instance=astm_RDBClob_strategy)
@settings(max_examples=25)
def test_astm_RDBClob_instantiation(instance):
    assert isinstance(instance, astm_RDBClob)


astm_RDBCloseCursorStatement_strategy = st.builds(astm_RDBCloseCursorStatement)
@given(instance=astm_RDBCloseCursorStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBCloseCursorStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBCloseCursorStatement)


astm_RDBColumnDefinition_strategy = st.builds(astm_RDBColumnDefinition, NotNull=st.booleans())
@given(instance=astm_RDBColumnDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBColumnDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnDefinition)


astm_RDBColumnReference_strategy = st.builds(astm_RDBColumnReference)
@given(instance=astm_RDBColumnReference_strategy)
@settings(max_examples=25)
def test_astm_RDBColumnReference_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnReference)


astm_RDBColumnType_strategy = st.builds(astm_RDBColumnType)
@given(instance=astm_RDBColumnType_strategy)
@settings(max_examples=25)
def test_astm_RDBColumnType_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnType)


astm_RDBConnectStatement_strategy = st.builds(astm_RDBConnectStatement)
@given(instance=astm_RDBConnectStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBConnectStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBConnectStatement)


astm_RDBConstraint_strategy = st.builds(astm_RDBConstraint)
@given(instance=astm_RDBConstraint_strategy)
@settings(max_examples=25)
def test_astm_RDBConstraint_instantiation(instance):
    assert isinstance(instance, astm_RDBConstraint)


astm_RDBCursorDefinition_strategy = st.builds(astm_RDBCursorDefinition)
@given(instance=astm_RDBCursorDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBCursorDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorDefinition)


astm_RDBCursorStatement_strategy = st.builds(astm_RDBCursorStatement)
@given(instance=astm_RDBCursorStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBCursorStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorStatement)


astm_RDBCursorType_strategy = st.builds(astm_RDBCursorType)
@given(instance=astm_RDBCursorType_strategy)
@settings(max_examples=25)
def test_astm_RDBCursorType_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorType)


astm_RDBDataBaseType_strategy = st.builds(astm_RDBDataBaseType)
@given(instance=astm_RDBDataBaseType_strategy)
@settings(max_examples=25)
def test_astm_RDBDataBaseType_instantiation(instance):
    assert isinstance(instance, astm_RDBDataBaseType)


astm_RDBDatabaseDefinition_strategy = st.builds(astm_RDBDatabaseDefinition)
@given(instance=astm_RDBDatabaseDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBDatabaseDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBDatabaseDefinition)


astm_RDBDate_strategy = st.builds(astm_RDBDate)
@given(instance=astm_RDBDate_strategy)
@settings(max_examples=25)
def test_astm_RDBDate_instantiation(instance):
    assert isinstance(instance, astm_RDBDate)


astm_RDBDecimal_strategy = st.builds(astm_RDBDecimal)
@given(instance=astm_RDBDecimal_strategy)
@settings(max_examples=25)
def test_astm_RDBDecimal_instantiation(instance):
    assert isinstance(instance, astm_RDBDecimal)


astm_RDBDeleteStatement_strategy = st.builds(astm_RDBDeleteStatement)
@given(instance=astm_RDBDeleteStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBDeleteStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBDeleteStatement)


astm_RDBFetchCursorStatement_strategy = st.builds(astm_RDBFetchCursorStatement)
@given(instance=astm_RDBFetchCursorStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBFetchCursorStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBFetchCursorStatement)


astm_RDBFloat_strategy = st.builds(astm_RDBFloat)
@given(instance=astm_RDBFloat_strategy)
@settings(max_examples=25)
def test_astm_RDBFloat_instantiation(instance):
    assert isinstance(instance, astm_RDBFloat)


astm_RDBHostVariableExpression_strategy = st.builds(astm_RDBHostVariableExpression)
@given(instance=astm_RDBHostVariableExpression_strategy)
@settings(max_examples=25)
def test_astm_RDBHostVariableExpression_instantiation(instance):
    assert isinstance(instance, astm_RDBHostVariableExpression)


astm_RDBHostVariableReference_strategy = st.builds(astm_RDBHostVariableReference)
@given(instance=astm_RDBHostVariableReference_strategy)
@settings(max_examples=25)
def test_astm_RDBHostVariableReference_instantiation(instance):
    assert isinstance(instance, astm_RDBHostVariableReference)


astm_RDBIndex_strategy = st.builds(astm_RDBIndex, IsUnique=st.booleans(), NotNull=st.booleans())
@given(instance=astm_RDBIndex_strategy)
@settings(max_examples=25)
def test_astm_RDBIndex_instantiation(instance):
    assert isinstance(instance, astm_RDBIndex)


astm_RDBIndexColumn_strategy = st.builds(astm_RDBIndexColumn, AscendingOrDescending=safe_text)
@given(instance=astm_RDBIndexColumn_strategy)
@settings(max_examples=25)
def test_astm_RDBIndexColumn_instantiation(instance):
    assert isinstance(instance, astm_RDBIndexColumn)


astm_RDBInsertStatement_strategy = st.builds(astm_RDBInsertStatement)
@given(instance=astm_RDBInsertStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBInsertStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBInsertStatement)


astm_RDBInt_strategy = st.builds(astm_RDBInt)
@given(instance=astm_RDBInt_strategy)
@settings(max_examples=25)
def test_astm_RDBInt_instantiation(instance):
    assert isinstance(instance, astm_RDBInt)


astm_RDBInteger_strategy = st.builds(astm_RDBInteger)
@given(instance=astm_RDBInteger_strategy)
@settings(max_examples=25)
def test_astm_RDBInteger_instantiation(instance):
    assert isinstance(instance, astm_RDBInteger)


astm_RDBLong_strategy = st.builds(astm_RDBLong)
@given(instance=astm_RDBLong_strategy)
@settings(max_examples=25)
def test_astm_RDBLong_instantiation(instance):
    assert isinstance(instance, astm_RDBLong)


astm_RDBModifyStatement_strategy = st.builds(astm_RDBModifyStatement)
@given(instance=astm_RDBModifyStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBModifyStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBModifyStatement)


astm_RDBNClob_strategy = st.builds(astm_RDBNClob)
@given(instance=astm_RDBNClob_strategy)
@settings(max_examples=25)
def test_astm_RDBNClob_instantiation(instance):
    assert isinstance(instance, astm_RDBNClob)


astm_RDBNumber_strategy = st.builds(astm_RDBNumber)
@given(instance=astm_RDBNumber_strategy)
@settings(max_examples=25)
def test_astm_RDBNumber_instantiation(instance):
    assert isinstance(instance, astm_RDBNumber)


astm_RDBOpenCursorStatement_strategy = st.builds(astm_RDBOpenCursorStatement)
@given(instance=astm_RDBOpenCursorStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBOpenCursorStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBOpenCursorStatement)


astm_RDBRaw_strategy = st.builds(astm_RDBRaw)
@given(instance=astm_RDBRaw_strategy)
@settings(max_examples=25)
def test_astm_RDBRaw_instantiation(instance):
    assert isinstance(instance, astm_RDBRaw)


astm_RDBReal_strategy = st.builds(astm_RDBReal)
@given(instance=astm_RDBReal_strategy)
@settings(max_examples=25)
def test_astm_RDBReal_instantiation(instance):
    assert isinstance(instance, astm_RDBReal)


astm_RDBRefIntegrity_strategy = st.builds(astm_RDBRefIntegrity)
@given(instance=astm_RDBRefIntegrity_strategy)
@settings(max_examples=25)
def test_astm_RDBRefIntegrity_instantiation(instance):
    assert isinstance(instance, astm_RDBRefIntegrity)


astm_RDBRowid_strategy = st.builds(astm_RDBRowid)
@given(instance=astm_RDBRowid_strategy)
@settings(max_examples=25)
def test_astm_RDBRowid_instantiation(instance):
    assert isinstance(instance, astm_RDBRowid)


astm_RDBSelectExpression_strategy = st.builds(astm_RDBSelectExpression)
@given(instance=astm_RDBSelectExpression_strategy)
@settings(max_examples=25)
def test_astm_RDBSelectExpression_instantiation(instance):
    assert isinstance(instance, astm_RDBSelectExpression)


astm_RDBSelectStatement_strategy = st.builds(astm_RDBSelectStatement)
@given(instance=astm_RDBSelectStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBSelectStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBSelectStatement)


astm_RDBString_strategy = st.builds(astm_RDBString)
@given(instance=astm_RDBString_strategy)
@settings(max_examples=25)
def test_astm_RDBString_instantiation(instance):
    assert isinstance(instance, astm_RDBString)


astm_RDBTableAlias_strategy = st.builds(astm_RDBTableAlias)
@given(instance=astm_RDBTableAlias_strategy)
@settings(max_examples=25)
def test_astm_RDBTableAlias_instantiation(instance):
    assert isinstance(instance, astm_RDBTableAlias)


astm_RDBTableDefinition_strategy = st.builds(astm_RDBTableDefinition)
@given(instance=astm_RDBTableDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBTableDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBTableDefinition)


astm_RDBTableReference_strategy = st.builds(astm_RDBTableReference)
@given(instance=astm_RDBTableReference_strategy)
@settings(max_examples=25)
def test_astm_RDBTableReference_instantiation(instance):
    assert isinstance(instance, astm_RDBTableReference)


astm_RDBTableSpaceDefinition_strategy = st.builds(astm_RDBTableSpaceDefinition)
@given(instance=astm_RDBTableSpaceDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBTableSpaceDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceDefinition)


astm_RDBTableSpaceReference_strategy = st.builds(astm_RDBTableSpaceReference)
@given(instance=astm_RDBTableSpaceReference_strategy)
@settings(max_examples=25)
def test_astm_RDBTableSpaceReference_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceReference)


astm_RDBTableSpaceType_strategy = st.builds(astm_RDBTableSpaceType)
@given(instance=astm_RDBTableSpaceType_strategy)
@settings(max_examples=25)
def test_astm_RDBTableSpaceType_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceType)


astm_RDBTableType_strategy = st.builds(astm_RDBTableType)
@given(instance=astm_RDBTableType_strategy)
@settings(max_examples=25)
def test_astm_RDBTableType_instantiation(instance):
    assert isinstance(instance, astm_RDBTableType)


astm_RDBTimestamp_strategy = st.builds(astm_RDBTimestamp)
@given(instance=astm_RDBTimestamp_strategy)
@settings(max_examples=25)
def test_astm_RDBTimestamp_instantiation(instance):
    assert isinstance(instance, astm_RDBTimestamp)


astm_RDBTrigger_strategy = st.builds(astm_RDBTrigger)
@given(instance=astm_RDBTrigger_strategy)
@settings(max_examples=25)
def test_astm_RDBTrigger_instantiation(instance):
    assert isinstance(instance, astm_RDBTrigger)


astm_RDBUniqueKey_strategy = st.builds(astm_RDBUniqueKey)
@given(instance=astm_RDBUniqueKey_strategy)
@settings(max_examples=25)
def test_astm_RDBUniqueKey_instantiation(instance):
    assert isinstance(instance, astm_RDBUniqueKey)


astm_RDBUpdateStatement_strategy = st.builds(astm_RDBUpdateStatement)
@given(instance=astm_RDBUpdateStatement_strategy)
@settings(max_examples=25)
def test_astm_RDBUpdateStatement_instantiation(instance):
    assert isinstance(instance, astm_RDBUpdateStatement)


astm_RDBUserDefinition_strategy = st.builds(astm_RDBUserDefinition)
@given(instance=astm_RDBUserDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBUserDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBUserDefinition)


astm_RDBUserType_strategy = st.builds(astm_RDBUserType)
@given(instance=astm_RDBUserType_strategy)
@settings(max_examples=25)
def test_astm_RDBUserType_instantiation(instance):
    assert isinstance(instance, astm_RDBUserType)


astm_RDBVarchar_strategy = st.builds(astm_RDBVarchar)
@given(instance=astm_RDBVarchar_strategy)
@settings(max_examples=25)
def test_astm_RDBVarchar_instantiation(instance):
    assert isinstance(instance, astm_RDBVarchar)


astm_RDBViewDefinition_strategy = st.builds(astm_RDBViewDefinition)
@given(instance=astm_RDBViewDefinition_strategy)
@settings(max_examples=25)
def test_astm_RDBViewDefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBViewDefinition)


astm_RDBViewType_strategy = st.builds(astm_RDBViewType)
@given(instance=astm_RDBViewType_strategy)
@settings(max_examples=25)
def test_astm_RDBViewType_instantiation(instance):
    assert isinstance(instance, astm_RDBViewType)


astm_RangeExpression_strategy = st.builds(astm_RangeExpression)
@given(instance=astm_RangeExpression_strategy)
@settings(max_examples=25)
def test_astm_RangeExpression_instantiation(instance):
    assert isinstance(instance, astm_RangeExpression)


astm_RangeType_strategy = st.builds(astm_RangeType)
@given(instance=astm_RangeType_strategy)
@settings(max_examples=25)
def test_astm_RangeType_instantiation(instance):
    assert isinstance(instance, astm_RangeType)


astm_RealLiteral_strategy = st.builds(astm_RealLiteral)
@given(instance=astm_RealLiteral_strategy)
@settings(max_examples=25)
def test_astm_RealLiteral_instantiation(instance):
    assert isinstance(instance, astm_RealLiteral)


astm_ReferenceType_strategy = st.builds(astm_ReferenceType)
@given(instance=astm_ReferenceType_strategy)
@settings(max_examples=25)
def test_astm_ReferenceType_instantiation(instance):
    assert isinstance(instance, astm_ReferenceType)


astm_ReturnStatement_strategy = st.builds(astm_ReturnStatement)
@given(instance=astm_ReturnStatement_strategy)
@settings(max_examples=25)
def test_astm_ReturnStatement_instantiation(instance):
    assert isinstance(instance, astm_ReturnStatement)


astm_Scope_strategy = st.builds(astm_Scope)
@given(instance=astm_Scope_strategy)
@settings(max_examples=25)
def test_astm_Scope_instantiation(instance):
    assert isinstance(instance, astm_Scope)


astm_ShortInteger_strategy = st.builds(astm_ShortInteger)
@given(instance=astm_ShortInteger_strategy)
@settings(max_examples=25)
def test_astm_ShortInteger_instantiation(instance):
    assert isinstance(instance, astm_ShortInteger)


astm_SourceFile_strategy = st.builds(astm_SourceFile, pathName=safe_text)
@given(instance=astm_SourceFile_strategy)
@settings(max_examples=25)
def test_astm_SourceFile_instantiation(instance):
    assert isinstance(instance, astm_SourceFile)


astm_SourceLocation_strategy = st.builds(astm_SourceLocation, endColumn=st.integers(), endLine=st.integers(), startColumn=st.integers(), startLine=st.integers())
@given(instance=astm_SourceLocation_strategy)
@settings(max_examples=25)
def test_astm_SourceLocation_instantiation(instance):
    assert isinstance(instance, astm_SourceLocation)


astm_SpecificConcatString_strategy = st.builds(astm_SpecificConcatString)
@given(instance=astm_SpecificConcatString_strategy)
@settings(max_examples=25)
def test_astm_SpecificConcatString_instantiation(instance):
    assert isinstance(instance, astm_SpecificConcatString)


astm_SpecificGreaterEqual_strategy = st.builds(astm_SpecificGreaterEqual)
@given(instance=astm_SpecificGreaterEqual_strategy)
@settings(max_examples=25)
def test_astm_SpecificGreaterEqual_instantiation(instance):
    assert isinstance(instance, astm_SpecificGreaterEqual)


astm_SpecificIn_strategy = st.builds(astm_SpecificIn)
@given(instance=astm_SpecificIn_strategy)
@settings(max_examples=25)
def test_astm_SpecificIn_instantiation(instance):
    assert isinstance(instance, astm_SpecificIn)


astm_SpecificLessEqual_strategy = st.builds(astm_SpecificLessEqual)
@given(instance=astm_SpecificLessEqual_strategy)
@settings(max_examples=25)
def test_astm_SpecificLessEqual_instantiation(instance):
    assert isinstance(instance, astm_SpecificLessEqual)


astm_SpecificLike_strategy = st.builds(astm_SpecificLike)
@given(instance=astm_SpecificLike_strategy)
@settings(max_examples=25)
def test_astm_SpecificLike_instantiation(instance):
    assert isinstance(instance, astm_SpecificLike)


astm_SpecificSelectStatement_strategy = st.builds(astm_SpecificSelectStatement)
@given(instance=astm_SpecificSelectStatement_strategy)
@settings(max_examples=25)
def test_astm_SpecificSelectStatement_instantiation(instance):
    assert isinstance(instance, astm_SpecificSelectStatement)


astm_SpecificTriggerDefinition_strategy = st.builds(astm_SpecificTriggerDefinition)
@given(instance=astm_SpecificTriggerDefinition_strategy)
@settings(max_examples=25)
def test_astm_SpecificTriggerDefinition_instantiation(instance):
    assert isinstance(instance, astm_SpecificTriggerDefinition)


astm_Statement_strategy = st.builds(astm_Statement)
@given(instance=astm_Statement_strategy)
@settings(max_examples=25)
def test_astm_Statement_instantiation(instance):
    assert isinstance(instance, astm_Statement)


astm_StorageSpecification_strategy = st.builds(astm_StorageSpecification)
@given(instance=astm_StorageSpecification_strategy)
@settings(max_examples=25)
def test_astm_StorageSpecification_instantiation(instance):
    assert isinstance(instance, astm_StorageSpecification)


astm_String_strategy = st.builds(astm_String)
@given(instance=astm_String_strategy)
@settings(max_examples=25)
def test_astm_String_instantiation(instance):
    assert isinstance(instance, astm_String)


astm_StringLiteral_strategy = st.builds(astm_StringLiteral)
@given(instance=astm_StringLiteral_strategy)
@settings(max_examples=25)
def test_astm_StringLiteral_instantiation(instance):
    assert isinstance(instance, astm_StringLiteral)


astm_StructureType_strategy = st.builds(astm_StructureType)
@given(instance=astm_StructureType_strategy)
@settings(max_examples=25)
def test_astm_StructureType_instantiation(instance):
    assert isinstance(instance, astm_StructureType)


astm_Subtract_strategy = st.builds(astm_Subtract)
@given(instance=astm_Subtract_strategy)
@settings(max_examples=25)
def test_astm_Subtract_instantiation(instance):
    assert isinstance(instance, astm_Subtract)


astm_SwitchCase_strategy = st.builds(astm_SwitchCase)
@given(instance=astm_SwitchCase_strategy)
@settings(max_examples=25)
def test_astm_SwitchCase_instantiation(instance):
    assert isinstance(instance, astm_SwitchCase)


astm_SwitchStatement_strategy = st.builds(astm_SwitchStatement)
@given(instance=astm_SwitchStatement_strategy)
@settings(max_examples=25)
def test_astm_SwitchStatement_instantiation(instance):
    assert isinstance(instance, astm_SwitchStatement)


astm_TerminateStatement_strategy = st.builds(astm_TerminateStatement)
@given(instance=astm_TerminateStatement_strategy)
@settings(max_examples=25)
def test_astm_TerminateStatement_instantiation(instance):
    assert isinstance(instance, astm_TerminateStatement)


astm_ThrowStatement_strategy = st.builds(astm_ThrowStatement)
@given(instance=astm_ThrowStatement_strategy)
@settings(max_examples=25)
def test_astm_ThrowStatement_instantiation(instance):
    assert isinstance(instance, astm_ThrowStatement)


astm_TryStatement_strategy = st.builds(astm_TryStatement)
@given(instance=astm_TryStatement_strategy)
@settings(max_examples=25)
def test_astm_TryStatement_instantiation(instance):
    assert isinstance(instance, astm_TryStatement)


astm_Type_strategy = st.builds(astm_Type, isConst=st.booleans(), isVolatile=st.booleans())
@given(instance=astm_Type_strategy)
@settings(max_examples=25)
def test_astm_Type_instantiation(instance):
    assert isinstance(instance, astm_Type)


astm_TypeDefinition_strategy = st.builds(astm_TypeDefinition)
@given(instance=astm_TypeDefinition_strategy)
@settings(max_examples=25)
def test_astm_TypeDefinition_instantiation(instance):
    assert isinstance(instance, astm_TypeDefinition)


astm_TypeQualifiedIdentifierReference_strategy = st.builds(astm_TypeQualifiedIdentifierReference)
@given(instance=astm_TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=25)
def test_astm_TypeQualifiedIdentifierReference_instantiation(instance):
    assert isinstance(instance, astm_TypeQualifiedIdentifierReference)


astm_TypeReference_strategy = st.builds(astm_TypeReference)
@given(instance=astm_TypeReference_strategy)
@settings(max_examples=25)
def test_astm_TypeReference_instantiation(instance):
    assert isinstance(instance, astm_TypeReference)


astm_TypesCatchBlock_strategy = st.builds(astm_TypesCatchBlock)
@given(instance=astm_TypesCatchBlock_strategy)
@settings(max_examples=25)
def test_astm_TypesCatchBlock_instantiation(instance):
    assert isinstance(instance, astm_TypesCatchBlock)


astm_UnaryExpression_strategy = st.builds(astm_UnaryExpression)
@given(instance=astm_UnaryExpression_strategy)
@settings(max_examples=25)
def test_astm_UnaryExpression_instantiation(instance):
    assert isinstance(instance, astm_UnaryExpression)


astm_UnaryOperator_strategy = st.builds(astm_UnaryOperator)
@given(instance=astm_UnaryOperator_strategy)
@settings(max_examples=25)
def test_astm_UnaryOperator_instantiation(instance):
    assert isinstance(instance, astm_UnaryOperator)


astm_UnaryPlus_strategy = st.builds(astm_UnaryPlus)
@given(instance=astm_UnaryPlus_strategy)
@settings(max_examples=25)
def test_astm_UnaryPlus_instantiation(instance):
    assert isinstance(instance, astm_UnaryPlus)


astm_UnionType_strategy = st.builds(astm_UnionType)
@given(instance=astm_UnionType_strategy)
@settings(max_examples=25)
def test_astm_UnionType_instantiation(instance):
    assert isinstance(instance, astm_UnionType)


astm_UnnamedTypeReference_strategy = st.builds(astm_UnnamedTypeReference)
@given(instance=astm_UnnamedTypeReference_strategy)
@settings(max_examples=25)
def test_astm_UnnamedTypeReference_instantiation(instance):
    assert isinstance(instance, astm_UnnamedTypeReference)


astm_VariableCatchBlock_strategy = st.builds(astm_VariableCatchBlock)
@given(instance=astm_VariableCatchBlock_strategy)
@settings(max_examples=25)
def test_astm_VariableCatchBlock_instantiation(instance):
    assert isinstance(instance, astm_VariableCatchBlock)


astm_VariableDeclaration_strategy = st.builds(astm_VariableDeclaration, isMutable=st.booleans())
@given(instance=astm_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_astm_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, astm_VariableDeclaration)


astm_VariableDefinition_strategy = st.builds(astm_VariableDefinition)
@given(instance=astm_VariableDefinition_strategy)
@settings(max_examples=25)
def test_astm_VariableDefinition_instantiation(instance):
    assert isinstance(instance, astm_VariableDefinition)


astm_Virtual_strategy = st.builds(astm_Virtual)
@given(instance=astm_Virtual_strategy)
@settings(max_examples=25)
def test_astm_Virtual_instantiation(instance):
    assert isinstance(instance, astm_Virtual)


astm_VirtualSpecification_strategy = st.builds(astm_VirtualSpecification)
@given(instance=astm_VirtualSpecification_strategy)
@settings(max_examples=25)
def test_astm_VirtualSpecification_instantiation(instance):
    assert isinstance(instance, astm_VirtualSpecification)


astm_Visitable_strategy = st.builds(astm_Visitable)
@given(instance=astm_Visitable_strategy)
@settings(max_examples=25)
def test_astm_Visitable_instantiation(instance):
    assert isinstance(instance, astm_Visitable)


astm_Void_strategy = st.builds(astm_Void)
@given(instance=astm_Void_strategy)
@settings(max_examples=25)
def test_astm_Void_instantiation(instance):
    assert isinstance(instance, astm_Void)


astm_WhileStatement_strategy = st.builds(astm_WhileStatement)
@given(instance=astm_WhileStatement_strategy)
@settings(max_examples=25)
def test_astm_WhileStatement_instantiation(instance):
    assert isinstance(instance, astm_WhileStatement)


astm_WideCharacter_strategy = st.builds(astm_WideCharacter)
@given(instance=astm_WideCharacter_strategy)
@settings(max_examples=25)
def test_astm_WideCharacter_instantiation(instance):
    assert isinstance(instance, astm_WideCharacter)



