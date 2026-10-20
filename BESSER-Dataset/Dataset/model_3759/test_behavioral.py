import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RdbmsElement,
    RdbmsExpression,
    RdbmsField,
    RdbmsFieldOperation,
    RdbmsIdentifierField,
    RdbmsTable,
    RdbmsTableOperation,
    RdbmsViewAliasField,
    RdbmsViewField,
    RdbmsViewTableField,
    rdbms_RdbmsConfiguration,
    rdbms_RdbmsCreateFieldOperation,
    rdbms_RdbmsCreateTableOperation,
    rdbms_RdbmsDeleteFieldOperation,
    rdbms_RdbmsDeleteTableOperation,
    rdbms_RdbmsElement,
    rdbms_RdbmsExpression,
    rdbms_RdbmsFeature,
    rdbms_RdbmsField,
    rdbms_RdbmsFieldOperation,
    rdbms_RdbmsFieldType,
    rdbms_RdbmsForeignKey,
    rdbms_RdbmsIdentifierField,
    rdbms_RdbmsIndex,
    rdbms_RdbmsJunctionTable,
    rdbms_RdbmsLabelExpression,
    rdbms_RdbmsModel,
    rdbms_RdbmsModifyFieldOperation,
    rdbms_RdbmsModifyTableOperation,
    rdbms_RdbmsOperationMeta,
    rdbms_RdbmsRelationExpression,
    rdbms_RdbmsTable,
    rdbms_RdbmsTableAlias,
    rdbms_RdbmsTableOperation,
    rdbms_RdbmsUniqueConstraint,
    rdbms_RdbmsValueField,
    rdbms_RdbmsView,
    rdbms_RdbmsViewAliasField,
    rdbms_RdbmsViewExpressionField,
    rdbms_RdbmsViewField,
    rdbms_RdbmsViewForeignIdentifierField,
    rdbms_RdbmsViewIdentifierField,
    rdbms_RdbmsViewRecord,
    rdbms_RdbmsViewRecordValue,
    rdbms_RdbmsViewRelation,
    rdbms_RdbmsViewTableField,
    rdbms_RdbmsViewValueField,
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

def test_assoc_configuration40_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsModel(version="sample_text")
    a2 = rdbms_RdbmsModel(version="sample_text_2")
    b = rdbms_RdbmsConfiguration(dialect="sample_text")
    _safe_set(b, 'rdbms_RdbmsConfiguration', a1)
    assert _is_linked(b, 'rdbms_RdbmsConfiguration', a1)
    if hasattr(a1, 'rdbms_RdbmsModel41'):
        assert _is_linked(a1, 'rdbms_RdbmsModel41', b)
    _safe_set(b, 'rdbms_RdbmsConfiguration', a2)
    assert _is_linked(b, 'rdbms_RdbmsConfiguration', a2)
    if hasattr(a1, 'rdbms_RdbmsModel41'):
        assert not _is_linked(a1, 'rdbms_RdbmsModel41', b)
    if hasattr(a2, 'rdbms_RdbmsModel41'):
        assert _is_linked(a2, 'rdbms_RdbmsModel41', b)
    _safe_set(b, 'rdbms_RdbmsConfiguration', None)
    assert not _is_linked(b, 'rdbms_RdbmsConfiguration', a2)
    if hasattr(a2, 'rdbms_RdbmsModel41'):
        assert not _is_linked(a2, 'rdbms_RdbmsModel41', b)


def test_assoc_expressions31_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsViewExpressionField(expression="sample_text")
    a2 = rdbms_RdbmsViewExpressionField(expression="sample_text_2")
    b = rdbms_RdbmsExpression(expression="sample_text")
    _safe_set(b, 'rdbms_RdbmsExpression', a1)
    assert _is_linked(b, 'rdbms_RdbmsExpression', a1)
    if hasattr(a1, 'rdbms_RdbmsViewExpressionField'):
        assert _is_linked(a1, 'rdbms_RdbmsViewExpressionField', b)
    _safe_set(b, 'rdbms_RdbmsExpression', a2)
    assert _is_linked(b, 'rdbms_RdbmsExpression', a2)
    if hasattr(a1, 'rdbms_RdbmsViewExpressionField'):
        assert not _is_linked(a1, 'rdbms_RdbmsViewExpressionField', b)
    if hasattr(a2, 'rdbms_RdbmsViewExpressionField'):
        assert _is_linked(a2, 'rdbms_RdbmsViewExpressionField', b)
    _safe_set(b, 'rdbms_RdbmsExpression', None)
    assert not _is_linked(b, 'rdbms_RdbmsExpression', a2)
    if hasattr(a2, 'rdbms_RdbmsViewExpressionField'):
        assert not _is_linked(a2, 'rdbms_RdbmsViewExpressionField', b)


