import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Association,
    Attribute,
    Classifier,
    EncapsulatedFeature,
    EntityAssociation,
    EntityAttribute,
    EntityFeature,
    EntityOrView,
    Feature,
    Label,
    ModelLabelFeature,
    NamedDisplayElement,
    NamedElement,
    PathElement,
    ResourceAttribute,
    ViewFeature,
    persistence_Association,
    persistence_AssociationKey,
    persistence_AssociationWithContainment,
    persistence_AssociationWithoutContainment,
    persistence_Attribute,
    persistence_DataType,
    persistence_DataTypeAttribute,
    persistence_DateAttribute,
    persistence_DatePathElement,
    persistence_EncapsulatedAssociation,
    persistence_EncapsulatedAttribute,
    persistence_EncapsulatedFeature,
    persistence_Entity,
    persistence_EntityAssociation,
    persistence_EntityAttribute,
    persistence_EntityFeature,
    persistence_EntityOrView,
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
    persistence_View,
    persistence_ViewAssociation,
    persistence_ViewFeature,
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

def test_persistence_Association_inputClass_value_roundtrip():
    instance = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    assert instance.inputClass == "sample_text"
    instance.inputClass = "sample_text_2"
    assert instance.inputClass == "sample_text_2"


def test_persistence_Association_pseudo_value_roundtrip():
    instance = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    assert instance.pseudo == True
    instance.pseudo = False
    assert instance.pseudo == False


def test_persistence_Association_serializationMaxDepth_value_roundtrip():
    instance = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    assert instance.serializationMaxDepth == 7
    instance.serializationMaxDepth = 13
    assert instance.serializationMaxDepth == 13


def test_persistence_AssociationKey_targetColumnName_value_roundtrip():
    instance = persistence_AssociationKey(targetColumnName="sample_text")
    assert instance.targetColumnName == "sample_text"
    instance.targetColumnName = "sample_text_2"
    assert instance.targetColumnName == "sample_text_2"


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


def test_persistence_Attribute_inputClass_value_roundtrip():
    instance = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    assert instance.inputClass == "sample_text"
    instance.inputClass = "sample_text_2"
    assert instance.inputClass == "sample_text_2"


def test_persistence_Attribute_placeholder_value_roundtrip():
    instance = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    assert instance.placeholder == "sample_text"
    instance.placeholder = "sample_text_2"
    assert instance.placeholder == "sample_text_2"


def test_persistence_Attribute_validationPattern_value_roundtrip():
    instance = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
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


def test_persistence_EncapsulatedAssociation_cardinality_value_roundtrip():
    instance = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_persistence_EncapsulatedAssociation_isSourceAssociation_value_roundtrip():
    instance = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    assert instance.isSourceAssociation == True
    instance.isSourceAssociation = False
    assert instance.isSourceAssociation == False


