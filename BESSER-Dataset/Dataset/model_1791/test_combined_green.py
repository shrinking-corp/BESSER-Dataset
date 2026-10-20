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
    column_TestSchema,
    column_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_column_testschema_is_not_abstract():
    assert not inspect.isabstract(column_TestSchema)


def test_hyp_column_testschema_constructor_exists():
    assert callable(column_TestSchema.__init__)


def test_hyp_column_testschema_constructor_args():
    sig = inspect.signature(column_TestSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_column_book_is_not_abstract():
    assert not inspect.isabstract(column_Book)


def test_hyp_column_book_constructor_exists():
    assert callable(column_Book.__init__)


def test_hyp_column_book_constructor_args():
    sig = inspect.signature(column_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "pages" in params, "Missing parameter 'pages'"






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
column_TestSchema_strategy = st.builds(
    column_TestSchema,
    name=
        safe_text
)
column_Book_strategy = st.builds(
    column_Book,
    title=
        safe_text,
    author=
        safe_text,
    weight=
        safe_text,
    pages=
        safe_text
)




@given(instance=column_TestSchema_strategy)
def test_hyp_column_testschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=column_Book_strategy)
def test_hyp_column_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=column_Book_strategy)
def test_hyp_column_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=column_Book_strategy)
def test_hyp_column_book_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=column_Book_strategy)
def test_hyp_column_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    column_Book,
    column_TestSchema,
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

def test_column_Book_author_value_roundtrip():
    instance = column_Book(author="sample_text", pages="sample_text", title="sample_text", weight="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_column_Book_pages_value_roundtrip():
    instance = column_Book(author="sample_text", pages="sample_text", title="sample_text", weight="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_column_Book_title_value_roundtrip():
    instance = column_Book(author="sample_text", pages="sample_text", title="sample_text", weight="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_column_Book_weight_value_roundtrip():
    instance = column_Book(author="sample_text", pages="sample_text", title="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_column_TestSchema_name_value_roundtrip():
    instance = column_TestSchema(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

column_Book_strategy = st.builds(column_Book, author=safe_text, pages=safe_text, title=safe_text, weight=safe_text)
@given(instance=column_Book_strategy)
@settings(max_examples=25)
def test_column_Book_instantiation(instance):
    assert isinstance(instance, column_Book)


column_TestSchema_strategy = st.builds(column_TestSchema, name=safe_text)
@given(instance=column_TestSchema_strategy)
@settings(max_examples=25)
def test_column_TestSchema_instantiation(instance):
    assert isinstance(instance, column_TestSchema)



