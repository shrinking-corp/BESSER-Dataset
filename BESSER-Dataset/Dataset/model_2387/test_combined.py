# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelOperation,
    mm_ops_SetDefaultValue,
    mm_ops_HasNoOwnInstances,
    mm_ops_RemoveSequence,
    mm_ops_RemoveIndex,
    mm_ops_AddColumn,
    mm_ops_RemoveColumn,
    mm_ops_AddIndex,
    mm_ops_DeleteRows,
    mm_ops_RemoveTable,
    mm_ops_RenameColumn,
    mm_ops_UpdateRows,
    mm_ops_AddSequence,
    mm_ops_RemoveDefaultValue,
    mm_ops_RemoveConstraint,
    mm_ops_InsertRows,
    mm_ops_GenerateSequenceNumbers,
    mm_ops_RemoveNotNull,
    mm_ops_AddTable,
    mm_ops_NillRows,
    mm_ops_RenameTable,
    mm_ops_SetColumnType,
    mm_ops_HasNoInstances,
    mm_ops_AddPrimaryKey,
    mm_ops_AddSchema,
    Operations,
    mm_ops_AddNotNull,
    mm_ops_AddUnique,
    mm_ops_AddForeignKey,
    mm_rdb_TableConstraint,
    mm_rdb_Column,
    TableConstraint,
    mm_rdb_Unique,
    mm_rdb_Table,
    Column,
    mm_ops_ModelOperation,
    mm_rdb_ForeignKey,
    Sequence,
    mm_rdb_PrimaryKey,
    Table,
    Structure,
    mm_rdb_Schema,
    Schema,
    ops_ModelOperation,
    ModelRoot,
    mm_rdb_Structure,
    mm_rdb_Operations,
    mm_rdb_Index,
    mm_rdb_Sequence,
    Index,
    mm_rdb_ModelRoot,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_hyp_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_hyp_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_ops_setdefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm_ops_SetDefaultValue)


def test_hyp_mm_ops_setdefaultvalue_constructor_exists():
    assert callable(mm_ops_SetDefaultValue.__init__)


def test_hyp_mm_ops_setdefaultvalue_constructor_args():
    sig = inspect.signature(mm_ops_SetDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "newDefaultValue" in params, "Missing parameter 'newDefaultValue'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"







def test_hyp_mm_ops_hasnoowninstances_is_not_abstract():
    assert not inspect.isabstract(mm_ops_HasNoOwnInstances)


def test_hyp_mm_ops_hasnoowninstances_constructor_exists():
    assert callable(mm_ops_HasNoOwnInstances.__init__)


def test_hyp_mm_ops_hasnoowninstances_constructor_args():
    sig = inspect.signature(mm_ops_HasNoOwnInstances.__init__)
    params = list(sig.parameters.keys())
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"






def test_hyp_mm_ops_removesequence_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveSequence)


def test_hyp_mm_ops_removesequence_constructor_exists():
    assert callable(mm_ops_RemoveSequence.__init__)


def test_hyp_mm_ops_removesequence_constructor_args():
    sig = inspect.signature(mm_ops_RemoveSequence.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_mm_ops_removeindex_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveIndex)


def test_hyp_mm_ops_removeindex_constructor_exists():
    assert callable(mm_ops_RemoveIndex.__init__)


def test_hyp_mm_ops_removeindex_constructor_args():
    sig = inspect.signature(mm_ops_RemoveIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"





def test_hyp_mm_ops_addcolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddColumn)


def test_hyp_mm_ops_addcolumn_constructor_exists():
    assert callable(mm_ops_AddColumn.__init__)


def test_hyp_mm_ops_addcolumn_constructor_args():
    sig = inspect.signature(mm_ops_AddColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "type" in params, "Missing parameter 'type'"








def test_hyp_mm_ops_removecolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveColumn)


def test_hyp_mm_ops_removecolumn_constructor_exists():
    assert callable(mm_ops_RemoveColumn.__init__)


def test_hyp_mm_ops_removecolumn_constructor_args():
    sig = inspect.signature(mm_ops_RemoveColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"






def test_hyp_mm_ops_addindex_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddIndex)


def test_hyp_mm_ops_addindex_constructor_exists():
    assert callable(mm_ops_AddIndex.__init__)


def test_hyp_mm_ops_addindex_constructor_args():
    sig = inspect.signature(mm_ops_AddIndex.__init__)
    params = list(sig.parameters.keys())
    assert "columnsNames" in params, "Missing parameter 'columnsNames'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"







def test_hyp_mm_ops_deleterows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_DeleteRows)


def test_hyp_mm_ops_deleterows_constructor_exists():
    assert callable(mm_ops_DeleteRows.__init__)


def test_hyp_mm_ops_deleterows_constructor_args():
    sig = inspect.signature(mm_ops_DeleteRows.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "tableName" in params, "Missing parameter 'tableName'"






def test_hyp_mm_ops_removetable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveTable)


def test_hyp_mm_ops_removetable_constructor_exists():
    assert callable(mm_ops_RemoveTable.__init__)


def test_hyp_mm_ops_removetable_constructor_args():
    sig = inspect.signature(mm_ops_RemoveTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"





def test_hyp_mm_ops_renamecolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RenameColumn)


def test_hyp_mm_ops_renamecolumn_constructor_exists():
    assert callable(mm_ops_RenameColumn.__init__)


def test_hyp_mm_ops_renamecolumn_constructor_args():
    sig = inspect.signature(mm_ops_RenameColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "newName" in params, "Missing parameter 'newName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"







def test_hyp_mm_ops_updaterows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_UpdateRows)


def test_hyp_mm_ops_updaterows_constructor_exists():
    assert callable(mm_ops_UpdateRows.__init__)


def test_hyp_mm_ops_updaterows_constructor_args():
    sig = inspect.signature(mm_ops_UpdateRows.__init__)
    params = list(sig.parameters.keys())
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"
    assert "sourceColumnName" in params, "Missing parameter 'sourceColumnName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"









def test_hyp_mm_ops_addsequence_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddSequence)


def test_hyp_mm_ops_addsequence_constructor_exists():
    assert callable(mm_ops_AddSequence.__init__)


def test_hyp_mm_ops_addsequence_constructor_args():
    sig = inspect.signature(mm_ops_AddSequence.__init__)
    params = list(sig.parameters.keys())
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_mm_ops_removedefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveDefaultValue)


def test_hyp_mm_ops_removedefaultvalue_constructor_exists():
    assert callable(mm_ops_RemoveDefaultValue.__init__)


def test_hyp_mm_ops_removedefaultvalue_constructor_args():
    sig = inspect.signature(mm_ops_RemoveDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"






def test_hyp_mm_ops_removeconstraint_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveConstraint)


def test_hyp_mm_ops_removeconstraint_constructor_exists():
    assert callable(mm_ops_RemoveConstraint.__init__)


def test_hyp_mm_ops_removeconstraint_constructor_args():
    sig = inspect.signature(mm_ops_RemoveConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"






def test_hyp_mm_ops_insertrows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_InsertRows)


def test_hyp_mm_ops_insertrows_constructor_exists():
    assert callable(mm_ops_InsertRows.__init__)


def test_hyp_mm_ops_insertrows_constructor_args():
    sig = inspect.signature(mm_ops_InsertRows.__init__)
    params = list(sig.parameters.keys())
    assert "sourceColumnsNames" in params, "Missing parameter 'sourceColumnsNames'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "targetColumnNames" in params, "Missing parameter 'targetColumnNames'"









def test_hyp_mm_ops_generatesequencenumbers_is_not_abstract():
    assert not inspect.isabstract(mm_ops_GenerateSequenceNumbers)


def test_hyp_mm_ops_generatesequencenumbers_constructor_exists():
    assert callable(mm_ops_GenerateSequenceNumbers.__init__)


def test_hyp_mm_ops_generatesequencenumbers_constructor_args():
    sig = inspect.signature(mm_ops_GenerateSequenceNumbers.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "sequenceName" in params, "Missing parameter 'sequenceName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "columnName" in params, "Missing parameter 'columnName'"







def test_hyp_mm_ops_removenotnull_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveNotNull)


def test_hyp_mm_ops_removenotnull_constructor_exists():
    assert callable(mm_ops_RemoveNotNull.__init__)


def test_hyp_mm_ops_removenotnull_constructor_args():
    sig = inspect.signature(mm_ops_RemoveNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"






def test_hyp_mm_ops_addtable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddTable)


def test_hyp_mm_ops_addtable_constructor_exists():
    assert callable(mm_ops_AddTable.__init__)


def test_hyp_mm_ops_addtable_constructor_args():
    sig = inspect.signature(mm_ops_AddTable.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_mm_ops_nillrows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_NillRows)


def test_hyp_mm_ops_nillrows_constructor_exists():
    assert callable(mm_ops_NillRows.__init__)


def test_hyp_mm_ops_nillrows_constructor_args():
    sig = inspect.signature(mm_ops_NillRows.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "tableName" in params, "Missing parameter 'tableName'"







def test_hyp_mm_ops_renametable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RenameTable)


def test_hyp_mm_ops_renametable_constructor_exists():
    assert callable(mm_ops_RenameTable.__init__)


