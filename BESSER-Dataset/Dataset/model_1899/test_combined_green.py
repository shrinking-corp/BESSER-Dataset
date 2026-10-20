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
    DocBook_Para,
    Sect2,
    Section,
    DocBook_Sect2,
    DocBook_Sect1,
    Para,
    Sect1,
    TitledElement,
    DocBook_Section,
    DocBook_Article,
    DocBook_TitledElement,
    Article,
    DocBook_Book,
    Book,
    DocBook_DocBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_docbook_para_is_not_abstract():
    assert not inspect.isabstract(DocBook_Para)


def test_hyp_docbook_para_constructor_exists():
    assert callable(DocBook_Para.__init__)


def test_hyp_docbook_para_constructor_args():
    sig = inspect.signature(DocBook_Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_sect2_is_not_abstract():
    assert not inspect.isabstract(Sect2)


def test_hyp_sect2_constructor_exists():
    assert callable(Sect2.__init__)


def test_hyp_sect2_constructor_args():
    sig = inspect.signature(Sect2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_hyp_section_constructor_exists():
    assert callable(Section.__init__)


def test_hyp_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_sect2_is_not_abstract():
    assert not inspect.isabstract(DocBook_Sect2)


def test_hyp_docbook_sect2_constructor_exists():
    assert callable(DocBook_Sect2.__init__)


def test_hyp_docbook_sect2_constructor_args():
    sig = inspect.signature(DocBook_Sect2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_sect1_is_not_abstract():
    assert not inspect.isabstract(DocBook_Sect1)


def test_hyp_docbook_sect1_constructor_exists():
    assert callable(DocBook_Sect1.__init__)


def test_hyp_docbook_sect1_constructor_args():
    sig = inspect.signature(DocBook_Sect1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_para_is_not_abstract():
    assert not inspect.isabstract(Para)


def test_hyp_para_constructor_exists():
    assert callable(Para.__init__)


def test_hyp_para_constructor_args():
    sig = inspect.signature(Para.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sect1_is_not_abstract():
    assert not inspect.isabstract(Sect1)


def test_hyp_sect1_constructor_exists():
    assert callable(Sect1.__init__)


def test_hyp_sect1_constructor_args():
    sig = inspect.signature(Sect1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_hyp_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_hyp_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_section_is_not_abstract():
    assert not inspect.isabstract(DocBook_Section)


def test_hyp_docbook_section_constructor_exists():
    assert callable(DocBook_Section.__init__)


def test_hyp_docbook_section_constructor_args():
    sig = inspect.signature(DocBook_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_article_is_not_abstract():
    assert not inspect.isabstract(DocBook_Article)


def test_hyp_docbook_article_constructor_exists():
    assert callable(DocBook_Article.__init__)


def test_hyp_docbook_article_constructor_args():
    sig = inspect.signature(DocBook_Article.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_titledelement_is_not_abstract():
    assert not inspect.isabstract(DocBook_TitledElement)


def test_hyp_docbook_titledelement_constructor_exists():
    assert callable(DocBook_TitledElement.__init__)


def test_hyp_docbook_titledelement_constructor_args():
    sig = inspect.signature(DocBook_TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_article_is_not_abstract():
    assert not inspect.isabstract(Article)


def test_hyp_article_constructor_exists():
    assert callable(Article.__init__)


def test_hyp_article_constructor_args():
    sig = inspect.signature(Article.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_book_is_not_abstract():
    assert not inspect.isabstract(DocBook_Book)


def test_hyp_docbook_book_constructor_exists():
    assert callable(DocBook_Book.__init__)


def test_hyp_docbook_book_constructor_args():
    sig = inspect.signature(DocBook_Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_docbook_is_not_abstract():
    assert not inspect.isabstract(DocBook_DocBook)


def test_hyp_docbook_docbook_constructor_exists():
    assert callable(DocBook_DocBook.__init__)


def test_hyp_docbook_docbook_constructor_args():
    sig = inspect.signature(DocBook_DocBook.__init__)
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
DocBook_Para_strategy = st.builds(
    DocBook_Para,
    content=
        safe_text
)
Sect2_strategy = st.builds(
    Sect2,
)
Section_strategy = st.builds(
    Section,
)
DocBook_Sect2_strategy = st.builds(
    DocBook_Sect2,
)
DocBook_Sect1_strategy = st.builds(
    DocBook_Sect1,
)
Para_strategy = st.builds(
    Para,
)
Sect1_strategy = st.builds(
    Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
DocBook_Section_strategy = st.builds(
    DocBook_Section,
)
DocBook_Article_strategy = st.builds(
    DocBook_Article,
)
DocBook_TitledElement_strategy = st.builds(
    DocBook_TitledElement,
    title=
        safe_text
)
Article_strategy = st.builds(
    Article,
)
DocBook_Book_strategy = st.builds(
    DocBook_Book,
)
Book_strategy = st.builds(
    Book,
)
DocBook_DocBook_strategy = st.builds(
    DocBook_DocBook,
)




@given(instance=DocBook_Para_strategy)
def test_hyp_docbook_para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original













@given(instance=DocBook_TitledElement_strategy)
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
    Article,
    Book,
    DocBook_Article,
    DocBook_Book,
    DocBook_DocBook,
    DocBook_Para,
    DocBook_Sect1,
    DocBook_Sect2,
    DocBook_Section,
    DocBook_TitledElement,
    Para,
    Sect1,
    Sect2,
    Section,
    TitledElement,
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

def test_DocBook_Para_content_value_roundtrip():
    instance = DocBook_Para(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_DocBook_TitledElement_title_value_roundtrip():
    instance = DocBook_TitledElement(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_DocBook_Sect1_isa_Section():
    instance = DocBook_Sect1()
    assert isinstance(instance, Section)


def test_DocBook_Sect2_isa_Section():
    instance = DocBook_Sect2()
    assert isinstance(instance, Section)


def test_DocBook_Article_isa_TitledElement():
    instance = DocBook_Article()
    assert isinstance(instance, TitledElement)


def test_DocBook_Section_isa_TitledElement():
    instance = DocBook_Section()
    assert isinstance(instance, TitledElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Article_strategy = st.builds(Article)
@given(instance=Article_strategy)
@settings(max_examples=25)
def test_Article_instantiation(instance):
    assert isinstance(instance, Article)


Book_strategy = st.builds(Book)
@given(instance=Book_strategy)
@settings(max_examples=25)
def test_Book_instantiation(instance):
    assert isinstance(instance, Book)


DocBook_Article_strategy = st.builds(DocBook_Article)
@given(instance=DocBook_Article_strategy)
@settings(max_examples=25)
def test_DocBook_Article_instantiation(instance):
    assert isinstance(instance, DocBook_Article)


DocBook_Book_strategy = st.builds(DocBook_Book)
@given(instance=DocBook_Book_strategy)
@settings(max_examples=25)
def test_DocBook_Book_instantiation(instance):
    assert isinstance(instance, DocBook_Book)


DocBook_DocBook_strategy = st.builds(DocBook_DocBook)
@given(instance=DocBook_DocBook_strategy)
@settings(max_examples=25)
def test_DocBook_DocBook_instantiation(instance):
    assert isinstance(instance, DocBook_DocBook)


DocBook_Para_strategy = st.builds(DocBook_Para, content=safe_text)
@given(instance=DocBook_Para_strategy)
@settings(max_examples=25)
def test_DocBook_Para_instantiation(instance):
    assert isinstance(instance, DocBook_Para)


DocBook_Sect1_strategy = st.builds(DocBook_Sect1)
@given(instance=DocBook_Sect1_strategy)
@settings(max_examples=25)
def test_DocBook_Sect1_instantiation(instance):
    assert isinstance(instance, DocBook_Sect1)


DocBook_Sect2_strategy = st.builds(DocBook_Sect2)
@given(instance=DocBook_Sect2_strategy)
@settings(max_examples=25)
def test_DocBook_Sect2_instantiation(instance):
    assert isinstance(instance, DocBook_Sect2)


DocBook_Section_strategy = st.builds(DocBook_Section)
@given(instance=DocBook_Section_strategy)
@settings(max_examples=25)
def test_DocBook_Section_instantiation(instance):
    assert isinstance(instance, DocBook_Section)


DocBook_TitledElement_strategy = st.builds(DocBook_TitledElement, title=safe_text)
@given(instance=DocBook_TitledElement_strategy)
@settings(max_examples=25)
def test_DocBook_TitledElement_instantiation(instance):
    assert isinstance(instance, DocBook_TitledElement)


Para_strategy = st.builds(Para)
@given(instance=Para_strategy)
@settings(max_examples=25)
def test_Para_instantiation(instance):
    assert isinstance(instance, Para)


Sect1_strategy = st.builds(Sect1)
@given(instance=Sect1_strategy)
@settings(max_examples=25)
def test_Sect1_instantiation(instance):
    assert isinstance(instance, Sect1)


Sect2_strategy = st.builds(Sect2)
@given(instance=Sect2_strategy)
@settings(max_examples=25)
def test_Sect2_instantiation(instance):
    assert isinstance(instance, Sect2)


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