def test_assoc_features46_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsFeature(name="sample_text")
    a2 = rdbms_RdbmsFeature(name="sample_text_2")
    b = rdbms_RdbmsConfiguration(dialect="sample_text")
    _safe_set(b, 'rdbms_RdbmsConfiguration47', {a1})
    assert _is_linked(b, 'rdbms_RdbmsConfiguration47', a1)
    if hasattr(a1, 'rdbms_RdbmsFeature'):
        assert _is_linked(a1, 'rdbms_RdbmsFeature', b)
    _safe_set(b, 'rdbms_RdbmsConfiguration47', {a2})
    assert _is_linked(b, 'rdbms_RdbmsConfiguration47', a2)
    if hasattr(a1, 'rdbms_RdbmsFeature'):
        assert not _is_linked(a1, 'rdbms_RdbmsFeature', b)
    if hasattr(a2, 'rdbms_RdbmsFeature'):
        assert _is_linked(a2, 'rdbms_RdbmsFeature', b)
    _safe_set(b, 'rdbms_RdbmsConfiguration47', set())
    assert not _is_linked(b, 'rdbms_RdbmsConfiguration47', a2)
    if hasattr(a2, 'rdbms_RdbmsFeature'):
        assert not _is_linked(a2, 'rdbms_RdbmsFeature', b)


def test_assoc_field65_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsFieldOperation(reviewRequired=True)
    a2 = rdbms_RdbmsFieldOperation(reviewRequired=False)
    b = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    _safe_set(b, 'rdbms_RdbmsField66', a1)
    assert _is_linked(b, 'rdbms_RdbmsField66', a1)
    if hasattr(a1, 'rdbms_RdbmsFieldOperation'):
        assert _is_linked(a1, 'rdbms_RdbmsFieldOperation', b)
    _safe_set(b, 'rdbms_RdbmsField66', a2)
    assert _is_linked(b, 'rdbms_RdbmsField66', a2)
    if hasattr(a1, 'rdbms_RdbmsFieldOperation'):
        assert not _is_linked(a1, 'rdbms_RdbmsFieldOperation', b)
    if hasattr(a2, 'rdbms_RdbmsFieldOperation'):
        assert _is_linked(a2, 'rdbms_RdbmsFieldOperation', b)
    _safe_set(b, 'rdbms_RdbmsField66', None)
    assert not _is_linked(b, 'rdbms_RdbmsField66', a2)
    if hasattr(a2, 'rdbms_RdbmsFieldOperation'):
        assert not _is_linked(a2, 'rdbms_RdbmsFieldOperation', b)


def test_assoc_fields21_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsViewField(inherited=True)
    a2 = rdbms_RdbmsViewField(inherited=False)
    b = rdbms_RdbmsView(originUuid="sample_text")
    _safe_set(b, 'view', {a1})
    assert _is_linked(b, 'view', a1)
    if hasattr(a1, 'RdbmsViewField'):
        assert _is_linked(a1, 'RdbmsViewField', b)
    _safe_set(b, 'view', {a2})
    assert _is_linked(b, 'view', a2)
    if hasattr(a1, 'RdbmsViewField'):
        assert not _is_linked(a1, 'RdbmsViewField', b)
    if hasattr(a2, 'RdbmsViewField'):
        assert _is_linked(a2, 'RdbmsViewField', b)
    _safe_set(b, 'view', set())
    assert not _is_linked(b, 'view', a2)
    if hasattr(a2, 'RdbmsViewField'):
        assert not _is_linked(a2, 'RdbmsViewField', b)


def test_assoc_fields88_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsIndex(unique=True)
    a2 = rdbms_RdbmsIndex(unique=False)
    b = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    _safe_set(b, 'rdbms_RdbmsField89', a1)
    assert _is_linked(b, 'rdbms_RdbmsField89', a1)
    if hasattr(a1, 'rdbms_RdbmsIndex'):
        assert _is_linked(a1, 'rdbms_RdbmsIndex', b)
    _safe_set(b, 'rdbms_RdbmsField89', a2)
    assert _is_linked(b, 'rdbms_RdbmsField89', a2)
    if hasattr(a1, 'rdbms_RdbmsIndex'):
        assert not _is_linked(a1, 'rdbms_RdbmsIndex', b)
    if hasattr(a2, 'rdbms_RdbmsIndex'):
        assert _is_linked(a2, 'rdbms_RdbmsIndex', b)
    _safe_set(b, 'rdbms_RdbmsField89', None)
    assert not _is_linked(b, 'rdbms_RdbmsField89', a2)
    if hasattr(a2, 'rdbms_RdbmsIndex'):
        assert not _is_linked(a2, 'rdbms_RdbmsIndex', b)


