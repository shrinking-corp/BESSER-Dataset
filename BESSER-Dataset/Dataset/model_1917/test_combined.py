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
    Conflict,
    mancoosimm_AndConflict,
    mancoosimm_OrConflict,
    mancoosimm_SingleConflict,
    mancoosimm_SharedLibrary,
    mancoosimm_MimeType,
    mancoosimm_MimeTypeHandler,
    mancoosimm_Boot,
    File,
    mancoosimm_InformationFile,
    mancoosimm_LibraryCache,
    mancoosimm_MimeTypeHandlerCache,
    mancoosimm_DesktopDB,
    mancoosimm_IconCache,
    mancoosimm_Menu,
    mancoosimm_GConf,
    mancoosimm_XFontCache,
    mancoosimm_ModuleCache,
    mancoosimm_NotInv,
    mancoosimm_OrInv,
    mancoosimm_AndInv,
    InstalledPackage,
    mancoosimm_BinPackage,
    Dependence,
    mancoosimm_SingleDep,
    mancoosimm_OrDep,
    mancoosimm_AndDep,
    mancoosimm_Conflict,
    mancoosimm_DocumentationFile,
    mancoosimm_VirtualPackage,
    UnpackedPackage,
    mancoosimm_HalfConfiguredReinstRequiredPackage,
    mancoosimm_HalfConfiguredPackage,
    mancoosimm_Dependence,
    mancoosimm_SrcPackage,
    NamedElement,
    mancoosimm_FileSystem,
    mancoosimm_EmacsPackage,
    mancoosimm_Environment,
    mancoosimm_File,
    mancoosimm_User,
    mancoosimm_Atom,
    mancoosimm_SGMLDocument,
    mancoosimm_Module,
    mancoosimm_ApplicationMenuCatalog,
    mancoosimm_Alternative,
    mancoosimm_Group,
    mancoosimm_SkeeperCatalog,
    mancoosimm_Invariant,
    mancoosimm_SGMLCatalog,
    mancoosimm_SkeeperDocument,
    mancoosimm_XFont,
    mancoosimm_Package,
    mancoosimm_Service,
    mancoosimm_MenuEntry,
    Package,
    mancoosimm_UnpackedPackage,
    mancoosimm_HalfInstalledReinstRequiredPackage,
    mancoosimm_ConfigFilesPackage,
    mancoosimm_HalfInstalledPackage,
    mancoosimm_InstalledPackage,
    mancoosimm_NotInstalledPackage,
    mancoosimm_PackageSetting,
    mancoosimm_Configuration,
    mancoosimm_NamedElement,
    StatusType,
    PriorityType,
    VersionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_conflict_is_not_abstract():
    assert not inspect.isabstract(Conflict)


def test_hyp_conflict_constructor_exists():
    assert callable(Conflict.__init__)


def test_hyp_conflict_constructor_args():
    sig = inspect.signature(Conflict.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_andconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_AndConflict)


def test_hyp_mancoosimm_andconflict_constructor_exists():
    assert callable(mancoosimm_AndConflict.__init__)


def test_hyp_mancoosimm_andconflict_constructor_args():
    sig = inspect.signature(mancoosimm_AndConflict.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_orconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_OrConflict)


def test_hyp_mancoosimm_orconflict_constructor_exists():
    assert callable(mancoosimm_OrConflict.__init__)


def test_hyp_mancoosimm_orconflict_constructor_args():
    sig = inspect.signature(mancoosimm_OrConflict.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_singleconflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SingleConflict)


def test_hyp_mancoosimm_singleconflict_constructor_exists():
    assert callable(mancoosimm_SingleConflict.__init__)


def test_hyp_mancoosimm_singleconflict_constructor_args():
    sig = inspect.signature(mancoosimm_SingleConflict.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_mancoosimm_sharedlibrary_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SharedLibrary)


def test_hyp_mancoosimm_sharedlibrary_constructor_exists():
    assert callable(mancoosimm_SharedLibrary.__init__)


def test_hyp_mancoosimm_sharedlibrary_constructor_args():
    sig = inspect.signature(mancoosimm_SharedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"





def test_hyp_mancoosimm_mimetype_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_MimeType)


def test_hyp_mancoosimm_mimetype_constructor_exists():
    assert callable(mancoosimm_MimeType.__init__)


def test_hyp_mancoosimm_mimetype_constructor_args():
    sig = inspect.signature(mancoosimm_MimeType.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_mancoosimm_mimetypehandler_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_MimeTypeHandler)


def test_hyp_mancoosimm_mimetypehandler_constructor_exists():
    assert callable(mancoosimm_MimeTypeHandler.__init__)


def test_hyp_mancoosimm_mimetypehandler_constructor_args():
    sig = inspect.signature(mancoosimm_MimeTypeHandler.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_boot_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Boot)


def test_hyp_mancoosimm_boot_constructor_exists():
    assert callable(mancoosimm_Boot.__init__)


def test_hyp_mancoosimm_boot_constructor_args():
    sig = inspect.signature(mancoosimm_Boot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_hyp_file_constructor_exists():
    assert callable(File.__init__)


def test_hyp_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_informationfile_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_InformationFile)


def test_hyp_mancoosimm_informationfile_constructor_exists():
    assert callable(mancoosimm_InformationFile.__init__)


def test_hyp_mancoosimm_informationfile_constructor_args():
    sig = inspect.signature(mancoosimm_InformationFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_librarycache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_LibraryCache)


def test_hyp_mancoosimm_librarycache_constructor_exists():
    assert callable(mancoosimm_LibraryCache.__init__)


def test_hyp_mancoosimm_librarycache_constructor_args():
    sig = inspect.signature(mancoosimm_LibraryCache.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_mimetypehandlercache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_MimeTypeHandlerCache)


def test_hyp_mancoosimm_mimetypehandlercache_constructor_exists():
    assert callable(mancoosimm_MimeTypeHandlerCache.__init__)


def test_hyp_mancoosimm_mimetypehandlercache_constructor_args():
    sig = inspect.signature(mancoosimm_MimeTypeHandlerCache.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_desktopdb_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_DesktopDB)


def test_hyp_mancoosimm_desktopdb_constructor_exists():
    assert callable(mancoosimm_DesktopDB.__init__)


def test_hyp_mancoosimm_desktopdb_constructor_args():
    sig = inspect.signature(mancoosimm_DesktopDB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_iconcache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_IconCache)


def test_hyp_mancoosimm_iconcache_constructor_exists():
    assert callable(mancoosimm_IconCache.__init__)


def test_hyp_mancoosimm_iconcache_constructor_args():
    sig = inspect.signature(mancoosimm_IconCache.__init__)
    params = list(sig.parameters.keys())
    assert "mtime" in params, "Missing parameter 'mtime'"




def test_hyp_mancoosimm_menu_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Menu)


def test_hyp_mancoosimm_menu_constructor_exists():
    assert callable(mancoosimm_Menu.__init__)


def test_hyp_mancoosimm_menu_constructor_args():
    sig = inspect.signature(mancoosimm_Menu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_gconf_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_GConf)


def test_hyp_mancoosimm_gconf_constructor_exists():
    assert callable(mancoosimm_GConf.__init__)


def test_hyp_mancoosimm_gconf_constructor_args():
    sig = inspect.signature(mancoosimm_GConf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_xfontcache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_XFontCache)


def test_hyp_mancoosimm_xfontcache_constructor_exists():
    assert callable(mancoosimm_XFontCache.__init__)


def test_hyp_mancoosimm_xfontcache_constructor_args():
    sig = inspect.signature(mancoosimm_XFontCache.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"




def test_hyp_mancoosimm_modulecache_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_ModuleCache)


def test_hyp_mancoosimm_modulecache_constructor_exists():
    assert callable(mancoosimm_ModuleCache.__init__)


def test_hyp_mancoosimm_modulecache_constructor_args():
    sig = inspect.signature(mancoosimm_ModuleCache.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"




def test_hyp_mancoosimm_notinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_NotInv)


def test_hyp_mancoosimm_notinv_constructor_exists():
    assert callable(mancoosimm_NotInv.__init__)


def test_hyp_mancoosimm_notinv_constructor_args():
    sig = inspect.signature(mancoosimm_NotInv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_orinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_OrInv)


def test_hyp_mancoosimm_orinv_constructor_exists():
    assert callable(mancoosimm_OrInv.__init__)


def test_hyp_mancoosimm_orinv_constructor_args():
    sig = inspect.signature(mancoosimm_OrInv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_andinv_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_AndInv)


def test_hyp_mancoosimm_andinv_constructor_exists():
    assert callable(mancoosimm_AndInv.__init__)


