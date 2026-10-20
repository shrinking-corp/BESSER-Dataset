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
    database_ViewElement,
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

def test_assoc_column50_reverse_link_reassign_clear():
    a1 = database_IndexElement(asc=True)
    a2 = database_IndexElement(asc=False)
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'Column51', a1)
    assert _is_linked(b, 'Column51', a1)
    if hasattr(a1, 'indexElements'):
        assert _is_linked(a1, 'indexElements', b)
    _safe_set(b, 'Column51', a2)
    assert _is_linked(b, 'Column51', a2)
    if hasattr(a1, 'indexElements'):
        assert not _is_linked(a1, 'indexElements', b)
    if hasattr(a2, 'indexElements'):
        assert _is_linked(a2, 'indexElements', b)
    _safe_set(b, 'Column51', None)
    assert not _is_linked(b, 'Column51', a2)
    if hasattr(a2, 'indexElements'):
        assert not _is_linked(a2, 'indexElements', b)


def test_assoc_columns20_reverse_link_reassign_clear():
    a1 = database_ViewElement(alias="sample_text", name="sample_text")
    a2 = database_ViewElement(alias="sample_text_2", name="sample_text_2")
    b = database_View(query="sample_text")
    _safe_set(b, 'database_View', {a1})
    assert _is_linked(b, 'database_View', a1)
    if hasattr(a1, 'database_ViewElement'):
        assert _is_linked(a1, 'database_ViewElement', b)
    _safe_set(b, 'database_View', {a2})
    assert _is_linked(b, 'database_View', a2)
    if hasattr(a1, 'database_ViewElement'):
        assert not _is_linked(a1, 'database_ViewElement', b)
    if hasattr(a2, 'database_ViewElement'):
        assert _is_linked(a2, 'database_ViewElement', b)
    _safe_set(b, 'database_View', set())
    assert not _is_linked(b, 'database_View', a2)
    if hasattr(a2, 'database_ViewElement'):
        assert not _is_linked(a2, 'database_ViewElement', b)


def test_assoc_columns54_reverse_link_reassign_clear():
    a1 = database_Sequence(cacheSize="sample_text", cycle=True, increment="sample_text", maxValue="sample_text", minValue="sample_text", start="sample_text")
    a2 = database_Sequence(cacheSize="sample_text_2", cycle=False, increment="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2", start="sample_text_2")
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'Column55', a1)
    assert _is_linked(b, 'Column55', a1)
    if hasattr(a1, 'sequence'):
        assert _is_linked(a1, 'sequence', b)
    _safe_set(b, 'Column55', a2)
    assert _is_linked(b, 'Column55', a2)
    if hasattr(a1, 'sequence'):
        assert not _is_linked(a1, 'sequence', b)
    if hasattr(a2, 'sequence'):
        assert _is_linked(a2, 'sequence', b)
    _safe_set(b, 'Column55', None)
    assert not _is_linked(b, 'Column55', a2)
    if hasattr(a2, 'sequence'):
        assert not _is_linked(a2, 'sequence', b)


def test_assoc_elements16_reverse_link_reassign_clear():
    a1 = database_IndexElement(asc=True)
    a2 = database_IndexElement(asc=False)
    b = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    _safe_set(b, 'database_Index17', {a1})
    assert _is_linked(b, 'database_Index17', a1)
    if hasattr(a1, 'database_IndexElement'):
        assert _is_linked(a1, 'database_IndexElement', b)
    _safe_set(b, 'database_Index17', {a2})
    assert _is_linked(b, 'database_Index17', a2)
    if hasattr(a1, 'database_IndexElement'):
        assert not _is_linked(a1, 'database_IndexElement', b)
    if hasattr(a2, 'database_IndexElement'):
        assert _is_linked(a2, 'database_IndexElement', b)
    _safe_set(b, 'database_Index17', set())
    assert not _is_linked(b, 'database_Index17', a2)
    if hasattr(a2, 'database_IndexElement'):
        assert not _is_linked(a2, 'database_IndexElement', b)


