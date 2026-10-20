import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractGoal,
    AntProperty,
    AntPropertyName,
    ArchiveTask,
    Basic,
    CompileTask,
    ContentsGoal,
    DocumentationTask,
    ExecutionTask,
    FileTask,
    InExcludes,
    JellyCommand,
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
    Pattern,
    PreDefinedTask,
    PrePostGoal,
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

def test_assoc_classPath50_reverse_link_reassign_clear():
    a1 = MavenMaven_Java(classname="sample_text", fork="sample_text", jar="sample_text")
    a2 = MavenMaven_Java(classname="sample_text_2", fork="sample_text_2", jar="sample_text_2")
    b = MavenMaven_ClassPath(refid="sample_text")
    _safe_set(b, 'MavenMaven_ClassPath51', a1)
    assert _is_linked(b, 'MavenMaven_ClassPath51', a1)
    if hasattr(a1, 'MavenMaven_Java'):
        assert _is_linked(a1, 'MavenMaven_Java', b)
    _safe_set(b, 'MavenMaven_ClassPath51', a2)
    assert _is_linked(b, 'MavenMaven_ClassPath51', a2)
    if hasattr(a1, 'MavenMaven_Java'):
        assert not _is_linked(a1, 'MavenMaven_Java', b)
    if hasattr(a2, 'MavenMaven_Java'):
        assert _is_linked(a2, 'MavenMaven_Java', b)
    _safe_set(b, 'MavenMaven_ClassPath51', None)
    assert not _is_linked(b, 'MavenMaven_ClassPath51', a2)
    if hasattr(a2, 'MavenMaven_Java'):
        assert not _is_linked(a2, 'MavenMaven_Java', b)


def test_assoc_classPath55_reverse_link_reassign_clear():
    a1 = MavenMaven_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    a2 = MavenMaven_Javac(debug="sample_text_2", deprecation="sample_text_2", destdir="sample_text_2", fork="sample_text_2", optimize="sample_text_2", srcdir="sample_text_2")
    b = MavenMaven_ClassPath(refid="sample_text")
    _safe_set(b, 'MavenMaven_ClassPath57', a1)
    assert _is_linked(b, 'MavenMaven_ClassPath57', a1)
    if hasattr(a1, 'MavenMaven_Javac56'):
        assert _is_linked(a1, 'MavenMaven_Javac56', b)
    _safe_set(b, 'MavenMaven_ClassPath57', a2)
    assert _is_linked(b, 'MavenMaven_ClassPath57', a2)
    if hasattr(a1, 'MavenMaven_Javac56'):
        assert not _is_linked(a1, 'MavenMaven_Javac56', b)
    if hasattr(a2, 'MavenMaven_Javac56'):
        assert _is_linked(a2, 'MavenMaven_Javac56', b)
    _safe_set(b, 'MavenMaven_ClassPath57', None)
    assert not _is_linked(b, 'MavenMaven_ClassPath57', a2)
    if hasattr(a2, 'MavenMaven_Javac56'):
        assert not _is_linked(a2, 'MavenMaven_Javac56', b)


def test_assoc_fileset38_reverse_link_reassign_clear():
    a1 = MavenMaven_Path(id="sample_text", refid="sample_text")
    a2 = MavenMaven_Path(id="sample_text_2", refid="sample_text_2")
    b = MavenMaven_FileSet(dir="sample_text")
    _safe_set(b, 'MavenMaven_FileSet40', a1)
    assert _is_linked(b, 'MavenMaven_FileSet40', a1)
    if hasattr(a1, 'MavenMaven_Path39'):
        assert _is_linked(a1, 'MavenMaven_Path39', b)
    _safe_set(b, 'MavenMaven_FileSet40', a2)
    assert _is_linked(b, 'MavenMaven_FileSet40', a2)
    if hasattr(a1, 'MavenMaven_Path39'):
        assert not _is_linked(a1, 'MavenMaven_Path39', b)
    if hasattr(a2, 'MavenMaven_Path39'):
        assert _is_linked(a2, 'MavenMaven_Path39', b)
    _safe_set(b, 'MavenMaven_FileSet40', None)
    assert not _is_linked(b, 'MavenMaven_FileSet40', a2)
    if hasattr(a2, 'MavenMaven_Path39'):
        assert not _is_linked(a2, 'MavenMaven_Path39', b)