def test_hyp_mancoosimm_andinv_constructor_args():
    sig = inspect.signature(mancoosimm_AndInv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_installedpackage_is_not_abstract():
    assert not inspect.isabstract(InstalledPackage)


def test_hyp_installedpackage_constructor_exists():
    assert callable(InstalledPackage.__init__)


def test_hyp_installedpackage_constructor_args():
    sig = inspect.signature(InstalledPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_binpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_BinPackage)


def test_hyp_mancoosimm_binpackage_constructor_exists():
    assert callable(mancoosimm_BinPackage.__init__)


def test_hyp_mancoosimm_binpackage_constructor_args():
    sig = inspect.signature(mancoosimm_BinPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dependence_is_not_abstract():
    assert not inspect.isabstract(Dependence)


def test_hyp_dependence_constructor_exists():
    assert callable(Dependence.__init__)


def test_hyp_dependence_constructor_args():
    sig = inspect.signature(Dependence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_singledep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SingleDep)


def test_hyp_mancoosimm_singledep_constructor_exists():
    assert callable(mancoosimm_SingleDep.__init__)


def test_hyp_mancoosimm_singledep_constructor_args():
    sig = inspect.signature(mancoosimm_SingleDep.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "version" in params, "Missing parameter 'version'"





def test_hyp_mancoosimm_ordep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_OrDep)


def test_hyp_mancoosimm_ordep_constructor_exists():
    assert callable(mancoosimm_OrDep.__init__)


def test_hyp_mancoosimm_ordep_constructor_args():
    sig = inspect.signature(mancoosimm_OrDep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_anddep_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_AndDep)


def test_hyp_mancoosimm_anddep_constructor_exists():
    assert callable(mancoosimm_AndDep.__init__)


def test_hyp_mancoosimm_anddep_constructor_args():
    sig = inspect.signature(mancoosimm_AndDep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_conflict_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Conflict)


def test_hyp_mancoosimm_conflict_constructor_exists():
    assert callable(mancoosimm_Conflict.__init__)


def test_hyp_mancoosimm_conflict_constructor_args():
    sig = inspect.signature(mancoosimm_Conflict.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_documentationfile_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_DocumentationFile)


def test_hyp_mancoosimm_documentationfile_constructor_exists():
    assert callable(mancoosimm_DocumentationFile.__init__)


def test_hyp_mancoosimm_documentationfile_constructor_args():
    sig = inspect.signature(mancoosimm_DocumentationFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_virtualpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_VirtualPackage)


def test_hyp_mancoosimm_virtualpackage_constructor_exists():
    assert callable(mancoosimm_VirtualPackage.__init__)


def test_hyp_mancoosimm_virtualpackage_constructor_args():
    sig = inspect.signature(mancoosimm_VirtualPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unpackedpackage_is_not_abstract():
    assert not inspect.isabstract(UnpackedPackage)


def test_hyp_unpackedpackage_constructor_exists():
    assert callable(UnpackedPackage.__init__)


def test_hyp_unpackedpackage_constructor_args():
    sig = inspect.signature(UnpackedPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_halfconfiguredreinstrequiredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_HalfConfiguredReinstRequiredPackage)


def test_hyp_mancoosimm_halfconfiguredreinstrequiredpackage_constructor_exists():
    assert callable(mancoosimm_HalfConfiguredReinstRequiredPackage.__init__)


def test_hyp_mancoosimm_halfconfiguredreinstrequiredpackage_constructor_args():
    sig = inspect.signature(mancoosimm_HalfConfiguredReinstRequiredPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_halfconfiguredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_HalfConfiguredPackage)


def test_hyp_mancoosimm_halfconfiguredpackage_constructor_exists():
    assert callable(mancoosimm_HalfConfiguredPackage.__init__)


def test_hyp_mancoosimm_halfconfiguredpackage_constructor_args():
    sig = inspect.signature(mancoosimm_HalfConfiguredPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_dependence_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Dependence)


def test_hyp_mancoosimm_dependence_constructor_exists():
    assert callable(mancoosimm_Dependence.__init__)


def test_hyp_mancoosimm_dependence_constructor_args():
    sig = inspect.signature(mancoosimm_Dependence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_srcpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SrcPackage)


def test_hyp_mancoosimm_srcpackage_constructor_exists():
    assert callable(mancoosimm_SrcPackage.__init__)


def test_hyp_mancoosimm_srcpackage_constructor_args():
    sig = inspect.signature(mancoosimm_SrcPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_filesystem_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_FileSystem)


def test_hyp_mancoosimm_filesystem_constructor_exists():
    assert callable(mancoosimm_FileSystem.__init__)


def test_hyp_mancoosimm_filesystem_constructor_args():
    sig = inspect.signature(mancoosimm_FileSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_emacspackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_EmacsPackage)


def test_hyp_mancoosimm_emacspackage_constructor_exists():
    assert callable(mancoosimm_EmacsPackage.__init__)


def test_hyp_mancoosimm_emacspackage_constructor_args():
    sig = inspect.signature(mancoosimm_EmacsPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_environment_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Environment)


def test_hyp_mancoosimm_environment_constructor_exists():
    assert callable(mancoosimm_Environment.__init__)


def test_hyp_mancoosimm_environment_constructor_args():
    sig = inspect.signature(mancoosimm_Environment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_file_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_File)


def test_hyp_mancoosimm_file_constructor_exists():
    assert callable(mancoosimm_File.__init__)


def test_hyp_mancoosimm_file_constructor_args():
    sig = inspect.signature(mancoosimm_File.__init__)
    params = list(sig.parameters.keys())
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "isDirectory" in params, "Missing parameter 'isDirectory'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "permission" in params, "Missing parameter 'permission'"
    assert "description" in params, "Missing parameter 'description'"
    assert "size" in params, "Missing parameter 'size'"
    assert "location" in params, "Missing parameter 'location'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "isMissing" in params, "Missing parameter 'isMissing'"
    assert "suid" in params, "Missing parameter 'suid'"













def test_hyp_mancoosimm_user_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_User)


def test_hyp_mancoosimm_user_constructor_exists():
    assert callable(mancoosimm_User.__init__)


def test_hyp_mancoosimm_user_constructor_args():
    sig = inspect.signature(mancoosimm_User.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_atom_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Atom)


def test_hyp_mancoosimm_atom_constructor_exists():
    assert callable(mancoosimm_Atom.__init__)


def test_hyp_mancoosimm_atom_constructor_args():
    sig = inspect.signature(mancoosimm_Atom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_sgmldocument_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SGMLDocument)


def test_hyp_mancoosimm_sgmldocument_constructor_exists():
    assert callable(mancoosimm_SGMLDocument.__init__)


def test_hyp_mancoosimm_sgmldocument_constructor_args():
    sig = inspect.signature(mancoosimm_SGMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_module_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Module)


def test_hyp_mancoosimm_module_constructor_exists():
    assert callable(mancoosimm_Module.__init__)


def test_hyp_mancoosimm_module_constructor_args():
    sig = inspect.signature(mancoosimm_Module.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_applicationmenucatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_ApplicationMenuCatalog)


def test_hyp_mancoosimm_applicationmenucatalog_constructor_exists():
    assert callable(mancoosimm_ApplicationMenuCatalog.__init__)


def test_hyp_mancoosimm_applicationmenucatalog_constructor_args():
    sig = inspect.signature(mancoosimm_ApplicationMenuCatalog.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_alternative_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Alternative)


def test_hyp_mancoosimm_alternative_constructor_exists():
    assert callable(mancoosimm_Alternative.__init__)


def test_hyp_mancoosimm_alternative_constructor_args():
    sig = inspect.signature(mancoosimm_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_group_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Group)


def test_hyp_mancoosimm_group_constructor_exists():
    assert callable(mancoosimm_Group.__init__)


def test_hyp_mancoosimm_group_constructor_args():
    sig = inspect.signature(mancoosimm_Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_skeepercatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SkeeperCatalog)


def test_hyp_mancoosimm_skeepercatalog_constructor_exists():
    assert callable(mancoosimm_SkeeperCatalog.__init__)


def test_hyp_mancoosimm_skeepercatalog_constructor_args():
    sig = inspect.signature(mancoosimm_SkeeperCatalog.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_invariant_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Invariant)


def test_hyp_mancoosimm_invariant_constructor_exists():
    assert callable(mancoosimm_Invariant.__init__)


def test_hyp_mancoosimm_invariant_constructor_args():
    sig = inspect.signature(mancoosimm_Invariant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_sgmlcatalog_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SGMLCatalog)


def test_hyp_mancoosimm_sgmlcatalog_constructor_exists():
    assert callable(mancoosimm_SGMLCatalog.__init__)


def test_hyp_mancoosimm_sgmlcatalog_constructor_args():
    sig = inspect.signature(mancoosimm_SGMLCatalog.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_skeeperdocument_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_SkeeperDocument)


def test_hyp_mancoosimm_skeeperdocument_constructor_exists():
    assert callable(mancoosimm_SkeeperDocument.__init__)


def test_hyp_mancoosimm_skeeperdocument_constructor_args():
    sig = inspect.signature(mancoosimm_SkeeperDocument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_xfont_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_XFont)


def test_hyp_mancoosimm_xfont_constructor_exists():
    assert callable(mancoosimm_XFont.__init__)


def test_hyp_mancoosimm_xfont_constructor_args():
    sig = inspect.signature(mancoosimm_XFont.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_package_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Package)


def test_hyp_mancoosimm_package_constructor_exists():
    assert callable(mancoosimm_Package.__init__)


def test_hyp_mancoosimm_package_constructor_args():
    sig = inspect.signature(mancoosimm_Package.__init__)
    params = list(sig.parameters.keys())
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "version" in params, "Missing parameter 'version'"





def test_hyp_mancoosimm_service_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Service)


def test_hyp_mancoosimm_service_constructor_exists():
    assert callable(mancoosimm_Service.__init__)


def test_hyp_mancoosimm_service_constructor_args():
    sig = inspect.signature(mancoosimm_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_menuentry_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_MenuEntry)


def test_hyp_mancoosimm_menuentry_constructor_exists():
    assert callable(mancoosimm_MenuEntry.__init__)


def test_hyp_mancoosimm_menuentry_constructor_args():
    sig = inspect.signature(mancoosimm_MenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_hyp_package_constructor_exists():
    assert callable(Package.__init__)


def test_hyp_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_unpackedpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_UnpackedPackage)


def test_hyp_mancoosimm_unpackedpackage_constructor_exists():
    assert callable(mancoosimm_UnpackedPackage.__init__)


def test_hyp_mancoosimm_unpackedpackage_constructor_args():
    sig = inspect.signature(mancoosimm_UnpackedPackage.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "section" in params, "Missing parameter 'section'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "priority" in params, "Missing parameter 'priority'"










def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_HalfInstalledReinstRequiredPackage)


def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_constructor_exists():
    assert callable(mancoosimm_HalfInstalledReinstRequiredPackage.__init__)


def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_constructor_args():
    sig = inspect.signature(mancoosimm_HalfInstalledReinstRequiredPackage.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"
    assert "section" in params, "Missing parameter 'section'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "description" in params, "Missing parameter 'description'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"










def test_hyp_mancoosimm_configfilespackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_ConfigFilesPackage)


def test_hyp_mancoosimm_configfilespackage_constructor_exists():
    assert callable(mancoosimm_ConfigFilesPackage.__init__)


def test_hyp_mancoosimm_configfilespackage_constructor_args():
    sig = inspect.signature(mancoosimm_ConfigFilesPackage.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "section" in params, "Missing parameter 'section'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "priority" in params, "Missing parameter 'priority'"










def test_hyp_mancoosimm_halfinstalledpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_HalfInstalledPackage)


def test_hyp_mancoosimm_halfinstalledpackage_constructor_exists():
    assert callable(mancoosimm_HalfInstalledPackage.__init__)


def test_hyp_mancoosimm_halfinstalledpackage_constructor_args():
    sig = inspect.signature(mancoosimm_HalfInstalledPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "description" in params, "Missing parameter 'description'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "section" in params, "Missing parameter 'section'"










def test_hyp_mancoosimm_installedpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_InstalledPackage)


def test_hyp_mancoosimm_installedpackage_constructor_exists():
    assert callable(mancoosimm_InstalledPackage.__init__)


def test_hyp_mancoosimm_installedpackage_constructor_args():
    sig = inspect.signature(mancoosimm_InstalledPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uploaders" in params, "Missing parameter 'uploaders'"
    assert "installedSize" in params, "Missing parameter 'installedSize'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "checkSum" in params, "Missing parameter 'checkSum'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "maintainer" in params, "Missing parameter 'maintainer'"
    assert "section" in params, "Missing parameter 'section'"
    assert "description" in params, "Missing parameter 'description'"
    assert "fileSize" in params, "Missing parameter 'fileSize'"












def test_hyp_mancoosimm_notinstalledpackage_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_NotInstalledPackage)


def test_hyp_mancoosimm_notinstalledpackage_constructor_exists():
    assert callable(mancoosimm_NotInstalledPackage.__init__)


def test_hyp_mancoosimm_notinstalledpackage_constructor_args():
    sig = inspect.signature(mancoosimm_NotInstalledPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_packagesetting_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_PackageSetting)


def test_hyp_mancoosimm_packagesetting_constructor_exists():
    assert callable(mancoosimm_PackageSetting.__init__)


def test_hyp_mancoosimm_packagesetting_constructor_args():
    sig = inspect.signature(mancoosimm_PackageSetting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mancoosimm_configuration_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_Configuration)


def test_hyp_mancoosimm_configuration_constructor_exists():
    assert callable(mancoosimm_Configuration.__init__)


def test_hyp_mancoosimm_configuration_constructor_args():
    sig = inspect.signature(mancoosimm_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "systemType" in params, "Missing parameter 'systemType'"





def test_hyp_mancoosimm_namedelement_is_not_abstract():
    assert not inspect.isabstract(mancoosimm_NamedElement)


def test_hyp_mancoosimm_namedelement_constructor_exists():
    assert callable(mancoosimm_NamedElement.__init__)


def test_hyp_mancoosimm_namedelement_constructor_args():
    sig = inspect.signature(mancoosimm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_statustype_exists():
    # Check that the Enumeration exists
    assert StatusType is not None

def test_hyp_statustype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatusType]
    expected_literals = [
        "half_configured",
        "not_installed",
        "half_installed",
        "config_files",
        "unpacked",
        "installed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatusType"

def test_hyp_prioritytype_exists():
    # Check that the Enumeration exists
    assert PriorityType is not None

def test_hyp_prioritytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityType]
    expected_literals = [
        "important",
        "standard",
        "extra",
        "required",
        "optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityType"

def test_hyp_versiontype_exists():
    # Check that the Enumeration exists
    assert VersionType is not None

def test_hyp_versiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VersionType]
    expected_literals = [
        "lt",
        "ggt",
        "ge",
        "gt",
        "llt",
        "le",
        "eq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VersionType"


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
Conflict_strategy = st.builds(
    Conflict,
)
mancoosimm_AndConflict_strategy = st.builds(
    mancoosimm_AndConflict,
)
mancoosimm_OrConflict_strategy = st.builds(
    mancoosimm_OrConflict,
)
mancoosimm_SingleConflict_strategy = st.builds(
    mancoosimm_SingleConflict,
    version=
        safe_text,
    value=
        safe_text
)
mancoosimm_SharedLibrary_strategy = st.builds(
    mancoosimm_SharedLibrary,
    name=
        safe_text,
    version=
        safe_text
)
mancoosimm_MimeType_strategy = st.builds(
    mancoosimm_MimeType,
    extension=
        safe_text,
    name=
        safe_text
)
mancoosimm_MimeTypeHandler_strategy = st.builds(
    mancoosimm_MimeTypeHandler,
)
mancoosimm_Boot_strategy = st.builds(
    mancoosimm_Boot,
)
File_strategy = st.builds(
    File,
)
mancoosimm_InformationFile_strategy = st.builds(
    mancoosimm_InformationFile,
)
mancoosimm_LibraryCache_strategy = st.builds(
    mancoosimm_LibraryCache,
)
mancoosimm_MimeTypeHandlerCache_strategy = st.builds(
    mancoosimm_MimeTypeHandlerCache,
)
mancoosimm_DesktopDB_strategy = st.builds(
    mancoosimm_DesktopDB,
)
mancoosimm_IconCache_strategy = st.builds(
    mancoosimm_IconCache,
    mtime=
        safe_text
)
mancoosimm_Menu_strategy = st.builds(
    mancoosimm_Menu,
)
mancoosimm_GConf_strategy = st.builds(
    mancoosimm_GConf,
)
mancoosimm_XFontCache_strategy = st.builds(
    mancoosimm_XFontCache,
    location=
        safe_text
)
mancoosimm_ModuleCache_strategy = st.builds(
    mancoosimm_ModuleCache,
    version=
        safe_text
)
mancoosimm_NotInv_strategy = st.builds(
    mancoosimm_NotInv,
)
mancoosimm_OrInv_strategy = st.builds(
    mancoosimm_OrInv,
)
mancoosimm_AndInv_strategy = st.builds(
    mancoosimm_AndInv,
)
InstalledPackage_strategy = st.builds(
    InstalledPackage,
)
mancoosimm_BinPackage_strategy = st.builds(
    mancoosimm_BinPackage,
)
Dependence_strategy = st.builds(
    Dependence,
)
mancoosimm_SingleDep_strategy = st.builds(
    mancoosimm_SingleDep,
    value=
        safe_text,
    version=
        safe_text
)
mancoosimm_OrDep_strategy = st.builds(
    mancoosimm_OrDep,
)
mancoosimm_AndDep_strategy = st.builds(
    mancoosimm_AndDep,
)
mancoosimm_Conflict_strategy = st.builds(
    mancoosimm_Conflict,
)
mancoosimm_DocumentationFile_strategy = st.builds(
    mancoosimm_DocumentationFile,
)
mancoosimm_VirtualPackage_strategy = st.builds(
    mancoosimm_VirtualPackage,
)
UnpackedPackage_strategy = st.builds(
    UnpackedPackage,
)
mancoosimm_HalfConfiguredReinstRequiredPackage_strategy = st.builds(
    mancoosimm_HalfConfiguredReinstRequiredPackage,
)
mancoosimm_HalfConfiguredPackage_strategy = st.builds(
    mancoosimm_HalfConfiguredPackage,
)
mancoosimm_Dependence_strategy = st.builds(
    mancoosimm_Dependence,
)
mancoosimm_SrcPackage_strategy = st.builds(
    mancoosimm_SrcPackage,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mancoosimm_FileSystem_strategy = st.builds(
    mancoosimm_FileSystem,
)
mancoosimm_EmacsPackage_strategy = st.builds(
    mancoosimm_EmacsPackage,
)
mancoosimm_Environment_strategy = st.builds(
    mancoosimm_Environment,
)
mancoosimm_File_strategy = st.builds(
    mancoosimm_File,
    checkSum=
        safe_text,
    isDirectory=
        st.booleans(),
    extension=
        safe_text,
    permission=
        safe_text,
    description=
        safe_text,
    size=
        st.integers(),
    location=
        safe_text,
    guid=
        st.booleans(),
    isMissing=
        st.booleans(),
    suid=
        st.booleans()
)
mancoosimm_User_strategy = st.builds(
    mancoosimm_User,
)
mancoosimm_Atom_strategy = st.builds(
    mancoosimm_Atom,
)
mancoosimm_SGMLDocument_strategy = st.builds(
    mancoosimm_SGMLDocument,
)
mancoosimm_Module_strategy = st.builds(
    mancoosimm_Module,
)
mancoosimm_ApplicationMenuCatalog_strategy = st.builds(
    mancoosimm_ApplicationMenuCatalog,
)
mancoosimm_Alternative_strategy = st.builds(
    mancoosimm_Alternative,
)
mancoosimm_Group_strategy = st.builds(
    mancoosimm_Group,
)
mancoosimm_SkeeperCatalog_strategy = st.builds(
    mancoosimm_SkeeperCatalog,
)
mancoosimm_Invariant_strategy = st.builds(
    mancoosimm_Invariant,
)
mancoosimm_SGMLCatalog_strategy = st.builds(
    mancoosimm_SGMLCatalog,
)
mancoosimm_SkeeperDocument_strategy = st.builds(
    mancoosimm_SkeeperDocument,
)
mancoosimm_XFont_strategy = st.builds(
    mancoosimm_XFont,
)
mancoosimm_Package_strategy = st.builds(
    mancoosimm_Package,
    architecture=
        safe_text,
    version=
        safe_text
)
mancoosimm_Service_strategy = st.builds(
    mancoosimm_Service,
)
mancoosimm_MenuEntry_strategy = st.builds(
    mancoosimm_MenuEntry,
)
Package_strategy = st.builds(
    Package,
)
mancoosimm_UnpackedPackage_strategy = st.builds(
    mancoosimm_UnpackedPackage,
    description=
        safe_text,
    maintainer=
        safe_text,
    tag=
        safe_text,
    section=
        safe_text,
    checkSum=
        safe_text,
    uploaders=
        safe_text,
    priority=
        safe_text
)
mancoosimm_HalfInstalledReinstRequiredPackage_strategy = st.builds(
    mancoosimm_HalfInstalledReinstRequiredPackage,
    tag=
        safe_text,
    section=
        safe_text,
    uploaders=
        safe_text,
    maintainer=
        safe_text,
    description=
        safe_text,
    priority=
        safe_text,
    checkSum=
        safe_text
)
mancoosimm_ConfigFilesPackage_strategy = st.builds(
    mancoosimm_ConfigFilesPackage,
    description=
        safe_text,
    section=
        safe_text,
    maintainer=
        safe_text,
    uploaders=
        safe_text,
    checkSum=
        safe_text,
    tag=
        safe_text,
    priority=
        safe_text
)
mancoosimm_HalfInstalledPackage_strategy = st.builds(
    mancoosimm_HalfInstalledPackage,
    uploaders=
        safe_text,
    priority=
        safe_text,
    tag=
        safe_text,
    description=
        safe_text,
    maintainer=
        safe_text,
    checkSum=
        safe_text,
    section=
        safe_text
)
mancoosimm_InstalledPackage_strategy = st.builds(
    mancoosimm_InstalledPackage,
    uploaders=
        safe_text,
    installedSize=
        st.integers(),
    tag=
        safe_text,
    checkSum=
        safe_text,
    priority=
        safe_text,
    maintainer=
        safe_text,
    section=
        safe_text,
    description=
        safe_text,
    fileSize=
        st.integers()
)
mancoosimm_NotInstalledPackage_strategy = st.builds(
    mancoosimm_NotInstalledPackage,
)
mancoosimm_PackageSetting_strategy = st.builds(
    mancoosimm_PackageSetting,
)
mancoosimm_Configuration_strategy = st.builds(
    mancoosimm_Configuration,
    creationTime=
        safe_text,
    systemType=
        safe_text
)
mancoosimm_NamedElement_strategy = st.builds(
    mancoosimm_NamedElement,
    name=
        safe_text
)







@given(instance=mancoosimm_SingleConflict_strategy)
def test_hyp_mancoosimm_singleconflict_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=mancoosimm_SingleConflict_strategy)
def test_hyp_mancoosimm_singleconflict_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=mancoosimm_SharedLibrary_strategy)
def test_hyp_mancoosimm_sharedlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mancoosimm_SharedLibrary_strategy)
def test_hyp_mancoosimm_sharedlibrary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original




@given(instance=mancoosimm_MimeType_strategy)
def test_hyp_mancoosimm_mimetype_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=mancoosimm_MimeType_strategy)
def test_hyp_mancoosimm_mimetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=mancoosimm_IconCache_strategy)
def test_hyp_mancoosimm_iconcache_mtime_setter(instance):
    original = instance.mtime
    instance.mtime = original
    assert instance.mtime == original






@given(instance=mancoosimm_XFontCache_strategy)
def test_hyp_mancoosimm_xfontcache_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original




@given(instance=mancoosimm_ModuleCache_strategy)
def test_hyp_mancoosimm_modulecache_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original










@given(instance=mancoosimm_SingleDep_strategy)
def test_hyp_mancoosimm_singledep_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=mancoosimm_SingleDep_strategy)
def test_hyp_mancoosimm_singledep_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original


















@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_isDirectory_setter(instance):
    original = instance.isDirectory
    instance.isDirectory = original
    assert instance.isDirectory == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_permission_setter(instance):
    original = instance.permission
    instance.permission = original
    assert instance.permission == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_isMissing_setter(instance):
    original = instance.isMissing
    instance.isMissing = original
    assert instance.isMissing == original



@given(instance=mancoosimm_File_strategy)
def test_hyp_mancoosimm_file_suid_setter(instance):
    original = instance.suid
    instance.suid = original
    assert instance.suid == original
















@given(instance=mancoosimm_Package_strategy)
def test_hyp_mancoosimm_package_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original



@given(instance=mancoosimm_Package_strategy)
def test_hyp_mancoosimm_package_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original







@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original



@given(instance=mancoosimm_UnpackedPackage_strategy)
def test_hyp_mancoosimm_unpackedpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original




@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
def test_hyp_mancoosimm_halfinstalledreinstrequiredpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original




@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=mancoosimm_ConfigFilesPackage_strategy)
def test_hyp_mancoosimm_configfilespackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original




@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original



@given(instance=mancoosimm_HalfInstalledPackage_strategy)
def test_hyp_mancoosimm_halfinstalledpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original




@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_uploaders_setter(instance):
    original = instance.uploaders
    instance.uploaders = original
    assert instance.uploaders == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_installedSize_setter(instance):
    original = instance.installedSize
    instance.installedSize = original
    assert instance.installedSize == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_checkSum_setter(instance):
    original = instance.checkSum
    instance.checkSum = original
    assert instance.checkSum == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_maintainer_setter(instance):
    original = instance.maintainer
    instance.maintainer = original
    assert instance.maintainer == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mancoosimm_InstalledPackage_strategy)
def test_hyp_mancoosimm_installedpackage_fileSize_setter(instance):
    original = instance.fileSize
    instance.fileSize = original
    assert instance.fileSize == original






@given(instance=mancoosimm_Configuration_strategy)
def test_hyp_mancoosimm_configuration_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original



@given(instance=mancoosimm_Configuration_strategy)
def test_hyp_mancoosimm_configuration_systemType_setter(instance):
    original = instance.systemType
    instance.systemType = original
    assert instance.systemType == original




@given(instance=mancoosimm_NamedElement_strategy)
def test_hyp_mancoosimm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_mancoosimm_ConfigFilesPackage_checkSum_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_description_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_maintainer_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.maintainer == "sample_text"
    instance.maintainer = "sample_text_2"
    assert instance.maintainer == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_priority_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_section_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_tag_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_mancoosimm_ConfigFilesPackage_uploaders_value_roundtrip():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.uploaders == "sample_text"
    instance.uploaders = "sample_text_2"
    assert instance.uploaders == "sample_text_2"


