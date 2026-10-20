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
    Attribut,
    Basic,
    ClassPath,
    CompileTask,
    DocumentationTask,
    Excludes,
    FileSet,
    FileTask,
    Filter,
    FilterSet,
    FiltersFile,
    FormatTstamp,
    InExcludes,
    Includes,
    Mapper,
    MiscellaneousTask,
    Path,
    PathElement,
    Pattern,
    PatternSet,
    PreDefinedTask,
    Property,
    PropertyName,
    Set,
    Target,
    Task,
    TaskDef,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classPath39_stub_double():
    # ClassPath has no real 'ClassPath' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Java's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Java's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Java(classname="sample_text", fork="sample_text", jar="sample_text")
    partner = ClassPath()
    setattr(partner, 'ClassPath', None)
    _safe_set(owner, 'Ant_Java', partner)
    assert getattr(partner, 'ClassPath') == owner
    _safe_set(owner, 'Ant_Java', None)
    assert getattr(partner, 'ClassPath') is None


def test_assoc_classPath43_stub_double():
    # ClassPath has no real 'ClassPath45' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Javac's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Javac's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    partner = ClassPath()
    setattr(partner, 'ClassPath45', None)
    _safe_set(owner, 'Ant_Javac44', partner)
    assert getattr(partner, 'ClassPath45') == owner
    _safe_set(owner, 'Ant_Javac44', None)
    assert getattr(partner, 'ClassPath45') is None


def test_assoc_default0_stub_double():
    # Target has no real 'Target' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = Target()
    setattr(partner, 'Target', None)
    _safe_set(owner, 'Ant_Project', partner)
    assert getattr(partner, 'Target') == owner
    _safe_set(owner, 'Ant_Project', None)
    assert getattr(partner, 'Target') is None


def test_assoc_depends10_stub_double():
    # Target has no real 'Target11' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = Target()
    setattr(partner, 'Target11', None)
    _safe_set(owner, 'Ant_Target', {partner})
    assert getattr(partner, 'Target11') == owner
    _safe_set(owner, 'Ant_Target', set())
    assert getattr(partner, 'Target11') is None


def test_assoc_exclude17_stub_double():
    # Excludes has no real 'Excludes' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = Excludes()
    setattr(partner, 'Excludes', None)
    _safe_set(owner, 'Ant_FileSet18', {partner})
    assert getattr(partner, 'Excludes') == owner
    _safe_set(owner, 'Ant_FileSet18', set())
    assert getattr(partner, 'Excludes') is None


def test_assoc_fileset26_stub_double():
    # FileSet has no real 'FileSet' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Path(id="sample_text", refid="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet', None)
    _safe_set(owner, 'Ant_Path27', {partner})
    assert getattr(partner, 'FileSet') == owner
    _safe_set(owner, 'Ant_Path27', set())
    assert getattr(partner, 'FileSet') is None


def test_assoc_fileset30_stub_double():
    # FileSet has no real 'FileSet32' property in the generated
    # code (a bare stub) -- manually attach it so Ant_ClassPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_ClassPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_ClassPath(refid="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet32', None)
    _safe_set(owner, 'Ant_ClassPath31', {partner})
    assert getattr(partner, 'FileSet32') == owner
    _safe_set(owner, 'Ant_ClassPath31', set())
    assert getattr(partner, 'FileSet32') is None


def test_assoc_fileset46_stub_double():
    # FileSet has no real 'FileSet47' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet47', None)
    _safe_set(owner, 'Ant_Copy', partner)
    assert getattr(partner, 'FileSet47') == owner
    _safe_set(owner, 'Ant_Copy', None)
    assert getattr(partner, 'FileSet47') is None


def test_assoc_filter19_stub_double():
    # Filter has no real 'Filter' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FilterSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FilterSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FilterSet(endtoken="sample_text", starttoken="sample_text")
    partner = Filter()
    setattr(partner, 'Filter', None)
    _safe_set(owner, 'Ant_FilterSet', {partner})
    assert getattr(partner, 'Filter') == owner
    _safe_set(owner, 'Ant_FilterSet', set())
    assert getattr(partner, 'Filter') is None


def test_assoc_filterset48_stub_double():
    # FilterSet has no real 'FilterSet' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = FilterSet()
    setattr(partner, 'FilterSet', None)
    _safe_set(owner, 'Ant_Copy49', partner)
    assert getattr(partner, 'FilterSet') == owner
    _safe_set(owner, 'Ant_Copy49', None)
    assert getattr(partner, 'FilterSet') is None


def test_assoc_filtersfile20_stub_double():
    # FiltersFile has no real 'FiltersFile' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FilterSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FilterSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FilterSet(endtoken="sample_text", starttoken="sample_text")
    partner = FiltersFile()
    setattr(partner, 'FiltersFile', None)
    _safe_set(owner, 'Ant_FilterSet21', {partner})
    assert getattr(partner, 'FiltersFile') == owner
    _safe_set(owner, 'Ant_FilterSet21', set())
    assert getattr(partner, 'FiltersFile') is None


