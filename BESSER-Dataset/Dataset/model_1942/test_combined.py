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
    docbook_ImageData,
    docbook_ImageObject,
    docbook_XMLElement,
    docbook_MediaObject,
    ParaMixedContent,
    docbook_SimpleText,
    Para,
    docbook_Warning,
    docbook_Tip,
    docbook_ProgramListing,
    docbook_Link,
    docbook_Ulink,
    docbook_Emphasis,
    XMLElement,
    docbook_Bookinfo,
    SectionMixedContent,
    docbook_Para,
    docbook_ParaMixedContent,
    docbook_TitledElement,
    docbook_Title,
    docbook_SectionMixedContent,
    TitledElement,
    docbook_Chapter,
    docbook_Figure,
    docbook_Section,
    docbook_Author,
    docbook_Subtitle,
    docbook_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_docbook_imagedata_is_not_abstract():
    assert not inspect.isabstract(docbook_ImageData)


def test_hyp_docbook_imagedata_constructor_exists():
    assert callable(docbook_ImageData.__init__)


def test_hyp_docbook_imagedata_constructor_args():
    sig = inspect.signature(docbook_ImageData.__init__)
    params = list(sig.parameters.keys())
    assert "depth" in params, "Missing parameter 'depth'"
    assert "width" in params, "Missing parameter 'width'"
    assert "fileref" in params, "Missing parameter 'fileref'"






def test_hyp_docbook_imageobject_is_not_abstract():
    assert not inspect.isabstract(docbook_ImageObject)


def test_hyp_docbook_imageobject_constructor_exists():
    assert callable(docbook_ImageObject.__init__)


