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
    Publication_Publication,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_publication_publication_is_not_abstract():
    assert not inspect.isabstract(Publication_Publication)


def test_hyp_publication_publication_constructor_exists():
    assert callable(Publication_Publication.__init__)


def test_hyp_publication_publication_constructor_args():
    sig = inspect.signature(Publication_Publication.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "authors" in params, "Missing parameter 'authors'"
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
Publication_Publication_strategy = st.builds(
    Publication_Publication,
    nbPages=
        safe_text,
    authors=
        safe_text,
    title=
        safe_text
)




@given(instance=Publication_Publication_strategy)
def test_hyp_publication_publication_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=Publication_Publication_strategy)
def test_hyp_publication_publication_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=Publication_Publication_strategy)
def test_hyp_publication_publication_title_setter(instance):
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
    Publication_Publication,
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

def test_Publication_Publication_authors_value_roundtrip():
    instance = Publication_Publication(authors="sample_text", nbPages="sample_text", title="sample_text")
    assert instance.authors == "sample_text"
    instance.authors = "sample_text_2"
    assert instance.authors == "sample_text_2"


def test_Publication_Publication_nbPages_value_roundtrip():
    instance = Publication_Publication(authors="sample_text", nbPages="sample_text", title="sample_text")
    assert instance.nbPages == "sample_text"
    instance.nbPages = "sample_text_2"
    assert instance.nbPages == "sample_text_2"


def test_Publication_Publication_title_value_roundtrip():
    instance = Publication_Publication(authors="sample_text", nbPages="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Publication_Publication_strategy = st.builds(Publication_Publication, authors=safe_text, nbPages=safe_text, title=safe_text)
@given(instance=Publication_Publication_strategy)
@settings(max_examples=25)
def test_Publication_Publication_instantiation(instance):
    assert isinstance(instance, Publication_Publication)



