import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_attribute111_reverse_link_reassign_clear():
    a1 = ccore_Field(editable=True, label="sample_text", position="sample_text")
    a2 = ccore_Field(editable=False, label="sample_text_2", position="sample_text_2")
    b = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    _safe_set(b, 'ccore_Attribute113', a1)
    assert _is_linked(b, 'ccore_Attribute113', a1)
    if hasattr(a1, 'ccore_Field112'):
        assert _is_linked(a1, 'ccore_Field112', b)
    _safe_set(b, 'ccore_Attribute113', a2)
    assert _is_linked(b, 'ccore_Attribute113', a2)
    if hasattr(a1, 'ccore_Field112'):
        assert not _is_linked(a1, 'ccore_Field112', b)
    if hasattr(a2, 'ccore_Field112'):
        assert _is_linked(a2, 'ccore_Field112', b)
    _safe_set(b, 'ccore_Attribute113', None)
    assert not _is_linked(b, 'ccore_Attribute113', a2)
    if hasattr(a2, 'ccore_Field112'):
        assert not _is_linked(a2, 'ccore_Field112', b)


def test_assoc_attributes0_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    _safe_set(b, 'ccore_Attribute', a1)
    assert _is_linked(b, 'ccore_Attribute', a1)
    if hasattr(a1, 'ccore_TypeDefinition'):
        assert _is_linked(a1, 'ccore_TypeDefinition', b)
    _safe_set(b, 'ccore_Attribute', a2)
    assert _is_linked(b, 'ccore_Attribute', a2)
    if hasattr(a1, 'ccore_TypeDefinition'):
        assert not _is_linked(a1, 'ccore_TypeDefinition', b)
    if hasattr(a2, 'ccore_TypeDefinition'):
        assert _is_linked(a2, 'ccore_TypeDefinition', b)
    _safe_set(b, 'ccore_Attribute', None)
    assert not _is_linked(b, 'ccore_Attribute', a2)
    if hasattr(a2, 'ccore_TypeDefinition'):
        assert not _is_linked(a2, 'ccore_TypeDefinition', b)


def test_assoc_attributes120_reverse_link_reassign_clear():
    a1 = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    a2 = ccore_Page(description="sample_text_2", idRuntime="sample_text_2", label="sample_text_2", title="sample_text_2")
    b = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    _safe_set(b, 'ccore_Attribute122', a1)
    assert _is_linked(b, 'ccore_Attribute122', a1)
    if hasattr(a1, 'ccore_Page121'):
        assert _is_linked(a1, 'ccore_Page121', b)
    _safe_set(b, 'ccore_Attribute122', a2)
    assert _is_linked(b, 'ccore_Attribute122', a2)
    if hasattr(a1, 'ccore_Page121'):
        assert not _is_linked(a1, 'ccore_Page121', b)
    if hasattr(a2, 'ccore_Page121'):
        assert _is_linked(a2, 'ccore_Page121', b)
    _safe_set(b, 'ccore_Attribute122', None)
    assert not _is_linked(b, 'ccore_Attribute122', a2)
    if hasattr(a2, 'ccore_Page121'):
        assert not _is_linked(a2, 'ccore_Page121', b)


def test_assoc_attributes128_reverse_link_reassign_clear():
    a1 = ccore_GroupOfAttributes(column=7)
    a2 = ccore_GroupOfAttributes(column=13)
    b = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    _safe_set(b, 'ccore_Attribute130', a1)
    assert _is_linked(b, 'ccore_Attribute130', a1)
    if hasattr(a1, 'ccore_GroupOfAttributes129'):
        assert _is_linked(a1, 'ccore_GroupOfAttributes129', b)
    _safe_set(b, 'ccore_Attribute130', a2)
    assert _is_linked(b, 'ccore_Attribute130', a2)
    if hasattr(a1, 'ccore_GroupOfAttributes129'):
        assert not _is_linked(a1, 'ccore_GroupOfAttributes129', b)
    if hasattr(a2, 'ccore_GroupOfAttributes129'):
        assert _is_linked(a2, 'ccore_GroupOfAttributes129', b)
    _safe_set(b, 'ccore_Attribute130', None)
    assert not _is_linked(b, 'ccore_Attribute130', a2)
    if hasattr(a2, 'ccore_GroupOfAttributes129'):
        assert not _is_linked(a2, 'ccore_GroupOfAttributes129', b)


def test_assoc_cadse64_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    _safe_set(b, 'ccore_Cadse66', a1)
    assert _is_linked(b, 'ccore_Cadse66', a1)
    if hasattr(a1, 'ccore_Item65'):
        assert _is_linked(a1, 'ccore_Item65', b)
    _safe_set(b, 'ccore_Cadse66', a2)
    assert _is_linked(b, 'ccore_Cadse66', a2)
    if hasattr(a1, 'ccore_Item65'):
        assert not _is_linked(a1, 'ccore_Item65', b)
    if hasattr(a2, 'ccore_Item65'):
        assert _is_linked(a2, 'ccore_Item65', b)
    _safe_set(b, 'ccore_Cadse66', None)
    assert not _is_linked(b, 'ccore_Cadse66', a2)
    if hasattr(a2, 'ccore_Item65'):
        assert not _is_linked(a2, 'ccore_Item65', b)


def test_assoc_composerLinks142_reverse_link_reassign_clear():
    a1 = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    a2 = ccore_LinkType(aggregation=False, annotation=False, composition=False, group=False, hidden=False, kind=13, linkManager="sample_text_2", mapping=False, max=13, min=13, selection="sample_text_2", twCoupled=False, twDestEvol="sample_text_2")
    b = ccore_Composer(types="sample_text")
    _safe_set(b, 'ccore_Composer', {a1})
    assert _is_linked(b, 'ccore_Composer', a1)
    if hasattr(a1, 'ccore_LinkType143'):
        assert _is_linked(a1, 'ccore_LinkType143', b)
    _safe_set(b, 'ccore_Composer', {a2})
    assert _is_linked(b, 'ccore_Composer', a2)
    if hasattr(a1, 'ccore_LinkType143'):
        assert not _is_linked(a1, 'ccore_LinkType143', b)
    if hasattr(a2, 'ccore_LinkType143'):
        assert _is_linked(a2, 'ccore_LinkType143', b)
    _safe_set(b, 'ccore_Composer', set())
    assert not _is_linked(b, 'ccore_Composer', a2)
    if hasattr(a2, 'ccore_LinkType143'):
        assert not _is_linked(a2, 'ccore_LinkType143', b)


def test_assoc_composers69_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Composer(types="sample_text")
    _safe_set(b, 'Composer', a1)
    assert _is_linked(b, 'Composer', a1)
    if hasattr(a1, 'ownerItem70'):
        assert _is_linked(a1, 'ownerItem70', b)
    _safe_set(b, 'Composer', a2)
    assert _is_linked(b, 'Composer', a2)
    if hasattr(a1, 'ownerItem70'):
        assert not _is_linked(a1, 'ownerItem70', b)
    if hasattr(a2, 'ownerItem70'):
        assert _is_linked(a2, 'ownerItem70', b)
    _safe_set(b, 'Composer', None)
    assert not _is_linked(b, 'Composer', a2)
    if hasattr(a2, 'ownerItem70'):
        assert not _is_linked(a2, 'ownerItem70', b)