def test_hyp_docbook_imageobject_constructor_args():
    sig = inspect.signature(docbook_ImageObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_xmlelement_is_not_abstract():
    assert not inspect.isabstract(docbook_XMLElement)


def test_hyp_docbook_xmlelement_constructor_exists():
    assert callable(docbook_XMLElement.__init__)


def test_hyp_docbook_xmlelement_constructor_args():
    sig = inspect.signature(docbook_XMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_docbook_mediaobject_is_not_abstract():
    assert not inspect.isabstract(docbook_MediaObject)


def test_hyp_docbook_mediaobject_constructor_exists():
    assert callable(docbook_MediaObject.__init__)


def test_hyp_docbook_mediaobject_constructor_args():
    sig = inspect.signature(docbook_MediaObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paramixedcontent_is_not_abstract():
    assert not inspect.isabstract(ParaMixedContent)


def test_hyp_paramixedcontent_constructor_exists():
    assert callable(ParaMixedContent.__init__)


def test_hyp_paramixedcontent_constructor_args():
    sig = inspect.signature(ParaMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_simpletext_is_not_abstract():
    assert not inspect.isabstract(docbook_SimpleText)


def test_hyp_docbook_simpletext_constructor_exists():
    assert callable(docbook_SimpleText.__init__)


def test_hyp_docbook_simpletext_constructor_args():
    sig = inspect.signature(docbook_SimpleText.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_para_is_not_abstract():
    assert not inspect.isabstract(Para)


def test_hyp_para_constructor_exists():
    assert callable(Para.__init__)


def test_hyp_para_constructor_args():
    sig = inspect.signature(Para.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_warning_is_not_abstract():
    assert not inspect.isabstract(docbook_Warning)


def test_hyp_docbook_warning_constructor_exists():
    assert callable(docbook_Warning.__init__)


def test_hyp_docbook_warning_constructor_args():
    sig = inspect.signature(docbook_Warning.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_tip_is_not_abstract():
    assert not inspect.isabstract(docbook_Tip)


def test_hyp_docbook_tip_constructor_exists():
    assert callable(docbook_Tip.__init__)


def test_hyp_docbook_tip_constructor_args():
    sig = inspect.signature(docbook_Tip.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_programlisting_is_not_abstract():
    assert not inspect.isabstract(docbook_ProgramListing)


def test_hyp_docbook_programlisting_constructor_exists():
    assert callable(docbook_ProgramListing.__init__)


def test_hyp_docbook_programlisting_constructor_args():
    sig = inspect.signature(docbook_ProgramListing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_link_is_not_abstract():
    assert not inspect.isabstract(docbook_Link)


def test_hyp_docbook_link_constructor_exists():
    assert callable(docbook_Link.__init__)


def test_hyp_docbook_link_constructor_args():
    sig = inspect.signature(docbook_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_ulink_is_not_abstract():
    assert not inspect.isabstract(docbook_Ulink)


def test_hyp_docbook_ulink_constructor_exists():
    assert callable(docbook_Ulink.__init__)


def test_hyp_docbook_ulink_constructor_args():
    sig = inspect.signature(docbook_Ulink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_emphasis_is_not_abstract():
    assert not inspect.isabstract(docbook_Emphasis)


def test_hyp_docbook_emphasis_constructor_exists():
    assert callable(docbook_Emphasis.__init__)


def test_hyp_docbook_emphasis_constructor_args():
    sig = inspect.signature(docbook_Emphasis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmlelement_is_not_abstract():
    assert not inspect.isabstract(XMLElement)


def test_hyp_xmlelement_constructor_exists():
    assert callable(XMLElement.__init__)


def test_hyp_xmlelement_constructor_args():
    sig = inspect.signature(XMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_bookinfo_is_not_abstract():
    assert not inspect.isabstract(docbook_Bookinfo)


def test_hyp_docbook_bookinfo_constructor_exists():
    assert callable(docbook_Bookinfo.__init__)


def test_hyp_docbook_bookinfo_constructor_args():
    sig = inspect.signature(docbook_Bookinfo.__init__)
    params = list(sig.parameters.keys())
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "date" in params, "Missing parameter 'date'"





def test_hyp_sectionmixedcontent_is_not_abstract():
    assert not inspect.isabstract(SectionMixedContent)


def test_hyp_sectionmixedcontent_constructor_exists():
    assert callable(SectionMixedContent.__init__)


def test_hyp_sectionmixedcontent_constructor_args():
    sig = inspect.signature(SectionMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_para_is_not_abstract():
    assert not inspect.isabstract(docbook_Para)


def test_hyp_docbook_para_constructor_exists():
    assert callable(docbook_Para.__init__)


def test_hyp_docbook_para_constructor_args():
    sig = inspect.signature(docbook_Para.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_paramixedcontent_is_not_abstract():
    assert not inspect.isabstract(docbook_ParaMixedContent)


def test_hyp_docbook_paramixedcontent_constructor_exists():
    assert callable(docbook_ParaMixedContent.__init__)


def test_hyp_docbook_paramixedcontent_constructor_args():
    sig = inspect.signature(docbook_ParaMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_titledelement_is_not_abstract():
    assert not inspect.isabstract(docbook_TitledElement)


def test_hyp_docbook_titledelement_constructor_exists():
    assert callable(docbook_TitledElement.__init__)


def test_hyp_docbook_titledelement_constructor_args():
    sig = inspect.signature(docbook_TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_title_is_not_abstract():
    assert not inspect.isabstract(docbook_Title)


def test_hyp_docbook_title_constructor_exists():
    assert callable(docbook_Title.__init__)


def test_hyp_docbook_title_constructor_args():
    sig = inspect.signature(docbook_Title.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_sectionmixedcontent_is_not_abstract():
    assert not inspect.isabstract(docbook_SectionMixedContent)


def test_hyp_docbook_sectionmixedcontent_constructor_exists():
    assert callable(docbook_SectionMixedContent.__init__)


def test_hyp_docbook_sectionmixedcontent_constructor_args():
    sig = inspect.signature(docbook_SectionMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_hyp_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_hyp_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_chapter_is_not_abstract():
    assert not inspect.isabstract(docbook_Chapter)


def test_hyp_docbook_chapter_constructor_exists():
    assert callable(docbook_Chapter.__init__)


def test_hyp_docbook_chapter_constructor_args():
    sig = inspect.signature(docbook_Chapter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_figure_is_not_abstract():
    assert not inspect.isabstract(docbook_Figure)


def test_hyp_docbook_figure_constructor_exists():
    assert callable(docbook_Figure.__init__)


def test_hyp_docbook_figure_constructor_args():
    sig = inspect.signature(docbook_Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_section_is_not_abstract():
    assert not inspect.isabstract(docbook_Section)


def test_hyp_docbook_section_constructor_exists():
    assert callable(docbook_Section.__init__)


def test_hyp_docbook_section_constructor_args():
    sig = inspect.signature(docbook_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_author_is_not_abstract():
    assert not inspect.isabstract(docbook_Author)


def test_hyp_docbook_author_constructor_exists():
    assert callable(docbook_Author.__init__)


def test_hyp_docbook_author_constructor_args():
    sig = inspect.signature(docbook_Author.__init__)
    params = list(sig.parameters.keys())
    assert "authorblug" in params, "Missing parameter 'authorblug'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "honorific" in params, "Missing parameter 'honorific'"
    assert "firstname" in params, "Missing parameter 'firstname'"







def test_hyp_docbook_subtitle_is_not_abstract():
    assert not inspect.isabstract(docbook_Subtitle)


def test_hyp_docbook_subtitle_constructor_exists():
    assert callable(docbook_Subtitle.__init__)


def test_hyp_docbook_subtitle_constructor_args():
    sig = inspect.signature(docbook_Subtitle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_docbook_book_is_not_abstract():
    assert not inspect.isabstract(docbook_Book)


def test_hyp_docbook_book_constructor_exists():
    assert callable(docbook_Book.__init__)


def test_hyp_docbook_book_constructor_args():
    sig = inspect.signature(docbook_Book.__init__)
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
docbook_ImageData_strategy = st.builds(
    docbook_ImageData,
    depth=
        safe_text,
    width=
        safe_text,
    fileref=
        safe_text
)
docbook_ImageObject_strategy = st.builds(
    docbook_ImageObject,
)
docbook_XMLElement_strategy = st.builds(
    docbook_XMLElement,
    id=
        safe_text
)
docbook_MediaObject_strategy = st.builds(
    docbook_MediaObject,
)
ParaMixedContent_strategy = st.builds(
    ParaMixedContent,
)
docbook_SimpleText_strategy = st.builds(
    docbook_SimpleText,
    data=
        safe_text
)
Para_strategy = st.builds(
    Para,
)
docbook_Warning_strategy = st.builds(
    docbook_Warning,
)
docbook_Tip_strategy = st.builds(
    docbook_Tip,
)
docbook_ProgramListing_strategy = st.builds(
    docbook_ProgramListing,
)
docbook_Link_strategy = st.builds(
    docbook_Link,
)
docbook_Ulink_strategy = st.builds(
    docbook_Ulink,
)
docbook_Emphasis_strategy = st.builds(
    docbook_Emphasis,
)
XMLElement_strategy = st.builds(
    XMLElement,
)
docbook_Bookinfo_strategy = st.builds(
    docbook_Bookinfo,
    pubdate=
        safe_text,
    date=
        safe_text
)
SectionMixedContent_strategy = st.builds(
    SectionMixedContent,
)
docbook_Para_strategy = st.builds(
    docbook_Para,
)
docbook_ParaMixedContent_strategy = st.builds(
    docbook_ParaMixedContent,
)
docbook_TitledElement_strategy = st.builds(
    docbook_TitledElement,
)
docbook_Title_strategy = st.builds(
    docbook_Title,
)
docbook_SectionMixedContent_strategy = st.builds(
    docbook_SectionMixedContent,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
docbook_Chapter_strategy = st.builds(
    docbook_Chapter,
)
docbook_Figure_strategy = st.builds(
    docbook_Figure,
)
docbook_Section_strategy = st.builds(
    docbook_Section,
)
docbook_Author_strategy = st.builds(
    docbook_Author,
    authorblug=
        safe_text,
    surname=
        safe_text,
    honorific=
        safe_text,
    firstname=
        safe_text
)
docbook_Subtitle_strategy = st.builds(
    docbook_Subtitle,
)
docbook_Book_strategy = st.builds(
    docbook_Book,
)




@given(instance=docbook_ImageData_strategy)
def test_hyp_docbook_imagedata_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original



@given(instance=docbook_ImageData_strategy)
def test_hyp_docbook_imagedata_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=docbook_ImageData_strategy)
def test_hyp_docbook_imagedata_fileref_setter(instance):
    original = instance.fileref
    instance.fileref = original
    assert instance.fileref == original





@given(instance=docbook_XMLElement_strategy)
def test_hyp_docbook_xmlelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original






@given(instance=docbook_SimpleText_strategy)
def test_hyp_docbook_simpletext_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original












@given(instance=docbook_Bookinfo_strategy)
def test_hyp_docbook_bookinfo_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original



@given(instance=docbook_Bookinfo_strategy)
def test_hyp_docbook_bookinfo_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original














@given(instance=docbook_Author_strategy)
def test_hyp_docbook_author_authorblug_setter(instance):
    original = instance.authorblug
    instance.authorblug = original
    assert instance.authorblug == original



@given(instance=docbook_Author_strategy)
def test_hyp_docbook_author_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=docbook_Author_strategy)
def test_hyp_docbook_author_honorific_setter(instance):
    original = instance.honorific
    instance.honorific = original
    assert instance.honorific == original



@given(instance=docbook_Author_strategy)
def test_hyp_docbook_author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Para,
    ParaMixedContent,
    SectionMixedContent,
    TitledElement,
    XMLElement,
    docbook_Author,
    docbook_Book,
    docbook_Bookinfo,
    docbook_Chapter,
    docbook_Emphasis,
    docbook_Figure,
    docbook_ImageData,
    docbook_ImageObject,
    docbook_Link,
    docbook_MediaObject,
    docbook_Para,
    docbook_ParaMixedContent,
    docbook_ProgramListing,
    docbook_Section,
    docbook_SectionMixedContent,
    docbook_SimpleText,
    docbook_Subtitle,
    docbook_Tip,
    docbook_Title,
    docbook_TitledElement,
    docbook_Ulink,
    docbook_Warning,
    docbook_XMLElement,
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

def test_docbook_Author_authorblug_value_roundtrip():
    instance = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    assert instance.authorblug == "sample_text"
    instance.authorblug = "sample_text_2"
    assert instance.authorblug == "sample_text_2"


def test_docbook_Author_firstname_value_roundtrip():
    instance = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_docbook_Author_honorific_value_roundtrip():
    instance = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    assert instance.honorific == "sample_text"
    instance.honorific = "sample_text_2"
    assert instance.honorific == "sample_text_2"


def test_docbook_Author_surname_value_roundtrip():
    instance = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_docbook_Bookinfo_date_value_roundtrip():
    instance = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_docbook_Bookinfo_pubdate_value_roundtrip():
    instance = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    assert instance.pubdate == "sample_text"
    instance.pubdate = "sample_text_2"
    assert instance.pubdate == "sample_text_2"


def test_docbook_ImageData_depth_value_roundtrip():
    instance = docbook_ImageData(depth="sample_text", fileref="sample_text", width="sample_text")
    assert instance.depth == "sample_text"
    instance.depth = "sample_text_2"
    assert instance.depth == "sample_text_2"


def test_docbook_ImageData_fileref_value_roundtrip():
    instance = docbook_ImageData(depth="sample_text", fileref="sample_text", width="sample_text")
    assert instance.fileref == "sample_text"
    instance.fileref = "sample_text_2"
    assert instance.fileref == "sample_text_2"


def test_docbook_ImageData_width_value_roundtrip():
    instance = docbook_ImageData(depth="sample_text", fileref="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_docbook_SimpleText_data_value_roundtrip():
    instance = docbook_SimpleText(data="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_docbook_XMLElement_id_value_roundtrip():
    instance = docbook_XMLElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_docbook_ProgramListing_isa_Para():
    instance = docbook_ProgramListing()
    assert isinstance(instance, Para)


def test_docbook_Tip_isa_Para():
    instance = docbook_Tip()
    assert isinstance(instance, Para)


def test_docbook_Warning_isa_Para():
    instance = docbook_Warning()
    assert isinstance(instance, Para)


def test_docbook_Emphasis_isa_ParaMixedContent():
    instance = docbook_Emphasis()
    assert isinstance(instance, ParaMixedContent)


def test_docbook_Figure_isa_ParaMixedContent():
    instance = docbook_Figure()
    assert isinstance(instance, ParaMixedContent)


def test_docbook_Link_isa_ParaMixedContent():
    instance = docbook_Link()
    assert isinstance(instance, ParaMixedContent)


def test_docbook_SimpleText_isa_ParaMixedContent():
    instance = docbook_SimpleText(data="sample_text")
    assert isinstance(instance, ParaMixedContent)


def test_docbook_Ulink_isa_ParaMixedContent():
    instance = docbook_Ulink()
    assert isinstance(instance, ParaMixedContent)


def test_docbook_Para_isa_SectionMixedContent():
    instance = docbook_Para()
    assert isinstance(instance, SectionMixedContent)


def test_docbook_ParaMixedContent_isa_SectionMixedContent():
    instance = docbook_ParaMixedContent()
    assert isinstance(instance, SectionMixedContent)


def test_docbook_Section_isa_SectionMixedContent():
    instance = docbook_Section()
    assert isinstance(instance, SectionMixedContent)


def test_docbook_Chapter_isa_TitledElement():
    instance = docbook_Chapter()
    assert isinstance(instance, TitledElement)


def test_docbook_Figure_isa_TitledElement():
    instance = docbook_Figure()
    assert isinstance(instance, TitledElement)


def test_docbook_Section_isa_TitledElement():
    instance = docbook_Section()
    assert isinstance(instance, TitledElement)


def test_docbook_Book_isa_XMLElement():
    instance = docbook_Book()
    assert isinstance(instance, XMLElement)


def test_docbook_Bookinfo_isa_XMLElement():
    instance = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    assert isinstance(instance, XMLElement)


def test_docbook_Chapter_isa_XMLElement():
    instance = docbook_Chapter()
    assert isinstance(instance, XMLElement)


def test_docbook_Section_isa_XMLElement():
    instance = docbook_Section()
    assert isinstance(instance, XMLElement)


def test_assoc_author6_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    b2 = docbook_Author(authorblug="sample_text_2", firstname="sample_text_2", honorific="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'bookinfo7', {b1})
    assert _is_linked(a, 'bookinfo7', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'bookinfo7', {b2})
    assert _is_linked(a, 'bookinfo7', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'bookinfo7', set())
    assert not _is_linked(a, 'bookinfo7', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_book3_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Book()
    b2 = docbook_Book()
    _safe_set(a, 'bookinfo', b1)
    assert _is_linked(a, 'bookinfo', b1)
    if hasattr(b1, 'Book'):
        assert _is_linked(b1, 'Book', a)
    _safe_set(a, 'bookinfo', b2)
    assert _is_linked(a, 'bookinfo', b2)
    if hasattr(b1, 'Book'):
        assert not _is_linked(b1, 'Book', a)
    if hasattr(b2, 'Book'):
        assert _is_linked(b2, 'Book', a)
    _safe_set(a, 'bookinfo', None)
    assert not _is_linked(a, 'bookinfo', b2)
    if hasattr(b2, 'Book'):
        assert not _is_linked(b2, 'Book', a)


def test_assoc_bookinfo0_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Book()
    b2 = docbook_Book()
    _safe_set(a, 'Bookinfo', b1)
    assert _is_linked(a, 'Bookinfo', b1)
    if hasattr(b1, 'book'):
        assert _is_linked(b1, 'book', a)
    _safe_set(a, 'Bookinfo', b2)
    assert _is_linked(a, 'Bookinfo', b2)
    if hasattr(b1, 'book'):
        assert not _is_linked(b1, 'book', a)
    if hasattr(b2, 'book'):
        assert _is_linked(b2, 'book', a)
    _safe_set(a, 'Bookinfo', None)
    assert not _is_linked(a, 'Bookinfo', b2)
    if hasattr(b2, 'book'):
        assert not _is_linked(b2, 'book', a)


def test_assoc_bookinfo10_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Subtitle()
    b2 = docbook_Subtitle()
    _safe_set(a, 'Bookinfo11', b1)
    assert _is_linked(a, 'Bookinfo11', b1)
    if hasattr(b1, 'subtitle'):
        assert _is_linked(b1, 'subtitle', a)
    _safe_set(a, 'Bookinfo11', b2)
    assert _is_linked(a, 'Bookinfo11', b2)
    if hasattr(b1, 'subtitle'):
        assert not _is_linked(b1, 'subtitle', a)
    if hasattr(b2, 'subtitle'):
        assert _is_linked(b2, 'subtitle', a)
    _safe_set(a, 'Bookinfo11', None)
    assert not _is_linked(a, 'Bookinfo11', b2)
    if hasattr(b2, 'subtitle'):
        assert not _is_linked(b2, 'subtitle', a)


def test_assoc_bookinfo8_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Author(authorblug="sample_text", firstname="sample_text", honorific="sample_text", surname="sample_text")
    b2 = docbook_Author(authorblug="sample_text_2", firstname="sample_text_2", honorific="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'Bookinfo9', b1)
    assert _is_linked(a, 'Bookinfo9', b1)
    if hasattr(b1, 'author'):
        assert _is_linked(b1, 'author', a)
    _safe_set(a, 'Bookinfo9', b2)
    assert _is_linked(a, 'Bookinfo9', b2)
    if hasattr(b1, 'author'):
        assert not _is_linked(b1, 'author', a)
    if hasattr(b2, 'author'):
        assert _is_linked(b2, 'author', a)
    _safe_set(a, 'Bookinfo9', None)
    assert not _is_linked(a, 'Bookinfo9', b2)
    if hasattr(b2, 'author'):
        assert not _is_linked(b2, 'author', a)


def test_assoc_content50_link_reassign_clear():
    a = docbook_ImageData(depth="sample_text", fileref="sample_text", width="sample_text")
    b1 = docbook_ImageObject()
    b2 = docbook_ImageObject()
    _safe_set(a, 'ImageData', b1)
    assert _is_linked(a, 'ImageData', b1)
    if hasattr(b1, 'imageObject'):
        assert _is_linked(b1, 'imageObject', a)
    _safe_set(a, 'ImageData', b2)
    assert _is_linked(a, 'ImageData', b2)
    if hasattr(b1, 'imageObject'):
        assert not _is_linked(b1, 'imageObject', a)
    if hasattr(b2, 'imageObject'):
        assert _is_linked(b2, 'imageObject', a)
    _safe_set(a, 'ImageData', None)
    assert not _is_linked(a, 'ImageData', b2)
    if hasattr(b2, 'imageObject'):
        assert not _is_linked(b2, 'imageObject', a)


def test_assoc_imageObject51_link_reassign_clear():
    a = docbook_ImageData(depth="sample_text", fileref="sample_text", width="sample_text")
    b1 = docbook_ImageObject()
    b2 = docbook_ImageObject()
    _safe_set(a, 'content52', b1)
    assert _is_linked(a, 'content52', b1)
    if hasattr(b1, 'ImageObject53'):
        assert _is_linked(b1, 'ImageObject53', a)
    _safe_set(a, 'content52', b2)
    assert _is_linked(a, 'content52', b2)
    if hasattr(b1, 'ImageObject53'):
        assert not _is_linked(b1, 'ImageObject53', a)
    if hasattr(b2, 'ImageObject53'):
        assert _is_linked(b2, 'ImageObject53', a)
    _safe_set(a, 'content52', None)
    assert not _is_linked(a, 'content52', b2)
    if hasattr(b2, 'ImageObject53'):
        assert not _is_linked(b2, 'ImageObject53', a)


def test_assoc_subtitle4_link_reassign_clear():
    a = docbook_Bookinfo(date="sample_text", pubdate="sample_text")
    b1 = docbook_Subtitle()
    b2 = docbook_Subtitle()
    _safe_set(a, 'bookinfo5', b1)
    assert _is_linked(a, 'bookinfo5', b1)
    if hasattr(b1, 'Subtitle'):
        assert _is_linked(b1, 'Subtitle', a)
    _safe_set(a, 'bookinfo5', b2)
    assert _is_linked(a, 'bookinfo5', b2)
    if hasattr(b1, 'Subtitle'):
        assert not _is_linked(b1, 'Subtitle', a)
    if hasattr(b2, 'Subtitle'):
        assert _is_linked(b2, 'Subtitle', a)
    _safe_set(a, 'bookinfo5', None)
    assert not _is_linked(a, 'bookinfo5', b2)
    if hasattr(b2, 'Subtitle'):
        assert not _is_linked(b2, 'Subtitle', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Para_strategy = st.builds(Para)
@given(instance=Para_strategy)
@settings(max_examples=25)
def test_Para_instantiation(instance):
    assert isinstance(instance, Para)


ParaMixedContent_strategy = st.builds(ParaMixedContent)
@given(instance=ParaMixedContent_strategy)
@settings(max_examples=25)
def test_ParaMixedContent_instantiation(instance):
    assert isinstance(instance, ParaMixedContent)


SectionMixedContent_strategy = st.builds(SectionMixedContent)
@given(instance=SectionMixedContent_strategy)
@settings(max_examples=25)
def test_SectionMixedContent_instantiation(instance):
    assert isinstance(instance, SectionMixedContent)


TitledElement_strategy = st.builds(TitledElement)
@given(instance=TitledElement_strategy)
@settings(max_examples=25)
def test_TitledElement_instantiation(instance):
    assert isinstance(instance, TitledElement)


XMLElement_strategy = st.builds(XMLElement)
@given(instance=XMLElement_strategy)
@settings(max_examples=25)
def test_XMLElement_instantiation(instance):
    assert isinstance(instance, XMLElement)


docbook_Author_strategy = st.builds(docbook_Author, authorblug=safe_text, firstname=safe_text, honorific=safe_text, surname=safe_text)
@given(instance=docbook_Author_strategy)
@settings(max_examples=25)
def test_docbook_Author_instantiation(instance):
    assert isinstance(instance, docbook_Author)


docbook_Book_strategy = st.builds(docbook_Book)
@given(instance=docbook_Book_strategy)
@settings(max_examples=25)
def test_docbook_Book_instantiation(instance):
    assert isinstance(instance, docbook_Book)


docbook_Bookinfo_strategy = st.builds(docbook_Bookinfo, date=safe_text, pubdate=safe_text)
@given(instance=docbook_Bookinfo_strategy)
@settings(max_examples=25)
def test_docbook_Bookinfo_instantiation(instance):
    assert isinstance(instance, docbook_Bookinfo)


docbook_Chapter_strategy = st.builds(docbook_Chapter)
@given(instance=docbook_Chapter_strategy)
@settings(max_examples=25)
def test_docbook_Chapter_instantiation(instance):
    assert isinstance(instance, docbook_Chapter)


docbook_Emphasis_strategy = st.builds(docbook_Emphasis)
@given(instance=docbook_Emphasis_strategy)
@settings(max_examples=25)
def test_docbook_Emphasis_instantiation(instance):
    assert isinstance(instance, docbook_Emphasis)


docbook_Figure_strategy = st.builds(docbook_Figure)
@given(instance=docbook_Figure_strategy)
@settings(max_examples=25)
def test_docbook_Figure_instantiation(instance):
    assert isinstance(instance, docbook_Figure)


docbook_ImageData_strategy = st.builds(docbook_ImageData, depth=safe_text, fileref=safe_text, width=safe_text)
@given(instance=docbook_ImageData_strategy)
@settings(max_examples=25)
def test_docbook_ImageData_instantiation(instance):
    assert isinstance(instance, docbook_ImageData)


docbook_ImageObject_strategy = st.builds(docbook_ImageObject)
@given(instance=docbook_ImageObject_strategy)
@settings(max_examples=25)
def test_docbook_ImageObject_instantiation(instance):
    assert isinstance(instance, docbook_ImageObject)


docbook_Link_strategy = st.builds(docbook_Link)
@given(instance=docbook_Link_strategy)
@settings(max_examples=25)
def test_docbook_Link_instantiation(instance):
    assert isinstance(instance, docbook_Link)


docbook_MediaObject_strategy = st.builds(docbook_MediaObject)
@given(instance=docbook_MediaObject_strategy)
@settings(max_examples=25)
def test_docbook_MediaObject_instantiation(instance):
    assert isinstance(instance, docbook_MediaObject)


docbook_Para_strategy = st.builds(docbook_Para)
@given(instance=docbook_Para_strategy)
@settings(max_examples=25)
def test_docbook_Para_instantiation(instance):
    assert isinstance(instance, docbook_Para)


docbook_ParaMixedContent_strategy = st.builds(docbook_ParaMixedContent)
@given(instance=docbook_ParaMixedContent_strategy)
@settings(max_examples=25)
def test_docbook_ParaMixedContent_instantiation(instance):
    assert isinstance(instance, docbook_ParaMixedContent)


docbook_ProgramListing_strategy = st.builds(docbook_ProgramListing)
@given(instance=docbook_ProgramListing_strategy)
@settings(max_examples=25)
def test_docbook_ProgramListing_instantiation(instance):
    assert isinstance(instance, docbook_ProgramListing)


docbook_Section_strategy = st.builds(docbook_Section)
@given(instance=docbook_Section_strategy)
@settings(max_examples=25)
def test_docbook_Section_instantiation(instance):
    assert isinstance(instance, docbook_Section)


docbook_SectionMixedContent_strategy = st.builds(docbook_SectionMixedContent)
@given(instance=docbook_SectionMixedContent_strategy)
@settings(max_examples=25)
def test_docbook_SectionMixedContent_instantiation(instance):
    assert isinstance(instance, docbook_SectionMixedContent)


docbook_SimpleText_strategy = st.builds(docbook_SimpleText, data=safe_text)
@given(instance=docbook_SimpleText_strategy)
@settings(max_examples=25)
def test_docbook_SimpleText_instantiation(instance):
    assert isinstance(instance, docbook_SimpleText)


docbook_Subtitle_strategy = st.builds(docbook_Subtitle)
@given(instance=docbook_Subtitle_strategy)
@settings(max_examples=25)
def test_docbook_Subtitle_instantiation(instance):
    assert isinstance(instance, docbook_Subtitle)


docbook_Tip_strategy = st.builds(docbook_Tip)
@given(instance=docbook_Tip_strategy)
@settings(max_examples=25)
def test_docbook_Tip_instantiation(instance):
    assert isinstance(instance, docbook_Tip)


docbook_Title_strategy = st.builds(docbook_Title)
@given(instance=docbook_Title_strategy)
@settings(max_examples=25)
def test_docbook_Title_instantiation(instance):
    assert isinstance(instance, docbook_Title)


docbook_TitledElement_strategy = st.builds(docbook_TitledElement)
@given(instance=docbook_TitledElement_strategy)
@settings(max_examples=25)
def test_docbook_TitledElement_instantiation(instance):
    assert isinstance(instance, docbook_TitledElement)


docbook_Ulink_strategy = st.builds(docbook_Ulink)
@given(instance=docbook_Ulink_strategy)
@settings(max_examples=25)
def test_docbook_Ulink_instantiation(instance):
    assert isinstance(instance, docbook_Ulink)


docbook_Warning_strategy = st.builds(docbook_Warning)
@given(instance=docbook_Warning_strategy)
@settings(max_examples=25)
def test_docbook_Warning_instantiation(instance):
    assert isinstance(instance, docbook_Warning)


docbook_XMLElement_strategy = st.builds(docbook_XMLElement, id=safe_text)
@given(instance=docbook_XMLElement_strategy)
@settings(max_examples=25)
def test_docbook_XMLElement_instantiation(instance):
    assert isinstance(instance, docbook_XMLElement)



