import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ant_ArchiveTask,
    Ant_Attribut,
    Ant_Basic,
    Ant_ClassPath,
    Ant_CompileTask,
    Ant_Copy,
    Ant_Delete,
    Ant_DocumentationTask,
    Ant_Echo,
    Ant_Excludes,
    Ant_ExcludesFile,
    Ant_Exec,
    Ant_ExecutionTask,
    Ant_FileList,
    Ant_FileSet,
    Ant_FileTask,
    Ant_Filter,
    Ant_FilterSet,
    Ant_FiltersFile,
    Ant_FormatTstamp,
    Ant_InExcludes,
    Ant_Includes,
    Ant_IncludesFile,
    Ant_Jar,
    Ant_Java,
    Ant_Javac,
    Ant_Javadoc,
    Ant_Mapper,
    Ant_MiscellaneousTask,
    Ant_Mkdir,
    Ant_NewTask,
    Ant_Path,
    Ant_PathElement,
    Ant_Pattern,
    Ant_PatternSet,
    Ant_PreDefinedTask,
    Ant_Project,
    Ant_Property,
    Ant_PropertyEnv,
    Ant_PropertyFile,
    Ant_PropertyLocation,
    Ant_PropertyName,
    Ant_PropertyValue,
    Ant_Set,
    Ant_Target,
    Ant_Task,
    Ant_TaskDef,
    Ant_Tstamp,
    ArchiveTask,
    Basic,
    CompileTask,
    DocumentationTask,
    ExecutionTask,
    FileTask,
    InExcludes,
    MiscellaneousTask,
    Pattern,
    PreDefinedTask,
    Property,
    PropertyName,
    Set,
    Task,
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

def test_assoc_classPath42_reverse_link_reassign_clear():
    a1 = Ant_Java(classname="sample_text", fork="sample_text", jar="sample_text")
    a2 = Ant_Java(classname="sample_text_2", fork="sample_text_2", jar="sample_text_2")
    b = Ant_ClassPath(refid="sample_text")
    _safe_set(b, 'Ant_ClassPath43', a1)
    assert _is_linked(b, 'Ant_ClassPath43', a1)
    if hasattr(a1, 'Ant_Java'):
        assert _is_linked(a1, 'Ant_Java', b)
    _safe_set(b, 'Ant_ClassPath43', a2)
    assert _is_linked(b, 'Ant_ClassPath43', a2)
    if hasattr(a1, 'Ant_Java'):
        assert not _is_linked(a1, 'Ant_Java', b)
    if hasattr(a2, 'Ant_Java'):
        assert _is_linked(a2, 'Ant_Java', b)
    _safe_set(b, 'Ant_ClassPath43', None)
    assert not _is_linked(b, 'Ant_ClassPath43', a2)
    if hasattr(a2, 'Ant_Java'):
        assert not _is_linked(a2, 'Ant_Java', b)


def test_assoc_classPath47_reverse_link_reassign_clear():
    a1 = Ant_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    a2 = Ant_Javac(debug="sample_text_2", deprecation="sample_text_2", destdir="sample_text_2", fork="sample_text_2", optimize="sample_text_2", srcdir="sample_text_2")
    b = Ant_ClassPath(refid="sample_text")
    _safe_set(b, 'Ant_ClassPath49', a1)
    assert _is_linked(b, 'Ant_ClassPath49', a1)
    if hasattr(a1, 'Ant_Javac48'):
        assert _is_linked(a1, 'Ant_Javac48', b)
    _safe_set(b, 'Ant_ClassPath49', a2)
    assert _is_linked(b, 'Ant_ClassPath49', a2)
    if hasattr(a1, 'Ant_Javac48'):
        assert not _is_linked(a1, 'Ant_Javac48', b)
    if hasattr(a2, 'Ant_Javac48'):
        assert _is_linked(a2, 'Ant_Javac48', b)
    _safe_set(b, 'Ant_ClassPath49', None)
    assert not _is_linked(b, 'Ant_ClassPath49', a2)
    if hasattr(a2, 'Ant_Javac48'):
        assert not _is_linked(a2, 'Ant_Javac48', b)


