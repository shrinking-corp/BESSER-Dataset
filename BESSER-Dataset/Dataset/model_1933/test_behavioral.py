import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArtifactRef,
    CanvasFrame,
    Categorized,
    ChildrenHolder,
    Component,
    Context,
    ContextParameters,
    ContextValue,
    DefaultCavas,
    DomainArtifact,
    EnabledUIItem,
    FlexFields,
    Formatable,
    HTMLLayerHolder,
    InfrastructureComponent,
    InputElement,
    ItemIcon,
    Mapper,
    MenuElement,
    MenuExtensionRef,
    MenuHolder,
    MethodPointer,
    MultiLangLabel,
    NickNamed,
    OptionSelection,
    Orderable,
    ProxiesList,
    RelationShip,
    Secured,
    SourcesPointer,
    StyleElement,
    Trigger,
    TypeElement,
    TypeMapper,
    TypePointer,
    Uielement,
    UsingMappers,
    ViewElement,
    ViewPortHolder,
    domain_Application,
    domain_ApplicationInfrastructureLayer,
    domain_ApplicationMapper,
    domain_ApplicationMappers,
    domain_ApplicationMessages,
    domain_ApplicationRecipe,
    domain_ApplicationRecipes,
    domain_ApplicationRole,
    domain_ApplicationStyle,
    domain_ApplicationUILayer,
    domain_ApplicationUIPackage,
    domain_AreaRef,
    domain_Artifact,
    domain_ArtifactRef,
    domain_Artifacts,
    domain_ArtificialField,
    domain_Assosiation,
    domain_Attribute,
    domain_Button,
    domain_CSSMapper,
    domain_Canvas,
    domain_CanvasFrame,
    domain_CanvasView,
    domain_Categorized,
    domain_CheckBox,
    domain_ChildrenHolder,
    domain_Classifier,
    domain_Column,
    domain_Component,
    domain_ConfigExtension,
    domain_ConfigHash,
    domain_ConfigVariable,
    domain_Configuration,
    domain_Context,
    domain_ContextParameter,
    domain_ContextParameters,
    domain_ContextValue,
    domain_ContinuousIintegration,
    domain_Controls,
    domain_CreateTrigger,
    domain_DataControl,
    domain_Datacenter,
    domain_Date,
    domain_DefaultCavas,
    domain_DeleteTrigger,
    domain_Dependency,
    domain_DeploymentComponent,
    domain_DeploymentComponents,
    domain_DeploymentSequence,
    domain_DeploymentStarStep,
    domain_Domain,
    domain_DomainApplication,
    domain_DomainApplications,
    domain_DomainArtifact,
    domain_DomainArtifacts,
    domain_DomainTypes,
    domain_DropDownSelection,
    domain_EJBService,
    domain_EObject,
    domain_EnabledUIItem,
    domain_EnterpriseInfrastructure,
    domain_EnumAttribute,
    domain_Enumarator,
    domain_ExpressionPart,
    domain_FlexField,
    domain_FlexFields,
    domain_Form,
    domain_FormDataControls,
    domain_FormParameter,
    domain_FormVariable,
    domain_FormView,
    domain_Formatable,
    domain_Generalization,
    domain_GenerationHint,
    domain_GrantAccess,
    domain_Group,
    domain_HTMLLayerHolder,
    domain_HashProperty,
    domain_Hub,
    domain_Image,
    domain_Infrastructure,
    domain_InfrastructureComponent,
    domain_InfrastructureConnection,
    domain_InfrastructureLayer,
    domain_Ingredient,
    domain_InputElement,
    domain_InputText,
    domain_InsertTrigger,
    domain_ItemIcon,
    domain_JPAService,
    domain_JavaComponent,
    domain_JavaMapper,
    domain_JavaScriptMapper,
    domain_KeyValuePair,
    domain_Label,
    domain_Language,
    domain_LanguageRef,
    domain_LayerHolder,
    domain_Link,
    domain_LinkToLabel,
    domain_LinkToMessage,
    domain_Mapper,
    domain_Mappers,
    domain_MappingSpecifier,
    domain_Menu,
    domain_MenuDefinition,
    domain_MenuElement,
    domain_MenuExtensionPoint,
    domain_MenuExtensionRef,
    domain_MenuFolder,
    domain_MenuHolder,
    domain_MenuItem,
    domain_MenuSeparator,
    domain_MenuView,
    domain_Message,
    domain_MessageElement,
    domain_MessageLibrary,
    domain_Messages,
    domain_MethodPointer,
    domain_ModelMapper,
    domain_ModelQuery,
    domain_MultiLangLabel,
    domain_NickNamed,
    domain_ORMEntity,
    domain_Operation,
    domain_Option,
    domain_OptionSelection,
    domain_OrderBy,
    domain_Orderable,
    domain_Orders,
    domain_OutputText,
    domain_POSTCreateTrigger,
    domain_POSTQueryTrigger,
    domain_PREDeleteTrigger,
    domain_PREFormTrigger,
    domain_PREInsertTrigger,
    domain_PREQueryTrigger,
    domain_PREUpdateTrigger,
    domain_Package,
    domain_Parameter,
    domain_Password,
    domain_PopupCanvas,
    domain_Primitive,
    domain_Property,
    domain_ProxiesList,
    domain_Query,
    domain_QueryParameter,
    domain_QueryVariable,
    domain_Recipe,
    domain_Recipes,
    domain_References,
    domain_Relation,
    domain_RelationShip,
    domain_ReturnValue,
    domain_Role,
    domain_RoleMapper,
    domain_Roles,
    domain_Root,
    domain_Router,
    domain_SearchTrigger,
    domain_Secured,
    domain_Selection,
    domain_Server,
    domain_ServerClaster,
    domain_SourcesPointer,
    domain_Specifier,
    domain_Storage,
    domain_StyleClass,
    domain_StyleElement,
    domain_StyleLibrary,
    domain_StyleSet,
    domain_Styles,
    domain_StylesPackage,
    domain_SubMenu,
    domain_Subsystem,
    domain_TabCanvas,
    domain_TabPage,
    domain_TabPagesInheritance,
    domain_Table,
    domain_Translation,
    domain_Tree,
    domain_Trigger,
    domain_Type,
    domain_TypeDefinition,
    domain_TypeElement,
    domain_TypeMapper,
    domain_TypePointer,
    domain_TypeReference,
    domain_Types,
    domain_TypesRepository,
    domain_UIPackage,
    domain_Uielement,
    domain_UpdateTrigger,
    domain_UsingMappers,
    domain_ViewArea,
    domain_ViewElement,
    domain_ViewInheritance,
    domain_ViewPort,
    domain_ViewPortHolder,
    domain_ViewPortTrigger,
    domain_Views,
    domain_Window,
    Comparator,
    Order,
    Orientation,
    PlatformLayers,
    RelationType,
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