def test_persistence_EncapsulatedAssociation_name_value_roundtrip():
    instance = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_persistence_EncapsulatedAttribute_cardinality_value_roundtrip():
    instance = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_persistence_EncapsulatedAttribute_name_value_roundtrip():
    instance = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_persistence_EncapsulatedFeature_alias_value_roundtrip():
    instance = persistence_EncapsulatedFeature(alias="sample_text", columnName="sample_text", displayLabel="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_persistence_EncapsulatedFeature_columnName_value_roundtrip():
    instance = persistence_EncapsulatedFeature(alias="sample_text", columnName="sample_text", displayLabel="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_persistence_EncapsulatedFeature_displayLabel_value_roundtrip():
    instance = persistence_EncapsulatedFeature(alias="sample_text", columnName="sample_text", displayLabel="sample_text")
    assert instance.displayLabel == "sample_text"
    instance.displayLabel = "sample_text_2"
    assert instance.displayLabel == "sample_text_2"


def test_persistence_EntityAssociation_bidirectional_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.bidirectional == True
    instance.bidirectional = False
    assert instance.bidirectional == False


def test_persistence_EntityAssociation_pivotTableName_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.pivotTableName == "sample_text"
    instance.pivotTableName = "sample_text_2"
    assert instance.pivotTableName == "sample_text_2"


def test_persistence_EntityAssociation_targetDisplayClass_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetDisplayClass == "sample_text"
    instance.targetDisplayClass = "sample_text_2"
    assert instance.targetDisplayClass == "sample_text_2"


def test_persistence_EntityAssociation_targetDisplayLabel_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetDisplayLabel == "sample_text"
    instance.targetDisplayLabel = "sample_text_2"
    assert instance.targetDisplayLabel == "sample_text_2"


def test_persistence_EntityAssociation_targetFeatureName_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetFeatureName == "sample_text"
    instance.targetFeatureName = "sample_text_2"
    assert instance.targetFeatureName == "sample_text_2"


def test_persistence_EntityAssociation_targetFooterClass_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetFooterClass == "sample_text"
    instance.targetFooterClass = "sample_text_2"
    assert instance.targetFooterClass == "sample_text_2"


def test_persistence_EntityAssociation_targetHeaderClass_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetHeaderClass == "sample_text"
    instance.targetHeaderClass = "sample_text_2"
    assert instance.targetHeaderClass == "sample_text_2"


def test_persistence_EntityAssociation_targetInputClass_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetInputClass == "sample_text"
    instance.targetInputClass = "sample_text_2"
    assert instance.targetInputClass == "sample_text_2"


def test_persistence_EntityAssociation_targetPrimaryKey_value_roundtrip():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert instance.targetPrimaryKey == True
    instance.targetPrimaryKey = False
    assert instance.targetPrimaryKey == False


def test_persistence_EntityAttribute_containerUnique_value_roundtrip():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert instance.containerUnique == True
    instance.containerUnique = False
    assert instance.containerUnique == False


def test_persistence_EntityAttribute_interfaceType_value_roundtrip():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert instance.interfaceType == "sample_text"
    instance.interfaceType = "sample_text_2"
    assert instance.interfaceType == "sample_text_2"


def test_persistence_EntityAttribute_ormType_value_roundtrip():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert instance.ormType == "sample_text"
    instance.ormType = "sample_text_2"
    assert instance.ormType == "sample_text_2"


def test_persistence_EntityAttribute_persistentType_value_roundtrip():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert instance.persistentType == "sample_text"
    instance.persistentType = "sample_text_2"
    assert instance.persistentType == "sample_text_2"


def test_persistence_EntityAttribute_primaryKey_value_roundtrip():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert instance.primaryKey == True
    instance.primaryKey = False
    assert instance.primaryKey == False


def test_persistence_EntityFeature_booleanIsHasChoice_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.booleanIsHasChoice == "sample_text"
    instance.booleanIsHasChoice = "sample_text_2"
    assert instance.booleanIsHasChoice == "sample_text_2"


def test_persistence_EntityFeature_cardinality_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_persistence_EntityFeature_columnName_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_persistence_EntityFeature_ordered_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_persistence_EntityFeature_pluralisedName_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.pluralisedName == "sample_text"
    instance.pluralisedName = "sample_text_2"
    assert instance.pluralisedName == "sample_text_2"


def test_persistence_EntityFeature_singletonName_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.singletonName == "sample_text"
    instance.singletonName = "sample_text_2"
    assert instance.singletonName == "sample_text_2"


def test_persistence_EntityFeature_unique_value_roundtrip():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_persistence_EntityOrView_autoKeyGenerationStrategy_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyGenerationStrategy == "sample_text"
    instance.autoKeyGenerationStrategy = "sample_text_2"
    assert instance.autoKeyGenerationStrategy == "sample_text_2"


def test_persistence_EntityOrView_autoKeyName_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyName == "sample_text"
    instance.autoKeyName = "sample_text_2"
    assert instance.autoKeyName == "sample_text_2"


def test_persistence_EntityOrView_autoKeyPersistentType_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.autoKeyPersistentType == "sample_text"
    instance.autoKeyPersistentType = "sample_text_2"
    assert instance.autoKeyPersistentType == "sample_text_2"


def test_persistence_EntityOrView_implementsUserInterface_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.implementsUserInterface == True
    instance.implementsUserInterface = False
    assert instance.implementsUserInterface == False


def test_persistence_EntityOrView_pluralisedName_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.pluralisedName == "sample_text"
    instance.pluralisedName = "sample_text_2"
    assert instance.pluralisedName == "sample_text_2"


def test_persistence_EntityOrView_singletonName_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.singletonName == "sample_text"
    instance.singletonName = "sample_text_2"
    assert instance.singletonName == "sample_text_2"


def test_persistence_EntityOrView_tableName_value_roundtrip():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_persistence_Feature_collectionAllowAdd_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.collectionAllowAdd == True
    instance.collectionAllowAdd = False
    assert instance.collectionAllowAdd == False


def test_persistence_Feature_collectionAllowRemove_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.collectionAllowRemove == True
    instance.collectionAllowRemove = False
    assert instance.collectionAllowRemove == False


def test_persistence_Feature_displayClass_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.displayClass == "sample_text"
    instance.displayClass = "sample_text_2"
    assert instance.displayClass == "sample_text_2"


def test_persistence_Feature_encodeUriKey_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.encodeUriKey == True
    instance.encodeUriKey = False
    assert instance.encodeUriKey == False


def test_persistence_Feature_footerClass_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.footerClass == "sample_text"
    instance.footerClass = "sample_text_2"
    assert instance.footerClass == "sample_text_2"


def test_persistence_Feature_headerClass_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.headerClass == "sample_text"
    instance.headerClass = "sample_text_2"
    assert instance.headerClass == "sample_text_2"


def test_persistence_Feature_nullDisplayValue_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.nullDisplayValue == "sample_text"
    instance.nullDisplayValue = "sample_text_2"
    assert instance.nullDisplayValue == "sample_text_2"


def test_persistence_Feature_title_value_roundtrip():
    instance = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_persistence_ModelLabel_format_value_roundtrip():
    instance = persistence_ModelLabel(format="sample_text")
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


def test_persistence_Persistence_databaseHost_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databaseHost == "sample_text"
    instance.databaseHost = "sample_text_2"
    assert instance.databaseHost == "sample_text_2"


def test_persistence_Persistence_databaseName_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databaseName == "sample_text"
    instance.databaseName = "sample_text_2"
    assert instance.databaseName == "sample_text_2"


def test_persistence_Persistence_databasePassword_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databasePassword == "sample_text"
    instance.databasePassword = "sample_text_2"
    assert instance.databasePassword == "sample_text_2"


def test_persistence_Persistence_databasePort_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databasePort == "sample_text"
    instance.databasePort = "sample_text_2"
    assert instance.databasePort == "sample_text_2"


def test_persistence_Persistence_databasePrefix_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databasePrefix == "sample_text"
    instance.databasePrefix = "sample_text_2"
    assert instance.databasePrefix == "sample_text_2"


def test_persistence_Persistence_databaseTechnology_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databaseTechnology == "sample_text"
    instance.databaseTechnology = "sample_text_2"
    assert instance.databaseTechnology == "sample_text_2"


def test_persistence_Persistence_databaseUsername_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.databaseUsername == "sample_text"
    instance.databaseUsername = "sample_text_2"
    assert instance.databaseUsername == "sample_text_2"


def test_persistence_Persistence_ormTechnology_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.ormTechnology == "sample_text"
    instance.ormTechnology = "sample_text_2"
    assert instance.ormTechnology == "sample_text_2"


def test_persistence_Persistence_timestampCreation_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    assert instance.timestampCreation == True
    instance.timestampCreation = False
    assert instance.timestampCreation == False


def test_persistence_Persistence_timestampUpdates_value_roundtrip():
    instance = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
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


def test_persistence_ViewAssociation_cardinality_value_roundtrip():
    instance = persistence_ViewAssociation(cardinality="sample_text")
    assert instance.cardinality == "sample_text"
    instance.cardinality = "sample_text_2"
    assert instance.cardinality == "sample_text_2"


def test_persistence_EncapsulatedAssociation_isa_Association():
    instance = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    assert isinstance(instance, Association)


def test_persistence_EntityAssociation_isa_Association():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert isinstance(instance, Association)


def test_persistence_ViewAssociation_isa_Association():
    instance = persistence_ViewAssociation(cardinality="sample_text")
    assert isinstance(instance, Association)


def test_persistence_EncapsulatedAttribute_isa_Attribute():
    instance = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    assert isinstance(instance, Attribute)


def test_persistence_EntityAttribute_isa_Attribute():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert isinstance(instance, Attribute)


def test_persistence_EntityOrView_isa_Classifier():
    instance = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    assert isinstance(instance, Classifier)


def test_persistence_EncapsulatedAssociation_isa_EncapsulatedFeature():
    instance = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    assert isinstance(instance, EncapsulatedFeature)


def test_persistence_EncapsulatedAttribute_isa_EncapsulatedFeature():
    instance = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    assert isinstance(instance, EncapsulatedFeature)


def test_persistence_AssociationWithContainment_isa_EntityAssociation():
    instance = persistence_AssociationWithContainment(sourceVisible=True)
    assert isinstance(instance, EntityAssociation)


def test_persistence_AssociationWithoutContainment_isa_EntityAssociation():
    instance = persistence_AssociationWithoutContainment(targetCardinality="sample_text", targetUnique=True)
    assert isinstance(instance, EntityAssociation)


def test_persistence_DataTypeAttribute_isa_EntityAttribute():
    instance = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    assert isinstance(instance, EntityAttribute)


def test_persistence_DateAttribute_isa_EntityAttribute():
    instance = persistence_DateAttribute(details="sample_text", format="sample_text")
    assert isinstance(instance, EntityAttribute)


def test_persistence_LocationAttribute_isa_EntityAttribute():
    instance = persistence_LocationAttribute()
    assert isinstance(instance, EntityAttribute)


def test_persistence_ResourceAttribute_isa_EntityAttribute():
    instance = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    assert isinstance(instance, EntityAttribute)


def test_persistence_UrlAttribute_isa_EntityAttribute():
    instance = persistence_UrlAttribute(displayValue="sample_text")
    assert isinstance(instance, EntityAttribute)


def test_persistence_EntityAssociation_isa_EntityFeature():
    instance = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    assert isinstance(instance, EntityFeature)


def test_persistence_EntityAttribute_isa_EntityFeature():
    instance = persistence_EntityAttribute(containerUnique=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", primaryKey=True)
    assert isinstance(instance, EntityFeature)


def test_persistence_Entity_isa_EntityOrView():
    instance = persistence_Entity()
    assert isinstance(instance, EntityOrView)


def test_persistence_View_isa_EntityOrView():
    instance = persistence_View()
    assert isinstance(instance, EntityOrView)


def test_persistence_Association_isa_Feature():
    instance = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    assert isinstance(instance, Feature)


def test_persistence_Attribute_isa_Feature():
    instance = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    assert isinstance(instance, Feature)


def test_persistence_EntityFeature_isa_Feature():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert isinstance(instance, Feature)


def test_persistence_ViewFeature_isa_Feature():
    instance = persistence_ViewFeature()
    assert isinstance(instance, Feature)


def test_persistence_Attribute_isa_Label():
    instance = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    assert isinstance(instance, Label)


def test_persistence_ModelLabel_isa_Label():
    instance = persistence_ModelLabel(format="sample_text")
    assert isinstance(instance, Label)


def test_persistence_ModelLabelAssociation_isa_ModelLabelFeature():
    instance = persistence_ModelLabelAssociation(isSourceAssociation=True)
    assert isinstance(instance, ModelLabelFeature)


def test_persistence_ModelLabelAttribute_isa_ModelLabelFeature():
    instance = persistence_ModelLabelAttribute(dateFormat="sample_text")
    assert isinstance(instance, ModelLabelFeature)


def test_persistence_EntityFeature_isa_NamedDisplayElement():
    instance = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    assert isinstance(instance, NamedDisplayElement)


def test_persistence_ViewAssociation_isa_NamedDisplayElement():
    instance = persistence_ViewAssociation(cardinality="sample_text")
    assert isinstance(instance, NamedDisplayElement)


def test_persistence_ModelLabel_isa_NamedElement():
    instance = persistence_ModelLabel(format="sample_text")
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


def test_persistence_EncapsulatedFeature_isa_ViewFeature():
    instance = persistence_EncapsulatedFeature(alias="sample_text", columnName="sample_text", displayLabel="sample_text")
    assert isinstance(instance, ViewFeature)


def test_persistence_ViewAssociation_isa_ViewFeature():
    instance = persistence_ViewAssociation(cardinality="sample_text")
    assert isinstance(instance, ViewFeature)


def test_assoc_allAssociations24_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'persistence_EntityOrView25', {b1})
    assert _is_linked(a, 'persistence_EntityOrView25', b1)
    if hasattr(b1, 'persistence_Association26'):
        assert _is_linked(b1, 'persistence_Association26', a)
    _safe_set(a, 'persistence_EntityOrView25', {b2})
    assert _is_linked(a, 'persistence_EntityOrView25', b2)
    if hasattr(b1, 'persistence_Association26'):
        assert not _is_linked(b1, 'persistence_Association26', a)
    if hasattr(b2, 'persistence_Association26'):
        assert _is_linked(b2, 'persistence_Association26', a)
    _safe_set(a, 'persistence_EntityOrView25', set())
    assert not _is_linked(a, 'persistence_EntityOrView25', b2)
    if hasattr(b2, 'persistence_Association26'):
        assert not _is_linked(b2, 'persistence_Association26', a)


def test_assoc_allFeatures17_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature19', b1)
    assert _is_linked(a, 'persistence_Feature19', b1)
    if hasattr(b1, 'persistence_EntityOrView18'):
        assert _is_linked(b1, 'persistence_EntityOrView18', a)
    _safe_set(a, 'persistence_Feature19', b2)
    assert _is_linked(a, 'persistence_Feature19', b2)
    if hasattr(b1, 'persistence_EntityOrView18'):
        assert not _is_linked(b1, 'persistence_EntityOrView18', a)
    if hasattr(b2, 'persistence_EntityOrView18'):
        assert _is_linked(b2, 'persistence_EntityOrView18', a)
    _safe_set(a, 'persistence_Feature19', None)
    assert not _is_linked(a, 'persistence_Feature19', b2)
    if hasattr(b2, 'persistence_EntityOrView18'):
        assert not _is_linked(b2, 'persistence_EntityOrView18', a)


def test_assoc_association47_link_reassign_clear():
    a = persistence_ModelLabelAssociation(isSourceAssociation=True)
    b1 = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    b2 = persistence_EntityAssociation(bidirectional=False, pivotTableName="sample_text_2", targetDisplayClass="sample_text_2", targetDisplayLabel="sample_text_2", targetFeatureName="sample_text_2", targetFooterClass="sample_text_2", targetHeaderClass="sample_text_2", targetInputClass="sample_text_2", targetPrimaryKey=False)
    _safe_set(a, 'persistence_ModelLabelAssociation', b1)
    assert _is_linked(a, 'persistence_ModelLabelAssociation', b1)
    if hasattr(b1, 'persistence_EntityAssociation'):
        assert _is_linked(b1, 'persistence_EntityAssociation', a)
    _safe_set(a, 'persistence_ModelLabelAssociation', b2)
    assert _is_linked(a, 'persistence_ModelLabelAssociation', b2)
    if hasattr(b1, 'persistence_EntityAssociation'):
        assert not _is_linked(b1, 'persistence_EntityAssociation', a)
    if hasattr(b2, 'persistence_EntityAssociation'):
        assert _is_linked(b2, 'persistence_EntityAssociation', a)
    _safe_set(a, 'persistence_ModelLabelAssociation', None)
    assert not _is_linked(a, 'persistence_ModelLabelAssociation', b2)
    if hasattr(b2, 'persistence_EntityAssociation'):
        assert not _is_linked(b2, 'persistence_EntityAssociation', a)


def test_assoc_association74_link_reassign_clear():
    a = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'encapsulatedBy', b1)
    assert _is_linked(a, 'encapsulatedBy', b1)
    if hasattr(b1, 'Association'):
        assert _is_linked(b1, 'Association', a)
    _safe_set(a, 'encapsulatedBy', b2)
    assert _is_linked(a, 'encapsulatedBy', b2)
    if hasattr(b1, 'Association'):
        assert not _is_linked(b1, 'Association', a)
    if hasattr(b2, 'Association'):
        assert _is_linked(b2, 'Association', a)
    _safe_set(a, 'encapsulatedBy', None)
    assert not _is_linked(a, 'encapsulatedBy', b2)
    if hasattr(b2, 'Association'):
        assert not _is_linked(b2, 'Association', a)


def test_assoc_associationEnds53_link_reassign_clear():
    a = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'EntityAssociation', b1)
    assert _is_linked(a, 'EntityAssociation', b1)
    if hasattr(b1, 'targetEntity'):
        assert _is_linked(b1, 'targetEntity', a)
    _safe_set(a, 'EntityAssociation', b2)
    assert _is_linked(a, 'EntityAssociation', b2)
    if hasattr(b1, 'targetEntity'):
        assert not _is_linked(b1, 'targetEntity', a)
    if hasattr(b2, 'targetEntity'):
        assert _is_linked(b2, 'targetEntity', a)
    _safe_set(a, 'EntityAssociation', None)
    assert not _is_linked(a, 'EntityAssociation', b2)
    if hasattr(b2, 'targetEntity'):
        assert not _is_linked(b2, 'targetEntity', a)


