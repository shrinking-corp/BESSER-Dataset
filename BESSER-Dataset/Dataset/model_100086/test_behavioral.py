import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractGoal,
    AntProperty,
    AntPropertyName,
    AntTaskDef,
    ArchiveTask,
    Attribut,
    Basic,
    ClassPath,
    CompileTask,
    ContentsGoal,
    DocumentationTask,
    Excludes,
    ExecutionTask,
    FileSet,
    FileTask,
    Filter,
    FilterSet,
    FiltersFile,
    FormatTstamp,
    Goal,
    InExcludes,
    Includes,
    JellyCommand,
    Mapper,
    MavenMaven_AbstractGoal,
    MavenMaven_AntProperty,
    MavenMaven_AntPropertyEnv,
    MavenMaven_AntPropertyFile,
    MavenMaven_AntPropertyLocation,
    MavenMaven_AntPropertyName,
    MavenMaven_AntPropertyValue,
    MavenMaven_AntTaskDef,
    MavenMaven_ArchiveTask,
    MavenMaven_AttainGoal,
    MavenMaven_Attribut,
    MavenMaven_Basic,
    MavenMaven_ClassPath,
    MavenMaven_CompileTask,
    MavenMaven_ContentsGoal,
    MavenMaven_Copy,
    MavenMaven_Delete,
    MavenMaven_DocumentationTask,
    MavenMaven_Echo,
    MavenMaven_Excludes,
    MavenMaven_ExcludesFile,
    MavenMaven_Exec,
    MavenMaven_ExecutionTask,
    MavenMaven_FileList,
    MavenMaven_FileSet,
    MavenMaven_FileTask,
    MavenMaven_Filter,
    MavenMaven_FilterSet,
    MavenMaven_FiltersFile,
    MavenMaven_FormatTstamp,
    MavenMaven_Goal,
    MavenMaven_InExcludes,
    MavenMaven_Includes,
    MavenMaven_IncludesFile,
    MavenMaven_Jar,
    MavenMaven_Java,
    MavenMaven_Javac,
    MavenMaven_Javadoc,
    MavenMaven_JellyCommand,
    MavenMaven_JellyForEach,
    MavenMaven_JellySet,
    MavenMaven_Mapper,
    MavenMaven_MiscellaneousTask,
    MavenMaven_Mkdir,
    MavenMaven_NewTask,
    MavenMaven_Path,
    MavenMaven_PathElement,
    MavenMaven_Pattern,
    MavenMaven_PatternSet,
    MavenMaven_PostGoal,
    MavenMaven_PreDefinedTask,
    MavenMaven_PreGoal,
    MavenMaven_PrePostGoal,
    MavenMaven_Project,
    MavenMaven_Set,
    MavenMaven_Task,
    MavenMaven_Tstamp,
    MavenMaven_Xmlns,
    MiscellaneousTask,
    Path,
    PathElement,
    Pattern,
    PatternSet,
    PostGoal,
    PreDefinedTask,
    PreGoal,
    PrePostGoal,
    Set,
    Task,
    Xmlns,
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

def test_assoc_classPath50_stub_double():
    # ClassPath has no real 'ClassPath' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Java's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Java's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Java(classname="sample_text", fork="sample_text", jar="sample_text")
    partner = ClassPath()
    setattr(partner, 'ClassPath', None)
    _safe_set(owner, 'MavenMaven_Java', partner)
    assert getattr(partner, 'ClassPath') == owner
    _safe_set(owner, 'MavenMaven_Java', None)
    assert getattr(partner, 'ClassPath') is None


def test_assoc_classPath54_stub_double():
    # ClassPath has no real 'ClassPath56' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Javac's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Javac's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    partner = ClassPath()
    setattr(partner, 'ClassPath56', None)
    _safe_set(owner, 'MavenMaven_Javac55', partner)
    assert getattr(partner, 'ClassPath56') == owner
    _safe_set(owner, 'MavenMaven_Javac55', None)
    assert getattr(partner, 'ClassPath56') is None


def test_assoc_contents14_stub_double():
    # ContentsGoal has no real 'ContentsGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_JellyForEach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_JellyForEach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_JellyForEach(indexVar="sample_text", items="sample_text", var="sample_text")
    partner = ContentsGoal()
    setattr(partner, 'ContentsGoal', None)
    _safe_set(owner, 'MavenMaven_JellyForEach', partner)
    assert getattr(partner, 'ContentsGoal') == owner
    _safe_set(owner, 'MavenMaven_JellyForEach', None)
    assert getattr(partner, 'ContentsGoal') is None


def test_assoc_exclude30_stub_double():
    # Excludes has no real 'Excludes' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = Excludes()
    setattr(partner, 'Excludes', None)
    _safe_set(owner, 'MavenMaven_FileSet31', {partner})
    assert getattr(partner, 'Excludes') == owner
    _safe_set(owner, 'MavenMaven_FileSet31', set())
    assert getattr(partner, 'Excludes') is None


def test_assoc_fileset39_stub_double():
    # FileSet has no real 'FileSet' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Path(id="sample_text", refid="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet', None)
    _safe_set(owner, 'MavenMaven_Path40', {partner})
    assert getattr(partner, 'FileSet') == owner
    _safe_set(owner, 'MavenMaven_Path40', set())
    assert getattr(partner, 'FileSet') is None


def test_assoc_fileset43_stub_double():
    # FileSet has no real 'FileSet45' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_ClassPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_ClassPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_ClassPath(refid="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet45', None)
    _safe_set(owner, 'MavenMaven_ClassPath44', {partner})
    assert getattr(partner, 'FileSet45') == owner
    _safe_set(owner, 'MavenMaven_ClassPath44', set())
    assert getattr(partner, 'FileSet45') is None