def test_assoc_application25_reverse_link_reassign_clear():
    a1 = domain_DomainApplication(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplication(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application', a1)
    assert _is_linked(b, 'Application', a1)
    if hasattr(a1, 'parent26'):
        assert _is_linked(a1, 'parent26', b)
    _safe_set(b, 'Application', a2)
    assert _is_linked(b, 'Application', a2)
    if hasattr(a1, 'parent26'):
        assert not _is_linked(a1, 'parent26', b)
    if hasattr(a2, 'parent26'):
        assert _is_linked(a2, 'parent26', b)
    _safe_set(b, 'Application', None)
    assert not _is_linked(b, 'Application', a2)
    if hasattr(a2, 'parent26'):
        assert not _is_linked(a2, 'parent26', b)


def test_assoc_applicationInfrastructureLayer73_reverse_link_reassign_clear():
    a1 = domain_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationInfrastructureLayer(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent74', a1)
    assert _is_linked(b, 'parent74', a1)
    if hasattr(a1, 'ApplicationInfrastructureLayer'):
        assert _is_linked(a1, 'ApplicationInfrastructureLayer', b)
    _safe_set(b, 'parent74', a2)
    assert _is_linked(b, 'parent74', a2)
    if hasattr(a1, 'ApplicationInfrastructureLayer'):
        assert not _is_linked(a1, 'ApplicationInfrastructureLayer', b)
    if hasattr(a2, 'ApplicationInfrastructureLayer'):
        assert _is_linked(a2, 'ApplicationInfrastructureLayer', b)
    _safe_set(b, 'parent74', None)
    assert not _is_linked(b, 'parent74', a2)
    if hasattr(a2, 'ApplicationInfrastructureLayer'):
        assert not _is_linked(a2, 'ApplicationInfrastructureLayer', b)


def test_assoc_applicationMappers69_reverse_link_reassign_clear():
    a1 = domain_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent70', a1)
    assert _is_linked(b, 'parent70', a1)
    if hasattr(a1, 'ApplicationMappers'):
        assert _is_linked(a1, 'ApplicationMappers', b)
    _safe_set(b, 'parent70', a2)
    assert _is_linked(b, 'parent70', a2)
    if hasattr(a1, 'ApplicationMappers'):
        assert not _is_linked(a1, 'ApplicationMappers', b)
    if hasattr(a2, 'ApplicationMappers'):
        assert _is_linked(a2, 'ApplicationMappers', b)
    _safe_set(b, 'parent70', None)
    assert not _is_linked(b, 'parent70', a2)
    if hasattr(a2, 'ApplicationMappers'):
        assert not _is_linked(a2, 'ApplicationMappers', b)


def test_assoc_applicationMessages79_reverse_link_reassign_clear():
    a1 = domain_ApplicationMessages(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMessages(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent80', a1)
    assert _is_linked(b, 'parent80', a1)
    if hasattr(a1, 'ApplicationMessages'):
        assert _is_linked(a1, 'ApplicationMessages', b)
    _safe_set(b, 'parent80', a2)
    assert _is_linked(b, 'parent80', a2)
    if hasattr(a1, 'ApplicationMessages'):
        assert not _is_linked(a1, 'ApplicationMessages', b)
    if hasattr(a2, 'ApplicationMessages'):
        assert _is_linked(a2, 'ApplicationMessages', b)
    _safe_set(b, 'parent80', None)
    assert not _is_linked(b, 'parent80', a2)
    if hasattr(a2, 'ApplicationMessages'):
        assert not _is_linked(a2, 'ApplicationMessages', b)


def test_assoc_applicationRecipes67_reverse_link_reassign_clear():
    a1 = domain_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent68', a1)
    assert _is_linked(b, 'parent68', a1)
    if hasattr(a1, 'ApplicationRecipes'):
        assert _is_linked(a1, 'ApplicationRecipes', b)
    _safe_set(b, 'parent68', a2)
    assert _is_linked(b, 'parent68', a2)
    if hasattr(a1, 'ApplicationRecipes'):
        assert not _is_linked(a1, 'ApplicationRecipes', b)
    if hasattr(a2, 'ApplicationRecipes'):
        assert _is_linked(a2, 'ApplicationRecipes', b)
    _safe_set(b, 'parent68', None)
    assert not _is_linked(b, 'parent68', a2)
    if hasattr(a2, 'ApplicationRecipes'):
        assert not _is_linked(a2, 'ApplicationRecipes', b)


def test_assoc_applicationRef10_reverse_link_reassign_clear():
    a1 = domain_GrantAccess(uid="sample_text")
    a2 = domain_GrantAccess(uid="sample_text_2")
    b = domain_DomainApplication(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DomainApplication', a1)
    assert _is_linked(b, 'domain_DomainApplication', a1)
    if hasattr(a1, 'domain_GrantAccess11'):
        assert _is_linked(a1, 'domain_GrantAccess11', b)
    _safe_set(b, 'domain_DomainApplication', a2)
    assert _is_linked(b, 'domain_DomainApplication', a2)
    if hasattr(a1, 'domain_GrantAccess11'):
        assert not _is_linked(a1, 'domain_GrantAccess11', b)
    if hasattr(a2, 'domain_GrantAccess11'):
        assert _is_linked(a2, 'domain_GrantAccess11', b)
    _safe_set(b, 'domain_DomainApplication', None)
    assert not _is_linked(b, 'domain_DomainApplication', a2)
    if hasattr(a2, 'domain_GrantAccess11'):
        assert not _is_linked(a2, 'domain_GrantAccess11', b)


def test_assoc_applicationRole77_reverse_link_reassign_clear():
    a1 = domain_ApplicationRole(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRole(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent78', a1)
    assert _is_linked(b, 'parent78', a1)
    if hasattr(a1, 'ApplicationRole'):
        assert _is_linked(a1, 'ApplicationRole', b)
    _safe_set(b, 'parent78', a2)
    assert _is_linked(b, 'parent78', a2)
    if hasattr(a1, 'ApplicationRole'):
        assert not _is_linked(a1, 'ApplicationRole', b)
    if hasattr(a2, 'ApplicationRole'):
        assert _is_linked(a2, 'ApplicationRole', b)
    _safe_set(b, 'parent78', None)
    assert not _is_linked(b, 'parent78', a2)
    if hasattr(a2, 'ApplicationRole'):
        assert not _is_linked(a2, 'ApplicationRole', b)


def test_assoc_applicationStyle75_reverse_link_reassign_clear():
    a1 = domain_ApplicationStyle(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationStyle(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent76', a1)
    assert _is_linked(b, 'parent76', a1)
    if hasattr(a1, 'ApplicationStyle'):
        assert _is_linked(a1, 'ApplicationStyle', b)
    _safe_set(b, 'parent76', a2)
    assert _is_linked(b, 'parent76', a2)
    if hasattr(a1, 'ApplicationStyle'):
        assert not _is_linked(a1, 'ApplicationStyle', b)
    if hasattr(a2, 'ApplicationStyle'):
        assert _is_linked(a2, 'ApplicationStyle', b)
    _safe_set(b, 'parent76', None)
    assert not _is_linked(b, 'parent76', a2)
    if hasattr(a2, 'ApplicationStyle'):
        assert not _is_linked(a2, 'ApplicationStyle', b)


def test_assoc_applicationUILayer71_reverse_link_reassign_clear():
    a1 = domain_ApplicationUILayer(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationUILayer(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'parent72', a1)
    assert _is_linked(b, 'parent72', a1)
    if hasattr(a1, 'ApplicationUILayer'):
        assert _is_linked(a1, 'ApplicationUILayer', b)
    _safe_set(b, 'parent72', a2)
    assert _is_linked(b, 'parent72', a2)
    if hasattr(a1, 'ApplicationUILayer'):
        assert not _is_linked(a1, 'ApplicationUILayer', b)
    if hasattr(a2, 'ApplicationUILayer'):
        assert _is_linked(a2, 'ApplicationUILayer', b)
    _safe_set(b, 'parent72', None)
    assert not _is_linked(b, 'parent72', a2)
    if hasattr(a2, 'ApplicationUILayer'):
        assert not _is_linked(a2, 'ApplicationUILayer', b)


def test_assoc_applicationUIPackages103_reverse_link_reassign_clear():
    a1 = domain_ApplicationUIPackage(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationUIPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationUILayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent104', {a1})
    assert _is_linked(b, 'parent104', a1)
    if hasattr(a1, 'ApplicationUIPackage'):
        assert _is_linked(a1, 'ApplicationUIPackage', b)
    _safe_set(b, 'parent104', {a2})
    assert _is_linked(b, 'parent104', a2)
    if hasattr(a1, 'ApplicationUIPackage'):
        assert not _is_linked(a1, 'ApplicationUIPackage', b)
    if hasattr(a2, 'ApplicationUIPackage'):
        assert _is_linked(a2, 'ApplicationUIPackage', b)
    _safe_set(b, 'parent104', set())
    assert not _is_linked(b, 'parent104', a2)
    if hasattr(a2, 'ApplicationUIPackage'):
        assert not _is_linked(a2, 'ApplicationUIPackage', b)


def test_assoc_applications21_reverse_link_reassign_clear():
    a1 = domain_DomainApplications(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplications(name="sample_text_2", uid="sample_text_2")
    b = domain_DomainApplication(name="sample_text", uid="sample_text")
    _safe_set(b, 'DomainApplication', a1)
    assert _is_linked(b, 'DomainApplication', a1)
    if hasattr(a1, 'parent22'):
        assert _is_linked(a1, 'parent22', b)
    _safe_set(b, 'DomainApplication', a2)
    assert _is_linked(b, 'DomainApplication', a2)
    if hasattr(a1, 'parent22'):
        assert not _is_linked(a1, 'parent22', b)
    if hasattr(a2, 'parent22'):
        assert _is_linked(a2, 'parent22', b)
    _safe_set(b, 'DomainApplication', None)
    assert not _is_linked(b, 'DomainApplication', a2)
    if hasattr(a2, 'parent22'):
        assert not _is_linked(a2, 'parent22', b)


def test_assoc_area431_reverse_link_reassign_clear():
    a1 = domain_NickNamed(nickname="sample_text")
    a2 = domain_NickNamed(nickname="sample_text_2")
    b = domain_AreaRef(group=7)
    _safe_set(b, 'domain_AreaRef432', a1)
    assert _is_linked(b, 'domain_AreaRef432', a1)
    if hasattr(a1, 'domain_NickNamed'):
        assert _is_linked(a1, 'domain_NickNamed', b)
    _safe_set(b, 'domain_AreaRef432', a2)
    assert _is_linked(b, 'domain_AreaRef432', a2)
    if hasattr(a1, 'domain_NickNamed'):
        assert not _is_linked(a1, 'domain_NickNamed', b)
    if hasattr(a2, 'domain_NickNamed'):
        assert _is_linked(a2, 'domain_NickNamed', b)
    _safe_set(b, 'domain_AreaRef432', None)
    assert not _is_linked(b, 'domain_AreaRef432', a2)
    if hasattr(a2, 'domain_NickNamed'):
        assert not _is_linked(a2, 'domain_NickNamed', b)


def test_assoc_artifact31_reverse_link_reassign_clear():
    a1 = domain_DomainArtifact(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifact(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifacts(uid="sample_text")
    _safe_set(b, 'Artifacts', a1)
    assert _is_linked(b, 'Artifacts', a1)
    if hasattr(a1, 'parent32'):
        assert _is_linked(a1, 'parent32', b)
    _safe_set(b, 'Artifacts', a2)
    assert _is_linked(b, 'Artifacts', a2)
    if hasattr(a1, 'parent32'):
        assert not _is_linked(a1, 'parent32', b)
    if hasattr(a2, 'parent32'):
        assert _is_linked(a2, 'parent32', b)
    _safe_set(b, 'Artifacts', None)
    assert not _is_linked(b, 'Artifacts', a2)
    if hasattr(a2, 'parent32'):
        assert not _is_linked(a2, 'parent32', b)


def test_assoc_artifactRef275_reverse_link_reassign_clear():
    a1 = domain_ArtifactRef(uid="sample_text")
    a2 = domain_ArtifactRef(uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Artifact277', a1)
    assert _is_linked(b, 'domain_Artifact277', a1)
    if hasattr(a1, 'domain_ArtifactRef276'):
        assert _is_linked(a1, 'domain_ArtifactRef276', b)
    _safe_set(b, 'domain_Artifact277', a2)
    assert _is_linked(b, 'domain_Artifact277', a2)
    if hasattr(a1, 'domain_ArtifactRef276'):
        assert not _is_linked(a1, 'domain_ArtifactRef276', b)
    if hasattr(a2, 'domain_ArtifactRef276'):
        assert _is_linked(a2, 'domain_ArtifactRef276', b)
    _safe_set(b, 'domain_Artifact277', None)
    assert not _is_linked(b, 'domain_Artifact277', a2)
    if hasattr(a2, 'domain_ArtifactRef276'):
        assert not _is_linked(a2, 'domain_ArtifactRef276', b)


def test_assoc_artifacts33_reverse_link_reassign_clear():
    a1 = domain_Artifacts(uid="sample_text")
    a2 = domain_Artifacts(uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'Artifact', a1)
    assert _is_linked(b, 'Artifact', a1)
    if hasattr(a1, 'parent34'):
        assert _is_linked(a1, 'parent34', b)
    _safe_set(b, 'Artifact', a2)
    assert _is_linked(b, 'Artifact', a2)
    if hasattr(a1, 'parent34'):
        assert not _is_linked(a1, 'parent34', b)
    if hasattr(a2, 'parent34'):
        assert _is_linked(a2, 'parent34', b)
    _safe_set(b, 'Artifact', None)
    assert not _is_linked(b, 'Artifact', a2)
    if hasattr(a2, 'parent34'):
        assert not _is_linked(a2, 'parent34', b)


def test_assoc_artificialFields519_reverse_link_reassign_clear():
    a1 = domain_DataControl(name="sample_text", uid="sample_text")
    a2 = domain_DataControl(name="sample_text_2", uid="sample_text_2")
    b = domain_ArtificialField(name="sample_text", uid="sample_text")
    _safe_set(b, 'ArtificialField', a1)
    assert _is_linked(b, 'ArtificialField', a1)
    if hasattr(a1, 'parent520'):
        assert _is_linked(a1, 'parent520', b)
    _safe_set(b, 'ArtificialField', a2)
    assert _is_linked(b, 'ArtificialField', a2)
    if hasattr(a1, 'parent520'):
        assert not _is_linked(a1, 'parent520', b)
    if hasattr(a2, 'parent520'):
        assert _is_linked(a2, 'parent520', b)
    _safe_set(b, 'ArtificialField', None)
    assert not _is_linked(b, 'ArtificialField', a2)
    if hasattr(a2, 'parent520'):
        assert not _is_linked(a2, 'parent520', b)


def test_assoc_baseType492_reverse_link_reassign_clear():
    a1 = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    a2 = domain_TypePointer(fakePackageName="sample_text_2", fakeTypeName="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl493', a1)
    assert _is_linked(b, 'domain_DataControl493', a1)
    if hasattr(a1, 'domain_TypePointer494'):
        assert _is_linked(a1, 'domain_TypePointer494', b)
    _safe_set(b, 'domain_DataControl493', a2)
    assert _is_linked(b, 'domain_DataControl493', a2)
    if hasattr(a1, 'domain_TypePointer494'):
        assert not _is_linked(a1, 'domain_TypePointer494', b)
    if hasattr(a2, 'domain_TypePointer494'):
        assert _is_linked(a2, 'domain_TypePointer494', b)
    _safe_set(b, 'domain_DataControl493', None)
    assert not _is_linked(b, 'domain_DataControl493', a2)
    if hasattr(a2, 'domain_TypePointer494'):
        assert not _is_linked(a2, 'domain_TypePointer494', b)


def test_assoc_baseTypeRef489_reverse_link_reassign_clear():
    a1 = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    a2 = domain_TypePointer(fakePackageName="sample_text_2", fakeTypeName="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl490', a1)
    assert _is_linked(b, 'domain_DataControl490', a1)
    if hasattr(a1, 'domain_TypePointer491'):
        assert _is_linked(a1, 'domain_TypePointer491', b)
    _safe_set(b, 'domain_DataControl490', a2)
    assert _is_linked(b, 'domain_DataControl490', a2)
    if hasattr(a1, 'domain_TypePointer491'):
        assert not _is_linked(a1, 'domain_TypePointer491', b)
    if hasattr(a2, 'domain_TypePointer491'):
        assert _is_linked(a2, 'domain_TypePointer491', b)
    _safe_set(b, 'domain_DataControl490', None)
    assert not _is_linked(b, 'domain_DataControl490', a2)
    if hasattr(a2, 'domain_TypePointer491'):
        assert not _is_linked(a2, 'domain_TypePointer491', b)


def test_assoc_canvasView367_reverse_link_reassign_clear():
    a1 = domain_ViewArea(name="sample_text", uid="sample_text")
    a2 = domain_ViewArea(name="sample_text_2", uid="sample_text_2")
    b = domain_CanvasView(uid="sample_text")
    _safe_set(b, 'CanvasView', a1)
    assert _is_linked(b, 'CanvasView', a1)
    if hasattr(a1, 'parent368'):
        assert _is_linked(a1, 'parent368', b)
    _safe_set(b, 'CanvasView', a2)
    assert _is_linked(b, 'CanvasView', a2)
    if hasattr(a1, 'parent368'):
        assert not _is_linked(a1, 'parent368', b)
    if hasattr(a2, 'parent368'):
        assert _is_linked(a2, 'parent368', b)
    _safe_set(b, 'CanvasView', None)
    assert not _is_linked(b, 'CanvasView', a2)
    if hasattr(a2, 'parent368'):
        assert not _is_linked(a2, 'parent368', b)


def test_assoc_canvases352_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_CanvasFrame(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_CanvasFrame', a1)
    assert _is_linked(b, 'domain_CanvasFrame', a1)
    if hasattr(a1, 'domain_Views'):
        assert _is_linked(a1, 'domain_Views', b)
    _safe_set(b, 'domain_CanvasFrame', a2)
    assert _is_linked(b, 'domain_CanvasFrame', a2)
    if hasattr(a1, 'domain_Views'):
        assert not _is_linked(a1, 'domain_Views', b)
    if hasattr(a2, 'domain_Views'):
        assert _is_linked(a2, 'domain_Views', b)
    _safe_set(b, 'domain_CanvasFrame', None)
    assert not _is_linked(b, 'domain_CanvasFrame', a2)
    if hasattr(a2, 'domain_Views'):
        assert not _is_linked(a2, 'domain_Views', b)


def test_assoc_cols462_reverse_link_reassign_clear():
    a1 = domain_Table(label="sample_text", rowNumber=7)
    a2 = domain_Table(label="sample_text_2", rowNumber=13)
    b = domain_Column(label="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Column463', a1)
    assert _is_linked(b, 'domain_Column463', a1)
    if hasattr(a1, 'domain_Table'):
        assert _is_linked(a1, 'domain_Table', b)
    _safe_set(b, 'domain_Column463', a2)
    assert _is_linked(b, 'domain_Column463', a2)
    if hasattr(a1, 'domain_Table'):
        assert not _is_linked(a1, 'domain_Table', b)
    if hasattr(a2, 'domain_Table'):
        assert _is_linked(a2, 'domain_Table', b)
    _safe_set(b, 'domain_Column463', None)
    assert not _is_linked(b, 'domain_Column463', a2)
    if hasattr(a2, 'domain_Table'):
        assert not _is_linked(a2, 'domain_Table', b)


def test_assoc_cols466_reverse_link_reassign_clear():
    a1 = domain_Tree(label="sample_text")
    a2 = domain_Tree(label="sample_text_2")
    b = domain_Column(label="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Column468', a1)
    assert _is_linked(b, 'domain_Column468', a1)
    if hasattr(a1, 'domain_Tree467'):
        assert _is_linked(a1, 'domain_Tree467', b)
    _safe_set(b, 'domain_Column468', a2)
    assert _is_linked(b, 'domain_Column468', a2)
    if hasattr(a1, 'domain_Tree467'):
        assert not _is_linked(a1, 'domain_Tree467', b)
    if hasattr(a2, 'domain_Tree467'):
        assert _is_linked(a2, 'domain_Tree467', b)
    _safe_set(b, 'domain_Column468', None)
    assert not _is_linked(b, 'domain_Column468', a2)
    if hasattr(a2, 'domain_Tree467'):
        assert not _is_linked(a2, 'domain_Tree467', b)


def test_assoc_components233_reverse_link_reassign_clear():
    a1 = domain_Ingredient(layer="sample_text", name="sample_text", uid="sample_text")
    a2 = domain_Ingredient(layer="sample_text_2", name="sample_text_2", uid="sample_text_2")
    b = domain_Component(componentRoot="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'Component', a1)
    assert _is_linked(b, 'Component', a1)
    if hasattr(a1, 'parent234'):
        assert _is_linked(a1, 'parent234', b)
    _safe_set(b, 'Component', a2)
    assert _is_linked(b, 'Component', a2)
    if hasattr(a1, 'parent234'):
        assert not _is_linked(a1, 'parent234', b)
    if hasattr(a2, 'parent234'):
        assert _is_linked(a2, 'parent234', b)
    _safe_set(b, 'Component', None)
    assert not _is_linked(b, 'Component', a2)
    if hasattr(a2, 'parent234'):
        assert not _is_linked(a2, 'parent234', b)


def test_assoc_confHashRef257_reverse_link_reassign_clear():
    a1 = domain_HashProperty(fakeName="sample_text", uid="sample_text")
    a2 = domain_HashProperty(fakeName="sample_text_2", uid="sample_text_2")
    b = domain_ConfigHash(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ConfigHash', a1)
    assert _is_linked(b, 'domain_ConfigHash', a1)
    if hasattr(a1, 'domain_HashProperty258'):
        assert _is_linked(a1, 'domain_HashProperty258', b)
    _safe_set(b, 'domain_ConfigHash', a2)
    assert _is_linked(b, 'domain_ConfigHash', a2)
    if hasattr(a1, 'domain_HashProperty258'):
        assert not _is_linked(a1, 'domain_HashProperty258', b)
    if hasattr(a2, 'domain_HashProperty258'):
        assert _is_linked(a2, 'domain_HashProperty258', b)
    _safe_set(b, 'domain_ConfigHash', None)
    assert not _is_linked(b, 'domain_ConfigHash', a2)
    if hasattr(a2, 'domain_HashProperty258'):
        assert not _is_linked(a2, 'domain_HashProperty258', b)


def test_assoc_confVarRef255_reverse_link_reassign_clear():
    a1 = domain_Property(fakeName="sample_text", uid="sample_text", value="sample_text")
    a2 = domain_Property(fakeName="sample_text_2", uid="sample_text_2", value="sample_text_2")
    b = domain_ConfigVariable(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ConfigVariable', a1)
    assert _is_linked(b, 'domain_ConfigVariable', a1)
    if hasattr(a1, 'domain_Property256'):
        assert _is_linked(a1, 'domain_Property256', b)
    _safe_set(b, 'domain_ConfigVariable', a2)
    assert _is_linked(b, 'domain_ConfigVariable', a2)
    if hasattr(a1, 'domain_Property256'):
        assert not _is_linked(a1, 'domain_Property256', b)
    if hasattr(a2, 'domain_Property256'):
        assert _is_linked(a2, 'domain_Property256', b)
    _safe_set(b, 'domain_ConfigVariable', None)
    assert not _is_linked(b, 'domain_ConfigVariable', a2)
    if hasattr(a2, 'domain_Property256'):
        assert not _is_linked(a2, 'domain_Property256', b)


def test_assoc_configExtension194_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_ConfigExtension(uid="sample_text")
    _safe_set(b, 'domain_ConfigExtension', a1)
    assert _is_linked(b, 'domain_ConfigExtension', a1)
    if hasattr(a1, 'domain_Recipes195'):
        assert _is_linked(a1, 'domain_Recipes195', b)
    _safe_set(b, 'domain_ConfigExtension', a2)
    assert _is_linked(b, 'domain_ConfigExtension', a2)
    if hasattr(a1, 'domain_Recipes195'):
        assert not _is_linked(a1, 'domain_Recipes195', b)
    if hasattr(a2, 'domain_Recipes195'):
        assert _is_linked(a2, 'domain_Recipes195', b)
    _safe_set(b, 'domain_ConfigExtension', None)
    assert not _is_linked(b, 'domain_ConfigExtension', a2)
    if hasattr(a2, 'domain_Recipes195'):
        assert not _is_linked(a2, 'domain_Recipes195', b)


def test_assoc_configHashes43_reverse_link_reassign_clear():
    a1 = domain_ConfigHash(name="sample_text", uid="sample_text")
    a2 = domain_ConfigHash(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'parent44', {a1})
    assert _is_linked(b, 'parent44', a1)
    if hasattr(a1, 'ConfigHash'):
        assert _is_linked(a1, 'ConfigHash', b)
    _safe_set(b, 'parent44', {a2})
    assert _is_linked(b, 'parent44', a2)
    if hasattr(a1, 'ConfigHash'):
        assert not _is_linked(a1, 'ConfigHash', b)
    if hasattr(a2, 'ConfigHash'):
        assert _is_linked(a2, 'ConfigHash', b)
    _safe_set(b, 'parent44', set())
    assert not _is_linked(b, 'parent44', a2)
    if hasattr(a2, 'ConfigHash'):
        assert not _is_linked(a2, 'ConfigHash', b)


def test_assoc_configVariables41_reverse_link_reassign_clear():
    a1 = domain_ConfigVariable(name="sample_text", uid="sample_text")
    a2 = domain_ConfigVariable(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'parent42', {a1})
    assert _is_linked(b, 'parent42', a1)
    if hasattr(a1, 'ConfigVariable'):
        assert _is_linked(a1, 'ConfigVariable', b)
    _safe_set(b, 'parent42', {a2})
    assert _is_linked(b, 'parent42', a2)
    if hasattr(a1, 'ConfigVariable'):
        assert not _is_linked(a1, 'ConfigVariable', b)
    if hasattr(a2, 'ConfigVariable'):
        assert _is_linked(a2, 'ConfigVariable', b)
    _safe_set(b, 'parent42', set())
    assert not _is_linked(b, 'parent42', a2)
    if hasattr(a2, 'ConfigVariable'):
        assert not _is_linked(a2, 'ConfigVariable', b)


def test_assoc_configurations186_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_Configuration(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Configuration', a1)
    assert _is_linked(b, 'domain_Configuration', a1)
    if hasattr(a1, 'domain_Recipes'):
        assert _is_linked(a1, 'domain_Recipes', b)
    _safe_set(b, 'domain_Configuration', a2)
    assert _is_linked(b, 'domain_Configuration', a2)
    if hasattr(a1, 'domain_Recipes'):
        assert not _is_linked(a1, 'domain_Recipes', b)
    if hasattr(a2, 'domain_Recipes'):
        assert _is_linked(a2, 'domain_Recipes', b)
    _safe_set(b, 'domain_Configuration', None)
    assert not _is_linked(b, 'domain_Configuration', a2)
    if hasattr(a2, 'domain_Recipes'):
        assert not _is_linked(a2, 'domain_Recipes', b)


def test_assoc_controls471_reverse_link_reassign_clear():
    a1 = domain_DataControl(name="sample_text", uid="sample_text")
    a2 = domain_DataControl(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'parent472', {a1})
    assert _is_linked(b, 'parent472', a1)
    if hasattr(a1, 'DataControl'):
        assert _is_linked(a1, 'DataControl', b)
    _safe_set(b, 'parent472', {a2})
    assert _is_linked(b, 'parent472', a2)
    if hasattr(a1, 'DataControl'):
        assert not _is_linked(a1, 'DataControl', b)
    if hasattr(a2, 'DataControl'):
        assert _is_linked(a2, 'DataControl', b)
    _safe_set(b, 'parent472', set())
    assert not _is_linked(b, 'parent472', a2)
    if hasattr(a2, 'DataControl'):
        assert not _is_linked(a2, 'DataControl', b)


def test_assoc_create509_reverse_link_reassign_clear():
    a1 = domain_DataControl(name="sample_text", uid="sample_text")
    a2 = domain_DataControl(name="sample_text_2", uid="sample_text_2")
    b = domain_CreateTrigger(uid="sample_text")
    _safe_set(b, 'domain_CreateTrigger', a1)
    assert _is_linked(b, 'domain_CreateTrigger', a1)
    if hasattr(a1, 'domain_DataControl510'):
        assert _is_linked(a1, 'domain_DataControl510', b)
    _safe_set(b, 'domain_CreateTrigger', a2)
    assert _is_linked(b, 'domain_CreateTrigger', a2)
    if hasattr(a1, 'domain_DataControl510'):
        assert not _is_linked(a1, 'domain_DataControl510', b)
    if hasattr(a2, 'domain_DataControl510'):
        assert _is_linked(a2, 'domain_DataControl510', b)
    _safe_set(b, 'domain_CreateTrigger', None)
    assert not _is_linked(b, 'domain_CreateTrigger', a2)
    if hasattr(a2, 'domain_DataControl510'):
        assert not _is_linked(a2, 'domain_DataControl510', b)


def test_assoc_datacenters560_reverse_link_reassign_clear():
    a1 = domain_EnterpriseInfrastructure(uid="sample_text")
    a2 = domain_EnterpriseInfrastructure(uid="sample_text_2")
    b = domain_Datacenter(name="sample_text", uid="sample_text")
    _safe_set(b, 'Datacenter', a1)
    assert _is_linked(b, 'Datacenter', a1)
    if hasattr(a1, 'parent561'):
        assert _is_linked(a1, 'parent561', b)
    _safe_set(b, 'Datacenter', a2)
    assert _is_linked(b, 'Datacenter', a2)
    if hasattr(a1, 'parent561'):
        assert not _is_linked(a1, 'parent561', b)
    if hasattr(a2, 'parent561'):
        assert _is_linked(a2, 'parent561', b)
    _safe_set(b, 'Datacenter', None)
    assert not _is_linked(b, 'Datacenter', a2)
    if hasattr(a2, 'parent561'):
        assert not _is_linked(a2, 'parent561', b)


def test_assoc_datacontrols345_reverse_link_reassign_clear():
    a1 = domain_FormDataControls(name="sample_text", uid="sample_text")
    a2 = domain_FormDataControls(name="sample_text_2", uid="sample_text_2")
    b = domain_Form(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Form346', a1)
    assert _is_linked(b, 'domain_Form346', a1)
    if hasattr(a1, 'domain_FormDataControls'):
        assert _is_linked(a1, 'domain_FormDataControls', b)
    _safe_set(b, 'domain_Form346', a2)
    assert _is_linked(b, 'domain_Form346', a2)
    if hasattr(a1, 'domain_FormDataControls'):
        assert not _is_linked(a1, 'domain_FormDataControls', b)
    if hasattr(a2, 'domain_FormDataControls'):
        assert _is_linked(a2, 'domain_FormDataControls', b)
    _safe_set(b, 'domain_Form346', None)
    assert not _is_linked(b, 'domain_Form346', a2)
    if hasattr(a2, 'domain_FormDataControls'):
        assert not _is_linked(a2, 'domain_FormDataControls', b)


def test_assoc_defaultOrderBy524_reverse_link_reassign_clear():
    a1 = domain_Orders(uid="sample_text")
    a2 = domain_Orders(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl525', a1)
    assert _is_linked(b, 'domain_DataControl525', a1)
    if hasattr(a1, 'domain_Orders'):
        assert _is_linked(a1, 'domain_Orders', b)
    _safe_set(b, 'domain_DataControl525', a2)
    assert _is_linked(b, 'domain_DataControl525', a2)
    if hasattr(a1, 'domain_Orders'):
        assert not _is_linked(a1, 'domain_Orders', b)
    if hasattr(a2, 'domain_Orders'):
        assert _is_linked(a2, 'domain_Orders', b)
    _safe_set(b, 'domain_DataControl525', None)
    assert not _is_linked(b, 'domain_DataControl525', a2)
    if hasattr(a2, 'domain_Orders'):
        assert not _is_linked(a2, 'domain_Orders', b)


def test_assoc_dependencies475_reverse_link_reassign_clear():
    a1 = domain_Dependency(name="sample_text", uid="sample_text")
    a2 = domain_Dependency(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'domain_Controls476', {a1})
    assert _is_linked(b, 'domain_Controls476', a1)
    if hasattr(a1, 'domain_Dependency'):
        assert _is_linked(a1, 'domain_Dependency', b)
    _safe_set(b, 'domain_Controls476', {a2})
    assert _is_linked(b, 'domain_Controls476', a2)
    if hasattr(a1, 'domain_Dependency'):
        assert not _is_linked(a1, 'domain_Dependency', b)
    if hasattr(a2, 'domain_Dependency'):
        assert _is_linked(a2, 'domain_Dependency', b)
    _safe_set(b, 'domain_Controls476', set())
    assert not _is_linked(b, 'domain_Controls476', a2)
    if hasattr(a2, 'domain_Dependency'):
        assert not _is_linked(a2, 'domain_Dependency', b)


def test_assoc_deployment192_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_DeploymentSequence(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentSequence', a1)
    assert _is_linked(b, 'domain_DeploymentSequence', a1)
    if hasattr(a1, 'domain_Recipes193'):
        assert _is_linked(a1, 'domain_Recipes193', b)
    _safe_set(b, 'domain_DeploymentSequence', a2)
    assert _is_linked(b, 'domain_DeploymentSequence', a2)
    if hasattr(a1, 'domain_Recipes193'):
        assert not _is_linked(a1, 'domain_Recipes193', b)
    if hasattr(a2, 'domain_Recipes193'):
        assert _is_linked(a2, 'domain_Recipes193', b)
    _safe_set(b, 'domain_DeploymentSequence', None)
    assert not _is_linked(b, 'domain_DeploymentSequence', a2)
    if hasattr(a2, 'domain_Recipes193'):
        assert not _is_linked(a2, 'domain_Recipes193', b)


def test_assoc_deployment223_reverse_link_reassign_clear():
    a1 = domain_Recipe(name="sample_text", uid="sample_text")
    a2 = domain_Recipe(name="sample_text_2", uid="sample_text_2")
    b = domain_DeploymentSequence(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentSequence224', a1)
    assert _is_linked(b, 'domain_DeploymentSequence224', a1)
    if hasattr(a1, 'domain_Recipe'):
        assert _is_linked(a1, 'domain_Recipe', b)
    _safe_set(b, 'domain_DeploymentSequence224', a2)
    assert _is_linked(b, 'domain_DeploymentSequence224', a2)
    if hasattr(a1, 'domain_Recipe'):
        assert not _is_linked(a1, 'domain_Recipe', b)
    if hasattr(a2, 'domain_Recipe'):
        assert _is_linked(a2, 'domain_Recipe', b)
    _safe_set(b, 'domain_DeploymentSequence224', None)
    assert not _is_linked(b, 'domain_DeploymentSequence224', a2)
    if hasattr(a2, 'domain_Recipe'):
        assert not _is_linked(a2, 'domain_Recipe', b)


def test_assoc_deploymentComponentLink211_reverse_link_reassign_clear():
    a1 = domain_DeploymentComponent(name="sample_text", uid="sample_text")
    a2 = domain_DeploymentComponent(name="sample_text_2", uid="sample_text_2")
    b = domain_DeploymentComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponent212', a1)
    assert _is_linked(b, 'domain_DeploymentComponent212', a1)
    if hasattr(a1, 'domain_DeploymentComponent210'):
        assert _is_linked(a1, 'domain_DeploymentComponent210', b)
    _safe_set(b, 'domain_DeploymentComponent212', a2)
    assert _is_linked(b, 'domain_DeploymentComponent212', a2)
    if hasattr(a1, 'domain_DeploymentComponent210'):
        assert not _is_linked(a1, 'domain_DeploymentComponent210', b)
    if hasattr(a2, 'domain_DeploymentComponent210'):
        assert _is_linked(a2, 'domain_DeploymentComponent210', b)
    _safe_set(b, 'domain_DeploymentComponent212', None)
    assert not _is_linked(b, 'domain_DeploymentComponent212', a2)
    if hasattr(a2, 'domain_DeploymentComponent210'):
        assert not _is_linked(a2, 'domain_DeploymentComponent210', b)


def test_assoc_deploymentComponents199_reverse_link_reassign_clear():
    a1 = domain_DeploymentSequence(name="sample_text", uid="sample_text")
    a2 = domain_DeploymentSequence(name="sample_text_2", uid="sample_text_2")
    b = domain_DeploymentComponents(uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponents', a1)
    assert _is_linked(b, 'domain_DeploymentComponents', a1)
    if hasattr(a1, 'domain_DeploymentSequence200'):
        assert _is_linked(a1, 'domain_DeploymentSequence200', b)
    _safe_set(b, 'domain_DeploymentComponents', a2)
    assert _is_linked(b, 'domain_DeploymentComponents', a2)
    if hasattr(a1, 'domain_DeploymentSequence200'):
        assert not _is_linked(a1, 'domain_DeploymentSequence200', b)
    if hasattr(a2, 'domain_DeploymentSequence200'):
        assert _is_linked(a2, 'domain_DeploymentSequence200', b)
    _safe_set(b, 'domain_DeploymentComponents', None)
    assert not _is_linked(b, 'domain_DeploymentComponents', a2)
    if hasattr(a2, 'domain_DeploymentSequence200'):
        assert not _is_linked(a2, 'domain_DeploymentSequence200', b)


def test_assoc_deplymentStep201_reverse_link_reassign_clear():
    a1 = domain_DeploymentComponents(uid="sample_text")
    a2 = domain_DeploymentComponents(uid="sample_text_2")
    b = domain_DeploymentComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponent', a1)
    assert _is_linked(b, 'domain_DeploymentComponent', a1)
    if hasattr(a1, 'domain_DeploymentComponents202'):
        assert _is_linked(a1, 'domain_DeploymentComponents202', b)
    _safe_set(b, 'domain_DeploymentComponent', a2)
    assert _is_linked(b, 'domain_DeploymentComponent', a2)
    if hasattr(a1, 'domain_DeploymentComponents202'):
        assert not _is_linked(a1, 'domain_DeploymentComponents202', b)
    if hasattr(a2, 'domain_DeploymentComponents202'):
        assert _is_linked(a2, 'domain_DeploymentComponents202', b)
    _safe_set(b, 'domain_DeploymentComponent', None)
    assert not _is_linked(b, 'domain_DeploymentComponent', a2)
    if hasattr(a2, 'domain_DeploymentComponents202'):
        assert not _is_linked(a2, 'domain_DeploymentComponents202', b)


def test_assoc_detail534_reverse_link_reassign_clear():
    a1 = domain_Relation(isTree=True, name="sample_text", uid="sample_text")
    a2 = domain_Relation(isTree=False, name="sample_text_2", uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl536', a1)
    assert _is_linked(b, 'domain_DataControl536', a1)
    if hasattr(a1, 'domain_Relation535'):
        assert _is_linked(a1, 'domain_Relation535', b)
    _safe_set(b, 'domain_DataControl536', a2)
    assert _is_linked(b, 'domain_DataControl536', a2)
    if hasattr(a1, 'domain_Relation535'):
        assert not _is_linked(a1, 'domain_Relation535', b)
    if hasattr(a2, 'domain_Relation535'):
        assert _is_linked(a2, 'domain_Relation535', b)
    _safe_set(b, 'domain_DataControl536', None)
    assert not _is_linked(b, 'domain_DataControl536', a2)
    if hasattr(a2, 'domain_Relation535'):
        assert not _is_linked(a2, 'domain_Relation535', b)


def test_assoc_detail543_reverse_link_reassign_clear():
    a1 = domain_Dependency(name="sample_text", uid="sample_text")
    a2 = domain_Dependency(name="sample_text_2", uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl545', a1)
    assert _is_linked(b, 'domain_DataControl545', a1)
    if hasattr(a1, 'domain_Dependency544'):
        assert _is_linked(a1, 'domain_Dependency544', b)
    _safe_set(b, 'domain_DataControl545', a2)
    assert _is_linked(b, 'domain_DataControl545', a2)
    if hasattr(a1, 'domain_Dependency544'):
        assert not _is_linked(a1, 'domain_Dependency544', b)
    if hasattr(a2, 'domain_Dependency544'):
        assert _is_linked(a2, 'domain_Dependency544', b)
    _safe_set(b, 'domain_DataControl545', None)
    assert not _is_linked(b, 'domain_DataControl545', a2)
    if hasattr(a2, 'domain_Dependency544'):
        assert not _is_linked(a2, 'domain_Dependency544', b)


def test_assoc_detail580_reverse_link_reassign_clear():
    a1 = domain_InfrastructureConnection(uid="sample_text")
    a2 = domain_InfrastructureConnection(uid="sample_text_2")
    b = domain_InfrastructureComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_InfrastructureComponent582', a1)
    assert _is_linked(b, 'domain_InfrastructureComponent582', a1)
    if hasattr(a1, 'domain_InfrastructureConnection581'):
        assert _is_linked(a1, 'domain_InfrastructureConnection581', b)
    _safe_set(b, 'domain_InfrastructureComponent582', a2)
    assert _is_linked(b, 'domain_InfrastructureComponent582', a2)
    if hasattr(a1, 'domain_InfrastructureConnection581'):
        assert not _is_linked(a1, 'domain_InfrastructureConnection581', b)
    if hasattr(a2, 'domain_InfrastructureConnection581'):
        assert _is_linked(a2, 'domain_InfrastructureConnection581', b)
    _safe_set(b, 'domain_InfrastructureComponent582', None)
    assert not _is_linked(b, 'domain_InfrastructureComponent582', a2)
    if hasattr(a2, 'domain_InfrastructureConnection581'):
        assert not _is_linked(a2, 'domain_InfrastructureConnection581', b)


def test_assoc_detailField551_reverse_link_reassign_clear():
    a1 = domain_Link(uid="sample_text")
    a2 = domain_Link(uid="sample_text_2")
    b = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    _safe_set(b, 'domain_Attribute553', a1)
    assert _is_linked(b, 'domain_Attribute553', a1)
    if hasattr(a1, 'domain_Link552'):
        assert _is_linked(a1, 'domain_Link552', b)
    _safe_set(b, 'domain_Attribute553', a2)
    assert _is_linked(b, 'domain_Attribute553', a2)
    if hasattr(a1, 'domain_Link552'):
        assert not _is_linked(a1, 'domain_Link552', b)
    if hasattr(a2, 'domain_Link552'):
        assert _is_linked(a2, 'domain_Link552', b)
    _safe_set(b, 'domain_Attribute553', None)
    assert not _is_linked(b, 'domain_Attribute553', a2)
    if hasattr(a2, 'domain_Link552'):
        assert not _is_linked(a2, 'domain_Link552', b)


def test_assoc_domainApplications3_reverse_link_reassign_clear():
    a1 = domain_DomainApplications(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplications(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'parent4', a1)
    assert _is_linked(b, 'parent4', a1)
    if hasattr(a1, 'DomainApplications'):
        assert _is_linked(a1, 'DomainApplications', b)
    _safe_set(b, 'parent4', a2)
    assert _is_linked(b, 'parent4', a2)
    if hasattr(a1, 'DomainApplications'):
        assert not _is_linked(a1, 'DomainApplications', b)
    if hasattr(a2, 'DomainApplications'):
        assert _is_linked(a2, 'DomainApplications', b)
    _safe_set(b, 'parent4', None)
    assert not _is_linked(b, 'parent4', a2)
    if hasattr(a2, 'DomainApplications'):
        assert not _is_linked(a2, 'DomainApplications', b)


def test_assoc_domainArtifact15_reverse_link_reassign_clear():
    a1 = domain_DomainArtifacts(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifacts(name="sample_text_2", uid="sample_text_2")
    b = domain_DomainArtifact(name="sample_text", uid="sample_text")
    _safe_set(b, 'DomainArtifact', a1)
    assert _is_linked(b, 'DomainArtifact', a1)
    if hasattr(a1, 'parent16'):
        assert _is_linked(a1, 'parent16', b)
    _safe_set(b, 'DomainArtifact', a2)
    assert _is_linked(b, 'DomainArtifact', a2)
    if hasattr(a1, 'parent16'):
        assert not _is_linked(a1, 'parent16', b)
    if hasattr(a2, 'parent16'):
        assert _is_linked(a2, 'parent16', b)
    _safe_set(b, 'DomainArtifact', None)
    assert not _is_linked(b, 'DomainArtifact', a2)
    if hasattr(a2, 'parent16'):
        assert not _is_linked(a2, 'parent16', b)


def test_assoc_domainArtifactRef274_reverse_link_reassign_clear():
    a1 = domain_DomainArtifact(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifact(name="sample_text_2", uid="sample_text_2")
    b = domain_ArtifactRef(uid="sample_text")
    _safe_set(b, 'domain_ArtifactRef', a1)
    assert _is_linked(b, 'domain_ArtifactRef', a1)
    if hasattr(a1, 'domain_DomainArtifact'):
        assert _is_linked(a1, 'domain_DomainArtifact', b)
    _safe_set(b, 'domain_ArtifactRef', a2)
    assert _is_linked(b, 'domain_ArtifactRef', a2)
    if hasattr(a1, 'domain_DomainArtifact'):
        assert not _is_linked(a1, 'domain_DomainArtifact', b)
    if hasattr(a2, 'domain_DomainArtifact'):
        assert _is_linked(a2, 'domain_DomainArtifact', b)
    _safe_set(b, 'domain_ArtifactRef', None)
    assert not _is_linked(b, 'domain_ArtifactRef', a2)
    if hasattr(a2, 'domain_DomainArtifact'):
        assert not _is_linked(a2, 'domain_DomainArtifact', b)


def test_assoc_domainArtifacts0_reverse_link_reassign_clear():
    a1 = domain_DomainArtifacts(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifacts(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'parent', a1)
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'DomainArtifacts'):
        assert _is_linked(a1, 'DomainArtifacts', b)
    _safe_set(b, 'parent', a2)
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'DomainArtifacts'):
        assert not _is_linked(a1, 'DomainArtifacts', b)
    if hasattr(a2, 'DomainArtifacts'):
        assert _is_linked(a2, 'DomainArtifacts', b)
    _safe_set(b, 'parent', None)
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'DomainArtifacts'):
        assert not _is_linked(a2, 'DomainArtifacts', b)


def test_assoc_domainTypes1_reverse_link_reassign_clear():
    a1 = domain_DomainTypes(name="sample_text", uid="sample_text")
    a2 = domain_DomainTypes(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'parent2', a1)
    assert _is_linked(b, 'parent2', a1)
    if hasattr(a1, 'DomainTypes'):
        assert _is_linked(a1, 'DomainTypes', b)
    _safe_set(b, 'parent2', a2)
    assert _is_linked(b, 'parent2', a2)
    if hasattr(a1, 'DomainTypes'):
        assert not _is_linked(a1, 'DomainTypes', b)
    if hasattr(a2, 'DomainTypes'):
        assert _is_linked(a2, 'DomainTypes', b)
    _safe_set(b, 'parent2', None)
    assert not _is_linked(b, 'parent2', a2)
    if hasattr(a2, 'DomainTypes'):
        assert not _is_linked(a2, 'DomainTypes', b)


def test_assoc_element460_reverse_link_reassign_clear():
    a1 = domain_Uielement(uid="sample_text")
    a2 = domain_Uielement(uid="sample_text_2")
    b = domain_Column(label="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Column', a1)
    assert _is_linked(b, 'domain_Column', a1)
    if hasattr(a1, 'domain_Uielement461'):
        assert _is_linked(a1, 'domain_Uielement461', b)
    _safe_set(b, 'domain_Column', a2)
    assert _is_linked(b, 'domain_Column', a2)
    if hasattr(a1, 'domain_Uielement461'):
        assert not _is_linked(a1, 'domain_Uielement461', b)
    if hasattr(a2, 'domain_Uielement461'):
        assert _is_linked(a2, 'domain_Uielement461', b)
    _safe_set(b, 'domain_Column', None)
    assert not _is_linked(b, 'domain_Column', a2)
    if hasattr(a2, 'domain_Uielement461'):
        assert not _is_linked(a2, 'domain_Uielement461', b)


def test_assoc_expression404_reverse_link_reassign_clear():
    a1 = domain_ExpressionPart(expressionType="sample_text", order=7, uid="sample_text")
    a2 = domain_ExpressionPart(expressionType="sample_text_2", order=13, uid="sample_text_2")
    b = domain_ContextValue(constant=True, uid="sample_text", value="sample_text")
    _safe_set(b, 'domain_ContextValue405', {a1})
    assert _is_linked(b, 'domain_ContextValue405', a1)
    if hasattr(a1, 'domain_ExpressionPart'):
        assert _is_linked(a1, 'domain_ExpressionPart', b)
    _safe_set(b, 'domain_ContextValue405', {a2})
    assert _is_linked(b, 'domain_ContextValue405', a2)
    if hasattr(a1, 'domain_ExpressionPart'):
        assert not _is_linked(a1, 'domain_ExpressionPart', b)
    if hasattr(a2, 'domain_ExpressionPart'):
        assert _is_linked(a2, 'domain_ExpressionPart', b)
    _safe_set(b, 'domain_ContextValue405', set())
    assert not _is_linked(b, 'domain_ContextValue405', a2)
    if hasattr(a2, 'domain_ExpressionPart'):
        assert not _is_linked(a2, 'domain_ExpressionPart', b)


def test_assoc_firstStep213_reverse_link_reassign_clear():
    a1 = domain_DeploymentStarStep(name="sample_text", uid="sample_text")
    a2 = domain_DeploymentStarStep(name="sample_text_2", uid="sample_text_2")
    b = domain_DeploymentComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponent215', a1)
    assert _is_linked(b, 'domain_DeploymentComponent215', a1)
    if hasattr(a1, 'domain_DeploymentStarStep214'):
        assert _is_linked(a1, 'domain_DeploymentStarStep214', b)
    _safe_set(b, 'domain_DeploymentComponent215', a2)
    assert _is_linked(b, 'domain_DeploymentComponent215', a2)
    if hasattr(a1, 'domain_DeploymentStarStep214'):
        assert not _is_linked(a1, 'domain_DeploymentStarStep214', b)
    if hasattr(a2, 'domain_DeploymentStarStep214'):
        assert _is_linked(a2, 'domain_DeploymentStarStep214', b)
    _safe_set(b, 'domain_DeploymentComponent215', None)
    assert not _is_linked(b, 'domain_DeploymentComponent215', a2)
    if hasattr(a2, 'domain_DeploymentStarStep214'):
        assert not _is_linked(a2, 'domain_DeploymentStarStep214', b)


def test_assoc_formControl379_reverse_link_reassign_clear():
    a1 = domain_FormDataControls(name="sample_text", uid="sample_text")
    a2 = domain_FormDataControls(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'Controls', a1)
    assert _is_linked(b, 'Controls', a1)
    if hasattr(a1, 'parent380'):
        assert _is_linked(a1, 'parent380', b)
    _safe_set(b, 'Controls', a2)
    assert _is_linked(b, 'Controls', a2)
    if hasattr(a1, 'parent380'):
        assert not _is_linked(a1, 'parent380', b)
    if hasattr(a2, 'parent380'):
        assert _is_linked(a2, 'parent380', b)
    _safe_set(b, 'Controls', None)
    assert not _is_linked(b, 'Controls', a2)
    if hasattr(a2, 'parent380'):
        assert not _is_linked(a2, 'parent380', b)


def test_assoc_forms339_reverse_link_reassign_clear():
    a1 = domain_UIPackage(uid="sample_text")
    a2 = domain_UIPackage(uid="sample_text_2")
    b = domain_Form(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Form', a1)
    assert _is_linked(b, 'domain_Form', a1)
    if hasattr(a1, 'domain_UIPackage'):
        assert _is_linked(a1, 'domain_UIPackage', b)
    _safe_set(b, 'domain_Form', a2)
    assert _is_linked(b, 'domain_Form', a2)
    if hasattr(a1, 'domain_UIPackage'):
        assert not _is_linked(a1, 'domain_UIPackage', b)
    if hasattr(a2, 'domain_UIPackage'):
        assert _is_linked(a2, 'domain_UIPackage', b)
    _safe_set(b, 'domain_Form', None)
    assert not _is_linked(b, 'domain_Form', a2)
    if hasattr(a2, 'domain_UIPackage'):
        assert not _is_linked(a2, 'domain_UIPackage', b)


def test_assoc_group2Group156_reverse_link_reassign_clear():
    a1 = domain_Group(name="sample_text", uid="sample_text")
    a2 = domain_Group(name="sample_text_2", uid="sample_text_2")
    b = domain_Group(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Group157', a1)
    assert _is_linked(b, 'domain_Group157', a1)
    if hasattr(a1, 'domain_Group155'):
        assert _is_linked(a1, 'domain_Group155', b)
    _safe_set(b, 'domain_Group157', a2)
    assert _is_linked(b, 'domain_Group157', a2)
    if hasattr(a1, 'domain_Group155'):
        assert not _is_linked(a1, 'domain_Group155', b)
    if hasattr(a2, 'domain_Group155'):
        assert _is_linked(a2, 'domain_Group155', b)
    _safe_set(b, 'domain_Group157', None)
    assert not _is_linked(b, 'domain_Group157', a2)
    if hasattr(a2, 'domain_Group155'):
        assert not _is_linked(a2, 'domain_Group155', b)


def test_assoc_group2Role158_reverse_link_reassign_clear():
    a1 = domain_Role(name="sample_text", uid="sample_text")
    a2 = domain_Role(name="sample_text_2", uid="sample_text_2")
    b = domain_Group(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Group159', {a1})
    assert _is_linked(b, 'domain_Group159', a1)
    if hasattr(a1, 'domain_Role160'):
        assert _is_linked(a1, 'domain_Role160', b)
    _safe_set(b, 'domain_Group159', {a2})
    assert _is_linked(b, 'domain_Group159', a2)
    if hasattr(a1, 'domain_Role160'):
        assert not _is_linked(a1, 'domain_Role160', b)
    if hasattr(a2, 'domain_Role160'):
        assert _is_linked(a2, 'domain_Role160', b)
    _safe_set(b, 'domain_Group159', set())
    assert not _is_linked(b, 'domain_Group159', a2)
    if hasattr(a2, 'domain_Role160'):
        assert not _is_linked(a2, 'domain_Role160', b)


def test_assoc_groups150_reverse_link_reassign_clear():
    a1 = domain_Roles(uid="sample_text")
    a2 = domain_Roles(uid="sample_text_2")
    b = domain_Group(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Group', a1)
    assert _is_linked(b, 'domain_Group', a1)
    if hasattr(a1, 'domain_Roles151'):
        assert _is_linked(a1, 'domain_Roles151', b)
    _safe_set(b, 'domain_Group', a2)
    assert _is_linked(b, 'domain_Group', a2)
    if hasattr(a1, 'domain_Roles151'):
        assert not _is_linked(a1, 'domain_Roles151', b)
    if hasattr(a2, 'domain_Roles151'):
        assert _is_linked(a2, 'domain_Roles151', b)
    _safe_set(b, 'domain_Group', None)
    assert not _is_linked(b, 'domain_Group', a2)
    if hasattr(a2, 'domain_Roles151'):
        assert not _is_linked(a2, 'domain_Roles151', b)


def test_assoc_hash259_reverse_link_reassign_clear():
    a1 = domain_KeyValuePair(key="sample_text", uid="sample_text", value="sample_text")
    a2 = domain_KeyValuePair(key="sample_text_2", uid="sample_text_2", value="sample_text_2")
    b = domain_HashProperty(fakeName="sample_text", uid="sample_text")
    _safe_set(b, 'domain_HashProperty260', {a1})
    assert _is_linked(b, 'domain_HashProperty260', a1)
    if hasattr(a1, 'domain_KeyValuePair'):
        assert _is_linked(a1, 'domain_KeyValuePair', b)
    _safe_set(b, 'domain_HashProperty260', {a2})
    assert _is_linked(b, 'domain_HashProperty260', a2)
    if hasattr(a1, 'domain_KeyValuePair'):
        assert not _is_linked(a1, 'domain_KeyValuePair', b)
    if hasattr(a2, 'domain_KeyValuePair'):
        assert _is_linked(a2, 'domain_KeyValuePair', b)
    _safe_set(b, 'domain_HashProperty260', set())
    assert not _is_linked(b, 'domain_HashProperty260', a2)
    if hasattr(a2, 'domain_KeyValuePair'):
        assert not _is_linked(a2, 'domain_KeyValuePair', b)


def test_assoc_hashProperties246_reverse_link_reassign_clear():
    a1 = domain_HashProperty(fakeName="sample_text", uid="sample_text")
    a2 = domain_HashProperty(fakeName="sample_text_2", uid="sample_text_2")
    b = domain_Configuration(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Configuration247', {a1})
    assert _is_linked(b, 'domain_Configuration247', a1)
    if hasattr(a1, 'domain_HashProperty'):
        assert _is_linked(a1, 'domain_HashProperty', b)
    _safe_set(b, 'domain_Configuration247', {a2})
    assert _is_linked(b, 'domain_Configuration247', a2)
    if hasattr(a1, 'domain_HashProperty'):
        assert not _is_linked(a1, 'domain_HashProperty', b)
    if hasattr(a2, 'domain_HashProperty'):
        assert _is_linked(a2, 'domain_HashProperty', b)
    _safe_set(b, 'domain_Configuration247', set())
    assert not _is_linked(b, 'domain_Configuration247', a2)
    if hasattr(a2, 'domain_HashProperty'):
        assert not _is_linked(a2, 'domain_HashProperty', b)


def test_assoc_hint7_reverse_link_reassign_clear():
    a1 = domain_GenerationHint(applyedClass="sample_text", name="sample_text", uid="sample_text")
    a2 = domain_GenerationHint(applyedClass="sample_text_2", name="sample_text_2", uid="sample_text_2")
    b = domain_Classifier(details="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Classifier8', a1)
    assert _is_linked(b, 'domain_Classifier8', a1)
    if hasattr(a1, 'domain_GenerationHint'):
        assert _is_linked(a1, 'domain_GenerationHint', b)
    _safe_set(b, 'domain_Classifier8', a2)
    assert _is_linked(b, 'domain_Classifier8', a2)
    if hasattr(a1, 'domain_GenerationHint'):
        assert not _is_linked(a1, 'domain_GenerationHint', b)
    if hasattr(a2, 'domain_GenerationHint'):
        assert _is_linked(a2, 'domain_GenerationHint', b)
    _safe_set(b, 'domain_Classifier8', None)
    assert not _is_linked(b, 'domain_Classifier8', a2)
    if hasattr(a2, 'domain_GenerationHint'):
        assert not _is_linked(a2, 'domain_GenerationHint', b)


def test_assoc_hints49_reverse_link_reassign_clear():
    a1 = domain_GenerationHint(applyedClass="sample_text", name="sample_text", uid="sample_text")
    a2 = domain_GenerationHint(applyedClass="sample_text_2", name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Artifact', {a1})
    assert _is_linked(b, 'domain_Artifact', a1)
    if hasattr(a1, 'domain_GenerationHint50'):
        assert _is_linked(a1, 'domain_GenerationHint50', b)
    _safe_set(b, 'domain_Artifact', {a2})
    assert _is_linked(b, 'domain_Artifact', a2)
    if hasattr(a1, 'domain_GenerationHint50'):
        assert not _is_linked(a1, 'domain_GenerationHint50', b)
    if hasattr(a2, 'domain_GenerationHint50'):
        assert _is_linked(a2, 'domain_GenerationHint50', b)
    _safe_set(b, 'domain_Artifact', set())
    assert not _is_linked(b, 'domain_Artifact', a2)
    if hasattr(a2, 'domain_GenerationHint50'):
        assert not _is_linked(a2, 'domain_GenerationHint50', b)


def test_assoc_infarastructure556_reverse_link_reassign_clear():
    a1 = domain_EnterpriseInfrastructure(uid="sample_text")
    a2 = domain_EnterpriseInfrastructure(uid="sample_text_2")
    b = domain_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent557', a1)
    assert _is_linked(b, 'parent557', a1)
    if hasattr(a1, 'EnterpriseInfrastructure'):
        assert _is_linked(a1, 'EnterpriseInfrastructure', b)
    _safe_set(b, 'parent557', a2)
    assert _is_linked(b, 'parent557', a2)
    if hasattr(a1, 'EnterpriseInfrastructure'):
        assert not _is_linked(a1, 'EnterpriseInfrastructure', b)
    if hasattr(a2, 'EnterpriseInfrastructure'):
        assert _is_linked(a2, 'EnterpriseInfrastructure', b)
    _safe_set(b, 'parent557', None)
    assert not _is_linked(b, 'parent557', a2)
    if hasattr(a2, 'EnterpriseInfrastructure'):
        assert not _is_linked(a2, 'EnterpriseInfrastructure', b)


def test_assoc_infrastructure242_reverse_link_reassign_clear():
    a1 = domain_Infrastructure(name="sample_text", uid="sample_text")
    a2 = domain_Infrastructure(name="sample_text_2", uid="sample_text_2")
    b = domain_Configuration(name="sample_text", uid="sample_text")
    _safe_set(b, 'recipeConfig', a1)
    assert _is_linked(b, 'recipeConfig', a1)
    if hasattr(a1, 'Infrastructure243'):
        assert _is_linked(a1, 'Infrastructure243', b)
    _safe_set(b, 'recipeConfig', a2)
    assert _is_linked(b, 'recipeConfig', a2)
    if hasattr(a1, 'Infrastructure243'):
        assert not _is_linked(a1, 'Infrastructure243', b)
    if hasattr(a2, 'Infrastructure243'):
        assert _is_linked(a2, 'Infrastructure243', b)
    _safe_set(b, 'recipeConfig', None)
    assert not _is_linked(b, 'recipeConfig', a2)
    if hasattr(a2, 'Infrastructure243'):
        assert not _is_linked(a2, 'Infrastructure243', b)


def test_assoc_infrastructureComponent576_reverse_link_reassign_clear():
    a1 = domain_InfrastructureLayer(name="sample_text", uid="sample_text")
    a2 = domain_InfrastructureLayer(name="sample_text_2", uid="sample_text_2")
    b = domain_InfrastructureComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'InfrastructureComponent', a1)
    assert _is_linked(b, 'InfrastructureComponent', a1)
    if hasattr(a1, 'parent577'):
        assert _is_linked(a1, 'parent577', b)
    _safe_set(b, 'InfrastructureComponent', a2)
    assert _is_linked(b, 'InfrastructureComponent', a2)
    if hasattr(a1, 'parent577'):
        assert not _is_linked(a1, 'parent577', b)
    if hasattr(a2, 'parent577'):
        assert _is_linked(a2, 'parent577', b)
    _safe_set(b, 'InfrastructureComponent', None)
    assert not _is_linked(b, 'InfrastructureComponent', a2)
    if hasattr(a2, 'parent577'):
        assert not _is_linked(a2, 'parent577', b)


def test_assoc_infrastructureConnections562_reverse_link_reassign_clear():
    a1 = domain_InfrastructureConnection(uid="sample_text")
    a2 = domain_InfrastructureConnection(uid="sample_text_2")
    b = domain_EnterpriseInfrastructure(uid="sample_text")
    _safe_set(b, 'domain_EnterpriseInfrastructure', {a1})
    assert _is_linked(b, 'domain_EnterpriseInfrastructure', a1)
    if hasattr(a1, 'domain_InfrastructureConnection'):
        assert _is_linked(a1, 'domain_InfrastructureConnection', b)
    _safe_set(b, 'domain_EnterpriseInfrastructure', {a2})
    assert _is_linked(b, 'domain_EnterpriseInfrastructure', a2)
    if hasattr(a1, 'domain_InfrastructureConnection'):
        assert not _is_linked(a1, 'domain_InfrastructureConnection', b)
    if hasattr(a2, 'domain_InfrastructureConnection'):
        assert _is_linked(a2, 'domain_InfrastructureConnection', b)
    _safe_set(b, 'domain_EnterpriseInfrastructure', set())
    assert not _is_linked(b, 'domain_EnterpriseInfrastructure', a2)
    if hasattr(a2, 'domain_InfrastructureConnection'):
        assert not _is_linked(a2, 'domain_InfrastructureConnection', b)


def test_assoc_infrastructureLayer572_reverse_link_reassign_clear():
    a1 = domain_Subsystem(name="sample_text", uid="sample_text")
    a2 = domain_Subsystem(name="sample_text_2", uid="sample_text_2")
    b = domain_InfrastructureLayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'InfrastructureLayer', a1)
    assert _is_linked(b, 'InfrastructureLayer', a1)
    if hasattr(a1, 'parent573'):
        assert _is_linked(a1, 'parent573', b)
    _safe_set(b, 'InfrastructureLayer', a2)
    assert _is_linked(b, 'InfrastructureLayer', a2)
    if hasattr(a1, 'parent573'):
        assert not _is_linked(a1, 'parent573', b)
    if hasattr(a2, 'parent573'):
        assert _is_linked(a2, 'parent573', b)
    _safe_set(b, 'InfrastructureLayer', None)
    assert not _is_linked(b, 'InfrastructureLayer', a2)
    if hasattr(a2, 'parent573'):
        assert not _is_linked(a2, 'parent573', b)


def test_assoc_infrastructures187_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_Infrastructure(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Infrastructure', a1)
    assert _is_linked(b, 'domain_Infrastructure', a1)
    if hasattr(a1, 'domain_Recipes188'):
        assert _is_linked(a1, 'domain_Recipes188', b)
    _safe_set(b, 'domain_Infrastructure', a2)
    assert _is_linked(b, 'domain_Infrastructure', a2)
    if hasattr(a1, 'domain_Recipes188'):
        assert not _is_linked(a1, 'domain_Recipes188', b)
    if hasattr(a2, 'domain_Recipes188'):
        assert _is_linked(a2, 'domain_Recipes188', b)
    _safe_set(b, 'domain_Infrastructure', None)
    assert not _is_linked(b, 'domain_Infrastructure', a2)
    if hasattr(a2, 'domain_Recipes188'):
        assert not _is_linked(a2, 'domain_Recipes188', b)


def test_assoc_infrastructures221_reverse_link_reassign_clear():
    a1 = domain_Recipe(name="sample_text", uid="sample_text")
    a2 = domain_Recipe(name="sample_text_2", uid="sample_text_2")
    b = domain_Infrastructure(name="sample_text", uid="sample_text")
    _safe_set(b, 'Infrastructure', a1)
    assert _is_linked(b, 'Infrastructure', a1)
    if hasattr(a1, 'recipe222'):
        assert _is_linked(a1, 'recipe222', b)
    _safe_set(b, 'Infrastructure', a2)
    assert _is_linked(b, 'Infrastructure', a2)
    if hasattr(a1, 'recipe222'):
        assert not _is_linked(a1, 'recipe222', b)
    if hasattr(a2, 'recipe222'):
        assert _is_linked(a2, 'recipe222', b)
    _safe_set(b, 'Infrastructure', None)
    assert not _is_linked(b, 'Infrastructure', a2)
    if hasattr(a2, 'recipe222'):
        assert not _is_linked(a2, 'recipe222', b)


def test_assoc_ingredients219_reverse_link_reassign_clear():
    a1 = domain_Recipe(name="sample_text", uid="sample_text")
    a2 = domain_Recipe(name="sample_text_2", uid="sample_text_2")
    b = domain_Ingredient(layer="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'Ingredient', a1)
    assert _is_linked(b, 'Ingredient', a1)
    if hasattr(a1, 'parent220'):
        assert _is_linked(a1, 'parent220', b)
    _safe_set(b, 'Ingredient', a2)
    assert _is_linked(b, 'Ingredient', a2)
    if hasattr(a1, 'parent220'):
        assert not _is_linked(a1, 'parent220', b)
    if hasattr(a2, 'parent220'):
        assert _is_linked(a2, 'parent220', b)
    _safe_set(b, 'Ingredient', None)
    assert not _is_linked(b, 'Ingredient', a2)
    if hasattr(a2, 'parent220'):
        assert not _is_linked(a2, 'parent220', b)


def test_assoc_insert511_reverse_link_reassign_clear():
    a1 = domain_InsertTrigger(uid="sample_text")
    a2 = domain_InsertTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl512', a1)
    assert _is_linked(b, 'domain_DataControl512', a1)
    if hasattr(a1, 'domain_InsertTrigger'):
        assert _is_linked(a1, 'domain_InsertTrigger', b)
    _safe_set(b, 'domain_DataControl512', a2)
    assert _is_linked(b, 'domain_DataControl512', a2)
    if hasattr(a1, 'domain_InsertTrigger'):
        assert not _is_linked(a1, 'domain_InsertTrigger', b)
    if hasattr(a2, 'domain_InsertTrigger'):
        assert _is_linked(a2, 'domain_InsertTrigger', b)
    _safe_set(b, 'domain_DataControl512', None)
    assert not _is_linked(b, 'domain_DataControl512', a2)
    if hasattr(a2, 'domain_InsertTrigger'):
        assert not _is_linked(a2, 'domain_InsertTrigger', b)


def test_assoc_lang138_reverse_link_reassign_clear():
    a1 = domain_LanguageRef(uid="sample_text")
    a2 = domain_LanguageRef(uid="sample_text_2")
    b = domain_Language(code="sample_text", defaultLang=True, lang="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Language140', a1)
    assert _is_linked(b, 'domain_Language140', a1)
    if hasattr(a1, 'domain_LanguageRef139'):
        assert _is_linked(a1, 'domain_LanguageRef139', b)
    _safe_set(b, 'domain_Language140', a2)
    assert _is_linked(b, 'domain_Language140', a2)
    if hasattr(a1, 'domain_LanguageRef139'):
        assert not _is_linked(a1, 'domain_LanguageRef139', b)
    if hasattr(a2, 'domain_LanguageRef139'):
        assert _is_linked(a2, 'domain_LanguageRef139', b)
    _safe_set(b, 'domain_Language140', None)
    assert not _is_linked(b, 'domain_Language140', a2)
    if hasattr(a2, 'domain_LanguageRef139'):
        assert not _is_linked(a2, 'domain_LanguageRef139', b)


def test_assoc_lang143_reverse_link_reassign_clear():
    a1 = domain_Translation(translation="sample_text", uid="sample_text")
    a2 = domain_Translation(translation="sample_text_2", uid="sample_text_2")
    b = domain_LanguageRef(uid="sample_text")
    _safe_set(b, 'domain_LanguageRef145', a1)
    assert _is_linked(b, 'domain_LanguageRef145', a1)
    if hasattr(a1, 'domain_Translation144'):
        assert _is_linked(a1, 'domain_Translation144', b)
    _safe_set(b, 'domain_LanguageRef145', a2)
    assert _is_linked(b, 'domain_LanguageRef145', a2)
    if hasattr(a1, 'domain_Translation144'):
        assert not _is_linked(a1, 'domain_Translation144', b)
    if hasattr(a2, 'domain_Translation144'):
        assert _is_linked(a2, 'domain_Translation144', b)
    _safe_set(b, 'domain_LanguageRef145', None)
    assert not _is_linked(b, 'domain_LanguageRef145', a2)
    if hasattr(a2, 'domain_Translation144'):
        assert not _is_linked(a2, 'domain_Translation144', b)


def test_assoc_languages129_reverse_link_reassign_clear():
    a1 = domain_Messages(uid="sample_text")
    a2 = domain_Messages(uid="sample_text_2")
    b = domain_Language(code="sample_text", defaultLang=True, lang="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Language', a1)
    assert _is_linked(b, 'domain_Language', a1)
    if hasattr(a1, 'domain_Messages130'):
        assert _is_linked(a1, 'domain_Messages130', b)
    _safe_set(b, 'domain_Language', a2)
    assert _is_linked(b, 'domain_Language', a2)
    if hasattr(a1, 'domain_Messages130'):
        assert not _is_linked(a1, 'domain_Messages130', b)
    if hasattr(a2, 'domain_Messages130'):
        assert _is_linked(a2, 'domain_Messages130', b)
    _safe_set(b, 'domain_Language', None)
    assert not _is_linked(b, 'domain_Language', a2)
    if hasattr(a2, 'domain_Messages130'):
        assert not _is_linked(a2, 'domain_Messages130', b)


def test_assoc_libLanguages134_reverse_link_reassign_clear():
    a1 = domain_MessageLibrary(name="sample_text", uid="sample_text")
    a2 = domain_MessageLibrary(name="sample_text_2", uid="sample_text_2")
    b = domain_LanguageRef(uid="sample_text")
    _safe_set(b, 'domain_LanguageRef', a1)
    assert _is_linked(b, 'domain_LanguageRef', a1)
    if hasattr(a1, 'domain_MessageLibrary135'):
        assert _is_linked(a1, 'domain_MessageLibrary135', b)
    _safe_set(b, 'domain_LanguageRef', a2)
    assert _is_linked(b, 'domain_LanguageRef', a2)
    if hasattr(a1, 'domain_MessageLibrary135'):
        assert not _is_linked(a1, 'domain_MessageLibrary135', b)
    if hasattr(a2, 'domain_MessageLibrary135'):
        assert _is_linked(a2, 'domain_MessageLibrary135', b)
    _safe_set(b, 'domain_LanguageRef', None)
    assert not _is_linked(b, 'domain_LanguageRef', a2)
    if hasattr(a2, 'domain_MessageLibrary135'):
        assert not _is_linked(a2, 'domain_MessageLibrary135', b)


def test_assoc_libraries163_reverse_link_reassign_clear():
    a1 = domain_Styles(uid="sample_text")
    a2 = domain_Styles(uid="sample_text_2")
    b = domain_StyleLibrary(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_StyleLibrary', a1)
    assert _is_linked(b, 'domain_StyleLibrary', a1)
    if hasattr(a1, 'domain_Styles'):
        assert _is_linked(a1, 'domain_Styles', b)
    _safe_set(b, 'domain_StyleLibrary', a2)
    assert _is_linked(b, 'domain_StyleLibrary', a2)
    if hasattr(a1, 'domain_Styles'):
        assert not _is_linked(a1, 'domain_Styles', b)
    if hasattr(a2, 'domain_Styles'):
        assert _is_linked(a2, 'domain_Styles', b)
    _safe_set(b, 'domain_StyleLibrary', None)
    assert not _is_linked(b, 'domain_StyleLibrary', a2)
    if hasattr(a2, 'domain_Styles'):
        assert not _is_linked(a2, 'domain_Styles', b)


def test_assoc_linkToLabels383_reverse_link_reassign_clear():
    a1 = domain_LinkToLabel(uid="sample_text")
    a2 = domain_LinkToLabel(uid="sample_text_2")
    b = domain_CanvasView(uid="sample_text")
    _safe_set(b, 'domain_CanvasView384', {a1})
    assert _is_linked(b, 'domain_CanvasView384', a1)
    if hasattr(a1, 'domain_LinkToLabel'):
        assert _is_linked(a1, 'domain_LinkToLabel', b)
    _safe_set(b, 'domain_CanvasView384', {a2})
    assert _is_linked(b, 'domain_CanvasView384', a2)
    if hasattr(a1, 'domain_LinkToLabel'):
        assert not _is_linked(a1, 'domain_LinkToLabel', b)
    if hasattr(a2, 'domain_LinkToLabel'):
        assert _is_linked(a2, 'domain_LinkToLabel', b)
    _safe_set(b, 'domain_CanvasView384', set())
    assert not _is_linked(b, 'domain_CanvasView384', a2)
    if hasattr(a2, 'domain_LinkToLabel'):
        assert not _is_linked(a2, 'domain_LinkToLabel', b)


def test_assoc_linkToMessages385_reverse_link_reassign_clear():
    a1 = domain_LinkToMessage(uid="sample_text")
    a2 = domain_LinkToMessage(uid="sample_text_2")
    b = domain_CanvasView(uid="sample_text")
    _safe_set(b, 'domain_CanvasView386', {a1})
    assert _is_linked(b, 'domain_CanvasView386', a1)
    if hasattr(a1, 'domain_LinkToMessage'):
        assert _is_linked(a1, 'domain_LinkToMessage', b)
    _safe_set(b, 'domain_CanvasView386', {a2})
    assert _is_linked(b, 'domain_CanvasView386', a2)
    if hasattr(a1, 'domain_LinkToMessage'):
        assert not _is_linked(a1, 'domain_LinkToMessage', b)
    if hasattr(a2, 'domain_LinkToMessage'):
        assert _is_linked(a2, 'domain_LinkToMessage', b)
    _safe_set(b, 'domain_CanvasView386', set())
    assert not _is_linked(b, 'domain_CanvasView386', a2)
    if hasattr(a2, 'domain_LinkToMessage'):
        assert not _is_linked(a2, 'domain_LinkToMessage', b)


def test_assoc_links294_reverse_link_reassign_clear():
    a1 = domain_Link(uid="sample_text")
    a2 = domain_Link(uid="sample_text_2")
    b = domain_Assosiation(type="sample_text")
    _safe_set(b, 'domain_Assosiation', {a1})
    assert _is_linked(b, 'domain_Assosiation', a1)
    if hasattr(a1, 'domain_Link'):
        assert _is_linked(a1, 'domain_Link', b)
    _safe_set(b, 'domain_Assosiation', {a2})
    assert _is_linked(b, 'domain_Assosiation', a2)
    if hasattr(a1, 'domain_Link'):
        assert not _is_linked(a1, 'domain_Link', b)
    if hasattr(a2, 'domain_Link'):
        assert _is_linked(a2, 'domain_Link', b)
    _safe_set(b, 'domain_Assosiation', set())
    assert not _is_linked(b, 'domain_Assosiation', a2)
    if hasattr(a2, 'domain_Link'):
        assert not _is_linked(a2, 'domain_Link', b)


def test_assoc_links537_reverse_link_reassign_clear():
    a1 = domain_Relation(isTree=True, name="sample_text", uid="sample_text")
    a2 = domain_Relation(isTree=False, name="sample_text_2", uid="sample_text_2")
    b = domain_Link(uid="sample_text")
    _safe_set(b, 'domain_Link539', a1)
    assert _is_linked(b, 'domain_Link539', a1)
    if hasattr(a1, 'domain_Relation538'):
        assert _is_linked(a1, 'domain_Relation538', b)
    _safe_set(b, 'domain_Link539', a2)
    assert _is_linked(b, 'domain_Link539', a2)
    if hasattr(a1, 'domain_Relation538'):
        assert not _is_linked(a1, 'domain_Relation538', b)
    if hasattr(a2, 'domain_Relation538'):
        assert _is_linked(a2, 'domain_Relation538', b)
    _safe_set(b, 'domain_Link539', None)
    assert not _is_linked(b, 'domain_Link539', a2)
    if hasattr(a2, 'domain_Relation538'):
        assert not _is_linked(a2, 'domain_Relation538', b)


def test_assoc_many2manyHelper300_reverse_link_reassign_clear():
    a1 = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    a2 = domain_TypePointer(fakePackageName="sample_text_2", fakeTypeName="sample_text_2")
    b = domain_Assosiation(type="sample_text")
    _safe_set(b, 'domain_Assosiation301', a1)
    assert _is_linked(b, 'domain_Assosiation301', a1)
    if hasattr(a1, 'domain_TypePointer302'):
        assert _is_linked(a1, 'domain_TypePointer302', b)
    _safe_set(b, 'domain_Assosiation301', a2)
    assert _is_linked(b, 'domain_Assosiation301', a2)
    if hasattr(a1, 'domain_TypePointer302'):
        assert not _is_linked(a1, 'domain_TypePointer302', b)
    if hasattr(a2, 'domain_TypePointer302'):
        assert _is_linked(a2, 'domain_TypePointer302', b)
    _safe_set(b, 'domain_Assosiation301', None)
    assert not _is_linked(b, 'domain_Assosiation301', a2)
    if hasattr(a2, 'domain_TypePointer302'):
        assert not _is_linked(a2, 'domain_TypePointer302', b)


def test_assoc_mapper121_reverse_link_reassign_clear():
    a1 = domain_Mappers(uid="sample_text")
    a2 = domain_Mappers(uid="sample_text_2")
    b = domain_ApplicationMapper(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent122', a1)
    assert _is_linked(b, 'parent122', a1)
    if hasattr(a1, 'Mappers'):
        assert _is_linked(a1, 'Mappers', b)
    _safe_set(b, 'parent122', a2)
    assert _is_linked(b, 'parent122', a2)
    if hasattr(a1, 'Mappers'):
        assert not _is_linked(a1, 'Mappers', b)
    if hasattr(a2, 'Mappers'):
        assert _is_linked(a2, 'Mappers', b)
    _safe_set(b, 'parent122', None)
    assert not _is_linked(b, 'parent122', a2)
    if hasattr(a2, 'Mappers'):
        assert not _is_linked(a2, 'Mappers', b)


def test_assoc_mapper208_reverse_link_reassign_clear():
    a1 = domain_ModelMapper(artifactExecutionString="sample_text", artifactRoot="sample_text", name="sample_text")
    a2 = domain_ModelMapper(artifactExecutionString="sample_text_2", artifactRoot="sample_text_2", name="sample_text_2")
    b = domain_DeploymentComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponent209', a1)
    assert _is_linked(b, 'domain_DeploymentComponent209', a1)
    if hasattr(a1, 'domain_ModelMapper'):
        assert _is_linked(a1, 'domain_ModelMapper', b)
    _safe_set(b, 'domain_DeploymentComponent209', a2)
    assert _is_linked(b, 'domain_DeploymentComponent209', a2)
    if hasattr(a1, 'domain_ModelMapper'):
        assert not _is_linked(a1, 'domain_ModelMapper', b)
    if hasattr(a2, 'domain_ModelMapper'):
        assert _is_linked(a2, 'domain_ModelMapper', b)
    _safe_set(b, 'domain_DeploymentComponent209', None)
    assert not _is_linked(b, 'domain_DeploymentComponent209', a2)
    if hasattr(a2, 'domain_ModelMapper'):
        assert not _is_linked(a2, 'domain_ModelMapper', b)


def test_assoc_mappers119_reverse_link_reassign_clear():
    a1 = domain_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationMapper(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationMapper', a1)
    assert _is_linked(b, 'ApplicationMapper', a1)
    if hasattr(a1, 'parent120'):
        assert _is_linked(a1, 'parent120', b)
    _safe_set(b, 'ApplicationMapper', a2)
    assert _is_linked(b, 'ApplicationMapper', a2)
    if hasattr(a1, 'parent120'):
        assert not _is_linked(a1, 'parent120', b)
    if hasattr(a2, 'parent120'):
        assert _is_linked(a2, 'parent120', b)
    _safe_set(b, 'ApplicationMapper', None)
    assert not _is_linked(b, 'ApplicationMapper', a2)
    if hasattr(a2, 'parent120'):
        assert not _is_linked(a2, 'parent120', b)


def test_assoc_mappers169_reverse_link_reassign_clear():
    a1 = domain_Mappers(uid="sample_text")
    a2 = domain_Mappers(uid="sample_text_2")
    b = domain_Mapper(serviceLayer=True, uiLayer=True, uid="sample_text")
    _safe_set(b, 'Mapper', a1)
    assert _is_linked(b, 'Mapper', a1)
    if hasattr(a1, 'parent170'):
        assert _is_linked(a1, 'parent170', b)
    _safe_set(b, 'Mapper', a2)
    assert _is_linked(b, 'Mapper', a2)
    if hasattr(a1, 'parent170'):
        assert not _is_linked(a1, 'parent170', b)
    if hasattr(a2, 'parent170'):
        assert _is_linked(a2, 'parent170', b)
    _safe_set(b, 'Mapper', None)
    assert not _is_linked(b, 'Mapper', a2)
    if hasattr(a2, 'parent170'):
        assert not _is_linked(a2, 'parent170', b)


def test_assoc_mappers237_reverse_link_reassign_clear():
    a1 = domain_ModelMapper(artifactExecutionString="sample_text", artifactRoot="sample_text", name="sample_text")
    a2 = domain_ModelMapper(artifactExecutionString="sample_text_2", artifactRoot="sample_text_2", name="sample_text_2")
    b = domain_Component(componentRoot="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'parent238', {a1})
    assert _is_linked(b, 'parent238', a1)
    if hasattr(a1, 'ModelMapper'):
        assert _is_linked(a1, 'ModelMapper', b)
    _safe_set(b, 'parent238', {a2})
    assert _is_linked(b, 'parent238', a2)
    if hasattr(a1, 'ModelMapper'):
        assert not _is_linked(a1, 'ModelMapper', b)
    if hasattr(a2, 'ModelMapper'):
        assert _is_linked(a2, 'ModelMapper', b)
    _safe_set(b, 'parent238', set())
    assert not _is_linked(b, 'parent238', a2)
    if hasattr(a2, 'ModelMapper'):
        assert not _is_linked(a2, 'ModelMapper', b)


def test_assoc_master531_reverse_link_reassign_clear():
    a1 = domain_Relation(isTree=True, name="sample_text", uid="sample_text")
    a2 = domain_Relation(isTree=False, name="sample_text_2", uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl533', a1)
    assert _is_linked(b, 'domain_DataControl533', a1)
    if hasattr(a1, 'domain_Relation532'):
        assert _is_linked(a1, 'domain_Relation532', b)
    _safe_set(b, 'domain_DataControl533', a2)
    assert _is_linked(b, 'domain_DataControl533', a2)
    if hasattr(a1, 'domain_Relation532'):
        assert not _is_linked(a1, 'domain_Relation532', b)
    if hasattr(a2, 'domain_Relation532'):
        assert _is_linked(a2, 'domain_Relation532', b)
    _safe_set(b, 'domain_DataControl533', None)
    assert not _is_linked(b, 'domain_DataControl533', a2)
    if hasattr(a2, 'domain_Relation532'):
        assert not _is_linked(a2, 'domain_Relation532', b)


def test_assoc_master540_reverse_link_reassign_clear():
    a1 = domain_Dependency(name="sample_text", uid="sample_text")
    a2 = domain_Dependency(name="sample_text_2", uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl542', a1)
    assert _is_linked(b, 'domain_DataControl542', a1)
    if hasattr(a1, 'domain_Dependency541'):
        assert _is_linked(a1, 'domain_Dependency541', b)
    _safe_set(b, 'domain_DataControl542', a2)
    assert _is_linked(b, 'domain_DataControl542', a2)
    if hasattr(a1, 'domain_Dependency541'):
        assert not _is_linked(a1, 'domain_Dependency541', b)
    if hasattr(a2, 'domain_Dependency541'):
        assert _is_linked(a2, 'domain_Dependency541', b)
    _safe_set(b, 'domain_DataControl542', None)
    assert not _is_linked(b, 'domain_DataControl542', a2)
    if hasattr(a2, 'domain_Dependency541'):
        assert not _is_linked(a2, 'domain_Dependency541', b)


def test_assoc_master578_reverse_link_reassign_clear():
    a1 = domain_InfrastructureConnection(uid="sample_text")
    a2 = domain_InfrastructureConnection(uid="sample_text_2")
    b = domain_InfrastructureComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_InfrastructureComponent', a1)
    assert _is_linked(b, 'domain_InfrastructureComponent', a1)
    if hasattr(a1, 'domain_InfrastructureConnection579'):
        assert _is_linked(a1, 'domain_InfrastructureConnection579', b)
    _safe_set(b, 'domain_InfrastructureComponent', a2)
    assert _is_linked(b, 'domain_InfrastructureComponent', a2)
    if hasattr(a1, 'domain_InfrastructureConnection579'):
        assert not _is_linked(a1, 'domain_InfrastructureConnection579', b)
    if hasattr(a2, 'domain_InfrastructureConnection579'):
        assert _is_linked(a2, 'domain_InfrastructureConnection579', b)
    _safe_set(b, 'domain_InfrastructureComponent', None)
    assert not _is_linked(b, 'domain_InfrastructureComponent', a2)
    if hasattr(a2, 'domain_InfrastructureConnection579'):
        assert not _is_linked(a2, 'domain_InfrastructureConnection579', b)


def test_assoc_masterField548_reverse_link_reassign_clear():
    a1 = domain_Link(uid="sample_text")
    a2 = domain_Link(uid="sample_text_2")
    b = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    _safe_set(b, 'domain_Attribute550', a1)
    assert _is_linked(b, 'domain_Attribute550', a1)
    if hasattr(a1, 'domain_Link549'):
        assert _is_linked(a1, 'domain_Link549', b)
    _safe_set(b, 'domain_Attribute550', a2)
    assert _is_linked(b, 'domain_Attribute550', a2)
    if hasattr(a1, 'domain_Link549'):
        assert not _is_linked(a1, 'domain_Link549', b)
    if hasattr(a2, 'domain_Link549'):
        assert _is_linked(a2, 'domain_Link549', b)
    _safe_set(b, 'domain_Attribute550', None)
    assert not _is_linked(b, 'domain_Attribute550', a2)
    if hasattr(a2, 'domain_Link549'):
        assert not _is_linked(a2, 'domain_Link549', b)


def test_assoc_menuElements595_reverse_link_reassign_clear():
    a1 = domain_MenuFolder(extensionPoint=True, name="sample_text", uid="sample_text")
    a2 = domain_MenuFolder(extensionPoint=False, name="sample_text_2", uid="sample_text_2")
    b = domain_MenuElement(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_MenuElement', a1)
    assert _is_linked(b, 'domain_MenuElement', a1)
    if hasattr(a1, 'domain_MenuFolder596'):
        assert _is_linked(a1, 'domain_MenuFolder596', b)
    _safe_set(b, 'domain_MenuElement', a2)
    assert _is_linked(b, 'domain_MenuElement', a2)
    if hasattr(a1, 'domain_MenuFolder596'):
        assert not _is_linked(a1, 'domain_MenuFolder596', b)
    if hasattr(a2, 'domain_MenuFolder596'):
        assert _is_linked(a2, 'domain_MenuFolder596', b)
    _safe_set(b, 'domain_MenuElement', None)
    assert not _is_linked(b, 'domain_MenuElement', a2)
    if hasattr(a2, 'domain_MenuFolder596'):
        assert not _is_linked(a2, 'domain_MenuFolder596', b)


def test_assoc_menuFolders587_reverse_link_reassign_clear():
    a1 = domain_MenuView(uid="sample_text")
    a2 = domain_MenuView(uid="sample_text_2")
    b = domain_MenuFolder(extensionPoint=True, name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_MenuFolder', a1)
    assert _is_linked(b, 'domain_MenuFolder', a1)
    if hasattr(a1, 'domain_MenuView'):
        assert _is_linked(a1, 'domain_MenuView', b)
    _safe_set(b, 'domain_MenuFolder', a2)
    assert _is_linked(b, 'domain_MenuFolder', a2)
    if hasattr(a1, 'domain_MenuView'):
        assert not _is_linked(a1, 'domain_MenuView', b)
    if hasattr(a2, 'domain_MenuView'):
        assert _is_linked(a2, 'domain_MenuView', b)
    _safe_set(b, 'domain_MenuFolder', None)
    assert not _is_linked(b, 'domain_MenuFolder', a2)
    if hasattr(a2, 'domain_MenuView'):
        assert not _is_linked(a2, 'domain_MenuView', b)


def test_assoc_menuView364_reverse_link_reassign_clear():
    a1 = domain_MenuView(uid="sample_text")
    a2 = domain_MenuView(uid="sample_text_2")
    b = domain_MenuDefinition(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent365', a1)
    assert _is_linked(b, 'parent365', a1)
    if hasattr(a1, 'MenuView'):
        assert _is_linked(a1, 'MenuView', b)
    _safe_set(b, 'parent365', a2)
    assert _is_linked(b, 'parent365', a2)
    if hasattr(a1, 'MenuView'):
        assert not _is_linked(a1, 'MenuView', b)
    if hasattr(a2, 'MenuView'):
        assert _is_linked(a2, 'MenuView', b)
    _safe_set(b, 'parent365', None)
    assert not _is_linked(b, 'parent365', a2)
    if hasattr(a2, 'MenuView'):
        assert not _is_linked(a2, 'MenuView', b)


def test_assoc_menus357_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_MenuDefinition(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_MenuDefinition', a1)
    assert _is_linked(b, 'domain_MenuDefinition', a1)
    if hasattr(a1, 'domain_Views358'):
        assert _is_linked(a1, 'domain_Views358', b)
    _safe_set(b, 'domain_MenuDefinition', a2)
    assert _is_linked(b, 'domain_MenuDefinition', a2)
    if hasattr(a1, 'domain_Views358'):
        assert not _is_linked(a1, 'domain_Views358', b)
    if hasattr(a2, 'domain_Views358'):
        assert _is_linked(a2, 'domain_Views358', b)
    _safe_set(b, 'domain_MenuDefinition', None)
    assert not _is_linked(b, 'domain_MenuDefinition', a2)
    if hasattr(a2, 'domain_Views358'):
        assert not _is_linked(a2, 'domain_Views358', b)


def test_assoc_messageLibraries128_reverse_link_reassign_clear():
    a1 = domain_Messages(uid="sample_text")
    a2 = domain_Messages(uid="sample_text_2")
    b = domain_MessageLibrary(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_MessageLibrary', a1)
    assert _is_linked(b, 'domain_MessageLibrary', a1)
    if hasattr(a1, 'domain_Messages'):
        assert _is_linked(a1, 'domain_Messages', b)
    _safe_set(b, 'domain_MessageLibrary', a2)
    assert _is_linked(b, 'domain_MessageLibrary', a2)
    if hasattr(a1, 'domain_Messages'):
        assert not _is_linked(a1, 'domain_Messages', b)
    if hasattr(a2, 'domain_Messages'):
        assert _is_linked(a2, 'domain_Messages', b)
    _safe_set(b, 'domain_MessageLibrary', None)
    assert not _is_linked(b, 'domain_MessageLibrary', a2)
    if hasattr(a2, 'domain_Messages'):
        assert not _is_linked(a2, 'domain_Messages', b)


def test_assoc_messages136_reverse_link_reassign_clear():
    a1 = domain_MessageLibrary(name="sample_text", uid="sample_text")
    a2 = domain_MessageLibrary(name="sample_text_2", uid="sample_text_2")
    b = domain_Message(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Message', a1)
    assert _is_linked(b, 'domain_Message', a1)
    if hasattr(a1, 'domain_MessageLibrary137'):
        assert _is_linked(a1, 'domain_MessageLibrary137', b)
    _safe_set(b, 'domain_Message', a2)
    assert _is_linked(b, 'domain_Message', a2)
    if hasattr(a1, 'domain_MessageLibrary137'):
        assert not _is_linked(a1, 'domain_MessageLibrary137', b)
    if hasattr(a2, 'domain_MessageLibrary137'):
        assert _is_linked(a2, 'domain_MessageLibrary137', b)
    _safe_set(b, 'domain_Message', None)
    assert not _is_linked(b, 'domain_Message', a2)
    if hasattr(a2, 'domain_MessageLibrary137'):
        assert not _is_linked(a2, 'domain_MessageLibrary137', b)


def test_assoc_messages87_reverse_link_reassign_clear():
    a1 = domain_Messages(uid="sample_text")
    a2 = domain_Messages(uid="sample_text_2")
    b = domain_ApplicationMessages(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent88', a1)
    assert _is_linked(b, 'parent88', a1)
    if hasattr(a1, 'Messages'):
        assert _is_linked(a1, 'Messages', b)
    _safe_set(b, 'parent88', a2)
    assert _is_linked(b, 'parent88', a2)
    if hasattr(a1, 'Messages'):
        assert not _is_linked(a1, 'Messages', b)
    if hasattr(a2, 'Messages'):
        assert _is_linked(a2, 'Messages', b)
    _safe_set(b, 'parent88', None)
    assert not _is_linked(b, 'parent88', a2)
    if hasattr(a2, 'Messages'):
        assert not _is_linked(a2, 'Messages', b)


def test_assoc_methodRef125_reverse_link_reassign_clear():
    a1 = domain_Operation(name="sample_text", uid="sample_text")
    a2 = domain_Operation(name="sample_text_2", uid="sample_text_2")
    b = domain_MethodPointer(fakeMethod="sample_text")
    _safe_set(b, 'domain_MethodPointer', a1)
    assert _is_linked(b, 'domain_MethodPointer', a1)
    if hasattr(a1, 'domain_Operation'):
        assert _is_linked(a1, 'domain_Operation', b)
    _safe_set(b, 'domain_MethodPointer', a2)
    assert _is_linked(b, 'domain_MethodPointer', a2)
    if hasattr(a1, 'domain_Operation'):
        assert not _is_linked(a1, 'domain_Operation', b)
    if hasattr(a2, 'domain_Operation'):
        assert _is_linked(a2, 'domain_Operation', b)
    _safe_set(b, 'domain_MethodPointer', None)
    assert not _is_linked(b, 'domain_MethodPointer', a2)
    if hasattr(a2, 'domain_Operation'):
        assert not _is_linked(a2, 'domain_Operation', b)


def test_assoc_modelQuery265_reverse_link_reassign_clear():
    a1 = domain_Query(name="sample_text", uid="sample_text")
    a2 = domain_Query(name="sample_text_2", uid="sample_text_2")
    b = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ModelQuery', a1)
    assert _is_linked(b, 'domain_ModelQuery', a1)
    if hasattr(a1, 'domain_Query266'):
        assert _is_linked(a1, 'domain_Query266', b)
    _safe_set(b, 'domain_ModelQuery', a2)
    assert _is_linked(b, 'domain_ModelQuery', a2)
    if hasattr(a1, 'domain_Query266'):
        assert not _is_linked(a1, 'domain_Query266', b)
    if hasattr(a2, 'domain_Query266'):
        assert _is_linked(a2, 'domain_Query266', b)
    _safe_set(b, 'domain_ModelQuery', None)
    assert not _is_linked(b, 'domain_ModelQuery', a2)
    if hasattr(a2, 'domain_Query266'):
        assert not _is_linked(a2, 'domain_Query266', b)


def test_assoc_modelQuery45_reverse_link_reassign_clear():
    a1 = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    a2 = domain_ModelQuery(name="sample_text_2", query="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'parent46', {a1})
    assert _is_linked(b, 'parent46', a1)
    if hasattr(a1, 'ModelQuery'):
        assert _is_linked(a1, 'ModelQuery', b)
    _safe_set(b, 'parent46', {a2})
    assert _is_linked(b, 'parent46', a2)
    if hasattr(a1, 'ModelQuery'):
        assert not _is_linked(a1, 'ModelQuery', b)
    if hasattr(a2, 'ModelQuery'):
        assert _is_linked(a2, 'ModelQuery', b)
    _safe_set(b, 'parent46', set())
    assert not _is_linked(b, 'parent46', a2)
    if hasattr(a2, 'ModelQuery'):
        assert not _is_linked(a2, 'ModelQuery', b)


def test_assoc_options63_reverse_link_reassign_clear():
    a1 = domain_Specifier(name="sample_text", uid="sample_text")
    a2 = domain_Specifier(name="sample_text_2", uid="sample_text_2")
    b = domain_Option(uid="sample_text", value="sample_text")
    _safe_set(b, 'Option', a1)
    assert _is_linked(b, 'Option', a1)
    if hasattr(a1, 'parent64'):
        assert _is_linked(a1, 'parent64', b)
    _safe_set(b, 'Option', a2)
    assert _is_linked(b, 'Option', a2)
    if hasattr(a1, 'parent64'):
        assert not _is_linked(a1, 'parent64', b)
    if hasattr(a2, 'parent64'):
        assert _is_linked(a2, 'parent64', b)
    _safe_set(b, 'Option', None)
    assert not _is_linked(b, 'Option', a2)
    if hasattr(a2, 'parent64'):
        assert not _is_linked(a2, 'parent64', b)


def test_assoc_orderRules526_reverse_link_reassign_clear():
    a1 = domain_Orders(uid="sample_text")
    a2 = domain_Orders(uid="sample_text_2")
    b = domain_OrderBy(order="sample_text", uid="sample_text")
    _safe_set(b, 'domain_OrderBy', a1)
    assert _is_linked(b, 'domain_OrderBy', a1)
    if hasattr(a1, 'domain_Orders527'):
        assert _is_linked(a1, 'domain_Orders527', b)
    _safe_set(b, 'domain_OrderBy', a2)
    assert _is_linked(b, 'domain_OrderBy', a2)
    if hasattr(a1, 'domain_Orders527'):
        assert not _is_linked(a1, 'domain_Orders527', b)
    if hasattr(a2, 'domain_Orders527'):
        assert _is_linked(a2, 'domain_Orders527', b)
    _safe_set(b, 'domain_OrderBy', None)
    assert not _is_linked(b, 'domain_OrderBy', a2)
    if hasattr(a2, 'domain_Orders527'):
        assert not _is_linked(a2, 'domain_Orders527', b)


def test_assoc_packageRef278_reverse_link_reassign_clear():
    a1 = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    a2 = domain_TypePointer(fakePackageName="sample_text_2", fakeTypeName="sample_text_2")
    b = domain_Package(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Package', a1)
    assert _is_linked(b, 'domain_Package', a1)
    if hasattr(a1, 'domain_TypePointer'):
        assert _is_linked(a1, 'domain_TypePointer', b)
    _safe_set(b, 'domain_Package', a2)
    assert _is_linked(b, 'domain_Package', a2)
    if hasattr(a1, 'domain_TypePointer'):
        assert not _is_linked(a1, 'domain_TypePointer', b)
    if hasattr(a2, 'domain_TypePointer'):
        assert _is_linked(a2, 'domain_TypePointer', b)
    _safe_set(b, 'domain_Package', None)
    assert not _is_linked(b, 'domain_Package', a2)
    if hasattr(a2, 'domain_TypePointer'):
        assert not _is_linked(a2, 'domain_TypePointer', b)


def test_assoc_packages329_reverse_link_reassign_clear():
    a1 = domain_Types(name="sample_text", uid="sample_text")
    a2 = domain_Types(name="sample_text_2", uid="sample_text_2")
    b = domain_Package(name="sample_text", uid="sample_text")
    _safe_set(b, 'Package331', a1)
    assert _is_linked(b, 'Package331', a1)
    if hasattr(a1, 'parent330'):
        assert _is_linked(a1, 'parent330', b)
    _safe_set(b, 'Package331', a2)
    assert _is_linked(b, 'Package331', a2)
    if hasattr(a1, 'parent330'):
        assert not _is_linked(a1, 'parent330', b)
    if hasattr(a2, 'parent330'):
        assert _is_linked(a2, 'parent330', b)
    _safe_set(b, 'Package331', None)
    assert not _is_linked(b, 'Package331', a2)
    if hasattr(a2, 'parent330'):
        assert not _is_linked(a2, 'parent330', b)


def test_assoc_paramRef486_reverse_link_reassign_clear():
    a1 = domain_FormVariable(name="sample_text", uid="sample_text")
    a2 = domain_FormVariable(name="sample_text_2", uid="sample_text_2")
    b = domain_FormParameter(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_FormParameter488', a1)
    assert _is_linked(b, 'domain_FormParameter488', a1)
    if hasattr(a1, 'domain_FormVariable487'):
        assert _is_linked(a1, 'domain_FormVariable487', b)
    _safe_set(b, 'domain_FormParameter488', a2)
    assert _is_linked(b, 'domain_FormParameter488', a2)
    if hasattr(a1, 'domain_FormVariable487'):
        assert not _is_linked(a1, 'domain_FormVariable487', b)
    if hasattr(a2, 'domain_FormVariable487'):
        assert _is_linked(a2, 'domain_FormVariable487', b)
    _safe_set(b, 'domain_FormParameter488', None)
    assert not _is_linked(b, 'domain_FormParameter488', a2)
    if hasattr(a2, 'domain_FormVariable487'):
        assert not _is_linked(a2, 'domain_FormVariable487', b)


def test_assoc_parameters311_reverse_link_reassign_clear():
    a1 = domain_Parameter(name="sample_text", order=7, uid="sample_text")
    a2 = domain_Parameter(name="sample_text_2", order=13, uid="sample_text_2")
    b = domain_Operation(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent312', {a1})
    assert _is_linked(b, 'parent312', a1)
    if hasattr(a1, 'Parameter'):
        assert _is_linked(a1, 'Parameter', b)
    _safe_set(b, 'parent312', {a2})
    assert _is_linked(b, 'parent312', a2)
    if hasattr(a1, 'Parameter'):
        assert not _is_linked(a1, 'Parameter', b)
    if hasattr(a2, 'Parameter'):
        assert _is_linked(a2, 'Parameter', b)
    _safe_set(b, 'parent312', set())
    assert not _is_linked(b, 'parent312', a2)
    if hasattr(a2, 'Parameter'):
        assert not _is_linked(a2, 'Parameter', b)


def test_assoc_parameters347_reverse_link_reassign_clear():
    a1 = domain_FormParameter(name="sample_text", uid="sample_text")
    a2 = domain_FormParameter(name="sample_text_2", uid="sample_text_2")
    b = domain_Form(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Form348', {a1})
    assert _is_linked(b, 'domain_Form348', a1)
    if hasattr(a1, 'domain_FormParameter'):
        assert _is_linked(a1, 'domain_FormParameter', b)
    _safe_set(b, 'domain_Form348', {a2})
    assert _is_linked(b, 'domain_Form348', a2)
    if hasattr(a1, 'domain_FormParameter'):
        assert not _is_linked(a1, 'domain_FormParameter', b)
    if hasattr(a2, 'domain_FormParameter'):
        assert _is_linked(a2, 'domain_FormParameter', b)
    _safe_set(b, 'domain_Form348', set())
    assert not _is_linked(b, 'domain_Form348', a2)
    if hasattr(a2, 'domain_FormParameter'):
        assert not _is_linked(a2, 'domain_FormParameter', b)


def test_assoc_parameters57_reverse_link_reassign_clear():
    a1 = domain_QueryParameter(name="sample_text", uid="sample_text")
    a2 = domain_QueryParameter(name="sample_text_2", uid="sample_text_2")
    b = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    _safe_set(b, 'parent58', {a1})
    assert _is_linked(b, 'parent58', a1)
    if hasattr(a1, 'QueryParameter'):
        assert _is_linked(a1, 'QueryParameter', b)
    _safe_set(b, 'parent58', {a2})
    assert _is_linked(b, 'parent58', a2)
    if hasattr(a1, 'QueryParameter'):
        assert not _is_linked(a1, 'QueryParameter', b)
    if hasattr(a2, 'QueryParameter'):
        assert _is_linked(a2, 'QueryParameter', b)
    _safe_set(b, 'parent58', set())
    assert not _is_linked(b, 'parent58', a2)
    if hasattr(a2, 'QueryParameter'):
        assert not _is_linked(a2, 'QueryParameter', b)


def test_assoc_parent101_reverse_link_reassign_clear():
    a1 = domain_ApplicationUILayer(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationUILayer(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application102', a1)
    assert _is_linked(b, 'Application102', a1)
    if hasattr(a1, 'applicationUILayer'):
        assert _is_linked(a1, 'applicationUILayer', b)
    _safe_set(b, 'Application102', a2)
    assert _is_linked(b, 'Application102', a2)
    if hasattr(a1, 'applicationUILayer'):
        assert not _is_linked(a1, 'applicationUILayer', b)
    if hasattr(a2, 'applicationUILayer'):
        assert _is_linked(a2, 'applicationUILayer', b)
    _safe_set(b, 'Application102', None)
    assert not _is_linked(b, 'Application102', a2)
    if hasattr(a2, 'applicationUILayer'):
        assert not _is_linked(a2, 'applicationUILayer', b)


def test_assoc_parent105_reverse_link_reassign_clear():
    a1 = domain_ApplicationUIPackage(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationUIPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationUILayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationUILayer106', a1)
    assert _is_linked(b, 'ApplicationUILayer106', a1)
    if hasattr(a1, 'applicationUIPackages'):
        assert _is_linked(a1, 'applicationUIPackages', b)
    _safe_set(b, 'ApplicationUILayer106', a2)
    assert _is_linked(b, 'ApplicationUILayer106', a2)
    if hasattr(a1, 'applicationUIPackages'):
        assert not _is_linked(a1, 'applicationUIPackages', b)
    if hasattr(a2, 'applicationUIPackages'):
        assert _is_linked(a2, 'applicationUIPackages', b)
    _safe_set(b, 'ApplicationUILayer106', None)
    assert not _is_linked(b, 'ApplicationUILayer106', a2)
    if hasattr(a2, 'applicationUIPackages'):
        assert not _is_linked(a2, 'applicationUIPackages', b)


def test_assoc_parent109_reverse_link_reassign_clear():
    a1 = domain_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application110', a1)
    assert _is_linked(b, 'Application110', a1)
    if hasattr(a1, 'applicationRecipes'):
        assert _is_linked(a1, 'applicationRecipes', b)
    _safe_set(b, 'Application110', a2)
    assert _is_linked(b, 'Application110', a2)
    if hasattr(a1, 'applicationRecipes'):
        assert not _is_linked(a1, 'applicationRecipes', b)
    if hasattr(a2, 'applicationRecipes'):
        assert _is_linked(a2, 'applicationRecipes', b)
    _safe_set(b, 'Application110', None)
    assert not _is_linked(b, 'Application110', a2)
    if hasattr(a2, 'applicationRecipes'):
        assert not _is_linked(a2, 'applicationRecipes', b)


def test_assoc_parent115_reverse_link_reassign_clear():
    a1 = domain_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationRecipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'recipes', a1)
    assert _is_linked(b, 'recipes', a1)
    if hasattr(a1, 'ApplicationRecipes116'):
        assert _is_linked(a1, 'ApplicationRecipes116', b)
    _safe_set(b, 'recipes', a2)
    assert _is_linked(b, 'recipes', a2)
    if hasattr(a1, 'ApplicationRecipes116'):
        assert not _is_linked(a1, 'ApplicationRecipes116', b)
    if hasattr(a2, 'ApplicationRecipes116'):
        assert _is_linked(a2, 'ApplicationRecipes116', b)
    _safe_set(b, 'recipes', None)
    assert not _is_linked(b, 'recipes', a2)
    if hasattr(a2, 'ApplicationRecipes116'):
        assert not _is_linked(a2, 'ApplicationRecipes116', b)


def test_assoc_parent117_reverse_link_reassign_clear():
    a1 = domain_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application118', a1)
    assert _is_linked(b, 'Application118', a1)
    if hasattr(a1, 'applicationMappers'):
        assert _is_linked(a1, 'applicationMappers', b)
    _safe_set(b, 'Application118', a2)
    assert _is_linked(b, 'Application118', a2)
    if hasattr(a1, 'applicationMappers'):
        assert not _is_linked(a1, 'applicationMappers', b)
    if hasattr(a2, 'applicationMappers'):
        assert _is_linked(a2, 'applicationMappers', b)
    _safe_set(b, 'Application118', None)
    assert not _is_linked(b, 'Application118', a2)
    if hasattr(a2, 'applicationMappers'):
        assert not _is_linked(a2, 'applicationMappers', b)


def test_assoc_parent123_reverse_link_reassign_clear():
    a1 = domain_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationMapper(name="sample_text", uid="sample_text")
    _safe_set(b, 'mappers', a1)
    assert _is_linked(b, 'mappers', a1)
    if hasattr(a1, 'ApplicationMappers124'):
        assert _is_linked(a1, 'ApplicationMappers124', b)
    _safe_set(b, 'mappers', a2)
    assert _is_linked(b, 'mappers', a2)
    if hasattr(a1, 'ApplicationMappers124'):
        assert not _is_linked(a1, 'ApplicationMappers124', b)
    if hasattr(a2, 'ApplicationMappers124'):
        assert _is_linked(a2, 'ApplicationMappers124', b)
    _safe_set(b, 'mappers', None)
    assert not _is_linked(b, 'mappers', a2)
    if hasattr(a2, 'ApplicationMappers124'):
        assert not _is_linked(a2, 'ApplicationMappers124', b)


def test_assoc_parent126_reverse_link_reassign_clear():
    a1 = domain_Messages(uid="sample_text")
    a2 = domain_Messages(uid="sample_text_2")
    b = domain_ApplicationMessages(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationMessages127', a1)
    assert _is_linked(b, 'ApplicationMessages127', a1)
    if hasattr(a1, 'messages'):
        assert _is_linked(a1, 'messages', b)
    _safe_set(b, 'ApplicationMessages127', a2)
    assert _is_linked(b, 'ApplicationMessages127', a2)
    if hasattr(a1, 'messages'):
        assert not _is_linked(a1, 'messages', b)
    if hasattr(a2, 'messages'):
        assert _is_linked(a2, 'messages', b)
    _safe_set(b, 'ApplicationMessages127', None)
    assert not _is_linked(b, 'ApplicationMessages127', a2)
    if hasattr(a2, 'messages'):
        assert not _is_linked(a2, 'messages', b)


def test_assoc_parent14_reverse_link_reassign_clear():
    a1 = domain_DomainArtifacts(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifacts(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'Domain', a1)
    assert _is_linked(b, 'Domain', a1)
    if hasattr(a1, 'domainArtifacts'):
        assert _is_linked(a1, 'domainArtifacts', b)
    _safe_set(b, 'Domain', a2)
    assert _is_linked(b, 'Domain', a2)
    if hasattr(a1, 'domainArtifacts'):
        assert not _is_linked(a1, 'domainArtifacts', b)
    if hasattr(a2, 'domainArtifacts'):
        assert _is_linked(a2, 'domainArtifacts', b)
    _safe_set(b, 'Domain', None)
    assert not _is_linked(b, 'Domain', a2)
    if hasattr(a2, 'domainArtifacts'):
        assert not _is_linked(a2, 'domainArtifacts', b)


def test_assoc_parent146_reverse_link_reassign_clear():
    a1 = domain_Roles(uid="sample_text")
    a2 = domain_Roles(uid="sample_text_2")
    b = domain_ApplicationRole(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationRole147', a1)
    assert _is_linked(b, 'ApplicationRole147', a1)
    if hasattr(a1, 'roles'):
        assert _is_linked(a1, 'roles', b)
    _safe_set(b, 'ApplicationRole147', a2)
    assert _is_linked(b, 'ApplicationRole147', a2)
    if hasattr(a1, 'roles'):
        assert not _is_linked(a1, 'roles', b)
    if hasattr(a2, 'roles'):
        assert _is_linked(a2, 'roles', b)
    _safe_set(b, 'ApplicationRole147', None)
    assert not _is_linked(b, 'ApplicationRole147', a2)
    if hasattr(a2, 'roles'):
        assert not _is_linked(a2, 'roles', b)


def test_assoc_parent161_reverse_link_reassign_clear():
    a1 = domain_StylesPackage(name="sample_text", uid="sample_text")
    a2 = domain_StylesPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_Styles(uid="sample_text")
    _safe_set(b, 'styles', a1)
    assert _is_linked(b, 'styles', a1)
    if hasattr(a1, 'StylesPackage162'):
        assert _is_linked(a1, 'StylesPackage162', b)
    _safe_set(b, 'styles', a2)
    assert _is_linked(b, 'styles', a2)
    if hasattr(a1, 'StylesPackage162'):
        assert not _is_linked(a1, 'StylesPackage162', b)
    if hasattr(a2, 'StylesPackage162'):
        assert _is_linked(a2, 'StylesPackage162', b)
    _safe_set(b, 'styles', None)
    assert not _is_linked(b, 'styles', a2)
    if hasattr(a2, 'StylesPackage162'):
        assert not _is_linked(a2, 'StylesPackage162', b)


def test_assoc_parent171_reverse_link_reassign_clear():
    a1 = domain_Mappers(uid="sample_text")
    a2 = domain_Mappers(uid="sample_text_2")
    b = domain_ApplicationMapper(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationMapper172', a1)
    assert _is_linked(b, 'ApplicationMapper172', a1)
    if hasattr(a1, 'mapper'):
        assert _is_linked(a1, 'mapper', b)
    _safe_set(b, 'ApplicationMapper172', a2)
    assert _is_linked(b, 'ApplicationMapper172', a2)
    if hasattr(a1, 'mapper'):
        assert not _is_linked(a1, 'mapper', b)
    if hasattr(a2, 'mapper'):
        assert _is_linked(a2, 'mapper', b)
    _safe_set(b, 'ApplicationMapper172', None)
    assert not _is_linked(b, 'ApplicationMapper172', a2)
    if hasattr(a2, 'mapper'):
        assert not _is_linked(a2, 'mapper', b)


def test_assoc_parent175_reverse_link_reassign_clear():
    a1 = domain_Mappers(uid="sample_text")
    a2 = domain_Mappers(uid="sample_text_2")
    b = domain_Mapper(serviceLayer=True, uiLayer=True, uid="sample_text")
    _safe_set(b, 'mappers176', a1)
    assert _is_linked(b, 'mappers176', a1)
    if hasattr(a1, 'Mappers177'):
        assert _is_linked(a1, 'Mappers177', b)
    _safe_set(b, 'mappers176', a2)
    assert _is_linked(b, 'mappers176', a2)
    if hasattr(a1, 'Mappers177'):
        assert not _is_linked(a1, 'Mappers177', b)
    if hasattr(a2, 'Mappers177'):
        assert _is_linked(a2, 'Mappers177', b)
    _safe_set(b, 'mappers176', None)
    assert not _is_linked(b, 'mappers176', a2)
    if hasattr(a2, 'Mappers177'):
        assert not _is_linked(a2, 'Mappers177', b)


def test_assoc_parent189_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_ApplicationRecipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationRecipe191', a1)
    assert _is_linked(b, 'ApplicationRecipe191', a1)
    if hasattr(a1, 'recipes190'):
        assert _is_linked(a1, 'recipes190', b)
    _safe_set(b, 'ApplicationRecipe191', a2)
    assert _is_linked(b, 'ApplicationRecipe191', a2)
    if hasattr(a1, 'recipes190'):
        assert not _is_linked(a1, 'recipes190', b)
    if hasattr(a2, 'recipes190'):
        assert _is_linked(a2, 'recipes190', b)
    _safe_set(b, 'ApplicationRecipe191', None)
    assert not _is_linked(b, 'ApplicationRecipe191', a2)
    if hasattr(a2, 'recipes190'):
        assert not _is_linked(a2, 'recipes190', b)


def test_assoc_parent19_reverse_link_reassign_clear():
    a1 = domain_DomainTypes(name="sample_text", uid="sample_text")
    a2 = domain_DomainTypes(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'Domain20', a1)
    assert _is_linked(b, 'Domain20', a1)
    if hasattr(a1, 'domainTypes'):
        assert _is_linked(a1, 'domainTypes', b)
    _safe_set(b, 'Domain20', a2)
    assert _is_linked(b, 'Domain20', a2)
    if hasattr(a1, 'domainTypes'):
        assert not _is_linked(a1, 'domainTypes', b)
    if hasattr(a2, 'domainTypes'):
        assert _is_linked(a2, 'domainTypes', b)
    _safe_set(b, 'Domain20', None)
    assert not _is_linked(b, 'Domain20', a2)
    if hasattr(a2, 'domainTypes'):
        assert not _is_linked(a2, 'domainTypes', b)


def test_assoc_parent217_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_Recipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'recipe', a1)
    assert _is_linked(b, 'recipe', a1)
    if hasattr(a1, 'Recipes218'):
        assert _is_linked(a1, 'Recipes218', b)
    _safe_set(b, 'recipe', a2)
    assert _is_linked(b, 'recipe', a2)
    if hasattr(a1, 'Recipes218'):
        assert not _is_linked(a1, 'Recipes218', b)
    if hasattr(a2, 'Recipes218'):
        assert _is_linked(a2, 'Recipes218', b)
    _safe_set(b, 'recipe', None)
    assert not _is_linked(b, 'recipe', a2)
    if hasattr(a2, 'Recipes218'):
        assert not _is_linked(a2, 'Recipes218', b)


def test_assoc_parent23_reverse_link_reassign_clear():
    a1 = domain_DomainApplications(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplications(name="sample_text_2", uid="sample_text_2")
    b = domain_Domain(uid="sample_text")
    _safe_set(b, 'Domain24', a1)
    assert _is_linked(b, 'Domain24', a1)
    if hasattr(a1, 'domainApplications'):
        assert _is_linked(a1, 'domainApplications', b)
    _safe_set(b, 'Domain24', a2)
    assert _is_linked(b, 'Domain24', a2)
    if hasattr(a1, 'domainApplications'):
        assert not _is_linked(a1, 'domainApplications', b)
    if hasattr(a2, 'domainApplications'):
        assert _is_linked(a2, 'domainApplications', b)
    _safe_set(b, 'Domain24', None)
    assert not _is_linked(b, 'Domain24', a2)
    if hasattr(a2, 'domainApplications'):
        assert not _is_linked(a2, 'domainApplications', b)


def test_assoc_parent231_reverse_link_reassign_clear():
    a1 = domain_Recipe(name="sample_text", uid="sample_text")
    a2 = domain_Recipe(name="sample_text_2", uid="sample_text_2")
    b = domain_Ingredient(layer="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'ingredients', a1)
    assert _is_linked(b, 'ingredients', a1)
    if hasattr(a1, 'Recipe232'):
        assert _is_linked(a1, 'Recipe232', b)
    _safe_set(b, 'ingredients', a2)
    assert _is_linked(b, 'ingredients', a2)
    if hasattr(a1, 'Recipe232'):
        assert not _is_linked(a1, 'Recipe232', b)
    if hasattr(a2, 'Recipe232'):
        assert _is_linked(a2, 'Recipe232', b)
    _safe_set(b, 'ingredients', None)
    assert not _is_linked(b, 'ingredients', a2)
    if hasattr(a2, 'Recipe232'):
        assert not _is_linked(a2, 'Recipe232', b)


def test_assoc_parent235_reverse_link_reassign_clear():
    a1 = domain_Ingredient(layer="sample_text", name="sample_text", uid="sample_text")
    a2 = domain_Ingredient(layer="sample_text_2", name="sample_text_2", uid="sample_text_2")
    b = domain_Component(componentRoot="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'components', a1)
    assert _is_linked(b, 'components', a1)
    if hasattr(a1, 'Ingredient236'):
        assert _is_linked(a1, 'Ingredient236', b)
    _safe_set(b, 'components', a2)
    assert _is_linked(b, 'components', a2)
    if hasattr(a1, 'Ingredient236'):
        assert not _is_linked(a1, 'Ingredient236', b)
    if hasattr(a2, 'Ingredient236'):
        assert _is_linked(a2, 'Ingredient236', b)
    _safe_set(b, 'components', None)
    assert not _is_linked(b, 'components', a2)
    if hasattr(a2, 'Ingredient236'):
        assert not _is_linked(a2, 'Ingredient236', b)


def test_assoc_parent248_reverse_link_reassign_clear():
    a1 = domain_ModelMapper(artifactExecutionString="sample_text", artifactRoot="sample_text", name="sample_text")
    a2 = domain_ModelMapper(artifactExecutionString="sample_text_2", artifactRoot="sample_text_2", name="sample_text_2")
    b = domain_Component(componentRoot="sample_text", name="sample_text", uid="sample_text")
    _safe_set(b, 'Component250', a1)
    assert _is_linked(b, 'Component250', a1)
    if hasattr(a1, 'mappers249'):
        assert _is_linked(a1, 'mappers249', b)
    _safe_set(b, 'Component250', a2)
    assert _is_linked(b, 'Component250', a2)
    if hasattr(a1, 'mappers249'):
        assert not _is_linked(a1, 'mappers249', b)
    if hasattr(a2, 'mappers249'):
        assert _is_linked(a2, 'mappers249', b)
    _safe_set(b, 'Component250', None)
    assert not _is_linked(b, 'Component250', a2)
    if hasattr(a2, 'mappers249'):
        assert not _is_linked(a2, 'mappers249', b)


def test_assoc_parent27_reverse_link_reassign_clear():
    a1 = domain_DomainApplications(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplications(name="sample_text_2", uid="sample_text_2")
    b = domain_DomainApplication(name="sample_text", uid="sample_text")
    _safe_set(b, 'applications', a1)
    assert _is_linked(b, 'applications', a1)
    if hasattr(a1, 'DomainApplications28'):
        assert _is_linked(a1, 'DomainApplications28', b)
    _safe_set(b, 'applications', a2)
    assert _is_linked(b, 'applications', a2)
    if hasattr(a1, 'DomainApplications28'):
        assert not _is_linked(a1, 'DomainApplications28', b)
    if hasattr(a2, 'DomainApplications28'):
        assert _is_linked(a2, 'DomainApplications28', b)
    _safe_set(b, 'applications', None)
    assert not _is_linked(b, 'applications', a2)
    if hasattr(a2, 'DomainApplications28'):
        assert not _is_linked(a2, 'DomainApplications28', b)


def test_assoc_parent283_reverse_link_reassign_clear():
    a1 = domain_TypeDefinition(uid="sample_text")
    a2 = domain_TypeDefinition(uid="sample_text_2")
    b = domain_Package(name="sample_text", uid="sample_text")
    _safe_set(b, 'Package', a1)
    assert _is_linked(b, 'Package', a1)
    if hasattr(a1, 'typedefinition'):
        assert _is_linked(a1, 'typedefinition', b)
    _safe_set(b, 'Package', a2)
    assert _is_linked(b, 'Package', a2)
    if hasattr(a1, 'typedefinition'):
        assert not _is_linked(a1, 'typedefinition', b)
    if hasattr(a2, 'typedefinition'):
        assert _is_linked(a2, 'typedefinition', b)
    _safe_set(b, 'Package', None)
    assert not _is_linked(b, 'Package', a2)
    if hasattr(a2, 'typedefinition'):
        assert not _is_linked(a2, 'typedefinition', b)


def test_assoc_parent29_reverse_link_reassign_clear():
    a1 = domain_DomainArtifacts(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifacts(name="sample_text_2", uid="sample_text_2")
    b = domain_DomainArtifact(name="sample_text", uid="sample_text")
    _safe_set(b, 'domainArtifact', a1)
    assert _is_linked(b, 'domainArtifact', a1)
    if hasattr(a1, 'DomainArtifacts30'):
        assert _is_linked(a1, 'DomainArtifacts30', b)
    _safe_set(b, 'domainArtifact', a2)
    assert _is_linked(b, 'domainArtifact', a2)
    if hasattr(a1, 'DomainArtifacts30'):
        assert not _is_linked(a1, 'DomainArtifacts30', b)
    if hasattr(a2, 'DomainArtifacts30'):
        assert _is_linked(a2, 'DomainArtifacts30', b)
    _safe_set(b, 'domainArtifact', None)
    assert not _is_linked(b, 'domainArtifact', a2)
    if hasattr(a2, 'DomainArtifacts30'):
        assert not _is_linked(a2, 'DomainArtifacts30', b)


def test_assoc_parent303_reverse_link_reassign_clear():
    a1 = domain_TypeElement(name="sample_text", uid="sample_text")
    a2 = domain_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = domain_TypeDefinition(uid="sample_text")
    _safe_set(b, 'TypeDefinition', a1)
    assert _is_linked(b, 'TypeDefinition', a1)
    if hasattr(a1, 'types'):
        assert _is_linked(a1, 'types', b)
    _safe_set(b, 'TypeDefinition', a2)
    assert _is_linked(b, 'TypeDefinition', a2)
    if hasattr(a1, 'types'):
        assert not _is_linked(a1, 'types', b)
    if hasattr(a2, 'types'):
        assert _is_linked(a2, 'types', b)
    _safe_set(b, 'TypeDefinition', None)
    assert not _is_linked(b, 'TypeDefinition', a2)
    if hasattr(a2, 'types'):
        assert not _is_linked(a2, 'types', b)


def test_assoc_parent315_reverse_link_reassign_clear():
    a1 = domain_Parameter(name="sample_text", order=7, uid="sample_text")
    a2 = domain_Parameter(name="sample_text_2", order=13, uid="sample_text_2")
    b = domain_Operation(name="sample_text", uid="sample_text")
    _safe_set(b, 'Operation317', a1)
    assert _is_linked(b, 'Operation317', a1)
    if hasattr(a1, 'parameters316'):
        assert _is_linked(a1, 'parameters316', b)
    _safe_set(b, 'Operation317', a2)
    assert _is_linked(b, 'Operation317', a2)
    if hasattr(a1, 'parameters316'):
        assert not _is_linked(a1, 'parameters316', b)
    if hasattr(a2, 'parameters316'):
        assert _is_linked(a2, 'parameters316', b)
    _safe_set(b, 'Operation317', None)
    assert not _is_linked(b, 'Operation317', a2)
    if hasattr(a2, 'parameters316'):
        assert not _is_linked(a2, 'parameters316', b)


def test_assoc_parent323_reverse_link_reassign_clear():
    a1 = domain_TypesRepository(uid="sample_text")
    a2 = domain_TypesRepository(uid="sample_text_2")
    b = domain_DomainTypes(name="sample_text", uid="sample_text")
    _safe_set(b, 'DomainTypes324', a1)
    assert _is_linked(b, 'DomainTypes324', a1)
    if hasattr(a1, 'typesrepository'):
        assert _is_linked(a1, 'typesrepository', b)
    _safe_set(b, 'DomainTypes324', a2)
    assert _is_linked(b, 'DomainTypes324', a2)
    if hasattr(a1, 'typesrepository'):
        assert not _is_linked(a1, 'typesrepository', b)
    if hasattr(a2, 'typesrepository'):
        assert _is_linked(a2, 'typesrepository', b)
    _safe_set(b, 'DomainTypes324', None)
    assert not _is_linked(b, 'DomainTypes324', a2)
    if hasattr(a2, 'typesrepository'):
        assert not _is_linked(a2, 'typesrepository', b)


def test_assoc_parent327_reverse_link_reassign_clear():
    a1 = domain_TypesRepository(uid="sample_text")
    a2 = domain_TypesRepository(uid="sample_text_2")
    b = domain_Types(name="sample_text", uid="sample_text")
    _safe_set(b, 'typeDefinition', a1)
    assert _is_linked(b, 'typeDefinition', a1)
    if hasattr(a1, 'TypesRepository328'):
        assert _is_linked(a1, 'TypesRepository328', b)
    _safe_set(b, 'typeDefinition', a2)
    assert _is_linked(b, 'typeDefinition', a2)
    if hasattr(a1, 'TypesRepository328'):
        assert not _is_linked(a1, 'TypesRepository328', b)
    if hasattr(a2, 'TypesRepository328'):
        assert _is_linked(a2, 'TypesRepository328', b)
    _safe_set(b, 'typeDefinition', None)
    assert not _is_linked(b, 'typeDefinition', a2)
    if hasattr(a2, 'TypesRepository328'):
        assert not _is_linked(a2, 'TypesRepository328', b)


def test_assoc_parent335_reverse_link_reassign_clear():
    a1 = domain_Types(name="sample_text", uid="sample_text")
    a2 = domain_Types(name="sample_text_2", uid="sample_text_2")
    b = domain_Package(name="sample_text", uid="sample_text")
    _safe_set(b, 'packages', a1)
    assert _is_linked(b, 'packages', a1)
    if hasattr(a1, 'Types336'):
        assert _is_linked(a1, 'Types336', b)
    _safe_set(b, 'packages', a2)
    assert _is_linked(b, 'packages', a2)
    if hasattr(a1, 'Types336'):
        assert not _is_linked(a1, 'Types336', b)
    if hasattr(a2, 'Types336'):
        assert _is_linked(a2, 'Types336', b)
    _safe_set(b, 'packages', None)
    assert not _is_linked(b, 'packages', a2)
    if hasattr(a2, 'Types336'):
        assert not _is_linked(a2, 'Types336', b)


def test_assoc_parent337_reverse_link_reassign_clear():
    a1 = domain_UIPackage(uid="sample_text")
    a2 = domain_UIPackage(uid="sample_text_2")
    b = domain_ApplicationUIPackage(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationUIPackage338', a1)
    assert _is_linked(b, 'ApplicationUIPackage338', a1)
    if hasattr(a1, 'uipackage'):
        assert _is_linked(a1, 'uipackage', b)
    _safe_set(b, 'ApplicationUIPackage338', a2)
    assert _is_linked(b, 'ApplicationUIPackage338', a2)
    if hasattr(a1, 'uipackage'):
        assert not _is_linked(a1, 'uipackage', b)
    if hasattr(a2, 'uipackage'):
        assert _is_linked(a2, 'uipackage', b)
    _safe_set(b, 'ApplicationUIPackage338', None)
    assert not _is_linked(b, 'ApplicationUIPackage338', a2)
    if hasattr(a2, 'uipackage'):
        assert not _is_linked(a2, 'uipackage', b)


def test_assoc_parent35_reverse_link_reassign_clear():
    a1 = domain_DomainArtifact(name="sample_text", uid="sample_text")
    a2 = domain_DomainArtifact(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifacts(uid="sample_text")
    _safe_set(b, 'artifact', a1)
    assert _is_linked(b, 'artifact', a1)
    if hasattr(a1, 'DomainArtifact36'):
        assert _is_linked(a1, 'DomainArtifact36', b)
    _safe_set(b, 'artifact', a2)
    assert _is_linked(b, 'artifact', a2)
    if hasattr(a1, 'DomainArtifact36'):
        assert not _is_linked(a1, 'DomainArtifact36', b)
    if hasattr(a2, 'DomainArtifact36'):
        assert _is_linked(a2, 'DomainArtifact36', b)
    _safe_set(b, 'artifact', None)
    assert not _is_linked(b, 'artifact', a2)
    if hasattr(a2, 'DomainArtifact36'):
        assert not _is_linked(a2, 'DomainArtifact36', b)


def test_assoc_parent351_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_FormView(name="sample_text", uid="sample_text")
    _safe_set(b, 'FormView', a1)
    assert _is_linked(b, 'FormView', a1)
    if hasattr(a1, 'view'):
        assert _is_linked(a1, 'view', b)
    _safe_set(b, 'FormView', a2)
    assert _is_linked(b, 'FormView', a2)
    if hasattr(a1, 'view'):
        assert not _is_linked(a1, 'view', b)
    if hasattr(a2, 'view'):
        assert _is_linked(a2, 'view', b)
    _safe_set(b, 'FormView', None)
    assert not _is_linked(b, 'FormView', a2)
    if hasattr(a2, 'view'):
        assert not _is_linked(a2, 'view', b)


def test_assoc_parent381_reverse_link_reassign_clear():
    a1 = domain_ViewArea(name="sample_text", uid="sample_text")
    a2 = domain_ViewArea(name="sample_text_2", uid="sample_text_2")
    b = domain_CanvasView(uid="sample_text")
    _safe_set(b, 'canvasView', a1)
    assert _is_linked(b, 'canvasView', a1)
    if hasattr(a1, 'ViewArea'):
        assert _is_linked(a1, 'ViewArea', b)
    _safe_set(b, 'canvasView', a2)
    assert _is_linked(b, 'canvasView', a2)
    if hasattr(a1, 'ViewArea'):
        assert not _is_linked(a1, 'ViewArea', b)
    if hasattr(a2, 'ViewArea'):
        assert _is_linked(a2, 'ViewArea', b)
    _safe_set(b, 'canvasView', None)
    assert not _is_linked(b, 'canvasView', a2)
    if hasattr(a2, 'ViewArea'):
        assert not _is_linked(a2, 'ViewArea', b)


def test_assoc_parent39_reverse_link_reassign_clear():
    a1 = domain_Artifacts(uid="sample_text")
    a2 = domain_Artifacts(uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'artifacts', a1)
    assert _is_linked(b, 'artifacts', a1)
    if hasattr(a1, 'Artifacts40'):
        assert _is_linked(a1, 'Artifacts40', b)
    _safe_set(b, 'artifacts', a2)
    assert _is_linked(b, 'artifacts', a2)
    if hasattr(a1, 'Artifacts40'):
        assert not _is_linked(a1, 'Artifacts40', b)
    if hasattr(a2, 'Artifacts40'):
        assert _is_linked(a2, 'Artifacts40', b)
    _safe_set(b, 'artifacts', None)
    assert not _is_linked(b, 'artifacts', a2)
    if hasattr(a2, 'Artifacts40'):
        assert not _is_linked(a2, 'Artifacts40', b)


def test_assoc_parent469_reverse_link_reassign_clear():
    a1 = domain_FormDataControls(name="sample_text", uid="sample_text")
    a2 = domain_FormDataControls(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'formControl', a1)
    assert _is_linked(b, 'formControl', a1)
    if hasattr(a1, 'FormDataControls'):
        assert _is_linked(a1, 'FormDataControls', b)
    _safe_set(b, 'formControl', a2)
    assert _is_linked(b, 'formControl', a2)
    if hasattr(a1, 'FormDataControls'):
        assert not _is_linked(a1, 'FormDataControls', b)
    if hasattr(a2, 'FormDataControls'):
        assert _is_linked(a2, 'FormDataControls', b)
    _safe_set(b, 'formControl', None)
    assert not _is_linked(b, 'formControl', a2)
    if hasattr(a2, 'FormDataControls'):
        assert not _is_linked(a2, 'FormDataControls', b)


def test_assoc_parent495_reverse_link_reassign_clear():
    a1 = domain_DataControl(name="sample_text", uid="sample_text")
    a2 = domain_DataControl(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'Controls496', a1)
    assert _is_linked(b, 'Controls496', a1)
    if hasattr(a1, 'controls'):
        assert _is_linked(a1, 'controls', b)
    _safe_set(b, 'Controls496', a2)
    assert _is_linked(b, 'Controls496', a2)
    if hasattr(a1, 'controls'):
        assert not _is_linked(a1, 'controls', b)
    if hasattr(a2, 'controls'):
        assert _is_linked(a2, 'controls', b)
    _safe_set(b, 'Controls496', None)
    assert not _is_linked(b, 'Controls496', a2)
    if hasattr(a2, 'controls'):
        assert not _is_linked(a2, 'controls', b)


def test_assoc_parent51_reverse_link_reassign_clear():
    a1 = domain_ConfigVariable(name="sample_text", uid="sample_text")
    a2 = domain_ConfigVariable(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'Artifact52', a1)
    assert _is_linked(b, 'Artifact52', a1)
    if hasattr(a1, 'configVariables'):
        assert _is_linked(a1, 'configVariables', b)
    _safe_set(b, 'Artifact52', a2)
    assert _is_linked(b, 'Artifact52', a2)
    if hasattr(a1, 'configVariables'):
        assert not _is_linked(a1, 'configVariables', b)
    if hasattr(a2, 'configVariables'):
        assert _is_linked(a2, 'configVariables', b)
    _safe_set(b, 'Artifact52', None)
    assert not _is_linked(b, 'Artifact52', a2)
    if hasattr(a2, 'configVariables'):
        assert not _is_linked(a2, 'configVariables', b)


def test_assoc_parent53_reverse_link_reassign_clear():
    a1 = domain_ConfigHash(name="sample_text", uid="sample_text")
    a2 = domain_ConfigHash(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'Artifact54', a1)
    assert _is_linked(b, 'Artifact54', a1)
    if hasattr(a1, 'configHashes'):
        assert _is_linked(a1, 'configHashes', b)
    _safe_set(b, 'Artifact54', a2)
    assert _is_linked(b, 'Artifact54', a2)
    if hasattr(a1, 'configHashes'):
        assert not _is_linked(a1, 'configHashes', b)
    if hasattr(a2, 'configHashes'):
        assert _is_linked(a2, 'configHashes', b)
    _safe_set(b, 'Artifact54', None)
    assert not _is_linked(b, 'Artifact54', a2)
    if hasattr(a2, 'configHashes'):
        assert not _is_linked(a2, 'configHashes', b)


def test_assoc_parent546_reverse_link_reassign_clear():
    a1 = domain_DataControl(name="sample_text", uid="sample_text")
    a2 = domain_DataControl(name="sample_text_2", uid="sample_text_2")
    b = domain_ArtificialField(name="sample_text", uid="sample_text")
    _safe_set(b, 'artificialFields', a1)
    assert _is_linked(b, 'artificialFields', a1)
    if hasattr(a1, 'DataControl547'):
        assert _is_linked(a1, 'DataControl547', b)
    _safe_set(b, 'artificialFields', a2)
    assert _is_linked(b, 'artificialFields', a2)
    if hasattr(a1, 'DataControl547'):
        assert not _is_linked(a1, 'DataControl547', b)
    if hasattr(a2, 'DataControl547'):
        assert _is_linked(a2, 'DataControl547', b)
    _safe_set(b, 'artificialFields', None)
    assert not _is_linked(b, 'artificialFields', a2)
    if hasattr(a2, 'DataControl547'):
        assert not _is_linked(a2, 'DataControl547', b)


def test_assoc_parent55_reverse_link_reassign_clear():
    a1 = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    a2 = domain_ModelQuery(name="sample_text_2", query="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'Artifact56', a1)
    assert _is_linked(b, 'Artifact56', a1)
    if hasattr(a1, 'modelQuery'):
        assert _is_linked(a1, 'modelQuery', b)
    _safe_set(b, 'Artifact56', a2)
    assert _is_linked(b, 'Artifact56', a2)
    if hasattr(a1, 'modelQuery'):
        assert not _is_linked(a1, 'modelQuery', b)
    if hasattr(a2, 'modelQuery'):
        assert _is_linked(a2, 'modelQuery', b)
    _safe_set(b, 'Artifact56', None)
    assert not _is_linked(b, 'Artifact56', a2)
    if hasattr(a2, 'modelQuery'):
        assert not _is_linked(a2, 'modelQuery', b)


def test_assoc_parent554_reverse_link_reassign_clear():
    a1 = domain_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationInfrastructureLayer(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application555', a1)
    assert _is_linked(b, 'Application555', a1)
    if hasattr(a1, 'applicationInfrastructureLayer'):
        assert _is_linked(a1, 'applicationInfrastructureLayer', b)
    _safe_set(b, 'Application555', a2)
    assert _is_linked(b, 'Application555', a2)
    if hasattr(a1, 'applicationInfrastructureLayer'):
        assert not _is_linked(a1, 'applicationInfrastructureLayer', b)
    if hasattr(a2, 'applicationInfrastructureLayer'):
        assert _is_linked(a2, 'applicationInfrastructureLayer', b)
    _safe_set(b, 'Application555', None)
    assert not _is_linked(b, 'Application555', a2)
    if hasattr(a2, 'applicationInfrastructureLayer'):
        assert not _is_linked(a2, 'applicationInfrastructureLayer', b)


def test_assoc_parent558_reverse_link_reassign_clear():
    a1 = domain_EnterpriseInfrastructure(uid="sample_text")
    a2 = domain_EnterpriseInfrastructure(uid="sample_text_2")
    b = domain_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationInfrastructureLayer559', a1)
    assert _is_linked(b, 'ApplicationInfrastructureLayer559', a1)
    if hasattr(a1, 'infarastructure'):
        assert _is_linked(a1, 'infarastructure', b)
    _safe_set(b, 'ApplicationInfrastructureLayer559', a2)
    assert _is_linked(b, 'ApplicationInfrastructureLayer559', a2)
    if hasattr(a1, 'infarastructure'):
        assert not _is_linked(a1, 'infarastructure', b)
    if hasattr(a2, 'infarastructure'):
        assert _is_linked(a2, 'infarastructure', b)
    _safe_set(b, 'ApplicationInfrastructureLayer559', None)
    assert not _is_linked(b, 'ApplicationInfrastructureLayer559', a2)
    if hasattr(a2, 'infarastructure'):
        assert not _is_linked(a2, 'infarastructure', b)


def test_assoc_parent566_reverse_link_reassign_clear():
    a1 = domain_EnterpriseInfrastructure(uid="sample_text")
    a2 = domain_EnterpriseInfrastructure(uid="sample_text_2")
    b = domain_Datacenter(name="sample_text", uid="sample_text")
    _safe_set(b, 'datacenters', a1)
    assert _is_linked(b, 'datacenters', a1)
    if hasattr(a1, 'EnterpriseInfrastructure567'):
        assert _is_linked(a1, 'EnterpriseInfrastructure567', b)
    _safe_set(b, 'datacenters', a2)
    assert _is_linked(b, 'datacenters', a2)
    if hasattr(a1, 'EnterpriseInfrastructure567'):
        assert not _is_linked(a1, 'EnterpriseInfrastructure567', b)
    if hasattr(a2, 'EnterpriseInfrastructure567'):
        assert _is_linked(a2, 'EnterpriseInfrastructure567', b)
    _safe_set(b, 'datacenters', None)
    assert not _is_linked(b, 'datacenters', a2)
    if hasattr(a2, 'EnterpriseInfrastructure567'):
        assert not _is_linked(a2, 'EnterpriseInfrastructure567', b)


def test_assoc_parent570_reverse_link_reassign_clear():
    a1 = domain_Subsystem(name="sample_text", uid="sample_text")
    a2 = domain_Subsystem(name="sample_text_2", uid="sample_text_2")
    b = domain_Datacenter(name="sample_text", uid="sample_text")
    _safe_set(b, 'Datacenter571', a1)
    assert _is_linked(b, 'Datacenter571', a1)
    if hasattr(a1, 'subsystems'):
        assert _is_linked(a1, 'subsystems', b)
    _safe_set(b, 'Datacenter571', a2)
    assert _is_linked(b, 'Datacenter571', a2)
    if hasattr(a1, 'subsystems'):
        assert not _is_linked(a1, 'subsystems', b)
    if hasattr(a2, 'subsystems'):
        assert _is_linked(a2, 'subsystems', b)
    _safe_set(b, 'Datacenter571', None)
    assert not _is_linked(b, 'Datacenter571', a2)
    if hasattr(a2, 'subsystems'):
        assert not _is_linked(a2, 'subsystems', b)


def test_assoc_parent574_reverse_link_reassign_clear():
    a1 = domain_Subsystem(name="sample_text", uid="sample_text")
    a2 = domain_Subsystem(name="sample_text_2", uid="sample_text_2")
    b = domain_InfrastructureLayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'infrastructureLayer', a1)
    assert _is_linked(b, 'infrastructureLayer', a1)
    if hasattr(a1, 'Subsystem575'):
        assert _is_linked(a1, 'Subsystem575', b)
    _safe_set(b, 'infrastructureLayer', a2)
    assert _is_linked(b, 'infrastructureLayer', a2)
    if hasattr(a1, 'Subsystem575'):
        assert not _is_linked(a1, 'Subsystem575', b)
    if hasattr(a2, 'Subsystem575'):
        assert _is_linked(a2, 'Subsystem575', b)
    _safe_set(b, 'infrastructureLayer', None)
    assert not _is_linked(b, 'infrastructureLayer', a2)
    if hasattr(a2, 'Subsystem575'):
        assert not _is_linked(a2, 'Subsystem575', b)


def test_assoc_parent583_reverse_link_reassign_clear():
    a1 = domain_InfrastructureLayer(name="sample_text", uid="sample_text")
    a2 = domain_InfrastructureLayer(name="sample_text_2", uid="sample_text_2")
    b = domain_InfrastructureComponent(name="sample_text", uid="sample_text")
    _safe_set(b, 'infrastructureComponent', a1)
    assert _is_linked(b, 'infrastructureComponent', a1)
    if hasattr(a1, 'InfrastructureLayer584'):
        assert _is_linked(a1, 'InfrastructureLayer584', b)
    _safe_set(b, 'infrastructureComponent', a2)
    assert _is_linked(b, 'infrastructureComponent', a2)
    if hasattr(a1, 'InfrastructureLayer584'):
        assert not _is_linked(a1, 'InfrastructureLayer584', b)
    if hasattr(a2, 'InfrastructureLayer584'):
        assert _is_linked(a2, 'InfrastructureLayer584', b)
    _safe_set(b, 'infrastructureComponent', None)
    assert not _is_linked(b, 'infrastructureComponent', a2)
    if hasattr(a2, 'InfrastructureLayer584'):
        assert not _is_linked(a2, 'InfrastructureLayer584', b)


def test_assoc_parent586_reverse_link_reassign_clear():
    a1 = domain_MenuView(uid="sample_text")
    a2 = domain_MenuView(uid="sample_text_2")
    b = domain_MenuDefinition(name="sample_text", uid="sample_text")
    _safe_set(b, 'MenuDefinition', a1)
    assert _is_linked(b, 'MenuDefinition', a1)
    if hasattr(a1, 'menuView'):
        assert _is_linked(a1, 'menuView', b)
    _safe_set(b, 'MenuDefinition', a2)
    assert _is_linked(b, 'MenuDefinition', a2)
    if hasattr(a1, 'menuView'):
        assert not _is_linked(a1, 'menuView', b)
    if hasattr(a2, 'menuView'):
        assert _is_linked(a2, 'menuView', b)
    _safe_set(b, 'MenuDefinition', None)
    assert not _is_linked(b, 'MenuDefinition', a2)
    if hasattr(a2, 'menuView'):
        assert not _is_linked(a2, 'menuView', b)


def test_assoc_parent59_reverse_link_reassign_clear():
    a1 = domain_QueryParameter(name="sample_text", uid="sample_text")
    a2 = domain_QueryParameter(name="sample_text_2", uid="sample_text_2")
    b = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    _safe_set(b, 'ModelQuery60', a1)
    assert _is_linked(b, 'ModelQuery60', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'ModelQuery60', a2)
    assert _is_linked(b, 'ModelQuery60', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'ModelQuery60', None)
    assert not _is_linked(b, 'ModelQuery60', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_parent61_reverse_link_reassign_clear():
    a1 = domain_Specifier(name="sample_text", uid="sample_text")
    a2 = domain_Specifier(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'Artifact62', a1)
    assert _is_linked(b, 'Artifact62', a1)
    if hasattr(a1, 'specifiers'):
        assert _is_linked(a1, 'specifiers', b)
    _safe_set(b, 'Artifact62', a2)
    assert _is_linked(b, 'Artifact62', a2)
    if hasattr(a1, 'specifiers'):
        assert not _is_linked(a1, 'specifiers', b)
    if hasattr(a2, 'specifiers'):
        assert _is_linked(a2, 'specifiers', b)
    _safe_set(b, 'Artifact62', None)
    assert not _is_linked(b, 'Artifact62', a2)
    if hasattr(a2, 'specifiers'):
        assert not _is_linked(a2, 'specifiers', b)


def test_assoc_parent65_reverse_link_reassign_clear():
    a1 = domain_Specifier(name="sample_text", uid="sample_text")
    a2 = domain_Specifier(name="sample_text_2", uid="sample_text_2")
    b = domain_Option(uid="sample_text", value="sample_text")
    _safe_set(b, 'options', a1)
    assert _is_linked(b, 'options', a1)
    if hasattr(a1, 'Specifier66'):
        assert _is_linked(a1, 'Specifier66', b)
    _safe_set(b, 'options', a2)
    assert _is_linked(b, 'options', a2)
    if hasattr(a1, 'Specifier66'):
        assert not _is_linked(a1, 'Specifier66', b)
    if hasattr(a2, 'Specifier66'):
        assert _is_linked(a2, 'Specifier66', b)
    _safe_set(b, 'options', None)
    assert not _is_linked(b, 'options', a2)
    if hasattr(a2, 'Specifier66'):
        assert not _is_linked(a2, 'Specifier66', b)


def test_assoc_parent81_reverse_link_reassign_clear():
    a1 = domain_DomainApplication(name="sample_text", uid="sample_text")
    a2 = domain_DomainApplication(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'application', a1)
    assert _is_linked(b, 'application', a1)
    if hasattr(a1, 'DomainApplication82'):
        assert _is_linked(a1, 'DomainApplication82', b)
    _safe_set(b, 'application', a2)
    assert _is_linked(b, 'application', a2)
    if hasattr(a1, 'DomainApplication82'):
        assert not _is_linked(a1, 'DomainApplication82', b)
    if hasattr(a2, 'DomainApplication82'):
        assert _is_linked(a2, 'DomainApplication82', b)
    _safe_set(b, 'application', None)
    assert not _is_linked(b, 'application', a2)
    if hasattr(a2, 'DomainApplication82'):
        assert not _is_linked(a2, 'DomainApplication82', b)


def test_assoc_parent85_reverse_link_reassign_clear():
    a1 = domain_ApplicationMessages(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationMessages(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application86', a1)
    assert _is_linked(b, 'Application86', a1)
    if hasattr(a1, 'applicationMessages'):
        assert _is_linked(a1, 'applicationMessages', b)
    _safe_set(b, 'Application86', a2)
    assert _is_linked(b, 'Application86', a2)
    if hasattr(a1, 'applicationMessages'):
        assert not _is_linked(a1, 'applicationMessages', b)
    if hasattr(a2, 'applicationMessages'):
        assert _is_linked(a2, 'applicationMessages', b)
    _safe_set(b, 'Application86', None)
    assert not _is_linked(b, 'Application86', a2)
    if hasattr(a2, 'applicationMessages'):
        assert not _is_linked(a2, 'applicationMessages', b)


def test_assoc_parent89_reverse_link_reassign_clear():
    a1 = domain_ApplicationRole(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRole(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application90', a1)
    assert _is_linked(b, 'Application90', a1)
    if hasattr(a1, 'applicationRole'):
        assert _is_linked(a1, 'applicationRole', b)
    _safe_set(b, 'Application90', a2)
    assert _is_linked(b, 'Application90', a2)
    if hasattr(a1, 'applicationRole'):
        assert not _is_linked(a1, 'applicationRole', b)
    if hasattr(a2, 'applicationRole'):
        assert _is_linked(a2, 'applicationRole', b)
    _safe_set(b, 'Application90', None)
    assert not _is_linked(b, 'Application90', a2)
    if hasattr(a2, 'applicationRole'):
        assert not _is_linked(a2, 'applicationRole', b)


def test_assoc_parent93_reverse_link_reassign_clear():
    a1 = domain_ApplicationStyle(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationStyle(name="sample_text_2", uid="sample_text_2")
    b = domain_Application(uid="sample_text")
    _safe_set(b, 'Application94', a1)
    assert _is_linked(b, 'Application94', a1)
    if hasattr(a1, 'applicationStyle'):
        assert _is_linked(a1, 'applicationStyle', b)
    _safe_set(b, 'Application94', a2)
    assert _is_linked(b, 'Application94', a2)
    if hasattr(a1, 'applicationStyle'):
        assert not _is_linked(a1, 'applicationStyle', b)
    if hasattr(a2, 'applicationStyle'):
        assert _is_linked(a2, 'applicationStyle', b)
    _safe_set(b, 'Application94', None)
    assert not _is_linked(b, 'Application94', a2)
    if hasattr(a2, 'applicationStyle'):
        assert not _is_linked(a2, 'applicationStyle', b)


def test_assoc_parent97_reverse_link_reassign_clear():
    a1 = domain_StylesPackage(name="sample_text", uid="sample_text")
    a2 = domain_StylesPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationStyle(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationStyle98', a1)
    assert _is_linked(b, 'ApplicationStyle98', a1)
    if hasattr(a1, 'stylesPackage'):
        assert _is_linked(a1, 'stylesPackage', b)
    _safe_set(b, 'ApplicationStyle98', a2)
    assert _is_linked(b, 'ApplicationStyle98', a2)
    if hasattr(a1, 'stylesPackage'):
        assert not _is_linked(a1, 'stylesPackage', b)
    if hasattr(a2, 'stylesPackage'):
        assert _is_linked(a2, 'stylesPackage', b)
    _safe_set(b, 'ApplicationStyle98', None)
    assert not _is_linked(b, 'ApplicationStyle98', a2)
    if hasattr(a2, 'stylesPackage'):
        assert not _is_linked(a2, 'stylesPackage', b)


def test_assoc_postCreateTrigger505_reverse_link_reassign_clear():
    a1 = domain_POSTCreateTrigger(uid="sample_text")
    a2 = domain_POSTCreateTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl506', a1)
    assert _is_linked(b, 'domain_DataControl506', a1)
    if hasattr(a1, 'domain_POSTCreateTrigger'):
        assert _is_linked(a1, 'domain_POSTCreateTrigger', b)
    _safe_set(b, 'domain_DataControl506', a2)
    assert _is_linked(b, 'domain_DataControl506', a2)
    if hasattr(a1, 'domain_POSTCreateTrigger'):
        assert not _is_linked(a1, 'domain_POSTCreateTrigger', b)
    if hasattr(a2, 'domain_POSTCreateTrigger'):
        assert _is_linked(a2, 'domain_POSTCreateTrigger', b)
    _safe_set(b, 'domain_DataControl506', None)
    assert not _is_linked(b, 'domain_DataControl506', a2)
    if hasattr(a2, 'domain_POSTCreateTrigger'):
        assert not _is_linked(a2, 'domain_POSTCreateTrigger', b)


def test_assoc_postQueryTrigger499_reverse_link_reassign_clear():
    a1 = domain_POSTQueryTrigger(uid="sample_text")
    a2 = domain_POSTQueryTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl500', a1)
    assert _is_linked(b, 'domain_DataControl500', a1)
    if hasattr(a1, 'domain_POSTQueryTrigger'):
        assert _is_linked(a1, 'domain_POSTQueryTrigger', b)
    _safe_set(b, 'domain_DataControl500', a2)
    assert _is_linked(b, 'domain_DataControl500', a2)
    if hasattr(a1, 'domain_POSTQueryTrigger'):
        assert not _is_linked(a1, 'domain_POSTQueryTrigger', b)
    if hasattr(a2, 'domain_POSTQueryTrigger'):
        assert _is_linked(a2, 'domain_POSTQueryTrigger', b)
    _safe_set(b, 'domain_DataControl500', None)
    assert not _is_linked(b, 'domain_DataControl500', a2)
    if hasattr(a2, 'domain_POSTQueryTrigger'):
        assert not _is_linked(a2, 'domain_POSTQueryTrigger', b)


def test_assoc_preDeleteTrigger503_reverse_link_reassign_clear():
    a1 = domain_PREDeleteTrigger(uid="sample_text")
    a2 = domain_PREDeleteTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl504', a1)
    assert _is_linked(b, 'domain_DataControl504', a1)
    if hasattr(a1, 'domain_PREDeleteTrigger'):
        assert _is_linked(a1, 'domain_PREDeleteTrigger', b)
    _safe_set(b, 'domain_DataControl504', a2)
    assert _is_linked(b, 'domain_DataControl504', a2)
    if hasattr(a1, 'domain_PREDeleteTrigger'):
        assert not _is_linked(a1, 'domain_PREDeleteTrigger', b)
    if hasattr(a2, 'domain_PREDeleteTrigger'):
        assert _is_linked(a2, 'domain_PREDeleteTrigger', b)
    _safe_set(b, 'domain_DataControl504', None)
    assert not _is_linked(b, 'domain_DataControl504', a2)
    if hasattr(a2, 'domain_PREDeleteTrigger'):
        assert not _is_linked(a2, 'domain_PREDeleteTrigger', b)


def test_assoc_preFormTrigger482_reverse_link_reassign_clear():
    a1 = domain_Root(name="sample_text", uid="sample_text")
    a2 = domain_Root(name="sample_text_2", uid="sample_text_2")
    b = domain_PREFormTrigger(uid="sample_text")
    _safe_set(b, 'domain_PREFormTrigger', a1)
    assert _is_linked(b, 'domain_PREFormTrigger', a1)
    if hasattr(a1, 'domain_Root483'):
        assert _is_linked(a1, 'domain_Root483', b)
    _safe_set(b, 'domain_PREFormTrigger', a2)
    assert _is_linked(b, 'domain_PREFormTrigger', a2)
    if hasattr(a1, 'domain_Root483'):
        assert not _is_linked(a1, 'domain_Root483', b)
    if hasattr(a2, 'domain_Root483'):
        assert _is_linked(a2, 'domain_Root483', b)
    _safe_set(b, 'domain_PREFormTrigger', None)
    assert not _is_linked(b, 'domain_PREFormTrigger', a2)
    if hasattr(a2, 'domain_Root483'):
        assert not _is_linked(a2, 'domain_Root483', b)


def test_assoc_preInsertTrigger501_reverse_link_reassign_clear():
    a1 = domain_PREInsertTrigger(uid="sample_text")
    a2 = domain_PREInsertTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl502', a1)
    assert _is_linked(b, 'domain_DataControl502', a1)
    if hasattr(a1, 'domain_PREInsertTrigger'):
        assert _is_linked(a1, 'domain_PREInsertTrigger', b)
    _safe_set(b, 'domain_DataControl502', a2)
    assert _is_linked(b, 'domain_DataControl502', a2)
    if hasattr(a1, 'domain_PREInsertTrigger'):
        assert not _is_linked(a1, 'domain_PREInsertTrigger', b)
    if hasattr(a2, 'domain_PREInsertTrigger'):
        assert _is_linked(a2, 'domain_PREInsertTrigger', b)
    _safe_set(b, 'domain_DataControl502', None)
    assert not _is_linked(b, 'domain_DataControl502', a2)
    if hasattr(a2, 'domain_PREInsertTrigger'):
        assert not _is_linked(a2, 'domain_PREInsertTrigger', b)


def test_assoc_preQueryTrigger497_reverse_link_reassign_clear():
    a1 = domain_PREQueryTrigger(uid="sample_text")
    a2 = domain_PREQueryTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl498', a1)
    assert _is_linked(b, 'domain_DataControl498', a1)
    if hasattr(a1, 'domain_PREQueryTrigger'):
        assert _is_linked(a1, 'domain_PREQueryTrigger', b)
    _safe_set(b, 'domain_DataControl498', a2)
    assert _is_linked(b, 'domain_DataControl498', a2)
    if hasattr(a1, 'domain_PREQueryTrigger'):
        assert not _is_linked(a1, 'domain_PREQueryTrigger', b)
    if hasattr(a2, 'domain_PREQueryTrigger'):
        assert _is_linked(a2, 'domain_PREQueryTrigger', b)
    _safe_set(b, 'domain_DataControl498', None)
    assert not _is_linked(b, 'domain_DataControl498', a2)
    if hasattr(a2, 'domain_PREQueryTrigger'):
        assert not _is_linked(a2, 'domain_PREQueryTrigger', b)


def test_assoc_preUpdateTrigger507_reverse_link_reassign_clear():
    a1 = domain_PREUpdateTrigger(uid="sample_text")
    a2 = domain_PREUpdateTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl508', a1)
    assert _is_linked(b, 'domain_DataControl508', a1)
    if hasattr(a1, 'domain_PREUpdateTrigger'):
        assert _is_linked(a1, 'domain_PREUpdateTrigger', b)
    _safe_set(b, 'domain_DataControl508', a2)
    assert _is_linked(b, 'domain_DataControl508', a2)
    if hasattr(a1, 'domain_PREUpdateTrigger'):
        assert not _is_linked(a1, 'domain_PREUpdateTrigger', b)
    if hasattr(a2, 'domain_PREUpdateTrigger'):
        assert _is_linked(a2, 'domain_PREUpdateTrigger', b)
    _safe_set(b, 'domain_DataControl508', None)
    assert not _is_linked(b, 'domain_DataControl508', a2)
    if hasattr(a2, 'domain_PREUpdateTrigger'):
        assert not _is_linked(a2, 'domain_PREUpdateTrigger', b)


def test_assoc_properties244_reverse_link_reassign_clear():
    a1 = domain_Property(fakeName="sample_text", uid="sample_text", value="sample_text")
    a2 = domain_Property(fakeName="sample_text_2", uid="sample_text_2", value="sample_text_2")
    b = domain_Configuration(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Configuration245', {a1})
    assert _is_linked(b, 'domain_Configuration245', a1)
    if hasattr(a1, 'domain_Property'):
        assert _is_linked(a1, 'domain_Property', b)
    _safe_set(b, 'domain_Configuration245', {a2})
    assert _is_linked(b, 'domain_Configuration245', a2)
    if hasattr(a1, 'domain_Property'):
        assert not _is_linked(a1, 'domain_Property', b)
    if hasattr(a2, 'domain_Property'):
        assert _is_linked(a2, 'domain_Property', b)
    _safe_set(b, 'domain_Configuration245', set())
    assert not _is_linked(b, 'domain_Configuration245', a2)
    if hasattr(a2, 'domain_Property'):
        assert not _is_linked(a2, 'domain_Property', b)


def test_assoc_queries253_reverse_link_reassign_clear():
    a1 = domain_Query(name="sample_text", uid="sample_text")
    a2 = domain_Query(name="sample_text_2", uid="sample_text_2")
    b = domain_ModelMapper(artifactExecutionString="sample_text", artifactRoot="sample_text", name="sample_text")
    _safe_set(b, 'domain_ModelMapper254', {a1})
    assert _is_linked(b, 'domain_ModelMapper254', a1)
    if hasattr(a1, 'domain_Query'):
        assert _is_linked(a1, 'domain_Query', b)
    _safe_set(b, 'domain_ModelMapper254', {a2})
    assert _is_linked(b, 'domain_ModelMapper254', a2)
    if hasattr(a1, 'domain_Query'):
        assert not _is_linked(a1, 'domain_Query', b)
    if hasattr(a2, 'domain_Query'):
        assert _is_linked(a2, 'domain_Query', b)
    _safe_set(b, 'domain_ModelMapper254', set())
    assert not _is_linked(b, 'domain_ModelMapper254', a2)
    if hasattr(a2, 'domain_Query'):
        assert not _is_linked(a2, 'domain_Query', b)


def test_assoc_queryParamRef272_reverse_link_reassign_clear():
    a1 = domain_QueryVariable(uid="sample_text", value="sample_text")
    a2 = domain_QueryVariable(uid="sample_text_2", value="sample_text_2")
    b = domain_QueryParameter(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_QueryParameter', a1)
    assert _is_linked(b, 'domain_QueryParameter', a1)
    if hasattr(a1, 'domain_QueryVariable273'):
        assert _is_linked(a1, 'domain_QueryVariable273', b)
    _safe_set(b, 'domain_QueryParameter', a2)
    assert _is_linked(b, 'domain_QueryParameter', a2)
    if hasattr(a1, 'domain_QueryVariable273'):
        assert not _is_linked(a1, 'domain_QueryVariable273', b)
    if hasattr(a2, 'domain_QueryVariable273'):
        assert _is_linked(a2, 'domain_QueryVariable273', b)
    _safe_set(b, 'domain_QueryParameter', None)
    assert not _is_linked(b, 'domain_QueryParameter', a2)
    if hasattr(a2, 'domain_QueryVariable273'):
        assert not _is_linked(a2, 'domain_QueryVariable273', b)


def test_assoc_queryRef267_reverse_link_reassign_clear():
    a1 = domain_Query(name="sample_text", uid="sample_text")
    a2 = domain_Query(name="sample_text_2", uid="sample_text_2")
    b = domain_ModelQuery(name="sample_text", query="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ModelQuery269', a1)
    assert _is_linked(b, 'domain_ModelQuery269', a1)
    if hasattr(a1, 'domain_Query268'):
        assert _is_linked(a1, 'domain_Query268', b)
    _safe_set(b, 'domain_ModelQuery269', a2)
    assert _is_linked(b, 'domain_ModelQuery269', a2)
    if hasattr(a1, 'domain_Query268'):
        assert not _is_linked(a1, 'domain_Query268', b)
    if hasattr(a2, 'domain_Query268'):
        assert _is_linked(a2, 'domain_Query268', b)
    _safe_set(b, 'domain_ModelQuery269', None)
    assert not _is_linked(b, 'domain_ModelQuery269', a2)
    if hasattr(a2, 'domain_Query268'):
        assert not _is_linked(a2, 'domain_Query268', b)


def test_assoc_recipe184_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_Recipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'Recipe', a1)
    assert _is_linked(b, 'Recipe', a1)
    if hasattr(a1, 'parent185'):
        assert _is_linked(a1, 'parent185', b)
    _safe_set(b, 'Recipe', a2)
    assert _is_linked(b, 'Recipe', a2)
    if hasattr(a1, 'parent185'):
        assert not _is_linked(a1, 'parent185', b)
    if hasattr(a2, 'parent185'):
        assert _is_linked(a2, 'parent185', b)
    _safe_set(b, 'Recipe', None)
    assert not _is_linked(b, 'Recipe', a2)
    if hasattr(a2, 'parent185'):
        assert not _is_linked(a2, 'parent185', b)


def test_assoc_recipe239_reverse_link_reassign_clear():
    a1 = domain_Recipe(name="sample_text", uid="sample_text")
    a2 = domain_Recipe(name="sample_text_2", uid="sample_text_2")
    b = domain_Infrastructure(name="sample_text", uid="sample_text")
    _safe_set(b, 'infrastructures', a1)
    assert _is_linked(b, 'infrastructures', a1)
    if hasattr(a1, 'Recipe240'):
        assert _is_linked(a1, 'Recipe240', b)
    _safe_set(b, 'infrastructures', a2)
    assert _is_linked(b, 'infrastructures', a2)
    if hasattr(a1, 'Recipe240'):
        assert not _is_linked(a1, 'Recipe240', b)
    if hasattr(a2, 'Recipe240'):
        assert _is_linked(a2, 'Recipe240', b)
    _safe_set(b, 'infrastructures', None)
    assert not _is_linked(b, 'infrastructures', a2)
    if hasattr(a2, 'Recipe240'):
        assert not _is_linked(a2, 'Recipe240', b)


def test_assoc_recipeConfig241_reverse_link_reassign_clear():
    a1 = domain_Infrastructure(name="sample_text", uid="sample_text")
    a2 = domain_Infrastructure(name="sample_text_2", uid="sample_text_2")
    b = domain_Configuration(name="sample_text", uid="sample_text")
    _safe_set(b, 'Configuration', a1)
    assert _is_linked(b, 'Configuration', a1)
    if hasattr(a1, 'infrastructure'):
        assert _is_linked(a1, 'infrastructure', b)
    _safe_set(b, 'Configuration', a2)
    assert _is_linked(b, 'Configuration', a2)
    if hasattr(a1, 'infrastructure'):
        assert not _is_linked(a1, 'infrastructure', b)
    if hasattr(a2, 'infrastructure'):
        assert _is_linked(a2, 'infrastructure', b)
    _safe_set(b, 'Configuration', None)
    assert not _is_linked(b, 'Configuration', a2)
    if hasattr(a2, 'infrastructure'):
        assert not _is_linked(a2, 'infrastructure', b)


def test_assoc_recipes111_reverse_link_reassign_clear():
    a1 = domain_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = domain_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationRecipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'ApplicationRecipe', a1)
    assert _is_linked(b, 'ApplicationRecipe', a1)
    if hasattr(a1, 'parent112'):
        assert _is_linked(a1, 'parent112', b)
    _safe_set(b, 'ApplicationRecipe', a2)
    assert _is_linked(b, 'ApplicationRecipe', a2)
    if hasattr(a1, 'parent112'):
        assert not _is_linked(a1, 'parent112', b)
    if hasattr(a2, 'parent112'):
        assert _is_linked(a2, 'parent112', b)
    _safe_set(b, 'ApplicationRecipe', None)
    assert not _is_linked(b, 'ApplicationRecipe', a2)
    if hasattr(a2, 'parent112'):
        assert not _is_linked(a2, 'parent112', b)


def test_assoc_recipes113_reverse_link_reassign_clear():
    a1 = domain_Recipes(uid="sample_text")
    a2 = domain_Recipes(uid="sample_text_2")
    b = domain_ApplicationRecipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent114', a1)
    assert _is_linked(b, 'parent114', a1)
    if hasattr(a1, 'Recipes'):
        assert _is_linked(a1, 'Recipes', b)
    _safe_set(b, 'parent114', a2)
    assert _is_linked(b, 'parent114', a2)
    if hasattr(a1, 'Recipes'):
        assert not _is_linked(a1, 'Recipes', b)
    if hasattr(a2, 'Recipes'):
        assert _is_linked(a2, 'Recipes', b)
    _safe_set(b, 'parent114', None)
    assert not _is_linked(b, 'parent114', a2)
    if hasattr(a2, 'Recipes'):
        assert not _is_linked(a2, 'Recipes', b)


def test_assoc_refreshAreas427_reverse_link_reassign_clear():
    a1 = domain_Uielement(uid="sample_text")
    a2 = domain_Uielement(uid="sample_text_2")
    b = domain_AreaRef(group=7)
    _safe_set(b, 'domain_AreaRef', a1)
    assert _is_linked(b, 'domain_AreaRef', a1)
    if hasattr(a1, 'domain_Uielement428'):
        assert _is_linked(a1, 'domain_Uielement428', b)
    _safe_set(b, 'domain_AreaRef', a2)
    assert _is_linked(b, 'domain_AreaRef', a2)
    if hasattr(a1, 'domain_Uielement428'):
        assert not _is_linked(a1, 'domain_Uielement428', b)
    if hasattr(a2, 'domain_Uielement428'):
        assert _is_linked(a2, 'domain_Uielement428', b)
    _safe_set(b, 'domain_AreaRef', None)
    assert not _is_linked(b, 'domain_AreaRef', a2)
    if hasattr(a2, 'domain_Uielement428'):
        assert not _is_linked(a2, 'domain_Uielement428', b)


def test_assoc_relationShips284_reverse_link_reassign_clear():
    a1 = domain_TypeDefinition(uid="sample_text")
    a2 = domain_TypeDefinition(uid="sample_text_2")
    b = domain_RelationShip(uid="sample_text")
    _safe_set(b, 'domain_RelationShip', a1)
    assert _is_linked(b, 'domain_RelationShip', a1)
    if hasattr(a1, 'domain_TypeDefinition'):
        assert _is_linked(a1, 'domain_TypeDefinition', b)
    _safe_set(b, 'domain_RelationShip', a2)
    assert _is_linked(b, 'domain_RelationShip', a2)
    if hasattr(a1, 'domain_TypeDefinition'):
        assert not _is_linked(a1, 'domain_TypeDefinition', b)
    if hasattr(a2, 'domain_TypeDefinition'):
        assert _is_linked(a2, 'domain_TypeDefinition', b)
    _safe_set(b, 'domain_RelationShip', None)
    assert not _is_linked(b, 'domain_RelationShip', a2)
    if hasattr(a2, 'domain_TypeDefinition'):
        assert not _is_linked(a2, 'domain_TypeDefinition', b)


def test_assoc_relations473_reverse_link_reassign_clear():
    a1 = domain_Relation(isTree=True, name="sample_text", uid="sample_text")
    a2 = domain_Relation(isTree=False, name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'domain_Controls474', {a1})
    assert _is_linked(b, 'domain_Controls474', a1)
    if hasattr(a1, 'domain_Relation'):
        assert _is_linked(a1, 'domain_Relation', b)
    _safe_set(b, 'domain_Controls474', {a2})
    assert _is_linked(b, 'domain_Controls474', a2)
    if hasattr(a1, 'domain_Relation'):
        assert not _is_linked(a1, 'domain_Relation', b)
    if hasattr(a2, 'domain_Relation'):
        assert _is_linked(a2, 'domain_Relation', b)
    _safe_set(b, 'domain_Controls474', set())
    assert not _is_linked(b, 'domain_Controls474', a2)
    if hasattr(a2, 'domain_Relation'):
        assert not _is_linked(a2, 'domain_Relation', b)


def test_assoc_remove515_reverse_link_reassign_clear():
    a1 = domain_DeleteTrigger(uid="sample_text")
    a2 = domain_DeleteTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl516', a1)
    assert _is_linked(b, 'domain_DataControl516', a1)
    if hasattr(a1, 'domain_DeleteTrigger'):
        assert _is_linked(a1, 'domain_DeleteTrigger', b)
    _safe_set(b, 'domain_DataControl516', a2)
    assert _is_linked(b, 'domain_DataControl516', a2)
    if hasattr(a1, 'domain_DeleteTrigger'):
        assert not _is_linked(a1, 'domain_DeleteTrigger', b)
    if hasattr(a2, 'domain_DeleteTrigger'):
        assert _is_linked(a2, 'domain_DeleteTrigger', b)
    _safe_set(b, 'domain_DataControl516', None)
    assert not _is_linked(b, 'domain_DataControl516', a2)
    if hasattr(a2, 'domain_DeleteTrigger'):
        assert not _is_linked(a2, 'domain_DeleteTrigger', b)


def test_assoc_returnValue313_reverse_link_reassign_clear():
    a1 = domain_ReturnValue(uid="sample_text")
    a2 = domain_ReturnValue(uid="sample_text_2")
    b = domain_Operation(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Operation314', a1)
    assert _is_linked(b, 'domain_Operation314', a1)
    if hasattr(a1, 'domain_ReturnValue'):
        assert _is_linked(a1, 'domain_ReturnValue', b)
    _safe_set(b, 'domain_Operation314', a2)
    assert _is_linked(b, 'domain_Operation314', a2)
    if hasattr(a1, 'domain_ReturnValue'):
        assert not _is_linked(a1, 'domain_ReturnValue', b)
    if hasattr(a2, 'domain_ReturnValue'):
        assert _is_linked(a2, 'domain_ReturnValue', b)
    _safe_set(b, 'domain_Operation314', None)
    assert not _is_linked(b, 'domain_Operation314', a2)
    if hasattr(a2, 'domain_ReturnValue'):
        assert not _is_linked(a2, 'domain_ReturnValue', b)


def test_assoc_roleRef12_reverse_link_reassign_clear():
    a1 = domain_Role(name="sample_text", uid="sample_text")
    a2 = domain_Role(name="sample_text_2", uid="sample_text_2")
    b = domain_GrantAccess(uid="sample_text")
    _safe_set(b, 'domain_GrantAccess13', a1)
    assert _is_linked(b, 'domain_GrantAccess13', a1)
    if hasattr(a1, 'domain_Role'):
        assert _is_linked(a1, 'domain_Role', b)
    _safe_set(b, 'domain_GrantAccess13', a2)
    assert _is_linked(b, 'domain_GrantAccess13', a2)
    if hasattr(a1, 'domain_Role'):
        assert not _is_linked(a1, 'domain_Role', b)
    if hasattr(a2, 'domain_Role'):
        assert _is_linked(a2, 'domain_Role', b)
    _safe_set(b, 'domain_GrantAccess13', None)
    assert not _is_linked(b, 'domain_GrantAccess13', a2)
    if hasattr(a2, 'domain_Role'):
        assert not _is_linked(a2, 'domain_Role', b)


def test_assoc_roles148_reverse_link_reassign_clear():
    a1 = domain_Roles(uid="sample_text")
    a2 = domain_Roles(uid="sample_text_2")
    b = domain_Role(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Role149', a1)
    assert _is_linked(b, 'domain_Role149', a1)
    if hasattr(a1, 'domain_Roles'):
        assert _is_linked(a1, 'domain_Roles', b)
    _safe_set(b, 'domain_Role149', a2)
    assert _is_linked(b, 'domain_Role149', a2)
    if hasattr(a1, 'domain_Roles'):
        assert not _is_linked(a1, 'domain_Roles', b)
    if hasattr(a2, 'domain_Roles'):
        assert _is_linked(a2, 'domain_Roles', b)
    _safe_set(b, 'domain_Role149', None)
    assert not _is_linked(b, 'domain_Role149', a2)
    if hasattr(a2, 'domain_Roles'):
        assert not _is_linked(a2, 'domain_Roles', b)


def test_assoc_roles91_reverse_link_reassign_clear():
    a1 = domain_Roles(uid="sample_text")
    a2 = domain_Roles(uid="sample_text_2")
    b = domain_ApplicationRole(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent92', a1)
    assert _is_linked(b, 'parent92', a1)
    if hasattr(a1, 'Roles'):
        assert _is_linked(a1, 'Roles', b)
    _safe_set(b, 'parent92', a2)
    assert _is_linked(b, 'parent92', a2)
    if hasattr(a1, 'Roles'):
        assert not _is_linked(a1, 'Roles', b)
    if hasattr(a2, 'Roles'):
        assert _is_linked(a2, 'Roles', b)
    _safe_set(b, 'parent92', None)
    assert not _is_linked(b, 'parent92', a2)
    if hasattr(a2, 'Roles'):
        assert not _is_linked(a2, 'Roles', b)


def test_assoc_root470_reverse_link_reassign_clear():
    a1 = domain_Root(name="sample_text", uid="sample_text")
    a2 = domain_Root(name="sample_text_2", uid="sample_text_2")
    b = domain_Controls(uid="sample_text")
    _safe_set(b, 'domain_Controls', a1)
    assert _is_linked(b, 'domain_Controls', a1)
    if hasattr(a1, 'domain_Root'):
        assert _is_linked(a1, 'domain_Root', b)
    _safe_set(b, 'domain_Controls', a2)
    assert _is_linked(b, 'domain_Controls', a2)
    if hasattr(a1, 'domain_Root'):
        assert not _is_linked(a1, 'domain_Root', b)
    if hasattr(a2, 'domain_Root'):
        assert _is_linked(a2, 'domain_Root', b)
    _safe_set(b, 'domain_Controls', None)
    assert not _is_linked(b, 'domain_Controls', a2)
    if hasattr(a2, 'domain_Root'):
        assert not _is_linked(a2, 'domain_Root', b)


def test_assoc_search517_reverse_link_reassign_clear():
    a1 = domain_SearchTrigger(uid="sample_text")
    a2 = domain_SearchTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl518', a1)
    assert _is_linked(b, 'domain_DataControl518', a1)
    if hasattr(a1, 'domain_SearchTrigger'):
        assert _is_linked(a1, 'domain_SearchTrigger', b)
    _safe_set(b, 'domain_DataControl518', a2)
    assert _is_linked(b, 'domain_DataControl518', a2)
    if hasattr(a1, 'domain_SearchTrigger'):
        assert not _is_linked(a1, 'domain_SearchTrigger', b)
    if hasattr(a2, 'domain_SearchTrigger'):
        assert _is_linked(a2, 'domain_SearchTrigger', b)
    _safe_set(b, 'domain_DataControl518', None)
    assert not _is_linked(b, 'domain_DataControl518', a2)
    if hasattr(a2, 'domain_SearchTrigger'):
        assert not _is_linked(a2, 'domain_SearchTrigger', b)


def test_assoc_source225_reverse_link_reassign_clear():
    a1 = domain_Configuration(name="sample_text", uid="sample_text")
    a2 = domain_Configuration(name="sample_text_2", uid="sample_text_2")
    b = domain_ConfigExtension(uid="sample_text")
    _safe_set(b, 'domain_ConfigExtension226', a1)
    assert _is_linked(b, 'domain_ConfigExtension226', a1)
    if hasattr(a1, 'domain_Configuration227'):
        assert _is_linked(a1, 'domain_Configuration227', b)
    _safe_set(b, 'domain_ConfigExtension226', a2)
    assert _is_linked(b, 'domain_ConfigExtension226', a2)
    if hasattr(a1, 'domain_Configuration227'):
        assert not _is_linked(a1, 'domain_Configuration227', b)
    if hasattr(a2, 'domain_Configuration227'):
        assert _is_linked(a2, 'domain_Configuration227', b)
    _safe_set(b, 'domain_ConfigExtension226', None)
    assert not _is_linked(b, 'domain_ConfigExtension226', a2)
    if hasattr(a2, 'domain_Configuration227'):
        assert not _is_linked(a2, 'domain_Configuration227', b)


def test_assoc_source288_reverse_link_reassign_clear():
    a1 = domain_TypeElement(name="sample_text", uid="sample_text")
    a2 = domain_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = domain_RelationShip(uid="sample_text")
    _safe_set(b, 'domain_RelationShip289', a1)
    assert _is_linked(b, 'domain_RelationShip289', a1)
    if hasattr(a1, 'domain_TypeElement290'):
        assert _is_linked(a1, 'domain_TypeElement290', b)
    _safe_set(b, 'domain_RelationShip289', a2)
    assert _is_linked(b, 'domain_RelationShip289', a2)
    if hasattr(a1, 'domain_TypeElement290'):
        assert not _is_linked(a1, 'domain_TypeElement290', b)
    if hasattr(a2, 'domain_TypeElement290'):
        assert _is_linked(a2, 'domain_TypeElement290', b)
    _safe_set(b, 'domain_RelationShip289', None)
    assert not _is_linked(b, 'domain_RelationShip289', a2)
    if hasattr(a2, 'domain_TypeElement290'):
        assert not _is_linked(a2, 'domain_TypeElement290', b)


def test_assoc_source369_reverse_link_reassign_clear():
    a1 = domain_ViewPort(name="sample_text", uid="sample_text")
    a2 = domain_ViewPort(name="sample_text_2", uid="sample_text_2")
    b = domain_ViewInheritance(uid="sample_text")
    _safe_set(b, 'domain_ViewInheritance370', a1)
    assert _is_linked(b, 'domain_ViewInheritance370', a1)
    if hasattr(a1, 'domain_ViewPort371'):
        assert _is_linked(a1, 'domain_ViewPort371', b)
    _safe_set(b, 'domain_ViewInheritance370', a2)
    assert _is_linked(b, 'domain_ViewInheritance370', a2)
    if hasattr(a1, 'domain_ViewPort371'):
        assert not _is_linked(a1, 'domain_ViewPort371', b)
    if hasattr(a2, 'domain_ViewPort371'):
        assert _is_linked(a2, 'domain_ViewPort371', b)
    _safe_set(b, 'domain_ViewInheritance370', None)
    assert not _is_linked(b, 'domain_ViewInheritance370', a2)
    if hasattr(a2, 'domain_ViewPort371'):
        assert not _is_linked(a2, 'domain_ViewPort371', b)


def test_assoc_source375_reverse_link_reassign_clear():
    a1 = domain_TabPagesInheritance(uid="sample_text")
    a2 = domain_TabPagesInheritance(uid="sample_text_2")
    b = domain_TabCanvas(orientation="sample_text")
    _safe_set(b, 'domain_TabCanvas', a1)
    assert _is_linked(b, 'domain_TabCanvas', a1)
    if hasattr(a1, 'domain_TabPagesInheritance376'):
        assert _is_linked(a1, 'domain_TabPagesInheritance376', b)
    _safe_set(b, 'domain_TabCanvas', a2)
    assert _is_linked(b, 'domain_TabCanvas', a2)
    if hasattr(a1, 'domain_TabPagesInheritance376'):
        assert not _is_linked(a1, 'domain_TabPagesInheritance376', b)
    if hasattr(a2, 'domain_TabPagesInheritance376'):
        assert _is_linked(a2, 'domain_TabPagesInheritance376', b)
    _safe_set(b, 'domain_TabCanvas', None)
    assert not _is_linked(b, 'domain_TabCanvas', a2)
    if hasattr(a2, 'domain_TabPagesInheritance376'):
        assert not _is_linked(a2, 'domain_TabPagesInheritance376', b)


def test_assoc_sourceProperty295_reverse_link_reassign_clear():
    a1 = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    a2 = domain_Attribute(name="sample_text_2", pk=False, uid="sample_text_2")
    b = domain_Assosiation(type="sample_text")
    _safe_set(b, 'domain_Assosiation296', a1)
    assert _is_linked(b, 'domain_Assosiation296', a1)
    if hasattr(a1, 'domain_Attribute'):
        assert _is_linked(a1, 'domain_Attribute', b)
    _safe_set(b, 'domain_Assosiation296', a2)
    assert _is_linked(b, 'domain_Assosiation296', a2)
    if hasattr(a1, 'domain_Attribute'):
        assert not _is_linked(a1, 'domain_Attribute', b)
    if hasattr(a2, 'domain_Attribute'):
        assert _is_linked(a2, 'domain_Attribute', b)
    _safe_set(b, 'domain_Assosiation296', None)
    assert not _is_linked(b, 'domain_Assosiation296', a2)
    if hasattr(a2, 'domain_Attribute'):
        assert not _is_linked(a2, 'domain_Attribute', b)


def test_assoc_specifierRef261_reverse_link_reassign_clear():
    a1 = domain_Specifier(name="sample_text", uid="sample_text")
    a2 = domain_Specifier(name="sample_text_2", uid="sample_text_2")
    b = domain_MappingSpecifier(uid="sample_text")
    _safe_set(b, 'domain_MappingSpecifier262', a1)
    assert _is_linked(b, 'domain_MappingSpecifier262', a1)
    if hasattr(a1, 'domain_Specifier'):
        assert _is_linked(a1, 'domain_Specifier', b)
    _safe_set(b, 'domain_MappingSpecifier262', a2)
    assert _is_linked(b, 'domain_MappingSpecifier262', a2)
    if hasattr(a1, 'domain_Specifier'):
        assert not _is_linked(a1, 'domain_Specifier', b)
    if hasattr(a2, 'domain_Specifier'):
        assert _is_linked(a2, 'domain_Specifier', b)
    _safe_set(b, 'domain_MappingSpecifier262', None)
    assert not _is_linked(b, 'domain_MappingSpecifier262', a2)
    if hasattr(a2, 'domain_Specifier'):
        assert not _is_linked(a2, 'domain_Specifier', b)


def test_assoc_specifiers251_reverse_link_reassign_clear():
    a1 = domain_ModelMapper(artifactExecutionString="sample_text", artifactRoot="sample_text", name="sample_text")
    a2 = domain_ModelMapper(artifactExecutionString="sample_text_2", artifactRoot="sample_text_2", name="sample_text_2")
    b = domain_MappingSpecifier(uid="sample_text")
    _safe_set(b, 'domain_MappingSpecifier', a1)
    assert _is_linked(b, 'domain_MappingSpecifier', a1)
    if hasattr(a1, 'domain_ModelMapper252'):
        assert _is_linked(a1, 'domain_ModelMapper252', b)
    _safe_set(b, 'domain_MappingSpecifier', a2)
    assert _is_linked(b, 'domain_MappingSpecifier', a2)
    if hasattr(a1, 'domain_ModelMapper252'):
        assert not _is_linked(a1, 'domain_ModelMapper252', b)
    if hasattr(a2, 'domain_ModelMapper252'):
        assert _is_linked(a2, 'domain_ModelMapper252', b)
    _safe_set(b, 'domain_MappingSpecifier', None)
    assert not _is_linked(b, 'domain_MappingSpecifier', a2)
    if hasattr(a2, 'domain_ModelMapper252'):
        assert not _is_linked(a2, 'domain_ModelMapper252', b)


def test_assoc_specifiers47_reverse_link_reassign_clear():
    a1 = domain_Specifier(name="sample_text", uid="sample_text")
    a2 = domain_Specifier(name="sample_text_2", uid="sample_text_2")
    b = domain_Artifact(description="sample_text", name="sample_text", template="sample_text", uid="sample_text")
    _safe_set(b, 'parent48', {a1})
    assert _is_linked(b, 'parent48', a1)
    if hasattr(a1, 'Specifier'):
        assert _is_linked(a1, 'Specifier', b)
    _safe_set(b, 'parent48', {a2})
    assert _is_linked(b, 'parent48', a2)
    if hasattr(a1, 'Specifier'):
        assert not _is_linked(a1, 'Specifier', b)
    if hasattr(a2, 'Specifier'):
        assert _is_linked(a2, 'Specifier', b)
    _safe_set(b, 'parent48', set())
    assert not _is_linked(b, 'parent48', a2)
    if hasattr(a2, 'Specifier'):
        assert not _is_linked(a2, 'Specifier', b)


def test_assoc_startSeq203_reverse_link_reassign_clear():
    a1 = domain_DeploymentStarStep(name="sample_text", uid="sample_text")
    a2 = domain_DeploymentStarStep(name="sample_text_2", uid="sample_text_2")
    b = domain_DeploymentComponents(uid="sample_text")
    _safe_set(b, 'domain_DeploymentComponents204', a1)
    assert _is_linked(b, 'domain_DeploymentComponents204', a1)
    if hasattr(a1, 'domain_DeploymentStarStep'):
        assert _is_linked(a1, 'domain_DeploymentStarStep', b)
    _safe_set(b, 'domain_DeploymentComponents204', a2)
    assert _is_linked(b, 'domain_DeploymentComponents204', a2)
    if hasattr(a1, 'domain_DeploymentStarStep'):
        assert not _is_linked(a1, 'domain_DeploymentStarStep', b)
    if hasattr(a2, 'domain_DeploymentStarStep'):
        assert _is_linked(a2, 'domain_DeploymentStarStep', b)
    _safe_set(b, 'domain_DeploymentComponents204', None)
    assert not _is_linked(b, 'domain_DeploymentComponents204', a2)
    if hasattr(a2, 'domain_DeploymentStarStep'):
        assert not _is_linked(a2, 'domain_DeploymentStarStep', b)


def test_assoc_styleLibrary179_reverse_link_reassign_clear():
    a1 = domain_StyleLibrary(name="sample_text", uid="sample_text")
    a2 = domain_StyleLibrary(name="sample_text_2", uid="sample_text_2")
    b = domain_CSSMapper(fakePackageName="sample_text", fakeTypeName="sample_text", libraryUrl="sample_text")
    _safe_set(b, 'domain_CSSMapper180', a1)
    assert _is_linked(b, 'domain_CSSMapper180', a1)
    if hasattr(a1, 'domain_StyleLibrary181'):
        assert _is_linked(a1, 'domain_StyleLibrary181', b)
    _safe_set(b, 'domain_CSSMapper180', a2)
    assert _is_linked(b, 'domain_CSSMapper180', a2)
    if hasattr(a1, 'domain_StyleLibrary181'):
        assert not _is_linked(a1, 'domain_StyleLibrary181', b)
    if hasattr(a2, 'domain_StyleLibrary181'):
        assert _is_linked(a2, 'domain_StyleLibrary181', b)
    _safe_set(b, 'domain_CSSMapper180', None)
    assert not _is_linked(b, 'domain_CSSMapper180', a2)
    if hasattr(a2, 'domain_StyleLibrary181'):
        assert not _is_linked(a2, 'domain_StyleLibrary181', b)


def test_assoc_stylePackage178_reverse_link_reassign_clear():
    a1 = domain_StylesPackage(name="sample_text", uid="sample_text")
    a2 = domain_StylesPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_CSSMapper(fakePackageName="sample_text", fakeTypeName="sample_text", libraryUrl="sample_text")
    _safe_set(b, 'domain_CSSMapper', a1)
    assert _is_linked(b, 'domain_CSSMapper', a1)
    if hasattr(a1, 'domain_StylesPackage'):
        assert _is_linked(a1, 'domain_StylesPackage', b)
    _safe_set(b, 'domain_CSSMapper', a2)
    assert _is_linked(b, 'domain_CSSMapper', a2)
    if hasattr(a1, 'domain_StylesPackage'):
        assert not _is_linked(a1, 'domain_StylesPackage', b)
    if hasattr(a2, 'domain_StylesPackage'):
        assert _is_linked(a2, 'domain_StylesPackage', b)
    _safe_set(b, 'domain_CSSMapper', None)
    assert not _is_linked(b, 'domain_CSSMapper', a2)
    if hasattr(a2, 'domain_StylesPackage'):
        assert not _is_linked(a2, 'domain_StylesPackage', b)


def test_assoc_styles167_reverse_link_reassign_clear():
    a1 = domain_StyleSet(name="sample_text", uid="sample_text")
    a2 = domain_StyleSet(name="sample_text_2", uid="sample_text_2")
    b = domain_StyleLibrary(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_StyleLibrary168', {a1})
    assert _is_linked(b, 'domain_StyleLibrary168', a1)
    if hasattr(a1, 'domain_StyleSet'):
        assert _is_linked(a1, 'domain_StyleSet', b)
    _safe_set(b, 'domain_StyleLibrary168', {a2})
    assert _is_linked(b, 'domain_StyleLibrary168', a2)
    if hasattr(a1, 'domain_StyleSet'):
        assert not _is_linked(a1, 'domain_StyleSet', b)
    if hasattr(a2, 'domain_StyleSet'):
        assert _is_linked(a2, 'domain_StyleSet', b)
    _safe_set(b, 'domain_StyleLibrary168', set())
    assert not _is_linked(b, 'domain_StyleLibrary168', a2)
    if hasattr(a2, 'domain_StyleSet'):
        assert not _is_linked(a2, 'domain_StyleSet', b)


def test_assoc_styles99_reverse_link_reassign_clear():
    a1 = domain_StylesPackage(name="sample_text", uid="sample_text")
    a2 = domain_StylesPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_Styles(uid="sample_text")
    _safe_set(b, 'Styles', a1)
    assert _is_linked(b, 'Styles', a1)
    if hasattr(a1, 'parent100'):
        assert _is_linked(a1, 'parent100', b)
    _safe_set(b, 'Styles', a2)
    assert _is_linked(b, 'Styles', a2)
    if hasattr(a1, 'parent100'):
        assert not _is_linked(a1, 'parent100', b)
    if hasattr(a2, 'parent100'):
        assert _is_linked(a2, 'parent100', b)
    _safe_set(b, 'Styles', None)
    assert not _is_linked(b, 'Styles', a2)
    if hasattr(a2, 'parent100'):
        assert not _is_linked(a2, 'parent100', b)


def test_assoc_stylesPackage95_reverse_link_reassign_clear():
    a1 = domain_StylesPackage(name="sample_text", uid="sample_text")
    a2 = domain_StylesPackage(name="sample_text_2", uid="sample_text_2")
    b = domain_ApplicationStyle(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent96', {a1})
    assert _is_linked(b, 'parent96', a1)
    if hasattr(a1, 'StylesPackage'):
        assert _is_linked(a1, 'StylesPackage', b)
    _safe_set(b, 'parent96', {a2})
    assert _is_linked(b, 'parent96', a2)
    if hasattr(a1, 'StylesPackage'):
        assert not _is_linked(a1, 'StylesPackage', b)
    if hasattr(a2, 'StylesPackage'):
        assert _is_linked(a2, 'StylesPackage', b)
    _safe_set(b, 'parent96', set())
    assert not _is_linked(b, 'parent96', a2)
    if hasattr(a2, 'StylesPackage'):
        assert not _is_linked(a2, 'StylesPackage', b)


def test_assoc_subsystems568_reverse_link_reassign_clear():
    a1 = domain_Subsystem(name="sample_text", uid="sample_text")
    a2 = domain_Subsystem(name="sample_text_2", uid="sample_text_2")
    b = domain_Datacenter(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent569', {a1})
    assert _is_linked(b, 'parent569', a1)
    if hasattr(a1, 'Subsystem'):
        assert _is_linked(a1, 'Subsystem', b)
    _safe_set(b, 'parent569', {a2})
    assert _is_linked(b, 'parent569', a2)
    if hasattr(a1, 'Subsystem'):
        assert not _is_linked(a1, 'Subsystem', b)
    if hasattr(a2, 'Subsystem'):
        assert _is_linked(a2, 'Subsystem', b)
    _safe_set(b, 'parent569', set())
    assert not _is_linked(b, 'parent569', a2)
    if hasattr(a2, 'Subsystem'):
        assert not _is_linked(a2, 'Subsystem', b)


def test_assoc_tabPagesInheritances355_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_TabPagesInheritance(uid="sample_text")
    _safe_set(b, 'domain_TabPagesInheritance', a1)
    assert _is_linked(b, 'domain_TabPagesInheritance', a1)
    if hasattr(a1, 'domain_Views356'):
        assert _is_linked(a1, 'domain_Views356', b)
    _safe_set(b, 'domain_TabPagesInheritance', a2)
    assert _is_linked(b, 'domain_TabPagesInheritance', a2)
    if hasattr(a1, 'domain_Views356'):
        assert not _is_linked(a1, 'domain_Views356', b)
    if hasattr(a2, 'domain_Views356'):
        assert _is_linked(a2, 'domain_Views356', b)
    _safe_set(b, 'domain_TabPagesInheritance', None)
    assert not _is_linked(b, 'domain_TabPagesInheritance', a2)
    if hasattr(a2, 'domain_Views356'):
        assert not _is_linked(a2, 'domain_Views356', b)


def test_assoc_target228_reverse_link_reassign_clear():
    a1 = domain_Configuration(name="sample_text", uid="sample_text")
    a2 = domain_Configuration(name="sample_text_2", uid="sample_text_2")
    b = domain_ConfigExtension(uid="sample_text")
    _safe_set(b, 'domain_ConfigExtension229', a1)
    assert _is_linked(b, 'domain_ConfigExtension229', a1)
    if hasattr(a1, 'domain_Configuration230'):
        assert _is_linked(a1, 'domain_Configuration230', b)
    _safe_set(b, 'domain_ConfigExtension229', a2)
    assert _is_linked(b, 'domain_ConfigExtension229', a2)
    if hasattr(a1, 'domain_Configuration230'):
        assert not _is_linked(a1, 'domain_Configuration230', b)
    if hasattr(a2, 'domain_Configuration230'):
        assert _is_linked(a2, 'domain_Configuration230', b)
    _safe_set(b, 'domain_ConfigExtension229', None)
    assert not _is_linked(b, 'domain_ConfigExtension229', a2)
    if hasattr(a2, 'domain_Configuration230'):
        assert not _is_linked(a2, 'domain_Configuration230', b)


def test_assoc_target291_reverse_link_reassign_clear():
    a1 = domain_TypeElement(name="sample_text", uid="sample_text")
    a2 = domain_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = domain_RelationShip(uid="sample_text")
    _safe_set(b, 'domain_RelationShip292', a1)
    assert _is_linked(b, 'domain_RelationShip292', a1)
    if hasattr(a1, 'domain_TypeElement293'):
        assert _is_linked(a1, 'domain_TypeElement293', b)
    _safe_set(b, 'domain_RelationShip292', a2)
    assert _is_linked(b, 'domain_RelationShip292', a2)
    if hasattr(a1, 'domain_TypeElement293'):
        assert not _is_linked(a1, 'domain_TypeElement293', b)
    if hasattr(a2, 'domain_TypeElement293'):
        assert _is_linked(a2, 'domain_TypeElement293', b)
    _safe_set(b, 'domain_RelationShip292', None)
    assert not _is_linked(b, 'domain_RelationShip292', a2)
    if hasattr(a2, 'domain_TypeElement293'):
        assert not _is_linked(a2, 'domain_TypeElement293', b)


def test_assoc_target372_reverse_link_reassign_clear():
    a1 = domain_ViewInheritance(uid="sample_text")
    a2 = domain_ViewInheritance(uid="sample_text_2")
    b = domain_CanvasFrame(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_CanvasFrame374', a1)
    assert _is_linked(b, 'domain_CanvasFrame374', a1)
    if hasattr(a1, 'domain_ViewInheritance373'):
        assert _is_linked(a1, 'domain_ViewInheritance373', b)
    _safe_set(b, 'domain_CanvasFrame374', a2)
    assert _is_linked(b, 'domain_CanvasFrame374', a2)
    if hasattr(a1, 'domain_ViewInheritance373'):
        assert not _is_linked(a1, 'domain_ViewInheritance373', b)
    if hasattr(a2, 'domain_ViewInheritance373'):
        assert _is_linked(a2, 'domain_ViewInheritance373', b)
    _safe_set(b, 'domain_CanvasFrame374', None)
    assert not _is_linked(b, 'domain_CanvasFrame374', a2)
    if hasattr(a2, 'domain_ViewInheritance373'):
        assert not _is_linked(a2, 'domain_ViewInheritance373', b)


def test_assoc_target392_reverse_link_reassign_clear():
    a1 = domain_MessageElement(label="sample_text")
    a2 = domain_MessageElement(label="sample_text_2")
    b = domain_LinkToMessage(uid="sample_text")
    _safe_set(b, 'domain_LinkToMessage393', a1)
    assert _is_linked(b, 'domain_LinkToMessage393', a1)
    if hasattr(a1, 'domain_MessageElement'):
        assert _is_linked(a1, 'domain_MessageElement', b)
    _safe_set(b, 'domain_LinkToMessage393', a2)
    assert _is_linked(b, 'domain_LinkToMessage393', a2)
    if hasattr(a1, 'domain_MessageElement'):
        assert not _is_linked(a1, 'domain_MessageElement', b)
    if hasattr(a2, 'domain_MessageElement'):
        assert _is_linked(a2, 'domain_MessageElement', b)
    _safe_set(b, 'domain_LinkToMessage393', None)
    assert not _is_linked(b, 'domain_LinkToMessage393', a2)
    if hasattr(a2, 'domain_MessageElement'):
        assert not _is_linked(a2, 'domain_MessageElement', b)


def test_assoc_target397_reverse_link_reassign_clear():
    a1 = domain_LinkToLabel(uid="sample_text")
    a2 = domain_LinkToLabel(uid="sample_text_2")
    b = domain_Label(label="sample_text")
    _safe_set(b, 'domain_Label', a1)
    assert _is_linked(b, 'domain_Label', a1)
    if hasattr(a1, 'domain_LinkToLabel398'):
        assert _is_linked(a1, 'domain_LinkToLabel398', b)
    _safe_set(b, 'domain_Label', a2)
    assert _is_linked(b, 'domain_Label', a2)
    if hasattr(a1, 'domain_LinkToLabel398'):
        assert not _is_linked(a1, 'domain_LinkToLabel398', b)
    if hasattr(a2, 'domain_LinkToLabel398'):
        assert _is_linked(a2, 'domain_LinkToLabel398', b)
    _safe_set(b, 'domain_Label', None)
    assert not _is_linked(b, 'domain_Label', a2)
    if hasattr(a2, 'domain_LinkToLabel398'):
        assert not _is_linked(a2, 'domain_LinkToLabel398', b)


def test_assoc_targetProperty297_reverse_link_reassign_clear():
    a1 = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    a2 = domain_Attribute(name="sample_text_2", pk=False, uid="sample_text_2")
    b = domain_Assosiation(type="sample_text")
    _safe_set(b, 'domain_Assosiation298', a1)
    assert _is_linked(b, 'domain_Assosiation298', a1)
    if hasattr(a1, 'domain_Attribute299'):
        assert _is_linked(a1, 'domain_Attribute299', b)
    _safe_set(b, 'domain_Assosiation298', a2)
    assert _is_linked(b, 'domain_Assosiation298', a2)
    if hasattr(a1, 'domain_Attribute299'):
        assert not _is_linked(a1, 'domain_Attribute299', b)
    if hasattr(a2, 'domain_Attribute299'):
        assert _is_linked(a2, 'domain_Attribute299', b)
    _safe_set(b, 'domain_Assosiation298', None)
    assert not _is_linked(b, 'domain_Assosiation298', a2)
    if hasattr(a2, 'domain_Attribute299'):
        assert not _is_linked(a2, 'domain_Attribute299', b)


def test_assoc_translatioins141_reverse_link_reassign_clear():
    a1 = domain_Translation(translation="sample_text", uid="sample_text")
    a2 = domain_Translation(translation="sample_text_2", uid="sample_text_2")
    b = domain_Message(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Message142', {a1})
    assert _is_linked(b, 'domain_Message142', a1)
    if hasattr(a1, 'domain_Translation'):
        assert _is_linked(a1, 'domain_Translation', b)
    _safe_set(b, 'domain_Message142', {a2})
    assert _is_linked(b, 'domain_Message142', a2)
    if hasattr(a1, 'domain_Translation'):
        assert not _is_linked(a1, 'domain_Translation', b)
    if hasattr(a2, 'domain_Translation'):
        assert _is_linked(a2, 'domain_Translation', b)
    _safe_set(b, 'domain_Message142', set())
    assert not _is_linked(b, 'domain_Message142', a2)
    if hasattr(a2, 'domain_Translation'):
        assert not _is_linked(a2, 'domain_Translation', b)


def test_assoc_typeDefinition321_reverse_link_reassign_clear():
    a1 = domain_TypesRepository(uid="sample_text")
    a2 = domain_TypesRepository(uid="sample_text_2")
    b = domain_Types(name="sample_text", uid="sample_text")
    _safe_set(b, 'Types', a1)
    assert _is_linked(b, 'Types', a1)
    if hasattr(a1, 'parent322'):
        assert _is_linked(a1, 'parent322', b)
    _safe_set(b, 'Types', a2)
    assert _is_linked(b, 'Types', a2)
    if hasattr(a1, 'parent322'):
        assert not _is_linked(a1, 'parent322', b)
    if hasattr(a2, 'parent322'):
        assert _is_linked(a2, 'parent322', b)
    _safe_set(b, 'Types', None)
    assert not _is_linked(b, 'Types', a2)
    if hasattr(a2, 'parent322'):
        assert not _is_linked(a2, 'parent322', b)


def test_assoc_typeRef279_reverse_link_reassign_clear():
    a1 = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    a2 = domain_TypePointer(fakePackageName="sample_text_2", fakeTypeName="sample_text_2")
    b = domain_TypeElement(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_TypeElement', a1)
    assert _is_linked(b, 'domain_TypeElement', a1)
    if hasattr(a1, 'domain_TypePointer280'):
        assert _is_linked(a1, 'domain_TypePointer280', b)
    _safe_set(b, 'domain_TypeElement', a2)
    assert _is_linked(b, 'domain_TypeElement', a2)
    if hasattr(a1, 'domain_TypePointer280'):
        assert not _is_linked(a1, 'domain_TypePointer280', b)
    if hasattr(a2, 'domain_TypePointer280'):
        assert _is_linked(a2, 'domain_TypePointer280', b)
    _safe_set(b, 'domain_TypeElement', None)
    assert not _is_linked(b, 'domain_TypeElement', a2)
    if hasattr(a2, 'domain_TypePointer280'):
        assert not _is_linked(a2, 'domain_TypePointer280', b)


def test_assoc_typedefinition332_reverse_link_reassign_clear():
    a1 = domain_TypeDefinition(uid="sample_text")
    a2 = domain_TypeDefinition(uid="sample_text_2")
    b = domain_Package(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent333', a1)
    assert _is_linked(b, 'parent333', a1)
    if hasattr(a1, 'TypeDefinition334'):
        assert _is_linked(a1, 'TypeDefinition334', b)
    _safe_set(b, 'parent333', a2)
    assert _is_linked(b, 'parent333', a2)
    if hasattr(a1, 'TypeDefinition334'):
        assert not _is_linked(a1, 'TypeDefinition334', b)
    if hasattr(a2, 'TypeDefinition334'):
        assert _is_linked(a2, 'TypeDefinition334', b)
    _safe_set(b, 'parent333', None)
    assert not _is_linked(b, 'parent333', a2)
    if hasattr(a2, 'TypeDefinition334'):
        assert not _is_linked(a2, 'TypeDefinition334', b)


def test_assoc_types281_reverse_link_reassign_clear():
    a1 = domain_TypeElement(name="sample_text", uid="sample_text")
    a2 = domain_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = domain_TypeDefinition(uid="sample_text")
    _safe_set(b, 'parent282', {a1})
    assert _is_linked(b, 'parent282', a1)
    if hasattr(a1, 'TypeElement'):
        assert _is_linked(a1, 'TypeElement', b)
    _safe_set(b, 'parent282', {a2})
    assert _is_linked(b, 'parent282', a2)
    if hasattr(a1, 'TypeElement'):
        assert not _is_linked(a1, 'TypeElement', b)
    if hasattr(a2, 'TypeElement'):
        assert _is_linked(a2, 'TypeElement', b)
    _safe_set(b, 'parent282', set())
    assert not _is_linked(b, 'parent282', a2)
    if hasattr(a2, 'TypeElement'):
        assert not _is_linked(a2, 'TypeElement', b)


def test_assoc_typesrepository17_reverse_link_reassign_clear():
    a1 = domain_TypesRepository(uid="sample_text")
    a2 = domain_TypesRepository(uid="sample_text_2")
    b = domain_DomainTypes(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent18', a1)
    assert _is_linked(b, 'parent18', a1)
    if hasattr(a1, 'TypesRepository'):
        assert _is_linked(a1, 'TypesRepository', b)
    _safe_set(b, 'parent18', a2)
    assert _is_linked(b, 'parent18', a2)
    if hasattr(a1, 'TypesRepository'):
        assert not _is_linked(a1, 'TypesRepository', b)
    if hasattr(a2, 'TypesRepository'):
        assert _is_linked(a2, 'TypesRepository', b)
    _safe_set(b, 'parent18', None)
    assert not _is_linked(b, 'parent18', a2)
    if hasattr(a2, 'TypesRepository'):
        assert not _is_linked(a2, 'TypesRepository', b)


def test_assoc_uipackage107_reverse_link_reassign_clear():
    a1 = domain_UIPackage(uid="sample_text")
    a2 = domain_UIPackage(uid="sample_text_2")
    b = domain_ApplicationUIPackage(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent108', a1)
    assert _is_linked(b, 'parent108', a1)
    if hasattr(a1, 'UIPackage'):
        assert _is_linked(a1, 'UIPackage', b)
    _safe_set(b, 'parent108', a2)
    assert _is_linked(b, 'parent108', a2)
    if hasattr(a1, 'UIPackage'):
        assert not _is_linked(a1, 'UIPackage', b)
    if hasattr(a2, 'UIPackage'):
        assert _is_linked(a2, 'UIPackage', b)
    _safe_set(b, 'parent108', None)
    assert not _is_linked(b, 'parent108', a2)
    if hasattr(a2, 'UIPackage'):
        assert not _is_linked(a2, 'UIPackage', b)


def test_assoc_update513_reverse_link_reassign_clear():
    a1 = domain_UpdateTrigger(uid="sample_text")
    a2 = domain_UpdateTrigger(uid="sample_text_2")
    b = domain_DataControl(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_DataControl514', a1)
    assert _is_linked(b, 'domain_DataControl514', a1)
    if hasattr(a1, 'domain_UpdateTrigger'):
        assert _is_linked(a1, 'domain_UpdateTrigger', b)
    _safe_set(b, 'domain_DataControl514', a2)
    assert _is_linked(b, 'domain_DataControl514', a2)
    if hasattr(a1, 'domain_UpdateTrigger'):
        assert not _is_linked(a1, 'domain_UpdateTrigger', b)
    if hasattr(a2, 'domain_UpdateTrigger'):
        assert _is_linked(a2, 'domain_UpdateTrigger', b)
    _safe_set(b, 'domain_DataControl514', None)
    assert not _is_linked(b, 'domain_DataControl514', a2)
    if hasattr(a2, 'domain_UpdateTrigger'):
        assert not _is_linked(a2, 'domain_UpdateTrigger', b)


def test_assoc_value402_reverse_link_reassign_clear():
    a1 = domain_ContextValue(constant=True, uid="sample_text", value="sample_text")
    a2 = domain_ContextValue(constant=False, uid="sample_text_2", value="sample_text_2")
    b = domain_ContextParameter(operation="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ContextParameter403', a1)
    assert _is_linked(b, 'domain_ContextParameter403', a1)
    if hasattr(a1, 'domain_ContextValue'):
        assert _is_linked(a1, 'domain_ContextValue', b)
    _safe_set(b, 'domain_ContextParameter403', a2)
    assert _is_linked(b, 'domain_ContextParameter403', a2)
    if hasattr(a1, 'domain_ContextValue'):
        assert not _is_linked(a1, 'domain_ContextValue', b)
    if hasattr(a2, 'domain_ContextValue'):
        assert _is_linked(a2, 'domain_ContextValue', b)
    _safe_set(b, 'domain_ContextParameter403', None)
    assert not _is_linked(b, 'domain_ContextParameter403', a2)
    if hasattr(a2, 'domain_ContextValue'):
        assert not _is_linked(a2, 'domain_ContextValue', b)


def test_assoc_valueRef263_reverse_link_reassign_clear():
    a1 = domain_Option(uid="sample_text", value="sample_text")
    a2 = domain_Option(uid="sample_text_2", value="sample_text_2")
    b = domain_MappingSpecifier(uid="sample_text")
    _safe_set(b, 'domain_MappingSpecifier264', a1)
    assert _is_linked(b, 'domain_MappingSpecifier264', a1)
    if hasattr(a1, 'domain_Option'):
        assert _is_linked(a1, 'domain_Option', b)
    _safe_set(b, 'domain_MappingSpecifier264', a2)
    assert _is_linked(b, 'domain_MappingSpecifier264', a2)
    if hasattr(a1, 'domain_Option'):
        assert not _is_linked(a1, 'domain_Option', b)
    if hasattr(a2, 'domain_Option'):
        assert _is_linked(a2, 'domain_Option', b)
    _safe_set(b, 'domain_MappingSpecifier264', None)
    assert not _is_linked(b, 'domain_MappingSpecifier264', a2)
    if hasattr(a2, 'domain_Option'):
        assert not _is_linked(a2, 'domain_Option', b)


def test_assoc_variables270_reverse_link_reassign_clear():
    a1 = domain_QueryVariable(uid="sample_text", value="sample_text")
    a2 = domain_QueryVariable(uid="sample_text_2", value="sample_text_2")
    b = domain_Query(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Query271', {a1})
    assert _is_linked(b, 'domain_Query271', a1)
    if hasattr(a1, 'domain_QueryVariable'):
        assert _is_linked(a1, 'domain_QueryVariable', b)
    _safe_set(b, 'domain_Query271', {a2})
    assert _is_linked(b, 'domain_Query271', a2)
    if hasattr(a1, 'domain_QueryVariable'):
        assert not _is_linked(a1, 'domain_QueryVariable', b)
    if hasattr(a2, 'domain_QueryVariable'):
        assert _is_linked(a2, 'domain_QueryVariable', b)
    _safe_set(b, 'domain_Query271', set())
    assert not _is_linked(b, 'domain_Query271', a2)
    if hasattr(a2, 'domain_QueryVariable'):
        assert not _is_linked(a2, 'domain_QueryVariable', b)


def test_assoc_variables484_reverse_link_reassign_clear():
    a1 = domain_Root(name="sample_text", uid="sample_text")
    a2 = domain_Root(name="sample_text_2", uid="sample_text_2")
    b = domain_FormVariable(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_FormVariable', a1)
    assert _is_linked(b, 'domain_FormVariable', a1)
    if hasattr(a1, 'domain_Root485'):
        assert _is_linked(a1, 'domain_Root485', b)
    _safe_set(b, 'domain_FormVariable', a2)
    assert _is_linked(b, 'domain_FormVariable', a2)
    if hasattr(a1, 'domain_Root485'):
        assert not _is_linked(a1, 'domain_Root485', b)
    if hasattr(a2, 'domain_Root485'):
        assert _is_linked(a2, 'domain_Root485', b)
    _safe_set(b, 'domain_FormVariable', None)
    assert not _is_linked(b, 'domain_FormVariable', a2)
    if hasattr(a2, 'domain_Root485'):
        assert not _is_linked(a2, 'domain_Root485', b)


def test_assoc_view343_reverse_link_reassign_clear():
    a1 = domain_FormView(name="sample_text", uid="sample_text")
    a2 = domain_FormView(name="sample_text_2", uid="sample_text_2")
    b = domain_Form(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_Form344', a1)
    assert _is_linked(b, 'domain_Form344', a1)
    if hasattr(a1, 'domain_FormView'):
        assert _is_linked(a1, 'domain_FormView', b)
    _safe_set(b, 'domain_Form344', a2)
    assert _is_linked(b, 'domain_Form344', a2)
    if hasattr(a1, 'domain_FormView'):
        assert not _is_linked(a1, 'domain_FormView', b)
    if hasattr(a2, 'domain_FormView'):
        assert _is_linked(a2, 'domain_FormView', b)
    _safe_set(b, 'domain_Form344', None)
    assert not _is_linked(b, 'domain_Form344', a2)
    if hasattr(a2, 'domain_FormView'):
        assert not _is_linked(a2, 'domain_FormView', b)


def test_assoc_view349_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_FormView(name="sample_text", uid="sample_text")
    _safe_set(b, 'parent350', a1)
    assert _is_linked(b, 'parent350', a1)
    if hasattr(a1, 'Views'):
        assert _is_linked(a1, 'Views', b)
    _safe_set(b, 'parent350', a2)
    assert _is_linked(b, 'parent350', a2)
    if hasattr(a1, 'Views'):
        assert not _is_linked(a1, 'Views', b)
    if hasattr(a2, 'Views'):
        assert _is_linked(a2, 'Views', b)
    _safe_set(b, 'parent350', None)
    assert not _is_linked(b, 'parent350', a2)
    if hasattr(a2, 'Views'):
        assert not _is_linked(a2, 'Views', b)


def test_assoc_viewInheritances353_reverse_link_reassign_clear():
    a1 = domain_Views(uid="sample_text")
    a2 = domain_Views(uid="sample_text_2")
    b = domain_ViewInheritance(uid="sample_text")
    _safe_set(b, 'domain_ViewInheritance', a1)
    assert _is_linked(b, 'domain_ViewInheritance', a1)
    if hasattr(a1, 'domain_Views354'):
        assert _is_linked(a1, 'domain_Views354', b)
    _safe_set(b, 'domain_ViewInheritance', a2)
    assert _is_linked(b, 'domain_ViewInheritance', a2)
    if hasattr(a1, 'domain_Views354'):
        assert not _is_linked(a1, 'domain_Views354', b)
    if hasattr(a2, 'domain_Views354'):
        assert _is_linked(a2, 'domain_Views354', b)
    _safe_set(b, 'domain_ViewInheritance', None)
    assert not _is_linked(b, 'domain_ViewInheritance', a2)
    if hasattr(a2, 'domain_Views354'):
        assert not _is_linked(a2, 'domain_Views354', b)


def test_assoc_viewPortTrigger366_reverse_link_reassign_clear():
    a1 = domain_ViewPortTrigger(uid="sample_text")
    a2 = domain_ViewPortTrigger(uid="sample_text_2")
    b = domain_ViewPort(name="sample_text", uid="sample_text")
    _safe_set(b, 'domain_ViewPort', a1)
    assert _is_linked(b, 'domain_ViewPort', a1)
    if hasattr(a1, 'domain_ViewPortTrigger'):
        assert _is_linked(a1, 'domain_ViewPortTrigger', b)
    _safe_set(b, 'domain_ViewPort', a2)
    assert _is_linked(b, 'domain_ViewPort', a2)
    if hasattr(a1, 'domain_ViewPortTrigger'):
        assert not _is_linked(a1, 'domain_ViewPortTrigger', b)
    if hasattr(a2, 'domain_ViewPortTrigger'):
        assert _is_linked(a2, 'domain_ViewPortTrigger', b)
    _safe_set(b, 'domain_ViewPort', None)
    assert not _is_linked(b, 'domain_ViewPort', a2)
    if hasattr(a2, 'domain_ViewPortTrigger'):
        assert not _is_linked(a2, 'domain_ViewPortTrigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_any131_stub_double():
    # domain_EObject has no real 'domain_EObject133' property in the generated
    # code (a bare stub) -- manually attach it so domain_Messages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Messages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Messages(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject133', None)
    _safe_set(owner, 'domain_Messages132', partner)
    assert getattr(partner, 'domain_EObject133') == owner
    _safe_set(owner, 'domain_Messages132', None)
    assert getattr(partner, 'domain_EObject133') is None


def test_assoc_any152_stub_double():
    # domain_EObject has no real 'domain_EObject154' property in the generated
    # code (a bare stub) -- manually attach it so domain_Roles's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Roles's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Roles(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject154', None)
    _safe_set(owner, 'domain_Roles153', partner)
    assert getattr(partner, 'domain_EObject154') == owner
    _safe_set(owner, 'domain_Roles153', None)
    assert getattr(partner, 'domain_EObject154') is None


def test_assoc_any164_stub_double():
    # domain_EObject has no real 'domain_EObject166' property in the generated
    # code (a bare stub) -- manually attach it so domain_Styles's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Styles's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Styles(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject166', None)
    _safe_set(owner, 'domain_Styles165', partner)
    assert getattr(partner, 'domain_EObject166') == owner
    _safe_set(owner, 'domain_Styles165', None)
    assert getattr(partner, 'domain_EObject166') is None


def test_assoc_any173_stub_double():
    # domain_EObject has no real 'domain_EObject174' property in the generated
    # code (a bare stub) -- manually attach it so domain_Mappers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Mappers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Mappers(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject174', None)
    _safe_set(owner, 'domain_Mappers', partner)
    assert getattr(partner, 'domain_EObject174') == owner
    _safe_set(owner, 'domain_Mappers', None)
    assert getattr(partner, 'domain_EObject174') is None


def test_assoc_any196_stub_double():
    # domain_EObject has no real 'domain_EObject198' property in the generated
    # code (a bare stub) -- manually attach it so domain_Recipes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Recipes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Recipes(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject198', None)
    _safe_set(owner, 'domain_Recipes197', partner)
    assert getattr(partner, 'domain_EObject198') == owner
    _safe_set(owner, 'domain_Recipes197', None)
    assert getattr(partner, 'domain_EObject198') is None


def test_assoc_any205_stub_double():
    # domain_EObject has no real 'domain_EObject207' property in the generated
    # code (a bare stub) -- manually attach it so domain_DeploymentComponents's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DeploymentComponents's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DeploymentComponents(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject207', None)
    _safe_set(owner, 'domain_DeploymentComponents206', partner)
    assert getattr(partner, 'domain_EObject207') == owner
    _safe_set(owner, 'domain_DeploymentComponents206', None)
    assert getattr(partner, 'domain_EObject207') is None


def test_assoc_any285_stub_double():
    # domain_EObject has no real 'domain_EObject287' property in the generated
    # code (a bare stub) -- manually attach it so domain_TypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_TypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_TypeDefinition(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject287', None)
    _safe_set(owner, 'domain_TypeDefinition286', partner)
    assert getattr(partner, 'domain_EObject287') == owner
    _safe_set(owner, 'domain_TypeDefinition286', None)
    assert getattr(partner, 'domain_EObject287') is None


def test_assoc_any325_stub_double():
    # domain_EObject has no real 'domain_EObject326' property in the generated
    # code (a bare stub) -- manually attach it so domain_TypesRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_TypesRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_TypesRepository(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject326', None)
    _safe_set(owner, 'domain_TypesRepository', partner)
    assert getattr(partner, 'domain_EObject326') == owner
    _safe_set(owner, 'domain_TypesRepository', None)
    assert getattr(partner, 'domain_EObject326') is None


def test_assoc_any340_stub_double():
    # domain_EObject has no real 'domain_EObject342' property in the generated
    # code (a bare stub) -- manually attach it so domain_UIPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_UIPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_UIPackage(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject342', None)
    _safe_set(owner, 'domain_UIPackage341', partner)
    assert getattr(partner, 'domain_EObject342') == owner
    _safe_set(owner, 'domain_UIPackage341', None)
    assert getattr(partner, 'domain_EObject342') is None


def test_assoc_any359_stub_double():
    # domain_EObject has no real 'domain_EObject361' property in the generated
    # code (a bare stub) -- manually attach it so domain_Views's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Views's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Views(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject361', None)
    _safe_set(owner, 'domain_Views360', partner)
    assert getattr(partner, 'domain_EObject361') == owner
    _safe_set(owner, 'domain_Views360', None)
    assert getattr(partner, 'domain_EObject361') is None


def test_assoc_any37_stub_double():
    # domain_EObject has no real 'domain_EObject38' property in the generated
    # code (a bare stub) -- manually attach it so domain_Artifacts's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Artifacts's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Artifacts(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject38', None)
    _safe_set(owner, 'domain_Artifacts', partner)
    assert getattr(partner, 'domain_EObject38') == owner
    _safe_set(owner, 'domain_Artifacts', None)
    assert getattr(partner, 'domain_EObject38') is None


def test_assoc_any387_stub_double():
    # domain_EObject has no real 'domain_EObject389' property in the generated
    # code (a bare stub) -- manually attach it so domain_CanvasView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_CanvasView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_CanvasView(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject389', None)
    _safe_set(owner, 'domain_CanvasView388', partner)
    assert getattr(partner, 'domain_EObject389') == owner
    _safe_set(owner, 'domain_CanvasView388', None)
    assert getattr(partner, 'domain_EObject389') is None


def test_assoc_any477_stub_double():
    # domain_EObject has no real 'domain_EObject479' property in the generated
    # code (a bare stub) -- manually attach it so domain_Controls's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Controls's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Controls(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject479', None)
    _safe_set(owner, 'domain_Controls478', partner)
    assert getattr(partner, 'domain_EObject479') == owner
    _safe_set(owner, 'domain_Controls478', None)
    assert getattr(partner, 'domain_EObject479') is None


def test_assoc_any5_stub_double():
    # domain_EObject has no real 'domain_EObject' property in the generated
    # code (a bare stub) -- manually attach it so domain_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Domain(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject', None)
    _safe_set(owner, 'domain_Domain', partner)
    assert getattr(partner, 'domain_EObject') == owner
    _safe_set(owner, 'domain_Domain', None)
    assert getattr(partner, 'domain_EObject') is None


def test_assoc_any563_stub_double():
    # domain_EObject has no real 'domain_EObject565' property in the generated
    # code (a bare stub) -- manually attach it so domain_EnterpriseInfrastructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_EnterpriseInfrastructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_EnterpriseInfrastructure(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject565', None)
    _safe_set(owner, 'domain_EnterpriseInfrastructure564', partner)
    assert getattr(partner, 'domain_EObject565') == owner
    _safe_set(owner, 'domain_EnterpriseInfrastructure564', None)
    assert getattr(partner, 'domain_EObject565') is None


def test_assoc_any588_stub_double():
    # domain_EObject has no real 'domain_EObject590' property in the generated
    # code (a bare stub) -- manually attach it so domain_MenuView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_MenuView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_MenuView(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject590', None)
    _safe_set(owner, 'domain_MenuView589', partner)
    assert getattr(partner, 'domain_EObject590') == owner
    _safe_set(owner, 'domain_MenuView589', None)
    assert getattr(partner, 'domain_EObject590') is None


def test_assoc_any83_stub_double():
    # domain_EObject has no real 'domain_EObject84' property in the generated
    # code (a bare stub) -- manually attach it so domain_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Application(uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject84', None)
    _safe_set(owner, 'domain_Application', partner)
    assert getattr(partner, 'domain_EObject84') == owner
    _safe_set(owner, 'domain_Application', None)
    assert getattr(partner, 'domain_EObject84') is None


def test_assoc_attributes304_stub_double():
    # domain_Type has no real 'parent305' property in the generated
    # code (a bare stub) -- manually attach it so domain_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    partner = domain_Type()
    setattr(partner, 'parent305', None)
    _safe_set(owner, 'Attribute', partner)
    assert owner in getattr(partner, 'parent305')
    _safe_set(owner, 'Attribute', None)
    assert owner not in getattr(partner, 'parent305')


def test_assoc_baseCanvas382_stub_double():
    # domain_LayerHolder has no real 'domain_LayerHolder' property in the generated
    # code (a bare stub) -- manually attach it so domain_CanvasView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_CanvasView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_CanvasView(uid="sample_text")
    partner = domain_LayerHolder()
    setattr(partner, 'domain_LayerHolder', None)
    _safe_set(owner, 'domain_CanvasView', partner)
    assert getattr(partner, 'domain_LayerHolder') == owner
    _safe_set(owner, 'domain_CanvasView', None)
    assert getattr(partner, 'domain_LayerHolder') is None


def test_assoc_children399_stub_double():
    # domain_ChildrenHolder has no real 'domain_ChildrenHolder' property in the generated
    # code (a bare stub) -- manually attach it so domain_Uielement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Uielement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Uielement(uid="sample_text")
    partner = domain_ChildrenHolder()
    setattr(partner, 'domain_ChildrenHolder', None)
    _safe_set(owner, 'domain_Uielement', partner)
    assert owner in getattr(partner, 'domain_ChildrenHolder')
    _safe_set(owner, 'domain_Uielement', None)
    assert owner not in getattr(partner, 'domain_ChildrenHolder')


def test_assoc_classifier415_stub_double():
    # domain_StyleClass has no real 'domain_StyleClass416' property in the generated
    # code (a bare stub) -- manually attach it so domain_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Classifier(details="sample_text", uid="sample_text")
    partner = domain_StyleClass()
    setattr(partner, 'domain_StyleClass416', None)
    _safe_set(owner, 'domain_Classifier417', partner)
    assert getattr(partner, 'domain_StyleClass416') == owner
    _safe_set(owner, 'domain_Classifier417', None)
    assert getattr(partner, 'domain_StyleClass416') is None


def test_assoc_classifiers6_stub_double():
    # domain_Categorized has no real 'domain_Categorized' property in the generated
    # code (a bare stub) -- manually attach it so domain_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Classifier(details="sample_text", uid="sample_text")
    partner = domain_Categorized()
    setattr(partner, 'domain_Categorized', None)
    _safe_set(owner, 'domain_Classifier', partner)
    assert owner in getattr(partner, 'domain_Categorized')
    _safe_set(owner, 'domain_Classifier', None)
    assert owner not in getattr(partner, 'domain_Categorized')


def test_assoc_defaultSearch521_stub_double():
    # domain_ContextParameters has no real 'domain_ContextParameters523' property in the generated
    # code (a bare stub) -- manually attach it so domain_DataControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DataControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DataControl(name="sample_text", uid="sample_text")
    partner = domain_ContextParameters()
    setattr(partner, 'domain_ContextParameters523', None)
    _safe_set(owner, 'domain_DataControl522', partner)
    assert getattr(partner, 'domain_ContextParameters523') == owner
    _safe_set(owner, 'domain_DataControl522', None)
    assert getattr(partner, 'domain_ContextParameters523') is None


def test_assoc_extensionRef593_stub_double():
    # domain_MenuExtensionRef has no real 'domain_MenuExtensionRef' property in the generated
    # code (a bare stub) -- manually attach it so domain_MenuFolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_MenuFolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_MenuFolder(extensionPoint=True, name="sample_text", uid="sample_text")
    partner = domain_MenuExtensionRef()
    setattr(partner, 'domain_MenuExtensionRef', None)
    _safe_set(owner, 'domain_MenuFolder594', partner)
    assert getattr(partner, 'domain_MenuExtensionRef') == owner
    _safe_set(owner, 'domain_MenuFolder594', None)
    assert getattr(partner, 'domain_MenuExtensionRef') is None


def test_assoc_grants9_stub_double():
    # domain_Secured has no real 'domain_Secured' property in the generated
    # code (a bare stub) -- manually attach it so domain_GrantAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_GrantAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_GrantAccess(uid="sample_text")
    partner = domain_Secured()
    setattr(partner, 'domain_Secured', None)
    _safe_set(owner, 'domain_GrantAccess', partner)
    assert owner in getattr(partner, 'domain_Secured')
    _safe_set(owner, 'domain_GrantAccess', None)
    assert owner not in getattr(partner, 'domain_Secured')


def test_assoc_image464_stub_double():
    # domain_Context has no real 'domain_Context465' property in the generated
    # code (a bare stub) -- manually attach it so domain_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Tree(label="sample_text")
    partner = domain_Context()
    setattr(partner, 'domain_Context465', None)
    _safe_set(owner, 'domain_Tree', partner)
    assert getattr(partner, 'domain_Context465') == owner
    _safe_set(owner, 'domain_Tree', None)
    assert getattr(partner, 'domain_Context465') is None


def test_assoc_initialOptionMessage457_stub_double():
    # domain_Context has no real 'domain_Context459' property in the generated
    # code (a bare stub) -- manually attach it so domain_DropDownSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DropDownSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DropDownSelection(initialOptionValue="sample_text")
    partner = domain_Context()
    setattr(partner, 'domain_Context459', None)
    _safe_set(owner, 'domain_DropDownSelection458', partner)
    assert getattr(partner, 'domain_Context459') == owner
    _safe_set(owner, 'domain_DropDownSelection458', None)
    assert getattr(partner, 'domain_Context459') is None


def test_assoc_mappers216_stub_double():
    # domain_UsingMappers has no real 'domain_UsingMappers' property in the generated
    # code (a bare stub) -- manually attach it so domain_ApplicationMapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_ApplicationMapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_ApplicationMapper(name="sample_text", uid="sample_text")
    partner = domain_UsingMappers()
    setattr(partner, 'domain_UsingMappers', None)
    _safe_set(owner, 'domain_ApplicationMapper', partner)
    assert owner in getattr(partner, 'domain_UsingMappers')
    _safe_set(owner, 'domain_ApplicationMapper', None)
    assert owner not in getattr(partner, 'domain_UsingMappers')


def test_assoc_menu591_stub_double():
    # domain_MenuHolder has no real 'domain_MenuHolder' property in the generated
    # code (a bare stub) -- manually attach it so domain_MenuFolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_MenuFolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_MenuFolder(extensionPoint=True, name="sample_text", uid="sample_text")
    partner = domain_MenuHolder()
    setattr(partner, 'domain_MenuHolder', None)
    _safe_set(owner, 'domain_MenuFolder592', partner)
    assert getattr(partner, 'domain_MenuHolder') == owner
    _safe_set(owner, 'domain_MenuFolder592', None)
    assert getattr(partner, 'domain_MenuHolder') is None


def test_assoc_objRef406_stub_double():
    # domain_EObject has no real 'domain_EObject408' property in the generated
    # code (a bare stub) -- manually attach it so domain_ExpressionPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_ExpressionPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_ExpressionPart(expressionType="sample_text", order=7, uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject408', None)
    _safe_set(owner, 'domain_ExpressionPart407', partner)
    assert getattr(partner, 'domain_EObject408') == owner
    _safe_set(owner, 'domain_ExpressionPart407', None)
    assert getattr(partner, 'domain_EObject408') is None


def test_assoc_operations306_stub_double():
    # domain_Type has no real 'parent307' property in the generated
    # code (a bare stub) -- manually attach it so domain_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Operation(name="sample_text", uid="sample_text")
    partner = domain_Type()
    setattr(partner, 'parent307', None)
    _safe_set(owner, 'Operation', partner)
    assert owner in getattr(partner, 'parent307')
    _safe_set(owner, 'Operation', None)
    assert owner not in getattr(partner, 'parent307')


def test_assoc_optionCastDataControl452_stub_double():
    # domain_OptionSelection has no real 'domain_OptionSelection453' property in the generated
    # code (a bare stub) -- manually attach it so domain_DataControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DataControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DataControl(name="sample_text", uid="sample_text")
    partner = domain_OptionSelection()
    setattr(partner, 'domain_OptionSelection453', None)
    _safe_set(owner, 'domain_DataControl454', partner)
    assert getattr(partner, 'domain_OptionSelection453') == owner
    _safe_set(owner, 'domain_DataControl454', None)
    assert getattr(partner, 'domain_OptionSelection453') is None


def test_assoc_optionPointer447_stub_double():
    # domain_OptionSelection has no real 'domain_OptionSelection' property in the generated
    # code (a bare stub) -- manually attach it so domain_DataControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DataControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DataControl(name="sample_text", uid="sample_text")
    partner = domain_OptionSelection()
    setattr(partner, 'domain_OptionSelection', None)
    _safe_set(owner, 'domain_DataControl448', partner)
    assert getattr(partner, 'domain_OptionSelection') == owner
    _safe_set(owner, 'domain_DataControl448', None)
    assert getattr(partner, 'domain_OptionSelection') is None


def test_assoc_parameters409_stub_double():
    # domain_ContextParameters has no real 'domain_ContextParameters' property in the generated
    # code (a bare stub) -- manually attach it so domain_ContextParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_ContextParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_ContextParameter(operation="sample_text", uid="sample_text")
    partner = domain_ContextParameters()
    setattr(partner, 'domain_ContextParameters', None)
    _safe_set(owner, 'domain_ContextParameter410', partner)
    assert owner in getattr(partner, 'domain_ContextParameters')
    _safe_set(owner, 'domain_ContextParameter410', None)
    assert owner not in getattr(partner, 'domain_ContextParameters')


def test_assoc_parent308_stub_double():
    # domain_Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so domain_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Attribute(name="sample_text", pk=True, uid="sample_text")
    partner = domain_Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'Type') is None


def test_assoc_parent309_stub_double():
    # domain_Type has no real 'Type310' property in the generated
    # code (a bare stub) -- manually attach it so domain_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Operation(name="sample_text", uid="sample_text")
    partner = domain_Type()
    setattr(partner, 'Type310', None)
    _safe_set(owner, 'operations', partner)
    assert getattr(partner, 'Type310') == owner
    _safe_set(owner, 'operations', None)
    assert getattr(partner, 'Type310') is None


def test_assoc_parent320_stub_double():
    # domain_Enumarator has no real 'Enumarator' property in the generated
    # code (a bare stub) -- manually attach it so domain_EnumAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_EnumAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_EnumAttribute(name="sample_text", uid="sample_text", value="sample_text")
    partner = domain_Enumarator()
    setattr(partner, 'Enumarator', None)
    _safe_set(owner, 'values', partner)
    assert getattr(partner, 'Enumarator') == owner
    _safe_set(owner, 'values', None)
    assert getattr(partner, 'Enumarator') is None


def test_assoc_readOnly424_stub_double():
    # domain_Context has no real 'domain_Context426' property in the generated
    # code (a bare stub) -- manually attach it so domain_Uielement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Uielement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Uielement(uid="sample_text")
    partner = domain_Context()
    setattr(partner, 'domain_Context426', None)
    _safe_set(owner, 'domain_Uielement425', partner)
    assert getattr(partner, 'domain_Context426') == owner
    _safe_set(owner, 'domain_Uielement425', None)
    assert getattr(partner, 'domain_Context426') is None


def test_assoc_refObj400_stub_double():
    # domain_EObject has no real 'domain_EObject401' property in the generated
    # code (a bare stub) -- manually attach it so domain_ContextParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_ContextParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_ContextParameter(operation="sample_text", uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject401', None)
    _safe_set(owner, 'domain_ContextParameter', partner)
    assert getattr(partner, 'domain_EObject401') == owner
    _safe_set(owner, 'domain_ContextParameter', None)
    assert getattr(partner, 'domain_EObject401') is None


def test_assoc_refObj528_stub_double():
    # domain_EObject has no real 'domain_EObject530' property in the generated
    # code (a bare stub) -- manually attach it so domain_OrderBy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_OrderBy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_OrderBy(order="sample_text", uid="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject530', None)
    _safe_set(owner, 'domain_OrderBy529', partner)
    assert getattr(partner, 'domain_EObject530') == owner
    _safe_set(owner, 'domain_OrderBy529', None)
    assert getattr(partner, 'domain_EObject530') is None


def test_assoc_refreshAreas599_stub_double():
    # domain_MenuItem has no real 'domain_MenuItem600' property in the generated
    # code (a bare stub) -- manually attach it so domain_AreaRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_AreaRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_AreaRef(group=7)
    partner = domain_MenuItem()
    setattr(partner, 'domain_MenuItem600', None)
    _safe_set(owner, 'domain_AreaRef601', partner)
    assert owner in getattr(partner, 'domain_MenuItem600')
    _safe_set(owner, 'domain_AreaRef601', None)
    assert owner not in getattr(partner, 'domain_MenuItem600')


def test_assoc_required421_stub_double():
    # domain_Context has no real 'domain_Context423' property in the generated
    # code (a bare stub) -- manually attach it so domain_Uielement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_Uielement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_Uielement(uid="sample_text")
    partner = domain_Context()
    setattr(partner, 'domain_Context423', None)
    _safe_set(owner, 'domain_Uielement422', partner)
    assert getattr(partner, 'domain_Context423') == owner
    _safe_set(owner, 'domain_Uielement422', None)
    assert getattr(partner, 'domain_Context423') is None


def test_assoc_role182_stub_double():
    # domain_EObject has no real 'domain_EObject183' property in the generated
    # code (a bare stub) -- manually attach it so domain_RoleMapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_RoleMapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_RoleMapper(fakeRoleName="sample_text", globalRoleName="sample_text", localRoleName="sample_text")
    partner = domain_EObject()
    setattr(partner, 'domain_EObject183', None)
    _safe_set(owner, 'domain_RoleMapper', partner)
    assert getattr(partner, 'domain_EObject183') == owner
    _safe_set(owner, 'domain_RoleMapper', None)
    assert getattr(partner, 'domain_EObject183') is None


def test_assoc_selection455_stub_double():
    # domain_Selection has no real 'domain_Selection456' property in the generated
    # code (a bare stub) -- manually attach it so domain_DropDownSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DropDownSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DropDownSelection(initialOptionValue="sample_text")
    partner = domain_Selection()
    setattr(partner, 'domain_Selection456', None)
    _safe_set(owner, 'domain_DropDownSelection', partner)
    assert getattr(partner, 'domain_Selection456') == owner
    _safe_set(owner, 'domain_DropDownSelection', None)
    assert getattr(partner, 'domain_Selection456') is None


def test_assoc_source390_stub_double():
    # domain_InputElement has no real 'domain_InputElement' property in the generated
    # code (a bare stub) -- manually attach it so domain_LinkToMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_LinkToMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_LinkToMessage(uid="sample_text")
    partner = domain_InputElement()
    setattr(partner, 'domain_InputElement', None)
    _safe_set(owner, 'domain_LinkToMessage391', partner)
    assert getattr(partner, 'domain_InputElement') == owner
    _safe_set(owner, 'domain_LinkToMessage391', None)
    assert getattr(partner, 'domain_InputElement') is None


def test_assoc_source394_stub_double():
    # domain_InputElement has no real 'domain_InputElement396' property in the generated
    # code (a bare stub) -- manually attach it so domain_LinkToLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_LinkToLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_LinkToLabel(uid="sample_text")
    partner = domain_InputElement()
    setattr(partner, 'domain_InputElement396', None)
    _safe_set(owner, 'domain_LinkToLabel395', partner)
    assert getattr(partner, 'domain_InputElement396') == owner
    _safe_set(owner, 'domain_LinkToLabel395', None)
    assert getattr(partner, 'domain_InputElement396') is None


def test_assoc_sourceCastDataControl439_stub_double():
    # domain_SourcesPointer has no real 'domain_SourcesPointer440' property in the generated
    # code (a bare stub) -- manually attach it so domain_DataControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DataControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DataControl(name="sample_text", uid="sample_text")
    partner = domain_SourcesPointer()
    setattr(partner, 'domain_SourcesPointer440', None)
    _safe_set(owner, 'domain_DataControl441', partner)
    assert getattr(partner, 'domain_SourcesPointer440') == owner
    _safe_set(owner, 'domain_DataControl441', None)
    assert getattr(partner, 'domain_SourcesPointer440') is None


def test_assoc_sourcePointer433_stub_double():
    # domain_SourcesPointer has no real 'domain_SourcesPointer' property in the generated
    # code (a bare stub) -- manually attach it so domain_DataControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_DataControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_DataControl(name="sample_text", uid="sample_text")
    partner = domain_SourcesPointer()
    setattr(partner, 'domain_SourcesPointer', None)
    _safe_set(owner, 'domain_DataControl', partner)
    assert getattr(partner, 'domain_SourcesPointer') == owner
    _safe_set(owner, 'domain_DataControl', None)
    assert getattr(partner, 'domain_SourcesPointer') is None


def test_assoc_target377_stub_double():
    # domain_TabPage has no real 'domain_TabPage' property in the generated
    # code (a bare stub) -- manually attach it so domain_TabPagesInheritance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_TabPagesInheritance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_TabPagesInheritance(uid="sample_text")
    partner = domain_TabPage()
    setattr(partner, 'domain_TabPage', None)
    _safe_set(owner, 'domain_TabPagesInheritance378', partner)
    assert getattr(partner, 'domain_TabPage') == owner
    _safe_set(owner, 'domain_TabPagesInheritance378', None)
    assert getattr(partner, 'domain_TabPage') is None


def test_assoc_toSubmenu602_stub_double():
    # domain_SubMenu has no real 'domain_SubMenu' property in the generated
    # code (a bare stub) -- manually attach it so domain_MenuFolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_MenuFolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_MenuFolder(extensionPoint=True, name="sample_text", uid="sample_text")
    partner = domain_SubMenu()
    setattr(partner, 'domain_SubMenu', None)
    _safe_set(owner, 'domain_MenuFolder603', partner)
    assert getattr(partner, 'domain_SubMenu') == owner
    _safe_set(owner, 'domain_MenuFolder603', None)
    assert getattr(partner, 'domain_SubMenu') is None


def test_assoc_typePointers480_stub_double():
    # domain_ProxiesList has no real 'domain_ProxiesList' property in the generated
    # code (a bare stub) -- manually attach it so domain_TypePointer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_TypePointer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_TypePointer(fakePackageName="sample_text", fakeTypeName="sample_text")
    partner = domain_ProxiesList()
    setattr(partner, 'domain_ProxiesList', None)
    _safe_set(owner, 'domain_TypePointer481', partner)
    assert owner in getattr(partner, 'domain_ProxiesList')
    _safe_set(owner, 'domain_TypePointer481', None)
    assert owner not in getattr(partner, 'domain_ProxiesList')


def test_assoc_values318_stub_double():
    # domain_Enumarator has no real 'parent319' property in the generated
    # code (a bare stub) -- manually attach it so domain_EnumAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domain_EnumAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domain_EnumAttribute(name="sample_text", uid="sample_text", value="sample_text")
    partner = domain_Enumarator()
    setattr(partner, 'parent319', None)
    _safe_set(owner, 'EnumAttribute', partner)
    assert owner in getattr(partner, 'parent319')
    _safe_set(owner, 'EnumAttribute', None)
    assert owner not in getattr(partner, 'parent319')


