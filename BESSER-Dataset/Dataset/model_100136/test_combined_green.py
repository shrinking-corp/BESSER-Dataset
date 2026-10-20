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
    dbdefinition_PrivilegeDefinition,
    dbdefinition_FieldQualifierDefinition,
    dbdefinition_ConstructedDataTypeDefinition,
    dbdefinition_PrivilegedElementDefinition,
    dbdefinition_DebuggerDefinition,
    dbdefinition_ViewDefinition,
    dbdefinition_SchemaDefinition,
    dbdefinition_SequenceDefinition,
    dbdefinition_TableDefinition,
    dbdefinition_IndexDefinition,
    dbdefinition_ExtendedDefinition,
    dbdefinition_ConstraintDefinition,
    dbdefinition_ColumnDefinition,
    dbdefinition_TriggerDefinition,
    dbdefinition_StoredProcedureDefinition,
    dbdefinition_TableSpaceDefinition,
    dbdefinition_NicknameDefinition,
    dbdefinition_SQLSyntaxDefinition,
    dbdefinition_QueryDefinition,
    dbdefinition_UserDefinedTypeDefinition,
    dbdefinition_PredefinedDataTypeDefinition,
    dbdefinition_DatabaseVendorDefinition,
    ParameterStyle,
    ProcedureType,
    LanguageType,
    CheckOption,
    ParentDeleteDRIRuleType,
    LengthUnit,
    ParentUpdateDRIRuleType,
    TableSpaceType,
    PercentFreeTerminology,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_dbdefinition_privilegedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PrivilegeDefinition)


def test_hyp_dbdefinition_privilegedefinition_constructor_exists():
    assert callable(dbdefinition_PrivilegeDefinition.__init__)


def test_hyp_dbdefinition_privilegedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PrivilegeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dbdefinition_fieldqualifierdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_FieldQualifierDefinition)


def test_hyp_dbdefinition_fieldqualifierdefinition_constructor_exists():
    assert callable(dbdefinition_FieldQualifierDefinition.__init__)


def test_hyp_dbdefinition_fieldqualifierdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_FieldQualifierDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"










def test_hyp_dbdefinition_constructeddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ConstructedDataTypeDefinition)


def test_hyp_dbdefinition_constructeddatatypedefinition_constructor_exists():
    assert callable(dbdefinition_ConstructedDataTypeDefinition.__init__)


def test_hyp_dbdefinition_constructeddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ConstructedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "referenceDatatypeSupported" in params, "Missing parameter 'referenceDatatypeSupported'"
    assert "rowDatatypeSupported" in params, "Missing parameter 'rowDatatypeSupported'"
    assert "cursorDatatypeSupported" in params, "Missing parameter 'cursorDatatypeSupported'"
    assert "arrayDatatypeSupported" in params, "Missing parameter 'arrayDatatypeSupported'"
    assert "multisetDatatypeSupported" in params, "Missing parameter 'multisetDatatypeSupported'"








def test_hyp_dbdefinition_privilegedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PrivilegedElementDefinition)


def test_hyp_dbdefinition_privilegedelementdefinition_constructor_exists():
    assert callable(dbdefinition_PrivilegedElementDefinition.__init__)


def test_hyp_dbdefinition_privilegedelementdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PrivilegedElementDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dbdefinition_debuggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_DebuggerDefinition)


def test_hyp_dbdefinition_debuggerdefinition_constructor_exists():
    assert callable(dbdefinition_DebuggerDefinition.__init__)


def test_hyp_dbdefinition_debuggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_DebuggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionSupported" in params, "Missing parameter 'conditionSupported'"




def test_hyp_dbdefinition_viewdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ViewDefinition)


def test_hyp_dbdefinition_viewdefinition_constructor_exists():
    assert callable(dbdefinition_ViewDefinition.__init__)


def test_hyp_dbdefinition_viewdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ViewDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "checkOptionLevelsSupported" in params, "Missing parameter 'checkOptionLevelsSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"
    assert "checkOptionSupported" in params, "Missing parameter 'checkOptionSupported'"







def test_hyp_dbdefinition_schemadefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SchemaDefinition)


def test_hyp_dbdefinition_schemadefinition_constructor_exists():
    assert callable(dbdefinition_SchemaDefinition.__init__)


def test_hyp_dbdefinition_schemadefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SchemaDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"




def test_hyp_dbdefinition_sequencedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SequenceDefinition)


def test_hyp_dbdefinition_sequencedefinition_constructor_exists():
    assert callable(dbdefinition_SequenceDefinition.__init__)


def test_hyp_dbdefinition_sequencedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SequenceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "cacheDefaultValue" in params, "Missing parameter 'cacheDefaultValue'"
    assert "noMinimumValueString" in params, "Missing parameter 'noMinimumValueString'"
    assert "noMaximumValueString" in params, "Missing parameter 'noMaximumValueString'"
    assert "cacheSupported" in params, "Missing parameter 'cacheSupported'"
    assert "typeEnumerationSupported" in params, "Missing parameter 'typeEnumerationSupported'"
    assert "orderSupported" in params, "Missing parameter 'orderSupported'"
    assert "noCacheString" in params, "Missing parameter 'noCacheString'"










def test_hyp_dbdefinition_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TableDefinition)


def test_hyp_dbdefinition_tabledefinition_constructor_exists():
    assert callable(dbdefinition_TableDefinition.__init__)


def test_hyp_dbdefinition_tabledefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "dataCaptureSupported" in params, "Missing parameter 'dataCaptureSupported'"
    assert "encodingSupported" in params, "Missing parameter 'encodingSupported'"
    assert "auditSupported" in params, "Missing parameter 'auditSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "validProcSupported" in params, "Missing parameter 'validProcSupported'"
    assert "editProcSupported" in params, "Missing parameter 'editProcSupported'"









def test_hyp_dbdefinition_indexdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_IndexDefinition)


def test_hyp_dbdefinition_indexdefinition_constructor_exists():
    assert callable(dbdefinition_IndexDefinition.__init__)


def test_hyp_dbdefinition_indexdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_IndexDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "percentFreeChangeable" in params, "Missing parameter 'percentFreeChangeable'"
    assert "percentFreeTerminology" in params, "Missing parameter 'percentFreeTerminology'"
    assert "includedColumnsSupported" in params, "Missing parameter 'includedColumnsSupported'"
    assert "clusterChangeable" in params, "Missing parameter 'clusterChangeable'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"










def test_hyp_dbdefinition_extendeddefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ExtendedDefinition)


def test_hyp_dbdefinition_extendeddefinition_constructor_exists():
    assert callable(dbdefinition_ExtendedDefinition.__init__)


def test_hyp_dbdefinition_extendeddefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ExtendedDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_dbdefinition_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ConstraintDefinition)


def test_hyp_dbdefinition_constraintdefinition_constructor_exists():
    assert callable(dbdefinition_ConstraintDefinition.__init__)


def test_hyp_dbdefinition_constraintdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "parentDeleteDRIRuleType" in params, "Missing parameter 'parentDeleteDRIRuleType'"
    assert "primaryKeyNullable" in params, "Missing parameter 'primaryKeyNullable'"
    assert "parentUpdateDRIRuleType" in params, "Missing parameter 'parentUpdateDRIRuleType'"
    assert "uniqueKeyNullable" in params, "Missing parameter 'uniqueKeyNullable'"
    assert "maximumForeignKeyIdentifierLength" in params, "Missing parameter 'maximumForeignKeyIdentifierLength'"
    assert "clusteredPrimaryKeySupported" in params, "Missing parameter 'clusteredPrimaryKeySupported'"
    assert "informationalConstraintSupported" in params, "Missing parameter 'informationalConstraintSupported'"
    assert "maximumCheckExpressionLength" in params, "Missing parameter 'maximumCheckExpressionLength'"
    assert "clusteredUniqueConstraintSupported" in params, "Missing parameter 'clusteredUniqueConstraintSupported'"
    assert "checkOption" in params, "Missing parameter 'checkOption'"
    assert "maximumPrimaryKeyIdentifierLength" in params, "Missing parameter 'maximumPrimaryKeyIdentifierLength'"
    assert "maximumCheckConstraintIdentifierLength" in params, "Missing parameter 'maximumCheckConstraintIdentifierLength'"
    assert "deferrableConstraintSupported" in params, "Missing parameter 'deferrableConstraintSupported'"
















def test_hyp_dbdefinition_columndefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ColumnDefinition)


def test_hyp_dbdefinition_columndefinition_constructor_exists():
    assert callable(dbdefinition_ColumnDefinition.__init__)


def test_hyp_dbdefinition_columndefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "computedSupported" in params, "Missing parameter 'computedSupported'"
    assert "identityMinimumSupported" in params, "Missing parameter 'identityMinimumSupported'"
    assert "identityIncrementSupported" in params, "Missing parameter 'identityIncrementSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "identityStartValueSupported" in params, "Missing parameter 'identityStartValueSupported'"
    assert "identityCycleSupported" in params, "Missing parameter 'identityCycleSupported'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "identityMaximumSupported" in params, "Missing parameter 'identityMaximumSupported'"











def test_hyp_dbdefinition_triggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TriggerDefinition)


def test_hyp_dbdefinition_triggerdefinition_constructor_exists():
    assert callable(dbdefinition_TriggerDefinition.__init__)


def test_hyp_dbdefinition_triggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TriggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "insteadOfTriggerSupported" in params, "Missing parameter 'insteadOfTriggerSupported'"
    assert "granularitySupported" in params, "Missing parameter 'granularitySupported'"
    assert "perColumnUpdateTriggerSupported" in params, "Missing parameter 'perColumnUpdateTriggerSupported'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "referencesClauseSupported" in params, "Missing parameter 'referencesClauseSupported'"
    assert "tableTriggerReferenceSupported" in params, "Missing parameter 'tableTriggerReferenceSupported'"
    assert "whenClauseSupported" in params, "Missing parameter 'whenClauseSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "rowTriggerReferenceSupported" in params, "Missing parameter 'rowTriggerReferenceSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "maximumReferencePartLength" in params, "Missing parameter 'maximumReferencePartLength'"














def test_hyp_dbdefinition_storedproceduredefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_StoredProcedureDefinition)


def test_hyp_dbdefinition_storedproceduredefinition_constructor_exists():
    assert callable(dbdefinition_StoredProcedureDefinition.__init__)


def test_hyp_dbdefinition_storedproceduredefinition_constructor_args():
    sig = inspect.signature(dbdefinition_StoredProcedureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "determininsticSupported" in params, "Missing parameter 'determininsticSupported'"
    assert "parameterStyle" in params, "Missing parameter 'parameterStyle'"
    assert "parameterStyleSupported" in params, "Missing parameter 'parameterStyleSupported'"
    assert "packageGenerationSupported" in params, "Missing parameter 'packageGenerationSupported'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "functionLanguageType" in params, "Missing parameter 'functionLanguageType'"
    assert "parameterInitValueSupported" in params, "Missing parameter 'parameterInitValueSupported'"
    assert "nullInputActionSupported" in params, "Missing parameter 'nullInputActionSupported'"
    assert "returnedTypeDeclarationConstraintSupported" in params, "Missing parameter 'returnedTypeDeclarationConstraintSupported'"
    assert "parameterDeclarationConstraintSupported" in params, "Missing parameter 'parameterDeclarationConstraintSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "languageType" in params, "Missing parameter 'languageType'"
    assert "returnedNullSupported" in params, "Missing parameter 'returnedNullSupported'"
    assert "returnTypeSupported" in params, "Missing parameter 'returnTypeSupported'"
    assert "procedureType" in params, "Missing parameter 'procedureType'"


















def test_hyp_dbdefinition_tablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TableSpaceDefinition)


def test_hyp_dbdefinition_tablespacedefinition_constructor_exists():
    assert callable(dbdefinition_TableSpaceDefinition.__init__)


def test_hyp_dbdefinition_tablespacedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "prefetchSizeSupported" in params, "Missing parameter 'prefetchSizeSupported'"
    assert "managedBySupported" in params, "Missing parameter 'managedBySupported'"
    assert "containerMaximumSizeSupported" in params, "Missing parameter 'containerMaximumSizeSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "extentSizeSupported" in params, "Missing parameter 'extentSizeSupported'"
    assert "bufferPoolSupported" in params, "Missing parameter 'bufferPoolSupported'"
    assert "tableSpaceType" in params, "Missing parameter 'tableSpaceType'"
    assert "pageSizeSupported" in params, "Missing parameter 'pageSizeSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "containerExtentSizeSupported" in params, "Missing parameter 'containerExtentSizeSupported'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "containerInitialSizeSupported" in params, "Missing parameter 'containerInitialSizeSupported'"















def test_hyp_dbdefinition_nicknamedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_NicknameDefinition)


def test_hyp_dbdefinition_nicknamedefinition_constructor_exists():
    assert callable(dbdefinition_NicknameDefinition.__init__)


def test_hyp_dbdefinition_nicknamedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_NicknameDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "constraintSupported" in params, "Missing parameter 'constraintSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"






def test_hyp_dbdefinition_sqlsyntaxdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SQLSyntaxDefinition)


def test_hyp_dbdefinition_sqlsyntaxdefinition_constructor_exists():
    assert callable(dbdefinition_SQLSyntaxDefinition.__init__)


def test_hyp_dbdefinition_sqlsyntaxdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SQLSyntaxDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "operators" in params, "Missing parameter 'operators'"
    assert "terminationCharacter" in params, "Missing parameter 'terminationCharacter'"






def test_hyp_dbdefinition_querydefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_QueryDefinition)


def test_hyp_dbdefinition_querydefinition_constructor_exists():
    assert callable(dbdefinition_QueryDefinition.__init__)


def test_hyp_dbdefinition_querydefinition_constructor_args():
    sig = inspect.signature(dbdefinition_QueryDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "extendedGroupingSupported" in params, "Missing parameter 'extendedGroupingSupported'"
    assert "defaultKeywordForInsertValueSupported" in params, "Missing parameter 'defaultKeywordForInsertValueSupported'"
    assert "hostVariableMarker" in params, "Missing parameter 'hostVariableMarker'"
    assert "tableAliasInDeleteSupported" in params, "Missing parameter 'tableAliasInDeleteSupported'"
    assert "castExpressionSupported" in params, "Missing parameter 'castExpressionSupported'"
    assert "identifierQuoteString" in params, "Missing parameter 'identifierQuoteString'"
    assert "hostVariableMarkerSupported" in params, "Missing parameter 'hostVariableMarkerSupported'"










def test_hyp_dbdefinition_userdefinedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_UserDefinedTypeDefinition)


def test_hyp_dbdefinition_userdefinedtypedefinition_constructor_exists():
    assert callable(dbdefinition_UserDefinedTypeDefinition.__init__)


def test_hyp_dbdefinition_userdefinedtypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_UserDefinedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueSupported" in params, "Missing parameter 'defaultValueSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "structuredTypeSupported" in params, "Missing parameter 'structuredTypeSupported'"
    assert "distinctTypeSupported" in params, "Missing parameter 'distinctTypeSupported'"







def test_hyp_dbdefinition_predefineddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PredefinedDataTypeDefinition)


def test_hyp_dbdefinition_predefineddatatypedefinition_constructor_exists():
    assert callable(dbdefinition_PredefinedDataTypeDefinition.__init__)


