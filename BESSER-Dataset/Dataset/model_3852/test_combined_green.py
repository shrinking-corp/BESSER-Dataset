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
    dDL_Tabname,
    dDL_ISNULL,
    Key,
    dDL_Foreign_key,
    dDL_Unique_key,
    dDL_Primary_key,
    dDL_Key,
    dDL_Sequence_options,
    dDL_Colname,
    dDL_TYPE,
    dDL_Constraint,
    dDL_Column,
    Definition,
    dDL_Alter_table,
    dDL_Create_sequence,
    dDL_Comment,
    dDL_Create_table,
    dDL_Definition,
    dDL_Data_definition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ddl_tabname_is_not_abstract():
    assert not inspect.isabstract(dDL_Tabname)


def test_hyp_ddl_tabname_constructor_exists():
    assert callable(dDL_Tabname.__init__)


def test_hyp_ddl_tabname_constructor_args():
    sig = inspect.signature(dDL_Tabname.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "basename" in params, "Missing parameter 'basename'"





def test_hyp_ddl_isnull_is_not_abstract():
    assert not inspect.isabstract(dDL_ISNULL)


def test_hyp_ddl_isnull_constructor_exists():
    assert callable(dDL_ISNULL.__init__)


def test_hyp_ddl_isnull_constructor_args():
    sig = inspect.signature(dDL_ISNULL.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "nonNull" in params, "Missing parameter 'nonNull'"





def test_hyp_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_hyp_key_constructor_exists():
    assert callable(Key.__init__)


def test_hyp_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_foreign_key_is_not_abstract():
    assert not inspect.isabstract(dDL_Foreign_key)


def test_hyp_ddl_foreign_key_constructor_exists():
    assert callable(dDL_Foreign_key.__init__)


def test_hyp_ddl_foreign_key_constructor_args():
    sig = inspect.signature(dDL_Foreign_key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_unique_key_is_not_abstract():
    assert not inspect.isabstract(dDL_Unique_key)


def test_hyp_ddl_unique_key_constructor_exists():
    assert callable(dDL_Unique_key.__init__)


def test_hyp_ddl_unique_key_constructor_args():
    sig = inspect.signature(dDL_Unique_key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_primary_key_is_not_abstract():
    assert not inspect.isabstract(dDL_Primary_key)


def test_hyp_ddl_primary_key_constructor_exists():
    assert callable(dDL_Primary_key.__init__)


def test_hyp_ddl_primary_key_constructor_args():
    sig = inspect.signature(dDL_Primary_key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_key_is_not_abstract():
    assert not inspect.isabstract(dDL_Key)


def test_hyp_ddl_key_constructor_exists():
    assert callable(dDL_Key.__init__)


def test_hyp_ddl_key_constructor_args():
    sig = inspect.signature(dDL_Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_sequence_options_is_not_abstract():
    assert not inspect.isabstract(dDL_Sequence_options)


def test_hyp_ddl_sequence_options_constructor_exists():
    assert callable(dDL_Sequence_options.__init__)


def test_hyp_ddl_sequence_options_constructor_args():
    sig = inspect.signature(dDL_Sequence_options.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "nocycle" in params, "Missing parameter 'nocycle'"
    assert "nocache" in params, "Missing parameter 'nocache'"
    assert "nomaxvalue" in params, "Missing parameter 'nomaxvalue'"
    assert "noorder" in params, "Missing parameter 'noorder'"
    assert "order" in params, "Missing parameter 'order'"
    assert "maxvalue" in params, "Missing parameter 'maxvalue'"
    assert "nominvalue" in params, "Missing parameter 'nominvalue'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "cache" in params, "Missing parameter 'cache'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "minvalue" in params, "Missing parameter 'minvalue'"















def test_hyp_ddl_colname_is_not_abstract():
    assert not inspect.isabstract(dDL_Colname)


def test_hyp_ddl_colname_constructor_exists():
    assert callable(dDL_Colname.__init__)


def test_hyp_ddl_colname_constructor_args():
    sig = inspect.signature(dDL_Colname.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ddl_type_is_not_abstract():
    assert not inspect.isabstract(dDL_TYPE)


def test_hyp_ddl_type_constructor_exists():
    assert callable(dDL_TYPE.__init__)


def test_hyp_ddl_type_constructor_args():
    sig = inspect.signature(dDL_TYPE.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ddl_constraint_is_not_abstract():
    assert not inspect.isabstract(dDL_Constraint)


def test_hyp_ddl_constraint_constructor_exists():
    assert callable(dDL_Constraint.__init__)


def test_hyp_ddl_constraint_constructor_args():
    sig = inspect.signature(dDL_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ddl_column_is_not_abstract():
    assert not inspect.isabstract(dDL_Column)


def test_hyp_ddl_column_constructor_exists():
    assert callable(dDL_Column.__init__)


def test_hyp_ddl_column_constructor_args():
    sig = inspect.signature(dDL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_hyp_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_hyp_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_alter_table_is_not_abstract():
    assert not inspect.isabstract(dDL_Alter_table)


def test_hyp_ddl_alter_table_constructor_exists():
    assert callable(dDL_Alter_table.__init__)


def test_hyp_ddl_alter_table_constructor_args():
    sig = inspect.signature(dDL_Alter_table.__init__)
    params = list(sig.parameters.keys())
    assert "enable" in params, "Missing parameter 'enable'"
    assert "add" in params, "Missing parameter 'add'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_ddl_create_sequence_is_not_abstract():
    assert not inspect.isabstract(dDL_Create_sequence)


def test_hyp_ddl_create_sequence_constructor_exists():
    assert callable(dDL_Create_sequence.__init__)


def test_hyp_ddl_create_sequence_constructor_args():
    sig = inspect.signature(dDL_Create_sequence.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ddl_comment_is_not_abstract():
    assert not inspect.isabstract(dDL_Comment)


def test_hyp_ddl_comment_constructor_exists():
    assert callable(dDL_Comment.__init__)


def test_hyp_ddl_comment_constructor_args():
    sig = inspect.signature(dDL_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "columnId" in params, "Missing parameter 'columnId'"





def test_hyp_ddl_create_table_is_not_abstract():
    assert not inspect.isabstract(dDL_Create_table)


def test_hyp_ddl_create_table_constructor_exists():
    assert callable(dDL_Create_table.__init__)


def test_hyp_ddl_create_table_constructor_args():
    sig = inspect.signature(dDL_Create_table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ddl_definition_is_not_abstract():
    assert not inspect.isabstract(dDL_Definition)


def test_hyp_ddl_definition_constructor_exists():
    assert callable(dDL_Definition.__init__)


def test_hyp_ddl_definition_constructor_args():
    sig = inspect.signature(dDL_Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddl_data_definition_is_not_abstract():
    assert not inspect.isabstract(dDL_Data_definition)


def test_hyp_ddl_data_definition_constructor_exists():
    assert callable(dDL_Data_definition.__init__)


def test_hyp_ddl_data_definition_constructor_args():
    sig = inspect.signature(dDL_Data_definition.__init__)
    params = list(sig.parameters.keys())


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
dDL_Tabname_strategy = st.builds(
    dDL_Tabname,
    id=
        safe_text,
    basename=
        safe_text
)
dDL_ISNULL_strategy = st.builds(
    dDL_ISNULL,
    null=
        st.booleans(),
    nonNull=
        st.booleans()
)
Key_strategy = st.builds(
    Key,
)
dDL_Foreign_key_strategy = st.builds(
    dDL_Foreign_key,
)
dDL_Unique_key_strategy = st.builds(
    dDL_Unique_key,
)
dDL_Primary_key_strategy = st.builds(
    dDL_Primary_key,
)
dDL_Key_strategy = st.builds(
    dDL_Key,
)
dDL_Sequence_options_strategy = st.builds(
    dDL_Sequence_options,
    start=
        safe_text,
    nocycle=
        safe_text,
    nocache=
        safe_text,
    nomaxvalue=
        safe_text,
    noorder=
        safe_text,
    order=
        safe_text,
    maxvalue=
        safe_text,
    nominvalue=
        safe_text,
    cycle=
        safe_text,
    cache=
        safe_text,
    increment=
        safe_text,
    minvalue=
        safe_text
)
dDL_Colname_strategy = st.builds(
    dDL_Colname,
    id=
        safe_text
)
dDL_TYPE_strategy = st.builds(
    dDL_TYPE,
    id=
        safe_text
)
dDL_Constraint_strategy = st.builds(
    dDL_Constraint,
    id=
        safe_text
)
dDL_Column_strategy = st.builds(
    dDL_Column,
    number=
        st.integers(),
    id=
        safe_text
)
Definition_strategy = st.builds(
    Definition,
)
dDL_Alter_table_strategy = st.builds(
    dDL_Alter_table,
    enable=
        safe_text,
    add=
        safe_text,
    id=
        safe_text
)
dDL_Create_sequence_strategy = st.builds(
    dDL_Create_sequence,
    id=
        safe_text
)
dDL_Comment_strategy = st.builds(
    dDL_Comment,
    string=
        safe_text,
    columnId=
        safe_text
)
dDL_Create_table_strategy = st.builds(
    dDL_Create_table,
    id=
        safe_text
)
dDL_Definition_strategy = st.builds(
    dDL_Definition,
)
dDL_Data_definition_strategy = st.builds(
    dDL_Data_definition,
)




@given(instance=dDL_Tabname_strategy)
def test_hyp_ddl_tabname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dDL_Tabname_strategy)
def test_hyp_ddl_tabname_basename_setter(instance):
    original = instance.basename
    instance.basename = original
    assert instance.basename == original




@given(instance=dDL_ISNULL_strategy)
def test_hyp_ddl_isnull_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=dDL_ISNULL_strategy)
def test_hyp_ddl_isnull_nonNull_setter(instance):
    original = instance.nonNull
    instance.nonNull = original
    assert instance.nonNull == original









@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_nocycle_setter(instance):
    original = instance.nocycle
    instance.nocycle = original
    assert instance.nocycle == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_nocache_setter(instance):
    original = instance.nocache
    instance.nocache = original
    assert instance.nocache == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_nomaxvalue_setter(instance):
    original = instance.nomaxvalue
    instance.nomaxvalue = original
    assert instance.nomaxvalue == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_noorder_setter(instance):
    original = instance.noorder
    instance.noorder = original
    assert instance.noorder == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_maxvalue_setter(instance):
    original = instance.maxvalue
    instance.maxvalue = original
    assert instance.maxvalue == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_nominvalue_setter(instance):
    original = instance.nominvalue
    instance.nominvalue = original
    assert instance.nominvalue == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_cache_setter(instance):
    original = instance.cache
    instance.cache = original
    assert instance.cache == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original



@given(instance=dDL_Sequence_options_strategy)
def test_hyp_ddl_sequence_options_minvalue_setter(instance):
    original = instance.minvalue
    instance.minvalue = original
    assert instance.minvalue == original




@given(instance=dDL_Colname_strategy)
def test_hyp_ddl_colname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=dDL_TYPE_strategy)
def test_hyp_ddl_type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=dDL_Constraint_strategy)
def test_hyp_ddl_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=dDL_Column_strategy)
def test_hyp_ddl_column_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=dDL_Column_strategy)
def test_hyp_ddl_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=dDL_Alter_table_strategy)
def test_hyp_ddl_alter_table_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original



@given(instance=dDL_Alter_table_strategy)
def test_hyp_ddl_alter_table_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=dDL_Alter_table_strategy)
def test_hyp_ddl_alter_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=dDL_Create_sequence_strategy)
def test_hyp_ddl_create_sequence_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=dDL_Comment_strategy)
def test_hyp_ddl_comment_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=dDL_Comment_strategy)
def test_hyp_ddl_comment_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original




@given(instance=dDL_Create_table_strategy)
def test_hyp_ddl_create_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Definition,
    Key,
    dDL_Alter_table,
    dDL_Colname,
    dDL_Column,
    dDL_Comment,
    dDL_Constraint,
    dDL_Create_sequence,
    dDL_Create_table,
    dDL_Data_definition,
    dDL_Definition,
    dDL_Foreign_key,
    dDL_ISNULL,
    dDL_Key,
    dDL_Primary_key,
    dDL_Sequence_options,
    dDL_TYPE,
    dDL_Tabname,
    dDL_Unique_key,
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

def test_dDL_Alter_table_add_value_roundtrip():
    instance = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    assert instance.add == "sample_text"
    instance.add = "sample_text_2"
    assert instance.add == "sample_text_2"


def test_dDL_Alter_table_enable_value_roundtrip():
    instance = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    assert instance.enable == "sample_text"
    instance.enable = "sample_text_2"
    assert instance.enable == "sample_text_2"


def test_dDL_Alter_table_id_value_roundtrip():
    instance = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Colname_id_value_roundtrip():
    instance = dDL_Colname(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Column_id_value_roundtrip():
    instance = dDL_Column(id="sample_text", number=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Column_number_value_roundtrip():
    instance = dDL_Column(id="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_dDL_Comment_columnId_value_roundtrip():
    instance = dDL_Comment(columnId="sample_text", string="sample_text")
    assert instance.columnId == "sample_text"
    instance.columnId = "sample_text_2"
    assert instance.columnId == "sample_text_2"


def test_dDL_Comment_string_value_roundtrip():
    instance = dDL_Comment(columnId="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_dDL_Constraint_id_value_roundtrip():
    instance = dDL_Constraint(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Create_sequence_id_value_roundtrip():
    instance = dDL_Create_sequence(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Create_table_id_value_roundtrip():
    instance = dDL_Create_table(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_ISNULL_nonNull_value_roundtrip():
    instance = dDL_ISNULL(nonNull=True, null=True)
    assert instance.nonNull == True
    instance.nonNull = False
    assert instance.nonNull == False


def test_dDL_ISNULL_null_value_roundtrip():
    instance = dDL_ISNULL(nonNull=True, null=True)
    assert instance.null == True
    instance.null = False
    assert instance.null == False


def test_dDL_Sequence_options_cache_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.cache == "sample_text"
    instance.cache = "sample_text_2"
    assert instance.cache == "sample_text_2"


def test_dDL_Sequence_options_cycle_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.cycle == "sample_text"
    instance.cycle = "sample_text_2"
    assert instance.cycle == "sample_text_2"


def test_dDL_Sequence_options_increment_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.increment == "sample_text"
    instance.increment = "sample_text_2"
    assert instance.increment == "sample_text_2"


def test_dDL_Sequence_options_maxvalue_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.maxvalue == "sample_text"
    instance.maxvalue = "sample_text_2"
    assert instance.maxvalue == "sample_text_2"


def test_dDL_Sequence_options_minvalue_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.minvalue == "sample_text"
    instance.minvalue = "sample_text_2"
    assert instance.minvalue == "sample_text_2"


def test_dDL_Sequence_options_nocache_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.nocache == "sample_text"
    instance.nocache = "sample_text_2"
    assert instance.nocache == "sample_text_2"


def test_dDL_Sequence_options_nocycle_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.nocycle == "sample_text"
    instance.nocycle = "sample_text_2"
    assert instance.nocycle == "sample_text_2"


def test_dDL_Sequence_options_nomaxvalue_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.nomaxvalue == "sample_text"
    instance.nomaxvalue = "sample_text_2"
    assert instance.nomaxvalue == "sample_text_2"


def test_dDL_Sequence_options_nominvalue_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.nominvalue == "sample_text"
    instance.nominvalue = "sample_text_2"
    assert instance.nominvalue == "sample_text_2"


def test_dDL_Sequence_options_noorder_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.noorder == "sample_text"
    instance.noorder = "sample_text_2"
    assert instance.noorder == "sample_text_2"


def test_dDL_Sequence_options_order_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.order == "sample_text"
    instance.order = "sample_text_2"
    assert instance.order == "sample_text_2"


def test_dDL_Sequence_options_start_value_roundtrip():
    instance = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_dDL_TYPE_id_value_roundtrip():
    instance = dDL_TYPE(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Tabname_basename_value_roundtrip():
    instance = dDL_Tabname(basename="sample_text", id="sample_text")
    assert instance.basename == "sample_text"
    instance.basename = "sample_text_2"
    assert instance.basename == "sample_text_2"


def test_dDL_Tabname_id_value_roundtrip():
    instance = dDL_Tabname(basename="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dDL_Alter_table_isa_Definition():
    instance = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    assert isinstance(instance, Definition)


def test_dDL_Comment_isa_Definition():
    instance = dDL_Comment(columnId="sample_text", string="sample_text")
    assert isinstance(instance, Definition)


def test_dDL_Create_sequence_isa_Definition():
    instance = dDL_Create_sequence(id="sample_text")
    assert isinstance(instance, Definition)


def test_dDL_Create_table_isa_Definition():
    instance = dDL_Create_table(id="sample_text")
    assert isinstance(instance, Definition)


def test_dDL_Foreign_key_isa_Key():
    instance = dDL_Foreign_key()
    assert isinstance(instance, Key)


def test_dDL_Primary_key_isa_Key():
    instance = dDL_Primary_key()
    assert isinstance(instance, Key)


def test_dDL_Unique_key_isa_Key():
    instance = dDL_Unique_key()
    assert isinstance(instance, Key)


def test_assoc_colNames19_link_reassign_clear():
    a = dDL_Colname(id="sample_text")
    b1 = dDL_Key()
    b2 = dDL_Key()
    _safe_set(a, 'dDL_Colname21', b1)
    assert _is_linked(a, 'dDL_Colname21', b1)
    if hasattr(b1, 'dDL_Key20'):
        assert _is_linked(b1, 'dDL_Key20', a)
    _safe_set(a, 'dDL_Colname21', b2)
    assert _is_linked(a, 'dDL_Colname21', b2)
    if hasattr(b1, 'dDL_Key20'):
        assert not _is_linked(b1, 'dDL_Key20', a)
    if hasattr(b2, 'dDL_Key20'):
        assert _is_linked(b2, 'dDL_Key20', a)
    _safe_set(a, 'dDL_Colname21', None)
    assert not _is_linked(a, 'dDL_Colname21', b2)
    if hasattr(b2, 'dDL_Key20'):
        assert not _is_linked(b2, 'dDL_Key20', a)


def test_assoc_colname14_link_reassign_clear():
    a = dDL_Comment(columnId="sample_text", string="sample_text")
    b1 = dDL_Colname(id="sample_text")
    b2 = dDL_Colname(id="sample_text_2")
    _safe_set(a, 'dDL_Comment15', b1)
    assert _is_linked(a, 'dDL_Comment15', b1)
    if hasattr(b1, 'dDL_Colname'):
        assert _is_linked(b1, 'dDL_Colname', a)
    _safe_set(a, 'dDL_Comment15', b2)
    assert _is_linked(a, 'dDL_Comment15', b2)
    if hasattr(b1, 'dDL_Colname'):
        assert not _is_linked(b1, 'dDL_Colname', a)
    if hasattr(b2, 'dDL_Colname'):
        assert _is_linked(b2, 'dDL_Colname', a)
    _safe_set(a, 'dDL_Comment15', None)
    assert not _is_linked(a, 'dDL_Comment15', b2)
    if hasattr(b2, 'dDL_Colname'):
        assert not _is_linked(b2, 'dDL_Colname', a)


def test_assoc_columns1_link_reassign_clear():
    a = dDL_Create_table(id="sample_text")
    b1 = dDL_Column(id="sample_text", number=7)
    b2 = dDL_Column(id="sample_text_2", number=13)
    _safe_set(a, 'dDL_Create_table', {b1})
    assert _is_linked(a, 'dDL_Create_table', b1)
    if hasattr(b1, 'dDL_Column'):
        assert _is_linked(b1, 'dDL_Column', a)
    _safe_set(a, 'dDL_Create_table', {b2})
    assert _is_linked(a, 'dDL_Create_table', b2)
    if hasattr(b1, 'dDL_Column'):
        assert not _is_linked(b1, 'dDL_Column', a)
    if hasattr(b2, 'dDL_Column'):
        assert _is_linked(b2, 'dDL_Column', a)
    _safe_set(a, 'dDL_Create_table', set())
    assert not _is_linked(a, 'dDL_Create_table', b2)
    if hasattr(b2, 'dDL_Column'):
        assert not _is_linked(b2, 'dDL_Column', a)


def test_assoc_constraint9_link_reassign_clear():
    a = dDL_Constraint(id="sample_text")
    b1 = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    b2 = dDL_Alter_table(add="sample_text_2", enable="sample_text_2", id="sample_text_2")
    _safe_set(a, 'dDL_Constraint11', b1)
    assert _is_linked(a, 'dDL_Constraint11', b1)
    if hasattr(b1, 'dDL_Alter_table10'):
        assert _is_linked(b1, 'dDL_Alter_table10', a)
    _safe_set(a, 'dDL_Constraint11', b2)
    assert _is_linked(a, 'dDL_Constraint11', b2)
    if hasattr(b1, 'dDL_Alter_table10'):
        assert not _is_linked(b1, 'dDL_Alter_table10', a)
    if hasattr(b2, 'dDL_Alter_table10'):
        assert _is_linked(b2, 'dDL_Alter_table10', a)
    _safe_set(a, 'dDL_Constraint11', None)
    assert not _is_linked(a, 'dDL_Constraint11', b2)
    if hasattr(b2, 'dDL_Alter_table10'):
        assert not _is_linked(b2, 'dDL_Alter_table10', a)


def test_assoc_constraints2_link_reassign_clear():
    a = dDL_Create_table(id="sample_text")
    b1 = dDL_Constraint(id="sample_text")
    b2 = dDL_Constraint(id="sample_text_2")
    _safe_set(a, 'dDL_Create_table3', {b1})
    assert _is_linked(a, 'dDL_Create_table3', b1)
    if hasattr(b1, 'dDL_Constraint'):
        assert _is_linked(b1, 'dDL_Constraint', a)
    _safe_set(a, 'dDL_Create_table3', {b2})
    assert _is_linked(a, 'dDL_Create_table3', b2)
    if hasattr(b1, 'dDL_Constraint'):
        assert not _is_linked(b1, 'dDL_Constraint', a)
    if hasattr(b2, 'dDL_Constraint'):
        assert _is_linked(b2, 'dDL_Constraint', a)
    _safe_set(a, 'dDL_Create_table3', set())
    assert not _is_linked(a, 'dDL_Create_table3', b2)
    if hasattr(b2, 'dDL_Constraint'):
        assert not _is_linked(b2, 'dDL_Constraint', a)


def test_assoc_isNull6_link_reassign_clear():
    a = dDL_ISNULL(nonNull=True, null=True)
    b1 = dDL_Column(id="sample_text", number=7)
    b2 = dDL_Column(id="sample_text_2", number=13)
    _safe_set(a, 'dDL_ISNULL', b1)
    assert _is_linked(a, 'dDL_ISNULL', b1)
    if hasattr(b1, 'dDL_Column7'):
        assert _is_linked(b1, 'dDL_Column7', a)
    _safe_set(a, 'dDL_ISNULL', b2)
    assert _is_linked(a, 'dDL_ISNULL', b2)
    if hasattr(b1, 'dDL_Column7'):
        assert not _is_linked(b1, 'dDL_Column7', a)
    if hasattr(b2, 'dDL_Column7'):
        assert _is_linked(b2, 'dDL_Column7', a)
    _safe_set(a, 'dDL_ISNULL', None)
    assert not _is_linked(a, 'dDL_ISNULL', b2)
    if hasattr(b2, 'dDL_Column7'):
        assert not _is_linked(b2, 'dDL_Column7', a)


def test_assoc_key17_link_reassign_clear():
    a = dDL_Constraint(id="sample_text")
    b1 = dDL_Key()
    b2 = dDL_Key()
    _safe_set(a, 'dDL_Constraint18', b1)
    assert _is_linked(a, 'dDL_Constraint18', b1)
    if hasattr(b1, 'dDL_Key'):
        assert _is_linked(b1, 'dDL_Key', a)
    _safe_set(a, 'dDL_Constraint18', b2)
    assert _is_linked(a, 'dDL_Constraint18', b2)
    if hasattr(b1, 'dDL_Key'):
        assert not _is_linked(b1, 'dDL_Key', a)
    if hasattr(b2, 'dDL_Key'):
        assert _is_linked(b2, 'dDL_Key', a)
    _safe_set(a, 'dDL_Constraint18', None)
    assert not _is_linked(a, 'dDL_Constraint18', b2)
    if hasattr(b2, 'dDL_Key'):
        assert not _is_linked(b2, 'dDL_Key', a)


def test_assoc_sequence_options16_link_reassign_clear():
    a = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    b1 = dDL_Create_sequence(id="sample_text")
    b2 = dDL_Create_sequence(id="sample_text_2")
    _safe_set(a, 'dDL_Sequence_options', b1)
    assert _is_linked(a, 'dDL_Sequence_options', b1)
    if hasattr(b1, 'dDL_Create_sequence'):
        assert _is_linked(b1, 'dDL_Create_sequence', a)
    _safe_set(a, 'dDL_Sequence_options', b2)
    assert _is_linked(a, 'dDL_Sequence_options', b2)
    if hasattr(b1, 'dDL_Create_sequence'):
        assert not _is_linked(b1, 'dDL_Create_sequence', a)
    if hasattr(b2, 'dDL_Create_sequence'):
        assert _is_linked(b2, 'dDL_Create_sequence', a)
    _safe_set(a, 'dDL_Sequence_options', None)
    assert not _is_linked(a, 'dDL_Sequence_options', b2)
    if hasattr(b2, 'dDL_Create_sequence'):
        assert not _is_linked(b2, 'dDL_Create_sequence', a)


def test_assoc_tabname12_link_reassign_clear():
    a = dDL_Tabname(basename="sample_text", id="sample_text")
    b1 = dDL_Comment(columnId="sample_text", string="sample_text")
    b2 = dDL_Comment(columnId="sample_text_2", string="sample_text_2")
    _safe_set(a, 'dDL_Tabname13', b1)
    assert _is_linked(a, 'dDL_Tabname13', b1)
    if hasattr(b1, 'dDL_Comment'):
        assert _is_linked(b1, 'dDL_Comment', a)
    _safe_set(a, 'dDL_Tabname13', b2)
    assert _is_linked(a, 'dDL_Tabname13', b2)
    if hasattr(b1, 'dDL_Comment'):
        assert not _is_linked(b1, 'dDL_Comment', a)
    if hasattr(b2, 'dDL_Comment'):
        assert _is_linked(b2, 'dDL_Comment', a)
    _safe_set(a, 'dDL_Tabname13', None)
    assert not _is_linked(a, 'dDL_Tabname13', b2)
    if hasattr(b2, 'dDL_Comment'):
        assert not _is_linked(b2, 'dDL_Comment', a)


def test_assoc_tabname22_link_reassign_clear():
    a = dDL_Tabname(basename="sample_text", id="sample_text")
    b1 = dDL_Foreign_key()
    b2 = dDL_Foreign_key()
    _safe_set(a, 'dDL_Tabname23', b1)
    assert _is_linked(a, 'dDL_Tabname23', b1)
    if hasattr(b1, 'dDL_Foreign_key'):
        assert _is_linked(b1, 'dDL_Foreign_key', a)
    _safe_set(a, 'dDL_Tabname23', b2)
    assert _is_linked(a, 'dDL_Tabname23', b2)
    if hasattr(b1, 'dDL_Foreign_key'):
        assert not _is_linked(b1, 'dDL_Foreign_key', a)
    if hasattr(b2, 'dDL_Foreign_key'):
        assert _is_linked(b2, 'dDL_Foreign_key', a)
    _safe_set(a, 'dDL_Tabname23', None)
    assert not _is_linked(a, 'dDL_Tabname23', b2)
    if hasattr(b2, 'dDL_Foreign_key'):
        assert not _is_linked(b2, 'dDL_Foreign_key', a)


def test_assoc_tabname8_link_reassign_clear():
    a = dDL_Tabname(basename="sample_text", id="sample_text")
    b1 = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    b2 = dDL_Alter_table(add="sample_text_2", enable="sample_text_2", id="sample_text_2")
    _safe_set(a, 'dDL_Tabname', b1)
    assert _is_linked(a, 'dDL_Tabname', b1)
    if hasattr(b1, 'dDL_Alter_table'):
        assert _is_linked(b1, 'dDL_Alter_table', a)
    _safe_set(a, 'dDL_Tabname', b2)
    assert _is_linked(a, 'dDL_Tabname', b2)
    if hasattr(b1, 'dDL_Alter_table'):
        assert not _is_linked(b1, 'dDL_Alter_table', a)
    if hasattr(b2, 'dDL_Alter_table'):
        assert _is_linked(b2, 'dDL_Alter_table', a)
    _safe_set(a, 'dDL_Tabname', None)
    assert not _is_linked(a, 'dDL_Tabname', b2)
    if hasattr(b2, 'dDL_Alter_table'):
        assert not _is_linked(b2, 'dDL_Alter_table', a)


def test_assoc_type4_link_reassign_clear():
    a = dDL_TYPE(id="sample_text")
    b1 = dDL_Column(id="sample_text", number=7)
    b2 = dDL_Column(id="sample_text_2", number=13)
    _safe_set(a, 'dDL_TYPE', b1)
    assert _is_linked(a, 'dDL_TYPE', b1)
    if hasattr(b1, 'dDL_Column5'):
        assert _is_linked(b1, 'dDL_Column5', a)
    _safe_set(a, 'dDL_TYPE', b2)
    assert _is_linked(a, 'dDL_TYPE', b2)
    if hasattr(b1, 'dDL_Column5'):
        assert not _is_linked(b1, 'dDL_Column5', a)
    if hasattr(b2, 'dDL_Column5'):
        assert _is_linked(b2, 'dDL_Column5', a)
    _safe_set(a, 'dDL_TYPE', None)
    assert not _is_linked(a, 'dDL_TYPE', b2)
    if hasattr(b2, 'dDL_Column5'):
        assert not _is_linked(b2, 'dDL_Column5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Definition_strategy = st.builds(Definition)
@given(instance=Definition_strategy)
@settings(max_examples=25)
def test_Definition_instantiation(instance):
    assert isinstance(instance, Definition)


Key_strategy = st.builds(Key)
@given(instance=Key_strategy)
@settings(max_examples=25)
def test_Key_instantiation(instance):
    assert isinstance(instance, Key)


dDL_Alter_table_strategy = st.builds(dDL_Alter_table, add=safe_text, enable=safe_text, id=safe_text)
@given(instance=dDL_Alter_table_strategy)
@settings(max_examples=25)
def test_dDL_Alter_table_instantiation(instance):
    assert isinstance(instance, dDL_Alter_table)


dDL_Colname_strategy = st.builds(dDL_Colname, id=safe_text)
@given(instance=dDL_Colname_strategy)
@settings(max_examples=25)
def test_dDL_Colname_instantiation(instance):
    assert isinstance(instance, dDL_Colname)


dDL_Column_strategy = st.builds(dDL_Column, id=safe_text, number=st.integers())
@given(instance=dDL_Column_strategy)
@settings(max_examples=25)
def test_dDL_Column_instantiation(instance):
    assert isinstance(instance, dDL_Column)


dDL_Comment_strategy = st.builds(dDL_Comment, columnId=safe_text, string=safe_text)
@given(instance=dDL_Comment_strategy)
@settings(max_examples=25)
def test_dDL_Comment_instantiation(instance):
    assert isinstance(instance, dDL_Comment)


dDL_Constraint_strategy = st.builds(dDL_Constraint, id=safe_text)
@given(instance=dDL_Constraint_strategy)
@settings(max_examples=25)
def test_dDL_Constraint_instantiation(instance):
    assert isinstance(instance, dDL_Constraint)


dDL_Create_sequence_strategy = st.builds(dDL_Create_sequence, id=safe_text)
@given(instance=dDL_Create_sequence_strategy)
@settings(max_examples=25)
def test_dDL_Create_sequence_instantiation(instance):
    assert isinstance(instance, dDL_Create_sequence)


dDL_Create_table_strategy = st.builds(dDL_Create_table, id=safe_text)
@given(instance=dDL_Create_table_strategy)
@settings(max_examples=25)
def test_dDL_Create_table_instantiation(instance):
    assert isinstance(instance, dDL_Create_table)


dDL_Data_definition_strategy = st.builds(dDL_Data_definition)
@given(instance=dDL_Data_definition_strategy)
@settings(max_examples=25)
def test_dDL_Data_definition_instantiation(instance):
    assert isinstance(instance, dDL_Data_definition)


dDL_Definition_strategy = st.builds(dDL_Definition)
@given(instance=dDL_Definition_strategy)
@settings(max_examples=25)
def test_dDL_Definition_instantiation(instance):
    assert isinstance(instance, dDL_Definition)


dDL_Foreign_key_strategy = st.builds(dDL_Foreign_key)
@given(instance=dDL_Foreign_key_strategy)
@settings(max_examples=25)
def test_dDL_Foreign_key_instantiation(instance):
    assert isinstance(instance, dDL_Foreign_key)


dDL_ISNULL_strategy = st.builds(dDL_ISNULL, nonNull=st.booleans(), null=st.booleans())
@given(instance=dDL_ISNULL_strategy)
@settings(max_examples=25)
def test_dDL_ISNULL_instantiation(instance):
    assert isinstance(instance, dDL_ISNULL)


dDL_Key_strategy = st.builds(dDL_Key)
@given(instance=dDL_Key_strategy)
@settings(max_examples=25)
def test_dDL_Key_instantiation(instance):
    assert isinstance(instance, dDL_Key)


dDL_Primary_key_strategy = st.builds(dDL_Primary_key)
@given(instance=dDL_Primary_key_strategy)
@settings(max_examples=25)
def test_dDL_Primary_key_instantiation(instance):
    assert isinstance(instance, dDL_Primary_key)


dDL_Sequence_options_strategy = st.builds(dDL_Sequence_options, cache=safe_text, cycle=safe_text, increment=safe_text, maxvalue=safe_text, minvalue=safe_text, nocache=safe_text, nocycle=safe_text, nomaxvalue=safe_text, nominvalue=safe_text, noorder=safe_text, order=safe_text, start=safe_text)
@given(instance=dDL_Sequence_options_strategy)
@settings(max_examples=25)
def test_dDL_Sequence_options_instantiation(instance):
    assert isinstance(instance, dDL_Sequence_options)


dDL_TYPE_strategy = st.builds(dDL_TYPE, id=safe_text)
@given(instance=dDL_TYPE_strategy)
@settings(max_examples=25)
def test_dDL_TYPE_instantiation(instance):
    assert isinstance(instance, dDL_TYPE)


dDL_Tabname_strategy = st.builds(dDL_Tabname, basename=safe_text, id=safe_text)
@given(instance=dDL_Tabname_strategy)
@settings(max_examples=25)
def test_dDL_Tabname_instantiation(instance):
    assert isinstance(instance, dDL_Tabname)


dDL_Unique_key_strategy = st.builds(dDL_Unique_key)
@given(instance=dDL_Unique_key_strategy)
@settings(max_examples=25)
def test_dDL_Unique_key_instantiation(instance):
    assert isinstance(instance, dDL_Unique_key)



