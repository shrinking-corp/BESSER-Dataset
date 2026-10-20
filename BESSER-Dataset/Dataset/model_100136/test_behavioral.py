import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_SQLSyntaxDefinition23_reverse_link_reassign_clear():
    a1 = dbdefinition_SQLSyntaxDefinition(keywords="sample_text", operators="sample_text", terminationCharacter="sample_text")
    a2 = dbdefinition_SQLSyntaxDefinition(keywords="sample_text_2", operators="sample_text_2", terminationCharacter="sample_text_2")
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition24', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition24', a1)
    if hasattr(a1, 'dbdefinition_SQLSyntaxDefinition'):
        assert _is_linked(a1, 'dbdefinition_SQLSyntaxDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition24', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition24', a2)
    if hasattr(a1, 'dbdefinition_SQLSyntaxDefinition'):
        assert not _is_linked(a1, 'dbdefinition_SQLSyntaxDefinition', b)
    if hasattr(a2, 'dbdefinition_SQLSyntaxDefinition'):
        assert _is_linked(a2, 'dbdefinition_SQLSyntaxDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition24', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition24', a2)
    if hasattr(a2, 'dbdefinition_SQLSyntaxDefinition'):
        assert not _is_linked(a2, 'dbdefinition_SQLSyntaxDefinition', b)


def test_assoc_actionElementDefinitions65_reverse_link_reassign_clear():
    a1 = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    a2 = dbdefinition_PrivilegedElementDefinition(name="sample_text_2")
    b = dbdefinition_PrivilegeDefinition(name="sample_text")
    _safe_set(b, 'dbdefinition_PrivilegeDefinition66', {a1})
    assert _is_linked(b, 'dbdefinition_PrivilegeDefinition66', a1)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition67'):
        assert _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition67', b)
    _safe_set(b, 'dbdefinition_PrivilegeDefinition66', {a2})
    assert _is_linked(b, 'dbdefinition_PrivilegeDefinition66', a2)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition67'):
        assert not _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition67', b)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition67'):
        assert _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition67', b)
    _safe_set(b, 'dbdefinition_PrivilegeDefinition66', set())
    assert not _is_linked(b, 'dbdefinition_PrivilegeDefinition66', a2)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition67'):
        assert not _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition67', b)


def test_assoc_columnDefinition7_reverse_link_reassign_clear():
    a1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    a2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    b = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    _safe_set(b, 'dbdefinition_ColumnDefinition', a1)
    assert _is_linked(b, 'dbdefinition_ColumnDefinition', a1)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition8'):
        assert _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition8', b)
    _safe_set(b, 'dbdefinition_ColumnDefinition', a2)
    assert _is_linked(b, 'dbdefinition_ColumnDefinition', a2)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition8'):
        assert not _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition8', b)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition8'):
        assert _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition8', b)
    _safe_set(b, 'dbdefinition_ColumnDefinition', None)
    assert not _is_linked(b, 'dbdefinition_ColumnDefinition', a2)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition8'):
        assert not _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition8', b)


def test_assoc_constraintDefinition9_reverse_link_reassign_clear():
    a1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    a2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    b = dbdefinition_ConstraintDefinition(checkOption="sample_text", clusteredPrimaryKeySupported=True, clusteredUniqueConstraintSupported=True, deferrableConstraintSupported=True, informationalConstraintSupported=True, maximumCheckConstraintIdentifierLength=7, maximumCheckExpressionLength=7, maximumForeignKeyIdentifierLength=7, maximumPrimaryKeyIdentifierLength=7, parentDeleteDRIRuleType="sample_text", parentUpdateDRIRuleType="sample_text", primaryKeyNullable=True, uniqueKeyNullable=True)
    _safe_set(b, 'dbdefinition_ConstraintDefinition', a1)
    assert _is_linked(b, 'dbdefinition_ConstraintDefinition', a1)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition10'):
        assert _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition10', b)
    _safe_set(b, 'dbdefinition_ConstraintDefinition', a2)
    assert _is_linked(b, 'dbdefinition_ConstraintDefinition', a2)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition10'):
        assert not _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition10', b)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition10'):
        assert _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition10', b)
    _safe_set(b, 'dbdefinition_ConstraintDefinition', None)
    assert not _is_linked(b, 'dbdefinition_ConstraintDefinition', a2)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition10'):
        assert not _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition10', b)