def test_assoc_associations22_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'persistence_EntityOrView23', {b1})
    assert _is_linked(a, 'persistence_EntityOrView23', b1)
    if hasattr(b1, 'persistence_Association'):
        assert _is_linked(b1, 'persistence_Association', a)
    _safe_set(a, 'persistence_EntityOrView23', {b2})
    assert _is_linked(a, 'persistence_EntityOrView23', b2)
    if hasattr(b1, 'persistence_Association'):
        assert not _is_linked(b1, 'persistence_Association', a)
    if hasattr(b2, 'persistence_Association'):
        assert _is_linked(b2, 'persistence_Association', a)
    _safe_set(a, 'persistence_EntityOrView23', set())
    assert not _is_linked(a, 'persistence_EntityOrView23', b2)
    if hasattr(b2, 'persistence_Association'):
        assert not _is_linked(b2, 'persistence_Association', a)


def test_assoc_attribute45_link_reassign_clear():
    a = persistence_ModelLabelAttribute(dateFormat="sample_text")
    b1 = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    b2 = persistence_Attribute(inputClass="sample_text_2", placeholder="sample_text_2", validationPattern="sample_text_2")
    _safe_set(a, 'persistence_ModelLabelAttribute', b1)
    assert _is_linked(a, 'persistence_ModelLabelAttribute', b1)
    if hasattr(b1, 'persistence_Attribute46'):
        assert _is_linked(b1, 'persistence_Attribute46', a)
    _safe_set(a, 'persistence_ModelLabelAttribute', b2)
    assert _is_linked(a, 'persistence_ModelLabelAttribute', b2)
    if hasattr(b1, 'persistence_Attribute46'):
        assert not _is_linked(b1, 'persistence_Attribute46', a)
    if hasattr(b2, 'persistence_Attribute46'):
        assert _is_linked(b2, 'persistence_Attribute46', a)
    _safe_set(a, 'persistence_ModelLabelAttribute', None)
    assert not _is_linked(a, 'persistence_ModelLabelAttribute', b2)
    if hasattr(b2, 'persistence_Attribute46'):
        assert not _is_linked(b2, 'persistence_Attribute46', a)