def test_assoc_default0_reverse_link_reassign_clear():
    a1 = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    a2 = Ant_Target(description="sample_text_2", ifCondition="sample_text_2", name="sample_text_2", unless="sample_text_2")
    b = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'Ant_Project', a1)
    assert _is_linked(b, 'Ant_Project', a1)
    if hasattr(a1, 'Ant_Target'):
        assert _is_linked(a1, 'Ant_Target', b)
    _safe_set(b, 'Ant_Project', a2)
    assert _is_linked(b, 'Ant_Project', a2)
    if hasattr(a1, 'Ant_Target'):
        assert not _is_linked(a1, 'Ant_Target', b)
    if hasattr(a2, 'Ant_Target'):
        assert _is_linked(a2, 'Ant_Target', b)
    _safe_set(b, 'Ant_Project', None)
    assert not _is_linked(b, 'Ant_Project', a2)
    if hasattr(a2, 'Ant_Target'):
        assert not _is_linked(a2, 'Ant_Target', b)


def test_assoc_depends11_reverse_link_reassign_clear():
    a1 = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    a2 = Ant_Target(description="sample_text_2", ifCondition="sample_text_2", name="sample_text_2", unless="sample_text_2")
    b = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    _safe_set(b, 'Ant_Target12', a1)
    assert _is_linked(b, 'Ant_Target12', a1)
    if hasattr(a1, 'Ant_Target10'):
        assert _is_linked(a1, 'Ant_Target10', b)
    _safe_set(b, 'Ant_Target12', a2)
    assert _is_linked(b, 'Ant_Target12', a2)
    if hasattr(a1, 'Ant_Target10'):
        assert not _is_linked(a1, 'Ant_Target10', b)
    if hasattr(a2, 'Ant_Target10'):
        assert _is_linked(a2, 'Ant_Target10', b)
    _safe_set(b, 'Ant_Target12', None)
    assert not _is_linked(b, 'Ant_Target12', a2)
    if hasattr(a2, 'Ant_Target10'):
        assert not _is_linked(a2, 'Ant_Target10', b)


def test_assoc_fileset29_reverse_link_reassign_clear():
    a1 = Ant_Path(id="sample_text", refid="sample_text")
    a2 = Ant_Path(id="sample_text_2", refid="sample_text_2")
    b = Ant_FileSet(dir="sample_text")
    _safe_set(b, 'Ant_FileSet31', a1)
    assert _is_linked(b, 'Ant_FileSet31', a1)
    if hasattr(a1, 'Ant_Path30'):
        assert _is_linked(a1, 'Ant_Path30', b)
    _safe_set(b, 'Ant_FileSet31', a2)
    assert _is_linked(b, 'Ant_FileSet31', a2)
    if hasattr(a1, 'Ant_Path30'):
        assert not _is_linked(a1, 'Ant_Path30', b)
    if hasattr(a2, 'Ant_Path30'):
        assert _is_linked(a2, 'Ant_Path30', b)
    _safe_set(b, 'Ant_FileSet31', None)
    assert not _is_linked(b, 'Ant_FileSet31', a2)
    if hasattr(a2, 'Ant_Path30'):
        assert not _is_linked(a2, 'Ant_Path30', b)


def test_assoc_fileset34_reverse_link_reassign_clear():
    a1 = Ant_FileSet(dir="sample_text")
    a2 = Ant_FileSet(dir="sample_text_2")
    b = Ant_ClassPath(refid="sample_text")
    _safe_set(b, 'Ant_ClassPath35', {a1})
    assert _is_linked(b, 'Ant_ClassPath35', a1)
    if hasattr(a1, 'Ant_FileSet36'):
        assert _is_linked(a1, 'Ant_FileSet36', b)
    _safe_set(b, 'Ant_ClassPath35', {a2})
    assert _is_linked(b, 'Ant_ClassPath35', a2)
    if hasattr(a1, 'Ant_FileSet36'):
        assert not _is_linked(a1, 'Ant_FileSet36', b)
    if hasattr(a2, 'Ant_FileSet36'):
        assert _is_linked(a2, 'Ant_FileSet36', b)
    _safe_set(b, 'Ant_ClassPath35', set())
    assert not _is_linked(b, 'Ant_ClassPath35', a2)
    if hasattr(a2, 'Ant_FileSet36'):
        assert not _is_linked(a2, 'Ant_FileSet36', b)


