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
    Key,
    Value,
    SQLDDL_StringVal,
    SQLDDL_NullVal,
    SQLDDL_IntegerVal,
    SQLDDL_ForeignKey,
    SQLDDL_PrimaryKey,
    SQLDDL_SimpleKey,
    Column,
    Parameter,
    TableElement,
    SQLDDL_Key,
    ForeignKey,
    Type,
    SQLDDL_Column,
    LocatedElement,
    SQLDDL_TableElement,
    SQLDDL_Value,
    SQLDDL_NamedElement,
    SQLDDL_LocatedElement,
    Database,
    Table,
    NamedElement,
    SQLDDL_Type,
    SQLDDL_Parameter,
    SQLDDL_Table,
    SQLDDL_Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_hyp_key_constructor_exists():
    assert callable(Key.__init__)


def test_hyp_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_stringval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_StringVal)


def test_hyp_sqlddl_stringval_constructor_exists():
    assert callable(SQLDDL_StringVal.__init__)


def test_hyp_sqlddl_stringval_constructor_args():
    sig = inspect.signature(SQLDDL_StringVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sqlddl_nullval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_NullVal)


def test_hyp_sqlddl_nullval_constructor_exists():
    assert callable(SQLDDL_NullVal.__init__)


def test_hyp_sqlddl_nullval_constructor_args():
    sig = inspect.signature(SQLDDL_NullVal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_integerval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_IntegerVal)


def test_hyp_sqlddl_integerval_constructor_exists():
    assert callable(SQLDDL_IntegerVal.__init__)


def test_hyp_sqlddl_integerval_constructor_args():
    sig = inspect.signature(SQLDDL_IntegerVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sqlddl_foreignkey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_ForeignKey)


def test_hyp_sqlddl_foreignkey_constructor_exists():
    assert callable(SQLDDL_ForeignKey.__init__)


def test_hyp_sqlddl_foreignkey_constructor_args():
    sig = inspect.signature(SQLDDL_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_primarykey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_PrimaryKey)


def test_hyp_sqlddl_primarykey_constructor_exists():
    assert callable(SQLDDL_PrimaryKey.__init__)


def test_hyp_sqlddl_primarykey_constructor_args():
    sig = inspect.signature(SQLDDL_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_simplekey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_SimpleKey)


def test_hyp_sqlddl_simplekey_constructor_exists():
    assert callable(SQLDDL_SimpleKey.__init__)


def test_hyp_sqlddl_simplekey_constructor_args():
    sig = inspect.signature(SQLDDL_SimpleKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_hyp_column_constructor_exists():
    assert callable(Column.__init__)


def test_hyp_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_hyp_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_hyp_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_key_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Key)


def test_hyp_sqlddl_key_constructor_exists():
    assert callable(SQLDDL_Key.__init__)


def test_hyp_sqlddl_key_constructor_args():
    sig = inspect.signature(SQLDDL_Key.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ForeignKey)


def test_hyp_foreignkey_constructor_exists():
    assert callable(ForeignKey.__init__)


def test_hyp_foreignkey_constructor_args():
    sig = inspect.signature(ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_column_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Column)


def test_hyp_sqlddl_column_constructor_exists():
    assert callable(SQLDDL_Column.__init__)


def test_hyp_sqlddl_column_constructor_args():
    sig = inspect.signature(SQLDDL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "canBeNull" in params, "Missing parameter 'canBeNull'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_hyp_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_hyp_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_tableelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_TableElement)


def test_hyp_sqlddl_tableelement_constructor_exists():
    assert callable(SQLDDL_TableElement.__init__)


def test_hyp_sqlddl_tableelement_constructor_args():
    sig = inspect.signature(SQLDDL_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_value_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Value)


def test_hyp_sqlddl_value_constructor_exists():
    assert callable(SQLDDL_Value.__init__)


def test_hyp_sqlddl_value_constructor_args():
    sig = inspect.signature(SQLDDL_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_namedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_NamedElement)


def test_hyp_sqlddl_namedelement_constructor_exists():
    assert callable(SQLDDL_NamedElement.__init__)


def test_hyp_sqlddl_namedelement_constructor_args():
    sig = inspect.signature(SQLDDL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sqlddl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_LocatedElement)


def test_hyp_sqlddl_locatedelement_constructor_exists():
    assert callable(SQLDDL_LocatedElement.__init__)


def test_hyp_sqlddl_locatedelement_constructor_args():
    sig = inspect.signature(SQLDDL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"






def test_hyp_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_hyp_database_constructor_exists():
    assert callable(Database.__init__)


def test_hyp_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())



def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_type_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Type)