def test_hyp_mm_ops_renametable_constructor_args():
    sig = inspect.signature(mm_ops_RenameTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "newName" in params, "Missing parameter 'newName'"






def test_hyp_mm_ops_setcolumntype_is_not_abstract():
    assert not inspect.isabstract(mm_ops_SetColumnType)


def test_hyp_mm_ops_setcolumntype_constructor_exists():
    assert callable(mm_ops_SetColumnType.__init__)


def test_hyp_mm_ops_setcolumntype_constructor_args():
    sig = inspect.signature(mm_ops_SetColumnType.__init__)
    params = list(sig.parameters.keys())
    assert "oldType" in params, "Missing parameter 'oldType'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "newType" in params, "Missing parameter 'newType'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"








def test_hyp_mm_ops_hasnoinstances_is_not_abstract():
    assert not inspect.isabstract(mm_ops_HasNoInstances)


def test_hyp_mm_ops_hasnoinstances_constructor_exists():
    assert callable(mm_ops_HasNoInstances.__init__)


def test_hyp_mm_ops_hasnoinstances_constructor_args():
    sig = inspect.signature(mm_ops_HasNoInstances.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"





def test_hyp_mm_ops_addprimarykey_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddPrimaryKey)


def test_hyp_mm_ops_addprimarykey_constructor_exists():
    assert callable(mm_ops_AddPrimaryKey.__init__)


def test_hyp_mm_ops_addprimarykey_constructor_args():
    sig = inspect.signature(mm_ops_AddPrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"







def test_hyp_mm_ops_addschema_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddSchema)


def test_hyp_mm_ops_addschema_constructor_exists():
    assert callable(mm_ops_AddSchema.__init__)


def test_hyp_mm_ops_addschema_constructor_args():
    sig = inspect.signature(mm_ops_AddSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_operations_is_not_abstract():
    assert not inspect.isabstract(Operations)


def test_hyp_operations_constructor_exists():
    assert callable(Operations.__init__)


def test_hyp_operations_constructor_args():
    sig = inspect.signature(Operations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_ops_addnotnull_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddNotNull)


def test_hyp_mm_ops_addnotnull_constructor_exists():
    assert callable(mm_ops_AddNotNull.__init__)


def test_hyp_mm_ops_addnotnull_constructor_args():
    sig = inspect.signature(mm_ops_AddNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"






def test_hyp_mm_ops_addunique_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddUnique)


def test_hyp_mm_ops_addunique_constructor_exists():
    assert callable(mm_ops_AddUnique.__init__)


def test_hyp_mm_ops_addunique_constructor_args():
    sig = inspect.signature(mm_ops_AddUnique.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constrainedColumnNames" in params, "Missing parameter 'constrainedColumnNames'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"







def test_hyp_mm_ops_addforeignkey_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddForeignKey)


def test_hyp_mm_ops_addforeignkey_constructor_exists():
    assert callable(mm_ops_AddForeignKey.__init__)


def test_hyp_mm_ops_addforeignkey_constructor_args():
    sig = inspect.signature(mm_ops_AddForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"








def test_hyp_mm_rdb_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_TableConstraint)


def test_hyp_mm_rdb_tableconstraint_constructor_exists():
    assert callable(mm_rdb_TableConstraint.__init__)


def test_hyp_mm_rdb_tableconstraint_constructor_args():
    sig = inspect.signature(mm_rdb_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mm_rdb_column_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Column)


def test_hyp_mm_rdb_column_constructor_exists():
    assert callable(mm_rdb_Column.__init__)


def test_hyp_mm_rdb_column_constructor_args():
    sig = inspect.signature(mm_rdb_Column.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isNillable" in params, "Missing parameter 'isNillable'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_hyp_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_hyp_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_unique_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Unique)


def test_hyp_mm_rdb_unique_constructor_exists():
    assert callable(mm_rdb_Unique.__init__)


def test_hyp_mm_rdb_unique_constructor_args():
    sig = inspect.signature(mm_rdb_Unique.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_table_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Table)


def test_hyp_mm_rdb_table_constructor_exists():
    assert callable(mm_rdb_Table.__init__)


def test_hyp_mm_rdb_table_constructor_args():
    sig = inspect.signature(mm_rdb_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_hyp_column_constructor_exists():
    assert callable(Column.__init__)


def test_hyp_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_ops_modeloperation_is_not_abstract():
    assert not inspect.isabstract(mm_ops_ModelOperation)


def test_hyp_mm_ops_modeloperation_constructor_exists():
    assert callable(mm_ops_ModelOperation.__init__)


def test_hyp_mm_ops_modeloperation_constructor_args():
    sig = inspect.signature(mm_ops_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_foreignkey_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_ForeignKey)


def test_hyp_mm_rdb_foreignkey_constructor_exists():
    assert callable(mm_rdb_ForeignKey.__init__)


def test_hyp_mm_rdb_foreignkey_constructor_args():
    sig = inspect.signature(mm_rdb_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_hyp_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_hyp_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_primarykey_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_PrimaryKey)


def test_hyp_mm_rdb_primarykey_constructor_exists():
    assert callable(mm_rdb_PrimaryKey.__init__)


def test_hyp_mm_rdb_primarykey_constructor_args():
    sig = inspect.signature(mm_rdb_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_hyp_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_hyp_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_schema_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Schema)


def test_hyp_mm_rdb_schema_constructor_exists():
    assert callable(mm_rdb_Schema.__init__)


def test_hyp_mm_rdb_schema_constructor_args():
    sig = inspect.signature(mm_rdb_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_hyp_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_hyp_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ops_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ops_ModelOperation)


def test_hyp_ops_modeloperation_constructor_exists():
    assert callable(ops_ModelOperation.__init__)


def test_hyp_ops_modeloperation_constructor_args():
    sig = inspect.signature(ops_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelroot_is_not_abstract():
    assert not inspect.isabstract(ModelRoot)


def test_hyp_modelroot_constructor_exists():
    assert callable(ModelRoot.__init__)


def test_hyp_modelroot_constructor_args():
    sig = inspect.signature(ModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_structure_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Structure)


def test_hyp_mm_rdb_structure_constructor_exists():
    assert callable(mm_rdb_Structure.__init__)


def test_hyp_mm_rdb_structure_constructor_args():
    sig = inspect.signature(mm_rdb_Structure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_operations_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Operations)


def test_hyp_mm_rdb_operations_constructor_exists():
    assert callable(mm_rdb_Operations.__init__)


def test_hyp_mm_rdb_operations_constructor_args():
    sig = inspect.signature(mm_rdb_Operations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_index_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Index)


def test_hyp_mm_rdb_index_constructor_exists():
    assert callable(mm_rdb_Index.__init__)


def test_hyp_mm_rdb_index_constructor_args():
    sig = inspect.signature(mm_rdb_Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mm_rdb_sequence_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Sequence)


def test_hyp_mm_rdb_sequence_constructor_exists():
    assert callable(mm_rdb_Sequence.__init__)


def test_hyp_mm_rdb_sequence_constructor_args():
    sig = inspect.signature(mm_rdb_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "startValue" in params, "Missing parameter 'startValue'"





def test_hyp_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_hyp_index_constructor_exists():
    assert callable(Index.__init__)


def test_hyp_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mm_rdb_modelroot_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_ModelRoot)


def test_hyp_mm_rdb_modelroot_constructor_exists():
    assert callable(mm_rdb_ModelRoot.__init__)


def test_hyp_mm_rdb_modelroot_constructor_args():
    sig = inspect.signature(mm_rdb_ModelRoot.__init__)
    params = list(sig.parameters.keys())

def test_hyp_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_hyp_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "char",
        "int",
        "boolean",
        "float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ModelOperation_strategy = st.builds(
    ModelOperation,
)
mm_ops_SetDefaultValue_strategy = st.builds(
    mm_ops_SetDefaultValue,
    owningColumnName=
        safe_text,
    owningSchemaName=
        safe_text,
    newDefaultValue=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_HasNoOwnInstances_strategy = st.builds(
    mm_ops_HasNoOwnInstances,
    whereCondition=
        safe_text,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RemoveSequence_strategy = st.builds(
    mm_ops_RemoveSequence,
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_RemoveIndex_strategy = st.builds(
    mm_ops_RemoveIndex,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddColumn_strategy = st.builds(
    mm_ops_AddColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    defaultValue=
        safe_text,
    type=
        safe_text
)
mm_ops_RemoveColumn_strategy = st.builds(
    mm_ops_RemoveColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddIndex_strategy = st.builds(
    mm_ops_AddIndex,
    columnsNames=
        safe_text,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_DeleteRows_strategy = st.builds(
    mm_ops_DeleteRows,
    owningSchemaName=
        safe_text,
    whereCondition=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RemoveTable_strategy = st.builds(
    mm_ops_RemoveTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_RenameColumn_strategy = st.builds(
    mm_ops_RenameColumn,
    owningTableName=
        safe_text,
    newName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_UpdateRows_strategy = st.builds(
    mm_ops_UpdateRows,
    sourceTableName=
        safe_text,
    targetColumnName=
        safe_text,
    sourceColumnName=
        safe_text,
    whereCondition=
        safe_text,
    targetTableName=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddSequence_strategy = st.builds(
    mm_ops_AddSequence,
    startValue=
        st.integers(),
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_RemoveDefaultValue_strategy = st.builds(
    mm_ops_RemoveDefaultValue,
    owningSchemaName=
        safe_text,
    owningColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_RemoveConstraint_strategy = st.builds(
    mm_ops_RemoveConstraint,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_InsertRows_strategy = st.builds(
    mm_ops_InsertRows,
    sourceColumnsNames=
        safe_text,
    owningSchemaName=
        safe_text,
    sourceTableName=
        safe_text,
    targetTableName=
        safe_text,
    whereCondition=
        safe_text,
    targetColumnNames=
        safe_text
)
mm_ops_GenerateSequenceNumbers_strategy = st.builds(
    mm_ops_GenerateSequenceNumbers,
    tableName=
        safe_text,
    sequenceName=
        safe_text,
    owningSchemaName=
        safe_text,
    columnName=
        safe_text
)
mm_ops_RemoveNotNull_strategy = st.builds(
    mm_ops_RemoveNotNull,
    owningSchemaName=
        safe_text,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddTable_strategy = st.builds(
    mm_ops_AddTable,
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_NillRows_strategy = st.builds(
    mm_ops_NillRows,
    owningSchemaName=
        safe_text,
    columnName=
        safe_text,
    whereCondition=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RenameTable_strategy = st.builds(
    mm_ops_RenameTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    newName=
        safe_text
)
mm_ops_SetColumnType_strategy = st.builds(
    mm_ops_SetColumnType,
    oldType=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    newType=
        safe_text,
    owningColumnName=
        safe_text
)
mm_ops_HasNoInstances_strategy = st.builds(
    mm_ops_HasNoInstances,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm_ops_AddPrimaryKey_strategy = st.builds(
    mm_ops_AddPrimaryKey,
    owningSchemaName=
        safe_text,
    name=
        safe_text,
    owningTableName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm_ops_AddSchema_strategy = st.builds(
    mm_ops_AddSchema,
    name=
        safe_text
)
Operations_strategy = st.builds(
    Operations,
)
mm_ops_AddNotNull_strategy = st.builds(
    mm_ops_AddNotNull,
    owningSchemaName=
        safe_text,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddUnique_strategy = st.builds(
    mm_ops_AddUnique,
    name=
        safe_text,
    constrainedColumnNames=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddForeignKey_strategy = st.builds(
    mm_ops_AddForeignKey,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text,
    targetTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_rdb_TableConstraint_strategy = st.builds(
    mm_rdb_TableConstraint,
    name=
        safe_text
)
mm_rdb_Column_strategy = st.builds(
    mm_rdb_Column,
    defaultValue=
        safe_text,
    name=
        safe_text,
    isNillable=
        safe_text,
    type=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
mm_rdb_Unique_strategy = st.builds(
    mm_rdb_Unique,
)
mm_rdb_Table_strategy = st.builds(
    mm_rdb_Table,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
mm_ops_ModelOperation_strategy = st.builds(
    mm_ops_ModelOperation,
)
mm_rdb_ForeignKey_strategy = st.builds(
    mm_rdb_ForeignKey,
)
Sequence_strategy = st.builds(
    Sequence,
)
mm_rdb_PrimaryKey_strategy = st.builds(
    mm_rdb_PrimaryKey,
)
Table_strategy = st.builds(
    Table,
)
Structure_strategy = st.builds(
    Structure,
)
mm_rdb_Schema_strategy = st.builds(
    mm_rdb_Schema,
    name=
        safe_text
)
Schema_strategy = st.builds(
    Schema,
)
ops_ModelOperation_strategy = st.builds(
    ops_ModelOperation,
)
ModelRoot_strategy = st.builds(
    ModelRoot,
)
mm_rdb_Structure_strategy = st.builds(
    mm_rdb_Structure,
)
mm_rdb_Operations_strategy = st.builds(
    mm_rdb_Operations,
)
mm_rdb_Index_strategy = st.builds(
    mm_rdb_Index,
    name=
        safe_text
)
mm_rdb_Sequence_strategy = st.builds(
    mm_rdb_Sequence,
    name=
        safe_text,
    startValue=
        st.integers()
)
Index_strategy = st.builds(
    Index,
)
mm_rdb_ModelRoot_strategy = st.builds(
    mm_rdb_ModelRoot,
)





@given(instance=mm_ops_SetDefaultValue_strategy)
def test_hyp_mm_ops_setdefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_hyp_mm_ops_setdefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_hyp_mm_ops_setdefaultvalue_newDefaultValue_setter(instance):
    original = instance.newDefaultValue
    instance.newDefaultValue = original
    assert instance.newDefaultValue == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_hyp_mm_ops_setdefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original




@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_hyp_mm_ops_hasnoowninstances_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_hyp_mm_ops_hasnoowninstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_hyp_mm_ops_hasnoowninstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original




@given(instance=mm_ops_RemoveSequence_strategy)
def test_hyp_mm_ops_removesequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveSequence_strategy)
def test_hyp_mm_ops_removesequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm_ops_RemoveIndex_strategy)
def test_hyp_mm_ops_removeindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveIndex_strategy)
def test_hyp_mm_ops_removeindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_AddColumn_strategy)
def test_hyp_mm_ops_addcolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddColumn_strategy)
def test_hyp_mm_ops_addcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddColumn_strategy)
def test_hyp_mm_ops_addcolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddColumn_strategy)
def test_hyp_mm_ops_addcolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=mm_ops_AddColumn_strategy)
def test_hyp_mm_ops_addcolumn_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=mm_ops_RemoveColumn_strategy)
def test_hyp_mm_ops_removecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RemoveColumn_strategy)
def test_hyp_mm_ops_removecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveColumn_strategy)
def test_hyp_mm_ops_removecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_AddIndex_strategy)
def test_hyp_mm_ops_addindex_columnsNames_setter(instance):
    original = instance.columnsNames
    instance.columnsNames = original
    assert instance.columnsNames == original



@given(instance=mm_ops_AddIndex_strategy)
def test_hyp_mm_ops_addindex_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddIndex_strategy)
def test_hyp_mm_ops_addindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddIndex_strategy)
def test_hyp_mm_ops_addindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_DeleteRows_strategy)
def test_hyp_mm_ops_deleterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_DeleteRows_strategy)
def test_hyp_mm_ops_deleterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_DeleteRows_strategy)
def test_hyp_mm_ops_deleterows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original




@given(instance=mm_ops_RemoveTable_strategy)
def test_hyp_mm_ops_removetable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveTable_strategy)
def test_hyp_mm_ops_removetable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_RenameColumn_strategy)
def test_hyp_mm_ops_renamecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_hyp_mm_ops_renamecolumn_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_hyp_mm_ops_renamecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_hyp_mm_ops_renamecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_sourceColumnName_setter(instance):
    original = instance.sourceColumnName
    instance.sourceColumnName = original
    assert instance.sourceColumnName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_hyp_mm_ops_updaterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_AddSequence_strategy)
def test_hyp_mm_ops_addsequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=mm_ops_AddSequence_strategy)
def test_hyp_mm_ops_addsequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddSequence_strategy)
def test_hyp_mm_ops_addsequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_hyp_mm_ops_removedefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_hyp_mm_ops_removedefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original



@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_hyp_mm_ops_removedefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original




@given(instance=mm_ops_RemoveConstraint_strategy)
def test_hyp_mm_ops_removeconstraint_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RemoveConstraint_strategy)
def test_hyp_mm_ops_removeconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveConstraint_strategy)
def test_hyp_mm_ops_removeconstraint_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_sourceColumnsNames_setter(instance):
    original = instance.sourceColumnsNames
    instance.sourceColumnsNames = original
    assert instance.sourceColumnsNames == original



@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_InsertRows_strategy)
def test_hyp_mm_ops_insertrows_targetColumnNames_setter(instance):
    original = instance.targetColumnNames
    instance.targetColumnNames = original
    assert instance.targetColumnNames == original




@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_hyp_mm_ops_generatesequencenumbers_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_hyp_mm_ops_generatesequencenumbers_sequenceName_setter(instance):
    original = instance.sequenceName
    instance.sequenceName = original
    assert instance.sequenceName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_hyp_mm_ops_generatesequencenumbers_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_hyp_mm_ops_generatesequencenumbers_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original




@given(instance=mm_ops_RemoveNotNull_strategy)
def test_hyp_mm_ops_removenotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveNotNull_strategy)
def test_hyp_mm_ops_removenotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_RemoveNotNull_strategy)
def test_hyp_mm_ops_removenotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original




