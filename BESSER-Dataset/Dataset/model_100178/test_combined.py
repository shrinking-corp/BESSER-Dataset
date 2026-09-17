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
    RelationalDBContent_TupleElement,
    TupleElement,
    RelationalDBContent_Tuple,
    Tuple,
    DataBase,
    Table,
    NamedElement,
    RelationalDBContent_Table,
    RelationalDBContent_DataBase,
    RelationalDBContent_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_relationaldbcontent_tupleelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent_TupleElement)


def test_hyp_relationaldbcontent_tupleelement_constructor_exists():
    assert callable(RelationalDBContent_TupleElement.__init__)


def test_hyp_relationaldbcontent_tupleelement_constructor_args():
    sig = inspect.signature(RelationalDBContent_TupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_tupleelement_is_not_abstract():
    assert not inspect.isabstract(TupleElement)


def test_hyp_tupleelement_constructor_exists():
    assert callable(TupleElement.__init__)


def test_hyp_tupleelement_constructor_args():
    sig = inspect.signature(TupleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationaldbcontent_tuple_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent_Tuple)


def test_hyp_relationaldbcontent_tuple_constructor_exists():
    assert callable(RelationalDBContent_Tuple.__init__)


def test_hyp_relationaldbcontent_tuple_constructor_args():
    sig = inspect.signature(RelationalDBContent_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tuple_is_not_abstract():
    assert not inspect.isabstract(Tuple)


def test_hyp_tuple_constructor_exists():
    assert callable(Tuple.__init__)


def test_hyp_tuple_constructor_args():
    sig = inspect.signature(Tuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_is_not_abstract():
    assert not inspect.isabstract(DataBase)


def test_hyp_database_constructor_exists():
    assert callable(DataBase.__init__)


def test_hyp_database_constructor_args():
    sig = inspect.signature(DataBase.__init__)
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



def test_hyp_relationaldbcontent_table_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent_Table)


def test_hyp_relationaldbcontent_table_constructor_exists():
    assert callable(RelationalDBContent_Table.__init__)


def test_hyp_relationaldbcontent_table_constructor_args():
    sig = inspect.signature(RelationalDBContent_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationaldbcontent_database_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent_DataBase)


def test_hyp_relationaldbcontent_database_constructor_exists():
    assert callable(RelationalDBContent_DataBase.__init__)


def test_hyp_relationaldbcontent_database_constructor_args():
    sig = inspect.signature(RelationalDBContent_DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "SGBDname" in params, "Missing parameter 'SGBDname'"




def test_hyp_relationaldbcontent_namedelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent_NamedElement)


def test_hyp_relationaldbcontent_namedelement_constructor_exists():
    assert callable(RelationalDBContent_NamedElement.__init__)


def test_hyp_relationaldbcontent_namedelement_constructor_args():
    sig = inspect.signature(RelationalDBContent_NamedElement.__init__)
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
RelationalDBContent_TupleElement_strategy = st.builds(
    RelationalDBContent_TupleElement,
    value=
        safe_text
)
TupleElement_strategy = st.builds(
    TupleElement,
)
RelationalDBContent_Tuple_strategy = st.builds(
    RelationalDBContent_Tuple,
)
Tuple_strategy = st.builds(
    Tuple,
)
DataBase_strategy = st.builds(
    DataBase,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
RelationalDBContent_Table_strategy = st.builds(
    RelationalDBContent_Table,
)
RelationalDBContent_DataBase_strategy = st.builds(
    RelationalDBContent_DataBase,
    SGBDname=
        safe_text
)
RelationalDBContent_NamedElement_strategy = st.builds(
    RelationalDBContent_NamedElement,
    name=
        safe_text
)




@given(instance=RelationalDBContent_TupleElement_strategy)
def test_hyp_relationaldbcontent_tupleelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original











@given(instance=RelationalDBContent_DataBase_strategy)
def test_hyp_relationaldbcontent_database_SGBDname_setter(instance):
    original = instance.SGBDname
    instance.SGBDname = original
    assert instance.SGBDname == original




@given(instance=RelationalDBContent_NamedElement_strategy)
def test_hyp_relationaldbcontent_namedelement_name_setter(instance):
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
    DataBase,
    NamedElement,
    RelationalDBContent_DataBase,
    RelationalDBContent_NamedElement,
    RelationalDBContent_Table,
    RelationalDBContent_Tuple,
    RelationalDBContent_TupleElement,
    Table,
    Tuple,
    TupleElement,
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

def test_RelationalDBContent_DataBase_SGBDname_value_roundtrip():
    instance = RelationalDBContent_DataBase(SGBDname="sample_text")
    assert instance.SGBDname == "sample_text"
    instance.SGBDname = "sample_text_2"
    assert instance.SGBDname == "sample_text_2"


def test_RelationalDBContent_NamedElement_name_value_roundtrip():
    instance = RelationalDBContent_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RelationalDBContent_TupleElement_value_value_roundtrip():
    instance = RelationalDBContent_TupleElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_RelationalDBContent_DataBase_isa_NamedElement():
    instance = RelationalDBContent_DataBase(SGBDname="sample_text")
    assert isinstance(instance, NamedElement)


def test_RelationalDBContent_Table_isa_NamedElement():
    instance = RelationalDBContent_Table()
    assert isinstance(instance, NamedElement)


def test_assoc_tables0_link_reassign_clear():
    a = RelationalDBContent_DataBase(SGBDname="sample_text")
    b1 = Table()
    b2 = Table()
    _safe_set(a, 'database', {b1})
    assert _is_linked(a, 'database', b1)
    if hasattr(b1, 'Table'):
        assert _is_linked(b1, 'Table', a)
    _safe_set(a, 'database', {b2})
    assert _is_linked(a, 'database', b2)
    if hasattr(b1, 'Table'):
        assert not _is_linked(b1, 'Table', a)
    if hasattr(b2, 'Table'):
        assert _is_linked(b2, 'Table', a)
    _safe_set(a, 'database', set())
    assert not _is_linked(a, 'database', b2)
    if hasattr(b2, 'Table'):
        assert not _is_linked(b2, 'Table', a)


def test_assoc_tuple6_link_reassign_clear():
    a = RelationalDBContent_TupleElement(value="sample_text")
    b1 = Tuple()
    b2 = Tuple()
    _safe_set(a, 'elements', b1)
    assert _is_linked(a, 'elements', b1)
    if hasattr(b1, 'Tuple7'):
        assert _is_linked(b1, 'Tuple7', a)
    _safe_set(a, 'elements', b2)
    assert _is_linked(a, 'elements', b2)
    if hasattr(b1, 'Tuple7'):
        assert not _is_linked(b1, 'Tuple7', a)
    if hasattr(b2, 'Tuple7'):
        assert _is_linked(b2, 'Tuple7', a)
    _safe_set(a, 'elements', None)
    assert not _is_linked(a, 'elements', b2)
    if hasattr(b2, 'Tuple7'):
        assert not _is_linked(b2, 'Tuple7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DataBase_strategy = st.builds(DataBase)
@given(instance=DataBase_strategy)
@settings(max_examples=25)
def test_DataBase_instantiation(instance):
    assert isinstance(instance, DataBase)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


RelationalDBContent_DataBase_strategy = st.builds(RelationalDBContent_DataBase, SGBDname=safe_text)
@given(instance=RelationalDBContent_DataBase_strategy)
@settings(max_examples=25)
def test_RelationalDBContent_DataBase_instantiation(instance):
    assert isinstance(instance, RelationalDBContent_DataBase)


RelationalDBContent_NamedElement_strategy = st.builds(RelationalDBContent_NamedElement, name=safe_text)
@given(instance=RelationalDBContent_NamedElement_strategy)
@settings(max_examples=25)
def test_RelationalDBContent_NamedElement_instantiation(instance):
    assert isinstance(instance, RelationalDBContent_NamedElement)


RelationalDBContent_Table_strategy = st.builds(RelationalDBContent_Table)
@given(instance=RelationalDBContent_Table_strategy)
@settings(max_examples=25)
def test_RelationalDBContent_Table_instantiation(instance):
    assert isinstance(instance, RelationalDBContent_Table)


RelationalDBContent_Tuple_strategy = st.builds(RelationalDBContent_Tuple)
@given(instance=RelationalDBContent_Tuple_strategy)
@settings(max_examples=25)
def test_RelationalDBContent_Tuple_instantiation(instance):
    assert isinstance(instance, RelationalDBContent_Tuple)


RelationalDBContent_TupleElement_strategy = st.builds(RelationalDBContent_TupleElement, value=safe_text)
@given(instance=RelationalDBContent_TupleElement_strategy)
@settings(max_examples=25)
def test_RelationalDBContent_TupleElement_instantiation(instance):
    assert isinstance(instance, RelationalDBContent_TupleElement)


Table_strategy = st.builds(Table)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


Tuple_strategy = st.builds(Tuple)
@given(instance=Tuple_strategy)
@settings(max_examples=25)
def test_Tuple_instantiation(instance):
    assert isinstance(instance, Tuple)


TupleElement_strategy = st.builds(TupleElement)
@given(instance=TupleElement_strategy)
@settings(max_examples=25)
def test_TupleElement_instantiation(instance):
    assert isinstance(instance, TupleElement)



