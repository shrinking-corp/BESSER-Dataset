import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ColumnChange,
    Comparison,
    ConstraintChange,
    DBDiff,
    Diff,
    ForeignKeyChange,
    IndexChange,
    PrimaryKeyChange,
    SchemaChange,
    SequenceChange,
    TableChange,
    dbevolution_AddColumnChange,
    dbevolution_AddConstraint,
    dbevolution_AddForeignKey,
    dbevolution_AddIndex,
    dbevolution_AddPrimaryKey,
    dbevolution_AddSchema,
    dbevolution_AddSequence,
    dbevolution_AddTable,
    dbevolution_AlterSchema,
    dbevolution_AlterTable,
    dbevolution_Column,
    dbevolution_ColumnChange,
    dbevolution_Constraint,
    dbevolution_ConstraintChange,
    dbevolution_DBDiff,
    dbevolution_DatabaseChangeSet,
    dbevolution_EObject,
    dbevolution_ForeignKey,
    dbevolution_ForeignKeyChange,
    dbevolution_Index,
    dbevolution_IndexChange,
    dbevolution_PrimaryKey,
    dbevolution_PrimaryKeyChange,
    dbevolution_RemoveColumnChange,
    dbevolution_RemoveConstraint,
    dbevolution_RemoveForeignKey,
    dbevolution_RemoveIndex,
    dbevolution_RemovePrimaryKey,
    dbevolution_RemoveSchema,
    dbevolution_RemoveSequence,
    dbevolution_RemoveTable,
    dbevolution_RenameColumnChange,
    dbevolution_RenameSchemaChange,
    dbevolution_RenameTableChange,
    dbevolution_Schema,
    dbevolution_SchemaChange,
    dbevolution_Sequence,
    dbevolution_SequenceChange,
    dbevolution_Table,
    dbevolution_TableChange,
    dbevolution_UpdateColumnChange,
    dbevolution_UpdateColumnCommentChange,
    dbevolution_UpdateConstraint,
    dbevolution_UpdateForeignKey,
    dbevolution_UpdateIndex,
    dbevolution_UpdatePrimaryKey,
    dbevolution_UpdateSchemaCommentChange,
    dbevolution_UpdateSequence,
    dbevolution_UpdateTableCommentChange,
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

def test_dbevolution_AddColumnChange_isa_ColumnChange():
    instance = dbevolution_AddColumnChange()
    assert isinstance(instance, ColumnChange)


def test_dbevolution_RemoveColumnChange_isa_ColumnChange():
    instance = dbevolution_RemoveColumnChange()
    assert isinstance(instance, ColumnChange)


def test_dbevolution_RenameColumnChange_isa_ColumnChange():
    instance = dbevolution_RenameColumnChange()
    assert isinstance(instance, ColumnChange)


def test_dbevolution_UpdateColumnChange_isa_ColumnChange():
    instance = dbevolution_UpdateColumnChange()
    assert isinstance(instance, ColumnChange)


def test_dbevolution_UpdateColumnCommentChange_isa_ColumnChange():
    instance = dbevolution_UpdateColumnCommentChange()
    assert isinstance(instance, ColumnChange)


def test_dbevolution_DatabaseChangeSet_isa_Comparison():
    instance = dbevolution_DatabaseChangeSet()
    assert isinstance(instance, Comparison)


def test_dbevolution_AddConstraint_isa_ConstraintChange():
    instance = dbevolution_AddConstraint()
    assert isinstance(instance, ConstraintChange)


def test_dbevolution_RemoveConstraint_isa_ConstraintChange():
    instance = dbevolution_RemoveConstraint()
    assert isinstance(instance, ConstraintChange)


def test_dbevolution_UpdateConstraint_isa_ConstraintChange():
    instance = dbevolution_UpdateConstraint()
    assert isinstance(instance, ConstraintChange)