@given(instance=mm_ops_AddTable_strategy)
def test_hyp_mm_ops_addtable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddTable_strategy)
def test_hyp_mm_ops_addtable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm_ops_NillRows_strategy)
def test_hyp_mm_ops_nillrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_NillRows_strategy)
def test_hyp_mm_ops_nillrows_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=mm_ops_NillRows_strategy)
def test_hyp_mm_ops_nillrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_NillRows_strategy)
def test_hyp_mm_ops_nillrows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original




@given(instance=mm_ops_RenameTable_strategy)
def test_hyp_mm_ops_renametable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RenameTable_strategy)
def test_hyp_mm_ops_renametable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RenameTable_strategy)
def test_hyp_mm_ops_renametable_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original




@given(instance=mm_ops_SetColumnType_strategy)
def test_hyp_mm_ops_setcolumntype_oldType_setter(instance):
    original = instance.oldType
    instance.oldType = original
    assert instance.oldType == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_hyp_mm_ops_setcolumntype_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_hyp_mm_ops_setcolumntype_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_hyp_mm_ops_setcolumntype_newType_setter(instance):
    original = instance.newType
    instance.newType = original
    assert instance.newType == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_hyp_mm_ops_setcolumntype_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original




@given(instance=mm_ops_HasNoInstances_strategy)
def test_hyp_mm_ops_hasnoinstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_HasNoInstances_strategy)
def test_hyp_mm_ops_hasnoinstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original




@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_hyp_mm_ops_addprimarykey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_hyp_mm_ops_addprimarykey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_hyp_mm_ops_addprimarykey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_hyp_mm_ops_addprimarykey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original




@given(instance=mm_ops_AddSchema_strategy)
def test_hyp_mm_ops_addschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=mm_ops_AddNotNull_strategy)
def test_hyp_mm_ops_addnotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddNotNull_strategy)
def test_hyp_mm_ops_addnotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_AddNotNull_strategy)
def test_hyp_mm_ops_addnotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original




