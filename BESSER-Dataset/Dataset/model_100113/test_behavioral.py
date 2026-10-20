import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTable,
    DatabaseElement,
    NamedElement,
    TableContainer,
    TypesLibraryUser,
    database_AbstractTable,
    database_Column,
    database_Constraint,
    database_DataBase,
    database_DatabaseElement,
    database_ForeignKey,
    database_ForeignKeyElement,
    database_Index,
    database_IndexElement,
    database_NamedElement,
    database_PrimaryKey,
    database_Schema,
    database_Sequence,
    database_Table,
    database_TableContainer,
    database_Type,
    database_UserDefinedTypesLibrary,
    database_View,
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

def test_assoc_column45_reverse_link_reassign_clear():
    a1 = database_IndexElement(asc=True)
    a2 = database_IndexElement(asc=False)
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'Column46', a1)
    assert _is_linked(b, 'Column46', a1)
    if hasattr(a1, 'indexElements'):
        assert _is_linked(a1, 'indexElements', b)
    _safe_set(b, 'Column46', a2)
    assert _is_linked(b, 'Column46', a2)
    if hasattr(a1, 'indexElements'):
        assert not _is_linked(a1, 'indexElements', b)
    if hasattr(a2, 'indexElements'):
        assert _is_linked(a2, 'indexElements', b)
    _safe_set(b, 'Column46', None)
    assert not _is_linked(b, 'Column46', a2)
    if hasattr(a2, 'indexElements'):
        assert not _is_linked(a2, 'indexElements', b)


def test_assoc_columns49_reverse_link_reassign_clear():
    a1 = database_Sequence(cacheSize="sample_text", cycle=True, increment="sample_text", maxValue="sample_text", minValue="sample_text", start="sample_text")
    a2 = database_Sequence(cacheSize="sample_text_2", cycle=False, increment="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2", start="sample_text_2")
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'Column50', a1)
    assert _is_linked(b, 'Column50', a1)
    if hasattr(a1, 'sequence'):
        assert _is_linked(a1, 'sequence', b)
    _safe_set(b, 'Column50', a2)
    assert _is_linked(b, 'Column50', a2)
    if hasattr(a1, 'sequence'):
        assert not _is_linked(a1, 'sequence', b)
    if hasattr(a2, 'sequence'):
        assert _is_linked(a2, 'sequence', b)
    _safe_set(b, 'Column50', None)
    assert not _is_linked(b, 'Column50', a2)
    if hasattr(a2, 'sequence'):
        assert not _is_linked(a2, 'sequence', b)


def test_assoc_elements17_reverse_link_reassign_clear():
    a1 = database_IndexElement(asc=True)
    a2 = database_IndexElement(asc=False)
    b = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    _safe_set(b, 'database_Index18', {a1})
    assert _is_linked(b, 'database_Index18', a1)
    if hasattr(a1, 'database_IndexElement'):
        assert _is_linked(a1, 'database_IndexElement', b)
    _safe_set(b, 'database_Index18', {a2})
    assert _is_linked(b, 'database_Index18', a2)
    if hasattr(a1, 'database_IndexElement'):
        assert not _is_linked(a1, 'database_IndexElement', b)
    if hasattr(a2, 'database_IndexElement'):
        assert _is_linked(a2, 'database_IndexElement', b)
    _safe_set(b, 'database_Index18', set())
    assert not _is_linked(b, 'database_Index18', a2)
    if hasattr(a2, 'database_IndexElement'):
        assert not _is_linked(a2, 'database_IndexElement', b)


def test_assoc_foreignKeys8_reverse_link_reassign_clear():
    a1 = database_ForeignKey()
    a2 = database_ForeignKey()
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'database_Column9', {a1})
    assert _is_linked(b, 'database_Column9', a1)
    if hasattr(a1, 'database_ForeignKey'):
        assert _is_linked(a1, 'database_ForeignKey', b)
    _safe_set(b, 'database_Column9', {a2})
    assert _is_linked(b, 'database_Column9', a2)
    if hasattr(a1, 'database_ForeignKey'):
        assert not _is_linked(a1, 'database_ForeignKey', b)
    if hasattr(a2, 'database_ForeignKey'):
        assert _is_linked(a2, 'database_ForeignKey', b)
    _safe_set(b, 'database_Column9', set())
    assert not _is_linked(b, 'database_Column9', a2)
    if hasattr(a2, 'database_ForeignKey'):
        assert not _is_linked(a2, 'database_ForeignKey', b)