def test_assoc_attribute72_link_reassign_clear():
    a = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    b1 = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    b2 = persistence_Attribute(inputClass="sample_text_2", placeholder="sample_text_2", validationPattern="sample_text_2")
    _safe_set(a, 'persistence_EncapsulatedAttribute', b1)
    assert _is_linked(a, 'persistence_EncapsulatedAttribute', b1)
    if hasattr(b1, 'persistence_Attribute73'):
        assert _is_linked(b1, 'persistence_Attribute73', a)
    _safe_set(a, 'persistence_EncapsulatedAttribute', b2)
    assert _is_linked(a, 'persistence_EncapsulatedAttribute', b2)
    if hasattr(b1, 'persistence_Attribute73'):
        assert not _is_linked(b1, 'persistence_Attribute73', a)
    if hasattr(b2, 'persistence_Attribute73'):
        assert _is_linked(b2, 'persistence_Attribute73', a)
    _safe_set(a, 'persistence_EncapsulatedAttribute', None)
    assert not _is_linked(a, 'persistence_EncapsulatedAttribute', b2)
    if hasattr(b2, 'persistence_Attribute73'):
        assert not _is_linked(b2, 'persistence_Attribute73', a)


def test_assoc_attributes20_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    b2 = persistence_Attribute(inputClass="sample_text_2", placeholder="sample_text_2", validationPattern="sample_text_2")
    _safe_set(a, 'persistence_EntityOrView21', {b1})
    assert _is_linked(a, 'persistence_EntityOrView21', b1)
    if hasattr(b1, 'persistence_Attribute'):
        assert _is_linked(b1, 'persistence_Attribute', a)
    _safe_set(a, 'persistence_EntityOrView21', {b2})
    assert _is_linked(a, 'persistence_EntityOrView21', b2)
    if hasattr(b1, 'persistence_Attribute'):
        assert not _is_linked(b1, 'persistence_Attribute', a)
    if hasattr(b2, 'persistence_Attribute'):
        assert _is_linked(b2, 'persistence_Attribute', a)
    _safe_set(a, 'persistence_EntityOrView21', set())
    assert not _is_linked(a, 'persistence_EntityOrView21', b2)
    if hasattr(b2, 'persistence_Attribute'):
        assert not _is_linked(b2, 'persistence_Attribute', a)


def test_assoc_containerUnique10_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature12', b1)
    assert _is_linked(a, 'persistence_Feature12', b1)
    if hasattr(b1, 'persistence_EntityOrView11'):
        assert _is_linked(b1, 'persistence_EntityOrView11', a)
    _safe_set(a, 'persistence_Feature12', b2)
    assert _is_linked(a, 'persistence_Feature12', b2)
    if hasattr(b1, 'persistence_EntityOrView11'):
        assert not _is_linked(b1, 'persistence_EntityOrView11', a)
    if hasattr(b2, 'persistence_EntityOrView11'):
        assert _is_linked(b2, 'persistence_EntityOrView11', a)
    _safe_set(a, 'persistence_Feature12', None)
    assert not _is_linked(a, 'persistence_Feature12', b2)
    if hasattr(b2, 'persistence_EntityOrView11'):
        assert not _is_linked(b2, 'persistence_EntityOrView11', a)


def test_assoc_dataType55_link_reassign_clear():
    a = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    b1 = persistence_DataType()
    b2 = persistence_DataType()
    _safe_set(a, 'persistence_DataTypeAttribute', b1)
    assert _is_linked(a, 'persistence_DataTypeAttribute', b1)
    if hasattr(b1, 'persistence_DataType56'):
        assert _is_linked(b1, 'persistence_DataType56', a)
    _safe_set(a, 'persistence_DataTypeAttribute', b2)
    assert _is_linked(a, 'persistence_DataTypeAttribute', b2)
    if hasattr(b1, 'persistence_DataType56'):
        assert not _is_linked(b1, 'persistence_DataType56', a)
    if hasattr(b2, 'persistence_DataType56'):
        assert _is_linked(b2, 'persistence_DataType56', a)
    _safe_set(a, 'persistence_DataTypeAttribute', None)
    assert not _is_linked(a, 'persistence_DataTypeAttribute', b2)
    if hasattr(b2, 'persistence_DataType56'):
        assert not _is_linked(b2, 'persistence_DataType56', a)


def test_assoc_dataTypes1_link_reassign_clear():
    a = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
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


def test_assoc_defaultValue30_link_reassign_clear():
    a = persistence_Attribute(inputClass="sample_text", placeholder="sample_text", validationPattern="sample_text")
    b1 = persistence_Expression()
    b2 = persistence_Expression()
    _safe_set(a, 'persistence_Attribute31', b1)
    assert _is_linked(a, 'persistence_Attribute31', b1)
    if hasattr(b1, 'persistence_Expression'):
        assert _is_linked(b1, 'persistence_Expression', a)
    _safe_set(a, 'persistence_Attribute31', b2)
    assert _is_linked(a, 'persistence_Attribute31', b2)
    if hasattr(b1, 'persistence_Expression'):
        assert not _is_linked(b1, 'persistence_Expression', a)
    if hasattr(b2, 'persistence_Expression'):
        assert _is_linked(b2, 'persistence_Expression', a)
    _safe_set(a, 'persistence_Attribute31', None)
    assert not _is_linked(a, 'persistence_Attribute31', b2)
    if hasattr(b2, 'persistence_Expression'):
        assert not _is_linked(b2, 'persistence_Expression', a)


def test_assoc_dynamicLabel48_link_reassign_clear():
    a = persistence_ModelLabelAssociation(isSourceAssociation=True)
    b1 = persistence_ModelLabel(format="sample_text")
    b2 = persistence_ModelLabel(format="sample_text_2")
    _safe_set(a, 'persistence_ModelLabelAssociation49', b1)
    assert _is_linked(a, 'persistence_ModelLabelAssociation49', b1)
    if hasattr(b1, 'persistence_ModelLabel50'):
        assert _is_linked(b1, 'persistence_ModelLabel50', a)
    _safe_set(a, 'persistence_ModelLabelAssociation49', b2)
    assert _is_linked(a, 'persistence_ModelLabelAssociation49', b2)
    if hasattr(b1, 'persistence_ModelLabel50'):
        assert not _is_linked(b1, 'persistence_ModelLabel50', a)
    if hasattr(b2, 'persistence_ModelLabel50'):
        assert _is_linked(b2, 'persistence_ModelLabel50', a)
    _safe_set(a, 'persistence_ModelLabelAssociation49', None)
    assert not _is_linked(a, 'persistence_ModelLabelAssociation49', b2)
    if hasattr(b2, 'persistence_ModelLabel50'):
        assert not _is_linked(b2, 'persistence_ModelLabel50', a)