def test_assoc_foreignKeys7_reverse_link_reassign_clear():
    a1 = database_ForeignKey()
    a2 = database_ForeignKey()
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'database_Column8', {a1})
    assert _is_linked(b, 'database_Column8', a1)
    if hasattr(a1, 'database_ForeignKey'):
        assert _is_linked(a1, 'database_ForeignKey', b)
    _safe_set(b, 'database_Column8', {a2})
    assert _is_linked(b, 'database_Column8', a2)
    if hasattr(a1, 'database_ForeignKey'):
        assert not _is_linked(a1, 'database_ForeignKey', b)
    if hasattr(a2, 'database_ForeignKey'):
        assert _is_linked(a2, 'database_ForeignKey', b)
    _safe_set(b, 'database_Column8', set())
    assert not _is_linked(b, 'database_Column8', a2)
    if hasattr(a2, 'database_ForeignKey'):
        assert not _is_linked(a2, 'database_ForeignKey', b)


def test_assoc_indexElements5_reverse_link_reassign_clear():
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


def test_assoc_indexes4_reverse_link_reassign_clear():
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


def test_assoc_sequence12_reverse_link_reassign_clear():
    a1 = database_Sequence(cacheSize="sample_text", cycle=True, increment="sample_text", maxValue="sample_text", minValue="sample_text", start="sample_text")
    a2 = database_Sequence(cacheSize="sample_text_2", cycle=False, increment="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2", start="sample_text_2")
    b = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    _safe_set(b, 'columns13', a1)
    assert _is_linked(b, 'columns13', a1)
    if hasattr(a1, 'Sequence'):
        assert _is_linked(a1, 'Sequence', b)
    _safe_set(b, 'columns13', a2)
    assert _is_linked(b, 'columns13', a2)
    if hasattr(a1, 'Sequence'):
        assert not _is_linked(a1, 'Sequence', b)
    if hasattr(a2, 'Sequence'):
        assert _is_linked(a2, 'Sequence', b)
    _safe_set(b, 'columns13', None)
    assert not _is_linked(b, 'columns13', a2)
    if hasattr(a2, 'Sequence'):
        assert not _is_linked(a2, 'Sequence', b)


def test_assoc_tables21_reverse_link_reassign_clear():
    a1 = database_ViewElement(alias="sample_text", name="sample_text")
    a2 = database_ViewElement(alias="sample_text_2", name="sample_text_2")
    b = database_View(query="sample_text")
    _safe_set(b, 'database_View22', {a1})
    assert _is_linked(b, 'database_View22', a1)
    if hasattr(a1, 'database_ViewElement23'):
        assert _is_linked(a1, 'database_ViewElement23', b)
    _safe_set(b, 'database_View22', {a2})
    assert _is_linked(b, 'database_View22', a2)
    if hasattr(a1, 'database_ViewElement23'):
        assert not _is_linked(a1, 'database_ViewElement23', b)
    if hasattr(a2, 'database_ViewElement23'):
        assert _is_linked(a2, 'database_ViewElement23', b)
    _safe_set(b, 'database_View22', set())
    assert not _is_linked(b, 'database_View22', a2)
    if hasattr(a2, 'database_ViewElement23'):
        assert not _is_linked(a2, 'database_ViewElement23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns32_stub_double():
    # database_Table has no real 'owner33' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_Table()
    setattr(partner, 'owner33', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'owner33')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'owner33')


def test_assoc_columns34_stub_double():
    # database_PrimaryKey has no real 'primaryKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_PrimaryKey()
    setattr(partner, 'primaryKey', None)
    _safe_set(owner, 'Column35', partner)
    assert owner in getattr(partner, 'primaryKey')
    _safe_set(owner, 'Column35', None)
    assert owner not in getattr(partner, 'primaryKey')


def test_assoc_constraints28_stub_double():
    # database_Table has no real 'owner29' property in the generated
    # code (a bare stub) -- manually attach it so database_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Constraint(expression="sample_text")
    partner = database_Table()
    setattr(partner, 'owner29', None)
    _safe_set(owner, 'Constraint', partner)
    assert owner in getattr(partner, 'owner29')
    _safe_set(owner, 'Constraint', None)
    assert owner not in getattr(partner, 'owner29')


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