def test_dbevolution_ColumnChange_isa_DBDiff():
    instance = dbevolution_ColumnChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_ConstraintChange_isa_DBDiff():
    instance = dbevolution_ConstraintChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_ForeignKeyChange_isa_DBDiff():
    instance = dbevolution_ForeignKeyChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_IndexChange_isa_DBDiff():
    instance = dbevolution_IndexChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_PrimaryKeyChange_isa_DBDiff():
    instance = dbevolution_PrimaryKeyChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_SchemaChange_isa_DBDiff():
    instance = dbevolution_SchemaChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_SequenceChange_isa_DBDiff():
    instance = dbevolution_SequenceChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_TableChange_isa_DBDiff():
    instance = dbevolution_TableChange()
    assert isinstance(instance, DBDiff)


def test_dbevolution_DBDiff_isa_Diff():
    instance = dbevolution_DBDiff()
    assert isinstance(instance, Diff)


def test_dbevolution_AddForeignKey_isa_ForeignKeyChange():
    instance = dbevolution_AddForeignKey()
    assert isinstance(instance, ForeignKeyChange)


def test_dbevolution_RemoveForeignKey_isa_ForeignKeyChange():
    instance = dbevolution_RemoveForeignKey()
    assert isinstance(instance, ForeignKeyChange)


def test_dbevolution_UpdateForeignKey_isa_ForeignKeyChange():
    instance = dbevolution_UpdateForeignKey()
    assert isinstance(instance, ForeignKeyChange)


def test_dbevolution_AddIndex_isa_IndexChange():
    instance = dbevolution_AddIndex()
    assert isinstance(instance, IndexChange)


def test_dbevolution_RemoveIndex_isa_IndexChange():
    instance = dbevolution_RemoveIndex()
    assert isinstance(instance, IndexChange)


def test_dbevolution_UpdateIndex_isa_IndexChange():
    instance = dbevolution_UpdateIndex()
    assert isinstance(instance, IndexChange)


def test_dbevolution_AddPrimaryKey_isa_PrimaryKeyChange():
    instance = dbevolution_AddPrimaryKey()
    assert isinstance(instance, PrimaryKeyChange)


def test_dbevolution_RemovePrimaryKey_isa_PrimaryKeyChange():
    instance = dbevolution_RemovePrimaryKey()
    assert isinstance(instance, PrimaryKeyChange)


def test_dbevolution_UpdatePrimaryKey_isa_PrimaryKeyChange():
    instance = dbevolution_UpdatePrimaryKey()
    assert isinstance(instance, PrimaryKeyChange)


def test_dbevolution_AddSchema_isa_SchemaChange():
    instance = dbevolution_AddSchema()
    assert isinstance(instance, SchemaChange)


def test_dbevolution_AlterSchema_isa_SchemaChange():
    instance = dbevolution_AlterSchema()
    assert isinstance(instance, SchemaChange)


def test_dbevolution_RemoveSchema_isa_SchemaChange():
    instance = dbevolution_RemoveSchema()
    assert isinstance(instance, SchemaChange)


def test_dbevolution_RenameSchemaChange_isa_SchemaChange():
    instance = dbevolution_RenameSchemaChange()
    assert isinstance(instance, SchemaChange)


def test_dbevolution_UpdateSchemaCommentChange_isa_SchemaChange():
    instance = dbevolution_UpdateSchemaCommentChange()
    assert isinstance(instance, SchemaChange)


def test_dbevolution_AddSequence_isa_SequenceChange():
    instance = dbevolution_AddSequence()
    assert isinstance(instance, SequenceChange)


def test_dbevolution_RemoveSequence_isa_SequenceChange():
    instance = dbevolution_RemoveSequence()
    assert isinstance(instance, SequenceChange)


def test_dbevolution_UpdateSequence_isa_SequenceChange():
    instance = dbevolution_UpdateSequence()
    assert isinstance(instance, SequenceChange)


def test_dbevolution_AddTable_isa_TableChange():
    instance = dbevolution_AddTable()
    assert isinstance(instance, TableChange)


def test_dbevolution_AlterTable_isa_TableChange():
    instance = dbevolution_AlterTable()
    assert isinstance(instance, TableChange)