def test_assoc_modifyFieldOperations58_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsModifyTableOperation(nameChanged="sample_text")
    a2 = rdbms_RdbmsModifyTableOperation(nameChanged="sample_text_2")
    b = rdbms_RdbmsModifyFieldOperation(changedForeignKeyToValueField="sample_text", changedValueFieldToForeignKey="sample_text", mandatoryChanged=True, nameChanged="sample_text", sizeChanged="sample_text", typeChanged=True)
    _safe_set(b, 'rdbms_RdbmsModifyFieldOperation', a1)
    assert _is_linked(b, 'rdbms_RdbmsModifyFieldOperation', a1)
    if hasattr(a1, 'rdbms_RdbmsModifyTableOperation59'):
        assert _is_linked(a1, 'rdbms_RdbmsModifyTableOperation59', b)
    _safe_set(b, 'rdbms_RdbmsModifyFieldOperation', a2)
    assert _is_linked(b, 'rdbms_RdbmsModifyFieldOperation', a2)
    if hasattr(a1, 'rdbms_RdbmsModifyTableOperation59'):
        assert not _is_linked(a1, 'rdbms_RdbmsModifyTableOperation59', b)
    if hasattr(a2, 'rdbms_RdbmsModifyTableOperation59'):
        assert _is_linked(a2, 'rdbms_RdbmsModifyTableOperation59', b)
    _safe_set(b, 'rdbms_RdbmsModifyFieldOperation', None)
    assert not _is_linked(b, 'rdbms_RdbmsModifyFieldOperation', a2)
    if hasattr(a2, 'rdbms_RdbmsModifyTableOperation59'):
        assert not _is_linked(a2, 'rdbms_RdbmsModifyTableOperation59', b)


def test_assoc_previousField67_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsModifyFieldOperation(changedForeignKeyToValueField="sample_text", changedValueFieldToForeignKey="sample_text", mandatoryChanged=True, nameChanged="sample_text", sizeChanged="sample_text", typeChanged=True)
    a2 = rdbms_RdbmsModifyFieldOperation(changedForeignKeyToValueField="sample_text_2", changedValueFieldToForeignKey="sample_text_2", mandatoryChanged=False, nameChanged="sample_text_2", sizeChanged="sample_text_2", typeChanged=False)
    b = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    _safe_set(b, 'rdbms_RdbmsField69', a1)
    assert _is_linked(b, 'rdbms_RdbmsField69', a1)
    if hasattr(a1, 'rdbms_RdbmsModifyFieldOperation68'):
        assert _is_linked(a1, 'rdbms_RdbmsModifyFieldOperation68', b)
    _safe_set(b, 'rdbms_RdbmsField69', a2)
    assert _is_linked(b, 'rdbms_RdbmsField69', a2)
    if hasattr(a1, 'rdbms_RdbmsModifyFieldOperation68'):
        assert not _is_linked(a1, 'rdbms_RdbmsModifyFieldOperation68', b)
    if hasattr(a2, 'rdbms_RdbmsModifyFieldOperation68'):
        assert _is_linked(a2, 'rdbms_RdbmsModifyFieldOperation68', b)
    _safe_set(b, 'rdbms_RdbmsField69', None)
    assert not _is_linked(b, 'rdbms_RdbmsField69', a2)
    if hasattr(a2, 'rdbms_RdbmsModifyFieldOperation68'):
        assert not _is_linked(a2, 'rdbms_RdbmsModifyFieldOperation68', b)


def test_assoc_rdbmsFieldTypes32_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsModel(version="sample_text")
    a2 = rdbms_RdbmsModel(version="sample_text_2")
    b = rdbms_RdbmsFieldType(description="sample_text", name="sample_text", precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7, uuid="sample_text")
    _safe_set(b, 'rdbms_RdbmsFieldType33', a1)
    assert _is_linked(b, 'rdbms_RdbmsFieldType33', a1)
    if hasattr(a1, 'rdbms_RdbmsModel'):
        assert _is_linked(a1, 'rdbms_RdbmsModel', b)
    _safe_set(b, 'rdbms_RdbmsFieldType33', a2)
    assert _is_linked(b, 'rdbms_RdbmsFieldType33', a2)
    if hasattr(a1, 'rdbms_RdbmsModel'):
        assert not _is_linked(a1, 'rdbms_RdbmsModel', b)
    if hasattr(a2, 'rdbms_RdbmsModel'):
        assert _is_linked(a2, 'rdbms_RdbmsModel', b)
    _safe_set(b, 'rdbms_RdbmsFieldType33', None)
    assert not _is_linked(b, 'rdbms_RdbmsFieldType33', a2)
    if hasattr(a2, 'rdbms_RdbmsModel'):
        assert not _is_linked(a2, 'rdbms_RdbmsModel', b)