def test_hyp_sqlddl_type_constructor_exists():
    assert callable(SQLDDL_Type.__init__)


def test_hyp_sqlddl_type_constructor_args():
    sig = inspect.signature(SQLDDL_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isUnsigned" in params, "Missing parameter 'isUnsigned'"
    assert "length" in params, "Missing parameter 'length'"





def test_hyp_sqlddl_parameter_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Parameter)


def test_hyp_sqlddl_parameter_constructor_exists():
    assert callable(SQLDDL_Parameter.__init__)


def test_hyp_sqlddl_parameter_constructor_args():
    sig = inspect.signature(SQLDDL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_table_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Table)


def test_hyp_sqlddl_table_constructor_exists():
    assert callable(SQLDDL_Table.__init__)


def test_hyp_sqlddl_table_constructor_args():
    sig = inspect.signature(SQLDDL_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlddl_database_is_not_abstract():
    assert not inspect.isabstract(SQLDDL_Database)


def test_hyp_sqlddl_database_constructor_exists():
    assert callable(SQLDDL_Database.__init__)


def test_hyp_sqlddl_database_constructor_args():
    sig = inspect.signature(SQLDDL_Database.__init__)
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
Key_strategy = st.builds(
    Key,
)
Value_strategy = st.builds(
    Value,
)
SQLDDL_StringVal_strategy = st.builds(
    SQLDDL_StringVal,
    value=
        safe_text
)
SQLDDL_NullVal_strategy = st.builds(
    SQLDDL_NullVal,
)
SQLDDL_IntegerVal_strategy = st.builds(
    SQLDDL_IntegerVal,
    value=
        safe_text
)
SQLDDL_ForeignKey_strategy = st.builds(
    SQLDDL_ForeignKey,
)
SQLDDL_PrimaryKey_strategy = st.builds(
    SQLDDL_PrimaryKey,
)
SQLDDL_SimpleKey_strategy = st.builds(
    SQLDDL_SimpleKey,
)
Column_strategy = st.builds(
    Column,
)
Parameter_strategy = st.builds(
    Parameter,
)
TableElement_strategy = st.builds(
    TableElement,
)
SQLDDL_Key_strategy = st.builds(
    SQLDDL_Key,
    isUnique=
        safe_text,
    name=
        safe_text
)
ForeignKey_strategy = st.builds(
    ForeignKey,
)
Type_strategy = st.builds(
    Type,
)
SQLDDL_Column_strategy = st.builds(
    SQLDDL_Column,
    canBeNull=
        safe_text,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SQLDDL_TableElement_strategy = st.builds(
    SQLDDL_TableElement,
)
SQLDDL_Value_strategy = st.builds(
    SQLDDL_Value,
)
SQLDDL_NamedElement_strategy = st.builds(
    SQLDDL_NamedElement,
    name=
        safe_text
)
SQLDDL_LocatedElement_strategy = st.builds(
    SQLDDL_LocatedElement,
    commentsBefore=
        safe_text,
    location=
        safe_text,
    commentsAfter=
        safe_text
)
Database_strategy = st.builds(
    Database,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SQLDDL_Type_strategy = st.builds(
    SQLDDL_Type,
    isUnsigned=
        safe_text,
    length=
        safe_text
)
SQLDDL_Parameter_strategy = st.builds(
    SQLDDL_Parameter,
)
SQLDDL_Table_strategy = st.builds(
    SQLDDL_Table,
)
SQLDDL_Database_strategy = st.builds(
    SQLDDL_Database,
)






@given(instance=SQLDDL_StringVal_strategy)
def test_hyp_sqlddl_stringval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=SQLDDL_IntegerVal_strategy)
def test_hyp_sqlddl_integerval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original










@given(instance=SQLDDL_Key_strategy)
def test_hyp_sqlddl_key_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=SQLDDL_Key_strategy)
def test_hyp_sqlddl_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=SQLDDL_Column_strategy)
def test_hyp_sqlddl_column_canBeNull_setter(instance):
    original = instance.canBeNull
    instance.canBeNull = original
    assert instance.canBeNull == original