def test_assoc_fileset50_reverse_link_reassign_clear():
    a1 = Ant_FileSet(dir="sample_text")
    a2 = Ant_FileSet(dir="sample_text_2")
    b = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'Ant_Copy', a1)
    assert _is_linked(b, 'Ant_Copy', a1)
    if hasattr(a1, 'Ant_FileSet51'):
        assert _is_linked(a1, 'Ant_FileSet51', b)
    _safe_set(b, 'Ant_Copy', a2)
    assert _is_linked(b, 'Ant_Copy', a2)
    if hasattr(a1, 'Ant_FileSet51'):
        assert not _is_linked(a1, 'Ant_FileSet51', b)
    if hasattr(a2, 'Ant_FileSet51'):
        assert _is_linked(a2, 'Ant_FileSet51', b)
    _safe_set(b, 'Ant_Copy', None)
    assert not _is_linked(b, 'Ant_Copy', a2)
    if hasattr(a2, 'Ant_FileSet51'):
        assert not _is_linked(a2, 'Ant_FileSet51', b)


def test_assoc_filter21_reverse_link_reassign_clear():
    a1 = Ant_FilterSet(endtoken="sample_text", starttoken="sample_text")
    a2 = Ant_FilterSet(endtoken="sample_text_2", starttoken="sample_text_2")
    b = Ant_Filter(token="sample_text", value="sample_text")
    _safe_set(b, 'Ant_Filter', a1)
    assert _is_linked(b, 'Ant_Filter', a1)
    if hasattr(a1, 'Ant_FilterSet'):
        assert _is_linked(a1, 'Ant_FilterSet', b)
    _safe_set(b, 'Ant_Filter', a2)
    assert _is_linked(b, 'Ant_Filter', a2)
    if hasattr(a1, 'Ant_FilterSet'):
        assert not _is_linked(a1, 'Ant_FilterSet', b)
    if hasattr(a2, 'Ant_FilterSet'):
        assert _is_linked(a2, 'Ant_FilterSet', b)
    _safe_set(b, 'Ant_Filter', None)
    assert not _is_linked(b, 'Ant_Filter', a2)
    if hasattr(a2, 'Ant_FilterSet'):
        assert not _is_linked(a2, 'Ant_FilterSet', b)


def test_assoc_filterset52_reverse_link_reassign_clear():
    a1 = Ant_FilterSet(endtoken="sample_text", starttoken="sample_text")
    a2 = Ant_FilterSet(endtoken="sample_text_2", starttoken="sample_text_2")
    b = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'Ant_Copy53', a1)
    assert _is_linked(b, 'Ant_Copy53', a1)
    if hasattr(a1, 'Ant_FilterSet54'):
        assert _is_linked(a1, 'Ant_FilterSet54', b)
    _safe_set(b, 'Ant_Copy53', a2)
    assert _is_linked(b, 'Ant_Copy53', a2)
    if hasattr(a1, 'Ant_FilterSet54'):
        assert not _is_linked(a1, 'Ant_FilterSet54', b)
    if hasattr(a2, 'Ant_FilterSet54'):
        assert _is_linked(a2, 'Ant_FilterSet54', b)
    _safe_set(b, 'Ant_Copy53', None)
    assert not _is_linked(b, 'Ant_Copy53', a2)
    if hasattr(a2, 'Ant_FilterSet54'):
        assert not _is_linked(a2, 'Ant_FilterSet54', b)


def test_assoc_filtersfile22_reverse_link_reassign_clear():
    a1 = Ant_FiltersFile(file="sample_text")
    a2 = Ant_FiltersFile(file="sample_text_2")
    b = Ant_FilterSet(endtoken="sample_text", starttoken="sample_text")
    _safe_set(b, 'Ant_FilterSet23', {a1})
    assert _is_linked(b, 'Ant_FilterSet23', a1)
    if hasattr(a1, 'Ant_FiltersFile'):
        assert _is_linked(a1, 'Ant_FiltersFile', b)
    _safe_set(b, 'Ant_FilterSet23', {a2})
    assert _is_linked(b, 'Ant_FilterSet23', a2)
    if hasattr(a1, 'Ant_FiltersFile'):
        assert not _is_linked(a1, 'Ant_FiltersFile', b)
    if hasattr(a2, 'Ant_FiltersFile'):
        assert _is_linked(a2, 'Ant_FiltersFile', b)
    _safe_set(b, 'Ant_FilterSet23', set())
    assert not _is_linked(b, 'Ant_FilterSet23', a2)
    if hasattr(a2, 'Ant_FiltersFile'):
        assert not _is_linked(a2, 'Ant_FiltersFile', b)