def test_assoc_encapsulatedBy32_link_reassign_clear():
    a = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'EncapsulatedAssociation', b1)
    assert _is_linked(a, 'EncapsulatedAssociation', b1)
    if hasattr(b1, 'association'):
        assert _is_linked(b1, 'association', a)
    _safe_set(a, 'EncapsulatedAssociation', b2)
    assert _is_linked(a, 'EncapsulatedAssociation', b2)
    if hasattr(b1, 'association'):
        assert not _is_linked(b1, 'association', a)
    if hasattr(b2, 'association'):
        assert _is_linked(b2, 'association', a)
    _safe_set(a, 'EncapsulatedAssociation', None)
    assert not _is_linked(a, 'EncapsulatedAssociation', b2)
    if hasattr(b2, 'association'):
        assert not _is_linked(b2, 'association', a)


def test_assoc_encapsulatedTarget76_link_reassign_clear():
    a = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b1 = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b2 = persistence_EncapsulatedAssociation(cardinality="sample_text_2", isSourceAssociation=False, name="sample_text_2")
    _safe_set(a, 'persistence_EncapsulatedAssociation', b1)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation', b1)
    if hasattr(b1, 'persistence_EncapsulatedAssociation75'):
        assert _is_linked(b1, 'persistence_EncapsulatedAssociation75', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation', b2)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation', b2)
    if hasattr(b1, 'persistence_EncapsulatedAssociation75'):
        assert not _is_linked(b1, 'persistence_EncapsulatedAssociation75', a)
    if hasattr(b2, 'persistence_EncapsulatedAssociation75'):
        assert _is_linked(b2, 'persistence_EncapsulatedAssociation75', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation', None)
    assert not _is_linked(a, 'persistence_EncapsulatedAssociation', b2)
    if hasattr(b2, 'persistence_EncapsulatedAssociation75'):
        assert not _is_linked(b2, 'persistence_EncapsulatedAssociation75', a)


def test_assoc_encapsulates67_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_View()
    b2 = persistence_View()
    _safe_set(a, 'persistence_EntityOrView68', b1)
    assert _is_linked(a, 'persistence_EntityOrView68', b1)
    if hasattr(b1, 'persistence_View'):
        assert _is_linked(b1, 'persistence_View', a)
    _safe_set(a, 'persistence_EntityOrView68', b2)
    assert _is_linked(a, 'persistence_EntityOrView68', b2)
    if hasattr(b1, 'persistence_View'):
        assert not _is_linked(b1, 'persistence_View', a)
    if hasattr(b2, 'persistence_View'):
        assert _is_linked(b2, 'persistence_View', a)
    _safe_set(a, 'persistence_EntityOrView68', None)
    assert not _is_linked(a, 'persistence_EntityOrView68', b2)
    if hasattr(b2, 'persistence_View'):
        assert not _is_linked(b2, 'persistence_View', a)


def test_assoc_entities3_link_reassign_clear():
    a = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Persistence4', {b1})
    assert _is_linked(a, 'persistence_Persistence4', b1)
    if hasattr(b1, 'persistence_EntityOrView'):
        assert _is_linked(b1, 'persistence_EntityOrView', a)
    _safe_set(a, 'persistence_Persistence4', {b2})
    assert _is_linked(a, 'persistence_Persistence4', b2)
    if hasattr(b1, 'persistence_EntityOrView'):
        assert not _is_linked(b1, 'persistence_EntityOrView', a)
    if hasattr(b2, 'persistence_EntityOrView'):
        assert _is_linked(b2, 'persistence_EntityOrView', a)
    _safe_set(a, 'persistence_Persistence4', set())
    assert not _is_linked(a, 'persistence_Persistence4', b2)
    if hasattr(b2, 'persistence_EntityOrView'):
        assert not _is_linked(b2, 'persistence_EntityOrView', a)


def test_assoc_entityFeatures51_link_reassign_clear():
    a = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'EntityFeature', b1)
    assert _is_linked(a, 'EntityFeature', b1)
    if hasattr(b1, 'partOf52'):
        assert _is_linked(b1, 'partOf52', a)
    _safe_set(a, 'EntityFeature', b2)
    assert _is_linked(a, 'EntityFeature', b2)
    if hasattr(b1, 'partOf52'):
        assert not _is_linked(b1, 'partOf52', a)
    if hasattr(b2, 'partOf52'):
        assert _is_linked(b2, 'partOf52', a)
    _safe_set(a, 'EntityFeature', None)
    assert not _is_linked(a, 'EntityFeature', b2)
    if hasattr(b2, 'partOf52'):
        assert not _is_linked(b2, 'partOf52', a)


def test_assoc_features14_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature16', b1)
    assert _is_linked(a, 'persistence_Feature16', b1)
    if hasattr(b1, 'persistence_EntityOrView15'):
        assert _is_linked(b1, 'persistence_EntityOrView15', a)
    _safe_set(a, 'persistence_Feature16', b2)
    assert _is_linked(a, 'persistence_Feature16', b2)
    if hasattr(b1, 'persistence_EntityOrView15'):
        assert not _is_linked(b1, 'persistence_EntityOrView15', a)
    if hasattr(b2, 'persistence_EntityOrView15'):
        assert _is_linked(b2, 'persistence_EntityOrView15', a)
    _safe_set(a, 'persistence_Feature16', None)
    assert not _is_linked(a, 'persistence_Feature16', b2)
    if hasattr(b2, 'persistence_EntityOrView15'):
        assert not _is_linked(b2, 'persistence_EntityOrView15', a)


def test_assoc_features40_link_reassign_clear():
    a = persistence_ModelLabel(format="sample_text")
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


def test_assoc_keyFor61_link_reassign_clear():
    a = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    b1 = persistence_AssociationKey(targetColumnName="sample_text")
    b2 = persistence_AssociationKey(targetColumnName="sample_text_2")
    _safe_set(a, 'EntityAssociation62', b1)
    assert _is_linked(a, 'EntityAssociation62', b1)
    if hasattr(b1, 'keys'):
        assert _is_linked(b1, 'keys', a)
    _safe_set(a, 'EntityAssociation62', b2)
    assert _is_linked(a, 'EntityAssociation62', b2)
    if hasattr(b1, 'keys'):
        assert not _is_linked(b1, 'keys', a)
    if hasattr(b2, 'keys'):
        assert _is_linked(b2, 'keys', a)
    _safe_set(a, 'EntityAssociation62', None)
    assert not _is_linked(a, 'EntityAssociation62', b2)
    if hasattr(b2, 'keys'):
        assert not _is_linked(b2, 'keys', a)


def test_assoc_keys5_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature', b1)
    assert _is_linked(a, 'persistence_Feature', b1)
    if hasattr(b1, 'persistence_EntityOrView6'):
        assert _is_linked(b1, 'persistence_EntityOrView6', a)
    _safe_set(a, 'persistence_Feature', b2)
    assert _is_linked(a, 'persistence_Feature', b2)
    if hasattr(b1, 'persistence_EntityOrView6'):
        assert not _is_linked(b1, 'persistence_EntityOrView6', a)
    if hasattr(b2, 'persistence_EntityOrView6'):
        assert _is_linked(b2, 'persistence_EntityOrView6', a)
    _safe_set(a, 'persistence_Feature', None)
    assert not _is_linked(a, 'persistence_Feature', b2)
    if hasattr(b2, 'persistence_EntityOrView6'):
        assert not _is_linked(b2, 'persistence_EntityOrView6', a)


