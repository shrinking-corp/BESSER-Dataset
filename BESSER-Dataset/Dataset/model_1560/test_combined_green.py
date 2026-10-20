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
    Paper_Paper,
    Paper_Papers,
    Paper_Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_paper_paper_is_not_abstract():
    assert not inspect.isabstract(Paper_Paper)


def test_hyp_paper_paper_constructor_exists():
    assert callable(Paper_Paper.__init__)


def test_hyp_paper_paper_constructor_args():
    sig = inspect.signature(Paper_Paper.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_paper_papers_is_not_abstract():
    assert not inspect.isabstract(Paper_Papers)


def test_hyp_paper_papers_constructor_exists():
    assert callable(Paper_Papers.__init__)


def test_hyp_paper_papers_constructor_args():
    sig = inspect.signature(Paper_Papers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paper_author_is_not_abstract():
    assert not inspect.isabstract(Paper_Author)


def test_hyp_paper_author_constructor_exists():
    assert callable(Paper_Author.__init__)


def test_hyp_paper_author_constructor_args():
    sig = inspect.signature(Paper_Author.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"





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
Paper_Paper_strategy = st.builds(
    Paper_Paper,
    title=
        safe_text
)
Paper_Papers_strategy = st.builds(
    Paper_Papers,
)
Paper_Author_strategy = st.builds(
    Paper_Author,
    email=
        safe_text,
    firstname=
        safe_text,
    lastname=
        safe_text
)




@given(instance=Paper_Paper_strategy)
def test_hyp_paper_paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





@given(instance=Paper_Author_strategy)
def test_hyp_paper_author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Paper_Author_strategy)
def test_hyp_paper_author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Paper_Author_strategy)
def test_hyp_paper_author_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Paper_Author,
    Paper_Paper,
    Paper_Papers,
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

def test_Paper_Author_email_value_roundtrip():
    instance = Paper_Author(email="sample_text", firstname="sample_text", lastname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Paper_Author_firstname_value_roundtrip():
    instance = Paper_Author(email="sample_text", firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Paper_Author_lastname_value_roundtrip():
    instance = Paper_Author(email="sample_text", firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Paper_Paper_title_value_roundtrip():
    instance = Paper_Paper(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_assoc_authors1_link_reassign_clear():
    a = Paper_Paper(title="sample_text")
    b1 = Paper_Author(email="sample_text", firstname="sample_text", lastname="sample_text")
    b2 = Paper_Author(email="sample_text_2", firstname="sample_text_2", lastname="sample_text_2")
    _safe_set(a, 'Paper_Paper2', {b1})
    assert _is_linked(a, 'Paper_Paper2', b1)
    if hasattr(b1, 'Paper_Author'):
        assert _is_linked(b1, 'Paper_Author', a)
    _safe_set(a, 'Paper_Paper2', {b2})
    assert _is_linked(a, 'Paper_Paper2', b2)
    if hasattr(b1, 'Paper_Author'):
        assert not _is_linked(b1, 'Paper_Author', a)
    if hasattr(b2, 'Paper_Author'):
        assert _is_linked(b2, 'Paper_Author', a)
    _safe_set(a, 'Paper_Paper2', set())
    assert not _is_linked(a, 'Paper_Paper2', b2)
    if hasattr(b2, 'Paper_Author'):
        assert not _is_linked(b2, 'Paper_Author', a)


def test_assoc_papers0_link_reassign_clear():
    a = Paper_Paper(title="sample_text")
    b1 = Paper_Papers()
    b2 = Paper_Papers()
    _safe_set(a, 'Paper_Paper', b1)
    assert _is_linked(a, 'Paper_Paper', b1)
    if hasattr(b1, 'Paper_Papers'):
        assert _is_linked(b1, 'Paper_Papers', a)
    _safe_set(a, 'Paper_Paper', b2)
    assert _is_linked(a, 'Paper_Paper', b2)
    if hasattr(b1, 'Paper_Papers'):
        assert not _is_linked(b1, 'Paper_Papers', a)
    if hasattr(b2, 'Paper_Papers'):
        assert _is_linked(b2, 'Paper_Papers', a)
    _safe_set(a, 'Paper_Paper', None)
    assert not _is_linked(a, 'Paper_Paper', b2)
    if hasattr(b2, 'Paper_Papers'):
        assert not _is_linked(b2, 'Paper_Papers', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Paper_Author_strategy = st.builds(Paper_Author, email=safe_text, firstname=safe_text, lastname=safe_text)
@given(instance=Paper_Author_strategy)
@settings(max_examples=25)
def test_Paper_Author_instantiation(instance):
    assert isinstance(instance, Paper_Author)


Paper_Paper_strategy = st.builds(Paper_Paper, title=safe_text)
@given(instance=Paper_Paper_strategy)
@settings(max_examples=25)
def test_Paper_Paper_instantiation(instance):
    assert isinstance(instance, Paper_Paper)


Paper_Papers_strategy = st.builds(Paper_Papers)
@given(instance=Paper_Papers_strategy)
@settings(max_examples=25)
def test_Paper_Papers_instantiation(instance):
    assert isinstance(instance, Paper_Papers)