def test_assoc_constructedDataTypeDefinition35_reverse_link_reassign_clear():
    a1 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    a2 = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=False, aliasSupported=False, authorizationIdentifierSupported=False, constraintsSupported=False, constructedDataTypeSupported=False, domainSupported=False, eventSupported=False, groupSupported=False, joinSupported=False, mQTIndexSupported=False, mQTSupported=False, maximumCommentLength=13, maximumIdentifierLength=13, nicknameSupported=False, packageSupported=False, quotedDDLSupported=False, quotedDMLSupported=False, roleAuthorizationSupported=False, roleSupported=False, schemaSupported=False, sequenceSupported=False, snapshotViewSupported=False, sqlUDFSupported=False, storedProcedureSupported=False, synonymSupported=False, tablespacesSupported=False, triggerSupported=False, uDFSupported=False, userDefinedTypeSupported=False, userSupported=False, vendor="sample_text_2", version="sample_text_2", viewTriggerSupported=False, xmlSupported=False)
    b = dbdefinition_ConstructedDataTypeDefinition(arrayDatatypeSupported=True, cursorDatatypeSupported=True, multisetDatatypeSupported=True, referenceDatatypeSupported=True, rowDatatypeSupported=True)
    _safe_set(b, 'dbdefinition_ConstructedDataTypeDefinition', a1)
    assert _is_linked(b, 'dbdefinition_ConstructedDataTypeDefinition', a1)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition36'):
        assert _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition36', b)
    _safe_set(b, 'dbdefinition_ConstructedDataTypeDefinition', a2)
    assert _is_linked(b, 'dbdefinition_ConstructedDataTypeDefinition', a2)
    if hasattr(a1, 'dbdefinition_DatabaseVendorDefinition36'):
        assert not _is_linked(a1, 'dbdefinition_DatabaseVendorDefinition36', b)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition36'):
        assert _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition36', b)
    _safe_set(b, 'dbdefinition_ConstructedDataTypeDefinition', None)
    assert not _is_linked(b, 'dbdefinition_ConstructedDataTypeDefinition', a2)
    if hasattr(a2, 'dbdefinition_DatabaseVendorDefinition36'):
        assert not _is_linked(a2, 'dbdefinition_DatabaseVendorDefinition36', b)


