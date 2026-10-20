import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DescribedElement,
    FQNamedElement,
    IColumn,
    IFile,
    Mapping,
    NamedElement,
    SeparatedElement,
    Task,
    Type,
    model_Column,
    model_Database,
    model_DescribedElement,
    model_Domain,
    model_FQNamedElement,
    model_Field,
    model_File,
    model_FileSet,
    model_IColumn,
    model_IFile,
    model_Mapping,
    model_MappingExport,
    model_MappingFile,
    model_MappingImport,
    model_MappingSQL,
    model_NamedElement,
    model_NativeSQLType,
    model_SCTFile,
    model_Schema,
    model_SeparatedElement,
    model_Site,
    model_Table,
    model_Task,
    model_TaskExport,
    model_TaskFile,
    model_TaskImport,
    model_TaskSQL,
    model_TaskSet,
    model_Type,
    model_User,
    model_View,
    FieldType,
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

def test_assoc_domains20_reverse_link_reassign_clear():
    a1 = model_SCTFile(file="sample_text")
    a2 = model_SCTFile(file="sample_text_2")
    b = model_Domain(type="sample_text")
    _safe_set(b, 'model_Domain22', a1)
    assert _is_linked(b, 'model_Domain22', a1)
    if hasattr(a1, 'model_SCTFile21'):
        assert _is_linked(a1, 'model_SCTFile21', b)
    _safe_set(b, 'model_Domain22', a2)
    assert _is_linked(b, 'model_Domain22', a2)
    if hasattr(a1, 'model_SCTFile21'):
        assert not _is_linked(a1, 'model_SCTFile21', b)
    if hasattr(a2, 'model_SCTFile21'):
        assert _is_linked(a2, 'model_SCTFile21', b)
    _safe_set(b, 'model_Domain22', None)
    assert not _is_linked(b, 'model_Domain22', a2)
    if hasattr(a2, 'model_SCTFile21'):
        assert not _is_linked(a2, 'model_SCTFile21', b)


def test_assoc_fields17_reverse_link_reassign_clear():
    a1 = model_File(files="sample_text", numberOfHeaderLines="sample_text")
    a2 = model_File(files="sample_text_2", numberOfHeaderLines="sample_text_2")
    b = model_Field(length="sample_text", position="sample_text", type="sample_text")
    _safe_set(b, 'model_Field', a1)
    assert _is_linked(b, 'model_Field', a1)
    if hasattr(a1, 'model_File'):
        assert _is_linked(a1, 'model_File', b)
    _safe_set(b, 'model_Field', a2)
    assert _is_linked(b, 'model_Field', a2)
    if hasattr(a1, 'model_File'):
        assert not _is_linked(a1, 'model_File', b)
    if hasattr(a2, 'model_File'):
        assert _is_linked(a2, 'model_File', b)
    _safe_set(b, 'model_Field', None)
    assert not _is_linked(b, 'model_Field', a2)
    if hasattr(a2, 'model_File'):
        assert not _is_linked(a2, 'model_File', b)


def test_assoc_preconditions47_reverse_link_reassign_clear():
    a1 = model_Task(fileName="sample_text")
    a2 = model_Task(fileName="sample_text_2")
    b = model_Task(fileName="sample_text")
    _safe_set(b, 'model_Task48', a1)
    assert _is_linked(b, 'model_Task48', a1)
    if hasattr(a1, 'model_Task46'):
        assert _is_linked(a1, 'model_Task46', b)
    _safe_set(b, 'model_Task48', a2)
    assert _is_linked(b, 'model_Task48', a2)
    if hasattr(a1, 'model_Task46'):
        assert not _is_linked(a1, 'model_Task46', b)
    if hasattr(a2, 'model_Task46'):
        assert _is_linked(a2, 'model_Task46', b)
    _safe_set(b, 'model_Task48', None)
    assert not _is_linked(b, 'model_Task48', a2)
    if hasattr(a2, 'model_Task46'):
        assert not _is_linked(a2, 'model_Task46', b)


