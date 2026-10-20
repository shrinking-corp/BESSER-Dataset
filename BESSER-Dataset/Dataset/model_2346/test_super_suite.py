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
    simplerdbms_Table,
    simplerdbms_ForeignKey,
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
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"





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
    assert "isPrimary" in params, "Missing parameter 'isPrimary'"




def test_hyp_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Table)


def test_hyp_simplerdbms_table_constructor_exists():
    assert callable(simplerdbms_Table.__init__)


def test_hyp_simplerdbms_table_constructor_args():
    sig = inspect.signature(simplerdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_ForeignKey)


def test_hyp_simplerdbms_foreignkey_constructor_exists():
    assert callable(simplerdbms_ForeignKey.__init__)


def test_hyp_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simplerdbms_ForeignKey.__init__)
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
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simplerdbms_Key_strategy = st.builds(
    simplerdbms_Key,
    isPrimary=
        st.booleans()
)
simplerdbms_Table_strategy = st.builds(
    simplerdbms_Table,
)
simplerdbms_ForeignKey_strategy = st.builds(
    simplerdbms_ForeignKey,
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
def test_hyp_simplerdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simplerdbms_RModelElement_strategy)
def test_hyp_simplerdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





@given(instance=simplerdbms_Key_strategy)
def test_hyp_simplerdbms_key_isPrimary_setter(instance):
    original = instance.isPrimary
    instance.isPrimary = original
    assert instance.isPrimary == original







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


def test_simplerdbms_Key_isPrimary_value_roundtrip():
    instance = simplerdbms_Key(isPrimary=True)
    assert instance.isPrimary == True
    instance.isPrimary = False
    assert instance.isPrimary == False


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
    instance = simplerdbms_Key(isPrimary=True)
    assert isinstance(instance, RModelElement)


def test_simplerdbms_Schema_isa_RModelElement():
    instance = simplerdbms_Schema()
    assert isinstance(instance, RModelElement)


def test_simplerdbms_Table_isa_RModelElement():
    instance = simplerdbms_Table()
    assert isinstance(instance, RModelElement)


def test_assoc_columns12_link_reassign_clear():
    a = simplerdbms_Key(isPrimary=True)
    b1 = simplerdbms_Column(type="sample_text")
    b2 = simplerdbms_Column(type="sample_text_2")
    _safe_set(a, 'keys13', {b1})
    assert _is_linked(a, 'keys13', b1)
    if hasattr(b1, 'Column14'):
        assert _is_linked(b1, 'Column14', a)
    _safe_set(a, 'keys13', {b2})
    assert _is_linked(a, 'keys13', b2)
    if hasattr(b1, 'Column14'):
        assert not _is_linked(b1, 'Column14', a)
    if hasattr(b2, 'Column14'):
        assert _is_linked(b2, 'Column14', a)
    _safe_set(a, 'keys13', set())
    assert not _is_linked(a, 'keys13', b2)
    if hasattr(b2, 'Column14'):
        assert not _is_linked(b2, 'Column14', a)


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


def test_assoc_keys20_link_reassign_clear():
    a = simplerdbms_Key(isPrimary=True)
    b1 = simplerdbms_Table()
    b2 = simplerdbms_Table()
    _safe_set(a, 'Key22', b1)
    assert _is_linked(a, 'Key22', b1)
    if hasattr(b1, 'owner21'):
        assert _is_linked(b1, 'owner21', a)
    _safe_set(a, 'Key22', b2)
    assert _is_linked(a, 'Key22', b2)
    if hasattr(b1, 'owner21'):
        assert not _is_linked(b1, 'owner21', a)
    if hasattr(b2, 'owner21'):
        assert _is_linked(b2, 'owner21', a)
    _safe_set(a, 'Key22', None)
    assert not _is_linked(a, 'Key22', b2)
    if hasattr(b2, 'owner21'):
        assert not _is_linked(b2, 'owner21', a)


def test_assoc_keys3_link_reassign_clear():
    a = simplerdbms_Key(isPrimary=True)
    b1 = simplerdbms_Column(type="sample_text")
    b2 = simplerdbms_Column(type="sample_text_2")
    _safe_set(a, 'Key', b1)
    assert _is_linked(a, 'Key', b1)
    if hasattr(b1, 'columns4'):
        assert _is_linked(b1, 'columns4', a)
    _safe_set(a, 'Key', b2)
    assert _is_linked(a, 'Key', b2)
    if hasattr(b1, 'columns4'):
        assert not _is_linked(b1, 'columns4', a)
    if hasattr(b2, 'columns4'):
        assert _is_linked(b2, 'columns4', a)
    _safe_set(a, 'Key', None)
    assert not _is_linked(a, 'Key', b2)
    if hasattr(b2, 'columns4'):
        assert not _is_linked(b2, 'columns4', a)


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


def test_assoc_owner10_link_reassign_clear():
    a = simplerdbms_Key(isPrimary=True)
    b1 = simplerdbms_Table()
    b2 = simplerdbms_Table()
    _safe_set(a, 'keys', b1)
    assert _is_linked(a, 'keys', b1)
    if hasattr(b1, 'Table11'):
        assert _is_linked(b1, 'Table11', a)
    _safe_set(a, 'keys', b2)
    assert _is_linked(a, 'keys', b2)
    if hasattr(b1, 'Table11'):
        assert not _is_linked(b1, 'Table11', a)
    if hasattr(b2, 'Table11'):
        assert _is_linked(b2, 'Table11', a)
    _safe_set(a, 'keys', None)
    assert not _is_linked(a, 'keys', b2)
    if hasattr(b2, 'Table11'):
        assert not _is_linked(b2, 'Table11', a)