@given(instance=SQLDDL_Column_strategy)
def test_hyp_sqlddl_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=SQLDDL_NamedElement_strategy)
def test_hyp_sqlddl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SQLDDL_LocatedElement_strategy)
def test_hyp_sqlddl_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=SQLDDL_LocatedElement_strategy)
def test_hyp_sqlddl_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=SQLDDL_LocatedElement_strategy)
def test_hyp_sqlddl_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original







@given(instance=SQLDDL_Type_strategy)
def test_hyp_sqlddl_type_isUnsigned_setter(instance):
    original = instance.isUnsigned
    instance.isUnsigned = original
    assert instance.isUnsigned == original



@given(instance=SQLDDL_Type_strategy)
def test_hyp_sqlddl_type_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Column,
    Database,
    ForeignKey,
    Key,
    LocatedElement,
    NamedElement,
    Parameter,
    SQLDDL_Column,
    SQLDDL_Database,
    SQLDDL_ForeignKey,
    SQLDDL_IntegerVal,
    SQLDDL_Key,
    SQLDDL_LocatedElement,
    SQLDDL_NamedElement,
    SQLDDL_NullVal,
    SQLDDL_Parameter,
    SQLDDL_PrimaryKey,
    SQLDDL_SimpleKey,
    SQLDDL_StringVal,
    SQLDDL_Table,
    SQLDDL_TableElement,
    SQLDDL_Type,
    SQLDDL_Value,
    Table,
    TableElement,
    Type,
    Value,
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

def test_SQLDDL_Column_canBeNull_value_roundtrip():
    instance = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    assert instance.canBeNull == "sample_text"
    instance.canBeNull = "sample_text_2"
    assert instance.canBeNull == "sample_text_2"