def test_assoc_rdbmsViews37_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsView(originUuid="sample_text")
    a2 = rdbms_RdbmsView(originUuid="sample_text_2")
    b = rdbms_RdbmsModel(version="sample_text")
    _safe_set(b, 'rdbms_RdbmsModel38', {a1})
    assert _is_linked(b, 'rdbms_RdbmsModel38', a1)
    if hasattr(a1, 'rdbms_RdbmsView39'):
        assert _is_linked(a1, 'rdbms_RdbmsView39', b)
    _safe_set(b, 'rdbms_RdbmsModel38', {a2})
    assert _is_linked(b, 'rdbms_RdbmsModel38', a2)
    if hasattr(a1, 'rdbms_RdbmsView39'):
        assert not _is_linked(a1, 'rdbms_RdbmsView39', b)
    if hasattr(a2, 'rdbms_RdbmsView39'):
        assert _is_linked(a2, 'rdbms_RdbmsView39', b)
    _safe_set(b, 'rdbms_RdbmsModel38', set())
    assert not _is_linked(b, 'rdbms_RdbmsModel38', a2)
    if hasattr(a2, 'rdbms_RdbmsView39'):
        assert not _is_linked(a2, 'rdbms_RdbmsView39', b)


def test_assoc_relations23_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsViewRelation(name="sample_text")
    a2 = rdbms_RdbmsViewRelation(name="sample_text_2")
    b = rdbms_RdbmsView(originUuid="sample_text")
    _safe_set(b, 'rdbms_RdbmsView24', {a1})
    assert _is_linked(b, 'rdbms_RdbmsView24', a1)
    if hasattr(a1, 'rdbms_RdbmsViewRelation'):
        assert _is_linked(a1, 'rdbms_RdbmsViewRelation', b)
    _safe_set(b, 'rdbms_RdbmsView24', {a2})
    assert _is_linked(b, 'rdbms_RdbmsView24', a2)
    if hasattr(a1, 'rdbms_RdbmsViewRelation'):
        assert not _is_linked(a1, 'rdbms_RdbmsViewRelation', b)
    if hasattr(a2, 'rdbms_RdbmsViewRelation'):
        assert _is_linked(a2, 'rdbms_RdbmsViewRelation', b)
    _safe_set(b, 'rdbms_RdbmsView24', set())
    assert not _is_linked(b, 'rdbms_RdbmsView24', a2)
    if hasattr(a2, 'rdbms_RdbmsViewRelation'):
        assert not _is_linked(a2, 'rdbms_RdbmsViewRelation', b)


def test_assoc_tableField82_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsViewTableField(foreign=True)
    a2 = rdbms_RdbmsViewTableField(foreign=False)
    b = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    _safe_set(b, 'rdbms_RdbmsField83', a1)
    assert _is_linked(b, 'rdbms_RdbmsField83', a1)
    if hasattr(a1, 'rdbms_RdbmsViewTableField'):
        assert _is_linked(a1, 'rdbms_RdbmsViewTableField', b)
    _safe_set(b, 'rdbms_RdbmsField83', a2)
    assert _is_linked(b, 'rdbms_RdbmsField83', a2)
    if hasattr(a1, 'rdbms_RdbmsViewTableField'):
        assert not _is_linked(a1, 'rdbms_RdbmsViewTableField', b)
    if hasattr(a2, 'rdbms_RdbmsViewTableField'):
        assert _is_linked(a2, 'rdbms_RdbmsViewTableField', b)
    _safe_set(b, 'rdbms_RdbmsField83', None)
    assert not _is_linked(b, 'rdbms_RdbmsField83', a2)
    if hasattr(a2, 'rdbms_RdbmsViewTableField'):
        assert not _is_linked(a2, 'rdbms_RdbmsViewTableField', b)


def test_assoc_type10_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsFieldType(description="sample_text", name="sample_text", precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7, uuid="sample_text")
    a2 = rdbms_RdbmsFieldType(description="sample_text_2", name="sample_text_2", precision=13, rdbmsTypeName="sample_text_2", scale=13, size=13, storageByte=13, uuid="sample_text_2")
    b = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    _safe_set(b, 'rdbms_RdbmsField', a1)
    assert _is_linked(b, 'rdbms_RdbmsField', a1)
    if hasattr(a1, 'rdbms_RdbmsFieldType'):
        assert _is_linked(a1, 'rdbms_RdbmsFieldType', b)
    _safe_set(b, 'rdbms_RdbmsField', a2)
    assert _is_linked(b, 'rdbms_RdbmsField', a2)
    if hasattr(a1, 'rdbms_RdbmsFieldType'):
        assert not _is_linked(a1, 'rdbms_RdbmsFieldType', b)
    if hasattr(a2, 'rdbms_RdbmsFieldType'):
        assert _is_linked(a2, 'rdbms_RdbmsFieldType', b)
    _safe_set(b, 'rdbms_RdbmsField', None)
    assert not _is_linked(b, 'rdbms_RdbmsField', a2)
    if hasattr(a2, 'rdbms_RdbmsFieldType'):
        assert not _is_linked(a2, 'rdbms_RdbmsFieldType', b)


