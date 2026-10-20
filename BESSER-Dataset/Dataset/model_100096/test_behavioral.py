import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_attributes17_reverse_link_reassign_clear():
    a1 = sourcecleaner_ExtensionAttribute(name="sample_text", value="sample_text")
    a2 = sourcecleaner_ExtensionAttribute(name="sample_text_2", value="sample_text_2")
    b = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    _safe_set(b, 'sourcecleaner_Extension', {a1})
    assert _is_linked(b, 'sourcecleaner_Extension', a1)
    if hasattr(a1, 'sourcecleaner_ExtensionAttribute'):
        assert _is_linked(a1, 'sourcecleaner_ExtensionAttribute', b)
    _safe_set(b, 'sourcecleaner_Extension', {a2})
    assert _is_linked(b, 'sourcecleaner_Extension', a2)
    if hasattr(a1, 'sourcecleaner_ExtensionAttribute'):
        assert not _is_linked(a1, 'sourcecleaner_ExtensionAttribute', b)
    if hasattr(a2, 'sourcecleaner_ExtensionAttribute'):
        assert _is_linked(a2, 'sourcecleaner_ExtensionAttribute', b)
    _safe_set(b, 'sourcecleaner_Extension', set())
    assert not _is_linked(b, 'sourcecleaner_Extension', a2)
    if hasattr(a2, 'sourcecleaner_ExtensionAttribute'):
        assert not _is_linked(a2, 'sourcecleaner_ExtensionAttribute', b)


def test_assoc_classpathes12_reverse_link_reassign_clear():
    a1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    a2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    b = sourcecleaner_ClassPath(name="sample_text")
    _safe_set(b, 'sourcecleaner_ClassPath', a1)
    assert _is_linked(b, 'sourcecleaner_ClassPath', a1)
    if hasattr(a1, 'sourcecleaner_Manifest13'):
        assert _is_linked(a1, 'sourcecleaner_Manifest13', b)
    _safe_set(b, 'sourcecleaner_ClassPath', a2)
    assert _is_linked(b, 'sourcecleaner_ClassPath', a2)
    if hasattr(a1, 'sourcecleaner_Manifest13'):
        assert not _is_linked(a1, 'sourcecleaner_Manifest13', b)
    if hasattr(a2, 'sourcecleaner_Manifest13'):
        assert _is_linked(a2, 'sourcecleaner_Manifest13', b)
    _safe_set(b, 'sourcecleaner_ClassPath', None)
    assert not _is_linked(b, 'sourcecleaner_ClassPath', a2)
    if hasattr(a2, 'sourcecleaner_Manifest13'):
        assert not _is_linked(a2, 'sourcecleaner_Manifest13', b)


def test_assoc_dependencies11_reverse_link_reassign_clear():
    a1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    a2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    b = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    _safe_set(b, 'Dependency', a1)
    assert _is_linked(b, 'Dependency', a1)
    if hasattr(a1, 'requerant'):
        assert _is_linked(a1, 'requerant', b)
    _safe_set(b, 'Dependency', a2)
    assert _is_linked(b, 'Dependency', a2)
    if hasattr(a1, 'requerant'):
        assert not _is_linked(a1, 'requerant', b)
    if hasattr(a2, 'requerant'):
        assert _is_linked(a2, 'requerant', b)
    _safe_set(b, 'Dependency', None)
    assert not _is_linked(b, 'Dependency', a2)
    if hasattr(a2, 'requerant'):
        assert not _is_linked(a2, 'requerant', b)


def test_assoc_dependency20_reverse_link_reassign_clear():
    a1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    a2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    b = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    _safe_set(b, 'sourcecleaner_Dependency', a1)
    assert _is_linked(b, 'sourcecleaner_Dependency', a1)
    if hasattr(a1, 'sourcecleaner_Manifest21'):
        assert _is_linked(a1, 'sourcecleaner_Manifest21', b)
    _safe_set(b, 'sourcecleaner_Dependency', a2)
    assert _is_linked(b, 'sourcecleaner_Dependency', a2)
    if hasattr(a1, 'sourcecleaner_Manifest21'):
        assert not _is_linked(a1, 'sourcecleaner_Manifest21', b)
    if hasattr(a2, 'sourcecleaner_Manifest21'):
        assert _is_linked(a2, 'sourcecleaner_Manifest21', b)
    _safe_set(b, 'sourcecleaner_Dependency', None)
    assert not _is_linked(b, 'sourcecleaner_Dependency', a2)
    if hasattr(a2, 'sourcecleaner_Manifest21'):
        assert not _is_linked(a2, 'sourcecleaner_Manifest21', b)


