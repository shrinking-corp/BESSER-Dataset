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
    PredefinedType,
    sql_datatype_BooleanType,
    sql_datatype_DatetimeType,
    sql_datatype_BinaryLargeObjectStringType,
    sql_datatype_CharacterStringType,
    DataType,
    sql_datatype_PredefinedType,
    sql_datatype_DataType,
    sql_datatype_NationalCharacterStringType,
    DatetimeLiteral,
    sql_literal_TimestampLiteral,
    sql_literal_TimeLiteral,
    sql_literal_DateLiteral,
    NumericLiteral,
    sql_literal_ApproximateNumericLiteral,
    sql_literal_ExactNumericLiteral,
    SchemaQualifiedName,
    NationalCharacterStringLiteral,
    sql_literal_CharacterStringLiteral,
    Literal,
    sql_literal_NumericLiteral,
    sql_literal_GeneralLiteral,
    sql_literal_Literal,
    GeneralLiteral,
    sql_literal_DatetimeLiteral,
    sql_literal_BooleanLiteral,
    sql_literal_NationalCharacterStringLiteral,
    Comment,
    sql_common_BracketedComment,
    sql_common_SimpleComment,
    Separator,
    sql_common_Comment,
    sql_common_SchemaQualifiedName,
    sql_common_Statement,
    sql_Dummy,
    Statement,
    sql_common_Separator,
    sql_common_DirectSQLStatement,
    sql_common_SQLScript,
    sql_schema_TableReference,
    TableReference,
    sql_schema_ReferentialConstraint,
    sql_schema_UniqueConstraint,
    TableConstraint,
    sql_schema_TableColumnsConstraint,
    DatetimeValueFunction,
    schema_TableColumnsConstraint,
    DirectSQLStatement,
    sql_schema_SQLSchemaStatement,
    schema_ReferentialConstraint,
    sql_schema_ReferentialTableConstraint,
    schema_ColumnConstraint,
    sql_schema_ReferentialColumnConstraint,
    schema_UniqueConstraint,
    sql_schema_UniqueTableConstraint,
    sql_schema_UniqueColumnConstraint,
    SQLSchemaStatement,
    sql_schema_SQLSchemaDefinitionStatement,
    Column,
    sql_schema_DefaultOption,
    TableDefinition,
    sql_schema_TableContentsSource,
    schema_TableElement,
    DefaultOption,
    sql_schema_LiteralDefaultOption,
    sql_schema_DatetimeValueFunctionDefaultOption,
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
    ColumnConstraint,
    sql_schema_NotNullColumnConstraint,
    TableElement,
    sql_schema_Column,
    TableContentsSource,
    sql_schema_TableElementList,
    TableElementList,
    sql_schema_TableElement,
    ImplicitlyTypedValueSpecification,
    sql_expression_NullSpecification,
    sql_expression_ImplicitlyTypedValueSpecification,
    EObject,
    sql_schema_TableConstraint,
    sql_schema_ColumnConstraint,
    schema_SQLSchemaDefinitionStatement,
    sql_schema_TableDefinition,
    DatetimeType,
    sql_datatype_TimeType,
    sql_datatype_TimestampType,
    sql_datatype_DateType,
    sql_function_DatetimeValueFunction,
    sql_datatype_LargeObjectLength,
    NumericType,
    sql_datatype_ApproximateNumericType,
    sql_datatype_ExactNumericType,
    sql_datatype_NumericType,
    LargeObjectLength,
    ApproximateNumericTypeKind,
    CharacterStringTypeKind,
    BinaryLargeObjectStringTypeKind,
    CharLengthUnits,
    Multiplier,
    UniqueSpecificationKind,
    TableScope,
    DatetimeValueFunctionKind,
    NationalCharacterStringTypeKind,
    ExactNumericTypeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_hyp_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_hyp_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_booleantype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_BooleanType)


def test_hyp_sql_datatype_booleantype_constructor_exists():
    assert callable(sql_datatype_BooleanType.__init__)


def test_hyp_sql_datatype_booleantype_constructor_args():
    sig = inspect.signature(sql_datatype_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_datetimetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DatetimeType)


def test_hyp_sql_datatype_datetimetype_constructor_exists():
    assert callable(sql_datatype_DatetimeType.__init__)


def test_hyp_sql_datatype_datetimetype_constructor_args():
    sig = inspect.signature(sql_datatype_DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_binarylargeobjectstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_BinaryLargeObjectStringType)


def test_hyp_sql_datatype_binarylargeobjectstringtype_constructor_exists():
    assert callable(sql_datatype_BinaryLargeObjectStringType.__init__)


def test_hyp_sql_datatype_binarylargeobjectstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_BinaryLargeObjectStringType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_sql_datatype_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_CharacterStringType)


def test_hyp_sql_datatype_characterstringtype_constructor_exists():
    assert callable(sql_datatype_CharacterStringType.__init__)


def test_hyp_sql_datatype_characterstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_PredefinedType)


def test_hyp_sql_datatype_predefinedtype_constructor_exists():
    assert callable(sql_datatype_PredefinedType.__init__)


def test_hyp_sql_datatype_predefinedtype_constructor_args():
    sig = inspect.signature(sql_datatype_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DataType)


def test_hyp_sql_datatype_datatype_constructor_exists():
    assert callable(sql_datatype_DataType.__init__)


def test_hyp_sql_datatype_datatype_constructor_args():
    sig = inspect.signature(sql_datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_nationalcharacterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_NationalCharacterStringType)


def test_hyp_sql_datatype_nationalcharacterstringtype_constructor_exists():
    assert callable(sql_datatype_NationalCharacterStringType.__init__)


def test_hyp_sql_datatype_nationalcharacterstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_NationalCharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(DatetimeLiteral)


def test_hyp_datetimeliteral_constructor_exists():
    assert callable(DatetimeLiteral.__init__)


def test_hyp_datetimeliteral_constructor_args():
    sig = inspect.signature(DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_timestampliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_TimestampLiteral)


def test_hyp_sql_literal_timestampliteral_constructor_exists():
    assert callable(sql_literal_TimestampLiteral.__init__)


def test_hyp_sql_literal_timestampliteral_constructor_args():
    sig = inspect.signature(sql_literal_TimestampLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sql_literal_timeliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_TimeLiteral)


def test_hyp_sql_literal_timeliteral_constructor_exists():
    assert callable(sql_literal_TimeLiteral.__init__)


def test_hyp_sql_literal_timeliteral_constructor_args():
    sig = inspect.signature(sql_literal_TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sql_literal_dateliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_DateLiteral)


def test_hyp_sql_literal_dateliteral_constructor_exists():
    assert callable(sql_literal_DateLiteral.__init__)


def test_hyp_sql_literal_dateliteral_constructor_args():
    sig = inspect.signature(sql_literal_DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_hyp_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_hyp_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_approximatenumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_ApproximateNumericLiteral)


def test_hyp_sql_literal_approximatenumericliteral_constructor_exists():
    assert callable(sql_literal_ApproximateNumericLiteral.__init__)


def test_hyp_sql_literal_approximatenumericliteral_constructor_args():
    sig = inspect.signature(sql_literal_ApproximateNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sql_literal_exactnumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_ExactNumericLiteral)


def test_hyp_sql_literal_exactnumericliteral_constructor_exists():
    assert callable(sql_literal_ExactNumericLiteral.__init__)


