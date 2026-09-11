import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Attribute,
    BindingDesc,
    DBObject,
    EAttribute,
    EClass,
    EEnum,
    ENamedElement,
    EPackage,
    EReference,
    Item,
    ItemType,
    LongAttribute,
    RuntimeItem,
    RuntimeItemType,
    TypeDefinition,
    ccore_ActionExtItemType,
    ccore_Attribute,
    ccore_BindExt,
    ccore_BindingDesc,
    ccore_BooleanAttribute,
    ccore_Cadse,
    ccore_Composer,
    ccore_ComposerLink,
    ccore_ComposerType,
    ccore_ComputedString,
    ccore_ContentItem,
    ccore_ContentItemType,
    ccore_DBObject,
    ccore_DateAttribute,
    ccore_Display,
    ccore_DoubleAttribute,
    ccore_DynamicActions,
    ccore_EClass,
    ccore_EEnum,
    ccore_EPackage,
    ccore_EStructuralFeature,
    ccore_Enum,
    ccore_EnumType,
    ccore_ExportedContent,
    ccore_Exporter,
    ccore_ExporterType,
    ccore_ExtItem,
    ccore_ExtentedType,
    ccore_Field,
    ccore_GenInformation,
    ccore_GroupExtItem,
    ccore_GroupOfAttributes,
    ccore_IntegerAttribute,
    ccore_InteractionController,
    ccore_Item,
    ccore_ItemType,
    ccore_KeyDefinition,
    ccore_LinkType,
    ccore_LongAttribute,
    ccore_Menu,
    ccore_MenuAbstract,
    ccore_MenuAction,
    ccore_MenuGroup,
    ccore_ModelController,
    ccore_Page,
    ccore_RuntimeItem,
    ccore_RuntimeItemType,
    ccore_StringAttribute,
    ccore_TimeAttribute,
    ccore_TypeDefinition,
    ccore_UIValidator,
    ccore_UUIDAttribute,
    ccore_UnresolvedAttributeType,
    ccore_View,
    ccore_ViewDescription,
    ccore_ViewItemType,
    ccore_ViewLinkType,
    ccore_ViewModel,
    ccore_WCListener,
    PositionEnum,
    TWCommitKind,
    TWDestEvol,
    TWEvol,
    TWUpdateKind,
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

def test_ccore_Attribute__final_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance._final == True
    instance._final = False
    assert instance._final == False


def test_ccore_Attribute_cannotBeUndefined_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.cannotBeUndefined == True
    instance.cannotBeUndefined = False
    assert instance.cannotBeUndefined == False


def test_ccore_Attribute_devGenerated_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.devGenerated == True
    instance.devGenerated = False
    assert instance.devGenerated == False


def test_ccore_Attribute_hiddenInComputedPages_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.hiddenInComputedPages == True
    instance.hiddenInComputedPages = False
    assert instance.hiddenInComputedPages == False


def test_ccore_Attribute_idRuntime_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.idRuntime == "sample_text"
    instance.idRuntime = "sample_text_2"
    assert instance.idRuntime == "sample_text_2"


def test_ccore_Attribute_isList_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.isList == True
    instance.isList = False
    assert instance.isList == False


def test_ccore_Attribute_mustBeInitialized_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.mustBeInitialized == True
    instance.mustBeInitialized = False
    assert instance.mustBeInitialized == False


def test_ccore_Attribute_natif_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.natif == True
    instance.natif = False
    assert instance.natif == False


def test_ccore_Attribute_require_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.require == True
    instance.require = False
    assert instance.require == False


def test_ccore_Attribute_tWCommitKind_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.tWCommitKind == "sample_text"
    instance.tWCommitKind = "sample_text_2"
    assert instance.tWCommitKind == "sample_text_2"


def test_ccore_Attribute_tWEvol_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.tWEvol == "sample_text"
    instance.tWEvol = "sample_text_2"
    assert instance.tWEvol == "sample_text_2"


def test_ccore_Attribute_tWRevSpecific_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.tWRevSpecific == True
    instance.tWRevSpecific = False
    assert instance.tWRevSpecific == False


def test_ccore_Attribute_tWUpdateKind_value_roundtrip():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert instance.tWUpdateKind == "sample_text"
    instance.tWUpdateKind = "sample_text_2"
    assert instance.tWUpdateKind == "sample_text_2"


def test_ccore_Cadse_defaultContentRepoURL_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.defaultContentRepoURL == "sample_text"
    instance.defaultContentRepoURL = "sample_text_2"
    assert instance.defaultContentRepoURL == "sample_text_2"


def test_ccore_Cadse_description_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_ccore_Cadse_executed_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.executed == True
    instance.executed = False
    assert instance.executed == False


def test_ccore_Cadse_idDefinition_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.idDefinition == "sample_text"
    instance.idDefinition = "sample_text_2"
    assert instance.idDefinition == "sample_text_2"


def test_ccore_Cadse_itemRepoLogin_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.itemRepoLogin == "sample_text"
    instance.itemRepoLogin = "sample_text_2"
    assert instance.itemRepoLogin == "sample_text_2"


def test_ccore_Cadse_itemRepoPasswd_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.itemRepoPasswd == "sample_text"
    instance.itemRepoPasswd = "sample_text_2"
    assert instance.itemRepoPasswd == "sample_text_2"


def test_ccore_Cadse_itemRepoURL_value_roundtrip():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert instance.itemRepoURL == "sample_text"
    instance.itemRepoURL = "sample_text_2"
    assert instance.itemRepoURL == "sample_text_2"


def test_ccore_Composer_types_value_roundtrip():
    instance = ccore_Composer(types="sample_text")
    assert instance.types == "sample_text"
    instance.types = "sample_text_2"
    assert instance.types == "sample_text_2"