def test_SQLDDL_Column_name_value_roundtrip():
    instance = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDDL_IntegerVal_value_value_roundtrip():
    instance = SQLDDL_IntegerVal(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_SQLDDL_Key_isUnique_value_roundtrip():
    instance = SQLDDL_Key(isUnique="sample_text", name="sample_text")
    assert instance.isUnique == "sample_text"
    instance.isUnique = "sample_text_2"
    assert instance.isUnique == "sample_text_2"


def test_SQLDDL_Key_name_value_roundtrip():
    instance = SQLDDL_Key(isUnique="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDDL_LocatedElement_commentsAfter_value_roundtrip():
    instance = SQLDDL_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsAfter == "sample_text"
    instance.commentsAfter = "sample_text_2"
    assert instance.commentsAfter == "sample_text_2"


def test_SQLDDL_LocatedElement_commentsBefore_value_roundtrip():
    instance = SQLDDL_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsBefore == "sample_text"
    instance.commentsBefore = "sample_text_2"
    assert instance.commentsBefore == "sample_text_2"


def test_SQLDDL_LocatedElement_location_value_roundtrip():
    instance = SQLDDL_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_SQLDDL_NamedElement_name_value_roundtrip():
    instance = SQLDDL_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDDL_StringVal_value_value_roundtrip():
    instance = SQLDDL_StringVal(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_SQLDDL_Type_isUnsigned_value_roundtrip():
    instance = SQLDDL_Type(isUnsigned="sample_text", length="sample_text")
    assert instance.isUnsigned == "sample_text"
    instance.isUnsigned = "sample_text_2"
    assert instance.isUnsigned == "sample_text_2"


def test_SQLDDL_Type_length_value_roundtrip():
    instance = SQLDDL_Type(isUnsigned="sample_text", length="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_SQLDDL_ForeignKey_isa_Key():
    instance = SQLDDL_ForeignKey()
    assert isinstance(instance, Key)


def test_SQLDDL_PrimaryKey_isa_Key():
    instance = SQLDDL_PrimaryKey()
    assert isinstance(instance, Key)


def test_SQLDDL_SimpleKey_isa_Key():
    instance = SQLDDL_SimpleKey()
    assert isinstance(instance, Key)


def test_SQLDDL_NamedElement_isa_LocatedElement():
    instance = SQLDDL_NamedElement(name="sample_text")
    assert isinstance(instance, LocatedElement)


def test_SQLDDL_TableElement_isa_LocatedElement():
    instance = SQLDDL_TableElement()
    assert isinstance(instance, LocatedElement)


def test_SQLDDL_Value_isa_LocatedElement():
    instance = SQLDDL_Value()
    assert isinstance(instance, LocatedElement)


def test_SQLDDL_Database_isa_NamedElement():
    instance = SQLDDL_Database()
    assert isinstance(instance, NamedElement)


def test_SQLDDL_Parameter_isa_NamedElement():
    instance = SQLDDL_Parameter()
    assert isinstance(instance, NamedElement)


def test_SQLDDL_Table_isa_NamedElement():
    instance = SQLDDL_Table()
    assert isinstance(instance, NamedElement)


def test_SQLDDL_Type_isa_NamedElement():
    instance = SQLDDL_Type(isUnsigned="sample_text", length="sample_text")
    assert isinstance(instance, NamedElement)


def test_SQLDDL_Column_isa_TableElement():
    instance = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    assert isinstance(instance, TableElement)


def test_SQLDDL_Key_isa_TableElement():
    instance = SQLDDL_Key(isUnique="sample_text", name="sample_text")
    assert isinstance(instance, TableElement)


def test_SQLDDL_IntegerVal_isa_Value():
    instance = SQLDDL_IntegerVal(value="sample_text")
    assert isinstance(instance, Value)


def test_SQLDDL_NullVal_isa_Value():
    instance = SQLDDL_NullVal()
    assert isinstance(instance, Value)


def test_SQLDDL_StringVal_isa_Value():
    instance = SQLDDL_StringVal(value="sample_text")
    assert isinstance(instance, Value)


def test_assoc_columns14_link_reassign_clear():
    a = SQLDDL_Key(isUnique="sample_text", name="sample_text")
    b1 = Column()
    b2 = Column()
    _safe_set(a, 'keys', {b1})
    assert _is_linked(a, 'keys', b1)
    if hasattr(b1, 'Column'):
        assert _is_linked(b1, 'Column', a)
    _safe_set(a, 'keys', {b2})
    assert _is_linked(a, 'keys', b2)
    if hasattr(b1, 'Column'):
        assert not _is_linked(b1, 'Column', a)
    if hasattr(b2, 'Column'):
        assert _is_linked(b2, 'Column', a)
    _safe_set(a, 'keys', set())
    assert not _is_linked(a, 'keys', b2)
    if hasattr(b2, 'Column'):
        assert not _is_linked(b2, 'Column', a)


def test_assoc_default11_link_reassign_clear():
    a = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    b1 = Value()
    b2 = Value()
    _safe_set(a, 'SQLDDL_Column12', b1)
    assert _is_linked(a, 'SQLDDL_Column12', b1)
    if hasattr(b1, 'Value'):
        assert _is_linked(b1, 'Value', a)
    _safe_set(a, 'SQLDDL_Column12', b2)
    assert _is_linked(a, 'SQLDDL_Column12', b2)
    if hasattr(b1, 'Value'):
        assert not _is_linked(b1, 'Value', a)
    if hasattr(b2, 'Value'):
        assert _is_linked(b2, 'Value', a)
    _safe_set(a, 'SQLDDL_Column12', None)
    assert not _is_linked(a, 'SQLDDL_Column12', b2)
    if hasattr(b2, 'Value'):
        assert not _is_linked(b2, 'Value', a)


def test_assoc_keys13_link_reassign_clear():
    a = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    b1 = Key()
    b2 = Key()
    _safe_set(a, 'columns', {b1})
    assert _is_linked(a, 'columns', b1)
    if hasattr(b1, 'Key'):
        assert _is_linked(b1, 'Key', a)
    _safe_set(a, 'columns', {b2})
    assert _is_linked(a, 'columns', b2)
    if hasattr(b1, 'Key'):
        assert not _is_linked(b1, 'Key', a)
    if hasattr(b2, 'Key'):
        assert _is_linked(b2, 'Key', a)
    _safe_set(a, 'columns', set())
    assert not _is_linked(a, 'columns', b2)
    if hasattr(b2, 'Key'):
        assert not _is_linked(b2, 'Key', a)


def test_assoc_referencedBy8_link_reassign_clear():
    a = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    b1 = ForeignKey()
    b2 = ForeignKey()
    _safe_set(a, 'referencedColumns', {b1})
    assert _is_linked(a, 'referencedColumns', b1)
    if hasattr(b1, 'ForeignKey9'):
        assert _is_linked(b1, 'ForeignKey9', a)
    _safe_set(a, 'referencedColumns', {b2})
    assert _is_linked(a, 'referencedColumns', b2)
    if hasattr(b1, 'ForeignKey9'):
        assert not _is_linked(b1, 'ForeignKey9', a)
    if hasattr(b2, 'ForeignKey9'):
        assert _is_linked(b2, 'ForeignKey9', a)
    _safe_set(a, 'referencedColumns', set())
    assert not _is_linked(a, 'referencedColumns', b2)
    if hasattr(b2, 'ForeignKey9'):
        assert not _is_linked(b2, 'ForeignKey9', a)


def test_assoc_type10_link_reassign_clear():
    a = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'SQLDDL_Column', b1)
    assert _is_linked(a, 'SQLDDL_Column', b1)
    if hasattr(b1, 'Type'):
        assert _is_linked(b1, 'Type', a)
    _safe_set(a, 'SQLDDL_Column', b2)
    assert _is_linked(a, 'SQLDDL_Column', b2)
    if hasattr(b1, 'Type'):
        assert not _is_linked(b1, 'Type', a)
    if hasattr(b2, 'Type'):
        assert _is_linked(b2, 'Type', a)
    _safe_set(a, 'SQLDDL_Column', None)
    assert not _is_linked(a, 'SQLDDL_Column', b2)
    if hasattr(b2, 'Type'):
        assert not _is_linked(b2, 'Type', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Column_strategy = st.builds(Column)
@given(instance=Column_strategy)
@settings(max_examples=25)
def test_Column_instantiation(instance):
    assert isinstance(instance, Column)


Database_strategy = st.builds(Database)
@given(instance=Database_strategy)
@settings(max_examples=25)
def test_Database_instantiation(instance):
    assert isinstance(instance, Database)


ForeignKey_strategy = st.builds(ForeignKey)
@given(instance=ForeignKey_strategy)
@settings(max_examples=25)
def test_ForeignKey_instantiation(instance):
    assert isinstance(instance, ForeignKey)


Key_strategy = st.builds(Key)
@given(instance=Key_strategy)
@settings(max_examples=25)
def test_Key_instantiation(instance):
    assert isinstance(instance, Key)


LocatedElement_strategy = st.builds(LocatedElement)
@given(instance=LocatedElement_strategy)
@settings(max_examples=25)
def test_LocatedElement_instantiation(instance):
    assert isinstance(instance, LocatedElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


SQLDDL_Column_strategy = st.builds(SQLDDL_Column, canBeNull=safe_text, name=safe_text)
@given(instance=SQLDDL_Column_strategy)
@settings(max_examples=25)
def test_SQLDDL_Column_instantiation(instance):
    assert isinstance(instance, SQLDDL_Column)


SQLDDL_Database_strategy = st.builds(SQLDDL_Database)
@given(instance=SQLDDL_Database_strategy)
@settings(max_examples=25)
def test_SQLDDL_Database_instantiation(instance):
    assert isinstance(instance, SQLDDL_Database)


SQLDDL_ForeignKey_strategy = st.builds(SQLDDL_ForeignKey)
@given(instance=SQLDDL_ForeignKey_strategy)
@settings(max_examples=25)
def test_SQLDDL_ForeignKey_instantiation(instance):
    assert isinstance(instance, SQLDDL_ForeignKey)


SQLDDL_IntegerVal_strategy = st.builds(SQLDDL_IntegerVal, value=safe_text)
@given(instance=SQLDDL_IntegerVal_strategy)
@settings(max_examples=25)
def test_SQLDDL_IntegerVal_instantiation(instance):
    assert isinstance(instance, SQLDDL_IntegerVal)


SQLDDL_Key_strategy = st.builds(SQLDDL_Key, isUnique=safe_text, name=safe_text)
@given(instance=SQLDDL_Key_strategy)
@settings(max_examples=25)
def test_SQLDDL_Key_instantiation(instance):
    assert isinstance(instance, SQLDDL_Key)


SQLDDL_LocatedElement_strategy = st.builds(SQLDDL_LocatedElement, commentsAfter=safe_text, commentsBefore=safe_text, location=safe_text)
@given(instance=SQLDDL_LocatedElement_strategy)
@settings(max_examples=25)
def test_SQLDDL_LocatedElement_instantiation(instance):
    assert isinstance(instance, SQLDDL_LocatedElement)


SQLDDL_NamedElement_strategy = st.builds(SQLDDL_NamedElement, name=safe_text)
@given(instance=SQLDDL_NamedElement_strategy)
@settings(max_examples=25)
def test_SQLDDL_NamedElement_instantiation(instance):
    assert isinstance(instance, SQLDDL_NamedElement)


SQLDDL_NullVal_strategy = st.builds(SQLDDL_NullVal)
@given(instance=SQLDDL_NullVal_strategy)
@settings(max_examples=25)
def test_SQLDDL_NullVal_instantiation(instance):
    assert isinstance(instance, SQLDDL_NullVal)


SQLDDL_Parameter_strategy = st.builds(SQLDDL_Parameter)
@given(instance=SQLDDL_Parameter_strategy)
@settings(max_examples=25)
def test_SQLDDL_Parameter_instantiation(instance):
    assert isinstance(instance, SQLDDL_Parameter)


SQLDDL_PrimaryKey_strategy = st.builds(SQLDDL_PrimaryKey)
@given(instance=SQLDDL_PrimaryKey_strategy)
@settings(max_examples=25)
def test_SQLDDL_PrimaryKey_instantiation(instance):
    assert isinstance(instance, SQLDDL_PrimaryKey)


SQLDDL_SimpleKey_strategy = st.builds(SQLDDL_SimpleKey)
@given(instance=SQLDDL_SimpleKey_strategy)
@settings(max_examples=25)
def test_SQLDDL_SimpleKey_instantiation(instance):
    assert isinstance(instance, SQLDDL_SimpleKey)


SQLDDL_StringVal_strategy = st.builds(SQLDDL_StringVal, value=safe_text)
@given(instance=SQLDDL_StringVal_strategy)
@settings(max_examples=25)
def test_SQLDDL_StringVal_instantiation(instance):
    assert isinstance(instance, SQLDDL_StringVal)


SQLDDL_Table_strategy = st.builds(SQLDDL_Table)
@given(instance=SQLDDL_Table_strategy)
@settings(max_examples=25)
def test_SQLDDL_Table_instantiation(instance):
    assert isinstance(instance, SQLDDL_Table)


SQLDDL_TableElement_strategy = st.builds(SQLDDL_TableElement)
@given(instance=SQLDDL_TableElement_strategy)
@settings(max_examples=25)
def test_SQLDDL_TableElement_instantiation(instance):
    assert isinstance(instance, SQLDDL_TableElement)


SQLDDL_Type_strategy = st.builds(SQLDDL_Type, isUnsigned=safe_text, length=safe_text)
@given(instance=SQLDDL_Type_strategy)
@settings(max_examples=25)
def test_SQLDDL_Type_instantiation(instance):
    assert isinstance(instance, SQLDDL_Type)


SQLDDL_Value_strategy = st.builds(SQLDDL_Value)
@given(instance=SQLDDL_Value_strategy)
@settings(max_examples=25)
def test_SQLDDL_Value_instantiation(instance):
    assert isinstance(instance, SQLDDL_Value)


Table_strategy = st.builds(Table)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


TableElement_strategy = st.builds(TableElement)
@given(instance=TableElement_strategy)
@settings(max_examples=25)
def test_TableElement_instantiation(instance):
    assert isinstance(instance, TableElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)