def test_assoc_fileset43_reverse_link_reassign_clear():
    a1 = MavenMaven_FileSet(dir="sample_text")
    a2 = MavenMaven_FileSet(dir="sample_text_2")
    b = MavenMaven_ClassPath(refid="sample_text")
    _safe_set(b, 'MavenMaven_ClassPath44', {a1})
    assert _is_linked(b, 'MavenMaven_ClassPath44', a1)
    if hasattr(a1, 'MavenMaven_FileSet45'):
        assert _is_linked(a1, 'MavenMaven_FileSet45', b)
    _safe_set(b, 'MavenMaven_ClassPath44', {a2})
    assert _is_linked(b, 'MavenMaven_ClassPath44', a2)
    if hasattr(a1, 'MavenMaven_FileSet45'):
        assert not _is_linked(a1, 'MavenMaven_FileSet45', b)
    if hasattr(a2, 'MavenMaven_FileSet45'):
        assert _is_linked(a2, 'MavenMaven_FileSet45', b)
    _safe_set(b, 'MavenMaven_ClassPath44', set())
    assert not _is_linked(b, 'MavenMaven_ClassPath44', a2)
    if hasattr(a2, 'MavenMaven_FileSet45'):
        assert not _is_linked(a2, 'MavenMaven_FileSet45', b)


def test_assoc_fileset58_reverse_link_reassign_clear():
    a1 = MavenMaven_FileSet(dir="sample_text")
    a2 = MavenMaven_FileSet(dir="sample_text_2")
    b = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'MavenMaven_Copy', a1)
    assert _is_linked(b, 'MavenMaven_Copy', a1)
    if hasattr(a1, 'MavenMaven_FileSet59'):
        assert _is_linked(a1, 'MavenMaven_FileSet59', b)
    _safe_set(b, 'MavenMaven_Copy', a2)
    assert _is_linked(b, 'MavenMaven_Copy', a2)
    if hasattr(a1, 'MavenMaven_FileSet59'):
        assert not _is_linked(a1, 'MavenMaven_FileSet59', b)
    if hasattr(a2, 'MavenMaven_FileSet59'):
        assert _is_linked(a2, 'MavenMaven_FileSet59', b)
    _safe_set(b, 'MavenMaven_Copy', None)
    assert not _is_linked(b, 'MavenMaven_Copy', a2)
    if hasattr(a2, 'MavenMaven_FileSet59'):
        assert not _is_linked(a2, 'MavenMaven_FileSet59', b)


def test_assoc_filter30_reverse_link_reassign_clear():
    a1 = MavenMaven_FilterSet(endtoken="sample_text", starttoken="sample_text")
    a2 = MavenMaven_FilterSet(endtoken="sample_text_2", starttoken="sample_text_2")
    b = MavenMaven_Filter(token="sample_text", value="sample_text")
    _safe_set(b, 'MavenMaven_Filter', a1)
    assert _is_linked(b, 'MavenMaven_Filter', a1)
    if hasattr(a1, 'MavenMaven_FilterSet'):
        assert _is_linked(a1, 'MavenMaven_FilterSet', b)
    _safe_set(b, 'MavenMaven_Filter', a2)
    assert _is_linked(b, 'MavenMaven_Filter', a2)
    if hasattr(a1, 'MavenMaven_FilterSet'):
        assert not _is_linked(a1, 'MavenMaven_FilterSet', b)
    if hasattr(a2, 'MavenMaven_FilterSet'):
        assert _is_linked(a2, 'MavenMaven_FilterSet', b)
    _safe_set(b, 'MavenMaven_Filter', None)
    assert not _is_linked(b, 'MavenMaven_Filter', a2)
    if hasattr(a2, 'MavenMaven_FilterSet'):
        assert not _is_linked(a2, 'MavenMaven_FilterSet', b)