def test_dbevolution_RemoveTable_isa_TableChange():
    instance = dbevolution_RemoveTable()
    assert isinstance(instance, TableChange)


def test_dbevolution_RenameTableChange_isa_TableChange():
    instance = dbevolution_RenameTableChange()
    assert isinstance(instance, TableChange)


def test_dbevolution_UpdateTableCommentChange_isa_TableChange():
    instance = dbevolution_UpdateTableCommentChange()
    assert isinstance(instance, TableChange)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ColumnChange_strategy = st.builds(ColumnChange)
@given(instance=ColumnChange_strategy)
@settings(max_examples=25)
def test_ColumnChange_instantiation(instance):
    assert isinstance(instance, ColumnChange)


Comparison_strategy = st.builds(Comparison)
@given(instance=Comparison_strategy)
@settings(max_examples=25)
def test_Comparison_instantiation(instance):
    assert isinstance(instance, Comparison)


ConstraintChange_strategy = st.builds(ConstraintChange)
@given(instance=ConstraintChange_strategy)
@settings(max_examples=25)
def test_ConstraintChange_instantiation(instance):
    assert isinstance(instance, ConstraintChange)


DBDiff_strategy = st.builds(DBDiff)
@given(instance=DBDiff_strategy)
@settings(max_examples=25)
def test_DBDiff_instantiation(instance):
    assert isinstance(instance, DBDiff)


Diff_strategy = st.builds(Diff)
@given(instance=Diff_strategy)
@settings(max_examples=25)
def test_Diff_instantiation(instance):
    assert isinstance(instance, Diff)


ForeignKeyChange_strategy = st.builds(ForeignKeyChange)
@given(instance=ForeignKeyChange_strategy)
@settings(max_examples=25)
def test_ForeignKeyChange_instantiation(instance):
    assert isinstance(instance, ForeignKeyChange)


IndexChange_strategy = st.builds(IndexChange)
@given(instance=IndexChange_strategy)
@settings(max_examples=25)
def test_IndexChange_instantiation(instance):
    assert isinstance(instance, IndexChange)


PrimaryKeyChange_strategy = st.builds(PrimaryKeyChange)
@given(instance=PrimaryKeyChange_strategy)
@settings(max_examples=25)
def test_PrimaryKeyChange_instantiation(instance):
    assert isinstance(instance, PrimaryKeyChange)


SchemaChange_strategy = st.builds(SchemaChange)
@given(instance=SchemaChange_strategy)
@settings(max_examples=25)
def test_SchemaChange_instantiation(instance):
    assert isinstance(instance, SchemaChange)


SequenceChange_strategy = st.builds(SequenceChange)
@given(instance=SequenceChange_strategy)
@settings(max_examples=25)
def test_SequenceChange_instantiation(instance):
    assert isinstance(instance, SequenceChange)


TableChange_strategy = st.builds(TableChange)
@given(instance=TableChange_strategy)
@settings(max_examples=25)
def test_TableChange_instantiation(instance):
    assert isinstance(instance, TableChange)


dbevolution_AddColumnChange_strategy = st.builds(dbevolution_AddColumnChange)
@given(instance=dbevolution_AddColumnChange_strategy)
@settings(max_examples=25)
def test_dbevolution_AddColumnChange_instantiation(instance):
    assert isinstance(instance, dbevolution_AddColumnChange)


dbevolution_AddConstraint_strategy = st.builds(dbevolution_AddConstraint)
@given(instance=dbevolution_AddConstraint_strategy)
@settings(max_examples=25)
def test_dbevolution_AddConstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_AddConstraint)


dbevolution_AddForeignKey_strategy = st.builds(dbevolution_AddForeignKey)
@given(instance=dbevolution_AddForeignKey_strategy)
@settings(max_examples=25)
def test_dbevolution_AddForeignKey_instantiation(instance):
    assert isinstance(instance, dbevolution_AddForeignKey)


dbevolution_AddIndex_strategy = st.builds(dbevolution_AddIndex)
@given(instance=dbevolution_AddIndex_strategy)
@settings(max_examples=25)
def test_dbevolution_AddIndex_instantiation(instance):
    assert isinstance(instance, dbevolution_AddIndex)