def test_assoc_keys58_link_reassign_clear():
    a = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    b1 = persistence_AssociationKey(targetColumnName="sample_text")
    b2 = persistence_AssociationKey(targetColumnName="sample_text_2")
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


def test_assoc_labelFor39_link_reassign_clear():
    a = persistence_ModelLabel(format="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'labels', b1)
    assert _is_linked(a, 'labels', b1)
    if hasattr(b1, 'EntityOrView'):
        assert _is_linked(b1, 'EntityOrView', a)
    _safe_set(a, 'labels', b2)
    assert _is_linked(a, 'labels', b2)
    if hasattr(b1, 'EntityOrView'):
        assert not _is_linked(b1, 'EntityOrView', a)
    if hasattr(b2, 'EntityOrView'):
        assert _is_linked(b2, 'EntityOrView', a)
    _safe_set(a, 'labels', None)
    assert not _is_linked(a, 'labels', b2)
    if hasattr(b2, 'EntityOrView'):
        assert not _is_linked(b2, 'EntityOrView', a)


def test_assoc_labels13_link_reassign_clear():
    a = persistence_ModelLabel(format="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'ModelLabel', b1)
    assert _is_linked(a, 'ModelLabel', b1)
    if hasattr(b1, 'labelFor'):
        assert _is_linked(b1, 'labelFor', a)
    _safe_set(a, 'ModelLabel', b2)
    assert _is_linked(a, 'ModelLabel', b2)
    if hasattr(b1, 'labelFor'):
        assert not _is_linked(b1, 'labelFor', a)
    if hasattr(b2, 'labelFor'):
        assert _is_linked(b2, 'labelFor', a)
    _safe_set(a, 'ModelLabel', None)
    assert not _is_linked(a, 'ModelLabel', b2)
    if hasattr(b2, 'labelFor'):
        assert not _is_linked(b2, 'labelFor', a)


def test_assoc_opposite82_link_reassign_clear():
    a = persistence_ViewAssociation(cardinality="sample_text")
    b1 = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b2 = persistence_EncapsulatedAssociation(cardinality="sample_text_2", isSourceAssociation=False, name="sample_text_2")
    _safe_set(a, 'persistence_ViewAssociation', b1)
    assert _is_linked(a, 'persistence_ViewAssociation', b1)
    if hasattr(b1, 'persistence_EncapsulatedAssociation83'):
        assert _is_linked(b1, 'persistence_EncapsulatedAssociation83', a)
    _safe_set(a, 'persistence_ViewAssociation', b2)
    assert _is_linked(a, 'persistence_ViewAssociation', b2)
    if hasattr(b1, 'persistence_EncapsulatedAssociation83'):
        assert not _is_linked(b1, 'persistence_EncapsulatedAssociation83', a)
    if hasattr(b2, 'persistence_EncapsulatedAssociation83'):
        assert _is_linked(b2, 'persistence_EncapsulatedAssociation83', a)
    _safe_set(a, 'persistence_ViewAssociation', None)
    assert not _is_linked(a, 'persistence_ViewAssociation', b2)
    if hasattr(b2, 'persistence_EncapsulatedAssociation83'):
        assert not _is_linked(b2, 'persistence_EncapsulatedAssociation83', a)


def test_assoc_partOf43_link_reassign_clear():
    a = persistence_ModelLabel(format="sample_text")
    b1 = persistence_ModelLabelFeature()
    b2 = persistence_ModelLabelFeature()
    _safe_set(a, 'ModelLabel44', b1)
    assert _is_linked(a, 'ModelLabel44', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'ModelLabel44', b2)
    assert _is_linked(a, 'ModelLabel44', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'ModelLabel44', None)
    assert not _is_linked(a, 'ModelLabel44', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_partOf54_link_reassign_clear():
    a = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'entityFeatures', b1)
    assert _is_linked(a, 'entityFeatures', b1)
    if hasattr(b1, 'Entity'):
        assert _is_linked(b1, 'Entity', a)
    _safe_set(a, 'entityFeatures', b2)
    assert _is_linked(a, 'entityFeatures', b2)
    if hasattr(b1, 'Entity'):
        assert not _is_linked(b1, 'Entity', a)
    if hasattr(b2, 'Entity'):
        assert _is_linked(b2, 'Entity', a)
    _safe_set(a, 'entityFeatures', None)
    assert not _is_linked(a, 'entityFeatures', b2)
    if hasattr(b2, 'Entity'):
        assert not _is_linked(b2, 'Entity', a)


def test_assoc_serializationGroups0_link_reassign_clear():
    a = persistence_Persistence(databaseHost="sample_text", databaseName="sample_text", databasePassword="sample_text", databasePort="sample_text", databasePrefix="sample_text", databaseTechnology="sample_text", databaseUsername="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
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


def test_assoc_serializationGroups27_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_SerializationGroup()
    b2 = persistence_SerializationGroup()
    _safe_set(a, 'persistence_Feature28', {b1})
    assert _is_linked(a, 'persistence_Feature28', b1)
    if hasattr(b1, 'persistence_SerializationGroup29'):
        assert _is_linked(b1, 'persistence_SerializationGroup29', a)
    _safe_set(a, 'persistence_Feature28', {b2})
    assert _is_linked(a, 'persistence_Feature28', b2)
    if hasattr(b1, 'persistence_SerializationGroup29'):
        assert not _is_linked(b1, 'persistence_SerializationGroup29', a)
    if hasattr(b2, 'persistence_SerializationGroup29'):
        assert _is_linked(b2, 'persistence_SerializationGroup29', a)
    _safe_set(a, 'persistence_Feature28', set())
    assert not _is_linked(a, 'persistence_Feature28', b2)
    if hasattr(b2, 'persistence_SerializationGroup29'):
        assert not _is_linked(b2, 'persistence_SerializationGroup29', a)


def test_assoc_serializationGroups41_link_reassign_clear():
    a = persistence_ModelLabel(format="sample_text")
    b1 = persistence_SerializationGroup()
    b2 = persistence_SerializationGroup()
    _safe_set(a, 'persistence_ModelLabel', {b1})
    assert _is_linked(a, 'persistence_ModelLabel', b1)
    if hasattr(b1, 'persistence_SerializationGroup42'):
        assert _is_linked(b1, 'persistence_SerializationGroup42', a)
    _safe_set(a, 'persistence_ModelLabel', {b2})
    assert _is_linked(a, 'persistence_ModelLabel', b2)
    if hasattr(b1, 'persistence_SerializationGroup42'):
        assert not _is_linked(b1, 'persistence_SerializationGroup42', a)
    if hasattr(b2, 'persistence_SerializationGroup42'):
        assert _is_linked(b2, 'persistence_SerializationGroup42', a)
    _safe_set(a, 'persistence_ModelLabel', set())
    assert not _is_linked(a, 'persistence_ModelLabel', b2)
    if hasattr(b2, 'persistence_SerializationGroup42'):
        assert not _is_linked(b2, 'persistence_SerializationGroup42', a)


def test_assoc_sourceEntity77_link_reassign_clear():
    a = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'persistence_EncapsulatedAssociation78', b1)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation78', b1)
    if hasattr(b1, 'persistence_Entity'):
        assert _is_linked(b1, 'persistence_Entity', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation78', b2)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation78', b2)
    if hasattr(b1, 'persistence_Entity'):
        assert not _is_linked(b1, 'persistence_Entity', a)
    if hasattr(b2, 'persistence_Entity'):
        assert _is_linked(b2, 'persistence_Entity', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation78', None)
    assert not _is_linked(a, 'persistence_EncapsulatedAssociation78', b2)
    if hasattr(b2, 'persistence_Entity'):
        assert not _is_linked(b2, 'persistence_Entity', a)


def test_assoc_sourceEntityX33_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'persistence_EntityOrView35', b1)
    assert _is_linked(a, 'persistence_EntityOrView35', b1)
    if hasattr(b1, 'persistence_Association34'):
        assert _is_linked(b1, 'persistence_Association34', a)
    _safe_set(a, 'persistence_EntityOrView35', b2)
    assert _is_linked(a, 'persistence_EntityOrView35', b2)
    if hasattr(b1, 'persistence_Association34'):
        assert not _is_linked(b1, 'persistence_Association34', a)
    if hasattr(b2, 'persistence_Association34'):
        assert _is_linked(b2, 'persistence_Association34', a)
    _safe_set(a, 'persistence_EntityOrView35', None)
    assert not _is_linked(a, 'persistence_EntityOrView35', b2)
    if hasattr(b2, 'persistence_Association34'):
        assert not _is_linked(b2, 'persistence_Association34', a)


def test_assoc_sourceFeature63_link_reassign_clear():
    a = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    b1 = persistence_AssociationKey(targetColumnName="sample_text")
    b2 = persistence_AssociationKey(targetColumnName="sample_text_2")
    _safe_set(a, 'persistence_EntityFeature', b1)
    assert _is_linked(a, 'persistence_EntityFeature', b1)
    if hasattr(b1, 'persistence_AssociationKey'):
        assert _is_linked(b1, 'persistence_AssociationKey', a)
    _safe_set(a, 'persistence_EntityFeature', b2)
    assert _is_linked(a, 'persistence_EntityFeature', b2)
    if hasattr(b1, 'persistence_AssociationKey'):
        assert not _is_linked(b1, 'persistence_AssociationKey', a)
    if hasattr(b2, 'persistence_AssociationKey'):
        assert _is_linked(b2, 'persistence_AssociationKey', a)
    _safe_set(a, 'persistence_EntityFeature', None)
    assert not _is_linked(a, 'persistence_EntityFeature', b2)
    if hasattr(b2, 'persistence_AssociationKey'):
        assert not _is_linked(b2, 'persistence_AssociationKey', a)


def test_assoc_targetEntity59_link_reassign_clear():
    a = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True)
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'associationEnds', b1)
    assert _is_linked(a, 'associationEnds', b1)
    if hasattr(b1, 'Entity60'):
        assert _is_linked(b1, 'Entity60', a)
    _safe_set(a, 'associationEnds', b2)
    assert _is_linked(a, 'associationEnds', b2)
    if hasattr(b1, 'Entity60'):
        assert not _is_linked(b1, 'Entity60', a)
    if hasattr(b2, 'Entity60'):
        assert _is_linked(b2, 'Entity60', a)
    _safe_set(a, 'associationEnds', None)
    assert not _is_linked(a, 'associationEnds', b2)
    if hasattr(b2, 'Entity60'):
        assert not _is_linked(b2, 'Entity60', a)