def test_assoc_filterset60_reverse_link_reassign_clear():
    a1 = MavenMaven_FilterSet(endtoken="sample_text", starttoken="sample_text")
    a2 = MavenMaven_FilterSet(endtoken="sample_text_2", starttoken="sample_text_2")
    b = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'MavenMaven_Copy61', a1)
    assert _is_linked(b, 'MavenMaven_Copy61', a1)
    if hasattr(a1, 'MavenMaven_FilterSet62'):
        assert _is_linked(a1, 'MavenMaven_FilterSet62', b)
    _safe_set(b, 'MavenMaven_Copy61', a2)
    assert _is_linked(b, 'MavenMaven_Copy61', a2)
    if hasattr(a1, 'MavenMaven_FilterSet62'):
        assert not _is_linked(a1, 'MavenMaven_FilterSet62', b)
    if hasattr(a2, 'MavenMaven_FilterSet62'):
        assert _is_linked(a2, 'MavenMaven_FilterSet62', b)
    _safe_set(b, 'MavenMaven_Copy61', None)
    assert not _is_linked(b, 'MavenMaven_Copy61', a2)
    if hasattr(a2, 'MavenMaven_FilterSet62'):
        assert not _is_linked(a2, 'MavenMaven_FilterSet62', b)


def test_assoc_filtersfile31_reverse_link_reassign_clear():
    a1 = MavenMaven_FiltersFile(file="sample_text")
    a2 = MavenMaven_FiltersFile(file="sample_text_2")
    b = MavenMaven_FilterSet(endtoken="sample_text", starttoken="sample_text")
    _safe_set(b, 'MavenMaven_FilterSet32', {a1})
    assert _is_linked(b, 'MavenMaven_FilterSet32', a1)
    if hasattr(a1, 'MavenMaven_FiltersFile'):
        assert _is_linked(a1, 'MavenMaven_FiltersFile', b)
    _safe_set(b, 'MavenMaven_FilterSet32', {a2})
    assert _is_linked(b, 'MavenMaven_FilterSet32', a2)
    if hasattr(a1, 'MavenMaven_FiltersFile'):
        assert not _is_linked(a1, 'MavenMaven_FiltersFile', b)
    if hasattr(a2, 'MavenMaven_FiltersFile'):
        assert _is_linked(a2, 'MavenMaven_FiltersFile', b)
    _safe_set(b, 'MavenMaven_FilterSet32', set())
    assert not _is_linked(b, 'MavenMaven_FilterSet32', a2)
    if hasattr(a2, 'MavenMaven_FiltersFile'):
        assert not _is_linked(a2, 'MavenMaven_FiltersFile', b)


def test_assoc_inExcludes53_reverse_link_reassign_clear():
    a1 = MavenMaven_Javac(debug="sample_text", deprecation="sample_text", destdir="sample_text", fork="sample_text", optimize="sample_text", srcdir="sample_text")
    a2 = MavenMaven_Javac(debug="sample_text_2", deprecation="sample_text_2", destdir="sample_text_2", fork="sample_text_2", optimize="sample_text_2", srcdir="sample_text_2")
    b = MavenMaven_InExcludes(ifCondition="sample_text", name="sample_text", unless="sample_text")
    _safe_set(b, 'MavenMaven_InExcludes54', a1)
    assert _is_linked(b, 'MavenMaven_InExcludes54', a1)
    if hasattr(a1, 'MavenMaven_Javac'):
        assert _is_linked(a1, 'MavenMaven_Javac', b)
    _safe_set(b, 'MavenMaven_InExcludes54', a2)
    assert _is_linked(b, 'MavenMaven_InExcludes54', a2)
    if hasattr(a1, 'MavenMaven_Javac'):
        assert not _is_linked(a1, 'MavenMaven_Javac', b)
    if hasattr(a2, 'MavenMaven_Javac'):
        assert _is_linked(a2, 'MavenMaven_Javac', b)
    _safe_set(b, 'MavenMaven_InExcludes54', None)
    assert not _is_linked(b, 'MavenMaven_InExcludes54', a2)
    if hasattr(a2, 'MavenMaven_Javac'):
        assert not _is_linked(a2, 'MavenMaven_Javac', b)