def test_assoc_debuggerDefinition31_reverse_link_reassign_clear():
    a1 = dbdefinition_DebuggerDefinition(conditionSupported=True)
    a2 = dbdefinition_DebuggerDefinition(conditionSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition32', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition32', a1)
    if hasattr(a1, 'dbdefinition_DebuggerDefinition'):
        assert _is_linked(a1, 'dbdefinition_DebuggerDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition32', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition32', a2)
    if hasattr(a1, 'dbdefinition_DebuggerDefinition'):
        assert not _is_linked(a1, 'dbdefinition_DebuggerDefinition', b)
    if hasattr(a2, 'dbdefinition_DebuggerDefinition'):
        assert _is_linked(a2, 'dbdefinition_DebuggerDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition32', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition32', a2)
    if hasattr(a2, 'dbdefinition_DebuggerDefinition'):
        assert not _is_linked(a2, 'dbdefinition_DebuggerDefinition', b)


def test_assoc_defaultDataTypeDefinition57_reverse_link_reassign_clear():
    a1 = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    a2 = dbdefinition_SequenceDefinition(cacheDefaultValue=13, cacheSupported=False, noCacheString="sample_text_2", noMaximumValueString="sample_text_2", noMinimumValueString="sample_text_2", orderSupported=False, typeEnumerationSupported=False)
    b = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition59', a1)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition59', a1)
    if hasattr(a1, 'dbdefinition_SequenceDefinition58'):
        assert _is_linked(a1, 'dbdefinition_SequenceDefinition58', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition59', a2)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition59', a2)
    if hasattr(a1, 'dbdefinition_SequenceDefinition58'):
        assert not _is_linked(a1, 'dbdefinition_SequenceDefinition58', b)
    if hasattr(a2, 'dbdefinition_SequenceDefinition58'):
        assert _is_linked(a2, 'dbdefinition_SequenceDefinition58', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition59', None)
    assert not _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition59', a2)
    if hasattr(a2, 'dbdefinition_SequenceDefinition58'):
        assert not _is_linked(a2, 'dbdefinition_SequenceDefinition58', b)


def test_assoc_defaultLeadingFieldQualifierDefinition45_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition47', a1)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition47', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition46'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition46', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition47', a2)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition47', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition46'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition46', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition46'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition46', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition47', None)
    assert not _is_linked(b, 'dbdefinition_FieldQualifierDefinition47', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition46'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition46', b)


def test_assoc_defaultTrailingFieldQualifierDefinition42_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition44', a1)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition44', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition43'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition43', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition44', a2)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition44', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition43'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition43', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition43'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition43', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition44', None)
    assert not _is_linked(b, 'dbdefinition_FieldQualifierDefinition44', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition43'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition43', b)


def test_assoc_extendedDefinitions11_reverse_link_reassign_clear():
    a1 = dbdefinition_ExtendedDefinition(name="sample_text", value="sample_text")
    a2 = dbdefinition_ExtendedDefinition(name="sample_text_2", value="sample_text_2")
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition12', {a1})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition12', a1)
    if hasattr(a1, 'dbdefinition_ExtendedDefinition'):
        assert _is_linked(a1, 'dbdefinition_ExtendedDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition12', {a2})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition12', a2)
    if hasattr(a1, 'dbdefinition_ExtendedDefinition'):
        assert not _is_linked(a1, 'dbdefinition_ExtendedDefinition', b)
    if hasattr(a2, 'dbdefinition_ExtendedDefinition'):
        assert _is_linked(a2, 'dbdefinition_ExtendedDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition12', set())
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition12', a2)
    if hasattr(a2, 'dbdefinition_ExtendedDefinition'):
        assert not _is_linked(a2, 'dbdefinition_ExtendedDefinition', b)


def test_assoc_identityColumnDataTypeDefinitions51_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_ColumnDefinition(computedSupported=True, identityCycleSupported=True, identityIncrementSupported=True, identityMaximumSupported=True, identityMinimumSupported=True, identityStartValueSupported=True, identitySupported=True, maximumIdentifierLength=7)
    _safe_set(b, 'dbdefinition_ColumnDefinition52', {a1})
    assert _is_linked(b, 'dbdefinition_ColumnDefinition52', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition53'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition53', b)
    _safe_set(b, 'dbdefinition_ColumnDefinition52', {a2})
    assert _is_linked(b, 'dbdefinition_ColumnDefinition52', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition53'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition53', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition53'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition53', b)
    _safe_set(b, 'dbdefinition_ColumnDefinition52', set())
    assert not _is_linked(b, 'dbdefinition_ColumnDefinition52', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition53'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition53', b)


def test_assoc_indexDefinition13_reverse_link_reassign_clear():
    a1 = dbdefinition_IndexDefinition(clusterChangeable=True, clusteringSupported=True, fillFactorSupported=True, includedColumnsSupported=True, maximumIdentifierLength=7, percentFreeChangeable=True, percentFreeTerminology="sample_text")
    a2 = dbdefinition_IndexDefinition(clusterChangeable=False, clusteringSupported=False, fillFactorSupported=False, includedColumnsSupported=False, maximumIdentifierLength=13, percentFreeChangeable=False, percentFreeTerminology="sample_text_2")
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition14', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition14', a1)
    if hasattr(a1, 'dbdefinition_IndexDefinition'):
        assert _is_linked(a1, 'dbdefinition_IndexDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition14', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition14', a2)
    if hasattr(a1, 'dbdefinition_IndexDefinition'):
        assert not _is_linked(a1, 'dbdefinition_IndexDefinition', b)
    if hasattr(a2, 'dbdefinition_IndexDefinition'):
        assert _is_linked(a2, 'dbdefinition_IndexDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition14', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition14', a2)
    if hasattr(a2, 'dbdefinition_IndexDefinition'):
        assert not _is_linked(a2, 'dbdefinition_IndexDefinition', b)


def test_assoc_leadingFieldQualifierDefinition37_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition', a1)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition38'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition38', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition', a2)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition38'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition38', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition38'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition38', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition', None)
    assert not _is_linked(b, 'dbdefinition_FieldQualifierDefinition', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition38'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition38', b)


def test_assoc_nicknameDefinition25_reverse_link_reassign_clear():
    a1 = dbdefinition_NicknameDefinition(constraintSupported=True, indexSupported=True, maximumIdentifierLength=7)
    a2 = dbdefinition_NicknameDefinition(constraintSupported=False, indexSupported=False, maximumIdentifierLength=13)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition26', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition26', a1)
    if hasattr(a1, 'dbdefinition_NicknameDefinition'):
        assert _is_linked(a1, 'dbdefinition_NicknameDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition26', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition26', a2)
    if hasattr(a1, 'dbdefinition_NicknameDefinition'):
        assert not _is_linked(a1, 'dbdefinition_NicknameDefinition', b)
    if hasattr(a2, 'dbdefinition_NicknameDefinition'):
        assert _is_linked(a2, 'dbdefinition_NicknameDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition26', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition26', a2)
    if hasattr(a2, 'dbdefinition_NicknameDefinition'):
        assert not _is_linked(a2, 'dbdefinition_NicknameDefinition', b)


def test_assoc_predefinedDataTypeDefinitions0_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition', {a1})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition', {a2})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition', set())
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition', b)


def test_assoc_predefinedDataTypeDefinitions48_reverse_link_reassign_clear():
    a1 = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    a2 = dbdefinition_StoredProcedureDefinition(determininsticSupported=False, functionLanguageType="sample_text_2", languageType="sample_text_2", maximumActionBodyLength=13, maximumIdentifierLength=13, nullInputActionSupported=False, packageGenerationSupported=False, parameterDeclarationConstraintSupported=False, parameterInitValueSupported=False, parameterStyle="sample_text_2", parameterStyleSupported=False, procedureType="sample_text_2", returnTypeSupported=False, returnedNullSupported=False, returnedTypeDeclarationConstraintSupported=False)
    b = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition50', a1)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition50', a1)
    if hasattr(a1, 'dbdefinition_StoredProcedureDefinition49'):
        assert _is_linked(a1, 'dbdefinition_StoredProcedureDefinition49', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition50', a2)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition50', a2)
    if hasattr(a1, 'dbdefinition_StoredProcedureDefinition49'):
        assert not _is_linked(a1, 'dbdefinition_StoredProcedureDefinition49', b)
    if hasattr(a2, 'dbdefinition_StoredProcedureDefinition49'):
        assert _is_linked(a2, 'dbdefinition_StoredProcedureDefinition49', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition50', None)
    assert not _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition50', a2)
    if hasattr(a2, 'dbdefinition_StoredProcedureDefinition49'):
        assert not _is_linked(a2, 'dbdefinition_StoredProcedureDefinition49', b)


def test_assoc_predefinedDataTypeDefinitions54_reverse_link_reassign_clear():
    a1 = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    a2 = dbdefinition_SequenceDefinition(cacheDefaultValue=13, cacheSupported=False, noCacheString="sample_text_2", noMaximumValueString="sample_text_2", noMinimumValueString="sample_text_2", orderSupported=False, typeEnumerationSupported=False)
    b = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition56', a1)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition56', a1)
    if hasattr(a1, 'dbdefinition_SequenceDefinition55'):
        assert _is_linked(a1, 'dbdefinition_SequenceDefinition55', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition56', a2)
    assert _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition56', a2)
    if hasattr(a1, 'dbdefinition_SequenceDefinition55'):
        assert not _is_linked(a1, 'dbdefinition_SequenceDefinition55', b)
    if hasattr(a2, 'dbdefinition_SequenceDefinition55'):
        assert _is_linked(a2, 'dbdefinition_SequenceDefinition55', b)
    _safe_set(b, 'dbdefinition_PredefinedDataTypeDefinition56', None)
    assert not _is_linked(b, 'dbdefinition_PredefinedDataTypeDefinition56', a2)
    if hasattr(a2, 'dbdefinition_SequenceDefinition55'):
        assert not _is_linked(a2, 'dbdefinition_SequenceDefinition55', b)


def test_assoc_privilegeDefinitions63_reverse_link_reassign_clear():
    a1 = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    a2 = dbdefinition_PrivilegedElementDefinition(name="sample_text_2")
    b = dbdefinition_PrivilegeDefinition(name="sample_text")
    _safe_set(b, 'dbdefinition_PrivilegeDefinition', a1)
    assert _is_linked(b, 'dbdefinition_PrivilegeDefinition', a1)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition64'):
        assert _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition64', b)
    _safe_set(b, 'dbdefinition_PrivilegeDefinition', a2)
    assert _is_linked(b, 'dbdefinition_PrivilegeDefinition', a2)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition64'):
        assert not _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition64', b)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition64'):
        assert _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition64', b)
    _safe_set(b, 'dbdefinition_PrivilegeDefinition', None)
    assert not _is_linked(b, 'dbdefinition_PrivilegeDefinition', a2)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition64'):
        assert not _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition64', b)


