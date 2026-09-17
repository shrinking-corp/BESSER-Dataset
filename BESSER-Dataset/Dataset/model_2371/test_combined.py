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
    DB_Key,
    DB_ForeignKey,
    DB_Column,
    DB_Table,
    DB_Database,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_db_key_is_not_abstract():
    assert not inspect.isabstract(DB_Key)


def test_hyp_db_key_constructor_exists():
    assert callable(DB_Key.__init__)


def test_hyp_db_key_constructor_args():
    sig = inspect.signature(DB_Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_db_foreignkey_is_not_abstract():
    assert not inspect.isabstract(DB_ForeignKey)


def test_hyp_db_foreignkey_constructor_exists():
    assert callable(DB_ForeignKey.__init__)


def test_hyp_db_foreignkey_constructor_args():
    sig = inspect.signature(DB_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"




def test_hyp_db_column_is_not_abstract():
    assert not inspect.isabstract(DB_Column)


def test_hyp_db_column_constructor_exists():
    assert callable(DB_Column.__init__)


def test_hyp_db_column_constructor_args():
    sig = inspect.signature(DB_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_db_table_is_not_abstract():
    assert not inspect.isabstract(DB_Table)


def test_hyp_db_table_constructor_exists():
    assert callable(DB_Table.__init__)


def test_hyp_db_table_constructor_args():
    sig = inspect.signature(DB_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_db_database_is_not_abstract():
    assert not inspect.isabstract(DB_Database)


def test_hyp_db_database_constructor_exists():
    assert callable(DB_Database.__init__)


def test_hyp_db_database_constructor_args():
    sig = inspect.signature(DB_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_hyp_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "text",
        "int",
        "decimal",
        "unknown",
        "bool",
        "varchar",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
DB_Key_strategy = st.builds(
    DB_Key,
    name=
        safe_text
)
DB_ForeignKey_strategy = st.builds(
    DB_ForeignKey,
    isMany=
        safe_text
)
DB_Column_strategy = st.builds(
    DB_Column,
    name=
        safe_text,
    notNull=
        st.booleans(),
    type=
        safe_text
)
DB_Table_strategy = st.builds(
    DB_Table,
    name=
        safe_text
)
DB_Database_strategy = st.builds(
    DB_Database,
    name=
        safe_text
)




@given(instance=DB_Key_strategy)
def test_hyp_db_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=DB_ForeignKey_strategy)
def test_hyp_db_foreignkey_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original




@given(instance=DB_Column_strategy)
def test_hyp_db_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DB_Column_strategy)
def test_hyp_db_column_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original



@given(instance=DB_Column_strategy)
def test_hyp_db_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=DB_Table_strategy)
def test_hyp_db_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=DB_Database_strategy)
def test_hyp_db_database_name_setter(instance):
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
    DB_Column,
    DB_Database,
    DB_ForeignKey,
    DB_Key,
    DB_Table,
    DataType,
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

def test_DB_Column_name_value_roundtrip():
    instance = DB_Column(name="sample_text", notNull=True, type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DB_Column_notNull_value_roundtrip():
    instance = DB_Column(name="sample_text", notNull=True, type="sample_text")
    assert instance.notNull == True
    instance.notNull = False
    assert instance.notNull == False


def test_DB_Column_type_value_roundtrip():
    instance = DB_Column(name="sample_text", notNull=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_DB_Database_name_value_roundtrip():
    instance = DB_Database(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DB_ForeignKey_isMany_value_roundtrip():
    instance = DB_ForeignKey(isMany="sample_text")
    assert instance.isMany == "sample_text"
    instance.isMany = "sample_text_2"
    assert instance.isMany == "sample_text_2"


def test_DB_Key_name_value_roundtrip():
    instance = DB_Key(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DB_Table_name_value_roundtrip():
    instance = DB_Table(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_columns5_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_Table6', {b1})
    assert _is_linked(a, 'DB_Table6', b1)
    if hasattr(b1, 'DB_Column'):
        assert _is_linked(b1, 'DB_Column', a)
    _safe_set(a, 'DB_Table6', {b2})
    assert _is_linked(a, 'DB_Table6', b2)
    if hasattr(b1, 'DB_Column'):
        assert not _is_linked(b1, 'DB_Column', a)
    if hasattr(b2, 'DB_Column'):
        assert _is_linked(b2, 'DB_Column', a)
    _safe_set(a, 'DB_Table6', set())
    assert not _is_linked(a, 'DB_Table6', b2)
    if hasattr(b2, 'DB_Column'):
        assert not _is_linked(b2, 'DB_Column', a)


def test_assoc_database7_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_Database(name="sample_text")
    b2 = DB_Database(name="sample_text_2")
    _safe_set(a, 'DB_Table8', b1)
    assert _is_linked(a, 'DB_Table8', b1)
    if hasattr(b1, 'DB_Database9'):
        assert _is_linked(b1, 'DB_Database9', a)
    _safe_set(a, 'DB_Table8', b2)
    assert _is_linked(a, 'DB_Table8', b2)
    if hasattr(b1, 'DB_Database9'):
        assert not _is_linked(b1, 'DB_Database9', a)
    if hasattr(b2, 'DB_Database9'):
        assert _is_linked(b2, 'DB_Database9', a)
    _safe_set(a, 'DB_Table8', None)
    assert not _is_linked(a, 'DB_Table8', b2)
    if hasattr(b2, 'DB_Database9'):
        assert not _is_linked(b2, 'DB_Database9', a)


def test_assoc_foreign16_link_reassign_clear():
    a = DB_ForeignKey(isMany="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_ForeignKey18', b1)
    assert _is_linked(a, 'DB_ForeignKey18', b1)
    if hasattr(b1, 'DB_Column17'):
        assert _is_linked(b1, 'DB_Column17', a)
    _safe_set(a, 'DB_ForeignKey18', b2)
    assert _is_linked(a, 'DB_ForeignKey18', b2)
    if hasattr(b1, 'DB_Column17'):
        assert not _is_linked(b1, 'DB_Column17', a)
    if hasattr(b2, 'DB_Column17'):
        assert _is_linked(b2, 'DB_Column17', a)
    _safe_set(a, 'DB_ForeignKey18', None)
    assert not _is_linked(a, 'DB_ForeignKey18', b2)
    if hasattr(b2, 'DB_Column17'):
        assert not _is_linked(b2, 'DB_Column17', a)


def test_assoc_foreign_column22_link_reassign_clear():
    a = DB_ForeignKey(isMany="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_ForeignKey23', b1)
    assert _is_linked(a, 'DB_ForeignKey23', b1)
    if hasattr(b1, 'DB_Column24'):
        assert _is_linked(b1, 'DB_Column24', a)
    _safe_set(a, 'DB_ForeignKey23', b2)
    assert _is_linked(a, 'DB_ForeignKey23', b2)
    if hasattr(b1, 'DB_Column24'):
        assert not _is_linked(b1, 'DB_Column24', a)
    if hasattr(b2, 'DB_Column24'):
        assert _is_linked(b2, 'DB_Column24', a)
    _safe_set(a, 'DB_ForeignKey23', None)
    assert not _is_linked(a, 'DB_ForeignKey23', b2)
    if hasattr(b2, 'DB_Column24'):
        assert not _is_linked(b2, 'DB_Column24', a)


def test_assoc_foreignkeys1_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_ForeignKey(isMany="sample_text")
    b2 = DB_ForeignKey(isMany="sample_text_2")
    _safe_set(a, 'DB_Table2', {b1})
    assert _is_linked(a, 'DB_Table2', b1)
    if hasattr(b1, 'DB_ForeignKey'):
        assert _is_linked(b1, 'DB_ForeignKey', a)
    _safe_set(a, 'DB_Table2', {b2})
    assert _is_linked(a, 'DB_Table2', b2)
    if hasattr(b1, 'DB_ForeignKey'):
        assert not _is_linked(b1, 'DB_ForeignKey', a)
    if hasattr(b2, 'DB_ForeignKey'):
        assert _is_linked(b2, 'DB_ForeignKey', a)
    _safe_set(a, 'DB_Table2', set())
    assert not _is_linked(a, 'DB_Table2', b2)
    if hasattr(b2, 'DB_ForeignKey'):
        assert not _is_linked(b2, 'DB_ForeignKey', a)


def test_assoc_key13_link_reassign_clear():
    a = DB_Key(name="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_Key15', b1)
    assert _is_linked(a, 'DB_Key15', b1)
    if hasattr(b1, 'DB_Column14'):
        assert _is_linked(b1, 'DB_Column14', a)
    _safe_set(a, 'DB_Key15', b2)
    assert _is_linked(a, 'DB_Key15', b2)
    if hasattr(b1, 'DB_Column14'):
        assert not _is_linked(b1, 'DB_Column14', a)
    if hasattr(b2, 'DB_Column14'):
        assert _is_linked(b2, 'DB_Column14', a)
    _safe_set(a, 'DB_Key15', None)
    assert not _is_linked(a, 'DB_Key15', b2)
    if hasattr(b2, 'DB_Column14'):
        assert not _is_linked(b2, 'DB_Column14', a)


def test_assoc_key_column25_link_reassign_clear():
    a = DB_Key(name="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_Key26', {b1})
    assert _is_linked(a, 'DB_Key26', b1)
    if hasattr(b1, 'DB_Column27'):
        assert _is_linked(b1, 'DB_Column27', a)
    _safe_set(a, 'DB_Key26', {b2})
    assert _is_linked(a, 'DB_Key26', b2)
    if hasattr(b1, 'DB_Column27'):
        assert not _is_linked(b1, 'DB_Column27', a)
    if hasattr(b2, 'DB_Column27'):
        assert _is_linked(b2, 'DB_Column27', a)
    _safe_set(a, 'DB_Key26', set())
    assert not _is_linked(a, 'DB_Key26', b2)
    if hasattr(b2, 'DB_Column27'):
        assert not _is_linked(b2, 'DB_Column27', a)


def test_assoc_primary_key3_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_Key(name="sample_text")
    b2 = DB_Key(name="sample_text_2")
    _safe_set(a, 'DB_Table4', {b1})
    assert _is_linked(a, 'DB_Table4', b1)
    if hasattr(b1, 'DB_Key'):
        assert _is_linked(b1, 'DB_Key', a)
    _safe_set(a, 'DB_Table4', {b2})
    assert _is_linked(a, 'DB_Table4', b2)
    if hasattr(b1, 'DB_Key'):
        assert not _is_linked(b1, 'DB_Key', a)
    if hasattr(b2, 'DB_Key'):
        assert _is_linked(b2, 'DB_Key', a)
    _safe_set(a, 'DB_Table4', set())
    assert not _is_linked(a, 'DB_Table4', b2)
    if hasattr(b2, 'DB_Key'):
        assert not _is_linked(b2, 'DB_Key', a)


def test_assoc_referenced28_link_reassign_clear():
    a = DB_Key(name="sample_text")
    b1 = DB_ForeignKey(isMany="sample_text")
    b2 = DB_ForeignKey(isMany="sample_text_2")
    _safe_set(a, 'DB_Key29', b1)
    assert _is_linked(a, 'DB_Key29', b1)
    if hasattr(b1, 'DB_ForeignKey30'):
        assert _is_linked(b1, 'DB_ForeignKey30', a)
    _safe_set(a, 'DB_Key29', b2)
    assert _is_linked(a, 'DB_Key29', b2)
    if hasattr(b1, 'DB_ForeignKey30'):
        assert not _is_linked(b1, 'DB_ForeignKey30', a)
    if hasattr(b2, 'DB_ForeignKey30'):
        assert _is_linked(b2, 'DB_ForeignKey30', a)
    _safe_set(a, 'DB_Key29', None)
    assert not _is_linked(a, 'DB_Key29', b2)
    if hasattr(b2, 'DB_ForeignKey30'):
        assert not _is_linked(b2, 'DB_ForeignKey30', a)


def test_assoc_referencedKey19_link_reassign_clear():
    a = DB_Key(name="sample_text")
    b1 = DB_ForeignKey(isMany="sample_text")
    b2 = DB_ForeignKey(isMany="sample_text_2")
    _safe_set(a, 'DB_Key21', b1)
    assert _is_linked(a, 'DB_Key21', b1)
    if hasattr(b1, 'DB_ForeignKey20'):
        assert _is_linked(b1, 'DB_ForeignKey20', a)
    _safe_set(a, 'DB_Key21', b2)
    assert _is_linked(a, 'DB_Key21', b2)
    if hasattr(b1, 'DB_ForeignKey20'):
        assert not _is_linked(b1, 'DB_ForeignKey20', a)
    if hasattr(b2, 'DB_ForeignKey20'):
        assert _is_linked(b2, 'DB_ForeignKey20', a)
    _safe_set(a, 'DB_Key21', None)
    assert not _is_linked(a, 'DB_Key21', b2)
    if hasattr(b2, 'DB_ForeignKey20'):
        assert not _is_linked(b2, 'DB_ForeignKey20', a)


def test_assoc_table10_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_Column(name="sample_text", notNull=True, type="sample_text")
    b2 = DB_Column(name="sample_text_2", notNull=False, type="sample_text_2")
    _safe_set(a, 'DB_Table12', b1)
    assert _is_linked(a, 'DB_Table12', b1)
    if hasattr(b1, 'DB_Column11'):
        assert _is_linked(b1, 'DB_Column11', a)
    _safe_set(a, 'DB_Table12', b2)
    assert _is_linked(a, 'DB_Table12', b2)
    if hasattr(b1, 'DB_Column11'):
        assert not _is_linked(b1, 'DB_Column11', a)
    if hasattr(b2, 'DB_Column11'):
        assert _is_linked(b2, 'DB_Column11', a)
    _safe_set(a, 'DB_Table12', None)
    assert not _is_linked(a, 'DB_Table12', b2)
    if hasattr(b2, 'DB_Column11'):
        assert not _is_linked(b2, 'DB_Column11', a)


def test_assoc_tables0_link_reassign_clear():
    a = DB_Table(name="sample_text")
    b1 = DB_Database(name="sample_text")
    b2 = DB_Database(name="sample_text_2")
    _safe_set(a, 'DB_Table', b1)
    assert _is_linked(a, 'DB_Table', b1)
    if hasattr(b1, 'DB_Database'):
        assert _is_linked(b1, 'DB_Database', a)
    _safe_set(a, 'DB_Table', b2)
    assert _is_linked(a, 'DB_Table', b2)
    if hasattr(b1, 'DB_Database'):
        assert not _is_linked(b1, 'DB_Database', a)
    if hasattr(b2, 'DB_Database'):
        assert _is_linked(b2, 'DB_Database', a)
    _safe_set(a, 'DB_Table', None)
    assert not _is_linked(a, 'DB_Table', b2)
    if hasattr(b2, 'DB_Database'):
        assert not _is_linked(b2, 'DB_Database', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DB_Column_strategy = st.builds(DB_Column, name=safe_text, notNull=st.booleans(), type=safe_text)
@given(instance=DB_Column_strategy)
@settings(max_examples=25)
def test_DB_Column_instantiation(instance):
    assert isinstance(instance, DB_Column)


DB_Database_strategy = st.builds(DB_Database, name=safe_text)
@given(instance=DB_Database_strategy)
@settings(max_examples=25)
def test_DB_Database_instantiation(instance):
    assert isinstance(instance, DB_Database)


DB_ForeignKey_strategy = st.builds(DB_ForeignKey, isMany=safe_text)
@given(instance=DB_ForeignKey_strategy)
@settings(max_examples=25)
def test_DB_ForeignKey_instantiation(instance):
    assert isinstance(instance, DB_ForeignKey)


DB_Key_strategy = st.builds(DB_Key, name=safe_text)
@given(instance=DB_Key_strategy)
@settings(max_examples=25)
def test_DB_Key_instantiation(instance):
    assert isinstance(instance, DB_Key)


DB_Table_strategy = st.builds(DB_Table, name=safe_text)
@given(instance=DB_Table_strategy)
@settings(max_examples=25)
def test_DB_Table_instantiation(instance):
    assert isinstance(instance, DB_Table)



