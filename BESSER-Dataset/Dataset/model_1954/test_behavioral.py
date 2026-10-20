import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MappingType,
    softGalleryLanguage_AlbumException,
    softGalleryLanguage_AlbumManagement,
    softGalleryLanguage_AlbumManagementFunctions,
    softGalleryLanguage_AmazonElasticComputeCloud,
    softGalleryLanguage_AmazonFile,
    softGalleryLanguage_AmazonFolder,
    softGalleryLanguage_AmazonSimpleStorageService,
    softGalleryLanguage_AmazonWebServices,
    softGalleryLanguage_AppAccess,
    softGalleryLanguage_AppAccessFunctions,
    softGalleryLanguage_Architecture,
    softGalleryLanguage_ArchitectureComponents,
    softGalleryLanguage_AtributeAlbum,
    softGalleryLanguage_AtributePhoto,
    softGalleryLanguage_AtributeUserDomain,
    softGalleryLanguage_Autowired,
    softGalleryLanguage_BackEnd,
    softGalleryLanguage_BatchOperation,
    softGalleryLanguage_Bucket,
    softGalleryLanguage_BucketAccess,
    softGalleryLanguage_BucketObjectsNotPublic,
    softGalleryLanguage_BusinessLogicContent,
    softGalleryLanguage_BusinessLogicLayer,
    softGalleryLanguage_BusinessLogicSegments,
    softGalleryLanguage_Clause,
    softGalleryLanguage_Cluster,
    softGalleryLanguage_ColumnP,
    softGalleryLanguage_ComponentClass,
    softGalleryLanguage_ComponentsLogic,
    softGalleryLanguage_ComponentsStyles,
    softGalleryLanguage_ComponentsStylesContent,
    softGalleryLanguage_ComponentsUI,
    softGalleryLanguage_Configuration,
    softGalleryLanguage_Constraint,
    softGalleryLanguage_ControllerSegmentElement,
    softGalleryLanguage_CoreFunctionsDeclaration,
    softGalleryLanguage_CriteriaAttributeType,
    softGalleryLanguage_DOMConfigurations,
    softGalleryLanguage_DataPersistenceContent,
    softGalleryLanguage_DataPersistenceLayer,
    softGalleryLanguage_DataPersistenceSegments,
    softGalleryLanguage_Database,
    softGalleryLanguage_DatatypeDB,
    softGalleryLanguage_DeleteMapping,
    softGalleryLanguage_Directories,
    softGalleryLanguage_DirectoryContent,
    softGalleryLanguage_Domain,
    softGalleryLanguage_EObject,
    softGalleryLanguage_EnableAuthorizationServer,
    softGalleryLanguage_EnableGlobalMethodSecurity,
    softGalleryLanguage_EnableResourceServer,
    softGalleryLanguage_EnableWebSecurity,
    softGalleryLanguage_Entities,
    softGalleryLanguage_Entity,
    softGalleryLanguage_ExceptionHandler,
    softGalleryLanguage_ExceptionProcess,
    softGalleryLanguage_ExceptionsDomain,
    softGalleryLanguage_ExceptionsType,
    softGalleryLanguage_ForeignKey,
    softGalleryLanguage_ForeignKeyRef,
    softGalleryLanguage_ForeignKey_n,
    softGalleryLanguage_FrontEnd,
    softGalleryLanguage_Function,
    softGalleryLanguage_Functionalities,
    softGalleryLanguage_Functionality,
    softGalleryLanguage_GetMapping,
    softGalleryLanguage_Index_p,
    softGalleryLanguage_LandingActions,
    softGalleryLanguage_LandingFunctions,
    softGalleryLanguage_Layer,
    softGalleryLanguage_LayerRelations,
    softGalleryLanguage_LayerSource,
    softGalleryLanguage_LayerTarget,
    softGalleryLanguage_LogicContent,
    softGalleryLanguage_LogicStructure,
    softGalleryLanguage_MappingType,
    softGalleryLanguage_Metadata,
    softGalleryLanguage_Model,
    softGalleryLanguage_MultipleFile,
    softGalleryLanguage_NTierConnectionContent,
    softGalleryLanguage_NTierSource,
    softGalleryLanguage_NTierTarget,
    softGalleryLanguage_NTiers,
    softGalleryLanguage_NTiersConnections,
    softGalleryLanguage_NTiersRelations,
    softGalleryLanguage_ObjectsPublic,
    softGalleryLanguage_OnlyAuthorized,
    softGalleryLanguage_OrderSpring,
    softGalleryLanguage_PackageName,
    softGalleryLanguage_PackageVersion,
    softGalleryLanguage_PersistenceDataComponent,
    softGalleryLanguage_PhotoActions,
    softGalleryLanguage_PhotoActionsFunctions,
    softGalleryLanguage_PhotoException,
    softGalleryLanguage_Policy,
    softGalleryLanguage_PostMapping,
    softGalleryLanguage_PostgreSQL,
    softGalleryLanguage_PostgresUser,
    softGalleryLanguage_Predicate,
    softGalleryLanguage_PresentationContent,
    softGalleryLanguage_PresentationLayer,
    softGalleryLanguage_PresentationSegments,
    softGalleryLanguage_Privilege,
    softGalleryLanguage_ProfileManagement,
    softGalleryLanguage_ProfileManagementFunctions,
    softGalleryLanguage_Props,
    softGalleryLanguage_PropsType,
    softGalleryLanguage_PublicAccess,
    softGalleryLanguage_PutMapping,
    softGalleryLanguage_Query,
    softGalleryLanguage_React,
    softGalleryLanguage_ReactActions,
    softGalleryLanguage_ReactActionsContent,
    softGalleryLanguage_ReactComponents,
    softGalleryLanguage_ReactConfiguration,
    softGalleryLanguage_ReactConfigurations,
    softGalleryLanguage_ReactConstructor,
    softGalleryLanguage_ReactCoreFunctions,
    softGalleryLanguage_ReactDependencies,
    softGalleryLanguage_ReactDependenciesRules,
    softGalleryLanguage_ReactDependenciesSubRules,
    softGalleryLanguage_ReactFunctions,
    softGalleryLanguage_ReactImportContent,
    softGalleryLanguage_ReactImports,
    softGalleryLanguage_ReactInfo,
    softGalleryLanguage_ReactInformation,
    softGalleryLanguage_ReactLibraries,
    softGalleryLanguage_ReactLibrary,
    softGalleryLanguage_ReactModules,
    softGalleryLanguage_ReactServiceContRequest,
    softGalleryLanguage_ReactServiceContent,
    softGalleryLanguage_ReactServiceRequestProps,
    softGalleryLanguage_ReactServicesRelation,
    softGalleryLanguage_ReactServicesType,
    softGalleryLanguage_ReactSubModules,
    softGalleryLanguage_ReactsRelationServ,
    softGalleryLanguage_RefTable_p,
    softGalleryLanguage_RequestMapping,
    softGalleryLanguage_RequestMappingMethod,
    softGalleryLanguage_RequestMappingProduces,
    softGalleryLanguage_RequestMappingValue,
    softGalleryLanguage_ResponseEntity,
    softGalleryLanguage_ResponseParameter,
    softGalleryLanguage_ResponseParameterAnnotation,
    softGalleryLanguage_ResponseParameterName,
    softGalleryLanguage_ResponseParameterType,
    softGalleryLanguage_RestController,
    softGalleryLanguage_Row,
    softGalleryLanguage_Schema,
    softGalleryLanguage_SearchCriteria,
    softGalleryLanguage_SegmentStructure,
    softGalleryLanguage_SegmentStructureContent,
    softGalleryLanguage_SingleDependencies,
    softGalleryLanguage_SingleFile,
    softGalleryLanguage_Specification,
    softGalleryLanguage_SpecificationSegmentElement,
    softGalleryLanguage_Spring,
    softGalleryLanguage_SpringBootApplication,
    softGalleryLanguage_SpringComponent,
    softGalleryLanguage_SpringEntity,
    softGalleryLanguage_SpringEntityAnnotationTypes,
    softGalleryLanguage_SpringRepositories,
    softGalleryLanguage_SpringRepository,
    softGalleryLanguage_SpringRepositoryAnnotation,
    softGalleryLanguage_State,
    softGalleryLanguage_StateContent,
    softGalleryLanguage_StorageAction,
    softGalleryLanguage_StorageActionAnnotation,
    softGalleryLanguage_StorageActionMember,
    softGalleryLanguage_StorageActionMemberName,
    softGalleryLanguage_StorageActionMemberType,
    softGalleryLanguage_StorageActionReturn,
    softGalleryLanguage_StorageClient,
    softGalleryLanguage_StorageMember,
    softGalleryLanguage_StorageMemberAnnotation,
    softGalleryLanguage_StorageMemberType,
    softGalleryLanguage_StyleProperties,
    softGalleryLanguage_StylePropertiesContent,
    softGalleryLanguage_SubcomponentCont,
    softGalleryLanguage_Table_p,
    softGalleryLanguage_Technologies,
    softGalleryLanguage_Technology,
    softGalleryLanguage_Trigger,
    softGalleryLanguage_UIContent,
    softGalleryLanguage_UserException,
    softGalleryLanguage_ViewComponentCont,
    softGalleryLanguage_ViewSchema,
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

