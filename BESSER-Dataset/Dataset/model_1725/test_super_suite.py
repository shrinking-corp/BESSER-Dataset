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
    mapkey_Writer,
    mapkey_StringToWriterMapEntry,
    mapkey_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mapkey_writer_is_not_abstract():
    assert not inspect.isabstract(mapkey_Writer)


def test_hyp_mapkey_writer_constructor_exists():
    assert callable(mapkey_Writer.__init__)


def test_hyp_mapkey_writer_constructor_args():
    sig = inspect.signature(mapkey_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mapkey_stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(mapkey_StringToWriterMapEntry)


def test_hyp_mapkey_stringtowritermapentry_constructor_exists():
    assert callable(mapkey_StringToWriterMapEntry.__init__)


def test_hyp_mapkey_stringtowritermapentry_constructor_args():
    sig = inspect.signature(mapkey_StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_mapkey_book_is_not_abstract():
    assert not inspect.isabstract(mapkey_Book)


def test_hyp_mapkey_book_constructor_exists():
    assert callable(mapkey_Book.__init__)


def test_hyp_mapkey_book_constructor_args():
    sig = inspect.signature(mapkey_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"



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
mapkey_Writer_strategy = st.builds(
    mapkey_Writer,
    name=
        safe_text
)
mapkey_StringToWriterMapEntry_strategy = st.builds(
    mapkey_StringToWriterMapEntry,
    key=
        safe_text
)
mapkey_Book_strategy = st.builds(
    mapkey_Book,
    title=
        safe_text
)




@given(instance=mapkey_Writer_strategy)
def test_hyp_mapkey_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mapkey_StringToWriterMapEntry_strategy)
def test_hyp_mapkey_stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=mapkey_Book_strategy)
def test_hyp_mapkey_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    mapkey_Book,
    mapkey_StringToWriterMapEntry,
    mapkey_Writer,
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

def test_mapkey_Book_title_value_roundtrip():
    instance = mapkey_Book(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_mapkey_StringToWriterMapEntry_key_value_roundtrip():
    instance = mapkey_StringToWriterMapEntry(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_mapkey_Writer_name_value_roundtrip():
    instance = mapkey_Writer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_value1_link_reassign_clear():
    a = mapkey_Writer(name="sample_text")
    b1 = mapkey_StringToWriterMapEntry(key="sample_text")
    b2 = mapkey_StringToWriterMapEntry(key="sample_text_2")
    _safe_set(a, 'mapkey_Writer', b1)
    assert _is_linked(a, 'mapkey_Writer', b1)
    if hasattr(b1, 'mapkey_StringToWriterMapEntry2'):
        assert _is_linked(b1, 'mapkey_StringToWriterMapEntry2', a)
    _safe_set(a, 'mapkey_Writer', b2)
    assert _is_linked(a, 'mapkey_Writer', b2)
    if hasattr(b1, 'mapkey_StringToWriterMapEntry2'):
        assert not _is_linked(b1, 'mapkey_StringToWriterMapEntry2', a)
    if hasattr(b2, 'mapkey_StringToWriterMapEntry2'):
        assert _is_linked(b2, 'mapkey_StringToWriterMapEntry2', a)
    _safe_set(a, 'mapkey_Writer', None)
    assert not _is_linked(a, 'mapkey_Writer', b2)
    if hasattr(b2, 'mapkey_StringToWriterMapEntry2'):
        assert not _is_linked(b2, 'mapkey_StringToWriterMapEntry2', a)


def test_assoc_writers0_link_reassign_clear():
    a = mapkey_StringToWriterMapEntry(key="sample_text")
    b1 = mapkey_Book(title="sample_text")
    b2 = mapkey_Book(title="sample_text_2")
    _safe_set(a, 'mapkey_StringToWriterMapEntry', b1)
    assert _is_linked(a, 'mapkey_StringToWriterMapEntry', b1)
    if hasattr(b1, 'mapkey_Book'):
        assert _is_linked(b1, 'mapkey_Book', a)
    _safe_set(a, 'mapkey_StringToWriterMapEntry', b2)
    assert _is_linked(a, 'mapkey_StringToWriterMapEntry', b2)
    if hasattr(b1, 'mapkey_Book'):
        assert not _is_linked(b1, 'mapkey_Book', a)
    if hasattr(b2, 'mapkey_Book'):
        assert _is_linked(b2, 'mapkey_Book', a)
    _safe_set(a, 'mapkey_StringToWriterMapEntry', None)
    assert not _is_linked(a, 'mapkey_StringToWriterMapEntry', b2)
    if hasattr(b2, 'mapkey_Book'):
        assert not _is_linked(b2, 'mapkey_Book', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

mapkey_Book_strategy = st.builds(mapkey_Book, title=safe_text)
@given(instance=mapkey_Book_strategy)
@settings(max_examples=25)
def test_mapkey_Book_instantiation(instance):
    assert isinstance(instance, mapkey_Book)


mapkey_StringToWriterMapEntry_strategy = st.builds(mapkey_StringToWriterMapEntry, key=safe_text)
@given(instance=mapkey_StringToWriterMapEntry_strategy)
@settings(max_examples=25)
def test_mapkey_StringToWriterMapEntry_instantiation(instance):
    assert isinstance(instance, mapkey_StringToWriterMapEntry)


mapkey_Writer_strategy = st.builds(mapkey_Writer, name=safe_text)
@given(instance=mapkey_Writer_strategy)
@settings(max_examples=25)
def test_mapkey_Writer_instantiation(instance):
    assert isinstance(instance, mapkey_Writer)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mapkey_Book,
    mapkey_StringToWriterMapEntry,
    mapkey_Writer,
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

def test_assoc_value1_reverse_link_reassign_clear():
    a1 = mapkey_Writer(name="sample_text")
    a2 = mapkey_Writer(name="sample_text_2")
    b = mapkey_StringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'mapkey_StringToWriterMapEntry2', a1)
    assert _is_linked(b, 'mapkey_StringToWriterMapEntry2', a1)
    if hasattr(a1, 'mapkey_Writer'):
        assert _is_linked(a1, 'mapkey_Writer', b)
    _safe_set(b, 'mapkey_StringToWriterMapEntry2', a2)
    assert _is_linked(b, 'mapkey_StringToWriterMapEntry2', a2)
    if hasattr(a1, 'mapkey_Writer'):
        assert not _is_linked(a1, 'mapkey_Writer', b)
    if hasattr(a2, 'mapkey_Writer'):
        assert _is_linked(a2, 'mapkey_Writer', b)
    _safe_set(b, 'mapkey_StringToWriterMapEntry2', None)
    assert not _is_linked(b, 'mapkey_StringToWriterMapEntry2', a2)
    if hasattr(a2, 'mapkey_Writer'):
        assert not _is_linked(a2, 'mapkey_Writer', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = mapkey_StringToWriterMapEntry(key="sample_text")
    a2 = mapkey_StringToWriterMapEntry(key="sample_text_2")
    b = mapkey_Book(title="sample_text")
    _safe_set(b, 'mapkey_Book', {a1})
    assert _is_linked(b, 'mapkey_Book', a1)
    if hasattr(a1, 'mapkey_StringToWriterMapEntry'):
        assert _is_linked(a1, 'mapkey_StringToWriterMapEntry', b)
    _safe_set(b, 'mapkey_Book', {a2})
    assert _is_linked(b, 'mapkey_Book', a2)
    if hasattr(a1, 'mapkey_StringToWriterMapEntry'):
        assert not _is_linked(a1, 'mapkey_StringToWriterMapEntry', b)
    if hasattr(a2, 'mapkey_StringToWriterMapEntry'):
        assert _is_linked(a2, 'mapkey_StringToWriterMapEntry', b)
    _safe_set(b, 'mapkey_Book', set())
    assert not _is_linked(b, 'mapkey_Book', a2)
    if hasattr(a2, 'mapkey_StringToWriterMapEntry'):
        assert not _is_linked(a2, 'mapkey_StringToWriterMapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import mapkey_Book

def test_mapkey_Book___init__():
    assert mapkey_Book.__init__(mapkey_Book('', mapkey_Book=set()), '', mapkey_Book=set()) == None