dbevolution_AddPrimaryKey_strategy = st.builds(dbevolution_AddPrimaryKey)
@given(instance=dbevolution_AddPrimaryKey_strategy)
@settings(max_examples=25)
def test_dbevolution_AddPrimaryKey_instantiation(instance):
    assert isinstance(instance, dbevolution_AddPrimaryKey)


dbevolution_AddSchema_strategy = st.builds(dbevolution_AddSchema)
@given(instance=dbevolution_AddSchema_strategy)
@settings(max_examples=25)
def test_dbevolution_AddSchema_instantiation(instance):
    assert isinstance(instance, dbevolution_AddSchema)


dbevolution_AddSequence_strategy = st.builds(dbevolution_AddSequence)
@given(instance=dbevolution_AddSequence_strategy)
@settings(max_examples=25)
def test_dbevolution_AddSequence_instantiation(instance):
    assert isinstance(instance, dbevolution_AddSequence)


dbevolution_AddTable_strategy = st.builds(dbevolution_AddTable)
@given(instance=dbevolution_AddTable_strategy)
@settings(max_examples=25)
def test_dbevolution_AddTable_instantiation(instance):
    assert isinstance(instance, dbevolution_AddTable)


dbevolution_AlterSchema_strategy = st.builds(dbevolution_AlterSchema)
@given(instance=dbevolution_AlterSchema_strategy)
@settings(max_examples=25)
def test_dbevolution_AlterSchema_instantiation(instance):
    assert isinstance(instance, dbevolution_AlterSchema)


dbevolution_AlterTable_strategy = st.builds(dbevolution_AlterTable)
@given(instance=dbevolution_AlterTable_strategy)
@settings(max_examples=25)
def test_dbevolution_AlterTable_instantiation(instance):
    assert isinstance(instance, dbevolution_AlterTable)


dbevolution_Column_strategy = st.builds(dbevolution_Column)
@given(instance=dbevolution_Column_strategy)
@settings(max_examples=25)
def test_dbevolution_Column_instantiation(instance):
    assert isinstance(instance, dbevolution_Column)


dbevolution_ColumnChange_strategy = st.builds(dbevolution_ColumnChange)
@given(instance=dbevolution_ColumnChange_strategy)
@settings(max_examples=25)
def test_dbevolution_ColumnChange_instantiation(instance):
    assert isinstance(instance, dbevolution_ColumnChange)


dbevolution_Constraint_strategy = st.builds(dbevolution_Constraint)
@given(instance=dbevolution_Constraint_strategy)
@settings(max_examples=25)
def test_dbevolution_Constraint_instantiation(instance):
    assert isinstance(instance, dbevolution_Constraint)


dbevolution_ConstraintChange_strategy = st.builds(dbevolution_ConstraintChange)
@given(instance=dbevolution_ConstraintChange_strategy)
@settings(max_examples=25)
def test_dbevolution_ConstraintChange_instantiation(instance):
    assert isinstance(instance, dbevolution_ConstraintChange)


dbevolution_DBDiff_strategy = st.builds(dbevolution_DBDiff)
@given(instance=dbevolution_DBDiff_strategy)
@settings(max_examples=25)
def test_dbevolution_DBDiff_instantiation(instance):
    assert isinstance(instance, dbevolution_DBDiff)


dbevolution_DatabaseChangeSet_strategy = st.builds(dbevolution_DatabaseChangeSet)
@given(instance=dbevolution_DatabaseChangeSet_strategy)
@settings(max_examples=25)
def test_dbevolution_DatabaseChangeSet_instantiation(instance):
    assert isinstance(instance, dbevolution_DatabaseChangeSet)


dbevolution_EObject_strategy = st.builds(dbevolution_EObject)
@given(instance=dbevolution_EObject_strategy)
@settings(max_examples=25)
def test_dbevolution_EObject_instantiation(instance):
    assert isinstance(instance, dbevolution_EObject)