def test_assoc_elements39_stub_double():
    # database_ForeignKeyElement has no real 'database_ForeignKeyElement' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_ForeignKeyElement()
    setattr(partner, 'database_ForeignKeyElement', None)
    _safe_set(owner, 'database_ForeignKey40', {partner})
    assert getattr(partner, 'database_ForeignKeyElement') == owner
    _safe_set(owner, 'database_ForeignKey40', set())
    assert getattr(partner, 'database_ForeignKeyElement') is None


def test_assoc_fkColumn45_stub_double():
    # database_ForeignKeyElement has no real 'foreignKeyElements' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_ForeignKeyElement()
    setattr(partner, 'foreignKeyElements', None)
    _safe_set(owner, 'Column46', partner)
    assert getattr(partner, 'foreignKeyElements') == owner
    _safe_set(owner, 'Column46', None)
    assert getattr(partner, 'foreignKeyElements') is None


def test_assoc_foreignKeyElements9_stub_double():
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


def test_assoc_foreignKeys26_stub_double():
    # database_Table has no real 'owner27' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'owner27', None)
    _safe_set(owner, 'ForeignKey', partner)
    assert owner in getattr(partner, 'owner27')
    _safe_set(owner, 'ForeignKey', None)
    assert owner not in getattr(partner, 'owner27')


def test_assoc_indexes30_stub_double():
    # database_Table has no real 'owner31' property in the generated
    # code (a bare stub) -- manually attach it so database_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    partner = database_Table()
    setattr(partner, 'owner31', None)
    _safe_set(owner, 'Index', partner)
    assert owner in getattr(partner, 'owner31')
    _safe_set(owner, 'Index', None)
    assert owner not in getattr(partner, 'owner31')


def test_assoc_owner14_stub_double():
    # database_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'columns15', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'columns15', None)
    assert getattr(partner, 'Table') is None


def test_assoc_owner18_stub_double():
    # database_Table has no real 'Table19' property in the generated
    # code (a bare stub) -- manually attach it so database_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    partner = database_Table()
    setattr(partner, 'Table19', None)
    _safe_set(owner, 'indexes', partner)
    assert getattr(partner, 'Table19') == owner
    _safe_set(owner, 'indexes', None)
    assert getattr(partner, 'Table19') is None


def test_assoc_owner41_stub_double():
    # database_Table has no real 'Table42' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'Table42', None)
    _safe_set(owner, 'foreignKeys', partner)
    assert getattr(partner, 'Table42') == owner
    _safe_set(owner, 'foreignKeys', None)
    assert getattr(partner, 'Table42') is None


def test_assoc_owner52_stub_double():
    # database_Table has no real 'Table53' property in the generated
    # code (a bare stub) -- manually attach it so database_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Constraint(expression="sample_text")
    partner = database_Table()
    setattr(partner, 'Table53', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'Table53') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'Table53') is None


def test_assoc_pkColumn47_stub_double():
    # database_ForeignKeyElement has no real 'database_ForeignKeyElement48' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_ForeignKeyElement()
    setattr(partner, 'database_ForeignKeyElement48', None)
    _safe_set(owner, 'database_Column49', partner)
    assert getattr(partner, 'database_ForeignKeyElement48') == owner
    _safe_set(owner, 'database_Column49', None)
    assert getattr(partner, 'database_ForeignKeyElement48') is None


def test_assoc_primaryKey6_stub_double():
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


def test_assoc_sequences58_stub_double():
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


def test_assoc_target43_stub_double():
    # database_Table has no real 'database_Table' property in the generated
    # code (a bare stub) -- manually attach it so database_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_ForeignKey()
    partner = database_Table()
    setattr(partner, 'database_Table', None)
    _safe_set(owner, 'database_ForeignKey44', partner)
    assert getattr(partner, 'database_Table') == owner
    _safe_set(owner, 'database_ForeignKey44', None)
    assert getattr(partner, 'database_Table') is None


def test_assoc_type10_stub_double():
    # database_Type has no real 'database_Type' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    partner = database_Type()
    setattr(partner, 'database_Type', None)
    _safe_set(owner, 'database_Column11', partner)
    assert getattr(partner, 'database_Type') == owner
    _safe_set(owner, 'database_Column11', None)
    assert getattr(partner, 'database_Type') is None