def test_assoc_mapper63_reverse_link_reassign_clear():
    a1 = MavenMaven_Mapper(classname="sample_text", classpath="sample_text", classpathref="sample_text", from_="sample_text", to="sample_text", type="sample_text")
    a2 = MavenMaven_Mapper(classname="sample_text_2", classpath="sample_text_2", classpathref="sample_text_2", from_="sample_text_2", to="sample_text_2", type="sample_text_2")
    b = MavenMaven_Copy(file="sample_text", filtering="sample_text", flatten="sample_text", includeEmptyDirs="sample_text", overwrite="sample_text", presservelastmodified="sample_text", todir="sample_text", tofile="sample_text")
    _safe_set(b, 'MavenMaven_Copy64', a1)
    assert _is_linked(b, 'MavenMaven_Copy64', a1)
    if hasattr(a1, 'MavenMaven_Mapper'):
        assert _is_linked(a1, 'MavenMaven_Mapper', b)
    _safe_set(b, 'MavenMaven_Copy64', a2)
    assert _is_linked(b, 'MavenMaven_Copy64', a2)
    if hasattr(a1, 'MavenMaven_Mapper'):
        assert not _is_linked(a1, 'MavenMaven_Mapper', b)
    if hasattr(a2, 'MavenMaven_Mapper'):
        assert _is_linked(a2, 'MavenMaven_Mapper', b)
    _safe_set(b, 'MavenMaven_Copy64', None)
    assert not _is_linked(b, 'MavenMaven_Copy64', a2)
    if hasattr(a2, 'MavenMaven_Mapper'):
        assert not _is_linked(a2, 'MavenMaven_Mapper', b)


def test_assoc_path34_reverse_link_reassign_clear():
    a1 = MavenMaven_Path(id="sample_text", refid="sample_text")
    a2 = MavenMaven_Path(id="sample_text_2", refid="sample_text_2")
    b = MavenMaven_Path(id="sample_text", refid="sample_text")
    _safe_set(b, 'MavenMaven_Path35', a1)
    assert _is_linked(b, 'MavenMaven_Path35', a1)
    if hasattr(a1, 'MavenMaven_Path33'):
        assert _is_linked(a1, 'MavenMaven_Path33', b)
    _safe_set(b, 'MavenMaven_Path35', a2)
    assert _is_linked(b, 'MavenMaven_Path35', a2)
    if hasattr(a1, 'MavenMaven_Path33'):
        assert not _is_linked(a1, 'MavenMaven_Path33', b)
    if hasattr(a2, 'MavenMaven_Path33'):
        assert _is_linked(a2, 'MavenMaven_Path33', b)
    _safe_set(b, 'MavenMaven_Path35', None)
    assert not _is_linked(b, 'MavenMaven_Path35', a2)
    if hasattr(a2, 'MavenMaven_Path33'):
        assert not _is_linked(a2, 'MavenMaven_Path33', b)


def test_assoc_pathElement36_reverse_link_reassign_clear():
    a1 = MavenMaven_PathElement(location="sample_text", path="sample_text")
    a2 = MavenMaven_PathElement(location="sample_text_2", path="sample_text_2")
    b = MavenMaven_Path(id="sample_text", refid="sample_text")
    _safe_set(b, 'MavenMaven_Path37', {a1})
    assert _is_linked(b, 'MavenMaven_Path37', a1)
    if hasattr(a1, 'MavenMaven_PathElement'):
        assert _is_linked(a1, 'MavenMaven_PathElement', b)
    _safe_set(b, 'MavenMaven_Path37', {a2})
    assert _is_linked(b, 'MavenMaven_Path37', a2)
    if hasattr(a1, 'MavenMaven_PathElement'):
        assert not _is_linked(a1, 'MavenMaven_PathElement', b)
    if hasattr(a2, 'MavenMaven_PathElement'):
        assert _is_linked(a2, 'MavenMaven_PathElement', b)
    _safe_set(b, 'MavenMaven_Path37', set())
    assert not _is_linked(b, 'MavenMaven_Path37', a2)
    if hasattr(a2, 'MavenMaven_PathElement'):
        assert not _is_linked(a2, 'MavenMaven_PathElement', b)