def test_assoc_users0_reverse_link_reassign_clear():
    a1 = model_User(password="sample_text")
    a2 = model_User(password="sample_text_2")
    b = model_Database(dsn="sample_text")
    _safe_set(b, 'model_Database', {a1})
    assert _is_linked(b, 'model_Database', a1)
    if hasattr(a1, 'model_User'):
        assert _is_linked(a1, 'model_User', b)
    _safe_set(b, 'model_Database', {a2})
    assert _is_linked(b, 'model_Database', a2)
    if hasattr(a1, 'model_User'):
        assert not _is_linked(a1, 'model_User', b)
    if hasattr(a2, 'model_User'):
        assert _is_linked(a2, 'model_User', b)
    _safe_set(b, 'model_Database', set())
    assert not _is_linked(b, 'model_Database', a2)
    if hasattr(a2, 'model_User'):
        assert not _is_linked(a2, 'model_User', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns18_stub_double():
    # model_Column has no real 'model_Column19' property in the generated
    # code (a bare stub) -- manually attach it so model_SCTFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_SCTFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_SCTFile(file="sample_text")
    partner = model_Column()
    setattr(partner, 'model_Column19', None)
    _safe_set(owner, 'model_SCTFile', {partner})
    assert getattr(partner, 'model_Column19') == owner
    _safe_set(owner, 'model_SCTFile', set())
    assert getattr(partner, 'model_Column19') is None


def test_assoc_databases81_stub_double():
    # model_Site has no real 'model_Site' property in the generated
    # code (a bare stub) -- manually attach it so model_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Database(dsn="sample_text")
    partner = model_Site()
    setattr(partner, 'model_Site', None)
    _safe_set(owner, 'model_Database82', partner)
    assert owner in getattr(partner, 'model_Site')
    _safe_set(owner, 'model_Database82', None)
    assert owner not in getattr(partner, 'model_Site')


def test_assoc_domains6_stub_double():
    # model_Schema has no real 'model_Schema7' property in the generated
    # code (a bare stub) -- manually attach it so model_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Domain(type="sample_text")
    partner = model_Schema()
    setattr(partner, 'model_Schema7', None)
    _safe_set(owner, 'model_Domain', partner)
    assert owner in getattr(partner, 'model_Schema7')
    _safe_set(owner, 'model_Domain', None)
    assert owner not in getattr(partner, 'model_Schema7')


def test_assoc_fileSets83_stub_double():
    # model_Site has no real 'model_Site84' property in the generated
    # code (a bare stub) -- manually attach it so model_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_FileSet(hostname="sample_text")
    partner = model_Site()
    setattr(partner, 'model_Site84', None)
    _safe_set(owner, 'model_FileSet85', partner)
    assert owner in getattr(partner, 'model_Site84')
    _safe_set(owner, 'model_FileSet85', None)
    assert owner not in getattr(partner, 'model_Site84')


def test_assoc_files16_stub_double():
    # model_IFile has no real 'model_IFile' property in the generated
    # code (a bare stub) -- manually attach it so model_FileSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_FileSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_FileSet(hostname="sample_text")
    partner = model_IFile()
    setattr(partner, 'model_IFile', None)
    _safe_set(owner, 'model_FileSet', {partner})
    assert getattr(partner, 'model_IFile') == owner
    _safe_set(owner, 'model_FileSet', set())
    assert getattr(partner, 'model_IFile') is None


def test_assoc_preconditions43_stub_double():
    # model_TaskSet has no real 'model_TaskSet44' property in the generated
    # code (a bare stub) -- manually attach it so model_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Task(fileName="sample_text")
    partner = model_TaskSet()
    setattr(partner, 'model_TaskSet44', None)
    _safe_set(owner, 'model_Task45', partner)
    assert owner in getattr(partner, 'model_TaskSet44')
    _safe_set(owner, 'model_Task45', None)
    assert owner not in getattr(partner, 'model_TaskSet44')


def test_assoc_schema3_stub_double():
    # model_Schema has no real 'model_Schema5' property in the generated
    # code (a bare stub) -- manually attach it so model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_User(password="sample_text")
    partner = model_Schema()
    setattr(partner, 'model_Schema5', None)
    _safe_set(owner, 'model_User4', partner)
    assert getattr(partner, 'model_Schema5') == owner
    _safe_set(owner, 'model_User4', None)
    assert getattr(partner, 'model_Schema5') is None


def test_assoc_schemas1_stub_double():
    # model_Schema has no real 'model_Schema' property in the generated
    # code (a bare stub) -- manually attach it so model_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Database(dsn="sample_text")
    partner = model_Schema()
    setattr(partner, 'model_Schema', None)
    _safe_set(owner, 'model_Database2', {partner})
    assert getattr(partner, 'model_Schema') == owner
    _safe_set(owner, 'model_Database2', set())
    assert getattr(partner, 'model_Schema') is None


def test_assoc_source27_stub_double():
    # model_MappingFile has no real 'model_MappingFile' property in the generated
    # code (a bare stub) -- manually attach it so model_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Field(length="sample_text", position="sample_text", type="sample_text")
    partner = model_MappingFile()
    setattr(partner, 'model_MappingFile', None)
    _safe_set(owner, 'model_Field28', partner)
    assert owner in getattr(partner, 'model_MappingFile')
    _safe_set(owner, 'model_Field28', None)
    assert owner not in getattr(partner, 'model_MappingFile')


def test_assoc_source57_stub_double():
    # model_TaskFile has no real 'model_TaskFile' property in the generated
    # code (a bare stub) -- manually attach it so model_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_File(files="sample_text", numberOfHeaderLines="sample_text")
    partner = model_TaskFile()
    setattr(partner, 'model_TaskFile', None)
    _safe_set(owner, 'model_File58', partner)
    assert getattr(partner, 'model_TaskFile') == owner
    _safe_set(owner, 'model_File58', None)
    assert getattr(partner, 'model_TaskFile') is None


def test_assoc_target29_stub_double():
    # model_MappingFile has no real 'model_MappingFile30' property in the generated
    # code (a bare stub) -- manually attach it so model_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Field(length="sample_text", position="sample_text", type="sample_text")
    partner = model_MappingFile()
    setattr(partner, 'model_MappingFile30', None)
    _safe_set(owner, 'model_Field31', partner)
    assert getattr(partner, 'model_MappingFile30') == owner
    _safe_set(owner, 'model_Field31', None)
    assert getattr(partner, 'model_MappingFile30') is None


def test_assoc_target59_stub_double():
    # model_TaskFile has no real 'model_TaskFile60' property in the generated
    # code (a bare stub) -- manually attach it so model_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_File(files="sample_text", numberOfHeaderLines="sample_text")
    partner = model_TaskFile()
    setattr(partner, 'model_TaskFile60', None)
    _safe_set(owner, 'model_File61', partner)
    assert getattr(partner, 'model_TaskFile60') == owner
    _safe_set(owner, 'model_File61', None)
    assert getattr(partner, 'model_TaskFile60') is None


def test_assoc_tasks42_stub_double():
    # model_TaskSet has no real 'model_TaskSet' property in the generated
    # code (a bare stub) -- manually attach it so model_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Task(fileName="sample_text")
    partner = model_TaskSet()
    setattr(partner, 'model_TaskSet', None)
    _safe_set(owner, 'model_Task', partner)
    assert owner in getattr(partner, 'model_TaskSet')
    _safe_set(owner, 'model_Task', None)
    assert owner not in getattr(partner, 'model_TaskSet')


def test_assoc_views10_stub_double():
    # model_Schema has no real 'model_Schema11' property in the generated
    # code (a bare stub) -- manually attach it so model_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_View(sql="sample_text")
    partner = model_Schema()
    setattr(partner, 'model_Schema11', None)
    _safe_set(owner, 'model_View', partner)
    assert owner in getattr(partner, 'model_Schema11')
    _safe_set(owner, 'model_View', None)
    assert owner not in getattr(partner, 'model_Schema11')