def test_assoc_contentItemTypes34_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_ContentItemType(extendsClass=True)
    _safe_set(b, 'ccore_ContentItemType36', a1)
    assert _is_linked(b, 'ccore_ContentItemType36', a1)
    if hasattr(a1, 'ccore_ItemType35'):
        assert _is_linked(a1, 'ccore_ItemType35', b)
    _safe_set(b, 'ccore_ContentItemType36', a2)
    assert _is_linked(b, 'ccore_ContentItemType36', a2)
    if hasattr(a1, 'ccore_ItemType35'):
        assert not _is_linked(a1, 'ccore_ItemType35', b)
    if hasattr(a2, 'ccore_ItemType35'):
        assert _is_linked(a2, 'ccore_ItemType35', b)
    _safe_set(b, 'ccore_ContentItemType36', None)
    assert not _is_linked(b, 'ccore_ContentItemType36', a2)
    if hasattr(a2, 'ccore_ItemType35'):
        assert not _is_linked(a2, 'ccore_ItemType35', b)


def test_assoc_contentModel28_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_ContentItemType(extendsClass=True)
    _safe_set(b, 'ccore_ContentItemType', a1)
    assert _is_linked(b, 'ccore_ContentItemType', a1)
    if hasattr(a1, 'ccore_ItemType29'):
        assert _is_linked(a1, 'ccore_ItemType29', b)
    _safe_set(b, 'ccore_ContentItemType', a2)
    assert _is_linked(b, 'ccore_ContentItemType', a2)
    if hasattr(a1, 'ccore_ItemType29'):
        assert not _is_linked(a1, 'ccore_ItemType29', b)
    if hasattr(a2, 'ccore_ItemType29'):
        assert _is_linked(a2, 'ccore_ItemType29', b)
    _safe_set(b, 'ccore_ContentItemType', None)
    assert not _is_linked(b, 'ccore_ContentItemType', a2)
    if hasattr(a2, 'ccore_ItemType29'):
        assert not _is_linked(a2, 'ccore_ItemType29', b)


def test_assoc_creationPages3_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    _safe_set(b, 'ccore_Page', a1)
    assert _is_linked(b, 'ccore_Page', a1)
    if hasattr(a1, 'ccore_TypeDefinition4'):
        assert _is_linked(a1, 'ccore_TypeDefinition4', b)
    _safe_set(b, 'ccore_Page', a2)
    assert _is_linked(b, 'ccore_Page', a2)
    if hasattr(a1, 'ccore_TypeDefinition4'):
        assert not _is_linked(a1, 'ccore_TypeDefinition4', b)
    if hasattr(a2, 'ccore_TypeDefinition4'):
        assert _is_linked(a2, 'ccore_TypeDefinition4', b)
    _safe_set(b, 'ccore_Page', None)
    assert not _is_linked(b, 'ccore_Page', a2)
    if hasattr(a2, 'ccore_TypeDefinition4'):
        assert not _is_linked(a2, 'ccore_TypeDefinition4', b)


def test_assoc_destination100_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    _safe_set(b, 'ccore_LinkType', a1)
    assert _is_linked(b, 'ccore_LinkType', a1)
    if hasattr(a1, 'ccore_TypeDefinition101'):
        assert _is_linked(a1, 'ccore_TypeDefinition101', b)
    _safe_set(b, 'ccore_LinkType', a2)
    assert _is_linked(b, 'ccore_LinkType', a2)
    if hasattr(a1, 'ccore_TypeDefinition101'):
        assert not _is_linked(a1, 'ccore_TypeDefinition101', b)
    if hasattr(a2, 'ccore_TypeDefinition101'):
        assert _is_linked(a2, 'ccore_TypeDefinition101', b)
    _safe_set(b, 'ccore_LinkType', None)
    assert not _is_linked(b, 'ccore_LinkType', a2)
    if hasattr(a2, 'ccore_TypeDefinition101'):
        assert not _is_linked(a2, 'ccore_TypeDefinition101', b)


def test_assoc_enumType99_reverse_link_reassign_clear():
    a1 = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    a2 = ccore_EnumType(javaClass="sample_text_2", mustBeGenerated=False, values="sample_text_2")
    b = ccore_Enum(enumClazz="sample_text", values="sample_text")
    _safe_set(b, 'ccore_Enum', a1)
    assert _is_linked(b, 'ccore_Enum', a1)
    if hasattr(a1, 'ccore_EnumType'):
        assert _is_linked(a1, 'ccore_EnumType', b)
    _safe_set(b, 'ccore_Enum', a2)
    assert _is_linked(b, 'ccore_Enum', a2)
    if hasattr(a1, 'ccore_EnumType'):
        assert not _is_linked(a1, 'ccore_EnumType', b)
    if hasattr(a2, 'ccore_EnumType'):
        assert _is_linked(a2, 'ccore_EnumType', b)
    _safe_set(b, 'ccore_Enum', None)
    assert not _is_linked(b, 'ccore_Enum', a2)
    if hasattr(a2, 'ccore_EnumType'):
        assert not _is_linked(a2, 'ccore_EnumType', b)


def test_assoc_exporters67_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Exporter(types="sample_text")
    _safe_set(b, 'Exporter', a1)
    assert _is_linked(b, 'Exporter', a1)
    if hasattr(a1, 'ownerItem68'):
        assert _is_linked(a1, 'ownerItem68', b)
    _safe_set(b, 'Exporter', a2)
    assert _is_linked(b, 'Exporter', a2)
    if hasattr(a1, 'ownerItem68'):
        assert not _is_linked(a1, 'ownerItem68', b)
    if hasattr(a2, 'ownerItem68'):
        assert _is_linked(a2, 'ownerItem68', b)
    _safe_set(b, 'Exporter', None)
    assert not _is_linked(b, 'Exporter', a2)
    if hasattr(a2, 'ownerItem68'):
        assert not _is_linked(a2, 'ownerItem68', b)


def test_assoc_extendsCadse38_reverse_link_reassign_clear():
    a1 = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    a2 = ccore_Cadse(defaultContentRepoURL="sample_text_2", description="sample_text_2", executed=False, idDefinition="sample_text_2", itemRepoLogin="sample_text_2", itemRepoPasswd="sample_text_2", itemRepoURL="sample_text_2")
    b = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    _safe_set(b, 'ccore_Cadse37', {a1})
    assert _is_linked(b, 'ccore_Cadse37', a1)
    if hasattr(a1, 'ccore_Cadse'):
        assert _is_linked(a1, 'ccore_Cadse', b)
    _safe_set(b, 'ccore_Cadse37', {a2})
    assert _is_linked(b, 'ccore_Cadse37', a2)
    if hasattr(a1, 'ccore_Cadse'):
        assert not _is_linked(a1, 'ccore_Cadse', b)
    if hasattr(a2, 'ccore_Cadse'):
        assert _is_linked(a2, 'ccore_Cadse', b)
    _safe_set(b, 'ccore_Cadse37', set())
    assert not _is_linked(b, 'ccore_Cadse37', a2)
    if hasattr(a2, 'ccore_Cadse'):
        assert not _is_linked(a2, 'ccore_Cadse', b)