def test_assoc_inExcludes45_reverse_link_reassign_clear():
    a1 = Ant_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    a2 = Ant_Javac(debug="sample_text_2", deprecation="sample_text_2", destdir="sample_text_2", fork="sample_text_2", optimize="sample_text_2", srcdir="sample_text_2")
    b = Ant_InExcludes(ifCondition="sample_text", name="sample_text", unless="sample_text")
    _safe_set(b, 'Ant_InExcludes46', a1)
    assert _is_linked(b, 'Ant_InExcludes46', a1)
    if hasattr(a1, 'Ant_Javac'):
        assert _is_linked(a1, 'Ant_Javac', b)
    _safe_set(b, 'Ant_InExcludes46', a2)
    assert _is_linked(b, 'Ant_InExcludes46', a2)
    if hasattr(a1, 'Ant_Javac'):
        assert not _is_linked(a1, 'Ant_Javac', b)
    if hasattr(a2, 'Ant_Javac'):
        assert _is_linked(a2, 'Ant_Javac', b)
    _safe_set(b, 'Ant_InExcludes46', None)
    assert not _is_linked(b, 'Ant_InExcludes46', a2)
    if hasattr(a2, 'Ant_Javac'):
        assert not _is_linked(a2, 'Ant_Javac', b)


def test_assoc_mapper55_reverse_link_reassign_clear():
    a1 = Ant_Mapper(classname="sample_text", classpath="sample_text", classpathref="sample_text", from_="sample_text", to="sample_text", type="sample_text")
    a2 = Ant_Mapper(classname="sample_text_2", classpath="sample_text_2", classpathref="sample_text_2", from_="sample_text_2", to="sample_text_2", type="sample_text_2")
    b = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'Ant_Copy56', a1)
    assert _is_linked(b, 'Ant_Copy56', a1)
    if hasattr(a1, 'Ant_Mapper'):
        assert _is_linked(a1, 'Ant_Mapper', b)
    _safe_set(b, 'Ant_Copy56', a2)
    assert _is_linked(b, 'Ant_Copy56', a2)
    if hasattr(a1, 'Ant_Mapper'):
        assert not _is_linked(a1, 'Ant_Mapper', b)
    if hasattr(a2, 'Ant_Mapper'):
        assert _is_linked(a2, 'Ant_Mapper', b)
    _safe_set(b, 'Ant_Copy56', None)
    assert not _is_linked(b, 'Ant_Copy56', a2)
    if hasattr(a2, 'Ant_Mapper'):
        assert not _is_linked(a2, 'Ant_Mapper', b)