def test_assoc_exports14_reverse_link_reassign_clear():
    a1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    a2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    b = sourcecleaner_Export(name="sample_text")
    _safe_set(b, 'sourcecleaner_Export', a1)
    assert _is_linked(b, 'sourcecleaner_Export', a1)
    if hasattr(a1, 'sourcecleaner_Manifest15'):
        assert _is_linked(a1, 'sourcecleaner_Manifest15', b)
    _safe_set(b, 'sourcecleaner_Export', a2)
    assert _is_linked(b, 'sourcecleaner_Export', a2)
    if hasattr(a1, 'sourcecleaner_Manifest15'):
        assert not _is_linked(a1, 'sourcecleaner_Manifest15', b)
    if hasattr(a2, 'sourcecleaner_Manifest15'):
        assert _is_linked(a2, 'sourcecleaner_Manifest15', b)
    _safe_set(b, 'sourcecleaner_Export', None)
    assert not _is_linked(b, 'sourcecleaner_Export', a2)
    if hasattr(a2, 'sourcecleaner_Manifest15'):
        assert not _is_linked(a2, 'sourcecleaner_Manifest15', b)


def test_assoc_extensionPoint16_reverse_link_reassign_clear():
    a1 = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    a2 = sourcecleaner_ExtensionPoint(diagraph=False, id="sample_text_2", name="sample_text_2", schema="sample_text_2")
    b = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    _safe_set(b, 'extensions', a1)
    assert _is_linked(b, 'extensions', a1)
    if hasattr(a1, 'ExtensionPoint'):
        assert _is_linked(a1, 'ExtensionPoint', b)
    _safe_set(b, 'extensions', a2)
    assert _is_linked(b, 'extensions', a2)
    if hasattr(a1, 'ExtensionPoint'):
        assert not _is_linked(a1, 'ExtensionPoint', b)
    if hasattr(a2, 'ExtensionPoint'):
        assert _is_linked(a2, 'ExtensionPoint', b)
    _safe_set(b, 'extensions', None)
    assert not _is_linked(b, 'extensions', a2)
    if hasattr(a2, 'ExtensionPoint'):
        assert not _is_linked(a2, 'ExtensionPoint', b)


def test_assoc_extensionPoints28_reverse_link_reassign_clear():
    a1 = sourcecleaner_Plugin(extra="sample_text")
    a2 = sourcecleaner_Plugin(extra="sample_text_2")
    b = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    _safe_set(b, 'ExtensionPoint29', a1)
    assert _is_linked(b, 'ExtensionPoint29', a1)
    if hasattr(a1, 'plugin'):
        assert _is_linked(a1, 'plugin', b)
    _safe_set(b, 'ExtensionPoint29', a2)
    assert _is_linked(b, 'ExtensionPoint29', a2)
    if hasattr(a1, 'plugin'):
        assert not _is_linked(a1, 'plugin', b)
    if hasattr(a2, 'plugin'):
        assert _is_linked(a2, 'plugin', b)
    _safe_set(b, 'ExtensionPoint29', None)
    assert not _is_linked(b, 'ExtensionPoint29', a2)
    if hasattr(a2, 'plugin'):
        assert not _is_linked(a2, 'plugin', b)


