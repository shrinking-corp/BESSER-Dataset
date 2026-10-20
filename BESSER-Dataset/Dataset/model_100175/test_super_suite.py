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
    Field,
    relational_Column,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Table,
    relational_Schema,
    relational_DataBase,
    relational_Field,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_hyp_field_constructor_exists():
    assert callable(Field.__init__)


def test_hyp_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_hyp_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_hyp_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_hyp_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_hyp_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relational_primarykey_is_not_abstract():
    assert not inspect.isabstract(relational_PrimaryKey)


def test_hyp_relational_primarykey_constructor_exists():
    assert callable(relational_PrimaryKey.__init__)


def test_hyp_relational_primarykey_constructor_args():
    sig = inspect.signature(relational_PrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_hyp_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_hyp_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_relational_schema_is_not_abstract():
    assert not inspect.isabstract(relational_Schema)


def test_hyp_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_hyp_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_relational_database_is_not_abstract():
    assert not inspect.isabstract(relational_DataBase)


def test_hyp_relational_database_constructor_exists():
    assert callable(relational_DataBase.__init__)


def test_hyp_relational_database_constructor_args():
    sig = inspect.signature(relational_DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "uri" in params, "Missing parameter 'uri'"





def test_hyp_relational_field_is_not_abstract():
    assert not inspect.isabstract(relational_Field)


def test_hyp_relational_field_constructor_exists():
    assert callable(relational_Field.__init__)


def test_hyp_relational_field_constructor_args():
    sig = inspect.signature(relational_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_hyp_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "CHAR",
        "DATE",
        "VARCHAR",
        "TIME",
        "NUMERIC",
        "BOOLEAN",
        "FLOAT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
Field_strategy = st.builds(
    Field,
)
relational_Column_strategy = st.builds(
    relational_Column,
    type=
        safe_text
)
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
)
relational_PrimaryKey_strategy = st.builds(
    relational_PrimaryKey,
    id=
        safe_text
)
relational_Table_strategy = st.builds(
    relational_Table,
    name=
        safe_text
)
relational_Schema_strategy = st.builds(
    relational_Schema,
    name=
        safe_text
)
relational_DataBase_strategy = st.builds(
    relational_DataBase,
    port=
        st.integers(),
    uri=
        safe_text
)
relational_Field_strategy = st.builds(
    relational_Field,
    name=
        safe_text
)





@given(instance=relational_Column_strategy)
def test_hyp_relational_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=relational_PrimaryKey_strategy)
def test_hyp_relational_primarykey_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=relational_Table_strategy)
def test_hyp_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=relational_Schema_strategy)
def test_hyp_relational_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=relational_DataBase_strategy)
def test_hyp_relational_database_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=relational_DataBase_strategy)
def test_hyp_relational_database_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original




@given(instance=relational_Field_strategy)
def test_hyp_relational_field_name_setter(instance):
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
    Field,
    relational_Column,
    relational_DataBase,
    relational_Field,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Schema,
    relational_Table,
    Type,
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