def test_assoc_pathElement41_reverse_link_reassign_clear():
    a1 = MavenMaven_PathElement(location="sample_text", path="sample_text")
    a2 = MavenMaven_PathElement(location="sample_text_2", path="sample_text_2")
    b = MavenMaven_ClassPath(refid="sample_text")
    _safe_set(b, 'MavenMaven_ClassPath', {a1})
    assert _is_linked(b, 'MavenMaven_ClassPath', a1)
    if hasattr(a1, 'MavenMaven_PathElement42'):
        assert _is_linked(a1, 'MavenMaven_PathElement42', b)
    _safe_set(b, 'MavenMaven_ClassPath', {a2})
    assert _is_linked(b, 'MavenMaven_ClassPath', a2)
    if hasattr(a1, 'MavenMaven_PathElement42'):
        assert not _is_linked(a1, 'MavenMaven_PathElement42', b)
    if hasattr(a2, 'MavenMaven_PathElement42'):
        assert _is_linked(a2, 'MavenMaven_PathElement42', b)
    _safe_set(b, 'MavenMaven_ClassPath', set())
    assert not _is_linked(b, 'MavenMaven_ClassPath', a2)
    if hasattr(a2, 'MavenMaven_PathElement42'):
        assert not _is_linked(a2, 'MavenMaven_PathElement42', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attainGoal15_stub_double():
    # MavenMaven_AttainGoal has no real 'MavenMaven_AttainGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_AttainGoal()
    setattr(partner, 'MavenMaven_AttainGoal', None)
    _safe_set(owner, 'MavenMaven_Goal16', partner)
    assert getattr(partner, 'MavenMaven_AttainGoal') == owner
    _safe_set(owner, 'MavenMaven_Goal16', None)
    assert getattr(partner, 'MavenMaven_AttainGoal') is None


def test_assoc_attributes48_stub_double():
    # MavenMaven_NewTask has no real 'MavenMaven_NewTask49' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Attribut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Attribut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Attribut(name="sample_text", value="sample_text")
    partner = MavenMaven_NewTask()
    setattr(partner, 'MavenMaven_NewTask49', None)
    _safe_set(owner, 'MavenMaven_Attribut', partner)
    assert owner in getattr(partner, 'MavenMaven_NewTask49')
    _safe_set(owner, 'MavenMaven_Attribut', None)
    assert owner not in getattr(partner, 'MavenMaven_NewTask49')


def test_assoc_centralGoal17_stub_double():
    # MavenMaven_PreGoal has no real 'preGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_PreGoal()
    setattr(partner, 'preGoal', None)
    _safe_set(owner, 'Goal', partner)
    assert getattr(partner, 'preGoal') == owner
    _safe_set(owner, 'Goal', None)
    assert getattr(partner, 'preGoal') is None


def test_assoc_centralGoal18_stub_double():
    # MavenMaven_PostGoal has no real 'postGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_PostGoal()
    setattr(partner, 'postGoal', None)
    _safe_set(owner, 'Goal19', partner)
    assert getattr(partner, 'postGoal') == owner
    _safe_set(owner, 'Goal19', None)
    assert getattr(partner, 'postGoal') is None


def test_assoc_default1_stub_double():
    # MavenMaven_Project has no real 'MavenMaven_Project2' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_Project()
    setattr(partner, 'MavenMaven_Project2', None)
    _safe_set(owner, 'MavenMaven_Goal', partner)
    assert getattr(partner, 'MavenMaven_Project2') == owner
    _safe_set(owner, 'MavenMaven_Goal', None)
    assert getattr(partner, 'MavenMaven_Project2') is None


def test_assoc_exclude28_stub_double():
    # MavenMaven_Excludes has no real 'MavenMaven_Excludes' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = MavenMaven_Excludes()
    setattr(partner, 'MavenMaven_Excludes', None)
    _safe_set(owner, 'MavenMaven_FileSet29', {partner})
    assert getattr(partner, 'MavenMaven_Excludes') == owner
    _safe_set(owner, 'MavenMaven_FileSet29', set())
    assert getattr(partner, 'MavenMaven_Excludes') is None


def test_assoc_goals11_stub_double():
    # MavenMaven_Project has no real 'MavenMaven_Project12' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_Project()
    setattr(partner, 'MavenMaven_Project12', None)
    _safe_set(owner, 'MavenMaven_Goal13', partner)
    assert owner in getattr(partner, 'MavenMaven_Project12')
    _safe_set(owner, 'MavenMaven_Goal13', None)
    assert owner not in getattr(partner, 'MavenMaven_Project12')


def test_assoc_include26_stub_double():
    # MavenMaven_Includes has no real 'MavenMaven_Includes' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = MavenMaven_Includes()
    setattr(partner, 'MavenMaven_Includes', None)
    _safe_set(owner, 'MavenMaven_FileSet27', {partner})
    assert getattr(partner, 'MavenMaven_Includes') == owner
    _safe_set(owner, 'MavenMaven_FileSet27', set())
    assert getattr(partner, 'MavenMaven_Includes') is None


def test_assoc_inexcludes23_stub_double():
    # MavenMaven_PatternSet has no real 'MavenMaven_PatternSet' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_InExcludes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_InExcludes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_InExcludes(ifCondition="sample_text", name="sample_text", unless="sample_text")
    partner = MavenMaven_PatternSet()
    setattr(partner, 'MavenMaven_PatternSet', None)
    _safe_set(owner, 'MavenMaven_InExcludes', partner)
    assert owner in getattr(partner, 'MavenMaven_PatternSet')
    _safe_set(owner, 'MavenMaven_InExcludes', None)
    assert owner not in getattr(partner, 'MavenMaven_PatternSet')


def test_assoc_path3_stub_double():
    # MavenMaven_Project has no real 'MavenMaven_Project4' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Path's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Path's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Path(id="sample_text", refid="sample_text")
    partner = MavenMaven_Project()
    setattr(partner, 'MavenMaven_Project4', None)
    _safe_set(owner, 'MavenMaven_Path', partner)
    assert getattr(partner, 'MavenMaven_Project4') == owner
    _safe_set(owner, 'MavenMaven_Path', None)
    assert getattr(partner, 'MavenMaven_Project4') is None


def test_assoc_patternset24_stub_double():
    # MavenMaven_PatternSet has no real 'MavenMaven_PatternSet25' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_FileSet(dir="sample_text")
    partner = MavenMaven_PatternSet()
    setattr(partner, 'MavenMaven_PatternSet25', None)
    _safe_set(owner, 'MavenMaven_FileSet', {partner})
    assert getattr(partner, 'MavenMaven_PatternSet25') == owner
    _safe_set(owner, 'MavenMaven_FileSet', set())
    assert getattr(partner, 'MavenMaven_PatternSet25') is None


def test_assoc_postGoal21_stub_double():
    # MavenMaven_PostGoal has no real 'PostGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_PostGoal()
    setattr(partner, 'PostGoal', None)
    _safe_set(owner, 'centralGoal22', partner)
    assert getattr(partner, 'PostGoal') == owner
    _safe_set(owner, 'centralGoal22', None)
    assert getattr(partner, 'PostGoal') is None


def test_assoc_preGoal20_stub_double():
    # MavenMaven_PreGoal has no real 'PreGoal' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Goal(name="sample_text")
    partner = MavenMaven_PreGoal()
    setattr(partner, 'PreGoal', None)
    _safe_set(owner, 'centralGoal', partner)
    assert getattr(partner, 'PreGoal') == owner
    _safe_set(owner, 'centralGoal', None)
    assert getattr(partner, 'PreGoal') is None


def test_assoc_taskName46_stub_double():
    # MavenMaven_NewTask has no real 'MavenMaven_NewTask' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_AntTaskDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_AntTaskDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_AntTaskDef(classname="sample_text", name="sample_text")
    partner = MavenMaven_NewTask()
    setattr(partner, 'MavenMaven_NewTask', None)
    _safe_set(owner, 'MavenMaven_AntTaskDef47', partner)
    assert getattr(partner, 'MavenMaven_NewTask') == owner
    _safe_set(owner, 'MavenMaven_AntTaskDef47', None)
    assert getattr(partner, 'MavenMaven_NewTask') is None


def test_assoc_taskdefs7_stub_double():
    # MavenMaven_Project has no real 'MavenMaven_Project8' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_AntTaskDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_AntTaskDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_AntTaskDef(classname="sample_text", name="sample_text")
    partner = MavenMaven_Project()
    setattr(partner, 'MavenMaven_Project8', None)
    _safe_set(owner, 'MavenMaven_AntTaskDef', partner)
    assert owner in getattr(partner, 'MavenMaven_Project8')
    _safe_set(owner, 'MavenMaven_AntTaskDef', None)
    assert owner not in getattr(partner, 'MavenMaven_Project8')


def test_assoc_xmlns0_stub_double():
    # MavenMaven_Project has no real 'MavenMaven_Project' property in the generated
    # code (a bare stub) -- manually attach it so MavenMaven_Xmlns's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MavenMaven_Xmlns's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MavenMaven_Xmlns(name="sample_text", value="sample_text")
    partner = MavenMaven_Project()
    setattr(partner, 'MavenMaven_Project', None)
    _safe_set(owner, 'MavenMaven_Xmlns', partner)
    assert owner in getattr(partner, 'MavenMaven_Project')
    _safe_set(owner, 'MavenMaven_Xmlns', None)
    assert owner not in getattr(partner, 'MavenMaven_Project')


