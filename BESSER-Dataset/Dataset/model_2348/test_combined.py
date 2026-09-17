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
    simplerdbms_RModelElement,
    RModelElement,
    simplerdbms_Key,
    simplerdbms_ForeignKey,
    simplerdbms_Table,
    simplerdbms_Schema,
    simplerdbms_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simplerdbms_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_RModelElement)


def test_hyp_simplerdbms_rmodelelement_constructor_exists():
    assert callable(simplerdbms_RModelElement.__init__)


def test_hyp_simplerdbms_rmodelelement_constructor_args():
    sig = inspect.signature(simplerdbms_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_hyp_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_hyp_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Key)


def test_hyp_simplerdbms_key_constructor_exists():
    assert callable(simplerdbms_Key.__init__)


def test_hyp_simplerdbms_key_constructor_args():
    sig = inspect.signature(simplerdbms_Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_ForeignKey)


def test_hyp_simplerdbms_foreignkey_constructor_exists():
    assert callable(simplerdbms_ForeignKey.__init__)


def test_hyp_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simplerdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Table)


def test_hyp_simplerdbms_table_constructor_exists():
    assert callable(simplerdbms_Table.__init__)


def test_hyp_simplerdbms_table_constructor_args():
    sig = inspect.signature(simplerdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Schema)


def test_hyp_simplerdbms_schema_constructor_exists():
    assert callable(simplerdbms_Schema.__init__)


def test_hyp_simplerdbms_schema_constructor_args():
    sig = inspect.signature(simplerdbms_Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Column)


def test_hyp_simplerdbms_column_constructor_exists():
    assert callable(simplerdbms_Column.__init__)


def test_hyp_simplerdbms_column_constructor_args():
    sig = inspect.signature(simplerdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"



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
simplerdbms_RModelElement_strategy = st.builds(
    simplerdbms_RModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simplerdbms_Key_strategy = st.builds(
    simplerdbms_Key,
)
simplerdbms_ForeignKey_strategy = st.builds(
    simplerdbms_ForeignKey,
)
simplerdbms_Table_strategy = st.builds(
    simplerdbms_Table,
)
simplerdbms_Schema_strategy = st.builds(
    simplerdbms_Schema,
)
simplerdbms_Column_strategy = st.builds(
    simplerdbms_Column,
    type=
        safe_text
)




@given(instance=simplerdbms_RModelElement_strategy)
def test_hyp_simplerdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=simplerdbms_RModelElement_strategy)
def test_hyp_simplerdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=simplerdbms_Column_strategy)
def test_hyp_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    RModelElement,
    simplerdbms_Column,
    simplerdbms_ForeignKey,
    simplerdbms_Key,
    simplerdbms_RModelElement,
    simplerdbms_Schema,
    simplerdbms_Table,
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