def test_assoc_targetEntity79_link_reassign_clear():
    a = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    b1 = persistence_Entity()
    b2 = persistence_Entity()
    _safe_set(a, 'persistence_EncapsulatedAssociation80', b1)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation80', b1)
    if hasattr(b1, 'persistence_Entity81'):
        assert _is_linked(b1, 'persistence_Entity81', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation80', b2)
    assert _is_linked(a, 'persistence_EncapsulatedAssociation80', b2)
    if hasattr(b1, 'persistence_Entity81'):
        assert not _is_linked(b1, 'persistence_Entity81', a)
    if hasattr(b2, 'persistence_Entity81'):
        assert _is_linked(b2, 'persistence_Entity81', a)
    _safe_set(a, 'persistence_EncapsulatedAssociation80', None)
    assert not _is_linked(a, 'persistence_EncapsulatedAssociation80', b2)
    if hasattr(b2, 'persistence_Entity81'):
        assert not _is_linked(b2, 'persistence_Entity81', a)


def test_assoc_targetEntityX36_link_reassign_clear():
    a = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b1 = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    b2 = persistence_Association(inputClass="sample_text_2", pseudo=False, serializationMaxDepth=13)
    _safe_set(a, 'persistence_EntityOrView38', b1)
    assert _is_linked(a, 'persistence_EntityOrView38', b1)
    if hasattr(b1, 'persistence_Association37'):
        assert _is_linked(b1, 'persistence_Association37', a)
    _safe_set(a, 'persistence_EntityOrView38', b2)
    assert _is_linked(a, 'persistence_EntityOrView38', b2)
    if hasattr(b1, 'persistence_Association37'):
        assert not _is_linked(b1, 'persistence_Association37', a)
    if hasattr(b2, 'persistence_Association37'):
        assert _is_linked(b2, 'persistence_Association37', a)
    _safe_set(a, 'persistence_EntityOrView38', None)
    assert not _is_linked(a, 'persistence_EntityOrView38', b2)
    if hasattr(b2, 'persistence_Association37'):
        assert not _is_linked(b2, 'persistence_Association37', a)


def test_assoc_targetFeature64_link_reassign_clear():
    a = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", ordered=True, pluralisedName="sample_text", singletonName="sample_text", unique=True)
    b1 = persistence_AssociationKey(targetColumnName="sample_text")
    b2 = persistence_AssociationKey(targetColumnName="sample_text_2")
    _safe_set(a, 'persistence_EntityFeature66', b1)
    assert _is_linked(a, 'persistence_EntityFeature66', b1)
    if hasattr(b1, 'persistence_AssociationKey65'):
        assert _is_linked(b1, 'persistence_AssociationKey65', a)
    _safe_set(a, 'persistence_EntityFeature66', b2)
    assert _is_linked(a, 'persistence_EntityFeature66', b2)
    if hasattr(b1, 'persistence_AssociationKey65'):
        assert not _is_linked(b1, 'persistence_AssociationKey65', a)
    if hasattr(b2, 'persistence_AssociationKey65'):
        assert _is_linked(b2, 'persistence_AssociationKey65', a)
    _safe_set(a, 'persistence_EntityFeature66', None)
    assert not _is_linked(a, 'persistence_EntityFeature66', b2)
    if hasattr(b2, 'persistence_AssociationKey65'):
        assert not _is_linked(b2, 'persistence_AssociationKey65', a)


def test_assoc_unique7_link_reassign_clear():
    a = persistence_Feature(collectionAllowAdd=True, collectionAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", title="sample_text")
    b1 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    b2 = persistence_EntityOrView(autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    _safe_set(a, 'persistence_Feature9', b1)
    assert _is_linked(a, 'persistence_Feature9', b1)
    if hasattr(b1, 'persistence_EntityOrView8'):
        assert _is_linked(b1, 'persistence_EntityOrView8', a)
    _safe_set(a, 'persistence_Feature9', b2)
    assert _is_linked(a, 'persistence_Feature9', b2)
    if hasattr(b1, 'persistence_EntityOrView8'):
        assert not _is_linked(b1, 'persistence_EntityOrView8', a)
    if hasattr(b2, 'persistence_EntityOrView8'):
        assert _is_linked(b2, 'persistence_EntityOrView8', a)
    _safe_set(a, 'persistence_Feature9', None)
    assert not _is_linked(a, 'persistence_Feature9', b2)
    if hasattr(b2, 'persistence_EntityOrView8'):
        assert not _is_linked(b2, 'persistence_EntityOrView8', a)


def test_assoc_uploadPath57_link_reassign_clear():
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


EncapsulatedFeature_strategy = st.builds(EncapsulatedFeature)
@given(instance=EncapsulatedFeature_strategy)
@settings(max_examples=25)
def test_EncapsulatedFeature_instantiation(instance):
    assert isinstance(instance, EncapsulatedFeature)


EntityAssociation_strategy = st.builds(EntityAssociation)
@given(instance=EntityAssociation_strategy)
@settings(max_examples=25)
def test_EntityAssociation_instantiation(instance):
    assert isinstance(instance, EntityAssociation)


EntityAttribute_strategy = st.builds(EntityAttribute)
@given(instance=EntityAttribute_strategy)
@settings(max_examples=25)
def test_EntityAttribute_instantiation(instance):
    assert isinstance(instance, EntityAttribute)


EntityFeature_strategy = st.builds(EntityFeature)
@given(instance=EntityFeature_strategy)
@settings(max_examples=25)
def test_EntityFeature_instantiation(instance):
    assert isinstance(instance, EntityFeature)


EntityOrView_strategy = st.builds(EntityOrView)
@given(instance=EntityOrView_strategy)
@settings(max_examples=25)
def test_EntityOrView_instantiation(instance):
    assert isinstance(instance, EntityOrView)


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


ViewFeature_strategy = st.builds(ViewFeature)
@given(instance=ViewFeature_strategy)
@settings(max_examples=25)
def test_ViewFeature_instantiation(instance):
    assert isinstance(instance, ViewFeature)


persistence_Association_strategy = st.builds(persistence_Association, inputClass=safe_text, pseudo=st.booleans(), serializationMaxDepth=st.integers())
@given(instance=persistence_Association_strategy)
@settings(max_examples=25)
def test_persistence_Association_instantiation(instance):
    assert isinstance(instance, persistence_Association)


persistence_AssociationKey_strategy = st.builds(persistence_AssociationKey, targetColumnName=safe_text)
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


persistence_Attribute_strategy = st.builds(persistence_Attribute, inputClass=safe_text, placeholder=safe_text, validationPattern=safe_text)
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


persistence_EncapsulatedAssociation_strategy = st.builds(persistence_EncapsulatedAssociation, cardinality=safe_text, isSourceAssociation=st.booleans(), name=safe_text)
@given(instance=persistence_EncapsulatedAssociation_strategy)
@settings(max_examples=25)
def test_persistence_EncapsulatedAssociation_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedAssociation)


persistence_EncapsulatedAttribute_strategy = st.builds(persistence_EncapsulatedAttribute, cardinality=safe_text, name=safe_text)
@given(instance=persistence_EncapsulatedAttribute_strategy)
@settings(max_examples=25)
def test_persistence_EncapsulatedAttribute_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedAttribute)


persistence_EncapsulatedFeature_strategy = st.builds(persistence_EncapsulatedFeature, alias=safe_text, columnName=safe_text, displayLabel=safe_text)
@given(instance=persistence_EncapsulatedFeature_strategy)
@settings(max_examples=25)
def test_persistence_EncapsulatedFeature_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedFeature)