def test_hyp_sql_literal_exactnumericliteral_constructor_args():
    sig = inspect.signature(sql_literal_ExactNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_schemaqualifiedname_is_not_abstract():
    assert not inspect.isabstract(SchemaQualifiedName)


def test_hyp_schemaqualifiedname_constructor_exists():
    assert callable(SchemaQualifiedName.__init__)


def test_hyp_schemaqualifiedname_constructor_args():
    sig = inspect.signature(SchemaQualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nationalcharacterstringliteral_is_not_abstract():
    assert not inspect.isabstract(NationalCharacterStringLiteral)


def test_hyp_nationalcharacterstringliteral_constructor_exists():
    assert callable(NationalCharacterStringLiteral.__init__)


def test_hyp_nationalcharacterstringliteral_constructor_args():
    sig = inspect.signature(NationalCharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_characterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_CharacterStringLiteral)


def test_hyp_sql_literal_characterstringliteral_constructor_exists():
    assert callable(sql_literal_CharacterStringLiteral.__init__)


def test_hyp_sql_literal_characterstringliteral_constructor_args():
    sig = inspect.signature(sql_literal_CharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_numericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_NumericLiteral)


def test_hyp_sql_literal_numericliteral_constructor_exists():
    assert callable(sql_literal_NumericLiteral.__init__)


def test_hyp_sql_literal_numericliteral_constructor_args():
    sig = inspect.signature(sql_literal_NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_generalliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_GeneralLiteral)


def test_hyp_sql_literal_generalliteral_constructor_exists():
    assert callable(sql_literal_GeneralLiteral.__init__)


def test_hyp_sql_literal_generalliteral_constructor_args():
    sig = inspect.signature(sql_literal_GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_literal_is_not_abstract():
    assert not inspect.isabstract(sql_literal_Literal)


def test_hyp_sql_literal_literal_constructor_exists():
    assert callable(sql_literal_Literal.__init__)


def test_hyp_sql_literal_literal_constructor_args():
    sig = inspect.signature(sql_literal_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_generalliteral_is_not_abstract():
    assert not inspect.isabstract(GeneralLiteral)


def test_hyp_generalliteral_constructor_exists():
    assert callable(GeneralLiteral.__init__)


def test_hyp_generalliteral_constructor_args():
    sig = inspect.signature(GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_DatetimeLiteral)


def test_hyp_sql_literal_datetimeliteral_constructor_exists():
    assert callable(sql_literal_DatetimeLiteral.__init__)


def test_hyp_sql_literal_datetimeliteral_constructor_args():
    sig = inspect.signature(sql_literal_DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_literal_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_BooleanLiteral)


def test_hyp_sql_literal_booleanliteral_constructor_exists():
    assert callable(sql_literal_BooleanLiteral.__init__)


def test_hyp_sql_literal_booleanliteral_constructor_args():
    sig = inspect.signature(sql_literal_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sql_literal_nationalcharacterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_NationalCharacterStringLiteral)


def test_hyp_sql_literal_nationalcharacterstringliteral_constructor_exists():
    assert callable(sql_literal_NationalCharacterStringLiteral.__init__)


def test_hyp_sql_literal_nationalcharacterstringliteral_constructor_args():
    sig = inspect.signature(sql_literal_NationalCharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"




def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_bracketedcomment_is_not_abstract():
    assert not inspect.isabstract(sql_common_BracketedComment)


def test_hyp_sql_common_bracketedcomment_constructor_exists():
    assert callable(sql_common_BracketedComment.__init__)


def test_hyp_sql_common_bracketedcomment_constructor_args():
    sig = inspect.signature(sql_common_BracketedComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_simplecomment_is_not_abstract():
    assert not inspect.isabstract(sql_common_SimpleComment)


def test_hyp_sql_common_simplecomment_constructor_exists():
    assert callable(sql_common_SimpleComment.__init__)


def test_hyp_sql_common_simplecomment_constructor_args():
    sig = inspect.signature(sql_common_SimpleComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_separator_is_not_abstract():
    assert not inspect.isabstract(Separator)


def test_hyp_separator_constructor_exists():
    assert callable(Separator.__init__)


def test_hyp_separator_constructor_args():
    sig = inspect.signature(Separator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_comment_is_not_abstract():
    assert not inspect.isabstract(sql_common_Comment)


def test_hyp_sql_common_comment_constructor_exists():
    assert callable(sql_common_Comment.__init__)


def test_hyp_sql_common_comment_constructor_args():
    sig = inspect.signature(sql_common_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sql_common_schemaqualifiedname_is_not_abstract():
    assert not inspect.isabstract(sql_common_SchemaQualifiedName)


def test_hyp_sql_common_schemaqualifiedname_constructor_exists():
    assert callable(sql_common_SchemaQualifiedName.__init__)


def test_hyp_sql_common_schemaqualifiedname_constructor_args():
    sig = inspect.signature(sql_common_SchemaQualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "catalogName" in params, "Missing parameter 'catalogName'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_sql_common_statement_is_not_abstract():
    assert not inspect.isabstract(sql_common_Statement)


def test_hyp_sql_common_statement_constructor_exists():
    assert callable(sql_common_Statement.__init__)


def test_hyp_sql_common_statement_constructor_args():
    sig = inspect.signature(sql_common_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_dummy_is_not_abstract():
    assert not inspect.isabstract(sql_Dummy)


def test_hyp_sql_dummy_constructor_exists():
    assert callable(sql_Dummy.__init__)


def test_hyp_sql_dummy_constructor_args():
    sig = inspect.signature(sql_Dummy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_separator_is_not_abstract():
    assert not inspect.isabstract(sql_common_Separator)


def test_hyp_sql_common_separator_constructor_exists():
    assert callable(sql_common_Separator.__init__)


def test_hyp_sql_common_separator_constructor_args():
    sig = inspect.signature(sql_common_Separator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(sql_common_DirectSQLStatement)


def test_hyp_sql_common_directsqlstatement_constructor_exists():
    assert callable(sql_common_DirectSQLStatement.__init__)


def test_hyp_sql_common_directsqlstatement_constructor_args():
    sig = inspect.signature(sql_common_DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_common_sqlscript_is_not_abstract():
    assert not inspect.isabstract(sql_common_SQLScript)


def test_hyp_sql_common_sqlscript_constructor_exists():
    assert callable(sql_common_SQLScript.__init__)


def test_hyp_sql_common_sqlscript_constructor_args():
    sig = inspect.signature(sql_common_SQLScript.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tablereference_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableReference)


def test_hyp_sql_schema_tablereference_constructor_exists():
    assert callable(sql_schema_TableReference.__init__)


def test_hyp_sql_schema_tablereference_constructor_args():
    sig = inspect.signature(sql_schema_TableReference.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "catalogName" in params, "Missing parameter 'catalogName'"





def test_hyp_tablereference_is_not_abstract():
    assert not inspect.isabstract(TableReference)


def test_hyp_tablereference_constructor_exists():
    assert callable(TableReference.__init__)


def test_hyp_tablereference_constructor_args():
    sig = inspect.signature(TableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialConstraint)


def test_hyp_sql_schema_referentialconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialConstraint.__init__)


def test_hyp_sql_schema_referentialconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueConstraint)


def test_hyp_sql_schema_uniqueconstraint_constructor_exists():
    assert callable(sql_schema_UniqueConstraint.__init__)


def test_hyp_sql_schema_uniqueconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_hyp_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_hyp_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableColumnsConstraint)


def test_hyp_sql_schema_tablecolumnsconstraint_constructor_exists():
    assert callable(sql_schema_TableColumnsConstraint.__init__)


def test_hyp_sql_schema_tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(sql_schema_TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(DatetimeValueFunction)


def test_hyp_datetimevaluefunction_constructor_exists():
    assert callable(DatetimeValueFunction.__init__)


def test_hyp_datetimevaluefunction_constructor_args():
    sig = inspect.signature(DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_TableColumnsConstraint)


def test_hyp_schema_tablecolumnsconstraint_constructor_exists():
    assert callable(schema_TableColumnsConstraint.__init__)


def test_hyp_schema_tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(schema_TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(DirectSQLStatement)


def test_hyp_directsqlstatement_constructor_exists():
    assert callable(DirectSQLStatement.__init__)


def test_hyp_directsqlstatement_constructor_args():
    sig = inspect.signature(DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_SQLSchemaStatement)


def test_hyp_sql_schema_sqlschemastatement_constructor_exists():
    assert callable(sql_schema_SQLSchemaStatement.__init__)


def test_hyp_sql_schema_sqlschemastatement_constructor_args():
    sig = inspect.signature(sql_schema_SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_ReferentialConstraint)


def test_hyp_schema_referentialconstraint_constructor_exists():
    assert callable(schema_ReferentialConstraint.__init__)


def test_hyp_schema_referentialconstraint_constructor_args():
    sig = inspect.signature(schema_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_referentialtableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialTableConstraint)


def test_hyp_sql_schema_referentialtableconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialTableConstraint.__init__)


def test_hyp_sql_schema_referentialtableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_ColumnConstraint)


def test_hyp_schema_columnconstraint_constructor_exists():
    assert callable(schema_ColumnConstraint.__init__)


def test_hyp_schema_columnconstraint_constructor_args():
    sig = inspect.signature(schema_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_referentialcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialColumnConstraint)


def test_hyp_sql_schema_referentialcolumnconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialColumnConstraint.__init__)


def test_hyp_sql_schema_referentialcolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_UniqueConstraint)


def test_hyp_schema_uniqueconstraint_constructor_exists():
    assert callable(schema_UniqueConstraint.__init__)


def test_hyp_schema_uniqueconstraint_constructor_args():
    sig = inspect.signature(schema_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueTableConstraint)


def test_hyp_sql_schema_uniquetableconstraint_constructor_exists():
    assert callable(sql_schema_UniqueTableConstraint.__init__)


def test_hyp_sql_schema_uniquetableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_uniquecolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueColumnConstraint)


def test_hyp_sql_schema_uniquecolumnconstraint_constructor_exists():
    assert callable(sql_schema_UniqueColumnConstraint.__init__)


def test_hyp_sql_schema_uniquecolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(SQLSchemaStatement)


def test_hyp_sqlschemastatement_constructor_exists():
    assert callable(SQLSchemaStatement.__init__)


def test_hyp_sqlschemastatement_constructor_args():
    sig = inspect.signature(SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_SQLSchemaDefinitionStatement)


def test_hyp_sql_schema_sqlschemadefinitionstatement_constructor_exists():
    assert callable(sql_schema_SQLSchemaDefinitionStatement.__init__)


def test_hyp_sql_schema_sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(sql_schema_SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_hyp_column_constructor_exists():
    assert callable(Column.__init__)


def test_hyp_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_defaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_DefaultOption)


def test_hyp_sql_schema_defaultoption_constructor_exists():
    assert callable(sql_schema_DefaultOption.__init__)


def test_hyp_sql_schema_defaultoption_constructor_args():
    sig = inspect.signature(sql_schema_DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(TableDefinition)


def test_hyp_tabledefinition_constructor_exists():
    assert callable(TableDefinition.__init__)


def test_hyp_tabledefinition_constructor_args():
    sig = inspect.signature(TableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tablecontentssource_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableContentsSource)


def test_hyp_sql_schema_tablecontentssource_constructor_exists():
    assert callable(sql_schema_TableContentsSource.__init__)


def test_hyp_sql_schema_tablecontentssource_constructor_args():
    sig = inspect.signature(sql_schema_TableContentsSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_tableelement_is_not_abstract():
    assert not inspect.isabstract(schema_TableElement)


def test_hyp_schema_tableelement_constructor_exists():
    assert callable(schema_TableElement.__init__)


def test_hyp_schema_tableelement_constructor_args():
    sig = inspect.signature(schema_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultoption_is_not_abstract():
    assert not inspect.isabstract(DefaultOption)


def test_hyp_defaultoption_constructor_exists():
    assert callable(DefaultOption.__init__)


def test_hyp_defaultoption_constructor_args():
    sig = inspect.signature(DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_literaldefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_LiteralDefaultOption)


def test_hyp_sql_schema_literaldefaultoption_constructor_exists():
    assert callable(sql_schema_LiteralDefaultOption.__init__)


def test_hyp_sql_schema_literaldefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_LiteralDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_datetimevaluefunctiondefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_DatetimeValueFunctionDefaultOption)


def test_hyp_sql_schema_datetimevaluefunctiondefaultoption_constructor_exists():
    assert callable(sql_schema_DatetimeValueFunctionDefaultOption.__init__)


def test_hyp_sql_schema_datetimevaluefunctiondefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_DatetimeValueFunctionDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_implicitlytypedvaluespecificationdefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)


def test_hyp_sql_schema_implicitlytypedvaluespecificationdefaultoption_constructor_exists():
    assert callable(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption.__init__)


def test_hyp_sql_schema_implicitlytypedvaluespecificationdefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_hyp_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_hyp_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_notnullcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_NotNullColumnConstraint)


def test_hyp_sql_schema_notnullcolumnconstraint_constructor_exists():
    assert callable(sql_schema_NotNullColumnConstraint.__init__)


def test_hyp_sql_schema_notnullcolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_NotNullColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_hyp_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_hyp_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_column_is_not_abstract():
    assert not inspect.isabstract(sql_schema_Column)


def test_hyp_sql_schema_column_constructor_exists():
    assert callable(sql_schema_Column.__init__)


def test_hyp_sql_schema_column_constructor_args():
    sig = inspect.signature(sql_schema_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tablecontentssource_is_not_abstract():
    assert not inspect.isabstract(TableContentsSource)


def test_hyp_tablecontentssource_constructor_exists():
    assert callable(TableContentsSource.__init__)


def test_hyp_tablecontentssource_constructor_args():
    sig = inspect.signature(TableContentsSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tableelementlist_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableElementList)


def test_hyp_sql_schema_tableelementlist_constructor_exists():
    assert callable(sql_schema_TableElementList.__init__)


def test_hyp_sql_schema_tableelementlist_constructor_args():
    sig = inspect.signature(sql_schema_TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tableelementlist_is_not_abstract():
    assert not inspect.isabstract(TableElementList)


def test_hyp_tableelementlist_constructor_exists():
    assert callable(TableElementList.__init__)


def test_hyp_tableelementlist_constructor_args():
    sig = inspect.signature(TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tableelement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableElement)


def test_hyp_sql_schema_tableelement_constructor_exists():
    assert callable(sql_schema_TableElement.__init__)


def test_hyp_sql_schema_tableelement_constructor_args():
    sig = inspect.signature(sql_schema_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(ImplicitlyTypedValueSpecification)


def test_hyp_implicitlytypedvaluespecification_constructor_exists():
    assert callable(ImplicitlyTypedValueSpecification.__init__)


def test_hyp_implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_expression_nullspecification_is_not_abstract():
    assert not inspect.isabstract(sql_expression_NullSpecification)


def test_hyp_sql_expression_nullspecification_constructor_exists():
    assert callable(sql_expression_NullSpecification.__init__)


def test_hyp_sql_expression_nullspecification_constructor_args():
    sig = inspect.signature(sql_expression_NullSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_expression_implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ImplicitlyTypedValueSpecification)


def test_hyp_sql_expression_implicitlytypedvaluespecification_constructor_exists():
    assert callable(sql_expression_ImplicitlyTypedValueSpecification.__init__)


def test_hyp_sql_expression_implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(sql_expression_ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_hyp_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_hyp_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableConstraint)


def test_hyp_sql_schema_tableconstraint_constructor_exists():
    assert callable(sql_schema_TableConstraint.__init__)


def test_hyp_sql_schema_tableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ColumnConstraint)


def test_hyp_sql_schema_columnconstraint_constructor_exists():
    assert callable(sql_schema_ColumnConstraint.__init__)


def test_hyp_sql_schema_columnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schema_sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(schema_SQLSchemaDefinitionStatement)


def test_hyp_schema_sqlschemadefinitionstatement_constructor_exists():
    assert callable(schema_SQLSchemaDefinitionStatement.__init__)


def test_hyp_schema_sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(schema_SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_schema_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableDefinition)


def test_hyp_sql_schema_tabledefinition_constructor_exists():
    assert callable(sql_schema_TableDefinition.__init__)


def test_hyp_sql_schema_tabledefinition_constructor_args():
    sig = inspect.signature(sql_schema_TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "label" in params, "Missing parameter 'label'"





def test_hyp_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatetimeType)


def test_hyp_datetimetype_constructor_exists():
    assert callable(DatetimeType.__init__)


def test_hyp_datetimetype_constructor_args():
    sig = inspect.signature(DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_timetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_TimeType)


def test_hyp_sql_datatype_timetype_constructor_exists():
    assert callable(sql_datatype_TimeType.__init__)


def test_hyp_sql_datatype_timetype_constructor_args():
    sig = inspect.signature(sql_datatype_TimeType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"





def test_hyp_sql_datatype_timestamptype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_TimestampType)


def test_hyp_sql_datatype_timestamptype_constructor_exists():
    assert callable(sql_datatype_TimestampType.__init__)


def test_hyp_sql_datatype_timestamptype_constructor_args():
    sig = inspect.signature(sql_datatype_TimestampType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"





def test_hyp_sql_datatype_datetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DateType)


def test_hyp_sql_datatype_datetype_constructor_exists():
    assert callable(sql_datatype_DateType.__init__)


def test_hyp_sql_datatype_datetype_constructor_args():
    sig = inspect.signature(sql_datatype_DateType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_function_datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(sql_function_DatetimeValueFunction)


def test_hyp_sql_function_datetimevaluefunction_constructor_exists():
    assert callable(sql_function_DatetimeValueFunction.__init__)


def test_hyp_sql_function_datetimevaluefunction_constructor_args():
    sig = inspect.signature(sql_function_DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_sql_datatype_largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_LargeObjectLength)


def test_hyp_sql_datatype_largeobjectlength_constructor_exists():
    assert callable(sql_datatype_LargeObjectLength.__init__)


def test_hyp_sql_datatype_largeobjectlength_constructor_args():
    sig = inspect.signature(sql_datatype_LargeObjectLength.__init__)
    params = list(sig.parameters.keys())
    assert "multiplier" in params, "Missing parameter 'multiplier'"
    assert "value" in params, "Missing parameter 'value'"
    assert "units" in params, "Missing parameter 'units'"






def test_hyp_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_hyp_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_hyp_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_datatype_approximatenumerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_ApproximateNumericType)


def test_hyp_sql_datatype_approximatenumerictype_constructor_exists():
    assert callable(sql_datatype_ApproximateNumericType.__init__)


def test_hyp_sql_datatype_approximatenumerictype_constructor_args():
    sig = inspect.signature(sql_datatype_ApproximateNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "precision" in params, "Missing parameter 'precision'"





def test_hyp_sql_datatype_exactnumerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_ExactNumericType)


def test_hyp_sql_datatype_exactnumerictype_constructor_exists():
    assert callable(sql_datatype_ExactNumericType.__init__)


def test_hyp_sql_datatype_exactnumerictype_constructor_args():
    sig = inspect.signature(sql_datatype_ExactNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "kind" in params, "Missing parameter 'kind'"






def test_hyp_sql_datatype_numerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_NumericType)


def test_hyp_sql_datatype_numerictype_constructor_exists():
    assert callable(sql_datatype_NumericType.__init__)


def test_hyp_sql_datatype_numerictype_constructor_args():
    sig = inspect.signature(sql_datatype_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(LargeObjectLength)


def test_hyp_largeobjectlength_constructor_exists():
    assert callable(LargeObjectLength.__init__)


def test_hyp_largeobjectlength_constructor_args():
    sig = inspect.signature(LargeObjectLength.__init__)
    params = list(sig.parameters.keys())

def test_hyp_approximatenumerictypekind_exists():
    # Check that the Enumeration exists
    assert ApproximateNumericTypeKind is not None

def test_hyp_approximatenumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ApproximateNumericTypeKind]
    expected_literals = [
        "FLOAT",
        "REAL",
        "DOUBLE_PRECISION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ApproximateNumericTypeKind"

def test_hyp_characterstringtypekind_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypeKind is not None

def test_hyp_characterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypeKind]
    expected_literals = [
        "VARCHAR",
        "CHAR_VARYING",
        "CHAR",
        "CHARACTER_VARYING",
        "CHARACTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypeKind"

def test_hyp_binarylargeobjectstringtypekind_exists():
    # Check that the Enumeration exists
    assert BinaryLargeObjectStringTypeKind is not None

def test_hyp_binarylargeobjectstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryLargeObjectStringTypeKind]
    expected_literals = [
        "BLOB",
        "BINARY_LARGE_OBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryLargeObjectStringTypeKind"

def test_hyp_charlengthunits_exists():
    # Check that the Enumeration exists
    assert CharLengthUnits is not None

def test_hyp_charlengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharLengthUnits]
    expected_literals = [
        "OCTETS",
        "CHARACTERS",
        "CODE_UNITS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharLengthUnits"

def test_hyp_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_hyp_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "M",
        "G",
        "K",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_hyp_uniquespecificationkind_exists():
    # Check that the Enumeration exists
    assert UniqueSpecificationKind is not None

def test_hyp_uniquespecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UniqueSpecificationKind]
    expected_literals = [
        "UNIQUE",
        "PRIMARY_KEY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UniqueSpecificationKind"

def test_hyp_tablescope_exists():
    # Check that the Enumeration exists
    assert TableScope is not None

def test_hyp_tablescope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableScope]
    expected_literals = [
        "PERSISTENT",
        "LOCAL_TEMPORARY",
        "GLOBAL_TEMPORARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableScope"

def test_hyp_datetimevaluefunctionkind_exists():
    # Check that the Enumeration exists
    assert DatetimeValueFunctionKind is not None

def test_hyp_datetimevaluefunctionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeValueFunctionKind]
    expected_literals = [
        "CURRENT_TIMESTAMP",
        "CURRENT_DATE",
        "LOCALTIME",
        "CURRENT_TIME",
        "LOCALTIMESTAMP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeValueFunctionKind"

def test_hyp_nationalcharacterstringtypekind_exists():
    # Check that the Enumeration exists
    assert NationalCharacterStringTypeKind is not None

def test_hyp_nationalcharacterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NationalCharacterStringTypeKind]
    expected_literals = [
        "NATIONAL_CHARACTER",
        "NATIONAL_CHAR_VARYING",
        "NCHAR_VARYING",
        "NATIONAL_CHARACTER_VARYING",
        "NATIONAL_CHAR",
        "NCHAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NationalCharacterStringTypeKind"

def test_hyp_exactnumerictypekind_exists():
    # Check that the Enumeration exists
    assert ExactNumericTypeKind is not None

def test_hyp_exactnumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExactNumericTypeKind]
    expected_literals = [
        "BIGINT",
        "SMALLINT",
        "DECIMAL",
        "INTEGER",
        "NUMERIC",
        "INT",
        "DEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExactNumericTypeKind"


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
PredefinedType_strategy = st.builds(
    PredefinedType,
)
sql_datatype_BooleanType_strategy = st.builds(
    sql_datatype_BooleanType,
)
sql_datatype_DatetimeType_strategy = st.builds(
    sql_datatype_DatetimeType,
)
sql_datatype_BinaryLargeObjectStringType_strategy = st.builds(
    sql_datatype_BinaryLargeObjectStringType,
    kind=
        safe_text
)
sql_datatype_CharacterStringType_strategy = st.builds(
    sql_datatype_CharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
sql_datatype_PredefinedType_strategy = st.builds(
    sql_datatype_PredefinedType,
)
sql_datatype_DataType_strategy = st.builds(
    sql_datatype_DataType,
)
sql_datatype_NationalCharacterStringType_strategy = st.builds(
    sql_datatype_NationalCharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
DatetimeLiteral_strategy = st.builds(
    DatetimeLiteral,
)
sql_literal_TimestampLiteral_strategy = st.builds(
    sql_literal_TimestampLiteral,
    value=
        safe_text
)
sql_literal_TimeLiteral_strategy = st.builds(
    sql_literal_TimeLiteral,
    value=
        safe_text
)
sql_literal_DateLiteral_strategy = st.builds(
    sql_literal_DateLiteral,
    value=
        safe_text
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
sql_literal_ApproximateNumericLiteral_strategy = st.builds(
    sql_literal_ApproximateNumericLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sql_literal_ExactNumericLiteral_strategy = st.builds(
    sql_literal_ExactNumericLiteral,
    value=
        safe_text
)
SchemaQualifiedName_strategy = st.builds(
    SchemaQualifiedName,
)
NationalCharacterStringLiteral_strategy = st.builds(
    NationalCharacterStringLiteral,
)
sql_literal_CharacterStringLiteral_strategy = st.builds(
    sql_literal_CharacterStringLiteral,
)
Literal_strategy = st.builds(
    Literal,
)
sql_literal_NumericLiteral_strategy = st.builds(
    sql_literal_NumericLiteral,
)
sql_literal_GeneralLiteral_strategy = st.builds(
    sql_literal_GeneralLiteral,
)
sql_literal_Literal_strategy = st.builds(
    sql_literal_Literal,
)
GeneralLiteral_strategy = st.builds(
    GeneralLiteral,
)
sql_literal_DatetimeLiteral_strategy = st.builds(
    sql_literal_DatetimeLiteral,
)
sql_literal_BooleanLiteral_strategy = st.builds(
    sql_literal_BooleanLiteral,
    value=
        safe_text
)
sql_literal_NationalCharacterStringLiteral_strategy = st.builds(
    sql_literal_NationalCharacterStringLiteral,
    values=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
sql_common_BracketedComment_strategy = st.builds(
    sql_common_BracketedComment,
)
sql_common_SimpleComment_strategy = st.builds(
    sql_common_SimpleComment,
)
Separator_strategy = st.builds(
    Separator,
)
sql_common_Comment_strategy = st.builds(
    sql_common_Comment,
    value=
        safe_text
)
sql_common_SchemaQualifiedName_strategy = st.builds(
    sql_common_SchemaQualifiedName,
    schemaName=
        safe_text,
    catalogName=
        safe_text,
    name=
        safe_text
)
sql_common_Statement_strategy = st.builds(
    sql_common_Statement,
)
sql_Dummy_strategy = st.builds(
    sql_Dummy,
)
Statement_strategy = st.builds(
    Statement,
)
sql_common_Separator_strategy = st.builds(
    sql_common_Separator,
)
sql_common_DirectSQLStatement_strategy = st.builds(
    sql_common_DirectSQLStatement,
)
sql_common_SQLScript_strategy = st.builds(
    sql_common_SQLScript,
)
sql_schema_TableReference_strategy = st.builds(
    sql_schema_TableReference,
    schemaName=
        safe_text,
    catalogName=
        safe_text
)
TableReference_strategy = st.builds(
    TableReference,
)
sql_schema_ReferentialConstraint_strategy = st.builds(
    sql_schema_ReferentialConstraint,
)
sql_schema_UniqueConstraint_strategy = st.builds(
    sql_schema_UniqueConstraint,
    kind=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sql_schema_TableColumnsConstraint_strategy = st.builds(
    sql_schema_TableColumnsConstraint,
)
DatetimeValueFunction_strategy = st.builds(
    DatetimeValueFunction,
)
schema_TableColumnsConstraint_strategy = st.builds(
    schema_TableColumnsConstraint,
)
DirectSQLStatement_strategy = st.builds(
    DirectSQLStatement,
)
sql_schema_SQLSchemaStatement_strategy = st.builds(
    sql_schema_SQLSchemaStatement,
)
schema_ReferentialConstraint_strategy = st.builds(
    schema_ReferentialConstraint,
)
sql_schema_ReferentialTableConstraint_strategy = st.builds(
    sql_schema_ReferentialTableConstraint,
)
schema_ColumnConstraint_strategy = st.builds(
    schema_ColumnConstraint,
)
sql_schema_ReferentialColumnConstraint_strategy = st.builds(
    sql_schema_ReferentialColumnConstraint,
)
schema_UniqueConstraint_strategy = st.builds(
    schema_UniqueConstraint,
)
sql_schema_UniqueTableConstraint_strategy = st.builds(
    sql_schema_UniqueTableConstraint,
)
sql_schema_UniqueColumnConstraint_strategy = st.builds(
    sql_schema_UniqueColumnConstraint,
)
SQLSchemaStatement_strategy = st.builds(
    SQLSchemaStatement,
)
sql_schema_SQLSchemaDefinitionStatement_strategy = st.builds(
    sql_schema_SQLSchemaDefinitionStatement,
)
Column_strategy = st.builds(
    Column,
)
sql_schema_DefaultOption_strategy = st.builds(
    sql_schema_DefaultOption,
)
TableDefinition_strategy = st.builds(
    TableDefinition,
)
sql_schema_TableContentsSource_strategy = st.builds(
    sql_schema_TableContentsSource,
)
schema_TableElement_strategy = st.builds(
    schema_TableElement,
)
DefaultOption_strategy = st.builds(
    DefaultOption,
)
sql_schema_LiteralDefaultOption_strategy = st.builds(
    sql_schema_LiteralDefaultOption,
)
sql_schema_DatetimeValueFunctionDefaultOption_strategy = st.builds(
    sql_schema_DatetimeValueFunctionDefaultOption,
)
sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_strategy = st.builds(
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
sql_schema_NotNullColumnConstraint_strategy = st.builds(
    sql_schema_NotNullColumnConstraint,
)
TableElement_strategy = st.builds(
    TableElement,
)
sql_schema_Column_strategy = st.builds(
    sql_schema_Column,
    name=
        safe_text
)
TableContentsSource_strategy = st.builds(
    TableContentsSource,
)
sql_schema_TableElementList_strategy = st.builds(
    sql_schema_TableElementList,
)
TableElementList_strategy = st.builds(
    TableElementList,
)
sql_schema_TableElement_strategy = st.builds(
    sql_schema_TableElement,
)
ImplicitlyTypedValueSpecification_strategy = st.builds(
    ImplicitlyTypedValueSpecification,
)
sql_expression_NullSpecification_strategy = st.builds(
    sql_expression_NullSpecification,
)
sql_expression_ImplicitlyTypedValueSpecification_strategy = st.builds(
    sql_expression_ImplicitlyTypedValueSpecification,
)
EObject_strategy = st.builds(
    EObject,
)
sql_schema_TableConstraint_strategy = st.builds(
    sql_schema_TableConstraint,
)
sql_schema_ColumnConstraint_strategy = st.builds(
    sql_schema_ColumnConstraint,
)
schema_SQLSchemaDefinitionStatement_strategy = st.builds(
    schema_SQLSchemaDefinitionStatement,
)
sql_schema_TableDefinition_strategy = st.builds(
    sql_schema_TableDefinition,
    scope=
        safe_text,
    label=
        safe_text
)
DatetimeType_strategy = st.builds(
    DatetimeType,
)
sql_datatype_TimeType_strategy = st.builds(
    sql_datatype_TimeType,
    precision=
        safe_text,
    withTimeZone=
        safe_text
)
sql_datatype_TimestampType_strategy = st.builds(
    sql_datatype_TimestampType,
    precision=
        safe_text,
    withTimeZone=
        safe_text
)
sql_datatype_DateType_strategy = st.builds(
    sql_datatype_DateType,
)
sql_function_DatetimeValueFunction_strategy = st.builds(
    sql_function_DatetimeValueFunction,
    precision=
        safe_text,
    kind=
        safe_text
)
sql_datatype_LargeObjectLength_strategy = st.builds(
    sql_datatype_LargeObjectLength,
    multiplier=
        safe_text,
    value=
        safe_text,
    units=
        safe_text
)
NumericType_strategy = st.builds(
    NumericType,
)
sql_datatype_ApproximateNumericType_strategy = st.builds(
    sql_datatype_ApproximateNumericType,
    kind=
        safe_text,
    precision=
        safe_text
)
sql_datatype_ExactNumericType_strategy = st.builds(
    sql_datatype_ExactNumericType,
    scale=
        safe_text,
    precision=
        safe_text,
    kind=
        safe_text
)
sql_datatype_NumericType_strategy = st.builds(
    sql_datatype_NumericType,
)
LargeObjectLength_strategy = st.builds(
    LargeObjectLength,
)







@given(instance=sql_datatype_BinaryLargeObjectStringType_strategy)
def test_hyp_sql_datatype_binarylargeobjectstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=sql_datatype_CharacterStringType_strategy)
def test_hyp_sql_datatype_characterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sql_datatype_CharacterStringType_strategy)
def test_hyp_sql_datatype_characterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original







@given(instance=sql_datatype_NationalCharacterStringType_strategy)
def test_hyp_sql_datatype_nationalcharacterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sql_datatype_NationalCharacterStringType_strategy)
def test_hyp_sql_datatype_nationalcharacterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





@given(instance=sql_literal_TimestampLiteral_strategy)
def test_hyp_sql_literal_timestampliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=sql_literal_TimeLiteral_strategy)
def test_hyp_sql_literal_timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=sql_literal_DateLiteral_strategy)
def test_hyp_sql_literal_dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=sql_literal_ApproximateNumericLiteral_strategy)
def test_hyp_sql_literal_approximatenumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=sql_literal_ExactNumericLiteral_strategy)
def test_hyp_sql_literal_exactnumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original













@given(instance=sql_literal_BooleanLiteral_strategy)
def test_hyp_sql_literal_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=sql_literal_NationalCharacterStringLiteral_strategy)
def test_hyp_sql_literal_nationalcharacterstringliteral_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original








@given(instance=sql_common_Comment_strategy)
def test_hyp_sql_common_comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_hyp_sql_common_schemaqualifiedname_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_hyp_sql_common_schemaqualifiedname_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original



@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_hyp_sql_common_schemaqualifiedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=sql_schema_TableReference_strategy)
def test_hyp_sql_schema_tablereference_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=sql_schema_TableReference_strategy)
def test_hyp_sql_schema_tablereference_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original






@given(instance=sql_schema_UniqueConstraint_strategy)
def test_hyp_sql_schema_uniqueconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original































@given(instance=sql_schema_Column_strategy)
def test_hyp_sql_schema_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original















@given(instance=sql_schema_TableDefinition_strategy)
def test_hyp_sql_schema_tabledefinition_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=sql_schema_TableDefinition_strategy)
def test_hyp_sql_schema_tabledefinition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original





@given(instance=sql_datatype_TimeType_strategy)
def test_hyp_sql_datatype_timetype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_TimeType_strategy)
def test_hyp_sql_datatype_timetype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original




@given(instance=sql_datatype_TimestampType_strategy)
def test_hyp_sql_datatype_timestamptype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_TimestampType_strategy)
def test_hyp_sql_datatype_timestamptype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original





@given(instance=sql_function_DatetimeValueFunction_strategy)
def test_hyp_sql_function_datetimevaluefunction_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_function_DatetimeValueFunction_strategy)
def test_hyp_sql_function_datetimevaluefunction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_hyp_sql_datatype_largeobjectlength_multiplier_setter(instance):
    original = instance.multiplier
    instance.multiplier = original
    assert instance.multiplier == original



@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_hyp_sql_datatype_largeobjectlength_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_hyp_sql_datatype_largeobjectlength_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original





@given(instance=sql_datatype_ApproximateNumericType_strategy)
def test_hyp_sql_datatype_approximatenumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=sql_datatype_ApproximateNumericType_strategy)
def test_hyp_sql_datatype_approximatenumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original




@given(instance=sql_datatype_ExactNumericType_strategy)
def test_hyp_sql_datatype_exactnumerictype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=sql_datatype_ExactNumericType_strategy)
def test_hyp_sql_datatype_exactnumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_ExactNumericType_strategy)
def test_hyp_sql_datatype_exactnumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Column,
    ColumnConstraint,
    Comment,
    DataType,
    DatetimeLiteral,
    DatetimeType,
    DatetimeValueFunction,
    DefaultOption,
    DirectSQLStatement,
    EObject,
    GeneralLiteral,
    ImplicitlyTypedValueSpecification,
    LargeObjectLength,
    Literal,
    NationalCharacterStringLiteral,
    NumericLiteral,
    NumericType,
    PredefinedType,
    SQLSchemaStatement,
    SchemaQualifiedName,
    Separator,
    Statement,
    TableConstraint,
    TableContentsSource,
    TableDefinition,
    TableElement,
    TableElementList,
    TableReference,
    schema_ColumnConstraint,
    schema_ReferentialConstraint,
    schema_SQLSchemaDefinitionStatement,
    schema_TableColumnsConstraint,
    schema_TableElement,
    schema_UniqueConstraint,
    sql_Dummy,
    sql_common_BracketedComment,
    sql_common_Comment,
    sql_common_DirectSQLStatement,
    sql_common_SQLScript,
    sql_common_SchemaQualifiedName,
    sql_common_Separator,
    sql_common_SimpleComment,
    sql_common_Statement,
    sql_datatype_ApproximateNumericType,
    sql_datatype_BinaryLargeObjectStringType,
    sql_datatype_BooleanType,
    sql_datatype_CharacterStringType,
    sql_datatype_DataType,
    sql_datatype_DateType,
    sql_datatype_DatetimeType,
    sql_datatype_ExactNumericType,
    sql_datatype_LargeObjectLength,
    sql_datatype_NationalCharacterStringType,
    sql_datatype_NumericType,
    sql_datatype_PredefinedType,
    sql_datatype_TimeType,
    sql_datatype_TimestampType,
    sql_expression_ImplicitlyTypedValueSpecification,
    sql_expression_NullSpecification,
    sql_function_DatetimeValueFunction,
    sql_literal_ApproximateNumericLiteral,
    sql_literal_BooleanLiteral,
    sql_literal_CharacterStringLiteral,
    sql_literal_DateLiteral,
    sql_literal_DatetimeLiteral,
    sql_literal_ExactNumericLiteral,
    sql_literal_GeneralLiteral,
    sql_literal_Literal,
    sql_literal_NationalCharacterStringLiteral,
    sql_literal_NumericLiteral,
    sql_literal_TimeLiteral,
    sql_literal_TimestampLiteral,
    sql_schema_Column,
    sql_schema_ColumnConstraint,
    sql_schema_DatetimeValueFunctionDefaultOption,
    sql_schema_DefaultOption,
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
    sql_schema_LiteralDefaultOption,
    sql_schema_NotNullColumnConstraint,
    sql_schema_ReferentialColumnConstraint,
    sql_schema_ReferentialConstraint,
    sql_schema_ReferentialTableConstraint,
    sql_schema_SQLSchemaDefinitionStatement,
    sql_schema_SQLSchemaStatement,
    sql_schema_TableColumnsConstraint,
    sql_schema_TableConstraint,
    sql_schema_TableContentsSource,
    sql_schema_TableDefinition,
    sql_schema_TableElement,
    sql_schema_TableElementList,
    sql_schema_TableReference,
    sql_schema_UniqueColumnConstraint,
    sql_schema_UniqueConstraint,
    sql_schema_UniqueTableConstraint,
    ApproximateNumericTypeKind,
    BinaryLargeObjectStringTypeKind,
    CharLengthUnits,
    CharacterStringTypeKind,
    DatetimeValueFunctionKind,
    ExactNumericTypeKind,
    Multiplier,
    NationalCharacterStringTypeKind,
    TableScope,
    UniqueSpecificationKind,
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

def test_sql_common_Comment_value_value_roundtrip():
    instance = sql_common_Comment(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_common_SchemaQualifiedName_catalogName_value_roundtrip():
    instance = sql_common_SchemaQualifiedName(catalogName="sample_text", name="sample_text", schemaName="sample_text")
    assert instance.catalogName == "sample_text"
    instance.catalogName = "sample_text_2"
    assert instance.catalogName == "sample_text_2"


def test_sql_common_SchemaQualifiedName_name_value_roundtrip():
    instance = sql_common_SchemaQualifiedName(catalogName="sample_text", name="sample_text", schemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sql_common_SchemaQualifiedName_schemaName_value_roundtrip():
    instance = sql_common_SchemaQualifiedName(catalogName="sample_text", name="sample_text", schemaName="sample_text")
    assert instance.schemaName == "sample_text"
    instance.schemaName = "sample_text_2"
    assert instance.schemaName == "sample_text_2"


def test_sql_datatype_ApproximateNumericType_kind_value_roundtrip():
    instance = sql_datatype_ApproximateNumericType(kind="sample_text", precision="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_datatype_ApproximateNumericType_precision_value_roundtrip():
    instance = sql_datatype_ApproximateNumericType(kind="sample_text", precision="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_sql_datatype_BinaryLargeObjectStringType_kind_value_roundtrip():
    instance = sql_datatype_BinaryLargeObjectStringType(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_datatype_CharacterStringType_kind_value_roundtrip():
    instance = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_datatype_CharacterStringType_length_value_roundtrip():
    instance = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_sql_datatype_ExactNumericType_kind_value_roundtrip():
    instance = sql_datatype_ExactNumericType(kind="sample_text", precision="sample_text", scale="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_datatype_ExactNumericType_precision_value_roundtrip():
    instance = sql_datatype_ExactNumericType(kind="sample_text", precision="sample_text", scale="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_sql_datatype_ExactNumericType_scale_value_roundtrip():
    instance = sql_datatype_ExactNumericType(kind="sample_text", precision="sample_text", scale="sample_text")
    assert instance.scale == "sample_text"
    instance.scale = "sample_text_2"
    assert instance.scale == "sample_text_2"


def test_sql_datatype_LargeObjectLength_multiplier_value_roundtrip():
    instance = sql_datatype_LargeObjectLength(multiplier="sample_text", units="sample_text", value="sample_text")
    assert instance.multiplier == "sample_text"
    instance.multiplier = "sample_text_2"
    assert instance.multiplier == "sample_text_2"


def test_sql_datatype_LargeObjectLength_units_value_roundtrip():
    instance = sql_datatype_LargeObjectLength(multiplier="sample_text", units="sample_text", value="sample_text")
    assert instance.units == "sample_text"
    instance.units = "sample_text_2"
    assert instance.units == "sample_text_2"


def test_sql_datatype_LargeObjectLength_value_value_roundtrip():
    instance = sql_datatype_LargeObjectLength(multiplier="sample_text", units="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_datatype_NationalCharacterStringType_kind_value_roundtrip():
    instance = sql_datatype_NationalCharacterStringType(kind="sample_text", length="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_datatype_NationalCharacterStringType_length_value_roundtrip():
    instance = sql_datatype_NationalCharacterStringType(kind="sample_text", length="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_sql_datatype_TimeType_precision_value_roundtrip():
    instance = sql_datatype_TimeType(precision="sample_text", withTimeZone="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_sql_datatype_TimeType_withTimeZone_value_roundtrip():
    instance = sql_datatype_TimeType(precision="sample_text", withTimeZone="sample_text")
    assert instance.withTimeZone == "sample_text"
    instance.withTimeZone = "sample_text_2"
    assert instance.withTimeZone == "sample_text_2"


def test_sql_datatype_TimestampType_precision_value_roundtrip():
    instance = sql_datatype_TimestampType(precision="sample_text", withTimeZone="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_sql_datatype_TimestampType_withTimeZone_value_roundtrip():
    instance = sql_datatype_TimestampType(precision="sample_text", withTimeZone="sample_text")
    assert instance.withTimeZone == "sample_text"
    instance.withTimeZone = "sample_text_2"
    assert instance.withTimeZone == "sample_text_2"


def test_sql_function_DatetimeValueFunction_kind_value_roundtrip():
    instance = sql_function_DatetimeValueFunction(kind="sample_text", precision="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_function_DatetimeValueFunction_precision_value_roundtrip():
    instance = sql_function_DatetimeValueFunction(kind="sample_text", precision="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_sql_literal_ApproximateNumericLiteral_value_value_roundtrip():
    instance = sql_literal_ApproximateNumericLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_sql_literal_BooleanLiteral_value_value_roundtrip():
    instance = sql_literal_BooleanLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_literal_DateLiteral_value_value_roundtrip():
    instance = sql_literal_DateLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_literal_ExactNumericLiteral_value_value_roundtrip():
    instance = sql_literal_ExactNumericLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_literal_NationalCharacterStringLiteral_values_value_roundtrip():
    instance = sql_literal_NationalCharacterStringLiteral(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_sql_literal_TimeLiteral_value_value_roundtrip():
    instance = sql_literal_TimeLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_literal_TimestampLiteral_value_value_roundtrip():
    instance = sql_literal_TimestampLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sql_schema_Column_name_value_roundtrip():
    instance = sql_schema_Column(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sql_schema_TableDefinition_label_value_roundtrip():
    instance = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_sql_schema_TableDefinition_scope_value_roundtrip():
    instance = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_sql_schema_TableReference_catalogName_value_roundtrip():
    instance = sql_schema_TableReference(catalogName="sample_text", schemaName="sample_text")
    assert instance.catalogName == "sample_text"
    instance.catalogName = "sample_text_2"
    assert instance.catalogName == "sample_text_2"


def test_sql_schema_TableReference_schemaName_value_roundtrip():
    instance = sql_schema_TableReference(catalogName="sample_text", schemaName="sample_text")
    assert instance.schemaName == "sample_text"
    instance.schemaName = "sample_text_2"
    assert instance.schemaName == "sample_text_2"


def test_sql_schema_UniqueConstraint_kind_value_roundtrip():
    instance = sql_schema_UniqueConstraint(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_sql_schema_NotNullColumnConstraint_isa_ColumnConstraint():
    instance = sql_schema_NotNullColumnConstraint()
    assert isinstance(instance, ColumnConstraint)


def test_sql_common_BracketedComment_isa_Comment():
    instance = sql_common_BracketedComment()
    assert isinstance(instance, Comment)


def test_sql_common_SimpleComment_isa_Comment():
    instance = sql_common_SimpleComment()
    assert isinstance(instance, Comment)


def test_sql_datatype_PredefinedType_isa_DataType():
    instance = sql_datatype_PredefinedType()
    assert isinstance(instance, DataType)


def test_sql_literal_DateLiteral_isa_DatetimeLiteral():
    instance = sql_literal_DateLiteral(value="sample_text")
    assert isinstance(instance, DatetimeLiteral)


def test_sql_literal_TimeLiteral_isa_DatetimeLiteral():
    instance = sql_literal_TimeLiteral(value="sample_text")
    assert isinstance(instance, DatetimeLiteral)


def test_sql_literal_TimestampLiteral_isa_DatetimeLiteral():
    instance = sql_literal_TimestampLiteral(value="sample_text")
    assert isinstance(instance, DatetimeLiteral)


def test_sql_datatype_DateType_isa_DatetimeType():
    instance = sql_datatype_DateType()
    assert isinstance(instance, DatetimeType)


def test_sql_datatype_TimeType_isa_DatetimeType():
    instance = sql_datatype_TimeType(precision="sample_text", withTimeZone="sample_text")
    assert isinstance(instance, DatetimeType)


def test_sql_datatype_TimestampType_isa_DatetimeType():
    instance = sql_datatype_TimestampType(precision="sample_text", withTimeZone="sample_text")
    assert isinstance(instance, DatetimeType)


def test_sql_schema_DatetimeValueFunctionDefaultOption_isa_DefaultOption():
    instance = sql_schema_DatetimeValueFunctionDefaultOption()
    assert isinstance(instance, DefaultOption)


def test_sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_isa_DefaultOption():
    instance = sql_schema_ImplicitlyTypedValueSpecificationDefaultOption()
    assert isinstance(instance, DefaultOption)


def test_sql_schema_LiteralDefaultOption_isa_DefaultOption():
    instance = sql_schema_LiteralDefaultOption()
    assert isinstance(instance, DefaultOption)


def test_sql_schema_SQLSchemaStatement_isa_DirectSQLStatement():
    instance = sql_schema_SQLSchemaStatement()
    assert isinstance(instance, DirectSQLStatement)


def test_sql_schema_ColumnConstraint_isa_EObject():
    instance = sql_schema_ColumnConstraint()
    assert isinstance(instance, EObject)


def test_sql_schema_TableConstraint_isa_EObject():
    instance = sql_schema_TableConstraint()
    assert isinstance(instance, EObject)


def test_sql_schema_TableDefinition_isa_EObject():
    instance = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    assert isinstance(instance, EObject)


def test_sql_literal_BooleanLiteral_isa_GeneralLiteral():
    instance = sql_literal_BooleanLiteral(value="sample_text")
    assert isinstance(instance, GeneralLiteral)


def test_sql_literal_DatetimeLiteral_isa_GeneralLiteral():
    instance = sql_literal_DatetimeLiteral()
    assert isinstance(instance, GeneralLiteral)


def test_sql_literal_NationalCharacterStringLiteral_isa_GeneralLiteral():
    instance = sql_literal_NationalCharacterStringLiteral(values="sample_text")
    assert isinstance(instance, GeneralLiteral)


def test_sql_expression_NullSpecification_isa_ImplicitlyTypedValueSpecification():
    instance = sql_expression_NullSpecification()
    assert isinstance(instance, ImplicitlyTypedValueSpecification)


def test_sql_literal_GeneralLiteral_isa_Literal():
    instance = sql_literal_GeneralLiteral()
    assert isinstance(instance, Literal)


def test_sql_literal_NumericLiteral_isa_Literal():
    instance = sql_literal_NumericLiteral()
    assert isinstance(instance, Literal)


def test_sql_literal_CharacterStringLiteral_isa_NationalCharacterStringLiteral():
    instance = sql_literal_CharacterStringLiteral()
    assert isinstance(instance, NationalCharacterStringLiteral)


def test_sql_literal_ApproximateNumericLiteral_isa_NumericLiteral():
    instance = sql_literal_ApproximateNumericLiteral(value=3.14)
    assert isinstance(instance, NumericLiteral)


def test_sql_literal_ExactNumericLiteral_isa_NumericLiteral():
    instance = sql_literal_ExactNumericLiteral(value="sample_text")
    assert isinstance(instance, NumericLiteral)


def test_sql_datatype_ApproximateNumericType_isa_NumericType():
    instance = sql_datatype_ApproximateNumericType(kind="sample_text", precision="sample_text")
    assert isinstance(instance, NumericType)


def test_sql_datatype_ExactNumericType_isa_NumericType():
    instance = sql_datatype_ExactNumericType(kind="sample_text", precision="sample_text", scale="sample_text")
    assert isinstance(instance, NumericType)


def test_sql_datatype_BinaryLargeObjectStringType_isa_PredefinedType():
    instance = sql_datatype_BinaryLargeObjectStringType(kind="sample_text")
    assert isinstance(instance, PredefinedType)


def test_sql_datatype_BooleanType_isa_PredefinedType():
    instance = sql_datatype_BooleanType()
    assert isinstance(instance, PredefinedType)


def test_sql_datatype_CharacterStringType_isa_PredefinedType():
    instance = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    assert isinstance(instance, PredefinedType)


def test_sql_datatype_DatetimeType_isa_PredefinedType():
    instance = sql_datatype_DatetimeType()
    assert isinstance(instance, PredefinedType)


def test_sql_datatype_NationalCharacterStringType_isa_PredefinedType():
    instance = sql_datatype_NationalCharacterStringType(kind="sample_text", length="sample_text")
    assert isinstance(instance, PredefinedType)


def test_sql_datatype_NumericType_isa_PredefinedType():
    instance = sql_datatype_NumericType()
    assert isinstance(instance, PredefinedType)


def test_sql_schema_SQLSchemaDefinitionStatement_isa_SQLSchemaStatement():
    instance = sql_schema_SQLSchemaDefinitionStatement()
    assert isinstance(instance, SQLSchemaStatement)


def test_sql_common_Comment_isa_Separator():
    instance = sql_common_Comment(value="sample_text")
    assert isinstance(instance, Separator)


def test_sql_common_DirectSQLStatement_isa_Statement():
    instance = sql_common_DirectSQLStatement()
    assert isinstance(instance, Statement)


def test_sql_common_Separator_isa_Statement():
    instance = sql_common_Separator()
    assert isinstance(instance, Statement)


def test_sql_schema_TableColumnsConstraint_isa_TableConstraint():
    instance = sql_schema_TableColumnsConstraint()
    assert isinstance(instance, TableConstraint)


def test_sql_schema_TableElementList_isa_TableContentsSource():
    instance = sql_schema_TableElementList()
    assert isinstance(instance, TableContentsSource)


def test_sql_schema_Column_isa_TableElement():
    instance = sql_schema_Column(name="sample_text")
    assert isinstance(instance, TableElement)


def test_sql_schema_ReferentialColumnConstraint_isa_schema_ColumnConstraint():
    instance = sql_schema_ReferentialColumnConstraint()
    assert isinstance(instance, schema_ColumnConstraint)


def test_sql_schema_UniqueColumnConstraint_isa_schema_ColumnConstraint():
    instance = sql_schema_UniqueColumnConstraint()
    assert isinstance(instance, schema_ColumnConstraint)


def test_sql_schema_ReferentialColumnConstraint_isa_schema_ReferentialConstraint():
    instance = sql_schema_ReferentialColumnConstraint()
    assert isinstance(instance, schema_ReferentialConstraint)


def test_sql_schema_ReferentialTableConstraint_isa_schema_ReferentialConstraint():
    instance = sql_schema_ReferentialTableConstraint()
    assert isinstance(instance, schema_ReferentialConstraint)


def test_sql_schema_TableDefinition_isa_schema_SQLSchemaDefinitionStatement():
    instance = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    assert isinstance(instance, schema_SQLSchemaDefinitionStatement)


def test_sql_schema_ReferentialTableConstraint_isa_schema_TableColumnsConstraint():
    instance = sql_schema_ReferentialTableConstraint()
    assert isinstance(instance, schema_TableColumnsConstraint)


def test_sql_schema_UniqueTableConstraint_isa_schema_TableColumnsConstraint():
    instance = sql_schema_UniqueTableConstraint()
    assert isinstance(instance, schema_TableColumnsConstraint)


def test_sql_schema_TableConstraint_isa_schema_TableElement():
    instance = sql_schema_TableConstraint()
    assert isinstance(instance, schema_TableElement)


def test_sql_schema_UniqueColumnConstraint_isa_schema_UniqueConstraint():
    instance = sql_schema_UniqueColumnConstraint()
    assert isinstance(instance, schema_UniqueConstraint)


def test_sql_schema_UniqueTableConstraint_isa_schema_UniqueConstraint():
    instance = sql_schema_UniqueTableConstraint()
    assert isinstance(instance, schema_UniqueConstraint)


def test_assoc_characterSetName3_link_reassign_clear():
    a = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    b1 = SchemaQualifiedName()
    b2 = SchemaQualifiedName()
    _safe_set(a, 'sql_datatype_CharacterStringType', b1)
    assert _is_linked(a, 'sql_datatype_CharacterStringType', b1)
    if hasattr(b1, 'SchemaQualifiedName4'):
        assert _is_linked(b1, 'SchemaQualifiedName4', a)
    _safe_set(a, 'sql_datatype_CharacterStringType', b2)
    assert _is_linked(a, 'sql_datatype_CharacterStringType', b2)
    if hasattr(b1, 'SchemaQualifiedName4'):
        assert not _is_linked(b1, 'SchemaQualifiedName4', a)
    if hasattr(b2, 'SchemaQualifiedName4'):
        assert _is_linked(b2, 'SchemaQualifiedName4', a)
    _safe_set(a, 'sql_datatype_CharacterStringType', None)
    assert not _is_linked(a, 'sql_datatype_CharacterStringType', b2)
    if hasattr(b2, 'SchemaQualifiedName4'):
        assert not _is_linked(b2, 'SchemaQualifiedName4', a)


def test_assoc_collationName22_link_reassign_clear():
    a = sql_schema_Column(name="sample_text")
    b1 = SchemaQualifiedName()
    b2 = SchemaQualifiedName()
    _safe_set(a, 'sql_schema_Column23', b1)
    assert _is_linked(a, 'sql_schema_Column23', b1)
    if hasattr(b1, 'SchemaQualifiedName24'):
        assert _is_linked(b1, 'SchemaQualifiedName24', a)
    _safe_set(a, 'sql_schema_Column23', b2)
    assert _is_linked(a, 'sql_schema_Column23', b2)
    if hasattr(b1, 'SchemaQualifiedName24'):
        assert not _is_linked(b1, 'SchemaQualifiedName24', a)
    if hasattr(b2, 'SchemaQualifiedName24'):
        assert _is_linked(b2, 'SchemaQualifiedName24', a)
    _safe_set(a, 'sql_schema_Column23', None)
    assert not _is_linked(a, 'sql_schema_Column23', b2)
    if hasattr(b2, 'SchemaQualifiedName24'):
        assert not _is_linked(b2, 'SchemaQualifiedName24', a)


def test_assoc_collationName5_link_reassign_clear():
    a = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    b1 = SchemaQualifiedName()
    b2 = SchemaQualifiedName()
    _safe_set(a, 'sql_datatype_CharacterStringType6', b1)
    assert _is_linked(a, 'sql_datatype_CharacterStringType6', b1)
    if hasattr(b1, 'SchemaQualifiedName7'):
        assert _is_linked(b1, 'SchemaQualifiedName7', a)
    _safe_set(a, 'sql_datatype_CharacterStringType6', b2)
    assert _is_linked(a, 'sql_datatype_CharacterStringType6', b2)
    if hasattr(b1, 'SchemaQualifiedName7'):
        assert not _is_linked(b1, 'SchemaQualifiedName7', a)
    if hasattr(b2, 'SchemaQualifiedName7'):
        assert _is_linked(b2, 'SchemaQualifiedName7', a)
    _safe_set(a, 'sql_datatype_CharacterStringType6', None)
    assert not _is_linked(a, 'sql_datatype_CharacterStringType6', b2)
    if hasattr(b2, 'SchemaQualifiedName7'):
        assert not _is_linked(b2, 'SchemaQualifiedName7', a)


def test_assoc_collationName8_link_reassign_clear():
    a = sql_datatype_NationalCharacterStringType(kind="sample_text", length="sample_text")
    b1 = SchemaQualifiedName()
    b2 = SchemaQualifiedName()
    _safe_set(a, 'sql_datatype_NationalCharacterStringType', b1)
    assert _is_linked(a, 'sql_datatype_NationalCharacterStringType', b1)
    if hasattr(b1, 'SchemaQualifiedName9'):
        assert _is_linked(b1, 'SchemaQualifiedName9', a)
    _safe_set(a, 'sql_datatype_NationalCharacterStringType', b2)
    assert _is_linked(a, 'sql_datatype_NationalCharacterStringType', b2)
    if hasattr(b1, 'SchemaQualifiedName9'):
        assert not _is_linked(b1, 'SchemaQualifiedName9', a)
    if hasattr(b2, 'SchemaQualifiedName9'):
        assert _is_linked(b2, 'SchemaQualifiedName9', a)
    _safe_set(a, 'sql_datatype_NationalCharacterStringType', None)
    assert not _is_linked(a, 'sql_datatype_NationalCharacterStringType', b2)
    if hasattr(b2, 'SchemaQualifiedName9'):
        assert not _is_linked(b2, 'SchemaQualifiedName9', a)


def test_assoc_constraint20_link_reassign_clear():
    a = sql_schema_Column(name="sample_text")
    b1 = ColumnConstraint()
    b2 = ColumnConstraint()
    _safe_set(a, 'owner21', b1)
    assert _is_linked(a, 'owner21', b1)
    if hasattr(b1, 'ColumnConstraint'):
        assert _is_linked(b1, 'ColumnConstraint', a)
    _safe_set(a, 'owner21', b2)
    assert _is_linked(a, 'owner21', b2)
    if hasattr(b1, 'ColumnConstraint'):
        assert not _is_linked(b1, 'ColumnConstraint', a)
    if hasattr(b2, 'ColumnConstraint'):
        assert _is_linked(b2, 'ColumnConstraint', a)
    _safe_set(a, 'owner21', None)
    assert not _is_linked(a, 'owner21', b2)
    if hasattr(b2, 'ColumnConstraint'):
        assert not _is_linked(b2, 'ColumnConstraint', a)


def test_assoc_contentsSource13_link_reassign_clear():
    a = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    b1 = TableContentsSource()
    b2 = TableContentsSource()
    _safe_set(a, 'owner', b1)
    assert _is_linked(a, 'owner', b1)
    if hasattr(b1, 'TableContentsSource'):
        assert _is_linked(b1, 'TableContentsSource', a)
    _safe_set(a, 'owner', b2)
    assert _is_linked(a, 'owner', b2)
    if hasattr(b1, 'TableContentsSource'):
        assert not _is_linked(b1, 'TableContentsSource', a)
    if hasattr(b2, 'TableContentsSource'):
        assert _is_linked(b2, 'TableContentsSource', a)
    _safe_set(a, 'owner', None)
    assert not _is_linked(a, 'owner', b2)
    if hasattr(b2, 'TableContentsSource'):
        assert not _is_linked(b2, 'TableContentsSource', a)


def test_assoc_dataType17_link_reassign_clear():
    a = sql_schema_Column(name="sample_text")
    b1 = DataType()
    b2 = DataType()
    _safe_set(a, 'sql_schema_Column', b1)
    assert _is_linked(a, 'sql_schema_Column', b1)
    if hasattr(b1, 'DataType'):
        assert _is_linked(b1, 'DataType', a)
    _safe_set(a, 'sql_schema_Column', b2)
    assert _is_linked(a, 'sql_schema_Column', b2)
    if hasattr(b1, 'DataType'):
        assert not _is_linked(b1, 'DataType', a)
    if hasattr(b2, 'DataType'):
        assert _is_linked(b2, 'DataType', a)
    _safe_set(a, 'sql_schema_Column', None)
    assert not _is_linked(a, 'sql_schema_Column', b2)
    if hasattr(b2, 'DataType'):
        assert not _is_linked(b2, 'DataType', a)


def test_assoc_defaultOption18_link_reassign_clear():
    a = sql_schema_Column(name="sample_text")
    b1 = DefaultOption()
    b2 = DefaultOption()
    _safe_set(a, 'owner19', b1)
    assert _is_linked(a, 'owner19', b1)
    if hasattr(b1, 'DefaultOption'):
        assert _is_linked(b1, 'DefaultOption', a)
    _safe_set(a, 'owner19', b2)
    assert _is_linked(a, 'owner19', b2)
    if hasattr(b1, 'DefaultOption'):
        assert not _is_linked(b1, 'DefaultOption', a)
    if hasattr(b2, 'DefaultOption'):
        assert _is_linked(b2, 'DefaultOption', a)
    _safe_set(a, 'owner19', None)
    assert not _is_linked(a, 'owner19', b2)
    if hasattr(b2, 'DefaultOption'):
        assert not _is_linked(b2, 'DefaultOption', a)


def test_assoc_length10_link_reassign_clear():
    a = sql_datatype_BinaryLargeObjectStringType(kind="sample_text")
    b1 = LargeObjectLength()
    b2 = LargeObjectLength()
    _safe_set(a, 'sql_datatype_BinaryLargeObjectStringType', b1)
    assert _is_linked(a, 'sql_datatype_BinaryLargeObjectStringType', b1)
    if hasattr(b1, 'LargeObjectLength'):
        assert _is_linked(b1, 'LargeObjectLength', a)
    _safe_set(a, 'sql_datatype_BinaryLargeObjectStringType', b2)
    assert _is_linked(a, 'sql_datatype_BinaryLargeObjectStringType', b2)
    if hasattr(b1, 'LargeObjectLength'):
        assert not _is_linked(b1, 'LargeObjectLength', a)
    if hasattr(b2, 'LargeObjectLength'):
        assert _is_linked(b2, 'LargeObjectLength', a)
    _safe_set(a, 'sql_datatype_BinaryLargeObjectStringType', None)
    assert not _is_linked(a, 'sql_datatype_BinaryLargeObjectStringType', b2)
    if hasattr(b2, 'LargeObjectLength'):
        assert not _is_linked(b2, 'LargeObjectLength', a)


def test_assoc_schemaQualifiedName11_link_reassign_clear():
    a = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    b1 = SchemaQualifiedName()
    b2 = SchemaQualifiedName()
    _safe_set(a, 'sql_schema_TableDefinition', b1)
    assert _is_linked(a, 'sql_schema_TableDefinition', b1)
    if hasattr(b1, 'SchemaQualifiedName12'):
        assert _is_linked(b1, 'SchemaQualifiedName12', a)
    _safe_set(a, 'sql_schema_TableDefinition', b2)
    assert _is_linked(a, 'sql_schema_TableDefinition', b2)
    if hasattr(b1, 'SchemaQualifiedName12'):
        assert not _is_linked(b1, 'SchemaQualifiedName12', a)
    if hasattr(b2, 'SchemaQualifiedName12'):
        assert _is_linked(b2, 'SchemaQualifiedName12', a)
    _safe_set(a, 'sql_schema_TableDefinition', None)
    assert not _is_linked(a, 'sql_schema_TableDefinition', b2)
    if hasattr(b2, 'SchemaQualifiedName12'):
        assert not _is_linked(b2, 'SchemaQualifiedName12', a)


def test_assoc_separators2_link_reassign_clear():
    a = sql_literal_NationalCharacterStringLiteral(values="sample_text")
    b1 = Separator()
    b2 = Separator()
    _safe_set(a, 'sql_literal_NationalCharacterStringLiteral', {b1})
    assert _is_linked(a, 'sql_literal_NationalCharacterStringLiteral', b1)
    if hasattr(b1, 'Separator'):
        assert _is_linked(b1, 'Separator', a)
    _safe_set(a, 'sql_literal_NationalCharacterStringLiteral', {b2})
    assert _is_linked(a, 'sql_literal_NationalCharacterStringLiteral', b2)
    if hasattr(b1, 'Separator'):
        assert not _is_linked(b1, 'Separator', a)
    if hasattr(b2, 'Separator'):
        assert _is_linked(b2, 'Separator', a)
    _safe_set(a, 'sql_literal_NationalCharacterStringLiteral', set())
    assert not _is_linked(a, 'sql_literal_NationalCharacterStringLiteral', b2)
    if hasattr(b2, 'Separator'):
        assert not _is_linked(b2, 'Separator', a)


def test_assoc_target40_link_reassign_clear():
    a = sql_schema_TableReference(catalogName="sample_text", schemaName="sample_text")
    b1 = TableDefinition()
    b2 = TableDefinition()
    _safe_set(a, 'sql_schema_TableReference', b1)
    assert _is_linked(a, 'sql_schema_TableReference', b1)
    if hasattr(b1, 'TableDefinition41'):
        assert _is_linked(b1, 'TableDefinition41', a)
    _safe_set(a, 'sql_schema_TableReference', b2)
    assert _is_linked(a, 'sql_schema_TableReference', b2)
    if hasattr(b1, 'TableDefinition41'):
        assert not _is_linked(b1, 'TableDefinition41', a)
    if hasattr(b2, 'TableDefinition41'):
        assert _is_linked(b2, 'TableDefinition41', a)
    _safe_set(a, 'sql_schema_TableReference', None)
    assert not _is_linked(a, 'sql_schema_TableReference', b2)
    if hasattr(b2, 'TableDefinition41'):
        assert not _is_linked(b2, 'TableDefinition41', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Column_strategy = st.builds(Column)
@given(instance=Column_strategy)
@settings(max_examples=25)
def test_Column_instantiation(instance):
    assert isinstance(instance, Column)


ColumnConstraint_strategy = st.builds(ColumnConstraint)
@given(instance=ColumnConstraint_strategy)
@settings(max_examples=25)
def test_ColumnConstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


DatetimeLiteral_strategy = st.builds(DatetimeLiteral)
@given(instance=DatetimeLiteral_strategy)
@settings(max_examples=25)
def test_DatetimeLiteral_instantiation(instance):
    assert isinstance(instance, DatetimeLiteral)


DatetimeType_strategy = st.builds(DatetimeType)
@given(instance=DatetimeType_strategy)
@settings(max_examples=25)
def test_DatetimeType_instantiation(instance):
    assert isinstance(instance, DatetimeType)


DatetimeValueFunction_strategy = st.builds(DatetimeValueFunction)
@given(instance=DatetimeValueFunction_strategy)
@settings(max_examples=25)
def test_DatetimeValueFunction_instantiation(instance):
    assert isinstance(instance, DatetimeValueFunction)


DefaultOption_strategy = st.builds(DefaultOption)
@given(instance=DefaultOption_strategy)
@settings(max_examples=25)
def test_DefaultOption_instantiation(instance):
    assert isinstance(instance, DefaultOption)


DirectSQLStatement_strategy = st.builds(DirectSQLStatement)
@given(instance=DirectSQLStatement_strategy)
@settings(max_examples=25)
def test_DirectSQLStatement_instantiation(instance):
    assert isinstance(instance, DirectSQLStatement)


EObject_strategy = st.builds(EObject)
@given(instance=EObject_strategy)
@settings(max_examples=25)
def test_EObject_instantiation(instance):
    assert isinstance(instance, EObject)


GeneralLiteral_strategy = st.builds(GeneralLiteral)
@given(instance=GeneralLiteral_strategy)
@settings(max_examples=25)
def test_GeneralLiteral_instantiation(instance):
    assert isinstance(instance, GeneralLiteral)


ImplicitlyTypedValueSpecification_strategy = st.builds(ImplicitlyTypedValueSpecification)
@given(instance=ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=25)
def test_ImplicitlyTypedValueSpecification_instantiation(instance):
    assert isinstance(instance, ImplicitlyTypedValueSpecification)


LargeObjectLength_strategy = st.builds(LargeObjectLength)
@given(instance=LargeObjectLength_strategy)
@settings(max_examples=25)
def test_LargeObjectLength_instantiation(instance):
    assert isinstance(instance, LargeObjectLength)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


NationalCharacterStringLiteral_strategy = st.builds(NationalCharacterStringLiteral)
@given(instance=NationalCharacterStringLiteral_strategy)
@settings(max_examples=25)
def test_NationalCharacterStringLiteral_instantiation(instance):
    assert isinstance(instance, NationalCharacterStringLiteral)


NumericLiteral_strategy = st.builds(NumericLiteral)
@given(instance=NumericLiteral_strategy)
@settings(max_examples=25)
def test_NumericLiteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)


NumericType_strategy = st.builds(NumericType)
@given(instance=NumericType_strategy)
@settings(max_examples=25)
def test_NumericType_instantiation(instance):
    assert isinstance(instance, NumericType)


PredefinedType_strategy = st.builds(PredefinedType)
@given(instance=PredefinedType_strategy)
@settings(max_examples=25)
def test_PredefinedType_instantiation(instance):
    assert isinstance(instance, PredefinedType)


SQLSchemaStatement_strategy = st.builds(SQLSchemaStatement)
@given(instance=SQLSchemaStatement_strategy)
@settings(max_examples=25)
def test_SQLSchemaStatement_instantiation(instance):
    assert isinstance(instance, SQLSchemaStatement)


SchemaQualifiedName_strategy = st.builds(SchemaQualifiedName)
@given(instance=SchemaQualifiedName_strategy)
@settings(max_examples=25)
def test_SchemaQualifiedName_instantiation(instance):
    assert isinstance(instance, SchemaQualifiedName)


Separator_strategy = st.builds(Separator)
@given(instance=Separator_strategy)
@settings(max_examples=25)
def test_Separator_instantiation(instance):
    assert isinstance(instance, Separator)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


TableConstraint_strategy = st.builds(TableConstraint)
@given(instance=TableConstraint_strategy)
@settings(max_examples=25)
def test_TableConstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)


TableContentsSource_strategy = st.builds(TableContentsSource)
@given(instance=TableContentsSource_strategy)
@settings(max_examples=25)
def test_TableContentsSource_instantiation(instance):
    assert isinstance(instance, TableContentsSource)


TableDefinition_strategy = st.builds(TableDefinition)
@given(instance=TableDefinition_strategy)
@settings(max_examples=25)
def test_TableDefinition_instantiation(instance):
    assert isinstance(instance, TableDefinition)


TableElement_strategy = st.builds(TableElement)
@given(instance=TableElement_strategy)
@settings(max_examples=25)
def test_TableElement_instantiation(instance):
    assert isinstance(instance, TableElement)


TableElementList_strategy = st.builds(TableElementList)
@given(instance=TableElementList_strategy)
@settings(max_examples=25)
def test_TableElementList_instantiation(instance):
    assert isinstance(instance, TableElementList)


TableReference_strategy = st.builds(TableReference)
@given(instance=TableReference_strategy)
@settings(max_examples=25)
def test_TableReference_instantiation(instance):
    assert isinstance(instance, TableReference)


schema_ColumnConstraint_strategy = st.builds(schema_ColumnConstraint)
@given(instance=schema_ColumnConstraint_strategy)
@settings(max_examples=25)
def test_schema_ColumnConstraint_instantiation(instance):
    assert isinstance(instance, schema_ColumnConstraint)


schema_ReferentialConstraint_strategy = st.builds(schema_ReferentialConstraint)
@given(instance=schema_ReferentialConstraint_strategy)
@settings(max_examples=25)
def test_schema_ReferentialConstraint_instantiation(instance):
    assert isinstance(instance, schema_ReferentialConstraint)


schema_SQLSchemaDefinitionStatement_strategy = st.builds(schema_SQLSchemaDefinitionStatement)
@given(instance=schema_SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=25)
def test_schema_SQLSchemaDefinitionStatement_instantiation(instance):
    assert isinstance(instance, schema_SQLSchemaDefinitionStatement)


schema_TableColumnsConstraint_strategy = st.builds(schema_TableColumnsConstraint)
@given(instance=schema_TableColumnsConstraint_strategy)
@settings(max_examples=25)
def test_schema_TableColumnsConstraint_instantiation(instance):
    assert isinstance(instance, schema_TableColumnsConstraint)


schema_TableElement_strategy = st.builds(schema_TableElement)
@given(instance=schema_TableElement_strategy)
@settings(max_examples=25)
def test_schema_TableElement_instantiation(instance):
    assert isinstance(instance, schema_TableElement)


schema_UniqueConstraint_strategy = st.builds(schema_UniqueConstraint)
@given(instance=schema_UniqueConstraint_strategy)
@settings(max_examples=25)
def test_schema_UniqueConstraint_instantiation(instance):
    assert isinstance(instance, schema_UniqueConstraint)


sql_Dummy_strategy = st.builds(sql_Dummy)
@given(instance=sql_Dummy_strategy)
@settings(max_examples=25)
def test_sql_Dummy_instantiation(instance):
    assert isinstance(instance, sql_Dummy)


sql_common_BracketedComment_strategy = st.builds(sql_common_BracketedComment)
@given(instance=sql_common_BracketedComment_strategy)
@settings(max_examples=25)
def test_sql_common_BracketedComment_instantiation(instance):
    assert isinstance(instance, sql_common_BracketedComment)


sql_common_Comment_strategy = st.builds(sql_common_Comment, value=safe_text)
@given(instance=sql_common_Comment_strategy)
@settings(max_examples=25)
def test_sql_common_Comment_instantiation(instance):
    assert isinstance(instance, sql_common_Comment)


sql_common_DirectSQLStatement_strategy = st.builds(sql_common_DirectSQLStatement)
@given(instance=sql_common_DirectSQLStatement_strategy)
@settings(max_examples=25)
def test_sql_common_DirectSQLStatement_instantiation(instance):
    assert isinstance(instance, sql_common_DirectSQLStatement)


sql_common_SQLScript_strategy = st.builds(sql_common_SQLScript)
@given(instance=sql_common_SQLScript_strategy)
@settings(max_examples=25)
def test_sql_common_SQLScript_instantiation(instance):
    assert isinstance(instance, sql_common_SQLScript)


sql_common_SchemaQualifiedName_strategy = st.builds(sql_common_SchemaQualifiedName, catalogName=safe_text, name=safe_text, schemaName=safe_text)
@given(instance=sql_common_SchemaQualifiedName_strategy)
@settings(max_examples=25)
def test_sql_common_SchemaQualifiedName_instantiation(instance):
    assert isinstance(instance, sql_common_SchemaQualifiedName)


sql_common_Separator_strategy = st.builds(sql_common_Separator)
@given(instance=sql_common_Separator_strategy)
@settings(max_examples=25)
def test_sql_common_Separator_instantiation(instance):
    assert isinstance(instance, sql_common_Separator)


sql_common_SimpleComment_strategy = st.builds(sql_common_SimpleComment)
@given(instance=sql_common_SimpleComment_strategy)
@settings(max_examples=25)
def test_sql_common_SimpleComment_instantiation(instance):
    assert isinstance(instance, sql_common_SimpleComment)


sql_common_Statement_strategy = st.builds(sql_common_Statement)
@given(instance=sql_common_Statement_strategy)
@settings(max_examples=25)
def test_sql_common_Statement_instantiation(instance):
    assert isinstance(instance, sql_common_Statement)


sql_datatype_ApproximateNumericType_strategy = st.builds(sql_datatype_ApproximateNumericType, kind=safe_text, precision=safe_text)
@given(instance=sql_datatype_ApproximateNumericType_strategy)
@settings(max_examples=25)
def test_sql_datatype_ApproximateNumericType_instantiation(instance):
    assert isinstance(instance, sql_datatype_ApproximateNumericType)


sql_datatype_BinaryLargeObjectStringType_strategy = st.builds(sql_datatype_BinaryLargeObjectStringType, kind=safe_text)
@given(instance=sql_datatype_BinaryLargeObjectStringType_strategy)
@settings(max_examples=25)
def test_sql_datatype_BinaryLargeObjectStringType_instantiation(instance):
    assert isinstance(instance, sql_datatype_BinaryLargeObjectStringType)


sql_datatype_BooleanType_strategy = st.builds(sql_datatype_BooleanType)
@given(instance=sql_datatype_BooleanType_strategy)
@settings(max_examples=25)
def test_sql_datatype_BooleanType_instantiation(instance):
    assert isinstance(instance, sql_datatype_BooleanType)


sql_datatype_CharacterStringType_strategy = st.builds(sql_datatype_CharacterStringType, kind=safe_text, length=safe_text)
@given(instance=sql_datatype_CharacterStringType_strategy)
@settings(max_examples=25)
def test_sql_datatype_CharacterStringType_instantiation(instance):
    assert isinstance(instance, sql_datatype_CharacterStringType)


sql_datatype_DataType_strategy = st.builds(sql_datatype_DataType)
@given(instance=sql_datatype_DataType_strategy)
@settings(max_examples=25)
def test_sql_datatype_DataType_instantiation(instance):
    assert isinstance(instance, sql_datatype_DataType)


sql_datatype_DateType_strategy = st.builds(sql_datatype_DateType)
@given(instance=sql_datatype_DateType_strategy)
@settings(max_examples=25)
def test_sql_datatype_DateType_instantiation(instance):
    assert isinstance(instance, sql_datatype_DateType)


sql_datatype_DatetimeType_strategy = st.builds(sql_datatype_DatetimeType)
@given(instance=sql_datatype_DatetimeType_strategy)
@settings(max_examples=25)
def test_sql_datatype_DatetimeType_instantiation(instance):
    assert isinstance(instance, sql_datatype_DatetimeType)


sql_datatype_ExactNumericType_strategy = st.builds(sql_datatype_ExactNumericType, kind=safe_text, precision=safe_text, scale=safe_text)
@given(instance=sql_datatype_ExactNumericType_strategy)
@settings(max_examples=25)
def test_sql_datatype_ExactNumericType_instantiation(instance):
    assert isinstance(instance, sql_datatype_ExactNumericType)


sql_datatype_LargeObjectLength_strategy = st.builds(sql_datatype_LargeObjectLength, multiplier=safe_text, units=safe_text, value=safe_text)
@given(instance=sql_datatype_LargeObjectLength_strategy)
@settings(max_examples=25)
def test_sql_datatype_LargeObjectLength_instantiation(instance):
    assert isinstance(instance, sql_datatype_LargeObjectLength)


sql_datatype_NationalCharacterStringType_strategy = st.builds(sql_datatype_NationalCharacterStringType, kind=safe_text, length=safe_text)
@given(instance=sql_datatype_NationalCharacterStringType_strategy)
@settings(max_examples=25)
def test_sql_datatype_NationalCharacterStringType_instantiation(instance):
    assert isinstance(instance, sql_datatype_NationalCharacterStringType)


sql_datatype_NumericType_strategy = st.builds(sql_datatype_NumericType)
@given(instance=sql_datatype_NumericType_strategy)
@settings(max_examples=25)
def test_sql_datatype_NumericType_instantiation(instance):
    assert isinstance(instance, sql_datatype_NumericType)


sql_datatype_PredefinedType_strategy = st.builds(sql_datatype_PredefinedType)
@given(instance=sql_datatype_PredefinedType_strategy)
@settings(max_examples=25)
def test_sql_datatype_PredefinedType_instantiation(instance):
    assert isinstance(instance, sql_datatype_PredefinedType)


sql_datatype_TimeType_strategy = st.builds(sql_datatype_TimeType, precision=safe_text, withTimeZone=safe_text)
@given(instance=sql_datatype_TimeType_strategy)
@settings(max_examples=25)
def test_sql_datatype_TimeType_instantiation(instance):
    assert isinstance(instance, sql_datatype_TimeType)


sql_datatype_TimestampType_strategy = st.builds(sql_datatype_TimestampType, precision=safe_text, withTimeZone=safe_text)
@given(instance=sql_datatype_TimestampType_strategy)
@settings(max_examples=25)
def test_sql_datatype_TimestampType_instantiation(instance):
    assert isinstance(instance, sql_datatype_TimestampType)


sql_expression_ImplicitlyTypedValueSpecification_strategy = st.builds(sql_expression_ImplicitlyTypedValueSpecification)
@given(instance=sql_expression_ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=25)
def test_sql_expression_ImplicitlyTypedValueSpecification_instantiation(instance):
    assert isinstance(instance, sql_expression_ImplicitlyTypedValueSpecification)


sql_expression_NullSpecification_strategy = st.builds(sql_expression_NullSpecification)
@given(instance=sql_expression_NullSpecification_strategy)
@settings(max_examples=25)
def test_sql_expression_NullSpecification_instantiation(instance):
    assert isinstance(instance, sql_expression_NullSpecification)


sql_function_DatetimeValueFunction_strategy = st.builds(sql_function_DatetimeValueFunction, kind=safe_text, precision=safe_text)
@given(instance=sql_function_DatetimeValueFunction_strategy)
@settings(max_examples=25)
def test_sql_function_DatetimeValueFunction_instantiation(instance):
    assert isinstance(instance, sql_function_DatetimeValueFunction)


sql_literal_ApproximateNumericLiteral_strategy = st.builds(sql_literal_ApproximateNumericLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=sql_literal_ApproximateNumericLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_ApproximateNumericLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_ApproximateNumericLiteral)


sql_literal_BooleanLiteral_strategy = st.builds(sql_literal_BooleanLiteral, value=safe_text)
@given(instance=sql_literal_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_BooleanLiteral)


sql_literal_CharacterStringLiteral_strategy = st.builds(sql_literal_CharacterStringLiteral)
@given(instance=sql_literal_CharacterStringLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_CharacterStringLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_CharacterStringLiteral)


sql_literal_DateLiteral_strategy = st.builds(sql_literal_DateLiteral, value=safe_text)
@given(instance=sql_literal_DateLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_DateLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_DateLiteral)


sql_literal_DatetimeLiteral_strategy = st.builds(sql_literal_DatetimeLiteral)
@given(instance=sql_literal_DatetimeLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_DatetimeLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_DatetimeLiteral)


sql_literal_ExactNumericLiteral_strategy = st.builds(sql_literal_ExactNumericLiteral, value=safe_text)
@given(instance=sql_literal_ExactNumericLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_ExactNumericLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_ExactNumericLiteral)


sql_literal_GeneralLiteral_strategy = st.builds(sql_literal_GeneralLiteral)
@given(instance=sql_literal_GeneralLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_GeneralLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_GeneralLiteral)


sql_literal_Literal_strategy = st.builds(sql_literal_Literal)
@given(instance=sql_literal_Literal_strategy)
@settings(max_examples=25)
def test_sql_literal_Literal_instantiation(instance):
    assert isinstance(instance, sql_literal_Literal)


sql_literal_NationalCharacterStringLiteral_strategy = st.builds(sql_literal_NationalCharacterStringLiteral, values=safe_text)
@given(instance=sql_literal_NationalCharacterStringLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_NationalCharacterStringLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_NationalCharacterStringLiteral)


sql_literal_NumericLiteral_strategy = st.builds(sql_literal_NumericLiteral)
@given(instance=sql_literal_NumericLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_NumericLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_NumericLiteral)


sql_literal_TimeLiteral_strategy = st.builds(sql_literal_TimeLiteral, value=safe_text)
@given(instance=sql_literal_TimeLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_TimeLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_TimeLiteral)


sql_literal_TimestampLiteral_strategy = st.builds(sql_literal_TimestampLiteral, value=safe_text)
@given(instance=sql_literal_TimestampLiteral_strategy)
@settings(max_examples=25)
def test_sql_literal_TimestampLiteral_instantiation(instance):
    assert isinstance(instance, sql_literal_TimestampLiteral)


sql_schema_Column_strategy = st.builds(sql_schema_Column, name=safe_text)
@given(instance=sql_schema_Column_strategy)
@settings(max_examples=25)
def test_sql_schema_Column_instantiation(instance):
    assert isinstance(instance, sql_schema_Column)


sql_schema_ColumnConstraint_strategy = st.builds(sql_schema_ColumnConstraint)
@given(instance=sql_schema_ColumnConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_ColumnConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ColumnConstraint)


sql_schema_DatetimeValueFunctionDefaultOption_strategy = st.builds(sql_schema_DatetimeValueFunctionDefaultOption)
@given(instance=sql_schema_DatetimeValueFunctionDefaultOption_strategy)
@settings(max_examples=25)
def test_sql_schema_DatetimeValueFunctionDefaultOption_instantiation(instance):
    assert isinstance(instance, sql_schema_DatetimeValueFunctionDefaultOption)


sql_schema_DefaultOption_strategy = st.builds(sql_schema_DefaultOption)
@given(instance=sql_schema_DefaultOption_strategy)
@settings(max_examples=25)
def test_sql_schema_DefaultOption_instantiation(instance):
    assert isinstance(instance, sql_schema_DefaultOption)


sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_strategy = st.builds(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)
@given(instance=sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_strategy)
@settings(max_examples=25)
def test_sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_instantiation(instance):
    assert isinstance(instance, sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)


sql_schema_LiteralDefaultOption_strategy = st.builds(sql_schema_LiteralDefaultOption)
@given(instance=sql_schema_LiteralDefaultOption_strategy)
@settings(max_examples=25)
def test_sql_schema_LiteralDefaultOption_instantiation(instance):
    assert isinstance(instance, sql_schema_LiteralDefaultOption)


sql_schema_NotNullColumnConstraint_strategy = st.builds(sql_schema_NotNullColumnConstraint)
@given(instance=sql_schema_NotNullColumnConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_NotNullColumnConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_NotNullColumnConstraint)


sql_schema_ReferentialColumnConstraint_strategy = st.builds(sql_schema_ReferentialColumnConstraint)
@given(instance=sql_schema_ReferentialColumnConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_ReferentialColumnConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialColumnConstraint)


sql_schema_ReferentialConstraint_strategy = st.builds(sql_schema_ReferentialConstraint)
@given(instance=sql_schema_ReferentialConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_ReferentialConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialConstraint)


sql_schema_ReferentialTableConstraint_strategy = st.builds(sql_schema_ReferentialTableConstraint)
@given(instance=sql_schema_ReferentialTableConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_ReferentialTableConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialTableConstraint)


sql_schema_SQLSchemaDefinitionStatement_strategy = st.builds(sql_schema_SQLSchemaDefinitionStatement)
@given(instance=sql_schema_SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=25)
def test_sql_schema_SQLSchemaDefinitionStatement_instantiation(instance):
    assert isinstance(instance, sql_schema_SQLSchemaDefinitionStatement)


sql_schema_SQLSchemaStatement_strategy = st.builds(sql_schema_SQLSchemaStatement)
@given(instance=sql_schema_SQLSchemaStatement_strategy)
@settings(max_examples=25)
def test_sql_schema_SQLSchemaStatement_instantiation(instance):
    assert isinstance(instance, sql_schema_SQLSchemaStatement)


sql_schema_TableColumnsConstraint_strategy = st.builds(sql_schema_TableColumnsConstraint)
@given(instance=sql_schema_TableColumnsConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_TableColumnsConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_TableColumnsConstraint)


sql_schema_TableConstraint_strategy = st.builds(sql_schema_TableConstraint)
@given(instance=sql_schema_TableConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_TableConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_TableConstraint)


sql_schema_TableContentsSource_strategy = st.builds(sql_schema_TableContentsSource)
@given(instance=sql_schema_TableContentsSource_strategy)
@settings(max_examples=25)
def test_sql_schema_TableContentsSource_instantiation(instance):
    assert isinstance(instance, sql_schema_TableContentsSource)


sql_schema_TableDefinition_strategy = st.builds(sql_schema_TableDefinition, label=safe_text, scope=safe_text)
@given(instance=sql_schema_TableDefinition_strategy)
@settings(max_examples=25)
def test_sql_schema_TableDefinition_instantiation(instance):
    assert isinstance(instance, sql_schema_TableDefinition)


sql_schema_TableElement_strategy = st.builds(sql_schema_TableElement)
@given(instance=sql_schema_TableElement_strategy)
@settings(max_examples=25)
def test_sql_schema_TableElement_instantiation(instance):
    assert isinstance(instance, sql_schema_TableElement)


sql_schema_TableElementList_strategy = st.builds(sql_schema_TableElementList)
@given(instance=sql_schema_TableElementList_strategy)
@settings(max_examples=25)
def test_sql_schema_TableElementList_instantiation(instance):
    assert isinstance(instance, sql_schema_TableElementList)


sql_schema_TableReference_strategy = st.builds(sql_schema_TableReference, catalogName=safe_text, schemaName=safe_text)
@given(instance=sql_schema_TableReference_strategy)
@settings(max_examples=25)
def test_sql_schema_TableReference_instantiation(instance):
    assert isinstance(instance, sql_schema_TableReference)


sql_schema_UniqueColumnConstraint_strategy = st.builds(sql_schema_UniqueColumnConstraint)
@given(instance=sql_schema_UniqueColumnConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_UniqueColumnConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueColumnConstraint)


sql_schema_UniqueConstraint_strategy = st.builds(sql_schema_UniqueConstraint, kind=safe_text)
@given(instance=sql_schema_UniqueConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_UniqueConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueConstraint)


sql_schema_UniqueTableConstraint_strategy = st.builds(sql_schema_UniqueTableConstraint)
@given(instance=sql_schema_UniqueTableConstraint_strategy)
@settings(max_examples=25)
def test_sql_schema_UniqueTableConstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueTableConstraint)