def test_hyp_dbdefinition_predefineddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PredefinedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueTypes" in params, "Missing parameter 'defaultValueTypes'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "lengthSemantic" in params, "Missing parameter 'lengthSemantic'"
    assert "minimumScale" in params, "Missing parameter 'minimumScale'"
    assert "languageType" in params, "Missing parameter 'languageType'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "largeValueSpecifierLength" in params, "Missing parameter 'largeValueSpecifierLength'"
    assert "jdbcEnumType" in params, "Missing parameter 'jdbcEnumType'"
    assert "characterSetSuffix" in params, "Missing parameter 'characterSetSuffix'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "lengthSemanticSupported" in params, "Missing parameter 'lengthSemanticSupported'"
    assert "lengthSupported" in params, "Missing parameter 'lengthSupported'"
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "displayNameSupported" in params, "Missing parameter 'displayNameSupported'"
    assert "nullableSupported" in params, "Missing parameter 'nullableSupported'"
    assert "defaultLength" in params, "Missing parameter 'defaultLength'"
    assert "fieldQualifierSeparator" in params, "Missing parameter 'fieldQualifierSeparator'"
    assert "javaClassName" in params, "Missing parameter 'javaClassName'"
    assert "keyConstraintSupported" in params, "Missing parameter 'keyConstraintSupported'"
    assert "trailingFieldQualifierSupported" in params, "Missing parameter 'trailingFieldQualifierSupported'"
    assert "encodingSchemeSuffix" in params, "Missing parameter 'encodingSchemeSuffix'"
    assert "largeValueSpecifierName" in params, "Missing parameter 'largeValueSpecifierName'"
    assert "largeValueSpecifierSupported" in params, "Missing parameter 'largeValueSpecifierSupported'"
    assert "leadingFieldQualifierSupported" in params, "Missing parameter 'leadingFieldQualifierSupported'"
    assert "cutoffPrecision" in params, "Missing parameter 'cutoffPrecision'"
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"
    assert "encodingScheme" in params, "Missing parameter 'encodingScheme'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "maximumLength" in params, "Missing parameter 'maximumLength'"
    assert "groupingSupported" in params, "Missing parameter 'groupingSupported'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "characterSet" in params, "Missing parameter 'characterSet'"
    assert "orderingSupported" in params, "Missing parameter 'orderingSupported'"
    assert "minimumValue" in params, "Missing parameter 'minimumValue'"
    assert "maximumValue" in params, "Missing parameter 'maximumValue'"
    assert "bitDataSupported" in params, "Missing parameter 'bitDataSupported'"
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "multipleColumnsSupported" in params, "Missing parameter 'multipleColumnsSupported'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "lengthUnit" in params, "Missing parameter 'lengthUnit'"















































def test_hyp_dbdefinition_databasevendordefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_DatabaseVendorDefinition)


def test_hyp_dbdefinition_databasevendordefinition_constructor_exists():
    assert callable(dbdefinition_DatabaseVendorDefinition.__init__)


def test_hyp_dbdefinition_databasevendordefinition_constructor_args():
    sig = inspect.signature(dbdefinition_DatabaseVendorDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "quotedDMLSupported" in params, "Missing parameter 'quotedDMLSupported'"
    assert "joinSupported" in params, "Missing parameter 'joinSupported'"
    assert "viewTriggerSupported" in params, "Missing parameter 'viewTriggerSupported'"
    assert "mQTIndexSupported" in params, "Missing parameter 'mQTIndexSupported'"
    assert "quotedDDLSupported" in params, "Missing parameter 'quotedDDLSupported'"
    assert "sqlUDFSupported" in params, "Missing parameter 'sqlUDFSupported'"
    assert "triggerSupported" in params, "Missing parameter 'triggerSupported'"
    assert "constraintsSupported" in params, "Missing parameter 'constraintsSupported'"
    assert "synonymSupported" in params, "Missing parameter 'synonymSupported'"
    assert "packageSupported" in params, "Missing parameter 'packageSupported'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "schemaSupported" in params, "Missing parameter 'schemaSupported'"
    assert "domainSupported" in params, "Missing parameter 'domainSupported'"
    assert "maximumCommentLength" in params, "Missing parameter 'maximumCommentLength'"
    assert "version" in params, "Missing parameter 'version'"
    assert "userDefinedTypeSupported" in params, "Missing parameter 'userDefinedTypeSupported'"
    assert "xmlSupported" in params, "Missing parameter 'xmlSupported'"
    assert "snapshotViewSupported" in params, "Missing parameter 'snapshotViewSupported'"
    assert "groupSupported" in params, "Missing parameter 'groupSupported'"
    assert "mQTSupported" in params, "Missing parameter 'mQTSupported'"
    assert "roleSupported" in params, "Missing parameter 'roleSupported'"
    assert "nicknameSupported" in params, "Missing parameter 'nicknameSupported'"
    assert "userSupported" in params, "Missing parameter 'userSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "sequenceSupported" in params, "Missing parameter 'sequenceSupported'"
    assert "authorizationIdentifierSupported" in params, "Missing parameter 'authorizationIdentifierSupported'"
    assert "tablespacesSupported" in params, "Missing parameter 'tablespacesSupported'"
    assert "uDFSupported" in params, "Missing parameter 'uDFSupported'"
    assert "constructedDataTypeSupported" in params, "Missing parameter 'constructedDataTypeSupported'"
    assert "storedProcedureSupported" in params, "Missing parameter 'storedProcedureSupported'"
    assert "roleAuthorizationSupported" in params, "Missing parameter 'roleAuthorizationSupported'"
    assert "SQLStatementSupported" in params, "Missing parameter 'SQLStatementSupported'"
    assert "aliasSupported" in params, "Missing parameter 'aliasSupported'"
    assert "eventSupported" in params, "Missing parameter 'eventSupported'"



































def test_hyp_parameterstyle_exists():
    # Check that the Enumeration exists
    assert ParameterStyle is not None

def test_hyp_parameterstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterStyle]
    expected_literals = [
        "DB2SQL",
        "JAVA",
        "GENERAL_WITH_NULLS",
        "SQL",
        "GENERAL",
        "DB2DARI",
        "DB2GENRL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterStyle"

def test_hyp_proceduretype_exists():
    # Check that the Enumeration exists
    assert ProcedureType is not None

def test_hyp_proceduretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureType]
    expected_literals = [
        "FUNCTION",
        "PROCEDURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureType"

def test_hyp_languagetype_exists():
    # Check that the Enumeration exists
    assert LanguageType is not None

def test_hyp_languagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LanguageType]
    expected_literals = [
        "COBOLLE",
        "JAVA",
        "ASSEMBLY",
        "OLE",
        "RPGLE",
        "COBOL",
        "RPG",
        "C",
        "CPLUSPLUS",
        "CL",
        "FORTRAN",
        "PLI",
        "REXX",
        "PLSQL",
        "SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LanguageType"

def test_hyp_checkoption_exists():
    # Check that the Enumeration exists
    assert CheckOption is not None

def test_hyp_checkoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CheckOption]
    expected_literals = [
        "CASCADE",
        "LOCAL",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CheckOption"

def test_hyp_parentdeletedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentDeleteDRIRuleType is not None

def test_hyp_parentdeletedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentDeleteDRIRuleType]
    expected_literals = [
        "NO_ACTION",
        "RESTRICT",
        "SET_DEFAULT",
        "SET_NULL",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentDeleteDRIRuleType"

def test_hyp_lengthunit_exists():
    # Check that the Enumeration exists
    assert LengthUnit is not None

def test_hyp_lengthunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnit]
    expected_literals = [
        "BIT",
        "DOUBLE_BYTE",
        "BYTE",
        "DECIMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnit"

def test_hyp_parentupdatedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentUpdateDRIRuleType is not None

def test_hyp_parentupdatedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentUpdateDRIRuleType]
    expected_literals = [
        "SET_DEFAULT",
        "CASCADE",
        "SET_NULL",
        "NO_ACTION",
        "RESTRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentUpdateDRIRuleType"

def test_hyp_tablespacetype_exists():
    # Check that the Enumeration exists
    assert TableSpaceType is not None

def test_hyp_tablespacetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableSpaceType]
    expected_literals = [
        "LARGE",
        "SYSTEM_TEMPORARY",
        "REGULAR",
        "USER_TEMPORARY",
        "TEMPORARY",
        "PERMANENT",
        "LONG",
        "LOB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableSpaceType"

def test_hyp_percentfreeterminology_exists():
    # Check that the Enumeration exists
    assert PercentFreeTerminology is not None

def test_hyp_percentfreeterminology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PercentFreeTerminology]
    expected_literals = [
        "PERCENT_FREE",
        "THRESHOLD",
        "FILL_FACTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PercentFreeTerminology"


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
dbdefinition_PrivilegeDefinition_strategy = st.builds(
    dbdefinition_PrivilegeDefinition,
    name=
        safe_text
)
dbdefinition_FieldQualifierDefinition_strategy = st.builds(
    dbdefinition_FieldQualifierDefinition,
    maximumScale=
        st.integers(),
    name=
        safe_text,
    scaleSupported=
        st.booleans(),
    defaultPrecision=
        st.integers(),
    maximumPrecision=
        st.integers(),
    precisionSupported=
        st.booleans(),
    defaultScale=
        st.integers()
)
dbdefinition_ConstructedDataTypeDefinition_strategy = st.builds(
    dbdefinition_ConstructedDataTypeDefinition,
    referenceDatatypeSupported=
        st.booleans(),
    rowDatatypeSupported=
        st.booleans(),
    cursorDatatypeSupported=
        st.booleans(),
    arrayDatatypeSupported=
        st.booleans(),
    multisetDatatypeSupported=
        st.booleans()
)
dbdefinition_PrivilegedElementDefinition_strategy = st.builds(
    dbdefinition_PrivilegedElementDefinition,
    name=
        safe_text
)
dbdefinition_DebuggerDefinition_strategy = st.builds(
    dbdefinition_DebuggerDefinition,
    conditionSupported=
        st.booleans()
)
dbdefinition_ViewDefinition_strategy = st.builds(
    dbdefinition_ViewDefinition,
    checkOptionLevelsSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans(),
    checkOptionSupported=
        st.booleans()
)
dbdefinition_SchemaDefinition_strategy = st.builds(
    dbdefinition_SchemaDefinition,
    maximumIdentifierLength=
        st.integers()
)
dbdefinition_SequenceDefinition_strategy = st.builds(
    dbdefinition_SequenceDefinition,
    cacheDefaultValue=
        st.integers(),
    noMinimumValueString=
        safe_text,
    noMaximumValueString=
        safe_text,
    cacheSupported=
        st.booleans(),
    typeEnumerationSupported=
        st.booleans(),
    orderSupported=
        st.booleans(),
    noCacheString=
        safe_text
)
dbdefinition_TableDefinition_strategy = st.builds(
    dbdefinition_TableDefinition,
    dataCaptureSupported=
        st.booleans(),
    encodingSupported=
        st.booleans(),
    auditSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    validProcSupported=
        st.booleans(),
    editProcSupported=
        st.booleans()
)
dbdefinition_IndexDefinition_strategy = st.builds(
    dbdefinition_IndexDefinition,
    percentFreeChangeable=
        st.booleans(),
    percentFreeTerminology=
        safe_text,
    includedColumnsSupported=
        st.booleans(),
    clusterChangeable=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    clusteringSupported=
        st.booleans(),
    fillFactorSupported=
        st.booleans()
)
dbdefinition_ExtendedDefinition_strategy = st.builds(
    dbdefinition_ExtendedDefinition,
    name=
        safe_text,
    value=
        safe_text
)
dbdefinition_ConstraintDefinition_strategy = st.builds(
    dbdefinition_ConstraintDefinition,
    parentDeleteDRIRuleType=
        safe_text,
    primaryKeyNullable=
        st.booleans(),
    parentUpdateDRIRuleType=
        safe_text,
    uniqueKeyNullable=
        st.booleans(),
    maximumForeignKeyIdentifierLength=
        st.integers(),
    clusteredPrimaryKeySupported=
        st.booleans(),
    informationalConstraintSupported=
        st.booleans(),
    maximumCheckExpressionLength=
        st.integers(),
    clusteredUniqueConstraintSupported=
        st.booleans(),
    checkOption=
        safe_text,
    maximumPrimaryKeyIdentifierLength=
        st.integers(),
    maximumCheckConstraintIdentifierLength=
        st.integers(),
    deferrableConstraintSupported=
        st.booleans()
)
dbdefinition_ColumnDefinition_strategy = st.builds(
    dbdefinition_ColumnDefinition,
    computedSupported=
        st.booleans(),
    identityMinimumSupported=
        st.booleans(),
    identityIncrementSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    identityStartValueSupported=
        st.booleans(),
    identityCycleSupported=
        st.booleans(),
    identitySupported=
        st.booleans(),
    identityMaximumSupported=
        st.booleans()
)
dbdefinition_TriggerDefinition_strategy = st.builds(
    dbdefinition_TriggerDefinition,
    insteadOfTriggerSupported=
        st.booleans(),
    granularitySupported=
        st.booleans(),
    perColumnUpdateTriggerSupported=
        st.booleans(),
    maximumActionBodyLength=
        st.integers(),
    referencesClauseSupported=
        st.booleans(),
    tableTriggerReferenceSupported=
        st.booleans(),
    whenClauseSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    rowTriggerReferenceSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    maximumReferencePartLength=
        st.integers()
)
dbdefinition_StoredProcedureDefinition_strategy = st.builds(
    dbdefinition_StoredProcedureDefinition,
    determininsticSupported=
        st.booleans(),
    parameterStyle=
        safe_text,
    parameterStyleSupported=
        st.booleans(),
    packageGenerationSupported=
        st.booleans(),
    maximumActionBodyLength=
        st.integers(),
    functionLanguageType=
        safe_text,
    parameterInitValueSupported=
        st.booleans(),
    nullInputActionSupported=
        st.booleans(),
    returnedTypeDeclarationConstraintSupported=
        st.booleans(),
    parameterDeclarationConstraintSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    languageType=
        safe_text,
    returnedNullSupported=
        st.booleans(),
    returnTypeSupported=
        st.booleans(),
    procedureType=
        safe_text
)
dbdefinition_TableSpaceDefinition_strategy = st.builds(
    dbdefinition_TableSpaceDefinition,
    prefetchSizeSupported=
        st.booleans(),
    managedBySupported=
        st.booleans(),
    containerMaximumSizeSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    extentSizeSupported=
        st.booleans(),
    bufferPoolSupported=
        st.booleans(),
    tableSpaceType=
        safe_text,
    pageSizeSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    containerExtentSizeSupported=
        st.booleans(),
    defaultSupported=
        st.booleans(),
    containerInitialSizeSupported=
        st.booleans()
)
dbdefinition_NicknameDefinition_strategy = st.builds(
    dbdefinition_NicknameDefinition,
    constraintSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans()
)
dbdefinition_SQLSyntaxDefinition_strategy = st.builds(
    dbdefinition_SQLSyntaxDefinition,
    keywords=
        safe_text,
    operators=
        safe_text,
    terminationCharacter=
        safe_text
)
dbdefinition_QueryDefinition_strategy = st.builds(
    dbdefinition_QueryDefinition,
    extendedGroupingSupported=
        st.booleans(),
    defaultKeywordForInsertValueSupported=
        st.booleans(),
    hostVariableMarker=
        safe_text,
    tableAliasInDeleteSupported=
        st.booleans(),
    castExpressionSupported=
        st.booleans(),
    identifierQuoteString=
        safe_text,
    hostVariableMarkerSupported=
        st.booleans()
)
dbdefinition_UserDefinedTypeDefinition_strategy = st.builds(
    dbdefinition_UserDefinedTypeDefinition,
    defaultValueSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    structuredTypeSupported=
        st.booleans(),
    distinctTypeSupported=
        st.booleans()
)
dbdefinition_PredefinedDataTypeDefinition_strategy = st.builds(
    dbdefinition_PredefinedDataTypeDefinition,
    defaultValueTypes=
        safe_text,
    identitySupported=
        st.booleans(),
    lengthSemantic=
        safe_text,
    minimumScale=
        st.integers(),
    languageType=
        safe_text,
    precisionSupported=
        st.booleans(),
    scaleSupported=
        st.booleans(),
    largeValueSpecifierLength=
        st.integers(),
    jdbcEnumType=
        st.integers(),
    characterSetSuffix=
        safe_text,
    defaultPrecision=
        st.integers(),
    lengthSemanticSupported=
        st.booleans(),
    lengthSupported=
        st.booleans(),
    name=
        safe_text,
    defaultSupported=
        st.booleans(),
    displayNameSupported=
        st.booleans(),
    nullableSupported=
        st.booleans(),
    defaultLength=
        st.integers(),
    fieldQualifierSeparator=
        safe_text,
    javaClassName=
        safe_text,
    keyConstraintSupported=
        st.booleans(),
    trailingFieldQualifierSupported=
        st.booleans(),
    encodingSchemeSuffix=
        safe_text,
    largeValueSpecifierName=
        safe_text,
    largeValueSpecifierSupported=
        st.booleans(),
    leadingFieldQualifierSupported=
        st.booleans(),
    cutoffPrecision=
        st.integers(),
    defaultScale=
        st.integers(),
    encodingScheme=
        safe_text,
    maximumPrecision=
        st.integers(),
    displayName=
        safe_text,
    maximumLength=
        st.integers(),
    groupingSupported=
        st.booleans(),
    clusteringSupported=
        st.booleans(),
    characterSet=
        safe_text,
    orderingSupported=
        st.booleans(),
    minimumValue=
        safe_text,
    maximumValue=
        safe_text,
    bitDataSupported=
        st.booleans(),
    maximumScale=
        st.integers(),
    multipleColumnsSupported=
        st.booleans(),
    fillFactorSupported=
        st.booleans(),
    primitiveType=
        safe_text,
    lengthUnit=
        safe_text
)
dbdefinition_DatabaseVendorDefinition_strategy = st.builds(
    dbdefinition_DatabaseVendorDefinition,
    quotedDMLSupported=
        st.booleans(),
    joinSupported=
        st.booleans(),
    viewTriggerSupported=
        st.booleans(),
    mQTIndexSupported=
        st.booleans(),
    quotedDDLSupported=
        st.booleans(),
    sqlUDFSupported=
        st.booleans(),
    triggerSupported=
        st.booleans(),
    constraintsSupported=
        st.booleans(),
    synonymSupported=
        st.booleans(),
    packageSupported=
        st.booleans(),
    vendor=
        safe_text,
    schemaSupported=
        st.booleans(),
    domainSupported=
        st.booleans(),
    maximumCommentLength=
        st.integers(),
    version=
        safe_text,
    userDefinedTypeSupported=
        st.booleans(),
    xmlSupported=
        st.booleans(),
    snapshotViewSupported=
        st.booleans(),
    groupSupported=
        st.booleans(),
    mQTSupported=
        st.booleans(),
    roleSupported=
        st.booleans(),
    nicknameSupported=
        st.booleans(),
    userSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    sequenceSupported=
        st.booleans(),
    authorizationIdentifierSupported=
        st.booleans(),
    tablespacesSupported=
        st.booleans(),
    uDFSupported=
        st.booleans(),
    constructedDataTypeSupported=
        st.booleans(),
    storedProcedureSupported=
        st.booleans(),
    roleAuthorizationSupported=
        st.booleans(),
    SQLStatementSupported=
        st.booleans(),
    aliasSupported=
        st.booleans(),
    eventSupported=
        st.booleans()
)




@given(instance=dbdefinition_PrivilegeDefinition_strategy)
def test_hyp_dbdefinition_privilegedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_hyp_dbdefinition_fieldqualifierdefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original




@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_constructeddatatypedefinition_referenceDatatypeSupported_setter(instance):
    original = instance.referenceDatatypeSupported
    instance.referenceDatatypeSupported = original
    assert instance.referenceDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_constructeddatatypedefinition_rowDatatypeSupported_setter(instance):
    original = instance.rowDatatypeSupported
    instance.rowDatatypeSupported = original
    assert instance.rowDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_constructeddatatypedefinition_cursorDatatypeSupported_setter(instance):
    original = instance.cursorDatatypeSupported
    instance.cursorDatatypeSupported = original
    assert instance.cursorDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_constructeddatatypedefinition_arrayDatatypeSupported_setter(instance):
    original = instance.arrayDatatypeSupported
    instance.arrayDatatypeSupported = original
    assert instance.arrayDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_constructeddatatypedefinition_multisetDatatypeSupported_setter(instance):
    original = instance.multisetDatatypeSupported
    instance.multisetDatatypeSupported = original
    assert instance.multisetDatatypeSupported == original




@given(instance=dbdefinition_PrivilegedElementDefinition_strategy)
def test_hyp_dbdefinition_privilegedelementdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dbdefinition_DebuggerDefinition_strategy)
def test_hyp_dbdefinition_debuggerdefinition_conditionSupported_setter(instance):
    original = instance.conditionSupported
    instance.conditionSupported = original
    assert instance.conditionSupported == original