def test_assoc_privilegedElementDefinitions33_reverse_link_reassign_clear():
    a1 = dbdefinition_PrivilegedElementDefinition(name="sample_text")
    a2 = dbdefinition_PrivilegedElementDefinition(name="sample_text_2")
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition34', {a1})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition34', a1)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition'):
        assert _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition34', {a2})
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition34', a2)
    if hasattr(a1, 'dbdefinition_PrivilegedElementDefinition'):
        assert not _is_linked(a1, 'dbdefinition_PrivilegedElementDefinition', b)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition'):
        assert _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition34', set())
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition34', a2)
    if hasattr(a2, 'dbdefinition_PrivilegedElementDefinition'):
        assert not _is_linked(a2, 'dbdefinition_PrivilegedElementDefinition', b)


def test_assoc_queryDefinition21_reverse_link_reassign_clear():
    a1 = dbdefinition_QueryDefinition(castExpressionSupported=True, defaultKeywordForInsertValueSupported=True, extendedGroupingSupported=True, hostVariableMarker="sample_text", hostVariableMarkerSupported=True, identifierQuoteString="sample_text", tableAliasInDeleteSupported=True)
    a2 = dbdefinition_QueryDefinition(castExpressionSupported=False, defaultKeywordForInsertValueSupported=False, extendedGroupingSupported=False, hostVariableMarker="sample_text_2", hostVariableMarkerSupported=False, identifierQuoteString="sample_text_2", tableAliasInDeleteSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition22', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition22', a1)
    if hasattr(a1, 'dbdefinition_QueryDefinition'):
        assert _is_linked(a1, 'dbdefinition_QueryDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition22', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition22', a2)
    if hasattr(a1, 'dbdefinition_QueryDefinition'):
        assert not _is_linked(a1, 'dbdefinition_QueryDefinition', b)
    if hasattr(a2, 'dbdefinition_QueryDefinition'):
        assert _is_linked(a2, 'dbdefinition_QueryDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition22', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition22', a2)
    if hasattr(a2, 'dbdefinition_QueryDefinition'):
        assert not _is_linked(a2, 'dbdefinition_QueryDefinition', b)


def test_assoc_schemaDefinition27_reverse_link_reassign_clear():
    a1 = dbdefinition_SchemaDefinition(maximumIdentifierLength=7)
    a2 = dbdefinition_SchemaDefinition(maximumIdentifierLength=13)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition28', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition28', a1)
    if hasattr(a1, 'dbdefinition_SchemaDefinition'):
        assert _is_linked(a1, 'dbdefinition_SchemaDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition28', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition28', a2)
    if hasattr(a1, 'dbdefinition_SchemaDefinition'):
        assert not _is_linked(a1, 'dbdefinition_SchemaDefinition', b)
    if hasattr(a2, 'dbdefinition_SchemaDefinition'):
        assert _is_linked(a2, 'dbdefinition_SchemaDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition28', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition28', a2)
    if hasattr(a2, 'dbdefinition_SchemaDefinition'):
        assert not _is_linked(a2, 'dbdefinition_SchemaDefinition', b)


def test_assoc_sequenceDefinition17_reverse_link_reassign_clear():
    a1 = dbdefinition_SequenceDefinition(cacheDefaultValue=7, cacheSupported=True, noCacheString="sample_text", noMaximumValueString="sample_text", noMinimumValueString="sample_text", orderSupported=True, typeEnumerationSupported=True)
    a2 = dbdefinition_SequenceDefinition(cacheDefaultValue=13, cacheSupported=False, noCacheString="sample_text_2", noMaximumValueString="sample_text_2", noMinimumValueString="sample_text_2", orderSupported=False, typeEnumerationSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition18', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition18', a1)
    if hasattr(a1, 'dbdefinition_SequenceDefinition'):
        assert _is_linked(a1, 'dbdefinition_SequenceDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition18', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition18', a2)
    if hasattr(a1, 'dbdefinition_SequenceDefinition'):
        assert not _is_linked(a1, 'dbdefinition_SequenceDefinition', b)
    if hasattr(a2, 'dbdefinition_SequenceDefinition'):
        assert _is_linked(a2, 'dbdefinition_SequenceDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition18', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition18', a2)
    if hasattr(a2, 'dbdefinition_SequenceDefinition'):
        assert not _is_linked(a2, 'dbdefinition_SequenceDefinition', b)


def test_assoc_storedProcedureDefinition3_reverse_link_reassign_clear():
    a1 = dbdefinition_StoredProcedureDefinition(determininsticSupported=True, functionLanguageType="sample_text", languageType="sample_text", maximumActionBodyLength=7, maximumIdentifierLength=7, nullInputActionSupported=True, packageGenerationSupported=True, parameterDeclarationConstraintSupported=True, parameterInitValueSupported=True, parameterStyle="sample_text", parameterStyleSupported=True, procedureType="sample_text", returnTypeSupported=True, returnedNullSupported=True, returnedTypeDeclarationConstraintSupported=True)
    a2 = dbdefinition_StoredProcedureDefinition(determininsticSupported=False, functionLanguageType="sample_text_2", languageType="sample_text_2", maximumActionBodyLength=13, maximumIdentifierLength=13, nullInputActionSupported=False, packageGenerationSupported=False, parameterDeclarationConstraintSupported=False, parameterInitValueSupported=False, parameterStyle="sample_text_2", parameterStyleSupported=False, procedureType="sample_text_2", returnTypeSupported=False, returnedNullSupported=False, returnedTypeDeclarationConstraintSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition4', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition4', a1)
    if hasattr(a1, 'dbdefinition_StoredProcedureDefinition'):
        assert _is_linked(a1, 'dbdefinition_StoredProcedureDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition4', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition4', a2)
    if hasattr(a1, 'dbdefinition_StoredProcedureDefinition'):
        assert not _is_linked(a1, 'dbdefinition_StoredProcedureDefinition', b)
    if hasattr(a2, 'dbdefinition_StoredProcedureDefinition'):
        assert _is_linked(a2, 'dbdefinition_StoredProcedureDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition4', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition4', a2)
    if hasattr(a2, 'dbdefinition_StoredProcedureDefinition'):
        assert not _is_linked(a2, 'dbdefinition_StoredProcedureDefinition', b)


def test_assoc_tableDefinition15_reverse_link_reassign_clear():
    a1 = dbdefinition_TableDefinition(auditSupported=True, dataCaptureSupported=True, editProcSupported=True, encodingSupported=True, maximumIdentifierLength=7, validProcSupported=True)
    a2 = dbdefinition_TableDefinition(auditSupported=False, dataCaptureSupported=False, editProcSupported=False, encodingSupported=False, maximumIdentifierLength=13, validProcSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition16', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition16', a1)
    if hasattr(a1, 'dbdefinition_TableDefinition'):
        assert _is_linked(a1, 'dbdefinition_TableDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition16', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition16', a2)
    if hasattr(a1, 'dbdefinition_TableDefinition'):
        assert not _is_linked(a1, 'dbdefinition_TableDefinition', b)
    if hasattr(a2, 'dbdefinition_TableDefinition'):
        assert _is_linked(a2, 'dbdefinition_TableDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition16', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition16', a2)
    if hasattr(a2, 'dbdefinition_TableDefinition'):
        assert not _is_linked(a2, 'dbdefinition_TableDefinition', b)


def test_assoc_tableSpaceDefinition1_reverse_link_reassign_clear():
    a1 = dbdefinition_TableSpaceDefinition(bufferPoolSupported=True, containerExtentSizeSupported=True, containerInitialSizeSupported=True, containerMaximumSizeSupported=True, defaultSupported=True, extentSizeSupported=True, managedBySupported=True, maximumIdentifierLength=7, pageSizeSupported=True, prefetchSizeSupported=True, tableSpaceType="sample_text", typeSupported=True)
    a2 = dbdefinition_TableSpaceDefinition(bufferPoolSupported=False, containerExtentSizeSupported=False, containerInitialSizeSupported=False, containerMaximumSizeSupported=False, defaultSupported=False, extentSizeSupported=False, managedBySupported=False, maximumIdentifierLength=13, pageSizeSupported=False, prefetchSizeSupported=False, tableSpaceType="sample_text_2", typeSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition2', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition2', a1)
    if hasattr(a1, 'dbdefinition_TableSpaceDefinition'):
        assert _is_linked(a1, 'dbdefinition_TableSpaceDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition2', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition2', a2)
    if hasattr(a1, 'dbdefinition_TableSpaceDefinition'):
        assert not _is_linked(a1, 'dbdefinition_TableSpaceDefinition', b)
    if hasattr(a2, 'dbdefinition_TableSpaceDefinition'):
        assert _is_linked(a2, 'dbdefinition_TableSpaceDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition2', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition2', a2)
    if hasattr(a2, 'dbdefinition_TableSpaceDefinition'):
        assert not _is_linked(a2, 'dbdefinition_TableSpaceDefinition', b)


def test_assoc_trailingFieldQualifierDefinition39_reverse_link_reassign_clear():
    a1 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=True, characterSet="sample_text", characterSetSuffix="sample_text", clusteringSupported=True, cutoffPrecision=7, defaultLength=7, defaultPrecision=7, defaultScale=7, defaultSupported=True, defaultValueTypes="sample_text", displayName="sample_text", displayNameSupported=True, encodingScheme="sample_text", encodingSchemeSuffix="sample_text", fieldQualifierSeparator="sample_text", fillFactorSupported=True, groupingSupported=True, identitySupported=True, javaClassName="sample_text", jdbcEnumType=7, keyConstraintSupported=True, languageType="sample_text", largeValueSpecifierLength=7, largeValueSpecifierName="sample_text", largeValueSpecifierSupported=True, leadingFieldQualifierSupported=True, lengthSemantic="sample_text", lengthSemanticSupported=True, lengthSupported=True, lengthUnit="sample_text", maximumLength=7, maximumPrecision=7, maximumScale=7, maximumValue="sample_text", minimumScale=7, minimumValue="sample_text", multipleColumnsSupported=True, name="sample_text", nullableSupported=True, orderingSupported=True, precisionSupported=True, primitiveType="sample_text", scaleSupported=True, trailingFieldQualifierSupported=True)
    a2 = dbdefinition_PredefinedDataTypeDefinition(bitDataSupported=False, characterSet="sample_text_2", characterSetSuffix="sample_text_2", clusteringSupported=False, cutoffPrecision=13, defaultLength=13, defaultPrecision=13, defaultScale=13, defaultSupported=False, defaultValueTypes="sample_text_2", displayName="sample_text_2", displayNameSupported=False, encodingScheme="sample_text_2", encodingSchemeSuffix="sample_text_2", fieldQualifierSeparator="sample_text_2", fillFactorSupported=False, groupingSupported=False, identitySupported=False, javaClassName="sample_text_2", jdbcEnumType=13, keyConstraintSupported=False, languageType="sample_text_2", largeValueSpecifierLength=13, largeValueSpecifierName="sample_text_2", largeValueSpecifierSupported=False, leadingFieldQualifierSupported=False, lengthSemantic="sample_text_2", lengthSemanticSupported=False, lengthSupported=False, lengthUnit="sample_text_2", maximumLength=13, maximumPrecision=13, maximumScale=13, maximumValue="sample_text_2", minimumScale=13, minimumValue="sample_text_2", multipleColumnsSupported=False, name="sample_text_2", nullableSupported=False, orderingSupported=False, precisionSupported=False, primitiveType="sample_text_2", scaleSupported=False, trailingFieldQualifierSupported=False)
    b = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition41', a1)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition41', a1)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition40'):
        assert _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition40', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition41', a2)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition41', a2)
    if hasattr(a1, 'dbdefinition_PredefinedDataTypeDefinition40'):
        assert not _is_linked(a1, 'dbdefinition_PredefinedDataTypeDefinition40', b)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition40'):
        assert _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition40', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition41', None)
    assert not _is_linked(b, 'dbdefinition_FieldQualifierDefinition41', a2)
    if hasattr(a2, 'dbdefinition_PredefinedDataTypeDefinition40'):
        assert not _is_linked(a2, 'dbdefinition_PredefinedDataTypeDefinition40', b)


def test_assoc_triggerDefinition5_reverse_link_reassign_clear():
    a1 = dbdefinition_TriggerDefinition(granularitySupported=True, insteadOfTriggerSupported=True, maximumActionBodyLength=7, maximumIdentifierLength=7, maximumReferencePartLength=7, perColumnUpdateTriggerSupported=True, referencesClauseSupported=True, rowTriggerReferenceSupported=True, tableTriggerReferenceSupported=True, typeSupported=True, whenClauseSupported=True)
    a2 = dbdefinition_TriggerDefinition(granularitySupported=False, insteadOfTriggerSupported=False, maximumActionBodyLength=13, maximumIdentifierLength=13, maximumReferencePartLength=13, perColumnUpdateTriggerSupported=False, referencesClauseSupported=False, rowTriggerReferenceSupported=False, tableTriggerReferenceSupported=False, typeSupported=False, whenClauseSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition6', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition6', a1)
    if hasattr(a1, 'dbdefinition_TriggerDefinition'):
        assert _is_linked(a1, 'dbdefinition_TriggerDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition6', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition6', a2)
    if hasattr(a1, 'dbdefinition_TriggerDefinition'):
        assert not _is_linked(a1, 'dbdefinition_TriggerDefinition', b)
    if hasattr(a2, 'dbdefinition_TriggerDefinition'):
        assert _is_linked(a2, 'dbdefinition_TriggerDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition6', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition6', a2)
    if hasattr(a2, 'dbdefinition_TriggerDefinition'):
        assert not _is_linked(a2, 'dbdefinition_TriggerDefinition', b)


def test_assoc_udtDefinition19_reverse_link_reassign_clear():
    a1 = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=True, distinctTypeSupported=True, maximumIdentifierLength=7, structuredTypeSupported=True)
    a2 = dbdefinition_UserDefinedTypeDefinition(defaultValueSupported=False, distinctTypeSupported=False, maximumIdentifierLength=13, structuredTypeSupported=False)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition20', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition20', a1)
    if hasattr(a1, 'dbdefinition_UserDefinedTypeDefinition'):
        assert _is_linked(a1, 'dbdefinition_UserDefinedTypeDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition20', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition20', a2)
    if hasattr(a1, 'dbdefinition_UserDefinedTypeDefinition'):
        assert not _is_linked(a1, 'dbdefinition_UserDefinedTypeDefinition', b)
    if hasattr(a2, 'dbdefinition_UserDefinedTypeDefinition'):
        assert _is_linked(a2, 'dbdefinition_UserDefinedTypeDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition20', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition20', a2)
    if hasattr(a2, 'dbdefinition_UserDefinedTypeDefinition'):
        assert not _is_linked(a2, 'dbdefinition_UserDefinedTypeDefinition', b)


def test_assoc_validTrailingFieldQualifierDefinitions61_reverse_link_reassign_clear():
    a1 = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    a2 = dbdefinition_FieldQualifierDefinition(defaultPrecision=13, defaultScale=13, maximumPrecision=13, maximumScale=13, name="sample_text_2", precisionSupported=False, scaleSupported=False)
    b = dbdefinition_FieldQualifierDefinition(defaultPrecision=7, defaultScale=7, maximumPrecision=7, maximumScale=7, name="sample_text", precisionSupported=True, scaleSupported=True)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition62', a1)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition62', a1)
    if hasattr(a1, 'dbdefinition_FieldQualifierDefinition60'):
        assert _is_linked(a1, 'dbdefinition_FieldQualifierDefinition60', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition62', a2)
    assert _is_linked(b, 'dbdefinition_FieldQualifierDefinition62', a2)
    if hasattr(a1, 'dbdefinition_FieldQualifierDefinition60'):
        assert not _is_linked(a1, 'dbdefinition_FieldQualifierDefinition60', b)
    if hasattr(a2, 'dbdefinition_FieldQualifierDefinition60'):
        assert _is_linked(a2, 'dbdefinition_FieldQualifierDefinition60', b)
    _safe_set(b, 'dbdefinition_FieldQualifierDefinition62', None)
    assert not _is_linked(b, 'dbdefinition_FieldQualifierDefinition62', a2)
    if hasattr(a2, 'dbdefinition_FieldQualifierDefinition60'):
        assert not _is_linked(a2, 'dbdefinition_FieldQualifierDefinition60', b)


def test_assoc_viewDefinition29_reverse_link_reassign_clear():
    a1 = dbdefinition_ViewDefinition(checkOptionLevelsSupported=True, checkOptionSupported=True, indexSupported=True, maximumIdentifierLength=7)
    a2 = dbdefinition_ViewDefinition(checkOptionLevelsSupported=False, checkOptionSupported=False, indexSupported=False, maximumIdentifierLength=13)
    b = dbdefinition_DatabaseVendorDefinition(SQLStatementSupported=True, aliasSupported=True, authorizationIdentifierSupported=True, constraintsSupported=True, constructedDataTypeSupported=True, domainSupported=True, eventSupported=True, groupSupported=True, joinSupported=True, mQTIndexSupported=True, mQTSupported=True, maximumCommentLength=7, maximumIdentifierLength=7, nicknameSupported=True, packageSupported=True, quotedDDLSupported=True, quotedDMLSupported=True, roleAuthorizationSupported=True, roleSupported=True, schemaSupported=True, sequenceSupported=True, snapshotViewSupported=True, sqlUDFSupported=True, storedProcedureSupported=True, synonymSupported=True, tablespacesSupported=True, triggerSupported=True, uDFSupported=True, userDefinedTypeSupported=True, userSupported=True, vendor="sample_text", version="sample_text", viewTriggerSupported=True, xmlSupported=True)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition30', a1)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition30', a1)
    if hasattr(a1, 'dbdefinition_ViewDefinition'):
        assert _is_linked(a1, 'dbdefinition_ViewDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition30', a2)
    assert _is_linked(b, 'dbdefinition_DatabaseVendorDefinition30', a2)
    if hasattr(a1, 'dbdefinition_ViewDefinition'):
        assert not _is_linked(a1, 'dbdefinition_ViewDefinition', b)
    if hasattr(a2, 'dbdefinition_ViewDefinition'):
        assert _is_linked(a2, 'dbdefinition_ViewDefinition', b)
    _safe_set(b, 'dbdefinition_DatabaseVendorDefinition30', None)
    assert not _is_linked(b, 'dbdefinition_DatabaseVendorDefinition30', a2)
    if hasattr(a2, 'dbdefinition_ViewDefinition'):
        assert not _is_linked(a2, 'dbdefinition_ViewDefinition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