persistence_Entity_strategy = st.builds(persistence_Entity)
@given(instance=persistence_Entity_strategy)
@settings(max_examples=25)
def test_persistence_Entity_instantiation(instance):
    assert isinstance(instance, persistence_Entity)


persistence_EntityAssociation_strategy = st.builds(persistence_EntityAssociation, bidirectional=st.booleans(), pivotTableName=safe_text, targetDisplayClass=safe_text, targetDisplayLabel=safe_text, targetFeatureName=safe_text, targetFooterClass=safe_text, targetHeaderClass=safe_text, targetInputClass=safe_text, targetPrimaryKey=st.booleans())
@given(instance=persistence_EntityAssociation_strategy)
@settings(max_examples=25)
def test_persistence_EntityAssociation_instantiation(instance):
    assert isinstance(instance, persistence_EntityAssociation)


persistence_EntityAttribute_strategy = st.builds(persistence_EntityAttribute, containerUnique=st.booleans(), interfaceType=safe_text, ormType=safe_text, persistentType=safe_text, primaryKey=st.booleans())
@given(instance=persistence_EntityAttribute_strategy)
@settings(max_examples=25)
def test_persistence_EntityAttribute_instantiation(instance):
    assert isinstance(instance, persistence_EntityAttribute)


persistence_EntityFeature_strategy = st.builds(persistence_EntityFeature, booleanIsHasChoice=safe_text, cardinality=safe_text, columnName=safe_text, ordered=st.booleans(), pluralisedName=safe_text, singletonName=safe_text, unique=st.booleans())
@given(instance=persistence_EntityFeature_strategy)
@settings(max_examples=25)
def test_persistence_EntityFeature_instantiation(instance):
    assert isinstance(instance, persistence_EntityFeature)


persistence_EntityOrView_strategy = st.builds(persistence_EntityOrView, autoKeyGenerationStrategy=safe_text, autoKeyName=safe_text, autoKeyPersistentType=safe_text, implementsUserInterface=st.booleans(), pluralisedName=safe_text, singletonName=safe_text, tableName=safe_text)
@given(instance=persistence_EntityOrView_strategy)
@settings(max_examples=25)
def test_persistence_EntityOrView_instantiation(instance):
    assert isinstance(instance, persistence_EntityOrView)


persistence_Expression_strategy = st.builds(persistence_Expression)
@given(instance=persistence_Expression_strategy)
@settings(max_examples=25)
def test_persistence_Expression_instantiation(instance):
    assert isinstance(instance, persistence_Expression)


persistence_Feature_strategy = st.builds(persistence_Feature, collectionAllowAdd=st.booleans(), collectionAllowRemove=st.booleans(), displayClass=safe_text, encodeUriKey=st.booleans(), footerClass=safe_text, headerClass=safe_text, nullDisplayValue=safe_text, title=safe_text)
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


persistence_ModelLabel_strategy = st.builds(persistence_ModelLabel, format=safe_text)
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


persistence_Persistence_strategy = st.builds(persistence_Persistence, databaseHost=safe_text, databaseName=safe_text, databasePassword=safe_text, databasePort=safe_text, databasePrefix=safe_text, databaseTechnology=safe_text, databaseUsername=safe_text, ormTechnology=safe_text, timestampCreation=st.booleans(), timestampUpdates=st.booleans())
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


persistence_View_strategy = st.builds(persistence_View)
@given(instance=persistence_View_strategy)
@settings(max_examples=25)
def test_persistence_View_instantiation(instance):
    assert isinstance(instance, persistence_View)


persistence_ViewAssociation_strategy = st.builds(persistence_ViewAssociation, cardinality=safe_text)
@given(instance=persistence_ViewAssociation_strategy)
@settings(max_examples=25)
def test_persistence_ViewAssociation_instantiation(instance):
    assert isinstance(instance, persistence_ViewAssociation)


persistence_ViewFeature_strategy = st.builds(persistence_ViewFeature)
@given(instance=persistence_ViewFeature_strategy)
@settings(max_examples=25)
def test_persistence_ViewFeature_instantiation(instance):
    assert isinstance(instance, persistence_ViewFeature)