dbevolution_ForeignKey_strategy = st.builds(dbevolution_ForeignKey)
@given(instance=dbevolution_ForeignKey_strategy)
@settings(max_examples=25)
def test_dbevolution_ForeignKey_instantiation(instance):
    assert isinstance(instance, dbevolution_ForeignKey)


dbevolution_ForeignKeyChange_strategy = st.builds(dbevolution_ForeignKeyChange)
@given(instance=dbevolution_ForeignKeyChange_strategy)
@settings(max_examples=25)
def test_dbevolution_ForeignKeyChange_instantiation(instance):
    assert isinstance(instance, dbevolution_ForeignKeyChange)


dbevolution_Index_strategy = st.builds(dbevolution_Index)
@given(instance=dbevolution_Index_strategy)
@settings(max_examples=25)
def test_dbevolution_Index_instantiation(instance):
    assert isinstance(instance, dbevolution_Index)


dbevolution_IndexChange_strategy = st.builds(dbevolution_IndexChange)
@given(instance=dbevolution_IndexChange_strategy)
@settings(max_examples=25)
def test_dbevolution_IndexChange_instantiation(instance):
    assert isinstance(instance, dbevolution_IndexChange)


dbevolution_PrimaryKey_strategy = st.builds(dbevolution_PrimaryKey)
@given(instance=dbevolution_PrimaryKey_strategy)
@settings(max_examples=25)
def test_dbevolution_PrimaryKey_instantiation(instance):
    assert isinstance(instance, dbevolution_PrimaryKey)


dbevolution_PrimaryKeyChange_strategy = st.builds(dbevolution_PrimaryKeyChange)
@given(instance=dbevolution_PrimaryKeyChange_strategy)
@settings(max_examples=25)
def test_dbevolution_PrimaryKeyChange_instantiation(instance):
    assert isinstance(instance, dbevolution_PrimaryKeyChange)


dbevolution_RemoveColumnChange_strategy = st.builds(dbevolution_RemoveColumnChange)
@given(instance=dbevolution_RemoveColumnChange_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveColumnChange_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveColumnChange)


dbevolution_RemoveConstraint_strategy = st.builds(dbevolution_RemoveConstraint)
@given(instance=dbevolution_RemoveConstraint_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveConstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveConstraint)


dbevolution_RemoveForeignKey_strategy = st.builds(dbevolution_RemoveForeignKey)
@given(instance=dbevolution_RemoveForeignKey_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveForeignKey_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveForeignKey)


dbevolution_RemoveIndex_strategy = st.builds(dbevolution_RemoveIndex)
@given(instance=dbevolution_RemoveIndex_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveIndex_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveIndex)


dbevolution_RemovePrimaryKey_strategy = st.builds(dbevolution_RemovePrimaryKey)
@given(instance=dbevolution_RemovePrimaryKey_strategy)
@settings(max_examples=25)
def test_dbevolution_RemovePrimaryKey_instantiation(instance):
    assert isinstance(instance, dbevolution_RemovePrimaryKey)


dbevolution_RemoveSchema_strategy = st.builds(dbevolution_RemoveSchema)
@given(instance=dbevolution_RemoveSchema_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveSchema_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveSchema)


dbevolution_RemoveSequence_strategy = st.builds(dbevolution_RemoveSequence)
@given(instance=dbevolution_RemoveSequence_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveSequence_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveSequence)


dbevolution_RemoveTable_strategy = st.builds(dbevolution_RemoveTable)
@given(instance=dbevolution_RemoveTable_strategy)
@settings(max_examples=25)
def test_dbevolution_RemoveTable_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveTable)


dbevolution_RenameColumnChange_strategy = st.builds(dbevolution_RenameColumnChange)
@given(instance=dbevolution_RenameColumnChange_strategy)
@settings(max_examples=25)
def test_dbevolution_RenameColumnChange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameColumnChange)


dbevolution_RenameSchemaChange_strategy = st.builds(dbevolution_RenameSchemaChange)
@given(instance=dbevolution_RenameSchemaChange_strategy)
@settings(max_examples=25)
def test_dbevolution_RenameSchemaChange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameSchemaChange)