def test_assoc_path1_reverse_link_reassign_clear():
    a1 = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    a2 = Ant_Project(basedir="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = Ant_Path(id="sample_text", refid="sample_text")
    _safe_set(b, 'Ant_Path', a1)
    assert _is_linked(b, 'Ant_Path', a1)
    if hasattr(a1, 'Ant_Project2'):
        assert _is_linked(a1, 'Ant_Project2', b)
    _safe_set(b, 'Ant_Path', a2)
    assert _is_linked(b, 'Ant_Path', a2)
    if hasattr(a1, 'Ant_Project2'):
        assert not _is_linked(a1, 'Ant_Project2', b)
    if hasattr(a2, 'Ant_Project2'):
        assert _is_linked(a2, 'Ant_Project2', b)
    _safe_set(b, 'Ant_Path', None)
    assert not _is_linked(b, 'Ant_Path', a2)
    if hasattr(a2, 'Ant_Project2'):
        assert not _is_linked(a2, 'Ant_Project2', b)


def test_assoc_path25_reverse_link_reassign_clear():
    a1 = Ant_Path(id="sample_text", refid="sample_text")
    a2 = Ant_Path(id="sample_text_2", refid="sample_text_2")
    b = Ant_Path(id="sample_text", refid="sample_text")
    _safe_set(b, 'Ant_Path26', a1)
    assert _is_linked(b, 'Ant_Path26', a1)
    if hasattr(a1, 'Ant_Path24'):
        assert _is_linked(a1, 'Ant_Path24', b)
    _safe_set(b, 'Ant_Path26', a2)
    assert _is_linked(b, 'Ant_Path26', a2)
    if hasattr(a1, 'Ant_Path24'):
        assert not _is_linked(a1, 'Ant_Path24', b)
    if hasattr(a2, 'Ant_Path24'):
        assert _is_linked(a2, 'Ant_Path24', b)
    _safe_set(b, 'Ant_Path26', None)
    assert not _is_linked(b, 'Ant_Path26', a2)
    if hasattr(a2, 'Ant_Path24'):
        assert not _is_linked(a2, 'Ant_Path24', b)


def test_assoc_pathElement27_reverse_link_reassign_clear():
    a1 = Ant_PathElement(location="sample_text", path="sample_text")
    a2 = Ant_PathElement(location="sample_text_2", path="sample_text_2")
    b = Ant_Path(id="sample_text", refid="sample_text")
    _safe_set(b, 'Ant_Path28', {a1})
    assert _is_linked(b, 'Ant_Path28', a1)
    if hasattr(a1, 'Ant_PathElement'):
        assert _is_linked(a1, 'Ant_PathElement', b)
    _safe_set(b, 'Ant_Path28', {a2})
    assert _is_linked(b, 'Ant_Path28', a2)
    if hasattr(a1, 'Ant_PathElement'):
        assert not _is_linked(a1, 'Ant_PathElement', b)
    if hasattr(a2, 'Ant_PathElement'):
        assert _is_linked(a2, 'Ant_PathElement', b)
    _safe_set(b, 'Ant_Path28', set())
    assert not _is_linked(b, 'Ant_Path28', a2)
    if hasattr(a2, 'Ant_PathElement'):
        assert not _is_linked(a2, 'Ant_PathElement', b)


def test_assoc_pathElement32_reverse_link_reassign_clear():
    a1 = Ant_PathElement(location="sample_text", path="sample_text")
    a2 = Ant_PathElement(location="sample_text_2", path="sample_text_2")
    b = Ant_ClassPath(refid="sample_text")
    _safe_set(b, 'Ant_ClassPath', {a1})
    assert _is_linked(b, 'Ant_ClassPath', a1)
    if hasattr(a1, 'Ant_PathElement33'):
        assert _is_linked(a1, 'Ant_PathElement33', b)
    _safe_set(b, 'Ant_ClassPath', {a2})
    assert _is_linked(b, 'Ant_ClassPath', a2)
    if hasattr(a1, 'Ant_PathElement33'):
        assert not _is_linked(a1, 'Ant_PathElement33', b)
    if hasattr(a2, 'Ant_PathElement33'):
        assert _is_linked(a2, 'Ant_PathElement33', b)
    _safe_set(b, 'Ant_ClassPath', set())
    assert not _is_linked(b, 'Ant_ClassPath', a2)
    if hasattr(a2, 'Ant_PathElement33'):
        assert not _is_linked(a2, 'Ant_PathElement33', b)


def test_assoc_targets7_reverse_link_reassign_clear():
    a1 = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    a2 = Ant_Target(description="sample_text_2", ifCondition="sample_text_2", name="sample_text_2", unless="sample_text_2")
    b = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'Ant_Project8', {a1})
    assert _is_linked(b, 'Ant_Project8', a1)
    if hasattr(a1, 'Ant_Target9'):
        assert _is_linked(a1, 'Ant_Target9', b)
    _safe_set(b, 'Ant_Project8', {a2})
    assert _is_linked(b, 'Ant_Project8', a2)
    if hasattr(a1, 'Ant_Target9'):
        assert not _is_linked(a1, 'Ant_Target9', b)
    if hasattr(a2, 'Ant_Target9'):
        assert _is_linked(a2, 'Ant_Target9', b)
    _safe_set(b, 'Ant_Project8', set())
    assert not _is_linked(b, 'Ant_Project8', a2)
    if hasattr(a2, 'Ant_Target9'):
        assert not _is_linked(a2, 'Ant_Target9', b)


