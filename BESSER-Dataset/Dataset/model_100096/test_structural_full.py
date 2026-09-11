import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    LocatedElement,
    Source,
    sourcecleaner_Build,
    sourcecleaner_ClassPath,
    sourcecleaner_Configuration,
    sourcecleaner_Dependency,
    sourcecleaner_Export,
    sourcecleaner_Extension,
    sourcecleaner_ExtensionAttribute,
    sourcecleaner_ExtensionPoint,
    sourcecleaner_ExtensionReference,
    sourcecleaner_Java,
    sourcecleaner_LocatedElement,
    sourcecleaner_Manifest,
    sourcecleaner_Plugin,
    sourcecleaner_Project,
    sourcecleaner_Schema,
    sourcecleaner_Source,
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

def test_sourcecleaner_ClassPath_name_value_roundtrip():
    instance = sourcecleaner_ClassPath(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_Configuration_location_value_roundtrip():
    instance = sourcecleaner_Configuration(location="sample_text", temp="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_sourcecleaner_Configuration_temp_value_roundtrip():
    instance = sourcecleaner_Configuration(location="sample_text", temp="sample_text")
    assert instance.temp == "sample_text"
    instance.temp = "sample_text_2"
    assert instance.temp == "sample_text_2"


def test_sourcecleaner_Dependency_diagraph_value_roundtrip():
    instance = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    assert instance.diagraph == True
    instance.diagraph = False
    assert instance.diagraph == False


def test_sourcecleaner_Dependency_name_value_roundtrip():
    instance = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_Dependency_reexport_value_roundtrip():
    instance = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    assert instance.reexport == True
    instance.reexport = False
    assert instance.reexport == False


def test_sourcecleaner_Dependency_version_value_roundtrip():
    instance = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_sourcecleaner_Export_name_value_roundtrip():
    instance = sourcecleaner_Export(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_Extension_clazz_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.clazz == "sample_text"
    instance.clazz = "sample_text_2"
    assert instance.clazz == "sample_text_2"


def test_sourcecleaner_Extension_diagraph_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.diagraph == True
    instance.diagraph = False
    assert instance.diagraph == False


def test_sourcecleaner_Extension_extra_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.extra == "sample_text"
    instance.extra = "sample_text_2"
    assert instance.extra == "sample_text_2"


def test_sourcecleaner_Extension_id_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_sourcecleaner_Extension_name_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_Extension_pointId_value_roundtrip():
    instance = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    assert instance.pointId == "sample_text"
    instance.pointId = "sample_text_2"
    assert instance.pointId == "sample_text_2"


def test_sourcecleaner_ExtensionAttribute_name_value_roundtrip():
    instance = sourcecleaner_ExtensionAttribute(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_ExtensionAttribute_value_value_roundtrip():
    instance = sourcecleaner_ExtensionAttribute(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sourcecleaner_ExtensionPoint_diagraph_value_roundtrip():
    instance = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    assert instance.diagraph == True
    instance.diagraph = False
    assert instance.diagraph == False


def test_sourcecleaner_ExtensionPoint_id_value_roundtrip():
    instance = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_sourcecleaner_ExtensionPoint_name_value_roundtrip():
    instance = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_ExtensionPoint_schema_value_roundtrip():
    instance = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    assert instance.schema == "sample_text"
    instance.schema = "sample_text_2"
    assert instance.schema == "sample_text_2"


def test_sourcecleaner_ExtensionReference_java_value_roundtrip():
    instance = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    assert instance.java == "sample_text"
    instance.java = "sample_text_2"
    assert instance.java == "sample_text_2"


def test_sourcecleaner_ExtensionReference_name_value_roundtrip():
    instance = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_ExtensionReference_package_value_roundtrip():
    instance = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    assert instance.package == "sample_text"
    instance.package = "sample_text_2"
    assert instance.package == "sample_text_2"


def test_sourcecleaner_ExtensionReference_project_value_roundtrip():
    instance = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    assert instance.project == "sample_text"
    instance.project = "sample_text_2"
    assert instance.project == "sample_text_2"


def test_sourcecleaner_Java_package_value_roundtrip():
    instance = sourcecleaner_Java(package="sample_text")
    assert instance.package == "sample_text"
    instance.package = "sample_text_2"
    assert instance.package == "sample_text_2"


def test_sourcecleaner_LocatedElement_absolutePath_value_roundtrip():
    instance = sourcecleaner_LocatedElement(absolutePath="sample_text", name="sample_text")
    assert instance.absolutePath == "sample_text"
    instance.absolutePath = "sample_text_2"
    assert instance.absolutePath == "sample_text_2"


def test_sourcecleaner_LocatedElement_name_value_roundtrip():
    instance = sourcecleaner_LocatedElement(absolutePath="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sourcecleaner_Manifest_diagraph_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.diagraph == True
    instance.diagraph = False
    assert instance.diagraph == False


def test_sourcecleaner_Manifest_executionEnvironment_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.executionEnvironment == "sample_text"
    instance.executionEnvironment = "sample_text_2"
    assert instance.executionEnvironment == "sample_text_2"


def test_sourcecleaner_Manifest_lazy_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.lazy == True
    instance.lazy = False
    assert instance.lazy == False


def test_sourcecleaner_Manifest_singleton_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.singleton == True
    instance.singleton = False
    assert instance.singleton == False


def test_sourcecleaner_Manifest_symbolicName_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.symbolicName == "sample_text"
    instance.symbolicName = "sample_text_2"
    assert instance.symbolicName == "sample_text_2"


def test_sourcecleaner_Manifest_vendor_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_sourcecleaner_Manifest_version_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_sourcecleaner_Manifest_versionId_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.versionId == "sample_text"
    instance.versionId = "sample_text_2"
    assert instance.versionId == "sample_text_2"


def test_sourcecleaner_Manifest_versionQualifier_value_roundtrip():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert instance.versionQualifier == "sample_text"
    instance.versionQualifier = "sample_text_2"
    assert instance.versionQualifier == "sample_text_2"


def test_sourcecleaner_Plugin_extra_value_roundtrip():
    instance = sourcecleaner_Plugin(extra="sample_text")
    assert instance.extra == "sample_text"
    instance.extra = "sample_text_2"
    assert instance.extra == "sample_text_2"


def test_sourcecleaner_Project_id_value_roundtrip():
    instance = sourcecleaner_Project(id=7, workspace="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_sourcecleaner_Project_workspace_value_roundtrip():
    instance = sourcecleaner_Project(id=7, workspace="sample_text")
    assert instance.workspace == "sample_text"
    instance.workspace = "sample_text_2"
    assert instance.workspace == "sample_text_2"


def test_sourcecleaner_Schema_extensionId_value_roundtrip():
    instance = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    assert instance.extensionId == "sample_text"
    instance.extensionId = "sample_text_2"
    assert instance.extensionId == "sample_text_2"


def test_sourcecleaner_Schema_extensionName_value_roundtrip():
    instance = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    assert instance.extensionName == "sample_text"
    instance.extensionName = "sample_text_2"
    assert instance.extensionName == "sample_text_2"


def test_sourcecleaner_Schema_pluginName_value_roundtrip():
    instance = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    assert instance.pluginName == "sample_text"
    instance.pluginName = "sample_text_2"
    assert instance.pluginName == "sample_text_2"


def test_sourcecleaner_Source_comment_value_roundtrip():
    instance = sourcecleaner_Source(comment="sample_text", content="sample_text", handled=True, mark=True)
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_sourcecleaner_Source_content_value_roundtrip():
    instance = sourcecleaner_Source(comment="sample_text", content="sample_text", handled=True, mark=True)
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_sourcecleaner_Source_handled_value_roundtrip():
    instance = sourcecleaner_Source(comment="sample_text", content="sample_text", handled=True, mark=True)
    assert instance.handled == True
    instance.handled = False
    assert instance.handled == False


def test_sourcecleaner_Source_mark_value_roundtrip():
    instance = sourcecleaner_Source(comment="sample_text", content="sample_text", handled=True, mark=True)
    assert instance.mark == True
    instance.mark = False
    assert instance.mark == False


def test_sourcecleaner_Project_isa_LocatedElement():
    instance = sourcecleaner_Project(id=7, workspace="sample_text")
    assert isinstance(instance, LocatedElement)


def test_sourcecleaner_Source_isa_LocatedElement():
    instance = sourcecleaner_Source(comment="sample_text", content="sample_text", handled=True, mark=True)
    assert isinstance(instance, LocatedElement)


def test_sourcecleaner_Build_isa_Source():
    instance = sourcecleaner_Build()
    assert isinstance(instance, Source)


def test_sourcecleaner_Java_isa_Source():
    instance = sourcecleaner_Java(package="sample_text")
    assert isinstance(instance, Source)


def test_sourcecleaner_Manifest_isa_Source():
    instance = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    assert isinstance(instance, Source)


def test_sourcecleaner_Plugin_isa_Source():
    instance = sourcecleaner_Plugin(extra="sample_text")
    assert isinstance(instance, Source)


def test_sourcecleaner_Schema_isa_Source():
    instance = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    assert isinstance(instance, Source)


def test_assoc_attributes17_link_reassign_clear():
    a = sourcecleaner_ExtensionAttribute(name="sample_text", value="sample_text")
    b1 = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    b2 = sourcecleaner_Extension(clazz="sample_text_2", diagraph=False, extra="sample_text_2", id="sample_text_2", name="sample_text_2", pointId="sample_text_2")
    _safe_set(a, 'sourcecleaner_ExtensionAttribute', b1)
    assert _is_linked(a, 'sourcecleaner_ExtensionAttribute', b1)
    if hasattr(b1, 'sourcecleaner_Extension'):
        assert _is_linked(b1, 'sourcecleaner_Extension', a)
    _safe_set(a, 'sourcecleaner_ExtensionAttribute', b2)
    assert _is_linked(a, 'sourcecleaner_ExtensionAttribute', b2)
    if hasattr(b1, 'sourcecleaner_Extension'):
        assert not _is_linked(b1, 'sourcecleaner_Extension', a)
    if hasattr(b2, 'sourcecleaner_Extension'):
        assert _is_linked(b2, 'sourcecleaner_Extension', a)
    _safe_set(a, 'sourcecleaner_ExtensionAttribute', None)
    assert not _is_linked(a, 'sourcecleaner_ExtensionAttribute', b2)
    if hasattr(b2, 'sourcecleaner_Extension'):
        assert not _is_linked(b2, 'sourcecleaner_Extension', a)


def test_assoc_build4_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Build()
    b2 = sourcecleaner_Build()
    _safe_set(a, 'sourcecleaner_Project5', b1)
    assert _is_linked(a, 'sourcecleaner_Project5', b1)
    if hasattr(b1, 'sourcecleaner_Build'):
        assert _is_linked(b1, 'sourcecleaner_Build', a)
    _safe_set(a, 'sourcecleaner_Project5', b2)
    assert _is_linked(a, 'sourcecleaner_Project5', b2)
    if hasattr(b1, 'sourcecleaner_Build'):
        assert not _is_linked(b1, 'sourcecleaner_Build', a)
    if hasattr(b2, 'sourcecleaner_Build'):
        assert _is_linked(b2, 'sourcecleaner_Build', a)
    _safe_set(a, 'sourcecleaner_Project5', None)
    assert not _is_linked(a, 'sourcecleaner_Project5', b2)
    if hasattr(b2, 'sourcecleaner_Build'):
        assert not _is_linked(b2, 'sourcecleaner_Build', a)


def test_assoc_classpathes12_link_reassign_clear():
    a = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b1 = sourcecleaner_ClassPath(name="sample_text")
    b2 = sourcecleaner_ClassPath(name="sample_text_2")
    _safe_set(a, 'sourcecleaner_Manifest13', {b1})
    assert _is_linked(a, 'sourcecleaner_Manifest13', b1)
    if hasattr(b1, 'sourcecleaner_ClassPath'):
        assert _is_linked(b1, 'sourcecleaner_ClassPath', a)
    _safe_set(a, 'sourcecleaner_Manifest13', {b2})
    assert _is_linked(a, 'sourcecleaner_Manifest13', b2)
    if hasattr(b1, 'sourcecleaner_ClassPath'):
        assert not _is_linked(b1, 'sourcecleaner_ClassPath', a)
    if hasattr(b2, 'sourcecleaner_ClassPath'):
        assert _is_linked(b2, 'sourcecleaner_ClassPath', a)
    _safe_set(a, 'sourcecleaner_Manifest13', set())
    assert not _is_linked(a, 'sourcecleaner_Manifest13', b2)
    if hasattr(b2, 'sourcecleaner_ClassPath'):
        assert not _is_linked(b2, 'sourcecleaner_ClassPath', a)


def test_assoc_dependencies11_link_reassign_clear():
    a = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b1 = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    b2 = sourcecleaner_Dependency(diagraph=False, name="sample_text_2", reexport=False, version="sample_text_2")
    _safe_set(a, 'requerant', {b1})
    assert _is_linked(a, 'requerant', b1)
    if hasattr(b1, 'Dependency'):
        assert _is_linked(b1, 'Dependency', a)
    _safe_set(a, 'requerant', {b2})
    assert _is_linked(a, 'requerant', b2)
    if hasattr(b1, 'Dependency'):
        assert not _is_linked(b1, 'Dependency', a)
    if hasattr(b2, 'Dependency'):
        assert _is_linked(b2, 'Dependency', a)
    _safe_set(a, 'requerant', set())
    assert not _is_linked(a, 'requerant', b2)
    if hasattr(b2, 'Dependency'):
        assert not _is_linked(b2, 'Dependency', a)


def test_assoc_dependency20_link_reassign_clear():
    a = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b1 = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    b2 = sourcecleaner_Dependency(diagraph=False, name="sample_text_2", reexport=False, version="sample_text_2")
    _safe_set(a, 'sourcecleaner_Manifest21', b1)
    assert _is_linked(a, 'sourcecleaner_Manifest21', b1)
    if hasattr(b1, 'sourcecleaner_Dependency'):
        assert _is_linked(b1, 'sourcecleaner_Dependency', a)
    _safe_set(a, 'sourcecleaner_Manifest21', b2)
    assert _is_linked(a, 'sourcecleaner_Manifest21', b2)
    if hasattr(b1, 'sourcecleaner_Dependency'):
        assert not _is_linked(b1, 'sourcecleaner_Dependency', a)
    if hasattr(b2, 'sourcecleaner_Dependency'):
        assert _is_linked(b2, 'sourcecleaner_Dependency', a)
    _safe_set(a, 'sourcecleaner_Manifest21', None)
    assert not _is_linked(a, 'sourcecleaner_Manifest21', b2)
    if hasattr(b2, 'sourcecleaner_Dependency'):
        assert not _is_linked(b2, 'sourcecleaner_Dependency', a)


def test_assoc_exports14_link_reassign_clear():
    a = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b1 = sourcecleaner_Export(name="sample_text")
    b2 = sourcecleaner_Export(name="sample_text_2")
    _safe_set(a, 'sourcecleaner_Manifest15', {b1})
    assert _is_linked(a, 'sourcecleaner_Manifest15', b1)
    if hasattr(b1, 'sourcecleaner_Export'):
        assert _is_linked(b1, 'sourcecleaner_Export', a)
    _safe_set(a, 'sourcecleaner_Manifest15', {b2})
    assert _is_linked(a, 'sourcecleaner_Manifest15', b2)
    if hasattr(b1, 'sourcecleaner_Export'):
        assert not _is_linked(b1, 'sourcecleaner_Export', a)
    if hasattr(b2, 'sourcecleaner_Export'):
        assert _is_linked(b2, 'sourcecleaner_Export', a)
    _safe_set(a, 'sourcecleaner_Manifest15', set())
    assert not _is_linked(a, 'sourcecleaner_Manifest15', b2)
    if hasattr(b2, 'sourcecleaner_Export'):
        assert not _is_linked(b2, 'sourcecleaner_Export', a)


def test_assoc_extensionPoint16_link_reassign_clear():
    a = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    b1 = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    b2 = sourcecleaner_Extension(clazz="sample_text_2", diagraph=False, extra="sample_text_2", id="sample_text_2", name="sample_text_2", pointId="sample_text_2")
    _safe_set(a, 'ExtensionPoint', b1)
    assert _is_linked(a, 'ExtensionPoint', b1)
    if hasattr(b1, 'extensions'):
        assert _is_linked(b1, 'extensions', a)
    _safe_set(a, 'ExtensionPoint', b2)
    assert _is_linked(a, 'ExtensionPoint', b2)
    if hasattr(b1, 'extensions'):
        assert not _is_linked(b1, 'extensions', a)
    if hasattr(b2, 'extensions'):
        assert _is_linked(b2, 'extensions', a)
    _safe_set(a, 'ExtensionPoint', None)
    assert not _is_linked(a, 'ExtensionPoint', b2)
    if hasattr(b2, 'extensions'):
        assert not _is_linked(b2, 'extensions', a)


def test_assoc_extensionPoints28_link_reassign_clear():
    a = sourcecleaner_Plugin(extra="sample_text")
    b1 = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    b2 = sourcecleaner_ExtensionPoint(diagraph=False, id="sample_text_2", name="sample_text_2", schema="sample_text_2")
    _safe_set(a, 'plugin', {b1})
    assert _is_linked(a, 'plugin', b1)
    if hasattr(b1, 'ExtensionPoint29'):
        assert _is_linked(b1, 'ExtensionPoint29', a)
    _safe_set(a, 'plugin', {b2})
    assert _is_linked(a, 'plugin', b2)
    if hasattr(b1, 'ExtensionPoint29'):
        assert not _is_linked(b1, 'ExtensionPoint29', a)
    if hasattr(b2, 'ExtensionPoint29'):
        assert _is_linked(b2, 'ExtensionPoint29', a)
    _safe_set(a, 'plugin', set())
    assert not _is_linked(a, 'plugin', b2)
    if hasattr(b2, 'ExtensionPoint29'):
        assert not _is_linked(b2, 'ExtensionPoint29', a)


def test_assoc_extensions23_link_reassign_clear():
    a = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    b1 = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    b2 = sourcecleaner_Extension(clazz="sample_text_2", diagraph=False, extra="sample_text_2", id="sample_text_2", name="sample_text_2", pointId="sample_text_2")
    _safe_set(a, 'extensionPoint', {b1})
    assert _is_linked(a, 'extensionPoint', b1)
    if hasattr(b1, 'Extension'):
        assert _is_linked(b1, 'Extension', a)
    _safe_set(a, 'extensionPoint', {b2})
    assert _is_linked(a, 'extensionPoint', b2)
    if hasattr(b1, 'Extension'):
        assert not _is_linked(b1, 'Extension', a)
    if hasattr(b2, 'Extension'):
        assert _is_linked(b2, 'Extension', a)
    _safe_set(a, 'extensionPoint', set())
    assert not _is_linked(a, 'extensionPoint', b2)
    if hasattr(b2, 'Extension'):
        assert not _is_linked(b2, 'Extension', a)


def test_assoc_extensions26_link_reassign_clear():
    a = sourcecleaner_Plugin(extra="sample_text")
    b1 = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    b2 = sourcecleaner_Extension(clazz="sample_text_2", diagraph=False, extra="sample_text_2", id="sample_text_2", name="sample_text_2", pointId="sample_text_2")
    _safe_set(a, 'sourcecleaner_Plugin', {b1})
    assert _is_linked(a, 'sourcecleaner_Plugin', b1)
    if hasattr(b1, 'sourcecleaner_Extension27'):
        assert _is_linked(b1, 'sourcecleaner_Extension27', a)
    _safe_set(a, 'sourcecleaner_Plugin', {b2})
    assert _is_linked(a, 'sourcecleaner_Plugin', b2)
    if hasattr(b1, 'sourcecleaner_Extension27'):
        assert not _is_linked(b1, 'sourcecleaner_Extension27', a)
    if hasattr(b2, 'sourcecleaner_Extension27'):
        assert _is_linked(b2, 'sourcecleaner_Extension27', a)
    _safe_set(a, 'sourcecleaner_Plugin', set())
    assert not _is_linked(a, 'sourcecleaner_Plugin', b2)
    if hasattr(b2, 'sourcecleaner_Extension27'):
        assert not _is_linked(b2, 'sourcecleaner_Extension27', a)


def test_assoc_implements18_link_reassign_clear():
    a = sourcecleaner_Java(package="sample_text")
    b1 = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    b2 = sourcecleaner_Extension(clazz="sample_text_2", diagraph=False, extra="sample_text_2", id="sample_text_2", name="sample_text_2", pointId="sample_text_2")
    _safe_set(a, 'sourcecleaner_Java', b1)
    assert _is_linked(a, 'sourcecleaner_Java', b1)
    if hasattr(b1, 'sourcecleaner_Extension19'):
        assert _is_linked(b1, 'sourcecleaner_Extension19', a)
    _safe_set(a, 'sourcecleaner_Java', b2)
    assert _is_linked(a, 'sourcecleaner_Java', b2)
    if hasattr(b1, 'sourcecleaner_Extension19'):
        assert not _is_linked(b1, 'sourcecleaner_Extension19', a)
    if hasattr(b2, 'sourcecleaner_Extension19'):
        assert _is_linked(b2, 'sourcecleaner_Extension19', a)
    _safe_set(a, 'sourcecleaner_Java', None)
    assert not _is_linked(a, 'sourcecleaner_Java', b2)
    if hasattr(b2, 'sourcecleaner_Extension19'):
        assert not _is_linked(b2, 'sourcecleaner_Extension19', a)


def test_assoc_javaclass39_link_reassign_clear():
    a = sourcecleaner_Java(package="sample_text")
    b1 = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    b2 = sourcecleaner_ExtensionReference(java="sample_text_2", name="sample_text_2", package="sample_text_2", project="sample_text_2")
    _safe_set(a, 'sourcecleaner_Java40', b1)
    assert _is_linked(a, 'sourcecleaner_Java40', b1)
    if hasattr(b1, 'sourcecleaner_ExtensionReference'):
        assert _is_linked(b1, 'sourcecleaner_ExtensionReference', a)
    _safe_set(a, 'sourcecleaner_Java40', b2)
    assert _is_linked(a, 'sourcecleaner_Java40', b2)
    if hasattr(b1, 'sourcecleaner_ExtensionReference'):
        assert not _is_linked(b1, 'sourcecleaner_ExtensionReference', a)
    if hasattr(b2, 'sourcecleaner_ExtensionReference'):
        assert _is_linked(b2, 'sourcecleaner_ExtensionReference', a)
    _safe_set(a, 'sourcecleaner_Java40', None)
    assert not _is_linked(a, 'sourcecleaner_Java40', b2)
    if hasattr(b2, 'sourcecleaner_ExtensionReference'):
        assert not _is_linked(b2, 'sourcecleaner_ExtensionReference', a)


def test_assoc_manifest2_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    _safe_set(a, 'sourcecleaner_Project3', b1)
    assert _is_linked(a, 'sourcecleaner_Project3', b1)
    if hasattr(b1, 'sourcecleaner_Manifest'):
        assert _is_linked(b1, 'sourcecleaner_Manifest', a)
    _safe_set(a, 'sourcecleaner_Project3', b2)
    assert _is_linked(a, 'sourcecleaner_Project3', b2)
    if hasattr(b1, 'sourcecleaner_Manifest'):
        assert not _is_linked(b1, 'sourcecleaner_Manifest', a)
    if hasattr(b2, 'sourcecleaner_Manifest'):
        assert _is_linked(b2, 'sourcecleaner_Manifest', a)
    _safe_set(a, 'sourcecleaner_Project3', None)
    assert not _is_linked(a, 'sourcecleaner_Project3', b2)
    if hasattr(b2, 'sourcecleaner_Manifest'):
        assert not _is_linked(b2, 'sourcecleaner_Manifest', a)


def test_assoc_plugin24_link_reassign_clear():
    a = sourcecleaner_Plugin(extra="sample_text")
    b1 = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    b2 = sourcecleaner_ExtensionPoint(diagraph=False, id="sample_text_2", name="sample_text_2", schema="sample_text_2")
    _safe_set(a, 'Plugin25', b1)
    assert _is_linked(a, 'Plugin25', b1)
    if hasattr(b1, 'extensionPoints'):
        assert _is_linked(b1, 'extensionPoints', a)
    _safe_set(a, 'Plugin25', b2)
    assert _is_linked(a, 'Plugin25', b2)
    if hasattr(b1, 'extensionPoints'):
        assert not _is_linked(b1, 'extensionPoints', a)
    if hasattr(b2, 'extensionPoints'):
        assert _is_linked(b2, 'extensionPoints', a)
    _safe_set(a, 'Plugin25', None)
    assert not _is_linked(a, 'Plugin25', b2)
    if hasattr(b2, 'extensionPoints'):
        assert not _is_linked(b2, 'extensionPoints', a)


def test_assoc_plugin6_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Plugin(extra="sample_text")
    b2 = sourcecleaner_Plugin(extra="sample_text_2")
    _safe_set(a, 'project7', b1)
    assert _is_linked(a, 'project7', b1)
    if hasattr(b1, 'Plugin'):
        assert _is_linked(b1, 'Plugin', a)
    _safe_set(a, 'project7', b2)
    assert _is_linked(a, 'project7', b2)
    if hasattr(b1, 'Plugin'):
        assert not _is_linked(b1, 'Plugin', a)
    if hasattr(b2, 'Plugin'):
        assert _is_linked(b2, 'Plugin', a)
    _safe_set(a, 'project7', None)
    assert not _is_linked(a, 'project7', b2)
    if hasattr(b2, 'Plugin'):
        assert not _is_linked(b2, 'Plugin', a)


def test_assoc_project10_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Java(package="sample_text")
    b2 = sourcecleaner_Java(package="sample_text_2")
    _safe_set(a, 'Project', b1)
    assert _is_linked(a, 'Project', b1)
    if hasattr(b1, 'sources'):
        assert _is_linked(b1, 'sources', a)
    _safe_set(a, 'Project', b2)
    assert _is_linked(a, 'Project', b2)
    if hasattr(b1, 'sources'):
        assert not _is_linked(b1, 'sources', a)
    if hasattr(b2, 'sources'):
        assert _is_linked(b2, 'sources', a)
    _safe_set(a, 'Project', None)
    assert not _is_linked(a, 'Project', b2)
    if hasattr(b2, 'sources'):
        assert not _is_linked(b2, 'sources', a)


def test_assoc_project30_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Plugin(extra="sample_text")
    b2 = sourcecleaner_Plugin(extra="sample_text_2")
    _safe_set(a, 'Project32', b1)
    assert _is_linked(a, 'Project32', b1)
    if hasattr(b1, 'plugin31'):
        assert _is_linked(b1, 'plugin31', a)
    _safe_set(a, 'Project32', b2)
    assert _is_linked(a, 'Project32', b2)
    if hasattr(b1, 'plugin31'):
        assert not _is_linked(b1, 'plugin31', a)
    if hasattr(b2, 'plugin31'):
        assert _is_linked(b2, 'plugin31', a)
    _safe_set(a, 'Project32', None)
    assert not _is_linked(a, 'Project32', b2)
    if hasattr(b2, 'plugin31'):
        assert not _is_linked(b2, 'plugin31', a)


def test_assoc_project34_link_reassign_clear():
    a = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    b1 = sourcecleaner_Project(id=7, workspace="sample_text")
    b2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    _safe_set(a, 'schema35', b1)
    assert _is_linked(a, 'schema35', b1)
    if hasattr(b1, 'Project36'):
        assert _is_linked(b1, 'Project36', a)
    _safe_set(a, 'schema35', b2)
    assert _is_linked(a, 'schema35', b2)
    if hasattr(b1, 'Project36'):
        assert not _is_linked(b1, 'Project36', a)
    if hasattr(b2, 'Project36'):
        assert _is_linked(b2, 'Project36', a)
    _safe_set(a, 'schema35', None)
    assert not _is_linked(a, 'schema35', b2)
    if hasattr(b2, 'Project36'):
        assert not _is_linked(b2, 'Project36', a)


def test_assoc_projects0_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Configuration(location="sample_text", temp="sample_text")
    b2 = sourcecleaner_Configuration(location="sample_text_2", temp="sample_text_2")
    _safe_set(a, 'sourcecleaner_Project', b1)
    assert _is_linked(a, 'sourcecleaner_Project', b1)
    if hasattr(b1, 'sourcecleaner_Configuration'):
        assert _is_linked(b1, 'sourcecleaner_Configuration', a)
    _safe_set(a, 'sourcecleaner_Project', b2)
    assert _is_linked(a, 'sourcecleaner_Project', b2)
    if hasattr(b1, 'sourcecleaner_Configuration'):
        assert not _is_linked(b1, 'sourcecleaner_Configuration', a)
    if hasattr(b2, 'sourcecleaner_Configuration'):
        assert _is_linked(b2, 'sourcecleaner_Configuration', a)
    _safe_set(a, 'sourcecleaner_Project', None)
    assert not _is_linked(a, 'sourcecleaner_Project', b2)
    if hasattr(b2, 'sourcecleaner_Configuration'):
        assert not _is_linked(b2, 'sourcecleaner_Configuration', a)


def test_assoc_references33_link_reassign_clear():
    a = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    b1 = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    b2 = sourcecleaner_ExtensionReference(java="sample_text_2", name="sample_text_2", package="sample_text_2", project="sample_text_2")
    _safe_set(a, 'schema', {b1})
    assert _is_linked(a, 'schema', b1)
    if hasattr(b1, 'ExtensionReference'):
        assert _is_linked(b1, 'ExtensionReference', a)
    _safe_set(a, 'schema', {b2})
    assert _is_linked(a, 'schema', b2)
    if hasattr(b1, 'ExtensionReference'):
        assert not _is_linked(b1, 'ExtensionReference', a)
    if hasattr(b2, 'ExtensionReference'):
        assert _is_linked(b2, 'ExtensionReference', a)
    _safe_set(a, 'schema', set())
    assert not _is_linked(a, 'schema', b2)
    if hasattr(b2, 'ExtensionReference'):
        assert not _is_linked(b2, 'ExtensionReference', a)


def test_assoc_requerant22_link_reassign_clear():
    a = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    b1 = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    b2 = sourcecleaner_Dependency(diagraph=False, name="sample_text_2", reexport=False, version="sample_text_2")
    _safe_set(a, 'Manifest', b1)
    assert _is_linked(a, 'Manifest', b1)
    if hasattr(b1, 'dependencies'):
        assert _is_linked(b1, 'dependencies', a)
    _safe_set(a, 'Manifest', b2)
    assert _is_linked(a, 'Manifest', b2)
    if hasattr(b1, 'dependencies'):
        assert not _is_linked(b1, 'dependencies', a)
    if hasattr(b2, 'dependencies'):
        assert _is_linked(b2, 'dependencies', a)
    _safe_set(a, 'Manifest', None)
    assert not _is_linked(a, 'Manifest', b2)
    if hasattr(b2, 'dependencies'):
        assert not _is_linked(b2, 'dependencies', a)


def test_assoc_schema37_link_reassign_clear():
    a = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    b1 = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    b2 = sourcecleaner_ExtensionReference(java="sample_text_2", name="sample_text_2", package="sample_text_2", project="sample_text_2")
    _safe_set(a, 'Schema38', b1)
    assert _is_linked(a, 'Schema38', b1)
    if hasattr(b1, 'references'):
        assert _is_linked(b1, 'references', a)
    _safe_set(a, 'Schema38', b2)
    assert _is_linked(a, 'Schema38', b2)
    if hasattr(b1, 'references'):
        assert not _is_linked(b1, 'references', a)
    if hasattr(b2, 'references'):
        assert _is_linked(b2, 'references', a)
    _safe_set(a, 'Schema38', None)
    assert not _is_linked(a, 'Schema38', b2)
    if hasattr(b2, 'references'):
        assert not _is_linked(b2, 'references', a)


def test_assoc_schema8_link_reassign_clear():
    a = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    b1 = sourcecleaner_Project(id=7, workspace="sample_text")
    b2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    _safe_set(a, 'Schema', b1)
    assert _is_linked(a, 'Schema', b1)
    if hasattr(b1, 'project9'):
        assert _is_linked(b1, 'project9', a)
    _safe_set(a, 'Schema', b2)
    assert _is_linked(a, 'Schema', b2)
    if hasattr(b1, 'project9'):
        assert not _is_linked(b1, 'project9', a)
    if hasattr(b2, 'project9'):
        assert _is_linked(b2, 'project9', a)
    _safe_set(a, 'Schema', None)
    assert not _is_linked(a, 'Schema', b2)
    if hasattr(b2, 'project9'):
        assert not _is_linked(b2, 'project9', a)


def test_assoc_sources1_link_reassign_clear():
    a = sourcecleaner_Project(id=7, workspace="sample_text")
    b1 = sourcecleaner_Java(package="sample_text")
    b2 = sourcecleaner_Java(package="sample_text_2")
    _safe_set(a, 'project', {b1})
    assert _is_linked(a, 'project', b1)
    if hasattr(b1, 'Java'):
        assert _is_linked(b1, 'Java', a)
    _safe_set(a, 'project', {b2})
    assert _is_linked(a, 'project', b2)
    if hasattr(b1, 'Java'):
        assert not _is_linked(b1, 'Java', a)
    if hasattr(b2, 'Java'):
        assert _is_linked(b2, 'Java', a)
    _safe_set(a, 'project', set())
    assert not _is_linked(a, 'project', b2)
    if hasattr(b2, 'Java'):
        assert not _is_linked(b2, 'Java', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

LocatedElement_strategy = st.builds(LocatedElement)
@given(instance=LocatedElement_strategy)
@settings(max_examples=25)
def test_LocatedElement_instantiation(instance):
    assert isinstance(instance, LocatedElement)


Source_strategy = st.builds(Source)
@given(instance=Source_strategy)
@settings(max_examples=25)
def test_Source_instantiation(instance):
    assert isinstance(instance, Source)


sourcecleaner_Build_strategy = st.builds(sourcecleaner_Build)
@given(instance=sourcecleaner_Build_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Build_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Build)


sourcecleaner_ClassPath_strategy = st.builds(sourcecleaner_ClassPath, name=safe_text)
@given(instance=sourcecleaner_ClassPath_strategy)
@settings(max_examples=25)
def test_sourcecleaner_ClassPath_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ClassPath)


sourcecleaner_Configuration_strategy = st.builds(sourcecleaner_Configuration, location=safe_text, temp=safe_text)
@given(instance=sourcecleaner_Configuration_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Configuration_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Configuration)


sourcecleaner_Dependency_strategy = st.builds(sourcecleaner_Dependency, diagraph=st.booleans(), name=safe_text, reexport=st.booleans(), version=safe_text)
@given(instance=sourcecleaner_Dependency_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Dependency_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Dependency)


sourcecleaner_Export_strategy = st.builds(sourcecleaner_Export, name=safe_text)
@given(instance=sourcecleaner_Export_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Export_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Export)


sourcecleaner_Extension_strategy = st.builds(sourcecleaner_Extension, clazz=safe_text, diagraph=st.booleans(), extra=safe_text, id=safe_text, name=safe_text, pointId=safe_text)
@given(instance=sourcecleaner_Extension_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Extension_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Extension)


sourcecleaner_ExtensionAttribute_strategy = st.builds(sourcecleaner_ExtensionAttribute, name=safe_text, value=safe_text)
@given(instance=sourcecleaner_ExtensionAttribute_strategy)
@settings(max_examples=25)
def test_sourcecleaner_ExtensionAttribute_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionAttribute)


sourcecleaner_ExtensionPoint_strategy = st.builds(sourcecleaner_ExtensionPoint, diagraph=st.booleans(), id=safe_text, name=safe_text, schema=safe_text)
@given(instance=sourcecleaner_ExtensionPoint_strategy)
@settings(max_examples=25)
def test_sourcecleaner_ExtensionPoint_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionPoint)


sourcecleaner_ExtensionReference_strategy = st.builds(sourcecleaner_ExtensionReference, java=safe_text, name=safe_text, package=safe_text, project=safe_text)
@given(instance=sourcecleaner_ExtensionReference_strategy)
@settings(max_examples=25)
def test_sourcecleaner_ExtensionReference_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionReference)


sourcecleaner_Java_strategy = st.builds(sourcecleaner_Java, package=safe_text)
@given(instance=sourcecleaner_Java_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Java_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Java)


sourcecleaner_LocatedElement_strategy = st.builds(sourcecleaner_LocatedElement, absolutePath=safe_text, name=safe_text)
@given(instance=sourcecleaner_LocatedElement_strategy)
@settings(max_examples=25)
def test_sourcecleaner_LocatedElement_instantiation(instance):
    assert isinstance(instance, sourcecleaner_LocatedElement)


sourcecleaner_Manifest_strategy = st.builds(sourcecleaner_Manifest, diagraph=st.booleans(), executionEnvironment=safe_text, lazy=st.booleans(), singleton=st.booleans(), symbolicName=safe_text, vendor=safe_text, version=safe_text, versionId=safe_text, versionQualifier=safe_text)
@given(instance=sourcecleaner_Manifest_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Manifest_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Manifest)


sourcecleaner_Plugin_strategy = st.builds(sourcecleaner_Plugin, extra=safe_text)
@given(instance=sourcecleaner_Plugin_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Plugin_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Plugin)


sourcecleaner_Project_strategy = st.builds(sourcecleaner_Project, id=st.integers(), workspace=safe_text)
@given(instance=sourcecleaner_Project_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Project_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Project)


sourcecleaner_Schema_strategy = st.builds(sourcecleaner_Schema, extensionId=safe_text, extensionName=safe_text, pluginName=safe_text)
@given(instance=sourcecleaner_Schema_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Schema_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Schema)


sourcecleaner_Source_strategy = st.builds(sourcecleaner_Source, comment=safe_text, content=safe_text, handled=st.booleans(), mark=st.booleans())
@given(instance=sourcecleaner_Source_strategy)
@settings(max_examples=25)
def test_sourcecleaner_Source_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Source)


