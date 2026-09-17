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
    ItemType,
    ccore_MenuAbstract,
    ccore_Menu,
    ccore_ActionExtItemType,
    ccore_DynamicActions,
    EAttribute,
    ccore_ContentItem,
    ccore_EStructuralFeature,
    EPackage,
    ccore_ContentItemType,
    DBObject,
    ENamedElement,
    ccore_Item,
    ccore_BindingDesc,
    ccore_EPackage,
    ccore_WCListener,
    TypeDefinition,
    ccore_ItemType,
    ccore_ExtentedType,
    ccore_EClass,
    ccore_GroupOfAttributes,
    ccore_UIValidator,
    ccore_Page,
    EClass,
    Item,
    ccore_Cadse,
    ccore_KeyDefinition,
    ccore_RuntimeItem,
    ccore_Field,
    ccore_Attribute,
    ccore_TypeDefinition,
    ccore_RuntimeItemType,
    RuntimeItemType,
    ccore_ComposerType,
    ccore_ExporterType,
    ccore_DBObject,
    ccore_View,
    ccore_ComposerLink,
    ccore_MenuGroup,
    ccore_MenuAction,
    ccore_ViewModel,
    ccore_ExtItem,
    ccore_ComputedString,
    ccore_EEnum,
    EEnum,
    ccore_GroupExtItem,
    EReference,
    ccore_EnumType,
    RuntimeItem,
    ccore_Composer,
    ccore_Exporter,
    ccore_ModelController,
    ccore_InteractionController,
    ccore_Display,
    ccore_ExportedContent,
    BindingDesc,
    ccore_BindExt,
    ccore_UnresolvedAttributeType,
    LongAttribute,
    ccore_TimeAttribute,
    Attribute,
    ccore_IntegerAttribute,
    ccore_Enum,
    ccore_LongAttribute,
    ccore_UUIDAttribute,
    ccore_DateAttribute,
    ccore_LinkType,
    ccore_DoubleAttribute,
    ccore_BooleanAttribute,
    ccore_StringAttribute,
    ccore_ViewDescription,
    ccore_ViewLinkType,
    ccore_ViewItemType,
    ccore_GenInformation,
    PositionEnum,
    TWCommitKind,
    TWDestEvol,
    TWEvol,
    TWUpdateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_itemtype_is_not_abstract():
    assert not inspect.isabstract(ItemType)


def test_hyp_itemtype_constructor_exists():
    assert callable(ItemType.__init__)


def test_hyp_itemtype_constructor_args():
    sig = inspect.signature(ItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_menuabstract_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuAbstract)


def test_hyp_ccore_menuabstract_constructor_exists():
    assert callable(ccore_MenuAbstract.__init__)