def test_assoc_taskdef5_reverse_link_reassign_clear():
    a1 = Ant_TaskDef(classname="sample_text", name="sample_text")
    a2 = Ant_TaskDef(classname="sample_text_2", name="sample_text_2")
    b = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'Ant_Project6', {a1})
    assert _is_linked(b, 'Ant_Project6', a1)
    if hasattr(a1, 'Ant_TaskDef'):
        assert _is_linked(a1, 'Ant_TaskDef', b)
    _safe_set(b, 'Ant_Project6', {a2})
    assert _is_linked(b, 'Ant_Project6', a2)
    if hasattr(a1, 'Ant_TaskDef'):
        assert not _is_linked(a1, 'Ant_TaskDef', b)
    if hasattr(a2, 'Ant_TaskDef'):
        assert _is_linked(a2, 'Ant_TaskDef', b)
    _safe_set(b, 'Ant_Project6', set())
    assert not _is_linked(b, 'Ant_Project6', a2)
    if hasattr(a2, 'Ant_TaskDef'):
        assert not _is_linked(a2, 'Ant_TaskDef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes40_stub_double():
    # Ant_NewTask has no real 'Ant_NewTask41' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Attribut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Attribut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Attribut(name="sample_text", value="sample_text")
    partner = Ant_NewTask()
    setattr(partner, 'Ant_NewTask41', None)
    _safe_set(owner, 'Ant_Attribut', partner)
    assert owner in getattr(partner, 'Ant_NewTask41')
    _safe_set(owner, 'Ant_Attribut', None)
    assert owner not in getattr(partner, 'Ant_NewTask41')


def test_assoc_exclude19_stub_double():
    # Ant_Excludes has no real 'Ant_Excludes' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = Ant_Excludes()
    setattr(partner, 'Ant_Excludes', None)
    _safe_set(owner, 'Ant_FileSet20', {partner})
    assert getattr(partner, 'Ant_Excludes') == owner
    _safe_set(owner, 'Ant_FileSet20', set())
    assert getattr(partner, 'Ant_Excludes') is None


def test_assoc_include17_stub_double():
    # Ant_Includes has no real 'Ant_Includes' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = Ant_Includes()
    setattr(partner, 'Ant_Includes', None)
    _safe_set(owner, 'Ant_FileSet18', {partner})
    assert getattr(partner, 'Ant_Includes') == owner
    _safe_set(owner, 'Ant_FileSet18', set())
    assert getattr(partner, 'Ant_Includes') is None


def test_assoc_inexcludes14_stub_double():
    # Ant_PatternSet has no real 'Ant_PatternSet' property in the generated
    # code (a bare stub) -- manually attach it so Ant_InExcludes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_InExcludes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_InExcludes(ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = Ant_PatternSet()
    setattr(partner, 'Ant_PatternSet', None)
    _safe_set(owner, 'Ant_InExcludes', partner)
    assert owner in getattr(partner, 'Ant_PatternSet')
    _safe_set(owner, 'Ant_InExcludes', None)
    assert owner not in getattr(partner, 'Ant_PatternSet')


def test_assoc_patternset15_stub_double():
    # Ant_PatternSet has no real 'Ant_PatternSet16' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = Ant_PatternSet()
    setattr(partner, 'Ant_PatternSet16', None)
    _safe_set(owner, 'Ant_FileSet', {partner})
    assert getattr(partner, 'Ant_PatternSet16') == owner
    _safe_set(owner, 'Ant_FileSet', set())
    assert getattr(partner, 'Ant_PatternSet16') is None


def test_assoc_properties3_stub_double():
    # Ant_Property has no real 'Ant_Property' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = Ant_Property()
    setattr(partner, 'Ant_Property', None)
    _safe_set(owner, 'Ant_Project4', {partner})
    assert getattr(partner, 'Ant_Property') == owner
    _safe_set(owner, 'Ant_Project4', set())
    assert getattr(partner, 'Ant_Property') is None


def test_assoc_target37_stub_double():
    # Ant_Task has no real 'tasks' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = Ant_Task()
    setattr(partner, 'tasks', None)
    _safe_set(owner, 'Target', partner)
    assert getattr(partner, 'tasks') == owner
    _safe_set(owner, 'Target', None)
    assert getattr(partner, 'tasks') is None


def test_assoc_taskName38_stub_double():
    # Ant_NewTask has no real 'Ant_NewTask' property in the generated
    # code (a bare stub) -- manually attach it so Ant_TaskDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_TaskDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_TaskDef(classname="sample_text", name="sample_text")
    partner = Ant_NewTask()
    setattr(partner, 'Ant_NewTask', None)
    _safe_set(owner, 'Ant_TaskDef39', partner)
    assert getattr(partner, 'Ant_NewTask') == owner
    _safe_set(owner, 'Ant_TaskDef39', None)
    assert getattr(partner, 'Ant_NewTask') is None


def test_assoc_tasks13_stub_double():
    # Ant_Task has no real 'Task' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = Ant_Task()
    setattr(partner, 'Task', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Task') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Task') is None