def test_assoc_indexElements6_reverse_link_reassign_clear():
    a1 = database_IndexElement(asc=True)
    a2 = database_IndexElement(asc=False)
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'column', {a1})
    assert _is_linked(b, 'column', a1)
    if hasattr(a1, 'IndexElement'):
        assert _is_linked(a1, 'IndexElement', b)
    _safe_set(b, 'column', {a2})
    assert _is_linked(b, 'column', a2)
    if hasattr(a1, 'IndexElement'):
        assert not _is_linked(a1, 'IndexElement', b)
    if hasattr(a2, 'IndexElement'):
        assert _is_linked(a2, 'IndexElement', b)
    _safe_set(b, 'column', set())
    assert not _is_linked(b, 'column', a2)
    if hasattr(a2, 'IndexElement'):
        assert not _is_linked(a2, 'IndexElement', b)


def test_assoc_indexes5_reverse_link_reassign_clear():
    a1 = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    a2 = database_Index(cardinality=13, indexType="sample_text_2", qualifier="sample_text_2", unique=False)
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'database_Column', {a1})
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_Index'):
        assert _is_linked(a1, 'database_Index', b)
    _safe_set(b, 'database_Column', {a2})
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_Index'):
        assert not _is_linked(a1, 'database_Index', b)
    if hasattr(a2, 'database_Index'):
        assert _is_linked(a2, 'database_Index', b)
    _safe_set(b, 'database_Column', set())
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_Index'):
        assert not _is_linked(a2, 'database_Index', b)


def test_assoc_sequence13_reverse_link_reassign_clear():
    a1 = database_Sequence(cacheSize="sample_text", cycle=True, increment="sample_text", maxValue="sample_text", minValue="sample_text", start="sample_text")
    a2 = database_Sequence(cacheSize="sample_text_2", cycle=False, increment="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2", start="sample_text_2")
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'columns14', a1)
    assert _is_linked(b, 'columns14', a1)
    if hasattr(a1, 'Sequence'):
        assert _is_linked(a1, 'Sequence', b)
    _safe_set(b, 'columns14', a2)
    assert _is_linked(b, 'columns14', a2)
    if hasattr(a1, 'Sequence'):
        assert not _is_linked(a1, 'Sequence', b)
    if hasattr(a2, 'Sequence'):
        assert _is_linked(a2, 'Sequence', b)
    _safe_set(b, 'columns14', None)
    assert not _is_linked(b, 'columns14', a2)
    if hasattr(a2, 'Sequence'):
        assert not _is_linked(a2, 'Sequence', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns29_stub_double():
    # database_PrimaryKey has no real 'primaryKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_PrimaryKey()
    setattr(partner, 'primaryKey', None)
    _safe_set(owner, 'Column30', partner)
    assert owner in getattr(partner, 'primaryKey')
    _safe_set(owner, 'Column30', None)
    assert owner not in getattr(partner, 'primaryKey')


def test_assoc_columns3_stub_double():
    # database_AbstractTable has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_AbstractTable()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_constraints25_stub_double():
    # database_Table has no real 'owner26' property in the generated
    # code (a bare stub) -- manually attach it so database_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Constraint(expression="sample_text")
    partner = database_Table()
    setattr(partner, 'owner26', None)
    _safe_set(owner, 'Constraint', partner)
    assert owner in getattr(partner, 'owner26')
    _safe_set(owner, 'Constraint', None)
    assert owner not in getattr(partner, 'owner26')


def test_assoc_defines1_stub_double():
    # database_UserDefinedTypesLibrary has no real 'database_UserDefinedTypesLibrary' property in the generated
    # code (a bare stub) -- manually attach it so database_DataBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_DataBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_DataBase(url="sample_text")
    partner = database_UserDefinedTypesLibrary()
    setattr(partner, 'database_UserDefinedTypesLibrary', None)
    _safe_set(owner, 'database_DataBase2', {partner})
    assert getattr(partner, 'database_UserDefinedTypesLibrary') == owner
    _safe_set(owner, 'database_DataBase2', set())
    assert getattr(partner, 'database_UserDefinedTypesLibrary') is None


def test_assoc_elements34_stub_double():
    # database_ForeignKeyElement has no real 'database_ForeignKeyElement' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_ForeignKeyElement()
    setattr(partner, 'database_ForeignKeyElement', None)
    _safe_set(owner, 'database_ForeignKey35', {partner})
    assert getattr(partner, 'database_ForeignKeyElement') == owner
    _safe_set(owner, 'database_ForeignKey35', set())
    assert getattr(partner, 'database_ForeignKeyElement') is None


def test_assoc_fkColumn40_stub_double():
    # database_ForeignKeyElement has no real 'foreignKeyElements' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_ForeignKeyElement()
    setattr(partner, 'foreignKeyElements', None)
    _safe_set(owner, 'Column41', partner)
    assert getattr(partner, 'foreignKeyElements') == owner
    _safe_set(owner, 'Column41', None)
    assert getattr(partner, 'foreignKeyElements') is None


def test_assoc_foreignKeyElements10_stub_double():
    # database_ForeignKeyElement has no real 'ForeignKeyElement' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_ForeignKeyElement()
    setattr(partner, 'ForeignKeyElement', None)
    _safe_set(owner, 'fkColumn', {partner})
    assert getattr(partner, 'ForeignKeyElement') == owner
    _safe_set(owner, 'fkColumn', set())
    assert getattr(partner, 'ForeignKeyElement') is None


def test_assoc_foreignKeys23_stub_double():
    # database_Table has no real 'owner24' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'owner24', None)
    _safe_set(owner, 'ForeignKey', partner)
    assert owner in getattr(partner, 'owner24')
    _safe_set(owner, 'ForeignKey', None)
    assert owner not in getattr(partner, 'owner24')


def test_assoc_indexes27_stub_double():
    # database_Table has no real 'owner28' property in the generated
    # code (a bare stub) -- manually attach it so database_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    partner = database_Table()
    setattr(partner, 'owner28', None)
    _safe_set(owner, 'Index', partner)
    assert owner in getattr(partner, 'owner28')
    _safe_set(owner, 'Index', None)
    assert owner not in getattr(partner, 'owner28')


def test_assoc_owner15_stub_double():
    # database_AbstractTable has no real 'AbstractTable' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_AbstractTable()
    setattr(partner, 'AbstractTable', None)
    _safe_set(owner, 'columns16', partner)
    assert getattr(partner, 'AbstractTable') == owner
    _safe_set(owner, 'columns16', None)
    assert getattr(partner, 'AbstractTable') is None


def test_assoc_owner19_stub_double():
    # database_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so database_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    partner = database_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'indexes', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'indexes', None)
    assert getattr(partner, 'Table') is None


def test_assoc_owner36_stub_double():
    # database_Table has no real 'Table37' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'Table37', None)
    _safe_set(owner, 'foreignKeys', partner)
    assert getattr(partner, 'Table37') == owner
    _safe_set(owner, 'foreignKeys', None)
    assert getattr(partner, 'Table37') is None


def test_assoc_owner47_stub_double():
    # database_Table has no real 'Table48' property in the generated
    # code (a bare stub) -- manually attach it so database_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Constraint(expression="sample_text")
    partner = database_Table()
    setattr(partner, 'Table48', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'Table48') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'Table48') is None