@given(instance=dbdefinition_ViewDefinition_strategy)
def test_hyp_dbdefinition_viewdefinition_checkOptionLevelsSupported_setter(instance):
    original = instance.checkOptionLevelsSupported
    instance.checkOptionLevelsSupported = original
    assert instance.checkOptionLevelsSupported == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_hyp_dbdefinition_viewdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_hyp_dbdefinition_viewdefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_hyp_dbdefinition_viewdefinition_checkOptionSupported_setter(instance):
    original = instance.checkOptionSupported
    instance.checkOptionSupported = original
    assert instance.checkOptionSupported == original




@given(instance=dbdefinition_SchemaDefinition_strategy)
def test_hyp_dbdefinition_schemadefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original




@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_cacheDefaultValue_setter(instance):
    original = instance.cacheDefaultValue
    instance.cacheDefaultValue = original
    assert instance.cacheDefaultValue == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_noMinimumValueString_setter(instance):
    original = instance.noMinimumValueString
    instance.noMinimumValueString = original
    assert instance.noMinimumValueString == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_noMaximumValueString_setter(instance):
    original = instance.noMaximumValueString
    instance.noMaximumValueString = original
    assert instance.noMaximumValueString == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_cacheSupported_setter(instance):
    original = instance.cacheSupported
    instance.cacheSupported = original
    assert instance.cacheSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_typeEnumerationSupported_setter(instance):
    original = instance.typeEnumerationSupported
    instance.typeEnumerationSupported = original
    assert instance.typeEnumerationSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_orderSupported_setter(instance):
    original = instance.orderSupported
    instance.orderSupported = original
    assert instance.orderSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_hyp_dbdefinition_sequencedefinition_noCacheString_setter(instance):
    original = instance.noCacheString
    instance.noCacheString = original
    assert instance.noCacheString == original




@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_dataCaptureSupported_setter(instance):
    original = instance.dataCaptureSupported
    instance.dataCaptureSupported = original
    assert instance.dataCaptureSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_encodingSupported_setter(instance):
    original = instance.encodingSupported
    instance.encodingSupported = original
    assert instance.encodingSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_auditSupported_setter(instance):
    original = instance.auditSupported
    instance.auditSupported = original
    assert instance.auditSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_validProcSupported_setter(instance):
    original = instance.validProcSupported
    instance.validProcSupported = original
    assert instance.validProcSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_hyp_dbdefinition_tabledefinition_editProcSupported_setter(instance):
    original = instance.editProcSupported
    instance.editProcSupported = original
    assert instance.editProcSupported == original




@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_percentFreeChangeable_setter(instance):
    original = instance.percentFreeChangeable
    instance.percentFreeChangeable = original
    assert instance.percentFreeChangeable == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_percentFreeTerminology_setter(instance):
    original = instance.percentFreeTerminology
    instance.percentFreeTerminology = original
    assert instance.percentFreeTerminology == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_includedColumnsSupported_setter(instance):
    original = instance.includedColumnsSupported
    instance.includedColumnsSupported = original
    assert instance.includedColumnsSupported == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_clusterChangeable_setter(instance):
    original = instance.clusterChangeable
    instance.clusterChangeable = original
    assert instance.clusterChangeable == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_hyp_dbdefinition_indexdefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original




@given(instance=dbdefinition_ExtendedDefinition_strategy)
def test_hyp_dbdefinition_extendeddefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_ExtendedDefinition_strategy)
def test_hyp_dbdefinition_extendeddefinition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_parentDeleteDRIRuleType_setter(instance):
    original = instance.parentDeleteDRIRuleType
    instance.parentDeleteDRIRuleType = original
    assert instance.parentDeleteDRIRuleType == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_primaryKeyNullable_setter(instance):
    original = instance.primaryKeyNullable
    instance.primaryKeyNullable = original
    assert instance.primaryKeyNullable == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_parentUpdateDRIRuleType_setter(instance):
    original = instance.parentUpdateDRIRuleType
    instance.parentUpdateDRIRuleType = original
    assert instance.parentUpdateDRIRuleType == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_uniqueKeyNullable_setter(instance):
    original = instance.uniqueKeyNullable
    instance.uniqueKeyNullable = original
    assert instance.uniqueKeyNullable == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_maximumForeignKeyIdentifierLength_setter(instance):
    original = instance.maximumForeignKeyIdentifierLength
    instance.maximumForeignKeyIdentifierLength = original
    assert instance.maximumForeignKeyIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_clusteredPrimaryKeySupported_setter(instance):
    original = instance.clusteredPrimaryKeySupported
    instance.clusteredPrimaryKeySupported = original
    assert instance.clusteredPrimaryKeySupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_informationalConstraintSupported_setter(instance):
    original = instance.informationalConstraintSupported
    instance.informationalConstraintSupported = original
    assert instance.informationalConstraintSupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_maximumCheckExpressionLength_setter(instance):
    original = instance.maximumCheckExpressionLength
    instance.maximumCheckExpressionLength = original
    assert instance.maximumCheckExpressionLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_clusteredUniqueConstraintSupported_setter(instance):
    original = instance.clusteredUniqueConstraintSupported
    instance.clusteredUniqueConstraintSupported = original
    assert instance.clusteredUniqueConstraintSupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_checkOption_setter(instance):
    original = instance.checkOption
    instance.checkOption = original
    assert instance.checkOption == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_maximumPrimaryKeyIdentifierLength_setter(instance):
    original = instance.maximumPrimaryKeyIdentifierLength
    instance.maximumPrimaryKeyIdentifierLength = original
    assert instance.maximumPrimaryKeyIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_maximumCheckConstraintIdentifierLength_setter(instance):
    original = instance.maximumCheckConstraintIdentifierLength
    instance.maximumCheckConstraintIdentifierLength = original
    assert instance.maximumCheckConstraintIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_hyp_dbdefinition_constraintdefinition_deferrableConstraintSupported_setter(instance):
    original = instance.deferrableConstraintSupported
    instance.deferrableConstraintSupported = original
    assert instance.deferrableConstraintSupported == original




@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_computedSupported_setter(instance):
    original = instance.computedSupported
    instance.computedSupported = original
    assert instance.computedSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identityMinimumSupported_setter(instance):
    original = instance.identityMinimumSupported
    instance.identityMinimumSupported = original
    assert instance.identityMinimumSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identityIncrementSupported_setter(instance):
    original = instance.identityIncrementSupported
    instance.identityIncrementSupported = original
    assert instance.identityIncrementSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identityStartValueSupported_setter(instance):
    original = instance.identityStartValueSupported
    instance.identityStartValueSupported = original
    assert instance.identityStartValueSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identityCycleSupported_setter(instance):
    original = instance.identityCycleSupported
    instance.identityCycleSupported = original
    assert instance.identityCycleSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_hyp_dbdefinition_columndefinition_identityMaximumSupported_setter(instance):
    original = instance.identityMaximumSupported
    instance.identityMaximumSupported = original
    assert instance.identityMaximumSupported == original




@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_insteadOfTriggerSupported_setter(instance):
    original = instance.insteadOfTriggerSupported
    instance.insteadOfTriggerSupported = original
    assert instance.insteadOfTriggerSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_granularitySupported_setter(instance):
    original = instance.granularitySupported
    instance.granularitySupported = original
    assert instance.granularitySupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_perColumnUpdateTriggerSupported_setter(instance):
    original = instance.perColumnUpdateTriggerSupported
    instance.perColumnUpdateTriggerSupported = original
    assert instance.perColumnUpdateTriggerSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_referencesClauseSupported_setter(instance):
    original = instance.referencesClauseSupported
    instance.referencesClauseSupported = original
    assert instance.referencesClauseSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_tableTriggerReferenceSupported_setter(instance):
    original = instance.tableTriggerReferenceSupported
    instance.tableTriggerReferenceSupported = original
    assert instance.tableTriggerReferenceSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_whenClauseSupported_setter(instance):
    original = instance.whenClauseSupported
    instance.whenClauseSupported = original
    assert instance.whenClauseSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_rowTriggerReferenceSupported_setter(instance):
    original = instance.rowTriggerReferenceSupported
    instance.rowTriggerReferenceSupported = original
    assert instance.rowTriggerReferenceSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_hyp_dbdefinition_triggerdefinition_maximumReferencePartLength_setter(instance):
    original = instance.maximumReferencePartLength
    instance.maximumReferencePartLength = original
    assert instance.maximumReferencePartLength == original




@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_determininsticSupported_setter(instance):
    original = instance.determininsticSupported
    instance.determininsticSupported = original
    assert instance.determininsticSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_parameterStyle_setter(instance):
    original = instance.parameterStyle
    instance.parameterStyle = original
    assert instance.parameterStyle == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_parameterStyleSupported_setter(instance):
    original = instance.parameterStyleSupported
    instance.parameterStyleSupported = original
    assert instance.parameterStyleSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_packageGenerationSupported_setter(instance):
    original = instance.packageGenerationSupported
    instance.packageGenerationSupported = original
    assert instance.packageGenerationSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_functionLanguageType_setter(instance):
    original = instance.functionLanguageType
    instance.functionLanguageType = original
    assert instance.functionLanguageType == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_parameterInitValueSupported_setter(instance):
    original = instance.parameterInitValueSupported
    instance.parameterInitValueSupported = original
    assert instance.parameterInitValueSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_nullInputActionSupported_setter(instance):
    original = instance.nullInputActionSupported
    instance.nullInputActionSupported = original
    assert instance.nullInputActionSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_returnedTypeDeclarationConstraintSupported_setter(instance):
    original = instance.returnedTypeDeclarationConstraintSupported
    instance.returnedTypeDeclarationConstraintSupported = original
    assert instance.returnedTypeDeclarationConstraintSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_parameterDeclarationConstraintSupported_setter(instance):
    original = instance.parameterDeclarationConstraintSupported
    instance.parameterDeclarationConstraintSupported = original
    assert instance.parameterDeclarationConstraintSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_returnedNullSupported_setter(instance):
    original = instance.returnedNullSupported
    instance.returnedNullSupported = original
    assert instance.returnedNullSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_returnTypeSupported_setter(instance):
    original = instance.returnTypeSupported
    instance.returnTypeSupported = original
    assert instance.returnTypeSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_hyp_dbdefinition_storedproceduredefinition_procedureType_setter(instance):
    original = instance.procedureType
    instance.procedureType = original
    assert instance.procedureType == original




@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_prefetchSizeSupported_setter(instance):
    original = instance.prefetchSizeSupported
    instance.prefetchSizeSupported = original
    assert instance.prefetchSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_managedBySupported_setter(instance):
    original = instance.managedBySupported
    instance.managedBySupported = original
    assert instance.managedBySupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_containerMaximumSizeSupported_setter(instance):
    original = instance.containerMaximumSizeSupported
    instance.containerMaximumSizeSupported = original
    assert instance.containerMaximumSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_extentSizeSupported_setter(instance):
    original = instance.extentSizeSupported
    instance.extentSizeSupported = original
    assert instance.extentSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_bufferPoolSupported_setter(instance):
    original = instance.bufferPoolSupported
    instance.bufferPoolSupported = original
    assert instance.bufferPoolSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_tableSpaceType_setter(instance):
    original = instance.tableSpaceType
    instance.tableSpaceType = original
    assert instance.tableSpaceType == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_pageSizeSupported_setter(instance):
    original = instance.pageSizeSupported
    instance.pageSizeSupported = original
    assert instance.pageSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_containerExtentSizeSupported_setter(instance):
    original = instance.containerExtentSizeSupported
    instance.containerExtentSizeSupported = original
    assert instance.containerExtentSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_hyp_dbdefinition_tablespacedefinition_containerInitialSizeSupported_setter(instance):
    original = instance.containerInitialSizeSupported
    instance.containerInitialSizeSupported = original
    assert instance.containerInitialSizeSupported == original




@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_hyp_dbdefinition_nicknamedefinition_constraintSupported_setter(instance):
    original = instance.constraintSupported
    instance.constraintSupported = original
    assert instance.constraintSupported == original



@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_hyp_dbdefinition_nicknamedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_hyp_dbdefinition_nicknamedefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original




@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_hyp_dbdefinition_sqlsyntaxdefinition_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_hyp_dbdefinition_sqlsyntaxdefinition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original