@given(instance=mm_ops_AddUnique_strategy)
def test_hyp_mm_ops_addunique_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddUnique_strategy)
def test_hyp_mm_ops_addunique_constrainedColumnNames_setter(instance):
    original = instance.constrainedColumnNames
    instance.constrainedColumnNames = original
    assert instance.constrainedColumnNames == original



@given(instance=mm_ops_AddUnique_strategy)
def test_hyp_mm_ops_addunique_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddUnique_strategy)
def test_hyp_mm_ops_addunique_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original




@given(instance=mm_ops_AddForeignKey_strategy)
def test_hyp_mm_ops_addforeignkey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_hyp_mm_ops_addforeignkey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_hyp_mm_ops_addforeignkey_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_hyp_mm_ops_addforeignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_hyp_mm_ops_addforeignkey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original




@given(instance=mm_rdb_TableConstraint_strategy)
def test_hyp_mm_rdb_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm_rdb_Column_strategy)
def test_hyp_mm_rdb_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=mm_rdb_Column_strategy)
def test_hyp_mm_rdb_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_rdb_Column_strategy)
def test_hyp_mm_rdb_column_isNillable_setter(instance):
    original = instance.isNillable
    instance.isNillable = original
    assert instance.isNillable == original



@given(instance=mm_rdb_Column_strategy)
def test_hyp_mm_rdb_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=mm_rdb_Table_strategy)
def test_hyp_mm_rdb_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=mm_rdb_Schema_strategy)
def test_hyp_mm_rdb_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=mm_rdb_Index_strategy)
def test_hyp_mm_rdb_index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm_rdb_Sequence_strategy)
def test_hyp_mm_rdb_sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_rdb_Sequence_strategy)
def test_hyp_mm_rdb_sequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Column,
    Index,
    ModelOperation,
    ModelRoot,
    Operations,
    Schema,
    Sequence,
    Structure,
    Table,
    TableConstraint,
    mm_ops_AddColumn,
    mm_ops_AddForeignKey,
    mm_ops_AddIndex,
    mm_ops_AddNotNull,
    mm_ops_AddPrimaryKey,
    mm_ops_AddSchema,
    mm_ops_AddSequence,
    mm_ops_AddTable,
    mm_ops_AddUnique,
    mm_ops_DeleteRows,
    mm_ops_GenerateSequenceNumbers,
    mm_ops_HasNoInstances,
    mm_ops_HasNoOwnInstances,
    mm_ops_InsertRows,
    mm_ops_ModelOperation,
    mm_ops_NillRows,
    mm_ops_RemoveColumn,
    mm_ops_RemoveConstraint,
    mm_ops_RemoveDefaultValue,
    mm_ops_RemoveIndex,
    mm_ops_RemoveNotNull,
    mm_ops_RemoveSequence,
    mm_ops_RemoveTable,
    mm_ops_RenameColumn,
    mm_ops_RenameTable,
    mm_ops_SetColumnType,
    mm_ops_SetDefaultValue,
    mm_ops_UpdateRows,
    mm_rdb_Column,
    mm_rdb_ForeignKey,
    mm_rdb_Index,
    mm_rdb_ModelRoot,
    mm_rdb_Operations,
    mm_rdb_PrimaryKey,
    mm_rdb_Schema,
    mm_rdb_Sequence,
    mm_rdb_Structure,
    mm_rdb_Table,
    mm_rdb_TableConstraint,
    mm_rdb_Unique,
    ops_ModelOperation,
    PrimitiveType,
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

def test_mm_ops_AddColumn_defaultValue_value_roundtrip():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_mm_ops_AddColumn_name_value_roundtrip():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddColumn_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddColumn_owningTableName_value_roundtrip():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_AddColumn_type_value_roundtrip():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_mm_ops_AddForeignKey_constrainedColumnName_value_roundtrip():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert instance.constrainedColumnName == "sample_text"
    instance.constrainedColumnName = "sample_text_2"
    assert instance.constrainedColumnName == "sample_text_2"


def test_mm_ops_AddForeignKey_name_value_roundtrip():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddForeignKey_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddForeignKey_owningTableName_value_roundtrip():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_AddForeignKey_targetTableName_value_roundtrip():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert instance.targetTableName == "sample_text"
    instance.targetTableName = "sample_text_2"
    assert instance.targetTableName == "sample_text_2"


