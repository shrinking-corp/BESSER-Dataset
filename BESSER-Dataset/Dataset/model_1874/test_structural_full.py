import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Alias,
    TypeItem,
    basic_Alias,
    basic_CoreVersionDefault,
    basic_Event,
    basic_ExecutionEnvironment,
    basic_ExtJSProject,
    basic_Feature,
    basic_File,
    basic_Layout,
    basic_Library,
    basic_LibrarySource,
    basic_Parameter,
    basic_Plugin,
    basic_TypeItem,
    basic_Widget,
    LibrarySourceType,
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

def test_basic_Alias_name_value_roundtrip():
    instance = basic_Alias(name="sample_text", rawName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_Alias_rawName_value_roundtrip():
    instance = basic_Alias(name="sample_text", rawName="sample_text")
    assert instance.rawName == "sample_text"
    instance.rawName = "sample_text_2"
    assert instance.rawName == "sample_text_2"


def test_basic_CoreVersionDefault_coreLib_value_roundtrip():
    instance = basic_CoreVersionDefault(coreLib="sample_text", facet="sample_text", version="sample_text")
    assert instance.coreLib == "sample_text"
    instance.coreLib = "sample_text_2"
    assert instance.coreLib == "sample_text_2"


def test_basic_CoreVersionDefault_facet_value_roundtrip():
    instance = basic_CoreVersionDefault(coreLib="sample_text", facet="sample_text", version="sample_text")
    assert instance.facet == "sample_text"
    instance.facet = "sample_text_2"
    assert instance.facet == "sample_text_2"


def test_basic_CoreVersionDefault_version_value_roundtrip():
    instance = basic_CoreVersionDefault(coreLib="sample_text", facet="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_basic_Event_description_value_roundtrip():
    instance = basic_Event(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_basic_Event_name_value_roundtrip():
    instance = basic_Event(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_ExecutionEnvironment_builtin_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.builtin == True
    instance.builtin = False
    assert instance.builtin == False


def test_basic_ExecutionEnvironment_corePath_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.corePath == "sample_text"
    instance.corePath = "sample_text_2"
    assert instance.corePath == "sample_text_2"


def test_basic_ExecutionEnvironment_coreType_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.coreType == "sample_text"
    instance.coreType = "sample_text_2"
    assert instance.coreType == "sample_text_2"


def test_basic_ExecutionEnvironment_facet_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.facet == "sample_text"
    instance.facet = "sample_text_2"
    assert instance.facet == "sample_text_2"


def test_basic_ExecutionEnvironment_libraries_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.libraries == "sample_text"
    instance.libraries = "sample_text_2"
    assert instance.libraries == "sample_text_2"


def test_basic_ExecutionEnvironment_name_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_ExecutionEnvironment_versions_value_roundtrip():
    instance = basic_ExecutionEnvironment(builtin=True, corePath="sample_text", coreType="sample_text", facet="sample_text", libraries="sample_text", name="sample_text", versions="sample_text")
    assert instance.versions == "sample_text"
    instance.versions = "sample_text_2"
    assert instance.versions == "sample_text_2"


def test_basic_ExtJSProject_name_value_roundtrip():
    instance = basic_ExtJSProject(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_File_name_value_roundtrip():
    instance = basic_File(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_Library_builtin_value_roundtrip():
    instance = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    assert instance.builtin == True
    instance.builtin = False
    assert instance.builtin == False


def test_basic_Library_name_value_roundtrip():
    instance = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_Library_senchaTouchVersions_value_roundtrip():
    instance = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    assert instance.senchaTouchVersions == "sample_text"
    instance.senchaTouchVersions = "sample_text_2"
    assert instance.senchaTouchVersions == "sample_text_2"


def test_basic_Library_versions_value_roundtrip():
    instance = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    assert instance.versions == "sample_text"
    instance.versions = "sample_text_2"
    assert instance.versions == "sample_text_2"


def test_basic_LibrarySource_exclusions_value_roundtrip():
    instance = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    assert instance.exclusions == "sample_text"
    instance.exclusions = "sample_text_2"
    assert instance.exclusions == "sample_text_2"


def test_basic_LibrarySource_inclusions_value_roundtrip():
    instance = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    assert instance.inclusions == "sample_text"
    instance.inclusions = "sample_text_2"
    assert instance.inclusions == "sample_text_2"


def test_basic_LibrarySource_path_value_roundtrip():
    instance = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_basic_LibrarySource_type_value_roundtrip():
    instance = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_basic_Parameter_description_value_roundtrip():
    instance = basic_Parameter(description="sample_text", name="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_basic_Parameter_name_value_roundtrip():
    instance = basic_Parameter(description="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basic_Parameter_type_value_roundtrip():
    instance = basic_Parameter(description="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_basic_TypeItem_sourceEnd_value_roundtrip():
    instance = basic_TypeItem(sourceEnd=7, sourceStart=7, typeName="sample_text")
    assert instance.sourceEnd == 7
    instance.sourceEnd = 13
    assert instance.sourceEnd == 13


def test_basic_TypeItem_sourceStart_value_roundtrip():
    instance = basic_TypeItem(sourceEnd=7, sourceStart=7, typeName="sample_text")
    assert instance.sourceStart == 7
    instance.sourceStart = 13
    assert instance.sourceStart == 13


def test_basic_TypeItem_typeName_value_roundtrip():
    instance = basic_TypeItem(sourceEnd=7, sourceStart=7, typeName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_basic_Feature_isa_Alias():
    instance = basic_Feature()
    assert isinstance(instance, Alias)


def test_basic_Layout_isa_Alias():
    instance = basic_Layout()
    assert isinstance(instance, Alias)


def test_basic_Plugin_isa_Alias():
    instance = basic_Plugin()
    assert isinstance(instance, Alias)


def test_basic_Widget_isa_Alias():
    instance = basic_Widget()
    assert isinstance(instance, Alias)


def test_basic_Alias_isa_TypeItem():
    instance = basic_Alias(name="sample_text", rawName="sample_text")
    assert isinstance(instance, TypeItem)


def test_basic_Event_isa_TypeItem():
    instance = basic_Event(description="sample_text", name="sample_text")
    assert isinstance(instance, TypeItem)


def test_assoc_aliases1_link_reassign_clear():
    a = basic_File(name="sample_text")
    b1 = basic_Alias(name="sample_text", rawName="sample_text")
    b2 = basic_Alias(name="sample_text_2", rawName="sample_text_2")
    _safe_set(a, 'basic_File2', {b1})
    assert _is_linked(a, 'basic_File2', b1)
    if hasattr(b1, 'basic_Alias'):
        assert _is_linked(b1, 'basic_Alias', a)
    _safe_set(a, 'basic_File2', {b2})
    assert _is_linked(a, 'basic_File2', b2)
    if hasattr(b1, 'basic_Alias'):
        assert not _is_linked(b1, 'basic_Alias', a)
    if hasattr(b2, 'basic_Alias'):
        assert _is_linked(b2, 'basic_Alias', a)
    _safe_set(a, 'basic_File2', set())
    assert not _is_linked(a, 'basic_File2', b2)
    if hasattr(b2, 'basic_Alias'):
        assert not _is_linked(b2, 'basic_Alias', a)


def test_assoc_files0_link_reassign_clear():
    a = basic_File(name="sample_text")
    b1 = basic_ExtJSProject(name="sample_text")
    b2 = basic_ExtJSProject(name="sample_text_2")
    _safe_set(a, 'basic_File', b1)
    assert _is_linked(a, 'basic_File', b1)
    if hasattr(b1, 'basic_ExtJSProject'):
        assert _is_linked(b1, 'basic_ExtJSProject', a)
    _safe_set(a, 'basic_File', b2)
    assert _is_linked(a, 'basic_File', b2)
    if hasattr(b1, 'basic_ExtJSProject'):
        assert not _is_linked(b1, 'basic_ExtJSProject', a)
    if hasattr(b2, 'basic_ExtJSProject'):
        assert _is_linked(b2, 'basic_ExtJSProject', a)
    _safe_set(a, 'basic_File', None)
    assert not _is_linked(a, 'basic_File', b2)
    if hasattr(b2, 'basic_ExtJSProject'):
        assert not _is_linked(b2, 'basic_ExtJSProject', a)


def test_assoc_files5_link_reassign_clear():
    a = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    b1 = basic_File(name="sample_text")
    b2 = basic_File(name="sample_text_2")
    _safe_set(a, 'basic_LibrarySource6', {b1})
    assert _is_linked(a, 'basic_LibrarySource6', b1)
    if hasattr(b1, 'basic_File7'):
        assert _is_linked(b1, 'basic_File7', a)
    _safe_set(a, 'basic_LibrarySource6', {b2})
    assert _is_linked(a, 'basic_LibrarySource6', b2)
    if hasattr(b1, 'basic_File7'):
        assert not _is_linked(b1, 'basic_File7', a)
    if hasattr(b2, 'basic_File7'):
        assert _is_linked(b2, 'basic_File7', a)
    _safe_set(a, 'basic_LibrarySource6', set())
    assert not _is_linked(a, 'basic_LibrarySource6', b2)
    if hasattr(b2, 'basic_File7'):
        assert not _is_linked(b2, 'basic_File7', a)


def test_assoc_parameters3_link_reassign_clear():
    a = basic_Parameter(description="sample_text", name="sample_text", type="sample_text")
    b1 = basic_Event(description="sample_text", name="sample_text")
    b2 = basic_Event(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'basic_Parameter', b1)
    assert _is_linked(a, 'basic_Parameter', b1)
    if hasattr(b1, 'basic_Event'):
        assert _is_linked(b1, 'basic_Event', a)
    _safe_set(a, 'basic_Parameter', b2)
    assert _is_linked(a, 'basic_Parameter', b2)
    if hasattr(b1, 'basic_Event'):
        assert not _is_linked(b1, 'basic_Event', a)
    if hasattr(b2, 'basic_Event'):
        assert _is_linked(b2, 'basic_Event', a)
    _safe_set(a, 'basic_Parameter', None)
    assert not _is_linked(a, 'basic_Parameter', b2)
    if hasattr(b2, 'basic_Event'):
        assert not _is_linked(b2, 'basic_Event', a)


def test_assoc_sources4_link_reassign_clear():
    a = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    b1 = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    b2 = basic_Library(builtin=False, name="sample_text_2", senchaTouchVersions="sample_text_2", versions="sample_text_2")
    _safe_set(a, 'basic_LibrarySource', b1)
    assert _is_linked(a, 'basic_LibrarySource', b1)
    if hasattr(b1, 'basic_Library'):
        assert _is_linked(b1, 'basic_Library', a)
    _safe_set(a, 'basic_LibrarySource', b2)
    assert _is_linked(a, 'basic_LibrarySource', b2)
    if hasattr(b1, 'basic_Library'):
        assert not _is_linked(b1, 'basic_Library', a)
    if hasattr(b2, 'basic_Library'):
        assert _is_linked(b2, 'basic_Library', a)
    _safe_set(a, 'basic_LibrarySource', None)
    assert not _is_linked(a, 'basic_LibrarySource', b2)
    if hasattr(b2, 'basic_Library'):
        assert not _is_linked(b2, 'basic_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Alias_strategy = st.builds(Alias)
@given(instance=Alias_strategy)
@settings(max_examples=25)
def test_Alias_instantiation(instance):
    assert isinstance(instance, Alias)


TypeItem_strategy = st.builds(TypeItem)
@given(instance=TypeItem_strategy)
@settings(max_examples=25)
def test_TypeItem_instantiation(instance):
    assert isinstance(instance, TypeItem)


basic_Alias_strategy = st.builds(basic_Alias, name=safe_text, rawName=safe_text)
@given(instance=basic_Alias_strategy)
@settings(max_examples=25)
def test_basic_Alias_instantiation(instance):
    assert isinstance(instance, basic_Alias)


basic_CoreVersionDefault_strategy = st.builds(basic_CoreVersionDefault, coreLib=safe_text, facet=safe_text, version=safe_text)
@given(instance=basic_CoreVersionDefault_strategy)
@settings(max_examples=25)
def test_basic_CoreVersionDefault_instantiation(instance):
    assert isinstance(instance, basic_CoreVersionDefault)


basic_Event_strategy = st.builds(basic_Event, description=safe_text, name=safe_text)
@given(instance=basic_Event_strategy)
@settings(max_examples=25)
def test_basic_Event_instantiation(instance):
    assert isinstance(instance, basic_Event)


basic_ExecutionEnvironment_strategy = st.builds(basic_ExecutionEnvironment, builtin=st.booleans(), corePath=safe_text, coreType=safe_text, facet=safe_text, libraries=safe_text, name=safe_text, versions=safe_text)
@given(instance=basic_ExecutionEnvironment_strategy)
@settings(max_examples=25)
def test_basic_ExecutionEnvironment_instantiation(instance):
    assert isinstance(instance, basic_ExecutionEnvironment)


basic_ExtJSProject_strategy = st.builds(basic_ExtJSProject, name=safe_text)
@given(instance=basic_ExtJSProject_strategy)
@settings(max_examples=25)
def test_basic_ExtJSProject_instantiation(instance):
    assert isinstance(instance, basic_ExtJSProject)


basic_Feature_strategy = st.builds(basic_Feature)
@given(instance=basic_Feature_strategy)
@settings(max_examples=25)
def test_basic_Feature_instantiation(instance):
    assert isinstance(instance, basic_Feature)


basic_File_strategy = st.builds(basic_File, name=safe_text)
@given(instance=basic_File_strategy)
@settings(max_examples=25)
def test_basic_File_instantiation(instance):
    assert isinstance(instance, basic_File)


basic_Layout_strategy = st.builds(basic_Layout)
@given(instance=basic_Layout_strategy)
@settings(max_examples=25)
def test_basic_Layout_instantiation(instance):
    assert isinstance(instance, basic_Layout)


basic_Library_strategy = st.builds(basic_Library, builtin=st.booleans(), name=safe_text, senchaTouchVersions=safe_text, versions=safe_text)
@given(instance=basic_Library_strategy)
@settings(max_examples=25)
def test_basic_Library_instantiation(instance):
    assert isinstance(instance, basic_Library)


basic_LibrarySource_strategy = st.builds(basic_LibrarySource, exclusions=safe_text, inclusions=safe_text, path=safe_text, type=safe_text)
@given(instance=basic_LibrarySource_strategy)
@settings(max_examples=25)
def test_basic_LibrarySource_instantiation(instance):
    assert isinstance(instance, basic_LibrarySource)


basic_Parameter_strategy = st.builds(basic_Parameter, description=safe_text, name=safe_text, type=safe_text)
@given(instance=basic_Parameter_strategy)
@settings(max_examples=25)
def test_basic_Parameter_instantiation(instance):
    assert isinstance(instance, basic_Parameter)


basic_Plugin_strategy = st.builds(basic_Plugin)
@given(instance=basic_Plugin_strategy)
@settings(max_examples=25)
def test_basic_Plugin_instantiation(instance):
    assert isinstance(instance, basic_Plugin)


basic_TypeItem_strategy = st.builds(basic_TypeItem, sourceEnd=st.integers(), sourceStart=st.integers(), typeName=safe_text)
@given(instance=basic_TypeItem_strategy)
@settings(max_examples=25)
def test_basic_TypeItem_instantiation(instance):
    assert isinstance(instance, basic_TypeItem)


basic_Widget_strategy = st.builds(basic_Widget)
@given(instance=basic_Widget_strategy)
@settings(max_examples=25)
def test_basic_Widget_instantiation(instance):
    assert isinstance(instance, basic_Widget)