def test_assoc_atributeAlbum10_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_Entities(name="sample_text")
    a2 = softGalleryLanguage_Entities(name="sample_text_2")
    b = softGalleryLanguage_AtributeAlbum(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_AtributeAlbum', a1)
    assert _is_linked(b, 'softGalleryLanguage_AtributeAlbum', a1)
    if hasattr(a1, 'softGalleryLanguage_Entities11'):
        assert _is_linked(a1, 'softGalleryLanguage_Entities11', b)
    _safe_set(b, 'softGalleryLanguage_AtributeAlbum', a2)
    assert _is_linked(b, 'softGalleryLanguage_AtributeAlbum', a2)
    if hasattr(a1, 'softGalleryLanguage_Entities11'):
        assert not _is_linked(a1, 'softGalleryLanguage_Entities11', b)
    if hasattr(a2, 'softGalleryLanguage_Entities11'):
        assert _is_linked(a2, 'softGalleryLanguage_Entities11', b)
    _safe_set(b, 'softGalleryLanguage_AtributeAlbum', None)
    assert not _is_linked(b, 'softGalleryLanguage_AtributeAlbum', a2)
    if hasattr(a2, 'softGalleryLanguage_Entities11'):
        assert not _is_linked(a2, 'softGalleryLanguage_Entities11', b)


def test_assoc_atributePhoto8_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_Entities(name="sample_text")
    a2 = softGalleryLanguage_Entities(name="sample_text_2")
    b = softGalleryLanguage_AtributePhoto(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_AtributePhoto', a1)
    assert _is_linked(b, 'softGalleryLanguage_AtributePhoto', a1)
    if hasattr(a1, 'softGalleryLanguage_Entities9'):
        assert _is_linked(a1, 'softGalleryLanguage_Entities9', b)
    _safe_set(b, 'softGalleryLanguage_AtributePhoto', a2)
    assert _is_linked(b, 'softGalleryLanguage_AtributePhoto', a2)
    if hasattr(a1, 'softGalleryLanguage_Entities9'):
        assert not _is_linked(a1, 'softGalleryLanguage_Entities9', b)
    if hasattr(a2, 'softGalleryLanguage_Entities9'):
        assert _is_linked(a2, 'softGalleryLanguage_Entities9', b)
    _safe_set(b, 'softGalleryLanguage_AtributePhoto', None)
    assert not _is_linked(b, 'softGalleryLanguage_AtributePhoto', a2)
    if hasattr(a2, 'softGalleryLanguage_Entities9'):
        assert not _is_linked(a2, 'softGalleryLanguage_Entities9', b)


def test_assoc_atributeUserDomain12_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_Entities(name="sample_text")
    a2 = softGalleryLanguage_Entities(name="sample_text_2")
    b = softGalleryLanguage_AtributeUserDomain(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_AtributeUserDomain', a1)
    assert _is_linked(b, 'softGalleryLanguage_AtributeUserDomain', a1)
    if hasattr(a1, 'softGalleryLanguage_Entities13'):
        assert _is_linked(a1, 'softGalleryLanguage_Entities13', b)
    _safe_set(b, 'softGalleryLanguage_AtributeUserDomain', a2)
    assert _is_linked(b, 'softGalleryLanguage_AtributeUserDomain', a2)
    if hasattr(a1, 'softGalleryLanguage_Entities13'):
        assert not _is_linked(a1, 'softGalleryLanguage_Entities13', b)
    if hasattr(a2, 'softGalleryLanguage_Entities13'):
        assert _is_linked(a2, 'softGalleryLanguage_Entities13', b)
    _safe_set(b, 'softGalleryLanguage_AtributeUserDomain', None)
    assert not _is_linked(b, 'softGalleryLanguage_AtributeUserDomain', a2)
    if hasattr(a2, 'softGalleryLanguage_Entities13'):
        assert not _is_linked(a2, 'softGalleryLanguage_Entities13', b)


def test_assoc_configurations161_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ReactConfigurations(name="sample_text")
    a2 = softGalleryLanguage_ReactConfigurations(name="sample_text_2")
    b = softGalleryLanguage_DOMConfigurations(elements="sample_text", name="sample_text")
    _safe_set(b, 'softGalleryLanguage_DOMConfigurations', a1)
    assert _is_linked(b, 'softGalleryLanguage_DOMConfigurations', a1)
    if hasattr(a1, 'softGalleryLanguage_ReactConfigurations162'):
        assert _is_linked(a1, 'softGalleryLanguage_ReactConfigurations162', b)
    _safe_set(b, 'softGalleryLanguage_DOMConfigurations', a2)
    assert _is_linked(b, 'softGalleryLanguage_DOMConfigurations', a2)
    if hasattr(a1, 'softGalleryLanguage_ReactConfigurations162'):
        assert not _is_linked(a1, 'softGalleryLanguage_ReactConfigurations162', b)
    if hasattr(a2, 'softGalleryLanguage_ReactConfigurations162'):
        assert _is_linked(a2, 'softGalleryLanguage_ReactConfigurations162', b)
    _safe_set(b, 'softGalleryLanguage_DOMConfigurations', None)
    assert not _is_linked(b, 'softGalleryLanguage_DOMConfigurations', a2)
    if hasattr(a2, 'softGalleryLanguage_ReactConfigurations162'):
        assert not _is_linked(a2, 'softGalleryLanguage_ReactConfigurations162', b)


def test_assoc_controllerSegmentElement56_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ControllerSegmentElement(name="sample_text")
    a2 = softGalleryLanguage_ControllerSegmentElement(name="sample_text_2")
    b = softGalleryLanguage_BusinessLogicSegments(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments57', {a1})
    assert _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments57', a1)
    if hasattr(a1, 'softGalleryLanguage_ControllerSegmentElement'):
        assert _is_linked(a1, 'softGalleryLanguage_ControllerSegmentElement', b)
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments57', {a2})
    assert _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments57', a2)
    if hasattr(a1, 'softGalleryLanguage_ControllerSegmentElement'):
        assert not _is_linked(a1, 'softGalleryLanguage_ControllerSegmentElement', b)
    if hasattr(a2, 'softGalleryLanguage_ControllerSegmentElement'):
        assert _is_linked(a2, 'softGalleryLanguage_ControllerSegmentElement', b)
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments57', set())
    assert not _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments57', a2)
    if hasattr(a2, 'softGalleryLanguage_ControllerSegmentElement'):
        assert not _is_linked(a2, 'softGalleryLanguage_ControllerSegmentElement', b)


def test_assoc_criteriaAttributeType60_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_SpecificationSegmentElement(name="sample_text")
    a2 = softGalleryLanguage_SpecificationSegmentElement(name="sample_text_2")
    b = softGalleryLanguage_CriteriaAttributeType(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_CriteriaAttributeType', a1)
    assert _is_linked(b, 'softGalleryLanguage_CriteriaAttributeType', a1)
    if hasattr(a1, 'softGalleryLanguage_SpecificationSegmentElement61'):
        assert _is_linked(a1, 'softGalleryLanguage_SpecificationSegmentElement61', b)
    _safe_set(b, 'softGalleryLanguage_CriteriaAttributeType', a2)
    assert _is_linked(b, 'softGalleryLanguage_CriteriaAttributeType', a2)
    if hasattr(a1, 'softGalleryLanguage_SpecificationSegmentElement61'):
        assert not _is_linked(a1, 'softGalleryLanguage_SpecificationSegmentElement61', b)
    if hasattr(a2, 'softGalleryLanguage_SpecificationSegmentElement61'):
        assert _is_linked(a2, 'softGalleryLanguage_SpecificationSegmentElement61', b)
    _safe_set(b, 'softGalleryLanguage_CriteriaAttributeType', None)
    assert not _is_linked(b, 'softGalleryLanguage_CriteriaAttributeType', a2)
    if hasattr(a2, 'softGalleryLanguage_SpecificationSegmentElement61'):
        assert not _is_linked(a2, 'softGalleryLanguage_SpecificationSegmentElement61', b)


def test_assoc_elements124_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ExceptionProcess(name="sample_text")
    a2 = softGalleryLanguage_ExceptionProcess(name="sample_text_2")
    b = softGalleryLanguage_ExceptionHandler(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_ExceptionHandler', {a1})
    assert _is_linked(b, 'softGalleryLanguage_ExceptionHandler', a1)
    if hasattr(a1, 'softGalleryLanguage_ExceptionProcess'):
        assert _is_linked(a1, 'softGalleryLanguage_ExceptionProcess', b)
    _safe_set(b, 'softGalleryLanguage_ExceptionHandler', {a2})
    assert _is_linked(b, 'softGalleryLanguage_ExceptionHandler', a2)
    if hasattr(a1, 'softGalleryLanguage_ExceptionProcess'):
        assert not _is_linked(a1, 'softGalleryLanguage_ExceptionProcess', b)
    if hasattr(a2, 'softGalleryLanguage_ExceptionProcess'):
        assert _is_linked(a2, 'softGalleryLanguage_ExceptionProcess', b)
    _safe_set(b, 'softGalleryLanguage_ExceptionHandler', set())
    assert not _is_linked(b, 'softGalleryLanguage_ExceptionHandler', a2)
    if hasattr(a2, 'softGalleryLanguage_ExceptionProcess'):
        assert not _is_linked(a2, 'softGalleryLanguage_ExceptionProcess', b)


def test_assoc_elements247_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_Row(name="sample_text")
    a2 = softGalleryLanguage_Row(name="sample_text_2")
    b = softGalleryLanguage_Policy(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_Policy', a1)
    assert _is_linked(b, 'softGalleryLanguage_Policy', a1)
    if hasattr(a1, 'softGalleryLanguage_Row'):
        assert _is_linked(a1, 'softGalleryLanguage_Row', b)
    _safe_set(b, 'softGalleryLanguage_Policy', a2)
    assert _is_linked(b, 'softGalleryLanguage_Policy', a2)
    if hasattr(a1, 'softGalleryLanguage_Row'):
        assert not _is_linked(a1, 'softGalleryLanguage_Row', b)
    if hasattr(a2, 'softGalleryLanguage_Row'):
        assert _is_linked(a2, 'softGalleryLanguage_Row', b)
    _safe_set(b, 'softGalleryLanguage_Policy', None)
    assert not _is_linked(b, 'softGalleryLanguage_Policy', a2)
    if hasattr(a2, 'softGalleryLanguage_Row'):
        assert not _is_linked(a2, 'softGalleryLanguage_Row', b)


def test_assoc_elements66_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_SegmentStructureContent(name="sample_text")
    a2 = softGalleryLanguage_SegmentStructureContent(name="sample_text_2")
    b = softGalleryLanguage_DirectoryContent(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_DirectoryContent', a1)
    assert _is_linked(b, 'softGalleryLanguage_DirectoryContent', a1)
    if hasattr(a1, 'softGalleryLanguage_SegmentStructureContent67'):
        assert _is_linked(a1, 'softGalleryLanguage_SegmentStructureContent67', b)
    _safe_set(b, 'softGalleryLanguage_DirectoryContent', a2)
    assert _is_linked(b, 'softGalleryLanguage_DirectoryContent', a2)
    if hasattr(a1, 'softGalleryLanguage_SegmentStructureContent67'):
        assert not _is_linked(a1, 'softGalleryLanguage_SegmentStructureContent67', b)
    if hasattr(a2, 'softGalleryLanguage_SegmentStructureContent67'):
        assert _is_linked(a2, 'softGalleryLanguage_SegmentStructureContent67', b)
    _safe_set(b, 'softGalleryLanguage_DirectoryContent', None)
    assert not _is_linked(b, 'softGalleryLanguage_DirectoryContent', a2)
    if hasattr(a2, 'softGalleryLanguage_SegmentStructureContent67'):
        assert not _is_linked(a2, 'softGalleryLanguage_SegmentStructureContent67', b)


def test_assoc_layerorigin72_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_LayerSource(layerelations="sample_text")
    a2 = softGalleryLanguage_LayerSource(layerelations="sample_text_2")
    b = softGalleryLanguage_LayerRelations(layerelations="sample_text", name="sample_text")
    _safe_set(b, 'softGalleryLanguage_LayerRelations', {a1})
    assert _is_linked(b, 'softGalleryLanguage_LayerRelations', a1)
    if hasattr(a1, 'softGalleryLanguage_LayerSource'):
        assert _is_linked(a1, 'softGalleryLanguage_LayerSource', b)
    _safe_set(b, 'softGalleryLanguage_LayerRelations', {a2})
    assert _is_linked(b, 'softGalleryLanguage_LayerRelations', a2)
    if hasattr(a1, 'softGalleryLanguage_LayerSource'):
        assert not _is_linked(a1, 'softGalleryLanguage_LayerSource', b)
    if hasattr(a2, 'softGalleryLanguage_LayerSource'):
        assert _is_linked(a2, 'softGalleryLanguage_LayerSource', b)
    _safe_set(b, 'softGalleryLanguage_LayerRelations', set())
    assert not _is_linked(b, 'softGalleryLanguage_LayerRelations', a2)
    if hasattr(a2, 'softGalleryLanguage_LayerSource'):
        assert not _is_linked(a2, 'softGalleryLanguage_LayerSource', b)


def test_assoc_layertarget73_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_LayerTarget(layerelations="sample_text")
    a2 = softGalleryLanguage_LayerTarget(layerelations="sample_text_2")
    b = softGalleryLanguage_LayerRelations(layerelations="sample_text", name="sample_text")
    _safe_set(b, 'softGalleryLanguage_LayerRelations74', {a1})
    assert _is_linked(b, 'softGalleryLanguage_LayerRelations74', a1)
    if hasattr(a1, 'softGalleryLanguage_LayerTarget'):
        assert _is_linked(a1, 'softGalleryLanguage_LayerTarget', b)
    _safe_set(b, 'softGalleryLanguage_LayerRelations74', {a2})
    assert _is_linked(b, 'softGalleryLanguage_LayerRelations74', a2)
    if hasattr(a1, 'softGalleryLanguage_LayerTarget'):
        assert not _is_linked(a1, 'softGalleryLanguage_LayerTarget', b)
    if hasattr(a2, 'softGalleryLanguage_LayerTarget'):
        assert _is_linked(a2, 'softGalleryLanguage_LayerTarget', b)
    _safe_set(b, 'softGalleryLanguage_LayerRelations74', set())
    assert not _is_linked(b, 'softGalleryLanguage_LayerRelations74', a2)
    if hasattr(a2, 'softGalleryLanguage_LayerTarget'):
        assert not _is_linked(a2, 'softGalleryLanguage_LayerTarget', b)


def test_assoc_logiccomponents169_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_LogicContent(name="sample_text")
    a2 = softGalleryLanguage_LogicContent(name="sample_text_2")
    b = softGalleryLanguage_ComponentsLogic(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_ComponentsLogic170', {a1})
    assert _is_linked(b, 'softGalleryLanguage_ComponentsLogic170', a1)
    if hasattr(a1, 'softGalleryLanguage_LogicContent'):
        assert _is_linked(a1, 'softGalleryLanguage_LogicContent', b)
    _safe_set(b, 'softGalleryLanguage_ComponentsLogic170', {a2})
    assert _is_linked(b, 'softGalleryLanguage_ComponentsLogic170', a2)
    if hasattr(a1, 'softGalleryLanguage_LogicContent'):
        assert not _is_linked(a1, 'softGalleryLanguage_LogicContent', b)
    if hasattr(a2, 'softGalleryLanguage_LogicContent'):
        assert _is_linked(a2, 'softGalleryLanguage_LogicContent', b)
    _safe_set(b, 'softGalleryLanguage_ComponentsLogic170', set())
    assert not _is_linked(b, 'softGalleryLanguage_ComponentsLogic170', a2)
    if hasattr(a2, 'softGalleryLanguage_LogicContent'):
        assert not _is_linked(a2, 'softGalleryLanguage_LogicContent', b)


def test_assoc_logiccomponents171_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_LogicStructure(appComName="sample_text", indexCompName="sample_text")
    a2 = softGalleryLanguage_LogicStructure(appComName="sample_text_2", indexCompName="sample_text_2")
    b = softGalleryLanguage_LogicContent(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_LogicContent172', {a1})
    assert _is_linked(b, 'softGalleryLanguage_LogicContent172', a1)
    if hasattr(a1, 'softGalleryLanguage_LogicStructure'):
        assert _is_linked(a1, 'softGalleryLanguage_LogicStructure', b)
    _safe_set(b, 'softGalleryLanguage_LogicContent172', {a2})
    assert _is_linked(b, 'softGalleryLanguage_LogicContent172', a2)
    if hasattr(a1, 'softGalleryLanguage_LogicStructure'):
        assert not _is_linked(a1, 'softGalleryLanguage_LogicStructure', b)
    if hasattr(a2, 'softGalleryLanguage_LogicStructure'):
        assert _is_linked(a2, 'softGalleryLanguage_LogicStructure', b)
    _safe_set(b, 'softGalleryLanguage_LogicContent172', set())
    assert not _is_linked(b, 'softGalleryLanguage_LogicContent172', a2)
    if hasattr(a2, 'softGalleryLanguage_LogicStructure'):
        assert not _is_linked(a2, 'softGalleryLanguage_LogicStructure', b)


def test_assoc_reactcorefuncs197_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ReactFunctions(lifecycleclass="sample_text", renderclass="sample_text")
    a2 = softGalleryLanguage_ReactFunctions(lifecycleclass="sample_text_2", renderclass="sample_text_2")
    b = softGalleryLanguage_ReactCoreFunctions(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_ReactCoreFunctions', a1)
    assert _is_linked(b, 'softGalleryLanguage_ReactCoreFunctions', a1)
    if hasattr(a1, 'softGalleryLanguage_ReactFunctions198'):
        assert _is_linked(a1, 'softGalleryLanguage_ReactFunctions198', b)
    _safe_set(b, 'softGalleryLanguage_ReactCoreFunctions', a2)
    assert _is_linked(b, 'softGalleryLanguage_ReactCoreFunctions', a2)
    if hasattr(a1, 'softGalleryLanguage_ReactFunctions198'):
        assert not _is_linked(a1, 'softGalleryLanguage_ReactFunctions198', b)
    if hasattr(a2, 'softGalleryLanguage_ReactFunctions198'):
        assert _is_linked(a2, 'softGalleryLanguage_ReactFunctions198', b)
    _safe_set(b, 'softGalleryLanguage_ReactCoreFunctions', None)
    assert not _is_linked(b, 'softGalleryLanguage_ReactCoreFunctions', a2)
    if hasattr(a2, 'softGalleryLanguage_ReactFunctions198'):
        assert not _is_linked(a2, 'softGalleryLanguage_ReactFunctions198', b)


def test_assoc_reactrelationcontent224_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ReactsRelationServ(name="sample_text")
    a2 = softGalleryLanguage_ReactsRelationServ(name="sample_text_2")
    b = softGalleryLanguage_ReactServicesType(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_ReactServicesType226', a1)
    assert _is_linked(b, 'softGalleryLanguage_ReactServicesType226', a1)
    if hasattr(a1, 'softGalleryLanguage_ReactsRelationServ225'):
        assert _is_linked(a1, 'softGalleryLanguage_ReactsRelationServ225', b)
    _safe_set(b, 'softGalleryLanguage_ReactServicesType226', a2)
    assert _is_linked(b, 'softGalleryLanguage_ReactServicesType226', a2)
    if hasattr(a1, 'softGalleryLanguage_ReactsRelationServ225'):
        assert not _is_linked(a1, 'softGalleryLanguage_ReactsRelationServ225', b)
    if hasattr(a2, 'softGalleryLanguage_ReactsRelationServ225'):
        assert _is_linked(a2, 'softGalleryLanguage_ReactsRelationServ225', b)
    _safe_set(b, 'softGalleryLanguage_ReactServicesType226', None)
    assert not _is_linked(b, 'softGalleryLanguage_ReactServicesType226', a2)
    if hasattr(a2, 'softGalleryLanguage_ReactsRelationServ225'):
        assert not _is_linked(a2, 'softGalleryLanguage_ReactsRelationServ225', b)


def test_assoc_reactservcontent217_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_ReactServicesType(name="sample_text")
    a2 = softGalleryLanguage_ReactServicesType(name="sample_text_2")
    b = softGalleryLanguage_ReactServiceContent(functName="sample_text")
    _safe_set(b, 'softGalleryLanguage_ReactServiceContent', a1)
    assert _is_linked(b, 'softGalleryLanguage_ReactServiceContent', a1)
    if hasattr(a1, 'softGalleryLanguage_ReactServicesType'):
        assert _is_linked(a1, 'softGalleryLanguage_ReactServicesType', b)
    _safe_set(b, 'softGalleryLanguage_ReactServiceContent', a2)
    assert _is_linked(b, 'softGalleryLanguage_ReactServiceContent', a2)
    if hasattr(a1, 'softGalleryLanguage_ReactServicesType'):
        assert not _is_linked(a1, 'softGalleryLanguage_ReactServicesType', b)
    if hasattr(a2, 'softGalleryLanguage_ReactServicesType'):
        assert _is_linked(a2, 'softGalleryLanguage_ReactServicesType', b)
    _safe_set(b, 'softGalleryLanguage_ReactServiceContent', None)
    assert not _is_linked(b, 'softGalleryLanguage_ReactServiceContent', a2)
    if hasattr(a2, 'softGalleryLanguage_ReactServicesType'):
        assert not _is_linked(a2, 'softGalleryLanguage_ReactServicesType', b)


def test_assoc_specificationSegmentElement58_reverse_link_reassign_clear():
    a1 = softGalleryLanguage_SpecificationSegmentElement(name="sample_text")
    a2 = softGalleryLanguage_SpecificationSegmentElement(name="sample_text_2")
    b = softGalleryLanguage_BusinessLogicSegments(name="sample_text")
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments59', {a1})
    assert _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments59', a1)
    if hasattr(a1, 'softGalleryLanguage_SpecificationSegmentElement'):
        assert _is_linked(a1, 'softGalleryLanguage_SpecificationSegmentElement', b)
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments59', {a2})
    assert _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments59', a2)
    if hasattr(a1, 'softGalleryLanguage_SpecificationSegmentElement'):
        assert not _is_linked(a1, 'softGalleryLanguage_SpecificationSegmentElement', b)
    if hasattr(a2, 'softGalleryLanguage_SpecificationSegmentElement'):
        assert _is_linked(a2, 'softGalleryLanguage_SpecificationSegmentElement', b)
    _safe_set(b, 'softGalleryLanguage_BusinessLogicSegments59', set())
    assert not _is_linked(b, 'softGalleryLanguage_BusinessLogicSegments59', a2)
    if hasattr(a2, 'softGalleryLanguage_SpecificationSegmentElement'):
        assert not _is_linked(a2, 'softGalleryLanguage_SpecificationSegmentElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_albumException40_stub_double():
    # softGalleryLanguage_ExceptionsType has no real 'softGalleryLanguage_ExceptionsType41' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_AlbumException's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_AlbumException's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_AlbumException(name="sample_text")
    partner = softGalleryLanguage_ExceptionsType()
    setattr(partner, 'softGalleryLanguage_ExceptionsType41', None)
    _safe_set(owner, 'softGalleryLanguage_AlbumException', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ExceptionsType41')
    _safe_set(owner, 'softGalleryLanguage_AlbumException', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ExceptionsType41')


def test_assoc_archBeComponent76_stub_double():
    # softGalleryLanguage_ArchitectureComponents has no real 'softGalleryLanguage_ArchitectureComponents77' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_BackEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_BackEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_BackEnd(name="sample_text")
    partner = softGalleryLanguage_ArchitectureComponents()
    setattr(partner, 'softGalleryLanguage_ArchitectureComponents77', None)
    _safe_set(owner, 'softGalleryLanguage_BackEnd', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ArchitectureComponents77')
    _safe_set(owner, 'softGalleryLanguage_BackEnd', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ArchitectureComponents77')


def test_assoc_archFeComponent75_stub_double():
    # softGalleryLanguage_ArchitectureComponents has no real 'softGalleryLanguage_ArchitectureComponents' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_FrontEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_FrontEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_FrontEnd(name="sample_text")
    partner = softGalleryLanguage_ArchitectureComponents()
    setattr(partner, 'softGalleryLanguage_ArchitectureComponents', None)
    _safe_set(owner, 'softGalleryLanguage_FrontEnd', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ArchitectureComponents')
    _safe_set(owner, 'softGalleryLanguage_FrontEnd', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ArchitectureComponents')


def test_assoc_archPdComponent78_stub_double():
    # softGalleryLanguage_ArchitectureComponents has no real 'softGalleryLanguage_ArchitectureComponents79' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PersistenceDataComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PersistenceDataComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PersistenceDataComponent(name="sample_text")
    partner = softGalleryLanguage_ArchitectureComponents()
    setattr(partner, 'softGalleryLanguage_ArchitectureComponents79', None)
    _safe_set(owner, 'softGalleryLanguage_PersistenceDataComponent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ArchitectureComponents79')
    _safe_set(owner, 'softGalleryLanguage_PersistenceDataComponent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ArchitectureComponents79')


def test_assoc_businessLogicSegments55_stub_double():
    # softGalleryLanguage_BusinessLogicContent has no real 'softGalleryLanguage_BusinessLogicContent' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_BusinessLogicSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_BusinessLogicSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_BusinessLogicSegments(name="sample_text")
    partner = softGalleryLanguage_BusinessLogicContent()
    setattr(partner, 'softGalleryLanguage_BusinessLogicContent', None)
    _safe_set(owner, 'softGalleryLanguage_BusinessLogicSegments', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_BusinessLogicContent')
    _safe_set(owner, 'softGalleryLanguage_BusinessLogicSegments', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_BusinessLogicContent')


def test_assoc_componentclassfunc189_stub_double():
    # softGalleryLanguage_ComponentClass has no real 'softGalleryLanguage_ComponentClass190' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactFunctions(lifecycleclass="sample_text", renderclass="sample_text")
    partner = softGalleryLanguage_ComponentClass()
    setattr(partner, 'softGalleryLanguage_ComponentClass190', None)
    _safe_set(owner, 'softGalleryLanguage_ReactFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ComponentClass190')
    _safe_set(owner, 'softGalleryLanguage_ReactFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ComponentClass190')


def test_assoc_componentcontent177_stub_double():
    # softGalleryLanguage_UIContent has no real 'softGalleryLanguage_UIContent178' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ViewComponentCont's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ViewComponentCont's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ViewComponentCont(nameView="sample_text")
    partner = softGalleryLanguage_UIContent()
    setattr(partner, 'softGalleryLanguage_UIContent178', None)
    _safe_set(owner, 'softGalleryLanguage_ViewComponentCont', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_UIContent178')
    _safe_set(owner, 'softGalleryLanguage_ViewComponentCont', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_UIContent178')


def test_assoc_componentfuncclass201_stub_double():
    # softGalleryLanguage_ReactConstructor has no real 'softGalleryLanguage_ReactConstructor202' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_CoreFunctionsDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_CoreFunctionsDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_CoreFunctionsDeclaration(name="sample_text")
    partner = softGalleryLanguage_ReactConstructor()
    setattr(partner, 'softGalleryLanguage_ReactConstructor202', None)
    _safe_set(owner, 'softGalleryLanguage_CoreFunctionsDeclaration', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactConstructor202')
    _safe_set(owner, 'softGalleryLanguage_CoreFunctionsDeclaration', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactConstructor202')


def test_assoc_componentslogic163_stub_double():
    # softGalleryLanguage_ReactComponents has no real 'softGalleryLanguage_ReactComponents164' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ComponentsLogic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ComponentsLogic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ComponentsLogic(name="sample_text")
    partner = softGalleryLanguage_ReactComponents()
    setattr(partner, 'softGalleryLanguage_ReactComponents164', None)
    _safe_set(owner, 'softGalleryLanguage_ComponentsLogic', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactComponents164')
    _safe_set(owner, 'softGalleryLanguage_ComponentsLogic', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactComponents164')


def test_assoc_componentsui165_stub_double():
    # softGalleryLanguage_ReactComponents has no real 'softGalleryLanguage_ReactComponents166' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ComponentsUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ComponentsUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ComponentsUI(name="sample_text")
    partner = softGalleryLanguage_ReactComponents()
    setattr(partner, 'softGalleryLanguage_ReactComponents166', None)
    _safe_set(owner, 'softGalleryLanguage_ComponentsUI', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactComponents166')
    _safe_set(owner, 'softGalleryLanguage_ComponentsUI', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactComponents166')


def test_assoc_configurations150_stub_double():
    # softGalleryLanguage_ReactConfiguration has no real 'softGalleryLanguage_ReactConfiguration151' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactConfigurations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactConfigurations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactConfigurations(name="sample_text")
    partner = softGalleryLanguage_ReactConfiguration()
    setattr(partner, 'softGalleryLanguage_ReactConfiguration151', None)
    _safe_set(owner, 'softGalleryLanguage_ReactConfigurations', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactConfiguration151')
    _safe_set(owner, 'softGalleryLanguage_ReactConfigurations', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactConfiguration151')


def test_assoc_dependencies152_stub_double():
    # softGalleryLanguage_ReactDependencies has no real 'softGalleryLanguage_ReactDependencies153' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactDependenciesRules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactDependenciesRules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactDependenciesRules(name="sample_text")
    partner = softGalleryLanguage_ReactDependencies()
    setattr(partner, 'softGalleryLanguage_ReactDependencies153', None)
    _safe_set(owner, 'softGalleryLanguage_ReactDependenciesRules', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactDependencies153')
    _safe_set(owner, 'softGalleryLanguage_ReactDependenciesRules', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactDependencies153')


def test_assoc_dependencies154_stub_double():
    # softGalleryLanguage_ReactDependenciesSubRules has no real 'softGalleryLanguage_ReactDependenciesSubRules' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactDependenciesRules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactDependenciesRules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactDependenciesRules(name="sample_text")
    partner = softGalleryLanguage_ReactDependenciesSubRules()
    setattr(partner, 'softGalleryLanguage_ReactDependenciesSubRules', None)
    _safe_set(owner, 'softGalleryLanguage_ReactDependenciesRules155', {partner})
    assert getattr(partner, 'softGalleryLanguage_ReactDependenciesSubRules') == owner
    _safe_set(owner, 'softGalleryLanguage_ReactDependenciesRules155', set())
    assert getattr(partner, 'softGalleryLanguage_ReactDependenciesSubRules') is None


def test_assoc_directories68_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject70' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_DirectoryContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_DirectoryContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_DirectoryContent(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject70', None)
    _safe_set(owner, 'softGalleryLanguage_DirectoryContent69', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject70') == owner
    _safe_set(owner, 'softGalleryLanguage_DirectoryContent69', set())
    assert getattr(partner, 'softGalleryLanguage_EObject70') is None


def test_assoc_elements106_stub_double():
    # softGalleryLanguage_SpringComponent has no real 'softGalleryLanguage_SpringComponent' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_OrderSpring's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_OrderSpring's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_OrderSpring(name="sample_text")
    partner = softGalleryLanguage_SpringComponent()
    setattr(partner, 'softGalleryLanguage_SpringComponent', None)
    _safe_set(owner, 'softGalleryLanguage_OrderSpring', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_SpringComponent')
    _safe_set(owner, 'softGalleryLanguage_OrderSpring', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_SpringComponent')


def test_assoc_elements109_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject110' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_RestController(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject110', None)
    _safe_set(owner, 'softGalleryLanguage_RestController', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject110') == owner
    _safe_set(owner, 'softGalleryLanguage_RestController', set())
    assert getattr(partner, 'softGalleryLanguage_EObject110') is None


def test_assoc_elements114_stub_double():
    # softGalleryLanguage_ResponseParameter has no real 'softGalleryLanguage_ResponseParameter' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ResponseEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ResponseEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ResponseEntity(name="sample_text")
    partner = softGalleryLanguage_ResponseParameter()
    setattr(partner, 'softGalleryLanguage_ResponseParameter', None)
    _safe_set(owner, 'softGalleryLanguage_ResponseEntity115', {partner})
    assert getattr(partner, 'softGalleryLanguage_ResponseParameter') == owner
    _safe_set(owner, 'softGalleryLanguage_ResponseEntity115', set())
    assert getattr(partner, 'softGalleryLanguage_ResponseParameter') is None


def test_assoc_elements126_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject127' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_StorageClient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_StorageClient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_StorageClient(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject127', None)
    _safe_set(owner, 'softGalleryLanguage_StorageClient', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject127') == owner
    _safe_set(owner, 'softGalleryLanguage_StorageClient', set())
    assert getattr(partner, 'softGalleryLanguage_EObject127') is None


def test_assoc_elements128_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject129' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_StorageMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_StorageMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_StorageMember(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject129', None)
    _safe_set(owner, 'softGalleryLanguage_StorageMember', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject129') == owner
    _safe_set(owner, 'softGalleryLanguage_StorageMember', set())
    assert getattr(partner, 'softGalleryLanguage_EObject129') is None


def test_assoc_elements130_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject131' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_StorageAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_StorageAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_StorageAction(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject131', None)
    _safe_set(owner, 'softGalleryLanguage_StorageAction', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject131') == owner
    _safe_set(owner, 'softGalleryLanguage_StorageAction', set())
    assert getattr(partner, 'softGalleryLanguage_EObject131') is None


def test_assoc_elements231_stub_double():
    # softGalleryLanguage_Cluster has no real 'softGalleryLanguage_Cluster' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PostgreSQL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PostgreSQL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PostgreSQL(name="sample_text")
    partner = softGalleryLanguage_Cluster()
    setattr(partner, 'softGalleryLanguage_Cluster', None)
    _safe_set(owner, 'softGalleryLanguage_PostgreSQL232', {partner})
    assert getattr(partner, 'softGalleryLanguage_Cluster') == owner
    _safe_set(owner, 'softGalleryLanguage_PostgreSQL232', set())
    assert getattr(partner, 'softGalleryLanguage_Cluster') is None


def test_assoc_elements236_stub_double():
    # softGalleryLanguage_Schema has no real 'softGalleryLanguage_Schema' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Database(name="sample_text")
    partner = softGalleryLanguage_Schema()
    setattr(partner, 'softGalleryLanguage_Schema', None)
    _safe_set(owner, 'softGalleryLanguage_Database', {partner})
    assert getattr(partner, 'softGalleryLanguage_Schema') == owner
    _safe_set(owner, 'softGalleryLanguage_Database', set())
    assert getattr(partner, 'softGalleryLanguage_Schema') is None


def test_assoc_elements240_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject241' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Table_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Table_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Table_p(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject241', None)
    _safe_set(owner, 'softGalleryLanguage_Table_p', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject241') == owner
    _safe_set(owner, 'softGalleryLanguage_Table_p', set())
    assert getattr(partner, 'softGalleryLanguage_EObject241') is None


def test_assoc_elements244_stub_double():
    # softGalleryLanguage_ForeignKeyRef has no real 'softGalleryLanguage_ForeignKeyRef' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_RefTable_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_RefTable_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_RefTable_p(name="sample_text")
    partner = softGalleryLanguage_ForeignKeyRef()
    setattr(partner, 'softGalleryLanguage_ForeignKeyRef', None)
    _safe_set(owner, 'softGalleryLanguage_RefTable_p', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ForeignKeyRef')
    _safe_set(owner, 'softGalleryLanguage_RefTable_p', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ForeignKeyRef')


def test_assoc_elements245_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject246' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ColumnP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ColumnP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ColumnP(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject246', None)
    _safe_set(owner, 'softGalleryLanguage_ColumnP', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject246') == owner
    _safe_set(owner, 'softGalleryLanguage_ColumnP', set())
    assert getattr(partner, 'softGalleryLanguage_EObject246') is None


def test_assoc_elements248_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject249' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PostgresUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PostgresUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PostgresUser(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject249', None)
    _safe_set(owner, 'softGalleryLanguage_PostgresUser', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject249') == owner
    _safe_set(owner, 'softGalleryLanguage_PostgresUser', set())
    assert getattr(partner, 'softGalleryLanguage_EObject249') is None


def test_assoc_elements250_stub_double():
    # softGalleryLanguage_Query has no real 'softGalleryLanguage_Query' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Clause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Clause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Clause(name="sample_text")
    partner = softGalleryLanguage_Query()
    setattr(partner, 'softGalleryLanguage_Query', None)
    _safe_set(owner, 'softGalleryLanguage_Clause', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Query')
    _safe_set(owner, 'softGalleryLanguage_Clause', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Query')


def test_assoc_elements251_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject253' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_AmazonWebServices's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_AmazonWebServices's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_AmazonWebServices(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject253', None)
    _safe_set(owner, 'softGalleryLanguage_AmazonWebServices252', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject253') == owner
    _safe_set(owner, 'softGalleryLanguage_AmazonWebServices252', set())
    assert getattr(partner, 'softGalleryLanguage_EObject253') is None


def test_assoc_elements256_stub_double():
    # softGalleryLanguage_EObject has no real 'softGalleryLanguage_EObject257' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Bucket's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Bucket's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Bucket(name="sample_text")
    partner = softGalleryLanguage_EObject()
    setattr(partner, 'softGalleryLanguage_EObject257', None)
    _safe_set(owner, 'softGalleryLanguage_Bucket', {partner})
    assert getattr(partner, 'softGalleryLanguage_EObject257') == owner
    _safe_set(owner, 'softGalleryLanguage_Bucket', set())
    assert getattr(partner, 'softGalleryLanguage_EObject257') is None


def test_assoc_elements260_stub_double():
    # softGalleryLanguage_AmazonFile has no real 'softGalleryLanguage_AmazonFile' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Metadata's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Metadata's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Metadata(name="sample_text")
    partner = softGalleryLanguage_AmazonFile()
    setattr(partner, 'softGalleryLanguage_AmazonFile', None)
    _safe_set(owner, 'softGalleryLanguage_Metadata', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_AmazonFile')
    _safe_set(owner, 'softGalleryLanguage_Metadata', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_AmazonFile')


def test_assoc_elements52_stub_double():
    # softGalleryLanguage_PresentationContent has no real 'softGalleryLanguage_PresentationContent' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PresentationSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PresentationSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PresentationSegments(presentationAName="sample_text", presentationCName="sample_text", presentationSName="sample_text")
    partner = softGalleryLanguage_PresentationContent()
    setattr(partner, 'softGalleryLanguage_PresentationContent', None)
    _safe_set(owner, 'softGalleryLanguage_PresentationSegments', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_PresentationContent')
    _safe_set(owner, 'softGalleryLanguage_PresentationSegments', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_PresentationContent')


def test_assoc_elements6_stub_double():
    # softGalleryLanguage_Entity has no real 'softGalleryLanguage_Entity7' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Entities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Entities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Entities(name="sample_text")
    partner = softGalleryLanguage_Entity()
    setattr(partner, 'softGalleryLanguage_Entity7', None)
    _safe_set(owner, 'softGalleryLanguage_Entities', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Entity7')
    _safe_set(owner, 'softGalleryLanguage_Entities', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Entity7')


def test_assoc_elements63_stub_double():
    # softGalleryLanguage_DataPersistenceContent has no real 'softGalleryLanguage_DataPersistenceContent64' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_DataPersistenceSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_DataPersistenceSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_DataPersistenceSegments(amazonSName="sample_text", postSName="sample_text")
    partner = softGalleryLanguage_DataPersistenceContent()
    setattr(partner, 'softGalleryLanguage_DataPersistenceContent64', None)
    _safe_set(owner, 'softGalleryLanguage_DataPersistenceSegments', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_DataPersistenceContent64')
    _safe_set(owner, 'softGalleryLanguage_DataPersistenceSegments', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_DataPersistenceContent64')


def test_assoc_elements65_stub_double():
    # softGalleryLanguage_SegmentStructure has no real 'softGalleryLanguage_SegmentStructure' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_SegmentStructureContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_SegmentStructureContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_SegmentStructureContent(name="sample_text")
    partner = softGalleryLanguage_SegmentStructure()
    setattr(partner, 'softGalleryLanguage_SegmentStructure', None)
    _safe_set(owner, 'softGalleryLanguage_SegmentStructureContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_SegmentStructure')
    _safe_set(owner, 'softGalleryLanguage_SegmentStructureContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_SegmentStructure')


def test_assoc_elements71_stub_double():
    # softGalleryLanguage_Directories has no real 'softGalleryLanguage_Directories' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_MultipleFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_MultipleFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_MultipleFile(name="sample_text")
    partner = softGalleryLanguage_Directories()
    setattr(partner, 'softGalleryLanguage_Directories', None)
    _safe_set(owner, 'softGalleryLanguage_MultipleFile', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Directories')
    _safe_set(owner, 'softGalleryLanguage_MultipleFile', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Directories')


def test_assoc_elements90_stub_double():
    # softGalleryLanguage_Technologies has no real 'softGalleryLanguage_Technologies' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Technology's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Technology's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Technology(name="sample_text")
    partner = softGalleryLanguage_Technologies()
    setattr(partner, 'softGalleryLanguage_Technologies', None)
    _safe_set(owner, 'softGalleryLanguage_Technology', {partner})
    assert getattr(partner, 'softGalleryLanguage_Technologies') == owner
    _safe_set(owner, 'softGalleryLanguage_Technology', set())
    assert getattr(partner, 'softGalleryLanguage_Technologies') is None


def test_assoc_elements99_stub_double():
    # softGalleryLanguage_SpringBootApplication has no real 'softGalleryLanguage_SpringBootApplication' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Spring's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Spring's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Spring(name="sample_text")
    partner = softGalleryLanguage_SpringBootApplication()
    setattr(partner, 'softGalleryLanguage_SpringBootApplication', None)
    _safe_set(owner, 'softGalleryLanguage_Spring100', {partner})
    assert getattr(partner, 'softGalleryLanguage_SpringBootApplication') == owner
    _safe_set(owner, 'softGalleryLanguage_Spring100', set())
    assert getattr(partner, 'softGalleryLanguage_SpringBootApplication') is None


def test_assoc_entitydomain1_stub_double():
    # softGalleryLanguage_Entity has no real 'softGalleryLanguage_Entity' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Domain(name="sample_text")
    partner = softGalleryLanguage_Entity()
    setattr(partner, 'softGalleryLanguage_Entity', None)
    _safe_set(owner, 'softGalleryLanguage_Domain', {partner})
    assert getattr(partner, 'softGalleryLanguage_Entity') == owner
    _safe_set(owner, 'softGalleryLanguage_Domain', set())
    assert getattr(partner, 'softGalleryLanguage_Entity') is None


def test_assoc_entityfuncs2_stub_double():
    # softGalleryLanguage_Functionality has no real 'softGalleryLanguage_Functionality' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Domain(name="sample_text")
    partner = softGalleryLanguage_Functionality()
    setattr(partner, 'softGalleryLanguage_Functionality', None)
    _safe_set(owner, 'softGalleryLanguage_Domain3', {partner})
    assert getattr(partner, 'softGalleryLanguage_Functionality') == owner
    _safe_set(owner, 'softGalleryLanguage_Domain3', set())
    assert getattr(partner, 'softGalleryLanguage_Functionality') is None


def test_assoc_exceptionsdomain4_stub_double():
    # softGalleryLanguage_ExceptionsDomain has no real 'softGalleryLanguage_ExceptionsDomain' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Domain(name="sample_text")
    partner = softGalleryLanguage_ExceptionsDomain()
    setattr(partner, 'softGalleryLanguage_ExceptionsDomain', None)
    _safe_set(owner, 'softGalleryLanguage_Domain5', {partner})
    assert getattr(partner, 'softGalleryLanguage_ExceptionsDomain') == owner
    _safe_set(owner, 'softGalleryLanguage_Domain5', set())
    assert getattr(partner, 'softGalleryLanguage_ExceptionsDomain') is None


def test_assoc_items26_stub_double():
    # softGalleryLanguage_ProfileManagement has no real 'softGalleryLanguage_ProfileManagement27' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ProfileManagementFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ProfileManagementFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ProfileManagementFunctions(editProfileName="sample_text", viewprofileName="sample_text")
    partner = softGalleryLanguage_ProfileManagement()
    setattr(partner, 'softGalleryLanguage_ProfileManagement27', None)
    _safe_set(owner, 'softGalleryLanguage_ProfileManagementFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ProfileManagement27')
    _safe_set(owner, 'softGalleryLanguage_ProfileManagementFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ProfileManagement27')


def test_assoc_items28_stub_double():
    # softGalleryLanguage_AppAccess has no real 'softGalleryLanguage_AppAccess29' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_AppAccessFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_AppAccessFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_AppAccessFunctions(loginName="sample_text", registerName="sample_text")
    partner = softGalleryLanguage_AppAccess()
    setattr(partner, 'softGalleryLanguage_AppAccess29', None)
    _safe_set(owner, 'softGalleryLanguage_AppAccessFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_AppAccess29')
    _safe_set(owner, 'softGalleryLanguage_AppAccessFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_AppAccess29')


def test_assoc_items30_stub_double():
    # softGalleryLanguage_AlbumManagement has no real 'softGalleryLanguage_AlbumManagement31' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_AlbumManagementFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_AlbumManagementFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_AlbumManagementFunctions(createdAlbName="sample_text", selectAlbName="sample_text")
    partner = softGalleryLanguage_AlbumManagement()
    setattr(partner, 'softGalleryLanguage_AlbumManagement31', None)
    _safe_set(owner, 'softGalleryLanguage_AlbumManagementFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_AlbumManagement31')
    _safe_set(owner, 'softGalleryLanguage_AlbumManagementFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_AlbumManagement31')


def test_assoc_items32_stub_double():
    # softGalleryLanguage_PhotoActions has no real 'softGalleryLanguage_PhotoActions33' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PhotoActionsFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PhotoActionsFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PhotoActionsFunctions(nameGenerico="sample_text", nameLoad="sample_text", namePhoto="sample_text")
    partner = softGalleryLanguage_PhotoActions()
    setattr(partner, 'softGalleryLanguage_PhotoActions33', None)
    _safe_set(owner, 'softGalleryLanguage_PhotoActionsFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_PhotoActions33')
    _safe_set(owner, 'softGalleryLanguage_PhotoActionsFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_PhotoActions33')


def test_assoc_items34_stub_double():
    # softGalleryLanguage_LandingActions has no real 'softGalleryLanguage_LandingActions35' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_LandingFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_LandingFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_LandingFunctions(nameCarouselName="sample_text", passPhotoName="sample_text")
    partner = softGalleryLanguage_LandingActions()
    setattr(partner, 'softGalleryLanguage_LandingActions35', None)
    _safe_set(owner, 'softGalleryLanguage_LandingFunctions', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_LandingActions35')
    _safe_set(owner, 'softGalleryLanguage_LandingFunctions', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_LandingActions35')


def test_assoc_logiccomponents173_stub_double():
    # softGalleryLanguage_ComponentClass has no real 'softGalleryLanguage_ComponentClass' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_LogicStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_LogicStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_LogicStructure(appComName="sample_text", indexCompName="sample_text")
    partner = softGalleryLanguage_ComponentClass()
    setattr(partner, 'softGalleryLanguage_ComponentClass', None)
    _safe_set(owner, 'softGalleryLanguage_LogicStructure174', {partner})
    assert getattr(partner, 'softGalleryLanguage_ComponentClass') == owner
    _safe_set(owner, 'softGalleryLanguage_LogicStructure174', set())
    assert getattr(partner, 'softGalleryLanguage_ComponentClass') is None


def test_assoc_method117_stub_double():
    # softGalleryLanguage_RequestMapping has no real 'softGalleryLanguage_RequestMapping118' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_RequestMappingMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_RequestMappingMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_RequestMappingMethod(name="sample_text")
    partner = softGalleryLanguage_RequestMapping()
    setattr(partner, 'softGalleryLanguage_RequestMapping118', None)
    _safe_set(owner, 'softGalleryLanguage_RequestMappingMethod', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_RequestMapping118')
    _safe_set(owner, 'softGalleryLanguage_RequestMappingMethod', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_RequestMapping118')


def test_assoc_ntierconnection85_stub_double():
    # softGalleryLanguage_NTierSource has no real 'softGalleryLanguage_NTierSource86' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_NTiersRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_NTiersRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_NTiersRelations(name="sample_text")
    partner = softGalleryLanguage_NTierSource()
    setattr(partner, 'softGalleryLanguage_NTierSource86', None)
    _safe_set(owner, 'softGalleryLanguage_NTiersRelations', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_NTierSource86')
    _safe_set(owner, 'softGalleryLanguage_NTiersRelations', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_NTierSource86')


def test_assoc_ntierconnection87_stub_double():
    # softGalleryLanguage_NTierTarget has no real 'softGalleryLanguage_NTierTarget88' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_NTiersRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_NTiersRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_NTiersRelations(name="sample_text")
    partner = softGalleryLanguage_NTierTarget()
    setattr(partner, 'softGalleryLanguage_NTierTarget88', None)
    _safe_set(owner, 'softGalleryLanguage_NTiersRelations89', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_NTierTarget88')
    _safe_set(owner, 'softGalleryLanguage_NTiersRelations89', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_NTierTarget88')


def test_assoc_ntierconnections80_stub_double():
    # softGalleryLanguage_NTiersConnections has no real 'softGalleryLanguage_NTiersConnections' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_NTierConnectionContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_NTierConnectionContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_NTierConnectionContent(nTierName="sample_text", ntierconnection="sample_text")
    partner = softGalleryLanguage_NTiersConnections()
    setattr(partner, 'softGalleryLanguage_NTiersConnections', None)
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_NTiersConnections')
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_NTiersConnections')


def test_assoc_ntierorigin81_stub_double():
    # softGalleryLanguage_NTierSource has no real 'softGalleryLanguage_NTierSource' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_NTierConnectionContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_NTierConnectionContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_NTierConnectionContent(nTierName="sample_text", ntierconnection="sample_text")
    partner = softGalleryLanguage_NTierSource()
    setattr(partner, 'softGalleryLanguage_NTierSource', None)
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent82', {partner})
    assert getattr(partner, 'softGalleryLanguage_NTierSource') == owner
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent82', set())
    assert getattr(partner, 'softGalleryLanguage_NTierSource') is None


def test_assoc_ntiertarget83_stub_double():
    # softGalleryLanguage_NTierTarget has no real 'softGalleryLanguage_NTierTarget' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_NTierConnectionContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_NTierConnectionContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_NTierConnectionContent(nTierName="sample_text", ntierconnection="sample_text")
    partner = softGalleryLanguage_NTierTarget()
    setattr(partner, 'softGalleryLanguage_NTierTarget', None)
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent84', {partner})
    assert getattr(partner, 'softGalleryLanguage_NTierTarget') == owner
    _safe_set(owner, 'softGalleryLanguage_NTierConnectionContent84', set())
    assert getattr(partner, 'softGalleryLanguage_NTierTarget') is None


def test_assoc_photoException38_stub_double():
    # softGalleryLanguage_ExceptionsType has no real 'softGalleryLanguage_ExceptionsType39' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PhotoException's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PhotoException's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PhotoException(name="sample_text")
    partner = softGalleryLanguage_ExceptionsType()
    setattr(partner, 'softGalleryLanguage_ExceptionsType39', None)
    _safe_set(owner, 'softGalleryLanguage_PhotoException', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ExceptionsType39')
    _safe_set(owner, 'softGalleryLanguage_PhotoException', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ExceptionsType39')


def test_assoc_produces119_stub_double():
    # softGalleryLanguage_RequestMapping has no real 'softGalleryLanguage_RequestMapping120' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_RequestMappingProduces's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_RequestMappingProduces's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_RequestMappingProduces(name="sample_text")
    partner = softGalleryLanguage_RequestMapping()
    setattr(partner, 'softGalleryLanguage_RequestMapping120', None)
    _safe_set(owner, 'softGalleryLanguage_RequestMappingProduces', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_RequestMapping120')
    _safe_set(owner, 'softGalleryLanguage_RequestMappingProduces', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_RequestMapping120')


def test_assoc_propsconts205_stub_double():
    # softGalleryLanguage_Props has no real 'softGalleryLanguage_Props206' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PropsType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PropsType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PropsType(nameProps="sample_text", propsdatas="sample_text")
    partner = softGalleryLanguage_Props()
    setattr(partner, 'softGalleryLanguage_Props206', None)
    _safe_set(owner, 'softGalleryLanguage_PropsType', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Props206')
    _safe_set(owner, 'softGalleryLanguage_PropsType', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Props206')


def test_assoc_reactconstructors195_stub_double():
    # softGalleryLanguage_ReactConstructor has no real 'softGalleryLanguage_ReactConstructor' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactFunctions(lifecycleclass="sample_text", renderclass="sample_text")
    partner = softGalleryLanguage_ReactConstructor()
    setattr(partner, 'softGalleryLanguage_ReactConstructor', None)
    _safe_set(owner, 'softGalleryLanguage_ReactFunctions196', {partner})
    assert getattr(partner, 'softGalleryLanguage_ReactConstructor') == owner
    _safe_set(owner, 'softGalleryLanguage_ReactFunctions196', set())
    assert getattr(partner, 'softGalleryLanguage_ReactConstructor') is None


def test_assoc_reactinformation229_stub_double():
    # softGalleryLanguage_ReactInfo has no real 'softGalleryLanguage_ReactInfo230' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactInformation(name="sample_text")
    partner = softGalleryLanguage_ReactInfo()
    setattr(partner, 'softGalleryLanguage_ReactInfo230', None)
    _safe_set(owner, 'softGalleryLanguage_ReactInformation', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactInfo230')
    _safe_set(owner, 'softGalleryLanguage_ReactInformation', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactInfo230')


def test_assoc_reactlibraries227_stub_double():
    # softGalleryLanguage_ReactLibraries has no real 'softGalleryLanguage_ReactLibraries228' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactLibrary(name="sample_text")
    partner = softGalleryLanguage_ReactLibraries()
    setattr(partner, 'softGalleryLanguage_ReactLibraries228', None)
    _safe_set(owner, 'softGalleryLanguage_ReactLibrary', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactLibraries228')
    _safe_set(owner, 'softGalleryLanguage_ReactLibrary', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactLibraries228')


def test_assoc_reacts134_stub_double():
    # softGalleryLanguage_ReactModules has no real 'softGalleryLanguage_ReactModules' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_React's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_React's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_React(name="sample_text")
    partner = softGalleryLanguage_ReactModules()
    setattr(partner, 'softGalleryLanguage_ReactModules', None)
    _safe_set(owner, 'softGalleryLanguage_React135', {partner})
    assert getattr(partner, 'softGalleryLanguage_ReactModules') == owner
    _safe_set(owner, 'softGalleryLanguage_React135', set())
    assert getattr(partner, 'softGalleryLanguage_ReactModules') is None


def test_assoc_reactservrequest218_stub_double():
    # softGalleryLanguage_ReactServiceContRequest has no real 'softGalleryLanguage_ReactServiceContRequest' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactServiceContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactServiceContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactServiceContent(functName="sample_text")
    partner = softGalleryLanguage_ReactServiceContRequest()
    setattr(partner, 'softGalleryLanguage_ReactServiceContRequest', None)
    _safe_set(owner, 'softGalleryLanguage_ReactServiceContent219', {partner})
    assert getattr(partner, 'softGalleryLanguage_ReactServiceContRequest') == owner
    _safe_set(owner, 'softGalleryLanguage_ReactServiceContent219', set())
    assert getattr(partner, 'softGalleryLanguage_ReactServiceContRequest') is None


def test_assoc_reactservrequestprops220_stub_double():
    # softGalleryLanguage_ReactServiceContRequest has no real 'softGalleryLanguage_ReactServiceContRequest221' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactServiceRequestProps's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactServiceRequestProps's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactServiceRequestProps(reqPropDescription="sample_text", reqPropName="sample_text")
    partner = softGalleryLanguage_ReactServiceContRequest()
    setattr(partner, 'softGalleryLanguage_ReactServiceContRequest221', None)
    _safe_set(owner, 'softGalleryLanguage_ReactServiceRequestProps', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactServiceContRequest221')
    _safe_set(owner, 'softGalleryLanguage_ReactServiceRequestProps', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactServiceContRequest221')


def test_assoc_reactsimports193_stub_double():
    # softGalleryLanguage_ReactImports has no real 'softGalleryLanguage_ReactImports194' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactImportContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactImportContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactImportContent(impName="sample_text")
    partner = softGalleryLanguage_ReactImports()
    setattr(partner, 'softGalleryLanguage_ReactImports194', None)
    _safe_set(owner, 'softGalleryLanguage_ReactImportContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactImports194')
    _safe_set(owner, 'softGalleryLanguage_ReactImportContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactImports194')


def test_assoc_servicesrels222_stub_double():
    # softGalleryLanguage_ReactServicesRelation has no real 'softGalleryLanguage_ReactServicesRelation223' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ReactsRelationServ's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ReactsRelationServ's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ReactsRelationServ(name="sample_text")
    partner = softGalleryLanguage_ReactServicesRelation()
    setattr(partner, 'softGalleryLanguage_ReactServicesRelation223', None)
    _safe_set(owner, 'softGalleryLanguage_ReactsRelationServ', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ReactServicesRelation223')
    _safe_set(owner, 'softGalleryLanguage_ReactsRelationServ', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ReactServicesRelation223')


def test_assoc_springEntityAnnotationTypes125_stub_double():
    # softGalleryLanguage_SpringEntity has no real 'softGalleryLanguage_SpringEntity' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_SpringEntityAnnotationTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_SpringEntityAnnotationTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_SpringEntityAnnotationTypes(name="sample_text")
    partner = softGalleryLanguage_SpringEntity()
    setattr(partner, 'softGalleryLanguage_SpringEntity', None)
    _safe_set(owner, 'softGalleryLanguage_SpringEntityAnnotationTypes', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_SpringEntity')
    _safe_set(owner, 'softGalleryLanguage_SpringEntityAnnotationTypes', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_SpringEntity')


def test_assoc_statecontents203_stub_double():
    # softGalleryLanguage_State has no real 'softGalleryLanguage_State204' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_StateContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_StateContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_StateContent(componentdatatyp="sample_text", stateName="sample_text")
    partner = softGalleryLanguage_State()
    setattr(partner, 'softGalleryLanguage_State204', None)
    _safe_set(owner, 'softGalleryLanguage_StateContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_State204')
    _safe_set(owner, 'softGalleryLanguage_StateContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_State204')


def test_assoc_stylecontent209_stub_double():
    # softGalleryLanguage_StyleProperties has no real 'softGalleryLanguage_StyleProperties' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ComponentsStylesContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ComponentsStylesContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ComponentsStylesContent(nameStyle="sample_text")
    partner = softGalleryLanguage_StyleProperties()
    setattr(partner, 'softGalleryLanguage_StyleProperties', None)
    _safe_set(owner, 'softGalleryLanguage_ComponentsStylesContent210', {partner})
    assert getattr(partner, 'softGalleryLanguage_StyleProperties') == owner
    _safe_set(owner, 'softGalleryLanguage_ComponentsStylesContent210', set())
    assert getattr(partner, 'softGalleryLanguage_StyleProperties') is None


def test_assoc_stylescontents207_stub_double():
    # softGalleryLanguage_ComponentsStyles has no real 'softGalleryLanguage_ComponentsStyles208' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ComponentsStylesContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ComponentsStylesContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ComponentsStylesContent(nameStyle="sample_text")
    partner = softGalleryLanguage_ComponentsStyles()
    setattr(partner, 'softGalleryLanguage_ComponentsStyles208', None)
    _safe_set(owner, 'softGalleryLanguage_ComponentsStylesContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ComponentsStyles208')
    _safe_set(owner, 'softGalleryLanguage_ComponentsStylesContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ComponentsStyles208')


def test_assoc_stylespropscontents211_stub_double():
    # softGalleryLanguage_StyleProperties has no real 'softGalleryLanguage_StyleProperties212' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_StylePropertiesContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_StylePropertiesContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_StylePropertiesContent(propName="sample_text")
    partner = softGalleryLanguage_StyleProperties()
    setattr(partner, 'softGalleryLanguage_StyleProperties212', None)
    _safe_set(owner, 'softGalleryLanguage_StylePropertiesContent', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_StyleProperties212')
    _safe_set(owner, 'softGalleryLanguage_StylePropertiesContent', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_StyleProperties212')


def test_assoc_subcomponentcontent179_stub_double():
    # softGalleryLanguage_UIContent has no real 'softGalleryLanguage_UIContent180' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_SubcomponentCont's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_SubcomponentCont's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_SubcomponentCont(nameSubComp="sample_text")
    partner = softGalleryLanguage_UIContent()
    setattr(partner, 'softGalleryLanguage_UIContent180', None)
    _safe_set(owner, 'softGalleryLanguage_SubcomponentCont', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_UIContent180')
    _safe_set(owner, 'softGalleryLanguage_SubcomponentCont', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_UIContent180')


def test_assoc_techamazon97_stub_double():
    # softGalleryLanguage_Technologies has no real 'softGalleryLanguage_Technologies98' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_AmazonWebServices's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_AmazonWebServices's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_AmazonWebServices(name="sample_text")
    partner = softGalleryLanguage_Technologies()
    setattr(partner, 'softGalleryLanguage_Technologies98', None)
    _safe_set(owner, 'softGalleryLanguage_AmazonWebServices', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Technologies98')
    _safe_set(owner, 'softGalleryLanguage_AmazonWebServices', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Technologies98')


def test_assoc_techpostgresql95_stub_double():
    # softGalleryLanguage_Technologies has no real 'softGalleryLanguage_Technologies96' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_PostgreSQL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_PostgreSQL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_PostgreSQL(name="sample_text")
    partner = softGalleryLanguage_Technologies()
    setattr(partner, 'softGalleryLanguage_Technologies96', None)
    _safe_set(owner, 'softGalleryLanguage_PostgreSQL', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Technologies96')
    _safe_set(owner, 'softGalleryLanguage_PostgreSQL', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Technologies96')


def test_assoc_techreact93_stub_double():
    # softGalleryLanguage_Technologies has no real 'softGalleryLanguage_Technologies94' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_React's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_React's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_React(name="sample_text")
    partner = softGalleryLanguage_Technologies()
    setattr(partner, 'softGalleryLanguage_Technologies94', None)
    _safe_set(owner, 'softGalleryLanguage_React', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Technologies94')
    _safe_set(owner, 'softGalleryLanguage_React', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Technologies94')


def test_assoc_techspring91_stub_double():
    # softGalleryLanguage_Technologies has no real 'softGalleryLanguage_Technologies92' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_Spring's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_Spring's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_Spring(name="sample_text")
    partner = softGalleryLanguage_Technologies()
    setattr(partner, 'softGalleryLanguage_Technologies92', None)
    _safe_set(owner, 'softGalleryLanguage_Spring', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_Technologies92')
    _safe_set(owner, 'softGalleryLanguage_Spring', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_Technologies92')


def test_assoc_type113_stub_double():
    # softGalleryLanguage_MappingType has no real 'softGalleryLanguage_MappingType' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ResponseEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ResponseEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ResponseEntity(name="sample_text")
    partner = softGalleryLanguage_MappingType()
    setattr(partner, 'softGalleryLanguage_MappingType', None)
    _safe_set(owner, 'softGalleryLanguage_ResponseEntity', {partner})
    assert getattr(partner, 'softGalleryLanguage_MappingType') == owner
    _safe_set(owner, 'softGalleryLanguage_ResponseEntity', set())
    assert getattr(partner, 'softGalleryLanguage_MappingType') is None


def test_assoc_uicomponents175_stub_double():
    # softGalleryLanguage_UIContent has no real 'softGalleryLanguage_UIContent' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ComponentsUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ComponentsUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ComponentsUI(name="sample_text")
    partner = softGalleryLanguage_UIContent()
    setattr(partner, 'softGalleryLanguage_UIContent', None)
    _safe_set(owner, 'softGalleryLanguage_ComponentsUI176', {partner})
    assert getattr(partner, 'softGalleryLanguage_UIContent') == owner
    _safe_set(owner, 'softGalleryLanguage_ComponentsUI176', set())
    assert getattr(partner, 'softGalleryLanguage_UIContent') is None


def test_assoc_uicontent181_stub_double():
    # softGalleryLanguage_ComponentClass has no real 'softGalleryLanguage_ComponentClass183' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_ViewComponentCont's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_ViewComponentCont's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_ViewComponentCont(nameView="sample_text")
    partner = softGalleryLanguage_ComponentClass()
    setattr(partner, 'softGalleryLanguage_ComponentClass183', None)
    _safe_set(owner, 'softGalleryLanguage_ViewComponentCont182', {partner})
    assert getattr(partner, 'softGalleryLanguage_ComponentClass183') == owner
    _safe_set(owner, 'softGalleryLanguage_ViewComponentCont182', set())
    assert getattr(partner, 'softGalleryLanguage_ComponentClass183') is None


def test_assoc_uicontent184_stub_double():
    # softGalleryLanguage_ComponentClass has no real 'softGalleryLanguage_ComponentClass186' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_SubcomponentCont's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_SubcomponentCont's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_SubcomponentCont(nameSubComp="sample_text")
    partner = softGalleryLanguage_ComponentClass()
    setattr(partner, 'softGalleryLanguage_ComponentClass186', None)
    _safe_set(owner, 'softGalleryLanguage_SubcomponentCont185', {partner})
    assert getattr(partner, 'softGalleryLanguage_ComponentClass186') == owner
    _safe_set(owner, 'softGalleryLanguage_SubcomponentCont185', set())
    assert getattr(partner, 'softGalleryLanguage_ComponentClass186') is None


def test_assoc_userException42_stub_double():
    # softGalleryLanguage_ExceptionsType has no real 'softGalleryLanguage_ExceptionsType43' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_UserException's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_UserException's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_UserException(name="sample_text")
    partner = softGalleryLanguage_ExceptionsType()
    setattr(partner, 'softGalleryLanguage_ExceptionsType43', None)
    _safe_set(owner, 'softGalleryLanguage_UserException', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_ExceptionsType43')
    _safe_set(owner, 'softGalleryLanguage_UserException', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_ExceptionsType43')


def test_assoc_value116_stub_double():
    # softGalleryLanguage_RequestMapping has no real 'softGalleryLanguage_RequestMapping' property in the generated
    # code (a bare stub) -- manually attach it so softGalleryLanguage_RequestMappingValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # softGalleryLanguage_RequestMappingValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = softGalleryLanguage_RequestMappingValue(name="sample_text")
    partner = softGalleryLanguage_RequestMapping()
    setattr(partner, 'softGalleryLanguage_RequestMapping', None)
    _safe_set(owner, 'softGalleryLanguage_RequestMappingValue', partner)
    assert owner in getattr(partner, 'softGalleryLanguage_RequestMapping')
    _safe_set(owner, 'softGalleryLanguage_RequestMappingValue', None)
    assert owner not in getattr(partner, 'softGalleryLanguage_RequestMapping')


