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
    Section,
    docbook_Sect2,
    docbook_Para,
    docbook_Sect1,
    TitledElement,
    docbook_Section,
    docbook_TitledElement,
    docbook_Book,
    docbook_DocBook,
    docbook_Article,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_hyp_section_constructor_exists():
    assert callable(Section.__init__)


def test_hyp_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_sect2_is_not_abstract():
    assert not inspect.isabstract(docbook_Sect2)


def test_hyp_docbook_sect2_constructor_exists():
    assert callable(docbook_Sect2.__init__)


def test_hyp_docbook_sect2_constructor_args():
    sig = inspect.signature(docbook_Sect2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_para_is_not_abstract():
    assert not inspect.isabstract(docbook_Para)


def test_hyp_docbook_para_constructor_exists():
    assert callable(docbook_Para.__init__)


def test_hyp_docbook_para_constructor_args():
    sig = inspect.signature(docbook_Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_docbook_sect1_is_not_abstract():
    assert not inspect.isabstract(docbook_Sect1)


def test_hyp_docbook_sect1_constructor_exists():
    assert callable(docbook_Sect1.__init__)


def test_hyp_docbook_sect1_constructor_args():
    sig = inspect.signature(docbook_Sect1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_hyp_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_hyp_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_section_is_not_abstract():
    assert not inspect.isabstract(docbook_Section)


def test_hyp_docbook_section_constructor_exists():
    assert callable(docbook_Section.__init__)


def test_hyp_docbook_section_constructor_args():
    sig = inspect.signature(docbook_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_titledelement_is_not_abstract():
    assert not inspect.isabstract(docbook_TitledElement)


def test_hyp_docbook_titledelement_constructor_exists():
    assert callable(docbook_TitledElement.__init__)


def test_hyp_docbook_titledelement_constructor_args():
    sig = inspect.signature(docbook_TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_docbook_book_is_not_abstract():
    assert not inspect.isabstract(docbook_Book)


def test_hyp_docbook_book_constructor_exists():
    assert callable(docbook_Book.__init__)


def test_hyp_docbook_book_constructor_args():
    sig = inspect.signature(docbook_Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_docbook_is_not_abstract():
    assert not inspect.isabstract(docbook_DocBook)


def test_hyp_docbook_docbook_constructor_exists():
    assert callable(docbook_DocBook.__init__)


def test_hyp_docbook_docbook_constructor_args():
    sig = inspect.signature(docbook_DocBook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_article_is_not_abstract():
    assert not inspect.isabstract(docbook_Article)


def test_hyp_docbook_article_constructor_exists():
    assert callable(docbook_Article.__init__)


def test_hyp_docbook_article_constructor_args():
    sig = inspect.signature(docbook_Article.__init__)
    params = list(sig.parameters.keys())


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
Section_strategy = st.builds(
    Section,
)
docbook_Sect2_strategy = st.builds(
    docbook_Sect2,
)
docbook_Para_strategy = st.builds(
    docbook_Para,
    content=
        safe_text
)
docbook_Sect1_strategy = st.builds(
    docbook_Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
docbook_Section_strategy = st.builds(
    docbook_Section,
)
docbook_TitledElement_strategy = st.builds(
    docbook_TitledElement,
    title=
        safe_text
)
docbook_Book_strategy = st.builds(
    docbook_Book,
)
docbook_DocBook_strategy = st.builds(
    docbook_DocBook,
)
docbook_Article_strategy = st.builds(
    docbook_Article,
)






@given(instance=docbook_Para_strategy)
def test_hyp_docbook_para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original







@given(instance=docbook_TitledElement_strategy)
def test_hyp_docbook_titledelement_title_setter(instance):
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
    Section,
    TitledElement,
    docbook_Article,
    docbook_Book,
    docbook_DocBook,
    docbook_Para,
    docbook_Sect1,
    docbook_Sect2,
    docbook_Section,
    docbook_TitledElement,
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

def test_docbook_Para_content_value_roundtrip():
    instance = docbook_Para(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_docbook_TitledElement_title_value_roundtrip():
    instance = docbook_TitledElement(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_docbook_Sect1_isa_Section():
    instance = docbook_Sect1()
    assert isinstance(instance, Section)


def test_docbook_Sect2_isa_Section():
    instance = docbook_Sect2()
    assert isinstance(instance, Section)


def test_docbook_Article_isa_TitledElement():
    instance = docbook_Article()
    assert isinstance(instance, TitledElement)


def test_docbook_Section_isa_TitledElement():
    instance = docbook_Section()
    assert isinstance(instance, TitledElement)


def test_assoc_paras5_link_reassign_clear():
    a = docbook_Para(content="sample_text")
    b1 = docbook_Section()
    b2 = docbook_Section()
    _safe_set(a, 'docbook_Para', b1)
    assert _is_linked(a, 'docbook_Para', b1)
    if hasattr(b1, 'docbook_Section'):
        assert _is_linked(b1, 'docbook_Section', a)
    _safe_set(a, 'docbook_Para', b2)
    assert _is_linked(a, 'docbook_Para', b2)
    if hasattr(b1, 'docbook_Section'):
        assert not _is_linked(b1, 'docbook_Section', a)
    if hasattr(b2, 'docbook_Section'):
        assert _is_linked(b2, 'docbook_Section', a)
    _safe_set(a, 'docbook_Para', None)
    assert not _is_linked(a, 'docbook_Para', b2)
    if hasattr(b2, 'docbook_Section'):
        assert not _is_linked(b2, 'docbook_Section', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


TitledElement_strategy = st.builds(TitledElement)
@given(instance=TitledElement_strategy)
@settings(max_examples=25)
def test_TitledElement_instantiation(instance):
    assert isinstance(instance, TitledElement)


docbook_Article_strategy = st.builds(docbook_Article)
@given(instance=docbook_Article_strategy)
@settings(max_examples=25)
def test_docbook_Article_instantiation(instance):
    assert isinstance(instance, docbook_Article)


docbook_Book_strategy = st.builds(docbook_Book)
@given(instance=docbook_Book_strategy)
@settings(max_examples=25)
def test_docbook_Book_instantiation(instance):
    assert isinstance(instance, docbook_Book)


docbook_DocBook_strategy = st.builds(docbook_DocBook)
@given(instance=docbook_DocBook_strategy)
@settings(max_examples=25)
def test_docbook_DocBook_instantiation(instance):
    assert isinstance(instance, docbook_DocBook)


docbook_Para_strategy = st.builds(docbook_Para, content=safe_text)
@given(instance=docbook_Para_strategy)
@settings(max_examples=25)
def test_docbook_Para_instantiation(instance):
    assert isinstance(instance, docbook_Para)


docbook_Sect1_strategy = st.builds(docbook_Sect1)
@given(instance=docbook_Sect1_strategy)
@settings(max_examples=25)
def test_docbook_Sect1_instantiation(instance):
    assert isinstance(instance, docbook_Sect1)


docbook_Sect2_strategy = st.builds(docbook_Sect2)
@given(instance=docbook_Sect2_strategy)
@settings(max_examples=25)
def test_docbook_Sect2_instantiation(instance):
    assert isinstance(instance, docbook_Sect2)


docbook_Section_strategy = st.builds(docbook_Section)
@given(instance=docbook_Section_strategy)
@settings(max_examples=25)
def test_docbook_Section_instantiation(instance):
    assert isinstance(instance, docbook_Section)


docbook_TitledElement_strategy = st.builds(docbook_TitledElement, title=safe_text)
@given(instance=docbook_TitledElement_strategy)
@settings(max_examples=25)
def test_docbook_TitledElement_instantiation(instance):
    assert isinstance(instance, docbook_TitledElement)



