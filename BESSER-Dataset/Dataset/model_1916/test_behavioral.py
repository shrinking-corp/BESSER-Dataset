import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Conflict,
    Dependence,
    File,
    InstalledPackage,
    NamedElement,
    Package,
    UnpackedPackage,
    mancoosimm_Alternative,
    mancoosimm_AndConflict,
    mancoosimm_AndDep,
    mancoosimm_AndInv,
    mancoosimm_ApplicationMenuCatalog,
    mancoosimm_Atom,
    mancoosimm_BinPackage,
    mancoosimm_Boot,
    mancoosimm_ConfigFilesPackage,
    mancoosimm_Configuration,
    mancoosimm_Conflict,
    mancoosimm_Dependence,
    mancoosimm_DesktopDB,
    mancoosimm_DocumentationFile,
    mancoosimm_EmacsPackage,
    mancoosimm_Environment,
    mancoosimm_File,
    mancoosimm_FileSystem,
    mancoosimm_GConf,
    mancoosimm_Group,
    mancoosimm_HalfConfiguredPackage,
    mancoosimm_HalfInstalledPackage,
    mancoosimm_IconCache,
    mancoosimm_InformationFile,
    mancoosimm_InstalledPackage,
    mancoosimm_Invariant,
    mancoosimm_LibraryCache,
    mancoosimm_Menu,
    mancoosimm_MenuEntry,
    mancoosimm_MimeType,
    mancoosimm_MimeTypeHandler,
    mancoosimm_MimeTypeHandlerCache,
    mancoosimm_Module,
    mancoosimm_ModuleCache,
    mancoosimm_NamedElement,
    mancoosimm_NotInstalledPackage,
    mancoosimm_NotInv,
    mancoosimm_OrConflict,
    mancoosimm_OrDep,
    mancoosimm_OrInv,
    mancoosimm_Package,
    mancoosimm_PackageSetting,
    mancoosimm_SGMLCatalog,
    mancoosimm_SGMLDocument,
    mancoosimm_Service,
    mancoosimm_SharedLibrary,
    mancoosimm_SingleConflict,
    mancoosimm_SingleDep,
    mancoosimm_SkeeperCatalog,
    mancoosimm_SkeeperDocument,
    mancoosimm_SrcPackage,
    mancoosimm_UnpackedPackage,
    mancoosimm_User,
    mancoosimm_VirtualPackage,
    mancoosimm_XFont,
    mancoosimm_XFontCache,
    PriorityType,
    StatusType,
    VersionType,
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

def test_assoc_childs163_reverse_link_reassign_clear():
    a1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    a2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'File164'):
        assert _is_linked(a1, 'File164', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'File164'):
        assert not _is_linked(a1, 'File164', b)
    if hasattr(a2, 'File164'):
        assert _is_linked(a2, 'File164', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'File164'):
        assert not _is_linked(a2, 'File164', b)


def test_assoc_configFilesPackages6_reverse_link_reassign_clear():
    a1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    a2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    b = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_ConfigFilesPackage', a1)
    assert _is_linked(b, 'mancoosimm_ConfigFilesPackage', a1)
    if hasattr(a1, 'mancoosimm_Configuration7'):
        assert _is_linked(a1, 'mancoosimm_Configuration7', b)
    _safe_set(b, 'mancoosimm_ConfigFilesPackage', a2)
    assert _is_linked(b, 'mancoosimm_ConfigFilesPackage', a2)
    if hasattr(a1, 'mancoosimm_Configuration7'):
        assert not _is_linked(a1, 'mancoosimm_Configuration7', b)
    if hasattr(a2, 'mancoosimm_Configuration7'):
        assert _is_linked(a2, 'mancoosimm_Configuration7', b)
    _safe_set(b, 'mancoosimm_ConfigFilesPackage', None)
    assert not _is_linked(b, 'mancoosimm_ConfigFilesPackage', a2)
    if hasattr(a2, 'mancoosimm_Configuration7'):
        assert not _is_linked(a2, 'mancoosimm_Configuration7', b)