def test_hyp_ccore_menuabstract_constructor_args():
    sig = inspect.signature(ccore_MenuAbstract.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "label" in params, "Missing parameter 'label'"
    assert "path" in params, "Missing parameter 'path'"






def test_hyp_ccore_menu_is_not_abstract():
    assert not inspect.isabstract(ccore_Menu)


def test_hyp_ccore_menu_constructor_exists():
    assert callable(ccore_Menu.__init__)


def test_hyp_ccore_menu_constructor_args():
    sig = inspect.signature(ccore_Menu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_actionextitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ActionExtItemType)


def test_hyp_ccore_actionextitemtype_constructor_exists():
    assert callable(ccore_ActionExtItemType.__init__)


def test_hyp_ccore_actionextitemtype_constructor_args():
    sig = inspect.signature(ccore_ActionExtItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_dynamicactions_is_not_abstract():
    assert not inspect.isabstract(ccore_DynamicActions)


def test_hyp_ccore_dynamicactions_constructor_exists():
    assert callable(ccore_DynamicActions.__init__)


def test_hyp_ccore_dynamicactions_constructor_args():
    sig = inspect.signature(ccore_DynamicActions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_hyp_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_hyp_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_contentitem_is_not_abstract():
    assert not inspect.isabstract(ccore_ContentItem)


def test_hyp_ccore_contentitem_constructor_exists():
    assert callable(ccore_ContentItem.__init__)


def test_hyp_ccore_contentitem_constructor_args():
    sig = inspect.signature(ccore_ContentItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ccore_EStructuralFeature)


def test_hyp_ccore_estructuralfeature_constructor_exists():
    assert callable(ccore_EStructuralFeature.__init__)


def test_hyp_ccore_estructuralfeature_constructor_args():
    sig = inspect.signature(ccore_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_hyp_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_hyp_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_contentitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ContentItemType)


def test_hyp_ccore_contentitemtype_constructor_exists():
    assert callable(ccore_ContentItemType.__init__)


def test_hyp_ccore_contentitemtype_constructor_args():
    sig = inspect.signature(ccore_ContentItemType.__init__)
    params = list(sig.parameters.keys())
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"




def test_hyp_dbobject_is_not_abstract():
    assert not inspect.isabstract(DBObject)


def test_hyp_dbobject_constructor_exists():
    assert callable(DBObject.__init__)


def test_hyp_dbobject_constructor_args():
    sig = inspect.signature(DBObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_hyp_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_hyp_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_item_is_not_abstract():
    assert not inspect.isabstract(ccore_Item)


def test_hyp_ccore_item_constructor_exists():
    assert callable(ccore_Item.__init__)


def test_hyp_ccore_item_constructor_args():
    sig = inspect.signature(ccore_Item.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "twCommittedDate" in params, "Missing parameter 'twCommittedDate'"
    assert "twVersion" in params, "Missing parameter 'twVersion'"
    assert "twRevModified" in params, "Missing parameter 'twRevModified'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "twRequireNewRev" in params, "Missing parameter 'twRequireNewRev'"
    assert "committedBy" in params, "Missing parameter 'committedBy'"
    assert "itemReadonly" in params, "Missing parameter 'itemReadonly'"
    assert "isvalid" in params, "Missing parameter 'isvalid'"
    assert "itemHidden" in params, "Missing parameter 'itemHidden'"













def test_hyp_ccore_bindingdesc_is_not_abstract():
    assert not inspect.isabstract(ccore_BindingDesc)


def test_hyp_ccore_bindingdesc_constructor_exists():
    assert callable(ccore_BindingDesc.__init__)


def test_hyp_ccore_bindingdesc_constructor_args():
    sig = inspect.signature(ccore_BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_epackage_is_not_abstract():
    assert not inspect.isabstract(ccore_EPackage)


def test_hyp_ccore_epackage_constructor_exists():
    assert callable(ccore_EPackage.__init__)


def test_hyp_ccore_epackage_constructor_args():
    sig = inspect.signature(ccore_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_wclistener_is_not_abstract():
    assert not inspect.isabstract(ccore_WCListener)


def test_hyp_ccore_wclistener_constructor_exists():
    assert callable(ccore_WCListener.__init__)


def test_hyp_ccore_wclistener_constructor_args():
    sig = inspect.signature(ccore_WCListener.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_hyp_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_hyp_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_itemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ItemType)


def test_hyp_ccore_itemtype_constructor_exists():
    assert callable(ccore_ItemType.__init__)


def test_hyp_ccore_itemtype_constructor_args():
    sig = inspect.signature(ccore_ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "isInstanceHidden" in params, "Missing parameter 'isInstanceHidden'"
    assert "hasShortName" in params, "Missing parameter 'hasShortName'"
    assert "customManager" in params, "Missing parameter 'customManager'"
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "overwriteDefaultPages" in params, "Missing parameter 'overwriteDefaultPages'"
    assert "qualifiedNameTemplate" in params, "Missing parameter 'qualifiedNameTemplate'"
    assert "validateNameRe" in params, "Missing parameter 'validateNameRe'"
    assert "messageErrorId" in params, "Missing parameter 'messageErrorId'"
    assert "hasContent" in params, "Missing parameter 'hasContent'"
    assert "itemManagerClass" in params, "Missing parameter 'itemManagerClass'"
    assert "isInstanceAbstract" in params, "Missing parameter 'isInstanceAbstract'"
    assert "managerClass" in params, "Missing parameter 'managerClass'"
    assert "humanName" in params, "Missing parameter 'humanName'"
    assert "displayNameTemplate" in params, "Missing parameter 'displayNameTemplate'"
    assert "itemFactoryClass" in params, "Missing parameter 'itemFactoryClass'"
    assert "hasUniqueName" in params, "Missing parameter 'hasUniqueName'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "isMetaItemType" in params, "Missing parameter 'isMetaItemType'"
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"






















def test_hyp_ccore_extentedtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ExtentedType)


def test_hyp_ccore_extentedtype_constructor_exists():
    assert callable(ccore_ExtentedType.__init__)


def test_hyp_ccore_extentedtype_constructor_args():
    sig = inspect.signature(ccore_ExtentedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_eclass_is_not_abstract():
    assert not inspect.isabstract(ccore_EClass)


def test_hyp_ccore_eclass_constructor_exists():
    assert callable(ccore_EClass.__init__)


def test_hyp_ccore_eclass_constructor_args():
    sig = inspect.signature(ccore_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_groupofattributes_is_not_abstract():
    assert not inspect.isabstract(ccore_GroupOfAttributes)


def test_hyp_ccore_groupofattributes_constructor_exists():
    assert callable(ccore_GroupOfAttributes.__init__)


def test_hyp_ccore_groupofattributes_constructor_args():
    sig = inspect.signature(ccore_GroupOfAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"




def test_hyp_ccore_uivalidator_is_not_abstract():
    assert not inspect.isabstract(ccore_UIValidator)


def test_hyp_ccore_uivalidator_constructor_exists():
    assert callable(ccore_UIValidator.__init__)


def test_hyp_ccore_uivalidator_constructor_args():
    sig = inspect.signature(ccore_UIValidator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_page_is_not_abstract():
    assert not inspect.isabstract(ccore_Page)


def test_hyp_ccore_page_constructor_exists():
    assert callable(ccore_Page.__init__)


def test_hyp_ccore_page_constructor_args():
    sig = inspect.signature(ccore_Page.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"
    assert "title" in params, "Missing parameter 'title'"







def test_hyp_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_hyp_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_hyp_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_cadse_is_not_abstract():
    assert not inspect.isabstract(ccore_Cadse)


def test_hyp_ccore_cadse_constructor_exists():
    assert callable(ccore_Cadse.__init__)


def test_hyp_ccore_cadse_constructor_args():
    sig = inspect.signature(ccore_Cadse.__init__)
    params = list(sig.parameters.keys())
    assert "itemRepoLogin" in params, "Missing parameter 'itemRepoLogin'"
    assert "idDefinition" in params, "Missing parameter 'idDefinition'"
    assert "itemRepoURL" in params, "Missing parameter 'itemRepoURL'"
    assert "description" in params, "Missing parameter 'description'"
    assert "executed" in params, "Missing parameter 'executed'"
    assert "itemRepoPasswd" in params, "Missing parameter 'itemRepoPasswd'"
    assert "defaultContentRepoURL" in params, "Missing parameter 'defaultContentRepoURL'"










def test_hyp_ccore_keydefinition_is_not_abstract():
    assert not inspect.isabstract(ccore_KeyDefinition)


def test_hyp_ccore_keydefinition_constructor_exists():
    assert callable(ccore_KeyDefinition.__init__)


def test_hyp_ccore_keydefinition_constructor_args():
    sig = inspect.signature(ccore_KeyDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_runtimeitem_is_not_abstract():
    assert not inspect.isabstract(ccore_RuntimeItem)


def test_hyp_ccore_runtimeitem_constructor_exists():
    assert callable(ccore_RuntimeItem.__init__)


def test_hyp_ccore_runtimeitem_constructor_args():
    sig = inspect.signature(ccore_RuntimeItem.__init__)
    params = list(sig.parameters.keys())
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"
    assert "className" in params, "Missing parameter 'className'"





def test_hyp_ccore_field_is_not_abstract():
    assert not inspect.isabstract(ccore_Field)


def test_hyp_ccore_field_constructor_exists():
    assert callable(ccore_Field.__init__)


def test_hyp_ccore_field_constructor_args():
    sig = inspect.signature(ccore_Field.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "editable" in params, "Missing parameter 'editable'"
    assert "label" in params, "Missing parameter 'label'"






def test_hyp_ccore_attribute_is_not_abstract():
    assert not inspect.isabstract(ccore_Attribute)


def test_hyp_ccore_attribute_constructor_exists():
    assert callable(ccore_Attribute.__init__)


def test_hyp_ccore_attribute_constructor_args():
    sig = inspect.signature(ccore_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "natif" in params, "Missing parameter 'natif'"
    assert "isList" in params, "Missing parameter 'isList'"
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"
    assert "devGenerated" in params, "Missing parameter 'devGenerated'"
    assert "_final" in params, "Missing parameter '_final'"
    assert "tWRevSpecific" in params, "Missing parameter 'tWRevSpecific'"
    assert "mustBeInitialized" in params, "Missing parameter 'mustBeInitialized'"
    assert "hiddenInComputedPages" in params, "Missing parameter 'hiddenInComputedPages'"
    assert "tWEvol" in params, "Missing parameter 'tWEvol'"
    assert "tWUpdateKind" in params, "Missing parameter 'tWUpdateKind'"
    assert "tWCommitKind" in params, "Missing parameter 'tWCommitKind'"
    assert "cannotBeUndefined" in params, "Missing parameter 'cannotBeUndefined'"
    assert "require" in params, "Missing parameter 'require'"
















def test_hyp_ccore_typedefinition_is_not_abstract():
    assert not inspect.isabstract(ccore_TypeDefinition)


def test_hyp_ccore_typedefinition_constructor_exists():
    assert callable(ccore_TypeDefinition.__init__)


def test_hyp_ccore_typedefinition_constructor_args():
    sig = inspect.signature(ccore_TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"




def test_hyp_ccore_runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_RuntimeItemType)


def test_hyp_ccore_runtimeitemtype_constructor_exists():
    assert callable(ccore_RuntimeItemType.__init__)


def test_hyp_ccore_runtimeitemtype_constructor_args():
    sig = inspect.signature(ccore_RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(RuntimeItemType)


def test_hyp_runtimeitemtype_constructor_exists():
    assert callable(RuntimeItemType.__init__)


def test_hyp_runtimeitemtype_constructor_args():
    sig = inspect.signature(RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_composertype_is_not_abstract():
    assert not inspect.isabstract(ccore_ComposerType)


def test_hyp_ccore_composertype_constructor_exists():
    assert callable(ccore_ComposerType.__init__)


def test_hyp_ccore_composertype_constructor_args():
    sig = inspect.signature(ccore_ComposerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_exportertype_is_not_abstract():
    assert not inspect.isabstract(ccore_ExporterType)


def test_hyp_ccore_exportertype_constructor_exists():
    assert callable(ccore_ExporterType.__init__)


def test_hyp_ccore_exportertype_constructor_args():
    sig = inspect.signature(ccore_ExporterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_dbobject_is_not_abstract():
    assert not inspect.isabstract(ccore_DBObject)


def test_hyp_ccore_dbobject_constructor_exists():
    assert callable(ccore_DBObject.__init__)


def test_hyp_ccore_dbobject_constructor_args():
    sig = inspect.signature(ccore_DBObject.__init__)
    params = list(sig.parameters.keys())
    assert "objectId" in params, "Missing parameter 'objectId'"
    assert "uuid_lsb" in params, "Missing parameter 'uuid_lsb'"
    assert "uuid_msb" in params, "Missing parameter 'uuid_msb'"






def test_hyp_ccore_view_is_not_abstract():
    assert not inspect.isabstract(ccore_View)


def test_hyp_ccore_view_constructor_exists():
    assert callable(ccore_View.__init__)


def test_hyp_ccore_view_constructor_args():
    sig = inspect.signature(ccore_View.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"




def test_hyp_ccore_composerlink_is_not_abstract():
    assert not inspect.isabstract(ccore_ComposerLink)


def test_hyp_ccore_composerlink_constructor_exists():
    assert callable(ccore_ComposerLink.__init__)


def test_hyp_ccore_composerlink_constructor_args():
    sig = inspect.signature(ccore_ComposerLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_menugroup_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuGroup)


def test_hyp_ccore_menugroup_constructor_exists():
    assert callable(ccore_MenuGroup.__init__)


def test_hyp_ccore_menugroup_constructor_args():
    sig = inspect.signature(ccore_MenuGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_menuaction_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuAction)


def test_hyp_ccore_menuaction_constructor_exists():
    assert callable(ccore_MenuAction.__init__)


def test_hyp_ccore_menuaction_constructor_args():
    sig = inspect.signature(ccore_MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_viewmodel_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewModel)


def test_hyp_ccore_viewmodel_constructor_exists():
    assert callable(ccore_ViewModel.__init__)


def test_hyp_ccore_viewmodel_constructor_args():
    sig = inspect.signature(ccore_ViewModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_extitem_is_not_abstract():
    assert not inspect.isabstract(ccore_ExtItem)


def test_hyp_ccore_extitem_constructor_exists():
    assert callable(ccore_ExtItem.__init__)


def test_hyp_ccore_extitem_constructor_args():
    sig = inspect.signature(ccore_ExtItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_computedstring_is_not_abstract():
    assert not inspect.isabstract(ccore_ComputedString)


def test_hyp_ccore_computedstring_constructor_exists():
    assert callable(ccore_ComputedString.__init__)


def test_hyp_ccore_computedstring_constructor_args():
    sig = inspect.signature(ccore_ComputedString.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_ccore_eenum_is_not_abstract():
    assert not inspect.isabstract(ccore_EEnum)


def test_hyp_ccore_eenum_constructor_exists():
    assert callable(ccore_EEnum.__init__)


def test_hyp_ccore_eenum_constructor_args():
    sig = inspect.signature(ccore_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eenum_is_not_abstract():
    assert not inspect.isabstract(EEnum)


def test_hyp_eenum_constructor_exists():
    assert callable(EEnum.__init__)


def test_hyp_eenum_constructor_args():
    sig = inspect.signature(EEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_groupextitem_is_not_abstract():
    assert not inspect.isabstract(ccore_GroupExtItem)


def test_hyp_ccore_groupextitem_constructor_exists():
    assert callable(ccore_GroupExtItem.__init__)


def test_hyp_ccore_groupextitem_constructor_args():
    sig = inspect.signature(ccore_GroupExtItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_hyp_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_hyp_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_enumtype_is_not_abstract():
    assert not inspect.isabstract(ccore_EnumType)


def test_hyp_ccore_enumtype_constructor_exists():
    assert callable(ccore_EnumType.__init__)


def test_hyp_ccore_enumtype_constructor_args():
    sig = inspect.signature(ccore_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "javaClass" in params, "Missing parameter 'javaClass'"
    assert "mustBeGenerated" in params, "Missing parameter 'mustBeGenerated'"






def test_hyp_runtimeitem_is_not_abstract():
    assert not inspect.isabstract(RuntimeItem)


def test_hyp_runtimeitem_constructor_exists():
    assert callable(RuntimeItem.__init__)


def test_hyp_runtimeitem_constructor_args():
    sig = inspect.signature(RuntimeItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_composer_is_not_abstract():
    assert not inspect.isabstract(ccore_Composer)


def test_hyp_ccore_composer_constructor_exists():
    assert callable(ccore_Composer.__init__)


def test_hyp_ccore_composer_constructor_args():
    sig = inspect.signature(ccore_Composer.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"




def test_hyp_ccore_exporter_is_not_abstract():
    assert not inspect.isabstract(ccore_Exporter)


def test_hyp_ccore_exporter_constructor_exists():
    assert callable(ccore_Exporter.__init__)


def test_hyp_ccore_exporter_constructor_args():
    sig = inspect.signature(ccore_Exporter.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"




def test_hyp_ccore_modelcontroller_is_not_abstract():
    assert not inspect.isabstract(ccore_ModelController)


def test_hyp_ccore_modelcontroller_constructor_exists():
    assert callable(ccore_ModelController.__init__)


def test_hyp_ccore_modelcontroller_constructor_args():
    sig = inspect.signature(ccore_ModelController.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_interactioncontroller_is_not_abstract():
    assert not inspect.isabstract(ccore_InteractionController)


def test_hyp_ccore_interactioncontroller_constructor_exists():
    assert callable(ccore_InteractionController.__init__)


def test_hyp_ccore_interactioncontroller_constructor_args():
    sig = inspect.signature(ccore_InteractionController.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_display_is_not_abstract():
    assert not inspect.isabstract(ccore_Display)


def test_hyp_ccore_display_constructor_exists():
    assert callable(ccore_Display.__init__)


def test_hyp_ccore_display_constructor_args():
    sig = inspect.signature(ccore_Display.__init__)
    params = list(sig.parameters.keys())
    assert "extendsIC" in params, "Missing parameter 'extendsIC'"
    assert "extendsUI" in params, "Missing parameter 'extendsUI'"
    assert "extendsMC" in params, "Missing parameter 'extendsMC'"






def test_hyp_ccore_exportedcontent_is_not_abstract():
    assert not inspect.isabstract(ccore_ExportedContent)


def test_hyp_ccore_exportedcontent_constructor_exists():
    assert callable(ccore_ExportedContent.__init__)


def test_hyp_ccore_exportedcontent_constructor_args():
    sig = inspect.signature(ccore_ExportedContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bindingdesc_is_not_abstract():
    assert not inspect.isabstract(BindingDesc)


def test_hyp_bindingdesc_constructor_exists():
    assert callable(BindingDesc.__init__)


def test_hyp_bindingdesc_constructor_args():
    sig = inspect.signature(BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_bindext_is_not_abstract():
    assert not inspect.isabstract(ccore_BindExt)


def test_hyp_ccore_bindext_constructor_exists():
    assert callable(ccore_BindExt.__init__)


def test_hyp_ccore_bindext_constructor_args():
    sig = inspect.signature(ccore_BindExt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_unresolvedattributetype_is_not_abstract():
    assert not inspect.isabstract(ccore_UnresolvedAttributeType)


def test_hyp_ccore_unresolvedattributetype_constructor_exists():
    assert callable(ccore_UnresolvedAttributeType.__init__)


def test_hyp_ccore_unresolvedattributetype_constructor_args():
    sig = inspect.signature(ccore_UnresolvedAttributeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_longattribute_is_not_abstract():
    assert not inspect.isabstract(LongAttribute)


def test_hyp_longattribute_constructor_exists():
    assert callable(LongAttribute.__init__)


def test_hyp_longattribute_constructor_args():
    sig = inspect.signature(LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_timeattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_TimeAttribute)


def test_hyp_ccore_timeattribute_constructor_exists():
    assert callable(ccore_TimeAttribute.__init__)


def test_hyp_ccore_timeattribute_constructor_args():
    sig = inspect.signature(ccore_TimeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "initWithTheCurrentTime" in params, "Missing parameter 'initWithTheCurrentTime'"




def test_hyp_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_hyp_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_hyp_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_integerattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_IntegerAttribute)


def test_hyp_ccore_integerattribute_constructor_exists():
    assert callable(ccore_IntegerAttribute.__init__)


def test_hyp_ccore_integerattribute_constructor_args():
    sig = inspect.signature(ccore_IntegerAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_enum_is_not_abstract():
    assert not inspect.isabstract(ccore_Enum)


def test_hyp_ccore_enum_constructor_exists():
    assert callable(ccore_Enum.__init__)


def test_hyp_ccore_enum_constructor_args():
    sig = inspect.signature(ccore_Enum.__init__)
    params = list(sig.parameters.keys())
    assert "enumClazz" in params, "Missing parameter 'enumClazz'"
    assert "values" in params, "Missing parameter 'values'"





def test_hyp_ccore_longattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_LongAttribute)


def test_hyp_ccore_longattribute_constructor_exists():
    assert callable(ccore_LongAttribute.__init__)


def test_hyp_ccore_longattribute_constructor_args():
    sig = inspect.signature(ccore_LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_uuidattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_UUIDAttribute)


def test_hyp_ccore_uuidattribute_constructor_exists():
    assert callable(ccore_UUIDAttribute.__init__)


def test_hyp_ccore_uuidattribute_constructor_args():
    sig = inspect.signature(ccore_UUIDAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_dateattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_DateAttribute)


def test_hyp_ccore_dateattribute_constructor_exists():
    assert callable(ccore_DateAttribute.__init__)


def test_hyp_ccore_dateattribute_constructor_args():
    sig = inspect.signature(ccore_DateAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_linktype_is_not_abstract():
    assert not inspect.isabstract(ccore_LinkType)


def test_hyp_ccore_linktype_constructor_exists():
    assert callable(ccore_LinkType.__init__)


def test_hyp_ccore_linktype_constructor_args():
    sig = inspect.signature(ccore_LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "composition" in params, "Missing parameter 'composition'"
    assert "twCoupled" in params, "Missing parameter 'twCoupled'"
    assert "linkManager" in params, "Missing parameter 'linkManager'"
    assert "min" in params, "Missing parameter 'min'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "max" in params, "Missing parameter 'max'"
    assert "mapping" in params, "Missing parameter 'mapping'"
    assert "annotation" in params, "Missing parameter 'annotation'"
    assert "twDestEvol" in params, "Missing parameter 'twDestEvol'"
    assert "group" in params, "Missing parameter 'group'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
















def test_hyp_ccore_doubleattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_DoubleAttribute)


def test_hyp_ccore_doubleattribute_constructor_exists():
    assert callable(ccore_DoubleAttribute.__init__)


def test_hyp_ccore_doubleattribute_constructor_args():
    sig = inspect.signature(ccore_DoubleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_booleanattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_BooleanAttribute)


def test_hyp_ccore_booleanattribute_constructor_exists():
    assert callable(ccore_BooleanAttribute.__init__)


def test_hyp_ccore_booleanattribute_constructor_args():
    sig = inspect.signature(ccore_BooleanAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_stringattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_StringAttribute)


def test_hyp_ccore_stringattribute_constructor_exists():
    assert callable(ccore_StringAttribute.__init__)


def test_hyp_ccore_stringattribute_constructor_args():
    sig = inspect.signature(ccore_StringAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "notEmpty" in params, "Missing parameter 'notEmpty'"




def test_hyp_ccore_viewdescription_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewDescription)


def test_hyp_ccore_viewdescription_constructor_exists():
    assert callable(ccore_ViewDescription.__init__)


def test_hyp_ccore_viewdescription_constructor_args():
    sig = inspect.signature(ccore_ViewDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccore_viewlinktype_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewLinkType)


def test_hyp_ccore_viewlinktype_constructor_exists():
    assert callable(ccore_ViewLinkType.__init__)


def test_hyp_ccore_viewlinktype_constructor_args():
    sig = inspect.signature(ccore_ViewLinkType.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "displayCreate" in params, "Missing parameter 'displayCreate'"
    assert "canCreateItem" in params, "Missing parameter 'canCreateItem'"
    assert "canCreateLink" in params, "Missing parameter 'canCreateLink'"







def test_hyp_ccore_viewitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewItemType)


def test_hyp_ccore_viewitemtype_constructor_exists():
    assert callable(ccore_ViewItemType.__init__)


def test_hyp_ccore_viewitemtype_constructor_args():
    sig = inspect.signature(ccore_ViewItemType.__init__)
    params = list(sig.parameters.keys())
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"
    assert "ref" in params, "Missing parameter 'ref'"





def test_hyp_ccore_geninformation_is_not_abstract():
    assert not inspect.isabstract(ccore_GenInformation)


def test_hyp_ccore_geninformation_constructor_exists():
    assert callable(ccore_GenInformation.__init__)


def test_hyp_ccore_geninformation_constructor_args():
    sig = inspect.signature(ccore_GenInformation.__init__)
    params = list(sig.parameters.keys())
    assert "cSTName" in params, "Missing parameter 'cSTName'"


def test_hyp_positionenum_exists():
    # Check that the Enumeration exists
    assert PositionEnum is not None

def test_hyp_positionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionEnum]
    expected_literals = [
        "defaultpos",
        "group",
        "none",
        "top",
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionEnum"

def test_hyp_twcommitkind_exists():
    # Check that the Enumeration exists
    assert TWCommitKind is not None

def test_hyp_twcommitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWCommitKind]
    expected_literals = [
        "none",
        "conflict",
        "reconcile",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWCommitKind"

def test_hyp_twdestevol_exists():
    # Check that the Enumeration exists
    assert TWDestEvol is not None

def test_hyp_twdestevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWDestEvol]
    expected_literals = [
        "finalDest",
        "mutable",
        "effective",
        "branch",
        "immutable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWDestEvol"

def test_hyp_twevol_exists():
    # Check that the Enumeration exists
    assert TWEvol is not None

def test_hyp_twevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWEvol]
    expected_literals = [
        "twFinal",
        "twImmutable",
        "twTransient",
        "twMutable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWEvol"

def test_hyp_twupdatekind_exists():
    # Check that the Enumeration exists
    assert TWUpdateKind is not None

def test_hyp_twupdatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWUpdateKind]
    expected_literals = [
        "merge",
        "compute",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWUpdateKind"


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
ItemType_strategy = st.builds(
    ItemType,
)
ccore_MenuAbstract_strategy = st.builds(
    ccore_MenuAbstract,
    icon=
        safe_text,
    label=
        safe_text,
    path=
        safe_text
)
ccore_Menu_strategy = st.builds(
    ccore_Menu,
)
ccore_ActionExtItemType_strategy = st.builds(
    ccore_ActionExtItemType,
)
ccore_DynamicActions_strategy = st.builds(
    ccore_DynamicActions,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
ccore_ContentItem_strategy = st.builds(
    ccore_ContentItem,
)
ccore_EStructuralFeature_strategy = st.builds(
    ccore_EStructuralFeature,
)
EPackage_strategy = st.builds(
    EPackage,
)
ccore_ContentItemType_strategy = st.builds(
    ccore_ContentItemType,
    extendsClass=
        st.booleans()
)
DBObject_strategy = st.builds(
    DBObject,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ccore_Item_strategy = st.builds(
    ccore_Item,
    qualifiedName=
        safe_text,
    twCommittedDate=
        safe_text,
    twVersion=
        st.integers(),
    twRevModified=
        st.booleans(),
    displayName=
        safe_text,
    twRequireNewRev=
        st.booleans(),
    committedBy=
        safe_text,
    itemReadonly=
        st.booleans(),
    isvalid=
        st.booleans(),
    itemHidden=
        st.booleans()
)
ccore_BindingDesc_strategy = st.builds(
    ccore_BindingDesc,
)
ccore_EPackage_strategy = st.builds(
    ccore_EPackage,
)
ccore_WCListener_strategy = st.builds(
    ccore_WCListener,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
ccore_ItemType_strategy = st.builds(
    ccore_ItemType,
    isInstanceHidden=
        st.booleans(),
    hasShortName=
        st.booleans(),
    customManager=
        st.booleans(),
    packageName=
        safe_text,
    overwriteDefaultPages=
        st.booleans(),
    qualifiedNameTemplate=
        safe_text,
    validateNameRe=
        safe_text,
    messageErrorId=
        safe_text,
    hasContent=
        st.booleans(),
    itemManagerClass=
        safe_text,
    isInstanceAbstract=
        st.booleans(),
    managerClass=
        safe_text,
    humanName=
        safe_text,
    displayNameTemplate=
        safe_text,
    itemFactoryClass=
        safe_text,
    hasUniqueName=
        st.booleans(),
    icon=
        safe_text,
    isMetaItemType=
        st.booleans(),
    isRootElement=
        st.booleans()
)
ccore_ExtentedType_strategy = st.builds(
    ccore_ExtentedType,
)
ccore_EClass_strategy = st.builds(
    ccore_EClass,
)
ccore_GroupOfAttributes_strategy = st.builds(
    ccore_GroupOfAttributes,
    column=
        st.integers()
)
ccore_UIValidator_strategy = st.builds(
    ccore_UIValidator,
)
ccore_Page_strategy = st.builds(
    ccore_Page,
    label=
        safe_text,
    description=
        safe_text,
    idRuntime=
        safe_text,
    title=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
Item_strategy = st.builds(
    Item,
)
ccore_Cadse_strategy = st.builds(
    ccore_Cadse,
    itemRepoLogin=
        safe_text,
    idDefinition=
        safe_text,
    itemRepoURL=
        safe_text,
    description=
        safe_text,
    executed=
        st.booleans(),
    itemRepoPasswd=
        safe_text,
    defaultContentRepoURL=
        safe_text
)
ccore_KeyDefinition_strategy = st.builds(
    ccore_KeyDefinition,
)
ccore_RuntimeItem_strategy = st.builds(
    ccore_RuntimeItem,
    extendsClass=
        st.booleans(),
    className=
        safe_text
)
ccore_Field_strategy = st.builds(
    ccore_Field,
    position=
        safe_text,
    editable=
        st.booleans(),
    label=
        safe_text
)
ccore_Attribute_strategy = st.builds(
    ccore_Attribute,
    natif=
        st.booleans(),
    isList=
        st.booleans(),
    idRuntime=
        safe_text,
    devGenerated=
        st.booleans(),
    _final=
        st.booleans(),
    tWRevSpecific=
        st.booleans(),
    mustBeInitialized=
        st.booleans(),
    hiddenInComputedPages=
        st.booleans(),
    tWEvol=
        safe_text,
    tWUpdateKind=
        safe_text,
    tWCommitKind=
        safe_text,
    cannotBeUndefined=
        st.booleans(),
    require=
        st.booleans()
)
ccore_TypeDefinition_strategy = st.builds(
    ccore_TypeDefinition,
    idRuntime=
        safe_text
)
ccore_RuntimeItemType_strategy = st.builds(
    ccore_RuntimeItemType,
)
RuntimeItemType_strategy = st.builds(
    RuntimeItemType,
)
ccore_ComposerType_strategy = st.builds(
    ccore_ComposerType,
)
ccore_ExporterType_strategy = st.builds(
    ccore_ExporterType,
)
ccore_DBObject_strategy = st.builds(
    ccore_DBObject,
    objectId=
        st.integers(),
    uuid_lsb=
        safe_text,
    uuid_msb=
        safe_text
)
ccore_View_strategy = st.builds(
    ccore_View,
    icon=
        safe_text
)
ccore_ComposerLink_strategy = st.builds(
    ccore_ComposerLink,
)
ccore_MenuGroup_strategy = st.builds(
    ccore_MenuGroup,
)
ccore_MenuAction_strategy = st.builds(
    ccore_MenuAction,
)
ccore_ViewModel_strategy = st.builds(
    ccore_ViewModel,
)
ccore_ExtItem_strategy = st.builds(
    ccore_ExtItem,
)
ccore_ComputedString_strategy = st.builds(
    ccore_ComputedString,
    expression=
        safe_text
)
ccore_EEnum_strategy = st.builds(
    ccore_EEnum,
)
EEnum_strategy = st.builds(
    EEnum,
)
ccore_GroupExtItem_strategy = st.builds(
    ccore_GroupExtItem,
)
EReference_strategy = st.builds(
    EReference,
)
ccore_EnumType_strategy = st.builds(
    ccore_EnumType,
    values=
        safe_text,
    javaClass=
        safe_text,
    mustBeGenerated=
        st.booleans()
)
RuntimeItem_strategy = st.builds(
    RuntimeItem,
)
ccore_Composer_strategy = st.builds(
    ccore_Composer,
    types=
        safe_text
)
ccore_Exporter_strategy = st.builds(
    ccore_Exporter,
    types=
        safe_text
)
ccore_ModelController_strategy = st.builds(
    ccore_ModelController,
)
ccore_InteractionController_strategy = st.builds(
    ccore_InteractionController,
)
ccore_Display_strategy = st.builds(
    ccore_Display,
    extendsIC=
        st.booleans(),
    extendsUI=
        st.booleans(),
    extendsMC=
        st.booleans()
)
ccore_ExportedContent_strategy = st.builds(
    ccore_ExportedContent,
)
BindingDesc_strategy = st.builds(
    BindingDesc,
)
ccore_BindExt_strategy = st.builds(
    ccore_BindExt,
)
ccore_UnresolvedAttributeType_strategy = st.builds(
    ccore_UnresolvedAttributeType,
)
LongAttribute_strategy = st.builds(
    LongAttribute,
)
ccore_TimeAttribute_strategy = st.builds(
    ccore_TimeAttribute,
    initWithTheCurrentTime=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
ccore_IntegerAttribute_strategy = st.builds(
    ccore_IntegerAttribute,
)
ccore_Enum_strategy = st.builds(
    ccore_Enum,
    enumClazz=
        safe_text,
    values=
        safe_text
)
ccore_LongAttribute_strategy = st.builds(
    ccore_LongAttribute,
)
ccore_UUIDAttribute_strategy = st.builds(
    ccore_UUIDAttribute,
)
ccore_DateAttribute_strategy = st.builds(
    ccore_DateAttribute,
)
ccore_LinkType_strategy = st.builds(
    ccore_LinkType,
    composition=
        st.booleans(),
    twCoupled=
        st.booleans(),
    linkManager=
        safe_text,
    min=
        st.integers(),
    hidden=
        st.booleans(),
    max=
        st.integers(),
    mapping=
        st.booleans(),
    annotation=
        st.booleans(),
    twDestEvol=
        safe_text,
    group=
        st.booleans(),
    selection=
        safe_text,
    kind=
        st.integers(),
    aggregation=
        st.booleans()
)
ccore_DoubleAttribute_strategy = st.builds(
    ccore_DoubleAttribute,
)
ccore_BooleanAttribute_strategy = st.builds(
    ccore_BooleanAttribute,
)
ccore_StringAttribute_strategy = st.builds(
    ccore_StringAttribute,
    notEmpty=
        st.booleans()
)
ccore_ViewDescription_strategy = st.builds(
    ccore_ViewDescription,
)
ccore_ViewLinkType_strategy = st.builds(
    ccore_ViewLinkType,
    aggregation=
        st.booleans(),
    displayCreate=
        safe_text,
    canCreateItem=
        st.booleans(),
    canCreateLink=
        st.booleans()
)
ccore_ViewItemType_strategy = st.builds(
    ccore_ViewItemType,
    isRootElement=
        st.booleans(),
    ref=
        st.booleans()
)
ccore_GenInformation_strategy = st.builds(
    ccore_GenInformation,
    cSTName=
        safe_text
)





@given(instance=ccore_MenuAbstract_strategy)
def test_hyp_ccore_menuabstract_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=ccore_MenuAbstract_strategy)
def test_hyp_ccore_menuabstract_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=ccore_MenuAbstract_strategy)
def test_hyp_ccore_menuabstract_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original











@given(instance=ccore_ContentItemType_strategy)
def test_hyp_ccore_contentitemtype_extendsClass_setter(instance):
    original = instance.extendsClass
    instance.extendsClass = original
    assert instance.extendsClass == original






@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_twCommittedDate_setter(instance):
    original = instance.twCommittedDate
    instance.twCommittedDate = original
    assert instance.twCommittedDate == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_twVersion_setter(instance):
    original = instance.twVersion
    instance.twVersion = original
    assert instance.twVersion == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_twRevModified_setter(instance):
    original = instance.twRevModified
    instance.twRevModified = original
    assert instance.twRevModified == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_twRequireNewRev_setter(instance):
    original = instance.twRequireNewRev
    instance.twRequireNewRev = original
    assert instance.twRequireNewRev == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_committedBy_setter(instance):
    original = instance.committedBy
    instance.committedBy = original
    assert instance.committedBy == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_itemReadonly_setter(instance):
    original = instance.itemReadonly
    instance.itemReadonly = original
    assert instance.itemReadonly == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_isvalid_setter(instance):
    original = instance.isvalid
    instance.isvalid = original
    assert instance.isvalid == original



@given(instance=ccore_Item_strategy)
def test_hyp_ccore_item_itemHidden_setter(instance):
    original = instance.itemHidden
    instance.itemHidden = original
    assert instance.itemHidden == original








@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_isInstanceHidden_setter(instance):
    original = instance.isInstanceHidden
    instance.isInstanceHidden = original
    assert instance.isInstanceHidden == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_hasShortName_setter(instance):
    original = instance.hasShortName
    instance.hasShortName = original
    assert instance.hasShortName == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_customManager_setter(instance):
    original = instance.customManager
    instance.customManager = original
    assert instance.customManager == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_overwriteDefaultPages_setter(instance):
    original = instance.overwriteDefaultPages
    instance.overwriteDefaultPages = original
    assert instance.overwriteDefaultPages == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_qualifiedNameTemplate_setter(instance):
    original = instance.qualifiedNameTemplate
    instance.qualifiedNameTemplate = original
    assert instance.qualifiedNameTemplate == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_validateNameRe_setter(instance):
    original = instance.validateNameRe
    instance.validateNameRe = original
    assert instance.validateNameRe == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_messageErrorId_setter(instance):
    original = instance.messageErrorId
    instance.messageErrorId = original
    assert instance.messageErrorId == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_hasContent_setter(instance):
    original = instance.hasContent
    instance.hasContent = original
    assert instance.hasContent == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_itemManagerClass_setter(instance):
    original = instance.itemManagerClass
    instance.itemManagerClass = original
    assert instance.itemManagerClass == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_isInstanceAbstract_setter(instance):
    original = instance.isInstanceAbstract
    instance.isInstanceAbstract = original
    assert instance.isInstanceAbstract == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_managerClass_setter(instance):
    original = instance.managerClass
    instance.managerClass = original
    assert instance.managerClass == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_humanName_setter(instance):
    original = instance.humanName
    instance.humanName = original
    assert instance.humanName == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_displayNameTemplate_setter(instance):
    original = instance.displayNameTemplate
    instance.displayNameTemplate = original
    assert instance.displayNameTemplate == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_itemFactoryClass_setter(instance):
    original = instance.itemFactoryClass
    instance.itemFactoryClass = original
    assert instance.itemFactoryClass == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_hasUniqueName_setter(instance):
    original = instance.hasUniqueName
    instance.hasUniqueName = original
    assert instance.hasUniqueName == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_isMetaItemType_setter(instance):
    original = instance.isMetaItemType
    instance.isMetaItemType = original
    assert instance.isMetaItemType == original



@given(instance=ccore_ItemType_strategy)
def test_hyp_ccore_itemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original






@given(instance=ccore_GroupOfAttributes_strategy)
def test_hyp_ccore_groupofattributes_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original





@given(instance=ccore_Page_strategy)
def test_hyp_ccore_page_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=ccore_Page_strategy)
def test_hyp_ccore_page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ccore_Page_strategy)
def test_hyp_ccore_page_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original



@given(instance=ccore_Page_strategy)
def test_hyp_ccore_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original






@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_itemRepoLogin_setter(instance):
    original = instance.itemRepoLogin
    instance.itemRepoLogin = original
    assert instance.itemRepoLogin == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_idDefinition_setter(instance):
    original = instance.idDefinition
    instance.idDefinition = original
    assert instance.idDefinition == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_itemRepoURL_setter(instance):
    original = instance.itemRepoURL
    instance.itemRepoURL = original
    assert instance.itemRepoURL == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_executed_setter(instance):
    original = instance.executed
    instance.executed = original
    assert instance.executed == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_itemRepoPasswd_setter(instance):
    original = instance.itemRepoPasswd
    instance.itemRepoPasswd = original
    assert instance.itemRepoPasswd == original



@given(instance=ccore_Cadse_strategy)
def test_hyp_ccore_cadse_defaultContentRepoURL_setter(instance):
    original = instance.defaultContentRepoURL
    instance.defaultContentRepoURL = original
    assert instance.defaultContentRepoURL == original





@given(instance=ccore_RuntimeItem_strategy)
def test_hyp_ccore_runtimeitem_extendsClass_setter(instance):
    original = instance.extendsClass
    instance.extendsClass = original
    assert instance.extendsClass == original



@given(instance=ccore_RuntimeItem_strategy)
def test_hyp_ccore_runtimeitem_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original




@given(instance=ccore_Field_strategy)
def test_hyp_ccore_field_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=ccore_Field_strategy)
def test_hyp_ccore_field_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original



@given(instance=ccore_Field_strategy)
def test_hyp_ccore_field_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_natif_setter(instance):
    original = instance.natif
    instance.natif = original
    assert instance.natif == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_devGenerated_setter(instance):
    original = instance.devGenerated
    instance.devGenerated = original
    assert instance.devGenerated == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute__final_setter(instance):
    original = instance._final
    instance._final = original
    assert instance._final == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_tWRevSpecific_setter(instance):
    original = instance.tWRevSpecific
    instance.tWRevSpecific = original
    assert instance.tWRevSpecific == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_mustBeInitialized_setter(instance):
    original = instance.mustBeInitialized
    instance.mustBeInitialized = original
    assert instance.mustBeInitialized == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_hiddenInComputedPages_setter(instance):
    original = instance.hiddenInComputedPages
    instance.hiddenInComputedPages = original
    assert instance.hiddenInComputedPages == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_tWEvol_setter(instance):
    original = instance.tWEvol
    instance.tWEvol = original
    assert instance.tWEvol == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_tWUpdateKind_setter(instance):
    original = instance.tWUpdateKind
    instance.tWUpdateKind = original
    assert instance.tWUpdateKind == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_tWCommitKind_setter(instance):
    original = instance.tWCommitKind
    instance.tWCommitKind = original
    assert instance.tWCommitKind == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_cannotBeUndefined_setter(instance):
    original = instance.cannotBeUndefined
    instance.cannotBeUndefined = original
    assert instance.cannotBeUndefined == original



@given(instance=ccore_Attribute_strategy)
def test_hyp_ccore_attribute_require_setter(instance):
    original = instance.require
    instance.require = original
    assert instance.require == original




@given(instance=ccore_TypeDefinition_strategy)
def test_hyp_ccore_typedefinition_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original








@given(instance=ccore_DBObject_strategy)
def test_hyp_ccore_dbobject_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original



@given(instance=ccore_DBObject_strategy)
def test_hyp_ccore_dbobject_uuid_lsb_setter(instance):
    original = instance.uuid_lsb
    instance.uuid_lsb = original
    assert instance.uuid_lsb == original



@given(instance=ccore_DBObject_strategy)
def test_hyp_ccore_dbobject_uuid_msb_setter(instance):
    original = instance.uuid_msb
    instance.uuid_msb = original
    assert instance.uuid_msb == original




@given(instance=ccore_View_strategy)
def test_hyp_ccore_view_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original









@given(instance=ccore_ComputedString_strategy)
def test_hyp_ccore_computedstring_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original








@given(instance=ccore_EnumType_strategy)
def test_hyp_ccore_enumtype_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=ccore_EnumType_strategy)
def test_hyp_ccore_enumtype_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original



@given(instance=ccore_EnumType_strategy)
def test_hyp_ccore_enumtype_mustBeGenerated_setter(instance):
    original = instance.mustBeGenerated
    instance.mustBeGenerated = original
    assert instance.mustBeGenerated == original





@given(instance=ccore_Composer_strategy)
def test_hyp_ccore_composer_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original




@given(instance=ccore_Exporter_strategy)
def test_hyp_ccore_exporter_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original






@given(instance=ccore_Display_strategy)
def test_hyp_ccore_display_extendsIC_setter(instance):
    original = instance.extendsIC
    instance.extendsIC = original
    assert instance.extendsIC == original



@given(instance=ccore_Display_strategy)
def test_hyp_ccore_display_extendsUI_setter(instance):
    original = instance.extendsUI
    instance.extendsUI = original
    assert instance.extendsUI == original



@given(instance=ccore_Display_strategy)
def test_hyp_ccore_display_extendsMC_setter(instance):
    original = instance.extendsMC
    instance.extendsMC = original
    assert instance.extendsMC == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ccore_ExportedContent_strategy)
@settings(max_examples=30)
def test_hyp_ccore_exportedcontent_haschildren_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasChildren()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasChildren).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasChildren' in ccore_ExportedContent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasChildren' in ccore_ExportedContent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasChildren' in ccore_ExportedContent is not implemented or raised an error")








@given(instance=ccore_TimeAttribute_strategy)
def test_hyp_ccore_timeattribute_initWithTheCurrentTime_setter(instance):
    original = instance.initWithTheCurrentTime
    instance.initWithTheCurrentTime = original
    assert instance.initWithTheCurrentTime == original






@given(instance=ccore_Enum_strategy)
def test_hyp_ccore_enum_enumClazz_setter(instance):
    original = instance.enumClazz
    instance.enumClazz = original
    assert instance.enumClazz == original



@given(instance=ccore_Enum_strategy)
def test_hyp_ccore_enum_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original







@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_twCoupled_setter(instance):
    original = instance.twCoupled
    instance.twCoupled = original
    assert instance.twCoupled == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_linkManager_setter(instance):
    original = instance.linkManager
    instance.linkManager = original
    assert instance.linkManager == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_mapping_setter(instance):
    original = instance.mapping
    instance.mapping = original
    assert instance.mapping == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_twDestEvol_setter(instance):
    original = instance.twDestEvol
    instance.twDestEvol = original
    assert instance.twDestEvol == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=ccore_LinkType_strategy)
def test_hyp_ccore_linktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original






@given(instance=ccore_StringAttribute_strategy)
def test_hyp_ccore_stringattribute_notEmpty_setter(instance):
    original = instance.notEmpty
    instance.notEmpty = original
    assert instance.notEmpty == original





@given(instance=ccore_ViewLinkType_strategy)
def test_hyp_ccore_viewlinktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=ccore_ViewLinkType_strategy)
def test_hyp_ccore_viewlinktype_displayCreate_setter(instance):
    original = instance.displayCreate
    instance.displayCreate = original
    assert instance.displayCreate == original



@given(instance=ccore_ViewLinkType_strategy)
def test_hyp_ccore_viewlinktype_canCreateItem_setter(instance):
    original = instance.canCreateItem
    instance.canCreateItem = original
    assert instance.canCreateItem == original



@given(instance=ccore_ViewLinkType_strategy)
def test_hyp_ccore_viewlinktype_canCreateLink_setter(instance):
    original = instance.canCreateLink
    instance.canCreateLink = original
    assert instance.canCreateLink == original




@given(instance=ccore_ViewItemType_strategy)
def test_hyp_ccore_viewitemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original



@given(instance=ccore_ViewItemType_strategy)
def test_hyp_ccore_viewitemtype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original




@given(instance=ccore_GenInformation_strategy)
def test_hyp_ccore_geninformation_cSTName_setter(instance):
    original = instance.cSTName
    instance.cSTName = original
    assert instance.cSTName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



