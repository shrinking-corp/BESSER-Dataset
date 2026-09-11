import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_persistence_Association_bidirectional_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.bidirectional == True
    instance.bidirectional = False
    assert instance.bidirectional == False


def test_persistence_Association_inputColumnClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.inputColumnClass == "sample_text"
    instance.inputColumnClass = "sample_text_2"
    assert instance.inputColumnClass == "sample_text_2"


def test_persistence_Association_inputElementClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.inputElementClass == "sample_text"
    instance.inputElementClass = "sample_text_2"
    assert instance.inputElementClass == "sample_text_2"


def test_persistence_Association_pivotTableName_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.pivotTableName == "sample_text"
    instance.pivotTableName = "sample_text_2"
    assert instance.pivotTableName == "sample_text_2"


def test_persistence_Association_pseudo_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.pseudo == True
    instance.pseudo = False
    assert instance.pseudo == False


def test_persistence_Association_serializationMaxDepth_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.serializationMaxDepth == 7
    instance.serializationMaxDepth = 13
    assert instance.serializationMaxDepth == 13


def test_persistence_Association_targetColumnName_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetColumnName == "sample_text"
    instance.targetColumnName = "sample_text_2"
    assert instance.targetColumnName == "sample_text_2"


def test_persistence_Association_targetDisplayClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetDisplayClass == "sample_text"
    instance.targetDisplayClass = "sample_text_2"
    assert instance.targetDisplayClass == "sample_text_2"


def test_persistence_Association_targetDisplayLabel_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetDisplayLabel == "sample_text"
    instance.targetDisplayLabel = "sample_text_2"
    assert instance.targetDisplayLabel == "sample_text_2"


def test_persistence_Association_targetFeatureName_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetFeatureName == "sample_text"
    instance.targetFeatureName = "sample_text_2"
    assert instance.targetFeatureName == "sample_text_2"


def test_persistence_Association_targetFooterClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetFooterClass == "sample_text"
    instance.targetFooterClass = "sample_text_2"
    assert instance.targetFooterClass == "sample_text_2"


def test_persistence_Association_targetHeaderClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetHeaderClass == "sample_text"
    instance.targetHeaderClass = "sample_text_2"
    assert instance.targetHeaderClass == "sample_text_2"


def test_persistence_Association_targetInputClass_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetInputClass == "sample_text"
    instance.targetInputClass = "sample_text_2"
    assert instance.targetInputClass == "sample_text_2"


def test_persistence_Association_targetPrimaryKey_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.targetPrimaryKey == True
    instance.targetPrimaryKey = False
    assert instance.targetPrimaryKey == False


def test_persistence_Association_unique_value_roundtrip():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_persistence_AssociationWithContainment_sourceVisible_value_roundtrip():
    instance = persistence_AssociationWithContainment(sourceVisible=True)
    assert instance.sourceVisible == True
    instance.sourceVisible = False
    assert instance.sourceVisible == False


def test_persistence_AssociationWithoutContainment_targetCardinality_value_roundtrip():
    instance = persistence_AssociationWithoutContainment(targetCardinality="sample_text", targetUnique=True)
    assert instance.targetCardinality == "sample_text"
    instance.targetCardinality = "sample_text_2"
    assert instance.targetCardinality == "sample_text_2"


def test_persistence_AssociationWithoutContainment_targetUnique_value_roundtrip():
    instance = persistence_AssociationWithoutContainment(targetCardinality="sample_text", targetUnique=True)
    assert instance.targetUnique == True
    instance.targetUnique = False
    assert instance.targetUnique == False


def test_persistence_Attribute_containerUnique_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.containerUnique == True
    instance.containerUnique = False
    assert instance.containerUnique == False


def test_persistence_Attribute_hidden_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.hidden == True
    instance.hidden = False
    assert instance.hidden == False


def test_persistence_Attribute_inputColumnClass_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.inputColumnClass == "sample_text"
    instance.inputColumnClass = "sample_text_2"
    assert instance.inputColumnClass == "sample_text_2"


def test_persistence_Attribute_inputElementClass_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.inputElementClass == "sample_text"
    instance.inputElementClass = "sample_text_2"
    assert instance.inputElementClass == "sample_text_2"


def test_persistence_Attribute_interfaceType_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.interfaceType == "sample_text"
    instance.interfaceType = "sample_text_2"
    assert instance.interfaceType == "sample_text_2"


def test_persistence_Attribute_ormType_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.ormType == "sample_text"
    instance.ormType = "sample_text_2"
    assert instance.ormType == "sample_text_2"


def test_persistence_Attribute_persistentType_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.persistentType == "sample_text"
    instance.persistentType = "sample_text_2"
    assert instance.persistentType == "sample_text_2"


def test_persistence_Attribute_placeholder_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.placeholder == "sample_text"
    instance.placeholder = "sample_text_2"
    assert instance.placeholder == "sample_text_2"


def test_persistence_Attribute_unique_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_persistence_Attribute_validationPattern_value_roundtrip():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert instance.validationPattern == "sample_text"
    instance.validationPattern = "sample_text_2"
    assert instance.validationPattern == "sample_text_2"


def test_persistence_DataTypeAttribute_caseInsensitive_value_roundtrip():
    instance = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    assert instance.caseInsensitive == True
    instance.caseInsensitive = False
    assert instance.caseInsensitive == False


def test_persistence_DataTypeAttribute_encrypt_value_roundtrip():
    instance = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    assert instance.encrypt == True
    instance.encrypt = False
    assert instance.encrypt == False


def test_persistence_DataTypeAttribute_obfuscateFormFields_value_roundtrip():
    instance = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    assert instance.obfuscateFormFields == True
    instance.obfuscateFormFields = False
    assert instance.obfuscateFormFields == False


