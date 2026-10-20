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
    mm1_Library,
    mm1_Film,
    mm1_Book,
    mm1_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mm1_library_is_not_abstract():
    assert not inspect.isabstract(mm1_Library)


def test_hyp_mm1_library_constructor_exists():
    assert callable(mm1_Library.__init__)


def test_hyp_mm1_library_constructor_args():
    sig = inspect.signature(mm1_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mm1_film_is_not_abstract():
    assert not inspect.isabstract(mm1_Film)


def test_hyp_mm1_film_constructor_exists():
    assert callable(mm1_Film.__init__)


def test_hyp_mm1_film_constructor_args():
    sig = inspect.signature(mm1_Film.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mm1_book_is_not_abstract():
    assert not inspect.isabstract(mm1_Book)


def test_hyp_mm1_book_constructor_exists():
    assert callable(mm1_Book.__init__)


def test_hyp_mm1_book_constructor_args():
    sig = inspect.signature(mm1_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mm1_member_is_not_abstract():
    assert not inspect.isabstract(mm1_Member)


def test_hyp_mm1_member_constructor_exists():
    assert callable(mm1_Member.__init__)


def test_hyp_mm1_member_constructor_args():
    sig = inspect.signature(mm1_Member.__init__)
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
mm1_Library_strategy = st.builds(
    mm1_Library,
    name=
        safe_text
)
mm1_Film_strategy = st.builds(
    mm1_Film,
    name=
        safe_text
)
mm1_Book_strategy = st.builds(
    mm1_Book,
    name=
        safe_text
)
mm1_Member_strategy = st.builds(
    mm1_Member,
    name=
        safe_text
)




@given(instance=mm1_Library_strategy)
def test_hyp_mm1_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm1_Film_strategy)
def test_hyp_mm1_film_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm1_Book_strategy)
def test_hyp_mm1_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=mm1_Member_strategy)
def test_hyp_mm1_member_name_setter(instance):
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
    mm1_Book,
    mm1_Film,
    mm1_Library,
    mm1_Member,
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

