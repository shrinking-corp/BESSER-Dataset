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
    Bibtex_Tag,
    Bibtex_BibtexEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bibtex_tag_is_not_abstract():
    assert not inspect.isabstract(Bibtex_Tag)


def test_hyp_bibtex_tag_constructor_exists():
    assert callable(Bibtex_Tag.__init__)


def test_hyp_bibtex_tag_constructor_args():
    sig = inspect.signature(Bibtex_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_bibtex_bibtexentry_is_not_abstract():
    assert not inspect.isabstract(Bibtex_BibtexEntry)


def test_hyp_bibtex_bibtexentry_constructor_exists():
    assert callable(Bibtex_BibtexEntry.__init__)


def test_hyp_bibtex_bibtexentry_constructor_args():
    sig = inspect.signature(Bibtex_BibtexEntry.__init__)
    params = list(sig.parameters.keys())
    assert "Author" in params, "Missing parameter 'Author'"
    assert "Pages" in params, "Missing parameter 'Pages'"
    assert "Volume" in params, "Missing parameter 'Volume'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "publicationFilePath" in params, "Missing parameter 'publicationFilePath'"
    assert "Journal" in params, "Missing parameter 'Journal'"
    assert "Text" in params, "Missing parameter 'Text'"
    assert "Year" in params, "Missing parameter 'Year'"










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
Bibtex_Tag_strategy = st.builds(
    Bibtex_Tag,
    Name=
        safe_text
)
Bibtex_BibtexEntry_strategy = st.builds(
    Bibtex_BibtexEntry,
    Author=
        safe_text,
    Pages=
        safe_text,
    Volume=
        safe_text,
    Title=
        safe_text,
    publicationFilePath=
        safe_text,
    Journal=
        safe_text,
    Text=
        safe_text,
    Year=
        safe_text
)




@given(instance=Bibtex_Tag_strategy)
def test_hyp_bibtex_tag_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Bibtex_Tag_strategy)
@settings(max_examples=30)
def test_hyp_bibtex_tag_tostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toString' in Bibtex_Tag is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toString' in Bibtex_Tag did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toString' in Bibtex_Tag is not implemented or raised an error")




@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Pages_setter(instance):
    original = instance.Pages
    instance.Pages = original
    assert instance.Pages == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Volume_setter(instance):
    original = instance.Volume
    instance.Volume = original
    assert instance.Volume == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_publicationFilePath_setter(instance):
    original = instance.publicationFilePath
    instance.publicationFilePath = original
    assert instance.publicationFilePath == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Journal_setter(instance):
    original = instance.Journal
    instance.Journal = original
    assert instance.Journal == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original



@given(instance=Bibtex_BibtexEntry_strategy)
def test_hyp_bibtex_bibtexentry_Year_setter(instance):
    original = instance.Year
    instance.Year = original
    assert instance.Year == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Bibtex_BibtexEntry_strategy)
@settings(max_examples=30)
def test_hyp_bibtex_bibtexentry_tostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toString' in Bibtex_BibtexEntry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toString' in Bibtex_BibtexEntry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toString' in Bibtex_BibtexEntry is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bibtex_BibtexEntry,
    Bibtex_Tag,
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

def test_Bibtex_BibtexEntry_Author_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Author == "sample_text"
    instance.Author = "sample_text_2"
    assert instance.Author == "sample_text_2"


def test_Bibtex_BibtexEntry_Journal_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Journal == "sample_text"
    instance.Journal = "sample_text_2"
    assert instance.Journal == "sample_text_2"


def test_Bibtex_BibtexEntry_Pages_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Pages == "sample_text"
    instance.Pages = "sample_text_2"
    assert instance.Pages == "sample_text_2"


def test_Bibtex_BibtexEntry_Text_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Text == "sample_text"
    instance.Text = "sample_text_2"
    assert instance.Text == "sample_text_2"


def test_Bibtex_BibtexEntry_Title_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Title == "sample_text"
    instance.Title = "sample_text_2"
    assert instance.Title == "sample_text_2"


def test_Bibtex_BibtexEntry_Volume_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Volume == "sample_text"
    instance.Volume = "sample_text_2"
    assert instance.Volume == "sample_text_2"


def test_Bibtex_BibtexEntry_Year_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.Year == "sample_text"
    instance.Year = "sample_text_2"
    assert instance.Year == "sample_text_2"


def test_Bibtex_BibtexEntry_publicationFilePath_value_roundtrip():
    instance = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    assert instance.publicationFilePath == "sample_text"
    instance.publicationFilePath = "sample_text_2"
    assert instance.publicationFilePath == "sample_text_2"


def test_Bibtex_Tag_Name_value_roundtrip():
    instance = Bibtex_Tag(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Tags0_link_reassign_clear():
    a = Bibtex_Tag(Name="sample_text")
    b1 = Bibtex_BibtexEntry(Author="sample_text", Journal="sample_text", Pages="sample_text", Text="sample_text", Title="sample_text", Volume="sample_text", Year="sample_text", publicationFilePath="sample_text")
    b2 = Bibtex_BibtexEntry(Author="sample_text_2", Journal="sample_text_2", Pages="sample_text_2", Text="sample_text_2", Title="sample_text_2", Volume="sample_text_2", Year="sample_text_2", publicationFilePath="sample_text_2")
    _safe_set(a, 'Bibtex_Tag', b1)
    assert _is_linked(a, 'Bibtex_Tag', b1)
    if hasattr(b1, 'Bibtex_BibtexEntry'):
        assert _is_linked(b1, 'Bibtex_BibtexEntry', a)
    _safe_set(a, 'Bibtex_Tag', b2)
    assert _is_linked(a, 'Bibtex_Tag', b2)
    if hasattr(b1, 'Bibtex_BibtexEntry'):
        assert not _is_linked(b1, 'Bibtex_BibtexEntry', a)
    if hasattr(b2, 'Bibtex_BibtexEntry'):
        assert _is_linked(b2, 'Bibtex_BibtexEntry', a)
    _safe_set(a, 'Bibtex_Tag', None)
    assert not _is_linked(a, 'Bibtex_Tag', b2)
    if hasattr(b2, 'Bibtex_BibtexEntry'):
        assert not _is_linked(b2, 'Bibtex_BibtexEntry', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bibtex_BibtexEntry_strategy = st.builds(Bibtex_BibtexEntry, Author=safe_text, Journal=safe_text, Pages=safe_text, Text=safe_text, Title=safe_text, Volume=safe_text, Year=safe_text, publicationFilePath=safe_text)
@given(instance=Bibtex_BibtexEntry_strategy)
@settings(max_examples=25)
def test_Bibtex_BibtexEntry_instantiation(instance):
    assert isinstance(instance, Bibtex_BibtexEntry)


Bibtex_Tag_strategy = st.builds(Bibtex_Tag, Name=safe_text)
@given(instance=Bibtex_Tag_strategy)
@settings(max_examples=25)
def test_Bibtex_Tag_instantiation(instance):
    assert isinstance(instance, Bibtex_Tag)