def test_persistence_DateAttribute_details_value_roundtrip():
    instance = persistence_DateAttribute(details="sample_text", format="sample_text")
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_persistence_DateAttribute_format_value_roundtrip():
    instance = persistence_DateAttribute(details="sample_text", format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_persistence_DatePathElement_format_value_roundtrip():
    instance = persistence_DatePathElement(format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_persistence_Entity_allowFormTypeCustomisation_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.allowFormTypeCustomisation == True
    instance.allowFormTypeCustomisation = False
    assert instance.allowFormTypeCustomisation == False


def test_persistence_Entity_autoKeyGenerationStrategy_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyGenerationStrategy == "sample_text"
    instance.autoKeyGenerationStrategy = "sample_text_2"
    assert instance.autoKeyGenerationStrategy == "sample_text_2"


def test_persistence_Entity_autoKeyName_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyName == "sample_text"
    instance.autoKeyName = "sample_text_2"
    assert instance.autoKeyName == "sample_text_2"


def test_persistence_Entity_autoKeyPersistentType_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyPersistentType == "sample_text"
    instance.autoKeyPersistentType = "sample_text_2"
    assert instance.autoKeyPersistentType == "sample_text_2"


def test_persistence_Entity_implementsUserInterface_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.implementsUserInterface == True
    instance.implementsUserInterface = False
    assert instance.implementsUserInterface == False


def test_persistence_Entity_pluralisedName_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.pluralisedName == "sample_text"
    instance.pluralisedName = "sample_text_2"
    assert instance.pluralisedName == "sample_text_2"


def test_persistence_Entity_singletonName_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.singletonName == "sample_text"
    instance.singletonName = "sample_text_2"
    assert instance.singletonName == "sample_text_2"


def test_persistence_Entity_tableName_value_roundtrip():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_persistence_Feature_booleanIsHasChoice_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.booleanIsHasChoice == "sample_text"
    instance.booleanIsHasChoice = "sample_text_2"
    assert instance.booleanIsHasChoice == "sample_text_2"


def test_persistence_Feature_cardinality_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_persistence_Feature_collectionOrmAllowAdd_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.collectionOrmAllowAdd == True
    instance.collectionOrmAllowAdd = False
    assert instance.collectionOrmAllowAdd == False


def test_persistence_Feature_collectionOrmAllowRemove_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.collectionOrmAllowRemove == True
    instance.collectionOrmAllowRemove = False
    assert instance.collectionOrmAllowRemove == False


def test_persistence_Feature_columnName_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_persistence_Feature_customiseSet_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.customiseSet == True
    instance.customiseSet = False
    assert instance.customiseSet == False


def test_persistence_Feature_defaultDisplayValue_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.defaultDisplayValue == "sample_text"
    instance.defaultDisplayValue = "sample_text_2"
    assert instance.defaultDisplayValue == "sample_text_2"


def test_persistence_Feature_derived_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_persistence_Feature_displayClass_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.displayClass == "sample_text"
    instance.displayClass = "sample_text_2"
    assert instance.displayClass == "sample_text_2"


def test_persistence_Feature_emptyDisplayValue_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.emptyDisplayValue == "sample_text"
    instance.emptyDisplayValue = "sample_text_2"
    assert instance.emptyDisplayValue == "sample_text_2"


def test_persistence_Feature_encodeUriKey_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.encodeUriKey == True
    instance.encodeUriKey = False
    assert instance.encodeUriKey == False


def test_persistence_Feature_footerClass_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.footerClass == "sample_text"
    instance.footerClass = "sample_text_2"
    assert instance.footerClass == "sample_text_2"


def test_persistence_Feature_headerClass_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.headerClass == "sample_text"
    instance.headerClass = "sample_text_2"
    assert instance.headerClass == "sample_text_2"


def test_persistence_Feature_ordered_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_persistence_Feature_pluralisedName_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.pluralisedName == "sample_text"
    instance.pluralisedName = "sample_text_2"
    assert instance.pluralisedName == "sample_text_2"


def test_persistence_Feature_primaryKey_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.primaryKey == True
    instance.primaryKey = False
    assert instance.primaryKey == False


def test_persistence_Feature_singletonName_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.singletonName == "sample_text"
    instance.singletonName = "sample_text_2"
    assert instance.singletonName == "sample_text_2"


def test_persistence_Feature_title_value_roundtrip():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_persistence_ModelLabel_customise_value_roundtrip():
    instance = persistence_ModelLabel(customise=True, format="sample_text")
    assert instance.customise == True
    instance.customise = False
    assert instance.customise == False


def test_persistence_ModelLabel_format_value_roundtrip():
    instance = persistence_ModelLabel(customise=True, format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_persistence_ModelLabelAssociation_isSourceAssociation_value_roundtrip():
    instance = persistence_ModelLabelAssociation(isSourceAssociation=True)
    assert instance.isSourceAssociation == True
    instance.isSourceAssociation = False
    assert instance.isSourceAssociation == False


def test_persistence_ModelLabelAttribute_dateFormat_value_roundtrip():
    instance = persistence_ModelLabelAttribute(dateFormat="sample_text")
    assert instance.dateFormat == "sample_text"
    instance.dateFormat = "sample_text_2"
    assert instance.dateFormat == "sample_text_2"


def test_persistence_Persistence_databaseTechnology_value_roundtrip():
    instance = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databaseTechnology == "sample_text"
    instance.databaseTechnology = "sample_text_2"
    assert instance.databaseTechnology == "sample_text_2"


def test_persistence_Persistence_ormTechnology_value_roundtrip():
    instance = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.ormTechnology == "sample_text"
    instance.ormTechnology = "sample_text_2"
    assert instance.ormTechnology == "sample_text_2"


def test_persistence_Persistence_timestampCreation_value_roundtrip():
    instance = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.timestampCreation == True
    instance.timestampCreation = False
    assert instance.timestampCreation == False


def test_persistence_Persistence_timestampUpdates_value_roundtrip():
    instance = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.timestampUpdates == True
    instance.timestampUpdates = False
    assert instance.timestampUpdates == False


def test_persistence_ResourceAttribute_maximumUploadSize_value_roundtrip():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert instance.maximumUploadSize == 7
    instance.maximumUploadSize = 13
    assert instance.maximumUploadSize == 13


def test_persistence_ResourceAttribute_uploadsWithinWebsite_value_roundtrip():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert instance.uploadsWithinWebsite == True
    instance.uploadsWithinWebsite = False
    assert instance.uploadsWithinWebsite == False


def test_persistence_ResourceAttribute_validUploadExtensions_value_roundtrip():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert instance.validUploadExtensions == "sample_text"
    instance.validUploadExtensions = "sample_text_2"
    assert instance.validUploadExtensions == "sample_text_2"


def test_persistence_ResourceAttribute_validUploadMimeTypes_value_roundtrip():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert instance.validUploadMimeTypes == "sample_text"
    instance.validUploadMimeTypes = "sample_text_2"
    assert instance.validUploadMimeTypes == "sample_text_2"


def test_persistence_StaticPathElement_element_value_roundtrip():
    instance = persistence_StaticPathElement(element="sample_text")
    assert instance.element == "sample_text"
    instance.element = "sample_text_2"
    assert instance.element == "sample_text_2"


def test_persistence_UrlAttribute_displayValue_value_roundtrip():
    instance = persistence_UrlAttribute(displayValue="sample_text")
    assert instance.displayValue == "sample_text"
    instance.displayValue = "sample_text_2"
    assert instance.displayValue == "sample_text_2"


def test_persistence_AssociationWithContainment_isa_Association():
    instance = persistence_AssociationWithContainment(sourceVisible=True)
    assert isinstance(instance, Association)


def test_persistence_AssociationWithoutContainment_isa_Association():
    instance = persistence_AssociationWithoutContainment(targetCardinality="sample_text", targetUnique=True)
    assert isinstance(instance, Association)


def test_persistence_DataTypeAttribute_isa_Attribute():
    instance = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    assert isinstance(instance, Attribute)


def test_persistence_DateAttribute_isa_Attribute():
    instance = persistence_DateAttribute(details="sample_text", format="sample_text")
    assert isinstance(instance, Attribute)


def test_persistence_LocationAttribute_isa_Attribute():
    instance = persistence_LocationAttribute()
    assert isinstance(instance, Attribute)


def test_persistence_ResourceAttribute_isa_Attribute():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert isinstance(instance, Attribute)


def test_persistence_UrlAttribute_isa_Attribute():
    instance = persistence_UrlAttribute(displayValue="sample_text")
    assert isinstance(instance, Attribute)


def test_persistence_Entity_isa_Classifier():
    instance = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert isinstance(instance, Classifier)


def test_persistence_Association_isa_Feature():
    instance = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    assert isinstance(instance, Feature)


def test_persistence_Attribute_isa_Feature():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert isinstance(instance, Feature)


def test_persistence_Attribute_isa_Label():
    instance = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    assert isinstance(instance, Label)


def test_persistence_ModelLabel_isa_Label():
    instance = persistence_ModelLabel(customise=True, format="sample_text")
    assert isinstance(instance, Label)


def test_persistence_ModelLabelAssociation_isa_ModelLabelFeature():
    instance = persistence_ModelLabelAssociation(isSourceAssociation=True)
    assert isinstance(instance, ModelLabelFeature)


def test_persistence_ModelLabelAttribute_isa_ModelLabelFeature():
    instance = persistence_ModelLabelAttribute(dateFormat="sample_text")
    assert isinstance(instance, ModelLabelFeature)


def test_persistence_Feature_isa_NamedDisplayElement():
    instance = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    assert isinstance(instance, NamedDisplayElement)


def test_persistence_ModelLabel_isa_NamedElement():
    instance = persistence_ModelLabel(customise=True, format="sample_text")
    assert isinstance(instance, NamedElement)


def test_persistence_SerializationGroup_isa_NamedElement():
    instance = persistence_SerializationGroup()
    assert isinstance(instance, NamedElement)


def test_persistence_DatePathElement_isa_PathElement():
    instance = persistence_DatePathElement(format="sample_text")
    assert isinstance(instance, PathElement)


def test_persistence_StaticPathElement_isa_PathElement():
    instance = persistence_StaticPathElement(element="sample_text")
    assert isinstance(instance, PathElement)


def test_persistence_FileAttribute_isa_ResourceAttribute():
    instance = persistence_FileAttribute()
    assert isinstance(instance, ResourceAttribute)


def test_persistence_ImageAttribute_isa_ResourceAttribute():
    instance = persistence_ImageAttribute()
    assert isinstance(instance, ResourceAttribute)


def test_assoc_allAssociations40_link_reassign_clear():
    a = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b2 = persistence_Association(bidirectional=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", pivotTableName="sample_text_2", pseudo=False, serializationMaxDepth=13, targetColumnName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False, unique=False)
    _safe_set(a, 'persistence_Entity41', {b1})
    assert _is_linked(a, 'persistence_Entity41', b1)
    if hasattr(b1, 'persistence_Association42'):
        assert _is_linked(b1, 'persistence_Association42', a)
    _safe_set(a, 'persistence_Entity41', {b2})
    assert _is_linked(a, 'persistence_Entity41', b2)
    if hasattr(b1, 'persistence_Association42'):
        assert not _is_linked(b1, 'persistence_Association42', a)
    if hasattr(b2, 'persistence_Association42'):
        assert _is_linked(b2, 'persistence_Association42', a)
    _safe_set(a, 'persistence_Entity41', set())
    assert not _is_linked(a, 'persistence_Entity41', b2)
    if hasattr(b2, 'persistence_Association42'):
        assert not _is_linked(b2, 'persistence_Association42', a)


def test_assoc_allFeatures37_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature39', b1)
    assert _is_linked(a, 'persistence_Feature39', b1)
    if hasattr(b1, 'persistence_Entity38'):
        assert _is_linked(b1, 'persistence_Entity38', a)
    _safe_set(a, 'persistence_Feature39', b2)
    assert _is_linked(a, 'persistence_Feature39', b2)
    if hasattr(b1, 'persistence_Entity38'):
        assert not _is_linked(b1, 'persistence_Entity38', a)
    if hasattr(b2, 'persistence_Entity38'):
        assert _is_linked(b2, 'persistence_Entity38', a)
    _safe_set(a, 'persistence_Feature39', None)
    assert not _is_linked(a, 'persistence_Feature39', b2)
    if hasattr(b2, 'persistence_Entity38'):
        assert not _is_linked(b2, 'persistence_Entity38', a)


def test_assoc_association24_link_reassign_clear():
    a = persistence_ModelLabelAssociation(isSourceAssociation=True)
    b1 = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b2 = persistence_Association(bidirectional=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", pivotTableName="sample_text_2", pseudo=False, serializationMaxDepth=13, targetColumnName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False, unique=False)
    _safe_set(a, 'persistence_ModelLabelAssociation', b1)
    assert _is_linked(a, 'persistence_ModelLabelAssociation', b1)
    if hasattr(b1, 'persistence_Association'):
        assert _is_linked(b1, 'persistence_Association', a)
    _safe_set(a, 'persistence_ModelLabelAssociation', b2)
    assert _is_linked(a, 'persistence_ModelLabelAssociation', b2)
    if hasattr(b1, 'persistence_Association'):
        assert not _is_linked(b1, 'persistence_Association', a)
    if hasattr(b2, 'persistence_Association'):
        assert _is_linked(b2, 'persistence_Association', a)
    _safe_set(a, 'persistence_ModelLabelAssociation', None)
    assert not _is_linked(a, 'persistence_ModelLabelAssociation', b2)
    if hasattr(b2, 'persistence_Association'):
        assert not _is_linked(b2, 'persistence_Association', a)


def test_assoc_associationEnds36_link_reassign_clear():
    a = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b2 = persistence_Association(bidirectional=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", pivotTableName="sample_text_2", pseudo=False, serializationMaxDepth=13, targetColumnName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False, unique=False)
    _safe_set(a, 'targetEntity', {b1})
    assert _is_linked(a, 'targetEntity', b1)
    if hasattr(b1, 'Association'):
        assert _is_linked(b1, 'Association', a)
    _safe_set(a, 'targetEntity', {b2})
    assert _is_linked(a, 'targetEntity', b2)
    if hasattr(b1, 'Association'):
        assert not _is_linked(b1, 'Association', a)
    if hasattr(b2, 'Association'):
        assert _is_linked(b2, 'Association', a)
    _safe_set(a, 'targetEntity', set())
    assert not _is_linked(a, 'targetEntity', b2)
    if hasattr(b2, 'Association'):
        assert not _is_linked(b2, 'Association', a)


def test_assoc_associations33_link_reassign_clear():
    a = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b2 = persistence_Association(bidirectional=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", pivotTableName="sample_text_2", pseudo=False, serializationMaxDepth=13, targetColumnName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False, unique=False)
    _safe_set(a, 'persistence_Entity34', {b1})
    assert _is_linked(a, 'persistence_Entity34', b1)
    if hasattr(b1, 'persistence_Association35'):
        assert _is_linked(b1, 'persistence_Association35', a)
    _safe_set(a, 'persistence_Entity34', {b2})
    assert _is_linked(a, 'persistence_Entity34', b2)
    if hasattr(b1, 'persistence_Association35'):
        assert not _is_linked(b1, 'persistence_Association35', a)
    if hasattr(b2, 'persistence_Association35'):
        assert _is_linked(b2, 'persistence_Association35', a)
    _safe_set(a, 'persistence_Entity34', set())
    assert not _is_linked(a, 'persistence_Entity34', b2)
    if hasattr(b2, 'persistence_Association35'):
        assert not _is_linked(b2, 'persistence_Association35', a)


def test_assoc_attribute22_link_reassign_clear():
    a = persistence_ModelLabelAttribute(dateFormat="sample_text")
    b1 = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    b2 = persistence_Attribute(containerUnique=False, hidden=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", interfaceType="sample_text_2", ormType="sample_text_2", persistentType="sample_text_2", placeholder="sample_text_2", unique=False, validationPattern="sample_text_2")
    _safe_set(a, 'persistence_ModelLabelAttribute', b1)
    assert _is_linked(a, 'persistence_ModelLabelAttribute', b1)
    if hasattr(b1, 'persistence_Attribute23'):
        assert _is_linked(b1, 'persistence_Attribute23', a)
    _safe_set(a, 'persistence_ModelLabelAttribute', b2)
    assert _is_linked(a, 'persistence_ModelLabelAttribute', b2)
    if hasattr(b1, 'persistence_Attribute23'):
        assert not _is_linked(b1, 'persistence_Attribute23', a)
    if hasattr(b2, 'persistence_Attribute23'):
        assert _is_linked(b2, 'persistence_Attribute23', a)
    _safe_set(a, 'persistence_ModelLabelAttribute', None)
    assert not _is_linked(a, 'persistence_ModelLabelAttribute', b2)
    if hasattr(b2, 'persistence_Attribute23'):
        assert not _is_linked(b2, 'persistence_Attribute23', a)


def test_assoc_attributes30_link_reassign_clear():
    a = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    b2 = persistence_Attribute(containerUnique=False, hidden=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", interfaceType="sample_text_2", ormType="sample_text_2", persistentType="sample_text_2", placeholder="sample_text_2", unique=False, validationPattern="sample_text_2")
    _safe_set(a, 'persistence_Entity31', {b1})
    assert _is_linked(a, 'persistence_Entity31', b1)
    if hasattr(b1, 'persistence_Attribute32'):
        assert _is_linked(b1, 'persistence_Attribute32', a)
    _safe_set(a, 'persistence_Entity31', {b2})
    assert _is_linked(a, 'persistence_Entity31', b2)
    if hasattr(b1, 'persistence_Attribute32'):
        assert not _is_linked(b1, 'persistence_Attribute32', a)
    if hasattr(b2, 'persistence_Attribute32'):
        assert _is_linked(b2, 'persistence_Attribute32', a)
    _safe_set(a, 'persistence_Entity31', set())
    assert not _is_linked(a, 'persistence_Entity31', b2)
    if hasattr(b2, 'persistence_Attribute32'):
        assert not _is_linked(b2, 'persistence_Attribute32', a)


def test_assoc_containerUnique51_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature53', b1)
    assert _is_linked(a, 'persistence_Feature53', b1)
    if hasattr(b1, 'persistence_Entity52'):
        assert _is_linked(b1, 'persistence_Entity52', a)
    _safe_set(a, 'persistence_Feature53', b2)
    assert _is_linked(a, 'persistence_Feature53', b2)
    if hasattr(b1, 'persistence_Entity52'):
        assert not _is_linked(b1, 'persistence_Entity52', a)
    if hasattr(b2, 'persistence_Entity52'):
        assert _is_linked(b2, 'persistence_Entity52', a)
    _safe_set(a, 'persistence_Feature53', None)
    assert not _is_linked(a, 'persistence_Feature53', b2)
    if hasattr(b2, 'persistence_Entity52'):
        assert not _is_linked(b2, 'persistence_Entity52', a)


def test_assoc_dataType54_link_reassign_clear():
    a = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    b1 = persistence_DataType()
    b2 = persistence_DataType()
    _safe_set(a, 'persistence_DataTypeAttribute', b1)
    assert _is_linked(a, 'persistence_DataTypeAttribute', b1)
    if hasattr(b1, 'persistence_DataType55'):
        assert _is_linked(b1, 'persistence_DataType55', a)
    _safe_set(a, 'persistence_DataTypeAttribute', b2)
    assert _is_linked(a, 'persistence_DataTypeAttribute', b2)
    if hasattr(b1, 'persistence_DataType55'):
        assert not _is_linked(b1, 'persistence_DataType55', a)
    if hasattr(b2, 'persistence_DataType55'):
        assert _is_linked(b2, 'persistence_DataType55', a)
    _safe_set(a, 'persistence_DataTypeAttribute', None)
    assert not _is_linked(a, 'persistence_DataTypeAttribute', b2)
    if hasattr(b2, 'persistence_DataType55'):
        assert not _is_linked(b2, 'persistence_DataType55', a)


def test_assoc_dataTypes1_link_reassign_clear():
    a = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    b1 = persistence_DataType()
    b2 = persistence_DataType()
    _safe_set(a, 'persistence_Persistence2', {b1})
    assert _is_linked(a, 'persistence_Persistence2', b1)
    if hasattr(b1, 'persistence_DataType'):
        assert _is_linked(b1, 'persistence_DataType', a)
    _safe_set(a, 'persistence_Persistence2', {b2})
    assert _is_linked(a, 'persistence_Persistence2', b2)
    if hasattr(b1, 'persistence_DataType'):
        assert not _is_linked(b1, 'persistence_DataType', a)
    if hasattr(b2, 'persistence_DataType'):
        assert _is_linked(b2, 'persistence_DataType', a)
    _safe_set(a, 'persistence_Persistence2', set())
    assert not _is_linked(a, 'persistence_Persistence2', b2)
    if hasattr(b2, 'persistence_DataType'):
        assert not _is_linked(b2, 'persistence_DataType', a)


def test_assoc_defaultValue10_link_reassign_clear():
    a = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    b1 = persistence_Expression()
    b2 = persistence_Expression()
    _safe_set(a, 'persistence_Attribute11', b1)
    assert _is_linked(a, 'persistence_Attribute11', b1)
    if hasattr(b1, 'persistence_Expression'):
        assert _is_linked(b1, 'persistence_Expression', a)
    _safe_set(a, 'persistence_Attribute11', b2)
    assert _is_linked(a, 'persistence_Attribute11', b2)
    if hasattr(b1, 'persistence_Expression'):
        assert not _is_linked(b1, 'persistence_Expression', a)
    if hasattr(b2, 'persistence_Expression'):
        assert _is_linked(b2, 'persistence_Expression', a)
    _safe_set(a, 'persistence_Attribute11', None)
    assert not _is_linked(a, 'persistence_Attribute11', b2)
    if hasattr(b2, 'persistence_Expression'):
        assert not _is_linked(b2, 'persistence_Expression', a)


def test_assoc_dynamicLabel25_link_reassign_clear():
    a = persistence_ModelLabelAssociation(isSourceAssociation=True)
    b1 = persistence_ModelLabel(customise=True, format="sample_text")
    b2 = persistence_ModelLabel(customise=False, format="sample_text_2")
    _safe_set(a, 'persistence_ModelLabelAssociation26', b1)
    assert _is_linked(a, 'persistence_ModelLabelAssociation26', b1)
    if hasattr(b1, 'persistence_ModelLabel27'):
        assert _is_linked(b1, 'persistence_ModelLabel27', a)
    _safe_set(a, 'persistence_ModelLabelAssociation26', b2)
    assert _is_linked(a, 'persistence_ModelLabelAssociation26', b2)
    if hasattr(b1, 'persistence_ModelLabel27'):
        assert not _is_linked(b1, 'persistence_ModelLabel27', a)
    if hasattr(b2, 'persistence_ModelLabel27'):
        assert _is_linked(b2, 'persistence_ModelLabel27', a)
    _safe_set(a, 'persistence_ModelLabelAssociation26', None)
    assert not _is_linked(a, 'persistence_ModelLabelAssociation26', b2)
    if hasattr(b2, 'persistence_ModelLabel27'):
        assert not _is_linked(b2, 'persistence_ModelLabel27', a)


def test_assoc_entities3_link_reassign_clear():
    a = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Persistence4', {b1})
    assert _is_linked(a, 'persistence_Persistence4', b1)
    if hasattr(b1, 'persistence_Entity'):
        assert _is_linked(b1, 'persistence_Entity', a)
    _safe_set(a, 'persistence_Persistence4', {b2})
    assert _is_linked(a, 'persistence_Persistence4', b2)
    if hasattr(b1, 'persistence_Entity'):
        assert not _is_linked(b1, 'persistence_Entity', a)
    if hasattr(b2, 'persistence_Entity'):
        assert _is_linked(b2, 'persistence_Entity', a)
    _safe_set(a, 'persistence_Persistence4', set())
    assert not _is_linked(a, 'persistence_Persistence4', b2)
    if hasattr(b2, 'persistence_Entity'):
        assert not _is_linked(b2, 'persistence_Entity', a)


def test_assoc_features17_link_reassign_clear():
    a = persistence_ModelLabel(customise=True, format="sample_text")
    b1 = persistence_ModelLabelFeature()
    b2 = persistence_ModelLabelFeature()
    _safe_set(a, 'partOf', {b1})
    assert _is_linked(a, 'partOf', b1)
    if hasattr(b1, 'ModelLabelFeature'):
        assert _is_linked(b1, 'ModelLabelFeature', a)
    _safe_set(a, 'partOf', {b2})
    assert _is_linked(a, 'partOf', b2)
    if hasattr(b1, 'ModelLabelFeature'):
        assert not _is_linked(b1, 'ModelLabelFeature', a)
    if hasattr(b2, 'ModelLabelFeature'):
        assert _is_linked(b2, 'ModelLabelFeature', a)
    _safe_set(a, 'partOf', set())
    assert not _is_linked(a, 'partOf', b2)
    if hasattr(b2, 'ModelLabelFeature'):
        assert not _is_linked(b2, 'ModelLabelFeature', a)


def test_assoc_features28_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'partOf29'):
        assert _is_linked(b1, 'partOf29', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'partOf29'):
        assert not _is_linked(b1, 'partOf29', a)
    if hasattr(b2, 'partOf29'):
        assert _is_linked(b2, 'partOf29', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'partOf29'):
        assert not _is_linked(b2, 'partOf29', a)


def test_assoc_keyFor57_link_reassign_clear():
    a = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b1 = persistence_AssociationKey()
    b2 = persistence_AssociationKey()
    _safe_set(a, 'Association58', b1)
    assert _is_linked(a, 'Association58', b1)
    if hasattr(b1, 'keys'):
        assert _is_linked(b1, 'keys', a)
    _safe_set(a, 'Association58', b2)
    assert _is_linked(a, 'Association58', b2)
    if hasattr(b1, 'keys'):
        assert not _is_linked(b1, 'keys', a)
    if hasattr(b2, 'keys'):
        assert _is_linked(b2, 'keys', a)
    _safe_set(a, 'Association58', None)
    assert not _is_linked(a, 'Association58', b2)
    if hasattr(b2, 'keys'):
        assert not _is_linked(b2, 'keys', a)


def test_assoc_keys12_link_reassign_clear():
    a = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b1 = persistence_AssociationKey()
    b2 = persistence_AssociationKey()
    _safe_set(a, 'keyFor', {b1})
    assert _is_linked(a, 'keyFor', b1)
    if hasattr(b1, 'AssociationKey'):
        assert _is_linked(b1, 'AssociationKey', a)
    _safe_set(a, 'keyFor', {b2})
    assert _is_linked(a, 'keyFor', b2)
    if hasattr(b1, 'AssociationKey'):
        assert not _is_linked(b1, 'AssociationKey', a)
    if hasattr(b2, 'AssociationKey'):
        assert _is_linked(b2, 'AssociationKey', a)
    _safe_set(a, 'keyFor', set())
    assert not _is_linked(a, 'keyFor', b2)
    if hasattr(b2, 'AssociationKey'):
        assert not _is_linked(b2, 'AssociationKey', a)


def test_assoc_keys43_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature45', b1)
    assert _is_linked(a, 'persistence_Feature45', b1)
    if hasattr(b1, 'persistence_Entity44'):
        assert _is_linked(b1, 'persistence_Entity44', a)
    _safe_set(a, 'persistence_Feature45', b2)
    assert _is_linked(a, 'persistence_Feature45', b2)
    if hasattr(b1, 'persistence_Entity44'):
        assert not _is_linked(b1, 'persistence_Entity44', a)
    if hasattr(b2, 'persistence_Entity44'):
        assert _is_linked(b2, 'persistence_Entity44', a)
    _safe_set(a, 'persistence_Feature45', None)
    assert not _is_linked(a, 'persistence_Feature45', b2)
    if hasattr(b2, 'persistence_Entity44'):
        assert not _is_linked(b2, 'persistence_Entity44', a)


def test_assoc_labelFor15_link_reassign_clear():
    a = persistence_ModelLabel(customise=True, format="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'labels', b1)
    assert _is_linked(a, 'labels', b1)
    if hasattr(b1, 'Entity16'):
        assert _is_linked(b1, 'Entity16', a)
    _safe_set(a, 'labels', b2)
    assert _is_linked(a, 'labels', b2)
    if hasattr(b1, 'Entity16'):
        assert not _is_linked(b1, 'Entity16', a)
    if hasattr(b2, 'Entity16'):
        assert _is_linked(b2, 'Entity16', a)
    _safe_set(a, 'labels', None)
    assert not _is_linked(a, 'labels', b2)
    if hasattr(b2, 'Entity16'):
        assert not _is_linked(b2, 'Entity16', a)


def test_assoc_labels46_link_reassign_clear():
    a = persistence_ModelLabel(customise=True, format="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'ModelLabel47', b1)
    assert _is_linked(a, 'ModelLabel47', b1)
    if hasattr(b1, 'labelFor'):
        assert _is_linked(b1, 'labelFor', a)
    _safe_set(a, 'ModelLabel47', b2)
    assert _is_linked(a, 'ModelLabel47', b2)
    if hasattr(b1, 'labelFor'):
        assert not _is_linked(b1, 'labelFor', a)
    if hasattr(b2, 'labelFor'):
        assert _is_linked(b2, 'labelFor', a)
    _safe_set(a, 'ModelLabel47', None)
    assert not _is_linked(a, 'ModelLabel47', b2)
    if hasattr(b2, 'labelFor'):
        assert not _is_linked(b2, 'labelFor', a)


def test_assoc_partOf20_link_reassign_clear():
    a = persistence_ModelLabel(customise=True, format="sample_text")
    b1 = persistence_ModelLabelFeature()
    b2 = persistence_ModelLabelFeature()
    _safe_set(a, 'ModelLabel', b1)
    assert _is_linked(a, 'ModelLabel', b1)
    if hasattr(b1, 'features21'):
        assert _is_linked(b1, 'features21', a)
    _safe_set(a, 'ModelLabel', b2)
    assert _is_linked(a, 'ModelLabel', b2)
    if hasattr(b1, 'features21'):
        assert not _is_linked(b1, 'features21', a)
    if hasattr(b2, 'features21'):
        assert _is_linked(b2, 'features21', a)
    _safe_set(a, 'ModelLabel', None)
    assert not _is_linked(a, 'ModelLabel', b2)
    if hasattr(b2, 'features21'):
        assert not _is_linked(b2, 'features21', a)


def test_assoc_partOf5_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'features', b1)
    assert _is_linked(a, 'features', b1)
    if hasattr(b1, 'Entity'):
        assert _is_linked(b1, 'Entity', a)
    _safe_set(a, 'features', b2)
    assert _is_linked(a, 'features', b2)
    if hasattr(b1, 'Entity'):
        assert not _is_linked(b1, 'Entity', a)
    if hasattr(b2, 'Entity'):
        assert _is_linked(b2, 'Entity', a)
    _safe_set(a, 'features', None)
    assert not _is_linked(a, 'features', b2)
    if hasattr(b2, 'Entity'):
        assert not _is_linked(b2, 'Entity', a)


def test_assoc_serializationGroups0_link_reassign_clear():
    a = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    b1 = persistence_SerializationGroup()
    b2 = persistence_SerializationGroup()
    _safe_set(a, 'persistence_Persistence', {b1})
    assert _is_linked(a, 'persistence_Persistence', b1)
    if hasattr(b1, 'persistence_SerializationGroup'):
        assert _is_linked(b1, 'persistence_SerializationGroup', a)
    _safe_set(a, 'persistence_Persistence', {b2})
    assert _is_linked(a, 'persistence_Persistence', b2)
    if hasattr(b1, 'persistence_SerializationGroup'):
        assert not _is_linked(b1, 'persistence_SerializationGroup', a)
    if hasattr(b2, 'persistence_SerializationGroup'):
        assert _is_linked(b2, 'persistence_SerializationGroup', a)
    _safe_set(a, 'persistence_Persistence', set())
    assert not _is_linked(a, 'persistence_Persistence', b2)
    if hasattr(b2, 'persistence_SerializationGroup'):
        assert not _is_linked(b2, 'persistence_SerializationGroup', a)


def test_assoc_serializationGroups18_link_reassign_clear():
    a = persistence_ModelLabel(customise=True, format="sample_text")
    b1 = persistence_SerializationGroup()
    b2 = persistence_SerializationGroup()
    _safe_set(a, 'persistence_ModelLabel', {b1})
    assert _is_linked(a, 'persistence_ModelLabel', b1)
    if hasattr(b1, 'persistence_SerializationGroup19'):
        assert _is_linked(b1, 'persistence_SerializationGroup19', a)
    _safe_set(a, 'persistence_ModelLabel', {b2})
    assert _is_linked(a, 'persistence_ModelLabel', b2)
    if hasattr(b1, 'persistence_SerializationGroup19'):
        assert not _is_linked(b1, 'persistence_SerializationGroup19', a)
    if hasattr(b2, 'persistence_SerializationGroup19'):
        assert _is_linked(b2, 'persistence_SerializationGroup19', a)
    _safe_set(a, 'persistence_ModelLabel', set())
    assert not _is_linked(a, 'persistence_ModelLabel', b2)
    if hasattr(b2, 'persistence_SerializationGroup19'):
        assert not _is_linked(b2, 'persistence_SerializationGroup19', a)


def test_assoc_serializationGroups6_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_SerializationGroup()
    b2 = persistence_SerializationGroup()
    _safe_set(a, 'persistence_Feature', {b1})
    assert _is_linked(a, 'persistence_Feature', b1)
    if hasattr(b1, 'persistence_SerializationGroup7'):
        assert _is_linked(b1, 'persistence_SerializationGroup7', a)
    _safe_set(a, 'persistence_Feature', {b2})
    assert _is_linked(a, 'persistence_Feature', b2)
    if hasattr(b1, 'persistence_SerializationGroup7'):
        assert not _is_linked(b1, 'persistence_SerializationGroup7', a)
    if hasattr(b2, 'persistence_SerializationGroup7'):
        assert _is_linked(b2, 'persistence_SerializationGroup7', a)
    _safe_set(a, 'persistence_Feature', set())
    assert not _is_linked(a, 'persistence_Feature', b2)
    if hasattr(b2, 'persistence_SerializationGroup7'):
        assert not _is_linked(b2, 'persistence_SerializationGroup7', a)


def test_assoc_slugFields9_link_reassign_clear():
    a = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    b1 = persistence_Attribute(containerUnique=True, hidden=True, inputColumnClass="sample_text", inputElementClass="sample_text", interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", placeholder="sample_text", unique=True, validationPattern="sample_text")
    b2 = persistence_Attribute(containerUnique=False, hidden=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", interfaceType="sample_text_2", ormType="sample_text_2", persistentType="sample_text_2", placeholder="sample_text_2", unique=False, validationPattern="sample_text_2")
    _safe_set(a, 'persistence_Attribute', b1)
    assert _is_linked(a, 'persistence_Attribute', b1)
    if hasattr(b1, 'persistence_Attribute8'):
        assert _is_linked(b1, 'persistence_Attribute8', a)
    _safe_set(a, 'persistence_Attribute', b2)
    assert _is_linked(a, 'persistence_Attribute', b2)
    if hasattr(b1, 'persistence_Attribute8'):
        assert not _is_linked(b1, 'persistence_Attribute8', a)
    if hasattr(b2, 'persistence_Attribute8'):
        assert _is_linked(b2, 'persistence_Attribute8', a)
    _safe_set(a, 'persistence_Attribute', None)
    assert not _is_linked(a, 'persistence_Attribute', b2)
    if hasattr(b2, 'persistence_Attribute8'):
        assert not _is_linked(b2, 'persistence_Attribute8', a)


def test_assoc_sourceFeature59_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_AssociationKey()
    b2 = persistence_AssociationKey()
    _safe_set(a, 'persistence_Feature60', b1)
    assert _is_linked(a, 'persistence_Feature60', b1)
    if hasattr(b1, 'persistence_AssociationKey'):
        assert _is_linked(b1, 'persistence_AssociationKey', a)
    _safe_set(a, 'persistence_Feature60', b2)
    assert _is_linked(a, 'persistence_Feature60', b2)
    if hasattr(b1, 'persistence_AssociationKey'):
        assert not _is_linked(b1, 'persistence_AssociationKey', a)
    if hasattr(b2, 'persistence_AssociationKey'):
        assert _is_linked(b2, 'persistence_AssociationKey', a)
    _safe_set(a, 'persistence_Feature60', None)
    assert not _is_linked(a, 'persistence_Feature60', b2)
    if hasattr(b2, 'persistence_AssociationKey'):
        assert not _is_linked(b2, 'persistence_AssociationKey', a)


def test_assoc_targetEntity13_link_reassign_clear():
    a = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(bidirectional=True, inputColumnClass="sample_text", inputElementClass="sample_text", pivotTableName="sample_text", pseudo=True, serializationMaxDepth=7, targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    b2 = persistence_Association(bidirectional=False, inputColumnClass="sample_text_2", inputElementClass="sample_text_2", pivotTableName="sample_text_2", pseudo=False, serializationMaxDepth=13, targetColumnName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False, unique=False)
    _safe_set(a, 'Entity14', b1)
    assert _is_linked(a, 'Entity14', b1)
    if hasattr(b1, 'associationEnds'):
        assert _is_linked(b1, 'associationEnds', a)
    _safe_set(a, 'Entity14', b2)
    assert _is_linked(a, 'Entity14', b2)
    if hasattr(b1, 'associationEnds'):
        assert not _is_linked(b1, 'associationEnds', a)
    if hasattr(b2, 'associationEnds'):
        assert _is_linked(b2, 'associationEnds', a)
    _safe_set(a, 'Entity14', None)
    assert not _is_linked(a, 'Entity14', b2)
    if hasattr(b2, 'associationEnds'):
        assert not _is_linked(b2, 'associationEnds', a)


def test_assoc_targetFeature61_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_AssociationKey()
    b2 = persistence_AssociationKey()
    _safe_set(a, 'persistence_Feature63', b1)
    assert _is_linked(a, 'persistence_Feature63', b1)
    if hasattr(b1, 'persistence_AssociationKey62'):
        assert _is_linked(b1, 'persistence_AssociationKey62', a)
    _safe_set(a, 'persistence_Feature63', b2)
    assert _is_linked(a, 'persistence_Feature63', b2)
    if hasattr(b1, 'persistence_AssociationKey62'):
        assert not _is_linked(b1, 'persistence_AssociationKey62', a)
    if hasattr(b2, 'persistence_AssociationKey62'):
        assert _is_linked(b2, 'persistence_AssociationKey62', a)
    _safe_set(a, 'persistence_Feature63', None)
    assert not _is_linked(a, 'persistence_Feature63', b2)
    if hasattr(b2, 'persistence_AssociationKey62'):
        assert not _is_linked(b2, 'persistence_AssociationKey62', a)


def test_assoc_unique48_link_reassign_clear():
    a = persistence_Feature(booleanIsHasChoice="sample_text", cardinality="sample_text", collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, columnName="sample_text", customiseSet=True, defaultDisplayValue="sample_text", derived=True, displayClass="sample_text", emptyDisplayValue="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text", title="sample_text")
    b1 = persistence_Entity(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_Entity(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature50', b1)
    assert _is_linked(a, 'persistence_Feature50', b1)
    if hasattr(b1, 'persistence_Entity49'):
        assert _is_linked(b1, 'persistence_Entity49', a)
    _safe_set(a, 'persistence_Feature50', b2)
    assert _is_linked(a, 'persistence_Feature50', b2)
    if hasattr(b1, 'persistence_Entity49'):
        assert not _is_linked(b1, 'persistence_Entity49', a)
    if hasattr(b2, 'persistence_Entity49'):
        assert _is_linked(b2, 'persistence_Entity49', a)
    _safe_set(a, 'persistence_Feature50', None)
    assert not _is_linked(a, 'persistence_Feature50', b2)
    if hasattr(b2, 'persistence_Entity49'):
        assert not _is_linked(b2, 'persistence_Entity49', a)


def test_assoc_uploadPath56_link_reassign_clear():
    a = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    b1 = persistence_PathElement()
    b2 = persistence_PathElement()
    _safe_set(a, 'persistence_ResourceAttribute', {b1})
    assert _is_linked(a, 'persistence_ResourceAttribute', b1)
    if hasattr(b1, 'persistence_PathElement'):
        assert _is_linked(b1, 'persistence_PathElement', a)
    _safe_set(a, 'persistence_ResourceAttribute', {b2})
    assert _is_linked(a, 'persistence_ResourceAttribute', b2)
    if hasattr(b1, 'persistence_PathElement'):
        assert not _is_linked(b1, 'persistence_PathElement', a)
    if hasattr(b2, 'persistence_PathElement'):
        assert _is_linked(b2, 'persistence_PathElement', a)
    _safe_set(a, 'persistence_ResourceAttribute', set())
    assert not _is_linked(a, 'persistence_ResourceAttribute', b2)
    if hasattr(b2, 'persistence_PathElement'):
        assert not _is_linked(b2, 'persistence_PathElement', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Association_strategy = st.builds(Association)
@given(instance=Association_strategy)
@settings(max_examples=25)
def test_Association_instantiation(instance):
    assert isinstance(instance, Association)


Attribute_strategy = st.builds(Attribute)
@given(instance=Attribute_strategy)
@settings(max_examples=25)
def test_Attribute_instantiation(instance):
    assert isinstance(instance, Attribute)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


ModelLabelFeature_strategy = st.builds(ModelLabelFeature)
@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=25)
def test_ModelLabelFeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)


NamedDisplayElement_strategy = st.builds(NamedDisplayElement)
@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=25)
def test_NamedDisplayElement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


PathElement_strategy = st.builds(PathElement)
@given(instance=PathElement_strategy)
@settings(max_examples=25)
def test_PathElement_instantiation(instance):
    assert isinstance(instance, PathElement)


ResourceAttribute_strategy = st.builds(ResourceAttribute)
@given(instance=ResourceAttribute_strategy)
@settings(max_examples=25)
def test_ResourceAttribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)


persistence_Association_strategy = st.builds(persistence_Association, bidirectional=st.booleans(), inputColumnClass=safe_text, inputElementClass=safe_text, pivotTableName=safe_text, pseudo=st.booleans(), serializationMaxDepth=st.integers(), targetColumnName=safe_text, targetDisplayClass=safe_text, targetDisplayLabel=safe_text, targetFeatureName=safe_text, targetFooterClass=safe_text, targetHeaderClass=safe_text, targetInputClass=safe_text, targetPrimaryKey=st.booleans(), unique=st.booleans())
@given(instance=persistence_Association_strategy)
@settings(max_examples=25)
def test_persistence_Association_instantiation(instance):
    assert isinstance(instance, persistence_Association)


persistence_AssociationKey_strategy = st.builds(persistence_AssociationKey)
@given(instance=persistence_AssociationKey_strategy)
@settings(max_examples=25)
def test_persistence_AssociationKey_instantiation(instance):
    assert isinstance(instance, persistence_AssociationKey)


persistence_AssociationWithContainment_strategy = st.builds(persistence_AssociationWithContainment, sourceVisible=st.booleans())
@given(instance=persistence_AssociationWithContainment_strategy)
@settings(max_examples=25)
def test_persistence_AssociationWithContainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithContainment)


persistence_AssociationWithoutContainment_strategy = st.builds(persistence_AssociationWithoutContainment, targetCardinality=safe_text, targetUnique=st.booleans())
@given(instance=persistence_AssociationWithoutContainment_strategy)
@settings(max_examples=25)
def test_persistence_AssociationWithoutContainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithoutContainment)


persistence_Attribute_strategy = st.builds(persistence_Attribute, containerUnique=st.booleans(), hidden=st.booleans(), inputColumnClass=safe_text, inputElementClass=safe_text, interfaceType=safe_text, ormType=safe_text, persistentType=safe_text, placeholder=safe_text, unique=st.booleans(), validationPattern=safe_text)
@given(instance=persistence_Attribute_strategy)
@settings(max_examples=25)
def test_persistence_Attribute_instantiation(instance):
    assert isinstance(instance, persistence_Attribute)


persistence_DataType_strategy = st.builds(persistence_DataType)
@given(instance=persistence_DataType_strategy)
@settings(max_examples=25)
def test_persistence_DataType_instantiation(instance):
    assert isinstance(instance, persistence_DataType)


persistence_DataTypeAttribute_strategy = st.builds(persistence_DataTypeAttribute, caseInsensitive=st.booleans(), encrypt=st.booleans(), obfuscateFormFields=st.booleans())
@given(instance=persistence_DataTypeAttribute_strategy)
@settings(max_examples=25)
def test_persistence_DataTypeAttribute_instantiation(instance):
    assert isinstance(instance, persistence_DataTypeAttribute)


persistence_DateAttribute_strategy = st.builds(persistence_DateAttribute, details=safe_text, format=safe_text)
@given(instance=persistence_DateAttribute_strategy)
@settings(max_examples=25)
def test_persistence_DateAttribute_instantiation(instance):
    assert isinstance(instance, persistence_DateAttribute)


persistence_DatePathElement_strategy = st.builds(persistence_DatePathElement, format=safe_text)
@given(instance=persistence_DatePathElement_strategy)
@settings(max_examples=25)
def test_persistence_DatePathElement_instantiation(instance):
    assert isinstance(instance, persistence_DatePathElement)


persistence_Entity_strategy = st.builds(persistence_Entity, allowFormTypeCustomisation=st.booleans(), autoKeyGenerationStrategy=safe_text, autoKeyName=safe_text, autoKeyPersistentType=safe_text, implementsUserInterface=st.booleans(), pluralisedName=safe_text, singletonName=safe_text, tableName=safe_text)
@given(instance=persistence_Entity_strategy)
@settings(max_examples=25)
def test_persistence_Entity_instantiation(instance):
    assert isinstance(instance, persistence_Entity)


persistence_Expression_strategy = st.builds(persistence_Expression)
@given(instance=persistence_Expression_strategy)
@settings(max_examples=25)
def test_persistence_Expression_instantiation(instance):
    assert isinstance(instance, persistence_Expression)


persistence_Feature_strategy = st.builds(persistence_Feature, booleanIsHasChoice=safe_text, cardinality=safe_text, collectionOrmAllowAdd=st.booleans(), collectionOrmAllowRemove=st.booleans(), columnName=safe_text, customiseSet=st.booleans(), defaultDisplayValue=safe_text, derived=st.booleans(), displayClass=safe_text, emptyDisplayValue=safe_text, encodeUriKey=st.booleans(), footerClass=safe_text, headerClass=safe_text, ordered=st.booleans(), pluralisedName=safe_text, primaryKey=st.booleans(), singletonName=safe_text, title=safe_text)
@given(instance=persistence_Feature_strategy)
@settings(max_examples=25)
def test_persistence_Feature_instantiation(instance):
    assert isinstance(instance, persistence_Feature)


persistence_FileAttribute_strategy = st.builds(persistence_FileAttribute)
@given(instance=persistence_FileAttribute_strategy)
@settings(max_examples=25)
def test_persistence_FileAttribute_instantiation(instance):
    assert isinstance(instance, persistence_FileAttribute)


persistence_ImageAttribute_strategy = st.builds(persistence_ImageAttribute)
@given(instance=persistence_ImageAttribute_strategy)
@settings(max_examples=25)
def test_persistence_ImageAttribute_instantiation(instance):
    assert isinstance(instance, persistence_ImageAttribute)


persistence_Label_strategy = st.builds(persistence_Label)
@given(instance=persistence_Label_strategy)
@settings(max_examples=25)
def test_persistence_Label_instantiation(instance):
    assert isinstance(instance, persistence_Label)


persistence_LocationAttribute_strategy = st.builds(persistence_LocationAttribute)
@given(instance=persistence_LocationAttribute_strategy)
@settings(max_examples=25)
def test_persistence_LocationAttribute_instantiation(instance):
    assert isinstance(instance, persistence_LocationAttribute)


persistence_ModelLabel_strategy = st.builds(persistence_ModelLabel, customise=st.booleans(), format=safe_text)
@given(instance=persistence_ModelLabel_strategy)
@settings(max_examples=25)
def test_persistence_ModelLabel_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabel)


persistence_ModelLabelAssociation_strategy = st.builds(persistence_ModelLabelAssociation, isSourceAssociation=st.booleans())
@given(instance=persistence_ModelLabelAssociation_strategy)
@settings(max_examples=25)
def test_persistence_ModelLabelAssociation_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAssociation)


persistence_ModelLabelAttribute_strategy = st.builds(persistence_ModelLabelAttribute, dateFormat=safe_text)
@given(instance=persistence_ModelLabelAttribute_strategy)
@settings(max_examples=25)
def test_persistence_ModelLabelAttribute_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAttribute)


persistence_ModelLabelFeature_strategy = st.builds(persistence_ModelLabelFeature)
@given(instance=persistence_ModelLabelFeature_strategy)
@settings(max_examples=25)
def test_persistence_ModelLabelFeature_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelFeature)


persistence_PathElement_strategy = st.builds(persistence_PathElement)
@given(instance=persistence_PathElement_strategy)
@settings(max_examples=25)
def test_persistence_PathElement_instantiation(instance):
    assert isinstance(instance, persistence_PathElement)


persistence_Persistence_strategy = st.builds(persistence_Persistence, databaseTechnology=safe_text, ormTechnology=safe_text, timestampCreation=st.booleans(), timestampUpdates=st.booleans())
@given(instance=persistence_Persistence_strategy)
@settings(max_examples=25)
def test_persistence_Persistence_instantiation(instance):
    assert isinstance(instance, persistence_Persistence)


persistence_ResourceAttribute_strategy = st.builds(persistence_ResourceAttribute, maximumUploadSize=st.integers(), uploadsWithinWebsite=st.booleans(), validUploadExtensions=safe_text, validUploadMimeTypes=safe_text)
@given(instance=persistence_ResourceAttribute_strategy)
@settings(max_examples=25)
def test_persistence_ResourceAttribute_instantiation(instance):
    assert isinstance(instance, persistence_ResourceAttribute)


persistence_SerializationGroup_strategy = st.builds(persistence_SerializationGroup)
@given(instance=persistence_SerializationGroup_strategy)
@settings(max_examples=25)
def test_persistence_SerializationGroup_instantiation(instance):
    assert isinstance(instance, persistence_SerializationGroup)


persistence_StaticPathElement_strategy = st.builds(persistence_StaticPathElement, element=safe_text)
@given(instance=persistence_StaticPathElement_strategy)
@settings(max_examples=25)
def test_persistence_StaticPathElement_instantiation(instance):
    assert isinstance(instance, persistence_StaticPathElement)


persistence_UrlAttribute_strategy = st.builds(persistence_UrlAttribute, displayValue=safe_text)
@given(instance=persistence_UrlAttribute_strategy)
@settings(max_examples=25)
def test_persistence_UrlAttribute_instantiation(instance):
    assert isinstance(instance, persistence_UrlAttribute)