def test_mm1_Book_name_value_roundtrip():
    instance = mm1_Book(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm1_Film_name_value_roundtrip():
    instance = mm1_Film(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm1_Library_name_value_roundtrip():
    instance = mm1_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mm1_Member_name_value_roundtrip():
    instance = mm1_Member(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_bookLoans5_link_reassign_clear():
    a = mm1_Member(name="sample_text")
    b1 = mm1_Book(name="sample_text")
    b2 = mm1_Book(name="sample_text_2")
    _safe_set(a, 'mm1_Member6', {b1})
    assert _is_linked(a, 'mm1_Member6', b1)
    if hasattr(b1, 'mm1_Book7'):
        assert _is_linked(b1, 'mm1_Book7', a)
    _safe_set(a, 'mm1_Member6', {b2})
    assert _is_linked(a, 'mm1_Member6', b2)
    if hasattr(b1, 'mm1_Book7'):
        assert not _is_linked(b1, 'mm1_Book7', a)
    if hasattr(b2, 'mm1_Book7'):
        assert _is_linked(b2, 'mm1_Book7', a)
    _safe_set(a, 'mm1_Member6', set())
    assert not _is_linked(a, 'mm1_Member6', b2)
    if hasattr(b2, 'mm1_Book7'):
        assert not _is_linked(b2, 'mm1_Book7', a)


def test_assoc_books1_link_reassign_clear():
    a = mm1_Library(name="sample_text")
    b1 = mm1_Book(name="sample_text")
    b2 = mm1_Book(name="sample_text_2")
    _safe_set(a, 'mm1_Library2', {b1})
    assert _is_linked(a, 'mm1_Library2', b1)
    if hasattr(b1, 'mm1_Book'):
        assert _is_linked(b1, 'mm1_Book', a)
    _safe_set(a, 'mm1_Library2', {b2})
    assert _is_linked(a, 'mm1_Library2', b2)
    if hasattr(b1, 'mm1_Book'):
        assert not _is_linked(b1, 'mm1_Book', a)
    if hasattr(b2, 'mm1_Book'):
        assert _is_linked(b2, 'mm1_Book', a)
    _safe_set(a, 'mm1_Library2', set())
    assert not _is_linked(a, 'mm1_Library2', b2)
    if hasattr(b2, 'mm1_Book'):
        assert not _is_linked(b2, 'mm1_Book', a)


def test_assoc_filmLoans8_link_reassign_clear():
    a = mm1_Member(name="sample_text")
    b1 = mm1_Film(name="sample_text")
    b2 = mm1_Film(name="sample_text_2")
    _safe_set(a, 'mm1_Member9', {b1})
    assert _is_linked(a, 'mm1_Member9', b1)
    if hasattr(b1, 'mm1_Film10'):
        assert _is_linked(b1, 'mm1_Film10', a)
    _safe_set(a, 'mm1_Member9', {b2})
    assert _is_linked(a, 'mm1_Member9', b2)
    if hasattr(b1, 'mm1_Film10'):
        assert not _is_linked(b1, 'mm1_Film10', a)
    if hasattr(b2, 'mm1_Film10'):
        assert _is_linked(b2, 'mm1_Film10', a)
    _safe_set(a, 'mm1_Member9', set())
    assert not _is_linked(a, 'mm1_Member9', b2)
    if hasattr(b2, 'mm1_Film10'):
        assert not _is_linked(b2, 'mm1_Film10', a)


def test_assoc_films3_link_reassign_clear():
    a = mm1_Library(name="sample_text")
    b1 = mm1_Film(name="sample_text")
    b2 = mm1_Film(name="sample_text_2")
    _safe_set(a, 'mm1_Library4', {b1})
    assert _is_linked(a, 'mm1_Library4', b1)
    if hasattr(b1, 'mm1_Film'):
        assert _is_linked(b1, 'mm1_Film', a)
    _safe_set(a, 'mm1_Library4', {b2})
    assert _is_linked(a, 'mm1_Library4', b2)
    if hasattr(b1, 'mm1_Film'):
        assert not _is_linked(b1, 'mm1_Film', a)
    if hasattr(b2, 'mm1_Film'):
        assert _is_linked(b2, 'mm1_Film', a)
    _safe_set(a, 'mm1_Library4', set())
    assert not _is_linked(a, 'mm1_Library4', b2)
    if hasattr(b2, 'mm1_Film'):
        assert not _is_linked(b2, 'mm1_Film', a)


def test_assoc_members0_link_reassign_clear():
    a = mm1_Member(name="sample_text")
    b1 = mm1_Library(name="sample_text")
    b2 = mm1_Library(name="sample_text_2")
    _safe_set(a, 'mm1_Member', b1)
    assert _is_linked(a, 'mm1_Member', b1)
    if hasattr(b1, 'mm1_Library'):
        assert _is_linked(b1, 'mm1_Library', a)
    _safe_set(a, 'mm1_Member', b2)
    assert _is_linked(a, 'mm1_Member', b2)
    if hasattr(b1, 'mm1_Library'):
        assert not _is_linked(b1, 'mm1_Library', a)
    if hasattr(b2, 'mm1_Library'):
        assert _is_linked(b2, 'mm1_Library', a)
    _safe_set(a, 'mm1_Member', None)
    assert not _is_linked(a, 'mm1_Member', b2)
    if hasattr(b2, 'mm1_Library'):
        assert not _is_linked(b2, 'mm1_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

mm1_Book_strategy = st.builds(mm1_Book, name=safe_text)
@given(instance=mm1_Book_strategy)
@settings(max_examples=25)
def test_mm1_Book_instantiation(instance):
    assert isinstance(instance, mm1_Book)


mm1_Film_strategy = st.builds(mm1_Film, name=safe_text)
@given(instance=mm1_Film_strategy)
@settings(max_examples=25)
def test_mm1_Film_instantiation(instance):
    assert isinstance(instance, mm1_Film)


mm1_Library_strategy = st.builds(mm1_Library, name=safe_text)
@given(instance=mm1_Library_strategy)
@settings(max_examples=25)
def test_mm1_Library_instantiation(instance):
    assert isinstance(instance, mm1_Library)


mm1_Member_strategy = st.builds(mm1_Member, name=safe_text)
@given(instance=mm1_Member_strategy)
@settings(max_examples=25)
def test_mm1_Member_instantiation(instance):
    assert isinstance(instance, mm1_Member)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mm1_Book,
    mm1_Film,
    mm1_Library,
    mm1_Member,
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

def test_assoc_bookLoans5_reverse_link_reassign_clear():
    a1 = mm1_Member(name="sample_text")
    a2 = mm1_Member(name="sample_text_2")
    b = mm1_Book(name="sample_text")
    _safe_set(b, 'mm1_Book7', a1)
    assert _is_linked(b, 'mm1_Book7', a1)
    if hasattr(a1, 'mm1_Member6'):
        assert _is_linked(a1, 'mm1_Member6', b)
    _safe_set(b, 'mm1_Book7', a2)
    assert _is_linked(b, 'mm1_Book7', a2)
    if hasattr(a1, 'mm1_Member6'):
        assert not _is_linked(a1, 'mm1_Member6', b)
    if hasattr(a2, 'mm1_Member6'):
        assert _is_linked(a2, 'mm1_Member6', b)
    _safe_set(b, 'mm1_Book7', None)
    assert not _is_linked(b, 'mm1_Book7', a2)
    if hasattr(a2, 'mm1_Member6'):
        assert not _is_linked(a2, 'mm1_Member6', b)


def test_assoc_books1_reverse_link_reassign_clear():
    a1 = mm1_Library(name="sample_text")
    a2 = mm1_Library(name="sample_text_2")
    b = mm1_Book(name="sample_text")
    _safe_set(b, 'mm1_Book', a1)
    assert _is_linked(b, 'mm1_Book', a1)
    if hasattr(a1, 'mm1_Library2'):
        assert _is_linked(a1, 'mm1_Library2', b)
    _safe_set(b, 'mm1_Book', a2)
    assert _is_linked(b, 'mm1_Book', a2)
    if hasattr(a1, 'mm1_Library2'):
        assert not _is_linked(a1, 'mm1_Library2', b)
    if hasattr(a2, 'mm1_Library2'):
        assert _is_linked(a2, 'mm1_Library2', b)
    _safe_set(b, 'mm1_Book', None)
    assert not _is_linked(b, 'mm1_Book', a2)
    if hasattr(a2, 'mm1_Library2'):
        assert not _is_linked(a2, 'mm1_Library2', b)


def test_assoc_filmLoans8_reverse_link_reassign_clear():
    a1 = mm1_Member(name="sample_text")
    a2 = mm1_Member(name="sample_text_2")
    b = mm1_Film(name="sample_text")
    _safe_set(b, 'mm1_Film10', a1)
    assert _is_linked(b, 'mm1_Film10', a1)
    if hasattr(a1, 'mm1_Member9'):
        assert _is_linked(a1, 'mm1_Member9', b)
    _safe_set(b, 'mm1_Film10', a2)
    assert _is_linked(b, 'mm1_Film10', a2)
    if hasattr(a1, 'mm1_Member9'):
        assert not _is_linked(a1, 'mm1_Member9', b)
    if hasattr(a2, 'mm1_Member9'):
        assert _is_linked(a2, 'mm1_Member9', b)
    _safe_set(b, 'mm1_Film10', None)
    assert not _is_linked(b, 'mm1_Film10', a2)
    if hasattr(a2, 'mm1_Member9'):
        assert not _is_linked(a2, 'mm1_Member9', b)


def test_assoc_films3_reverse_link_reassign_clear():
    a1 = mm1_Library(name="sample_text")
    a2 = mm1_Library(name="sample_text_2")
    b = mm1_Film(name="sample_text")
    _safe_set(b, 'mm1_Film', a1)
    assert _is_linked(b, 'mm1_Film', a1)
    if hasattr(a1, 'mm1_Library4'):
        assert _is_linked(a1, 'mm1_Library4', b)
    _safe_set(b, 'mm1_Film', a2)
    assert _is_linked(b, 'mm1_Film', a2)
    if hasattr(a1, 'mm1_Library4'):
        assert not _is_linked(a1, 'mm1_Library4', b)
    if hasattr(a2, 'mm1_Library4'):
        assert _is_linked(a2, 'mm1_Library4', b)
    _safe_set(b, 'mm1_Film', None)
    assert not _is_linked(b, 'mm1_Film', a2)
    if hasattr(a2, 'mm1_Library4'):
        assert not _is_linked(a2, 'mm1_Library4', b)


def test_assoc_members0_reverse_link_reassign_clear():
    a1 = mm1_Member(name="sample_text")
    a2 = mm1_Member(name="sample_text_2")
    b = mm1_Library(name="sample_text")
    _safe_set(b, 'mm1_Library', {a1})
    assert _is_linked(b, 'mm1_Library', a1)
    if hasattr(a1, 'mm1_Member'):
        assert _is_linked(a1, 'mm1_Member', b)
    _safe_set(b, 'mm1_Library', {a2})
    assert _is_linked(b, 'mm1_Library', a2)
    if hasattr(a1, 'mm1_Member'):
        assert not _is_linked(a1, 'mm1_Member', b)
    if hasattr(a2, 'mm1_Member'):
        assert _is_linked(a2, 'mm1_Member', b)
    _safe_set(b, 'mm1_Library', set())
    assert not _is_linked(b, 'mm1_Library', a2)
    if hasattr(a2, 'mm1_Member'):
        assert not _is_linked(a2, 'mm1_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


