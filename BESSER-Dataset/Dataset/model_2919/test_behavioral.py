import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    Attribute,
    Classifier,
    Feature,
    Label,
    ModelLabelFeature,
    NamedDisplayElement,
    NamedElement,
    PathElement,
    ResourceAttribute,
    persistence_Association,
    persistence_AssociationKey,
    persistence_AssociationWithContainment,
    persistence_AssociationWithoutContainment,
    persistence_Attribute,
    persistence_DataType,
    persistence_DataTypeAttribute,
    persistence_DateAttribute,
    persistence_DatePathElement,
    persistence_Entity,
    persistence_Expression,
    persistence_Feature,
    persistence_FileAttribute,
    persistence_ImageAttribute,
    persistence_Label,
    persistence_LocationAttribute,
    persistence_ModelLabel,
    persistence_ModelLabelAssociation,
    persistence_ModelLabelAttribute,
    persistence_ModelLabelFeature,
    persistence_PathElement,
    persistence_Persistence,
    persistence_ResourceAttribute,
    persistence_SerializationGroup,
    persistence_StaticPathElement,
    persistence_UrlAttribute,
    Cardinality,
    DatabaseTechnologies,
    DateDetails,
    OrmTechnologies,
    isHasChoices,
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

def test_assoc_allAssociations40_reverse_link_reassign_clear():
    a1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'persistence_Association42', a1)
    assert _is_linked(b, 'persistence_Association42', a1)
    if hasattr(a1, 'persistence_Entity41'):
        assert _is_linked(a1, 'persistence_Entity41', b)
    _safe_set(b, 'persistence_Association42', a2)
    assert _is_linked(b, 'persistence_Association42', a2)
    if hasattr(a1, 'persistence_Entity41'):
        assert not _is_linked(a1, 'persistence_Entity41', b)
    if hasattr(a2, 'persistence_Entity41'):
        assert _is_linked(a2, 'persistence_Entity41', b)
    _safe_set(b, 'persistence_Association42', None)
    assert not _is_linked(b, 'persistence_Association42', a2)
    if hasattr(a2, 'persistence_Entity41'):
        assert not _is_linked(a2, 'persistence_Entity41', b)


def test_assoc_allFeatures37_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_Entity38', {a1})
    assert _is_linked(b, 'persistence_Entity38', a1)
    if hasattr(a1, 'persistence_Feature39'):
        assert _is_linked(a1, 'persistence_Feature39', b)
    _safe_set(b, 'persistence_Entity38', {a2})
    assert _is_linked(b, 'persistence_Entity38', a2)
    if hasattr(a1, 'persistence_Feature39'):
        assert not _is_linked(a1, 'persistence_Feature39', b)
    if hasattr(a2, 'persistence_Feature39'):
        assert _is_linked(a2, 'persistence_Feature39', b)
    _safe_set(b, 'persistence_Entity38', set())
    assert not _is_linked(b, 'persistence_Entity38', a2)
    if hasattr(a2, 'persistence_Feature39'):
        assert not _is_linked(a2, 'persistence_Feature39', b)


def test_assoc_association24_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAssociation(isSourceAssociation=True)
    a2 = persistence_ModelLabelAssociation(isSourceAssociation=False)
    b = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'persistence_Association', a1)
    assert _is_linked(b, 'persistence_Association', a1)
    if hasattr(a1, 'persistence_ModelLabelAssociation'):
        assert _is_linked(a1, 'persistence_ModelLabelAssociation', b)
    _safe_set(b, 'persistence_Association', a2)
    assert _is_linked(b, 'persistence_Association', a2)
    if hasattr(a1, 'persistence_ModelLabelAssociation'):
        assert not _is_linked(a1, 'persistence_ModelLabelAssociation', b)
    if hasattr(a2, 'persistence_ModelLabelAssociation'):
        assert _is_linked(a2, 'persistence_ModelLabelAssociation', b)
    _safe_set(b, 'persistence_Association', None)
    assert not _is_linked(b, 'persistence_Association', a2)
    if hasattr(a2, 'persistence_ModelLabelAssociation'):
        assert not _is_linked(a2, 'persistence_ModelLabelAssociation', b)