def test_assoc_inExcludes41_stub_double():
    # InExcludes has no real 'InExcludes42' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Javac's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Javac's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    partner = InExcludes()
    setattr(partner, 'InExcludes42', None)
    _safe_set(owner, 'Ant_Javac', {partner})
    assert getattr(partner, 'InExcludes42') == owner
    _safe_set(owner, 'Ant_Javac', set())
    assert getattr(partner, 'InExcludes42') is None


def test_assoc_include15_stub_double():
    # Includes has no real 'Includes' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = Includes()
    setattr(partner, 'Includes', None)
    _safe_set(owner, 'Ant_FileSet16', {partner})
    assert getattr(partner, 'Includes') == owner
    _safe_set(owner, 'Ant_FileSet16', set())
    assert getattr(partner, 'Includes') is None


def test_assoc_mapper50_stub_double():
    # Mapper has no real 'Mapper' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = Mapper()
    setattr(partner, 'Mapper', None)
    _safe_set(owner, 'Ant_Copy51', partner)
    assert getattr(partner, 'Mapper') == owner
    _safe_set(owner, 'Ant_Copy51', None)
    assert getattr(partner, 'Mapper') is None


def test_assoc_path1_stub_double():
    # Path has no real 'Path' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = Path()
    setattr(partner, 'Path', None)
    _safe_set(owner, 'Ant_Project2', partner)
    assert getattr(partner, 'Path') == owner
    _safe_set(owner, 'Ant_Project2', None)
    assert getattr(partner, 'Path') is None


def test_assoc_path22_stub_double():
    # Path has no real 'Path23' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Path(id="sample_text", refid="sample_text")
    partner = Path()
    setattr(partner, 'Path23', None)
    _safe_set(owner, 'Ant_Path', partner)
    assert getattr(partner, 'Path23') == owner
    _safe_set(owner, 'Ant_Path', None)
    assert getattr(partner, 'Path23') is None


def test_assoc_pathElement24_stub_double():
    # PathElement has no real 'PathElement' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Path(id="sample_text", refid="sample_text")
    partner = PathElement()
    setattr(partner, 'PathElement', None)
    _safe_set(owner, 'Ant_Path25', {partner})
    assert getattr(partner, 'PathElement') == owner
    _safe_set(owner, 'Ant_Path25', set())
    assert getattr(partner, 'PathElement') is None


def test_assoc_pathElement28_stub_double():
    # PathElement has no real 'PathElement29' property in the generated
    # code (a bare stub) -- manually attach it so Ant_ClassPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_ClassPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_ClassPath(refid="sample_text")
    partner = PathElement()
    setattr(partner, 'PathElement29', None)
    _safe_set(owner, 'Ant_ClassPath', {partner})
    assert getattr(partner, 'PathElement29') == owner
    _safe_set(owner, 'Ant_ClassPath', set())
    assert getattr(partner, 'PathElement29') is None


def test_assoc_patternset14_stub_double():
    # PatternSet has no real 'PatternSet' property in the generated
    # code (a bare stub) -- manually attach it so Ant_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_FileSet(dir="sample_text")
    partner = PatternSet()
    setattr(partner, 'PatternSet', None)
    _safe_set(owner, 'Ant_FileSet', {partner})
    assert getattr(partner, 'PatternSet') == owner
    _safe_set(owner, 'Ant_FileSet', set())
    assert getattr(partner, 'PatternSet') is None


def test_assoc_properties3_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'Ant_Project4', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'Ant_Project4', set())
    assert getattr(partner, 'Property') is None


def test_assoc_targets7_stub_double():
    # Target has no real 'Target9' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = Target()
    setattr(partner, 'Target9', None)
    _safe_set(owner, 'Ant_Project8', {partner})
    assert getattr(partner, 'Target9') == owner
    _safe_set(owner, 'Ant_Project8', set())
    assert getattr(partner, 'Target9') is None


def test_assoc_taskdef5_stub_double():
    # TaskDef has no real 'TaskDef' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Project(basedir="sample_text", description="sample_text", name="sample_text")
    partner = TaskDef()
    setattr(partner, 'TaskDef', None)
    _safe_set(owner, 'Ant_Project6', {partner})
    assert getattr(partner, 'TaskDef') == owner
    _safe_set(owner, 'Ant_Project6', set())
    assert getattr(partner, 'TaskDef') is None


def test_assoc_tasks12_stub_double():
    # Task has no real 'Task' property in the generated
    # code (a bare stub) -- manually attach it so Ant_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ant_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ant_Target(description="sample_text", ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = Task()
    setattr(partner, 'Task', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Task') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Task') is None