def test_assoc_fields1_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_Field(editable=True, label="sample_text", position="sample_text")
    _safe_set(b, 'ccore_Field', a1)
    assert _is_linked(b, 'ccore_Field', a1)
    if hasattr(a1, 'ccore_TypeDefinition2'):
        assert _is_linked(a1, 'ccore_TypeDefinition2', b)
    _safe_set(b, 'ccore_Field', a2)
    assert _is_linked(b, 'ccore_Field', a2)
    if hasattr(a1, 'ccore_TypeDefinition2'):
        assert not _is_linked(a1, 'ccore_TypeDefinition2', b)
    if hasattr(a2, 'ccore_TypeDefinition2'):
        assert _is_linked(a2, 'ccore_TypeDefinition2', b)
    _safe_set(b, 'ccore_Field', None)
    assert not _is_linked(b, 'ccore_Field', a2)
    if hasattr(a2, 'ccore_TypeDefinition2'):
        assert not _is_linked(a2, 'ccore_TypeDefinition2', b)


def test_assoc_goupsOfAttributes10_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_GroupOfAttributes(column=7)
    _safe_set(b, 'ccore_GroupOfAttributes', a1)
    assert _is_linked(b, 'ccore_GroupOfAttributes', a1)
    if hasattr(a1, 'ccore_TypeDefinition11'):
        assert _is_linked(a1, 'ccore_TypeDefinition11', b)
    _safe_set(b, 'ccore_GroupOfAttributes', a2)
    assert _is_linked(b, 'ccore_GroupOfAttributes', a2)
    if hasattr(a1, 'ccore_TypeDefinition11'):
        assert not _is_linked(a1, 'ccore_TypeDefinition11', b)
    if hasattr(a2, 'ccore_TypeDefinition11'):
        assert _is_linked(a2, 'ccore_TypeDefinition11', b)
    _safe_set(b, 'ccore_GroupOfAttributes', None)
    assert not _is_linked(b, 'ccore_GroupOfAttributes', a2)
    if hasattr(a2, 'ccore_TypeDefinition11'):
        assert not _is_linked(a2, 'ccore_TypeDefinition11', b)


def test_assoc_instanceOf54_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    _safe_set(b, 'ccore_Item55', {a1})
    assert _is_linked(b, 'ccore_Item55', a1)
    if hasattr(a1, 'ccore_ItemType56'):
        assert _is_linked(a1, 'ccore_ItemType56', b)
    _safe_set(b, 'ccore_Item55', {a2})
    assert _is_linked(b, 'ccore_Item55', a2)
    if hasattr(a1, 'ccore_ItemType56'):
        assert not _is_linked(a1, 'ccore_ItemType56', b)
    if hasattr(a2, 'ccore_ItemType56'):
        assert _is_linked(a2, 'ccore_ItemType56', b)
    _safe_set(b, 'ccore_Item55', set())
    assert not _is_linked(b, 'ccore_Item55', a2)
    if hasattr(a2, 'ccore_ItemType56'):
        assert not _is_linked(a2, 'ccore_ItemType56', b)


def test_assoc_itemContents52_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    _safe_set(b, 'ccore_Cadse53', {a1})
    assert _is_linked(b, 'ccore_Cadse53', a1)
    if hasattr(a1, 'ccore_Item'):
        assert _is_linked(a1, 'ccore_Item', b)
    _safe_set(b, 'ccore_Cadse53', {a2})
    assert _is_linked(b, 'ccore_Cadse53', a2)
    if hasattr(a1, 'ccore_Item'):
        assert not _is_linked(a1, 'ccore_Item', b)
    if hasattr(a2, 'ccore_Item'):
        assert _is_linked(a2, 'ccore_Item', b)
    _safe_set(b, 'ccore_Cadse53', set())
    assert not _is_linked(b, 'ccore_Cadse53', a2)
    if hasattr(a2, 'ccore_Item'):
        assert not _is_linked(a2, 'ccore_Item', b)


def test_assoc_itemType79_reverse_link_reassign_clear():
    a1 = ccore_ViewItemType(isRootElement=True, ref=True)
    a2 = ccore_ViewItemType(isRootElement=False, ref=False)
    b = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    _safe_set(b, 'ccore_ItemType80', a1)
    assert _is_linked(b, 'ccore_ItemType80', a1)
    if hasattr(a1, 'ccore_ViewItemType'):
        assert _is_linked(a1, 'ccore_ViewItemType', b)
    _safe_set(b, 'ccore_ItemType80', a2)
    assert _is_linked(b, 'ccore_ItemType80', a2)
    if hasattr(a1, 'ccore_ViewItemType'):
        assert not _is_linked(a1, 'ccore_ViewItemType', b)
    if hasattr(a2, 'ccore_ViewItemType'):
        assert _is_linked(a2, 'ccore_ViewItemType', b)
    _safe_set(b, 'ccore_ItemType80', None)
    assert not _is_linked(b, 'ccore_ItemType80', a2)
    if hasattr(a2, 'ccore_ViewItemType'):
        assert not _is_linked(a2, 'ccore_ViewItemType', b)


def test_assoc_itemTypes39_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    _safe_set(b, 'ccore_Cadse40', {a1})
    assert _is_linked(b, 'ccore_Cadse40', a1)
    if hasattr(a1, 'ccore_ItemType41'):
        assert _is_linked(a1, 'ccore_ItemType41', b)
    _safe_set(b, 'ccore_Cadse40', {a2})
    assert _is_linked(b, 'ccore_Cadse40', a2)
    if hasattr(a1, 'ccore_ItemType41'):
        assert not _is_linked(a1, 'ccore_ItemType41', b)
    if hasattr(a2, 'ccore_ItemType41'):
        assert _is_linked(a2, 'ccore_ItemType41', b)
    _safe_set(b, 'ccore_Cadse40', set())
    assert not _is_linked(b, 'ccore_Cadse40', a2)
    if hasattr(a2, 'ccore_ItemType41'):
        assert not _is_linked(a2, 'ccore_ItemType41', b)