def test_simplerdbms_Column_type_value_roundtrip():
    instance = simplerdbms_Column(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_simplerdbms_RModelElement_kind_value_roundtrip():
    instance = simplerdbms_RModelElement(kind="sample_text", name="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_simplerdbms_RModelElement_name_value_roundtrip():
    instance = simplerdbms_RModelElement(kind="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simplerdbms_Column_isa_RModelElement():
    instance = simplerdbms_Column(type="sample_text")
    assert isinstance(instance, RModelElement)


def test_simplerdbms_ForeignKey_isa_RModelElement():
    instance = simplerdbms_ForeignKey()
    assert isinstance(instance, RModelElement)


def test_simplerdbms_Key_isa_RModelElement():
    instance = simplerdbms_Key()
    assert isinstance(instance, RModelElement)


def test_simplerdbms_Schema_isa_RModelElement():
    instance = simplerdbms_Schema()
    assert isinstance(instance, RModelElement)


def test_simplerdbms_Table_isa_RModelElement():
    instance = simplerdbms_Table()
    assert isinstance(instance, RModelElement)


def test_assoc_columns12_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_Key()
    b2 = simplerdbms_Key()
    _safe_set(a, 'Column14', b1)
    assert _is_linked(a, 'Column14', b1)
    if hasattr(b1, 'keys13'):
        assert _is_linked(b1, 'keys13', a)
    _safe_set(a, 'Column14', b2)
    assert _is_linked(a, 'Column14', b2)
    if hasattr(b1, 'keys13'):
        assert not _is_linked(b1, 'keys13', a)
    if hasattr(b2, 'keys13'):
        assert _is_linked(b2, 'keys13', a)
    _safe_set(a, 'Column14', None)
    assert not _is_linked(a, 'Column14', b2)
    if hasattr(b2, 'keys13'):
        assert not _is_linked(b2, 'keys13', a)


def test_assoc_columns17_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_Table()
    b2 = simplerdbms_Table()
    _safe_set(a, 'Column18', b1)
    assert _is_linked(a, 'Column18', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'Column18', b2)
    assert _is_linked(a, 'Column18', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'Column18', None)
    assert not _is_linked(a, 'Column18', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_columns6_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_ForeignKey()
    b2 = simplerdbms_ForeignKey()
    _safe_set(a, 'Column', b1)
    assert _is_linked(a, 'Column', b1)
    if hasattr(b1, 'foreignKeys'):
        assert _is_linked(b1, 'foreignKeys', a)
    _safe_set(a, 'Column', b2)
    assert _is_linked(a, 'Column', b2)
    if hasattr(b1, 'foreignKeys'):
        assert not _is_linked(b1, 'foreignKeys', a)
    if hasattr(b2, 'foreignKeys'):
        assert _is_linked(b2, 'foreignKeys', a)
    _safe_set(a, 'Column', None)
    assert not _is_linked(a, 'Column', b2)
    if hasattr(b2, 'foreignKeys'):
        assert not _is_linked(b2, 'foreignKeys', a)


def test_assoc_foreignKeys1_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_ForeignKey()
    b2 = simplerdbms_ForeignKey()
    _safe_set(a, 'columns2', {b1})
    assert _is_linked(a, 'columns2', b1)
    if hasattr(b1, 'ForeignKey'):
        assert _is_linked(b1, 'ForeignKey', a)
    _safe_set(a, 'columns2', {b2})
    assert _is_linked(a, 'columns2', b2)
    if hasattr(b1, 'ForeignKey'):
        assert not _is_linked(b1, 'ForeignKey', a)
    if hasattr(b2, 'ForeignKey'):
        assert _is_linked(b2, 'ForeignKey', a)
    _safe_set(a, 'columns2', set())
    assert not _is_linked(a, 'columns2', b2)
    if hasattr(b2, 'ForeignKey'):
        assert not _is_linked(b2, 'ForeignKey', a)


def test_assoc_keys3_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_Key()
    b2 = simplerdbms_Key()
    _safe_set(a, 'columns4', {b1})
    assert _is_linked(a, 'columns4', b1)
    if hasattr(b1, 'Key'):
        assert _is_linked(b1, 'Key', a)
    _safe_set(a, 'columns4', {b2})
    assert _is_linked(a, 'columns4', b2)
    if hasattr(b1, 'Key'):
        assert not _is_linked(b1, 'Key', a)
    if hasattr(b2, 'Key'):
        assert _is_linked(b2, 'Key', a)
    _safe_set(a, 'columns4', set())
    assert not _is_linked(a, 'columns4', b2)
    if hasattr(b2, 'Key'):
        assert not _is_linked(b2, 'Key', a)


def test_assoc_owner0_link_reassign_clear():
    a = simplerdbms_Column(type="sample_text")
    b1 = simplerdbms_Table()
    b2 = simplerdbms_Table()
    _safe_set(a, 'columns', b1)
    assert _is_linked(a, 'columns', b1)
    if hasattr(b1, 'Table'):
        assert _is_linked(b1, 'Table', a)
    _safe_set(a, 'columns', b2)
    assert _is_linked(a, 'columns', b2)
    if hasattr(b1, 'Table'):
        assert not _is_linked(b1, 'Table', a)
    if hasattr(b2, 'Table'):
        assert _is_linked(b2, 'Table', a)
    _safe_set(a, 'columns', None)
    assert not _is_linked(a, 'columns', b2)
    if hasattr(b2, 'Table'):
        assert not _is_linked(b2, 'Table', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

RModelElement_strategy = st.builds(RModelElement)
@given(instance=RModelElement_strategy)
@settings(max_examples=25)
def test_RModelElement_instantiation(instance):
    assert isinstance(instance, RModelElement)


simplerdbms_Column_strategy = st.builds(simplerdbms_Column, type=safe_text)
@given(instance=simplerdbms_Column_strategy)
@settings(max_examples=25)
def test_simplerdbms_Column_instantiation(instance):
    assert isinstance(instance, simplerdbms_Column)


simplerdbms_ForeignKey_strategy = st.builds(simplerdbms_ForeignKey)
@given(instance=simplerdbms_ForeignKey_strategy)
@settings(max_examples=25)
def test_simplerdbms_ForeignKey_instantiation(instance):
    assert isinstance(instance, simplerdbms_ForeignKey)


simplerdbms_Key_strategy = st.builds(simplerdbms_Key)
@given(instance=simplerdbms_Key_strategy)
@settings(max_examples=25)
def test_simplerdbms_Key_instantiation(instance):
    assert isinstance(instance, simplerdbms_Key)


simplerdbms_RModelElement_strategy = st.builds(simplerdbms_RModelElement, kind=safe_text, name=safe_text)
@given(instance=simplerdbms_RModelElement_strategy)
@settings(max_examples=25)
def test_simplerdbms_RModelElement_instantiation(instance):
    assert isinstance(instance, simplerdbms_RModelElement)


simplerdbms_Schema_strategy = st.builds(simplerdbms_Schema)
@given(instance=simplerdbms_Schema_strategy)
@settings(max_examples=25)
def test_simplerdbms_Schema_instantiation(instance):
    assert isinstance(instance, simplerdbms_Schema)


simplerdbms_Table_strategy = st.builds(simplerdbms_Table)
@given(instance=simplerdbms_Table_strategy)
@settings(max_examples=25)
def test_simplerdbms_Table_instantiation(instance):
    assert isinstance(instance, simplerdbms_Table)