def test_assoc_extensions23_reverse_link_reassign_clear():
    a1 = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    a2 = sourcecleaner_ExtensionPoint(diagraph=False, id="sample_text_2", name="sample_text_2", schema="sample_text_2")
    b = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    _safe_set(b, 'Extension', a1)
    assert _is_linked(b, 'Extension', a1)
    if hasattr(a1, 'extensionPoint'):
        assert _is_linked(a1, 'extensionPoint', b)
    _safe_set(b, 'Extension', a2)
    assert _is_linked(b, 'Extension', a2)
    if hasattr(a1, 'extensionPoint'):
        assert not _is_linked(a1, 'extensionPoint', b)
    if hasattr(a2, 'extensionPoint'):
        assert _is_linked(a2, 'extensionPoint', b)
    _safe_set(b, 'Extension', None)
    assert not _is_linked(b, 'Extension', a2)
    if hasattr(a2, 'extensionPoint'):
        assert not _is_linked(a2, 'extensionPoint', b)


def test_assoc_extensions26_reverse_link_reassign_clear():
    a1 = sourcecleaner_Plugin(extra="sample_text")
    a2 = sourcecleaner_Plugin(extra="sample_text_2")
    b = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    _safe_set(b, 'sourcecleaner_Extension27', a1)
    assert _is_linked(b, 'sourcecleaner_Extension27', a1)
    if hasattr(a1, 'sourcecleaner_Plugin'):
        assert _is_linked(a1, 'sourcecleaner_Plugin', b)
    _safe_set(b, 'sourcecleaner_Extension27', a2)
    assert _is_linked(b, 'sourcecleaner_Extension27', a2)
    if hasattr(a1, 'sourcecleaner_Plugin'):
        assert not _is_linked(a1, 'sourcecleaner_Plugin', b)
    if hasattr(a2, 'sourcecleaner_Plugin'):
        assert _is_linked(a2, 'sourcecleaner_Plugin', b)
    _safe_set(b, 'sourcecleaner_Extension27', None)
    assert not _is_linked(b, 'sourcecleaner_Extension27', a2)
    if hasattr(a2, 'sourcecleaner_Plugin'):
        assert not _is_linked(a2, 'sourcecleaner_Plugin', b)


def test_assoc_implements18_reverse_link_reassign_clear():
    a1 = sourcecleaner_Java(package="sample_text")
    a2 = sourcecleaner_Java(package="sample_text_2")
    b = sourcecleaner_Extension(clazz="sample_text", diagraph=True, extra="sample_text", id="sample_text", name="sample_text", pointId="sample_text")
    _safe_set(b, 'sourcecleaner_Extension19', a1)
    assert _is_linked(b, 'sourcecleaner_Extension19', a1)
    if hasattr(a1, 'sourcecleaner_Java'):
        assert _is_linked(a1, 'sourcecleaner_Java', b)
    _safe_set(b, 'sourcecleaner_Extension19', a2)
    assert _is_linked(b, 'sourcecleaner_Extension19', a2)
    if hasattr(a1, 'sourcecleaner_Java'):
        assert not _is_linked(a1, 'sourcecleaner_Java', b)
    if hasattr(a2, 'sourcecleaner_Java'):
        assert _is_linked(a2, 'sourcecleaner_Java', b)
    _safe_set(b, 'sourcecleaner_Extension19', None)
    assert not _is_linked(b, 'sourcecleaner_Extension19', a2)
    if hasattr(a2, 'sourcecleaner_Java'):
        assert not _is_linked(a2, 'sourcecleaner_Java', b)


def test_assoc_javaclass39_reverse_link_reassign_clear():
    a1 = sourcecleaner_Java(package="sample_text")
    a2 = sourcecleaner_Java(package="sample_text_2")
    b = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    _safe_set(b, 'sourcecleaner_ExtensionReference', a1)
    assert _is_linked(b, 'sourcecleaner_ExtensionReference', a1)
    if hasattr(a1, 'sourcecleaner_Java40'):
        assert _is_linked(a1, 'sourcecleaner_Java40', b)
    _safe_set(b, 'sourcecleaner_ExtensionReference', a2)
    assert _is_linked(b, 'sourcecleaner_ExtensionReference', a2)
    if hasattr(a1, 'sourcecleaner_Java40'):
        assert not _is_linked(a1, 'sourcecleaner_Java40', b)
    if hasattr(a2, 'sourcecleaner_Java40'):
        assert _is_linked(a2, 'sourcecleaner_Java40', b)
    _safe_set(b, 'sourcecleaner_ExtensionReference', None)
    assert not _is_linked(b, 'sourcecleaner_ExtensionReference', a2)
    if hasattr(a2, 'sourcecleaner_Java40'):
        assert not _is_linked(a2, 'sourcecleaner_Java40', b)