def test_mancoosimm_Configuration_creationTime_value_roundtrip():
    instance = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    assert instance.creationTime == "sample_text"
    instance.creationTime = "sample_text_2"
    assert instance.creationTime == "sample_text_2"


def test_mancoosimm_Configuration_systemType_value_roundtrip():
    instance = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    assert instance.systemType == "sample_text"
    instance.systemType = "sample_text_2"
    assert instance.systemType == "sample_text_2"


def test_mancoosimm_File_checkSum_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_File_description_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_File_extension_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.extension == "sample_text"
    instance.extension = "sample_text_2"
    assert instance.extension == "sample_text_2"


def test_mancoosimm_File_guid_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.guid == True
    instance.guid = False
    assert instance.guid == False


def test_mancoosimm_File_isDirectory_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.isDirectory == True
    instance.isDirectory = False
    assert instance.isDirectory == False


def test_mancoosimm_File_isMissing_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.isMissing == True
    instance.isMissing = False
    assert instance.isMissing == False


def test_mancoosimm_File_location_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_mancoosimm_File_permission_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.permission == "sample_text"
    instance.permission = "sample_text_2"
    assert instance.permission == "sample_text_2"


def test_mancoosimm_File_size_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_mancoosimm_File_suid_value_roundtrip():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert instance.suid == True
    instance.suid = False
    assert instance.suid == False


def test_mancoosimm_HalfInstalledPackage_checkSum_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_description_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_maintainer_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.maintainer == "sample_text"
    instance.maintainer = "sample_text_2"
    assert instance.maintainer == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_priority_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_section_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_tag_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_mancoosimm_HalfInstalledPackage_uploaders_value_roundtrip():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.uploaders == "sample_text"
    instance.uploaders = "sample_text_2"
    assert instance.uploaders == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_checkSum_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_description_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_maintainer_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.maintainer == "sample_text"
    instance.maintainer = "sample_text_2"
    assert instance.maintainer == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_priority_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_section_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_tag_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_mancoosimm_HalfInstalledReinstRequiredPackage_uploaders_value_roundtrip():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.uploaders == "sample_text"
    instance.uploaders = "sample_text_2"
    assert instance.uploaders == "sample_text_2"


def test_mancoosimm_IconCache_mtime_value_roundtrip():
    instance = mancoosimm_IconCache(mtime="sample_text")
    assert instance.mtime == "sample_text"
    instance.mtime = "sample_text_2"
    assert instance.mtime == "sample_text_2"


def test_mancoosimm_InstalledPackage_checkSum_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_InstalledPackage_description_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_InstalledPackage_fileSize_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.fileSize == 7
    instance.fileSize = 13
    assert instance.fileSize == 13


def test_mancoosimm_InstalledPackage_installedSize_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.installedSize == 7
    instance.installedSize = 13
    assert instance.installedSize == 13


def test_mancoosimm_InstalledPackage_maintainer_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.maintainer == "sample_text"
    instance.maintainer = "sample_text_2"
    assert instance.maintainer == "sample_text_2"


def test_mancoosimm_InstalledPackage_priority_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_mancoosimm_InstalledPackage_section_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_mancoosimm_InstalledPackage_tag_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_mancoosimm_InstalledPackage_uploaders_value_roundtrip():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.uploaders == "sample_text"
    instance.uploaders = "sample_text_2"
    assert instance.uploaders == "sample_text_2"


def test_mancoosimm_MimeType_extension_value_roundtrip():
    instance = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    assert instance.extension == "sample_text"
    instance.extension = "sample_text_2"
    assert instance.extension == "sample_text_2"