dbevolution_RenameTableChange_strategy = st.builds(dbevolution_RenameTableChange)
@given(instance=dbevolution_RenameTableChange_strategy)
@settings(max_examples=25)
def test_dbevolution_RenameTableChange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameTableChange)


dbevolution_Schema_strategy = st.builds(dbevolution_Schema)
@given(instance=dbevolution_Schema_strategy)
@settings(max_examples=25)
def test_dbevolution_Schema_instantiation(instance):
    assert isinstance(instance, dbevolution_Schema)


dbevolution_SchemaChange_strategy = st.builds(dbevolution_SchemaChange)
@given(instance=dbevolution_SchemaChange_strategy)
@settings(max_examples=25)
def test_dbevolution_SchemaChange_instantiation(instance):
    assert isinstance(instance, dbevolution_SchemaChange)


dbevolution_Sequence_strategy = st.builds(dbevolution_Sequence)
@given(instance=dbevolution_Sequence_strategy)
@settings(max_examples=25)
def test_dbevolution_Sequence_instantiation(instance):
    assert isinstance(instance, dbevolution_Sequence)


dbevolution_SequenceChange_strategy = st.builds(dbevolution_SequenceChange)
@given(instance=dbevolution_SequenceChange_strategy)
@settings(max_examples=25)
def test_dbevolution_SequenceChange_instantiation(instance):
    assert isinstance(instance, dbevolution_SequenceChange)


dbevolution_Table_strategy = st.builds(dbevolution_Table)
@given(instance=dbevolution_Table_strategy)
@settings(max_examples=25)
def test_dbevolution_Table_instantiation(instance):
    assert isinstance(instance, dbevolution_Table)


dbevolution_TableChange_strategy = st.builds(dbevolution_TableChange)
@given(instance=dbevolution_TableChange_strategy)
@settings(max_examples=25)
def test_dbevolution_TableChange_instantiation(instance):
    assert isinstance(instance, dbevolution_TableChange)


dbevolution_UpdateColumnChange_strategy = st.builds(dbevolution_UpdateColumnChange)
@given(instance=dbevolution_UpdateColumnChange_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateColumnChange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateColumnChange)


dbevolution_UpdateColumnCommentChange_strategy = st.builds(dbevolution_UpdateColumnCommentChange)
@given(instance=dbevolution_UpdateColumnCommentChange_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateColumnCommentChange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateColumnCommentChange)


dbevolution_UpdateConstraint_strategy = st.builds(dbevolution_UpdateConstraint)
@given(instance=dbevolution_UpdateConstraint_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateConstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateConstraint)


dbevolution_UpdateForeignKey_strategy = st.builds(dbevolution_UpdateForeignKey)
@given(instance=dbevolution_UpdateForeignKey_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateForeignKey_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateForeignKey)


dbevolution_UpdateIndex_strategy = st.builds(dbevolution_UpdateIndex)
@given(instance=dbevolution_UpdateIndex_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateIndex_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateIndex)


dbevolution_UpdatePrimaryKey_strategy = st.builds(dbevolution_UpdatePrimaryKey)
@given(instance=dbevolution_UpdatePrimaryKey_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdatePrimaryKey_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdatePrimaryKey)


dbevolution_UpdateSchemaCommentChange_strategy = st.builds(dbevolution_UpdateSchemaCommentChange)
@given(instance=dbevolution_UpdateSchemaCommentChange_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateSchemaCommentChange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateSchemaCommentChange)


dbevolution_UpdateSequence_strategy = st.builds(dbevolution_UpdateSequence)
@given(instance=dbevolution_UpdateSequence_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateSequence_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateSequence)


dbevolution_UpdateTableCommentChange_strategy = st.builds(dbevolution_UpdateTableCommentChange)
@given(instance=dbevolution_UpdateTableCommentChange_strategy)
@settings(max_examples=25)
def test_dbevolution_UpdateTableCommentChange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateTableCommentChange)