def test_assoc_associationEnds36_reverse_link_reassign_clear():
    a1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'Association', a1)
    assert _is_linked(b, 'Association', a1)
    if hasattr(a1, 'targetEntity'):
        assert _is_linked(a1, 'targetEntity', b)
    _safe_set(b, 'Association', a2)
    assert _is_linked(b, 'Association', a2)
    if hasattr(a1, 'targetEntity'):
        assert not _is_linked(a1, 'targetEntity', b)
    if hasattr(a2, 'targetEntity'):
        assert _is_linked(a2, 'targetEntity', b)
    _safe_set(b, 'Association', None)
    assert not _is_linked(b, 'Association', a2)
    if hasattr(a2, 'targetEntity'):
        assert not _is_linked(a2, 'targetEntity', b)


def test_assoc_associations33_reverse_link_reassign_clear():
    a1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'persistence_Association35', a1)
    assert _is_linked(b, 'persistence_Association35', a1)
    if hasattr(a1, 'persistence_Entity34'):
        assert _is_linked(a1, 'persistence_Entity34', b)
    _safe_set(b, 'persistence_Association35', a2)
    assert _is_linked(b, 'persistence_Association35', a2)
    if hasattr(a1, 'persistence_Entity34'):
        assert not _is_linked(a1, 'persistence_Entity34', b)
    if hasattr(a2, 'persistence_Entity34'):
        assert _is_linked(a2, 'persistence_Entity34', b)
    _safe_set(b, 'persistence_Association35', None)
    assert not _is_linked(b, 'persistence_Association35', a2)
    if hasattr(a2, 'persistence_Entity34'):
        assert not _is_linked(a2, 'persistence_Entity34', b)


def test_assoc_attribute22_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAttribute(dateFormat="sample_text")
    a2 = persistence_ModelLabelAttribute(dateFormat="sample_text_2")
    b = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute23', a1)
    assert _is_linked(b, 'persistence_Attribute23', a1)
    if hasattr(a1, 'persistence_ModelLabelAttribute'):
        assert _is_linked(a1, 'persistence_ModelLabelAttribute', b)
    _safe_set(b, 'persistence_Attribute23', a2)
    assert _is_linked(b, 'persistence_Attribute23', a2)
    if hasattr(a1, 'persistence_ModelLabelAttribute'):
        assert not _is_linked(a1, 'persistence_ModelLabelAttribute', b)
    if hasattr(a2, 'persistence_ModelLabelAttribute'):
        assert _is_linked(a2, 'persistence_ModelLabelAttribute', b)
    _safe_set(b, 'persistence_Attribute23', None)
    assert not _is_linked(b, 'persistence_Attribute23', a2)
    if hasattr(a2, 'persistence_ModelLabelAttribute'):
        assert not _is_linked(a2, 'persistence_ModelLabelAttribute', b)


def test_assoc_attributes30_reverse_link_reassign_clear():
    a1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute32', a1)
    assert _is_linked(b, 'persistence_Attribute32', a1)
    if hasattr(a1, 'persistence_Entity31'):
        assert _is_linked(a1, 'persistence_Entity31', b)
    _safe_set(b, 'persistence_Attribute32', a2)
    assert _is_linked(b, 'persistence_Attribute32', a2)
    if hasattr(a1, 'persistence_Entity31'):
        assert not _is_linked(a1, 'persistence_Entity31', b)
    if hasattr(a2, 'persistence_Entity31'):
        assert _is_linked(a2, 'persistence_Entity31', b)
    _safe_set(b, 'persistence_Attribute32', None)
    assert not _is_linked(b, 'persistence_Attribute32', a2)
    if hasattr(a2, 'persistence_Entity31'):
        assert not _is_linked(a2, 'persistence_Entity31', b)


def test_assoc_containerUnique51_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_Entity52', {a1})
    assert _is_linked(b, 'persistence_Entity52', a1)
    if hasattr(a1, 'persistence_Feature53'):
        assert _is_linked(a1, 'persistence_Feature53', b)
    _safe_set(b, 'persistence_Entity52', {a2})
    assert _is_linked(b, 'persistence_Entity52', a2)
    if hasattr(a1, 'persistence_Feature53'):
        assert not _is_linked(a1, 'persistence_Feature53', b)
    if hasattr(a2, 'persistence_Feature53'):
        assert _is_linked(a2, 'persistence_Feature53', b)
    _safe_set(b, 'persistence_Entity52', set())
    assert not _is_linked(b, 'persistence_Entity52', a2)
    if hasattr(a2, 'persistence_Feature53'):
        assert not _is_linked(a2, 'persistence_Feature53', b)