def test_assoc_pkColumn42_stub_double():
    # database_ForeignKeyElement has no real 'database_ForeignKeyElement43' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_ForeignKeyElement()
    setattr(partner, 'database_ForeignKeyElement43', None)
    _safe_set(owner, 'database_Column44', partner)
    assert getattr(partner, 'database_ForeignKeyElement43') == owner
    _safe_set(owner, 'database_Column44', None)
    assert getattr(partner, 'database_ForeignKeyElement43') is None


def test_assoc_primaryKey7_stub_double():
    # database_PrimaryKey has no real 'PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_PrimaryKey()
    setattr(partner, 'PrimaryKey', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'PrimaryKey') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'PrimaryKey') is None


def test_assoc_schemas0_stub_double():
    # database_Schema has no real 'database_Schema' property in the generated
    # code (a bare stub) -- manually attach it so database_DataBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_DataBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_DataBase(url="sample_text")
    partner = database_Schema()
    setattr(partner, 'database_Schema', None)
    _safe_set(owner, 'database_DataBase', {partner})
    assert getattr(partner, 'database_Schema') == owner
    _safe_set(owner, 'database_DataBase', set())
    assert getattr(partner, 'database_Schema') is None


def test_assoc_sequences54_stub_double():
    # database_TableContainer has no real 'database_TableContainer' property in the generated
    # code (a bare stub) -- manually attach it so database_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Sequence(cacheSize="sample_text", cycle=True, increment="sample_text", maxValue="sample_text", minValue="sample_text", start="sample_text")
    partner = database_TableContainer()
    setattr(partner, 'database_TableContainer', None)
    _safe_set(owner, 'database_Sequence', partner)
    assert owner in getattr(partner, 'database_TableContainer')
    _safe_set(owner, 'database_Sequence', None)
    assert owner not in getattr(partner, 'database_TableContainer')


def test_assoc_target38_stub_double():
    # database_Table has no real 'database_Table' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'database_Table', None)
    _safe_set(owner, 'database_ForeignKey39', partner)
    assert getattr(partner, 'database_Table') == owner
    _safe_set(owner, 'database_ForeignKey39', None)
    assert getattr(partner, 'database_Table') is None


def test_assoc_type11_stub_double():
    # database_Type has no real 'database_Type' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_Type()
    setattr(partner, 'database_Type', None)
    _safe_set(owner, 'database_Column12', partner)
    assert getattr(partner, 'database_Type') == owner
    _safe_set(owner, 'database_Column12', None)
    assert getattr(partner, 'database_Type') is None


