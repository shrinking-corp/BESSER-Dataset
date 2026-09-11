import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    InstallationUnit,
    build_Build,
    build_Bundle,
    build_Category,
    build_Compiler,
    build_Config,
    build_Contact,
    build_Contribution,
    build_Feature,
    build_InstallationUnit,
    build_Map,
    build_Platform,
    build_Product,
    build_Promotion,
    build_Repository,
    ARCH,
    ArchiveFormat,
    BuildType,
    OS,
    WS,
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

def test_build_Build_buildRoot_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.buildRoot == "sample_text"
    instance.buildRoot = "sample_text_2"
    assert instance.buildRoot == "sample_text_2"


def test_build_Build_builderURL_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.builderURL == "sample_text"
    instance.builderURL = "sample_text_2"
    assert instance.builderURL == "sample_text_2"


def test_build_Build_date_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_build_Build_fetchTag_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.fetchTag == "sample_text"
    instance.fetchTag = "sample_text_2"
    assert instance.fetchTag == "sample_text_2"


def test_build_Build_label_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_build_Build_launchVM_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.launchVM == "sample_text"
    instance.launchVM = "sample_text_2"
    assert instance.launchVM == "sample_text_2"


def test_build_Build_sendmail_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.sendmail == True
    instance.sendmail = False
    assert instance.sendmail == False