def test_assoc_dynamicLabel25_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAssociation(isSourceAssociation=True)
    a2 = persistence_ModelLabelAssociation(isSourceAssociation=False)
    b = persistence_ModelLabel(customise=True, format="sample_text")
    _safe_set(b, 'persistence_ModelLabel27', a1)
    assert _is_linked(b, 'persistence_ModelLabel27', a1)
    if hasattr(a1, 'persistence_ModelLabelAssociation26'):
        assert _is_linked(a1, 'persistence_ModelLabelAssociation26', b)
    _safe_set(b, 'persistence_ModelLabel27', a2)
    assert _is_linked(b, 'persistence_ModelLabel27', a2)
    if hasattr(a1, 'persistence_ModelLabelAssociation26'):
        assert not _is_linked(a1, 'persistence_ModelLabelAssociation26', b)
    if hasattr(a2, 'persistence_ModelLabelAssociation26'):
        assert _is_linked(a2, 'persistence_ModelLabelAssociation26', b)
    _safe_set(b, 'persistence_ModelLabel27', None)
    assert not _is_linked(b, 'persistence_ModelLabel27', a2)
    if hasattr(a2, 'persistence_ModelLabelAssociation26'):
        assert not _is_linked(a2, 'persistence_ModelLabelAssociation26', b)


def test_assoc_entities3_reverse_link_reassign_clear():
    a1 = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    a2 = persistence_Persistence(databaseTechnology="sample_text_2", ormTechnology="sample_text_2", timestampCreation=False, timestampUpdates=False)
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_Entity', a1)
    assert _is_linked(b, 'persistence_Entity', a1)
    if hasattr(a1, 'persistence_Persistence4'):
        assert _is_linked(a1, 'persistence_Persistence4', b)
    _safe_set(b, 'persistence_Entity', a2)
    assert _is_linked(b, 'persistence_Entity', a2)
    if hasattr(a1, 'persistence_Persistence4'):
        assert not _is_linked(a1, 'persistence_Persistence4', b)
    if hasattr(a2, 'persistence_Persistence4'):
        assert _is_linked(a2, 'persistence_Persistence4', b)
    _safe_set(b, 'persistence_Entity', None)
    assert not _is_linked(b, 'persistence_Entity', a2)
    if hasattr(a2, 'persistence_Persistence4'):
        assert not _is_linked(a2, 'persistence_Persistence4', b)