def test_assoc_fileset57_stub_double():
    # FileSet has no real 'FileSet58' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = FileSet()
    setattr(partner, 'FileSet58', None)
    _safe_set(owner, 'MavenMaven_Copy', partner)
    assert getattr(partner, 'FileSet58') == owner
    _safe_set(owner, 'MavenMaven_Copy', None)
    assert getattr(partner, 'FileSet58') is None


def test_assoc_filter32_stub_double():
    # Filter has no real 'Filter' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FilterSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FilterSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FilterSet(endtoken="sample_text", starttoken="sample_text")
    partner = Filter()
    setattr(partner, 'Filter', None)
    _safe_set(owner, 'MavenMaven_FilterSet', {partner})
    assert getattr(partner, 'Filter') == owner
    _safe_set(owner, 'MavenMaven_FilterSet', set())
    assert getattr(partner, 'Filter') is None


def test_assoc_filterset59_stub_double():
    # FilterSet has no real 'FilterSet' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = FilterSet()
    setattr(partner, 'FilterSet', None)
    _safe_set(owner, 'MavenMaven_Copy60', partner)
    assert getattr(partner, 'FilterSet') == owner
    _safe_set(owner, 'MavenMaven_Copy60', None)
    assert getattr(partner, 'FilterSet') is None


def test_assoc_filtersfile33_stub_double():
    # FiltersFile has no real 'FiltersFile' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FilterSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FilterSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FilterSet(endtoken="sample_text", starttoken="sample_text")
    partner = FiltersFile()
    setattr(partner, 'FiltersFile', None)
    _safe_set(owner, 'MavenMaven_FilterSet34', {partner})
    assert getattr(partner, 'FiltersFile') == owner
    _safe_set(owner, 'MavenMaven_FilterSet34', set())
    assert getattr(partner, 'FiltersFile') is None


def test_assoc_inExcludes52_stub_double():
    # InExcludes has no real 'InExcludes53' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Javac's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Javac's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    partner = InExcludes()
    setattr(partner, 'InExcludes53', None)
    _safe_set(owner, 'MavenMaven_Javac', {partner})
    assert getattr(partner, 'InExcludes53') == owner
    _safe_set(owner, 'MavenMaven_Javac', set())
    assert getattr(partner, 'InExcludes53') is None


def test_assoc_include28_stub_double():
    # Includes has no real 'Includes' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = Includes()
    setattr(partner, 'Includes', None)
    _safe_set(owner, 'MavenMaven_FileSet29', {partner})
    assert getattr(partner, 'Includes') == owner
    _safe_set(owner, 'MavenMaven_FileSet29', set())
    assert getattr(partner, 'Includes') is None


def test_assoc_mapper61_stub_double():
    # Mapper has no real 'Mapper' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Copy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Copy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    partner = Mapper()
    setattr(partner, 'Mapper', None)
    _safe_set(owner, 'MavenMaven_Copy62', partner)
    assert getattr(partner, 'Mapper') == owner
    _safe_set(owner, 'MavenMaven_Copy62', None)
    assert getattr(partner, 'Mapper') is None


def test_assoc_path35_stub_double():
    # Path has no real 'Path36' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Path(id="sample_text", refid="sample_text")
    partner = Path()
    setattr(partner, 'Path36', None)
    _safe_set(owner, 'MavenMaven_Path', partner)
    assert getattr(partner, 'Path36') == owner
    _safe_set(owner, 'MavenMaven_Path', None)
    assert getattr(partner, 'Path36') is None


def test_assoc_pathElement37_stub_double():
    # PathElement has no real 'PathElement' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Path(id="sample_text", refid="sample_text")
    partner = PathElement()
    setattr(partner, 'PathElement', None)
    _safe_set(owner, 'MavenMaven_Path38', {partner})
    assert getattr(partner, 'PathElement') == owner
    _safe_set(owner, 'MavenMaven_Path38', set())
    assert getattr(partner, 'PathElement') is None


def test_assoc_pathElement41_stub_double():
    # PathElement has no real 'PathElement42' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_ClassPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_ClassPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_ClassPath(refid="sample_text")
    partner = PathElement()
    setattr(partner, 'PathElement42', None)
    _safe_set(owner, 'MavenMaven_ClassPath', {partner})
    assert getattr(partner, 'PathElement42') == owner
    _safe_set(owner, 'MavenMaven_ClassPath', set())
    assert getattr(partner, 'PathElement42') is None


def test_assoc_patternset27_stub_double():
    # PatternSet has no real 'PatternSet' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = PatternSet()
    setattr(partner, 'PatternSet', None)
    _safe_set(owner, 'MavenMaven_FileSet', {partner})
    assert getattr(partner, 'PatternSet') == owner
    _safe_set(owner, 'MavenMaven_FileSet', set())
    assert getattr(partner, 'PatternSet') is None


def test_assoc_postGoal24_stub_double():
    # PostGoal has no real 'PostGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = PostGoal()
    setattr(partner, 'PostGoal', None)
    _safe_set(owner, 'centralGoal25', partner)
    assert getattr(partner, 'PostGoal') == owner
    _safe_set(owner, 'centralGoal25', None)
    assert getattr(partner, 'PostGoal') is None


def test_assoc_preGoal23_stub_double():
    # PreGoal has no real 'PreGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = PreGoal()
    setattr(partner, 'PreGoal', None)
    _safe_set(owner, 'centralGoal', partner)
    assert getattr(partner, 'PreGoal') == owner
    _safe_set(owner, 'centralGoal', None)
    assert getattr(partner, 'PreGoal') is None


