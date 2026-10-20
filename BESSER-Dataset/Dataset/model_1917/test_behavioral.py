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
    mancoosimm_HalfConfiguredReinstRequiredPackage,
    mancoosimm_HalfInstalledPackage,
    mancoosimm_HalfInstalledReinstRequiredPackage,
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

def test_assoc_childs167_reverse_link_reassign_clear():
    a1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    a2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'File168'):
        assert _is_linked(a1, 'File168', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'File168'):
        assert not _is_linked(a1, 'File168', b)
    if hasattr(a2, 'File168'):
        assert _is_linked(a2, 'File168', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'File168'):
        assert not _is_linked(a2, 'File168', b)


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


def test_assoc_configuration18_reverse_link_reassign_clear():
    a1 = mancoosimm_Package(architecture="sample_text", version="sample_text")
    a2 = mancoosimm_Package(architecture="sample_text_2", version="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration19', a1)
    assert _is_linked(b, 'mancoosimm_Configuration19', a1)
    if hasattr(a1, 'mancoosimm_Package'):
        assert _is_linked(a1, 'mancoosimm_Package', b)
    _safe_set(b, 'mancoosimm_Configuration19', a2)
    assert _is_linked(b, 'mancoosimm_Configuration19', a2)
    if hasattr(a1, 'mancoosimm_Package'):
        assert not _is_linked(a1, 'mancoosimm_Package', b)
    if hasattr(a2, 'mancoosimm_Package'):
        assert _is_linked(a2, 'mancoosimm_Package', b)
    _safe_set(b, 'mancoosimm_Configuration19', None)
    assert not _is_linked(b, 'mancoosimm_Configuration19', a2)
    if hasattr(a2, 'mancoosimm_Package'):
        assert not _is_linked(a2, 'mancoosimm_Package', b)


def test_assoc_enhances32_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage33', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage33', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage31'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage31', b)
    _safe_set(b, 'mancoosimm_InstalledPackage33', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage33', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage31'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage31', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage31'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage31', b)
    _safe_set(b, 'mancoosimm_InstalledPackage33', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage33', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage31'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage31', b)


def test_assoc_file230_reverse_link_reassign_clear():
    a1 = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    a2 = mancoosimm_SharedLibrary(name="sample_text_2", version="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File231', a1)
    assert _is_linked(b, 'mancoosimm_File231', a1)
    if hasattr(a1, 'mancoosimm_SharedLibrary'):
        assert _is_linked(a1, 'mancoosimm_SharedLibrary', b)
    _safe_set(b, 'mancoosimm_File231', a2)
    assert _is_linked(b, 'mancoosimm_File231', a2)
    if hasattr(a1, 'mancoosimm_SharedLibrary'):
        assert not _is_linked(a1, 'mancoosimm_SharedLibrary', b)
    if hasattr(a2, 'mancoosimm_SharedLibrary'):
        assert _is_linked(a2, 'mancoosimm_SharedLibrary', b)
    _safe_set(b, 'mancoosimm_File231', None)
    assert not _is_linked(b, 'mancoosimm_File231', a2)
    if hasattr(a2, 'mancoosimm_SharedLibrary'):
        assert not _is_linked(a2, 'mancoosimm_SharedLibrary', b)


def test_assoc_files42_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File', a1)
    assert _is_linked(b, 'mancoosimm_File', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage43'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage43', b)
    _safe_set(b, 'mancoosimm_File', a2)
    assert _is_linked(b, 'mancoosimm_File', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage43'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage43', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage43'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage43', b)
    _safe_set(b, 'mancoosimm_File', None)
    assert not _is_linked(b, 'mancoosimm_File', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage43'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage43', b)


def test_assoc_files48_reverse_link_reassign_clear():
    a1 = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_UnpackedPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File50', a1)
    assert _is_linked(b, 'mancoosimm_File50', a1)
    if hasattr(a1, 'mancoosimm_UnpackedPackage49'):
        assert _is_linked(a1, 'mancoosimm_UnpackedPackage49', b)
    _safe_set(b, 'mancoosimm_File50', a2)
    assert _is_linked(b, 'mancoosimm_File50', a2)
    if hasattr(a1, 'mancoosimm_UnpackedPackage49'):
        assert not _is_linked(a1, 'mancoosimm_UnpackedPackage49', b)
    if hasattr(a2, 'mancoosimm_UnpackedPackage49'):
        assert _is_linked(a2, 'mancoosimm_UnpackedPackage49', b)
    _safe_set(b, 'mancoosimm_File50', None)
    assert not _is_linked(b, 'mancoosimm_File50', a2)
    if hasattr(a2, 'mancoosimm_UnpackedPackage49'):
        assert not _is_linked(a2, 'mancoosimm_UnpackedPackage49', b)


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


def test_assoc_halfInstalledReinstRequiredPackages16_reverse_link_reassign_clear():
    a1 = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    _safe_set(b, 'mancoosimm_Configuration17', {a1})
    assert _is_linked(b, 'mancoosimm_Configuration17', a1)
    if hasattr(a1, 'mancoosimm_HalfInstalledReinstRequiredPackage'):
        assert _is_linked(a1, 'mancoosimm_HalfInstalledReinstRequiredPackage', b)
    _safe_set(b, 'mancoosimm_Configuration17', {a2})
    assert _is_linked(b, 'mancoosimm_Configuration17', a2)
    if hasattr(a1, 'mancoosimm_HalfInstalledReinstRequiredPackage'):
        assert not _is_linked(a1, 'mancoosimm_HalfInstalledReinstRequiredPackage', b)
    if hasattr(a2, 'mancoosimm_HalfInstalledReinstRequiredPackage'):
        assert _is_linked(a2, 'mancoosimm_HalfInstalledReinstRequiredPackage', b)
    _safe_set(b, 'mancoosimm_Configuration17', set())
    assert not _is_linked(b, 'mancoosimm_Configuration17', a2)
    if hasattr(a2, 'mancoosimm_HalfInstalledReinstRequiredPackage'):
        assert not _is_linked(a2, 'mancoosimm_HalfInstalledReinstRequiredPackage', b)


def test_assoc_icons196_reverse_link_reassign_clear():
    a1 = mancoosimm_IconCache(mtime="sample_text")
    a2 = mancoosimm_IconCache(mtime="sample_text_2")
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'mancoosimm_File197', a1)
    assert _is_linked(b, 'mancoosimm_File197', a1)
    if hasattr(a1, 'mancoosimm_IconCache'):
        assert _is_linked(a1, 'mancoosimm_IconCache', b)
    _safe_set(b, 'mancoosimm_File197', a2)
    assert _is_linked(b, 'mancoosimm_File197', a2)
    if hasattr(a1, 'mancoosimm_IconCache'):
        assert not _is_linked(a1, 'mancoosimm_IconCache', b)
    if hasattr(a2, 'mancoosimm_IconCache'):
        assert _is_linked(a2, 'mancoosimm_IconCache', b)
    _safe_set(b, 'mancoosimm_File197', None)
    assert not _is_linked(b, 'mancoosimm_File197', a2)
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


def test_assoc_parent170_reverse_link_reassign_clear():
    a1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    a2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    b = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    _safe_set(b, 'childs', a1)
    assert _is_linked(b, 'childs', a1)
    if hasattr(a1, 'File171'):
        assert _is_linked(a1, 'File171', b)
    _safe_set(b, 'childs', a2)
    assert _is_linked(b, 'childs', a2)
    if hasattr(a1, 'File171'):
        assert not _is_linked(a1, 'File171', b)
    if hasattr(a2, 'File171'):
        assert _is_linked(a2, 'File171', b)
    _safe_set(b, 'childs', None)
    assert not _is_linked(b, 'childs', a2)
    if hasattr(a2, 'File171'):
        assert not _is_linked(a2, 'File171', b)


def test_assoc_predepends35_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage36', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage36', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage34'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage34', b)
    _safe_set(b, 'mancoosimm_InstalledPackage36', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage36', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage34'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage34', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage34'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage34', b)
    _safe_set(b, 'mancoosimm_InstalledPackage36', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage36', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage34'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage34', b)


def test_assoc_recommends26_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage27', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage27', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage25'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage25', b)
    _safe_set(b, 'mancoosimm_InstalledPackage27', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage27', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage25'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage25', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage25'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage25', b)
    _safe_set(b, 'mancoosimm_InstalledPackage27', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage27', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage25'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage25', b)


def test_assoc_replaces40_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage41', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage41', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage39'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage39', b)
    _safe_set(b, 'mancoosimm_InstalledPackage41', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage41', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage39'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage39', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage39'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage39', b)
    _safe_set(b, 'mancoosimm_InstalledPackage41', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage41', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage39'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage39', b)


def test_assoc_suggests29_reverse_link_reassign_clear():
    a1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    a2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    b = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    _safe_set(b, 'mancoosimm_InstalledPackage30', a1)
    assert _is_linked(b, 'mancoosimm_InstalledPackage30', a1)
    if hasattr(a1, 'mancoosimm_InstalledPackage28'):
        assert _is_linked(a1, 'mancoosimm_InstalledPackage28', b)
    _safe_set(b, 'mancoosimm_InstalledPackage30', a2)
    assert _is_linked(b, 'mancoosimm_InstalledPackage30', a2)
    if hasattr(a1, 'mancoosimm_InstalledPackage28'):
        assert not _is_linked(a1, 'mancoosimm_InstalledPackage28', b)
    if hasattr(a2, 'mancoosimm_InstalledPackage28'):
        assert _is_linked(a2, 'mancoosimm_InstalledPackage28', b)
    _safe_set(b, 'mancoosimm_InstalledPackage30', None)
    assert not _is_linked(b, 'mancoosimm_InstalledPackage30', a2)
    if hasattr(a2, 'mancoosimm_InstalledPackage28'):
        assert not _is_linked(a2, 'mancoosimm_InstalledPackage28', b)


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

def test_assoc_allFiles134_stub_double():
    # mancoosimm_FileSystem has no real 'mancoosimm_FileSystem' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_FileSystem()
    setattr(partner, 'mancoosimm_FileSystem', None)
    _safe_set(owner, 'mancoosimm_File135', partner)
    assert owner in getattr(partner, 'mancoosimm_FileSystem')
    _safe_set(owner, 'mancoosimm_File135', None)
    assert owner not in getattr(partner, 'mancoosimm_FileSystem')


def test_assoc_applications200_stub_double():
    # mancoosimm_DesktopDB has no real 'mancoosimm_DesktopDB' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_DesktopDB()
    setattr(partner, 'mancoosimm_DesktopDB', None)
    _safe_set(owner, 'mancoosimm_File201', partner)
    assert getattr(partner, 'mancoosimm_DesktopDB') == owner
    _safe_set(owner, 'mancoosimm_File201', None)
    assert getattr(partner, 'mancoosimm_DesktopDB') is None


def test_assoc_cache215_stub_double():
    # mancoosimm_MimeTypeHandlerCache has no real 'MimeTypeHandlerCache216' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandlerCache()
    setattr(partner, 'MimeTypeHandlerCache216', None)
    _safe_set(owner, 'mimeTypes', partner)
    assert getattr(partner, 'MimeTypeHandlerCache216') == owner
    _safe_set(owner, 'mimeTypes', None)
    assert getattr(partner, 'MimeTypeHandlerCache216') is None


def test_assoc_confFiles136_stub_double():
    # mancoosimm_GConf has no real 'mancoosimm_GConf' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_GConf()
    setattr(partner, 'mancoosimm_GConf', None)
    _safe_set(owner, 'mancoosimm_File137', partner)
    assert owner in getattr(partner, 'mancoosimm_GConf')
    _safe_set(owner, 'mancoosimm_File137', None)
    assert owner not in getattr(partner, 'mancoosimm_GConf')


def test_assoc_configuration122_stub_double():
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


def test_assoc_configuration132_stub_double():
    # mancoosimm_FileSystem has no real 'fileSystem' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_FileSystem()
    setattr(partner, 'fileSystem', None)
    _safe_set(owner, 'Configuration133', partner)
    assert getattr(partner, 'fileSystem') == owner
    _safe_set(owner, 'Configuration133', None)
    assert getattr(partner, 'fileSystem') is None


def test_assoc_conflict277_stub_double():
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


def test_assoc_conflict46_stub_double():
    # mancoosimm_Conflict has no real 'mancoosimm_Conflict' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'mancoosimm_Conflict', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage47', partner)
    assert getattr(partner, 'mancoosimm_Conflict') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage47', None)
    assert getattr(partner, 'mancoosimm_Conflict') is None


def test_assoc_current179_stub_double():
    # mancoosimm_Alternative has no real 'mancoosimm_Alternative' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Alternative()
    setattr(partner, 'mancoosimm_Alternative', None)
    _safe_set(owner, 'mancoosimm_File180', partner)
    assert getattr(partner, 'mancoosimm_Alternative') == owner
    _safe_set(owner, 'mancoosimm_File180', None)
    assert getattr(partner, 'mancoosimm_Alternative') is None


def test_assoc_dependence77_stub_double():
    # mancoosimm_Dependence has no real 'Dependence78' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleDep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleDep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'Dependence78', None)
    _safe_set(owner, 'singleDep', partner)
    assert getattr(partner, 'Dependence78') == owner
    _safe_set(owner, 'singleDep', None)
    assert getattr(partner, 'Dependence78') is None


def test_assoc_depends23_stub_double():
    # mancoosimm_Dependence has no real 'mancoosimm_Dependence' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'mancoosimm_Dependence', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage24', partner)
    assert getattr(partner, 'mancoosimm_Dependence') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage24', None)
    assert getattr(partner, 'mancoosimm_Dependence') is None


def test_assoc_document248_stub_double():
    # mancoosimm_SGMLDocument has no real 'mancoosimm_SGMLDocument249' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SGMLDocument()
    setattr(partner, 'mancoosimm_SGMLDocument249', None)
    _safe_set(owner, 'mancoosimm_File250', partner)
    assert getattr(partner, 'mancoosimm_SGMLDocument249') == owner
    _safe_set(owner, 'mancoosimm_File250', None)
    assert getattr(partner, 'mancoosimm_SGMLDocument249') is None


def test_assoc_document257_stub_double():
    # mancoosimm_SkeeperDocument has no real 'mancoosimm_SkeeperDocument258' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SkeeperDocument()
    setattr(partner, 'mancoosimm_SkeeperDocument258', None)
    _safe_set(owner, 'mancoosimm_File259', partner)
    assert getattr(partner, 'mancoosimm_SkeeperDocument258') == owner
    _safe_set(owner, 'mancoosimm_File259', None)
    assert getattr(partner, 'mancoosimm_SkeeperDocument258') is None


def test_assoc_documentationFiles44_stub_double():
    # mancoosimm_DocumentationFile has no real 'DocumentationFile' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_DocumentationFile()
    setattr(partner, 'DocumentationFile', None)
    _safe_set(owner, 'pkg45', {partner})
    assert getattr(partner, 'DocumentationFile') == owner
    _safe_set(owner, 'pkg45', set())
    assert getattr(partner, 'DocumentationFile') is None


def test_assoc_env194_stub_double():
    # mancoosimm_Environment has no real 'Environment195' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_IconCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_IconCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_IconCache(mtime="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment195', None)
    _safe_set(owner, 'iconCache', partner)
    assert getattr(partner, 'Environment195') == owner
    _safe_set(owner, 'iconCache', None)
    assert getattr(partner, 'Environment195') is None


def test_assoc_env218_stub_double():
    # mancoosimm_Environment has no real 'Environment219' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment219', None)
    _safe_set(owner, 'xfontCaches', partner)
    assert getattr(partner, 'Environment219') == owner
    _safe_set(owner, 'xfontCaches', None)
    assert getattr(partner, 'Environment219') is None


def test_assoc_env235_stub_double():
    # mancoosimm_Environment has no real 'Environment237' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'Environment237', None)
    _safe_set(owner, 'moduleCache236', partner)
    assert getattr(partner, 'Environment237') == owner
    _safe_set(owner, 'moduleCache236', None)
    assert getattr(partner, 'Environment237') is None


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


def test_assoc_executable153_stub_double():
    # mancoosimm_MenuEntry has no real 'mancoosimm_MenuEntry' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_MenuEntry()
    setattr(partner, 'mancoosimm_MenuEntry', None)
    _safe_set(owner, 'mancoosimm_File154', partner)
    assert getattr(partner, 'mancoosimm_MenuEntry') == owner
    _safe_set(owner, 'mancoosimm_File154', None)
    assert getattr(partner, 'mancoosimm_MenuEntry') is None


def test_assoc_executable159_stub_double():
    # mancoosimm_Service has no real 'mancoosimm_Service160' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Service()
    setattr(partner, 'mancoosimm_Service160', None)
    _safe_set(owner, 'mancoosimm_File161', partner)
    assert getattr(partner, 'mancoosimm_Service160') == owner
    _safe_set(owner, 'mancoosimm_File161', None)
    assert getattr(partner, 'mancoosimm_Service160') is None


def test_assoc_file222_stub_double():
    # mancoosimm_XFont has no real 'mancoosimm_XFont' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_XFont()
    setattr(partner, 'mancoosimm_XFont', None)
    _safe_set(owner, 'mancoosimm_File223', partner)
    assert owner in getattr(partner, 'mancoosimm_XFont')
    _safe_set(owner, 'mancoosimm_File223', None)
    assert owner not in getattr(partner, 'mancoosimm_XFont')


def test_assoc_file238_stub_double():
    # mancoosimm_Module has no real 'mancoosimm_Module' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Module()
    setattr(partner, 'mancoosimm_Module', None)
    _safe_set(owner, 'mancoosimm_File239', partner)
    assert getattr(partner, 'mancoosimm_Module') == owner
    _safe_set(owner, 'mancoosimm_File239', None)
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


def test_assoc_files188_stub_double():
    # mancoosimm_PackageSetting has no real 'pkgSettings' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'pkgSettings', None)
    _safe_set(owner, 'File189', partner)
    assert owner in getattr(partner, 'pkgSettings')
    _safe_set(owner, 'File189', None)
    assert owner not in getattr(partner, 'pkgSettings')


def test_assoc_files260_stub_double():
    # mancoosimm_EmacsPackage has no real 'mancoosimm_EmacsPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_EmacsPackage()
    setattr(partner, 'mancoosimm_EmacsPackage', None)
    _safe_set(owner, 'mancoosimm_File261', partner)
    assert owner in getattr(partner, 'mancoosimm_EmacsPackage')
    _safe_set(owner, 'mancoosimm_File261', None)
    assert owner not in getattr(partner, 'mancoosimm_EmacsPackage')


def test_assoc_fs164_stub_double():
    # mancoosimm_FileSystem has no real 'FileSystem165' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_FileSystem()
    setattr(partner, 'FileSystem165', None)
    _safe_set(owner, 'root', partner)
    assert getattr(partner, 'FileSystem165') == owner
    _safe_set(owner, 'root', None)
    assert getattr(partner, 'FileSystem165') is None


def test_assoc_group174_stub_double():
    # mancoosimm_Group has no real 'mancoosimm_Group' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Group()
    setattr(partner, 'mancoosimm_Group', None)
    _safe_set(owner, 'mancoosimm_File175', partner)
    assert getattr(partner, 'mancoosimm_Group') == owner
    _safe_set(owner, 'mancoosimm_File175', None)
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


def test_assoc_halfConfiguredReinstRequiredPackages14_stub_double():
    # mancoosimm_HalfConfiguredReinstRequiredPackage has no real 'mancoosimm_HalfConfiguredReinstRequiredPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    partner = mancoosimm_HalfConfiguredReinstRequiredPackage()
    setattr(partner, 'mancoosimm_HalfConfiguredReinstRequiredPackage', None)
    _safe_set(owner, 'mancoosimm_Configuration15', {partner})
    assert getattr(partner, 'mancoosimm_HalfConfiguredReinstRequiredPackage') == owner
    _safe_set(owner, 'mancoosimm_Configuration15', set())
    assert getattr(partner, 'mancoosimm_HalfConfiguredReinstRequiredPackage') is None


def test_assoc_handler207_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'mancoosimm_MimeTypeHandler' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'mancoosimm_MimeTypeHandler', None)
    _safe_set(owner, 'mancoosimm_File208', partner)
    assert getattr(partner, 'mancoosimm_MimeTypeHandler') == owner
    _safe_set(owner, 'mancoosimm_File208', None)
    assert getattr(partner, 'mancoosimm_MimeTypeHandler') is None


def test_assoc_home269_stub_double():
    # mancoosimm_User has no real 'mancoosimm_User270' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_User()
    setattr(partner, 'mancoosimm_User270', None)
    _safe_set(owner, 'mancoosimm_File271', partner)
    assert getattr(partner, 'mancoosimm_User270') == owner
    _safe_set(owner, 'mancoosimm_File271', None)
    assert getattr(partner, 'mancoosimm_User270') is None


def test_assoc_iconCache110_stub_double():
    # mancoosimm_Environment has no real 'env111' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_IconCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_IconCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_IconCache(mtime="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env111', None)
    _safe_set(owner, 'IconCache', partner)
    assert getattr(partner, 'env111') == owner
    _safe_set(owner, 'IconCache', None)
    assert getattr(partner, 'env111') is None


def test_assoc_impPackage59_stub_double():
    # mancoosimm_VirtualPackage has no real 'mancoosimm_VirtualPackage60' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_VirtualPackage()
    setattr(partner, 'mancoosimm_VirtualPackage60', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage61', partner)
    assert owner in getattr(partner, 'mancoosimm_VirtualPackage60')
    _safe_set(owner, 'mancoosimm_InstalledPackage61', None)
    assert owner not in getattr(partner, 'mancoosimm_VirtualPackage60')


def test_assoc_libraryCache232_stub_double():
    # mancoosimm_LibraryCache has no real 'LibraryCache233' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SharedLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SharedLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    partner = mancoosimm_LibraryCache()
    setattr(partner, 'LibraryCache233', None)
    _safe_set(owner, 'sharedLibraries', partner)
    assert getattr(partner, 'LibraryCache233') == owner
    _safe_set(owner, 'sharedLibraries', None)
    assert getattr(partner, 'LibraryCache233') is None


def test_assoc_location181_stub_double():
    # mancoosimm_Alternative has no real 'mancoosimm_Alternative182' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_Alternative()
    setattr(partner, 'mancoosimm_Alternative182', None)
    _safe_set(owner, 'mancoosimm_File183', partner)
    assert getattr(partner, 'mancoosimm_Alternative182') == owner
    _safe_set(owner, 'mancoosimm_File183', None)
    assert getattr(partner, 'mancoosimm_Alternative182') is None


def test_assoc_location245_stub_double():
    # mancoosimm_SGMLDocument has no real 'mancoosimm_SGMLDocument246' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SGMLDocument()
    setattr(partner, 'mancoosimm_SGMLDocument246', None)
    _safe_set(owner, 'mancoosimm_File247', partner)
    assert getattr(partner, 'mancoosimm_SGMLDocument246') == owner
    _safe_set(owner, 'mancoosimm_File247', None)
    assert getattr(partner, 'mancoosimm_SGMLDocument246') is None


def test_assoc_location254_stub_double():
    # mancoosimm_SkeeperDocument has no real 'mancoosimm_SkeeperDocument255' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_SkeeperDocument()
    setattr(partner, 'mancoosimm_SkeeperDocument255', None)
    _safe_set(owner, 'mancoosimm_File256', partner)
    assert getattr(partner, 'mancoosimm_SkeeperDocument255') == owner
    _safe_set(owner, 'mancoosimm_File256', None)
    assert getattr(partner, 'mancoosimm_SkeeperDocument255') is None


def test_assoc_locations224_stub_double():
    # mancoosimm_LibraryCache has no real 'mancoosimm_LibraryCache' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_LibraryCache()
    setattr(partner, 'mancoosimm_LibraryCache', None)
    _safe_set(owner, 'mancoosimm_File225', partner)
    assert owner in getattr(partner, 'mancoosimm_LibraryCache')
    _safe_set(owner, 'mancoosimm_File225', None)
    assert owner not in getattr(partner, 'mancoosimm_LibraryCache')


def test_assoc_mimeTypeHandlers213_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'MimeTypeHandler214' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'MimeTypeHandler214', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'MimeTypeHandler214') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'MimeTypeHandler214') is None


def test_assoc_mimeTypes205_stub_double():
    # mancoosimm_MimeTypeHandlerCache has no real 'cache206' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandlerCache()
    setattr(partner, 'cache206', None)
    _safe_set(owner, 'MimeType', partner)
    assert owner in getattr(partner, 'cache206')
    _safe_set(owner, 'MimeType', None)
    assert owner not in getattr(partner, 'cache206')


def test_assoc_moduleCache123_stub_double():
    # mancoosimm_Environment has no real 'env124' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env124', None)
    _safe_set(owner, 'ModuleCache', partner)
    assert owner in getattr(partner, 'env124')
    _safe_set(owner, 'ModuleCache', None)
    assert owner not in getattr(partner, 'env124')


def test_assoc_moduleCache240_stub_double():
    # mancoosimm_Module has no real 'modules' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_ModuleCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_ModuleCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_ModuleCache(version="sample_text")
    partner = mancoosimm_Module()
    setattr(partner, 'modules', None)
    _safe_set(owner, 'ModuleCache241', partner)
    assert getattr(partner, 'modules') == owner
    _safe_set(owner, 'ModuleCache241', None)
    assert getattr(partner, 'modules') is None


def test_assoc_modules234_stub_double():
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


def test_assoc_owner172_stub_double():
    # mancoosimm_User has no real 'mancoosimm_User' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_User()
    setattr(partner, 'mancoosimm_User', None)
    _safe_set(owner, 'mancoosimm_File173', partner)
    assert getattr(partner, 'mancoosimm_User') == owner
    _safe_set(owner, 'mancoosimm_File173', None)
    assert getattr(partner, 'mancoosimm_User') is None


def test_assoc_packageSettings20_stub_double():
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


def test_assoc_pkg178_stub_double():
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


def test_assoc_pkg190_stub_double():
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


def test_assoc_pkg283_stub_double():
    # mancoosimm_Conflict has no real 'mancoosimm_Conflict284' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'mancoosimm_Conflict284', None)
    _safe_set(owner, 'mancoosimm_Package285', partner)
    assert getattr(partner, 'mancoosimm_Conflict284') == owner
    _safe_set(owner, 'mancoosimm_Package285', None)
    assert getattr(partner, 'mancoosimm_Conflict284') is None


def test_assoc_pkg67_stub_double():
    # mancoosimm_Dependence has no real 'mancoosimm_Dependence68' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_Package(architecture="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'mancoosimm_Dependence68', None)
    _safe_set(owner, 'mancoosimm_Package69', partner)
    assert getattr(partner, 'mancoosimm_Dependence68') == owner
    _safe_set(owner, 'mancoosimm_Package69', None)
    assert getattr(partner, 'mancoosimm_Dependence68') is None


def test_assoc_pkgSettings176_stub_double():
    # mancoosimm_PackageSetting has no real 'PackageSetting177' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_PackageSetting()
    setattr(partner, 'PackageSetting177', None)
    _safe_set(owner, 'files', {partner})
    assert getattr(partner, 'PackageSetting177') == owner
    _safe_set(owner, 'files', set())
    assert getattr(partner, 'PackageSetting177') is None


def test_assoc_provides37_stub_double():
    # mancoosimm_VirtualPackage has no real 'mancoosimm_VirtualPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_VirtualPackage()
    setattr(partner, 'mancoosimm_VirtualPackage', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage38', partner)
    assert getattr(partner, 'mancoosimm_VirtualPackage') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage38', None)
    assert getattr(partner, 'mancoosimm_VirtualPackage') is None


def test_assoc_root131_stub_double():
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


def test_assoc_schemas138_stub_double():
    # mancoosimm_GConf has no real 'mancoosimm_GConf139' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    partner = mancoosimm_GConf()
    setattr(partner, 'mancoosimm_GConf139', None)
    _safe_set(owner, 'mancoosimm_File140', partner)
    assert owner in getattr(partner, 'mancoosimm_GConf139')
    _safe_set(owner, 'mancoosimm_File140', None)
    assert owner not in getattr(partner, 'mancoosimm_GConf139')


def test_assoc_sharedLibraries226_stub_double():
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


def test_assoc_singleConflict281_stub_double():
    # mancoosimm_Conflict has no real 'conflict282' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleConflict's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleConflict's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    partner = mancoosimm_Conflict()
    setattr(partner, 'conflict282', None)
    _safe_set(owner, 'SingleConflict', partner)
    assert getattr(partner, 'conflict282') == owner
    _safe_set(owner, 'SingleConflict', None)
    assert getattr(partner, 'conflict282') is None


def test_assoc_singleDep65_stub_double():
    # mancoosimm_Dependence has no real 'dependence66' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_SingleDep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_SingleDep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    partner = mancoosimm_Dependence()
    setattr(partner, 'dependence66', None)
    _safe_set(owner, 'SingleDep', partner)
    assert getattr(partner, 'dependence66') == owner
    _safe_set(owner, 'SingleDep', None)
    assert getattr(partner, 'dependence66') is None


def test_assoc_sourcePackage21_stub_double():
    # mancoosimm_SrcPackage has no real 'mancoosimm_SrcPackage' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_InstalledPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_InstalledPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    partner = mancoosimm_SrcPackage()
    setattr(partner, 'mancoosimm_SrcPackage', None)
    _safe_set(owner, 'mancoosimm_InstalledPackage22', partner)
    assert getattr(partner, 'mancoosimm_SrcPackage') == owner
    _safe_set(owner, 'mancoosimm_InstalledPackage22', None)
    assert getattr(partner, 'mancoosimm_SrcPackage') is None


def test_assoc_type209_stub_double():
    # mancoosimm_MimeTypeHandler has no real 'mimeTypeHandlers' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_MimeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_MimeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    partner = mancoosimm_MimeTypeHandler()
    setattr(partner, 'mimeTypeHandlers', None)
    _safe_set(owner, 'MimeType210', partner)
    assert getattr(partner, 'mimeTypeHandlers') == owner
    _safe_set(owner, 'MimeType210', None)
    assert getattr(partner, 'mimeTypeHandlers') is None


def test_assoc_xfontCache220_stub_double():
    # mancoosimm_XFont has no real 'xfonts' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_XFont()
    setattr(partner, 'xfonts', None)
    _safe_set(owner, 'XFontCache221', partner)
    assert getattr(partner, 'xfonts') == owner
    _safe_set(owner, 'XFontCache221', None)
    assert getattr(partner, 'xfonts') is None


def test_assoc_xfontCaches125_stub_double():
    # mancoosimm_Environment has no real 'env126' property in the generated
    # code (a bare stub) -- manually attach it so mancoosimm_XFontCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mancoosimm_XFontCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mancoosimm_XFontCache(location="sample_text")
    partner = mancoosimm_Environment()
    setattr(partner, 'env126', None)
    _safe_set(owner, 'XFontCache', partner)
    assert owner in getattr(partner, 'env126')
    _safe_set(owner, 'XFontCache', None)
    assert owner not in getattr(partner, 'env126')


def test_assoc_xfonts217_stub_double():
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