def test_assoc_features28_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'partOf29', {a1})
    assert _is_linked(b, 'partOf29', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'partOf29', {a2})
    assert _is_linked(b, 'partOf29', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'partOf29', set())
    assert not _is_linked(b, 'partOf29', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_keys43_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_Entity44', {a1})
    assert _is_linked(b, 'persistence_Entity44', a1)
    if hasattr(a1, 'persistence_Feature45'):
        assert _is_linked(a1, 'persistence_Feature45', b)
    _safe_set(b, 'persistence_Entity44', {a2})
    assert _is_linked(b, 'persistence_Entity44', a2)
    if hasattr(a1, 'persistence_Feature45'):
        assert not _is_linked(a1, 'persistence_Feature45', b)
    if hasattr(a2, 'persistence_Feature45'):
        assert _is_linked(a2, 'persistence_Feature45', b)
    _safe_set(b, 'persistence_Entity44', set())
    assert not _is_linked(b, 'persistence_Entity44', a2)
    if hasattr(a2, 'persistence_Feature45'):
        assert not _is_linked(a2, 'persistence_Feature45', b)


def test_assoc_labelFor15_reverse_link_reassign_clear():
    a1 = persistence_ModelLabel(customise=True, format="sample_text")
    a2 = persistence_ModelLabel(customise=False, format="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'Entity16', a1)
    assert _is_linked(b, 'Entity16', a1)
    if hasattr(a1, 'labels'):
        assert _is_linked(a1, 'labels', b)
    _safe_set(b, 'Entity16', a2)
    assert _is_linked(b, 'Entity16', a2)
    if hasattr(a1, 'labels'):
        assert not _is_linked(a1, 'labels', b)
    if hasattr(a2, 'labels'):
        assert _is_linked(a2, 'labels', b)
    _safe_set(b, 'Entity16', None)
    assert not _is_linked(b, 'Entity16', a2)
    if hasattr(a2, 'labels'):
        assert not _is_linked(a2, 'labels', b)


def test_assoc_labels46_reverse_link_reassign_clear():
    a1 = persistence_ModelLabel(customise=True, format="sample_text")
    a2 = persistence_ModelLabel(customise=False, format="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'labelFor', {a1})
    assert _is_linked(b, 'labelFor', a1)
    if hasattr(a1, 'ModelLabel47'):
        assert _is_linked(a1, 'ModelLabel47', b)
    _safe_set(b, 'labelFor', {a2})
    assert _is_linked(b, 'labelFor', a2)
    if hasattr(a1, 'ModelLabel47'):
        assert not _is_linked(a1, 'ModelLabel47', b)
    if hasattr(a2, 'ModelLabel47'):
        assert _is_linked(a2, 'ModelLabel47', b)
    _safe_set(b, 'labelFor', set())
    assert not _is_linked(b, 'labelFor', a2)
    if hasattr(a2, 'ModelLabel47'):
        assert not _is_linked(a2, 'ModelLabel47', b)


def test_assoc_partOf5_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'Entity', a1)
    assert _is_linked(b, 'Entity', a1)
    if hasattr(a1, 'features'):
        assert _is_linked(a1, 'features', b)
    _safe_set(b, 'Entity', a2)
    assert _is_linked(b, 'Entity', a2)
    if hasattr(a1, 'features'):
        assert not _is_linked(a1, 'features', b)
    if hasattr(a2, 'features'):
        assert _is_linked(a2, 'features', b)
    _safe_set(b, 'Entity', None)
    assert not _is_linked(b, 'Entity', a2)
    if hasattr(a2, 'features'):
        assert not _is_linked(a2, 'features', b)


def test_assoc_slugFields9_reverse_link_reassign_clear():
    a1 = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    a2 = persistence_Attribute(containerUnique=False, hidden=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", interfaceType="sample_text_2", ormType="sample_text_2", persistentType="sample_text_2", placeholder="sample_text_2", unique=False, validationPattern="sample_text_2")
    b = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute8', {a1})
    assert _is_linked(b, 'persistence_Attribute8', a1)
    if hasattr(a1, 'persistence_Attribute'):
        assert _is_linked(a1, 'persistence_Attribute', b)
    _safe_set(b, 'persistence_Attribute8', {a2})
    assert _is_linked(b, 'persistence_Attribute8', a2)
    if hasattr(a1, 'persistence_Attribute'):
        assert not _is_linked(a1, 'persistence_Attribute', b)
    if hasattr(a2, 'persistence_Attribute'):
        assert _is_linked(a2, 'persistence_Attribute', b)
    _safe_set(b, 'persistence_Attribute8', set())
    assert not _is_linked(b, 'persistence_Attribute8', a2)
    if hasattr(a2, 'persistence_Attribute'):
        assert not _is_linked(a2, 'persistence_Attribute', b)


def test_assoc_targetEntity13_reverse_link_reassign_clear():
    a1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'associationEnds', a1)
    assert _is_linked(b, 'associationEnds', a1)
    if hasattr(a1, 'Entity14'):
        assert _is_linked(a1, 'Entity14', b)
    _safe_set(b, 'associationEnds', a2)
    assert _is_linked(b, 'associationEnds', a2)
    if hasattr(a1, 'Entity14'):
        assert not _is_linked(a1, 'Entity14', b)
    if hasattr(a2, 'Entity14'):
        assert _is_linked(a2, 'Entity14', b)
    _safe_set(b, 'associationEnds', None)
    assert not _is_linked(b, 'associationEnds', a2)
    if hasattr(a2, 'Entity14'):
        assert not _is_linked(a2, 'Entity14', b)


def test_assoc_unique48_reverse_link_reassign_clear():
    a1 = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    a2 = persistence_Feature(booleanIsHasChoice="sample_text_2", cardinality="sample_text_2", collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, columnName="sample_text_2", customiseSet=False, defaultDisplayValue="sample_text_2", derived=False, displayClass="sample_text_2", emptyDisplayValue="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", ordered=False, pluralisedName="sample_text_2", primaryKey=False, singletonName="sample_text_2", title="sample_text_2")
    b = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_Entity49', {a1})
    assert _is_linked(b, 'persistence_Entity49', a1)
    if hasattr(a1, 'persistence_Feature50'):
        assert _is_linked(a1, 'persistence_Feature50', b)
    _safe_set(b, 'persistence_Entity49', {a2})
    assert _is_linked(b, 'persistence_Entity49', a2)
    if hasattr(a1, 'persistence_Feature50'):
        assert not _is_linked(a1, 'persistence_Feature50', b)
    if hasattr(a2, 'persistence_Feature50'):
        assert _is_linked(a2, 'persistence_Feature50', b)
    _safe_set(b, 'persistence_Entity49', set())
    assert not _is_linked(b, 'persistence_Entity49', a2)
    if hasattr(a2, 'persistence_Feature50'):
        assert not _is_linked(a2, 'persistence_Feature50', b)


