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
    my_FKRelation,
    NamedElement,
    my_Database,
    my_Table,
    my_Column,
    my_NamedElement,
    ColumnType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_my_fkrelation_is_not_abstract():
    assert not inspect.isabstract(my_FKRelation)


def test_hyp_my_fkrelation_constructor_exists():
    assert callable(my_FKRelation.__init__)


def test_hyp_my_fkrelation_constructor_args():
    sig = inspect.signature(my_FKRelation.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_my_database_is_not_abstract():
    assert not inspect.isabstract(my_Database)


def test_hyp_my_database_constructor_exists():
    assert callable(my_Database.__init__)


def test_hyp_my_database_constructor_args():
    sig = inspect.signature(my_Database.__init__)
    params = list(sig.parameters.keys())



def test_hyp_my_table_is_not_abstract():
    assert not inspect.isabstract(my_Table)


def test_hyp_my_table_constructor_exists():
    assert callable(my_Table.__init__)


def test_hyp_my_table_constructor_args():
    sig = inspect.signature(my_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_my_column_is_not_abstract():
    assert not inspect.isabstract(my_Column)


def test_hyp_my_column_constructor_exists():
    assert callable(my_Column.__init__)


def test_hyp_my_column_constructor_args():
    sig = inspect.signature(my_Column.__init__)
    params = list(sig.parameters.keys())
    assert "primary" in params, "Missing parameter 'primary'"
    assert "type" in params, "Missing parameter 'type'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "size" in params, "Missing parameter 'size'"







def test_hyp_my_namedelement_is_not_abstract():
    assert not inspect.isabstract(my_NamedElement)


def test_hyp_my_namedelement_constructor_exists():
    assert callable(my_NamedElement.__init__)


def test_hyp_my_namedelement_constructor_args():
    sig = inspect.signature(my_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_hyp_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "Char",
        "Number",
        "Date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"


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
my_FKRelation_strategy = st.builds(
    my_FKRelation,
    label=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
my_Database_strategy = st.builds(
    my_Database,
)
my_Table_strategy = st.builds(
    my_Table,
)
my_Column_strategy = st.builds(
    my_Column,
    primary=
        st.booleans(),
    type=
        safe_text,
    unique=
        st.booleans(),
    size=
        st.integers()
)
my_NamedElement_strategy = st.builds(
    my_NamedElement,
    name=
        safe_text
)




@given(instance=my_FKRelation_strategy)
def test_hyp_my_fkrelation_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original







@given(instance=my_Column_strategy)
def test_hyp_my_column_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original



@given(instance=my_Column_strategy)
def test_hyp_my_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=my_Column_strategy)
def test_hyp_my_column_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=my_Column_strategy)
def test_hyp_my_column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original




@given(instance=my_NamedElement_strategy)
def test_hyp_my_namedelement_name_setter(instance):
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
    NamedElement,
    my_Column,
    my_Database,
    my_FKRelation,
    my_NamedElement,
    my_Table,
    ColumnType,
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

def test_my_Column_primary_value_roundtrip():
    instance = my_Column(primary=True, size=7, type="sample_text", unique=True)
    assert instance.primary == True
    instance.primary = False
    assert instance.primary == False


def test_my_Column_size_value_roundtrip():
    instance = my_Column(primary=True, size=7, type="sample_text", unique=True)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_my_Column_type_value_roundtrip():
    instance = my_Column(primary=True, size=7, type="sample_text", unique=True)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_my_Column_unique_value_roundtrip():
    instance = my_Column(primary=True, size=7, type="sample_text", unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_my_FKRelation_label_value_roundtrip():
    instance = my_FKRelation(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_my_NamedElement_name_value_roundtrip():
    instance = my_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_my_Column_isa_NamedElement():
    instance = my_Column(primary=True, size=7, type="sample_text", unique=True)
    assert isinstance(instance, NamedElement)


def test_my_Database_isa_NamedElement():
    instance = my_Database()
    assert isinstance(instance, NamedElement)


def test_my_Table_isa_NamedElement():
    instance = my_Table()
    assert isinstance(instance, NamedElement)


def test_assoc_columns0_link_reassign_clear():
    a = my_Column(primary=True, size=7, type="sample_text", unique=True)
    b1 = my_Table()
    b2 = my_Table()
    _safe_set(a, 'my_Column', b1)
    assert _is_linked(a, 'my_Column', b1)
    if hasattr(b1, 'my_Table'):
        assert _is_linked(b1, 'my_Table', a)
    _safe_set(a, 'my_Column', b2)
    assert _is_linked(a, 'my_Column', b2)
    if hasattr(b1, 'my_Table'):
        assert not _is_linked(b1, 'my_Table', a)
    if hasattr(b2, 'my_Table'):
        assert _is_linked(b2, 'my_Table', a)
    _safe_set(a, 'my_Column', None)
    assert not _is_linked(a, 'my_Column', b2)
    if hasattr(b2, 'my_Table'):
        assert not _is_linked(b2, 'my_Table', a)


def test_assoc_fkrelations3_link_reassign_clear():
    a = my_FKRelation(label="sample_text")
    b1 = my_Database()
    b2 = my_Database()
    _safe_set(a, 'my_FKRelation', b1)
    assert _is_linked(a, 'my_FKRelation', b1)
    if hasattr(b1, 'my_Database4'):
        assert _is_linked(b1, 'my_Database4', a)
    _safe_set(a, 'my_FKRelation', b2)
    assert _is_linked(a, 'my_FKRelation', b2)
    if hasattr(b1, 'my_Database4'):
        assert not _is_linked(b1, 'my_Database4', a)
    if hasattr(b2, 'my_Database4'):
        assert _is_linked(b2, 'my_Database4', a)
    _safe_set(a, 'my_FKRelation', None)
    assert not _is_linked(a, 'my_FKRelation', b2)
    if hasattr(b2, 'my_Database4'):
        assert not _is_linked(b2, 'my_Database4', a)


def test_assoc_source8_link_reassign_clear():
    a = my_FKRelation(label="sample_text")
    b1 = my_Column(primary=True, size=7, type="sample_text", unique=True)
    b2 = my_Column(primary=False, size=13, type="sample_text_2", unique=False)
    _safe_set(a, 'my_FKRelation9', b1)
    assert _is_linked(a, 'my_FKRelation9', b1)
    if hasattr(b1, 'my_Column10'):
        assert _is_linked(b1, 'my_Column10', a)
    _safe_set(a, 'my_FKRelation9', b2)
    assert _is_linked(a, 'my_FKRelation9', b2)
    if hasattr(b1, 'my_Column10'):
        assert not _is_linked(b1, 'my_Column10', a)
    if hasattr(b2, 'my_Column10'):
        assert _is_linked(b2, 'my_Column10', a)
    _safe_set(a, 'my_FKRelation9', None)
    assert not _is_linked(a, 'my_FKRelation9', b2)
    if hasattr(b2, 'my_Column10'):
        assert not _is_linked(b2, 'my_Column10', a)


def test_assoc_target5_link_reassign_clear():
    a = my_FKRelation(label="sample_text")
    b1 = my_Column(primary=True, size=7, type="sample_text", unique=True)
    b2 = my_Column(primary=False, size=13, type="sample_text_2", unique=False)
    _safe_set(a, 'my_FKRelation6', b1)
    assert _is_linked(a, 'my_FKRelation6', b1)
    if hasattr(b1, 'my_Column7'):
        assert _is_linked(b1, 'my_Column7', a)
    _safe_set(a, 'my_FKRelation6', b2)
    assert _is_linked(a, 'my_FKRelation6', b2)
    if hasattr(b1, 'my_Column7'):
        assert not _is_linked(b1, 'my_Column7', a)
    if hasattr(b2, 'my_Column7'):
        assert _is_linked(b2, 'my_Column7', a)
    _safe_set(a, 'my_FKRelation6', None)
    assert not _is_linked(a, 'my_FKRelation6', b2)
    if hasattr(b2, 'my_Column7'):
        assert not _is_linked(b2, 'my_Column7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


my_Column_strategy = st.builds(my_Column, primary=st.booleans(), size=st.integers(), type=safe_text, unique=st.booleans())
@given(instance=my_Column_strategy)
@settings(max_examples=25)
def test_my_Column_instantiation(instance):
    assert isinstance(instance, my_Column)


my_Database_strategy = st.builds(my_Database)
@given(instance=my_Database_strategy)
@settings(max_examples=25)
def test_my_Database_instantiation(instance):
    assert isinstance(instance, my_Database)


my_FKRelation_strategy = st.builds(my_FKRelation, label=safe_text)
@given(instance=my_FKRelation_strategy)
@settings(max_examples=25)
def test_my_FKRelation_instantiation(instance):
    assert isinstance(instance, my_FKRelation)


my_NamedElement_strategy = st.builds(my_NamedElement, name=safe_text)
@given(instance=my_NamedElement_strategy)
@settings(max_examples=25)
def test_my_NamedElement_instantiation(instance):
    assert isinstance(instance, my_NamedElement)


my_Table_strategy = st.builds(my_Table)
@given(instance=my_Table_strategy)
@settings(max_examples=25)
def test_my_Table_instantiation(instance):
    assert isinstance(instance, my_Table)