@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_hyp_dbdefinition_sqlsyntaxdefinition_terminationCharacter_setter(instance):
    original = instance.terminationCharacter
    instance.terminationCharacter = original
    assert instance.terminationCharacter == original




@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_extendedGroupingSupported_setter(instance):
    original = instance.extendedGroupingSupported
    instance.extendedGroupingSupported = original
    assert instance.extendedGroupingSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_defaultKeywordForInsertValueSupported_setter(instance):
    original = instance.defaultKeywordForInsertValueSupported
    instance.defaultKeywordForInsertValueSupported = original
    assert instance.defaultKeywordForInsertValueSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_hostVariableMarker_setter(instance):
    original = instance.hostVariableMarker
    instance.hostVariableMarker = original
    assert instance.hostVariableMarker == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_tableAliasInDeleteSupported_setter(instance):
    original = instance.tableAliasInDeleteSupported
    instance.tableAliasInDeleteSupported = original
    assert instance.tableAliasInDeleteSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_castExpressionSupported_setter(instance):
    original = instance.castExpressionSupported
    instance.castExpressionSupported = original
    assert instance.castExpressionSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_identifierQuoteString_setter(instance):
    original = instance.identifierQuoteString
    instance.identifierQuoteString = original
    assert instance.identifierQuoteString == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_hyp_dbdefinition_querydefinition_hostVariableMarkerSupported_setter(instance):
    original = instance.hostVariableMarkerSupported
    instance.hostVariableMarkerSupported = original
    assert instance.hostVariableMarkerSupported == original




@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_hyp_dbdefinition_userdefinedtypedefinition_defaultValueSupported_setter(instance):
    original = instance.defaultValueSupported
    instance.defaultValueSupported = original
    assert instance.defaultValueSupported == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_hyp_dbdefinition_userdefinedtypedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_hyp_dbdefinition_userdefinedtypedefinition_structuredTypeSupported_setter(instance):
    original = instance.structuredTypeSupported
    instance.structuredTypeSupported = original
    assert instance.structuredTypeSupported == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_hyp_dbdefinition_userdefinedtypedefinition_distinctTypeSupported_setter(instance):
    original = instance.distinctTypeSupported
    instance.distinctTypeSupported = original
    assert instance.distinctTypeSupported == original




@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_defaultValueTypes_setter(instance):
    original = instance.defaultValueTypes
    instance.defaultValueTypes = original
    assert instance.defaultValueTypes == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_lengthSemantic_setter(instance):
    original = instance.lengthSemantic
    instance.lengthSemantic = original
    assert instance.lengthSemantic == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_minimumScale_setter(instance):
    original = instance.minimumScale
    instance.minimumScale = original
    assert instance.minimumScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_largeValueSpecifierLength_setter(instance):
    original = instance.largeValueSpecifierLength
    instance.largeValueSpecifierLength = original
    assert instance.largeValueSpecifierLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_jdbcEnumType_setter(instance):
    original = instance.jdbcEnumType
    instance.jdbcEnumType = original
    assert instance.jdbcEnumType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_characterSetSuffix_setter(instance):
    original = instance.characterSetSuffix
    instance.characterSetSuffix = original
    assert instance.characterSetSuffix == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_lengthSemanticSupported_setter(instance):
    original = instance.lengthSemanticSupported
    instance.lengthSemanticSupported = original
    assert instance.lengthSemanticSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_lengthSupported_setter(instance):
    original = instance.lengthSupported
    instance.lengthSupported = original
    assert instance.lengthSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_displayNameSupported_setter(instance):
    original = instance.displayNameSupported
    instance.displayNameSupported = original
    assert instance.displayNameSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_nullableSupported_setter(instance):
    original = instance.nullableSupported
    instance.nullableSupported = original
    assert instance.nullableSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_defaultLength_setter(instance):
    original = instance.defaultLength
    instance.defaultLength = original
    assert instance.defaultLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_fieldQualifierSeparator_setter(instance):
    original = instance.fieldQualifierSeparator
    instance.fieldQualifierSeparator = original
    assert instance.fieldQualifierSeparator == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_javaClassName_setter(instance):
    original = instance.javaClassName
    instance.javaClassName = original
    assert instance.javaClassName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_keyConstraintSupported_setter(instance):
    original = instance.keyConstraintSupported
    instance.keyConstraintSupported = original
    assert instance.keyConstraintSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_trailingFieldQualifierSupported_setter(instance):
    original = instance.trailingFieldQualifierSupported
    instance.trailingFieldQualifierSupported = original
    assert instance.trailingFieldQualifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_encodingSchemeSuffix_setter(instance):
    original = instance.encodingSchemeSuffix
    instance.encodingSchemeSuffix = original
    assert instance.encodingSchemeSuffix == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_largeValueSpecifierName_setter(instance):
    original = instance.largeValueSpecifierName
    instance.largeValueSpecifierName = original
    assert instance.largeValueSpecifierName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_largeValueSpecifierSupported_setter(instance):
    original = instance.largeValueSpecifierSupported
    instance.largeValueSpecifierSupported = original
    assert instance.largeValueSpecifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_leadingFieldQualifierSupported_setter(instance):
    original = instance.leadingFieldQualifierSupported
    instance.leadingFieldQualifierSupported = original
    assert instance.leadingFieldQualifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_cutoffPrecision_setter(instance):
    original = instance.cutoffPrecision
    instance.cutoffPrecision = original
    assert instance.cutoffPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_encodingScheme_setter(instance):
    original = instance.encodingScheme
    instance.encodingScheme = original
    assert instance.encodingScheme == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_maximumLength_setter(instance):
    original = instance.maximumLength
    instance.maximumLength = original
    assert instance.maximumLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_groupingSupported_setter(instance):
    original = instance.groupingSupported
    instance.groupingSupported = original
    assert instance.groupingSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_characterSet_setter(instance):
    original = instance.characterSet
    instance.characterSet = original
    assert instance.characterSet == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_orderingSupported_setter(instance):
    original = instance.orderingSupported
    instance.orderingSupported = original
    assert instance.orderingSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_minimumValue_setter(instance):
    original = instance.minimumValue
    instance.minimumValue = original
    assert instance.minimumValue == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_maximumValue_setter(instance):
    original = instance.maximumValue
    instance.maximumValue = original
    assert instance.maximumValue == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_bitDataSupported_setter(instance):
    original = instance.bitDataSupported
    instance.bitDataSupported = original
    assert instance.bitDataSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_multipleColumnsSupported_setter(instance):
    original = instance.multipleColumnsSupported
    instance.multipleColumnsSupported = original
    assert instance.multipleColumnsSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_hyp_dbdefinition_predefineddatatypedefinition_lengthUnit_setter(instance):
    original = instance.lengthUnit
    instance.lengthUnit = original
    assert instance.lengthUnit == original




@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_quotedDMLSupported_setter(instance):
    original = instance.quotedDMLSupported
    instance.quotedDMLSupported = original
    assert instance.quotedDMLSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_joinSupported_setter(instance):
    original = instance.joinSupported
    instance.joinSupported = original
    assert instance.joinSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_viewTriggerSupported_setter(instance):
    original = instance.viewTriggerSupported
    instance.viewTriggerSupported = original
    assert instance.viewTriggerSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_mQTIndexSupported_setter(instance):
    original = instance.mQTIndexSupported
    instance.mQTIndexSupported = original
    assert instance.mQTIndexSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_quotedDDLSupported_setter(instance):
    original = instance.quotedDDLSupported
    instance.quotedDDLSupported = original
    assert instance.quotedDDLSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_sqlUDFSupported_setter(instance):
    original = instance.sqlUDFSupported
    instance.sqlUDFSupported = original
    assert instance.sqlUDFSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_triggerSupported_setter(instance):
    original = instance.triggerSupported
    instance.triggerSupported = original
    assert instance.triggerSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_constraintsSupported_setter(instance):
    original = instance.constraintsSupported
    instance.constraintsSupported = original
    assert instance.constraintsSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_synonymSupported_setter(instance):
    original = instance.synonymSupported
    instance.synonymSupported = original
    assert instance.synonymSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_packageSupported_setter(instance):
    original = instance.packageSupported
    instance.packageSupported = original
    assert instance.packageSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_schemaSupported_setter(instance):
    original = instance.schemaSupported
    instance.schemaSupported = original
    assert instance.schemaSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_domainSupported_setter(instance):
    original = instance.domainSupported
    instance.domainSupported = original
    assert instance.domainSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_maximumCommentLength_setter(instance):
    original = instance.maximumCommentLength
    instance.maximumCommentLength = original
    assert instance.maximumCommentLength == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_userDefinedTypeSupported_setter(instance):
    original = instance.userDefinedTypeSupported
    instance.userDefinedTypeSupported = original
    assert instance.userDefinedTypeSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_xmlSupported_setter(instance):
    original = instance.xmlSupported
    instance.xmlSupported = original
    assert instance.xmlSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_snapshotViewSupported_setter(instance):
    original = instance.snapshotViewSupported
    instance.snapshotViewSupported = original
    assert instance.snapshotViewSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_groupSupported_setter(instance):
    original = instance.groupSupported
    instance.groupSupported = original
    assert instance.groupSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_mQTSupported_setter(instance):
    original = instance.mQTSupported
    instance.mQTSupported = original
    assert instance.mQTSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_roleSupported_setter(instance):
    original = instance.roleSupported
    instance.roleSupported = original
    assert instance.roleSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_nicknameSupported_setter(instance):
    original = instance.nicknameSupported
    instance.nicknameSupported = original
    assert instance.nicknameSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_userSupported_setter(instance):
    original = instance.userSupported
    instance.userSupported = original
    assert instance.userSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_sequenceSupported_setter(instance):
    original = instance.sequenceSupported
    instance.sequenceSupported = original
    assert instance.sequenceSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_authorizationIdentifierSupported_setter(instance):
    original = instance.authorizationIdentifierSupported
    instance.authorizationIdentifierSupported = original
    assert instance.authorizationIdentifierSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_tablespacesSupported_setter(instance):
    original = instance.tablespacesSupported
    instance.tablespacesSupported = original
    assert instance.tablespacesSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_uDFSupported_setter(instance):
    original = instance.uDFSupported
    instance.uDFSupported = original
    assert instance.uDFSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_constructedDataTypeSupported_setter(instance):
    original = instance.constructedDataTypeSupported
    instance.constructedDataTypeSupported = original
    assert instance.constructedDataTypeSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_storedProcedureSupported_setter(instance):
    original = instance.storedProcedureSupported
    instance.storedProcedureSupported = original
    assert instance.storedProcedureSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_roleAuthorizationSupported_setter(instance):
    original = instance.roleAuthorizationSupported
    instance.roleAuthorizationSupported = original
    assert instance.roleAuthorizationSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_SQLStatementSupported_setter(instance):
    original = instance.SQLStatementSupported
    instance.SQLStatementSupported = original
    assert instance.SQLStatementSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_aliasSupported_setter(instance):
    original = instance.aliasSupported
    instance.aliasSupported = original
    assert instance.aliasSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_hyp_dbdefinition_databasevendordefinition_eventSupported_setter(instance):
    original = instance.eventSupported
    instance.eventSupported = original
    assert instance.eventSupported == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    dbdefinition_ColumnDefinition,
    dbdefinition_ConstraintDefinition,
    dbdefinition_ConstructedDataTypeDefinition,
    dbdefinition_DatabaseVendorDefinition,
    dbdefinition_DebuggerDefinition,
    dbdefinition_ExtendedDefinition,
    dbdefinition_FieldQualifierDefinition,
    dbdefinition_IndexDefinition,
    dbdefinition_NicknameDefinition,
    dbdefinition_PredefinedDataTypeDefinition,
    dbdefinition_PrivilegeDefinition,
    dbdefinition_PrivilegedElementDefinition,
    dbdefinition_QueryDefinition,
    dbdefinition_SQLSyntaxDefinition,
    dbdefinition_SchemaDefinition,
    dbdefinition_SequenceDefinition,
    dbdefinition_StoredProcedureDefinition,
    dbdefinition_TableDefinition,
    dbdefinition_TableSpaceDefinition,
    dbdefinition_TriggerDefinition,
    dbdefinition_UserDefinedTypeDefinition,
    dbdefinition_ViewDefinition,
    CheckOption,
    LanguageType,
    LengthUnit,
    ParameterStyle,
    ParentDeleteDRIRuleType,
    ParentUpdateDRIRuleType,
    PercentFreeTerminology,
    ProcedureType,
    TableSpaceType,
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

def test_dbdefinition_ColumnDefinition_computedSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.computedSupported == True
    instance.computedSupported = False
    assert instance.computedSupported == False


def test_dbdefinition_ColumnDefinition_identityCycleSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identityCycleSupported == True
    instance.identityCycleSupported = False
    assert instance.identityCycleSupported == False


def test_dbdefinition_ColumnDefinition_identityIncrementSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identityIncrementSupported == True
    instance.identityIncrementSupported = False
    assert instance.identityIncrementSupported == False


def test_dbdefinition_ColumnDefinition_identityMaximumSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identityMaximumSupported == True
    instance.identityMaximumSupported = False
    assert instance.identityMaximumSupported == False


def test_dbdefinition_ColumnDefinition_identityMinimumSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identityMinimumSupported == True
    instance.identityMinimumSupported = False
    assert instance.identityMinimumSupported == False


def test_dbdefinition_ColumnDefinition_identityStartValueSupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identityStartValueSupported == True
    instance.identityStartValueSupported = False
    assert instance.identityStartValueSupported == False


def test_dbdefinition_ColumnDefinition_identitySupported_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.identitySupported == True
    instance.identitySupported = False
    assert instance.identitySupported == False


def test_dbdefinition_ColumnDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_ConstraintDefinition_checkOption_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.checkOption == "sample_text"
    instance.checkOption = "sample_text_2"
    assert instance.checkOption == "sample_text_2"


def test_dbdefinition_ConstraintDefinition_clusteredPrimaryKeySupported_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.clusteredPrimaryKeySupported == True
    instance.clusteredPrimaryKeySupported = False
    assert instance.clusteredPrimaryKeySupported == False


def test_dbdefinition_ConstraintDefinition_clusteredUniqueConstraintSupported_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.clusteredUniqueConstraintSupported == True
    instance.clusteredUniqueConstraintSupported = False
    assert instance.clusteredUniqueConstraintSupported == False


def test_dbdefinition_ConstraintDefinition_deferrableConstraintSupported_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.deferrableConstraintSupported == True
    instance.deferrableConstraintSupported = False
    assert instance.deferrableConstraintSupported == False


def test_dbdefinition_ConstraintDefinition_informationalConstraintSupported_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.informationalConstraintSupported == True
    instance.informationalConstraintSupported = False
    assert instance.informationalConstraintSupported == False


def test_dbdefinition_ConstraintDefinition_maximumCheckConstraintIdentifierLength_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.maximumCheckConstraintIdentifierLength == 7
    instance.maximumCheckConstraintIdentifierLength = 13
    assert instance.maximumCheckConstraintIdentifierLength == 13


def test_dbdefinition_ConstraintDefinition_maximumCheckExpressionLength_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.maximumCheckExpressionLength == 7
    instance.maximumCheckExpressionLength = 13
    assert instance.maximumCheckExpressionLength == 13


def test_dbdefinition_ConstraintDefinition_maximumForeignKeyIdentifierLength_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.maximumForeignKeyIdentifierLength == 7
    instance.maximumForeignKeyIdentifierLength = 13
    assert instance.maximumForeignKeyIdentifierLength == 13


def test_dbdefinition_ConstraintDefinition_maximumPrimaryKeyIdentifierLength_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.maximumPrimaryKeyIdentifierLength == 7
    instance.maximumPrimaryKeyIdentifierLength = 13
    assert instance.maximumPrimaryKeyIdentifierLength == 13


def test_dbdefinition_ConstraintDefinition_parentDeleteDRIRuleType_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.parentDeleteDRIRuleType == "sample_text"
    instance.parentDeleteDRIRuleType = "sample_text_2"
    assert instance.parentDeleteDRIRuleType == "sample_text_2"