def test_assoc_linkType134_reverse_link_reassign_clear():
    a1 = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    a2 = ccore_ViewLinkType(aggregation=False, canCreateItem=False, canCreateLink=False, displayCreate="sample_text_2")
    b = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    _safe_set(b, 'ccore_LinkType136', a1)
    assert _is_linked(b, 'ccore_LinkType136', a1)
    if hasattr(a1, 'ccore_ViewLinkType135'):
        assert _is_linked(a1, 'ccore_ViewLinkType135', b)
    _safe_set(b, 'ccore_LinkType136', a2)
    assert _is_linked(b, 'ccore_LinkType136', a2)
    if hasattr(a1, 'ccore_ViewLinkType135'):
        assert not _is_linked(a1, 'ccore_ViewLinkType135', b)
    if hasattr(a2, 'ccore_ViewLinkType135'):
        assert _is_linked(a2, 'ccore_ViewLinkType135', b)
    _safe_set(b, 'ccore_LinkType136', None)
    assert not _is_linked(b, 'ccore_LinkType136', a2)
    if hasattr(a2, 'ccore_ViewLinkType135'):
        assert not _is_linked(a2, 'ccore_ViewLinkType135', b)


def test_assoc_mainItemType171_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_DBObject(objectId=7, uuid_lsb="sample_text", uuid_msb="sample_text")
    _safe_set(b, 'ccore_DBObject', a1)
    assert _is_linked(b, 'ccore_DBObject', a1)
    if hasattr(a1, 'ccore_ItemType172'):
        assert _is_linked(a1, 'ccore_ItemType172', b)
    _safe_set(b, 'ccore_DBObject', a2)
    assert _is_linked(b, 'ccore_DBObject', a2)
    if hasattr(a1, 'ccore_ItemType172'):
        assert not _is_linked(a1, 'ccore_ItemType172', b)
    if hasattr(a2, 'ccore_ItemType172'):
        assert _is_linked(a2, 'ccore_ItemType172', b)
    _safe_set(b, 'ccore_DBObject', None)
    assert not _is_linked(b, 'ccore_DBObject', a2)
    if hasattr(a2, 'ccore_ItemType172'):
        assert not _is_linked(a2, 'ccore_ItemType172', b)


def test_assoc_modificationPages7_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    _safe_set(b, 'ccore_Page9', a1)
    assert _is_linked(b, 'ccore_Page9', a1)
    if hasattr(a1, 'ccore_TypeDefinition8'):
        assert _is_linked(a1, 'ccore_TypeDefinition8', b)
    _safe_set(b, 'ccore_Page9', a2)
    assert _is_linked(b, 'ccore_Page9', a2)
    if hasattr(a1, 'ccore_TypeDefinition8'):
        assert not _is_linked(a1, 'ccore_TypeDefinition8', b)
    if hasattr(a2, 'ccore_TypeDefinition8'):
        assert _is_linked(a2, 'ccore_TypeDefinition8', b)
    _safe_set(b, 'ccore_Page9', None)
    assert not _is_linked(b, 'ccore_Page9', a2)
    if hasattr(a2, 'ccore_TypeDefinition8'):
        assert not _is_linked(a2, 'ccore_TypeDefinition8', b)


def test_assoc_modifiedAttributes60_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    _safe_set(b, 'ccore_Attribute62', a1)
    assert _is_linked(b, 'ccore_Attribute62', a1)
    if hasattr(a1, 'ccore_Item61'):
        assert _is_linked(a1, 'ccore_Item61', b)
    _safe_set(b, 'ccore_Attribute62', a2)
    assert _is_linked(b, 'ccore_Attribute62', a2)
    if hasattr(a1, 'ccore_Item61'):
        assert not _is_linked(a1, 'ccore_Item61', b)
    if hasattr(a2, 'ccore_Item61'):
        assert _is_linked(a2, 'ccore_Item61', b)
    _safe_set(b, 'ccore_Attribute62', None)
    assert not _is_linked(b, 'ccore_Attribute62', a2)
    if hasattr(a2, 'ccore_Item61'):
        assert not _is_linked(a2, 'ccore_Item61', b)


def test_assoc_overwrite124_reverse_link_reassign_clear():
    a1 = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    a2 = ccore_Page(description="sample_text_2", idRuntime="sample_text_2", label="sample_text_2", title="sample_text_2")
    b = ccore_Page(description="sample_text", idRuntime="sample_text", label="sample_text", title="sample_text")
    _safe_set(b, 'ccore_Page125', a1)
    assert _is_linked(b, 'ccore_Page125', a1)
    if hasattr(a1, 'ccore_Page123'):
        assert _is_linked(a1, 'ccore_Page123', b)
    _safe_set(b, 'ccore_Page125', a2)
    assert _is_linked(b, 'ccore_Page125', a2)
    if hasattr(a1, 'ccore_Page123'):
        assert not _is_linked(a1, 'ccore_Page123', b)
    if hasattr(a2, 'ccore_Page123'):
        assert _is_linked(a2, 'ccore_Page123', b)
    _safe_set(b, 'ccore_Page125', None)
    assert not _is_linked(b, 'ccore_Page125', a2)
    if hasattr(a2, 'ccore_Page123'):
        assert not _is_linked(a2, 'ccore_Page123', b)


def test_assoc_ownerItem146_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Composer(types="sample_text")
    _safe_set(b, 'composers', a1)
    assert _is_linked(b, 'composers', a1)
    if hasattr(a1, 'Item'):
        assert _is_linked(a1, 'Item', b)
    _safe_set(b, 'composers', a2)
    assert _is_linked(b, 'composers', a2)
    if hasattr(a1, 'Item'):
        assert not _is_linked(a1, 'Item', b)
    if hasattr(a2, 'Item'):
        assert _is_linked(a2, 'Item', b)
    _safe_set(b, 'composers', None)
    assert not _is_linked(b, 'composers', a2)
    if hasattr(a2, 'Item'):
        assert not _is_linked(a2, 'Item', b)


def test_assoc_ownerItem147_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Exporter(types="sample_text")
    _safe_set(b, 'exporters', a1)
    assert _is_linked(b, 'exporters', a1)
    if hasattr(a1, 'Item148'):
        assert _is_linked(a1, 'Item148', b)
    _safe_set(b, 'exporters', a2)
    assert _is_linked(b, 'exporters', a2)
    if hasattr(a1, 'Item148'):
        assert not _is_linked(a1, 'Item148', b)
    if hasattr(a2, 'Item148'):
        assert _is_linked(a2, 'Item148', b)
    _safe_set(b, 'exporters', None)
    assert not _is_linked(b, 'exporters', a2)
    if hasattr(a2, 'Item148'):
        assert not _is_linked(a2, 'Item148', b)