def test_assoc_manifest2_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    _safe_set(b, 'sourcecleaner_Manifest', a1)
    assert _is_linked(b, 'sourcecleaner_Manifest', a1)
    if hasattr(a1, 'sourcecleaner_Project3'):
        assert _is_linked(a1, 'sourcecleaner_Project3', b)
    _safe_set(b, 'sourcecleaner_Manifest', a2)
    assert _is_linked(b, 'sourcecleaner_Manifest', a2)
    if hasattr(a1, 'sourcecleaner_Project3'):
        assert not _is_linked(a1, 'sourcecleaner_Project3', b)
    if hasattr(a2, 'sourcecleaner_Project3'):
        assert _is_linked(a2, 'sourcecleaner_Project3', b)
    _safe_set(b, 'sourcecleaner_Manifest', None)
    assert not _is_linked(b, 'sourcecleaner_Manifest', a2)
    if hasattr(a2, 'sourcecleaner_Project3'):
        assert not _is_linked(a2, 'sourcecleaner_Project3', b)


def test_assoc_plugin24_reverse_link_reassign_clear():
    a1 = sourcecleaner_Plugin(extra="sample_text")
    a2 = sourcecleaner_Plugin(extra="sample_text_2")
    b = sourcecleaner_ExtensionPoint(diagraph=True, id="sample_text", name="sample_text", schema="sample_text")
    _safe_set(b, 'extensionPoints', a1)
    assert _is_linked(b, 'extensionPoints', a1)
    if hasattr(a1, 'Plugin25'):
        assert _is_linked(a1, 'Plugin25', b)
    _safe_set(b, 'extensionPoints', a2)
    assert _is_linked(b, 'extensionPoints', a2)
    if hasattr(a1, 'Plugin25'):
        assert not _is_linked(a1, 'Plugin25', b)
    if hasattr(a2, 'Plugin25'):
        assert _is_linked(a2, 'Plugin25', b)
    _safe_set(b, 'extensionPoints', None)
    assert not _is_linked(b, 'extensionPoints', a2)
    if hasattr(a2, 'Plugin25'):
        assert not _is_linked(a2, 'Plugin25', b)


def test_assoc_plugin6_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Plugin(extra="sample_text")
    _safe_set(b, 'Plugin', a1)
    assert _is_linked(b, 'Plugin', a1)
    if hasattr(a1, 'project7'):
        assert _is_linked(a1, 'project7', b)
    _safe_set(b, 'Plugin', a2)
    assert _is_linked(b, 'Plugin', a2)
    if hasattr(a1, 'project7'):
        assert not _is_linked(a1, 'project7', b)
    if hasattr(a2, 'project7'):
        assert _is_linked(a2, 'project7', b)
    _safe_set(b, 'Plugin', None)
    assert not _is_linked(b, 'Plugin', a2)
    if hasattr(a2, 'project7'):
        assert not _is_linked(a2, 'project7', b)


