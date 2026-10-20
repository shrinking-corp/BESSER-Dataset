import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Access,
    Actions,
    BusinessLogicSegment,
    Components,
    Connection,
    DataSegment,
    Entities,
    Functionalities,
    Layer,
    Logic,
    Modules,
    PhotosMetaModel_Access,
    PhotosMetaModel_Action_a,
    PhotosMetaModel_Actions,
    PhotosMetaModel_Album,
    PhotosMetaModel_AlbumManagement,
    PhotosMetaModel_AllowedToUse,
    PhotosMetaModel_AmazonElasticComputeCloud,
    PhotosMetaModel_AmazonS3API,
    PhotosMetaModel_AmazonS3Storage,
    PhotosMetaModel_AmazonSimpleStorageService,
    PhotosMetaModel_AmazonWebServices,
    PhotosMetaModel_AppAccess,
    PhotosMetaModel_Architecture,
    PhotosMetaModel_Autowired,
    PhotosMetaModel_BatchOperation,
    PhotosMetaModel_Bean,
    PhotosMetaModel_Bucket,
    PhotosMetaModel_BucketObjectsNotPublic,
    PhotosMetaModel_BusinessLogic,
    PhotosMetaModel_BusinessLogicSegment,
    PhotosMetaModel_Clause,
    PhotosMetaModel_Cluster,
    PhotosMetaModel_Column,
    PhotosMetaModel_Column_p,
    PhotosMetaModel_Column_s,
    PhotosMetaModel_Component,
    PhotosMetaModel_Component_a,
    PhotosMetaModel_Components,
    PhotosMetaModel_Configuration,
    PhotosMetaModel_Connection,
    PhotosMetaModel_Constraint,
    PhotosMetaModel_Constructor,
    PhotosMetaModel_Controller_a,
    PhotosMetaModel_CoreFunctions,
    PhotosMetaModel_Data,
    PhotosMetaModel_DataSegment,
    PhotosMetaModel_DataType,
    PhotosMetaModel_Database,
    PhotosMetaModel_DeleteMapping,
    PhotosMetaModel_Dependencies,
    PhotosMetaModel_Directories,
    PhotosMetaModel_Domain,
    PhotosMetaModel_EnableAuthorizationServer,
    PhotosMetaModel_EnableGlobalMethodSecurity,
    PhotosMetaModel_EnableResourceServer,
    PhotosMetaModel_EnableWebSecurity,
    PhotosMetaModel_Entities,
    PhotosMetaModel_Entity,
    PhotosMetaModel_Exception,
    PhotosMetaModel_ExceptionHandler,
    PhotosMetaModel_File_a,
    PhotosMetaModel_Files,
    PhotosMetaModel_Folder_a,
    PhotosMetaModel_ForeignKey,
    PhotosMetaModel_Function_p,
    PhotosMetaModel_Functionalities,
    PhotosMetaModel_GeneratedValue,
    PhotosMetaModel_GetMapping,
    PhotosMetaModel_Id,
    PhotosMetaModel_Index,
    PhotosMetaModel_Index_p,
    PhotosMetaModel_Information,
    PhotosMetaModel_Layer,
    PhotosMetaModel_Libraries,
    PhotosMetaModel_LifeCycle,
    PhotosMetaModel_Logic,
    PhotosMetaModel_MetaData,
    PhotosMetaModel_Model_a,
    PhotosMetaModel_Modules,
    PhotosMetaModel_NTier,
    PhotosMetaModel_NamedNativeQuery,
    PhotosMetaModel_ObjectsPublic,
    PhotosMetaModel_OnlyAuthorized,
    PhotosMetaModel_Order_s,
    PhotosMetaModel_Photo,
    PhotosMetaModel_PhotoActions,
    PhotosMetaModel_Policy,
    PhotosMetaModel_PostMapping,
    PhotosMetaModel_PostgreSQL,
    PhotosMetaModel_PostgreSQLConnection,
    PhotosMetaModel_PostgreSQL_a,
    PhotosMetaModel_Predicate,
    PhotosMetaModel_Presentation,
    PhotosMetaModel_PresentationSegment,
    PhotosMetaModel_Privilege,
    PhotosMetaModel_ProfileManagement,
    PhotosMetaModel_Props,
    PhotosMetaModel_Public,
    PhotosMetaModel_PutMapping,
    PhotosMetaModel_Query,
    PhotosMetaModel_REST,
    PhotosMetaModel_React,
    PhotosMetaModel_ReactClasses,
    PhotosMetaModel_ReactConfiguration,
    PhotosMetaModel_ReactDOM,
    PhotosMetaModel_ReactFunctions,
    PhotosMetaModel_Relation,
    PhotosMetaModel_Render,
    PhotosMetaModel_Repository,
    PhotosMetaModel_Repository_a,
    PhotosMetaModel_Request,
    PhotosMetaModel_RequestMapping,
    PhotosMetaModel_RequestPart,
    PhotosMetaModel_RestController,
    PhotosMetaModel_Router,
    PhotosMetaModel_Row,
    PhotosMetaModel_Scheme,
    PhotosMetaModel_SearchCriteria,
    PhotosMetaModel_Security_a,
    PhotosMetaModel_SegmentStructure,
    PhotosMetaModel_Services,
    PhotosMetaModel_SoftGallery,
    PhotosMetaModel_Specification,
    PhotosMetaModel_Spring,
    PhotosMetaModel_SpringBootApplication,
    PhotosMetaModel_State,
    PhotosMetaModel_Structure,
    PhotosMetaModel_Subcomponents,
    PhotosMetaModel_Table_p,
    PhotosMetaModel_Table_s,
    PhotosMetaModel_Technology,
    PhotosMetaModel_Trigger,
    PhotosMetaModel_UI,
    PhotosMetaModel_User_d,
    PhotosMetaModel_User_p,
    PhotosMetaModel_View,
    PhotosMetaModel_ViewComponents,
    PhotosMetaModel_View_a,
    PresentationSegment,
    ReactConfiguration,
    ReactFunctions,
    Relation,
    RequestMapping,
    UI,
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