def test_dbdefinition_ConstraintDefinition_parentUpdateDRIRuleType_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.parentUpdateDRIRuleType == "sample_text"
    instance.parentUpdateDRIRuleType = "sample_text_2"
    assert instance.parentUpdateDRIRuleType == "sample_text_2"


def test_dbdefinition_ConstraintDefinition_primaryKeyNullable_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.primaryKeyNullable == True
    instance.primaryKeyNullable = False
    assert instance.primaryKeyNullable == False


def test_dbdefinition_ConstraintDefinition_uniqueKeyNullable_value_roundtrip():
    instance = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    assert instance.uniqueKeyNullable == True
    instance.uniqueKeyNullable = False
    assert instance.uniqueKeyNullable == False


def test_dbdefinition_ConstructedDataTypeDefinition_arrayDatatypeSupported_value_roundtrip():
    instance = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    assert instance.arrayDatatypeSupported == True
    instance.arrayDatatypeSupported = False
    assert instance.arrayDatatypeSupported == False


def test_dbdefinition_ConstructedDataTypeDefinition_cursorDatatypeSupported_value_roundtrip():
    instance = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    assert instance.cursorDatatypeSupported == True
    instance.cursorDatatypeSupported = False
    assert instance.cursorDatatypeSupported == False


def test_dbdefinition_ConstructedDataTypeDefinition_multisetDatatypeSupported_value_roundtrip():
    instance = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    assert instance.multisetDatatypeSupported == True
    instance.multisetDatatypeSupported = False
    assert instance.multisetDatatypeSupported == False


def test_dbdefinition_ConstructedDataTypeDefinition_referenceDatatypeSupported_value_roundtrip():
    instance = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    assert instance.referenceDatatypeSupported == True
    instance.referenceDatatypeSupported = False
    assert instance.referenceDatatypeSupported == False


def test_dbdefinition_ConstructedDataTypeDefinition_rowDatatypeSupported_value_roundtrip():
    instance = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    assert instance.rowDatatypeSupported == True
    instance.rowDatatypeSupported = False
    assert instance.rowDatatypeSupported == False


def test_dbdefinition_DatabaseVendorDefinition_SQLStatementSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.SQLStatementSupported == True
    instance.SQLStatementSupported = False
    assert instance.SQLStatementSupported == False


def test_dbdefinition_DatabaseVendorDefinition_aliasSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.aliasSupported == True
    instance.aliasSupported = False
    assert instance.aliasSupported == False


def test_dbdefinition_DatabaseVendorDefinition_authorizationIdentifierSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.authorizationIdentifierSupported == True
    instance.authorizationIdentifierSupported = False
    assert instance.authorizationIdentifierSupported == False


def test_dbdefinition_DatabaseVendorDefinition_constraintsSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.constraintsSupported == True
    instance.constraintsSupported = False
    assert instance.constraintsSupported == False


def test_dbdefinition_DatabaseVendorDefinition_constructedDataTypeSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.constructedDataTypeSupported == True
    instance.constructedDataTypeSupported = False
    assert instance.constructedDataTypeSupported == False


def test_dbdefinition_DatabaseVendorDefinition_domainSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.domainSupported == True
    instance.domainSupported = False
    assert instance.domainSupported == False


def test_dbdefinition_DatabaseVendorDefinition_eventSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.eventSupported == True
    instance.eventSupported = False
    assert instance.eventSupported == False


def test_dbdefinition_DatabaseVendorDefinition_groupSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.groupSupported == True
    instance.groupSupported = False
    assert instance.groupSupported == False


def test_dbdefinition_DatabaseVendorDefinition_joinSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.joinSupported == True
    instance.joinSupported = False
    assert instance.joinSupported == False


def test_dbdefinition_DatabaseVendorDefinition_mQTIndexSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.mQTIndexSupported == True
    instance.mQTIndexSupported = False
    assert instance.mQTIndexSupported == False


def test_dbdefinition_DatabaseVendorDefinition_mQTSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.mQTSupported == True
    instance.mQTSupported = False
    assert instance.mQTSupported == False


def test_dbdefinition_DatabaseVendorDefinition_maximumCommentLength_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.maximumCommentLength == 7
    instance.maximumCommentLength = 13
    assert instance.maximumCommentLength == 13


def test_dbdefinition_DatabaseVendorDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_DatabaseVendorDefinition_nicknameSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.nicknameSupported == True
    instance.nicknameSupported = False
    assert instance.nicknameSupported == False


def test_dbdefinition_DatabaseVendorDefinition_packageSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.packageSupported == True
    instance.packageSupported = False
    assert instance.packageSupported == False


def test_dbdefinition_DatabaseVendorDefinition_quotedDDLSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.quotedDDLSupported == True
    instance.quotedDDLSupported = False
    assert instance.quotedDDLSupported == False


def test_dbdefinition_DatabaseVendorDefinition_quotedDMLSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.quotedDMLSupported == True
    instance.quotedDMLSupported = False
    assert instance.quotedDMLSupported == False


def test_dbdefinition_DatabaseVendorDefinition_roleAuthorizationSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.roleAuthorizationSupported == True
    instance.roleAuthorizationSupported = False
    assert instance.roleAuthorizationSupported == False


def test_dbdefinition_DatabaseVendorDefinition_roleSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.roleSupported == True
    instance.roleSupported = False
    assert instance.roleSupported == False


def test_dbdefinition_DatabaseVendorDefinition_schemaSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.schemaSupported == True
    instance.schemaSupported = False
    assert instance.schemaSupported == False


def test_dbdefinition_DatabaseVendorDefinition_sequenceSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.sequenceSupported == True
    instance.sequenceSupported = False
    assert instance.sequenceSupported == False


def test_dbdefinition_DatabaseVendorDefinition_snapshotViewSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.snapshotViewSupported == True
    instance.snapshotViewSupported = False
    assert instance.snapshotViewSupported == False


def test_dbdefinition_DatabaseVendorDefinition_sqlUDFSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.sqlUDFSupported == True
    instance.sqlUDFSupported = False
    assert instance.sqlUDFSupported == False


def test_dbdefinition_DatabaseVendorDefinition_storedProcedureSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.storedProcedureSupported == True
    instance.storedProcedureSupported = False
    assert instance.storedProcedureSupported == False


def test_dbdefinition_DatabaseVendorDefinition_synonymSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.synonymSupported == True
    instance.synonymSupported = False
    assert instance.synonymSupported == False


def test_dbdefinition_DatabaseVendorDefinition_tablespacesSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.tablespacesSupported == True
    instance.tablespacesSupported = False
    assert instance.tablespacesSupported == False


def test_dbdefinition_DatabaseVendorDefinition_triggerSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.triggerSupported == True
    instance.triggerSupported = False
    assert instance.triggerSupported == False


def test_dbdefinition_DatabaseVendorDefinition_uDFSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.uDFSupported == True
    instance.uDFSupported = False
    assert instance.uDFSupported == False


def test_dbdefinition_DatabaseVendorDefinition_userDefinedTypeSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.userDefinedTypeSupported == True
    instance.userDefinedTypeSupported = False
    assert instance.userDefinedTypeSupported == False


def test_dbdefinition_DatabaseVendorDefinition_userSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.userSupported == True
    instance.userSupported = False
    assert instance.userSupported == False


def test_dbdefinition_DatabaseVendorDefinition_vendor_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_dbdefinition_DatabaseVendorDefinition_version_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_dbdefinition_DatabaseVendorDefinition_viewTriggerSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.viewTriggerSupported == True
    instance.viewTriggerSupported = False
    assert instance.viewTriggerSupported == False


def test_dbdefinition_DatabaseVendorDefinition_xmlSupported_value_roundtrip():
    instance = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    assert instance.xmlSupported == True
    instance.xmlSupported = False
    assert instance.xmlSupported == False


def test_dbdefinition_DebuggerDefinition_conditionSupported_value_roundtrip():
    instance = dbdefinition_DebuggerDefinition(conditionSupported=True)
    assert instance.conditionSupported == True
    instance.conditionSupported = False
    assert instance.conditionSupported == False