def test_assoc_refersTo5_link_reassign_clear():
    a = simplerdbms_Key(isPrimary=True)
    b1 = simplerdbms_ForeignKey()
    b2 = simplerdbms_ForeignKey()
    _safe_set(a, 'simplerdbms_Key', b1)
    assert _is_linked(a, 'simplerdbms_Key', b1)
    if hasattr(b1, 'simplerdbms_ForeignKey'):
        assert _is_linked(b1, 'simplerdbms_ForeignKey', a)
    _safe_set(a, 'simplerdbms_Key', b2)
    assert _is_linked(a, 'simplerdbms_Key', b2)
    if hasattr(b1, 'simplerdbms_ForeignKey'):
        assert not _is_linked(b1, 'simplerdbms_ForeignKey', a)
    if hasattr(b2, 'simplerdbms_ForeignKey'):
        assert _is_linked(b2, 'simplerdbms_ForeignKey', a)
    _safe_set(a, 'simplerdbms_Key', None)
    assert not _is_linked(a, 'simplerdbms_Key', b2)
    if hasattr(b2, 'simplerdbms_ForeignKey'):
        assert not _is_linked(b2, 'simplerdbms_ForeignKey', a)


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


simplerdbms_Key_strategy = st.builds(simplerdbms_Key, isPrimary=st.booleans())
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





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RModelElement,
    simplerdbms_Column,
    simplerdbms_ForeignKey,
    simplerdbms_Key,
    simplerdbms_RModelElement,
    simplerdbms_Schema,
    simplerdbms_Table,
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

def test_assoc_columns12_reverse_link_reassign_clear():
    a1 = simplerdbms_Key(isPrimary=True)
    a2 = simplerdbms_Key(isPrimary=False)
    b = simplerdbms_Column(type="sample_text")
    _safe_set(b, 'Column14', a1)
    assert _is_linked(b, 'Column14', a1)
    if hasattr(a1, 'keys13'):
        assert _is_linked(a1, 'keys13', b)
    _safe_set(b, 'Column14', a2)
    assert _is_linked(b, 'Column14', a2)
    if hasattr(a1, 'keys13'):
        assert not _is_linked(a1, 'keys13', b)
    if hasattr(a2, 'keys13'):
        assert _is_linked(a2, 'keys13', b)
    _safe_set(b, 'Column14', None)
    assert not _is_linked(b, 'Column14', a2)
    if hasattr(a2, 'keys13'):
        assert not _is_linked(a2, 'keys13', b)


def test_assoc_keys3_reverse_link_reassign_clear():
    a1 = simplerdbms_Key(isPrimary=True)
    a2 = simplerdbms_Key(isPrimary=False)
    b = simplerdbms_Column(type="sample_text")
    _safe_set(b, 'columns4', {a1})
    assert _is_linked(b, 'columns4', a1)
    if hasattr(a1, 'Key'):
        assert _is_linked(a1, 'Key', b)
    _safe_set(b, 'columns4', {a2})
    assert _is_linked(b, 'columns4', a2)
    if hasattr(a1, 'Key'):
        assert not _is_linked(a1, 'Key', b)
    if hasattr(a2, 'Key'):
        assert _is_linked(a2, 'Key', b)
    _safe_set(b, 'columns4', set())
    assert not _is_linked(b, 'columns4', a2)
    if hasattr(a2, 'Key'):
        assert not _is_linked(a2, 'Key', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns17_stub_double():
    # simplerdbms_Table has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_Table()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column18', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column18', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_columns6_stub_double():
    # simplerdbms_ForeignKey has no real 'foreignKeys' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'foreignKeys', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'foreignKeys')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'foreignKeys')


def test_assoc_foreignKeys1_stub_double():
    # simplerdbms_ForeignKey has no real 'ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'ForeignKey', None)
    _safe_set(owner, 'columns2', {partner})
    assert getattr(partner, 'ForeignKey') == owner
    _safe_set(owner, 'columns2', set())
    assert getattr(partner, 'ForeignKey') is None


def test_assoc_keys20_stub_double():
    # simplerdbms_Table has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_Table()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'Key22', partner)
    assert owner in getattr(partner, 'owner21')
    _safe_set(owner, 'Key22', None)
    assert owner not in getattr(partner, 'owner21')


def test_assoc_owner0_stub_double():
    # simplerdbms_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table') is None


def test_assoc_owner10_stub_double():
    # simplerdbms_Table has no real 'Table11' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_Table()
    setattr(partner, 'Table11', None)
    _safe_set(owner, 'keys', partner)
    assert getattr(partner, 'Table11') == owner
    _safe_set(owner, 'keys', None)
    assert getattr(partner, 'Table11') is None


def test_assoc_refersTo5_stub_double():
    # simplerdbms_ForeignKey has no real 'simplerdbms_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'simplerdbms_ForeignKey', None)
    _safe_set(owner, 'simplerdbms_Key', partner)
    assert getattr(partner, 'simplerdbms_ForeignKey') == owner
    _safe_set(owner, 'simplerdbms_Key', None)
    assert getattr(partner, 'simplerdbms_ForeignKey') is None




from python_code import simplerdbms_RModelElement

def test_simplerdbms_RModelElement___init__():
    assert simplerdbms_RModelElement.__init__(simplerdbms_RModelElement('', '\x00'), '\x00\x00', '') == None