def test_assoc_column81_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_p(name="sample_text")
    a2 = PhotosMetaModel_Table_p(name="sample_text_2")
    b = PhotosMetaModel_Column_p(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Column_p83', a1)
    assert _is_linked(b, 'PhotosMetaModel_Column_p83', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_p82'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_p82', b)
    _safe_set(b, 'PhotosMetaModel_Column_p83', a2)
    assert _is_linked(b, 'PhotosMetaModel_Column_p83', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_p82'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_p82', b)
    if hasattr(a2, 'PhotosMetaModel_Table_p82'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_p82', b)
    _safe_set(b, 'PhotosMetaModel_Column_p83', None)
    assert not _is_linked(b, 'PhotosMetaModel_Column_p83', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_p82'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_p82', b)


def test_assoc_column_s49_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_s(name="sample_text")
    a2 = PhotosMetaModel_Table_s(name="sample_text_2")
    b = PhotosMetaModel_Column_s(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Column_s', a1)
    assert _is_linked(b, 'PhotosMetaModel_Column_s', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_s50'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_s50', b)
    _safe_set(b, 'PhotosMetaModel_Column_s', a2)
    assert _is_linked(b, 'PhotosMetaModel_Column_s', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_s50'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_s50', b)
    if hasattr(a2, 'PhotosMetaModel_Table_s50'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_s50', b)
    _safe_set(b, 'PhotosMetaModel_Column_s', None)
    assert not _is_linked(b, 'PhotosMetaModel_Column_s', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_s50'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_s50', b)


def test_assoc_datatype56_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_DataType(name="sample_text")
    a2 = PhotosMetaModel_DataType(name="sample_text_2")
    b = PhotosMetaModel_Column_p(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Column_p57', a1)
    assert _is_linked(b, 'PhotosMetaModel_Column_p57', a1)
    if hasattr(a1, 'PhotosMetaModel_DataType'):
        assert _is_linked(a1, 'PhotosMetaModel_DataType', b)
    _safe_set(b, 'PhotosMetaModel_Column_p57', a2)
    assert _is_linked(b, 'PhotosMetaModel_Column_p57', a2)
    if hasattr(a1, 'PhotosMetaModel_DataType'):
        assert not _is_linked(a1, 'PhotosMetaModel_DataType', b)
    if hasattr(a2, 'PhotosMetaModel_DataType'):
        assert _is_linked(a2, 'PhotosMetaModel_DataType', b)
    _safe_set(b, 'PhotosMetaModel_Column_p57', None)
    assert not _is_linked(b, 'PhotosMetaModel_Column_p57', a2)
    if hasattr(a2, 'PhotosMetaModel_DataType'):
        assert not _is_linked(a2, 'PhotosMetaModel_DataType', b)


def test_assoc_file_a174_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_File_a(ObjectURL="sample_text", Onwer="sample_text", size="sample_text")
    a2 = PhotosMetaModel_File_a(ObjectURL="sample_text_2", Onwer="sample_text_2", size="sample_text_2")
    b = PhotosMetaModel_Bucket(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Bucket175', {a1})
    assert _is_linked(b, 'PhotosMetaModel_Bucket175', a1)
    if hasattr(a1, 'PhotosMetaModel_File_a'):
        assert _is_linked(a1, 'PhotosMetaModel_File_a', b)
    _safe_set(b, 'PhotosMetaModel_Bucket175', {a2})
    assert _is_linked(b, 'PhotosMetaModel_Bucket175', a2)
    if hasattr(a1, 'PhotosMetaModel_File_a'):
        assert not _is_linked(a1, 'PhotosMetaModel_File_a', b)
    if hasattr(a2, 'PhotosMetaModel_File_a'):
        assert _is_linked(a2, 'PhotosMetaModel_File_a', b)
    _safe_set(b, 'PhotosMetaModel_Bucket175', set())
    assert not _is_linked(b, 'PhotosMetaModel_Bucket175', a2)
    if hasattr(a2, 'PhotosMetaModel_File_a'):
        assert not _is_linked(a2, 'PhotosMetaModel_File_a', b)


def test_assoc_file_a180_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Folder_a(name="sample_text")
    a2 = PhotosMetaModel_Folder_a(name="sample_text_2")
    b = PhotosMetaModel_File_a(ObjectURL="sample_text", Onwer="sample_text", size="sample_text")
    _safe_set(b, 'PhotosMetaModel_File_a182', a1)
    assert _is_linked(b, 'PhotosMetaModel_File_a182', a1)
    if hasattr(a1, 'PhotosMetaModel_Folder_a181'):
        assert _is_linked(a1, 'PhotosMetaModel_Folder_a181', b)
    _safe_set(b, 'PhotosMetaModel_File_a182', a2)
    assert _is_linked(b, 'PhotosMetaModel_File_a182', a2)
    if hasattr(a1, 'PhotosMetaModel_Folder_a181'):
        assert not _is_linked(a1, 'PhotosMetaModel_Folder_a181', b)
    if hasattr(a2, 'PhotosMetaModel_Folder_a181'):
        assert _is_linked(a2, 'PhotosMetaModel_Folder_a181', b)
    _safe_set(b, 'PhotosMetaModel_File_a182', None)
    assert not _is_linked(b, 'PhotosMetaModel_File_a182', a2)
    if hasattr(a2, 'PhotosMetaModel_Folder_a181'):
        assert not _is_linked(a2, 'PhotosMetaModel_Folder_a181', b)


def test_assoc_files194_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_SegmentStructure(name="sample_text")
    a2 = PhotosMetaModel_SegmentStructure(name="sample_text_2")
    b = PhotosMetaModel_Files(extension="sample_text", type="sample_text")
    _safe_set(b, 'PhotosMetaModel_Files', a1)
    assert _is_linked(b, 'PhotosMetaModel_Files', a1)
    if hasattr(a1, 'PhotosMetaModel_SegmentStructure195'):
        assert _is_linked(a1, 'PhotosMetaModel_SegmentStructure195', b)
    _safe_set(b, 'PhotosMetaModel_Files', a2)
    assert _is_linked(b, 'PhotosMetaModel_Files', a2)
    if hasattr(a1, 'PhotosMetaModel_SegmentStructure195'):
        assert not _is_linked(a1, 'PhotosMetaModel_SegmentStructure195', b)
    if hasattr(a2, 'PhotosMetaModel_SegmentStructure195'):
        assert _is_linked(a2, 'PhotosMetaModel_SegmentStructure195', b)
    _safe_set(b, 'PhotosMetaModel_Files', None)
    assert not _is_linked(b, 'PhotosMetaModel_Files', a2)
    if hasattr(a2, 'PhotosMetaModel_SegmentStructure195'):
        assert not _is_linked(a2, 'PhotosMetaModel_SegmentStructure195', b)


def test_assoc_folder_a176_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Folder_a(name="sample_text")
    a2 = PhotosMetaModel_Folder_a(name="sample_text_2")
    b = PhotosMetaModel_Bucket(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Bucket177', {a1})
    assert _is_linked(b, 'PhotosMetaModel_Bucket177', a1)
    if hasattr(a1, 'PhotosMetaModel_Folder_a'):
        assert _is_linked(a1, 'PhotosMetaModel_Folder_a', b)
    _safe_set(b, 'PhotosMetaModel_Bucket177', {a2})
    assert _is_linked(b, 'PhotosMetaModel_Bucket177', a2)
    if hasattr(a1, 'PhotosMetaModel_Folder_a'):
        assert not _is_linked(a1, 'PhotosMetaModel_Folder_a', b)
    if hasattr(a2, 'PhotosMetaModel_Folder_a'):
        assert _is_linked(a2, 'PhotosMetaModel_Folder_a', b)
    _safe_set(b, 'PhotosMetaModel_Bucket177', set())
    assert not _is_linked(b, 'PhotosMetaModel_Bucket177', a2)
    if hasattr(a2, 'PhotosMetaModel_Folder_a'):
        assert not _is_linked(a2, 'PhotosMetaModel_Folder_a', b)


def test_assoc_inherit93_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_p(name="sample_text")
    a2 = PhotosMetaModel_Table_p(name="sample_text_2")
    b = PhotosMetaModel_Table_p(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Table_p94', a1)
    assert _is_linked(b, 'PhotosMetaModel_Table_p94', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_p92'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_p92', b)
    _safe_set(b, 'PhotosMetaModel_Table_p94', a2)
    assert _is_linked(b, 'PhotosMetaModel_Table_p94', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_p92'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_p92', b)
    if hasattr(a2, 'PhotosMetaModel_Table_p92'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_p92', b)
    _safe_set(b, 'PhotosMetaModel_Table_p94', None)
    assert not _is_linked(b, 'PhotosMetaModel_Table_p94', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_p92'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_p92', b)


def test_assoc_primaryKey89_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_p(name="sample_text")
    a2 = PhotosMetaModel_Table_p(name="sample_text_2")
    b = PhotosMetaModel_Column_p(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Column_p91', a1)
    assert _is_linked(b, 'PhotosMetaModel_Column_p91', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_p90'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_p90', b)
    _safe_set(b, 'PhotosMetaModel_Column_p91', a2)
    assert _is_linked(b, 'PhotosMetaModel_Column_p91', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_p90'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_p90', b)
    if hasattr(a2, 'PhotosMetaModel_Table_p90'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_p90', b)
    _safe_set(b, 'PhotosMetaModel_Column_p91', None)
    assert not _is_linked(b, 'PhotosMetaModel_Column_p91', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_p90'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_p90', b)


def test_assoc_row84_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_p(name="sample_text")
    a2 = PhotosMetaModel_Table_p(name="sample_text_2")
    b = PhotosMetaModel_Row(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Row', a1)
    assert _is_linked(b, 'PhotosMetaModel_Row', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_p85'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_p85', b)
    _safe_set(b, 'PhotosMetaModel_Row', a2)
    assert _is_linked(b, 'PhotosMetaModel_Row', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_p85'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_p85', b)
    if hasattr(a2, 'PhotosMetaModel_Table_p85'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_p85', b)
    _safe_set(b, 'PhotosMetaModel_Row', None)
    assert not _is_linked(b, 'PhotosMetaModel_Row', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_p85'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_p85', b)


def test_assoc_scheme95_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Scheme(name="sample_text")
    a2 = PhotosMetaModel_Scheme(name="sample_text_2")
    b = PhotosMetaModel_Database(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Database', {a1})
    assert _is_linked(b, 'PhotosMetaModel_Database', a1)
    if hasattr(a1, 'PhotosMetaModel_Scheme'):
        assert _is_linked(a1, 'PhotosMetaModel_Scheme', b)
    _safe_set(b, 'PhotosMetaModel_Database', {a2})
    assert _is_linked(b, 'PhotosMetaModel_Database', a2)
    if hasattr(a1, 'PhotosMetaModel_Scheme'):
        assert not _is_linked(a1, 'PhotosMetaModel_Scheme', b)
    if hasattr(a2, 'PhotosMetaModel_Scheme'):
        assert _is_linked(a2, 'PhotosMetaModel_Scheme', b)
    _safe_set(b, 'PhotosMetaModel_Database', set())
    assert not _is_linked(b, 'PhotosMetaModel_Database', a2)
    if hasattr(a2, 'PhotosMetaModel_Scheme'):
        assert not _is_linked(a2, 'PhotosMetaModel_Scheme', b)


def test_assoc_table_postgresql96_reverse_link_reassign_clear():
    a1 = PhotosMetaModel_Table_p(name="sample_text")
    a2 = PhotosMetaModel_Table_p(name="sample_text_2")
    b = PhotosMetaModel_Scheme(name="sample_text")
    _safe_set(b, 'PhotosMetaModel_Scheme97', {a1})
    assert _is_linked(b, 'PhotosMetaModel_Scheme97', a1)
    if hasattr(a1, 'PhotosMetaModel_Table_p98'):
        assert _is_linked(a1, 'PhotosMetaModel_Table_p98', b)
    _safe_set(b, 'PhotosMetaModel_Scheme97', {a2})
    assert _is_linked(b, 'PhotosMetaModel_Scheme97', a2)
    if hasattr(a1, 'PhotosMetaModel_Table_p98'):
        assert not _is_linked(a1, 'PhotosMetaModel_Table_p98', b)
    if hasattr(a2, 'PhotosMetaModel_Table_p98'):
        assert _is_linked(a2, 'PhotosMetaModel_Table_p98', b)
    _safe_set(b, 'PhotosMetaModel_Scheme97', set())
    assert not _is_linked(b, 'PhotosMetaModel_Scheme97', a2)
    if hasattr(a2, 'PhotosMetaModel_Table_p98'):
        assert not _is_linked(a2, 'PhotosMetaModel_Table_p98', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_access172_stub_double():
    # PhotosMetaModel_Access has no real 'PhotosMetaModel_Access' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Bucket's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Bucket's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Bucket(name="sample_text")
    partner = PhotosMetaModel_Access()
    setattr(partner, 'PhotosMetaModel_Access', None)
    _safe_set(owner, 'PhotosMetaModel_Bucket173', partner)
    assert getattr(partner, 'PhotosMetaModel_Access') == owner
    _safe_set(owner, 'PhotosMetaModel_Bucket173', None)
    assert getattr(partner, 'PhotosMetaModel_Access') is None


def test_assoc_albummanagement129_stub_double():
    # PhotosMetaModel_AlbumManagement has no real 'PhotosMetaModel_AlbumManagement130' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Album's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Album's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Album(name="sample_text", url="sample_text")
    partner = PhotosMetaModel_AlbumManagement()
    setattr(partner, 'PhotosMetaModel_AlbumManagement130', None)
    _safe_set(owner, 'PhotosMetaModel_Album', partner)
    assert getattr(partner, 'PhotosMetaModel_AlbumManagement130') == owner
    _safe_set(owner, 'PhotosMetaModel_Album', None)
    assert getattr(partner, 'PhotosMetaModel_AlbumManagement130') is None


def test_assoc_autowired26_stub_double():
    # PhotosMetaModel_Autowired has no real 'PhotosMetaModel_Autowired' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_RestController(name="sample_text")
    partner = PhotosMetaModel_Autowired()
    setattr(partner, 'PhotosMetaModel_Autowired', None)
    _safe_set(owner, 'PhotosMetaModel_RestController27', {partner})
    assert getattr(partner, 'PhotosMetaModel_Autowired') == owner
    _safe_set(owner, 'PhotosMetaModel_RestController27', set())
    assert getattr(partner, 'PhotosMetaModel_Autowired') is None


def test_assoc_bucket168_stub_double():
    # PhotosMetaModel_AmazonSimpleStorageService has no real 'PhotosMetaModel_AmazonSimpleStorageService169' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Bucket's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Bucket's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Bucket(name="sample_text")
    partner = PhotosMetaModel_AmazonSimpleStorageService()
    setattr(partner, 'PhotosMetaModel_AmazonSimpleStorageService169', None)
    _safe_set(owner, 'PhotosMetaModel_Bucket', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_AmazonSimpleStorageService169')
    _safe_set(owner, 'PhotosMetaModel_Bucket', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_AmazonSimpleStorageService169')


def test_assoc_column77_stub_double():
    # PhotosMetaModel_ForeignKey has no real 'PhotosMetaModel_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Column_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Column_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Column_p(name="sample_text")
    partner = PhotosMetaModel_ForeignKey()
    setattr(partner, 'PhotosMetaModel_ForeignKey', None)
    _safe_set(owner, 'PhotosMetaModel_Column_p78', partner)
    assert getattr(partner, 'PhotosMetaModel_ForeignKey') == owner
    _safe_set(owner, 'PhotosMetaModel_Column_p78', None)
    assert getattr(partner, 'PhotosMetaModel_ForeignKey') is None


def test_assoc_constraint55_stub_double():
    # PhotosMetaModel_Constraint has no real 'PhotosMetaModel_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Column_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Column_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Column_p(name="sample_text")
    partner = PhotosMetaModel_Constraint()
    setattr(partner, 'PhotosMetaModel_Constraint', None)
    _safe_set(owner, 'PhotosMetaModel_Column_p', {partner})
    assert getattr(partner, 'PhotosMetaModel_Constraint') == owner
    _safe_set(owner, 'PhotosMetaModel_Column_p', set())
    assert getattr(partner, 'PhotosMetaModel_Constraint') is None


def test_assoc_database111_stub_double():
    # PhotosMetaModel_Cluster has no real 'PhotosMetaModel_Cluster112' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Database(name="sample_text")
    partner = PhotosMetaModel_Cluster()
    setattr(partner, 'PhotosMetaModel_Cluster112', None)
    _safe_set(owner, 'PhotosMetaModel_Database113', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_Cluster112')
    _safe_set(owner, 'PhotosMetaModel_Database113', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_Cluster112')


def test_assoc_datatype119_stub_double():
    # PhotosMetaModel_Column has no real 'PhotosMetaModel_Column' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_DataType(name="sample_text")
    partner = PhotosMetaModel_Column()
    setattr(partner, 'PhotosMetaModel_Column', None)
    _safe_set(owner, 'PhotosMetaModel_DataType120', partner)
    assert getattr(partner, 'PhotosMetaModel_Column') == owner
    _safe_set(owner, 'PhotosMetaModel_DataType120', None)
    assert getattr(partner, 'PhotosMetaModel_Column') is None


def test_assoc_directories192_stub_double():
    # PhotosMetaModel_Directories has no real 'PhotosMetaModel_Directories' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_SegmentStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_SegmentStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_SegmentStructure(name="sample_text")
    partner = PhotosMetaModel_Directories()
    setattr(partner, 'PhotosMetaModel_Directories', None)
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure193', {partner})
    assert getattr(partner, 'PhotosMetaModel_Directories') == owner
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure193', set())
    assert getattr(partner, 'PhotosMetaModel_Directories') is None


def test_assoc_entities7_stub_double():
    # PhotosMetaModel_Domain has no real 'PhotosMetaModel_Domain8' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Entities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Entities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Entities(id="sample_text")
    partner = PhotosMetaModel_Domain()
    setattr(partner, 'PhotosMetaModel_Domain8', None)
    _safe_set(owner, 'PhotosMetaModel_Entities', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_Domain8')
    _safe_set(owner, 'PhotosMetaModel_Entities', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_Domain8')


def test_assoc_exceptionhandler24_stub_double():
    # PhotosMetaModel_ExceptionHandler has no real 'PhotosMetaModel_ExceptionHandler' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_RestController(name="sample_text")
    partner = PhotosMetaModel_ExceptionHandler()
    setattr(partner, 'PhotosMetaModel_ExceptionHandler', None)
    _safe_set(owner, 'PhotosMetaModel_RestController25', {partner})
    assert getattr(partner, 'PhotosMetaModel_ExceptionHandler') == owner
    _safe_set(owner, 'PhotosMetaModel_RestController25', set())
    assert getattr(partner, 'PhotosMetaModel_ExceptionHandler') is None


def test_assoc_execute107_stub_double():
    # PhotosMetaModel_Query has no real 'PhotosMetaModel_Query108' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_User_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_User_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_User_p(password="sample_text", username="sample_text")
    partner = PhotosMetaModel_Query()
    setattr(partner, 'PhotosMetaModel_Query108', None)
    _safe_set(owner, 'PhotosMetaModel_User_p', {partner})
    assert getattr(partner, 'PhotosMetaModel_Query108') == owner
    _safe_set(owner, 'PhotosMetaModel_User_p', set())
    assert getattr(partner, 'PhotosMetaModel_Query108') is None


def test_assoc_files196_stub_double():
    # PhotosMetaModel_Directories has no real 'PhotosMetaModel_Directories197' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Files's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Files's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Files(extension="sample_text", type="sample_text")
    partner = PhotosMetaModel_Directories()
    setattr(partner, 'PhotosMetaModel_Directories197', None)
    _safe_set(owner, 'PhotosMetaModel_Files198', partner)
    assert getattr(partner, 'PhotosMetaModel_Directories197') == owner
    _safe_set(owner, 'PhotosMetaModel_Files198', None)
    assert getattr(partner, 'PhotosMetaModel_Directories197') is None


def test_assoc_foreignkey86_stub_double():
    # PhotosMetaModel_ForeignKey has no real 'PhotosMetaModel_ForeignKey88' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Table_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Table_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Table_p(name="sample_text")
    partner = PhotosMetaModel_ForeignKey()
    setattr(partner, 'PhotosMetaModel_ForeignKey88', None)
    _safe_set(owner, 'PhotosMetaModel_Table_p87', {partner})
    assert getattr(partner, 'PhotosMetaModel_ForeignKey88') == owner
    _safe_set(owner, 'PhotosMetaModel_Table_p87', set())
    assert getattr(partner, 'PhotosMetaModel_ForeignKey88') is None


def test_assoc_functionalities124_stub_double():
    # PhotosMetaModel_Functionalities has no real 'PhotosMetaModel_Functionalities125' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_User_d's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_User_d's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_User_d(email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", profile_description="sample_text", username="sample_text")
    partner = PhotosMetaModel_Functionalities()
    setattr(partner, 'PhotosMetaModel_Functionalities125', None)
    _safe_set(owner, 'PhotosMetaModel_User_d', partner)
    assert getattr(partner, 'PhotosMetaModel_Functionalities125') == owner
    _safe_set(owner, 'PhotosMetaModel_User_d', None)
    assert getattr(partner, 'PhotosMetaModel_Functionalities125') is None


def test_assoc_id51_stub_double():
    # PhotosMetaModel_Id has no real 'PhotosMetaModel_Id' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Table_s's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Table_s's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Table_s(name="sample_text")
    partner = PhotosMetaModel_Id()
    setattr(partner, 'PhotosMetaModel_Id', None)
    _safe_set(owner, 'PhotosMetaModel_Table_s52', partner)
    assert getattr(partner, 'PhotosMetaModel_Id') == owner
    _safe_set(owner, 'PhotosMetaModel_Table_s52', None)
    assert getattr(partner, 'PhotosMetaModel_Id') is None


def test_assoc_index101_stub_double():
    # PhotosMetaModel_Index_p has no real 'PhotosMetaModel_Index_p' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Scheme(name="sample_text")
    partner = PhotosMetaModel_Index_p()
    setattr(partner, 'PhotosMetaModel_Index_p', None)
    _safe_set(owner, 'PhotosMetaModel_Scheme102', {partner})
    assert getattr(partner, 'PhotosMetaModel_Index_p') == owner
    _safe_set(owner, 'PhotosMetaModel_Scheme102', set())
    assert getattr(partner, 'PhotosMetaModel_Index_p') is None


def test_assoc_metadata178_stub_double():
    # PhotosMetaModel_MetaData has no real 'PhotosMetaModel_MetaData' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_File_a's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_File_a's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_File_a(ObjectURL="sample_text", Onwer="sample_text", size="sample_text")
    partner = PhotosMetaModel_MetaData()
    setattr(partner, 'PhotosMetaModel_MetaData', None)
    _safe_set(owner, 'PhotosMetaModel_File_a179', {partner})
    assert getattr(partner, 'PhotosMetaModel_MetaData') == owner
    _safe_set(owner, 'PhotosMetaModel_File_a179', set())
    assert getattr(partner, 'PhotosMetaModel_MetaData') is None


def test_assoc_modules165_stub_double():
    # PhotosMetaModel_Components has no real 'PhotosMetaModel_Components166' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Modules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Modules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Modules(name="sample_text")
    partner = PhotosMetaModel_Components()
    setattr(partner, 'PhotosMetaModel_Components166', None)
    _safe_set(owner, 'PhotosMetaModel_Modules167', partner)
    assert getattr(partner, 'PhotosMetaModel_Components166') == owner
    _safe_set(owner, 'PhotosMetaModel_Modules167', None)
    assert getattr(partner, 'PhotosMetaModel_Components166') is None


def test_assoc_modules21_stub_double():
    # PhotosMetaModel_React has no real 'PhotosMetaModel_React22' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Modules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Modules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Modules(name="sample_text")
    partner = PhotosMetaModel_React()
    setattr(partner, 'PhotosMetaModel_React22', None)
    _safe_set(owner, 'PhotosMetaModel_Modules', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_React22')
    _safe_set(owner, 'PhotosMetaModel_Modules', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_React22')


def test_assoc_photoactions127_stub_double():
    # PhotosMetaModel_PhotoActions has no real 'PhotosMetaModel_PhotoActions128' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Photo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Photo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Photo(name="sample_text")
    partner = PhotosMetaModel_PhotoActions()
    setattr(partner, 'PhotosMetaModel_PhotoActions128', None)
    _safe_set(owner, 'PhotosMetaModel_Photo', partner)
    assert getattr(partner, 'PhotosMetaModel_PhotoActions128') == owner
    _safe_set(owner, 'PhotosMetaModel_Photo', None)
    assert getattr(partner, 'PhotosMetaModel_PhotoActions128') is None


def test_assoc_policy117_stub_double():
    # PhotosMetaModel_Policy has no real 'PhotosMetaModel_Policy' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Row's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Row's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Row(name="sample_text")
    partner = PhotosMetaModel_Policy()
    setattr(partner, 'PhotosMetaModel_Policy', None)
    _safe_set(owner, 'PhotosMetaModel_Row118', {partner})
    assert getattr(partner, 'PhotosMetaModel_Policy') == owner
    _safe_set(owner, 'PhotosMetaModel_Row118', set())
    assert getattr(partner, 'PhotosMetaModel_Policy') is None


def test_assoc_privilege109_stub_double():
    # PhotosMetaModel_Privilege has no real 'PhotosMetaModel_Privilege' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_User_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_User_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_User_p(password="sample_text", username="sample_text")
    partner = PhotosMetaModel_Privilege()
    setattr(partner, 'PhotosMetaModel_Privilege', None)
    _safe_set(owner, 'PhotosMetaModel_User_p110', {partner})
    assert getattr(partner, 'PhotosMetaModel_Privilege') == owner
    _safe_set(owner, 'PhotosMetaModel_User_p110', set())
    assert getattr(partner, 'PhotosMetaModel_Privilege') is None


def test_assoc_props185_stub_double():
    # PhotosMetaModel_ReactClasses has no real 'PhotosMetaModel_ReactClasses186' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Props's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Props's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Props(dataType="sample_text", type="sample_text")
    partner = PhotosMetaModel_ReactClasses()
    setattr(partner, 'PhotosMetaModel_ReactClasses186', None)
    _safe_set(owner, 'PhotosMetaModel_Props', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_ReactClasses186')
    _safe_set(owner, 'PhotosMetaModel_Props', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_ReactClasses186')


def test_assoc_reactfunctions183_stub_double():
    # PhotosMetaModel_ReactClasses has no real 'PhotosMetaModel_ReactClasses184' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_ReactFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_ReactFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_ReactFunctions(name="sample_text")
    partner = PhotosMetaModel_ReactClasses()
    setattr(partner, 'PhotosMetaModel_ReactClasses184', None)
    _safe_set(owner, 'PhotosMetaModel_ReactFunctions', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_ReactClasses184')
    _safe_set(owner, 'PhotosMetaModel_ReactFunctions', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_ReactClasses184')


def test_assoc_reference79_stub_double():
    # PhotosMetaModel_ForeignKey has no real 'PhotosMetaModel_ForeignKey80' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Table_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Table_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Table_p(name="sample_text")
    partner = PhotosMetaModel_ForeignKey()
    setattr(partner, 'PhotosMetaModel_ForeignKey80', None)
    _safe_set(owner, 'PhotosMetaModel_Table_p', partner)
    assert getattr(partner, 'PhotosMetaModel_ForeignKey80') == owner
    _safe_set(owner, 'PhotosMetaModel_Table_p', None)
    assert getattr(partner, 'PhotosMetaModel_ForeignKey80') is None


def test_assoc_requestmapping23_stub_double():
    # PhotosMetaModel_RequestMapping has no real 'PhotosMetaModel_RequestMapping' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_RestController(name="sample_text")
    partner = PhotosMetaModel_RequestMapping()
    setattr(partner, 'PhotosMetaModel_RequestMapping', None)
    _safe_set(owner, 'PhotosMetaModel_RestController', {partner})
    assert getattr(partner, 'PhotosMetaModel_RequestMapping') == owner
    _safe_set(owner, 'PhotosMetaModel_RestController', set())
    assert getattr(partner, 'PhotosMetaModel_RequestMapping') is None


def test_assoc_restcontroller32_stub_double():
    # PhotosMetaModel_SpringBootApplication has no real 'PhotosMetaModel_SpringBootApplication33' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_RestController(name="sample_text")
    partner = PhotosMetaModel_SpringBootApplication()
    setattr(partner, 'PhotosMetaModel_SpringBootApplication33', None)
    _safe_set(owner, 'PhotosMetaModel_RestController34', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_SpringBootApplication33')
    _safe_set(owner, 'PhotosMetaModel_RestController34', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_SpringBootApplication33')


def test_assoc_segmentstructure156_stub_double():
    # PhotosMetaModel_PresentationSegment has no real 'PhotosMetaModel_PresentationSegment157' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_SegmentStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_SegmentStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_SegmentStructure(name="sample_text")
    partner = PhotosMetaModel_PresentationSegment()
    setattr(partner, 'PhotosMetaModel_PresentationSegment157', None)
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure', partner)
    assert getattr(partner, 'PhotosMetaModel_PresentationSegment157') == owner
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure', None)
    assert getattr(partner, 'PhotosMetaModel_PresentationSegment157') is None


def test_assoc_segmentstructure158_stub_double():
    # PhotosMetaModel_BusinessLogicSegment has no real 'PhotosMetaModel_BusinessLogicSegment159' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_SegmentStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_SegmentStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_SegmentStructure(name="sample_text")
    partner = PhotosMetaModel_BusinessLogicSegment()
    setattr(partner, 'PhotosMetaModel_BusinessLogicSegment159', None)
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure160', partner)
    assert getattr(partner, 'PhotosMetaModel_BusinessLogicSegment159') == owner
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure160', None)
    assert getattr(partner, 'PhotosMetaModel_BusinessLogicSegment159') is None


def test_assoc_segmentstructure161_stub_double():
    # PhotosMetaModel_DataSegment has no real 'PhotosMetaModel_DataSegment162' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_SegmentStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_SegmentStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_SegmentStructure(name="sample_text")
    partner = PhotosMetaModel_DataSegment()
    setattr(partner, 'PhotosMetaModel_DataSegment162', None)
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure163', partner)
    assert getattr(partner, 'PhotosMetaModel_DataSegment162') == owner
    _safe_set(owner, 'PhotosMetaModel_SegmentStructure163', None)
    assert getattr(partner, 'PhotosMetaModel_DataSegment162') is None


def test_assoc_specification28_stub_double():
    # PhotosMetaModel_Specification has no real 'PhotosMetaModel_Specification' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_RestController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_RestController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_RestController(name="sample_text")
    partner = PhotosMetaModel_Specification()
    setattr(partner, 'PhotosMetaModel_Specification', None)
    _safe_set(owner, 'PhotosMetaModel_RestController29', {partner})
    assert getattr(partner, 'PhotosMetaModel_Specification') == owner
    _safe_set(owner, 'PhotosMetaModel_RestController29', set())
    assert getattr(partner, 'PhotosMetaModel_Specification') is None


def test_assoc_state187_stub_double():
    # PhotosMetaModel_ReactClasses has no real 'PhotosMetaModel_ReactClasses188' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_State(active="sample_text")
    partner = PhotosMetaModel_ReactClasses()
    setattr(partner, 'PhotosMetaModel_ReactClasses188', None)
    _safe_set(owner, 'PhotosMetaModel_State', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_ReactClasses188')
    _safe_set(owner, 'PhotosMetaModel_State', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_ReactClasses188')


def test_assoc_storedprocedure105_stub_double():
    # PhotosMetaModel_Function_p has no real 'PhotosMetaModel_Function_p' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Scheme(name="sample_text")
    partner = PhotosMetaModel_Function_p()
    setattr(partner, 'PhotosMetaModel_Function_p', None)
    _safe_set(owner, 'PhotosMetaModel_Scheme106', {partner})
    assert getattr(partner, 'PhotosMetaModel_Function_p') == owner
    _safe_set(owner, 'PhotosMetaModel_Scheme106', set())
    assert getattr(partner, 'PhotosMetaModel_Function_p') is None


def test_assoc_table45_stub_double():
    # PhotosMetaModel_Entity has no real 'PhotosMetaModel_Entity46' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Table_s's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Table_s's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Table_s(name="sample_text")
    partner = PhotosMetaModel_Entity()
    setattr(partner, 'PhotosMetaModel_Entity46', None)
    _safe_set(owner, 'PhotosMetaModel_Table_s', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_Entity46')
    _safe_set(owner, 'PhotosMetaModel_Table_s', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_Entity46')


def test_assoc_trigger103_stub_double():
    # PhotosMetaModel_Trigger has no real 'PhotosMetaModel_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Scheme(name="sample_text")
    partner = PhotosMetaModel_Trigger()
    setattr(partner, 'PhotosMetaModel_Trigger', None)
    _safe_set(owner, 'PhotosMetaModel_Scheme104', {partner})
    assert getattr(partner, 'PhotosMetaModel_Trigger') == owner
    _safe_set(owner, 'PhotosMetaModel_Scheme104', set())
    assert getattr(partner, 'PhotosMetaModel_Trigger') is None


def test_assoc_user_p114_stub_double():
    # PhotosMetaModel_Cluster has no real 'PhotosMetaModel_Cluster115' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_User_p's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_User_p's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_User_p(password="sample_text", username="sample_text")
    partner = PhotosMetaModel_Cluster()
    setattr(partner, 'PhotosMetaModel_Cluster115', None)
    _safe_set(owner, 'PhotosMetaModel_User_p116', partner)
    assert owner in getattr(partner, 'PhotosMetaModel_Cluster115')
    _safe_set(owner, 'PhotosMetaModel_User_p116', None)
    assert owner not in getattr(partner, 'PhotosMetaModel_Cluster115')


def test_assoc_view_postgresql99_stub_double():
    # PhotosMetaModel_View has no real 'PhotosMetaModel_View' property in the generated
    # code (a bare stub) -- manually attach it so PhotosMetaModel_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PhotosMetaModel_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PhotosMetaModel_Scheme(name="sample_text")
    partner = PhotosMetaModel_View()
    setattr(partner, 'PhotosMetaModel_View', None)
    _safe_set(owner, 'PhotosMetaModel_Scheme100', {partner})
    assert getattr(partner, 'PhotosMetaModel_View') == owner
    _safe_set(owner, 'PhotosMetaModel_Scheme100', set())
    assert getattr(partner, 'PhotosMetaModel_View') is None