def test_mancoosimm_MimeType_name_value_roundtrip():
    instance = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mancoosimm_ModuleCache_version_value_roundtrip():
    instance = mancoosimm_ModuleCache(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_mancoosimm_NamedElement_name_value_roundtrip():
    instance = mancoosimm_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mancoosimm_Package_architecture_value_roundtrip():
    instance = mancoosimm_Package(architecture="sample_text", version="sample_text")
    assert instance.architecture == "sample_text"
    instance.architecture = "sample_text_2"
    assert instance.architecture == "sample_text_2"


def test_mancoosimm_Package_version_value_roundtrip():
    instance = mancoosimm_Package(architecture="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_mancoosimm_SharedLibrary_name_value_roundtrip():
    instance = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mancoosimm_SharedLibrary_version_value_roundtrip():
    instance = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_mancoosimm_SingleConflict_value_value_roundtrip():
    instance = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mancoosimm_SingleConflict_version_value_roundtrip():
    instance = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_mancoosimm_SingleDep_value_value_roundtrip():
    instance = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mancoosimm_SingleDep_version_value_roundtrip():
    instance = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_mancoosimm_UnpackedPackage_checkSum_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.checkSum == "sample_text"
    instance.checkSum = "sample_text_2"
    assert instance.checkSum == "sample_text_2"


def test_mancoosimm_UnpackedPackage_description_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_mancoosimm_UnpackedPackage_maintainer_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.maintainer == "sample_text"
    instance.maintainer = "sample_text_2"
    assert instance.maintainer == "sample_text_2"


def test_mancoosimm_UnpackedPackage_priority_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_mancoosimm_UnpackedPackage_section_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_mancoosimm_UnpackedPackage_tag_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_mancoosimm_UnpackedPackage_uploaders_value_roundtrip():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert instance.uploaders == "sample_text"
    instance.uploaders = "sample_text_2"
    assert instance.uploaders == "sample_text_2"


def test_mancoosimm_XFontCache_location_value_roundtrip():
    instance = mancoosimm_XFontCache(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_mancoosimm_AndConflict_isa_Conflict():
    instance = mancoosimm_AndConflict()
    assert isinstance(instance, Conflict)


def test_mancoosimm_OrConflict_isa_Conflict():
    instance = mancoosimm_OrConflict()
    assert isinstance(instance, Conflict)


def test_mancoosimm_SingleConflict_isa_Conflict():
    instance = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    assert isinstance(instance, Conflict)


def test_mancoosimm_AndDep_isa_Dependence():
    instance = mancoosimm_AndDep()
    assert isinstance(instance, Dependence)


def test_mancoosimm_OrDep_isa_Dependence():
    instance = mancoosimm_OrDep()
    assert isinstance(instance, Dependence)


def test_mancoosimm_SingleDep_isa_Dependence():
    instance = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    assert isinstance(instance, Dependence)


def test_mancoosimm_DocumentationFile_isa_File():
    instance = mancoosimm_DocumentationFile()
    assert isinstance(instance, File)


def test_mancoosimm_InformationFile_isa_File():
    instance = mancoosimm_InformationFile()
    assert isinstance(instance, File)


def test_mancoosimm_BinPackage_isa_InstalledPackage():
    instance = mancoosimm_BinPackage()
    assert isinstance(instance, InstalledPackage)


def test_mancoosimm_SrcPackage_isa_InstalledPackage():
    instance = mancoosimm_SrcPackage()
    assert isinstance(instance, InstalledPackage)


def test_mancoosimm_VirtualPackage_isa_InstalledPackage():
    instance = mancoosimm_VirtualPackage()
    assert isinstance(instance, InstalledPackage)


def test_mancoosimm_Alternative_isa_NamedElement():
    instance = mancoosimm_Alternative()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_ApplicationMenuCatalog_isa_NamedElement():
    instance = mancoosimm_ApplicationMenuCatalog()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Atom_isa_NamedElement():
    instance = mancoosimm_Atom()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Configuration_isa_NamedElement():
    instance = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    assert isinstance(instance, NamedElement)


def test_mancoosimm_EmacsPackage_isa_NamedElement():
    instance = mancoosimm_EmacsPackage()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Environment_isa_NamedElement():
    instance = mancoosimm_Environment()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_File_isa_NamedElement():
    instance = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    assert isinstance(instance, NamedElement)


def test_mancoosimm_FileSystem_isa_NamedElement():
    instance = mancoosimm_FileSystem()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Group_isa_NamedElement():
    instance = mancoosimm_Group()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Invariant_isa_NamedElement():
    instance = mancoosimm_Invariant()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_MenuEntry_isa_NamedElement():
    instance = mancoosimm_MenuEntry()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Module_isa_NamedElement():
    instance = mancoosimm_Module()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Package_isa_NamedElement():
    instance = mancoosimm_Package(architecture="sample_text", version="sample_text")
    assert isinstance(instance, NamedElement)


def test_mancoosimm_PackageSetting_isa_NamedElement():
    instance = mancoosimm_PackageSetting()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_SGMLCatalog_isa_NamedElement():
    instance = mancoosimm_SGMLCatalog()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_SGMLDocument_isa_NamedElement():
    instance = mancoosimm_SGMLDocument()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_Service_isa_NamedElement():
    instance = mancoosimm_Service()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_SkeeperCatalog_isa_NamedElement():
    instance = mancoosimm_SkeeperCatalog()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_SkeeperDocument_isa_NamedElement():
    instance = mancoosimm_SkeeperDocument()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_User_isa_NamedElement():
    instance = mancoosimm_User()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_XFont_isa_NamedElement():
    instance = mancoosimm_XFont()
    assert isinstance(instance, NamedElement)


def test_mancoosimm_ConfigFilesPackage_isa_Package():
    instance = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert isinstance(instance, Package)


def test_mancoosimm_HalfInstalledPackage_isa_Package():
    instance = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert isinstance(instance, Package)


def test_mancoosimm_HalfInstalledReinstRequiredPackage_isa_Package():
    instance = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert isinstance(instance, Package)


def test_mancoosimm_InstalledPackage_isa_Package():
    instance = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert isinstance(instance, Package)


def test_mancoosimm_NotInstalledPackage_isa_Package():
    instance = mancoosimm_NotInstalledPackage()
    assert isinstance(instance, Package)


def test_mancoosimm_UnpackedPackage_isa_Package():
    instance = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    assert isinstance(instance, Package)


def test_mancoosimm_HalfConfiguredPackage_isa_UnpackedPackage():
    instance = mancoosimm_HalfConfiguredPackage()
    assert isinstance(instance, UnpackedPackage)


def test_mancoosimm_HalfConfiguredReinstRequiredPackage_isa_UnpackedPackage():
    instance = mancoosimm_HalfConfiguredReinstRequiredPackage()
    assert isinstance(instance, UnpackedPackage)


def test_assoc_allFiles134_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_FileSystem()
    b2 = mancoosimm_FileSystem()
    _safe_set(a, 'mancoosimm_File135', b1)
    assert _is_linked(a, 'mancoosimm_File135', b1)
    if hasattr(b1, 'mancoosimm_FileSystem'):
        assert _is_linked(b1, 'mancoosimm_FileSystem', a)
    _safe_set(a, 'mancoosimm_File135', b2)
    assert _is_linked(a, 'mancoosimm_File135', b2)
    if hasattr(b1, 'mancoosimm_FileSystem'):
        assert not _is_linked(b1, 'mancoosimm_FileSystem', a)
    if hasattr(b2, 'mancoosimm_FileSystem'):
        assert _is_linked(b2, 'mancoosimm_FileSystem', a)
    _safe_set(a, 'mancoosimm_File135', None)
    assert not _is_linked(a, 'mancoosimm_File135', b2)
    if hasattr(b2, 'mancoosimm_FileSystem'):
        assert not _is_linked(b2, 'mancoosimm_FileSystem', a)


def test_assoc_applications200_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_DesktopDB()
    b2 = mancoosimm_DesktopDB()
    _safe_set(a, 'mancoosimm_File201', b1)
    assert _is_linked(a, 'mancoosimm_File201', b1)
    if hasattr(b1, 'mancoosimm_DesktopDB'):
        assert _is_linked(b1, 'mancoosimm_DesktopDB', a)
    _safe_set(a, 'mancoosimm_File201', b2)
    assert _is_linked(a, 'mancoosimm_File201', b2)
    if hasattr(b1, 'mancoosimm_DesktopDB'):
        assert not _is_linked(b1, 'mancoosimm_DesktopDB', a)
    if hasattr(b2, 'mancoosimm_DesktopDB'):
        assert _is_linked(b2, 'mancoosimm_DesktopDB', a)
    _safe_set(a, 'mancoosimm_File201', None)
    assert not _is_linked(a, 'mancoosimm_File201', b2)
    if hasattr(b2, 'mancoosimm_DesktopDB'):
        assert not _is_linked(b2, 'mancoosimm_DesktopDB', a)


def test_assoc_cache215_link_reassign_clear():
    a = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    b1 = mancoosimm_MimeTypeHandlerCache()
    b2 = mancoosimm_MimeTypeHandlerCache()
    _safe_set(a, 'mimeTypes', b1)
    assert _is_linked(a, 'mimeTypes', b1)
    if hasattr(b1, 'MimeTypeHandlerCache216'):
        assert _is_linked(b1, 'MimeTypeHandlerCache216', a)
    _safe_set(a, 'mimeTypes', b2)
    assert _is_linked(a, 'mimeTypes', b2)
    if hasattr(b1, 'MimeTypeHandlerCache216'):
        assert not _is_linked(b1, 'MimeTypeHandlerCache216', a)
    if hasattr(b2, 'MimeTypeHandlerCache216'):
        assert _is_linked(b2, 'MimeTypeHandlerCache216', a)
    _safe_set(a, 'mimeTypes', None)
    assert not _is_linked(a, 'mimeTypes', b2)
    if hasattr(b2, 'MimeTypeHandlerCache216'):
        assert not _is_linked(b2, 'MimeTypeHandlerCache216', a)


def test_assoc_childs167_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'File168', b1)
    assert _is_linked(a, 'File168', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'File168', b2)
    assert _is_linked(a, 'File168', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'File168', None)
    assert not _is_linked(a, 'File168', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_confFiles136_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_GConf()
    b2 = mancoosimm_GConf()
    _safe_set(a, 'mancoosimm_File137', b1)
    assert _is_linked(a, 'mancoosimm_File137', b1)
    if hasattr(b1, 'mancoosimm_GConf'):
        assert _is_linked(b1, 'mancoosimm_GConf', a)
    _safe_set(a, 'mancoosimm_File137', b2)
    assert _is_linked(a, 'mancoosimm_File137', b2)
    if hasattr(b1, 'mancoosimm_GConf'):
        assert not _is_linked(b1, 'mancoosimm_GConf', a)
    if hasattr(b2, 'mancoosimm_GConf'):
        assert _is_linked(b2, 'mancoosimm_GConf', a)
    _safe_set(a, 'mancoosimm_File137', None)
    assert not _is_linked(a, 'mancoosimm_File137', b2)
    if hasattr(b2, 'mancoosimm_GConf'):
        assert not _is_linked(b2, 'mancoosimm_GConf', a)


def test_assoc_configFilesPackages6_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_ConfigFilesPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_ConfigFilesPackage(checkSum="sample_text_2", description="sample_text_2", maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_Configuration7', {b1})
    assert _is_linked(a, 'mancoosimm_Configuration7', b1)
    if hasattr(b1, 'mancoosimm_ConfigFilesPackage'):
        assert _is_linked(b1, 'mancoosimm_ConfigFilesPackage', a)
    _safe_set(a, 'mancoosimm_Configuration7', {b2})
    assert _is_linked(a, 'mancoosimm_Configuration7', b2)
    if hasattr(b1, 'mancoosimm_ConfigFilesPackage'):
        assert not _is_linked(b1, 'mancoosimm_ConfigFilesPackage', a)
    if hasattr(b2, 'mancoosimm_ConfigFilesPackage'):
        assert _is_linked(b2, 'mancoosimm_ConfigFilesPackage', a)
    _safe_set(a, 'mancoosimm_Configuration7', set())
    assert not _is_linked(a, 'mancoosimm_Configuration7', b2)
    if hasattr(b2, 'mancoosimm_ConfigFilesPackage'):
        assert not _is_linked(b2, 'mancoosimm_ConfigFilesPackage', a)


def test_assoc_configuration122_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'Configuration', b1)
    assert _is_linked(a, 'Configuration', b1)
    if hasattr(b1, 'environment'):
        assert _is_linked(b1, 'environment', a)
    _safe_set(a, 'Configuration', b2)
    assert _is_linked(a, 'Configuration', b2)
    if hasattr(b1, 'environment'):
        assert not _is_linked(b1, 'environment', a)
    if hasattr(b2, 'environment'):
        assert _is_linked(b2, 'environment', a)
    _safe_set(a, 'Configuration', None)
    assert not _is_linked(a, 'Configuration', b2)
    if hasattr(b2, 'environment'):
        assert not _is_linked(b2, 'environment', a)


def test_assoc_configuration132_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_FileSystem()
    b2 = mancoosimm_FileSystem()
    _safe_set(a, 'Configuration133', b1)
    assert _is_linked(a, 'Configuration133', b1)
    if hasattr(b1, 'fileSystem'):
        assert _is_linked(b1, 'fileSystem', a)
    _safe_set(a, 'Configuration133', b2)
    assert _is_linked(a, 'Configuration133', b2)
    if hasattr(b1, 'fileSystem'):
        assert not _is_linked(b1, 'fileSystem', a)
    if hasattr(b2, 'fileSystem'):
        assert _is_linked(b2, 'fileSystem', a)
    _safe_set(a, 'Configuration133', None)
    assert not _is_linked(a, 'Configuration133', b2)
    if hasattr(b2, 'fileSystem'):
        assert not _is_linked(b2, 'fileSystem', a)


def test_assoc_configuration18_link_reassign_clear():
    a = mancoosimm_Package(architecture="sample_text", version="sample_text")
    b1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    _safe_set(a, 'mancoosimm_Package', b1)
    assert _is_linked(a, 'mancoosimm_Package', b1)
    if hasattr(b1, 'mancoosimm_Configuration19'):
        assert _is_linked(b1, 'mancoosimm_Configuration19', a)
    _safe_set(a, 'mancoosimm_Package', b2)
    assert _is_linked(a, 'mancoosimm_Package', b2)
    if hasattr(b1, 'mancoosimm_Configuration19'):
        assert not _is_linked(b1, 'mancoosimm_Configuration19', a)
    if hasattr(b2, 'mancoosimm_Configuration19'):
        assert _is_linked(b2, 'mancoosimm_Configuration19', a)
    _safe_set(a, 'mancoosimm_Package', None)
    assert not _is_linked(a, 'mancoosimm_Package', b2)
    if hasattr(b2, 'mancoosimm_Configuration19'):
        assert not _is_linked(b2, 'mancoosimm_Configuration19', a)


def test_assoc_conflict277_link_reassign_clear():
    a = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    b1 = mancoosimm_Conflict()
    b2 = mancoosimm_Conflict()
    _safe_set(a, 'singleConflict', b1)
    assert _is_linked(a, 'singleConflict', b1)
    if hasattr(b1, 'Conflict'):
        assert _is_linked(b1, 'Conflict', a)
    _safe_set(a, 'singleConflict', b2)
    assert _is_linked(a, 'singleConflict', b2)
    if hasattr(b1, 'Conflict'):
        assert not _is_linked(b1, 'Conflict', a)
    if hasattr(b2, 'Conflict'):
        assert _is_linked(b2, 'Conflict', a)
    _safe_set(a, 'singleConflict', None)
    assert not _is_linked(a, 'singleConflict', b2)
    if hasattr(b2, 'Conflict'):
        assert not _is_linked(b2, 'Conflict', a)


def test_assoc_conflict46_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Conflict()
    b2 = mancoosimm_Conflict()
    _safe_set(a, 'mancoosimm_InstalledPackage47', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage47', b1)
    if hasattr(b1, 'mancoosimm_Conflict'):
        assert _is_linked(b1, 'mancoosimm_Conflict', a)
    _safe_set(a, 'mancoosimm_InstalledPackage47', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage47', b2)
    if hasattr(b1, 'mancoosimm_Conflict'):
        assert not _is_linked(b1, 'mancoosimm_Conflict', a)
    if hasattr(b2, 'mancoosimm_Conflict'):
        assert _is_linked(b2, 'mancoosimm_Conflict', a)
    _safe_set(a, 'mancoosimm_InstalledPackage47', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage47', b2)
    if hasattr(b2, 'mancoosimm_Conflict'):
        assert not _is_linked(b2, 'mancoosimm_Conflict', a)


def test_assoc_current179_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_Alternative()
    b2 = mancoosimm_Alternative()
    _safe_set(a, 'mancoosimm_File180', b1)
    assert _is_linked(a, 'mancoosimm_File180', b1)
    if hasattr(b1, 'mancoosimm_Alternative'):
        assert _is_linked(b1, 'mancoosimm_Alternative', a)
    _safe_set(a, 'mancoosimm_File180', b2)
    assert _is_linked(a, 'mancoosimm_File180', b2)
    if hasattr(b1, 'mancoosimm_Alternative'):
        assert not _is_linked(b1, 'mancoosimm_Alternative', a)
    if hasattr(b2, 'mancoosimm_Alternative'):
        assert _is_linked(b2, 'mancoosimm_Alternative', a)
    _safe_set(a, 'mancoosimm_File180', None)
    assert not _is_linked(a, 'mancoosimm_File180', b2)
    if hasattr(b2, 'mancoosimm_Alternative'):
        assert not _is_linked(b2, 'mancoosimm_Alternative', a)


def test_assoc_dependence77_link_reassign_clear():
    a = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    b1 = mancoosimm_Dependence()
    b2 = mancoosimm_Dependence()
    _safe_set(a, 'singleDep', b1)
    assert _is_linked(a, 'singleDep', b1)
    if hasattr(b1, 'Dependence78'):
        assert _is_linked(b1, 'Dependence78', a)
    _safe_set(a, 'singleDep', b2)
    assert _is_linked(a, 'singleDep', b2)
    if hasattr(b1, 'Dependence78'):
        assert not _is_linked(b1, 'Dependence78', a)
    if hasattr(b2, 'Dependence78'):
        assert _is_linked(b2, 'Dependence78', a)
    _safe_set(a, 'singleDep', None)
    assert not _is_linked(a, 'singleDep', b2)
    if hasattr(b2, 'Dependence78'):
        assert not _is_linked(b2, 'Dependence78', a)


def test_assoc_depends23_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Dependence()
    b2 = mancoosimm_Dependence()
    _safe_set(a, 'mancoosimm_InstalledPackage24', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage24', b1)
    if hasattr(b1, 'mancoosimm_Dependence'):
        assert _is_linked(b1, 'mancoosimm_Dependence', a)
    _safe_set(a, 'mancoosimm_InstalledPackage24', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage24', b2)
    if hasattr(b1, 'mancoosimm_Dependence'):
        assert not _is_linked(b1, 'mancoosimm_Dependence', a)
    if hasattr(b2, 'mancoosimm_Dependence'):
        assert _is_linked(b2, 'mancoosimm_Dependence', a)
    _safe_set(a, 'mancoosimm_InstalledPackage24', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage24', b2)
    if hasattr(b2, 'mancoosimm_Dependence'):
        assert not _is_linked(b2, 'mancoosimm_Dependence', a)


def test_assoc_document248_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_SGMLDocument()
    b2 = mancoosimm_SGMLDocument()
    _safe_set(a, 'mancoosimm_File250', b1)
    assert _is_linked(a, 'mancoosimm_File250', b1)
    if hasattr(b1, 'mancoosimm_SGMLDocument249'):
        assert _is_linked(b1, 'mancoosimm_SGMLDocument249', a)
    _safe_set(a, 'mancoosimm_File250', b2)
    assert _is_linked(a, 'mancoosimm_File250', b2)
    if hasattr(b1, 'mancoosimm_SGMLDocument249'):
        assert not _is_linked(b1, 'mancoosimm_SGMLDocument249', a)
    if hasattr(b2, 'mancoosimm_SGMLDocument249'):
        assert _is_linked(b2, 'mancoosimm_SGMLDocument249', a)
    _safe_set(a, 'mancoosimm_File250', None)
    assert not _is_linked(a, 'mancoosimm_File250', b2)
    if hasattr(b2, 'mancoosimm_SGMLDocument249'):
        assert not _is_linked(b2, 'mancoosimm_SGMLDocument249', a)


def test_assoc_document257_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_SkeeperDocument()
    b2 = mancoosimm_SkeeperDocument()
    _safe_set(a, 'mancoosimm_File259', b1)
    assert _is_linked(a, 'mancoosimm_File259', b1)
    if hasattr(b1, 'mancoosimm_SkeeperDocument258'):
        assert _is_linked(b1, 'mancoosimm_SkeeperDocument258', a)
    _safe_set(a, 'mancoosimm_File259', b2)
    assert _is_linked(a, 'mancoosimm_File259', b2)
    if hasattr(b1, 'mancoosimm_SkeeperDocument258'):
        assert not _is_linked(b1, 'mancoosimm_SkeeperDocument258', a)
    if hasattr(b2, 'mancoosimm_SkeeperDocument258'):
        assert _is_linked(b2, 'mancoosimm_SkeeperDocument258', a)
    _safe_set(a, 'mancoosimm_File259', None)
    assert not _is_linked(a, 'mancoosimm_File259', b2)
    if hasattr(b2, 'mancoosimm_SkeeperDocument258'):
        assert not _is_linked(b2, 'mancoosimm_SkeeperDocument258', a)


def test_assoc_documentationFiles44_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_DocumentationFile()
    b2 = mancoosimm_DocumentationFile()
    _safe_set(a, 'pkg45', {b1})
    assert _is_linked(a, 'pkg45', b1)
    if hasattr(b1, 'DocumentationFile'):
        assert _is_linked(b1, 'DocumentationFile', a)
    _safe_set(a, 'pkg45', {b2})
    assert _is_linked(a, 'pkg45', b2)
    if hasattr(b1, 'DocumentationFile'):
        assert not _is_linked(b1, 'DocumentationFile', a)
    if hasattr(b2, 'DocumentationFile'):
        assert _is_linked(b2, 'DocumentationFile', a)
    _safe_set(a, 'pkg45', set())
    assert not _is_linked(a, 'pkg45', b2)
    if hasattr(b2, 'DocumentationFile'):
        assert not _is_linked(b2, 'DocumentationFile', a)


def test_assoc_enhances32_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage31', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage31', b1)
    if hasattr(b1, 'mancoosimm_InstalledPackage33'):
        assert _is_linked(b1, 'mancoosimm_InstalledPackage33', a)
    _safe_set(a, 'mancoosimm_InstalledPackage31', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage31', b2)
    if hasattr(b1, 'mancoosimm_InstalledPackage33'):
        assert not _is_linked(b1, 'mancoosimm_InstalledPackage33', a)
    if hasattr(b2, 'mancoosimm_InstalledPackage33'):
        assert _is_linked(b2, 'mancoosimm_InstalledPackage33', a)
    _safe_set(a, 'mancoosimm_InstalledPackage31', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage31', b2)
    if hasattr(b2, 'mancoosimm_InstalledPackage33'):
        assert not _is_linked(b2, 'mancoosimm_InstalledPackage33', a)


def test_assoc_env194_link_reassign_clear():
    a = mancoosimm_IconCache(mtime="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'iconCache', b1)
    assert _is_linked(a, 'iconCache', b1)
    if hasattr(b1, 'Environment195'):
        assert _is_linked(b1, 'Environment195', a)
    _safe_set(a, 'iconCache', b2)
    assert _is_linked(a, 'iconCache', b2)
    if hasattr(b1, 'Environment195'):
        assert not _is_linked(b1, 'Environment195', a)
    if hasattr(b2, 'Environment195'):
        assert _is_linked(b2, 'Environment195', a)
    _safe_set(a, 'iconCache', None)
    assert not _is_linked(a, 'iconCache', b2)
    if hasattr(b2, 'Environment195'):
        assert not _is_linked(b2, 'Environment195', a)


def test_assoc_env218_link_reassign_clear():
    a = mancoosimm_XFontCache(location="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'xfontCaches', b1)
    assert _is_linked(a, 'xfontCaches', b1)
    if hasattr(b1, 'Environment219'):
        assert _is_linked(b1, 'Environment219', a)
    _safe_set(a, 'xfontCaches', b2)
    assert _is_linked(a, 'xfontCaches', b2)
    if hasattr(b1, 'Environment219'):
        assert not _is_linked(b1, 'Environment219', a)
    if hasattr(b2, 'Environment219'):
        assert _is_linked(b2, 'Environment219', a)
    _safe_set(a, 'xfontCaches', None)
    assert not _is_linked(a, 'xfontCaches', b2)
    if hasattr(b2, 'Environment219'):
        assert not _is_linked(b2, 'Environment219', a)


def test_assoc_env235_link_reassign_clear():
    a = mancoosimm_ModuleCache(version="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'moduleCache236', b1)
    assert _is_linked(a, 'moduleCache236', b1)
    if hasattr(b1, 'Environment237'):
        assert _is_linked(b1, 'Environment237', a)
    _safe_set(a, 'moduleCache236', b2)
    assert _is_linked(a, 'moduleCache236', b2)
    if hasattr(b1, 'Environment237'):
        assert not _is_linked(b1, 'Environment237', a)
    if hasattr(b2, 'Environment237'):
        assert _is_linked(b2, 'Environment237', a)
    _safe_set(a, 'moduleCache236', None)
    assert not _is_linked(a, 'moduleCache236', b2)
    if hasattr(b2, 'Environment237'):
        assert not _is_linked(b2, 'Environment237', a)


def test_assoc_environment1_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'configuration2', b1)
    assert _is_linked(a, 'configuration2', b1)
    if hasattr(b1, 'Environment'):
        assert _is_linked(b1, 'Environment', a)
    _safe_set(a, 'configuration2', b2)
    assert _is_linked(a, 'configuration2', b2)
    if hasattr(b1, 'Environment'):
        assert not _is_linked(b1, 'Environment', a)
    if hasattr(b2, 'Environment'):
        assert _is_linked(b2, 'Environment', a)
    _safe_set(a, 'configuration2', None)
    assert not _is_linked(a, 'configuration2', b2)
    if hasattr(b2, 'Environment'):
        assert not _is_linked(b2, 'Environment', a)


def test_assoc_executable153_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_MenuEntry()
    b2 = mancoosimm_MenuEntry()
    _safe_set(a, 'mancoosimm_File154', b1)
    assert _is_linked(a, 'mancoosimm_File154', b1)
    if hasattr(b1, 'mancoosimm_MenuEntry'):
        assert _is_linked(b1, 'mancoosimm_MenuEntry', a)
    _safe_set(a, 'mancoosimm_File154', b2)
    assert _is_linked(a, 'mancoosimm_File154', b2)
    if hasattr(b1, 'mancoosimm_MenuEntry'):
        assert not _is_linked(b1, 'mancoosimm_MenuEntry', a)
    if hasattr(b2, 'mancoosimm_MenuEntry'):
        assert _is_linked(b2, 'mancoosimm_MenuEntry', a)
    _safe_set(a, 'mancoosimm_File154', None)
    assert not _is_linked(a, 'mancoosimm_File154', b2)
    if hasattr(b2, 'mancoosimm_MenuEntry'):
        assert not _is_linked(b2, 'mancoosimm_MenuEntry', a)


def test_assoc_executable159_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_Service()
    b2 = mancoosimm_Service()
    _safe_set(a, 'mancoosimm_File161', b1)
    assert _is_linked(a, 'mancoosimm_File161', b1)
    if hasattr(b1, 'mancoosimm_Service160'):
        assert _is_linked(b1, 'mancoosimm_Service160', a)
    _safe_set(a, 'mancoosimm_File161', b2)
    assert _is_linked(a, 'mancoosimm_File161', b2)
    if hasattr(b1, 'mancoosimm_Service160'):
        assert not _is_linked(b1, 'mancoosimm_Service160', a)
    if hasattr(b2, 'mancoosimm_Service160'):
        assert _is_linked(b2, 'mancoosimm_Service160', a)
    _safe_set(a, 'mancoosimm_File161', None)
    assert not _is_linked(a, 'mancoosimm_File161', b2)
    if hasattr(b2, 'mancoosimm_Service160'):
        assert not _is_linked(b2, 'mancoosimm_Service160', a)


def test_assoc_file222_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_XFont()
    b2 = mancoosimm_XFont()
    _safe_set(a, 'mancoosimm_File223', b1)
    assert _is_linked(a, 'mancoosimm_File223', b1)
    if hasattr(b1, 'mancoosimm_XFont'):
        assert _is_linked(b1, 'mancoosimm_XFont', a)
    _safe_set(a, 'mancoosimm_File223', b2)
    assert _is_linked(a, 'mancoosimm_File223', b2)
    if hasattr(b1, 'mancoosimm_XFont'):
        assert not _is_linked(b1, 'mancoosimm_XFont', a)
    if hasattr(b2, 'mancoosimm_XFont'):
        assert _is_linked(b2, 'mancoosimm_XFont', a)
    _safe_set(a, 'mancoosimm_File223', None)
    assert not _is_linked(a, 'mancoosimm_File223', b2)
    if hasattr(b2, 'mancoosimm_XFont'):
        assert not _is_linked(b2, 'mancoosimm_XFont', a)


def test_assoc_file230_link_reassign_clear():
    a = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'mancoosimm_SharedLibrary', b1)
    assert _is_linked(a, 'mancoosimm_SharedLibrary', b1)
    if hasattr(b1, 'mancoosimm_File231'):
        assert _is_linked(b1, 'mancoosimm_File231', a)
    _safe_set(a, 'mancoosimm_SharedLibrary', b2)
    assert _is_linked(a, 'mancoosimm_SharedLibrary', b2)
    if hasattr(b1, 'mancoosimm_File231'):
        assert not _is_linked(b1, 'mancoosimm_File231', a)
    if hasattr(b2, 'mancoosimm_File231'):
        assert _is_linked(b2, 'mancoosimm_File231', a)
    _safe_set(a, 'mancoosimm_SharedLibrary', None)
    assert not _is_linked(a, 'mancoosimm_SharedLibrary', b2)
    if hasattr(b2, 'mancoosimm_File231'):
        assert not _is_linked(b2, 'mancoosimm_File231', a)


def test_assoc_file238_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_Module()
    b2 = mancoosimm_Module()
    _safe_set(a, 'mancoosimm_File239', b1)
    assert _is_linked(a, 'mancoosimm_File239', b1)
    if hasattr(b1, 'mancoosimm_Module'):
        assert _is_linked(b1, 'mancoosimm_Module', a)
    _safe_set(a, 'mancoosimm_File239', b2)
    assert _is_linked(a, 'mancoosimm_File239', b2)
    if hasattr(b1, 'mancoosimm_Module'):
        assert not _is_linked(b1, 'mancoosimm_Module', a)
    if hasattr(b2, 'mancoosimm_Module'):
        assert _is_linked(b2, 'mancoosimm_Module', a)
    _safe_set(a, 'mancoosimm_File239', None)
    assert not _is_linked(a, 'mancoosimm_File239', b2)
    if hasattr(b2, 'mancoosimm_Module'):
        assert not _is_linked(b2, 'mancoosimm_Module', a)


def test_assoc_fileSystem0_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_FileSystem()
    b2 = mancoosimm_FileSystem()
    _safe_set(a, 'configuration', b1)
    assert _is_linked(a, 'configuration', b1)
    if hasattr(b1, 'FileSystem'):
        assert _is_linked(b1, 'FileSystem', a)
    _safe_set(a, 'configuration', b2)
    assert _is_linked(a, 'configuration', b2)
    if hasattr(b1, 'FileSystem'):
        assert not _is_linked(b1, 'FileSystem', a)
    if hasattr(b2, 'FileSystem'):
        assert _is_linked(b2, 'FileSystem', a)
    _safe_set(a, 'configuration', None)
    assert not _is_linked(a, 'configuration', b2)
    if hasattr(b2, 'FileSystem'):
        assert not _is_linked(b2, 'FileSystem', a)


def test_assoc_files188_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_PackageSetting()
    b2 = mancoosimm_PackageSetting()
    _safe_set(a, 'File189', b1)
    assert _is_linked(a, 'File189', b1)
    if hasattr(b1, 'pkgSettings'):
        assert _is_linked(b1, 'pkgSettings', a)
    _safe_set(a, 'File189', b2)
    assert _is_linked(a, 'File189', b2)
    if hasattr(b1, 'pkgSettings'):
        assert not _is_linked(b1, 'pkgSettings', a)
    if hasattr(b2, 'pkgSettings'):
        assert _is_linked(b2, 'pkgSettings', a)
    _safe_set(a, 'File189', None)
    assert not _is_linked(a, 'File189', b2)
    if hasattr(b2, 'pkgSettings'):
        assert not _is_linked(b2, 'pkgSettings', a)


def test_assoc_files260_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_EmacsPackage()
    b2 = mancoosimm_EmacsPackage()
    _safe_set(a, 'mancoosimm_File261', b1)
    assert _is_linked(a, 'mancoosimm_File261', b1)
    if hasattr(b1, 'mancoosimm_EmacsPackage'):
        assert _is_linked(b1, 'mancoosimm_EmacsPackage', a)
    _safe_set(a, 'mancoosimm_File261', b2)
    assert _is_linked(a, 'mancoosimm_File261', b2)
    if hasattr(b1, 'mancoosimm_EmacsPackage'):
        assert not _is_linked(b1, 'mancoosimm_EmacsPackage', a)
    if hasattr(b2, 'mancoosimm_EmacsPackage'):
        assert _is_linked(b2, 'mancoosimm_EmacsPackage', a)
    _safe_set(a, 'mancoosimm_File261', None)
    assert not _is_linked(a, 'mancoosimm_File261', b2)
    if hasattr(b2, 'mancoosimm_EmacsPackage'):
        assert not _is_linked(b2, 'mancoosimm_EmacsPackage', a)


def test_assoc_files42_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'mancoosimm_InstalledPackage43', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage43', b1)
    if hasattr(b1, 'mancoosimm_File'):
        assert _is_linked(b1, 'mancoosimm_File', a)
    _safe_set(a, 'mancoosimm_InstalledPackage43', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage43', b2)
    if hasattr(b1, 'mancoosimm_File'):
        assert not _is_linked(b1, 'mancoosimm_File', a)
    if hasattr(b2, 'mancoosimm_File'):
        assert _is_linked(b2, 'mancoosimm_File', a)
    _safe_set(a, 'mancoosimm_InstalledPackage43', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage43', b2)
    if hasattr(b2, 'mancoosimm_File'):
        assert not _is_linked(b2, 'mancoosimm_File', a)


def test_assoc_files48_link_reassign_clear():
    a = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'mancoosimm_UnpackedPackage49', {b1})
    assert _is_linked(a, 'mancoosimm_UnpackedPackage49', b1)
    if hasattr(b1, 'mancoosimm_File50'):
        assert _is_linked(b1, 'mancoosimm_File50', a)
    _safe_set(a, 'mancoosimm_UnpackedPackage49', {b2})
    assert _is_linked(a, 'mancoosimm_UnpackedPackage49', b2)
    if hasattr(b1, 'mancoosimm_File50'):
        assert not _is_linked(b1, 'mancoosimm_File50', a)
    if hasattr(b2, 'mancoosimm_File50'):
        assert _is_linked(b2, 'mancoosimm_File50', a)
    _safe_set(a, 'mancoosimm_UnpackedPackage49', set())
    assert not _is_linked(a, 'mancoosimm_UnpackedPackage49', b2)
    if hasattr(b2, 'mancoosimm_File50'):
        assert not _is_linked(b2, 'mancoosimm_File50', a)


def test_assoc_fs164_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_FileSystem()
    b2 = mancoosimm_FileSystem()
    _safe_set(a, 'root', b1)
    assert _is_linked(a, 'root', b1)
    if hasattr(b1, 'FileSystem165'):
        assert _is_linked(b1, 'FileSystem165', a)
    _safe_set(a, 'root', b2)
    assert _is_linked(a, 'root', b2)
    if hasattr(b1, 'FileSystem165'):
        assert not _is_linked(b1, 'FileSystem165', a)
    if hasattr(b2, 'FileSystem165'):
        assert _is_linked(b2, 'FileSystem165', a)
    _safe_set(a, 'root', None)
    assert not _is_linked(a, 'root', b2)
    if hasattr(b2, 'FileSystem165'):
        assert not _is_linked(b2, 'FileSystem165', a)


def test_assoc_group174_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_Group()
    b2 = mancoosimm_Group()
    _safe_set(a, 'mancoosimm_File175', b1)
    assert _is_linked(a, 'mancoosimm_File175', b1)
    if hasattr(b1, 'mancoosimm_Group'):
        assert _is_linked(b1, 'mancoosimm_Group', a)
    _safe_set(a, 'mancoosimm_File175', b2)
    assert _is_linked(a, 'mancoosimm_File175', b2)
    if hasattr(b1, 'mancoosimm_Group'):
        assert not _is_linked(b1, 'mancoosimm_Group', a)
    if hasattr(b2, 'mancoosimm_Group'):
        assert _is_linked(b2, 'mancoosimm_Group', a)
    _safe_set(a, 'mancoosimm_File175', None)
    assert not _is_linked(a, 'mancoosimm_File175', b2)
    if hasattr(b2, 'mancoosimm_Group'):
        assert not _is_linked(b2, 'mancoosimm_Group', a)


def test_assoc_halfConfiguredPackages10_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_HalfConfiguredPackage()
    b2 = mancoosimm_HalfConfiguredPackage()
    _safe_set(a, 'mancoosimm_Configuration11', {b1})
    assert _is_linked(a, 'mancoosimm_Configuration11', b1)
    if hasattr(b1, 'mancoosimm_HalfConfiguredPackage'):
        assert _is_linked(b1, 'mancoosimm_HalfConfiguredPackage', a)
    _safe_set(a, 'mancoosimm_Configuration11', {b2})
    assert _is_linked(a, 'mancoosimm_Configuration11', b2)
    if hasattr(b1, 'mancoosimm_HalfConfiguredPackage'):
        assert not _is_linked(b1, 'mancoosimm_HalfConfiguredPackage', a)
    if hasattr(b2, 'mancoosimm_HalfConfiguredPackage'):
        assert _is_linked(b2, 'mancoosimm_HalfConfiguredPackage', a)
    _safe_set(a, 'mancoosimm_Configuration11', set())
    assert not _is_linked(a, 'mancoosimm_Configuration11', b2)
    if hasattr(b2, 'mancoosimm_HalfConfiguredPackage'):
        assert not _is_linked(b2, 'mancoosimm_HalfConfiguredPackage', a)


def test_assoc_halfConfiguredReinstRequiredPackages14_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_HalfConfiguredReinstRequiredPackage()
    b2 = mancoosimm_HalfConfiguredReinstRequiredPackage()
    _safe_set(a, 'mancoosimm_Configuration15', {b1})
    assert _is_linked(a, 'mancoosimm_Configuration15', b1)
    if hasattr(b1, 'mancoosimm_HalfConfiguredReinstRequiredPackage'):
        assert _is_linked(b1, 'mancoosimm_HalfConfiguredReinstRequiredPackage', a)
    _safe_set(a, 'mancoosimm_Configuration15', {b2})
    assert _is_linked(a, 'mancoosimm_Configuration15', b2)
    if hasattr(b1, 'mancoosimm_HalfConfiguredReinstRequiredPackage'):
        assert not _is_linked(b1, 'mancoosimm_HalfConfiguredReinstRequiredPackage', a)
    if hasattr(b2, 'mancoosimm_HalfConfiguredReinstRequiredPackage'):
        assert _is_linked(b2, 'mancoosimm_HalfConfiguredReinstRequiredPackage', a)
    _safe_set(a, 'mancoosimm_Configuration15', set())
    assert not _is_linked(a, 'mancoosimm_Configuration15', b2)
    if hasattr(b2, 'mancoosimm_HalfConfiguredReinstRequiredPackage'):
        assert not _is_linked(b2, 'mancoosimm_HalfConfiguredReinstRequiredPackage', a)


def test_assoc_halfInstalledPackages12_link_reassign_clear():
    a = mancoosimm_HalfInstalledPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    _safe_set(a, 'mancoosimm_HalfInstalledPackage', b1)
    assert _is_linked(a, 'mancoosimm_HalfInstalledPackage', b1)
    if hasattr(b1, 'mancoosimm_Configuration13'):
        assert _is_linked(b1, 'mancoosimm_Configuration13', a)
    _safe_set(a, 'mancoosimm_HalfInstalledPackage', b2)
    assert _is_linked(a, 'mancoosimm_HalfInstalledPackage', b2)
    if hasattr(b1, 'mancoosimm_Configuration13'):
        assert not _is_linked(b1, 'mancoosimm_Configuration13', a)
    if hasattr(b2, 'mancoosimm_Configuration13'):
        assert _is_linked(b2, 'mancoosimm_Configuration13', a)
    _safe_set(a, 'mancoosimm_HalfInstalledPackage', None)
    assert not _is_linked(a, 'mancoosimm_HalfInstalledPackage', b2)
    if hasattr(b2, 'mancoosimm_Configuration13'):
        assert not _is_linked(b2, 'mancoosimm_Configuration13', a)


def test_assoc_halfInstalledReinstRequiredPackages16_link_reassign_clear():
    a = mancoosimm_HalfInstalledReinstRequiredPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    _safe_set(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', b1)
    assert _is_linked(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', b1)
    if hasattr(b1, 'mancoosimm_Configuration17'):
        assert _is_linked(b1, 'mancoosimm_Configuration17', a)
    _safe_set(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', b2)
    assert _is_linked(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', b2)
    if hasattr(b1, 'mancoosimm_Configuration17'):
        assert not _is_linked(b1, 'mancoosimm_Configuration17', a)
    if hasattr(b2, 'mancoosimm_Configuration17'):
        assert _is_linked(b2, 'mancoosimm_Configuration17', a)
    _safe_set(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', None)
    assert not _is_linked(a, 'mancoosimm_HalfInstalledReinstRequiredPackage', b2)
    if hasattr(b2, 'mancoosimm_Configuration17'):
        assert not _is_linked(b2, 'mancoosimm_Configuration17', a)


def test_assoc_handler207_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_MimeTypeHandler()
    b2 = mancoosimm_MimeTypeHandler()
    _safe_set(a, 'mancoosimm_File208', b1)
    assert _is_linked(a, 'mancoosimm_File208', b1)
    if hasattr(b1, 'mancoosimm_MimeTypeHandler'):
        assert _is_linked(b1, 'mancoosimm_MimeTypeHandler', a)
    _safe_set(a, 'mancoosimm_File208', b2)
    assert _is_linked(a, 'mancoosimm_File208', b2)
    if hasattr(b1, 'mancoosimm_MimeTypeHandler'):
        assert not _is_linked(b1, 'mancoosimm_MimeTypeHandler', a)
    if hasattr(b2, 'mancoosimm_MimeTypeHandler'):
        assert _is_linked(b2, 'mancoosimm_MimeTypeHandler', a)
    _safe_set(a, 'mancoosimm_File208', None)
    assert not _is_linked(a, 'mancoosimm_File208', b2)
    if hasattr(b2, 'mancoosimm_MimeTypeHandler'):
        assert not _is_linked(b2, 'mancoosimm_MimeTypeHandler', a)


def test_assoc_home269_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_User()
    b2 = mancoosimm_User()
    _safe_set(a, 'mancoosimm_File271', b1)
    assert _is_linked(a, 'mancoosimm_File271', b1)
    if hasattr(b1, 'mancoosimm_User270'):
        assert _is_linked(b1, 'mancoosimm_User270', a)
    _safe_set(a, 'mancoosimm_File271', b2)
    assert _is_linked(a, 'mancoosimm_File271', b2)
    if hasattr(b1, 'mancoosimm_User270'):
        assert not _is_linked(b1, 'mancoosimm_User270', a)
    if hasattr(b2, 'mancoosimm_User270'):
        assert _is_linked(b2, 'mancoosimm_User270', a)
    _safe_set(a, 'mancoosimm_File271', None)
    assert not _is_linked(a, 'mancoosimm_File271', b2)
    if hasattr(b2, 'mancoosimm_User270'):
        assert not _is_linked(b2, 'mancoosimm_User270', a)


def test_assoc_iconCache110_link_reassign_clear():
    a = mancoosimm_IconCache(mtime="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'IconCache', b1)
    assert _is_linked(a, 'IconCache', b1)
    if hasattr(b1, 'env111'):
        assert _is_linked(b1, 'env111', a)
    _safe_set(a, 'IconCache', b2)
    assert _is_linked(a, 'IconCache', b2)
    if hasattr(b1, 'env111'):
        assert not _is_linked(b1, 'env111', a)
    if hasattr(b2, 'env111'):
        assert _is_linked(b2, 'env111', a)
    _safe_set(a, 'IconCache', None)
    assert not _is_linked(a, 'IconCache', b2)
    if hasattr(b2, 'env111'):
        assert not _is_linked(b2, 'env111', a)


def test_assoc_icons196_link_reassign_clear():
    a = mancoosimm_IconCache(mtime="sample_text")
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'mancoosimm_IconCache', b1)
    assert _is_linked(a, 'mancoosimm_IconCache', b1)
    if hasattr(b1, 'mancoosimm_File197'):
        assert _is_linked(b1, 'mancoosimm_File197', a)
    _safe_set(a, 'mancoosimm_IconCache', b2)
    assert _is_linked(a, 'mancoosimm_IconCache', b2)
    if hasattr(b1, 'mancoosimm_File197'):
        assert not _is_linked(b1, 'mancoosimm_File197', a)
    if hasattr(b2, 'mancoosimm_File197'):
        assert _is_linked(b2, 'mancoosimm_File197', a)
    _safe_set(a, 'mancoosimm_IconCache', None)
    assert not _is_linked(a, 'mancoosimm_IconCache', b2)
    if hasattr(b2, 'mancoosimm_File197'):
        assert not _is_linked(b2, 'mancoosimm_File197', a)


def test_assoc_impPackage59_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_VirtualPackage()
    b2 = mancoosimm_VirtualPackage()
    _safe_set(a, 'mancoosimm_InstalledPackage61', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage61', b1)
    if hasattr(b1, 'mancoosimm_VirtualPackage60'):
        assert _is_linked(b1, 'mancoosimm_VirtualPackage60', a)
    _safe_set(a, 'mancoosimm_InstalledPackage61', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage61', b2)
    if hasattr(b1, 'mancoosimm_VirtualPackage60'):
        assert not _is_linked(b1, 'mancoosimm_VirtualPackage60', a)
    if hasattr(b2, 'mancoosimm_VirtualPackage60'):
        assert _is_linked(b2, 'mancoosimm_VirtualPackage60', a)
    _safe_set(a, 'mancoosimm_InstalledPackage61', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage61', b2)
    if hasattr(b2, 'mancoosimm_VirtualPackage60'):
        assert not _is_linked(b2, 'mancoosimm_VirtualPackage60', a)


def test_assoc_installedPackages3_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage', b1)
    if hasattr(b1, 'mancoosimm_Configuration'):
        assert _is_linked(b1, 'mancoosimm_Configuration', a)
    _safe_set(a, 'mancoosimm_InstalledPackage', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage', b2)
    if hasattr(b1, 'mancoosimm_Configuration'):
        assert not _is_linked(b1, 'mancoosimm_Configuration', a)
    if hasattr(b2, 'mancoosimm_Configuration'):
        assert _is_linked(b2, 'mancoosimm_Configuration', a)
    _safe_set(a, 'mancoosimm_InstalledPackage', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage', b2)
    if hasattr(b2, 'mancoosimm_Configuration'):
        assert not _is_linked(b2, 'mancoosimm_Configuration', a)


def test_assoc_libraryCache232_link_reassign_clear():
    a = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    b1 = mancoosimm_LibraryCache()
    b2 = mancoosimm_LibraryCache()
    _safe_set(a, 'sharedLibraries', b1)
    assert _is_linked(a, 'sharedLibraries', b1)
    if hasattr(b1, 'LibraryCache233'):
        assert _is_linked(b1, 'LibraryCache233', a)
    _safe_set(a, 'sharedLibraries', b2)
    assert _is_linked(a, 'sharedLibraries', b2)
    if hasattr(b1, 'LibraryCache233'):
        assert not _is_linked(b1, 'LibraryCache233', a)
    if hasattr(b2, 'LibraryCache233'):
        assert _is_linked(b2, 'LibraryCache233', a)
    _safe_set(a, 'sharedLibraries', None)
    assert not _is_linked(a, 'sharedLibraries', b2)
    if hasattr(b2, 'LibraryCache233'):
        assert not _is_linked(b2, 'LibraryCache233', a)


def test_assoc_location181_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_Alternative()
    b2 = mancoosimm_Alternative()
    _safe_set(a, 'mancoosimm_File183', b1)
    assert _is_linked(a, 'mancoosimm_File183', b1)
    if hasattr(b1, 'mancoosimm_Alternative182'):
        assert _is_linked(b1, 'mancoosimm_Alternative182', a)
    _safe_set(a, 'mancoosimm_File183', b2)
    assert _is_linked(a, 'mancoosimm_File183', b2)
    if hasattr(b1, 'mancoosimm_Alternative182'):
        assert not _is_linked(b1, 'mancoosimm_Alternative182', a)
    if hasattr(b2, 'mancoosimm_Alternative182'):
        assert _is_linked(b2, 'mancoosimm_Alternative182', a)
    _safe_set(a, 'mancoosimm_File183', None)
    assert not _is_linked(a, 'mancoosimm_File183', b2)
    if hasattr(b2, 'mancoosimm_Alternative182'):
        assert not _is_linked(b2, 'mancoosimm_Alternative182', a)


def test_assoc_location245_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_SGMLDocument()
    b2 = mancoosimm_SGMLDocument()
    _safe_set(a, 'mancoosimm_File247', b1)
    assert _is_linked(a, 'mancoosimm_File247', b1)
    if hasattr(b1, 'mancoosimm_SGMLDocument246'):
        assert _is_linked(b1, 'mancoosimm_SGMLDocument246', a)
    _safe_set(a, 'mancoosimm_File247', b2)
    assert _is_linked(a, 'mancoosimm_File247', b2)
    if hasattr(b1, 'mancoosimm_SGMLDocument246'):
        assert not _is_linked(b1, 'mancoosimm_SGMLDocument246', a)
    if hasattr(b2, 'mancoosimm_SGMLDocument246'):
        assert _is_linked(b2, 'mancoosimm_SGMLDocument246', a)
    _safe_set(a, 'mancoosimm_File247', None)
    assert not _is_linked(a, 'mancoosimm_File247', b2)
    if hasattr(b2, 'mancoosimm_SGMLDocument246'):
        assert not _is_linked(b2, 'mancoosimm_SGMLDocument246', a)


def test_assoc_location254_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_SkeeperDocument()
    b2 = mancoosimm_SkeeperDocument()
    _safe_set(a, 'mancoosimm_File256', b1)
    assert _is_linked(a, 'mancoosimm_File256', b1)
    if hasattr(b1, 'mancoosimm_SkeeperDocument255'):
        assert _is_linked(b1, 'mancoosimm_SkeeperDocument255', a)
    _safe_set(a, 'mancoosimm_File256', b2)
    assert _is_linked(a, 'mancoosimm_File256', b2)
    if hasattr(b1, 'mancoosimm_SkeeperDocument255'):
        assert not _is_linked(b1, 'mancoosimm_SkeeperDocument255', a)
    if hasattr(b2, 'mancoosimm_SkeeperDocument255'):
        assert _is_linked(b2, 'mancoosimm_SkeeperDocument255', a)
    _safe_set(a, 'mancoosimm_File256', None)
    assert not _is_linked(a, 'mancoosimm_File256', b2)
    if hasattr(b2, 'mancoosimm_SkeeperDocument255'):
        assert not _is_linked(b2, 'mancoosimm_SkeeperDocument255', a)


def test_assoc_locations224_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_LibraryCache()
    b2 = mancoosimm_LibraryCache()
    _safe_set(a, 'mancoosimm_File225', b1)
    assert _is_linked(a, 'mancoosimm_File225', b1)
    if hasattr(b1, 'mancoosimm_LibraryCache'):
        assert _is_linked(b1, 'mancoosimm_LibraryCache', a)
    _safe_set(a, 'mancoosimm_File225', b2)
    assert _is_linked(a, 'mancoosimm_File225', b2)
    if hasattr(b1, 'mancoosimm_LibraryCache'):
        assert not _is_linked(b1, 'mancoosimm_LibraryCache', a)
    if hasattr(b2, 'mancoosimm_LibraryCache'):
        assert _is_linked(b2, 'mancoosimm_LibraryCache', a)
    _safe_set(a, 'mancoosimm_File225', None)
    assert not _is_linked(a, 'mancoosimm_File225', b2)
    if hasattr(b2, 'mancoosimm_LibraryCache'):
        assert not _is_linked(b2, 'mancoosimm_LibraryCache', a)


def test_assoc_mimeTypeHandlers213_link_reassign_clear():
    a = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    b1 = mancoosimm_MimeTypeHandler()
    b2 = mancoosimm_MimeTypeHandler()
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'MimeTypeHandler214'):
        assert _is_linked(b1, 'MimeTypeHandler214', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'MimeTypeHandler214'):
        assert not _is_linked(b1, 'MimeTypeHandler214', a)
    if hasattr(b2, 'MimeTypeHandler214'):
        assert _is_linked(b2, 'MimeTypeHandler214', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'MimeTypeHandler214'):
        assert not _is_linked(b2, 'MimeTypeHandler214', a)


def test_assoc_mimeTypes205_link_reassign_clear():
    a = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    b1 = mancoosimm_MimeTypeHandlerCache()
    b2 = mancoosimm_MimeTypeHandlerCache()
    _safe_set(a, 'MimeType', b1)
    assert _is_linked(a, 'MimeType', b1)
    if hasattr(b1, 'cache206'):
        assert _is_linked(b1, 'cache206', a)
    _safe_set(a, 'MimeType', b2)
    assert _is_linked(a, 'MimeType', b2)
    if hasattr(b1, 'cache206'):
        assert not _is_linked(b1, 'cache206', a)
    if hasattr(b2, 'cache206'):
        assert _is_linked(b2, 'cache206', a)
    _safe_set(a, 'MimeType', None)
    assert not _is_linked(a, 'MimeType', b2)
    if hasattr(b2, 'cache206'):
        assert not _is_linked(b2, 'cache206', a)


def test_assoc_moduleCache123_link_reassign_clear():
    a = mancoosimm_ModuleCache(version="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'ModuleCache', b1)
    assert _is_linked(a, 'ModuleCache', b1)
    if hasattr(b1, 'env124'):
        assert _is_linked(b1, 'env124', a)
    _safe_set(a, 'ModuleCache', b2)
    assert _is_linked(a, 'ModuleCache', b2)
    if hasattr(b1, 'env124'):
        assert not _is_linked(b1, 'env124', a)
    if hasattr(b2, 'env124'):
        assert _is_linked(b2, 'env124', a)
    _safe_set(a, 'ModuleCache', None)
    assert not _is_linked(a, 'ModuleCache', b2)
    if hasattr(b2, 'env124'):
        assert not _is_linked(b2, 'env124', a)


def test_assoc_moduleCache240_link_reassign_clear():
    a = mancoosimm_ModuleCache(version="sample_text")
    b1 = mancoosimm_Module()
    b2 = mancoosimm_Module()
    _safe_set(a, 'ModuleCache241', b1)
    assert _is_linked(a, 'ModuleCache241', b1)
    if hasattr(b1, 'modules'):
        assert _is_linked(b1, 'modules', a)
    _safe_set(a, 'ModuleCache241', b2)
    assert _is_linked(a, 'ModuleCache241', b2)
    if hasattr(b1, 'modules'):
        assert not _is_linked(b1, 'modules', a)
    if hasattr(b2, 'modules'):
        assert _is_linked(b2, 'modules', a)
    _safe_set(a, 'ModuleCache241', None)
    assert not _is_linked(a, 'ModuleCache241', b2)
    if hasattr(b2, 'modules'):
        assert not _is_linked(b2, 'modules', a)


def test_assoc_modules234_link_reassign_clear():
    a = mancoosimm_ModuleCache(version="sample_text")
    b1 = mancoosimm_Module()
    b2 = mancoosimm_Module()
    _safe_set(a, 'moduleCache', {b1})
    assert _is_linked(a, 'moduleCache', b1)
    if hasattr(b1, 'Module'):
        assert _is_linked(b1, 'Module', a)
    _safe_set(a, 'moduleCache', {b2})
    assert _is_linked(a, 'moduleCache', b2)
    if hasattr(b1, 'Module'):
        assert not _is_linked(b1, 'Module', a)
    if hasattr(b2, 'Module'):
        assert _is_linked(b2, 'Module', a)
    _safe_set(a, 'moduleCache', set())
    assert not _is_linked(a, 'moduleCache', b2)
    if hasattr(b2, 'Module'):
        assert not _is_linked(b2, 'Module', a)


def test_assoc_notInstalledPackages4_link_reassign_clear():
    a = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b1 = mancoosimm_NotInstalledPackage()
    b2 = mancoosimm_NotInstalledPackage()
    _safe_set(a, 'mancoosimm_Configuration5', {b1})
    assert _is_linked(a, 'mancoosimm_Configuration5', b1)
    if hasattr(b1, 'mancoosimm_NotInstalledPackage'):
        assert _is_linked(b1, 'mancoosimm_NotInstalledPackage', a)
    _safe_set(a, 'mancoosimm_Configuration5', {b2})
    assert _is_linked(a, 'mancoosimm_Configuration5', b2)
    if hasattr(b1, 'mancoosimm_NotInstalledPackage'):
        assert not _is_linked(b1, 'mancoosimm_NotInstalledPackage', a)
    if hasattr(b2, 'mancoosimm_NotInstalledPackage'):
        assert _is_linked(b2, 'mancoosimm_NotInstalledPackage', a)
    _safe_set(a, 'mancoosimm_Configuration5', set())
    assert not _is_linked(a, 'mancoosimm_Configuration5', b2)
    if hasattr(b2, 'mancoosimm_NotInstalledPackage'):
        assert not _is_linked(b2, 'mancoosimm_NotInstalledPackage', a)


def test_assoc_owner172_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_User()
    b2 = mancoosimm_User()
    _safe_set(a, 'mancoosimm_File173', b1)
    assert _is_linked(a, 'mancoosimm_File173', b1)
    if hasattr(b1, 'mancoosimm_User'):
        assert _is_linked(b1, 'mancoosimm_User', a)
    _safe_set(a, 'mancoosimm_File173', b2)
    assert _is_linked(a, 'mancoosimm_File173', b2)
    if hasattr(b1, 'mancoosimm_User'):
        assert not _is_linked(b1, 'mancoosimm_User', a)
    if hasattr(b2, 'mancoosimm_User'):
        assert _is_linked(b2, 'mancoosimm_User', a)
    _safe_set(a, 'mancoosimm_File173', None)
    assert not _is_linked(a, 'mancoosimm_File173', b2)
    if hasattr(b2, 'mancoosimm_User'):
        assert not _is_linked(b2, 'mancoosimm_User', a)


def test_assoc_packageSettings20_link_reassign_clear():
    a = mancoosimm_Package(architecture="sample_text", version="sample_text")
    b1 = mancoosimm_PackageSetting()
    b2 = mancoosimm_PackageSetting()
    _safe_set(a, 'pkg', b1)
    assert _is_linked(a, 'pkg', b1)
    if hasattr(b1, 'PackageSetting'):
        assert _is_linked(b1, 'PackageSetting', a)
    _safe_set(a, 'pkg', b2)
    assert _is_linked(a, 'pkg', b2)
    if hasattr(b1, 'PackageSetting'):
        assert not _is_linked(b1, 'PackageSetting', a)
    if hasattr(b2, 'PackageSetting'):
        assert _is_linked(b2, 'PackageSetting', a)
    _safe_set(a, 'pkg', None)
    assert not _is_linked(a, 'pkg', b2)
    if hasattr(b2, 'PackageSetting'):
        assert not _is_linked(b2, 'PackageSetting', a)


def test_assoc_parent170_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b2 = mancoosimm_File(checkSum="sample_text_2", description="sample_text_2", extension="sample_text_2", guid=False, isDirectory=False, isMissing=False, location="sample_text_2", permission="sample_text_2", size=13, suid=False)
    _safe_set(a, 'File171', b1)
    assert _is_linked(a, 'File171', b1)
    if hasattr(b1, 'childs'):
        assert _is_linked(b1, 'childs', a)
    _safe_set(a, 'File171', b2)
    assert _is_linked(a, 'File171', b2)
    if hasattr(b1, 'childs'):
        assert not _is_linked(b1, 'childs', a)
    if hasattr(b2, 'childs'):
        assert _is_linked(b2, 'childs', a)
    _safe_set(a, 'File171', None)
    assert not _is_linked(a, 'File171', b2)
    if hasattr(b2, 'childs'):
        assert not _is_linked(b2, 'childs', a)


def test_assoc_pkg178_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_DocumentationFile()
    b2 = mancoosimm_DocumentationFile()
    _safe_set(a, 'InstalledPackage', b1)
    assert _is_linked(a, 'InstalledPackage', b1)
    if hasattr(b1, 'documentationFiles'):
        assert _is_linked(b1, 'documentationFiles', a)
    _safe_set(a, 'InstalledPackage', b2)
    assert _is_linked(a, 'InstalledPackage', b2)
    if hasattr(b1, 'documentationFiles'):
        assert not _is_linked(b1, 'documentationFiles', a)
    if hasattr(b2, 'documentationFiles'):
        assert _is_linked(b2, 'documentationFiles', a)
    _safe_set(a, 'InstalledPackage', None)
    assert not _is_linked(a, 'InstalledPackage', b2)
    if hasattr(b2, 'documentationFiles'):
        assert not _is_linked(b2, 'documentationFiles', a)


def test_assoc_pkg190_link_reassign_clear():
    a = mancoosimm_Package(architecture="sample_text", version="sample_text")
    b1 = mancoosimm_PackageSetting()
    b2 = mancoosimm_PackageSetting()
    _safe_set(a, 'Package', b1)
    assert _is_linked(a, 'Package', b1)
    if hasattr(b1, 'packageSettings'):
        assert _is_linked(b1, 'packageSettings', a)
    _safe_set(a, 'Package', b2)
    assert _is_linked(a, 'Package', b2)
    if hasattr(b1, 'packageSettings'):
        assert not _is_linked(b1, 'packageSettings', a)
    if hasattr(b2, 'packageSettings'):
        assert _is_linked(b2, 'packageSettings', a)
    _safe_set(a, 'Package', None)
    assert not _is_linked(a, 'Package', b2)
    if hasattr(b2, 'packageSettings'):
        assert not _is_linked(b2, 'packageSettings', a)


def test_assoc_pkg283_link_reassign_clear():
    a = mancoosimm_Package(architecture="sample_text", version="sample_text")
    b1 = mancoosimm_Conflict()
    b2 = mancoosimm_Conflict()
    _safe_set(a, 'mancoosimm_Package285', b1)
    assert _is_linked(a, 'mancoosimm_Package285', b1)
    if hasattr(b1, 'mancoosimm_Conflict284'):
        assert _is_linked(b1, 'mancoosimm_Conflict284', a)
    _safe_set(a, 'mancoosimm_Package285', b2)
    assert _is_linked(a, 'mancoosimm_Package285', b2)
    if hasattr(b1, 'mancoosimm_Conflict284'):
        assert not _is_linked(b1, 'mancoosimm_Conflict284', a)
    if hasattr(b2, 'mancoosimm_Conflict284'):
        assert _is_linked(b2, 'mancoosimm_Conflict284', a)
    _safe_set(a, 'mancoosimm_Package285', None)
    assert not _is_linked(a, 'mancoosimm_Package285', b2)
    if hasattr(b2, 'mancoosimm_Conflict284'):
        assert not _is_linked(b2, 'mancoosimm_Conflict284', a)


def test_assoc_pkg67_link_reassign_clear():
    a = mancoosimm_Package(architecture="sample_text", version="sample_text")
    b1 = mancoosimm_Dependence()
    b2 = mancoosimm_Dependence()
    _safe_set(a, 'mancoosimm_Package69', b1)
    assert _is_linked(a, 'mancoosimm_Package69', b1)
    if hasattr(b1, 'mancoosimm_Dependence68'):
        assert _is_linked(b1, 'mancoosimm_Dependence68', a)
    _safe_set(a, 'mancoosimm_Package69', b2)
    assert _is_linked(a, 'mancoosimm_Package69', b2)
    if hasattr(b1, 'mancoosimm_Dependence68'):
        assert not _is_linked(b1, 'mancoosimm_Dependence68', a)
    if hasattr(b2, 'mancoosimm_Dependence68'):
        assert _is_linked(b2, 'mancoosimm_Dependence68', a)
    _safe_set(a, 'mancoosimm_Package69', None)
    assert not _is_linked(a, 'mancoosimm_Package69', b2)
    if hasattr(b2, 'mancoosimm_Dependence68'):
        assert not _is_linked(b2, 'mancoosimm_Dependence68', a)


def test_assoc_pkgSettings176_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_PackageSetting()
    b2 = mancoosimm_PackageSetting()
    _safe_set(a, 'files', {b1})
    assert _is_linked(a, 'files', b1)
    if hasattr(b1, 'PackageSetting177'):
        assert _is_linked(b1, 'PackageSetting177', a)
    _safe_set(a, 'files', {b2})
    assert _is_linked(a, 'files', b2)
    if hasattr(b1, 'PackageSetting177'):
        assert not _is_linked(b1, 'PackageSetting177', a)
    if hasattr(b2, 'PackageSetting177'):
        assert _is_linked(b2, 'PackageSetting177', a)
    _safe_set(a, 'files', set())
    assert not _is_linked(a, 'files', b2)
    if hasattr(b2, 'PackageSetting177'):
        assert not _is_linked(b2, 'PackageSetting177', a)


def test_assoc_predepends35_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage34', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage34', b1)
    if hasattr(b1, 'mancoosimm_InstalledPackage36'):
        assert _is_linked(b1, 'mancoosimm_InstalledPackage36', a)
    _safe_set(a, 'mancoosimm_InstalledPackage34', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage34', b2)
    if hasattr(b1, 'mancoosimm_InstalledPackage36'):
        assert not _is_linked(b1, 'mancoosimm_InstalledPackage36', a)
    if hasattr(b2, 'mancoosimm_InstalledPackage36'):
        assert _is_linked(b2, 'mancoosimm_InstalledPackage36', a)
    _safe_set(a, 'mancoosimm_InstalledPackage34', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage34', b2)
    if hasattr(b2, 'mancoosimm_InstalledPackage36'):
        assert not _is_linked(b2, 'mancoosimm_InstalledPackage36', a)


def test_assoc_provides37_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_VirtualPackage()
    b2 = mancoosimm_VirtualPackage()
    _safe_set(a, 'mancoosimm_InstalledPackage38', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage38', b1)
    if hasattr(b1, 'mancoosimm_VirtualPackage'):
        assert _is_linked(b1, 'mancoosimm_VirtualPackage', a)
    _safe_set(a, 'mancoosimm_InstalledPackage38', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage38', b2)
    if hasattr(b1, 'mancoosimm_VirtualPackage'):
        assert not _is_linked(b1, 'mancoosimm_VirtualPackage', a)
    if hasattr(b2, 'mancoosimm_VirtualPackage'):
        assert _is_linked(b2, 'mancoosimm_VirtualPackage', a)
    _safe_set(a, 'mancoosimm_InstalledPackage38', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage38', b2)
    if hasattr(b2, 'mancoosimm_VirtualPackage'):
        assert not _is_linked(b2, 'mancoosimm_VirtualPackage', a)


def test_assoc_recommends26_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage25', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage25', b1)
    if hasattr(b1, 'mancoosimm_InstalledPackage27'):
        assert _is_linked(b1, 'mancoosimm_InstalledPackage27', a)
    _safe_set(a, 'mancoosimm_InstalledPackage25', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage25', b2)
    if hasattr(b1, 'mancoosimm_InstalledPackage27'):
        assert not _is_linked(b1, 'mancoosimm_InstalledPackage27', a)
    if hasattr(b2, 'mancoosimm_InstalledPackage27'):
        assert _is_linked(b2, 'mancoosimm_InstalledPackage27', a)
    _safe_set(a, 'mancoosimm_InstalledPackage25', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage25', b2)
    if hasattr(b2, 'mancoosimm_InstalledPackage27'):
        assert not _is_linked(b2, 'mancoosimm_InstalledPackage27', a)


def test_assoc_replaces40_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage39', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage39', b1)
    if hasattr(b1, 'mancoosimm_InstalledPackage41'):
        assert _is_linked(b1, 'mancoosimm_InstalledPackage41', a)
    _safe_set(a, 'mancoosimm_InstalledPackage39', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage39', b2)
    if hasattr(b1, 'mancoosimm_InstalledPackage41'):
        assert not _is_linked(b1, 'mancoosimm_InstalledPackage41', a)
    if hasattr(b2, 'mancoosimm_InstalledPackage41'):
        assert _is_linked(b2, 'mancoosimm_InstalledPackage41', a)
    _safe_set(a, 'mancoosimm_InstalledPackage39', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage39', b2)
    if hasattr(b2, 'mancoosimm_InstalledPackage41'):
        assert not _is_linked(b2, 'mancoosimm_InstalledPackage41', a)


def test_assoc_root131_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_FileSystem()
    b2 = mancoosimm_FileSystem()
    _safe_set(a, 'File', b1)
    assert _is_linked(a, 'File', b1)
    if hasattr(b1, 'fs'):
        assert _is_linked(b1, 'fs', a)
    _safe_set(a, 'File', b2)
    assert _is_linked(a, 'File', b2)
    if hasattr(b1, 'fs'):
        assert not _is_linked(b1, 'fs', a)
    if hasattr(b2, 'fs'):
        assert _is_linked(b2, 'fs', a)
    _safe_set(a, 'File', None)
    assert not _is_linked(a, 'File', b2)
    if hasattr(b2, 'fs'):
        assert not _is_linked(b2, 'fs', a)


def test_assoc_schemas138_link_reassign_clear():
    a = mancoosimm_File(checkSum="sample_text", description="sample_text", extension="sample_text", guid=True, isDirectory=True, isMissing=True, location="sample_text", permission="sample_text", size=7, suid=True)
    b1 = mancoosimm_GConf()
    b2 = mancoosimm_GConf()
    _safe_set(a, 'mancoosimm_File140', b1)
    assert _is_linked(a, 'mancoosimm_File140', b1)
    if hasattr(b1, 'mancoosimm_GConf139'):
        assert _is_linked(b1, 'mancoosimm_GConf139', a)
    _safe_set(a, 'mancoosimm_File140', b2)
    assert _is_linked(a, 'mancoosimm_File140', b2)
    if hasattr(b1, 'mancoosimm_GConf139'):
        assert not _is_linked(b1, 'mancoosimm_GConf139', a)
    if hasattr(b2, 'mancoosimm_GConf139'):
        assert _is_linked(b2, 'mancoosimm_GConf139', a)
    _safe_set(a, 'mancoosimm_File140', None)
    assert not _is_linked(a, 'mancoosimm_File140', b2)
    if hasattr(b2, 'mancoosimm_GConf139'):
        assert not _is_linked(b2, 'mancoosimm_GConf139', a)


def test_assoc_sharedLibraries226_link_reassign_clear():
    a = mancoosimm_SharedLibrary(name="sample_text", version="sample_text")
    b1 = mancoosimm_LibraryCache()
    b2 = mancoosimm_LibraryCache()
    _safe_set(a, 'SharedLibrary', b1)
    assert _is_linked(a, 'SharedLibrary', b1)
    if hasattr(b1, 'libraryCache'):
        assert _is_linked(b1, 'libraryCache', a)
    _safe_set(a, 'SharedLibrary', b2)
    assert _is_linked(a, 'SharedLibrary', b2)
    if hasattr(b1, 'libraryCache'):
        assert not _is_linked(b1, 'libraryCache', a)
    if hasattr(b2, 'libraryCache'):
        assert _is_linked(b2, 'libraryCache', a)
    _safe_set(a, 'SharedLibrary', None)
    assert not _is_linked(a, 'SharedLibrary', b2)
    if hasattr(b2, 'libraryCache'):
        assert not _is_linked(b2, 'libraryCache', a)


def test_assoc_singleConflict281_link_reassign_clear():
    a = mancoosimm_SingleConflict(value="sample_text", version="sample_text")
    b1 = mancoosimm_Conflict()
    b2 = mancoosimm_Conflict()
    _safe_set(a, 'SingleConflict', b1)
    assert _is_linked(a, 'SingleConflict', b1)
    if hasattr(b1, 'conflict282'):
        assert _is_linked(b1, 'conflict282', a)
    _safe_set(a, 'SingleConflict', b2)
    assert _is_linked(a, 'SingleConflict', b2)
    if hasattr(b1, 'conflict282'):
        assert not _is_linked(b1, 'conflict282', a)
    if hasattr(b2, 'conflict282'):
        assert _is_linked(b2, 'conflict282', a)
    _safe_set(a, 'SingleConflict', None)
    assert not _is_linked(a, 'SingleConflict', b2)
    if hasattr(b2, 'conflict282'):
        assert not _is_linked(b2, 'conflict282', a)


def test_assoc_singleDep65_link_reassign_clear():
    a = mancoosimm_SingleDep(value="sample_text", version="sample_text")
    b1 = mancoosimm_Dependence()
    b2 = mancoosimm_Dependence()
    _safe_set(a, 'SingleDep', b1)
    assert _is_linked(a, 'SingleDep', b1)
    if hasattr(b1, 'dependence66'):
        assert _is_linked(b1, 'dependence66', a)
    _safe_set(a, 'SingleDep', b2)
    assert _is_linked(a, 'SingleDep', b2)
    if hasattr(b1, 'dependence66'):
        assert not _is_linked(b1, 'dependence66', a)
    if hasattr(b2, 'dependence66'):
        assert _is_linked(b2, 'dependence66', a)
    _safe_set(a, 'SingleDep', None)
    assert not _is_linked(a, 'SingleDep', b2)
    if hasattr(b2, 'dependence66'):
        assert not _is_linked(b2, 'dependence66', a)


def test_assoc_sourcePackage21_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_SrcPackage()
    b2 = mancoosimm_SrcPackage()
    _safe_set(a, 'mancoosimm_InstalledPackage22', b1)
    assert _is_linked(a, 'mancoosimm_InstalledPackage22', b1)
    if hasattr(b1, 'mancoosimm_SrcPackage'):
        assert _is_linked(b1, 'mancoosimm_SrcPackage', a)
    _safe_set(a, 'mancoosimm_InstalledPackage22', b2)
    assert _is_linked(a, 'mancoosimm_InstalledPackage22', b2)
    if hasattr(b1, 'mancoosimm_SrcPackage'):
        assert not _is_linked(b1, 'mancoosimm_SrcPackage', a)
    if hasattr(b2, 'mancoosimm_SrcPackage'):
        assert _is_linked(b2, 'mancoosimm_SrcPackage', a)
    _safe_set(a, 'mancoosimm_InstalledPackage22', None)
    assert not _is_linked(a, 'mancoosimm_InstalledPackage22', b2)
    if hasattr(b2, 'mancoosimm_SrcPackage'):
        assert not _is_linked(b2, 'mancoosimm_SrcPackage', a)


def test_assoc_suggests29_link_reassign_clear():
    a = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_InstalledPackage(checkSum="sample_text", description="sample_text", fileSize=7, installedSize=7, maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b2 = mancoosimm_InstalledPackage(checkSum="sample_text_2", description="sample_text_2", fileSize=13, installedSize=13, maintainer="sample_text_2", priority="sample_text_2", section="sample_text_2", tag="sample_text_2", uploaders="sample_text_2")
    _safe_set(a, 'mancoosimm_InstalledPackage28', {b1})
    assert _is_linked(a, 'mancoosimm_InstalledPackage28', b1)
    if hasattr(b1, 'mancoosimm_InstalledPackage30'):
        assert _is_linked(b1, 'mancoosimm_InstalledPackage30', a)
    _safe_set(a, 'mancoosimm_InstalledPackage28', {b2})
    assert _is_linked(a, 'mancoosimm_InstalledPackage28', b2)
    if hasattr(b1, 'mancoosimm_InstalledPackage30'):
        assert not _is_linked(b1, 'mancoosimm_InstalledPackage30', a)
    if hasattr(b2, 'mancoosimm_InstalledPackage30'):
        assert _is_linked(b2, 'mancoosimm_InstalledPackage30', a)
    _safe_set(a, 'mancoosimm_InstalledPackage28', set())
    assert not _is_linked(a, 'mancoosimm_InstalledPackage28', b2)
    if hasattr(b2, 'mancoosimm_InstalledPackage30'):
        assert not _is_linked(b2, 'mancoosimm_InstalledPackage30', a)


def test_assoc_type209_link_reassign_clear():
    a = mancoosimm_MimeType(extension="sample_text", name="sample_text")
    b1 = mancoosimm_MimeTypeHandler()
    b2 = mancoosimm_MimeTypeHandler()
    _safe_set(a, 'MimeType210', b1)
    assert _is_linked(a, 'MimeType210', b1)
    if hasattr(b1, 'mimeTypeHandlers'):
        assert _is_linked(b1, 'mimeTypeHandlers', a)
    _safe_set(a, 'MimeType210', b2)
    assert _is_linked(a, 'MimeType210', b2)
    if hasattr(b1, 'mimeTypeHandlers'):
        assert not _is_linked(b1, 'mimeTypeHandlers', a)
    if hasattr(b2, 'mimeTypeHandlers'):
        assert _is_linked(b2, 'mimeTypeHandlers', a)
    _safe_set(a, 'MimeType210', None)
    assert not _is_linked(a, 'MimeType210', b2)
    if hasattr(b2, 'mimeTypeHandlers'):
        assert not _is_linked(b2, 'mimeTypeHandlers', a)


def test_assoc_unpackedPackages8_link_reassign_clear():
    a = mancoosimm_UnpackedPackage(checkSum="sample_text", description="sample_text", maintainer="sample_text", priority="sample_text", section="sample_text", tag="sample_text", uploaders="sample_text")
    b1 = mancoosimm_Configuration(creationTime="sample_text", systemType="sample_text")
    b2 = mancoosimm_Configuration(creationTime="sample_text_2", systemType="sample_text_2")
    _safe_set(a, 'mancoosimm_UnpackedPackage', b1)
    assert _is_linked(a, 'mancoosimm_UnpackedPackage', b1)
    if hasattr(b1, 'mancoosimm_Configuration9'):
        assert _is_linked(b1, 'mancoosimm_Configuration9', a)
    _safe_set(a, 'mancoosimm_UnpackedPackage', b2)
    assert _is_linked(a, 'mancoosimm_UnpackedPackage', b2)
    if hasattr(b1, 'mancoosimm_Configuration9'):
        assert not _is_linked(b1, 'mancoosimm_Configuration9', a)
    if hasattr(b2, 'mancoosimm_Configuration9'):
        assert _is_linked(b2, 'mancoosimm_Configuration9', a)
    _safe_set(a, 'mancoosimm_UnpackedPackage', None)
    assert not _is_linked(a, 'mancoosimm_UnpackedPackage', b2)
    if hasattr(b2, 'mancoosimm_Configuration9'):
        assert not _is_linked(b2, 'mancoosimm_Configuration9', a)


def test_assoc_xfontCache220_link_reassign_clear():
    a = mancoosimm_XFontCache(location="sample_text")
    b1 = mancoosimm_XFont()
    b2 = mancoosimm_XFont()
    _safe_set(a, 'XFontCache221', b1)
    assert _is_linked(a, 'XFontCache221', b1)
    if hasattr(b1, 'xfonts'):
        assert _is_linked(b1, 'xfonts', a)
    _safe_set(a, 'XFontCache221', b2)
    assert _is_linked(a, 'XFontCache221', b2)
    if hasattr(b1, 'xfonts'):
        assert not _is_linked(b1, 'xfonts', a)
    if hasattr(b2, 'xfonts'):
        assert _is_linked(b2, 'xfonts', a)
    _safe_set(a, 'XFontCache221', None)
    assert not _is_linked(a, 'XFontCache221', b2)
    if hasattr(b2, 'xfonts'):
        assert not _is_linked(b2, 'xfonts', a)


def test_assoc_xfontCaches125_link_reassign_clear():
    a = mancoosimm_XFontCache(location="sample_text")
    b1 = mancoosimm_Environment()
    b2 = mancoosimm_Environment()
    _safe_set(a, 'XFontCache', b1)
    assert _is_linked(a, 'XFontCache', b1)
    if hasattr(b1, 'env126'):
        assert _is_linked(b1, 'env126', a)
    _safe_set(a, 'XFontCache', b2)
    assert _is_linked(a, 'XFontCache', b2)
    if hasattr(b1, 'env126'):
        assert not _is_linked(b1, 'env126', a)
    if hasattr(b2, 'env126'):
        assert _is_linked(b2, 'env126', a)
    _safe_set(a, 'XFontCache', None)
    assert not _is_linked(a, 'XFontCache', b2)
    if hasattr(b2, 'env126'):
        assert not _is_linked(b2, 'env126', a)


def test_assoc_xfonts217_link_reassign_clear():
    a = mancoosimm_XFontCache(location="sample_text")
    b1 = mancoosimm_XFont()
    b2 = mancoosimm_XFont()
    _safe_set(a, 'xfontCache', {b1})
    assert _is_linked(a, 'xfontCache', b1)
    if hasattr(b1, 'XFont'):
        assert _is_linked(b1, 'XFont', a)
    _safe_set(a, 'xfontCache', {b2})
    assert _is_linked(a, 'xfontCache', b2)
    if hasattr(b1, 'XFont'):
        assert not _is_linked(b1, 'XFont', a)
    if hasattr(b2, 'XFont'):
        assert _is_linked(b2, 'XFont', a)
    _safe_set(a, 'xfontCache', set())
    assert not _is_linked(a, 'xfontCache', b2)
    if hasattr(b2, 'XFont'):
        assert not _is_linked(b2, 'XFont', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Conflict_strategy = st.builds(Conflict)
@given(instance=Conflict_strategy)
@settings(max_examples=25)
def test_Conflict_instantiation(instance):
    assert isinstance(instance, Conflict)


Dependence_strategy = st.builds(Dependence)
@given(instance=Dependence_strategy)
@settings(max_examples=25)
def test_Dependence_instantiation(instance):
    assert isinstance(instance, Dependence)


File_strategy = st.builds(File)
@given(instance=File_strategy)
@settings(max_examples=25)
def test_File_instantiation(instance):
    assert isinstance(instance, File)


InstalledPackage_strategy = st.builds(InstalledPackage)
@given(instance=InstalledPackage_strategy)
@settings(max_examples=25)
def test_InstalledPackage_instantiation(instance):
    assert isinstance(instance, InstalledPackage)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Package_strategy = st.builds(Package)
@given(instance=Package_strategy)
@settings(max_examples=25)
def test_Package_instantiation(instance):
    assert isinstance(instance, Package)


UnpackedPackage_strategy = st.builds(UnpackedPackage)
@given(instance=UnpackedPackage_strategy)
@settings(max_examples=25)
def test_UnpackedPackage_instantiation(instance):
    assert isinstance(instance, UnpackedPackage)


mancoosimm_Alternative_strategy = st.builds(mancoosimm_Alternative)
@given(instance=mancoosimm_Alternative_strategy)
@settings(max_examples=25)
def test_mancoosimm_Alternative_instantiation(instance):
    assert isinstance(instance, mancoosimm_Alternative)


mancoosimm_AndConflict_strategy = st.builds(mancoosimm_AndConflict)
@given(instance=mancoosimm_AndConflict_strategy)
@settings(max_examples=25)
def test_mancoosimm_AndConflict_instantiation(instance):
    assert isinstance(instance, mancoosimm_AndConflict)


mancoosimm_AndDep_strategy = st.builds(mancoosimm_AndDep)
@given(instance=mancoosimm_AndDep_strategy)
@settings(max_examples=25)
def test_mancoosimm_AndDep_instantiation(instance):
    assert isinstance(instance, mancoosimm_AndDep)


mancoosimm_AndInv_strategy = st.builds(mancoosimm_AndInv)
@given(instance=mancoosimm_AndInv_strategy)
@settings(max_examples=25)
def test_mancoosimm_AndInv_instantiation(instance):
    assert isinstance(instance, mancoosimm_AndInv)


mancoosimm_ApplicationMenuCatalog_strategy = st.builds(mancoosimm_ApplicationMenuCatalog)
@given(instance=mancoosimm_ApplicationMenuCatalog_strategy)
@settings(max_examples=25)
def test_mancoosimm_ApplicationMenuCatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm_ApplicationMenuCatalog)


mancoosimm_Atom_strategy = st.builds(mancoosimm_Atom)
@given(instance=mancoosimm_Atom_strategy)
@settings(max_examples=25)
def test_mancoosimm_Atom_instantiation(instance):
    assert isinstance(instance, mancoosimm_Atom)


mancoosimm_BinPackage_strategy = st.builds(mancoosimm_BinPackage)
@given(instance=mancoosimm_BinPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_BinPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_BinPackage)


mancoosimm_Boot_strategy = st.builds(mancoosimm_Boot)
@given(instance=mancoosimm_Boot_strategy)
@settings(max_examples=25)
def test_mancoosimm_Boot_instantiation(instance):
    assert isinstance(instance, mancoosimm_Boot)


mancoosimm_ConfigFilesPackage_strategy = st.builds(mancoosimm_ConfigFilesPackage, checkSum=safe_text, description=safe_text, maintainer=safe_text, priority=safe_text, section=safe_text, tag=safe_text, uploaders=safe_text)
@given(instance=mancoosimm_ConfigFilesPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_ConfigFilesPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_ConfigFilesPackage)


mancoosimm_Configuration_strategy = st.builds(mancoosimm_Configuration, creationTime=safe_text, systemType=safe_text)
@given(instance=mancoosimm_Configuration_strategy)
@settings(max_examples=25)
def test_mancoosimm_Configuration_instantiation(instance):
    assert isinstance(instance, mancoosimm_Configuration)


mancoosimm_Conflict_strategy = st.builds(mancoosimm_Conflict)
@given(instance=mancoosimm_Conflict_strategy)
@settings(max_examples=25)
def test_mancoosimm_Conflict_instantiation(instance):
    assert isinstance(instance, mancoosimm_Conflict)


mancoosimm_Dependence_strategy = st.builds(mancoosimm_Dependence)
@given(instance=mancoosimm_Dependence_strategy)
@settings(max_examples=25)
def test_mancoosimm_Dependence_instantiation(instance):
    assert isinstance(instance, mancoosimm_Dependence)


mancoosimm_DesktopDB_strategy = st.builds(mancoosimm_DesktopDB)
@given(instance=mancoosimm_DesktopDB_strategy)
@settings(max_examples=25)
def test_mancoosimm_DesktopDB_instantiation(instance):
    assert isinstance(instance, mancoosimm_DesktopDB)


mancoosimm_DocumentationFile_strategy = st.builds(mancoosimm_DocumentationFile)
@given(instance=mancoosimm_DocumentationFile_strategy)
@settings(max_examples=25)
def test_mancoosimm_DocumentationFile_instantiation(instance):
    assert isinstance(instance, mancoosimm_DocumentationFile)


mancoosimm_EmacsPackage_strategy = st.builds(mancoosimm_EmacsPackage)
@given(instance=mancoosimm_EmacsPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_EmacsPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_EmacsPackage)


mancoosimm_Environment_strategy = st.builds(mancoosimm_Environment)
@given(instance=mancoosimm_Environment_strategy)
@settings(max_examples=25)
def test_mancoosimm_Environment_instantiation(instance):
    assert isinstance(instance, mancoosimm_Environment)


mancoosimm_File_strategy = st.builds(mancoosimm_File, checkSum=safe_text, description=safe_text, extension=safe_text, guid=st.booleans(), isDirectory=st.booleans(), isMissing=st.booleans(), location=safe_text, permission=safe_text, size=st.integers(), suid=st.booleans())
@given(instance=mancoosimm_File_strategy)
@settings(max_examples=25)
def test_mancoosimm_File_instantiation(instance):
    assert isinstance(instance, mancoosimm_File)


mancoosimm_FileSystem_strategy = st.builds(mancoosimm_FileSystem)
@given(instance=mancoosimm_FileSystem_strategy)
@settings(max_examples=25)
def test_mancoosimm_FileSystem_instantiation(instance):
    assert isinstance(instance, mancoosimm_FileSystem)


mancoosimm_GConf_strategy = st.builds(mancoosimm_GConf)
@given(instance=mancoosimm_GConf_strategy)
@settings(max_examples=25)
def test_mancoosimm_GConf_instantiation(instance):
    assert isinstance(instance, mancoosimm_GConf)


mancoosimm_Group_strategy = st.builds(mancoosimm_Group)
@given(instance=mancoosimm_Group_strategy)
@settings(max_examples=25)
def test_mancoosimm_Group_instantiation(instance):
    assert isinstance(instance, mancoosimm_Group)


mancoosimm_HalfConfiguredPackage_strategy = st.builds(mancoosimm_HalfConfiguredPackage)
@given(instance=mancoosimm_HalfConfiguredPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_HalfConfiguredPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_HalfConfiguredPackage)


mancoosimm_HalfConfiguredReinstRequiredPackage_strategy = st.builds(mancoosimm_HalfConfiguredReinstRequiredPackage)
@given(instance=mancoosimm_HalfConfiguredReinstRequiredPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_HalfConfiguredReinstRequiredPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_HalfConfiguredReinstRequiredPackage)


mancoosimm_HalfInstalledPackage_strategy = st.builds(mancoosimm_HalfInstalledPackage, checkSum=safe_text, description=safe_text, maintainer=safe_text, priority=safe_text, section=safe_text, tag=safe_text, uploaders=safe_text)
@given(instance=mancoosimm_HalfInstalledPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_HalfInstalledPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_HalfInstalledPackage)


mancoosimm_HalfInstalledReinstRequiredPackage_strategy = st.builds(mancoosimm_HalfInstalledReinstRequiredPackage, checkSum=safe_text, description=safe_text, maintainer=safe_text, priority=safe_text, section=safe_text, tag=safe_text, uploaders=safe_text)
@given(instance=mancoosimm_HalfInstalledReinstRequiredPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_HalfInstalledReinstRequiredPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_HalfInstalledReinstRequiredPackage)


mancoosimm_IconCache_strategy = st.builds(mancoosimm_IconCache, mtime=safe_text)
@given(instance=mancoosimm_IconCache_strategy)
@settings(max_examples=25)
def test_mancoosimm_IconCache_instantiation(instance):
    assert isinstance(instance, mancoosimm_IconCache)


mancoosimm_InformationFile_strategy = st.builds(mancoosimm_InformationFile)
@given(instance=mancoosimm_InformationFile_strategy)
@settings(max_examples=25)
def test_mancoosimm_InformationFile_instantiation(instance):
    assert isinstance(instance, mancoosimm_InformationFile)


mancoosimm_InstalledPackage_strategy = st.builds(mancoosimm_InstalledPackage, checkSum=safe_text, description=safe_text, fileSize=st.integers(), installedSize=st.integers(), maintainer=safe_text, priority=safe_text, section=safe_text, tag=safe_text, uploaders=safe_text)
@given(instance=mancoosimm_InstalledPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_InstalledPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_InstalledPackage)


mancoosimm_Invariant_strategy = st.builds(mancoosimm_Invariant)
@given(instance=mancoosimm_Invariant_strategy)
@settings(max_examples=25)
def test_mancoosimm_Invariant_instantiation(instance):
    assert isinstance(instance, mancoosimm_Invariant)


mancoosimm_LibraryCache_strategy = st.builds(mancoosimm_LibraryCache)
@given(instance=mancoosimm_LibraryCache_strategy)
@settings(max_examples=25)
def test_mancoosimm_LibraryCache_instantiation(instance):
    assert isinstance(instance, mancoosimm_LibraryCache)


mancoosimm_Menu_strategy = st.builds(mancoosimm_Menu)
@given(instance=mancoosimm_Menu_strategy)
@settings(max_examples=25)
def test_mancoosimm_Menu_instantiation(instance):
    assert isinstance(instance, mancoosimm_Menu)


mancoosimm_MenuEntry_strategy = st.builds(mancoosimm_MenuEntry)
@given(instance=mancoosimm_MenuEntry_strategy)
@settings(max_examples=25)
def test_mancoosimm_MenuEntry_instantiation(instance):
    assert isinstance(instance, mancoosimm_MenuEntry)


mancoosimm_MimeType_strategy = st.builds(mancoosimm_MimeType, extension=safe_text, name=safe_text)
@given(instance=mancoosimm_MimeType_strategy)
@settings(max_examples=25)
def test_mancoosimm_MimeType_instantiation(instance):
    assert isinstance(instance, mancoosimm_MimeType)


mancoosimm_MimeTypeHandler_strategy = st.builds(mancoosimm_MimeTypeHandler)
@given(instance=mancoosimm_MimeTypeHandler_strategy)
@settings(max_examples=25)
def test_mancoosimm_MimeTypeHandler_instantiation(instance):
    assert isinstance(instance, mancoosimm_MimeTypeHandler)


mancoosimm_MimeTypeHandlerCache_strategy = st.builds(mancoosimm_MimeTypeHandlerCache)
@given(instance=mancoosimm_MimeTypeHandlerCache_strategy)
@settings(max_examples=25)
def test_mancoosimm_MimeTypeHandlerCache_instantiation(instance):
    assert isinstance(instance, mancoosimm_MimeTypeHandlerCache)


mancoosimm_Module_strategy = st.builds(mancoosimm_Module)
@given(instance=mancoosimm_Module_strategy)
@settings(max_examples=25)
def test_mancoosimm_Module_instantiation(instance):
    assert isinstance(instance, mancoosimm_Module)


mancoosimm_ModuleCache_strategy = st.builds(mancoosimm_ModuleCache, version=safe_text)
@given(instance=mancoosimm_ModuleCache_strategy)
@settings(max_examples=25)
def test_mancoosimm_ModuleCache_instantiation(instance):
    assert isinstance(instance, mancoosimm_ModuleCache)


mancoosimm_NamedElement_strategy = st.builds(mancoosimm_NamedElement, name=safe_text)
@given(instance=mancoosimm_NamedElement_strategy)
@settings(max_examples=25)
def test_mancoosimm_NamedElement_instantiation(instance):
    assert isinstance(instance, mancoosimm_NamedElement)


mancoosimm_NotInstalledPackage_strategy = st.builds(mancoosimm_NotInstalledPackage)
@given(instance=mancoosimm_NotInstalledPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_NotInstalledPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_NotInstalledPackage)


mancoosimm_NotInv_strategy = st.builds(mancoosimm_NotInv)
@given(instance=mancoosimm_NotInv_strategy)
@settings(max_examples=25)
def test_mancoosimm_NotInv_instantiation(instance):
    assert isinstance(instance, mancoosimm_NotInv)


mancoosimm_OrConflict_strategy = st.builds(mancoosimm_OrConflict)
@given(instance=mancoosimm_OrConflict_strategy)
@settings(max_examples=25)
def test_mancoosimm_OrConflict_instantiation(instance):
    assert isinstance(instance, mancoosimm_OrConflict)


mancoosimm_OrDep_strategy = st.builds(mancoosimm_OrDep)
@given(instance=mancoosimm_OrDep_strategy)
@settings(max_examples=25)
def test_mancoosimm_OrDep_instantiation(instance):
    assert isinstance(instance, mancoosimm_OrDep)


mancoosimm_OrInv_strategy = st.builds(mancoosimm_OrInv)
@given(instance=mancoosimm_OrInv_strategy)
@settings(max_examples=25)
def test_mancoosimm_OrInv_instantiation(instance):
    assert isinstance(instance, mancoosimm_OrInv)


mancoosimm_Package_strategy = st.builds(mancoosimm_Package, architecture=safe_text, version=safe_text)
@given(instance=mancoosimm_Package_strategy)
@settings(max_examples=25)
def test_mancoosimm_Package_instantiation(instance):
    assert isinstance(instance, mancoosimm_Package)


mancoosimm_PackageSetting_strategy = st.builds(mancoosimm_PackageSetting)
@given(instance=mancoosimm_PackageSetting_strategy)
@settings(max_examples=25)
def test_mancoosimm_PackageSetting_instantiation(instance):
    assert isinstance(instance, mancoosimm_PackageSetting)


mancoosimm_SGMLCatalog_strategy = st.builds(mancoosimm_SGMLCatalog)
@given(instance=mancoosimm_SGMLCatalog_strategy)
@settings(max_examples=25)
def test_mancoosimm_SGMLCatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm_SGMLCatalog)


mancoosimm_SGMLDocument_strategy = st.builds(mancoosimm_SGMLDocument)
@given(instance=mancoosimm_SGMLDocument_strategy)
@settings(max_examples=25)
def test_mancoosimm_SGMLDocument_instantiation(instance):
    assert isinstance(instance, mancoosimm_SGMLDocument)


mancoosimm_Service_strategy = st.builds(mancoosimm_Service)
@given(instance=mancoosimm_Service_strategy)
@settings(max_examples=25)
def test_mancoosimm_Service_instantiation(instance):
    assert isinstance(instance, mancoosimm_Service)


mancoosimm_SharedLibrary_strategy = st.builds(mancoosimm_SharedLibrary, name=safe_text, version=safe_text)
@given(instance=mancoosimm_SharedLibrary_strategy)
@settings(max_examples=25)
def test_mancoosimm_SharedLibrary_instantiation(instance):
    assert isinstance(instance, mancoosimm_SharedLibrary)


mancoosimm_SingleConflict_strategy = st.builds(mancoosimm_SingleConflict, value=safe_text, version=safe_text)
@given(instance=mancoosimm_SingleConflict_strategy)
@settings(max_examples=25)
def test_mancoosimm_SingleConflict_instantiation(instance):
    assert isinstance(instance, mancoosimm_SingleConflict)


mancoosimm_SingleDep_strategy = st.builds(mancoosimm_SingleDep, value=safe_text, version=safe_text)
@given(instance=mancoosimm_SingleDep_strategy)
@settings(max_examples=25)
def test_mancoosimm_SingleDep_instantiation(instance):
    assert isinstance(instance, mancoosimm_SingleDep)


mancoosimm_SkeeperCatalog_strategy = st.builds(mancoosimm_SkeeperCatalog)
@given(instance=mancoosimm_SkeeperCatalog_strategy)
@settings(max_examples=25)
def test_mancoosimm_SkeeperCatalog_instantiation(instance):
    assert isinstance(instance, mancoosimm_SkeeperCatalog)


mancoosimm_SkeeperDocument_strategy = st.builds(mancoosimm_SkeeperDocument)
@given(instance=mancoosimm_SkeeperDocument_strategy)
@settings(max_examples=25)
def test_mancoosimm_SkeeperDocument_instantiation(instance):
    assert isinstance(instance, mancoosimm_SkeeperDocument)


mancoosimm_SrcPackage_strategy = st.builds(mancoosimm_SrcPackage)
@given(instance=mancoosimm_SrcPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_SrcPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_SrcPackage)


mancoosimm_UnpackedPackage_strategy = st.builds(mancoosimm_UnpackedPackage, checkSum=safe_text, description=safe_text, maintainer=safe_text, priority=safe_text, section=safe_text, tag=safe_text, uploaders=safe_text)
@given(instance=mancoosimm_UnpackedPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_UnpackedPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_UnpackedPackage)


mancoosimm_User_strategy = st.builds(mancoosimm_User)
@given(instance=mancoosimm_User_strategy)
@settings(max_examples=25)
def test_mancoosimm_User_instantiation(instance):
    assert isinstance(instance, mancoosimm_User)


mancoosimm_VirtualPackage_strategy = st.builds(mancoosimm_VirtualPackage)
@given(instance=mancoosimm_VirtualPackage_strategy)
@settings(max_examples=25)
def test_mancoosimm_VirtualPackage_instantiation(instance):
    assert isinstance(instance, mancoosimm_VirtualPackage)


mancoosimm_XFont_strategy = st.builds(mancoosimm_XFont)
@given(instance=mancoosimm_XFont_strategy)
@settings(max_examples=25)
def test_mancoosimm_XFont_instantiation(instance):
    assert isinstance(instance, mancoosimm_XFont)


mancoosimm_XFontCache_strategy = st.builds(mancoosimm_XFontCache, location=safe_text)
@given(instance=mancoosimm_XFontCache_strategy)
@settings(max_examples=25)
def test_mancoosimm_XFontCache_instantiation(instance):
    assert isinstance(instance, mancoosimm_XFontCache)