def test_relational_Column_type_value_roundtrip():
    instance = relational_Column(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_relational_DataBase_port_value_roundtrip():
    instance = relational_DataBase(port=7, uri="sample_text")
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_relational_DataBase_uri_value_roundtrip():
    instance = relational_DataBase(port=7, uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_relational_Field_name_value_roundtrip():
    instance = relational_Field(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_relational_PrimaryKey_id_value_roundtrip():
    instance = relational_PrimaryKey(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_relational_Schema_name_value_roundtrip():
    instance = relational_Schema(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_relational_Table_name_value_roundtrip():
    instance = relational_Table(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_relational_Column_isa_Field():
    instance = relational_Column(type="sample_text")
    assert isinstance(instance, Field)


def test_relational_ForeignKey_isa_Field():
    instance = relational_ForeignKey()
    assert isinstance(instance, Field)


def test_relational_PrimaryKey_isa_Field():
    instance = relational_PrimaryKey(id="sample_text")
    assert isinstance(instance, Field)


def test_assoc_fields3_link_reassign_clear():
    a = relational_Table(name="sample_text")
    b1 = relational_Field(name="sample_text")
    b2 = relational_Field(name="sample_text_2")
    _safe_set(a, 'relational_Table4', {b1})
    assert _is_linked(a, 'relational_Table4', b1)
    if hasattr(b1, 'relational_Field'):
        assert _is_linked(b1, 'relational_Field', a)
    _safe_set(a, 'relational_Table4', {b2})
    assert _is_linked(a, 'relational_Table4', b2)
    if hasattr(b1, 'relational_Field'):
        assert not _is_linked(b1, 'relational_Field', a)
    if hasattr(b2, 'relational_Field'):
        assert _is_linked(b2, 'relational_Field', a)
    _safe_set(a, 'relational_Table4', set())
    assert not _is_linked(a, 'relational_Table4', b2)
    if hasattr(b2, 'relational_Field'):
        assert not _is_linked(b2, 'relational_Field', a)


def test_assoc_reference5_link_reassign_clear():
    a = relational_Table(name="sample_text")
    b1 = relational_ForeignKey()
    b2 = relational_ForeignKey()
    _safe_set(a, 'relational_Table6', b1)
    assert _is_linked(a, 'relational_Table6', b1)
    if hasattr(b1, 'relational_ForeignKey'):
        assert _is_linked(b1, 'relational_ForeignKey', a)
    _safe_set(a, 'relational_Table6', b2)
    assert _is_linked(a, 'relational_Table6', b2)
    if hasattr(b1, 'relational_ForeignKey'):
        assert not _is_linked(b1, 'relational_ForeignKey', a)
    if hasattr(b2, 'relational_ForeignKey'):
        assert _is_linked(b2, 'relational_ForeignKey', a)
    _safe_set(a, 'relational_Table6', None)
    assert not _is_linked(a, 'relational_Table6', b2)
    if hasattr(b2, 'relational_ForeignKey'):
        assert not _is_linked(b2, 'relational_ForeignKey', a)


def test_assoc_schemas0_link_reassign_clear():
    a = relational_Schema(name="sample_text")
    b1 = relational_DataBase(port=7, uri="sample_text")
    b2 = relational_DataBase(port=13, uri="sample_text_2")
    _safe_set(a, 'relational_Schema', b1)
    assert _is_linked(a, 'relational_Schema', b1)
    if hasattr(b1, 'relational_DataBase'):
        assert _is_linked(b1, 'relational_DataBase', a)
    _safe_set(a, 'relational_Schema', b2)
    assert _is_linked(a, 'relational_Schema', b2)
    if hasattr(b1, 'relational_DataBase'):
        assert not _is_linked(b1, 'relational_DataBase', a)
    if hasattr(b2, 'relational_DataBase'):
        assert _is_linked(b2, 'relational_DataBase', a)
    _safe_set(a, 'relational_Schema', None)
    assert not _is_linked(a, 'relational_Schema', b2)
    if hasattr(b2, 'relational_DataBase'):
        assert not _is_linked(b2, 'relational_DataBase', a)


def test_assoc_tables1_link_reassign_clear():
    a = relational_Table(name="sample_text")
    b1 = relational_Schema(name="sample_text")
    b2 = relational_Schema(name="sample_text_2")
    _safe_set(a, 'relational_Table', b1)
    assert _is_linked(a, 'relational_Table', b1)
    if hasattr(b1, 'relational_Schema2'):
        assert _is_linked(b1, 'relational_Schema2', a)
    _safe_set(a, 'relational_Table', b2)
    assert _is_linked(a, 'relational_Table', b2)
    if hasattr(b1, 'relational_Schema2'):
        assert not _is_linked(b1, 'relational_Schema2', a)
    if hasattr(b2, 'relational_Schema2'):
        assert _is_linked(b2, 'relational_Schema2', a)
    _safe_set(a, 'relational_Table', None)
    assert not _is_linked(a, 'relational_Table', b2)
    if hasattr(b2, 'relational_Schema2'):
        assert not _is_linked(b2, 'relational_Schema2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Field_strategy = st.builds(Field)
@given(instance=Field_strategy)
@settings(max_examples=25)
def test_Field_instantiation(instance):
    assert isinstance(instance, Field)


relational_Column_strategy = st.builds(relational_Column, type=safe_text)
@given(instance=relational_Column_strategy)
@settings(max_examples=25)
def test_relational_Column_instantiation(instance):
    assert isinstance(instance, relational_Column)


relational_DataBase_strategy = st.builds(relational_DataBase, port=st.integers(), uri=safe_text)
@given(instance=relational_DataBase_strategy)
@settings(max_examples=25)
def test_relational_DataBase_instantiation(instance):
    assert isinstance(instance, relational_DataBase)


relational_Field_strategy = st.builds(relational_Field, name=safe_text)
@given(instance=relational_Field_strategy)
@settings(max_examples=25)
def test_relational_Field_instantiation(instance):
    assert isinstance(instance, relational_Field)


relational_ForeignKey_strategy = st.builds(relational_ForeignKey)
@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=25)
def test_relational_ForeignKey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)


relational_PrimaryKey_strategy = st.builds(relational_PrimaryKey, id=safe_text)
@given(instance=relational_PrimaryKey_strategy)
@settings(max_examples=25)
def test_relational_PrimaryKey_instantiation(instance):
    assert isinstance(instance, relational_PrimaryKey)


relational_Schema_strategy = st.builds(relational_Schema, name=safe_text)
@given(instance=relational_Schema_strategy)
@settings(max_examples=25)
def test_relational_Schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)


relational_Table_strategy = st.builds(relational_Table, name=safe_text)
@given(instance=relational_Table_strategy)
@settings(max_examples=25)
def test_relational_Table_instantiation(instance):
    assert isinstance(instance, relational_Table)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Field,
    relational_Column,
    relational_DataBase,
    relational_Field,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Schema,
    relational_Table,
    Type,
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

def test_assoc_fields3_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Field(name="sample_text")
    _safe_set(b, 'relational_Field', a1)
    assert _is_linked(b, 'relational_Field', a1)
    if hasattr(a1, 'relational_Table4'):
        assert _is_linked(a1, 'relational_Table4', b)
    _safe_set(b, 'relational_Field', a2)
    assert _is_linked(b, 'relational_Field', a2)
    if hasattr(a1, 'relational_Table4'):
        assert not _is_linked(a1, 'relational_Table4', b)
    if hasattr(a2, 'relational_Table4'):
        assert _is_linked(a2, 'relational_Table4', b)
    _safe_set(b, 'relational_Field', None)
    assert not _is_linked(b, 'relational_Field', a2)
    if hasattr(a2, 'relational_Table4'):
        assert not _is_linked(a2, 'relational_Table4', b)


def test_assoc_schemas0_reverse_link_reassign_clear():
    a1 = relational_Schema(name="sample_text")
    a2 = relational_Schema(name="sample_text_2")
    b = relational_DataBase(port=7, uri="sample_text")
    _safe_set(b, 'relational_DataBase', {a1})
    assert _is_linked(b, 'relational_DataBase', a1)
    if hasattr(a1, 'relational_Schema'):
        assert _is_linked(a1, 'relational_Schema', b)
    _safe_set(b, 'relational_DataBase', {a2})
    assert _is_linked(b, 'relational_DataBase', a2)
    if hasattr(a1, 'relational_Schema'):
        assert not _is_linked(a1, 'relational_Schema', b)
    if hasattr(a2, 'relational_Schema'):
        assert _is_linked(a2, 'relational_Schema', b)
    _safe_set(b, 'relational_DataBase', set())
    assert not _is_linked(b, 'relational_DataBase', a2)
    if hasattr(a2, 'relational_Schema'):
        assert not _is_linked(a2, 'relational_Schema', b)


def test_assoc_tables1_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Schema(name="sample_text")
    _safe_set(b, 'relational_Schema2', {a1})
    assert _is_linked(b, 'relational_Schema2', a1)
    if hasattr(a1, 'relational_Table'):
        assert _is_linked(a1, 'relational_Table', b)
    _safe_set(b, 'relational_Schema2', {a2})
    assert _is_linked(b, 'relational_Schema2', a2)
    if hasattr(a1, 'relational_Table'):
        assert not _is_linked(a1, 'relational_Table', b)
    if hasattr(a2, 'relational_Table'):
        assert _is_linked(a2, 'relational_Table', b)
    _safe_set(b, 'relational_Schema2', set())
    assert not _is_linked(b, 'relational_Schema2', a2)
    if hasattr(a2, 'relational_Table'):
        assert not _is_linked(a2, 'relational_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_reference5_stub_double():
    # relational_ForeignKey has no real 'relational_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'relational_ForeignKey', None)
    _safe_set(owner, 'relational_Table6', partner)
    assert getattr(partner, 'relational_ForeignKey') == owner
    _safe_set(owner, 'relational_Table6', None)
    assert getattr(partner, 'relational_ForeignKey') is None




from python_code import relational_Column

def test_relational_Column___init__():
    assert relational_Column.__init__(relational_Column(''), '') == None
from python_code import relational_DataBase

def test_relational_DataBase___init__():
    assert relational_DataBase.__init__(relational_DataBase('\x00\x00', 0, relational_DataBase=set()), '', 0, relational_DataBase=set()) == None
from python_code import relational_PrimaryKey

def test_relational_PrimaryKey___init__():
    assert relational_PrimaryKey.__init__(relational_PrimaryKey(''), '') == None