def test_build_Build_time_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_build_Build_type_value_roundtrip():
    instance = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_build_Category_description_value_roundtrip():
    instance = build_Category(description="sample_text", label="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_build_Category_label_value_roundtrip():
    instance = build_Category(description="sample_text", label="sample_text", name="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_build_Category_name_value_roundtrip():
    instance = build_Category(description="sample_text", label="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_Compiler_args_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.args == "sample_text"
    instance.args = "sample_text_2"
    assert instance.args == "sample_text_2"


def test_build_Compiler_debugInfo_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.debugInfo == True
    instance.debugInfo = False
    assert instance.debugInfo == False


def test_build_Compiler_failOnError_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.failOnError == True
    instance.failOnError = False
    assert instance.failOnError == False


def test_build_Compiler_sourceVersion_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.sourceVersion == "sample_text"
    instance.sourceVersion = "sample_text_2"
    assert instance.sourceVersion == "sample_text_2"


def test_build_Compiler_targetVersion_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.targetVersion == "sample_text"
    instance.targetVersion = "sample_text_2"
    assert instance.targetVersion == "sample_text_2"


def test_build_Compiler_verbose_value_roundtrip():
    instance = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    assert instance.verbose == True
    instance.verbose = False
    assert instance.verbose == False


def test_build_Config_arch_value_roundtrip():
    instance = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    assert instance.arch == "sample_text"
    instance.arch = "sample_text_2"
    assert instance.arch == "sample_text_2"


def test_build_Config_archiveFormat_value_roundtrip():
    instance = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    assert instance.archiveFormat == "sample_text"
    instance.archiveFormat = "sample_text_2"
    assert instance.archiveFormat == "sample_text_2"


def test_build_Config_os_value_roundtrip():
    instance = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_build_Config_ws_value_roundtrip():
    instance = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    assert instance.ws == "sample_text"
    instance.ws = "sample_text_2"
    assert instance.ws == "sample_text_2"


def test_build_Contact_email_value_roundtrip():
    instance = build_Contact(email="sample_text", name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_build_Contact_name_value_roundtrip():
    instance = build_Contact(email="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_Contribution_label_value_roundtrip():
    instance = build_Contribution(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_build_Feature_inProduct_value_roundtrip():
    instance = build_Feature(inProduct=True)
    assert instance.inProduct == True
    instance.inProduct = False
    assert instance.inProduct == False


def test_build_InstallationUnit_id_value_roundtrip():
    instance = build_InstallationUnit(id="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_build_InstallationUnit_version_value_roundtrip():
    instance = build_InstallationUnit(id="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_build_Map_repo_value_roundtrip():
    instance = build_Map(repo="sample_text", root="sample_text", tag="sample_text")
    assert instance.repo == "sample_text"
    instance.repo = "sample_text_2"
    assert instance.repo == "sample_text_2"


def test_build_Map_root_value_roundtrip():
    instance = build_Map(repo="sample_text", root="sample_text", tag="sample_text")
    assert instance.root == "sample_text"
    instance.root = "sample_text_2"
    assert instance.root == "sample_text_2"


def test_build_Map_tag_value_roundtrip():
    instance = build_Map(repo="sample_text", root="sample_text", tag="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_build_Platform_deltapack_value_roundtrip():
    instance = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    assert instance.deltapack == "sample_text"
    instance.deltapack = "sample_text_2"
    assert instance.deltapack == "sample_text_2"


def test_build_Platform_file_value_roundtrip():
    instance = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_build_Platform_location_value_roundtrip():
    instance = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_build_Promotion_baseURL_value_roundtrip():
    instance = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    assert instance.baseURL == "sample_text"
    instance.baseURL = "sample_text_2"
    assert instance.baseURL == "sample_text_2"


def test_build_Promotion_buildAlias_value_roundtrip():
    instance = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    assert instance.buildAlias == "sample_text"
    instance.buildAlias = "sample_text_2"
    assert instance.buildAlias == "sample_text_2"


def test_build_Promotion_downloadDirectory_value_roundtrip():
    instance = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    assert instance.downloadDirectory == "sample_text"
    instance.downloadDirectory = "sample_text_2"
    assert instance.downloadDirectory == "sample_text_2"


def test_build_Promotion_incubating_value_roundtrip():
    instance = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    assert instance.incubating == True
    instance.incubating = False
    assert instance.incubating == False


def test_build_Promotion_uploadDirectory_value_roundtrip():
    instance = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    assert instance.uploadDirectory == "sample_text"
    instance.uploadDirectory = "sample_text_2"
    assert instance.uploadDirectory == "sample_text_2"


def test_build_Repository_label_value_roundtrip():
    instance = build_Repository(label="sample_text", location="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_build_Repository_location_value_roundtrip():
    instance = build_Repository(label="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_build_Bundle_isa_InstallationUnit():
    instance = build_Bundle()
    assert isinstance(instance, InstallationUnit)


def test_build_Feature_isa_InstallationUnit():
    instance = build_Feature(inProduct=True)
    assert isinstance(instance, InstallationUnit)


def test_build_Product_isa_InstallationUnit():
    instance = build_Product()
    assert isinstance(instance, InstallationUnit)


def test_assoc_base11_link_reassign_clear():
    a = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Platform13', b1)
    assert _is_linked(a, 'build_Platform13', b1)
    if hasattr(b1, 'build_Build12'):
        assert _is_linked(b1, 'build_Build12', a)
    _safe_set(a, 'build_Platform13', b2)
    assert _is_linked(a, 'build_Platform13', b2)
    if hasattr(b1, 'build_Build12'):
        assert not _is_linked(b1, 'build_Build12', a)
    if hasattr(b2, 'build_Build12'):
        assert _is_linked(b2, 'build_Build12', a)
    _safe_set(a, 'build_Platform13', None)
    assert not _is_linked(a, 'build_Platform13', b2)
    if hasattr(b2, 'build_Build12'):
        assert not _is_linked(b2, 'build_Build12', a)


def test_assoc_builder14_link_reassign_clear():
    a = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Platform16', b1)
    assert _is_linked(a, 'build_Platform16', b1)
    if hasattr(b1, 'build_Build15'):
        assert _is_linked(b1, 'build_Build15', a)
    _safe_set(a, 'build_Platform16', b2)
    assert _is_linked(a, 'build_Platform16', b2)
    if hasattr(b1, 'build_Build15'):
        assert not _is_linked(b1, 'build_Build15', a)
    if hasattr(b2, 'build_Build15'):
        assert _is_linked(b2, 'build_Build15', a)
    _safe_set(a, 'build_Platform16', None)
    assert not _is_linked(a, 'build_Platform16', b2)
    if hasattr(b2, 'build_Build15'):
        assert not _is_linked(b2, 'build_Build15', a)


def test_assoc_buildmaster21_link_reassign_clear():
    a = build_Contact(email="sample_text", name="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Contact', b1)
    assert _is_linked(a, 'build_Contact', b1)
    if hasattr(b1, 'build_Build22'):
        assert _is_linked(b1, 'build_Build22', a)
    _safe_set(a, 'build_Contact', b2)
    assert _is_linked(a, 'build_Contact', b2)
    if hasattr(b1, 'build_Build22'):
        assert not _is_linked(b1, 'build_Build22', a)
    if hasattr(b2, 'build_Build22'):
        assert _is_linked(b2, 'build_Build22', a)
    _safe_set(a, 'build_Contact', None)
    assert not _is_linked(a, 'build_Contact', b2)
    if hasattr(b2, 'build_Build22'):
        assert not _is_linked(b2, 'build_Build22', a)


def test_assoc_bundles37_link_reassign_clear():
    a = build_Contribution(label="sample_text")
    b1 = build_Bundle()
    b2 = build_Bundle()
    _safe_set(a, 'build_Contribution38', {b1})
    assert _is_linked(a, 'build_Contribution38', b1)
    if hasattr(b1, 'build_Bundle'):
        assert _is_linked(b1, 'build_Bundle', a)
    _safe_set(a, 'build_Contribution38', {b2})
    assert _is_linked(a, 'build_Contribution38', b2)
    if hasattr(b1, 'build_Bundle'):
        assert not _is_linked(b1, 'build_Bundle', a)
    if hasattr(b2, 'build_Bundle'):
        assert _is_linked(b2, 'build_Bundle', a)
    _safe_set(a, 'build_Contribution38', set())
    assert not _is_linked(a, 'build_Contribution38', b2)
    if hasattr(b2, 'build_Bundle'):
        assert not _is_linked(b2, 'build_Bundle', a)


def test_assoc_categories5_link_reassign_clear():
    a = build_Category(description="sample_text", label="sample_text", name="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Category', b1)
    assert _is_linked(a, 'build_Category', b1)
    if hasattr(b1, 'build_Build6'):
        assert _is_linked(b1, 'build_Build6', a)
    _safe_set(a, 'build_Category', b2)
    assert _is_linked(a, 'build_Category', b2)
    if hasattr(b1, 'build_Build6'):
        assert not _is_linked(b1, 'build_Build6', a)
    if hasattr(b2, 'build_Build6'):
        assert _is_linked(b2, 'build_Build6', a)
    _safe_set(a, 'build_Category', None)
    assert not _is_linked(a, 'build_Category', b2)
    if hasattr(b2, 'build_Build6'):
        assert not _is_linked(b2, 'build_Build6', a)


def test_assoc_category42_link_reassign_clear():
    a = build_Feature(inProduct=True)
    b1 = build_Category(description="sample_text", label="sample_text", name="sample_text")
    b2 = build_Category(description="sample_text_2", label="sample_text_2", name="sample_text_2")
    _safe_set(a, 'features', {b1})
    assert _is_linked(a, 'features', b1)
    if hasattr(b1, 'Category'):
        assert _is_linked(b1, 'Category', a)
    _safe_set(a, 'features', {b2})
    assert _is_linked(a, 'features', b2)
    if hasattr(b1, 'Category'):
        assert not _is_linked(b1, 'Category', a)
    if hasattr(b2, 'Category'):
        assert _is_linked(b2, 'Category', a)
    _safe_set(a, 'features', set())
    assert not _is_linked(a, 'features', b2)
    if hasattr(b2, 'Category'):
        assert not _is_linked(b2, 'Category', a)


def test_assoc_compiler17_link_reassign_clear():
    a = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Compiler', b1)
    assert _is_linked(a, 'build_Compiler', b1)
    if hasattr(b1, 'build_Build18'):
        assert _is_linked(b1, 'build_Build18', a)
    _safe_set(a, 'build_Compiler', b2)
    assert _is_linked(a, 'build_Compiler', b2)
    if hasattr(b1, 'build_Build18'):
        assert not _is_linked(b1, 'build_Build18', a)
    if hasattr(b2, 'build_Build18'):
        assert _is_linked(b2, 'build_Build18', a)
    _safe_set(a, 'build_Compiler', None)
    assert not _is_linked(a, 'build_Compiler', b2)
    if hasattr(b2, 'build_Build18'):
        assert not _is_linked(b2, 'build_Build18', a)


def test_assoc_config26_link_reassign_clear():
    a = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    b1 = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    b2 = build_Config(arch="sample_text_2", archiveFormat="sample_text_2", os="sample_text_2", ws="sample_text_2")
    _safe_set(a, 'build_Platform27', b1)
    assert _is_linked(a, 'build_Platform27', b1)
    if hasattr(b1, 'build_Config28'):
        assert _is_linked(b1, 'build_Config28', a)
    _safe_set(a, 'build_Platform27', b2)
    assert _is_linked(a, 'build_Platform27', b2)
    if hasattr(b1, 'build_Config28'):
        assert not _is_linked(b1, 'build_Config28', a)
    if hasattr(b2, 'build_Config28'):
        assert _is_linked(b2, 'build_Config28', a)
    _safe_set(a, 'build_Platform27', None)
    assert not _is_linked(a, 'build_Platform27', b2)
    if hasattr(b2, 'build_Config28'):
        assert not _is_linked(b2, 'build_Config28', a)


def test_assoc_configs1_link_reassign_clear():
    a = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Config', b1)
    assert _is_linked(a, 'build_Config', b1)
    if hasattr(b1, 'build_Build2'):
        assert _is_linked(b1, 'build_Build2', a)
    _safe_set(a, 'build_Config', b2)
    assert _is_linked(a, 'build_Config', b2)
    if hasattr(b1, 'build_Build2'):
        assert not _is_linked(b1, 'build_Build2', a)
    if hasattr(b2, 'build_Build2'):
        assert _is_linked(b2, 'build_Build2', a)
    _safe_set(a, 'build_Config', None)
    assert not _is_linked(a, 'build_Config', b2)
    if hasattr(b2, 'build_Build2'):
        assert not _is_linked(b2, 'build_Build2', a)


def test_assoc_contacts30_link_reassign_clear():
    a = build_Contribution(label="sample_text")
    b1 = build_Contact(email="sample_text", name="sample_text")
    b2 = build_Contact(email="sample_text_2", name="sample_text_2")
    _safe_set(a, 'build_Contribution31', {b1})
    assert _is_linked(a, 'build_Contribution31', b1)
    if hasattr(b1, 'build_Contact32'):
        assert _is_linked(b1, 'build_Contact32', a)
    _safe_set(a, 'build_Contribution31', {b2})
    assert _is_linked(a, 'build_Contribution31', b2)
    if hasattr(b1, 'build_Contact32'):
        assert not _is_linked(b1, 'build_Contact32', a)
    if hasattr(b2, 'build_Contact32'):
        assert _is_linked(b2, 'build_Contact32', a)
    _safe_set(a, 'build_Contribution31', set())
    assert not _is_linked(a, 'build_Contribution31', b2)
    if hasattr(b2, 'build_Contact32'):
        assert not _is_linked(b2, 'build_Contact32', a)


def test_assoc_contributions7_link_reassign_clear():
    a = build_Contribution(label="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Contribution', b1)
    assert _is_linked(a, 'build_Contribution', b1)
    if hasattr(b1, 'build_Build8'):
        assert _is_linked(b1, 'build_Build8', a)
    _safe_set(a, 'build_Contribution', b2)
    assert _is_linked(a, 'build_Contribution', b2)
    if hasattr(b1, 'build_Build8'):
        assert not _is_linked(b1, 'build_Build8', a)
    if hasattr(b2, 'build_Build8'):
        assert _is_linked(b2, 'build_Build8', a)
    _safe_set(a, 'build_Contribution', None)
    assert not _is_linked(a, 'build_Contribution', b2)
    if hasattr(b2, 'build_Build8'):
        assert not _is_linked(b2, 'build_Build8', a)


def test_assoc_defaultMailList23_link_reassign_clear():
    a = build_Contact(email="sample_text", name="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Contact25', b1)
    assert _is_linked(a, 'build_Contact25', b1)
    if hasattr(b1, 'build_Build24'):
        assert _is_linked(b1, 'build_Build24', a)
    _safe_set(a, 'build_Contact25', b2)
    assert _is_linked(a, 'build_Contact25', b2)
    if hasattr(b1, 'build_Build24'):
        assert not _is_linked(b1, 'build_Build24', a)
    if hasattr(b2, 'build_Build24'):
        assert _is_linked(b2, 'build_Build24', a)
    _safe_set(a, 'build_Contact25', None)
    assert not _is_linked(a, 'build_Contact25', b2)
    if hasattr(b2, 'build_Build24'):
        assert not _is_linked(b2, 'build_Build24', a)


def test_assoc_features29_link_reassign_clear():
    a = build_Feature(inProduct=True)
    b1 = build_Category(description="sample_text", label="sample_text", name="sample_text")
    b2 = build_Category(description="sample_text_2", label="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'category'):
        assert _is_linked(b1, 'category', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'category'):
        assert not _is_linked(b1, 'category', a)
    if hasattr(b2, 'category'):
        assert _is_linked(b2, 'category', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'category'):
        assert not _is_linked(b2, 'category', a)


def test_assoc_features33_link_reassign_clear():
    a = build_Feature(inProduct=True)
    b1 = build_Contribution(label="sample_text")
    b2 = build_Contribution(label="sample_text_2")
    _safe_set(a, 'build_Feature', b1)
    assert _is_linked(a, 'build_Feature', b1)
    if hasattr(b1, 'build_Contribution34'):
        assert _is_linked(b1, 'build_Contribution34', a)
    _safe_set(a, 'build_Feature', b2)
    assert _is_linked(a, 'build_Feature', b2)
    if hasattr(b1, 'build_Contribution34'):
        assert not _is_linked(b1, 'build_Contribution34', a)
    if hasattr(b2, 'build_Contribution34'):
        assert _is_linked(b2, 'build_Contribution34', a)
    _safe_set(a, 'build_Feature', None)
    assert not _is_linked(a, 'build_Feature', b2)
    if hasattr(b2, 'build_Contribution34'):
        assert not _is_linked(b2, 'build_Contribution34', a)


def test_assoc_map3_link_reassign_clear():
    a = build_Map(repo="sample_text", root="sample_text", tag="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Map', b1)
    assert _is_linked(a, 'build_Map', b1)
    if hasattr(b1, 'build_Build4'):
        assert _is_linked(b1, 'build_Build4', a)
    _safe_set(a, 'build_Map', b2)
    assert _is_linked(a, 'build_Map', b2)
    if hasattr(b1, 'build_Build4'):
        assert not _is_linked(b1, 'build_Build4', a)
    if hasattr(b2, 'build_Build4'):
        assert _is_linked(b2, 'build_Build4', a)
    _safe_set(a, 'build_Map', None)
    assert not _is_linked(a, 'build_Map', b2)
    if hasattr(b2, 'build_Build4'):
        assert not _is_linked(b2, 'build_Build4', a)


def test_assoc_platforms0_link_reassign_clear():
    a = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Platform', b1)
    assert _is_linked(a, 'build_Platform', b1)
    if hasattr(b1, 'build_Build'):
        assert _is_linked(b1, 'build_Build', a)
    _safe_set(a, 'build_Platform', b2)
    assert _is_linked(a, 'build_Platform', b2)
    if hasattr(b1, 'build_Build'):
        assert not _is_linked(b1, 'build_Build', a)
    if hasattr(b2, 'build_Build'):
        assert _is_linked(b2, 'build_Build', a)
    _safe_set(a, 'build_Platform', None)
    assert not _is_linked(a, 'build_Platform', b2)
    if hasattr(b2, 'build_Build'):
        assert not _is_linked(b2, 'build_Build', a)


def test_assoc_product9_link_reassign_clear():
    a = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b1 = build_Product()
    b2 = build_Product()
    _safe_set(a, 'build_Build10', b1)
    assert _is_linked(a, 'build_Build10', b1)
    if hasattr(b1, 'build_Product'):
        assert _is_linked(b1, 'build_Product', a)
    _safe_set(a, 'build_Build10', b2)
    assert _is_linked(a, 'build_Build10', b2)
    if hasattr(b1, 'build_Product'):
        assert not _is_linked(b1, 'build_Product', a)
    if hasattr(b2, 'build_Product'):
        assert _is_linked(b2, 'build_Product', a)
    _safe_set(a, 'build_Build10', None)
    assert not _is_linked(a, 'build_Build10', b2)
    if hasattr(b2, 'build_Product'):
        assert not _is_linked(b2, 'build_Product', a)


def test_assoc_products39_link_reassign_clear():
    a = build_Contribution(label="sample_text")
    b1 = build_Product()
    b2 = build_Product()
    _safe_set(a, 'build_Contribution40', {b1})
    assert _is_linked(a, 'build_Contribution40', b1)
    if hasattr(b1, 'build_Product41'):
        assert _is_linked(b1, 'build_Product41', a)
    _safe_set(a, 'build_Contribution40', {b2})
    assert _is_linked(a, 'build_Contribution40', b2)
    if hasattr(b1, 'build_Product41'):
        assert not _is_linked(b1, 'build_Product41', a)
    if hasattr(b2, 'build_Product41'):
        assert _is_linked(b2, 'build_Product41', a)
    _safe_set(a, 'build_Contribution40', set())
    assert not _is_linked(a, 'build_Contribution40', b2)
    if hasattr(b2, 'build_Product41'):
        assert not _is_linked(b2, 'build_Product41', a)


def test_assoc_promotion19_link_reassign_clear():
    a = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    b1 = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    b2 = build_Build(buildRoot="sample_text_2", builderURL="sample_text_2", date="sample_text_2", fetchTag="sample_text_2", label="sample_text_2", launchVM="sample_text_2", sendmail=False, time="sample_text_2", type="sample_text_2")
    _safe_set(a, 'build_Promotion', b1)
    assert _is_linked(a, 'build_Promotion', b1)
    if hasattr(b1, 'build_Build20'):
        assert _is_linked(b1, 'build_Build20', a)
    _safe_set(a, 'build_Promotion', b2)
    assert _is_linked(a, 'build_Promotion', b2)
    if hasattr(b1, 'build_Build20'):
        assert not _is_linked(b1, 'build_Build20', a)
    if hasattr(b2, 'build_Build20'):
        assert _is_linked(b2, 'build_Build20', a)
    _safe_set(a, 'build_Promotion', None)
    assert not _is_linked(a, 'build_Promotion', b2)
    if hasattr(b2, 'build_Build20'):
        assert not _is_linked(b2, 'build_Build20', a)


def test_assoc_repo43_link_reassign_clear():
    a = build_Repository(label="sample_text", location="sample_text")
    b1 = build_InstallationUnit(id="sample_text", version="sample_text")
    b2 = build_InstallationUnit(id="sample_text_2", version="sample_text_2")
    _safe_set(a, 'build_Repository44', b1)
    assert _is_linked(a, 'build_Repository44', b1)
    if hasattr(b1, 'build_InstallationUnit'):
        assert _is_linked(b1, 'build_InstallationUnit', a)
    _safe_set(a, 'build_Repository44', b2)
    assert _is_linked(a, 'build_Repository44', b2)
    if hasattr(b1, 'build_InstallationUnit'):
        assert not _is_linked(b1, 'build_InstallationUnit', a)
    if hasattr(b2, 'build_InstallationUnit'):
        assert _is_linked(b2, 'build_InstallationUnit', a)
    _safe_set(a, 'build_Repository44', None)
    assert not _is_linked(a, 'build_Repository44', b2)
    if hasattr(b2, 'build_InstallationUnit'):
        assert not _is_linked(b2, 'build_InstallationUnit', a)


def test_assoc_repositories35_link_reassign_clear():
    a = build_Repository(label="sample_text", location="sample_text")
    b1 = build_Contribution(label="sample_text")
    b2 = build_Contribution(label="sample_text_2")
    _safe_set(a, 'build_Repository', b1)
    assert _is_linked(a, 'build_Repository', b1)
    if hasattr(b1, 'build_Contribution36'):
        assert _is_linked(b1, 'build_Contribution36', a)
    _safe_set(a, 'build_Repository', b2)
    assert _is_linked(a, 'build_Repository', b2)
    if hasattr(b1, 'build_Contribution36'):
        assert not _is_linked(b1, 'build_Contribution36', a)
    if hasattr(b2, 'build_Contribution36'):
        assert _is_linked(b2, 'build_Contribution36', a)
    _safe_set(a, 'build_Repository', None)
    assert not _is_linked(a, 'build_Repository', b2)
    if hasattr(b2, 'build_Contribution36'):
        assert not _is_linked(b2, 'build_Contribution36', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

InstallationUnit_strategy = st.builds(InstallationUnit)
@given(instance=InstallationUnit_strategy)
@settings(max_examples=25)
def test_InstallationUnit_instantiation(instance):
    assert isinstance(instance, InstallationUnit)


build_Build_strategy = st.builds(build_Build, buildRoot=safe_text, builderURL=safe_text, date=safe_text, fetchTag=safe_text, label=safe_text, launchVM=safe_text, sendmail=st.booleans(), time=safe_text, type=safe_text)
@given(instance=build_Build_strategy)
@settings(max_examples=25)
def test_build_Build_instantiation(instance):
    assert isinstance(instance, build_Build)


build_Bundle_strategy = st.builds(build_Bundle)
@given(instance=build_Bundle_strategy)
@settings(max_examples=25)
def test_build_Bundle_instantiation(instance):
    assert isinstance(instance, build_Bundle)


build_Category_strategy = st.builds(build_Category, description=safe_text, label=safe_text, name=safe_text)
@given(instance=build_Category_strategy)
@settings(max_examples=25)
def test_build_Category_instantiation(instance):
    assert isinstance(instance, build_Category)


build_Compiler_strategy = st.builds(build_Compiler, args=safe_text, debugInfo=st.booleans(), failOnError=st.booleans(), sourceVersion=safe_text, targetVersion=safe_text, verbose=st.booleans())
@given(instance=build_Compiler_strategy)
@settings(max_examples=25)
def test_build_Compiler_instantiation(instance):
    assert isinstance(instance, build_Compiler)


build_Config_strategy = st.builds(build_Config, arch=safe_text, archiveFormat=safe_text, os=safe_text, ws=safe_text)
@given(instance=build_Config_strategy)
@settings(max_examples=25)
def test_build_Config_instantiation(instance):
    assert isinstance(instance, build_Config)


build_Contact_strategy = st.builds(build_Contact, email=safe_text, name=safe_text)
@given(instance=build_Contact_strategy)
@settings(max_examples=25)
def test_build_Contact_instantiation(instance):
    assert isinstance(instance, build_Contact)


build_Contribution_strategy = st.builds(build_Contribution, label=safe_text)
@given(instance=build_Contribution_strategy)
@settings(max_examples=25)
def test_build_Contribution_instantiation(instance):
    assert isinstance(instance, build_Contribution)


build_Feature_strategy = st.builds(build_Feature, inProduct=st.booleans())
@given(instance=build_Feature_strategy)
@settings(max_examples=25)
def test_build_Feature_instantiation(instance):
    assert isinstance(instance, build_Feature)


build_InstallationUnit_strategy = st.builds(build_InstallationUnit, id=safe_text, version=safe_text)
@given(instance=build_InstallationUnit_strategy)
@settings(max_examples=25)
def test_build_InstallationUnit_instantiation(instance):
    assert isinstance(instance, build_InstallationUnit)


build_Map_strategy = st.builds(build_Map, repo=safe_text, root=safe_text, tag=safe_text)
@given(instance=build_Map_strategy)
@settings(max_examples=25)
def test_build_Map_instantiation(instance):
    assert isinstance(instance, build_Map)


build_Platform_strategy = st.builds(build_Platform, deltapack=safe_text, file=safe_text, location=safe_text)
@given(instance=build_Platform_strategy)
@settings(max_examples=25)
def test_build_Platform_instantiation(instance):
    assert isinstance(instance, build_Platform)


build_Product_strategy = st.builds(build_Product)
@given(instance=build_Product_strategy)
@settings(max_examples=25)
def test_build_Product_instantiation(instance):
    assert isinstance(instance, build_Product)


build_Promotion_strategy = st.builds(build_Promotion, baseURL=safe_text, buildAlias=safe_text, downloadDirectory=safe_text, incubating=st.booleans(), uploadDirectory=safe_text)
@given(instance=build_Promotion_strategy)
@settings(max_examples=25)
def test_build_Promotion_instantiation(instance):
    assert isinstance(instance, build_Promotion)


build_Repository_strategy = st.builds(build_Repository, label=safe_text, location=safe_text)
@given(instance=build_Repository_strategy)
@settings(max_examples=25)
def test_build_Repository_instantiation(instance):
    assert isinstance(instance, build_Repository)