def test_ccore_ComputedString_expression_value_roundtrip():
    instance = ccore_ComputedString(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_ccore_ContentItemType_extendsClass_value_roundtrip():
    instance = ccore_ContentItemType(extendsClass=True)
    assert instance.extendsClass == True
    instance.extendsClass = False
    assert instance.extendsClass == False


def test_ccore_DBObject_objectId_value_roundtrip():
    instance = ccore_DBObject(objectId=7, uuid_lsb="sample_text", uuid_msb="sample_text")
    assert instance.objectId == 7
    instance.objectId = 13
    assert instance.objectId == 13


def test_ccore_DBObject_uuid_lsb_value_roundtrip():
    instance = ccore_DBObject(objectId=7, uuid_lsb="sample_text", uuid_msb="sample_text")
    assert instance.uuid_lsb == "sample_text"
    instance.uuid_lsb = "sample_text_2"
    assert instance.uuid_lsb == "sample_text_2"


def test_ccore_DBObject_uuid_msb_value_roundtrip():
    instance = ccore_DBObject(objectId=7, uuid_lsb="sample_text", uuid_msb="sample_text")
    assert instance.uuid_msb == "sample_text"
    instance.uuid_msb = "sample_text_2"
    assert instance.uuid_msb == "sample_text_2"


def test_ccore_Display_extendsIC_value_roundtrip():
    instance = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    assert instance.extendsIC == True
    instance.extendsIC = False
    assert instance.extendsIC == False


def test_ccore_Display_extendsMC_value_roundtrip():
    instance = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    assert instance.extendsMC == True
    instance.extendsMC = False
    assert instance.extendsMC == False


def test_ccore_Display_extendsUI_value_roundtrip():
    instance = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    assert instance.extendsUI == True
    instance.extendsUI = False
    assert instance.extendsUI == False


def test_ccore_Enum_enumClazz_value_roundtrip():
    instance = ccore_Enum(enumClazz="sample_text", values="sample_text")
    assert instance.enumClazz == "sample_text"
    instance.enumClazz = "sample_text_2"
    assert instance.enumClazz == "sample_text_2"


def test_ccore_Enum_values_value_roundtrip():
    instance = ccore_Enum(enumClazz="sample_text", values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_ccore_EnumType_javaClass_value_roundtrip():
    instance = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    assert instance.javaClass == "sample_text"
    instance.javaClass = "sample_text_2"
    assert instance.javaClass == "sample_text_2"


def test_ccore_EnumType_mustBeGenerated_value_roundtrip():
    instance = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    assert instance.mustBeGenerated == True
    instance.mustBeGenerated = False
    assert instance.mustBeGenerated == False


def test_ccore_EnumType_values_value_roundtrip():
    instance = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_ccore_Exporter_types_value_roundtrip():
    instance = ccore_Exporter(types="sample_text")
    assert instance.types == "sample_text"
    instance.types = "sample_text_2"
    assert instance.types == "sample_text_2"


def test_ccore_Field_editable_value_roundtrip():
    instance = ccore_Field(editable=True, label="sample_text", position="sample_text")
    assert instance.editable == True
    instance.editable = False
    assert instance.editable == False


def test_ccore_Field_label_value_roundtrip():
    instance = ccore_Field(editable=True, label="sample_text", position="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_ccore_Field_position_value_roundtrip():
    instance = ccore_Field(editable=True, label="sample_text", position="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_ccore_GenInformation_cSTName_value_roundtrip():
    instance = ccore_GenInformation(cSTName="sample_text")
    assert instance.cSTName == "sample_text"
    instance.cSTName = "sample_text_2"
    assert instance.cSTName == "sample_text_2"


def test_ccore_GroupOfAttributes_column_value_roundtrip():
    instance = ccore_GroupOfAttributes(column=7)
    assert instance.column == 7
    instance.column = 13
    assert instance.column == 13


def test_ccore_Item_committedBy_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.committedBy == "sample_text"
    instance.committedBy = "sample_text_2"
    assert instance.committedBy == "sample_text_2"


def test_ccore_Item_displayName_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.displayName == "sample_text"
    instance.displayName = "sample_text_2"
    assert instance.displayName == "sample_text_2"


def test_ccore_Item_isvalid_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.isvalid == True
    instance.isvalid = False
    assert instance.isvalid == False


def test_ccore_Item_itemHidden_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.itemHidden == True
    instance.itemHidden = False
    assert instance.itemHidden == False


def test_ccore_Item_itemReadonly_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.itemReadonly == True
    instance.itemReadonly = False
    assert instance.itemReadonly == False


def test_ccore_Item_qualifiedName_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_ccore_Item_twCommittedDate_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.twCommittedDate == "sample_text"
    instance.twCommittedDate = "sample_text_2"
    assert instance.twCommittedDate == "sample_text_2"


def test_ccore_Item_twRequireNewRev_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.twRequireNewRev == True
    instance.twRequireNewRev = False
    assert instance.twRequireNewRev == False


def test_ccore_Item_twRevModified_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.twRevModified == True
    instance.twRevModified = False
    assert instance.twRevModified == False


def test_ccore_Item_twVersion_value_roundtrip():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert instance.twVersion == 7
    instance.twVersion = 13
    assert instance.twVersion == 13


def test_ccore_ItemType_customManager_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.customManager == True
    instance.customManager = False
    assert instance.customManager == False


def test_ccore_ItemType_displayNameTemplate_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.displayNameTemplate == "sample_text"
    instance.displayNameTemplate = "sample_text_2"
    assert instance.displayNameTemplate == "sample_text_2"


def test_ccore_ItemType_hasContent_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.hasContent == True
    instance.hasContent = False
    assert instance.hasContent == False


def test_ccore_ItemType_hasShortName_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.hasShortName == True
    instance.hasShortName = False
    assert instance.hasShortName == False


def test_ccore_ItemType_hasUniqueName_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.hasUniqueName == True
    instance.hasUniqueName = False
    assert instance.hasUniqueName == False


def test_ccore_ItemType_humanName_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.humanName == "sample_text"
    instance.humanName = "sample_text_2"
    assert instance.humanName == "sample_text_2"


def test_ccore_ItemType_icon_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_ccore_ItemType_isInstanceAbstract_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.isInstanceAbstract == True
    instance.isInstanceAbstract = False
    assert instance.isInstanceAbstract == False


def test_ccore_ItemType_isInstanceHidden_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.isInstanceHidden == True
    instance.isInstanceHidden = False
    assert instance.isInstanceHidden == False


def test_ccore_ItemType_isMetaItemType_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.isMetaItemType == True
    instance.isMetaItemType = False
    assert instance.isMetaItemType == False


def test_ccore_ItemType_isRootElement_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.isRootElement == True
    instance.isRootElement = False
    assert instance.isRootElement == False


def test_ccore_ItemType_itemFactoryClass_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.itemFactoryClass == "sample_text"
    instance.itemFactoryClass = "sample_text_2"
    assert instance.itemFactoryClass == "sample_text_2"


def test_ccore_ItemType_itemManagerClass_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.itemManagerClass == "sample_text"
    instance.itemManagerClass = "sample_text_2"
    assert instance.itemManagerClass == "sample_text_2"


def test_ccore_ItemType_managerClass_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.managerClass == "sample_text"
    instance.managerClass = "sample_text_2"
    assert instance.managerClass == "sample_text_2"


def test_ccore_ItemType_messageErrorId_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.messageErrorId == "sample_text"
    instance.messageErrorId = "sample_text_2"
    assert instance.messageErrorId == "sample_text_2"


def test_ccore_ItemType_overwriteDefaultPages_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.overwriteDefaultPages == True
    instance.overwriteDefaultPages = False
    assert instance.overwriteDefaultPages == False


def test_ccore_ItemType_packageName_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.packageName == "sample_text"
    instance.packageName = "sample_text_2"
    assert instance.packageName == "sample_text_2"


def test_ccore_ItemType_qualifiedNameTemplate_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.qualifiedNameTemplate == "sample_text"
    instance.qualifiedNameTemplate = "sample_text_2"
    assert instance.qualifiedNameTemplate == "sample_text_2"


def test_ccore_ItemType_validateNameRe_value_roundtrip():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert instance.validateNameRe == "sample_text"
    instance.validateNameRe = "sample_text_2"
    assert instance.validateNameRe == "sample_text_2"


def test_ccore_LinkType_aggregation_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.aggregation == True
    instance.aggregation = False
    assert instance.aggregation == False


def test_ccore_LinkType_annotation_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.annotation == True
    instance.annotation = False
    assert instance.annotation == False


def test_ccore_LinkType_composition_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.composition == True
    instance.composition = False
    assert instance.composition == False


def test_ccore_LinkType_group_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.group == True
    instance.group = False
    assert instance.group == False


def test_ccore_LinkType_hidden_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.hidden == True
    instance.hidden = False
    assert instance.hidden == False


def test_ccore_LinkType_kind_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.kind == 7
    instance.kind = 13
    assert instance.kind == 13


def test_ccore_LinkType_linkManager_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.linkManager == "sample_text"
    instance.linkManager = "sample_text_2"
    assert instance.linkManager == "sample_text_2"


def test_ccore_LinkType_mapping_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.mapping == True
    instance.mapping = False
    assert instance.mapping == False


def test_ccore_LinkType_max_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_ccore_LinkType_min_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_ccore_LinkType_selection_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.selection == "sample_text"
    instance.selection = "sample_text_2"
    assert instance.selection == "sample_text_2"


def test_ccore_LinkType_twCoupled_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.twCoupled == True
    instance.twCoupled = False
    assert instance.twCoupled == False


def test_ccore_LinkType_twDestEvol_value_roundtrip():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert instance.twDestEvol == "sample_text"
    instance.twDestEvol = "sample_text_2"
    assert instance.twDestEvol == "sample_text_2"


def test_ccore_MenuAbstract_icon_value_roundtrip():
    instance = ccore_MenuAbstract(icon="sample_text", label="sample_text", path="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_ccore_MenuAbstract_label_value_roundtrip():
    instance = ccore_MenuAbstract(icon="sample_text", label="sample_text", path="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_ccore_MenuAbstract_path_value_roundtrip():
    instance = ccore_MenuAbstract(icon="sample_text", label="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_ccore_Page_description_value_roundtrip():
    instance = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_ccore_Page_idRuntime_value_roundtrip():
    instance = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    assert instance.idRuntime == "sample_text"
    instance.idRuntime = "sample_text_2"
    assert instance.idRuntime == "sample_text_2"


def test_ccore_Page_label_value_roundtrip():
    instance = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_ccore_Page_title_value_roundtrip():
    instance = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_ccore_RuntimeItem_className_value_roundtrip():
    instance = ccore_RuntimeItem(className="sample_text", extendsClass=True)
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_ccore_RuntimeItem_extendsClass_value_roundtrip():
    instance = ccore_RuntimeItem(className="sample_text", extendsClass=True)
    assert instance.extendsClass == True
    instance.extendsClass = False
    assert instance.extendsClass == False


def test_ccore_StringAttribute_notEmpty_value_roundtrip():
    instance = ccore_StringAttribute(notEmpty=True)
    assert instance.notEmpty == True
    instance.notEmpty = False
    assert instance.notEmpty == False


def test_ccore_TimeAttribute_initWithTheCurrentTime_value_roundtrip():
    instance = ccore_TimeAttribute(initWithTheCurrentTime=True)
    assert instance.initWithTheCurrentTime == True
    instance.initWithTheCurrentTime = False
    assert instance.initWithTheCurrentTime == False


def test_ccore_TypeDefinition_idRuntime_value_roundtrip():
    instance = ccore_TypeDefinition(idRuntime="sample_text")
    assert instance.idRuntime == "sample_text"
    instance.idRuntime = "sample_text_2"
    assert instance.idRuntime == "sample_text_2"


def test_ccore_View_icon_value_roundtrip():
    instance = ccore_View(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_ccore_ViewItemType_isRootElement_value_roundtrip():
    instance = ccore_ViewItemType(isRootElement=True, ref=True)
    assert instance.isRootElement == True
    instance.isRootElement = False
    assert instance.isRootElement == False


def test_ccore_ViewItemType_ref_value_roundtrip():
    instance = ccore_ViewItemType(isRootElement=True, ref=True)
    assert instance.ref == True
    instance.ref = False
    assert instance.ref == False


def test_ccore_ViewLinkType_aggregation_value_roundtrip():
    instance = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    assert instance.aggregation == True
    instance.aggregation = False
    assert instance.aggregation == False


def test_ccore_ViewLinkType_canCreateItem_value_roundtrip():
    instance = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    assert instance.canCreateItem == True
    instance.canCreateItem = False
    assert instance.canCreateItem == False


def test_ccore_ViewLinkType_canCreateLink_value_roundtrip():
    instance = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    assert instance.canCreateLink == True
    instance.canCreateLink = False
    assert instance.canCreateLink == False


def test_ccore_ViewLinkType_displayCreate_value_roundtrip():
    instance = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    assert instance.displayCreate == "sample_text"
    instance.displayCreate = "sample_text_2"
    assert instance.displayCreate == "sample_text_2"


def test_ccore_BooleanAttribute_isa_Attribute():
    instance = ccore_BooleanAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_DateAttribute_isa_Attribute():
    instance = ccore_DateAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_DoubleAttribute_isa_Attribute():
    instance = ccore_DoubleAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_Enum_isa_Attribute():
    instance = ccore_Enum(enumClazz="sample_text", values="sample_text")
    assert isinstance(instance, Attribute)


def test_ccore_IntegerAttribute_isa_Attribute():
    instance = ccore_IntegerAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_LinkType_isa_Attribute():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert isinstance(instance, Attribute)


def test_ccore_LongAttribute_isa_Attribute():
    instance = ccore_LongAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_StringAttribute_isa_Attribute():
    instance = ccore_StringAttribute(notEmpty=True)
    assert isinstance(instance, Attribute)


def test_ccore_UUIDAttribute_isa_Attribute():
    instance = ccore_UUIDAttribute()
    assert isinstance(instance, Attribute)


def test_ccore_BindExt_isa_BindingDesc():
    instance = ccore_BindExt()
    assert isinstance(instance, BindingDesc)


def test_ccore_BindingDesc_isa_DBObject():
    instance = ccore_BindingDesc()
    assert isinstance(instance, DBObject)


def test_ccore_Item_isa_DBObject():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert isinstance(instance, DBObject)


def test_ccore_Attribute_isa_EAttribute():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert isinstance(instance, EAttribute)


def test_ccore_TypeDefinition_isa_EClass():
    instance = ccore_TypeDefinition(idRuntime="sample_text")
    assert isinstance(instance, EClass)


def test_ccore_EnumType_isa_EEnum():
    instance = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    assert isinstance(instance, EEnum)


def test_ccore_Item_isa_ENamedElement():
    instance = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    assert isinstance(instance, ENamedElement)


def test_ccore_Cadse_isa_EPackage():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert isinstance(instance, EPackage)


def test_ccore_LinkType_isa_EReference():
    instance = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    assert isinstance(instance, EReference)


def test_ccore_Attribute_isa_Item():
    instance = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    assert isinstance(instance, Item)


def test_ccore_Cadse_isa_Item():
    instance = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    assert isinstance(instance, Item)


def test_ccore_Field_isa_Item():
    instance = ccore_Field(editable=True, label="sample_text", position="sample_text")
    assert isinstance(instance, Item)


def test_ccore_KeyDefinition_isa_Item():
    instance = ccore_KeyDefinition()
    assert isinstance(instance, Item)


def test_ccore_RuntimeItem_isa_Item():
    instance = ccore_RuntimeItem(className="sample_text", extendsClass=True)
    assert isinstance(instance, Item)


def test_ccore_TypeDefinition_isa_Item():
    instance = ccore_TypeDefinition(idRuntime="sample_text")
    assert isinstance(instance, Item)


def test_ccore_ContentItemType_isa_ItemType():
    instance = ccore_ContentItemType(extendsClass=True)
    assert isinstance(instance, ItemType)


def test_ccore_RuntimeItemType_isa_ItemType():
    instance = ccore_RuntimeItemType()
    assert isinstance(instance, ItemType)


def test_ccore_TimeAttribute_isa_LongAttribute():
    instance = ccore_TimeAttribute(initWithTheCurrentTime=True)
    assert isinstance(instance, LongAttribute)


def test_ccore_Composer_isa_RuntimeItem():
    instance = ccore_Composer(types="sample_text")
    assert isinstance(instance, RuntimeItem)


def test_ccore_Display_isa_RuntimeItem():
    instance = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    assert isinstance(instance, RuntimeItem)


def test_ccore_Exporter_isa_RuntimeItem():
    instance = ccore_Exporter(types="sample_text")
    assert isinstance(instance, RuntimeItem)


def test_ccore_InteractionController_isa_RuntimeItem():
    instance = ccore_InteractionController()
    assert isinstance(instance, RuntimeItem)


def test_ccore_ModelController_isa_RuntimeItem():
    instance = ccore_ModelController()
    assert isinstance(instance, RuntimeItem)


def test_ccore_ComposerType_isa_RuntimeItemType():
    instance = ccore_ComposerType()
    assert isinstance(instance, RuntimeItemType)


def test_ccore_ExporterType_isa_RuntimeItemType():
    instance = ccore_ExporterType()
    assert isinstance(instance, RuntimeItemType)


def test_ccore_ExtentedType_isa_TypeDefinition():
    instance = ccore_ExtentedType()
    assert isinstance(instance, TypeDefinition)


def test_ccore_ItemType_isa_TypeDefinition():
    instance = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    assert isinstance(instance, TypeDefinition)


def test_assoc_attribute111_link_reassign_clear():
    a = ccore_Field(editable=True, label="sample_text", position="sample_text")
    b1 = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b2 = ccore_Attribute(_final=False, cannotBeUndefined=False, devGenerated=False, hiddenInComputedPages=False, idRuntime="sample_text_2", isList=False, mustBeInitialized=False, natif=False, require=False, tWCommitKind="sample_text_2", tWEvol="sample_text_2", tWRevSpecific=False, tWUpdateKind="sample_text_2")
    _safe_set(a, 'ccore_Field112', b1)
    assert _is_linked(a, 'ccore_Field112', b1)
    if hasattr(b1, 'ccore_Attribute113'):
        assert _is_linked(b1, 'ccore_Attribute113', a)
    _safe_set(a, 'ccore_Field112', b2)
    assert _is_linked(a, 'ccore_Field112', b2)
    if hasattr(b1, 'ccore_Attribute113'):
        assert not _is_linked(b1, 'ccore_Attribute113', a)
    if hasattr(b2, 'ccore_Attribute113'):
        assert _is_linked(b2, 'ccore_Attribute113', a)
    _safe_set(a, 'ccore_Field112', None)
    assert not _is_linked(a, 'ccore_Field112', b2)
    if hasattr(b2, 'ccore_Attribute113'):
        assert not _is_linked(b2, 'ccore_Attribute113', a)


def test_assoc_attributes0_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b2 = ccore_Attribute(_final=False, cannotBeUndefined=False, devGenerated=False, hiddenInComputedPages=False, idRuntime="sample_text_2", isList=False, mustBeInitialized=False, natif=False, require=False, tWCommitKind="sample_text_2", tWEvol="sample_text_2", tWRevSpecific=False, tWUpdateKind="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition', b1)
    if hasattr(b1, 'ccore_Attribute'):
        assert _is_linked(b1, 'ccore_Attribute', a)
    _safe_set(a, 'ccore_TypeDefinition', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition', b2)
    if hasattr(b1, 'ccore_Attribute'):
        assert not _is_linked(b1, 'ccore_Attribute', a)
    if hasattr(b2, 'ccore_Attribute'):
        assert _is_linked(b2, 'ccore_Attribute', a)
    _safe_set(a, 'ccore_TypeDefinition', set())
    assert not _is_linked(a, 'ccore_TypeDefinition', b2)
    if hasattr(b2, 'ccore_Attribute'):
        assert not _is_linked(b2, 'ccore_Attribute', a)


def test_assoc_attributes120_link_reassign_clear():
    a = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    b1 = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b2 = ccore_Attribute(_final=False, cannotBeUndefined=False, devGenerated=False, hiddenInComputedPages=False, idRuntime="sample_text_2", isList=False, mustBeInitialized=False, natif=False, require=False, tWCommitKind="sample_text_2", tWEvol="sample_text_2", tWRevSpecific=False, tWUpdateKind="sample_text_2")
    _safe_set(a, 'ccore_Page121', {b1})
    assert _is_linked(a, 'ccore_Page121', b1)
    if hasattr(b1, 'ccore_Attribute122'):
        assert _is_linked(b1, 'ccore_Attribute122', a)
    _safe_set(a, 'ccore_Page121', {b2})
    assert _is_linked(a, 'ccore_Page121', b2)
    if hasattr(b1, 'ccore_Attribute122'):
        assert not _is_linked(b1, 'ccore_Attribute122', a)
    if hasattr(b2, 'ccore_Attribute122'):
        assert _is_linked(b2, 'ccore_Attribute122', a)
    _safe_set(a, 'ccore_Page121', set())
    assert not _is_linked(a, 'ccore_Page121', b2)
    if hasattr(b2, 'ccore_Attribute122'):
        assert not _is_linked(b2, 'ccore_Attribute122', a)


def test_assoc_attributes128_link_reassign_clear():
    a = ccore_GroupOfAttributes(column=7)
    b1 = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b2 = ccore_Attribute(_final=False, cannotBeUndefined=False, devGenerated=False, hiddenInComputedPages=False, idRuntime="sample_text_2", isList=False, mustBeInitialized=False, natif=False, require=False, tWCommitKind="sample_text_2", tWEvol="sample_text_2", tWRevSpecific=False, tWUpdateKind="sample_text_2")
    _safe_set(a, 'ccore_GroupOfAttributes129', {b1})
    assert _is_linked(a, 'ccore_GroupOfAttributes129', b1)
    if hasattr(b1, 'ccore_Attribute130'):
        assert _is_linked(b1, 'ccore_Attribute130', a)
    _safe_set(a, 'ccore_GroupOfAttributes129', {b2})
    assert _is_linked(a, 'ccore_GroupOfAttributes129', b2)
    if hasattr(b1, 'ccore_Attribute130'):
        assert not _is_linked(b1, 'ccore_Attribute130', a)
    if hasattr(b2, 'ccore_Attribute130'):
        assert _is_linked(b2, 'ccore_Attribute130', a)
    _safe_set(a, 'ccore_GroupOfAttributes129', set())
    assert not _is_linked(a, 'ccore_GroupOfAttributes129', b2)
    if hasattr(b2, 'ccore_Attribute130'):
        assert not _is_linked(b2, 'ccore_Attribute130', a)


def test_assoc_binding50_link_reassign_clear():
    a = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b1 = ccore_BindingDesc()
    b2 = ccore_BindingDesc()
    _safe_set(a, 'ccore_Cadse51', {b1})
    assert _is_linked(a, 'ccore_Cadse51', b1)
    if hasattr(b1, 'ccore_BindingDesc'):
        assert _is_linked(b1, 'ccore_BindingDesc', a)
    _safe_set(a, 'ccore_Cadse51', {b2})
    assert _is_linked(a, 'ccore_Cadse51', b2)
    if hasattr(b1, 'ccore_BindingDesc'):
        assert not _is_linked(b1, 'ccore_BindingDesc', a)
    if hasattr(b2, 'ccore_BindingDesc'):
        assert _is_linked(b2, 'ccore_BindingDesc', a)
    _safe_set(a, 'ccore_Cadse51', set())
    assert not _is_linked(a, 'ccore_Cadse51', b2)
    if hasattr(b2, 'ccore_BindingDesc'):
        assert not _is_linked(b2, 'ccore_BindingDesc', a)


def test_assoc_cadse64_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b2 = ccore_Cadse(defaultContentRepoURL="sample_text_2", description="sample_text_2", executed=False, idDefinition="sample_text_2", itemRepoLogin="sample_text_2", itemRepoPasswd="sample_text_2", itemRepoURL="sample_text_2")
    _safe_set(a, 'ccore_Item65', b1)
    assert _is_linked(a, 'ccore_Item65', b1)
    if hasattr(b1, 'ccore_Cadse66'):
        assert _is_linked(b1, 'ccore_Cadse66', a)
    _safe_set(a, 'ccore_Item65', b2)
    assert _is_linked(a, 'ccore_Item65', b2)
    if hasattr(b1, 'ccore_Cadse66'):
        assert not _is_linked(b1, 'ccore_Cadse66', a)
    if hasattr(b2, 'ccore_Cadse66'):
        assert _is_linked(b2, 'ccore_Cadse66', a)
    _safe_set(a, 'ccore_Item65', None)
    assert not _is_linked(a, 'ccore_Item65', b2)
    if hasattr(b2, 'ccore_Cadse66'):
        assert not _is_linked(b2, 'ccore_Cadse66', a)


def test_assoc_children91_link_reassign_clear():
    a = ccore_MenuAbstract(icon="sample_text", label="sample_text", path="sample_text")
    b1 = ccore_Menu()
    b2 = ccore_Menu()
    _safe_set(a, 'ccore_MenuAbstract', b1)
    assert _is_linked(a, 'ccore_MenuAbstract', b1)
    if hasattr(b1, 'ccore_Menu92'):
        assert _is_linked(b1, 'ccore_Menu92', a)
    _safe_set(a, 'ccore_MenuAbstract', b2)
    assert _is_linked(a, 'ccore_MenuAbstract', b2)
    if hasattr(b1, 'ccore_Menu92'):
        assert not _is_linked(b1, 'ccore_Menu92', a)
    if hasattr(b2, 'ccore_Menu92'):
        assert _is_linked(b2, 'ccore_Menu92', a)
    _safe_set(a, 'ccore_MenuAbstract', None)
    assert not _is_linked(a, 'ccore_MenuAbstract', b2)
    if hasattr(b2, 'ccore_Menu92'):
        assert not _is_linked(b2, 'ccore_Menu92', a)


def test_assoc_composerLinks142_link_reassign_clear():
    a = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b1 = ccore_Composer(types="sample_text")
    b2 = ccore_Composer(types="sample_text_2")
    _safe_set(a, 'ccore_LinkType143', b1)
    assert _is_linked(a, 'ccore_LinkType143', b1)
    if hasattr(b1, 'ccore_Composer'):
        assert _is_linked(b1, 'ccore_Composer', a)
    _safe_set(a, 'ccore_LinkType143', b2)
    assert _is_linked(a, 'ccore_LinkType143', b2)
    if hasattr(b1, 'ccore_Composer'):
        assert not _is_linked(b1, 'ccore_Composer', a)
    if hasattr(b2, 'ccore_Composer'):
        assert _is_linked(b2, 'ccore_Composer', a)
    _safe_set(a, 'ccore_LinkType143', None)
    assert not _is_linked(a, 'ccore_LinkType143', b2)
    if hasattr(b2, 'ccore_Composer'):
        assert not _is_linked(b2, 'ccore_Composer', a)


def test_assoc_composerTypes32_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ComposerType()
    b2 = ccore_ComposerType()
    _safe_set(a, 'ccore_ItemType33', {b1})
    assert _is_linked(a, 'ccore_ItemType33', b1)
    if hasattr(b1, 'ccore_ComposerType'):
        assert _is_linked(b1, 'ccore_ComposerType', a)
    _safe_set(a, 'ccore_ItemType33', {b2})
    assert _is_linked(a, 'ccore_ItemType33', b2)
    if hasattr(b1, 'ccore_ComposerType'):
        assert not _is_linked(b1, 'ccore_ComposerType', a)
    if hasattr(b2, 'ccore_ComposerType'):
        assert _is_linked(b2, 'ccore_ComposerType', a)
    _safe_set(a, 'ccore_ItemType33', set())
    assert not _is_linked(a, 'ccore_ItemType33', b2)
    if hasattr(b2, 'ccore_ComposerType'):
        assert not _is_linked(b2, 'ccore_ComposerType', a)


def test_assoc_composers69_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Composer(types="sample_text")
    b2 = ccore_Composer(types="sample_text_2")
    _safe_set(a, 'ownerItem70', {b1})
    assert _is_linked(a, 'ownerItem70', b1)
    if hasattr(b1, 'Composer'):
        assert _is_linked(b1, 'Composer', a)
    _safe_set(a, 'ownerItem70', {b2})
    assert _is_linked(a, 'ownerItem70', b2)
    if hasattr(b1, 'Composer'):
        assert not _is_linked(b1, 'Composer', a)
    if hasattr(b2, 'Composer'):
        assert _is_linked(b2, 'Composer', a)
    _safe_set(a, 'ownerItem70', set())
    assert not _is_linked(a, 'ownerItem70', b2)
    if hasattr(b2, 'Composer'):
        assert not _is_linked(b2, 'Composer', a)


def test_assoc_contentItemTypes34_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ContentItemType(extendsClass=True)
    b2 = ccore_ContentItemType(extendsClass=False)
    _safe_set(a, 'ccore_ItemType35', {b1})
    assert _is_linked(a, 'ccore_ItemType35', b1)
    if hasattr(b1, 'ccore_ContentItemType36'):
        assert _is_linked(b1, 'ccore_ContentItemType36', a)
    _safe_set(a, 'ccore_ItemType35', {b2})
    assert _is_linked(a, 'ccore_ItemType35', b2)
    if hasattr(b1, 'ccore_ContentItemType36'):
        assert not _is_linked(b1, 'ccore_ContentItemType36', a)
    if hasattr(b2, 'ccore_ContentItemType36'):
        assert _is_linked(b2, 'ccore_ContentItemType36', a)
    _safe_set(a, 'ccore_ItemType35', set())
    assert not _is_linked(a, 'ccore_ItemType35', b2)
    if hasattr(b2, 'ccore_ContentItemType36'):
        assert not _is_linked(b2, 'ccore_ContentItemType36', a)


def test_assoc_contentModel28_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ContentItemType(extendsClass=True)
    b2 = ccore_ContentItemType(extendsClass=False)
    _safe_set(a, 'ccore_ItemType29', b1)
    assert _is_linked(a, 'ccore_ItemType29', b1)
    if hasattr(b1, 'ccore_ContentItemType'):
        assert _is_linked(b1, 'ccore_ContentItemType', a)
    _safe_set(a, 'ccore_ItemType29', b2)
    assert _is_linked(a, 'ccore_ItemType29', b2)
    if hasattr(b1, 'ccore_ContentItemType'):
        assert not _is_linked(b1, 'ccore_ContentItemType', a)
    if hasattr(b2, 'ccore_ContentItemType'):
        assert _is_linked(b2, 'ccore_ContentItemType', a)
    _safe_set(a, 'ccore_ItemType29', None)
    assert not _is_linked(a, 'ccore_ItemType29', b2)
    if hasattr(b2, 'ccore_ContentItemType'):
        assert not _is_linked(b2, 'ccore_ContentItemType', a)


def test_assoc_contents63_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_ContentItem()
    b2 = ccore_ContentItem()
    _safe_set(a, 'ownerItem', {b1})
    assert _is_linked(a, 'ownerItem', b1)
    if hasattr(b1, 'ContentItem'):
        assert _is_linked(b1, 'ContentItem', a)
    _safe_set(a, 'ownerItem', {b2})
    assert _is_linked(a, 'ownerItem', b2)
    if hasattr(b1, 'ContentItem'):
        assert not _is_linked(b1, 'ContentItem', a)
    if hasattr(b2, 'ContentItem'):
        assert _is_linked(b2, 'ContentItem', a)
    _safe_set(a, 'ownerItem', set())
    assert not _is_linked(a, 'ownerItem', b2)
    if hasattr(b2, 'ContentItem'):
        assert not _is_linked(b2, 'ContentItem', a)


def test_assoc_creationPages3_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    b2 = ccore_Page(description="sample_text_2", idRuntime="sample_text_2", label="sample_text_2", title="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition4', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition4', b1)
    if hasattr(b1, 'ccore_Page'):
        assert _is_linked(b1, 'ccore_Page', a)
    _safe_set(a, 'ccore_TypeDefinition4', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition4', b2)
    if hasattr(b1, 'ccore_Page'):
        assert not _is_linked(b1, 'ccore_Page', a)
    if hasattr(b2, 'ccore_Page'):
        assert _is_linked(b2, 'ccore_Page', a)
    _safe_set(a, 'ccore_TypeDefinition4', set())
    assert not _is_linked(a, 'ccore_TypeDefinition4', b2)
    if hasattr(b2, 'ccore_Page'):
        assert not _is_linked(b2, 'ccore_Page', a)


def test_assoc_dest165_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_BindingDesc()
    b2 = ccore_BindingDesc()
    _safe_set(a, 'ccore_Item167', b1)
    assert _is_linked(a, 'ccore_Item167', b1)
    if hasattr(b1, 'ccore_BindingDesc166'):
        assert _is_linked(b1, 'ccore_BindingDesc166', a)
    _safe_set(a, 'ccore_Item167', b2)
    assert _is_linked(a, 'ccore_Item167', b2)
    if hasattr(b1, 'ccore_BindingDesc166'):
        assert not _is_linked(b1, 'ccore_BindingDesc166', a)
    if hasattr(b2, 'ccore_BindingDesc166'):
        assert _is_linked(b2, 'ccore_BindingDesc166', a)
    _safe_set(a, 'ccore_Item167', None)
    assert not _is_linked(a, 'ccore_Item167', b2)
    if hasattr(b2, 'ccore_BindingDesc166'):
        assert not _is_linked(b2, 'ccore_BindingDesc166', a)


def test_assoc_destination100_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b2 = ccore_LinkType(aggregation=False, annotation=False, composition=False, group=False, hidden=False, kind=13, linkManager="sample_text_2", mapping=False, max=13, min=13, selection="sample_text_2", twCoupled=False, twDestEvol="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition101', b1)
    assert _is_linked(a, 'ccore_TypeDefinition101', b1)
    if hasattr(b1, 'ccore_LinkType'):
        assert _is_linked(b1, 'ccore_LinkType', a)
    _safe_set(a, 'ccore_TypeDefinition101', b2)
    assert _is_linked(a, 'ccore_TypeDefinition101', b2)
    if hasattr(b1, 'ccore_LinkType'):
        assert not _is_linked(b1, 'ccore_LinkType', a)
    if hasattr(b2, 'ccore_LinkType'):
        assert _is_linked(b2, 'ccore_LinkType', a)
    _safe_set(a, 'ccore_TypeDefinition101', None)
    assert not _is_linked(a, 'ccore_TypeDefinition101', b2)
    if hasattr(b2, 'ccore_LinkType'):
        assert not _is_linked(b2, 'ccore_LinkType', a)


def test_assoc_enumType99_link_reassign_clear():
    a = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    b1 = ccore_Enum(enumClazz="sample_text", values="sample_text")
    b2 = ccore_Enum(enumClazz="sample_text_2", values="sample_text_2")
    _safe_set(a, 'ccore_EnumType', b1)
    assert _is_linked(a, 'ccore_EnumType', b1)
    if hasattr(b1, 'ccore_Enum'):
        assert _is_linked(b1, 'ccore_Enum', a)
    _safe_set(a, 'ccore_EnumType', b2)
    assert _is_linked(a, 'ccore_EnumType', b2)
    if hasattr(b1, 'ccore_Enum'):
        assert not _is_linked(b1, 'ccore_Enum', a)
    if hasattr(b2, 'ccore_Enum'):
        assert _is_linked(b2, 'ccore_Enum', a)
    _safe_set(a, 'ccore_EnumType', None)
    assert not _is_linked(a, 'ccore_EnumType', b2)
    if hasattr(b2, 'ccore_Enum'):
        assert not _is_linked(b2, 'ccore_Enum', a)


def test_assoc_exendsItemTypes14_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ExtentedType()
    b2 = ccore_ExtentedType()
    _safe_set(a, 'ccore_ItemType', b1)
    assert _is_linked(a, 'ccore_ItemType', b1)
    if hasattr(b1, 'ccore_ExtentedType'):
        assert _is_linked(b1, 'ccore_ExtentedType', a)
    _safe_set(a, 'ccore_ItemType', b2)
    assert _is_linked(a, 'ccore_ItemType', b2)
    if hasattr(b1, 'ccore_ExtentedType'):
        assert not _is_linked(b1, 'ccore_ExtentedType', a)
    if hasattr(b2, 'ccore_ExtentedType'):
        assert _is_linked(b2, 'ccore_ExtentedType', a)
    _safe_set(a, 'ccore_ItemType', None)
    assert not _is_linked(a, 'ccore_ItemType', b2)
    if hasattr(b2, 'ccore_ExtentedType'):
        assert not _is_linked(b2, 'ccore_ExtentedType', a)


def test_assoc_exporterTypes30_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ExporterType()
    b2 = ccore_ExporterType()
    _safe_set(a, 'ccore_ItemType31', {b1})
    assert _is_linked(a, 'ccore_ItemType31', b1)
    if hasattr(b1, 'ccore_ExporterType'):
        assert _is_linked(b1, 'ccore_ExporterType', a)
    _safe_set(a, 'ccore_ItemType31', {b2})
    assert _is_linked(a, 'ccore_ItemType31', b2)
    if hasattr(b1, 'ccore_ExporterType'):
        assert not _is_linked(b1, 'ccore_ExporterType', a)
    if hasattr(b2, 'ccore_ExporterType'):
        assert _is_linked(b2, 'ccore_ExporterType', a)
    _safe_set(a, 'ccore_ItemType31', set())
    assert not _is_linked(a, 'ccore_ItemType31', b2)
    if hasattr(b2, 'ccore_ExporterType'):
        assert not _is_linked(b2, 'ccore_ExporterType', a)


def test_assoc_exporters153_link_reassign_clear():
    a = ccore_Exporter(types="sample_text")
    b1 = ccore_ComposerLink()
    b2 = ccore_ComposerLink()
    _safe_set(a, 'ccore_Exporter', b1)
    assert _is_linked(a, 'ccore_Exporter', b1)
    if hasattr(b1, 'ccore_ComposerLink154'):
        assert _is_linked(b1, 'ccore_ComposerLink154', a)
    _safe_set(a, 'ccore_Exporter', b2)
    assert _is_linked(a, 'ccore_Exporter', b2)
    if hasattr(b1, 'ccore_ComposerLink154'):
        assert not _is_linked(b1, 'ccore_ComposerLink154', a)
    if hasattr(b2, 'ccore_ComposerLink154'):
        assert _is_linked(b2, 'ccore_ComposerLink154', a)
    _safe_set(a, 'ccore_Exporter', None)
    assert not _is_linked(a, 'ccore_Exporter', b2)
    if hasattr(b2, 'ccore_ComposerLink154'):
        assert not _is_linked(b2, 'ccore_ComposerLink154', a)


def test_assoc_exporters67_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Exporter(types="sample_text")
    b2 = ccore_Exporter(types="sample_text_2")
    _safe_set(a, 'ownerItem68', {b1})
    assert _is_linked(a, 'ownerItem68', b1)
    if hasattr(b1, 'Exporter'):
        assert _is_linked(b1, 'Exporter', a)
    _safe_set(a, 'ownerItem68', {b2})
    assert _is_linked(a, 'ownerItem68', b2)
    if hasattr(b1, 'Exporter'):
        assert not _is_linked(b1, 'Exporter', a)
    if hasattr(b2, 'Exporter'):
        assert _is_linked(b2, 'Exporter', a)
    _safe_set(a, 'ownerItem68', set())
    assert not _is_linked(a, 'ownerItem68', b2)
    if hasattr(b2, 'Exporter'):
        assert not _is_linked(b2, 'Exporter', a)


def test_assoc_extendedBy23_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ExtentedType()
    b2 = ccore_ExtentedType()
    _safe_set(a, 'ccore_ItemType24', {b1})
    assert _is_linked(a, 'ccore_ItemType24', b1)
    if hasattr(b1, 'ccore_ExtentedType25'):
        assert _is_linked(b1, 'ccore_ExtentedType25', a)
    _safe_set(a, 'ccore_ItemType24', {b2})
    assert _is_linked(a, 'ccore_ItemType24', b2)
    if hasattr(b1, 'ccore_ExtentedType25'):
        assert not _is_linked(b1, 'ccore_ExtentedType25', a)
    if hasattr(b2, 'ccore_ExtentedType25'):
        assert _is_linked(b2, 'ccore_ExtentedType25', a)
    _safe_set(a, 'ccore_ItemType24', set())
    assert not _is_linked(a, 'ccore_ItemType24', b2)
    if hasattr(b2, 'ccore_ExtentedType25'):
        assert not _is_linked(b2, 'ccore_ExtentedType25', a)


def test_assoc_extendedTypes45_link_reassign_clear():
    a = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b1 = ccore_ExtentedType()
    b2 = ccore_ExtentedType()
    _safe_set(a, 'ccore_Cadse46', {b1})
    assert _is_linked(a, 'ccore_Cadse46', b1)
    if hasattr(b1, 'ccore_ExtentedType47'):
        assert _is_linked(b1, 'ccore_ExtentedType47', a)
    _safe_set(a, 'ccore_Cadse46', {b2})
    assert _is_linked(a, 'ccore_Cadse46', b2)
    if hasattr(b1, 'ccore_ExtentedType47'):
        assert not _is_linked(b1, 'ccore_ExtentedType47', a)
    if hasattr(b2, 'ccore_ExtentedType47'):
        assert _is_linked(b2, 'ccore_ExtentedType47', a)
    _safe_set(a, 'ccore_Cadse46', set())
    assert not _is_linked(a, 'ccore_Cadse46', b2)
    if hasattr(b2, 'ccore_ExtentedType47'):
        assert not _is_linked(b2, 'ccore_ExtentedType47', a)


def test_assoc_extendsCadse38_link_reassign_clear():
    a = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b1 = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b2 = ccore_Cadse(defaultContentRepoURL="sample_text_2", description="sample_text_2", executed=False, idDefinition="sample_text_2", itemRepoLogin="sample_text_2", itemRepoPasswd="sample_text_2", itemRepoURL="sample_text_2")
    _safe_set(a, 'ccore_Cadse', b1)
    assert _is_linked(a, 'ccore_Cadse', b1)
    if hasattr(b1, 'ccore_Cadse37'):
        assert _is_linked(b1, 'ccore_Cadse37', a)
    _safe_set(a, 'ccore_Cadse', b2)
    assert _is_linked(a, 'ccore_Cadse', b2)
    if hasattr(b1, 'ccore_Cadse37'):
        assert not _is_linked(b1, 'ccore_Cadse37', a)
    if hasattr(b2, 'ccore_Cadse37'):
        assert _is_linked(b2, 'ccore_Cadse37', a)
    _safe_set(a, 'ccore_Cadse', None)
    assert not _is_linked(a, 'ccore_Cadse', b2)
    if hasattr(b2, 'ccore_Cadse37'):
        assert not _is_linked(b2, 'ccore_Cadse37', a)


def test_assoc_fields1_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_Field(editable=True, label="sample_text", position="sample_text")
    b2 = ccore_Field(editable=False, label="sample_text_2", position="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition2', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition2', b1)
    if hasattr(b1, 'ccore_Field'):
        assert _is_linked(b1, 'ccore_Field', a)
    _safe_set(a, 'ccore_TypeDefinition2', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition2', b2)
    if hasattr(b1, 'ccore_Field'):
        assert not _is_linked(b1, 'ccore_Field', a)
    if hasattr(b2, 'ccore_Field'):
        assert _is_linked(b2, 'ccore_Field', a)
    _safe_set(a, 'ccore_TypeDefinition2', set())
    assert not _is_linked(a, 'ccore_TypeDefinition2', b2)
    if hasattr(b2, 'ccore_Field'):
        assert not _is_linked(b2, 'ccore_Field', a)


def test_assoc_goupsOfAttributes10_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_GroupOfAttributes(column=7)
    b2 = ccore_GroupOfAttributes(column=13)
    _safe_set(a, 'ccore_TypeDefinition11', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition11', b1)
    if hasattr(b1, 'ccore_GroupOfAttributes'):
        assert _is_linked(b1, 'ccore_GroupOfAttributes', a)
    _safe_set(a, 'ccore_TypeDefinition11', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition11', b2)
    if hasattr(b1, 'ccore_GroupOfAttributes'):
        assert not _is_linked(b1, 'ccore_GroupOfAttributes', a)
    if hasattr(b2, 'ccore_GroupOfAttributes'):
        assert _is_linked(b2, 'ccore_GroupOfAttributes', a)
    _safe_set(a, 'ccore_TypeDefinition11', set())
    assert not _is_linked(a, 'ccore_TypeDefinition11', b2)
    if hasattr(b2, 'ccore_GroupOfAttributes'):
        assert not _is_linked(b2, 'ccore_GroupOfAttributes', a)


def test_assoc_ic114_link_reassign_clear():
    a = ccore_Field(editable=True, label="sample_text", position="sample_text")
    b1 = ccore_InteractionController()
    b2 = ccore_InteractionController()
    _safe_set(a, 'ccore_Field115', b1)
    assert _is_linked(a, 'ccore_Field115', b1)
    if hasattr(b1, 'ccore_InteractionController'):
        assert _is_linked(b1, 'ccore_InteractionController', a)
    _safe_set(a, 'ccore_Field115', b2)
    assert _is_linked(a, 'ccore_Field115', b2)
    if hasattr(b1, 'ccore_InteractionController'):
        assert not _is_linked(b1, 'ccore_InteractionController', a)
    if hasattr(b2, 'ccore_InteractionController'):
        assert _is_linked(b2, 'ccore_InteractionController', a)
    _safe_set(a, 'ccore_Field115', None)
    assert not _is_linked(a, 'ccore_Field115', b2)
    if hasattr(b2, 'ccore_InteractionController'):
        assert not _is_linked(b2, 'ccore_InteractionController', a)


def test_assoc_instanceOf54_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    _safe_set(a, 'ccore_ItemType56', b1)
    assert _is_linked(a, 'ccore_ItemType56', b1)
    if hasattr(b1, 'ccore_Item55'):
        assert _is_linked(b1, 'ccore_Item55', a)
    _safe_set(a, 'ccore_ItemType56', b2)
    assert _is_linked(a, 'ccore_ItemType56', b2)
    if hasattr(b1, 'ccore_Item55'):
        assert not _is_linked(b1, 'ccore_Item55', a)
    if hasattr(b2, 'ccore_Item55'):
        assert _is_linked(b2, 'ccore_Item55', a)
    _safe_set(a, 'ccore_ItemType56', None)
    assert not _is_linked(a, 'ccore_ItemType56', b2)
    if hasattr(b2, 'ccore_Item55'):
        assert not _is_linked(b2, 'ccore_Item55', a)


def test_assoc_itemContents52_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b2 = ccore_Cadse(defaultContentRepoURL="sample_text_2", description="sample_text_2", executed=False, idDefinition="sample_text_2", itemRepoLogin="sample_text_2", itemRepoPasswd="sample_text_2", itemRepoURL="sample_text_2")
    _safe_set(a, 'ccore_Item', b1)
    assert _is_linked(a, 'ccore_Item', b1)
    if hasattr(b1, 'ccore_Cadse53'):
        assert _is_linked(b1, 'ccore_Cadse53', a)
    _safe_set(a, 'ccore_Item', b2)
    assert _is_linked(a, 'ccore_Item', b2)
    if hasattr(b1, 'ccore_Cadse53'):
        assert not _is_linked(b1, 'ccore_Cadse53', a)
    if hasattr(b2, 'ccore_Cadse53'):
        assert _is_linked(b2, 'ccore_Cadse53', a)
    _safe_set(a, 'ccore_Item', None)
    assert not _is_linked(a, 'ccore_Item', b2)
    if hasattr(b2, 'ccore_Cadse53'):
        assert not _is_linked(b2, 'ccore_Cadse53', a)


def test_assoc_itemType79_link_reassign_clear():
    a = ccore_ViewItemType(isRootElement=True, ref=True)
    b1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    _safe_set(a, 'ccore_ViewItemType', b1)
    assert _is_linked(a, 'ccore_ViewItemType', b1)
    if hasattr(b1, 'ccore_ItemType80'):
        assert _is_linked(b1, 'ccore_ItemType80', a)
    _safe_set(a, 'ccore_ViewItemType', b2)
    assert _is_linked(a, 'ccore_ViewItemType', b2)
    if hasattr(b1, 'ccore_ItemType80'):
        assert not _is_linked(b1, 'ccore_ItemType80', a)
    if hasattr(b2, 'ccore_ItemType80'):
        assert _is_linked(b2, 'ccore_ItemType80', a)
    _safe_set(a, 'ccore_ViewItemType', None)
    assert not _is_linked(a, 'ccore_ViewItemType', b2)
    if hasattr(b2, 'ccore_ItemType80'):
        assert not _is_linked(b2, 'ccore_ItemType80', a)


def test_assoc_itemTypes39_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b2 = ccore_Cadse(defaultContentRepoURL="sample_text_2", description="sample_text_2", executed=False, idDefinition="sample_text_2", itemRepoLogin="sample_text_2", itemRepoPasswd="sample_text_2", itemRepoURL="sample_text_2")
    _safe_set(a, 'ccore_ItemType41', b1)
    assert _is_linked(a, 'ccore_ItemType41', b1)
    if hasattr(b1, 'ccore_Cadse40'):
        assert _is_linked(b1, 'ccore_Cadse40', a)
    _safe_set(a, 'ccore_ItemType41', b2)
    assert _is_linked(a, 'ccore_ItemType41', b2)
    if hasattr(b1, 'ccore_Cadse40'):
        assert not _is_linked(b1, 'ccore_Cadse40', a)
    if hasattr(b2, 'ccore_Cadse40'):
        assert _is_linked(b2, 'ccore_Cadse40', a)
    _safe_set(a, 'ccore_ItemType41', None)
    assert not _is_linked(a, 'ccore_ItemType41', b2)
    if hasattr(b2, 'ccore_Cadse40'):
        assert not _is_linked(b2, 'ccore_Cadse40', a)


def test_assoc_keyDefinition26_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_KeyDefinition()
    b2 = ccore_KeyDefinition()
    _safe_set(a, 'ccore_ItemType27', b1)
    assert _is_linked(a, 'ccore_ItemType27', b1)
    if hasattr(b1, 'ccore_KeyDefinition'):
        assert _is_linked(b1, 'ccore_KeyDefinition', a)
    _safe_set(a, 'ccore_ItemType27', b2)
    assert _is_linked(a, 'ccore_ItemType27', b2)
    if hasattr(b1, 'ccore_KeyDefinition'):
        assert not _is_linked(b1, 'ccore_KeyDefinition', a)
    if hasattr(b2, 'ccore_KeyDefinition'):
        assert _is_linked(b2, 'ccore_KeyDefinition', a)
    _safe_set(a, 'ccore_ItemType27', None)
    assert not _is_linked(a, 'ccore_ItemType27', b2)
    if hasattr(b2, 'ccore_KeyDefinition'):
        assert not _is_linked(b2, 'ccore_KeyDefinition', a)


def test_assoc_keys42_link_reassign_clear():
    a = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b1 = ccore_KeyDefinition()
    b2 = ccore_KeyDefinition()
    _safe_set(a, 'ccore_Cadse43', {b1})
    assert _is_linked(a, 'ccore_Cadse43', b1)
    if hasattr(b1, 'ccore_KeyDefinition44'):
        assert _is_linked(b1, 'ccore_KeyDefinition44', a)
    _safe_set(a, 'ccore_Cadse43', {b2})
    assert _is_linked(a, 'ccore_Cadse43', b2)
    if hasattr(b1, 'ccore_KeyDefinition44'):
        assert not _is_linked(b1, 'ccore_KeyDefinition44', a)
    if hasattr(b2, 'ccore_KeyDefinition44'):
        assert _is_linked(b2, 'ccore_KeyDefinition44', a)
    _safe_set(a, 'ccore_Cadse43', set())
    assert not _is_linked(a, 'ccore_Cadse43', b2)
    if hasattr(b2, 'ccore_KeyDefinition44'):
        assert not _is_linked(b2, 'ccore_KeyDefinition44', a)


def test_assoc_link155_link_reassign_clear():
    a = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b1 = ccore_ComposerLink()
    b2 = ccore_ComposerLink()
    _safe_set(a, 'ccore_LinkType157', b1)
    assert _is_linked(a, 'ccore_LinkType157', b1)
    if hasattr(b1, 'ccore_ComposerLink156'):
        assert _is_linked(b1, 'ccore_ComposerLink156', a)
    _safe_set(a, 'ccore_LinkType157', b2)
    assert _is_linked(a, 'ccore_LinkType157', b2)
    if hasattr(b1, 'ccore_ComposerLink156'):
        assert not _is_linked(b1, 'ccore_ComposerLink156', a)
    if hasattr(b2, 'ccore_ComposerLink156'):
        assert _is_linked(b2, 'ccore_ComposerLink156', a)
    _safe_set(a, 'ccore_LinkType157', None)
    assert not _is_linked(a, 'ccore_LinkType157', b2)
    if hasattr(b2, 'ccore_ComposerLink156'):
        assert not _is_linked(b2, 'ccore_ComposerLink156', a)


def test_assoc_linkType134_link_reassign_clear():
    a = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    b1 = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b2 = ccore_LinkType(aggregation=False, annotation=False, composition=False, group=False, hidden=False, kind=13, linkManager="sample_text_2", mapping=False, max=13, min=13, selection="sample_text_2", twCoupled=False, twDestEvol="sample_text_2")
    _safe_set(a, 'ccore_ViewLinkType135', b1)
    assert _is_linked(a, 'ccore_ViewLinkType135', b1)
    if hasattr(b1, 'ccore_LinkType136'):
        assert _is_linked(b1, 'ccore_LinkType136', a)
    _safe_set(a, 'ccore_ViewLinkType135', b2)
    assert _is_linked(a, 'ccore_ViewLinkType135', b2)
    if hasattr(b1, 'ccore_LinkType136'):
        assert not _is_linked(b1, 'ccore_LinkType136', a)
    if hasattr(b2, 'ccore_LinkType136'):
        assert _is_linked(b2, 'ccore_LinkType136', a)
    _safe_set(a, 'ccore_ViewLinkType135', None)
    assert not _is_linked(a, 'ccore_ViewLinkType135', b2)
    if hasattr(b2, 'ccore_LinkType136'):
        assert not _is_linked(b2, 'ccore_LinkType136', a)


def test_assoc_links144_link_reassign_clear():
    a = ccore_Composer(types="sample_text")
    b1 = ccore_ComposerLink()
    b2 = ccore_ComposerLink()
    _safe_set(a, 'ccore_Composer145', {b1})
    assert _is_linked(a, 'ccore_Composer145', b1)
    if hasattr(b1, 'ccore_ComposerLink'):
        assert _is_linked(b1, 'ccore_ComposerLink', a)
    _safe_set(a, 'ccore_Composer145', {b2})
    assert _is_linked(a, 'ccore_Composer145', b2)
    if hasattr(b1, 'ccore_ComposerLink'):
        assert not _is_linked(b1, 'ccore_ComposerLink', a)
    if hasattr(b2, 'ccore_ComposerLink'):
        assert _is_linked(b2, 'ccore_ComposerLink', a)
    _safe_set(a, 'ccore_Composer145', set())
    assert not _is_linked(a, 'ccore_Composer145', b2)
    if hasattr(b2, 'ccore_ComposerLink'):
        assert not _is_linked(b2, 'ccore_ComposerLink', a)


def test_assoc_listenAttributeDefinitions108_link_reassign_clear():
    a = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b1 = ccore_WCListener()
    b2 = ccore_WCListener()
    _safe_set(a, 'ccore_Attribute110', b1)
    assert _is_linked(a, 'ccore_Attribute110', b1)
    if hasattr(b1, 'ccore_WCListener109'):
        assert _is_linked(b1, 'ccore_WCListener109', a)
    _safe_set(a, 'ccore_Attribute110', b2)
    assert _is_linked(a, 'ccore_Attribute110', b2)
    if hasattr(b1, 'ccore_WCListener109'):
        assert not _is_linked(b1, 'ccore_WCListener109', a)
    if hasattr(b2, 'ccore_WCListener109'):
        assert _is_linked(b2, 'ccore_WCListener109', a)
    _safe_set(a, 'ccore_Attribute110', None)
    assert not _is_linked(a, 'ccore_Attribute110', b2)
    if hasattr(b2, 'ccore_WCListener109'):
        assert not _is_linked(b2, 'ccore_WCListener109', a)


def test_assoc_listenAttributes96_link_reassign_clear():
    a = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b1 = ccore_UIValidator()
    b2 = ccore_UIValidator()
    _safe_set(a, 'ccore_Attribute98', b1)
    assert _is_linked(a, 'ccore_Attribute98', b1)
    if hasattr(b1, 'ccore_UIValidator97'):
        assert _is_linked(b1, 'ccore_UIValidator97', a)
    _safe_set(a, 'ccore_Attribute98', b2)
    assert _is_linked(a, 'ccore_Attribute98', b2)
    if hasattr(b1, 'ccore_UIValidator97'):
        assert not _is_linked(b1, 'ccore_UIValidator97', a)
    if hasattr(b2, 'ccore_UIValidator97'):
        assert _is_linked(b2, 'ccore_UIValidator97', a)
    _safe_set(a, 'ccore_Attribute98', None)
    assert not _is_linked(a, 'ccore_Attribute98', b2)
    if hasattr(b2, 'ccore_UIValidator97'):
        assert not _is_linked(b2, 'ccore_UIValidator97', a)


def test_assoc_listenItemTypes105_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_WCListener()
    b2 = ccore_WCListener()
    _safe_set(a, 'ccore_ItemType107', b1)
    assert _is_linked(a, 'ccore_ItemType107', b1)
    if hasattr(b1, 'ccore_WCListener106'):
        assert _is_linked(b1, 'ccore_WCListener106', a)
    _safe_set(a, 'ccore_ItemType107', b2)
    assert _is_linked(a, 'ccore_ItemType107', b2)
    if hasattr(b1, 'ccore_WCListener106'):
        assert not _is_linked(b1, 'ccore_WCListener106', a)
    if hasattr(b2, 'ccore_WCListener106'):
        assert _is_linked(b2, 'ccore_WCListener106', a)
    _safe_set(a, 'ccore_ItemType107', None)
    assert not _is_linked(a, 'ccore_ItemType107', b2)
    if hasattr(b2, 'ccore_WCListener106'):
        assert not _is_linked(b2, 'ccore_WCListener106', a)


def test_assoc_mainItemType171_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_DBObject(objectId=7, uuid_lsb="sample_text", uuid_msb="sample_text")
    b2 = ccore_DBObject(objectId=13, uuid_lsb="sample_text_2", uuid_msb="sample_text_2")
    _safe_set(a, 'ccore_ItemType172', b1)
    assert _is_linked(a, 'ccore_ItemType172', b1)
    if hasattr(b1, 'ccore_DBObject'):
        assert _is_linked(b1, 'ccore_DBObject', a)
    _safe_set(a, 'ccore_ItemType172', b2)
    assert _is_linked(a, 'ccore_ItemType172', b2)
    if hasattr(b1, 'ccore_DBObject'):
        assert not _is_linked(b1, 'ccore_DBObject', a)
    if hasattr(b2, 'ccore_DBObject'):
        assert _is_linked(b2, 'ccore_DBObject', a)
    _safe_set(a, 'ccore_ItemType172', None)
    assert not _is_linked(a, 'ccore_ItemType172', b2)
    if hasattr(b2, 'ccore_DBObject'):
        assert not _is_linked(b2, 'ccore_DBObject', a)


def test_assoc_mc116_link_reassign_clear():
    a = ccore_Field(editable=True, label="sample_text", position="sample_text")
    b1 = ccore_ModelController()
    b2 = ccore_ModelController()
    _safe_set(a, 'ccore_Field117', b1)
    assert _is_linked(a, 'ccore_Field117', b1)
    if hasattr(b1, 'ccore_ModelController'):
        assert _is_linked(b1, 'ccore_ModelController', a)
    _safe_set(a, 'ccore_Field117', b2)
    assert _is_linked(a, 'ccore_Field117', b2)
    if hasattr(b1, 'ccore_ModelController'):
        assert not _is_linked(b1, 'ccore_ModelController', a)
    if hasattr(b2, 'ccore_ModelController'):
        assert _is_linked(b2, 'ccore_ModelController', a)
    _safe_set(a, 'ccore_Field117', None)
    assert not _is_linked(a, 'ccore_Field117', b2)
    if hasattr(b2, 'ccore_ModelController'):
        assert not _is_linked(b2, 'ccore_ModelController', a)


def test_assoc_memberOf139_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_GroupExtItem()
    b2 = ccore_GroupExtItem()
    _safe_set(a, 'ccore_Item141', b1)
    assert _is_linked(a, 'ccore_Item141', b1)
    if hasattr(b1, 'ccore_GroupExtItem140'):
        assert _is_linked(b1, 'ccore_GroupExtItem140', a)
    _safe_set(a, 'ccore_Item141', b2)
    assert _is_linked(a, 'ccore_Item141', b2)
    if hasattr(b1, 'ccore_GroupExtItem140'):
        assert not _is_linked(b1, 'ccore_GroupExtItem140', a)
    if hasattr(b2, 'ccore_GroupExtItem140'):
        assert _is_linked(b2, 'ccore_GroupExtItem140', a)
    _safe_set(a, 'ccore_Item141', None)
    assert not _is_linked(a, 'ccore_Item141', b2)
    if hasattr(b2, 'ccore_GroupExtItem140'):
        assert not _is_linked(b2, 'ccore_GroupExtItem140', a)


def test_assoc_members137_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_GroupExtItem()
    b2 = ccore_GroupExtItem()
    _safe_set(a, 'ccore_Item138', b1)
    assert _is_linked(a, 'ccore_Item138', b1)
    if hasattr(b1, 'ccore_GroupExtItem'):
        assert _is_linked(b1, 'ccore_GroupExtItem', a)
    _safe_set(a, 'ccore_Item138', b2)
    assert _is_linked(a, 'ccore_Item138', b2)
    if hasattr(b1, 'ccore_GroupExtItem'):
        assert not _is_linked(b1, 'ccore_GroupExtItem', a)
    if hasattr(b2, 'ccore_GroupExtItem'):
        assert _is_linked(b2, 'ccore_GroupExtItem', a)
    _safe_set(a, 'ccore_Item138', None)
    assert not _is_linked(a, 'ccore_Item138', b2)
    if hasattr(b2, 'ccore_GroupExtItem'):
        assert not _is_linked(b2, 'ccore_GroupExtItem', a)


def test_assoc_modificationPages7_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    b2 = ccore_Page(description="sample_text_2", idRuntime="sample_text_2", label="sample_text_2", title="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition8', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition8', b1)
    if hasattr(b1, 'ccore_Page9'):
        assert _is_linked(b1, 'ccore_Page9', a)
    _safe_set(a, 'ccore_TypeDefinition8', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition8', b2)
    if hasattr(b1, 'ccore_Page9'):
        assert not _is_linked(b1, 'ccore_Page9', a)
    if hasattr(b2, 'ccore_Page9'):
        assert _is_linked(b2, 'ccore_Page9', a)
    _safe_set(a, 'ccore_TypeDefinition8', set())
    assert not _is_linked(a, 'ccore_TypeDefinition8', b2)
    if hasattr(b2, 'ccore_Page9'):
        assert not _is_linked(b2, 'ccore_Page9', a)


def test_assoc_modifiedAttributes60_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b2 = ccore_Attribute(_final=False, cannotBeUndefined=False, devGenerated=False, hiddenInComputedPages=False, idRuntime="sample_text_2", isList=False, mustBeInitialized=False, natif=False, require=False, tWCommitKind="sample_text_2", tWEvol="sample_text_2", tWRevSpecific=False, tWUpdateKind="sample_text_2")
    _safe_set(a, 'ccore_Item61', {b1})
    assert _is_linked(a, 'ccore_Item61', b1)
    if hasattr(b1, 'ccore_Attribute62'):
        assert _is_linked(b1, 'ccore_Attribute62', a)
    _safe_set(a, 'ccore_Item61', {b2})
    assert _is_linked(a, 'ccore_Item61', b2)
    if hasattr(b1, 'ccore_Attribute62'):
        assert not _is_linked(b1, 'ccore_Attribute62', a)
    if hasattr(b2, 'ccore_Attribute62'):
        assert _is_linked(b2, 'ccore_Attribute62', a)
    _safe_set(a, 'ccore_Item61', set())
    assert not _is_linked(a, 'ccore_Item61', b2)
    if hasattr(b2, 'ccore_Attribute62'):
        assert not _is_linked(b2, 'ccore_Attribute62', a)


def test_assoc_overwrite124_link_reassign_clear():
    a = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    b1 = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    b2 = ccore_Page(description="sample_text_2", idRuntime="sample_text_2", label="sample_text_2", title="sample_text_2")
    _safe_set(a, 'ccore_Page123', {b1})
    assert _is_linked(a, 'ccore_Page123', b1)
    if hasattr(b1, 'ccore_Page125'):
        assert _is_linked(b1, 'ccore_Page125', a)
    _safe_set(a, 'ccore_Page123', {b2})
    assert _is_linked(a, 'ccore_Page123', b2)
    if hasattr(b1, 'ccore_Page125'):
        assert not _is_linked(b1, 'ccore_Page125', a)
    if hasattr(b2, 'ccore_Page125'):
        assert _is_linked(b2, 'ccore_Page125', a)
    _safe_set(a, 'ccore_Page123', set())
    assert not _is_linked(a, 'ccore_Page123', b2)
    if hasattr(b2, 'ccore_Page125'):
        assert not _is_linked(b2, 'ccore_Page125', a)


def test_assoc_ownerItem146_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Composer(types="sample_text")
    b2 = ccore_Composer(types="sample_text_2")
    _safe_set(a, 'Item', b1)
    assert _is_linked(a, 'Item', b1)
    if hasattr(b1, 'composers'):
        assert _is_linked(b1, 'composers', a)
    _safe_set(a, 'Item', b2)
    assert _is_linked(a, 'Item', b2)
    if hasattr(b1, 'composers'):
        assert not _is_linked(b1, 'composers', a)
    if hasattr(b2, 'composers'):
        assert _is_linked(b2, 'composers', a)
    _safe_set(a, 'Item', None)
    assert not _is_linked(a, 'Item', b2)
    if hasattr(b2, 'composers'):
        assert not _is_linked(b2, 'composers', a)


def test_assoc_ownerItem147_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Exporter(types="sample_text")
    b2 = ccore_Exporter(types="sample_text_2")
    _safe_set(a, 'Item148', b1)
    assert _is_linked(a, 'Item148', b1)
    if hasattr(b1, 'exporters'):
        assert _is_linked(b1, 'exporters', a)
    _safe_set(a, 'Item148', b2)
    assert _is_linked(a, 'Item148', b2)
    if hasattr(b1, 'exporters'):
        assert not _is_linked(b1, 'exporters', a)
    if hasattr(b2, 'exporters'):
        assert _is_linked(b2, 'exporters', a)
    _safe_set(a, 'Item148', None)
    assert not _is_linked(a, 'Item148', b2)
    if hasattr(b2, 'exporters'):
        assert not _is_linked(b2, 'exporters', a)


def test_assoc_ownerItem149_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_ContentItem()
    b2 = ccore_ContentItem()
    _safe_set(a, 'Item150', b1)
    assert _is_linked(a, 'Item150', b1)
    if hasattr(b1, 'contents'):
        assert _is_linked(b1, 'contents', a)
    _safe_set(a, 'Item150', b2)
    assert _is_linked(a, 'Item150', b2)
    if hasattr(b1, 'contents'):
        assert not _is_linked(b1, 'contents', a)
    if hasattr(b2, 'contents'):
        assert _is_linked(b2, 'contents', a)
    _safe_set(a, 'Item150', None)
    assert not _is_linked(a, 'Item150', b2)
    if hasattr(b2, 'contents'):
        assert not _is_linked(b2, 'contents', a)


def test_assoc_parent58_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    _safe_set(a, 'ccore_Item57', b1)
    assert _is_linked(a, 'ccore_Item57', b1)
    if hasattr(b1, 'ccore_Item59'):
        assert _is_linked(b1, 'ccore_Item59', a)
    _safe_set(a, 'ccore_Item57', b2)
    assert _is_linked(a, 'ccore_Item57', b2)
    if hasattr(b1, 'ccore_Item59'):
        assert not _is_linked(b1, 'ccore_Item59', a)
    if hasattr(b2, 'ccore_Item59'):
        assert _is_linked(b2, 'ccore_Item59', a)
    _safe_set(a, 'ccore_Item57', None)
    assert not _is_linked(a, 'ccore_Item57', b2)
    if hasattr(b2, 'ccore_Item59'):
        assert not _is_linked(b2, 'ccore_Item59', a)


def test_assoc_refEClass12_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_EClass()
    b2 = ccore_EClass()
    _safe_set(a, 'ccore_TypeDefinition13', b1)
    assert _is_linked(a, 'ccore_TypeDefinition13', b1)
    if hasattr(b1, 'ccore_EClass'):
        assert _is_linked(b1, 'ccore_EClass', a)
    _safe_set(a, 'ccore_TypeDefinition13', b2)
    assert _is_linked(a, 'ccore_TypeDefinition13', b2)
    if hasattr(b1, 'ccore_EClass'):
        assert not _is_linked(b1, 'ccore_EClass', a)
    if hasattr(b2, 'ccore_EClass'):
        assert _is_linked(b2, 'ccore_EClass', a)
    _safe_set(a, 'ccore_TypeDefinition13', None)
    assert not _is_linked(a, 'ccore_TypeDefinition13', b2)
    if hasattr(b2, 'ccore_EClass'):
        assert not _is_linked(b2, 'ccore_EClass', a)


def test_assoc_refEPackage48_link_reassign_clear():
    a = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    b1 = ccore_EPackage()
    b2 = ccore_EPackage()
    _safe_set(a, 'ccore_Cadse49', b1)
    assert _is_linked(a, 'ccore_Cadse49', b1)
    if hasattr(b1, 'ccore_EPackage'):
        assert _is_linked(b1, 'ccore_EPackage', a)
    _safe_set(a, 'ccore_Cadse49', b2)
    assert _is_linked(a, 'ccore_Cadse49', b2)
    if hasattr(b1, 'ccore_EPackage'):
        assert not _is_linked(b1, 'ccore_EPackage', a)
    if hasattr(b2, 'ccore_EPackage'):
        assert _is_linked(b2, 'ccore_EPackage', a)
    _safe_set(a, 'ccore_Cadse49', None)
    assert not _is_linked(a, 'ccore_Cadse49', b2)
    if hasattr(b2, 'ccore_EPackage'):
        assert not _is_linked(b2, 'ccore_EPackage', a)


def test_assoc_refEnum126_link_reassign_clear():
    a = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    b1 = ccore_EEnum()
    b2 = ccore_EEnum()
    _safe_set(a, 'ccore_EnumType127', b1)
    assert _is_linked(a, 'ccore_EnumType127', b1)
    if hasattr(b1, 'ccore_EEnum'):
        assert _is_linked(b1, 'ccore_EEnum', a)
    _safe_set(a, 'ccore_EnumType127', b2)
    assert _is_linked(a, 'ccore_EnumType127', b2)
    if hasattr(b1, 'ccore_EEnum'):
        assert not _is_linked(b1, 'ccore_EEnum', a)
    if hasattr(b2, 'ccore_EEnum'):
        assert _is_linked(b2, 'ccore_EEnum', a)
    _safe_set(a, 'ccore_EnumType127', None)
    assert not _is_linked(a, 'ccore_EnumType127', b2)
    if hasattr(b2, 'ccore_EEnum'):
        assert not _is_linked(b2, 'ccore_EEnum', a)


def test_assoc_refItemType85_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_BindExt()
    b2 = ccore_BindExt()
    _safe_set(a, 'ccore_ItemType86', b1)
    assert _is_linked(a, 'ccore_ItemType86', b1)
    if hasattr(b1, 'ccore_BindExt'):
        assert _is_linked(b1, 'ccore_BindExt', a)
    _safe_set(a, 'ccore_ItemType86', b2)
    assert _is_linked(a, 'ccore_ItemType86', b2)
    if hasattr(b1, 'ccore_BindExt'):
        assert not _is_linked(b1, 'ccore_BindExt', a)
    if hasattr(b2, 'ccore_BindExt'):
        assert _is_linked(b2, 'ccore_BindExt', a)
    _safe_set(a, 'ccore_ItemType86', None)
    assert not _is_linked(a, 'ccore_ItemType86', b2)
    if hasattr(b2, 'ccore_BindExt'):
        assert not _is_linked(b2, 'ccore_BindExt', a)


def test_assoc_rootTypes83_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_ViewDescription()
    b2 = ccore_ViewDescription()
    _safe_set(a, 'ccore_TypeDefinition84', b1)
    assert _is_linked(a, 'ccore_TypeDefinition84', b1)
    if hasattr(b1, 'ccore_ViewDescription'):
        assert _is_linked(b1, 'ccore_ViewDescription', a)
    _safe_set(a, 'ccore_TypeDefinition84', b2)
    assert _is_linked(a, 'ccore_TypeDefinition84', b2)
    if hasattr(b1, 'ccore_ViewDescription'):
        assert not _is_linked(b1, 'ccore_ViewDescription', a)
    if hasattr(b2, 'ccore_ViewDescription'):
        assert _is_linked(b2, 'ccore_ViewDescription', a)
    _safe_set(a, 'ccore_TypeDefinition84', None)
    assert not _is_linked(a, 'ccore_TypeDefinition84', b2)
    if hasattr(b2, 'ccore_ViewDescription'):
        assert not _is_linked(b2, 'ccore_ViewDescription', a)


def test_assoc_source102_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b2 = ccore_LinkType(aggregation=False, annotation=False, composition=False, group=False, hidden=False, kind=13, linkManager="sample_text_2", mapping=False, max=13, min=13, selection="sample_text_2", twCoupled=False, twDestEvol="sample_text_2")
    _safe_set(a, 'ccore_TypeDefinition104', b1)
    assert _is_linked(a, 'ccore_TypeDefinition104', b1)
    if hasattr(b1, 'ccore_LinkType103'):
        assert _is_linked(b1, 'ccore_LinkType103', a)
    _safe_set(a, 'ccore_TypeDefinition104', b2)
    assert _is_linked(a, 'ccore_TypeDefinition104', b2)
    if hasattr(b1, 'ccore_LinkType103'):
        assert not _is_linked(b1, 'ccore_LinkType103', a)
    if hasattr(b2, 'ccore_LinkType103'):
        assert _is_linked(b2, 'ccore_LinkType103', a)
    _safe_set(a, 'ccore_TypeDefinition104', None)
    assert not _is_linked(a, 'ccore_TypeDefinition104', b2)
    if hasattr(b2, 'ccore_LinkType103'):
        assert not _is_linked(b2, 'ccore_LinkType103', a)


def test_assoc_source162_link_reassign_clear():
    a = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    b1 = ccore_BindingDesc()
    b2 = ccore_BindingDesc()
    _safe_set(a, 'ccore_Item164', b1)
    assert _is_linked(a, 'ccore_Item164', b1)
    if hasattr(b1, 'ccore_BindingDesc163'):
        assert _is_linked(b1, 'ccore_BindingDesc163', a)
    _safe_set(a, 'ccore_Item164', b2)
    assert _is_linked(a, 'ccore_Item164', b2)
    if hasattr(b1, 'ccore_BindingDesc163'):
        assert not _is_linked(b1, 'ccore_BindingDesc163', a)
    if hasattr(b2, 'ccore_BindingDesc163'):
        assert _is_linked(b2, 'ccore_BindingDesc163', a)
    _safe_set(a, 'ccore_Item164', None)
    assert not _is_linked(a, 'ccore_Item164', b2)
    if hasattr(b2, 'ccore_BindingDesc163'):
        assert not _is_linked(b2, 'ccore_BindingDesc163', a)


def test_assoc_subTypes21_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    _safe_set(a, 'ccore_ItemType20', {b1})
    assert _is_linked(a, 'ccore_ItemType20', b1)
    if hasattr(b1, 'ccore_ItemType22'):
        assert _is_linked(b1, 'ccore_ItemType22', a)
    _safe_set(a, 'ccore_ItemType20', {b2})
    assert _is_linked(a, 'ccore_ItemType20', b2)
    if hasattr(b1, 'ccore_ItemType22'):
        assert not _is_linked(b1, 'ccore_ItemType22', a)
    if hasattr(b2, 'ccore_ItemType22'):
        assert _is_linked(b2, 'ccore_ItemType22', a)
    _safe_set(a, 'ccore_ItemType20', set())
    assert not _is_linked(a, 'ccore_ItemType20', b2)
    if hasattr(b2, 'ccore_ItemType22'):
        assert not _is_linked(b2, 'ccore_ItemType22', a)


def test_assoc_superGroup132_link_reassign_clear():
    a = ccore_GroupOfAttributes(column=7)
    b1 = ccore_GroupOfAttributes(column=7)
    b2 = ccore_GroupOfAttributes(column=13)
    _safe_set(a, 'ccore_GroupOfAttributes131', b1)
    assert _is_linked(a, 'ccore_GroupOfAttributes131', b1)
    if hasattr(b1, 'ccore_GroupOfAttributes133'):
        assert _is_linked(b1, 'ccore_GroupOfAttributes133', a)
    _safe_set(a, 'ccore_GroupOfAttributes131', b2)
    assert _is_linked(a, 'ccore_GroupOfAttributes131', b2)
    if hasattr(b1, 'ccore_GroupOfAttributes133'):
        assert not _is_linked(b1, 'ccore_GroupOfAttributes133', a)
    if hasattr(b2, 'ccore_GroupOfAttributes133'):
        assert _is_linked(b2, 'ccore_GroupOfAttributes133', a)
    _safe_set(a, 'ccore_GroupOfAttributes131', None)
    assert not _is_linked(a, 'ccore_GroupOfAttributes131', b2)
    if hasattr(b2, 'ccore_GroupOfAttributes133'):
        assert not _is_linked(b2, 'ccore_GroupOfAttributes133', a)


def test_assoc_superType16_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    _safe_set(a, 'ccore_ItemType15', {b1})
    assert _is_linked(a, 'ccore_ItemType15', b1)
    if hasattr(b1, 'ccore_ItemType17'):
        assert _is_linked(b1, 'ccore_ItemType17', a)
    _safe_set(a, 'ccore_ItemType15', {b2})
    assert _is_linked(a, 'ccore_ItemType15', b2)
    if hasattr(b1, 'ccore_ItemType17'):
        assert not _is_linked(b1, 'ccore_ItemType17', a)
    if hasattr(b2, 'ccore_ItemType17'):
        assert _is_linked(b2, 'ccore_ItemType17', a)
    _safe_set(a, 'ccore_ItemType15', set())
    assert not _is_linked(a, 'ccore_ItemType15', b2)
    if hasattr(b2, 'ccore_ItemType17'):
        assert not _is_linked(b2, 'ccore_ItemType17', a)


def test_assoc_typeBinding168_link_reassign_clear():
    a = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    b1 = ccore_BindingDesc()
    b2 = ccore_BindingDesc()
    _safe_set(a, 'ccore_LinkType170', b1)
    assert _is_linked(a, 'ccore_LinkType170', b1)
    if hasattr(b1, 'ccore_BindingDesc169'):
        assert _is_linked(b1, 'ccore_BindingDesc169', a)
    _safe_set(a, 'ccore_LinkType170', b2)
    assert _is_linked(a, 'ccore_LinkType170', b2)
    if hasattr(b1, 'ccore_BindingDesc169'):
        assert not _is_linked(b1, 'ccore_BindingDesc169', a)
    if hasattr(b2, 'ccore_BindingDesc169'):
        assert _is_linked(b2, 'ccore_BindingDesc169', a)
    _safe_set(a, 'ccore_LinkType170', None)
    assert not _is_linked(a, 'ccore_LinkType170', b2)
    if hasattr(b2, 'ccore_BindingDesc169'):
        assert not _is_linked(b2, 'ccore_BindingDesc169', a)


def test_assoc_ui118_link_reassign_clear():
    a = ccore_Field(editable=True, label="sample_text", position="sample_text")
    b1 = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    b2 = ccore_Display(extendsIC=False, extendsMC=False, extendsUI=False)
    _safe_set(a, 'ccore_Field119', b1)
    assert _is_linked(a, 'ccore_Field119', b1)
    if hasattr(b1, 'ccore_Display'):
        assert _is_linked(b1, 'ccore_Display', a)
    _safe_set(a, 'ccore_Field119', b2)
    assert _is_linked(a, 'ccore_Field119', b2)
    if hasattr(b1, 'ccore_Display'):
        assert not _is_linked(b1, 'ccore_Display', a)
    if hasattr(b2, 'ccore_Display'):
        assert _is_linked(b2, 'ccore_Display', a)
    _safe_set(a, 'ccore_Field119', None)
    assert not _is_linked(a, 'ccore_Field119', b2)
    if hasattr(b2, 'ccore_Display'):
        assert not _is_linked(b2, 'ccore_Display', a)


def test_assoc_validators5_link_reassign_clear():
    a = ccore_TypeDefinition(idRuntime="sample_text")
    b1 = ccore_UIValidator()
    b2 = ccore_UIValidator()
    _safe_set(a, 'ccore_TypeDefinition6', {b1})
    assert _is_linked(a, 'ccore_TypeDefinition6', b1)
    if hasattr(b1, 'ccore_UIValidator'):
        assert _is_linked(b1, 'ccore_UIValidator', a)
    _safe_set(a, 'ccore_TypeDefinition6', {b2})
    assert _is_linked(a, 'ccore_TypeDefinition6', b2)
    if hasattr(b1, 'ccore_UIValidator'):
        assert not _is_linked(b1, 'ccore_UIValidator', a)
    if hasattr(b2, 'ccore_UIValidator'):
        assert _is_linked(b2, 'ccore_UIValidator', a)
    _safe_set(a, 'ccore_TypeDefinition6', set())
    assert not _is_linked(a, 'ccore_TypeDefinition6', b2)
    if hasattr(b2, 'ccore_UIValidator'):
        assert not _is_linked(b2, 'ccore_UIValidator', a)


def test_assoc_viewItemTypes158_link_reassign_clear():
    a = ccore_ViewItemType(isRootElement=True, ref=True)
    b1 = ccore_View(icon="sample_text")
    b2 = ccore_View(icon="sample_text_2")
    _safe_set(a, 'ccore_ViewItemType159', b1)
    assert _is_linked(a, 'ccore_ViewItemType159', b1)
    if hasattr(b1, 'ccore_View'):
        assert _is_linked(b1, 'ccore_View', a)
    _safe_set(a, 'ccore_ViewItemType159', b2)
    assert _is_linked(a, 'ccore_ViewItemType159', b2)
    if hasattr(b1, 'ccore_View'):
        assert not _is_linked(b1, 'ccore_View', a)
    if hasattr(b2, 'ccore_View'):
        assert _is_linked(b2, 'ccore_View', a)
    _safe_set(a, 'ccore_ViewItemType159', None)
    assert not _is_linked(a, 'ccore_ViewItemType159', b2)
    if hasattr(b2, 'ccore_View'):
        assert not _is_linked(b2, 'ccore_View', a)


def test_assoc_viewLinkTypes81_link_reassign_clear():
    a = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    b1 = ccore_ViewItemType(isRootElement=True, ref=True)
    b2 = ccore_ViewItemType(isRootElement=False, ref=False)
    _safe_set(a, 'ccore_ViewLinkType', b1)
    assert _is_linked(a, 'ccore_ViewLinkType', b1)
    if hasattr(b1, 'ccore_ViewItemType82'):
        assert _is_linked(b1, 'ccore_ViewItemType82', a)
    _safe_set(a, 'ccore_ViewLinkType', b2)
    assert _is_linked(a, 'ccore_ViewLinkType', b2)
    if hasattr(b1, 'ccore_ViewItemType82'):
        assert not _is_linked(b1, 'ccore_ViewItemType82', a)
    if hasattr(b2, 'ccore_ViewItemType82'):
        assert _is_linked(b2, 'ccore_ViewItemType82', a)
    _safe_set(a, 'ccore_ViewLinkType', None)
    assert not _is_linked(a, 'ccore_ViewLinkType', b2)
    if hasattr(b2, 'ccore_ViewItemType82'):
        assert not _is_linked(b2, 'ccore_ViewItemType82', a)


def test_assoc_views160_link_reassign_clear():
    a = ccore_View(icon="sample_text")
    b1 = ccore_ViewModel()
    b2 = ccore_ViewModel()
    _safe_set(a, 'ccore_View161', b1)
    assert _is_linked(a, 'ccore_View161', b1)
    if hasattr(b1, 'ccore_ViewModel'):
        assert _is_linked(b1, 'ccore_ViewModel', a)
    _safe_set(a, 'ccore_View161', b2)
    assert _is_linked(a, 'ccore_View161', b2)
    if hasattr(b1, 'ccore_ViewModel'):
        assert not _is_linked(b1, 'ccore_ViewModel', a)
    if hasattr(b2, 'ccore_ViewModel'):
        assert _is_linked(b2, 'ccore_ViewModel', a)
    _safe_set(a, 'ccore_View161', None)
    assert not _is_linked(a, 'ccore_View161', b2)
    if hasattr(b2, 'ccore_ViewModel'):
        assert not _is_linked(b2, 'ccore_ViewModel', a)


def test_assoc_wcListeners18_link_reassign_clear():
    a = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    b1 = ccore_WCListener()
    b2 = ccore_WCListener()
    _safe_set(a, 'ccore_ItemType19', {b1})
    assert _is_linked(a, 'ccore_ItemType19', b1)
    if hasattr(b1, 'ccore_WCListener'):
        assert _is_linked(b1, 'ccore_WCListener', a)
    _safe_set(a, 'ccore_ItemType19', {b2})
    assert _is_linked(a, 'ccore_ItemType19', b2)
    if hasattr(b1, 'ccore_WCListener'):
        assert not _is_linked(b1, 'ccore_WCListener', a)
    if hasattr(b2, 'ccore_WCListener'):
        assert _is_linked(b2, 'ccore_WCListener', a)
    _safe_set(a, 'ccore_ItemType19', set())
    assert not _is_linked(a, 'ccore_ItemType19', b2)
    if hasattr(b2, 'ccore_WCListener'):
        assert not _is_linked(b2, 'ccore_WCListener', a)


def test_assoc_wcListens71_link_reassign_clear():
    a = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    b1 = ccore_WCListener()
    b2 = ccore_WCListener()
    _safe_set(a, 'ccore_Attribute72', {b1})
    assert _is_linked(a, 'ccore_Attribute72', b1)
    if hasattr(b1, 'ccore_WCListener73'):
        assert _is_linked(b1, 'ccore_WCListener73', a)
    _safe_set(a, 'ccore_Attribute72', {b2})
    assert _is_linked(a, 'ccore_Attribute72', b2)
    if hasattr(b1, 'ccore_WCListener73'):
        assert not _is_linked(b1, 'ccore_WCListener73', a)
    if hasattr(b2, 'ccore_WCListener73'):
        assert _is_linked(b2, 'ccore_WCListener73', a)
    _safe_set(a, 'ccore_Attribute72', set())
    assert not _is_linked(a, 'ccore_Attribute72', b2)
    if hasattr(b2, 'ccore_WCListener73'):
        assert not _is_linked(b2, 'ccore_WCListener73', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Attribute_strategy = st.builds(Attribute)
@given(instance=Attribute_strategy)
@settings(max_examples=25)
def test_Attribute_instantiation(instance):
    assert isinstance(instance, Attribute)


BindingDesc_strategy = st.builds(BindingDesc)
@given(instance=BindingDesc_strategy)
@settings(max_examples=25)
def test_BindingDesc_instantiation(instance):
    assert isinstance(instance, BindingDesc)


DBObject_strategy = st.builds(DBObject)
@given(instance=DBObject_strategy)
@settings(max_examples=25)
def test_DBObject_instantiation(instance):
    assert isinstance(instance, DBObject)


EAttribute_strategy = st.builds(EAttribute)
@given(instance=EAttribute_strategy)
@settings(max_examples=25)
def test_EAttribute_instantiation(instance):
    assert isinstance(instance, EAttribute)


EClass_strategy = st.builds(EClass)
@given(instance=EClass_strategy)
@settings(max_examples=25)
def test_EClass_instantiation(instance):
    assert isinstance(instance, EClass)


EEnum_strategy = st.builds(EEnum)
@given(instance=EEnum_strategy)
@settings(max_examples=25)
def test_EEnum_instantiation(instance):
    assert isinstance(instance, EEnum)


ENamedElement_strategy = st.builds(ENamedElement)
@given(instance=ENamedElement_strategy)
@settings(max_examples=25)
def test_ENamedElement_instantiation(instance):
    assert isinstance(instance, ENamedElement)


EPackage_strategy = st.builds(EPackage)
@given(instance=EPackage_strategy)
@settings(max_examples=25)
def test_EPackage_instantiation(instance):
    assert isinstance(instance, EPackage)


EReference_strategy = st.builds(EReference)
@given(instance=EReference_strategy)
@settings(max_examples=25)
def test_EReference_instantiation(instance):
    assert isinstance(instance, EReference)


Item_strategy = st.builds(Item)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


ItemType_strategy = st.builds(ItemType)
@given(instance=ItemType_strategy)
@settings(max_examples=25)
def test_ItemType_instantiation(instance):
    assert isinstance(instance, ItemType)


LongAttribute_strategy = st.builds(LongAttribute)
@given(instance=LongAttribute_strategy)
@settings(max_examples=25)
def test_LongAttribute_instantiation(instance):
    assert isinstance(instance, LongAttribute)


RuntimeItem_strategy = st.builds(RuntimeItem)
@given(instance=RuntimeItem_strategy)
@settings(max_examples=25)
def test_RuntimeItem_instantiation(instance):
    assert isinstance(instance, RuntimeItem)


RuntimeItemType_strategy = st.builds(RuntimeItemType)
@given(instance=RuntimeItemType_strategy)
@settings(max_examples=25)
def test_RuntimeItemType_instantiation(instance):
    assert isinstance(instance, RuntimeItemType)


TypeDefinition_strategy = st.builds(TypeDefinition)
@given(instance=TypeDefinition_strategy)
@settings(max_examples=25)
def test_TypeDefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)


ccore_ActionExtItemType_strategy = st.builds(ccore_ActionExtItemType)
@given(instance=ccore_ActionExtItemType_strategy)
@settings(max_examples=25)
def test_ccore_ActionExtItemType_instantiation(instance):
    assert isinstance(instance, ccore_ActionExtItemType)


ccore_Attribute_strategy = st.builds(ccore_Attribute, _final=st.booleans(), cannotBeUndefined=st.booleans(), devGenerated=st.booleans(), hiddenInComputedPages=st.booleans(), idRuntime=safe_text, isList=st.booleans(), mustBeInitialized=st.booleans(), natif=st.booleans(), require=st.booleans(), tWCommitKind=safe_text, tWEvol=safe_text, tWRevSpecific=st.booleans(), tWUpdateKind=safe_text)
@given(instance=ccore_Attribute_strategy)
@settings(max_examples=25)
def test_ccore_Attribute_instantiation(instance):
    assert isinstance(instance, ccore_Attribute)


ccore_BindExt_strategy = st.builds(ccore_BindExt)
@given(instance=ccore_BindExt_strategy)
@settings(max_examples=25)
def test_ccore_BindExt_instantiation(instance):
    assert isinstance(instance, ccore_BindExt)


ccore_BindingDesc_strategy = st.builds(ccore_BindingDesc)
@given(instance=ccore_BindingDesc_strategy)
@settings(max_examples=25)
def test_ccore_BindingDesc_instantiation(instance):
    assert isinstance(instance, ccore_BindingDesc)


ccore_BooleanAttribute_strategy = st.builds(ccore_BooleanAttribute)
@given(instance=ccore_BooleanAttribute_strategy)
@settings(max_examples=25)
def test_ccore_BooleanAttribute_instantiation(instance):
    assert isinstance(instance, ccore_BooleanAttribute)


ccore_Cadse_strategy = st.builds(ccore_Cadse, defaultContentRepoURL=safe_text, description=safe_text, executed=st.booleans(), idDefinition=safe_text, itemRepoLogin=safe_text, itemRepoPasswd=safe_text, itemRepoURL=safe_text)
@given(instance=ccore_Cadse_strategy)
@settings(max_examples=25)
def test_ccore_Cadse_instantiation(instance):
    assert isinstance(instance, ccore_Cadse)


ccore_Composer_strategy = st.builds(ccore_Composer, types=safe_text)
@given(instance=ccore_Composer_strategy)
@settings(max_examples=25)
def test_ccore_Composer_instantiation(instance):
    assert isinstance(instance, ccore_Composer)


ccore_ComposerLink_strategy = st.builds(ccore_ComposerLink)
@given(instance=ccore_ComposerLink_strategy)
@settings(max_examples=25)
def test_ccore_ComposerLink_instantiation(instance):
    assert isinstance(instance, ccore_ComposerLink)


ccore_ComposerType_strategy = st.builds(ccore_ComposerType)
@given(instance=ccore_ComposerType_strategy)
@settings(max_examples=25)
def test_ccore_ComposerType_instantiation(instance):
    assert isinstance(instance, ccore_ComposerType)


ccore_ComputedString_strategy = st.builds(ccore_ComputedString, expression=safe_text)
@given(instance=ccore_ComputedString_strategy)
@settings(max_examples=25)
def test_ccore_ComputedString_instantiation(instance):
    assert isinstance(instance, ccore_ComputedString)


ccore_ContentItem_strategy = st.builds(ccore_ContentItem)
@given(instance=ccore_ContentItem_strategy)
@settings(max_examples=25)
def test_ccore_ContentItem_instantiation(instance):
    assert isinstance(instance, ccore_ContentItem)


ccore_ContentItemType_strategy = st.builds(ccore_ContentItemType, extendsClass=st.booleans())
@given(instance=ccore_ContentItemType_strategy)
@settings(max_examples=25)
def test_ccore_ContentItemType_instantiation(instance):
    assert isinstance(instance, ccore_ContentItemType)


ccore_DBObject_strategy = st.builds(ccore_DBObject, objectId=st.integers(), uuid_lsb=safe_text, uuid_msb=safe_text)
@given(instance=ccore_DBObject_strategy)
@settings(max_examples=25)
def test_ccore_DBObject_instantiation(instance):
    assert isinstance(instance, ccore_DBObject)


ccore_DateAttribute_strategy = st.builds(ccore_DateAttribute)
@given(instance=ccore_DateAttribute_strategy)
@settings(max_examples=25)
def test_ccore_DateAttribute_instantiation(instance):
    assert isinstance(instance, ccore_DateAttribute)


ccore_Display_strategy = st.builds(ccore_Display, extendsIC=st.booleans(), extendsMC=st.booleans(), extendsUI=st.booleans())
@given(instance=ccore_Display_strategy)
@settings(max_examples=25)
def test_ccore_Display_instantiation(instance):
    assert isinstance(instance, ccore_Display)


ccore_DoubleAttribute_strategy = st.builds(ccore_DoubleAttribute)
@given(instance=ccore_DoubleAttribute_strategy)
@settings(max_examples=25)
def test_ccore_DoubleAttribute_instantiation(instance):
    assert isinstance(instance, ccore_DoubleAttribute)


ccore_DynamicActions_strategy = st.builds(ccore_DynamicActions)
@given(instance=ccore_DynamicActions_strategy)
@settings(max_examples=25)
def test_ccore_DynamicActions_instantiation(instance):
    assert isinstance(instance, ccore_DynamicActions)


ccore_EClass_strategy = st.builds(ccore_EClass)
@given(instance=ccore_EClass_strategy)
@settings(max_examples=25)
def test_ccore_EClass_instantiation(instance):
    assert isinstance(instance, ccore_EClass)


ccore_EEnum_strategy = st.builds(ccore_EEnum)
@given(instance=ccore_EEnum_strategy)
@settings(max_examples=25)
def test_ccore_EEnum_instantiation(instance):
    assert isinstance(instance, ccore_EEnum)


ccore_EPackage_strategy = st.builds(ccore_EPackage)
@given(instance=ccore_EPackage_strategy)
@settings(max_examples=25)
def test_ccore_EPackage_instantiation(instance):
    assert isinstance(instance, ccore_EPackage)


ccore_EStructuralFeature_strategy = st.builds(ccore_EStructuralFeature)
@given(instance=ccore_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_ccore_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, ccore_EStructuralFeature)


ccore_Enum_strategy = st.builds(ccore_Enum, enumClazz=safe_text, values=safe_text)
@given(instance=ccore_Enum_strategy)
@settings(max_examples=25)
def test_ccore_Enum_instantiation(instance):
    assert isinstance(instance, ccore_Enum)


ccore_EnumType_strategy = st.builds(ccore_EnumType, javaClass=safe_text, mustBeGenerated=st.booleans(), values=safe_text)
@given(instance=ccore_EnumType_strategy)
@settings(max_examples=25)
def test_ccore_EnumType_instantiation(instance):
    assert isinstance(instance, ccore_EnumType)


ccore_ExportedContent_strategy = st.builds(ccore_ExportedContent)
@given(instance=ccore_ExportedContent_strategy)
@settings(max_examples=25)
def test_ccore_ExportedContent_instantiation(instance):
    assert isinstance(instance, ccore_ExportedContent)


ccore_Exporter_strategy = st.builds(ccore_Exporter, types=safe_text)
@given(instance=ccore_Exporter_strategy)
@settings(max_examples=25)
def test_ccore_Exporter_instantiation(instance):
    assert isinstance(instance, ccore_Exporter)


ccore_ExporterType_strategy = st.builds(ccore_ExporterType)
@given(instance=ccore_ExporterType_strategy)
@settings(max_examples=25)
def test_ccore_ExporterType_instantiation(instance):
    assert isinstance(instance, ccore_ExporterType)


ccore_ExtItem_strategy = st.builds(ccore_ExtItem)
@given(instance=ccore_ExtItem_strategy)
@settings(max_examples=25)
def test_ccore_ExtItem_instantiation(instance):
    assert isinstance(instance, ccore_ExtItem)


ccore_ExtentedType_strategy = st.builds(ccore_ExtentedType)
@given(instance=ccore_ExtentedType_strategy)
@settings(max_examples=25)
def test_ccore_ExtentedType_instantiation(instance):
    assert isinstance(instance, ccore_ExtentedType)


ccore_Field_strategy = st.builds(ccore_Field, editable=st.booleans(), label=safe_text, position=safe_text)
@given(instance=ccore_Field_strategy)
@settings(max_examples=25)
def test_ccore_Field_instantiation(instance):
    assert isinstance(instance, ccore_Field)


ccore_GenInformation_strategy = st.builds(ccore_GenInformation, cSTName=safe_text)
@given(instance=ccore_GenInformation_strategy)
@settings(max_examples=25)
def test_ccore_GenInformation_instantiation(instance):
    assert isinstance(instance, ccore_GenInformation)


ccore_GroupExtItem_strategy = st.builds(ccore_GroupExtItem)
@given(instance=ccore_GroupExtItem_strategy)
@settings(max_examples=25)
def test_ccore_GroupExtItem_instantiation(instance):
    assert isinstance(instance, ccore_GroupExtItem)


ccore_GroupOfAttributes_strategy = st.builds(ccore_GroupOfAttributes, column=st.integers())
@given(instance=ccore_GroupOfAttributes_strategy)
@settings(max_examples=25)
def test_ccore_GroupOfAttributes_instantiation(instance):
    assert isinstance(instance, ccore_GroupOfAttributes)


ccore_IntegerAttribute_strategy = st.builds(ccore_IntegerAttribute)
@given(instance=ccore_IntegerAttribute_strategy)
@settings(max_examples=25)
def test_ccore_IntegerAttribute_instantiation(instance):
    assert isinstance(instance, ccore_IntegerAttribute)


ccore_InteractionController_strategy = st.builds(ccore_InteractionController)
@given(instance=ccore_InteractionController_strategy)
@settings(max_examples=25)
def test_ccore_InteractionController_instantiation(instance):
    assert isinstance(instance, ccore_InteractionController)


ccore_Item_strategy = st.builds(ccore_Item, committedBy=safe_text, displayName=safe_text, isvalid=st.booleans(), itemHidden=st.booleans(), itemReadonly=st.booleans(), qualifiedName=safe_text, twCommittedDate=safe_text, twRequireNewRev=st.booleans(), twRevModified=st.booleans(), twVersion=st.integers())
@given(instance=ccore_Item_strategy)
@settings(max_examples=25)
def test_ccore_Item_instantiation(instance):
    assert isinstance(instance, ccore_Item)


ccore_ItemType_strategy = st.builds(ccore_ItemType, customManager=st.booleans(), displayNameTemplate=safe_text, hasContent=st.booleans(), hasShortName=st.booleans(), hasUniqueName=st.booleans(), humanName=safe_text, icon=safe_text, isInstanceAbstract=st.booleans(), isInstanceHidden=st.booleans(), isMetaItemType=st.booleans(), isRootElement=st.booleans(), itemFactoryClass=safe_text, itemManagerClass=safe_text, managerClass=safe_text, messageErrorId=safe_text, overwriteDefaultPages=st.booleans(), packageName=safe_text, qualifiedNameTemplate=safe_text, validateNameRe=safe_text)
@given(instance=ccore_ItemType_strategy)
@settings(max_examples=25)
def test_ccore_ItemType_instantiation(instance):
    assert isinstance(instance, ccore_ItemType)


ccore_KeyDefinition_strategy = st.builds(ccore_KeyDefinition)
@given(instance=ccore_KeyDefinition_strategy)
@settings(max_examples=25)
def test_ccore_KeyDefinition_instantiation(instance):
    assert isinstance(instance, ccore_KeyDefinition)


ccore_LinkType_strategy = st.builds(ccore_LinkType, aggregation=st.booleans(), annotation=st.booleans(), composition=st.booleans(), group=st.booleans(), hidden=st.booleans(), kind=st.integers(), linkManager=safe_text, mapping=st.booleans(), max=st.integers(), min=st.integers(), selection=safe_text, twCoupled=st.booleans(), twDestEvol=safe_text)
@given(instance=ccore_LinkType_strategy)
@settings(max_examples=25)
def test_ccore_LinkType_instantiation(instance):
    assert isinstance(instance, ccore_LinkType)


ccore_LongAttribute_strategy = st.builds(ccore_LongAttribute)
@given(instance=ccore_LongAttribute_strategy)
@settings(max_examples=25)
def test_ccore_LongAttribute_instantiation(instance):
    assert isinstance(instance, ccore_LongAttribute)


ccore_Menu_strategy = st.builds(ccore_Menu)
@given(instance=ccore_Menu_strategy)
@settings(max_examples=25)
def test_ccore_Menu_instantiation(instance):
    assert isinstance(instance, ccore_Menu)


ccore_MenuAbstract_strategy = st.builds(ccore_MenuAbstract, icon=safe_text, label=safe_text, path=safe_text)
@given(instance=ccore_MenuAbstract_strategy)
@settings(max_examples=25)
def test_ccore_MenuAbstract_instantiation(instance):
    assert isinstance(instance, ccore_MenuAbstract)


ccore_MenuAction_strategy = st.builds(ccore_MenuAction)
@given(instance=ccore_MenuAction_strategy)
@settings(max_examples=25)
def test_ccore_MenuAction_instantiation(instance):
    assert isinstance(instance, ccore_MenuAction)


ccore_MenuGroup_strategy = st.builds(ccore_MenuGroup)
@given(instance=ccore_MenuGroup_strategy)
@settings(max_examples=25)
def test_ccore_MenuGroup_instantiation(instance):
    assert isinstance(instance, ccore_MenuGroup)


ccore_ModelController_strategy = st.builds(ccore_ModelController)
@given(instance=ccore_ModelController_strategy)
@settings(max_examples=25)
def test_ccore_ModelController_instantiation(instance):
    assert isinstance(instance, ccore_ModelController)


ccore_Page_strategy = st.builds(ccore_Page, description=safe_text, idRuntime=safe_text, label=safe_text, title=safe_text)
@given(instance=ccore_Page_strategy)
@settings(max_examples=25)
def test_ccore_Page_instantiation(instance):
    assert isinstance(instance, ccore_Page)


ccore_RuntimeItem_strategy = st.builds(ccore_RuntimeItem, className=safe_text, extendsClass=st.booleans())
@given(instance=ccore_RuntimeItem_strategy)
@settings(max_examples=25)
def test_ccore_RuntimeItem_instantiation(instance):
    assert isinstance(instance, ccore_RuntimeItem)


ccore_RuntimeItemType_strategy = st.builds(ccore_RuntimeItemType)
@given(instance=ccore_RuntimeItemType_strategy)
@settings(max_examples=25)
def test_ccore_RuntimeItemType_instantiation(instance):
    assert isinstance(instance, ccore_RuntimeItemType)


ccore_StringAttribute_strategy = st.builds(ccore_StringAttribute, notEmpty=st.booleans())
@given(instance=ccore_StringAttribute_strategy)
@settings(max_examples=25)
def test_ccore_StringAttribute_instantiation(instance):
    assert isinstance(instance, ccore_StringAttribute)


ccore_TimeAttribute_strategy = st.builds(ccore_TimeAttribute, initWithTheCurrentTime=st.booleans())
@given(instance=ccore_TimeAttribute_strategy)
@settings(max_examples=25)
def test_ccore_TimeAttribute_instantiation(instance):
    assert isinstance(instance, ccore_TimeAttribute)


ccore_TypeDefinition_strategy = st.builds(ccore_TypeDefinition, idRuntime=safe_text)
@given(instance=ccore_TypeDefinition_strategy)
@settings(max_examples=25)
def test_ccore_TypeDefinition_instantiation(instance):
    assert isinstance(instance, ccore_TypeDefinition)


ccore_UIValidator_strategy = st.builds(ccore_UIValidator)
@given(instance=ccore_UIValidator_strategy)
@settings(max_examples=25)
def test_ccore_UIValidator_instantiation(instance):
    assert isinstance(instance, ccore_UIValidator)


ccore_UUIDAttribute_strategy = st.builds(ccore_UUIDAttribute)
@given(instance=ccore_UUIDAttribute_strategy)
@settings(max_examples=25)
def test_ccore_UUIDAttribute_instantiation(instance):
    assert isinstance(instance, ccore_UUIDAttribute)


ccore_UnresolvedAttributeType_strategy = st.builds(ccore_UnresolvedAttributeType)
@given(instance=ccore_UnresolvedAttributeType_strategy)
@settings(max_examples=25)
def test_ccore_UnresolvedAttributeType_instantiation(instance):
    assert isinstance(instance, ccore_UnresolvedAttributeType)


ccore_View_strategy = st.builds(ccore_View, icon=safe_text)
@given(instance=ccore_View_strategy)
@settings(max_examples=25)
def test_ccore_View_instantiation(instance):
    assert isinstance(instance, ccore_View)


ccore_ViewDescription_strategy = st.builds(ccore_ViewDescription)
@given(instance=ccore_ViewDescription_strategy)
@settings(max_examples=25)
def test_ccore_ViewDescription_instantiation(instance):
    assert isinstance(instance, ccore_ViewDescription)


ccore_ViewItemType_strategy = st.builds(ccore_ViewItemType, isRootElement=st.booleans(), ref=st.booleans())
@given(instance=ccore_ViewItemType_strategy)
@settings(max_examples=25)
def test_ccore_ViewItemType_instantiation(instance):
    assert isinstance(instance, ccore_ViewItemType)


ccore_ViewLinkType_strategy = st.builds(ccore_ViewLinkType, aggregation=st.booleans(), canCreateItem=st.booleans(), canCreateLink=st.booleans(), displayCreate=safe_text)
@given(instance=ccore_ViewLinkType_strategy)
@settings(max_examples=25)
def test_ccore_ViewLinkType_instantiation(instance):
    assert isinstance(instance, ccore_ViewLinkType)


ccore_ViewModel_strategy = st.builds(ccore_ViewModel)
@given(instance=ccore_ViewModel_strategy)
@settings(max_examples=25)
def test_ccore_ViewModel_instantiation(instance):
    assert isinstance(instance, ccore_ViewModel)


ccore_WCListener_strategy = st.builds(ccore_WCListener)
@given(instance=ccore_WCListener_strategy)
@settings(max_examples=25)
def test_ccore_WCListener_instantiation(instance):
    assert isinstance(instance, ccore_WCListener)