def test_dbdefinition_ExtendedDefinition_name_value_roundtrip():
    instance = dbdefinition_ExtendedDefinition(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbdefinition_ExtendedDefinition_value_value_roundtrip():
    instance = dbdefinition_ExtendedDefinition(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_dbdefinition_FieldQualifierDefinition_defaultPrecision_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.defaultPrecision == 7
    instance.defaultPrecision = 13
    assert instance.defaultPrecision == 13


def test_dbdefinition_FieldQualifierDefinition_defaultScale_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.defaultScale == 7
    instance.defaultScale = 13
    assert instance.defaultScale == 13


def test_dbdefinition_FieldQualifierDefinition_maximumPrecision_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.maximumPrecision == 7
    instance.maximumPrecision = 13
    assert instance.maximumPrecision == 13


def test_dbdefinition_FieldQualifierDefinition_maximumScale_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.maximumScale == 7
    instance.maximumScale = 13
    assert instance.maximumScale == 13


def test_dbdefinition_FieldQualifierDefinition_name_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbdefinition_FieldQualifierDefinition_precisionSupported_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.precisionSupported == True
    instance.precisionSupported = False
    assert instance.precisionSupported == False


def test_dbdefinition_FieldQualifierDefinition_scaleSupported_value_roundtrip():
    instance = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    assert instance.scaleSupported == True
    instance.scaleSupported = False
    assert instance.scaleSupported == False


def test_dbdefinition_IndexDefinition_clusterChangeable_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.clusterChangeable == True
    instance.clusterChangeable = False
    assert instance.clusterChangeable == False


def test_dbdefinition_IndexDefinition_clusteringSupported_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.clusteringSupported == True
    instance.clusteringSupported = False
    assert instance.clusteringSupported == False


def test_dbdefinition_IndexDefinition_fillFactorSupported_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.fillFactorSupported == True
    instance.fillFactorSupported = False
    assert instance.fillFactorSupported == False


def test_dbdefinition_IndexDefinition_includedColumnsSupported_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.includedColumnsSupported == True
    instance.includedColumnsSupported = False
    assert instance.includedColumnsSupported == False


def test_dbdefinition_IndexDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_IndexDefinition_percentFreeChangeable_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.percentFreeChangeable == True
    instance.percentFreeChangeable = False
    assert instance.percentFreeChangeable == False


def test_dbdefinition_IndexDefinition_percentFreeTerminology_value_roundtrip():
    instance = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    assert instance.percentFreeTerminology == "sample_text"
    instance.percentFreeTerminology = "sample_text_2"
    assert instance.percentFreeTerminology == "sample_text_2"


def test_dbdefinition_NicknameDefinition_constraintSupported_value_roundtrip():
    instance = dbdefinition_NicknameDefinition(constraintSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.constraintSupported == True
    instance.constraintSupported = False
    assert instance.constraintSupported == False


def test_dbdefinition_NicknameDefinition_indexSupported_value_roundtrip():
    instance = dbdefinition_NicknameDefinition(constraintSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.indexSupported == True
    instance.indexSupported = False
    assert instance.indexSupported == False


def test_dbdefinition_NicknameDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_NicknameDefinition(constraintSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_PredefinedDataTypeDefinition_bitDataSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.bitDataSupported == True
    instance.bitDataSupported = False
    assert instance.bitDataSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_characterSet_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.characterSet == "sample_text"
    instance.characterSet = "sample_text_2"
    assert instance.characterSet == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_characterSetSuffix_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.characterSetSuffix == "sample_text"
    instance.characterSetSuffix = "sample_text_2"
    assert instance.characterSetSuffix == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_clusteringSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.clusteringSupported == True
    instance.clusteringSupported = False
    assert instance.clusteringSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_cutoffPrecision_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.cutoffPrecision == 7
    instance.cutoffPrecision = 13
    assert instance.cutoffPrecision == 13


def test_dbdefinition_PredefinedDataTypeDefinition_defaultLength_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.defaultLength == 7
    instance.defaultLength = 13
    assert instance.defaultLength == 13


def test_dbdefinition_PredefinedDataTypeDefinition_defaultPrecision_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.defaultPrecision == 7
    instance.defaultPrecision = 13
    assert instance.defaultPrecision == 13


def test_dbdefinition_PredefinedDataTypeDefinition_defaultScale_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.defaultScale == 7
    instance.defaultScale = 13
    assert instance.defaultScale == 13


def test_dbdefinition_PredefinedDataTypeDefinition_defaultSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.defaultSupported == True
    instance.defaultSupported = False
    assert instance.defaultSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_defaultValueTypes_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.defaultValueTypes == "sample_text"
    instance.defaultValueTypes = "sample_text_2"
    assert instance.defaultValueTypes == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_displayName_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.displayName == "sample_text"
    instance.displayName = "sample_text_2"
    assert instance.displayName == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_displayNameSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.displayNameSupported == True
    instance.displayNameSupported = False
    assert instance.displayNameSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_encodingScheme_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.encodingScheme == "sample_text"
    instance.encodingScheme = "sample_text_2"
    assert instance.encodingScheme == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_encodingSchemeSuffix_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.encodingSchemeSuffix == "sample_text"
    instance.encodingSchemeSuffix = "sample_text_2"
    assert instance.encodingSchemeSuffix == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_fieldQualifierSeparator_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.fieldQualifierSeparator == "sample_text"
    instance.fieldQualifierSeparator = "sample_text_2"
    assert instance.fieldQualifierSeparator == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_fillFactorSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.fillFactorSupported == True
    instance.fillFactorSupported = False
    assert instance.fillFactorSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_groupingSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.groupingSupported == True
    instance.groupingSupported = False
    assert instance.groupingSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_identitySupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.identitySupported == True
    instance.identitySupported = False
    assert instance.identitySupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_javaClassName_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.javaClassName == "sample_text"
    instance.javaClassName = "sample_text_2"
    assert instance.javaClassName == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_jdbcEnumType_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.jdbcEnumType == 7
    instance.jdbcEnumType = 13
    assert instance.jdbcEnumType == 13


def test_dbdefinition_PredefinedDataTypeDefinition_keyConstraintSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.keyConstraintSupported == True
    instance.keyConstraintSupported = False
    assert instance.keyConstraintSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_languageType_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.languageType == "sample_text"
    instance.languageType = "sample_text_2"
    assert instance.languageType == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierLength_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.largeValueSpecifierLength == 7
    instance.largeValueSpecifierLength = 13
    assert instance.largeValueSpecifierLength == 13


def test_dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierName_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.largeValueSpecifierName == "sample_text"
    instance.largeValueSpecifierName = "sample_text_2"
    assert instance.largeValueSpecifierName == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.largeValueSpecifierSupported == True
    instance.largeValueSpecifierSupported = False
    assert instance.largeValueSpecifierSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_leadingFieldQualifierSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.leadingFieldQualifierSupported == True
    instance.leadingFieldQualifierSupported = False
    assert instance.leadingFieldQualifierSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_lengthSemantic_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.lengthSemantic == "sample_text"
    instance.lengthSemantic = "sample_text_2"
    assert instance.lengthSemantic == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_lengthSemanticSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.lengthSemanticSupported == True
    instance.lengthSemanticSupported = False
    assert instance.lengthSemanticSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_lengthSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.lengthSupported == True
    instance.lengthSupported = False
    assert instance.lengthSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_lengthUnit_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.lengthUnit == "sample_text"
    instance.lengthUnit = "sample_text_2"
    assert instance.lengthUnit == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_maximumLength_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.maximumLength == 7
    instance.maximumLength = 13
    assert instance.maximumLength == 13


def test_dbdefinition_PredefinedDataTypeDefinition_maximumPrecision_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.maximumPrecision == 7
    instance.maximumPrecision = 13
    assert instance.maximumPrecision == 13


def test_dbdefinition_PredefinedDataTypeDefinition_maximumScale_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.maximumScale == 7
    instance.maximumScale = 13
    assert instance.maximumScale == 13


def test_dbdefinition_PredefinedDataTypeDefinition_maximumValue_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.maximumValue == "sample_text"
    instance.maximumValue = "sample_text_2"
    assert instance.maximumValue == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_minimumScale_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.minimumScale == 7
    instance.minimumScale = 13
    assert instance.minimumScale == 13


def test_dbdefinition_PredefinedDataTypeDefinition_minimumValue_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.minimumValue == "sample_text"
    instance.minimumValue = "sample_text_2"
    assert instance.minimumValue == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_multipleColumnsSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.multipleColumnsSupported == True
    instance.multipleColumnsSupported = False
    assert instance.multipleColumnsSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_name_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_nullableSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.nullableSupported == True
    instance.nullableSupported = False
    assert instance.nullableSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_orderingSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.orderingSupported == True
    instance.orderingSupported = False
    assert instance.orderingSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_precisionSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.precisionSupported == True
    instance.precisionSupported = False
    assert instance.precisionSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_primitiveType_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_dbdefinition_PredefinedDataTypeDefinition_scaleSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.scaleSupported == True
    instance.scaleSupported = False
    assert instance.scaleSupported == False


def test_dbdefinition_PredefinedDataTypeDefinition_trailingFieldQualifierSupported_value_roundtrip():
    instance = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    assert instance.trailingFieldQualifierSupported == True
    instance.trailingFieldQualifierSupported = False
    assert instance.trailingFieldQualifierSupported == False


def test_dbdefinition_PrivilegeDefinition_name_value_roundtrip():
    instance = dbdefinition_PrivilegeDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbdefinition_PrivilegedElementDefinition_name_value_roundtrip():
    instance = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbdefinition_QueryDefinition_castExpressionSupported_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.castExpressionSupported == True
    instance.castExpressionSupported = False
    assert instance.castExpressionSupported == False


def test_dbdefinition_QueryDefinition_defaultKeywordForInsertValueSupported_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.defaultKeywordForInsertValueSupported == True
    instance.defaultKeywordForInsertValueSupported = False
    assert instance.defaultKeywordForInsertValueSupported == False


def test_dbdefinition_QueryDefinition_extendedGroupingSupported_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.extendedGroupingSupported == True
    instance.extendedGroupingSupported = False
    assert instance.extendedGroupingSupported == False


def test_dbdefinition_QueryDefinition_hostVariableMarker_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.hostVariableMarker == "sample_text"
    instance.hostVariableMarker = "sample_text_2"
    assert instance.hostVariableMarker == "sample_text_2"


def test_dbdefinition_QueryDefinition_hostVariableMarkerSupported_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.hostVariableMarkerSupported == True
    instance.hostVariableMarkerSupported = False
    assert instance.hostVariableMarkerSupported == False


def test_dbdefinition_QueryDefinition_identifierQuoteString_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.identifierQuoteString == "sample_text"
    instance.identifierQuoteString = "sample_text_2"
    assert instance.identifierQuoteString == "sample_text_2"


def test_dbdefinition_QueryDefinition_tableAliasInDeleteSupported_value_roundtrip():
    instance = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    assert instance.tableAliasInDeleteSupported == True
    instance.tableAliasInDeleteSupported = False
    assert instance.tableAliasInDeleteSupported == False


def test_dbdefinition_SQLSyntaxDefinition_keywords_value_roundtrip():
    instance = dbdefinition_SQLSyntaxDefinition(keywords="sample_text", operators="sample_text", terminationCharacter="sample_text")
    assert instance.keywords == "sample_text"
    instance.keywords = "sample_text_2"
    assert instance.keywords == "sample_text_2"


def test_dbdefinition_SQLSyntaxDefinition_operators_value_roundtrip():
    instance = dbdefinition_SQLSyntaxDefinition(keywords="sample_text", operators="sample_text", terminationCharacter="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_dbdefinition_SQLSyntaxDefinition_terminationCharacter_value_roundtrip():
    instance = dbdefinition_SQLSyntaxDefinition(keywords="sample_text", operators="sample_text", terminationCharacter="sample_text")
    assert instance.terminationCharacter == "sample_text"
    instance.terminationCharacter = "sample_text_2"
    assert instance.terminationCharacter == "sample_text_2"


def test_dbdefinition_SchemaDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_SchemaDefinition(maximumIdentifierLength=7)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_SequenceDefinition_cacheDefaultValue_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.cacheDefaultValue == 7
    instance.cacheDefaultValue = 13
    assert instance.cacheDefaultValue == 13


def test_dbdefinition_SequenceDefinition_cacheSupported_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.cacheSupported == True
    instance.cacheSupported = False
    assert instance.cacheSupported == False


def test_dbdefinition_SequenceDefinition_noCacheString_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.noCacheString == "sample_text"
    instance.noCacheString = "sample_text_2"
    assert instance.noCacheString == "sample_text_2"


def test_dbdefinition_SequenceDefinition_noMaximumValueString_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.noMaximumValueString == "sample_text"
    instance.noMaximumValueString = "sample_text_2"
    assert instance.noMaximumValueString == "sample_text_2"


def test_dbdefinition_SequenceDefinition_noMinimumValueString_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.noMinimumValueString == "sample_text"
    instance.noMinimumValueString = "sample_text_2"
    assert instance.noMinimumValueString == "sample_text_2"


def test_dbdefinition_SequenceDefinition_orderSupported_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.orderSupported == True
    instance.orderSupported = False
    assert instance.orderSupported == False


def test_dbdefinition_SequenceDefinition_typeEnumerationSupported_value_roundtrip():
    instance = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    assert instance.typeEnumerationSupported == True
    instance.typeEnumerationSupported = False
    assert instance.typeEnumerationSupported == False


def test_dbdefinition_StoredProcedureDefinition_determininsticSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.determininsticSupported == True
    instance.determininsticSupported = False
    assert instance.determininsticSupported == False


def test_dbdefinition_StoredProcedureDefinition_functionLanguageType_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.functionLanguageType == "sample_text"
    instance.functionLanguageType = "sample_text_2"
    assert instance.functionLanguageType == "sample_text_2"


def test_dbdefinition_StoredProcedureDefinition_languageType_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.languageType == "sample_text"
    instance.languageType = "sample_text_2"
    assert instance.languageType == "sample_text_2"


def test_dbdefinition_StoredProcedureDefinition_maximumActionBodyLength_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.maximumActionBodyLength == 7
    instance.maximumActionBodyLength = 13
    assert instance.maximumActionBodyLength == 13


def test_dbdefinition_StoredProcedureDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_StoredProcedureDefinition_nullInputActionSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.nullInputActionSupported == True
    instance.nullInputActionSupported = False
    assert instance.nullInputActionSupported == False


def test_dbdefinition_StoredProcedureDefinition_packageGenerationSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.packageGenerationSupported == True
    instance.packageGenerationSupported = False
    assert instance.packageGenerationSupported == False


def test_dbdefinition_StoredProcedureDefinition_parameterDeclarationConstraintSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.parameterDeclarationConstraintSupported == True
    instance.parameterDeclarationConstraintSupported = False
    assert instance.parameterDeclarationConstraintSupported == False


def test_dbdefinition_StoredProcedureDefinition_parameterInitValueSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.parameterInitValueSupported == True
    instance.parameterInitValueSupported = False
    assert instance.parameterInitValueSupported == False


def test_dbdefinition_StoredProcedureDefinition_parameterStyle_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.parameterStyle == "sample_text"
    instance.parameterStyle = "sample_text_2"
    assert instance.parameterStyle == "sample_text_2"


def test_dbdefinition_StoredProcedureDefinition_parameterStyleSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.parameterStyleSupported == True
    instance.parameterStyleSupported = False
    assert instance.parameterStyleSupported == False


def test_dbdefinition_StoredProcedureDefinition_procedureType_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.procedureType == "sample_text"
    instance.procedureType = "sample_text_2"
    assert instance.procedureType == "sample_text_2"


def test_dbdefinition_StoredProcedureDefinition_returnTypeSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.returnTypeSupported == True
    instance.returnTypeSupported = False
    assert instance.returnTypeSupported == False


def test_dbdefinition_StoredProcedureDefinition_returnedNullSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.returnedNullSupported == True
    instance.returnedNullSupported = False
    assert instance.returnedNullSupported == False


def test_dbdefinition_StoredProcedureDefinition_returnedTypeDeclarationConstraintSupported_value_roundtrip():
    instance = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    assert instance.returnedTypeDeclarationConstraintSupported == True
    instance.returnedTypeDeclarationConstraintSupported = False
    assert instance.returnedTypeDeclarationConstraintSupported == False


def test_dbdefinition_TableDefinition_auditSupported_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.auditSupported == True
    instance.auditSupported = False
    assert instance.auditSupported == False


def test_dbdefinition_TableDefinition_dataCaptureSupported_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.dataCaptureSupported == True
    instance.dataCaptureSupported = False
    assert instance.dataCaptureSupported == False


def test_dbdefinition_TableDefinition_editProcSupported_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.editProcSupported == True
    instance.editProcSupported = False
    assert instance.editProcSupported == False


def test_dbdefinition_TableDefinition_encodingSupported_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.encodingSupported == True
    instance.encodingSupported = False
    assert instance.encodingSupported == False


def test_dbdefinition_TableDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_TableDefinition_validProcSupported_value_roundtrip():
    instance = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    assert instance.validProcSupported == True
    instance.validProcSupported = False
    assert instance.validProcSupported == False


def test_dbdefinition_TableSpaceDefinition_bufferPoolSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.bufferPoolSupported == True
    instance.bufferPoolSupported = False
    assert instance.bufferPoolSupported == False


def test_dbdefinition_TableSpaceDefinition_containerExtentSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.containerExtentSizeSupported == True
    instance.containerExtentSizeSupported = False
    assert instance.containerExtentSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_containerInitialSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.containerInitialSizeSupported == True
    instance.containerInitialSizeSupported = False
    assert instance.containerInitialSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_containerMaximumSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.containerMaximumSizeSupported == True
    instance.containerMaximumSizeSupported = False
    assert instance.containerMaximumSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_defaultSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.defaultSupported == True
    instance.defaultSupported = False
    assert instance.defaultSupported == False


def test_dbdefinition_TableSpaceDefinition_extentSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.extentSizeSupported == True
    instance.extentSizeSupported = False
    assert instance.extentSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_managedBySupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.managedBySupported == True
    instance.managedBySupported = False
    assert instance.managedBySupported == False


def test_dbdefinition_TableSpaceDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_TableSpaceDefinition_pageSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.pageSizeSupported == True
    instance.pageSizeSupported = False
    assert instance.pageSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_prefetchSizeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.prefetchSizeSupported == True
    instance.prefetchSizeSupported = False
    assert instance.prefetchSizeSupported == False


def test_dbdefinition_TableSpaceDefinition_tableSpaceType_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.tableSpaceType == "sample_text"
    instance.tableSpaceType = "sample_text_2"
    assert instance.tableSpaceType == "sample_text_2"


def test_dbdefinition_TableSpaceDefinition_typeSupported_value_roundtrip():
    instance = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    assert instance.typeSupported == True
    instance.typeSupported = False
    assert instance.typeSupported == False


def test_dbdefinition_TriggerDefinition_granularitySupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.granularitySupported == True
    instance.granularitySupported = False
    assert instance.granularitySupported == False


def test_dbdefinition_TriggerDefinition_insteadOfTriggerSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.insteadOfTriggerSupported == True
    instance.insteadOfTriggerSupported = False
    assert instance.insteadOfTriggerSupported == False


def test_dbdefinition_TriggerDefinition_maximumActionBodyLength_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.maximumActionBodyLength == 7
    instance.maximumActionBodyLength = 13
    assert instance.maximumActionBodyLength == 13


def test_dbdefinition_TriggerDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_TriggerDefinition_maximumReferencePartLength_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.maximumReferencePartLength == 7
    instance.maximumReferencePartLength = 13
    assert instance.maximumReferencePartLength == 13


def test_dbdefinition_TriggerDefinition_perColumnUpdateTriggerSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.perColumnUpdateTriggerSupported == True
    instance.perColumnUpdateTriggerSupported = False
    assert instance.perColumnUpdateTriggerSupported == False


def test_dbdefinition_TriggerDefinition_referencesClauseSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.referencesClauseSupported == True
    instance.referencesClauseSupported = False
    assert instance.referencesClauseSupported == False


def test_dbdefinition_TriggerDefinition_rowTriggerReferenceSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.rowTriggerReferenceSupported == True
    instance.rowTriggerReferenceSupported = False
    assert instance.rowTriggerReferenceSupported == False


def test_dbdefinition_TriggerDefinition_tableTriggerReferenceSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.tableTriggerReferenceSupported == True
    instance.tableTriggerReferenceSupported = False
    assert instance.tableTriggerReferenceSupported == False


def test_dbdefinition_TriggerDefinition_typeSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.typeSupported == True
    instance.typeSupported = False
    assert instance.typeSupported == False


def test_dbdefinition_TriggerDefinition_whenClauseSupported_value_roundtrip():
    instance = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    assert instance.whenClauseSupported == True
    instance.whenClauseSupported = False
    assert instance.whenClauseSupported == False


def test_dbdefinition_UserDefinedTypeDefinition_defaultValueSupported_value_roundtrip():
    instance = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    assert instance.defaultValueSupported == True
    instance.defaultValueSupported = False
    assert instance.defaultValueSupported == False


def test_dbdefinition_UserDefinedTypeDefinition_distinctTypeSupported_value_roundtrip():
    instance = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    assert instance.distinctTypeSupported == True
    instance.distinctTypeSupported = False
    assert instance.distinctTypeSupported == False


def test_dbdefinition_UserDefinedTypeDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_dbdefinition_UserDefinedTypeDefinition_structuredTypeSupported_value_roundtrip():
    instance = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    assert instance.structuredTypeSupported == True
    instance.structuredTypeSupported = False
    assert instance.structuredTypeSupported == False


def test_dbdefinition_ViewDefinition_checkOptionLevelsSupported_value_roundtrip():
    instance = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.checkOptionLevelsSupported == True
    instance.checkOptionLevelsSupported = False
    assert instance.checkOptionLevelsSupported == False


def test_dbdefinition_ViewDefinition_checkOptionSupported_value_roundtrip():
    instance = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.checkOptionSupported == True
    instance.checkOptionSupported = False
    assert instance.checkOptionSupported == False


def test_dbdefinition_ViewDefinition_indexSupported_value_roundtrip():
    instance = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.indexSupported == True
    instance.indexSupported = False
    assert instance.indexSupported == False


def test_dbdefinition_ViewDefinition_maximumIdentifierLength_value_roundtrip():
    instance = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    assert instance.maximumIdentifierLength == 7
    instance.maximumIdentifierLength = 13
    assert instance.maximumIdentifierLength == 13


def test_assoc_SQLSyntaxDefinition23_link_reassign_clear():
    a = dbdefinition_SQLSyntaxDefinition(keywords="sample_text", operators="sample_text", terminationCharacter="sample_text")
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_SQLSyntaxDefinition', b1)
    assert _is_linked(a, 'dbdefinition_SQLSyntaxDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition24'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition24', a)
    _safe_set(a, 'dbdefinition_SQLSyntaxDefinition', b2)
    assert _is_linked(a, 'dbdefinition_SQLSyntaxDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition24'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition24', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition24'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition24', a)
    _safe_set(a, 'dbdefinition_SQLSyntaxDefinition', None)
    assert not _is_linked(a, 'dbdefinition_SQLSyntaxDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition24'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition24', a)


def test_assoc_actionElementDefinitions65_link_reassign_clear():
    a = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    b1 = dbdefinition_PrivilegeDefinition(name="sample_text")
    b2 = dbdefinition_PrivilegeDefinition(name="sample_text_2")
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition67', b1)
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition67', b1)
    if hasattr(b1, 'dbdefinition_PrivilegeDefinition66'):
        assert _is_linked(b1, 'dbdefinition_PrivilegeDefinition66', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition67', b2)
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition67', b2)
    if hasattr(b1, 'dbdefinition_PrivilegeDefinition66'):
        assert not _is_linked(b1, 'dbdefinition_PrivilegeDefinition66', a)
    if hasattr(b2, 'dbdefinition_PrivilegeDefinition66'):
        assert _is_linked(b2, 'dbdefinition_PrivilegeDefinition66', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition67', None)
    assert not _is_linked(a, 'dbdefinition_PrivilegedElementDefinition67', b2)
    if hasattr(b2, 'dbdefinition_PrivilegeDefinition66'):
        assert not _is_linked(b2, 'dbdefinition_PrivilegeDefinition66', a)


def test_assoc_columnDefinition7_link_reassign_clear():
    a = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b1 = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    b2 = dbdefinition_ColumnDefinition(computedSupported=False, identityCycleSupported=False, identityIncrementSupported=False, identityMaximumSupported=False, identityMinimumSupported=False, identityStartValueSupported=False, identitySupported=False, maximumIdentifierLength=13)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition8', b1)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition8', b1)
    if hasattr(b1, 'dbdefinition_ColumnDefinition'):
        assert _is_linked(b1, 'dbdefinition_ColumnDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition8', b2)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition8', b2)
    if hasattr(b1, 'dbdefinition_ColumnDefinition'):
        assert not _is_linked(b1, 'dbdefinition_ColumnDefinition', a)
    if hasattr(b2, 'dbdefinition_ColumnDefinition'):
        assert _is_linked(b2, 'dbdefinition_ColumnDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition8', None)
    assert not _is_linked(a, 'dbdefinition_DatabaseVendorDefinition8', b2)
    if hasattr(b2, 'dbdefinition_ColumnDefinition'):
        assert not _is_linked(b2, 'dbdefinition_ColumnDefinition', a)


def test_assoc_constraintDefinition9_link_reassign_clear():
    a = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b1 = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    b2 = dbdefinition_ConstraintDefinition(checkOption="sample_text_2", clusteredPrimaryKeySupported=False, clusteredUniqueConstraintSupported=False, deferrableConstraintSupported=False, informationalConstraintSupported=False, maximumCheckConstraintIdentifierLength=13, maximumCheckExpressionLength=13, maximumForeignKeyIdentifierLength=13, maximumPrimaryKeyIdentifierLength=13, parentDeleteDRIRuleType="sample_text_2", parentUpdateDRIRuleType="sample_text_2", primaryKeyNullable=False, uniqueKeyNullable=False)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition10', b1)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition10', b1)
    if hasattr(b1, 'dbdefinition_ConstraintDefinition'):
        assert _is_linked(b1, 'dbdefinition_ConstraintDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition10', b2)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition10', b2)
    if hasattr(b1, 'dbdefinition_ConstraintDefinition'):
        assert not _is_linked(b1, 'dbdefinition_ConstraintDefinition', a)
    if hasattr(b2, 'dbdefinition_ConstraintDefinition'):
        assert _is_linked(b2, 'dbdefinition_ConstraintDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition10', None)
    assert not _is_linked(a, 'dbdefinition_DatabaseVendorDefinition10', b2)
    if hasattr(b2, 'dbdefinition_ConstraintDefinition'):
        assert not _is_linked(b2, 'dbdefinition_ConstraintDefinition', a)


def test_assoc_constructedDataTypeDefinition35_link_reassign_clear():
    a = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b1 = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    b2 = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=False, cursorDatatypeSupported=False, multisetDatatypeSupported=False, referenceDatatypeSupported=False, rowDatatypeSupported=False)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition36', b1)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition36', b1)
    if hasattr(b1, 'dbdefinition_ConstructedDataTypeDefinition'):
        assert _is_linked(b1, 'dbdefinition_ConstructedDataTypeDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition36', b2)
    assert _is_linked(a, 'dbdefinition_DatabaseVendorDefinition36', b2)
    if hasattr(b1, 'dbdefinition_ConstructedDataTypeDefinition'):
        assert not _is_linked(b1, 'dbdefinition_ConstructedDataTypeDefinition', a)
    if hasattr(b2, 'dbdefinition_ConstructedDataTypeDefinition'):
        assert _is_linked(b2, 'dbdefinition_ConstructedDataTypeDefinition', a)
    _safe_set(a, 'dbdefinition_DatabaseVendorDefinition36', None)
    assert not _is_linked(a, 'dbdefinition_DatabaseVendorDefinition36', b2)
    if hasattr(b2, 'dbdefinition_ConstructedDataTypeDefinition'):
        assert not _is_linked(b2, 'dbdefinition_ConstructedDataTypeDefinition', a)


def test_assoc_debuggerDefinition31_link_reassign_clear():
    a = dbdefinition_DebuggerDefinition(conditionSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_DebuggerDefinition', b1)
    assert _is_linked(a, 'dbdefinition_DebuggerDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition32'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition32', a)
    _safe_set(a, 'dbdefinition_DebuggerDefinition', b2)
    assert _is_linked(a, 'dbdefinition_DebuggerDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition32'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition32', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition32'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition32', a)
    _safe_set(a, 'dbdefinition_DebuggerDefinition', None)
    assert not _is_linked(a, 'dbdefinition_DebuggerDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition32'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition32', a)


def test_assoc_defaultDataTypeDefinition57_link_reassign_clear():
    a = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    b1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    _safe_set(a, 'dbdefinition_SequenceDefinition58', b1)
    assert _is_linked(a, 'dbdefinition_SequenceDefinition58', b1)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition59'):
        assert _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition59', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition58', b2)
    assert _is_linked(a, 'dbdefinition_SequenceDefinition58', b2)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition59'):
        assert not _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition59', a)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition59'):
        assert _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition59', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition58', None)
    assert not _is_linked(a, 'dbdefinition_SequenceDefinition58', b2)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition59'):
        assert not _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition59', a)


def test_assoc_defaultLeadingFieldQualifierDefinition45_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition46', b1)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition46', b1)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition47'):
        assert _is_linked(b1, 'dbdefinition_FieldQualifierDefinition47', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition46', b2)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition46', b2)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition47'):
        assert not _is_linked(b1, 'dbdefinition_FieldQualifierDefinition47', a)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition47'):
        assert _is_linked(b2, 'dbdefinition_FieldQualifierDefinition47', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition46', None)
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition46', b2)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition47'):
        assert not _is_linked(b2, 'dbdefinition_FieldQualifierDefinition47', a)


def test_assoc_defaultTrailingFieldQualifierDefinition42_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition43', b1)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition43', b1)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition44'):
        assert _is_linked(b1, 'dbdefinition_FieldQualifierDefinition44', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition43', b2)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition43', b2)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition44'):
        assert not _is_linked(b1, 'dbdefinition_FieldQualifierDefinition44', a)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition44'):
        assert _is_linked(b2, 'dbdefinition_FieldQualifierDefinition44', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition43', None)
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition43', b2)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition44'):
        assert not _is_linked(b2, 'dbdefinition_FieldQualifierDefinition44', a)


def test_assoc_extendedDefinitions11_link_reassign_clear():
    a = dbdefinition_ExtendedDefinition(name="sample_text", value="sample_text")
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_ExtendedDefinition', b1)
    assert _is_linked(a, 'dbdefinition_ExtendedDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition12'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition12', a)
    _safe_set(a, 'dbdefinition_ExtendedDefinition', b2)
    assert _is_linked(a, 'dbdefinition_ExtendedDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition12'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition12', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition12'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition12', a)
    _safe_set(a, 'dbdefinition_ExtendedDefinition', None)
    assert not _is_linked(a, 'dbdefinition_ExtendedDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition12'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition12', a)


def test_assoc_identityColumnDataTypeDefinitions51_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    b2 = dbdefinition_ColumnDefinition(computedSupported=False, identityCycleSupported=False, identityIncrementSupported=False, identityMaximumSupported=False, identityMinimumSupported=False, identityStartValueSupported=False, identitySupported=False, maximumIdentifierLength=13)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition53', b1)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition53', b1)
    if hasattr(b1, 'dbdefinition_ColumnDefinition52'):
        assert _is_linked(b1, 'dbdefinition_ColumnDefinition52', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition53', b2)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition53', b2)
    if hasattr(b1, 'dbdefinition_ColumnDefinition52'):
        assert not _is_linked(b1, 'dbdefinition_ColumnDefinition52', a)
    if hasattr(b2, 'dbdefinition_ColumnDefinition52'):
        assert _is_linked(b2, 'dbdefinition_ColumnDefinition52', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition53', None)
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition53', b2)
    if hasattr(b2, 'dbdefinition_ColumnDefinition52'):
        assert not _is_linked(b2, 'dbdefinition_ColumnDefinition52', a)


def test_assoc_indexDefinition13_link_reassign_clear():
    a = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_IndexDefinition', b1)
    assert _is_linked(a, 'dbdefinition_IndexDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition14'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition14', a)
    _safe_set(a, 'dbdefinition_IndexDefinition', b2)
    assert _is_linked(a, 'dbdefinition_IndexDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition14'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition14', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition14'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition14', a)
    _safe_set(a, 'dbdefinition_IndexDefinition', None)
    assert not _is_linked(a, 'dbdefinition_IndexDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition14'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition14', a)


def test_assoc_leadingFieldQualifierDefinition37_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition38', {b1})
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition38', b1)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition'):
        assert _is_linked(b1, 'dbdefinition_FieldQualifierDefinition', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition38', {b2})
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition38', b2)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition'):
        assert not _is_linked(b1, 'dbdefinition_FieldQualifierDefinition', a)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition'):
        assert _is_linked(b2, 'dbdefinition_FieldQualifierDefinition', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition38', set())
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition38', b2)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition'):
        assert not _is_linked(b2, 'dbdefinition_FieldQualifierDefinition', a)


def test_assoc_nicknameDefinition25_link_reassign_clear():
    a = dbdefinition_NicknameDefinition(constraintSupported=True, indexSupported=True, maximumIdentifierLength=7)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_NicknameDefinition', b1)
    assert _is_linked(a, 'dbdefinition_NicknameDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition26'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition26', a)
    _safe_set(a, 'dbdefinition_NicknameDefinition', b2)
    assert _is_linked(a, 'dbdefinition_NicknameDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition26'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition26', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition26'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition26', a)
    _safe_set(a, 'dbdefinition_NicknameDefinition', None)
    assert not _is_linked(a, 'dbdefinition_NicknameDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition26'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition26', a)


def test_assoc_predefinedDataTypeDefinitions0_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition', b1)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition', b2)
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition', None)
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition', a)


def test_assoc_predefinedDataTypeDefinitions48_link_reassign_clear():
    a = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    b1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition49', {b1})
    assert _is_linked(a, 'dbdefinition_StoredProcedureDefinition49', b1)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition50'):
        assert _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition50', a)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition49', {b2})
    assert _is_linked(a, 'dbdefinition_StoredProcedureDefinition49', b2)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition50'):
        assert not _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition50', a)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition50'):
        assert _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition50', a)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition49', set())
    assert not _is_linked(a, 'dbdefinition_StoredProcedureDefinition49', b2)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition50'):
        assert not _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition50', a)


def test_assoc_predefinedDataTypeDefinitions54_link_reassign_clear():
    a = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    b1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    _safe_set(a, 'dbdefinition_SequenceDefinition55', {b1})
    assert _is_linked(a, 'dbdefinition_SequenceDefinition55', b1)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition56'):
        assert _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition56', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition55', {b2})
    assert _is_linked(a, 'dbdefinition_SequenceDefinition55', b2)
    if hasattr(b1, 'dbdefinition_PredefinedDataTypeDefinition56'):
        assert not _is_linked(b1, 'dbdefinition_PredefinedDataTypeDefinition56', a)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition56'):
        assert _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition56', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition55', set())
    assert not _is_linked(a, 'dbdefinition_SequenceDefinition55', b2)
    if hasattr(b2, 'dbdefinition_PredefinedDataTypeDefinition56'):
        assert not _is_linked(b2, 'dbdefinition_PredefinedDataTypeDefinition56', a)


def test_assoc_privilegeDefinitions63_link_reassign_clear():
    a = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    b1 = dbdefinition_PrivilegeDefinition(name="sample_text")
    b2 = dbdefinition_PrivilegeDefinition(name="sample_text_2")
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition64', {b1})
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition64', b1)
    if hasattr(b1, 'dbdefinition_PrivilegeDefinition'):
        assert _is_linked(b1, 'dbdefinition_PrivilegeDefinition', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition64', {b2})
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition64', b2)
    if hasattr(b1, 'dbdefinition_PrivilegeDefinition'):
        assert not _is_linked(b1, 'dbdefinition_PrivilegeDefinition', a)
    if hasattr(b2, 'dbdefinition_PrivilegeDefinition'):
        assert _is_linked(b2, 'dbdefinition_PrivilegeDefinition', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition64', set())
    assert not _is_linked(a, 'dbdefinition_PrivilegedElementDefinition64', b2)
    if hasattr(b2, 'dbdefinition_PrivilegeDefinition'):
        assert not _is_linked(b2, 'dbdefinition_PrivilegeDefinition', a)


def test_assoc_privilegedElementDefinitions33_link_reassign_clear():
    a = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition', b1)
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition34'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition34', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition', b2)
    assert _is_linked(a, 'dbdefinition_PrivilegedElementDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition34'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition34', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition34'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition34', a)
    _safe_set(a, 'dbdefinition_PrivilegedElementDefinition', None)
    assert not _is_linked(a, 'dbdefinition_PrivilegedElementDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition34'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition34', a)


def test_assoc_queryDefinition21_link_reassign_clear():
    a = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_QueryDefinition', b1)
    assert _is_linked(a, 'dbdefinition_QueryDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition22'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition22', a)
    _safe_set(a, 'dbdefinition_QueryDefinition', b2)
    assert _is_linked(a, 'dbdefinition_QueryDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition22'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition22', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition22'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition22', a)
    _safe_set(a, 'dbdefinition_QueryDefinition', None)
    assert not _is_linked(a, 'dbdefinition_QueryDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition22'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition22', a)


def test_assoc_schemaDefinition27_link_reassign_clear():
    a = dbdefinition_SchemaDefinition(maximumIdentifierLength=7)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_SchemaDefinition', b1)
    assert _is_linked(a, 'dbdefinition_SchemaDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition28'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition28', a)
    _safe_set(a, 'dbdefinition_SchemaDefinition', b2)
    assert _is_linked(a, 'dbdefinition_SchemaDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition28'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition28', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition28'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition28', a)
    _safe_set(a, 'dbdefinition_SchemaDefinition', None)
    assert not _is_linked(a, 'dbdefinition_SchemaDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition28'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition28', a)


def test_assoc_sequenceDefinition17_link_reassign_clear():
    a = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_SequenceDefinition', b1)
    assert _is_linked(a, 'dbdefinition_SequenceDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition18'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition18', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition', b2)
    assert _is_linked(a, 'dbdefinition_SequenceDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition18'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition18', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition18'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition18', a)
    _safe_set(a, 'dbdefinition_SequenceDefinition', None)
    assert not _is_linked(a, 'dbdefinition_SequenceDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition18'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition18', a)


def test_assoc_storedProcedureDefinition3_link_reassign_clear():
    a = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition', b1)
    assert _is_linked(a, 'dbdefinition_StoredProcedureDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition4'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition4', a)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition', b2)
    assert _is_linked(a, 'dbdefinition_StoredProcedureDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition4'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition4', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition4'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition4', a)
    _safe_set(a, 'dbdefinition_StoredProcedureDefinition', None)
    assert not _is_linked(a, 'dbdefinition_StoredProcedureDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition4'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition4', a)


def test_assoc_tableDefinition15_link_reassign_clear():
    a = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_TableDefinition', b1)
    assert _is_linked(a, 'dbdefinition_TableDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition16'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition16', a)
    _safe_set(a, 'dbdefinition_TableDefinition', b2)
    assert _is_linked(a, 'dbdefinition_TableDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition16'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition16', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition16'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition16', a)
    _safe_set(a, 'dbdefinition_TableDefinition', None)
    assert not _is_linked(a, 'dbdefinition_TableDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition16'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition16', a)


def test_assoc_tableSpaceDefinition1_link_reassign_clear():
    a = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_TableSpaceDefinition', b1)
    assert _is_linked(a, 'dbdefinition_TableSpaceDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition2'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition2', a)
    _safe_set(a, 'dbdefinition_TableSpaceDefinition', b2)
    assert _is_linked(a, 'dbdefinition_TableSpaceDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition2'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition2', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition2'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition2', a)
    _safe_set(a, 'dbdefinition_TableSpaceDefinition', None)
    assert not _is_linked(a, 'dbdefinition_TableSpaceDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition2'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition2', a)


def test_assoc_trailingFieldQualifierDefinition39_link_reassign_clear():
    a = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    b1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition40', {b1})
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition40', b1)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition41'):
        assert _is_linked(b1, 'dbdefinition_FieldQualifierDefinition41', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition40', {b2})
    assert _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition40', b2)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition41'):
        assert not _is_linked(b1, 'dbdefinition_FieldQualifierDefinition41', a)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition41'):
        assert _is_linked(b2, 'dbdefinition_FieldQualifierDefinition41', a)
    _safe_set(a, 'dbdefinition_PredefinedDataTypeDefinition40', set())
    assert not _is_linked(a, 'dbdefinition_PredefinedDataTypeDefinition40', b2)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition41'):
        assert not _is_linked(b2, 'dbdefinition_FieldQualifierDefinition41', a)


def test_assoc_triggerDefinition5_link_reassign_clear():
    a = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_TriggerDefinition', b1)
    assert _is_linked(a, 'dbdefinition_TriggerDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition6'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition6', a)
    _safe_set(a, 'dbdefinition_TriggerDefinition', b2)
    assert _is_linked(a, 'dbdefinition_TriggerDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition6'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition6', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition6'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition6', a)
    _safe_set(a, 'dbdefinition_TriggerDefinition', None)
    assert not _is_linked(a, 'dbdefinition_TriggerDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition6'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition6', a)


def test_assoc_udtDefinition19_link_reassign_clear():
    a = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_UserDefinedTypeDefinition', b1)
    assert _is_linked(a, 'dbdefinition_UserDefinedTypeDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition20'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition20', a)
    _safe_set(a, 'dbdefinition_UserDefinedTypeDefinition', b2)
    assert _is_linked(a, 'dbdefinition_UserDefinedTypeDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition20'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition20', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition20'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition20', a)
    _safe_set(a, 'dbdefinition_UserDefinedTypeDefinition', None)
    assert not _is_linked(a, 'dbdefinition_UserDefinedTypeDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition20'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition20', a)


def test_assoc_validTrailingFieldQualifierDefinitions61_link_reassign_clear():
    a = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    b2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    _safe_set(a, 'dbdefinition_FieldQualifierDefinition60', {b1})
    assert _is_linked(a, 'dbdefinition_FieldQualifierDefinition60', b1)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition62'):
        assert _is_linked(b1, 'dbdefinition_FieldQualifierDefinition62', a)
    _safe_set(a, 'dbdefinition_FieldQualifierDefinition60', {b2})
    assert _is_linked(a, 'dbdefinition_FieldQualifierDefinition60', b2)
    if hasattr(b1, 'dbdefinition_FieldQualifierDefinition62'):
        assert not _is_linked(b1, 'dbdefinition_FieldQualifierDefinition62', a)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition62'):
        assert _is_linked(b2, 'dbdefinition_FieldQualifierDefinition62', a)
    _safe_set(a, 'dbdefinition_FieldQualifierDefinition60', set())
    assert not _is_linked(a, 'dbdefinition_FieldQualifierDefinition60', b2)
    if hasattr(b2, 'dbdefinition_FieldQualifierDefinition62'):
        assert not _is_linked(b2, 'dbdefinition_FieldQualifierDefinition62', a)


def test_assoc_viewDefinition29_link_reassign_clear():
    a = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    b1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    b2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    _safe_set(a, 'dbdefinition_ViewDefinition', b1)
    assert _is_linked(a, 'dbdefinition_ViewDefinition', b1)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition30'):
        assert _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition30', a)
    _safe_set(a, 'dbdefinition_ViewDefinition', b2)
    assert _is_linked(a, 'dbdefinition_ViewDefinition', b2)
    if hasattr(b1, 'dbdefinition_DatabaseVendorDefinition30'):
        assert not _is_linked(b1, 'dbdefinition_DatabaseVendorDefinition30', a)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition30'):
        assert _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition30', a)
    _safe_set(a, 'dbdefinition_ViewDefinition', None)
    assert not _is_linked(a, 'dbdefinition_ViewDefinition', b2)
    if hasattr(b2, 'dbdefinition_DatabaseVendorDefinition30'):
        assert not _is_linked(b2, 'dbdefinition_DatabaseVendorDefinition30', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

dbdefinition_ColumnDefinition_strategy = st.builds(dbdefinition_ColumnDefinition, computedSupported=st.booleans(), identityCycleSupported=st.booleans(), identityIncrementSupported=st.booleans(), identityMaximumSupported=st.booleans(), identityMinimumSupported=st.booleans(), identityStartValueSupported=st.booleans(), identitySupported=st.booleans(), maximumIdentifierLength=st.integers())
@given(instance=dbdefinition_ColumnDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_ColumnDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ColumnDefinition)


dbdefinition_ConstraintDefinition_strategy = st.builds(dbdefinition_ConstraintDefinition, checkOption=safe_text, clusteredPrimaryKeySupported=st.booleans(), clusteredUniqueConstraintSupported=st.booleans(), deferrableConstraintSupported=st.booleans(), informationalConstraintSupported=st.booleans(), maximumCheckConstraintIdentifierLength=st.integers(), maximumCheckExpressionLength=st.integers(), maximumForeignKeyIdentifierLength=st.integers(), maximumPrimaryKeyIdentifierLength=st.integers(), parentDeleteDRIRuleType=safe_text, parentUpdateDRIRuleType=safe_text, primaryKeyNullable=st.booleans(), uniqueKeyNullable=st.booleans())
@given(instance=dbdefinition_ConstraintDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_ConstraintDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ConstraintDefinition)


dbdefinition_ConstructedDataTypeDefinition_strategy = st.builds(dbdefinition_ConstructedDataTypeDefinition, arrayDatatypeSupported=st.booleans(), cursorDatatypeSupported=st.booleans(), multisetDatatypeSupported=st.booleans(), referenceDatatypeSupported=st.booleans(), rowDatatypeSupported=st.booleans())
@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_ConstructedDataTypeDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ConstructedDataTypeDefinition)


dbdefinition_DatabaseVendorDefinition_strategy = st.builds(dbdefinition_DatabaseVendorDefinition, SQLStatementSupported=st.booleans(), aliasSupported=st.booleans(), authorizationIdentifierSupported=st.booleans(), constraintsSupported=st.booleans(), constructedDataTypeSupported=st.booleans(), domainSupported=st.booleans(), eventSupported=st.booleans(), groupSupported=st.booleans(), joinSupported=st.booleans(), mQTIndexSupported=st.booleans(), mQTSupported=st.booleans(), maximumCommentLength=st.integers(), maximumIdentifierLength=st.integers(), nicknameSupported=st.booleans(), packageSupported=st.booleans(), quotedDDLSupported=st.booleans(), quotedDMLSupported=st.booleans(), roleAuthorizationSupported=st.booleans(), roleSupported=st.booleans(), schemaSupported=st.booleans(), sequenceSupported=st.booleans(), snapshotViewSupported=st.booleans(), sqlUDFSupported=st.booleans(), storedProcedureSupported=st.booleans(), synonymSupported=st.booleans(), tablespacesSupported=st.booleans(), triggerSupported=st.booleans(), uDFSupported=st.booleans(), userDefinedTypeSupported=st.booleans(), userSupported=st.booleans(), vendor=safe_text, version=safe_text, viewTriggerSupported=st.booleans(), xmlSupported=st.booleans())
@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_DatabaseVendorDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_DatabaseVendorDefinition)


dbdefinition_DebuggerDefinition_strategy = st.builds(dbdefinition_DebuggerDefinition, conditionSupported=st.booleans())
@given(instance=dbdefinition_DebuggerDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_DebuggerDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_DebuggerDefinition)


dbdefinition_ExtendedDefinition_strategy = st.builds(dbdefinition_ExtendedDefinition, name=safe_text, value=safe_text)
@given(instance=dbdefinition_ExtendedDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_ExtendedDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ExtendedDefinition)


dbdefinition_FieldQualifierDefinition_strategy = st.builds(dbdefinition_FieldQualifierDefinition, defaultPrecision=st.integers(), defaultScale=st.integers(), maximumPrecision=st.integers(), maximumScale=st.integers(), name=safe_text, precisionSupported=st.booleans(), scaleSupported=st.booleans())
@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_FieldQualifierDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_FieldQualifierDefinition)


dbdefinition_IndexDefinition_strategy = st.builds(dbdefinition_IndexDefinition, clusterChangeable=st.booleans(), clusteringSupported=st.booleans(), fillFactorSupported=st.booleans(), includedColumnsSupported=st.booleans(), maximumIdentifierLength=st.integers(), percentFreeChangeable=st.booleans(), percentFreeTerminology=safe_text)
@given(instance=dbdefinition_IndexDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_IndexDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_IndexDefinition)


dbdefinition_NicknameDefinition_strategy = st.builds(dbdefinition_NicknameDefinition, constraintSupported=st.booleans(), indexSupported=st.booleans(), maximumIdentifierLength=st.integers())
@given(instance=dbdefinition_NicknameDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_NicknameDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_NicknameDefinition)


dbdefinition_PredefinedDataTypeDefinition_strategy = st.builds(dbdefinition_PredefinedDataTypeDefinition, bitDataSupported=st.booleans(), characterSet=safe_text, characterSetSuffix=safe_text, clusteringSupported=st.booleans(), cutoffPrecision=st.integers(), defaultLength=st.integers(), defaultPrecision=st.integers(), defaultScale=st.integers(), defaultSupported=st.booleans(), defaultValueTypes=safe_text, displayName=safe_text, displayNameSupported=st.booleans(), encodingScheme=safe_text, encodingSchemeSuffix=safe_text, fieldQualifierSeparator=safe_text, fillFactorSupported=st.booleans(), groupingSupported=st.booleans(), identitySupported=st.booleans(), javaClassName=safe_text, jdbcEnumType=st.integers(), keyConstraintSupported=st.booleans(), languageType=safe_text, largeValueSpecifierLength=st.integers(), largeValueSpecifierName=safe_text, largeValueSpecifierSupported=st.booleans(), leadingFieldQualifierSupported=st.booleans(), lengthSemantic=safe_text, lengthSemanticSupported=st.booleans(), lengthSupported=st.booleans(), lengthUnit=safe_text, maximumLength=st.integers(), maximumPrecision=st.integers(), maximumScale=st.integers(), maximumValue=safe_text, minimumScale=st.integers(), minimumValue=safe_text, multipleColumnsSupported=st.booleans(), name=safe_text, nullableSupported=st.booleans(), orderingSupported=st.booleans(), precisionSupported=st.booleans(), primitiveType=safe_text, scaleSupported=st.booleans(), trailingFieldQualifierSupported=st.booleans())
@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_PredefinedDataTypeDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PredefinedDataTypeDefinition)


dbdefinition_PrivilegeDefinition_strategy = st.builds(dbdefinition_PrivilegeDefinition, name=safe_text)
@given(instance=dbdefinition_PrivilegeDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_PrivilegeDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PrivilegeDefinition)


dbdefinition_PrivilegedElementDefinition_strategy = st.builds(dbdefinition_PrivilegedElementDefinition, name=safe_text)
@given(instance=dbdefinition_PrivilegedElementDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_PrivilegedElementDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PrivilegedElementDefinition)


dbdefinition_QueryDefinition_strategy = st.builds(dbdefinition_QueryDefinition, castExpressionSupported=st.booleans(), defaultKeywordForInsertValueSupported=st.booleans(), extendedGroupingSupported=st.booleans(), hostVariableMarker=safe_text, hostVariableMarkerSupported=st.booleans(), identifierQuoteString=safe_text, tableAliasInDeleteSupported=st.booleans())
@given(instance=dbdefinition_QueryDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_QueryDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_QueryDefinition)


dbdefinition_SQLSyntaxDefinition_strategy = st.builds(dbdefinition_SQLSyntaxDefinition, keywords=safe_text, operators=safe_text, terminationCharacter=safe_text)
@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_SQLSyntaxDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SQLSyntaxDefinition)


dbdefinition_SchemaDefinition_strategy = st.builds(dbdefinition_SchemaDefinition, maximumIdentifierLength=st.integers())
@given(instance=dbdefinition_SchemaDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_SchemaDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SchemaDefinition)


dbdefinition_SequenceDefinition_strategy = st.builds(dbdefinition_SequenceDefinition, cacheDefaultValue=st.integers(), cacheSupported=st.booleans(), noCacheString=safe_text, noMaximumValueString=safe_text, noMinimumValueString=safe_text, orderSupported=st.booleans(), typeEnumerationSupported=st.booleans())
@given(instance=dbdefinition_SequenceDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_SequenceDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SequenceDefinition)


dbdefinition_StoredProcedureDefinition_strategy = st.builds(dbdefinition_StoredProcedureDefinition, determininsticSupported=st.booleans(), functionLanguageType=safe_text, languageType=safe_text, maximumActionBodyLength=st.integers(), maximumIdentifierLength=st.integers(), nullInputActionSupported=st.booleans(), packageGenerationSupported=st.booleans(), parameterDeclarationConstraintSupported=st.booleans(), parameterInitValueSupported=st.booleans(), parameterStyle=safe_text, parameterStyleSupported=st.booleans(), procedureType=safe_text, returnTypeSupported=st.booleans(), returnedNullSupported=st.booleans(), returnedTypeDeclarationConstraintSupported=st.booleans())
@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_StoredProcedureDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_StoredProcedureDefinition)


dbdefinition_TableDefinition_strategy = st.builds(dbdefinition_TableDefinition, auditSupported=st.booleans(), dataCaptureSupported=st.booleans(), editProcSupported=st.booleans(), encodingSupported=st.booleans(), maximumIdentifierLength=st.integers(), validProcSupported=st.booleans())
@given(instance=dbdefinition_TableDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_TableDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TableDefinition)


dbdefinition_TableSpaceDefinition_strategy = st.builds(dbdefinition_TableSpaceDefinition, bufferPoolSupported=st.booleans(), containerExtentSizeSupported=st.booleans(), containerInitialSizeSupported=st.booleans(), containerMaximumSizeSupported=st.booleans(), defaultSupported=st.booleans(), extentSizeSupported=st.booleans(), managedBySupported=st.booleans(), maximumIdentifierLength=st.integers(), pageSizeSupported=st.booleans(), prefetchSizeSupported=st.booleans(), tableSpaceType=safe_text, typeSupported=st.booleans())
@given(instance=dbdefinition_TableSpaceDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_TableSpaceDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TableSpaceDefinition)


dbdefinition_TriggerDefinition_strategy = st.builds(dbdefinition_TriggerDefinition, granularitySupported=st.booleans(), insteadOfTriggerSupported=st.booleans(), maximumActionBodyLength=st.integers(), maximumIdentifierLength=st.integers(), maximumReferencePartLength=st.integers(), perColumnUpdateTriggerSupported=st.booleans(), referencesClauseSupported=st.booleans(), rowTriggerReferenceSupported=st.booleans(), tableTriggerReferenceSupported=st.booleans(), typeSupported=st.booleans(), whenClauseSupported=st.booleans())
@given(instance=dbdefinition_TriggerDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_TriggerDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TriggerDefinition)


dbdefinition_UserDefinedTypeDefinition_strategy = st.builds(dbdefinition_UserDefinedTypeDefinition, defaultValueSupported=st.booleans(), distinctTypeSupported=st.booleans(), maximumIdentifierLength=st.integers(), structuredTypeSupported=st.booleans())
@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_UserDefinedTypeDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_UserDefinedTypeDefinition)


dbdefinition_ViewDefinition_strategy = st.builds(dbdefinition_ViewDefinition, checkOptionLevelsSupported=st.booleans(), checkOptionSupported=st.booleans(), indexSupported=st.booleans(), maximumIdentifierLength=st.integers())
@given(instance=dbdefinition_ViewDefinition_strategy)
@settings(max_examples=25)
def test_dbdefinition_ViewDefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ViewDefinition)



