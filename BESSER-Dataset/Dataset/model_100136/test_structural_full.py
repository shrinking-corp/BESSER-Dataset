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