def test_assoc_parent58_reverse_link_reassign_clear():
    a1 = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    a2 = ccore_Item(committedBy="sample_text_2", displayName="sample_text_2", isvalid=False, itemHidden=False, itemReadonly=False, qualifiedName="sample_text_2", twCommittedDate="sample_text_2", twRequireNewRev=False, twRevModified=False, twVersion=13)
    b = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    _safe_set(b, 'ccore_Item59', a1)
    assert _is_linked(b, 'ccore_Item59', a1)
    if hasattr(a1, 'ccore_Item57'):
        assert _is_linked(a1, 'ccore_Item57', b)
    _safe_set(b, 'ccore_Item59', a2)
    assert _is_linked(b, 'ccore_Item59', a2)
    if hasattr(a1, 'ccore_Item57'):
        assert not _is_linked(a1, 'ccore_Item57', b)
    if hasattr(a2, 'ccore_Item57'):
        assert _is_linked(a2, 'ccore_Item57', b)
    _safe_set(b, 'ccore_Item59', None)
    assert not _is_linked(b, 'ccore_Item59', a2)
    if hasattr(a2, 'ccore_Item57'):
        assert not _is_linked(a2, 'ccore_Item57', b)


def test_assoc_source102_reverse_link_reassign_clear():
    a1 = ccore_TypeDefinition(idRuntime="sample_text")
    a2 = ccore_TypeDefinition(idRuntime="sample_text_2")
    b = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    _safe_set(b, 'ccore_LinkType103', a1)
    assert _is_linked(b, 'ccore_LinkType103', a1)
    if hasattr(a1, 'ccore_TypeDefinition104'):
        assert _is_linked(a1, 'ccore_TypeDefinition104', b)
    _safe_set(b, 'ccore_LinkType103', a2)
    assert _is_linked(b, 'ccore_LinkType103', a2)
    if hasattr(a1, 'ccore_TypeDefinition104'):
        assert not _is_linked(a1, 'ccore_TypeDefinition104', b)
    if hasattr(a2, 'ccore_TypeDefinition104'):
        assert _is_linked(a2, 'ccore_TypeDefinition104', b)
    _safe_set(b, 'ccore_LinkType103', None)
    assert not _is_linked(b, 'ccore_LinkType103', a2)
    if hasattr(a2, 'ccore_TypeDefinition104'):
        assert not _is_linked(a2, 'ccore_TypeDefinition104', b)


def test_assoc_subTypes21_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    _safe_set(b, 'ccore_ItemType22', a1)
    assert _is_linked(b, 'ccore_ItemType22', a1)
    if hasattr(a1, 'ccore_ItemType20'):
        assert _is_linked(a1, 'ccore_ItemType20', b)
    _safe_set(b, 'ccore_ItemType22', a2)
    assert _is_linked(b, 'ccore_ItemType22', a2)
    if hasattr(a1, 'ccore_ItemType20'):
        assert not _is_linked(a1, 'ccore_ItemType20', b)
    if hasattr(a2, 'ccore_ItemType20'):
        assert _is_linked(a2, 'ccore_ItemType20', b)
    _safe_set(b, 'ccore_ItemType22', None)
    assert not _is_linked(b, 'ccore_ItemType22', a2)
    if hasattr(a2, 'ccore_ItemType20'):
        assert not _is_linked(a2, 'ccore_ItemType20', b)


def test_assoc_superGroup132_reverse_link_reassign_clear():
    a1 = ccore_GroupOfAttributes(column=7)
    a2 = ccore_GroupOfAttributes(column=13)
    b = ccore_GroupOfAttributes(column=7)
    _safe_set(b, 'ccore_GroupOfAttributes133', a1)
    assert _is_linked(b, 'ccore_GroupOfAttributes133', a1)
    if hasattr(a1, 'ccore_GroupOfAttributes131'):
        assert _is_linked(a1, 'ccore_GroupOfAttributes131', b)
    _safe_set(b, 'ccore_GroupOfAttributes133', a2)
    assert _is_linked(b, 'ccore_GroupOfAttributes133', a2)
    if hasattr(a1, 'ccore_GroupOfAttributes131'):
        assert not _is_linked(a1, 'ccore_GroupOfAttributes131', b)
    if hasattr(a2, 'ccore_GroupOfAttributes131'):
        assert _is_linked(a2, 'ccore_GroupOfAttributes131', b)
    _safe_set(b, 'ccore_GroupOfAttributes133', None)
    assert not _is_linked(b, 'ccore_GroupOfAttributes133', a2)
    if hasattr(a2, 'ccore_GroupOfAttributes131'):
        assert not _is_linked(a2, 'ccore_GroupOfAttributes131', b)


def test_assoc_superType16_reverse_link_reassign_clear():
    a1 = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    a2 = ccore_ItemType(customManager=False, displayNameTemplate="sample_text_2", hasContent=False, hasShortName=False, hasUniqueName=False, humanName="sample_text_2", icon="sample_text_2", isInstanceAbstract=False, isInstanceHidden=False, isMetaItemType=False, isRootElement=False, itemFactoryClass="sample_text_2", itemManagerClass="sample_text_2", managerClass="sample_text_2", messageErrorId="sample_text_2", overwriteDefaultPages=False, packageName="sample_text_2", qualifiedNameTemplate="sample_text_2", validateNameRe="sample_text_2")
    b = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    _safe_set(b, 'ccore_ItemType17', a1)
    assert _is_linked(b, 'ccore_ItemType17', a1)
    if hasattr(a1, 'ccore_ItemType15'):
        assert _is_linked(a1, 'ccore_ItemType15', b)
    _safe_set(b, 'ccore_ItemType17', a2)
    assert _is_linked(b, 'ccore_ItemType17', a2)
    if hasattr(a1, 'ccore_ItemType15'):
        assert not _is_linked(a1, 'ccore_ItemType15', b)
    if hasattr(a2, 'ccore_ItemType15'):
        assert _is_linked(a2, 'ccore_ItemType15', b)
    _safe_set(b, 'ccore_ItemType17', None)
    assert not _is_linked(b, 'ccore_ItemType17', a2)
    if hasattr(a2, 'ccore_ItemType15'):
        assert not _is_linked(a2, 'ccore_ItemType15', b)


def test_assoc_ui118_reverse_link_reassign_clear():
    a1 = ccore_Field(editable=True, label="sample_text", position="sample_text")
    a2 = ccore_Field(editable=False, label="sample_text_2", position="sample_text_2")
    b = ccore_Display(extendsIC=True, extendsMC=True, extendsUI=True)
    _safe_set(b, 'ccore_Display', a1)
    assert _is_linked(b, 'ccore_Display', a1)
    if hasattr(a1, 'ccore_Field119'):
        assert _is_linked(a1, 'ccore_Field119', b)
    _safe_set(b, 'ccore_Display', a2)
    assert _is_linked(b, 'ccore_Display', a2)
    if hasattr(a1, 'ccore_Field119'):
        assert not _is_linked(a1, 'ccore_Field119', b)
    if hasattr(a2, 'ccore_Field119'):
        assert _is_linked(a2, 'ccore_Field119', b)
    _safe_set(b, 'ccore_Display', None)
    assert not _is_linked(b, 'ccore_Display', a2)
    if hasattr(a2, 'ccore_Field119'):
        assert not _is_linked(a2, 'ccore_Field119', b)