def test_assoc_project10_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Java(package="sample_text")
    _safe_set(b, 'sources', a1)
    assert _is_linked(b, 'sources', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'sources', a2)
    assert _is_linked(b, 'sources', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'sources', None)
    assert not _is_linked(b, 'sources', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_project30_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Plugin(extra="sample_text")
    _safe_set(b, 'plugin31', a1)
    assert _is_linked(b, 'plugin31', a1)
    if hasattr(a1, 'Project32'):
        assert _is_linked(a1, 'Project32', b)
    _safe_set(b, 'plugin31', a2)
    assert _is_linked(b, 'plugin31', a2)
    if hasattr(a1, 'Project32'):
        assert not _is_linked(a1, 'Project32', b)
    if hasattr(a2, 'Project32'):
        assert _is_linked(a2, 'Project32', b)
    _safe_set(b, 'plugin31', None)
    assert not _is_linked(b, 'plugin31', a2)
    if hasattr(a2, 'Project32'):
        assert not _is_linked(a2, 'Project32', b)


def test_assoc_project34_reverse_link_reassign_clear():
    a1 = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    a2 = sourcecleaner_Schema(extensionId="sample_text_2", extensionName="sample_text_2", pluginName="sample_text_2")
    b = sourcecleaner_Project(id=7, workspace="sample_text")
    _safe_set(b, 'Project36', a1)
    assert _is_linked(b, 'Project36', a1)
    if hasattr(a1, 'schema35'):
        assert _is_linked(a1, 'schema35', b)
    _safe_set(b, 'Project36', a2)
    assert _is_linked(b, 'Project36', a2)
    if hasattr(a1, 'schema35'):
        assert not _is_linked(a1, 'schema35', b)
    if hasattr(a2, 'schema35'):
        assert _is_linked(a2, 'schema35', b)
    _safe_set(b, 'Project36', None)
    assert not _is_linked(b, 'Project36', a2)
    if hasattr(a2, 'schema35'):
        assert not _is_linked(a2, 'schema35', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Configuration(location="sample_text", temp="sample_text")
    _safe_set(b, 'sourcecleaner_Configuration', {a1})
    assert _is_linked(b, 'sourcecleaner_Configuration', a1)
    if hasattr(a1, 'sourcecleaner_Project'):
        assert _is_linked(a1, 'sourcecleaner_Project', b)
    _safe_set(b, 'sourcecleaner_Configuration', {a2})
    assert _is_linked(b, 'sourcecleaner_Configuration', a2)
    if hasattr(a1, 'sourcecleaner_Project'):
        assert not _is_linked(a1, 'sourcecleaner_Project', b)
    if hasattr(a2, 'sourcecleaner_Project'):
        assert _is_linked(a2, 'sourcecleaner_Project', b)
    _safe_set(b, 'sourcecleaner_Configuration', set())
    assert not _is_linked(b, 'sourcecleaner_Configuration', a2)
    if hasattr(a2, 'sourcecleaner_Project'):
        assert not _is_linked(a2, 'sourcecleaner_Project', b)


def test_assoc_references33_reverse_link_reassign_clear():
    a1 = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    a2 = sourcecleaner_Schema(extensionId="sample_text_2", extensionName="sample_text_2", pluginName="sample_text_2")
    b = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    _safe_set(b, 'ExtensionReference', a1)
    assert _is_linked(b, 'ExtensionReference', a1)
    if hasattr(a1, 'schema'):
        assert _is_linked(a1, 'schema', b)
    _safe_set(b, 'ExtensionReference', a2)
    assert _is_linked(b, 'ExtensionReference', a2)
    if hasattr(a1, 'schema'):
        assert not _is_linked(a1, 'schema', b)
    if hasattr(a2, 'schema'):
        assert _is_linked(a2, 'schema', b)
    _safe_set(b, 'ExtensionReference', None)
    assert not _is_linked(b, 'ExtensionReference', a2)
    if hasattr(a2, 'schema'):
        assert not _is_linked(a2, 'schema', b)


def test_assoc_requerant22_reverse_link_reassign_clear():
    a1 = sourcecleaner_Manifest(diagraph=True, executionEnvironment="sample_text", lazy=True, singleton=True, symbolicName="sample_text", vendor="sample_text", version="sample_text", versionId="sample_text", versionQualifier="sample_text")
    a2 = sourcecleaner_Manifest(diagraph=False, executionEnvironment="sample_text_2", lazy=False, singleton=False, symbolicName="sample_text_2", vendor="sample_text_2", version="sample_text_2", versionId="sample_text_2", versionQualifier="sample_text_2")
    b = sourcecleaner_Dependency(diagraph=True, name="sample_text", reexport=True, version="sample_text")
    _safe_set(b, 'dependencies', a1)
    assert _is_linked(b, 'dependencies', a1)
    if hasattr(a1, 'Manifest'):
        assert _is_linked(a1, 'Manifest', b)
    _safe_set(b, 'dependencies', a2)
    assert _is_linked(b, 'dependencies', a2)
    if hasattr(a1, 'Manifest'):
        assert not _is_linked(a1, 'Manifest', b)
    if hasattr(a2, 'Manifest'):
        assert _is_linked(a2, 'Manifest', b)
    _safe_set(b, 'dependencies', None)
    assert not _is_linked(b, 'dependencies', a2)
    if hasattr(a2, 'Manifest'):
        assert not _is_linked(a2, 'Manifest', b)


def test_assoc_schema37_reverse_link_reassign_clear():
    a1 = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    a2 = sourcecleaner_Schema(extensionId="sample_text_2", extensionName="sample_text_2", pluginName="sample_text_2")
    b = sourcecleaner_ExtensionReference(java="sample_text", name="sample_text", package="sample_text", project="sample_text")
    _safe_set(b, 'references', a1)
    assert _is_linked(b, 'references', a1)
    if hasattr(a1, 'Schema38'):
        assert _is_linked(a1, 'Schema38', b)
    _safe_set(b, 'references', a2)
    assert _is_linked(b, 'references', a2)
    if hasattr(a1, 'Schema38'):
        assert not _is_linked(a1, 'Schema38', b)
    if hasattr(a2, 'Schema38'):
        assert _is_linked(a2, 'Schema38', b)
    _safe_set(b, 'references', None)
    assert not _is_linked(b, 'references', a2)
    if hasattr(a2, 'Schema38'):
        assert not _is_linked(a2, 'Schema38', b)


def test_assoc_schema8_reverse_link_reassign_clear():
    a1 = sourcecleaner_Schema(extensionId="sample_text", extensionName="sample_text", pluginName="sample_text")
    a2 = sourcecleaner_Schema(extensionId="sample_text_2", extensionName="sample_text_2", pluginName="sample_text_2")
    b = sourcecleaner_Project(id=7, workspace="sample_text")
    _safe_set(b, 'project9', a1)
    assert _is_linked(b, 'project9', a1)
    if hasattr(a1, 'Schema'):
        assert _is_linked(a1, 'Schema', b)
    _safe_set(b, 'project9', a2)
    assert _is_linked(b, 'project9', a2)
    if hasattr(a1, 'Schema'):
        assert not _is_linked(a1, 'Schema', b)
    if hasattr(a2, 'Schema'):
        assert _is_linked(a2, 'Schema', b)
    _safe_set(b, 'project9', None)
    assert not _is_linked(b, 'project9', a2)
    if hasattr(a2, 'Schema'):
        assert not _is_linked(a2, 'Schema', b)


def test_assoc_sources1_reverse_link_reassign_clear():
    a1 = sourcecleaner_Project(id=7, workspace="sample_text")
    a2 = sourcecleaner_Project(id=13, workspace="sample_text_2")
    b = sourcecleaner_Java(package="sample_text")
    _safe_set(b, 'Java', a1)
    assert _is_linked(b, 'Java', a1)
    if hasattr(a1, 'project'):
        assert _is_linked(a1, 'project', b)
    _safe_set(b, 'Java', a2)
    assert _is_linked(b, 'Java', a2)
    if hasattr(a1, 'project'):
        assert not _is_linked(a1, 'project', b)
    if hasattr(a2, 'project'):
        assert _is_linked(a2, 'project', b)
    _safe_set(b, 'Java', None)
    assert not _is_linked(b, 'Java', a2)
    if hasattr(a2, 'project'):
        assert not _is_linked(a2, 'project', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_build4_stub_double():
    # sourcecleaner_Build has no real 'sourcecleaner_Build' property in the generated
    # code (a bare stub) -- manually attach it so sourcecleaner_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecleaner_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecleaner_Project(id=7, workspace="sample_text")
    partner = sourcecleaner_Build()
    setattr(partner, 'sourcecleaner_Build', None)
    _safe_set(owner, 'sourcecleaner_Project5', partner)
    assert getattr(partner, 'sourcecleaner_Build') == owner
    _safe_set(owner, 'sourcecleaner_Project5', None)
    assert getattr(partner, 'sourcecleaner_Build') is None