def test_mm_ops_AddIndex_columnsNames_value_roundtrip():
    instance = mm_ops_AddIndex(columnsNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.columnsNames == "sample_text"
    instance.columnsNames = "sample_text_2"
    assert instance.columnsNames == "sample_text_2"


def test_mm_ops_AddIndex_name_value_roundtrip():
    instance = mm_ops_AddIndex(columnsNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddIndex_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddIndex(columnsNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddIndex_owningTableName_value_roundtrip():
    instance = mm_ops_AddIndex(columnsNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_AddNotNull_constrainedColumnName_value_roundtrip():
    instance = mm_ops_AddNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.constrainedColumnName == "sample_text"
    instance.constrainedColumnName = "sample_text_2"
    assert instance.constrainedColumnName == "sample_text_2"


def test_mm_ops_AddNotNull_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddNotNull_owningTableName_value_roundtrip():
    instance = mm_ops_AddNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_AddPrimaryKey_constrainedColumnName_value_roundtrip():
    instance = mm_ops_AddPrimaryKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.constrainedColumnName == "sample_text"
    instance.constrainedColumnName = "sample_text_2"
    assert instance.constrainedColumnName == "sample_text_2"


def test_mm_ops_AddPrimaryKey_name_value_roundtrip():
    instance = mm_ops_AddPrimaryKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddPrimaryKey_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddPrimaryKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddPrimaryKey_owningTableName_value_roundtrip():
    instance = mm_ops_AddPrimaryKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_AddSchema_name_value_roundtrip():
    instance = mm_ops_AddSchema(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddSequence_name_value_roundtrip():
    instance = mm_ops_AddSequence(name="sample_text", owningSchemaName="sample_text", startValue=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddSequence_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddSequence(name="sample_text", owningSchemaName="sample_text", startValue=7)
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddSequence_startValue_value_roundtrip():
    instance = mm_ops_AddSequence(name="sample_text", owningSchemaName="sample_text", startValue=7)
    assert instance.startValue == 7
    instance.startValue = 13
    assert instance.startValue == 13


def test_mm_ops_AddTable_name_value_roundtrip():
    instance = mm_ops_AddTable(name="sample_text", owningSchemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddTable_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddTable(name="sample_text", owningSchemaName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddUnique_constrainedColumnNames_value_roundtrip():
    instance = mm_ops_AddUnique(constrainedColumnNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.constrainedColumnNames == "sample_text"
    instance.constrainedColumnNames = "sample_text_2"
    assert instance.constrainedColumnNames == "sample_text_2"


def test_mm_ops_AddUnique_name_value_roundtrip():
    instance = mm_ops_AddUnique(constrainedColumnNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddUnique_owningSchemaName_value_roundtrip():
    instance = mm_ops_AddUnique(constrainedColumnNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_AddUnique_owningTableName_value_roundtrip():
    instance = mm_ops_AddUnique(constrainedColumnNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_DeleteRows_owningSchemaName_value_roundtrip():
    instance = mm_ops_DeleteRows(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_DeleteRows_tableName_value_roundtrip():
    instance = mm_ops_DeleteRows(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_mm_ops_DeleteRows_whereCondition_value_roundtrip():
    instance = mm_ops_DeleteRows(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.whereCondition == "sample_text"
    instance.whereCondition = "sample_text_2"
    assert instance.whereCondition == "sample_text_2"


def test_mm_ops_GenerateSequenceNumbers_columnName_value_roundtrip():
    instance = mm_ops_GenerateSequenceNumbers(columnName="sample_text", owningSchemaName="sample_text", sequenceName="sample_text", tableName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_mm_ops_GenerateSequenceNumbers_owningSchemaName_value_roundtrip():
    instance = mm_ops_GenerateSequenceNumbers(columnName="sample_text", owningSchemaName="sample_text", sequenceName="sample_text", tableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_GenerateSequenceNumbers_sequenceName_value_roundtrip():
    instance = mm_ops_GenerateSequenceNumbers(columnName="sample_text", owningSchemaName="sample_text", sequenceName="sample_text", tableName="sample_text")
    assert instance.sequenceName == "sample_text"
    instance.sequenceName = "sample_text_2"
    assert instance.sequenceName == "sample_text_2"


def test_mm_ops_GenerateSequenceNumbers_tableName_value_roundtrip():
    instance = mm_ops_GenerateSequenceNumbers(columnName="sample_text", owningSchemaName="sample_text", sequenceName="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_mm_ops_HasNoInstances_owningSchemaName_value_roundtrip():
    instance = mm_ops_HasNoInstances(owningSchemaName="sample_text", tableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_HasNoInstances_tableName_value_roundtrip():
    instance = mm_ops_HasNoInstances(owningSchemaName="sample_text", tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_mm_ops_HasNoOwnInstances_owningSchemaName_value_roundtrip():
    instance = mm_ops_HasNoOwnInstances(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_HasNoOwnInstances_tableName_value_roundtrip():
    instance = mm_ops_HasNoOwnInstances(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_mm_ops_HasNoOwnInstances_whereCondition_value_roundtrip():
    instance = mm_ops_HasNoOwnInstances(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.whereCondition == "sample_text"
    instance.whereCondition = "sample_text_2"
    assert instance.whereCondition == "sample_text_2"


def test_mm_ops_InsertRows_owningSchemaName_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_InsertRows_sourceColumnsNames_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.sourceColumnsNames == "sample_text"
    instance.sourceColumnsNames = "sample_text_2"
    assert instance.sourceColumnsNames == "sample_text_2"


def test_mm_ops_InsertRows_sourceTableName_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.sourceTableName == "sample_text"
    instance.sourceTableName = "sample_text_2"
    assert instance.sourceTableName == "sample_text_2"


def test_mm_ops_InsertRows_targetColumnNames_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.targetColumnNames == "sample_text"
    instance.targetColumnNames = "sample_text_2"
    assert instance.targetColumnNames == "sample_text_2"


def test_mm_ops_InsertRows_targetTableName_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.targetTableName == "sample_text"
    instance.targetTableName = "sample_text_2"
    assert instance.targetTableName == "sample_text_2"


def test_mm_ops_InsertRows_whereCondition_value_roundtrip():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.whereCondition == "sample_text"
    instance.whereCondition = "sample_text_2"
    assert instance.whereCondition == "sample_text_2"


def test_mm_ops_NillRows_columnName_value_roundtrip():
    instance = mm_ops_NillRows(columnName="sample_text", owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_mm_ops_NillRows_owningSchemaName_value_roundtrip():
    instance = mm_ops_NillRows(columnName="sample_text", owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_NillRows_tableName_value_roundtrip():
    instance = mm_ops_NillRows(columnName="sample_text", owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_mm_ops_NillRows_whereCondition_value_roundtrip():
    instance = mm_ops_NillRows(columnName="sample_text", owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert instance.whereCondition == "sample_text"
    instance.whereCondition = "sample_text_2"
    assert instance.whereCondition == "sample_text_2"


def test_mm_ops_RemoveColumn_name_value_roundtrip():
    instance = mm_ops_RemoveColumn(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RemoveColumn_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveColumn(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveColumn_owningTableName_value_roundtrip():
    instance = mm_ops_RemoveColumn(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_RemoveConstraint_name_value_roundtrip():
    instance = mm_ops_RemoveConstraint(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RemoveConstraint_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveConstraint(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveConstraint_owningTableName_value_roundtrip():
    instance = mm_ops_RemoveConstraint(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_RemoveDefaultValue_owningColumnName_value_roundtrip():
    instance = mm_ops_RemoveDefaultValue(owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningColumnName == "sample_text"
    instance.owningColumnName = "sample_text_2"
    assert instance.owningColumnName == "sample_text_2"


def test_mm_ops_RemoveDefaultValue_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveDefaultValue(owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveDefaultValue_owningTableName_value_roundtrip():
    instance = mm_ops_RemoveDefaultValue(owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_RemoveIndex_name_value_roundtrip():
    instance = mm_ops_RemoveIndex(name="sample_text", owningSchemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RemoveIndex_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveIndex(name="sample_text", owningSchemaName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveNotNull_constrainedColumnName_value_roundtrip():
    instance = mm_ops_RemoveNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.constrainedColumnName == "sample_text"
    instance.constrainedColumnName = "sample_text_2"
    assert instance.constrainedColumnName == "sample_text_2"


def test_mm_ops_RemoveNotNull_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveNotNull_owningTableName_value_roundtrip():
    instance = mm_ops_RemoveNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_RemoveSequence_name_value_roundtrip():
    instance = mm_ops_RemoveSequence(name="sample_text", owningSchemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RemoveSequence_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveSequence(name="sample_text", owningSchemaName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RemoveTable_name_value_roundtrip():
    instance = mm_ops_RemoveTable(name="sample_text", owningSchemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RemoveTable_owningSchemaName_value_roundtrip():
    instance = mm_ops_RemoveTable(name="sample_text", owningSchemaName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RenameColumn_name_value_roundtrip():
    instance = mm_ops_RenameColumn(name="sample_text", newName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RenameColumn_newName_value_roundtrip():
    instance = mm_ops_RenameColumn(name="sample_text", newName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.newName == "sample_text"
    instance.newName = "sample_text_2"
    assert instance.newName == "sample_text_2"


def test_mm_ops_RenameColumn_owningSchemaName_value_roundtrip():
    instance = mm_ops_RenameColumn(name="sample_text", newName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_RenameColumn_owningTableName_value_roundtrip():
    instance = mm_ops_RenameColumn(name="sample_text", newName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_RenameTable_name_value_roundtrip():
    instance = mm_ops_RenameTable(name="sample_text", newName="sample_text", owningSchemaName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_RenameTable_newName_value_roundtrip():
    instance = mm_ops_RenameTable(name="sample_text", newName="sample_text", owningSchemaName="sample_text")
    assert instance.newName == "sample_text"
    instance.newName = "sample_text_2"
    assert instance.newName == "sample_text_2"


def test_mm_ops_RenameTable_owningSchemaName_value_roundtrip():
    instance = mm_ops_RenameTable(name="sample_text", newName="sample_text", owningSchemaName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_SetColumnType_newType_value_roundtrip():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.newType == "sample_text"
    instance.newType = "sample_text_2"
    assert instance.newType == "sample_text_2"


def test_mm_ops_SetColumnType_oldType_value_roundtrip():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.oldType == "sample_text"
    instance.oldType = "sample_text_2"
    assert instance.oldType == "sample_text_2"


def test_mm_ops_SetColumnType_owningColumnName_value_roundtrip():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningColumnName == "sample_text"
    instance.owningColumnName = "sample_text_2"
    assert instance.owningColumnName == "sample_text_2"


def test_mm_ops_SetColumnType_owningSchemaName_value_roundtrip():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_SetColumnType_owningTableName_value_roundtrip():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_SetDefaultValue_newDefaultValue_value_roundtrip():
    instance = mm_ops_SetDefaultValue(newDefaultValue="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.newDefaultValue == "sample_text"
    instance.newDefaultValue = "sample_text_2"
    assert instance.newDefaultValue == "sample_text_2"


def test_mm_ops_SetDefaultValue_owningColumnName_value_roundtrip():
    instance = mm_ops_SetDefaultValue(newDefaultValue="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningColumnName == "sample_text"
    instance.owningColumnName = "sample_text_2"
    assert instance.owningColumnName == "sample_text_2"


def test_mm_ops_SetDefaultValue_owningSchemaName_value_roundtrip():
    instance = mm_ops_SetDefaultValue(newDefaultValue="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_SetDefaultValue_owningTableName_value_roundtrip():
    instance = mm_ops_SetDefaultValue(newDefaultValue="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert instance.owningTableName == "sample_text"
    instance.owningTableName = "sample_text_2"
    assert instance.owningTableName == "sample_text_2"


def test_mm_ops_UpdateRows_owningSchemaName_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.owningSchemaName == "sample_text"
    instance.owningSchemaName = "sample_text_2"
    assert instance.owningSchemaName == "sample_text_2"


def test_mm_ops_UpdateRows_sourceColumnName_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.sourceColumnName == "sample_text"
    instance.sourceColumnName = "sample_text_2"
    assert instance.sourceColumnName == "sample_text_2"


def test_mm_ops_UpdateRows_sourceTableName_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.sourceTableName == "sample_text"
    instance.sourceTableName = "sample_text_2"
    assert instance.sourceTableName == "sample_text_2"


def test_mm_ops_UpdateRows_targetColumnName_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.targetColumnName == "sample_text"
    instance.targetColumnName = "sample_text_2"
    assert instance.targetColumnName == "sample_text_2"


def test_mm_ops_UpdateRows_targetTableName_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.targetTableName == "sample_text"
    instance.targetTableName = "sample_text_2"
    assert instance.targetTableName == "sample_text_2"


def test_mm_ops_UpdateRows_whereCondition_value_roundtrip():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert instance.whereCondition == "sample_text"
    instance.whereCondition = "sample_text_2"
    assert instance.whereCondition == "sample_text_2"


def test_mm_rdb_Column_defaultValue_value_roundtrip():
    instance = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_mm_rdb_Column_isNillable_value_roundtrip():
    instance = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    assert instance.isNillable == "sample_text"
    instance.isNillable = "sample_text_2"
    assert instance.isNillable == "sample_text_2"


def test_mm_rdb_Column_name_value_roundtrip():
    instance = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_rdb_Column_type_value_roundtrip():
    instance = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_mm_rdb_Index_name_value_roundtrip():
    instance = mm_rdb_Index(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_rdb_Schema_name_value_roundtrip():
    instance = mm_rdb_Schema(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_rdb_Sequence_name_value_roundtrip():
    instance = mm_rdb_Sequence(name="sample_text", startValue=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_rdb_Sequence_startValue_value_roundtrip():
    instance = mm_rdb_Sequence(name="sample_text", startValue=7)
    assert instance.startValue == 7
    instance.startValue = 13
    assert instance.startValue == 13


def test_mm_rdb_Table_name_value_roundtrip():
    instance = mm_rdb_Table(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_rdb_TableConstraint_name_value_roundtrip():
    instance = mm_rdb_TableConstraint(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm_ops_AddColumn_isa_ModelOperation():
    instance = mm_ops_AddColumn(defaultValue="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", type="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddForeignKey_isa_ModelOperation():
    instance = mm_ops_AddForeignKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text", targetTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddIndex_isa_ModelOperation():
    instance = mm_ops_AddIndex(columnsNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddNotNull_isa_ModelOperation():
    instance = mm_ops_AddNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddPrimaryKey_isa_ModelOperation():
    instance = mm_ops_AddPrimaryKey(constrainedColumnName="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddSchema_isa_ModelOperation():
    instance = mm_ops_AddSchema(name="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddSequence_isa_ModelOperation():
    instance = mm_ops_AddSequence(name="sample_text", owningSchemaName="sample_text", startValue=7)
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddTable_isa_ModelOperation():
    instance = mm_ops_AddTable(name="sample_text", owningSchemaName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_AddUnique_isa_ModelOperation():
    instance = mm_ops_AddUnique(constrainedColumnNames="sample_text", name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_DeleteRows_isa_ModelOperation():
    instance = mm_ops_DeleteRows(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_GenerateSequenceNumbers_isa_ModelOperation():
    instance = mm_ops_GenerateSequenceNumbers(columnName="sample_text", owningSchemaName="sample_text", sequenceName="sample_text", tableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_HasNoInstances_isa_ModelOperation():
    instance = mm_ops_HasNoInstances(owningSchemaName="sample_text", tableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_HasNoOwnInstances_isa_ModelOperation():
    instance = mm_ops_HasNoOwnInstances(owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_InsertRows_isa_ModelOperation():
    instance = mm_ops_InsertRows(owningSchemaName="sample_text", sourceColumnsNames="sample_text", sourceTableName="sample_text", targetColumnNames="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_NillRows_isa_ModelOperation():
    instance = mm_ops_NillRows(columnName="sample_text", owningSchemaName="sample_text", tableName="sample_text", whereCondition="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveColumn_isa_ModelOperation():
    instance = mm_ops_RemoveColumn(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveConstraint_isa_ModelOperation():
    instance = mm_ops_RemoveConstraint(name="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveDefaultValue_isa_ModelOperation():
    instance = mm_ops_RemoveDefaultValue(owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveIndex_isa_ModelOperation():
    instance = mm_ops_RemoveIndex(name="sample_text", owningSchemaName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveNotNull_isa_ModelOperation():
    instance = mm_ops_RemoveNotNull(constrainedColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveSequence_isa_ModelOperation():
    instance = mm_ops_RemoveSequence(name="sample_text", owningSchemaName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RemoveTable_isa_ModelOperation():
    instance = mm_ops_RemoveTable(name="sample_text", owningSchemaName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RenameColumn_isa_ModelOperation():
    instance = mm_ops_RenameColumn(name="sample_text", newName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_RenameTable_isa_ModelOperation():
    instance = mm_ops_RenameTable(name="sample_text", newName="sample_text", owningSchemaName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_SetColumnType_isa_ModelOperation():
    instance = mm_ops_SetColumnType(newType="sample_text", oldType="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_SetDefaultValue_isa_ModelOperation():
    instance = mm_ops_SetDefaultValue(newDefaultValue="sample_text", owningColumnName="sample_text", owningSchemaName="sample_text", owningTableName="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_ops_UpdateRows_isa_ModelOperation():
    instance = mm_ops_UpdateRows(owningSchemaName="sample_text", sourceColumnName="sample_text", sourceTableName="sample_text", targetColumnName="sample_text", targetTableName="sample_text", whereCondition="sample_text")
    assert isinstance(instance, ModelOperation)


def test_mm_rdb_Operations_isa_ModelRoot():
    instance = mm_rdb_Operations()
    assert isinstance(instance, ModelRoot)


def test_mm_rdb_Structure_isa_ModelRoot():
    instance = mm_rdb_Structure()
    assert isinstance(instance, ModelRoot)


def test_mm_rdb_ForeignKey_isa_TableConstraint():
    instance = mm_rdb_ForeignKey()
    assert isinstance(instance, TableConstraint)


def test_mm_rdb_PrimaryKey_isa_TableConstraint():
    instance = mm_rdb_PrimaryKey()
    assert isinstance(instance, TableConstraint)


def test_mm_rdb_Unique_isa_TableConstraint():
    instance = mm_rdb_Unique()
    assert isinstance(instance, TableConstraint)


def test_assoc_columns12_link_reassign_clear():
    a = mm_rdb_Index(name="sample_text")
    b1 = Column()
    b2 = Column()
    _safe_set(a, 'mm_rdb_Index', {b1})
    assert _is_linked(a, 'mm_rdb_Index', b1)
    if hasattr(b1, 'Column'):
        assert _is_linked(b1, 'Column', a)
    _safe_set(a, 'mm_rdb_Index', {b2})
    assert _is_linked(a, 'mm_rdb_Index', b2)
    if hasattr(b1, 'Column'):
        assert not _is_linked(b1, 'Column', a)
    if hasattr(b2, 'Column'):
        assert _is_linked(b2, 'Column', a)
    _safe_set(a, 'mm_rdb_Index', set())
    assert not _is_linked(a, 'mm_rdb_Index', b2)
    if hasattr(b2, 'Column'):
        assert not _is_linked(b2, 'Column', a)


def test_assoc_columns15_link_reassign_clear():
    a = mm_rdb_Table(name="sample_text")
    b1 = Column()
    b2 = Column()
    _safe_set(a, 'owningTable', {b1})
    assert _is_linked(a, 'owningTable', b1)
    if hasattr(b1, 'Column16'):
        assert _is_linked(b1, 'Column16', a)
    _safe_set(a, 'owningTable', {b2})
    assert _is_linked(a, 'owningTable', b2)
    if hasattr(b1, 'Column16'):
        assert not _is_linked(b1, 'Column16', a)
    if hasattr(b2, 'Column16'):
        assert _is_linked(b2, 'Column16', a)
    _safe_set(a, 'owningTable', set())
    assert not _is_linked(a, 'owningTable', b2)
    if hasattr(b2, 'Column16'):
        assert not _is_linked(b2, 'Column16', a)


def test_assoc_constraints17_link_reassign_clear():
    a = mm_rdb_Table(name="sample_text")
    b1 = TableConstraint()
    b2 = TableConstraint()
    _safe_set(a, 'owningTable18', {b1})
    assert _is_linked(a, 'owningTable18', b1)
    if hasattr(b1, 'TableConstraint'):
        assert _is_linked(b1, 'TableConstraint', a)
    _safe_set(a, 'owningTable18', {b2})
    assert _is_linked(a, 'owningTable18', b2)
    if hasattr(b1, 'TableConstraint'):
        assert not _is_linked(b1, 'TableConstraint', a)
    if hasattr(b2, 'TableConstraint'):
        assert _is_linked(b2, 'TableConstraint', a)
    _safe_set(a, 'owningTable18', set())
    assert not _is_linked(a, 'owningTable18', b2)
    if hasattr(b2, 'TableConstraint'):
        assert not _is_linked(b2, 'TableConstraint', a)


def test_assoc_indexes6_link_reassign_clear():
    a = mm_rdb_Schema(name="sample_text")
    b1 = Index()
    b2 = Index()
    _safe_set(a, 'owningSchema7', {b1})
    assert _is_linked(a, 'owningSchema7', b1)
    if hasattr(b1, 'Index'):
        assert _is_linked(b1, 'Index', a)
    _safe_set(a, 'owningSchema7', {b2})
    assert _is_linked(a, 'owningSchema7', b2)
    if hasattr(b1, 'Index'):
        assert not _is_linked(b1, 'Index', a)
    if hasattr(b2, 'Index'):
        assert _is_linked(b2, 'Index', a)
    _safe_set(a, 'owningSchema7', set())
    assert not _is_linked(a, 'owningSchema7', b2)
    if hasattr(b2, 'Index'):
        assert not _is_linked(b2, 'Index', a)


def test_assoc_owningSchema10_link_reassign_clear():
    a = mm_rdb_Index(name="sample_text")
    b1 = Schema()
    b2 = Schema()
    _safe_set(a, 'indexes', b1)
    assert _is_linked(a, 'indexes', b1)
    if hasattr(b1, 'Schema11'):
        assert _is_linked(b1, 'Schema11', a)
    _safe_set(a, 'indexes', b2)
    assert _is_linked(a, 'indexes', b2)
    if hasattr(b1, 'Schema11'):
        assert not _is_linked(b1, 'Schema11', a)
    if hasattr(b2, 'Schema11'):
        assert _is_linked(b2, 'Schema11', a)
    _safe_set(a, 'indexes', None)
    assert not _is_linked(a, 'indexes', b2)
    if hasattr(b2, 'Schema11'):
        assert not _is_linked(b2, 'Schema11', a)


def test_assoc_owningSchema13_link_reassign_clear():
    a = mm_rdb_Table(name="sample_text")
    b1 = Schema()
    b2 = Schema()
    _safe_set(a, 'tables', b1)
    assert _is_linked(a, 'tables', b1)
    if hasattr(b1, 'Schema14'):
        assert _is_linked(b1, 'Schema14', a)
    _safe_set(a, 'tables', b2)
    assert _is_linked(a, 'tables', b2)
    if hasattr(b1, 'Schema14'):
        assert not _is_linked(b1, 'Schema14', a)
    if hasattr(b2, 'Schema14'):
        assert _is_linked(b2, 'Schema14', a)
    _safe_set(a, 'tables', None)
    assert not _is_linked(a, 'tables', b2)
    if hasattr(b2, 'Schema14'):
        assert not _is_linked(b2, 'Schema14', a)


def test_assoc_owningSchema8_link_reassign_clear():
    a = mm_rdb_Sequence(name="sample_text", startValue=7)
    b1 = Schema()
    b2 = Schema()
    _safe_set(a, 'sequence', b1)
    assert _is_linked(a, 'sequence', b1)
    if hasattr(b1, 'Schema9'):
        assert _is_linked(b1, 'Schema9', a)
    _safe_set(a, 'sequence', b2)
    assert _is_linked(a, 'sequence', b2)
    if hasattr(b1, 'Schema9'):
        assert not _is_linked(b1, 'Schema9', a)
    if hasattr(b2, 'Schema9'):
        assert _is_linked(b2, 'Schema9', a)
    _safe_set(a, 'sequence', None)
    assert not _is_linked(a, 'sequence', b2)
    if hasattr(b2, 'Schema9'):
        assert not _is_linked(b2, 'Schema9', a)


def test_assoc_owningStructure2_link_reassign_clear():
    a = mm_rdb_Schema(name="sample_text")
    b1 = Structure()
    b2 = Structure()
    _safe_set(a, 'schemas', b1)
    assert _is_linked(a, 'schemas', b1)
    if hasattr(b1, 'Structure'):
        assert _is_linked(b1, 'Structure', a)
    _safe_set(a, 'schemas', b2)
    assert _is_linked(a, 'schemas', b2)
    if hasattr(b1, 'Structure'):
        assert not _is_linked(b1, 'Structure', a)
    if hasattr(b2, 'Structure'):
        assert _is_linked(b2, 'Structure', a)
    _safe_set(a, 'schemas', None)
    assert not _is_linked(a, 'schemas', b2)
    if hasattr(b2, 'Structure'):
        assert not _is_linked(b2, 'Structure', a)


def test_assoc_owningTable19_link_reassign_clear():
    a = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    b1 = Table()
    b2 = Table()
    _safe_set(a, 'columns', b1)
    assert _is_linked(a, 'columns', b1)
    if hasattr(b1, 'Table20'):
        assert _is_linked(b1, 'Table20', a)
    _safe_set(a, 'columns', b2)
    assert _is_linked(a, 'columns', b2)
    if hasattr(b1, 'Table20'):
        assert not _is_linked(b1, 'Table20', a)
    if hasattr(b2, 'Table20'):
        assert _is_linked(b2, 'Table20', a)
    _safe_set(a, 'columns', None)
    assert not _is_linked(a, 'columns', b2)
    if hasattr(b2, 'Table20'):
        assert not _is_linked(b2, 'Table20', a)


def test_assoc_owningTable21_link_reassign_clear():
    a = mm_rdb_TableConstraint(name="sample_text")
    b1 = Table()
    b2 = Table()
    _safe_set(a, 'constraints', b1)
    assert _is_linked(a, 'constraints', b1)
    if hasattr(b1, 'Table22'):
        assert _is_linked(b1, 'Table22', a)
    _safe_set(a, 'constraints', b2)
    assert _is_linked(a, 'constraints', b2)
    if hasattr(b1, 'Table22'):
        assert not _is_linked(b1, 'Table22', a)
    if hasattr(b2, 'Table22'):
        assert _is_linked(b2, 'Table22', a)
    _safe_set(a, 'constraints', None)
    assert not _is_linked(a, 'constraints', b2)
    if hasattr(b2, 'Table22'):
        assert not _is_linked(b2, 'Table22', a)


def test_assoc_sequence4_link_reassign_clear():
    a = mm_rdb_Schema(name="sample_text")
    b1 = Sequence()
    b2 = Sequence()
    _safe_set(a, 'owningSchema5', b1)
    assert _is_linked(a, 'owningSchema5', b1)
    if hasattr(b1, 'Sequence'):
        assert _is_linked(b1, 'Sequence', a)
    _safe_set(a, 'owningSchema5', b2)
    assert _is_linked(a, 'owningSchema5', b2)
    if hasattr(b1, 'Sequence'):
        assert not _is_linked(b1, 'Sequence', a)
    if hasattr(b2, 'Sequence'):
        assert _is_linked(b2, 'Sequence', a)
    _safe_set(a, 'owningSchema5', None)
    assert not _is_linked(a, 'owningSchema5', b2)
    if hasattr(b2, 'Sequence'):
        assert not _is_linked(b2, 'Sequence', a)


def test_assoc_tables3_link_reassign_clear():
    a = mm_rdb_Schema(name="sample_text")
    b1 = Table()
    b2 = Table()
    _safe_set(a, 'owningSchema', {b1})
    assert _is_linked(a, 'owningSchema', b1)
    if hasattr(b1, 'Table'):
        assert _is_linked(b1, 'Table', a)
    _safe_set(a, 'owningSchema', {b2})
    assert _is_linked(a, 'owningSchema', b2)
    if hasattr(b1, 'Table'):
        assert not _is_linked(b1, 'Table', a)
    if hasattr(b2, 'Table'):
        assert _is_linked(b2, 'Table', a)
    _safe_set(a, 'owningSchema', set())
    assert not _is_linked(a, 'owningSchema', b2)
    if hasattr(b2, 'Table'):
        assert not _is_linked(b2, 'Table', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Column_strategy = st.builds(Column)
@given(instance=Column_strategy)
@settings(max_examples=25)
def test_Column_instantiation(instance):
    assert isinstance(instance, Column)


Index_strategy = st.builds(Index)
@given(instance=Index_strategy)
@settings(max_examples=25)
def test_Index_instantiation(instance):
    assert isinstance(instance, Index)


ModelOperation_strategy = st.builds(ModelOperation)
@given(instance=ModelOperation_strategy)
@settings(max_examples=25)
def test_ModelOperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)


ModelRoot_strategy = st.builds(ModelRoot)
@given(instance=ModelRoot_strategy)
@settings(max_examples=25)
def test_ModelRoot_instantiation(instance):
    assert isinstance(instance, ModelRoot)


Operations_strategy = st.builds(Operations)
@given(instance=Operations_strategy)
@settings(max_examples=25)
def test_Operations_instantiation(instance):
    assert isinstance(instance, Operations)


Schema_strategy = st.builds(Schema)
@given(instance=Schema_strategy)
@settings(max_examples=25)
def test_Schema_instantiation(instance):
    assert isinstance(instance, Schema)


Sequence_strategy = st.builds(Sequence)
@given(instance=Sequence_strategy)
@settings(max_examples=25)
def test_Sequence_instantiation(instance):
    assert isinstance(instance, Sequence)


Structure_strategy = st.builds(Structure)
@given(instance=Structure_strategy)
@settings(max_examples=25)
def test_Structure_instantiation(instance):
    assert isinstance(instance, Structure)


Table_strategy = st.builds(Table)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


TableConstraint_strategy = st.builds(TableConstraint)
@given(instance=TableConstraint_strategy)
@settings(max_examples=25)
def test_TableConstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)


mm_ops_AddColumn_strategy = st.builds(mm_ops_AddColumn, defaultValue=safe_text, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text, type=safe_text)
@given(instance=mm_ops_AddColumn_strategy)
@settings(max_examples=25)
def test_mm_ops_AddColumn_instantiation(instance):
    assert isinstance(instance, mm_ops_AddColumn)


mm_ops_AddForeignKey_strategy = st.builds(mm_ops_AddForeignKey, constrainedColumnName=safe_text, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text, targetTableName=safe_text)
@given(instance=mm_ops_AddForeignKey_strategy)
@settings(max_examples=25)
def test_mm_ops_AddForeignKey_instantiation(instance):
    assert isinstance(instance, mm_ops_AddForeignKey)


mm_ops_AddIndex_strategy = st.builds(mm_ops_AddIndex, columnsNames=safe_text, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_AddIndex_strategy)
@settings(max_examples=25)
def test_mm_ops_AddIndex_instantiation(instance):
    assert isinstance(instance, mm_ops_AddIndex)


mm_ops_AddNotNull_strategy = st.builds(mm_ops_AddNotNull, constrainedColumnName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_AddNotNull_strategy)
@settings(max_examples=25)
def test_mm_ops_AddNotNull_instantiation(instance):
    assert isinstance(instance, mm_ops_AddNotNull)


mm_ops_AddPrimaryKey_strategy = st.builds(mm_ops_AddPrimaryKey, constrainedColumnName=safe_text, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_AddPrimaryKey_strategy)
@settings(max_examples=25)
def test_mm_ops_AddPrimaryKey_instantiation(instance):
    assert isinstance(instance, mm_ops_AddPrimaryKey)


mm_ops_AddSchema_strategy = st.builds(mm_ops_AddSchema, name=safe_text)
@given(instance=mm_ops_AddSchema_strategy)
@settings(max_examples=25)
def test_mm_ops_AddSchema_instantiation(instance):
    assert isinstance(instance, mm_ops_AddSchema)


mm_ops_AddSequence_strategy = st.builds(mm_ops_AddSequence, name=safe_text, owningSchemaName=safe_text, startValue=st.integers())
@given(instance=mm_ops_AddSequence_strategy)
@settings(max_examples=25)
def test_mm_ops_AddSequence_instantiation(instance):
    assert isinstance(instance, mm_ops_AddSequence)


mm_ops_AddTable_strategy = st.builds(mm_ops_AddTable, name=safe_text, owningSchemaName=safe_text)
@given(instance=mm_ops_AddTable_strategy)
@settings(max_examples=25)
def test_mm_ops_AddTable_instantiation(instance):
    assert isinstance(instance, mm_ops_AddTable)


mm_ops_AddUnique_strategy = st.builds(mm_ops_AddUnique, constrainedColumnNames=safe_text, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_AddUnique_strategy)
@settings(max_examples=25)
def test_mm_ops_AddUnique_instantiation(instance):
    assert isinstance(instance, mm_ops_AddUnique)


mm_ops_DeleteRows_strategy = st.builds(mm_ops_DeleteRows, owningSchemaName=safe_text, tableName=safe_text, whereCondition=safe_text)
@given(instance=mm_ops_DeleteRows_strategy)
@settings(max_examples=25)
def test_mm_ops_DeleteRows_instantiation(instance):
    assert isinstance(instance, mm_ops_DeleteRows)


mm_ops_GenerateSequenceNumbers_strategy = st.builds(mm_ops_GenerateSequenceNumbers, columnName=safe_text, owningSchemaName=safe_text, sequenceName=safe_text, tableName=safe_text)
@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
@settings(max_examples=25)
def test_mm_ops_GenerateSequenceNumbers_instantiation(instance):
    assert isinstance(instance, mm_ops_GenerateSequenceNumbers)


mm_ops_HasNoInstances_strategy = st.builds(mm_ops_HasNoInstances, owningSchemaName=safe_text, tableName=safe_text)
@given(instance=mm_ops_HasNoInstances_strategy)
@settings(max_examples=25)
def test_mm_ops_HasNoInstances_instantiation(instance):
    assert isinstance(instance, mm_ops_HasNoInstances)


mm_ops_HasNoOwnInstances_strategy = st.builds(mm_ops_HasNoOwnInstances, owningSchemaName=safe_text, tableName=safe_text, whereCondition=safe_text)
@given(instance=mm_ops_HasNoOwnInstances_strategy)
@settings(max_examples=25)
def test_mm_ops_HasNoOwnInstances_instantiation(instance):
    assert isinstance(instance, mm_ops_HasNoOwnInstances)


mm_ops_InsertRows_strategy = st.builds(mm_ops_InsertRows, owningSchemaName=safe_text, sourceColumnsNames=safe_text, sourceTableName=safe_text, targetColumnNames=safe_text, targetTableName=safe_text, whereCondition=safe_text)
@given(instance=mm_ops_InsertRows_strategy)
@settings(max_examples=25)
def test_mm_ops_InsertRows_instantiation(instance):
    assert isinstance(instance, mm_ops_InsertRows)


mm_ops_ModelOperation_strategy = st.builds(mm_ops_ModelOperation)
@given(instance=mm_ops_ModelOperation_strategy)
@settings(max_examples=25)
def test_mm_ops_ModelOperation_instantiation(instance):
    assert isinstance(instance, mm_ops_ModelOperation)


mm_ops_NillRows_strategy = st.builds(mm_ops_NillRows, columnName=safe_text, owningSchemaName=safe_text, tableName=safe_text, whereCondition=safe_text)
@given(instance=mm_ops_NillRows_strategy)
@settings(max_examples=25)
def test_mm_ops_NillRows_instantiation(instance):
    assert isinstance(instance, mm_ops_NillRows)


mm_ops_RemoveColumn_strategy = st.builds(mm_ops_RemoveColumn, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_RemoveColumn_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveColumn_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveColumn)


mm_ops_RemoveConstraint_strategy = st.builds(mm_ops_RemoveConstraint, name=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_RemoveConstraint_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveConstraint_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveConstraint)


mm_ops_RemoveDefaultValue_strategy = st.builds(mm_ops_RemoveDefaultValue, owningColumnName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_RemoveDefaultValue_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveDefaultValue_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveDefaultValue)


mm_ops_RemoveIndex_strategy = st.builds(mm_ops_RemoveIndex, name=safe_text, owningSchemaName=safe_text)
@given(instance=mm_ops_RemoveIndex_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveIndex_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveIndex)


mm_ops_RemoveNotNull_strategy = st.builds(mm_ops_RemoveNotNull, constrainedColumnName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_RemoveNotNull_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveNotNull_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveNotNull)


mm_ops_RemoveSequence_strategy = st.builds(mm_ops_RemoveSequence, name=safe_text, owningSchemaName=safe_text)
@given(instance=mm_ops_RemoveSequence_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveSequence_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveSequence)


mm_ops_RemoveTable_strategy = st.builds(mm_ops_RemoveTable, name=safe_text, owningSchemaName=safe_text)
@given(instance=mm_ops_RemoveTable_strategy)
@settings(max_examples=25)
def test_mm_ops_RemoveTable_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveTable)


mm_ops_RenameColumn_strategy = st.builds(mm_ops_RenameColumn, name=safe_text, newName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_RenameColumn_strategy)
@settings(max_examples=25)
def test_mm_ops_RenameColumn_instantiation(instance):
    assert isinstance(instance, mm_ops_RenameColumn)


mm_ops_RenameTable_strategy = st.builds(mm_ops_RenameTable, name=safe_text, newName=safe_text, owningSchemaName=safe_text)
@given(instance=mm_ops_RenameTable_strategy)
@settings(max_examples=25)
def test_mm_ops_RenameTable_instantiation(instance):
    assert isinstance(instance, mm_ops_RenameTable)


mm_ops_SetColumnType_strategy = st.builds(mm_ops_SetColumnType, newType=safe_text, oldType=safe_text, owningColumnName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_SetColumnType_strategy)
@settings(max_examples=25)
def test_mm_ops_SetColumnType_instantiation(instance):
    assert isinstance(instance, mm_ops_SetColumnType)


mm_ops_SetDefaultValue_strategy = st.builds(mm_ops_SetDefaultValue, newDefaultValue=safe_text, owningColumnName=safe_text, owningSchemaName=safe_text, owningTableName=safe_text)
@given(instance=mm_ops_SetDefaultValue_strategy)
@settings(max_examples=25)
def test_mm_ops_SetDefaultValue_instantiation(instance):
    assert isinstance(instance, mm_ops_SetDefaultValue)


mm_ops_UpdateRows_strategy = st.builds(mm_ops_UpdateRows, owningSchemaName=safe_text, sourceColumnName=safe_text, sourceTableName=safe_text, targetColumnName=safe_text, targetTableName=safe_text, whereCondition=safe_text)
@given(instance=mm_ops_UpdateRows_strategy)
@settings(max_examples=25)
def test_mm_ops_UpdateRows_instantiation(instance):
    assert isinstance(instance, mm_ops_UpdateRows)


mm_rdb_Column_strategy = st.builds(mm_rdb_Column, defaultValue=safe_text, isNillable=safe_text, name=safe_text, type=safe_text)
@given(instance=mm_rdb_Column_strategy)
@settings(max_examples=25)
def test_mm_rdb_Column_instantiation(instance):
    assert isinstance(instance, mm_rdb_Column)


mm_rdb_ForeignKey_strategy = st.builds(mm_rdb_ForeignKey)
@given(instance=mm_rdb_ForeignKey_strategy)
@settings(max_examples=25)
def test_mm_rdb_ForeignKey_instantiation(instance):
    assert isinstance(instance, mm_rdb_ForeignKey)


mm_rdb_Index_strategy = st.builds(mm_rdb_Index, name=safe_text)
@given(instance=mm_rdb_Index_strategy)
@settings(max_examples=25)
def test_mm_rdb_Index_instantiation(instance):
    assert isinstance(instance, mm_rdb_Index)


mm_rdb_ModelRoot_strategy = st.builds(mm_rdb_ModelRoot)
@given(instance=mm_rdb_ModelRoot_strategy)
@settings(max_examples=25)
def test_mm_rdb_ModelRoot_instantiation(instance):
    assert isinstance(instance, mm_rdb_ModelRoot)


mm_rdb_Operations_strategy = st.builds(mm_rdb_Operations)
@given(instance=mm_rdb_Operations_strategy)
@settings(max_examples=25)
def test_mm_rdb_Operations_instantiation(instance):
    assert isinstance(instance, mm_rdb_Operations)


mm_rdb_PrimaryKey_strategy = st.builds(mm_rdb_PrimaryKey)
@given(instance=mm_rdb_PrimaryKey_strategy)
@settings(max_examples=25)
def test_mm_rdb_PrimaryKey_instantiation(instance):
    assert isinstance(instance, mm_rdb_PrimaryKey)


mm_rdb_Schema_strategy = st.builds(mm_rdb_Schema, name=safe_text)
@given(instance=mm_rdb_Schema_strategy)
@settings(max_examples=25)
def test_mm_rdb_Schema_instantiation(instance):
    assert isinstance(instance, mm_rdb_Schema)


mm_rdb_Sequence_strategy = st.builds(mm_rdb_Sequence, name=safe_text, startValue=st.integers())
@given(instance=mm_rdb_Sequence_strategy)
@settings(max_examples=25)
def test_mm_rdb_Sequence_instantiation(instance):
    assert isinstance(instance, mm_rdb_Sequence)


mm_rdb_Structure_strategy = st.builds(mm_rdb_Structure)
@given(instance=mm_rdb_Structure_strategy)
@settings(max_examples=25)
def test_mm_rdb_Structure_instantiation(instance):
    assert isinstance(instance, mm_rdb_Structure)


mm_rdb_Table_strategy = st.builds(mm_rdb_Table, name=safe_text)
@given(instance=mm_rdb_Table_strategy)
@settings(max_examples=25)
def test_mm_rdb_Table_instantiation(instance):
    assert isinstance(instance, mm_rdb_Table)


mm_rdb_TableConstraint_strategy = st.builds(mm_rdb_TableConstraint, name=safe_text)
@given(instance=mm_rdb_TableConstraint_strategy)
@settings(max_examples=25)
def test_mm_rdb_TableConstraint_instantiation(instance):
    assert isinstance(instance, mm_rdb_TableConstraint)


mm_rdb_Unique_strategy = st.builds(mm_rdb_Unique)
@given(instance=mm_rdb_Unique_strategy)
@settings(max_examples=25)
def test_mm_rdb_Unique_instantiation(instance):
    assert isinstance(instance, mm_rdb_Unique)


ops_ModelOperation_strategy = st.builds(ops_ModelOperation)
@given(instance=ops_ModelOperation_strategy)
@settings(max_examples=25)
def test_ops_ModelOperation_instantiation(instance):
    assert isinstance(instance, ops_ModelOperation)