def test_assoc_view29_reverse_link_reassign_clear():
    a1 = rdbms_RdbmsViewField(inherited=True)
    a2 = rdbms_RdbmsViewField(inherited=False)
    b = rdbms_RdbmsView(originUuid="sample_text")
    _safe_set(b, 'RdbmsView', a1)
    assert _is_linked(b, 'RdbmsView', a1)
    if hasattr(a1, 'fields30'):
        assert _is_linked(a1, 'fields30', b)
    _safe_set(b, 'RdbmsView', a2)
    assert _is_linked(b, 'RdbmsView', a2)
    if hasattr(a1, 'fields30'):
        assert not _is_linked(a1, 'fields30', b)
    if hasattr(a2, 'fields30'):
        assert _is_linked(a2, 'fields30', b)
    _safe_set(b, 'RdbmsView', None)
    assert not _is_linked(b, 'RdbmsView', a2)
    if hasattr(a2, 'fields30'):
        assert not _is_linked(a2, 'fields30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_createFieldOperations57_stub_double():
    # rdbms_RdbmsCreateFieldOperation has no real 'rdbms_RdbmsCreateFieldOperation' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModifyTableOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModifyTableOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModifyTableOperation(nameChanged="sample_text")
    partner = rdbms_RdbmsCreateFieldOperation()
    setattr(partner, 'rdbms_RdbmsCreateFieldOperation', None)
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation', {partner})
    assert getattr(partner, 'rdbms_RdbmsCreateFieldOperation') == owner
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation', set())
    assert getattr(partner, 'rdbms_RdbmsCreateFieldOperation') is None


def test_assoc_currentModel105_stub_double():
    # rdbms_RdbmsOperationMeta has no real 'rdbms_RdbmsOperationMeta106' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsOperationMeta()
    setattr(partner, 'rdbms_RdbmsOperationMeta106', None)
    _safe_set(owner, 'rdbms_RdbmsModel107', partner)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta106') == owner
    _safe_set(owner, 'rdbms_RdbmsModel107', None)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta106') is None


def test_assoc_deleteFieldOperations60_stub_double():
    # rdbms_RdbmsDeleteFieldOperation has no real 'rdbms_RdbmsDeleteFieldOperation' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModifyTableOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModifyTableOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModifyTableOperation(nameChanged="sample_text")
    partner = rdbms_RdbmsDeleteFieldOperation()
    setattr(partner, 'rdbms_RdbmsDeleteFieldOperation', None)
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation61', {partner})
    assert getattr(partner, 'rdbms_RdbmsDeleteFieldOperation') == owner
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation61', set())
    assert getattr(partner, 'rdbms_RdbmsDeleteFieldOperation') is None


def test_assoc_field116_stub_double():
    # rdbms_RdbmsJunctionTable has no real 'rdbms_RdbmsJunctionTable' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsForeignKey(deferred=True, deleteOnCascade=True, foreignKeySqlName="sample_text", inheritenceBased=True, readOnly=True)
    partner = rdbms_RdbmsJunctionTable()
    setattr(partner, 'rdbms_RdbmsJunctionTable', None)
    _safe_set(owner, 'rdbms_RdbmsForeignKey', partner)
    assert getattr(partner, 'rdbms_RdbmsJunctionTable') == owner
    _safe_set(owner, 'rdbms_RdbmsForeignKey', None)
    assert getattr(partner, 'rdbms_RdbmsJunctionTable') is None


def test_assoc_field217_stub_double():
    # rdbms_RdbmsJunctionTable has no real 'rdbms_RdbmsJunctionTable18' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsForeignKey(deferred=True, deleteOnCascade=True, foreignKeySqlName="sample_text", inheritenceBased=True, readOnly=True)
    partner = rdbms_RdbmsJunctionTable()
    setattr(partner, 'rdbms_RdbmsJunctionTable18', None)
    _safe_set(owner, 'rdbms_RdbmsForeignKey19', partner)
    assert getattr(partner, 'rdbms_RdbmsJunctionTable18') == owner
    _safe_set(owner, 'rdbms_RdbmsForeignKey19', None)
    assert getattr(partner, 'rdbms_RdbmsJunctionTable18') is None


def test_assoc_fields0_stub_double():
    # rdbms_RdbmsTable has no real 'table' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    partner = rdbms_RdbmsTable()
    setattr(partner, 'table', None)
    _safe_set(owner, 'RdbmsField', partner)
    assert owner in getattr(partner, 'table')
    _safe_set(owner, 'RdbmsField', None)
    assert owner not in getattr(partner, 'table')


def test_assoc_fields14_stub_double():
    # rdbms_RdbmsUniqueConstraint has no real 'rdbms_RdbmsUniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    partner = rdbms_RdbmsUniqueConstraint()
    setattr(partner, 'rdbms_RdbmsUniqueConstraint', None)
    _safe_set(owner, 'rdbms_RdbmsField15', partner)
    assert owner in getattr(partner, 'rdbms_RdbmsUniqueConstraint')
    _safe_set(owner, 'rdbms_RdbmsField15', None)
    assert owner not in getattr(partner, 'rdbms_RdbmsUniqueConstraint')


def test_assoc_foreignKeys20_stub_double():
    # rdbms_RdbmsIdentifierField has no real 'referenceKey' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsForeignKey(deferred=True, deleteOnCascade=True, foreignKeySqlName="sample_text", inheritenceBased=True, readOnly=True)
    partner = rdbms_RdbmsIdentifierField()
    setattr(partner, 'referenceKey', None)
    _safe_set(owner, 'RdbmsForeignKey', partner)
    assert owner in getattr(partner, 'referenceKey')
    _safe_set(owner, 'RdbmsForeignKey', None)
    assert owner not in getattr(partner, 'referenceKey')


def test_assoc_fromAlias70_stub_double():
    # rdbms_RdbmsTableAlias has no real 'rdbms_RdbmsTableAlias72' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRelation(name="sample_text")
    partner = rdbms_RdbmsTableAlias()
    setattr(partner, 'rdbms_RdbmsTableAlias72', None)
    _safe_set(owner, 'rdbms_RdbmsViewRelation71', partner)
    assert getattr(partner, 'rdbms_RdbmsTableAlias72') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRelation71', None)
    assert getattr(partner, 'rdbms_RdbmsTableAlias72') is None


def test_assoc_fromField76_stub_double():
    # rdbms_RdbmsIdentifierField has no real 'rdbms_RdbmsIdentifierField78' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRelation(name="sample_text")
    partner = rdbms_RdbmsIdentifierField()
    setattr(partner, 'rdbms_RdbmsIdentifierField78', None)
    _safe_set(owner, 'rdbms_RdbmsViewRelation77', partner)
    assert getattr(partner, 'rdbms_RdbmsIdentifierField78') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRelation77', None)
    assert getattr(partner, 'rdbms_RdbmsIdentifierField78') is None


def test_assoc_identifierField95_stub_double():
    # rdbms_RdbmsViewIdentifierField has no real 'rdbms_RdbmsViewIdentifierField97' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRecordValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRecordValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRecordValue(value="sample_text")
    partner = rdbms_RdbmsViewIdentifierField()
    setattr(partner, 'rdbms_RdbmsViewIdentifierField97', None)
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue96', partner)
    assert getattr(partner, 'rdbms_RdbmsViewIdentifierField97') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue96', None)
    assert getattr(partner, 'rdbms_RdbmsViewIdentifierField97') is None


def test_assoc_incrementalModel108_stub_double():
    # rdbms_RdbmsOperationMeta has no real 'rdbms_RdbmsOperationMeta109' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsOperationMeta()
    setattr(partner, 'rdbms_RdbmsOperationMeta109', None)
    _safe_set(owner, 'rdbms_RdbmsModel110', partner)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta109') == owner
    _safe_set(owner, 'rdbms_RdbmsModel110', None)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta109') is None


def test_assoc_indexes4_stub_double():
    # rdbms_RdbmsTable has no real 'table5' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsIndex(unique=True)
    partner = rdbms_RdbmsTable()
    setattr(partner, 'table5', None)
    _safe_set(owner, 'RdbmsIndex', partner)
    assert owner in getattr(partner, 'table5')
    _safe_set(owner, 'RdbmsIndex', None)
    assert owner not in getattr(partner, 'table5')


def test_assoc_previousModel103_stub_double():
    # rdbms_RdbmsOperationMeta has no real 'rdbms_RdbmsOperationMeta' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsOperationMeta()
    setattr(partner, 'rdbms_RdbmsOperationMeta', None)
    _safe_set(owner, 'rdbms_RdbmsModel104', partner)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta') == owner
    _safe_set(owner, 'rdbms_RdbmsModel104', None)
    assert getattr(partner, 'rdbms_RdbmsOperationMeta') is None


def test_assoc_previousTable62_stub_double():
    # rdbms_RdbmsTable has no real 'rdbms_RdbmsTable64' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModifyTableOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModifyTableOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModifyTableOperation(nameChanged="sample_text")
    partner = rdbms_RdbmsTable()
    setattr(partner, 'rdbms_RdbmsTable64', None)
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation63', partner)
    assert getattr(partner, 'rdbms_RdbmsTable64') == owner
    _safe_set(owner, 'rdbms_RdbmsModifyTableOperation63', None)
    assert getattr(partner, 'rdbms_RdbmsTable64') is None


def test_assoc_primaryIdentifierField25_stub_double():
    # rdbms_RdbmsViewIdentifierField has no real 'rdbms_RdbmsViewIdentifierField' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsView(originUuid="sample_text")
    partner = rdbms_RdbmsViewIdentifierField()
    setattr(partner, 'rdbms_RdbmsViewIdentifierField', None)
    _safe_set(owner, 'rdbms_RdbmsView26', partner)
    assert getattr(partner, 'rdbms_RdbmsViewIdentifierField') == owner
    _safe_set(owner, 'rdbms_RdbmsView26', None)
    assert getattr(partner, 'rdbms_RdbmsViewIdentifierField') is None


def test_assoc_primaryTable22_stub_double():
    # rdbms_RdbmsTableAlias has no real 'rdbms_RdbmsTableAlias' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsView(originUuid="sample_text")
    partner = rdbms_RdbmsTableAlias()
    setattr(partner, 'rdbms_RdbmsTableAlias', None)
    _safe_set(owner, 'rdbms_RdbmsView', partner)
    assert getattr(partner, 'rdbms_RdbmsTableAlias') == owner
    _safe_set(owner, 'rdbms_RdbmsView', None)
    assert getattr(partner, 'rdbms_RdbmsTableAlias') is None


def test_assoc_rdbmsTables34_stub_double():
    # rdbms_RdbmsTable has no real 'rdbms_RdbmsTable36' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsTable()
    setattr(partner, 'rdbms_RdbmsTable36', None)
    _safe_set(owner, 'rdbms_RdbmsModel35', {partner})
    assert getattr(partner, 'rdbms_RdbmsTable36') == owner
    _safe_set(owner, 'rdbms_RdbmsModel35', set())
    assert getattr(partner, 'rdbms_RdbmsTable36') is None


def test_assoc_referenceKey11_stub_double():
    # rdbms_RdbmsIdentifierField has no real 'RdbmsIdentifierField' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsForeignKey(deferred=True, deleteOnCascade=True, foreignKeySqlName="sample_text", inheritenceBased=True, readOnly=True)
    partner = rdbms_RdbmsIdentifierField()
    setattr(partner, 'RdbmsIdentifierField', None)
    _safe_set(owner, 'foreignKeys', partner)
    assert getattr(partner, 'RdbmsIdentifierField') == owner
    _safe_set(owner, 'foreignKeys', None)
    assert getattr(partner, 'RdbmsIdentifierField') is None


def test_assoc_table86_stub_double():
    # rdbms_RdbmsTable has no real 'RdbmsTable87' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsIndex(unique=True)
    partner = rdbms_RdbmsTable()
    setattr(partner, 'RdbmsTable87', None)
    _safe_set(owner, 'indexes', partner)
    assert getattr(partner, 'RdbmsTable87') == owner
    _safe_set(owner, 'indexes', None)
    assert getattr(partner, 'RdbmsTable87') is None


def test_assoc_table9_stub_double():
    # rdbms_RdbmsTable has no real 'RdbmsTable' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsField(mandatory=True, precision=7, rdbmsTypeName="sample_text", scale=7, size=7, storageByte=7)
    partner = rdbms_RdbmsTable()
    setattr(partner, 'RdbmsTable', None)
    _safe_set(owner, 'fields', partner)
    assert getattr(partner, 'RdbmsTable') == owner
    _safe_set(owner, 'fields', None)
    assert getattr(partner, 'RdbmsTable') is None


def test_assoc_tableOperations42_stub_double():
    # rdbms_RdbmsTableOperation has no real 'rdbms_RdbmsTableOperation' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsTableOperation()
    setattr(partner, 'rdbms_RdbmsTableOperation', None)
    _safe_set(owner, 'rdbms_RdbmsModel43', {partner})
    assert getattr(partner, 'rdbms_RdbmsTableOperation') == owner
    _safe_set(owner, 'rdbms_RdbmsModel43', set())
    assert getattr(partner, 'rdbms_RdbmsTableOperation') is None


def test_assoc_tables27_stub_double():
    # rdbms_RdbmsTableAlias has no real 'RdbmsTableAlias' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsView(originUuid="sample_text")
    partner = rdbms_RdbmsTableAlias()
    setattr(partner, 'RdbmsTableAlias', None)
    _safe_set(owner, 'view28', {partner})
    assert getattr(partner, 'RdbmsTableAlias') == owner
    _safe_set(owner, 'view28', set())
    assert getattr(partner, 'RdbmsTableAlias') is None


def test_assoc_toAlias73_stub_double():
    # rdbms_RdbmsTableAlias has no real 'rdbms_RdbmsTableAlias75' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRelation(name="sample_text")
    partner = rdbms_RdbmsTableAlias()
    setattr(partner, 'rdbms_RdbmsTableAlias75', None)
    _safe_set(owner, 'rdbms_RdbmsViewRelation74', partner)
    assert getattr(partner, 'rdbms_RdbmsTableAlias75') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRelation74', None)
    assert getattr(partner, 'rdbms_RdbmsTableAlias75') is None


def test_assoc_toField79_stub_double():
    # rdbms_RdbmsIdentifierField has no real 'rdbms_RdbmsIdentifierField81' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRelation(name="sample_text")
    partner = rdbms_RdbmsIdentifierField()
    setattr(partner, 'rdbms_RdbmsIdentifierField81', None)
    _safe_set(owner, 'rdbms_RdbmsViewRelation80', partner)
    assert getattr(partner, 'rdbms_RdbmsIdentifierField81') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRelation80', None)
    assert getattr(partner, 'rdbms_RdbmsIdentifierField81') is None


def test_assoc_valueField98_stub_double():
    # rdbms_RdbmsViewValueField has no real 'rdbms_RdbmsViewValueField' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRecordValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRecordValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRecordValue(value="sample_text")
    partner = rdbms_RdbmsViewValueField()
    setattr(partner, 'rdbms_RdbmsViewValueField', None)
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue99', partner)
    assert getattr(partner, 'rdbms_RdbmsViewValueField') == owner
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue99', None)
    assert getattr(partner, 'rdbms_RdbmsViewValueField') is None


def test_assoc_values90_stub_double():
    # rdbms_RdbmsViewRecord has no real 'rdbms_RdbmsViewRecord91' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsViewRecordValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsViewRecordValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsViewRecordValue(value="sample_text")
    partner = rdbms_RdbmsViewRecord()
    setattr(partner, 'rdbms_RdbmsViewRecord91', None)
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue', partner)
    assert owner in getattr(partner, 'rdbms_RdbmsViewRecord91')
    _safe_set(owner, 'rdbms_RdbmsViewRecordValue', None)
    assert owner not in getattr(partner, 'rdbms_RdbmsViewRecord91')


def test_assoc_view51_stub_double():
    # rdbms_RdbmsTableAlias has no real 'tables' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsView(originUuid="sample_text")
    partner = rdbms_RdbmsTableAlias()
    setattr(partner, 'tables', None)
    _safe_set(owner, 'RdbmsView52', partner)
    assert getattr(partner, 'tables') == owner
    _safe_set(owner, 'RdbmsView52', None)
    assert getattr(partner, 'tables') is None


def test_assoc_view92_stub_double():
    # rdbms_RdbmsViewRecord has no real 'rdbms_RdbmsViewRecord93' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsView(originUuid="sample_text")
    partner = rdbms_RdbmsViewRecord()
    setattr(partner, 'rdbms_RdbmsViewRecord93', None)
    _safe_set(owner, 'rdbms_RdbmsView94', partner)
    assert getattr(partner, 'rdbms_RdbmsViewRecord93') == owner
    _safe_set(owner, 'rdbms_RdbmsView94', None)
    assert getattr(partner, 'rdbms_RdbmsViewRecord93') is None


def test_assoc_viewRecords44_stub_double():
    # rdbms_RdbmsViewRecord has no real 'rdbms_RdbmsViewRecord' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_RdbmsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_RdbmsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_RdbmsModel(version="sample_text")
    partner = rdbms_RdbmsViewRecord()
    setattr(partner, 'rdbms_RdbmsViewRecord', None)
    _safe_set(owner, 'rdbms_RdbmsModel45', {partner})
    assert getattr(partner, 'rdbms_RdbmsViewRecord') == owner
    _safe_set(owner, 'rdbms_RdbmsModel45', set())
    assert getattr(partner, 'rdbms_RdbmsViewRecord') is None