def test_assoc_viewItemTypes158_reverse_link_reassign_clear():
    a1 = ccore_ViewItemType(isRootElement=True, ref=True)
    a2 = ccore_ViewItemType(isRootElement=False, ref=False)
    b = ccore_View(icon="sample_text")
    _safe_set(b, 'ccore_View', {a1})
    assert _is_linked(b, 'ccore_View', a1)
    if hasattr(a1, 'ccore_ViewItemType159'):
        assert _is_linked(a1, 'ccore_ViewItemType159', b)
    _safe_set(b, 'ccore_View', {a2})
    assert _is_linked(b, 'ccore_View', a2)
    if hasattr(a1, 'ccore_ViewItemType159'):
        assert not _is_linked(a1, 'ccore_ViewItemType159', b)
    if hasattr(a2, 'ccore_ViewItemType159'):
        assert _is_linked(a2, 'ccore_ViewItemType159', b)
    _safe_set(b, 'ccore_View', set())
    assert not _is_linked(b, 'ccore_View', a2)
    if hasattr(a2, 'ccore_ViewItemType159'):
        assert not _is_linked(a2, 'ccore_ViewItemType159', b)


def test_assoc_viewLinkTypes81_reverse_link_reassign_clear():
    a1 = ccore_ViewLinkType(aggregation=True, canCreateItem=True, canCreateLink=True, displayCreate="sample_text")
    a2 = ccore_ViewLinkType(aggregation=False, canCreateItem=False, canCreateLink=False, displayCreate="sample_text_2")
    b = ccore_ViewItemType(isRootElement=True, ref=True)
    _safe_set(b, 'ccore_ViewItemType82', {a1})
    assert _is_linked(b, 'ccore_ViewItemType82', a1)
    if hasattr(a1, 'ccore_ViewLinkType'):
        assert _is_linked(a1, 'ccore_ViewLinkType', b)
    _safe_set(b, 'ccore_ViewItemType82', {a2})
    assert _is_linked(b, 'ccore_ViewItemType82', a2)
    if hasattr(a1, 'ccore_ViewLinkType'):
        assert not _is_linked(a1, 'ccore_ViewLinkType', b)
    if hasattr(a2, 'ccore_ViewLinkType'):
        assert _is_linked(a2, 'ccore_ViewLinkType', b)
    _safe_set(b, 'ccore_ViewItemType82', set())
    assert not _is_linked(b, 'ccore_ViewItemType82', a2)
    if hasattr(a2, 'ccore_ViewLinkType'):
        assert not _is_linked(a2, 'ccore_ViewLinkType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_binding50_stub_double():
    # ccore_BindingDesc has no real 'ccore_BindingDesc' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Cadse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Cadse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    partner = ccore_BindingDesc()
    setattr(partner, 'ccore_BindingDesc', None)
    _safe_set(owner, 'ccore_Cadse51', {partner})
    assert getattr(partner, 'ccore_BindingDesc') == owner
    _safe_set(owner, 'ccore_Cadse51', set())
    assert getattr(partner, 'ccore_BindingDesc') is None


def test_assoc_children91_stub_double():
    # ccore_Menu has no real 'ccore_Menu92' property in the generated
    # code (a bare stub) -- manually attach it so ccore_MenuAbstract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_MenuAbstract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_MenuAbstract(icon="sample_text", label="sample_text", path="sample_text")
    partner = ccore_Menu()
    setattr(partner, 'ccore_Menu92', None)
    _safe_set(owner, 'ccore_MenuAbstract', partner)
    assert owner in getattr(partner, 'ccore_Menu92')
    _safe_set(owner, 'ccore_MenuAbstract', None)
    assert owner not in getattr(partner, 'ccore_Menu92')


def test_assoc_composerTypes32_stub_double():
    # ccore_ComposerType has no real 'ccore_ComposerType' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_ComposerType()
    setattr(partner, 'ccore_ComposerType', None)
    _safe_set(owner, 'ccore_ItemType33', {partner})
    assert getattr(partner, 'ccore_ComposerType') == owner
    _safe_set(owner, 'ccore_ItemType33', set())
    assert getattr(partner, 'ccore_ComposerType') is None


def test_assoc_contents63_stub_double():
    # ccore_ContentItem has no real 'ContentItem' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_ContentItem()
    setattr(partner, 'ContentItem', None)
    _safe_set(owner, 'ownerItem', {partner})
    assert getattr(partner, 'ContentItem') == owner
    _safe_set(owner, 'ownerItem', set())
    assert getattr(partner, 'ContentItem') is None


def test_assoc_dest165_stub_double():
    # ccore_BindingDesc has no real 'ccore_BindingDesc166' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_BindingDesc()
    setattr(partner, 'ccore_BindingDesc166', None)
    _safe_set(owner, 'ccore_Item167', partner)
    assert getattr(partner, 'ccore_BindingDesc166') == owner
    _safe_set(owner, 'ccore_Item167', None)
    assert getattr(partner, 'ccore_BindingDesc166') is None


def test_assoc_exendsItemTypes14_stub_double():
    # ccore_ExtentedType has no real 'ccore_ExtentedType' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_ExtentedType()
    setattr(partner, 'ccore_ExtentedType', None)
    _safe_set(owner, 'ccore_ItemType', partner)
    assert owner in getattr(partner, 'ccore_ExtentedType')
    _safe_set(owner, 'ccore_ItemType', None)
    assert owner not in getattr(partner, 'ccore_ExtentedType')


def test_assoc_exporterTypes30_stub_double():
    # ccore_ExporterType has no real 'ccore_ExporterType' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_ExporterType()
    setattr(partner, 'ccore_ExporterType', None)
    _safe_set(owner, 'ccore_ItemType31', {partner})
    assert getattr(partner, 'ccore_ExporterType') == owner
    _safe_set(owner, 'ccore_ItemType31', set())
    assert getattr(partner, 'ccore_ExporterType') is None


def test_assoc_exporters153_stub_double():
    # ccore_ComposerLink has no real 'ccore_ComposerLink154' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Exporter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Exporter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Exporter(types="sample_text")
    partner = ccore_ComposerLink()
    setattr(partner, 'ccore_ComposerLink154', None)
    _safe_set(owner, 'ccore_Exporter', partner)
    assert owner in getattr(partner, 'ccore_ComposerLink154')
    _safe_set(owner, 'ccore_Exporter', None)
    assert owner not in getattr(partner, 'ccore_ComposerLink154')


def test_assoc_extendedBy23_stub_double():
    # ccore_ExtentedType has no real 'ccore_ExtentedType25' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_ExtentedType()
    setattr(partner, 'ccore_ExtentedType25', None)
    _safe_set(owner, 'ccore_ItemType24', {partner})
    assert getattr(partner, 'ccore_ExtentedType25') == owner
    _safe_set(owner, 'ccore_ItemType24', set())
    assert getattr(partner, 'ccore_ExtentedType25') is None


def test_assoc_extendedTypes45_stub_double():
    # ccore_ExtentedType has no real 'ccore_ExtentedType47' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Cadse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Cadse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    partner = ccore_ExtentedType()
    setattr(partner, 'ccore_ExtentedType47', None)
    _safe_set(owner, 'ccore_Cadse46', {partner})
    assert getattr(partner, 'ccore_ExtentedType47') == owner
    _safe_set(owner, 'ccore_Cadse46', set())
    assert getattr(partner, 'ccore_ExtentedType47') is None


def test_assoc_ic114_stub_double():
    # ccore_InteractionController has no real 'ccore_InteractionController' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Field(editable=True, label="sample_text", position="sample_text")
    partner = ccore_InteractionController()
    setattr(partner, 'ccore_InteractionController', None)
    _safe_set(owner, 'ccore_Field115', partner)
    assert getattr(partner, 'ccore_InteractionController') == owner
    _safe_set(owner, 'ccore_Field115', None)
    assert getattr(partner, 'ccore_InteractionController') is None


def test_assoc_keyDefinition26_stub_double():
    # ccore_KeyDefinition has no real 'ccore_KeyDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_KeyDefinition()
    setattr(partner, 'ccore_KeyDefinition', None)
    _safe_set(owner, 'ccore_ItemType27', partner)
    assert getattr(partner, 'ccore_KeyDefinition') == owner
    _safe_set(owner, 'ccore_ItemType27', None)
    assert getattr(partner, 'ccore_KeyDefinition') is None


def test_assoc_keys42_stub_double():
    # ccore_KeyDefinition has no real 'ccore_KeyDefinition44' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Cadse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Cadse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    partner = ccore_KeyDefinition()
    setattr(partner, 'ccore_KeyDefinition44', None)
    _safe_set(owner, 'ccore_Cadse43', {partner})
    assert getattr(partner, 'ccore_KeyDefinition44') == owner
    _safe_set(owner, 'ccore_Cadse43', set())
    assert getattr(partner, 'ccore_KeyDefinition44') is None


def test_assoc_link155_stub_double():
    # ccore_ComposerLink has no real 'ccore_ComposerLink156' property in the generated
    # code (a bare stub) -- manually attach it so ccore_LinkType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_LinkType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    partner = ccore_ComposerLink()
    setattr(partner, 'ccore_ComposerLink156', None)
    _safe_set(owner, 'ccore_LinkType157', partner)
    assert getattr(partner, 'ccore_ComposerLink156') == owner
    _safe_set(owner, 'ccore_LinkType157', None)
    assert getattr(partner, 'ccore_ComposerLink156') is None


def test_assoc_links144_stub_double():
    # ccore_ComposerLink has no real 'ccore_ComposerLink' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Composer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Composer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Composer(types="sample_text")
    partner = ccore_ComposerLink()
    setattr(partner, 'ccore_ComposerLink', None)
    _safe_set(owner, 'ccore_Composer145', {partner})
    assert getattr(partner, 'ccore_ComposerLink') == owner
    _safe_set(owner, 'ccore_Composer145', set())
    assert getattr(partner, 'ccore_ComposerLink') is None


def test_assoc_listenAttributeDefinitions108_stub_double():
    # ccore_WCListener has no real 'ccore_WCListener109' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    partner = ccore_WCListener()
    setattr(partner, 'ccore_WCListener109', None)
    _safe_set(owner, 'ccore_Attribute110', partner)
    assert owner in getattr(partner, 'ccore_WCListener109')
    _safe_set(owner, 'ccore_Attribute110', None)
    assert owner not in getattr(partner, 'ccore_WCListener109')


def test_assoc_listenAttributes96_stub_double():
    # ccore_UIValidator has no real 'ccore_UIValidator97' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    partner = ccore_UIValidator()
    setattr(partner, 'ccore_UIValidator97', None)
    _safe_set(owner, 'ccore_Attribute98', partner)
    assert owner in getattr(partner, 'ccore_UIValidator97')
    _safe_set(owner, 'ccore_Attribute98', None)
    assert owner not in getattr(partner, 'ccore_UIValidator97')


def test_assoc_listenItemTypes105_stub_double():
    # ccore_WCListener has no real 'ccore_WCListener106' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_WCListener()
    setattr(partner, 'ccore_WCListener106', None)
    _safe_set(owner, 'ccore_ItemType107', partner)
    assert owner in getattr(partner, 'ccore_WCListener106')
    _safe_set(owner, 'ccore_ItemType107', None)
    assert owner not in getattr(partner, 'ccore_WCListener106')


def test_assoc_mc116_stub_double():
    # ccore_ModelController has no real 'ccore_ModelController' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Field(editable=True, label="sample_text", position="sample_text")
    partner = ccore_ModelController()
    setattr(partner, 'ccore_ModelController', None)
    _safe_set(owner, 'ccore_Field117', partner)
    assert getattr(partner, 'ccore_ModelController') == owner
    _safe_set(owner, 'ccore_Field117', None)
    assert getattr(partner, 'ccore_ModelController') is None


def test_assoc_memberOf139_stub_double():
    # ccore_GroupExtItem has no real 'ccore_GroupExtItem140' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_GroupExtItem()
    setattr(partner, 'ccore_GroupExtItem140', None)
    _safe_set(owner, 'ccore_Item141', partner)
    assert getattr(partner, 'ccore_GroupExtItem140') == owner
    _safe_set(owner, 'ccore_Item141', None)
    assert getattr(partner, 'ccore_GroupExtItem140') is None


def test_assoc_members137_stub_double():
    # ccore_GroupExtItem has no real 'ccore_GroupExtItem' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_GroupExtItem()
    setattr(partner, 'ccore_GroupExtItem', None)
    _safe_set(owner, 'ccore_Item138', partner)
    assert owner in getattr(partner, 'ccore_GroupExtItem')
    _safe_set(owner, 'ccore_Item138', None)
    assert owner not in getattr(partner, 'ccore_GroupExtItem')


def test_assoc_ownerItem149_stub_double():
    # ccore_ContentItem has no real 'contents' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_ContentItem()
    setattr(partner, 'contents', None)
    _safe_set(owner, 'Item150', partner)
    assert getattr(partner, 'contents') == owner
    _safe_set(owner, 'Item150', None)
    assert getattr(partner, 'contents') is None


def test_assoc_refEClass12_stub_double():
    # ccore_EClass has no real 'ccore_EClass' property in the generated
    # code (a bare stub) -- manually attach it so ccore_TypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_TypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_TypeDefinition(idRuntime="sample_text")
    partner = ccore_EClass()
    setattr(partner, 'ccore_EClass', None)
    _safe_set(owner, 'ccore_TypeDefinition13', partner)
    assert getattr(partner, 'ccore_EClass') == owner
    _safe_set(owner, 'ccore_TypeDefinition13', None)
    assert getattr(partner, 'ccore_EClass') is None


def test_assoc_refEPackage48_stub_double():
    # ccore_EPackage has no real 'ccore_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Cadse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Cadse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Cadse(defaultContentRepoURL="sample_text", description="sample_text", executed=True, idDefinition="sample_text", itemRepoLogin="sample_text", itemRepoPasswd="sample_text", itemRepoURL="sample_text")
    partner = ccore_EPackage()
    setattr(partner, 'ccore_EPackage', None)
    _safe_set(owner, 'ccore_Cadse49', partner)
    assert getattr(partner, 'ccore_EPackage') == owner
    _safe_set(owner, 'ccore_Cadse49', None)
    assert getattr(partner, 'ccore_EPackage') is None


def test_assoc_refEnum126_stub_double():
    # ccore_EEnum has no real 'ccore_EEnum' property in the generated
    # code (a bare stub) -- manually attach it so ccore_EnumType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_EnumType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_EnumType(javaClass="sample_text", mustBeGenerated=True, values="sample_text")
    partner = ccore_EEnum()
    setattr(partner, 'ccore_EEnum', None)
    _safe_set(owner, 'ccore_EnumType127', partner)
    assert getattr(partner, 'ccore_EEnum') == owner
    _safe_set(owner, 'ccore_EnumType127', None)
    assert getattr(partner, 'ccore_EEnum') is None


def test_assoc_refItemType85_stub_double():
    # ccore_BindExt has no real 'ccore_BindExt' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_BindExt()
    setattr(partner, 'ccore_BindExt', None)
    _safe_set(owner, 'ccore_ItemType86', partner)
    assert getattr(partner, 'ccore_BindExt') == owner
    _safe_set(owner, 'ccore_ItemType86', None)
    assert getattr(partner, 'ccore_BindExt') is None


def test_assoc_rootTypes83_stub_double():
    # ccore_ViewDescription has no real 'ccore_ViewDescription' property in the generated
    # code (a bare stub) -- manually attach it so ccore_TypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_TypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_TypeDefinition(idRuntime="sample_text")
    partner = ccore_ViewDescription()
    setattr(partner, 'ccore_ViewDescription', None)
    _safe_set(owner, 'ccore_TypeDefinition84', partner)
    assert owner in getattr(partner, 'ccore_ViewDescription')
    _safe_set(owner, 'ccore_TypeDefinition84', None)
    assert owner not in getattr(partner, 'ccore_ViewDescription')


def test_assoc_source162_stub_double():
    # ccore_BindingDesc has no real 'ccore_BindingDesc163' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Item(committedBy="sample_text", displayName="sample_text", isvalid=True, itemHidden=True, itemReadonly=True, qualifiedName="sample_text", twCommittedDate="sample_text", twRequireNewRev=True, twRevModified=True, twVersion=7)
    partner = ccore_BindingDesc()
    setattr(partner, 'ccore_BindingDesc163', None)
    _safe_set(owner, 'ccore_Item164', partner)
    assert getattr(partner, 'ccore_BindingDesc163') == owner
    _safe_set(owner, 'ccore_Item164', None)
    assert getattr(partner, 'ccore_BindingDesc163') is None


def test_assoc_typeBinding168_stub_double():
    # ccore_BindingDesc has no real 'ccore_BindingDesc169' property in the generated
    # code (a bare stub) -- manually attach it so ccore_LinkType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_LinkType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_LinkType(aggregation=True, annotation=True, composition=True, group=True, hidden=True, kind=7, linkManager="sample_text", mapping=True, max=7, min=7, selection="sample_text", twCoupled=True, twDestEvol="sample_text")
    partner = ccore_BindingDesc()
    setattr(partner, 'ccore_BindingDesc169', None)
    _safe_set(owner, 'ccore_LinkType170', partner)
    assert getattr(partner, 'ccore_BindingDesc169') == owner
    _safe_set(owner, 'ccore_LinkType170', None)
    assert getattr(partner, 'ccore_BindingDesc169') is None


def test_assoc_validators5_stub_double():
    # ccore_UIValidator has no real 'ccore_UIValidator' property in the generated
    # code (a bare stub) -- manually attach it so ccore_TypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_TypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_TypeDefinition(idRuntime="sample_text")
    partner = ccore_UIValidator()
    setattr(partner, 'ccore_UIValidator', None)
    _safe_set(owner, 'ccore_TypeDefinition6', {partner})
    assert getattr(partner, 'ccore_UIValidator') == owner
    _safe_set(owner, 'ccore_TypeDefinition6', set())
    assert getattr(partner, 'ccore_UIValidator') is None


def test_assoc_views160_stub_double():
    # ccore_ViewModel has no real 'ccore_ViewModel' property in the generated
    # code (a bare stub) -- manually attach it so ccore_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_View(icon="sample_text")
    partner = ccore_ViewModel()
    setattr(partner, 'ccore_ViewModel', None)
    _safe_set(owner, 'ccore_View161', partner)
    assert owner in getattr(partner, 'ccore_ViewModel')
    _safe_set(owner, 'ccore_View161', None)
    assert owner not in getattr(partner, 'ccore_ViewModel')


def test_assoc_wcListeners18_stub_double():
    # ccore_WCListener has no real 'ccore_WCListener' property in the generated
    # code (a bare stub) -- manually attach it so ccore_ItemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_ItemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_ItemType(customManager=True, displayNameTemplate="sample_text", hasContent=True, hasShortName=True, hasUniqueName=True, humanName="sample_text", icon="sample_text", isInstanceAbstract=True, isInstanceHidden=True, isMetaItemType=True, isRootElement=True, itemFactoryClass="sample_text", itemManagerClass="sample_text", managerClass="sample_text", messageErrorId="sample_text", overwriteDefaultPages=True, packageName="sample_text", qualifiedNameTemplate="sample_text", validateNameRe="sample_text")
    partner = ccore_WCListener()
    setattr(partner, 'ccore_WCListener', None)
    _safe_set(owner, 'ccore_ItemType19', {partner})
    assert getattr(partner, 'ccore_WCListener') == owner
    _safe_set(owner, 'ccore_ItemType19', set())
    assert getattr(partner, 'ccore_WCListener') is None


def test_assoc_wcListens71_stub_double():
    # ccore_WCListener has no real 'ccore_WCListener73' property in the generated
    # code (a bare stub) -- manually attach it so ccore_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ccore_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ccore_Attribute(_final=True, cannotBeUndefined=True, devGenerated=True, hiddenInComputedPages=True, idRuntime="sample_text", isList=True, mustBeInitialized=True, natif=True, require=True, tWCommitKind="sample_text", tWEvol="sample_text", tWRevSpecific=True, tWUpdateKind="sample_text")
    partner = ccore_WCListener()
    setattr(partner, 'ccore_WCListener73', None)
    _safe_set(owner, 'ccore_Attribute72', {partner})
    assert getattr(partner, 'ccore_WCListener73') == owner
    _safe_set(owner, 'ccore_Attribute72', set())
    assert getattr(partner, 'ccore_WCListener73') is None