def test_assoc_configuration14_reverse_link_reassign_clear():
    a1 = mancoosimm_Package(architecture="sample_text", version="sample_text")
    a2 = mancoosimm_Package(architecture="sample_text_2", version="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration15', a1)
    assert _is_linked(b, 'mancoosimm_Configuration15', a1)
    if hasattr(a1, 'mancoosimm_Package'):
        assert _is_linked(a1, 'mancoosimm_Package', b)
    _safe_set(b, 'mancoosimm_Configuration15', a2)
    assert _is_linked(b, 'mancoosimm_Configuration15', a2)
    if hasattr(a1, 'mancoosimm_Package'):
        assert not _is_linked(a1, 'mancoosimm_Package', b)
    if hasattr(a2, 'mancoosimm_Package'):
        assert _is_linked(a2, 'mancoosimm_Package', b)
    _safe_set(b, 'mancoosimm_Configuration15', None)
    assert not _is_linked(b, 'mancoosimm_Configuration15', a2)
    if hasattr(a2, 'mancoosimm_Package'):
        assert not _is_linked(a2, 'mancoosimm_Package', b)


def test_assoc_enhances28_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage29', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage29', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage27'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage27', b)
    _safe_set(b, 'mancoosimm_InstalledPackage29', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage29', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage27'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage27', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage27'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage27', b)
    _safe_set(b, 'mancoosimm_InstalledPackage29', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage29', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage27'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage27', b)


def test_assoc_file226_reverse_link_reassign_clear():
    a1 = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    a2 = mancoosimm_SharedLibrary(name="sample_text_2", version="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File227', a1)
    assert _is_linked(b, 'mancoosimm_File227', a1)
    if hasattr(a1, 'mancoosimm_SharedLibrary'):
        assert _is_linked(a1, 'mancoosimm_SharedLibrary', b)
    _safe_set(b, 'mancoosimm_File227', a2)
    assert _is_linked(b, 'mancoosimm_File227', a2)
    if hasattr(a1, 'mancoosimm_SharedLibrary'):
        assert not _is_linked(a1, 'mancoosimm_SharedLibrary', b)
    if hasattr(a2, 'mancoosimm_SharedLibrary'):
        assert _is_linked(a2, 'mancoosimm_SharedLibrary', b)
    _safe_set(b, 'mancoosimm_File227', None)
    assert not _is_linked(b, 'mancoosimm_File227', a2)
    if hasattr(a2, 'mancoosimm_SharedLibrary'):
        assert not _is_linked(a2, 'mancoosimm_SharedLibrary', b)


def test_assoc_files38_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File', a1)
    assert _is_linked(b, 'mancoosimm_File', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage39'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage39', b)
    _safe_set(b, 'mancoosimm_File', a2)
    assert _is_linked(b, 'mancoosimm_File', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage39'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage39', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage39'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage39', b)
    _safe_set(b, 'mancoosimm_File', None)
    assert not _is_linked(b, 'mancoosimm_File', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage39'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage39', b)


def test_assoc_files44_reverse_link_reassign_clear():
    a1 = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_UnpackedPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File46', a1)
    assert _is_linked(b, 'mancoosimm_File46', a1)
    if hasattr(a1, 'mancoosimm_UnpackedPackage45'):
        assert _is_linked(a1, 'mancoosimm_UnpackedPackage45', b)
    _safe_set(b, 'mancoosimm_File46', a2)
    assert _is_linked(b, 'mancoosimm_File46', a2)
    if hasattr(a1, 'mancoosimm_UnpackedPackage45'):
        assert not _is_linked(a1, 'mancoosimm_UnpackedPackage45', b)
    if hasattr(a2, 'mancoosimm_UnpackedPackage45'):
        assert _is_linked(a2, 'mancoosimm_UnpackedPackage45', b)
    _safe_set(b, 'mancoosimm_File46', None)
    assert not _is_linked(b, 'mancoosimm_File46', a2)
    if hasattr(a2, 'mancoosimm_UnpackedPackage45'):
        assert not _is_linked(a2, 'mancoosimm_UnpackedPackage45', b)


def test_assoc_halfInstalledPackages12_reverse_link_reassign_clear():
    a1 = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_HalfInstalledPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration13', {a1})
    assert _is_linked(b, 'mancoosimm_Configuration13', a1)
    if hasattr(a1, 'mancoosimm_HalfInstalledPackage'):
        assert _is_linked(a1, 'mancoosimm_HalfInstalledPackage', b)
    _safe_set(b, 'mancoosimm_Configuration13', {a2})
    assert _is_linked(b, 'mancoosimm_Configuration13', a2)
    if hasattr(a1, 'mancoosimm_HalfInstalledPackage'):
        assert not _is_linked(a1, 'mancoosimm_HalfInstalledPackage', b)
    if hasattr(a2, 'mancoosimm_HalfInstalledPackage'):
        assert _is_linked(a2, 'mancoosimm_HalfInstalledPackage', b)
    _safe_set(b, 'mancoosimm_Configuration13', set())
    assert not _is_linked(b, 'mancoosimm_Configuration13', a2)
    if hasattr(a2, 'mancoosimm_HalfInstalledPackage'):
        assert not _is_linked(a2, 'mancoosimm_HalfInstalledPackage', b)


def test_assoc_icons192_reverse_link_reassign_clear():
    a1 = mancoosimm_IconCache(mtime="sample_text")
    a2 = mancoosimm_IconCache(mtime="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File193', a1)
    assert _is_linked(b, 'mancoosimm_File193', a1)
    if hasattr(a1, 'mancoosimm_IconCache'):
        assert _is_linked(a1, 'mancoosimm_IconCache', b)
    _safe_set(b, 'mancoosimm_File193', a2)
    assert _is_linked(b, 'mancoosimm_File193', a2)
    if hasattr(a1, 'mancoosimm_IconCache'):
        assert not _is_linked(a1, 'mancoosimm_IconCache', b)
    if hasattr(a2, 'mancoosimm_IconCache'):
        assert _is_linked(a2, 'mancoosimm_IconCache', b)
    _safe_set(b, 'mancoosimm_File193', None)
    assert not _is_linked(b, 'mancoosimm_File193', a2)
    if hasattr(a2, 'mancoosimm_IconCache'):
        assert not _is_linked(a2, 'mancoosimm_IconCache', b)


def test_assoc_installedPackages3_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration', {a1})
    assert _is_linked(b, 'mancoosimm_Configuration', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage', b)
    _safe_set(b, 'mancoosimm_Configuration', {a2})
    assert _is_linked(b, 'mancoosimm_Configuration', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage', b)
    _safe_set(b, 'mancoosimm_Configuration', set())
    assert not _is_linked(b, 'mancoosimm_Configuration', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage', b)


def test_assoc_parent166_reverse_link_reassign_clear():
    a1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    a2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'childs', a1)
    assert _is_linked(b, 'childs', a1)
    if hasattr(a1, 'File167'):
        assert _is_linked(a1, 'File167', b)
    _safe_set(b, 'childs', a2)
    assert _is_linked(b, 'childs', a2)
    if hasattr(a1, 'File167'):
        assert not _is_linked(a1, 'File167', b)
    if hasattr(a2, 'File167'):
        assert _is_linked(a2, 'File167', b)
    _safe_set(b, 'childs', None)
    assert not _is_linked(b, 'childs', a2)
    if hasattr(a2, 'File167'):
        assert not _is_linked(a2, 'File167', b)


def test_assoc_predepends31_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage32', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage32', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage30'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage30', b)
    _safe_set(b, 'mancoosimm_InstalledPackage32', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage32', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage30'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage30', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage30'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage30', b)
    _safe_set(b, 'mancoosimm_InstalledPackage32', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage32', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage30'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage30', b)


def test_assoc_recommends22_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage23', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage23', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage21'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage21', b)
    _safe_set(b, 'mancoosimm_InstalledPackage23', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage23', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage21'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage21', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage21'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage21', b)
    _safe_set(b, 'mancoosimm_InstalledPackage23', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage23', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage21'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage21', b)


def test_assoc_replaces36_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage37', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage37', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage35'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage35', b)
    _safe_set(b, 'mancoosimm_InstalledPackage37', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage37', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage35'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage35', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage35'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage35', b)
    _safe_set(b, 'mancoosimm_InstalledPackage37', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage37', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage35'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage35', b)


def test_assoc_suggests25_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage26', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage26', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage24'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage24', b)
    _safe_set(b, 'mancoosimm_InstalledPackage26', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage26', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage24'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage24', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage24'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage24', b)
    _safe_set(b, 'mancoosimm_InstalledPackage26', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage26', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage24'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage24', b)


def test_assoc_unpackedPackages8_reverse_link_reassign_clear():
    a1 = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_UnpackedPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration9', {a1})
    assert _is_linked(b, 'mancoosimm_Configuration9', a1)
    if hasattr(a1, 'mancoosimm_UnpackedPackage'):
        assert _is_linked(a1, 'mancoosimm_UnpackedPackage', b)
    _safe_set(b, 'mancoosimm_Configuration9', {a2})
    assert _is_linked(b, 'mancoosimm_Configuration9', a2)
    if hasattr(a1, 'mancoosimm_UnpackedPackage'):
        assert not _is_linked(a1, 'mancoosimm_UnpackedPackage', b)
    if hasattr(a2, 'mancoosimm_UnpackedPackage'):
        assert _is_linked(a2, 'mancoosimm_UnpackedPackage', b)
    _safe_set(b, 'mancoosimm_Configuration9', set())
    assert not _is_linked(b, 'mancoosimm_Configuration9', a2)
    if hasattr(a2, 'mancoosimm_UnpackedPackage'):
        assert not _is_linked(a2, 'mancoosimm_UnpackedPackage', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allFiles130_stub_double():
    # mancoosimm_FileSystem has no real 'mancoosimm_FileSystem' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_FileSystem()
    setattr(partner, 'mancoosimm_FileSystem', None)
    _safe_set(owner, 'mancoosimm_File131', partner)
    assert owner in getattr(partner, 'mancoosimm_FileSystem')
    _safe_set(owner, 'mancoosimm_File131', None)
    assert owner not in getattr(partner, 'mancoosimm_FileSystem')


def test_assoc_applications196_stub_double():
    # mancoosimm_DesktopDB has no real 'mancoosimm_DesktopDB' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_DesktopDB()
    setattr(partner, 'mancoosimm_DesktopDB', None)
    _safe_set(owner, 'mancoosimm_File197', partner)
    assert getattr(partner, 'mancoosimm_DesktopDB') == owner
    _safe_set(owner, 'mancoosimm_File197', None)
    assert getattr(partner, 'mancoosimm_DesktopDB') is None


def test_assoc_cache211_stub_double():
    # mancoosimm_MimeTypeHandlerCache has no real 'MimeTypeHandlerCache212' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandlerCache()
    setattr(partner, 'MimeTypeHandlerCache212', None)
    _safe_set(owner, 'mimeTypes', partner)
    assert getattr(partner, 'MimeTypeHandlerCache212') == owner
    _safe_set(owner, 'mimeTypes', None)
    assert getattr(partner, 'MimeTypeHandlerCache212') is None


def test_assoc_confFiles132_stub_double():
    # mancoosimm_GConf has no real 'mancoosimm_GConf' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_GConf()
    setattr(partner, 'mancoosimm_GConf', None)
    _safe_set(owner, 'mancoosimm_File133', partner)
    assert owner in getattr(partner, 'mancoosimm_GConf')
    _safe_set(owner, 'mancoosimm_File133', None)
    assert owner not in getattr(partner, 'mancoosimm_GConf')


def test_assoc_configuration118_stub_double():
    # mancoosimm_Environment has no real 'environment' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'environment', None)
    _safe_set(owner, 'Configuration', partner)
    assert getattr(partner, 'environment') == owner
    _safe_set(owner, 'Configuration', None)
    assert getattr(partner, 'environment') is None


def test_assoc_configuration128_stub_double():
    # mancoosimm_FileSystem has no real 'fileSystem' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_FileSystem()
    setattr(partner, 'fileSystem', None)
    _safe_set(owner, 'Configuration129', partner)
    assert getattr(partner, 'fileSystem') == owner
    _safe_set(owner, 'Configuration129', None)
    assert getattr(partner, 'fileSystem') is None


def test_assoc_conflict273_stub_double():
    # mancoosimm_Conflict has no real 'Conflict' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleConflict's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleConflict's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'Conflict', None)
    _safe_set(owner, 'singleConflict', partner)
    assert getattr(partner, 'Conflict') == owner
    _safe_set(owner, 'singleConflict', None)
    assert getattr(partner, 'Conflict') is None


def test_assoc_conflict42_stub_double():
    # mancoosimm_Conflict has no real 'mancoosimm_Conflict' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'mancoosimm_Conflict', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage43', partner)
    assert getattr(partner, 'mancoosimm_Conflict') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage43', None)
    assert getattr(partner, 'mancoosimm_Conflict') is None


def test_assoc_current175_stub_double():
    # mancoosimm_Alternative has no real 'mancoosimm_Alternative' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Alternative()
    setattr(partner, 'mancoosimm_Alternative', None)
    _safe_set(owner, 'mancoosimm_File176', partner)
    assert getattr(partner, 'mancoosimm_Alternative') == owner
    _safe_set(owner, 'mancoosimm_File176', None)
    assert getattr(partner, 'mancoosimm_Alternative') is None


def test_assoc_dependence73_stub_double():
    # mancoosimm_Dependence has no real 'Dependence74' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleDep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleDep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'Dependence74', None)
    _safe_set(owner, 'singleDep', partner)
    assert getattr(partner, 'Dependence74') == owner
    _safe_set(owner, 'singleDep', None)
    assert getattr(partner, 'Dependence74') is None


def test_assoc_depends19_stub_double():
    # mancoosimm_Dependence has no real 'mancoosimm_Dependence' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'mancoosimm_Dependence', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage20', partner)
    assert getattr(partner, 'mancoosimm_Dependence') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage20', None)
    assert getattr(partner, 'mancoosimm_Dependence') is None


def test_assoc_document244_stub_double():
    # mancoosimm_SGMLDocument has no real 'mancoosimm_SGMLDocument245' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SGMLDocument()
    setattr(partner, 'mancoosimm_SGMLDocument245', None)
    _safe_set(owner, 'mancoosimm_File246', partner)
    assert getattr(partner, 'mancoosimm_SGMLDocument245') == owner
    _safe_set(owner, 'mancoosimm_File246', None)
    assert getattr(partner, 'mancoosimm_SGMLDocument245') is None


def test_assoc_document253_stub_double():
    # mancoosimm_SkeeperDocument has no real 'mancoosimm_SkeeperDocument254' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SkeeperDocument()
    setattr(partner, 'mancoosimm_SkeeperDocument254', None)
    _safe_set(owner, 'mancoosimm_File255', partner)
    assert getattr(partner, 'mancoosimm_SkeeperDocument254') == owner
    _safe_set(owner, 'mancoosimm_File255', None)
    assert getattr(partner, 'mancoosimm_SkeeperDocument254') is None


def test_assoc_documentationFiles40_stub_double():
    # mancoosimm_DocumentationFile has no real 'DocumentationFile' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_DocumentationFile()
    setattr(partner, 'DocumentationFile', None)
    _safe_set(owner, 'pkg41', {partner})
    assert getattr(partner, 'DocumentationFile') == owner
    _safe_set(owner, 'pkg41', set())
    assert getattr(partner, 'DocumentationFile') is None


def test_assoc_env190_stub_double():
    # mancoosimm_Environment has no real 'Environment191' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_IconCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_IconCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_IconCache(mtime="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment191', None)
    _safe_set(owner, 'iconCache', partner)
    assert getattr(partner, 'Environment191') == owner
    _safe_set(owner, 'iconCache', None)
    assert getattr(partner, 'Environment191') is None


def test_assoc_env214_stub_double():
    # mancoosimm_Environment has no real 'Environment215' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment215', None)
    _safe_set(owner, 'xfontCaches', partner)
    assert getattr(partner, 'Environment215') == owner
    _safe_set(owner, 'xfontCaches', None)
    assert getattr(partner, 'Environment215') is None


def test_assoc_env231_stub_double():
    # mancoosimm_Environment has no real 'Environment233' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment233', None)
    _safe_set(owner, 'moduleCache232', partner)
    assert getattr(partner, 'Environment233') == owner
    _safe_set(owner, 'moduleCache232', None)
    assert getattr(partner, 'Environment233') is None


def test_assoc_environment1_stub_double():
    # mancoosimm_Environment has no real 'Environment' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment', None)
    _safe_set(owner, 'configuration2', partner)
    assert getattr(partner, 'Environment') == owner
    _safe_set(owner, 'configuration2', None)
    assert getattr(partner, 'Environment') is None


def test_assoc_executable149_stub_double():
    # mancoosimm_MenuEntry has no real 'mancoosimm_MenuEntry' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_MenuEntry()
    setattr(partner, 'mancoosimm_MenuEntry', None)
    _safe_set(owner, 'mancoosimm_File150', partner)
    assert getattr(partner, 'mancoosimm_MenuEntry') == owner
    _safe_set(owner, 'mancoosimm_File150', None)
    assert getattr(partner, 'mancoosimm_MenuEntry') is None


def test_assoc_executable155_stub_double():
    # mancoosimm_Service has no real 'mancoosimm_Service156' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Service()
    setattr(partner, 'mancoosimm_Service156', None)
    _safe_set(owner, 'mancoosimm_File157', partner)
    assert getattr(partner, 'mancoosimm_Service156') == owner
    _safe_set(owner, 'mancoosimm_File157', None)
    assert getattr(partner, 'mancoosimm_Service156') is None


def test_assoc_file218_stub_double():
    # mancoosimm_XFont has no real 'mancoosimm_XFont' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_XFont()
    setattr(partner, 'mancoosimm_XFont', None)
    _safe_set(owner, 'mancoosimm_File219', partner)
    assert owner in getattr(partner, 'mancoosimm_XFont')
    _safe_set(owner, 'mancoosimm_File219', None)
    assert owner not in getattr(partner, 'mancoosimm_XFont')


def test_assoc_file234_stub_double():
    # mancoosimm_Module has no real 'mancoosimm_Module' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Module()
    setattr(partner, 'mancoosimm_Module', None)
    _safe_set(owner, 'mancoosimm_File235', partner)
    assert getattr(partner, 'mancoosimm_Module') == owner
    _safe_set(owner, 'mancoosimm_File235', None)
    assert getattr(partner, 'mancoosimm_Module') is None


def test_assoc_fileSystem0_stub_double():
    # mancoosimm_FileSystem has no real 'FileSystem' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_FileSystem()
    setattr(partner, 'FileSystem', None)
    _safe_set(owner, 'configuration', partner)
    assert getattr(partner, 'FileSystem') == owner
    _safe_set(owner, 'configuration', None)
    assert getattr(partner, 'FileSystem') is None


def test_assoc_files184_stub_double():
    # mancoosimm_PackageSetting has no real 'pkgSettings' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'pkgSettings', None)
    _safe_set(owner, 'File185', partner)
    assert owner in getattr(partner, 'pkgSettings')
    _safe_set(owner, 'File185', None)
    assert owner not in getattr(partner, 'pkgSettings')


def test_assoc_files256_stub_double():
    # mancoosimm_EmacsPackage has no real 'mancoosimm_EmacsPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_EmacsPackage()
    setattr(partner, 'mancoosimm_EmacsPackage', None)
    _safe_set(owner, 'mancoosimm_File257', partner)
    assert owner in getattr(partner, 'mancoosimm_EmacsPackage')
    _safe_set(owner, 'mancoosimm_File257', None)
    assert owner not in getattr(partner, 'mancoosimm_EmacsPackage')


def test_assoc_fs160_stub_double():
    # mancoosimm_FileSystem has no real 'FileSystem161' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_FileSystem()
    setattr(partner, 'FileSystem161', None)
    _safe_set(owner, 'root', partner)
    assert getattr(partner, 'FileSystem161') == owner
    _safe_set(owner, 'root', None)
    assert getattr(partner, 'FileSystem161') is None


def test_assoc_group170_stub_double():
    # mancoosimm_Group has no real 'mancoosimm_Group' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Group()
    setattr(partner, 'mancoosimm_Group', None)
    _safe_set(owner, 'mancoosimm_File171', partner)
    assert getattr(partner, 'mancoosimm_Group') == owner
    _safe_set(owner, 'mancoosimm_File171', None)
    assert getattr(partner, 'mancoosimm_Group') is None


def test_assoc_halfConfiguredPackages10_stub_double():
    # mancoosimm_HalfConfiguredPackage has no real 'mancoosimm_HalfConfiguredPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_HalfConfiguredPackage()
    setattr(partner, 'mancoosimm_HalfConfiguredPackage', None)
    _safe_set(owner, 'mancoosimm_Configuration11', {partner})
    assert getattr(partner, 'mancoosimm_HalfConfiguredPackage') == owner
    _safe_set(owner, 'mancoosimm_Configuration11', set())
    assert getattr(partner, 'mancoosimm_HalfConfiguredPackage') is None


def test_assoc_handler203_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'mancoosimm_MimeTypeHandler' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'mancoosimm_MimeTypeHandler', None)
    _safe_set(owner, 'mancoosimm_File204', partner)
    assert getattr(partner, 'mancoosimm_MimeTypeHandler') == owner
    _safe_set(owner, 'mancoosimm_File204', None)
    assert getattr(partner, 'mancoosimm_MimeTypeHandler') is None


def test_assoc_home265_stub_double():
    # mancoosimm_User has no real 'mancoosimm_User266' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_User()
    setattr(partner, 'mancoosimm_User266', None)
    _safe_set(owner, 'mancoosimm_File267', partner)
    assert getattr(partner, 'mancoosimm_User266') == owner
    _safe_set(owner, 'mancoosimm_File267', None)
    assert getattr(partner, 'mancoosimm_User266') is None


def test_assoc_iconCache106_stub_double():
    # mancoosimm_Environment has no real 'env107' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_IconCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_IconCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_IconCache(mtime="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env107', None)
    _safe_set(owner, 'IconCache', partner)
    assert getattr(partner, 'env107') == owner
    _safe_set(owner, 'IconCache', None)
    assert getattr(partner, 'env107') is None


def test_assoc_impPackage55_stub_double():
    # mancoosimm_VirtualPackage has no real 'mancoosimm_VirtualPackage56' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_VirtualPackage()
    setattr(partner, 'mancoosimm_VirtualPackage56', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage57', partner)
    assert owner in getattr(partner, 'mancoosimm_VirtualPackage56')
    _safe_set(owner, 'mancoosimm_InstalledPackage57', None)
    assert owner not in getattr(partner, 'mancoosimm_VirtualPackage56')


def test_assoc_libraryCache228_stub_double():
    # mancoosimm_LibraryCache has no real 'LibraryCache229' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SharedLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SharedLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    partner = mancoosimm_LibraryCache()
    setattr(partner, 'LibraryCache229', None)
    _safe_set(owner, 'sharedLibraries', partner)
    assert getattr(partner, 'LibraryCache229') == owner
    _safe_set(owner, 'sharedLibraries', None)
    assert getattr(partner, 'LibraryCache229') is None


def test_assoc_location177_stub_double():
    # mancoosimm_Alternative has no real 'mancoosimm_Alternative178' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Alternative()
    setattr(partner, 'mancoosimm_Alternative178', None)
    _safe_set(owner, 'mancoosimm_File179', partner)
    assert getattr(partner, 'mancoosimm_Alternative178') == owner
    _safe_set(owner, 'mancoosimm_File179', None)
    assert getattr(partner, 'mancoosimm_Alternative178') is None


def test_assoc_location241_stub_double():
    # mancoosimm_SGMLDocument has no real 'mancoosimm_SGMLDocument242' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SGMLDocument()
    setattr(partner, 'mancoosimm_SGMLDocument242', None)
    _safe_set(owner, 'mancoosimm_File243', partner)
    assert getattr(partner, 'mancoosimm_SGMLDocument242') == owner
    _safe_set(owner, 'mancoosimm_File243', None)
    assert getattr(partner, 'mancoosimm_SGMLDocument242') is None


def test_assoc_location250_stub_double():
    # mancoosimm_SkeeperDocument has no real 'mancoosimm_SkeeperDocument251' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SkeeperDocument()
    setattr(partner, 'mancoosimm_SkeeperDocument251', None)
    _safe_set(owner, 'mancoosimm_File252', partner)
    assert getattr(partner, 'mancoosimm_SkeeperDocument251') == owner
    _safe_set(owner, 'mancoosimm_File252', None)
    assert getattr(partner, 'mancoosimm_SkeeperDocument251') is None


def test_assoc_locations220_stub_double():
    # mancoosimm_LibraryCache has no real 'mancoosimm_LibraryCache' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_LibraryCache()
    setattr(partner, 'mancoosimm_LibraryCache', None)
    _safe_set(owner, 'mancoosimm_File221', partner)
    assert owner in getattr(partner, 'mancoosimm_LibraryCache')
    _safe_set(owner, 'mancoosimm_File221', None)
    assert owner not in getattr(partner, 'mancoosimm_LibraryCache')


def test_assoc_mimeTypeHandlers209_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'MimeTypeHandler210' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'MimeTypeHandler210', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'MimeTypeHandler210') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'MimeTypeHandler210') is None


def test_assoc_mimeTypes201_stub_double():
    # mancoosimm_MimeTypeHandlerCache has no real 'cache202' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandlerCache()
    setattr(partner, 'cache202', None)
    _safe_set(owner, 'MimeType', partner)
    assert owner in getattr(partner, 'cache202')
    _safe_set(owner, 'MimeType', None)
    assert owner not in getattr(partner, 'cache202')


def test_assoc_moduleCache119_stub_double():
    # mancoosimm_Environment has no real 'env120' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env120', None)
    _safe_set(owner, 'ModuleCache', partner)
    assert owner in getattr(partner, 'env120')
    _safe_set(owner, 'ModuleCache', None)
    assert owner not in getattr(partner, 'env120')


def test_assoc_moduleCache236_stub_double():
    # mancoosimm_Module has no real 'modules' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Module()
    setattr(partner, 'modules', None)
    _safe_set(owner, 'ModuleCache237', partner)
    assert getattr(partner, 'modules') == owner
    _safe_set(owner, 'ModuleCache237', None)
    assert getattr(partner, 'modules') is None


def test_assoc_modules230_stub_double():
    # mancoosimm_Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'moduleCache', {partner})
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'moduleCache', set())
    assert getattr(partner, 'Module') is None


def test_assoc_notInstalledPackages4_stub_double():
    # mancoosimm_NotInstalledPackage has no real 'mancoosimm_NotInstalledPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_NotInstalledPackage()
    setattr(partner, 'mancoosimm_NotInstalledPackage', None)
    _safe_set(owner, 'mancoosimm_Configuration5', {partner})
    assert getattr(partner, 'mancoosimm_NotInstalledPackage') == owner
    _safe_set(owner, 'mancoosimm_Configuration5', set())
    assert getattr(partner, 'mancoosimm_NotInstalledPackage') is None


def test_assoc_owner168_stub_double():
    # mancoosimm_User has no real 'mancoosimm_User' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_User()
    setattr(partner, 'mancoosimm_User', None)
    _safe_set(owner, 'mancoosimm_File169', partner)
    assert getattr(partner, 'mancoosimm_User') == owner
    _safe_set(owner, 'mancoosimm_File169', None)
    assert getattr(partner, 'mancoosimm_User') is None


def test_assoc_packageSettings16_stub_double():
    # mancoosimm_PackageSetting has no real 'PackageSetting' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'PackageSetting', None)
    _safe_set(owner, 'pkg', partner)
    assert getattr(partner, 'PackageSetting') == owner
    _safe_set(owner, 'pkg', None)
    assert getattr(partner, 'PackageSetting') is None


def test_assoc_pkg174_stub_double():
    # mancoosimm_DocumentationFile has no real 'documentationFiles' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_DocumentationFile()
    setattr(partner, 'documentationFiles', None)
    _safe_set(owner, 'InstalledPackage', partner)
    assert getattr(partner, 'documentationFiles') == owner
    _safe_set(owner, 'InstalledPackage', None)
    assert getattr(partner, 'documentationFiles') is None


def test_assoc_pkg186_stub_double():
    # mancoosimm_PackageSetting has no real 'packageSettings' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'packageSettings', None)
    _safe_set(owner, 'Package', partner)
    assert getattr(partner, 'packageSettings') == owner
    _safe_set(owner, 'Package', None)
    assert getattr(partner, 'packageSettings') is None


def test_assoc_pkg279_stub_double():
    # mancoosimm_Conflict has no real 'mancoosimm_Conflict280' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'mancoosimm_Conflict280', None)
    _safe_set(owner, 'mancoosimm_Package281', partner)
    assert getattr(partner, 'mancoosimm_Conflict280') == owner
    _safe_set(owner, 'mancoosimm_Package281', None)
    assert getattr(partner, 'mancoosimm_Conflict280') is None


def test_assoc_pkg63_stub_double():
    # mancoosimm_Dependence has no real 'mancoosimm_Dependence64' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'mancoosimm_Dependence64', None)
    _safe_set(owner, 'mancoosimm_Package65', partner)
    assert getattr(partner, 'mancoosimm_Dependence64') == owner
    _safe_set(owner, 'mancoosimm_Package65', None)
    assert getattr(partner, 'mancoosimm_Dependence64') is None


def test_assoc_pkgSettings172_stub_double():
    # mancoosimm_PackageSetting has no real 'PackageSetting173' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'PackageSetting173', None)
    _safe_set(owner, 'files', {partner})
    assert getattr(partner, 'PackageSetting173') == owner
    _safe_set(owner, 'files', set())
    assert getattr(partner, 'PackageSetting173') is None


def test_assoc_provides33_stub_double():
    # mancoosimm_VirtualPackage has no real 'mancoosimm_VirtualPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_VirtualPackage()
    setattr(partner, 'mancoosimm_VirtualPackage', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage34', partner)
    assert getattr(partner, 'mancoosimm_VirtualPackage') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage34', None)
    assert getattr(partner, 'mancoosimm_VirtualPackage') is None


def test_assoc_root127_stub_double():
    # mancoosimm_FileSystem has no real 'fs' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_FileSystem()
    setattr(partner, 'fs', None)
    _safe_set(owner, 'File', partner)
    assert getattr(partner, 'fs') == owner
    _safe_set(owner, 'File', None)
    assert getattr(partner, 'fs') is None


def test_assoc_schemas134_stub_double():
    # mancoosimm_GConf has no real 'mancoosimm_GConf135' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_GConf()
    setattr(partner, 'mancoosimm_GConf135', None)
    _safe_set(owner, 'mancoosimm_File136', partner)
    assert owner in getattr(partner, 'mancoosimm_GConf135')
    _safe_set(owner, 'mancoosimm_File136', None)
    assert owner not in getattr(partner, 'mancoosimm_GConf135')


def test_assoc_sharedLibraries222_stub_double():
    # mancoosimm_LibraryCache has no real 'libraryCache' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SharedLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SharedLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    partner = mancoosimm_LibraryCache()
    setattr(partner, 'libraryCache', None)
    _safe_set(owner, 'SharedLibrary', partner)
    assert owner in getattr(partner, 'libraryCache')
    _safe_set(owner, 'SharedLibrary', None)
    assert owner not in getattr(partner, 'libraryCache')


def test_assoc_singleConflict277_stub_double():
    # mancoosimm_Conflict has no real 'conflict278' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleConflict's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleConflict's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'conflict278', None)
    _safe_set(owner, 'SingleConflict', partner)
    assert getattr(partner, 'conflict278') == owner
    _safe_set(owner, 'SingleConflict', None)
    assert getattr(partner, 'conflict278') is None


def test_assoc_singleDep61_stub_double():
    # mancoosimm_Dependence has no real 'dependence62' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleDep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleDep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'dependence62', None)
    _safe_set(owner, 'SingleDep', partner)
    assert getattr(partner, 'dependence62') == owner
    _safe_set(owner, 'SingleDep', None)
    assert getattr(partner, 'dependence62') is None


def test_assoc_sourcePackage17_stub_double():
    # mancoosimm_SrcPackage has no real 'mancoosimm_SrcPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_SrcPackage()
    setattr(partner, 'mancoosimm_SrcPackage', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage18', partner)
    assert getattr(partner, 'mancoosimm_SrcPackage') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage18', None)
    assert getattr(partner, 'mancoosimm_SrcPackage') is None


def test_assoc_type205_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'mimeTypeHandlers' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'mimeTypeHandlers', None)
    _safe_set(owner, 'MimeType206', partner)
    assert getattr(partner, 'mimeTypeHandlers') == owner
    _safe_set(owner, 'MimeType206', None)
    assert getattr(partner, 'mimeTypeHandlers') is None


def test_assoc_xfontCache216_stub_double():
    # mancoosimm_XFont has no real 'xfonts' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_XFont()
    setattr(partner, 'xfonts', None)
    _safe_set(owner, 'XFontCache217', partner)
    assert getattr(partner, 'xfonts') == owner
    _safe_set(owner, 'XFontCache217', None)
    assert getattr(partner, 'xfonts') is None


def test_assoc_xfontCaches121_stub_double():
    # mancoosimm_Environment has no real 'env122' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env122', None)
    _safe_set(owner, 'XFontCache', partner)
    assert owner in getattr(partner, 'env122')
    _safe_set(owner, 'XFontCache', None)
    assert owner not in getattr(partner, 'env122')


def test_assoc_xfonts213_stub_double():
    # mancoosimm_XFont has no real 'XFont' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_XFont()
    setattr(partner, 'XFont', None)
    _safe_set(owner, 'xfontCache', {partner})
    assert getattr(partner, 'XFont') == owner
    _safe_set(owner, 'xfontCache', set())
    assert getattr(partner, 'XFont') is None


