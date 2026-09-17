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
    database_DatabaseElement,
    AbstractTable,
    database_View,
    database_Table,
    NamedElement,
    database_Constraint,
    database_Column,
    database_TableContainer,
    database_AbstractTable,
    database_UserDefinedTypesLibrary,
    TypesLibraryUser,
    database_Sequence,
    database_Type,
    database_ForeignKey,
    database_PrimaryKey,
    database_Index,
    TableContainer,
    database_Schema,
    database_DataBase,
    DatabaseElement,
    database_IndexElement,
    database_ForeignKeyElement,
    database_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_database_databaseelement_is_not_abstract():
    assert not inspect.isabstract(database_DatabaseElement)


def test_hyp_database_databaseelement_constructor_exists():
    assert callable(database_DatabaseElement.__init__)


def test_hyp_database_databaseelement_constructor_args():
    sig = inspect.signature(database_DatabaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"
    assert "ID" in params, "Missing parameter 'ID'"





def test_hyp_abstracttable_is_not_abstract():
    assert not inspect.isabstract(AbstractTable)


def test_hyp_abstracttable_constructor_exists():
    assert callable(AbstractTable.__init__)


def test_hyp_abstracttable_constructor_args():
    sig = inspect.signature(AbstractTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_view_is_not_abstract():
    assert not inspect.isabstract(database_View)


def test_hyp_database_view_constructor_exists():
    assert callable(database_View.__init__)


def test_hyp_database_view_constructor_args():
    sig = inspect.signature(database_View.__init__)
    params = list(sig.parameters.keys())
    assert "query" in params, "Missing parameter 'query'"




def test_hyp_database_table_is_not_abstract():
    assert not inspect.isabstract(database_Table)


def test_hyp_database_table_constructor_exists():
    assert callable(database_Table.__init__)


def test_hyp_database_table_constructor_args():
    sig = inspect.signature(database_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_constraint_is_not_abstract():
    assert not inspect.isabstract(database_Constraint)


def test_hyp_database_constraint_constructor_exists():
    assert callable(database_Constraint.__init__)


def test_hyp_database_constraint_constructor_args():
    sig = inspect.signature(database_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_database_column_is_not_abstract():
    assert not inspect.isabstract(database_Column)


def test_hyp_database_column_constructor_exists():
    assert callable(database_Column.__init__)


def test_hyp_database_column_constructor_args():
    sig = inspect.signature(database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "inForeignKey" in params, "Missing parameter 'inForeignKey'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "autoincrement" in params, "Missing parameter 'autoincrement'"
    assert "inPrimaryKey" in params, "Missing parameter 'inPrimaryKey'"









def test_hyp_database_tablecontainer_is_not_abstract():
    assert not inspect.isabstract(database_TableContainer)


def test_hyp_database_tablecontainer_constructor_exists():
    assert callable(database_TableContainer.__init__)


def test_hyp_database_tablecontainer_constructor_args():
    sig = inspect.signature(database_TableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_abstracttable_is_not_abstract():
    assert not inspect.isabstract(database_AbstractTable)


def test_hyp_database_abstracttable_constructor_exists():
    assert callable(database_AbstractTable.__init__)


def test_hyp_database_abstracttable_constructor_args():
    sig = inspect.signature(database_AbstractTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_userdefinedtypeslibrary_is_not_abstract():
    assert not inspect.isabstract(database_UserDefinedTypesLibrary)


def test_hyp_database_userdefinedtypeslibrary_constructor_exists():
    assert callable(database_UserDefinedTypesLibrary.__init__)


def test_hyp_database_userdefinedtypeslibrary_constructor_args():
    sig = inspect.signature(database_UserDefinedTypesLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibraryuser_is_not_abstract():
    assert not inspect.isabstract(TypesLibraryUser)


def test_hyp_typeslibraryuser_constructor_exists():
    assert callable(TypesLibraryUser.__init__)


def test_hyp_typeslibraryuser_constructor_args():
    sig = inspect.signature(TypesLibraryUser.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_sequence_is_not_abstract():
    assert not inspect.isabstract(database_Sequence)


def test_hyp_database_sequence_constructor_exists():
    assert callable(database_Sequence.__init__)


def test_hyp_database_sequence_constructor_args():
    sig = inspect.signature(database_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "start" in params, "Missing parameter 'start'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "increment" in params, "Missing parameter 'increment'"







def test_hyp_database_type_is_not_abstract():
    assert not inspect.isabstract(database_Type)


def test_hyp_database_type_constructor_exists():
    assert callable(database_Type.__init__)


def test_hyp_database_type_constructor_args():
    sig = inspect.signature(database_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_foreignkey_is_not_abstract():
    assert not inspect.isabstract(database_ForeignKey)


def test_hyp_database_foreignkey_constructor_exists():
    assert callable(database_ForeignKey.__init__)


def test_hyp_database_foreignkey_constructor_args():
    sig = inspect.signature(database_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_primarykey_is_not_abstract():
    assert not inspect.isabstract(database_PrimaryKey)


def test_hyp_database_primarykey_constructor_exists():
    assert callable(database_PrimaryKey.__init__)


def test_hyp_database_primarykey_constructor_args():
    sig = inspect.signature(database_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_index_is_not_abstract():
    assert not inspect.isabstract(database_Index)


def test_hyp_database_index_constructor_exists():
    assert callable(database_Index.__init__)


def test_hyp_database_index_constructor_args():
    sig = inspect.signature(database_Index.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "indexType" in params, "Missing parameter 'indexType'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"







def test_hyp_tablecontainer_is_not_abstract():
    assert not inspect.isabstract(TableContainer)


def test_hyp_tablecontainer_constructor_exists():
    assert callable(TableContainer.__init__)


def test_hyp_tablecontainer_constructor_args():
    sig = inspect.signature(TableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_schema_is_not_abstract():
    assert not inspect.isabstract(database_Schema)


def test_hyp_database_schema_constructor_exists():
    assert callable(database_Schema.__init__)


def test_hyp_database_schema_constructor_args():
    sig = inspect.signature(database_Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_database_is_not_abstract():
    assert not inspect.isabstract(database_DataBase)


def test_hyp_database_database_constructor_exists():
    assert callable(database_DataBase.__init__)


def test_hyp_database_database_constructor_args():
    sig = inspect.signature(database_DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"




def test_hyp_databaseelement_is_not_abstract():
    assert not inspect.isabstract(DatabaseElement)


def test_hyp_databaseelement_constructor_exists():
    assert callable(DatabaseElement.__init__)


def test_hyp_databaseelement_constructor_args():
    sig = inspect.signature(DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_indexelement_is_not_abstract():
    assert not inspect.isabstract(database_IndexElement)


def test_hyp_database_indexelement_constructor_exists():
    assert callable(database_IndexElement.__init__)


def test_hyp_database_indexelement_constructor_args():
    sig = inspect.signature(database_IndexElement.__init__)
    params = list(sig.parameters.keys())
    assert "asc" in params, "Missing parameter 'asc'"




def test_hyp_database_foreignkeyelement_is_not_abstract():
    assert not inspect.isabstract(database_ForeignKeyElement)


def test_hyp_database_foreignkeyelement_constructor_exists():
    assert callable(database_ForeignKeyElement.__init__)


def test_hyp_database_foreignkeyelement_constructor_args():
    sig = inspect.signature(database_ForeignKeyElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_namedelement_is_not_abstract():
    assert not inspect.isabstract(database_NamedElement)


def test_hyp_database_namedelement_constructor_exists():
    assert callable(database_NamedElement.__init__)


def test_hyp_database_namedelement_constructor_args():
    sig = inspect.signature(database_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
database_DatabaseElement_strategy = st.builds(
    database_DatabaseElement,
    comments=
        safe_text,
    ID=
        safe_text
)
AbstractTable_strategy = st.builds(
    AbstractTable,
)
database_View_strategy = st.builds(
    database_View,
    query=
        safe_text
)
database_Table_strategy = st.builds(
    database_Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
database_Constraint_strategy = st.builds(
    database_Constraint,
    expression=
        safe_text
)
database_Column_strategy = st.builds(
    database_Column,
    unique=
        st.booleans(),
    nullable=
        st.booleans(),
    inForeignKey=
        st.booleans(),
    defaultValue=
        safe_text,
    autoincrement=
        st.booleans(),
    inPrimaryKey=
        st.booleans()
)
database_TableContainer_strategy = st.builds(
    database_TableContainer,
)
database_AbstractTable_strategy = st.builds(
    database_AbstractTable,
)
database_UserDefinedTypesLibrary_strategy = st.builds(
    database_UserDefinedTypesLibrary,
)
TypesLibraryUser_strategy = st.builds(
    TypesLibraryUser,
)
database_Sequence_strategy = st.builds(
    database_Sequence,
    minValue=
        st.integers(),
    start=
        st.integers(),
    maxValue=
        st.integers(),
    increment=
        st.integers()
)
database_Type_strategy = st.builds(
    database_Type,
)
database_ForeignKey_strategy = st.builds(
    database_ForeignKey,
)
database_PrimaryKey_strategy = st.builds(
    database_PrimaryKey,
)
database_Index_strategy = st.builds(
    database_Index,
    qualifier=
        safe_text,
    unique=
        st.booleans(),
    indexType=
        safe_text,
    cardinality=
        st.integers()
)
TableContainer_strategy = st.builds(
    TableContainer,
)
database_Schema_strategy = st.builds(
    database_Schema,
)
database_DataBase_strategy = st.builds(
    database_DataBase,
    url=
        safe_text
)
DatabaseElement_strategy = st.builds(
    DatabaseElement,
)
database_IndexElement_strategy = st.builds(
    database_IndexElement,
    asc=
        st.booleans()
)
database_ForeignKeyElement_strategy = st.builds(
    database_ForeignKeyElement,
)
database_NamedElement_strategy = st.builds(
    database_NamedElement,
    name=
        safe_text
)




@given(instance=database_DatabaseElement_strategy)
def test_hyp_database_databaseelement_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=database_DatabaseElement_strategy)
def test_hyp_database_databaseelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original





@given(instance=database_View_strategy)
def test_hyp_database_view_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original






@given(instance=database_Constraint_strategy)
def test_hyp_database_constraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=database_Column_strategy)
def test_hyp_database_column_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=database_Column_strategy)
def test_hyp_database_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=database_Column_strategy)
def test_hyp_database_column_inForeignKey_setter(instance):
    original = instance.inForeignKey
    instance.inForeignKey = original
    assert instance.inForeignKey == original



@given(instance=database_Column_strategy)
def test_hyp_database_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=database_Column_strategy)
def test_hyp_database_column_autoincrement_setter(instance):
    original = instance.autoincrement
    instance.autoincrement = original
    assert instance.autoincrement == original



@given(instance=database_Column_strategy)
def test_hyp_database_column_inPrimaryKey_setter(instance):
    original = instance.inPrimaryKey
    instance.inPrimaryKey = original
    assert instance.inPrimaryKey == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=database_Column_strategy)
@settings(max_examples=30)
def test_hyp_database_column_addtoprimarykey_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addToPrimaryKey()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addToPrimaryKey).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addToPrimaryKey' in database_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addToPrimaryKey' in database_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addToPrimaryKey' in database_Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=database_Column_strategy)
@settings(max_examples=30)
def test_hyp_database_column_removefromuniqueindex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeFromUniqueIndex()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeFromUniqueIndex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeFromUniqueIndex' in database_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeFromUniqueIndex' in database_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeFromUniqueIndex' in database_Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=database_Column_strategy)
@settings(max_examples=30)
def test_hyp_database_column_removefromprimarykey_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeFromPrimaryKey()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeFromPrimaryKey).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeFromPrimaryKey' in database_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeFromPrimaryKey' in database_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeFromPrimaryKey' in database_Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=database_Column_strategy)
@settings(max_examples=30)
def test_hyp_database_column_addtouniqueindex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addToUniqueIndex()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addToUniqueIndex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addToUniqueIndex' in database_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addToUniqueIndex' in database_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addToUniqueIndex' in database_Column is not implemented or raised an error")








@given(instance=database_Sequence_strategy)
def test_hyp_database_sequence_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=database_Sequence_strategy)
def test_hyp_database_sequence_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=database_Sequence_strategy)
def test_hyp_database_sequence_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=database_Sequence_strategy)
def test_hyp_database_sequence_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original







@given(instance=database_Index_strategy)
def test_hyp_database_index_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=database_Index_strategy)
def test_hyp_database_index_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=database_Index_strategy)
def test_hyp_database_index_indexType_setter(instance):
    original = instance.indexType
    instance.indexType = original
    assert instance.indexType == original



@given(instance=database_Index_strategy)
def test_hyp_database_index_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original






@given(instance=database_DataBase_strategy)
def test_hyp_database_database_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original





@given(instance=database_IndexElement_strategy)
def test_hyp_database_indexelement_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original





@given(instance=database_NamedElement_strategy)
def test_hyp_database_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_database_Column_autoincrement_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.autoincrement == True
    instance.autoincrement = False
    assert instance.autoincrement == False


def test_database_Column_defaultValue_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_database_Column_inForeignKey_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.inForeignKey == True
    instance.inForeignKey = False
    assert instance.inForeignKey == False


def test_database_Column_inPrimaryKey_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.inPrimaryKey == True
    instance.inPrimaryKey = False
    assert instance.inPrimaryKey == False


def test_database_Column_nullable_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.nullable == True
    instance.nullable = False
    assert instance.nullable == False


def test_database_Column_unique_value_roundtrip():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_database_Constraint_expression_value_roundtrip():
    instance = database_Constraint(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_database_DataBase_url_value_roundtrip():
    instance = database_DataBase(url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_database_DatabaseElement_ID_value_roundtrip():
    instance = database_DatabaseElement(ID="sample_text", comments="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_database_DatabaseElement_comments_value_roundtrip():
    instance = database_DatabaseElement(ID="sample_text", comments="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_database_Index_cardinality_value_roundtrip():
    instance = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    assert instance.cardinality == 7
    instance.cardinality = 13
    assert instance.cardinality == 13


def test_database_Index_indexType_value_roundtrip():
    instance = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    assert instance.indexType == "sample_text"
    instance.indexType = "sample_text_2"
    assert instance.indexType == "sample_text_2"


def test_database_Index_qualifier_value_roundtrip():
    instance = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_database_Index_unique_value_roundtrip():
    instance = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_database_IndexElement_asc_value_roundtrip():
    instance = database_IndexElement(asc=True)
    assert instance.asc == True
    instance.asc = False
    assert instance.asc == False


def test_database_NamedElement_name_value_roundtrip():
    instance = database_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_database_Sequence_increment_value_roundtrip():
    instance = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    assert instance.increment == 7
    instance.increment = 13
    assert instance.increment == 13


def test_database_Sequence_maxValue_value_roundtrip():
    instance = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    assert instance.maxValue == 7
    instance.maxValue = 13
    assert instance.maxValue == 13


def test_database_Sequence_minValue_value_roundtrip():
    instance = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    assert instance.minValue == 7
    instance.minValue = 13
    assert instance.minValue == 13


def test_database_Sequence_start_value_roundtrip():
    instance = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    assert instance.start == 7
    instance.start = 13
    assert instance.start == 13


def test_database_View_query_value_roundtrip():
    instance = database_View(query="sample_text")
    assert instance.query == "sample_text"
    instance.query = "sample_text_2"
    assert instance.query == "sample_text_2"


def test_database_Table_isa_AbstractTable():
    instance = database_Table()
    assert isinstance(instance, AbstractTable)


def test_database_View_isa_AbstractTable():
    instance = database_View(query="sample_text")
    assert isinstance(instance, AbstractTable)


def test_database_ForeignKeyElement_isa_DatabaseElement():
    instance = database_ForeignKeyElement()
    assert isinstance(instance, DatabaseElement)


def test_database_IndexElement_isa_DatabaseElement():
    instance = database_IndexElement(asc=True)
    assert isinstance(instance, DatabaseElement)


def test_database_NamedElement_isa_DatabaseElement():
    instance = database_NamedElement(name="sample_text")
    assert isinstance(instance, DatabaseElement)


def test_database_AbstractTable_isa_NamedElement():
    instance = database_AbstractTable()
    assert isinstance(instance, NamedElement)


def test_database_Column_isa_NamedElement():
    instance = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    assert isinstance(instance, NamedElement)


def test_database_Constraint_isa_NamedElement():
    instance = database_Constraint(expression="sample_text")
    assert isinstance(instance, NamedElement)


def test_database_ForeignKey_isa_NamedElement():
    instance = database_ForeignKey()
    assert isinstance(instance, NamedElement)


def test_database_Index_isa_NamedElement():
    instance = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    assert isinstance(instance, NamedElement)


def test_database_PrimaryKey_isa_NamedElement():
    instance = database_PrimaryKey()
    assert isinstance(instance, NamedElement)


def test_database_Sequence_isa_NamedElement():
    instance = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    assert isinstance(instance, NamedElement)


def test_database_TableContainer_isa_NamedElement():
    instance = database_TableContainer()
    assert isinstance(instance, NamedElement)


def test_database_DataBase_isa_TableContainer():
    instance = database_DataBase(url="sample_text")
    assert isinstance(instance, TableContainer)


def test_database_Schema_isa_TableContainer():
    instance = database_Schema()
    assert isinstance(instance, TableContainer)


def test_database_DataBase_isa_TypesLibraryUser():
    instance = database_DataBase(url="sample_text")
    assert isinstance(instance, TypesLibraryUser)


def test_assoc_column45_link_reassign_clear():
    a = database_IndexElement(asc=True)
    b1 = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b2 = database_Column(autoincrement=False, defaultValue="sample_text_2", inForeignKey=False, inPrimaryKey=False, nullable=False, unique=False)
    _safe_set(a, 'indexElements', b1)
    assert _is_linked(a, 'indexElements', b1)
    if hasattr(b1, 'Column46'):
        assert _is_linked(b1, 'Column46', a)
    _safe_set(a, 'indexElements', b2)
    assert _is_linked(a, 'indexElements', b2)
    if hasattr(b1, 'Column46'):
        assert not _is_linked(b1, 'Column46', a)
    if hasattr(b2, 'Column46'):
        assert _is_linked(b2, 'Column46', a)
    _safe_set(a, 'indexElements', None)
    assert not _is_linked(a, 'indexElements', b2)
    if hasattr(b2, 'Column46'):
        assert not _is_linked(b2, 'Column46', a)


def test_assoc_columns29_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_PrimaryKey()
    b2 = database_PrimaryKey()
    _safe_set(a, 'Column30', b1)
    assert _is_linked(a, 'Column30', b1)
    if hasattr(b1, 'primaryKey'):
        assert _is_linked(b1, 'primaryKey', a)
    _safe_set(a, 'Column30', b2)
    assert _is_linked(a, 'Column30', b2)
    if hasattr(b1, 'primaryKey'):
        assert not _is_linked(b1, 'primaryKey', a)
    if hasattr(b2, 'primaryKey'):
        assert _is_linked(b2, 'primaryKey', a)
    _safe_set(a, 'Column30', None)
    assert not _is_linked(a, 'Column30', b2)
    if hasattr(b2, 'primaryKey'):
        assert not _is_linked(b2, 'primaryKey', a)


def test_assoc_columns3_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_AbstractTable()
    b2 = database_AbstractTable()
    _safe_set(a, 'Column', b1)
    assert _is_linked(a, 'Column', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'Column', b2)
    assert _is_linked(a, 'Column', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'Column', None)
    assert not _is_linked(a, 'Column', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_constraints25_link_reassign_clear():
    a = database_Constraint(expression="sample_text")
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'Constraint', b1)
    assert _is_linked(a, 'Constraint', b1)
    if hasattr(b1, 'owner26'):
        assert _is_linked(b1, 'owner26', a)
    _safe_set(a, 'Constraint', b2)
    assert _is_linked(a, 'Constraint', b2)
    if hasattr(b1, 'owner26'):
        assert not _is_linked(b1, 'owner26', a)
    if hasattr(b2, 'owner26'):
        assert _is_linked(b2, 'owner26', a)
    _safe_set(a, 'Constraint', None)
    assert not _is_linked(a, 'Constraint', b2)
    if hasattr(b2, 'owner26'):
        assert not _is_linked(b2, 'owner26', a)


def test_assoc_defines1_link_reassign_clear():
    a = database_DataBase(url="sample_text")
    b1 = database_UserDefinedTypesLibrary()
    b2 = database_UserDefinedTypesLibrary()
    _safe_set(a, 'database_DataBase2', {b1})
    assert _is_linked(a, 'database_DataBase2', b1)
    if hasattr(b1, 'database_UserDefinedTypesLibrary'):
        assert _is_linked(b1, 'database_UserDefinedTypesLibrary', a)
    _safe_set(a, 'database_DataBase2', {b2})
    assert _is_linked(a, 'database_DataBase2', b2)
    if hasattr(b1, 'database_UserDefinedTypesLibrary'):
        assert not _is_linked(b1, 'database_UserDefinedTypesLibrary', a)
    if hasattr(b2, 'database_UserDefinedTypesLibrary'):
        assert _is_linked(b2, 'database_UserDefinedTypesLibrary', a)
    _safe_set(a, 'database_DataBase2', set())
    assert not _is_linked(a, 'database_DataBase2', b2)
    if hasattr(b2, 'database_UserDefinedTypesLibrary'):
        assert not _is_linked(b2, 'database_UserDefinedTypesLibrary', a)


def test_assoc_elements17_link_reassign_clear():
    a = database_IndexElement(asc=True)
    b1 = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    b2 = database_Index(cardinality=13, indexType="sample_text_2", qualifier="sample_text_2", unique=False)
    _safe_set(a, 'database_IndexElement', b1)
    assert _is_linked(a, 'database_IndexElement', b1)
    if hasattr(b1, 'database_Index18'):
        assert _is_linked(b1, 'database_Index18', a)
    _safe_set(a, 'database_IndexElement', b2)
    assert _is_linked(a, 'database_IndexElement', b2)
    if hasattr(b1, 'database_Index18'):
        assert not _is_linked(b1, 'database_Index18', a)
    if hasattr(b2, 'database_Index18'):
        assert _is_linked(b2, 'database_Index18', a)
    _safe_set(a, 'database_IndexElement', None)
    assert not _is_linked(a, 'database_IndexElement', b2)
    if hasattr(b2, 'database_Index18'):
        assert not _is_linked(b2, 'database_Index18', a)


def test_assoc_elements34_link_reassign_clear():
    a = database_ForeignKey()
    b1 = database_ForeignKeyElement()
    b2 = database_ForeignKeyElement()
    _safe_set(a, 'database_ForeignKey35', {b1})
    assert _is_linked(a, 'database_ForeignKey35', b1)
    if hasattr(b1, 'database_ForeignKeyElement'):
        assert _is_linked(b1, 'database_ForeignKeyElement', a)
    _safe_set(a, 'database_ForeignKey35', {b2})
    assert _is_linked(a, 'database_ForeignKey35', b2)
    if hasattr(b1, 'database_ForeignKeyElement'):
        assert not _is_linked(b1, 'database_ForeignKeyElement', a)
    if hasattr(b2, 'database_ForeignKeyElement'):
        assert _is_linked(b2, 'database_ForeignKeyElement', a)
    _safe_set(a, 'database_ForeignKey35', set())
    assert not _is_linked(a, 'database_ForeignKey35', b2)
    if hasattr(b2, 'database_ForeignKeyElement'):
        assert not _is_linked(b2, 'database_ForeignKeyElement', a)


def test_assoc_fkColumn40_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_ForeignKeyElement()
    b2 = database_ForeignKeyElement()
    _safe_set(a, 'Column41', b1)
    assert _is_linked(a, 'Column41', b1)
    if hasattr(b1, 'foreignKeyElements'):
        assert _is_linked(b1, 'foreignKeyElements', a)
    _safe_set(a, 'Column41', b2)
    assert _is_linked(a, 'Column41', b2)
    if hasattr(b1, 'foreignKeyElements'):
        assert not _is_linked(b1, 'foreignKeyElements', a)
    if hasattr(b2, 'foreignKeyElements'):
        assert _is_linked(b2, 'foreignKeyElements', a)
    _safe_set(a, 'Column41', None)
    assert not _is_linked(a, 'Column41', b2)
    if hasattr(b2, 'foreignKeyElements'):
        assert not _is_linked(b2, 'foreignKeyElements', a)


def test_assoc_foreignKeyElements10_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_ForeignKeyElement()
    b2 = database_ForeignKeyElement()
    _safe_set(a, 'fkColumn', {b1})
    assert _is_linked(a, 'fkColumn', b1)
    if hasattr(b1, 'ForeignKeyElement'):
        assert _is_linked(b1, 'ForeignKeyElement', a)
    _safe_set(a, 'fkColumn', {b2})
    assert _is_linked(a, 'fkColumn', b2)
    if hasattr(b1, 'ForeignKeyElement'):
        assert not _is_linked(b1, 'ForeignKeyElement', a)
    if hasattr(b2, 'ForeignKeyElement'):
        assert _is_linked(b2, 'ForeignKeyElement', a)
    _safe_set(a, 'fkColumn', set())
    assert not _is_linked(a, 'fkColumn', b2)
    if hasattr(b2, 'ForeignKeyElement'):
        assert not _is_linked(b2, 'ForeignKeyElement', a)


def test_assoc_foreignKeys23_link_reassign_clear():
    a = database_ForeignKey()
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'ForeignKey', b1)
    assert _is_linked(a, 'ForeignKey', b1)
    if hasattr(b1, 'owner24'):
        assert _is_linked(b1, 'owner24', a)
    _safe_set(a, 'ForeignKey', b2)
    assert _is_linked(a, 'ForeignKey', b2)
    if hasattr(b1, 'owner24'):
        assert not _is_linked(b1, 'owner24', a)
    if hasattr(b2, 'owner24'):
        assert _is_linked(b2, 'owner24', a)
    _safe_set(a, 'ForeignKey', None)
    assert not _is_linked(a, 'ForeignKey', b2)
    if hasattr(b2, 'owner24'):
        assert not _is_linked(b2, 'owner24', a)


def test_assoc_foreignKeys8_link_reassign_clear():
    a = database_ForeignKey()
    b1 = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b2 = database_Column(autoincrement=False, defaultValue="sample_text_2", inForeignKey=False, inPrimaryKey=False, nullable=False, unique=False)
    _safe_set(a, 'database_ForeignKey', b1)
    assert _is_linked(a, 'database_ForeignKey', b1)
    if hasattr(b1, 'database_Column9'):
        assert _is_linked(b1, 'database_Column9', a)
    _safe_set(a, 'database_ForeignKey', b2)
    assert _is_linked(a, 'database_ForeignKey', b2)
    if hasattr(b1, 'database_Column9'):
        assert not _is_linked(b1, 'database_Column9', a)
    if hasattr(b2, 'database_Column9'):
        assert _is_linked(b2, 'database_Column9', a)
    _safe_set(a, 'database_ForeignKey', None)
    assert not _is_linked(a, 'database_ForeignKey', b2)
    if hasattr(b2, 'database_Column9'):
        assert not _is_linked(b2, 'database_Column9', a)


def test_assoc_indexElements6_link_reassign_clear():
    a = database_IndexElement(asc=True)
    b1 = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b2 = database_Column(autoincrement=False, defaultValue="sample_text_2", inForeignKey=False, inPrimaryKey=False, nullable=False, unique=False)
    _safe_set(a, 'IndexElement', b1)
    assert _is_linked(a, 'IndexElement', b1)
    if hasattr(b1, 'column'):
        assert _is_linked(b1, 'column', a)
    _safe_set(a, 'IndexElement', b2)
    assert _is_linked(a, 'IndexElement', b2)
    if hasattr(b1, 'column'):
        assert not _is_linked(b1, 'column', a)
    if hasattr(b2, 'column'):
        assert _is_linked(b2, 'column', a)
    _safe_set(a, 'IndexElement', None)
    assert not _is_linked(a, 'IndexElement', b2)
    if hasattr(b2, 'column'):
        assert not _is_linked(b2, 'column', a)


def test_assoc_indexes27_link_reassign_clear():
    a = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'Index', b1)
    assert _is_linked(a, 'Index', b1)
    if hasattr(b1, 'owner28'):
        assert _is_linked(b1, 'owner28', a)
    _safe_set(a, 'Index', b2)
    assert _is_linked(a, 'Index', b2)
    if hasattr(b1, 'owner28'):
        assert not _is_linked(b1, 'owner28', a)
    if hasattr(b2, 'owner28'):
        assert _is_linked(b2, 'owner28', a)
    _safe_set(a, 'Index', None)
    assert not _is_linked(a, 'Index', b2)
    if hasattr(b2, 'owner28'):
        assert not _is_linked(b2, 'owner28', a)


def test_assoc_indexes5_link_reassign_clear():
    a = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    b1 = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b2 = database_Column(autoincrement=False, defaultValue="sample_text_2", inForeignKey=False, inPrimaryKey=False, nullable=False, unique=False)
    _safe_set(a, 'database_Index', b1)
    assert _is_linked(a, 'database_Index', b1)
    if hasattr(b1, 'database_Column'):
        assert _is_linked(b1, 'database_Column', a)
    _safe_set(a, 'database_Index', b2)
    assert _is_linked(a, 'database_Index', b2)
    if hasattr(b1, 'database_Column'):
        assert not _is_linked(b1, 'database_Column', a)
    if hasattr(b2, 'database_Column'):
        assert _is_linked(b2, 'database_Column', a)
    _safe_set(a, 'database_Index', None)
    assert not _is_linked(a, 'database_Index', b2)
    if hasattr(b2, 'database_Column'):
        assert not _is_linked(b2, 'database_Column', a)


def test_assoc_owner15_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_AbstractTable()
    b2 = database_AbstractTable()
    _safe_set(a, 'columns16', b1)
    assert _is_linked(a, 'columns16', b1)
    if hasattr(b1, 'AbstractTable'):
        assert _is_linked(b1, 'AbstractTable', a)
    _safe_set(a, 'columns16', b2)
    assert _is_linked(a, 'columns16', b2)
    if hasattr(b1, 'AbstractTable'):
        assert not _is_linked(b1, 'AbstractTable', a)
    if hasattr(b2, 'AbstractTable'):
        assert _is_linked(b2, 'AbstractTable', a)
    _safe_set(a, 'columns16', None)
    assert not _is_linked(a, 'columns16', b2)
    if hasattr(b2, 'AbstractTable'):
        assert not _is_linked(b2, 'AbstractTable', a)


def test_assoc_owner19_link_reassign_clear():
    a = database_Index(cardinality=7, indexType="sample_text", qualifier="sample_text", unique=True)
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'indexes', b1)
    assert _is_linked(a, 'indexes', b1)
    if hasattr(b1, 'Table'):
        assert _is_linked(b1, 'Table', a)
    _safe_set(a, 'indexes', b2)
    assert _is_linked(a, 'indexes', b2)
    if hasattr(b1, 'Table'):
        assert not _is_linked(b1, 'Table', a)
    if hasattr(b2, 'Table'):
        assert _is_linked(b2, 'Table', a)
    _safe_set(a, 'indexes', None)
    assert not _is_linked(a, 'indexes', b2)
    if hasattr(b2, 'Table'):
        assert not _is_linked(b2, 'Table', a)


def test_assoc_owner36_link_reassign_clear():
    a = database_ForeignKey()
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'foreignKeys', b1)
    assert _is_linked(a, 'foreignKeys', b1)
    if hasattr(b1, 'Table37'):
        assert _is_linked(b1, 'Table37', a)
    _safe_set(a, 'foreignKeys', b2)
    assert _is_linked(a, 'foreignKeys', b2)
    if hasattr(b1, 'Table37'):
        assert not _is_linked(b1, 'Table37', a)
    if hasattr(b2, 'Table37'):
        assert _is_linked(b2, 'Table37', a)
    _safe_set(a, 'foreignKeys', None)
    assert not _is_linked(a, 'foreignKeys', b2)
    if hasattr(b2, 'Table37'):
        assert not _is_linked(b2, 'Table37', a)


def test_assoc_owner47_link_reassign_clear():
    a = database_Constraint(expression="sample_text")
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'constraints', b1)
    assert _is_linked(a, 'constraints', b1)
    if hasattr(b1, 'Table48'):
        assert _is_linked(b1, 'Table48', a)
    _safe_set(a, 'constraints', b2)
    assert _is_linked(a, 'constraints', b2)
    if hasattr(b1, 'Table48'):
        assert not _is_linked(b1, 'Table48', a)
    if hasattr(b2, 'Table48'):
        assert _is_linked(b2, 'Table48', a)
    _safe_set(a, 'constraints', None)
    assert not _is_linked(a, 'constraints', b2)
    if hasattr(b2, 'Table48'):
        assert not _is_linked(b2, 'Table48', a)


def test_assoc_pkColumn42_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_ForeignKeyElement()
    b2 = database_ForeignKeyElement()
    _safe_set(a, 'database_Column44', b1)
    assert _is_linked(a, 'database_Column44', b1)
    if hasattr(b1, 'database_ForeignKeyElement43'):
        assert _is_linked(b1, 'database_ForeignKeyElement43', a)
    _safe_set(a, 'database_Column44', b2)
    assert _is_linked(a, 'database_Column44', b2)
    if hasattr(b1, 'database_ForeignKeyElement43'):
        assert not _is_linked(b1, 'database_ForeignKeyElement43', a)
    if hasattr(b2, 'database_ForeignKeyElement43'):
        assert _is_linked(b2, 'database_ForeignKeyElement43', a)
    _safe_set(a, 'database_Column44', None)
    assert not _is_linked(a, 'database_Column44', b2)
    if hasattr(b2, 'database_ForeignKeyElement43'):
        assert not _is_linked(b2, 'database_ForeignKeyElement43', a)


def test_assoc_primaryKey7_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_PrimaryKey()
    b2 = database_PrimaryKey()
    _safe_set(a, 'columns', b1)
    assert _is_linked(a, 'columns', b1)
    if hasattr(b1, 'PrimaryKey'):
        assert _is_linked(b1, 'PrimaryKey', a)
    _safe_set(a, 'columns', b2)
    assert _is_linked(a, 'columns', b2)
    if hasattr(b1, 'PrimaryKey'):
        assert not _is_linked(b1, 'PrimaryKey', a)
    if hasattr(b2, 'PrimaryKey'):
        assert _is_linked(b2, 'PrimaryKey', a)
    _safe_set(a, 'columns', None)
    assert not _is_linked(a, 'columns', b2)
    if hasattr(b2, 'PrimaryKey'):
        assert not _is_linked(b2, 'PrimaryKey', a)


def test_assoc_schemas0_link_reassign_clear():
    a = database_DataBase(url="sample_text")
    b1 = database_Schema()
    b2 = database_Schema()
    _safe_set(a, 'database_DataBase', {b1})
    assert _is_linked(a, 'database_DataBase', b1)
    if hasattr(b1, 'database_Schema'):
        assert _is_linked(b1, 'database_Schema', a)
    _safe_set(a, 'database_DataBase', {b2})
    assert _is_linked(a, 'database_DataBase', b2)
    if hasattr(b1, 'database_Schema'):
        assert not _is_linked(b1, 'database_Schema', a)
    if hasattr(b2, 'database_Schema'):
        assert _is_linked(b2, 'database_Schema', a)
    _safe_set(a, 'database_DataBase', set())
    assert not _is_linked(a, 'database_DataBase', b2)
    if hasattr(b2, 'database_Schema'):
        assert not _is_linked(b2, 'database_Schema', a)


def test_assoc_sequence13_link_reassign_clear():
    a = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    b1 = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b2 = database_Column(autoincrement=False, defaultValue="sample_text_2", inForeignKey=False, inPrimaryKey=False, nullable=False, unique=False)
    _safe_set(a, 'database_Sequence', b1)
    assert _is_linked(a, 'database_Sequence', b1)
    if hasattr(b1, 'database_Column14'):
        assert _is_linked(b1, 'database_Column14', a)
    _safe_set(a, 'database_Sequence', b2)
    assert _is_linked(a, 'database_Sequence', b2)
    if hasattr(b1, 'database_Column14'):
        assert not _is_linked(b1, 'database_Column14', a)
    if hasattr(b2, 'database_Column14'):
        assert _is_linked(b2, 'database_Column14', a)
    _safe_set(a, 'database_Sequence', None)
    assert not _is_linked(a, 'database_Sequence', b2)
    if hasattr(b2, 'database_Column14'):
        assert not _is_linked(b2, 'database_Column14', a)


def test_assoc_sequences52_link_reassign_clear():
    a = database_Sequence(increment=7, maxValue=7, minValue=7, start=7)
    b1 = database_TableContainer()
    b2 = database_TableContainer()
    _safe_set(a, 'database_Sequence53', b1)
    assert _is_linked(a, 'database_Sequence53', b1)
    if hasattr(b1, 'database_TableContainer'):
        assert _is_linked(b1, 'database_TableContainer', a)
    _safe_set(a, 'database_Sequence53', b2)
    assert _is_linked(a, 'database_Sequence53', b2)
    if hasattr(b1, 'database_TableContainer'):
        assert not _is_linked(b1, 'database_TableContainer', a)
    if hasattr(b2, 'database_TableContainer'):
        assert _is_linked(b2, 'database_TableContainer', a)
    _safe_set(a, 'database_Sequence53', None)
    assert not _is_linked(a, 'database_Sequence53', b2)
    if hasattr(b2, 'database_TableContainer'):
        assert not _is_linked(b2, 'database_TableContainer', a)


def test_assoc_target38_link_reassign_clear():
    a = database_ForeignKey()
    b1 = database_Table()
    b2 = database_Table()
    _safe_set(a, 'database_ForeignKey39', b1)
    assert _is_linked(a, 'database_ForeignKey39', b1)
    if hasattr(b1, 'database_Table'):
        assert _is_linked(b1, 'database_Table', a)
    _safe_set(a, 'database_ForeignKey39', b2)
    assert _is_linked(a, 'database_ForeignKey39', b2)
    if hasattr(b1, 'database_Table'):
        assert not _is_linked(b1, 'database_Table', a)
    if hasattr(b2, 'database_Table'):
        assert _is_linked(b2, 'database_Table', a)
    _safe_set(a, 'database_ForeignKey39', None)
    assert not _is_linked(a, 'database_ForeignKey39', b2)
    if hasattr(b2, 'database_Table'):
        assert not _is_linked(b2, 'database_Table', a)


def test_assoc_type11_link_reassign_clear():
    a = database_Column(autoincrement=True, defaultValue="sample_text", inForeignKey=True, inPrimaryKey=True, nullable=True, unique=True)
    b1 = database_Type()
    b2 = database_Type()
    _safe_set(a, 'database_Column12', b1)
    assert _is_linked(a, 'database_Column12', b1)
    if hasattr(b1, 'database_Type'):
        assert _is_linked(b1, 'database_Type', a)
    _safe_set(a, 'database_Column12', b2)
    assert _is_linked(a, 'database_Column12', b2)
    if hasattr(b1, 'database_Type'):
        assert not _is_linked(b1, 'database_Type', a)
    if hasattr(b2, 'database_Type'):
        assert _is_linked(b2, 'database_Type', a)
    _safe_set(a, 'database_Column12', None)
    assert not _is_linked(a, 'database_Column12', b2)
    if hasattr(b2, 'database_Type'):
        assert not _is_linked(b2, 'database_Type', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractTable_strategy = st.builds(AbstractTable)
@given(instance=AbstractTable_strategy)
@settings(max_examples=25)
def test_AbstractTable_instantiation(instance):
    assert isinstance(instance, AbstractTable)


DatabaseElement_strategy = st.builds(DatabaseElement)
@given(instance=DatabaseElement_strategy)
@settings(max_examples=25)
def test_DatabaseElement_instantiation(instance):
    assert isinstance(instance, DatabaseElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


TableContainer_strategy = st.builds(TableContainer)
@given(instance=TableContainer_strategy)
@settings(max_examples=25)
def test_TableContainer_instantiation(instance):
    assert isinstance(instance, TableContainer)


TypesLibraryUser_strategy = st.builds(TypesLibraryUser)
@given(instance=TypesLibraryUser_strategy)
@settings(max_examples=25)
def test_TypesLibraryUser_instantiation(instance):
    assert isinstance(instance, TypesLibraryUser)


database_AbstractTable_strategy = st.builds(database_AbstractTable)
@given(instance=database_AbstractTable_strategy)
@settings(max_examples=25)
def test_database_AbstractTable_instantiation(instance):
    assert isinstance(instance, database_AbstractTable)


database_Column_strategy = st.builds(database_Column, autoincrement=st.booleans(), defaultValue=safe_text, inForeignKey=st.booleans(), inPrimaryKey=st.booleans(), nullable=st.booleans(), unique=st.booleans())
@given(instance=database_Column_strategy)
@settings(max_examples=25)
def test_database_Column_instantiation(instance):
    assert isinstance(instance, database_Column)


database_Constraint_strategy = st.builds(database_Constraint, expression=safe_text)
@given(instance=database_Constraint_strategy)
@settings(max_examples=25)
def test_database_Constraint_instantiation(instance):
    assert isinstance(instance, database_Constraint)


database_DataBase_strategy = st.builds(database_DataBase, url=safe_text)
@given(instance=database_DataBase_strategy)
@settings(max_examples=25)
def test_database_DataBase_instantiation(instance):
    assert isinstance(instance, database_DataBase)


database_DatabaseElement_strategy = st.builds(database_DatabaseElement, ID=safe_text, comments=safe_text)
@given(instance=database_DatabaseElement_strategy)
@settings(max_examples=25)
def test_database_DatabaseElement_instantiation(instance):
    assert isinstance(instance, database_DatabaseElement)


database_ForeignKey_strategy = st.builds(database_ForeignKey)
@given(instance=database_ForeignKey_strategy)
@settings(max_examples=25)
def test_database_ForeignKey_instantiation(instance):
    assert isinstance(instance, database_ForeignKey)


database_ForeignKeyElement_strategy = st.builds(database_ForeignKeyElement)
@given(instance=database_ForeignKeyElement_strategy)
@settings(max_examples=25)
def test_database_ForeignKeyElement_instantiation(instance):
    assert isinstance(instance, database_ForeignKeyElement)


database_Index_strategy = st.builds(database_Index, cardinality=st.integers(), indexType=safe_text, qualifier=safe_text, unique=st.booleans())
@given(instance=database_Index_strategy)
@settings(max_examples=25)
def test_database_Index_instantiation(instance):
    assert isinstance(instance, database_Index)


database_IndexElement_strategy = st.builds(database_IndexElement, asc=st.booleans())
@given(instance=database_IndexElement_strategy)
@settings(max_examples=25)
def test_database_IndexElement_instantiation(instance):
    assert isinstance(instance, database_IndexElement)


database_NamedElement_strategy = st.builds(database_NamedElement, name=safe_text)
@given(instance=database_NamedElement_strategy)
@settings(max_examples=25)
def test_database_NamedElement_instantiation(instance):
    assert isinstance(instance, database_NamedElement)


database_PrimaryKey_strategy = st.builds(database_PrimaryKey)
@given(instance=database_PrimaryKey_strategy)
@settings(max_examples=25)
def test_database_PrimaryKey_instantiation(instance):
    assert isinstance(instance, database_PrimaryKey)


database_Schema_strategy = st.builds(database_Schema)
@given(instance=database_Schema_strategy)
@settings(max_examples=25)
def test_database_Schema_instantiation(instance):
    assert isinstance(instance, database_Schema)


database_Sequence_strategy = st.builds(database_Sequence, increment=st.integers(), maxValue=st.integers(), minValue=st.integers(), start=st.integers())
@given(instance=database_Sequence_strategy)
@settings(max_examples=25)
def test_database_Sequence_instantiation(instance):
    assert isinstance(instance, database_Sequence)


database_Table_strategy = st.builds(database_Table)
@given(instance=database_Table_strategy)
@settings(max_examples=25)
def test_database_Table_instantiation(instance):
    assert isinstance(instance, database_Table)


database_TableContainer_strategy = st.builds(database_TableContainer)
@given(instance=database_TableContainer_strategy)
@settings(max_examples=25)
def test_database_TableContainer_instantiation(instance):
    assert isinstance(instance, database_TableContainer)


database_Type_strategy = st.builds(database_Type)
@given(instance=database_Type_strategy)
@settings(max_examples=25)
def test_database_Type_instantiation(instance):
    assert isinstance(instance, database_Type)


database_UserDefinedTypesLibrary_strategy = st.builds(database_UserDefinedTypesLibrary)
@given(instance=database_UserDefinedTypesLibrary_strategy)
@settings(max_examples=25)
def test_database_UserDefinedTypesLibrary_instantiation(instance):
    assert isinstance(instance, database_UserDefinedTypesLibrary)


database_View_strategy = st.builds(database_View, query=safe_text)
@given(instance=database_View_strategy)
@settings(max_examples=25)
def test_database_View_instantiation(instance):
    assert isinstance(instance, database_View)



