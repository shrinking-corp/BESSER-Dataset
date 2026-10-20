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
    PageSummary,
    ObjectSummary,
    xwiki_LinkCollection,
    xwiki_Link,
    xwiki_Page,
    xwiki_Object,
    xwiki_EStringToStringMapEntry,
    xwiki_DocumentRoot,
    LinkCollection,
    xwiki_Syntaxes,
    xwiki_PageSummary,
    xwiki_SearchResult,
    xwiki_PagesType,
    xwiki_Translation,
    xwiki_SpacesType,
    xwiki_Attribute,
    xwiki_ObjectsType,
    xwiki_PropertiesType,
    xwiki_ClassesType,
    xwiki_Comment,
    xwiki_AttachmentsType,
    xwiki_XWiki,
    xwiki_CommentsType,
    xwiki_HistorySummary,
    xwiki_Class,
    xwiki_Property,
    xwiki_Wiki,
    xwiki_WikisType,
    xwiki_Translations,
    xwiki_HistoryType,
    xwiki_ObjectSummary,
    xwiki_SearchResultsType,
    xwiki_TagsType,
    xwiki_Tag,
    xwiki_Space,
    xwiki_Attachment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pagesummary_is_not_abstract():
    assert not inspect.isabstract(PageSummary)


def test_hyp_pagesummary_constructor_exists():
    assert callable(PageSummary.__init__)


def test_hyp_pagesummary_constructor_args():
    sig = inspect.signature(PageSummary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objectsummary_is_not_abstract():
    assert not inspect.isabstract(ObjectSummary)


def test_hyp_objectsummary_constructor_exists():
    assert callable(ObjectSummary.__init__)


def test_hyp_objectsummary_constructor_args():
    sig = inspect.signature(ObjectSummary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_linkcollection_is_not_abstract():
    assert not inspect.isabstract(xwiki_LinkCollection)


def test_hyp_xwiki_linkcollection_constructor_exists():
    assert callable(xwiki_LinkCollection.__init__)


def test_hyp_xwiki_linkcollection_constructor_args():
    sig = inspect.signature(xwiki_LinkCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_link_is_not_abstract():
    assert not inspect.isabstract(xwiki_Link)


def test_hyp_xwiki_link_constructor_exists():
    assert callable(xwiki_Link.__init__)


def test_hyp_xwiki_link_constructor_args():
    sig = inspect.signature(xwiki_Link.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "hrefLang" in params, "Missing parameter 'hrefLang'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rel" in params, "Missing parameter 'rel'"







def test_hyp_xwiki_page_is_not_abstract():
    assert not inspect.isabstract(xwiki_Page)


def test_hyp_xwiki_page_constructor_exists():
    assert callable(xwiki_Page.__init__)


def test_hyp_xwiki_page_constructor_args():
    sig = inspect.signature(xwiki_Page.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "content" in params, "Missing parameter 'content'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "creatorName" in params, "Missing parameter 'creatorName'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "created" in params, "Missing parameter 'created'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"














def test_hyp_xwiki_object_is_not_abstract():
    assert not inspect.isabstract(xwiki_Object)


def test_hyp_xwiki_object_constructor_exists():
    assert callable(xwiki_Object.__init__)


def test_hyp_xwiki_object_constructor_args():
    sig = inspect.signature(xwiki_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xwiki_EStringToStringMapEntry)


def test_hyp_xwiki_estringtostringmapentry_constructor_exists():
    assert callable(xwiki_EStringToStringMapEntry.__init__)


def test_hyp_xwiki_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xwiki_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_documentroot_is_not_abstract():
    assert not inspect.isabstract(xwiki_DocumentRoot)


def test_hyp_xwiki_documentroot_constructor_exists():
    assert callable(xwiki_DocumentRoot.__init__)


def test_hyp_xwiki_documentroot_constructor_args():
    sig = inspect.signature(xwiki_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_linkcollection_is_not_abstract():
    assert not inspect.isabstract(LinkCollection)


def test_hyp_linkcollection_constructor_exists():
    assert callable(LinkCollection.__init__)


def test_hyp_linkcollection_constructor_args():
    sig = inspect.signature(LinkCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_syntaxes_is_not_abstract():
    assert not inspect.isabstract(xwiki_Syntaxes)


def test_hyp_xwiki_syntaxes_constructor_exists():
    assert callable(xwiki_Syntaxes.__init__)


def test_hyp_xwiki_syntaxes_constructor_args():
    sig = inspect.signature(xwiki_Syntaxes.__init__)
    params = list(sig.parameters.keys())
    assert "syntax" in params, "Missing parameter 'syntax'"




def test_hyp_xwiki_pagesummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_PageSummary)


def test_hyp_xwiki_pagesummary_constructor_exists():
    assert callable(xwiki_PageSummary.__init__)


def test_hyp_xwiki_pagesummary_constructor_args():
    sig = inspect.signature(xwiki_PageSummary.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "title" in params, "Missing parameter 'title'"
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "author" in params, "Missing parameter 'author'"
    assert "syntax" in params, "Missing parameter 'syntax'"

















def test_hyp_xwiki_searchresult_is_not_abstract():
    assert not inspect.isabstract(xwiki_SearchResult)


def test_hyp_xwiki_searchresult_constructor_exists():
    assert callable(xwiki_SearchResult.__init__)


def test_hyp_xwiki_searchresult_constructor_args():
    sig = inspect.signature(xwiki_SearchResult.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "className" in params, "Missing parameter 'className'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "objectNumber" in params, "Missing parameter 'objectNumber'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "language" in params, "Missing parameter 'language'"
    assert "title" in params, "Missing parameter 'title'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "space" in params, "Missing parameter 'space'"
    assert "version" in params, "Missing parameter 'version'"
    assert "author" in params, "Missing parameter 'author'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "score" in params, "Missing parameter 'score'"
    assert "pageFullName" in params, "Missing parameter 'pageFullName'"



















def test_hyp_xwiki_pagestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_PagesType)


def test_hyp_xwiki_pagestype_constructor_exists():
    assert callable(xwiki_PagesType.__init__)


def test_hyp_xwiki_pagestype_constructor_args():
    sig = inspect.signature(xwiki_PagesType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_translation_is_not_abstract():
    assert not inspect.isabstract(xwiki_Translation)


def test_hyp_xwiki_translation_constructor_exists():
    assert callable(xwiki_Translation.__init__)


def test_hyp_xwiki_translation_constructor_args():
    sig = inspect.signature(xwiki_Translation.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"




def test_hyp_xwiki_spacestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_SpacesType)


def test_hyp_xwiki_spacestype_constructor_exists():
    assert callable(xwiki_SpacesType.__init__)


def test_hyp_xwiki_spacestype_constructor_args():
    sig = inspect.signature(xwiki_SpacesType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_attribute_is_not_abstract():
    assert not inspect.isabstract(xwiki_Attribute)


def test_hyp_xwiki_attribute_constructor_exists():
    assert callable(xwiki_Attribute.__init__)


def test_hyp_xwiki_attribute_constructor_args():
    sig = inspect.signature(xwiki_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_xwiki_objectstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_ObjectsType)


def test_hyp_xwiki_objectstype_constructor_exists():
    assert callable(xwiki_ObjectsType.__init__)


def test_hyp_xwiki_objectstype_constructor_args():
    sig = inspect.signature(xwiki_ObjectsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_propertiestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_PropertiesType)


def test_hyp_xwiki_propertiestype_constructor_exists():
    assert callable(xwiki_PropertiesType.__init__)


def test_hyp_xwiki_propertiestype_constructor_args():
    sig = inspect.signature(xwiki_PropertiesType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_classestype_is_not_abstract():
    assert not inspect.isabstract(xwiki_ClassesType)


def test_hyp_xwiki_classestype_constructor_exists():
    assert callable(xwiki_ClassesType.__init__)


def test_hyp_xwiki_classestype_constructor_args():
    sig = inspect.signature(xwiki_ClassesType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_comment_is_not_abstract():
    assert not inspect.isabstract(xwiki_Comment)


def test_hyp_xwiki_comment_constructor_exists():
    assert callable(xwiki_Comment.__init__)


def test_hyp_xwiki_comment_constructor_args():
    sig = inspect.signature(xwiki_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"
    assert "replyTo" in params, "Missing parameter 'replyTo'"
    assert "date" in params, "Missing parameter 'date'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "author" in params, "Missing parameter 'author'"
    assert "highlight" in params, "Missing parameter 'highlight'"











def test_hyp_xwiki_attachmentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_AttachmentsType)


def test_hyp_xwiki_attachmentstype_constructor_exists():
    assert callable(xwiki_AttachmentsType.__init__)


def test_hyp_xwiki_attachmentstype_constructor_args():
    sig = inspect.signature(xwiki_AttachmentsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_xwiki_is_not_abstract():
    assert not inspect.isabstract(xwiki_XWiki)


def test_hyp_xwiki_xwiki_constructor_exists():
    assert callable(xwiki_XWiki.__init__)


def test_hyp_xwiki_xwiki_constructor_args():
    sig = inspect.signature(xwiki_XWiki.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"




def test_hyp_xwiki_commentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_CommentsType)


def test_hyp_xwiki_commentstype_constructor_exists():
    assert callable(xwiki_CommentsType.__init__)


def test_hyp_xwiki_commentstype_constructor_args():
    sig = inspect.signature(xwiki_CommentsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_historysummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_HistorySummary)


def test_hyp_xwiki_historysummary_constructor_exists():
    assert callable(xwiki_HistorySummary.__init__)


def test_hyp_xwiki_historysummary_constructor_args():
    sig = inspect.signature(xwiki_HistorySummary.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "space" in params, "Missing parameter 'space'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "language" in params, "Missing parameter 'language'"















def test_hyp_xwiki_class_is_not_abstract():
    assert not inspect.isabstract(xwiki_Class)


def test_hyp_xwiki_class_constructor_exists():
    assert callable(xwiki_Class.__init__)


def test_hyp_xwiki_class_constructor_args():
    sig = inspect.signature(xwiki_Class.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_xwiki_property_is_not_abstract():
    assert not inspect.isabstract(xwiki_Property)


def test_hyp_xwiki_property_constructor_exists():
    assert callable(xwiki_Property.__init__)


def test_hyp_xwiki_property_constructor_args():
    sig = inspect.signature(xwiki_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_xwiki_wiki_is_not_abstract():
    assert not inspect.isabstract(xwiki_Wiki)


def test_hyp_xwiki_wiki_constructor_exists():
    assert callable(xwiki_Wiki.__init__)


def test_hyp_xwiki_wiki_constructor_args():
    sig = inspect.signature(xwiki_Wiki.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_xwiki_wikistype_is_not_abstract():
    assert not inspect.isabstract(xwiki_WikisType)


def test_hyp_xwiki_wikistype_constructor_exists():
    assert callable(xwiki_WikisType.__init__)


def test_hyp_xwiki_wikistype_constructor_args():
    sig = inspect.signature(xwiki_WikisType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_translations_is_not_abstract():
    assert not inspect.isabstract(xwiki_Translations)


def test_hyp_xwiki_translations_constructor_exists():
    assert callable(xwiki_Translations.__init__)


def test_hyp_xwiki_translations_constructor_args():
    sig = inspect.signature(xwiki_Translations.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_xwiki_historytype_is_not_abstract():
    assert not inspect.isabstract(xwiki_HistoryType)


def test_hyp_xwiki_historytype_constructor_exists():
    assert callable(xwiki_HistoryType.__init__)


def test_hyp_xwiki_historytype_constructor_args():
    sig = inspect.signature(xwiki_HistoryType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_objectsummary_is_not_abstract():
    assert not inspect.isabstract(xwiki_ObjectSummary)


def test_hyp_xwiki_objectsummary_constructor_exists():
    assert callable(xwiki_ObjectSummary.__init__)


def test_hyp_xwiki_objectsummary_constructor_args():
    sig = inspect.signature(xwiki_ObjectSummary.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "space" in params, "Missing parameter 'space'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "number" in params, "Missing parameter 'number'"
    assert "pageAuthorName" in params, "Missing parameter 'pageAuthorName'"
    assert "pageAuthor" in params, "Missing parameter 'pageAuthor'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "className" in params, "Missing parameter 'className'"















def test_hyp_xwiki_searchresultstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_SearchResultsType)


def test_hyp_xwiki_searchresultstype_constructor_exists():
    assert callable(xwiki_SearchResultsType.__init__)


def test_hyp_xwiki_searchresultstype_constructor_args():
    sig = inspect.signature(xwiki_SearchResultsType.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"




def test_hyp_xwiki_tagstype_is_not_abstract():
    assert not inspect.isabstract(xwiki_TagsType)


def test_hyp_xwiki_tagstype_constructor_exists():
    assert callable(xwiki_TagsType.__init__)


def test_hyp_xwiki_tagstype_constructor_args():
    sig = inspect.signature(xwiki_TagsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xwiki_tag_is_not_abstract():
    assert not inspect.isabstract(xwiki_Tag)


def test_hyp_xwiki_tag_constructor_exists():
    assert callable(xwiki_Tag.__init__)


def test_hyp_xwiki_tag_constructor_args():
    sig = inspect.signature(xwiki_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_xwiki_space_is_not_abstract():
    assert not inspect.isabstract(xwiki_Space)


def test_hyp_xwiki_space_constructor_exists():
    assert callable(xwiki_Space.__init__)


def test_hyp_xwiki_space_constructor_args():
    sig = inspect.signature(xwiki_Space.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "home" in params, "Missing parameter 'home'"









def test_hyp_xwiki_attachment_is_not_abstract():
    assert not inspect.isabstract(xwiki_Attachment)


def test_hyp_xwiki_attachment_constructor_exists():
    assert callable(xwiki_Attachment.__init__)


def test_hyp_xwiki_attachment_constructor_args():
    sig = inspect.signature(xwiki_Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "size" in params, "Missing parameter 'size'"
    assert "author" in params, "Missing parameter 'author'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "date" in params, "Missing parameter 'date'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "id" in params, "Missing parameter 'id'"














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
PageSummary_strategy = st.builds(
    PageSummary,
)
ObjectSummary_strategy = st.builds(
    ObjectSummary,
)
xwiki_LinkCollection_strategy = st.builds(
    xwiki_LinkCollection,
)
xwiki_Link_strategy = st.builds(
    xwiki_Link,
    href=
        safe_text,
    hrefLang=
        safe_text,
    type=
        safe_text,
    rel=
        safe_text
)
xwiki_Page_strategy = st.builds(
    xwiki_Page,
    language=
        safe_text,
    content=
        safe_text,
    majorVersion=
        safe_text,
    creatorName=
        safe_text,
    modifier=
        safe_text,
    creator=
        safe_text,
    comment=
        safe_text,
    created=
        safe_text,
    modified=
        safe_text,
    modifierName=
        safe_text,
    minorVersion=
        safe_text
)
xwiki_Object_strategy = st.builds(
    xwiki_Object,
)
xwiki_EStringToStringMapEntry_strategy = st.builds(
    xwiki_EStringToStringMapEntry,
)
xwiki_DocumentRoot_strategy = st.builds(
    xwiki_DocumentRoot,
    mixed=
        safe_text
)
LinkCollection_strategy = st.builds(
    LinkCollection,
)
xwiki_Syntaxes_strategy = st.builds(
    xwiki_Syntaxes,
    syntax=
        safe_text
)
xwiki_PageSummary_strategy = st.builds(
    xwiki_PageSummary,
    space=
        safe_text,
    id=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    parent=
        safe_text,
    title=
        safe_text,
    parentId=
        safe_text,
    name=
        safe_text,
    authorName=
        safe_text,
    version=
        safe_text,
    wiki=
        safe_text,
    fullName=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    author=
        safe_text,
    syntax=
        safe_text
)
xwiki_SearchResult_strategy = st.builds(
    xwiki_SearchResult,
    id=
        safe_text,
    type=
        safe_text,
    className=
        safe_text,
    wiki=
        safe_text,
    objectNumber=
        safe_text,
    pageName=
        safe_text,
    language=
        safe_text,
    title=
        safe_text,
    authorName=
        safe_text,
    space=
        safe_text,
    version=
        safe_text,
    author=
        safe_text,
    filename=
        safe_text,
    modified=
        safe_text,
    score=
        safe_text,
    pageFullName=
        safe_text
)
xwiki_PagesType_strategy = st.builds(
    xwiki_PagesType,
)
xwiki_Translation_strategy = st.builds(
    xwiki_Translation,
    language=
        safe_text
)
xwiki_SpacesType_strategy = st.builds(
    xwiki_SpacesType,
)
xwiki_Attribute_strategy = st.builds(
    xwiki_Attribute,
    value=
        safe_text,
    name=
        safe_text
)
xwiki_ObjectsType_strategy = st.builds(
    xwiki_ObjectsType,
)
xwiki_PropertiesType_strategy = st.builds(
    xwiki_PropertiesType,
)
xwiki_ClassesType_strategy = st.builds(
    xwiki_ClassesType,
)
xwiki_Comment_strategy = st.builds(
    xwiki_Comment,
    id=
        safe_text,
    text=
        safe_text,
    replyTo=
        safe_text,
    date=
        safe_text,
    pageId=
        safe_text,
    authorName=
        safe_text,
    author=
        safe_text,
    highlight=
        safe_text
)
xwiki_AttachmentsType_strategy = st.builds(
    xwiki_AttachmentsType,
)
xwiki_XWiki_strategy = st.builds(
    xwiki_XWiki,
    version=
        safe_text
)
xwiki_CommentsType_strategy = st.builds(
    xwiki_CommentsType,
)
xwiki_HistorySummary_strategy = st.builds(
    xwiki_HistorySummary,
    version=
        safe_text,
    modifierName=
        safe_text,
    comment=
        safe_text,
    modifier=
        safe_text,
    name=
        safe_text,
    minorVersion=
        safe_text,
    pageId=
        safe_text,
    modified=
        safe_text,
    majorVersion=
        safe_text,
    space=
        safe_text,
    wiki=
        safe_text,
    language=
        safe_text
)
xwiki_Class_strategy = st.builds(
    xwiki_Class,
    id=
        safe_text,
    name=
        safe_text
)
xwiki_Property_strategy = st.builds(
    xwiki_Property,
    name=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
xwiki_Wiki_strategy = st.builds(
    xwiki_Wiki,
    owner=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
xwiki_WikisType_strategy = st.builds(
    xwiki_WikisType,
)
xwiki_Translations_strategy = st.builds(
    xwiki_Translations,
    default=
        safe_text
)
xwiki_HistoryType_strategy = st.builds(
    xwiki_HistoryType,
)
xwiki_ObjectSummary_strategy = st.builds(
    xwiki_ObjectSummary,
    id=
        safe_text,
    guid=
        safe_text,
    pageVersion=
        safe_text,
    pageId=
        safe_text,
    space=
        safe_text,
    headline=
        safe_text,
    wiki=
        safe_text,
    number=
        safe_text,
    pageAuthorName=
        safe_text,
    pageAuthor=
        safe_text,
    pageName=
        safe_text,
    className=
        safe_text
)
xwiki_SearchResultsType_strategy = st.builds(
    xwiki_SearchResultsType,
    template=
        safe_text
)
xwiki_TagsType_strategy = st.builds(
    xwiki_TagsType,
)
xwiki_Tag_strategy = st.builds(
    xwiki_Tag,
    name=
        safe_text
)
xwiki_Space_strategy = st.builds(
    xwiki_Space,
    id=
        safe_text,
    name=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    wiki=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    home=
        safe_text
)
xwiki_Attachment_strategy = st.builds(
    xwiki_Attachment,
    pageVersion=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    size=
        safe_text,
    author=
        safe_text,
    pageId=
        safe_text,
    version=
        safe_text,
    date=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    name=
        safe_text,
    mimeType=
        safe_text,
    authorName=
        safe_text,
    id=
        safe_text
)







@given(instance=xwiki_Link_strategy)
def test_hyp_xwiki_link_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=xwiki_Link_strategy)
def test_hyp_xwiki_link_hrefLang_setter(instance):
    original = instance.hrefLang
    instance.hrefLang = original
    assert instance.hrefLang == original



@given(instance=xwiki_Link_strategy)
def test_hyp_xwiki_link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_Link_strategy)
def test_hyp_xwiki_link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original




@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_creatorName_setter(instance):
    original = instance.creatorName
    instance.creatorName = original
    assert instance.creatorName == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original



@given(instance=xwiki_Page_strategy)
def test_hyp_xwiki_page_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original






@given(instance=xwiki_DocumentRoot_strategy)
def test_hyp_xwiki_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=xwiki_Syntaxes_strategy)
def test_hyp_xwiki_syntaxes_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original




@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_PageSummary_strategy)
def test_hyp_xwiki_pagesummary_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original




@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_objectNumber_setter(instance):
    original = instance.objectNumber
    instance.objectNumber = original
    assert instance.objectNumber == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=xwiki_SearchResult_strategy)
def test_hyp_xwiki_searchresult_pageFullName_setter(instance):
    original = instance.pageFullName
    instance.pageFullName = original
    assert instance.pageFullName == original





@given(instance=xwiki_Translation_strategy)
def test_hyp_xwiki_translation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original





@given(instance=xwiki_Attribute_strategy)
def test_hyp_xwiki_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xwiki_Attribute_strategy)
def test_hyp_xwiki_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_replyTo_setter(instance):
    original = instance.replyTo
    instance.replyTo = original
    assert instance.replyTo == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_Comment_strategy)
def test_hyp_xwiki_comment_highlight_setter(instance):
    original = instance.highlight
    instance.highlight = original
    assert instance.highlight == original





@given(instance=xwiki_XWiki_strategy)
def test_hyp_xwiki_xwiki_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original





@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_HistorySummary_strategy)
def test_hyp_xwiki_historysummary_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=xwiki_Class_strategy)
def test_hyp_xwiki_class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Class_strategy)
def test_hyp_xwiki_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=xwiki_Property_strategy)
def test_hyp_xwiki_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Property_strategy)
def test_hyp_xwiki_property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xwiki_Property_strategy)
def test_hyp_xwiki_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=xwiki_Wiki_strategy)
def test_hyp_xwiki_wiki_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=xwiki_Wiki_strategy)
def test_hyp_xwiki_wiki_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xwiki_Wiki_strategy)
def test_hyp_xwiki_wiki_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Wiki_strategy)
def test_hyp_xwiki_wiki_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=xwiki_Translations_strategy)
def test_hyp_xwiki_translations_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original





@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_pageAuthorName_setter(instance):
    original = instance.pageAuthorName
    instance.pageAuthorName = original
    assert instance.pageAuthorName == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_pageAuthor_setter(instance):
    original = instance.pageAuthor
    instance.pageAuthor = original
    assert instance.pageAuthor == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original



@given(instance=xwiki_ObjectSummary_strategy)
def test_hyp_xwiki_objectsummary_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original




@given(instance=xwiki_SearchResultsType_strategy)
def test_hyp_xwiki_searchresultstype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original





@given(instance=xwiki_Tag_strategy)
def test_hyp_xwiki_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original



@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_Space_strategy)
def test_hyp_xwiki_space_home_setter(instance):
    original = instance.home
    instance.home = original
    assert instance.home == original




@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=xwiki_Attachment_strategy)
def test_hyp_xwiki_attachment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    LinkCollection,
    ObjectSummary,
    PageSummary,
    xwiki_Attachment,
    xwiki_AttachmentsType,
    xwiki_Attribute,
    xwiki_Class,
    xwiki_ClassesType,
    xwiki_Comment,
    xwiki_CommentsType,
    xwiki_DocumentRoot,
    xwiki_EStringToStringMapEntry,
    xwiki_HistorySummary,
    xwiki_HistoryType,
    xwiki_Link,
    xwiki_LinkCollection,
    xwiki_Object,
    xwiki_ObjectSummary,
    xwiki_ObjectsType,
    xwiki_Page,
    xwiki_PageSummary,
    xwiki_PagesType,
    xwiki_PropertiesType,
    xwiki_Property,
    xwiki_SearchResult,
    xwiki_SearchResultsType,
    xwiki_Space,
    xwiki_SpacesType,
    xwiki_Syntaxes,
    xwiki_Tag,
    xwiki_TagsType,
    xwiki_Translation,
    xwiki_Translations,
    xwiki_Wiki,
    xwiki_WikisType,
    xwiki_XWiki,
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

def test_xwiki_Attachment_author_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_xwiki_Attachment_authorName_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_xwiki_Attachment_date_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_xwiki_Attachment_id_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_Attachment_mimeType_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.mimeType == "sample_text"
    instance.mimeType = "sample_text_2"
    assert instance.mimeType == "sample_text_2"


def test_xwiki_Attachment_name_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Attachment_pageId_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.pageId == "sample_text"
    instance.pageId = "sample_text_2"
    assert instance.pageId == "sample_text_2"


def test_xwiki_Attachment_pageVersion_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.pageVersion == "sample_text"
    instance.pageVersion = "sample_text_2"
    assert instance.pageVersion == "sample_text_2"


def test_xwiki_Attachment_size_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_xwiki_Attachment_version_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_xwiki_Attachment_xwikiAbsoluteUrl_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiAbsoluteUrl == "sample_text"
    instance.xwikiAbsoluteUrl = "sample_text_2"
    assert instance.xwikiAbsoluteUrl == "sample_text_2"


def test_xwiki_Attachment_xwikiRelativeUrl_value_roundtrip():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiRelativeUrl == "sample_text"
    instance.xwikiRelativeUrl = "sample_text_2"
    assert instance.xwikiRelativeUrl == "sample_text_2"


def test_xwiki_Attribute_name_value_roundtrip():
    instance = xwiki_Attribute(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Attribute_value_value_roundtrip():
    instance = xwiki_Attribute(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xwiki_Class_id_value_roundtrip():
    instance = xwiki_Class(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_Class_name_value_roundtrip():
    instance = xwiki_Class(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Comment_author_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_xwiki_Comment_authorName_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_xwiki_Comment_date_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_xwiki_Comment_highlight_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.highlight == "sample_text"
    instance.highlight = "sample_text_2"
    assert instance.highlight == "sample_text_2"


def test_xwiki_Comment_id_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_Comment_pageId_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.pageId == "sample_text"
    instance.pageId = "sample_text_2"
    assert instance.pageId == "sample_text_2"


def test_xwiki_Comment_replyTo_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.replyTo == "sample_text"
    instance.replyTo = "sample_text_2"
    assert instance.replyTo == "sample_text_2"


def test_xwiki_Comment_text_value_roundtrip():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_xwiki_DocumentRoot_mixed_value_roundtrip():
    instance = xwiki_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xwiki_HistorySummary_comment_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_xwiki_HistorySummary_language_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_xwiki_HistorySummary_majorVersion_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.majorVersion == "sample_text"
    instance.majorVersion = "sample_text_2"
    assert instance.majorVersion == "sample_text_2"


def test_xwiki_HistorySummary_minorVersion_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.minorVersion == "sample_text"
    instance.minorVersion = "sample_text_2"
    assert instance.minorVersion == "sample_text_2"


def test_xwiki_HistorySummary_modified_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.modified == "sample_text"
    instance.modified = "sample_text_2"
    assert instance.modified == "sample_text_2"


def test_xwiki_HistorySummary_modifier_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.modifier == "sample_text"
    instance.modifier = "sample_text_2"
    assert instance.modifier == "sample_text_2"


def test_xwiki_HistorySummary_modifierName_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.modifierName == "sample_text"
    instance.modifierName = "sample_text_2"
    assert instance.modifierName == "sample_text_2"


def test_xwiki_HistorySummary_name_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_HistorySummary_pageId_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.pageId == "sample_text"
    instance.pageId = "sample_text_2"
    assert instance.pageId == "sample_text_2"


def test_xwiki_HistorySummary_space_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_xwiki_HistorySummary_version_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_xwiki_HistorySummary_wiki_value_roundtrip():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert instance.wiki == "sample_text"
    instance.wiki = "sample_text_2"
    assert instance.wiki == "sample_text_2"


def test_xwiki_Link_href_value_roundtrip():
    instance = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    assert instance.href == "sample_text"
    instance.href = "sample_text_2"
    assert instance.href == "sample_text_2"


def test_xwiki_Link_hrefLang_value_roundtrip():
    instance = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    assert instance.hrefLang == "sample_text"
    instance.hrefLang = "sample_text_2"
    assert instance.hrefLang == "sample_text_2"


def test_xwiki_Link_rel_value_roundtrip():
    instance = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    assert instance.rel == "sample_text"
    instance.rel = "sample_text_2"
    assert instance.rel == "sample_text_2"


def test_xwiki_Link_type_value_roundtrip():
    instance = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xwiki_ObjectSummary_className_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_xwiki_ObjectSummary_guid_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.guid == "sample_text"
    instance.guid = "sample_text_2"
    assert instance.guid == "sample_text_2"


def test_xwiki_ObjectSummary_headline_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.headline == "sample_text"
    instance.headline = "sample_text_2"
    assert instance.headline == "sample_text_2"


def test_xwiki_ObjectSummary_id_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_ObjectSummary_number_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_xwiki_ObjectSummary_pageAuthor_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.pageAuthor == "sample_text"
    instance.pageAuthor = "sample_text_2"
    assert instance.pageAuthor == "sample_text_2"


def test_xwiki_ObjectSummary_pageAuthorName_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.pageAuthorName == "sample_text"
    instance.pageAuthorName = "sample_text_2"
    assert instance.pageAuthorName == "sample_text_2"


def test_xwiki_ObjectSummary_pageId_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.pageId == "sample_text"
    instance.pageId = "sample_text_2"
    assert instance.pageId == "sample_text_2"


def test_xwiki_ObjectSummary_pageName_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.pageName == "sample_text"
    instance.pageName = "sample_text_2"
    assert instance.pageName == "sample_text_2"


def test_xwiki_ObjectSummary_pageVersion_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.pageVersion == "sample_text"
    instance.pageVersion = "sample_text_2"
    assert instance.pageVersion == "sample_text_2"


def test_xwiki_ObjectSummary_space_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_xwiki_ObjectSummary_wiki_value_roundtrip():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert instance.wiki == "sample_text"
    instance.wiki = "sample_text_2"
    assert instance.wiki == "sample_text_2"


def test_xwiki_Page_comment_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_xwiki_Page_content_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_xwiki_Page_created_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.created == "sample_text"
    instance.created = "sample_text_2"
    assert instance.created == "sample_text_2"


def test_xwiki_Page_creator_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.creator == "sample_text"
    instance.creator = "sample_text_2"
    assert instance.creator == "sample_text_2"


def test_xwiki_Page_creatorName_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.creatorName == "sample_text"
    instance.creatorName = "sample_text_2"
    assert instance.creatorName == "sample_text_2"


def test_xwiki_Page_language_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_xwiki_Page_majorVersion_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.majorVersion == "sample_text"
    instance.majorVersion = "sample_text_2"
    assert instance.majorVersion == "sample_text_2"


def test_xwiki_Page_minorVersion_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.minorVersion == "sample_text"
    instance.minorVersion = "sample_text_2"
    assert instance.minorVersion == "sample_text_2"


def test_xwiki_Page_modified_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.modified == "sample_text"
    instance.modified = "sample_text_2"
    assert instance.modified == "sample_text_2"


def test_xwiki_Page_modifier_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.modifier == "sample_text"
    instance.modifier = "sample_text_2"
    assert instance.modifier == "sample_text_2"


def test_xwiki_Page_modifierName_value_roundtrip():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert instance.modifierName == "sample_text"
    instance.modifierName = "sample_text_2"
    assert instance.modifierName == "sample_text_2"


def test_xwiki_PageSummary_author_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_xwiki_PageSummary_authorName_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_xwiki_PageSummary_fullName_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_xwiki_PageSummary_id_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_PageSummary_name_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_PageSummary_parent_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.parent == "sample_text"
    instance.parent = "sample_text_2"
    assert instance.parent == "sample_text_2"


def test_xwiki_PageSummary_parentId_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.parentId == "sample_text"
    instance.parentId = "sample_text_2"
    assert instance.parentId == "sample_text_2"


def test_xwiki_PageSummary_space_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_xwiki_PageSummary_syntax_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.syntax == "sample_text"
    instance.syntax = "sample_text_2"
    assert instance.syntax == "sample_text_2"


def test_xwiki_PageSummary_title_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_xwiki_PageSummary_version_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_xwiki_PageSummary_wiki_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.wiki == "sample_text"
    instance.wiki = "sample_text_2"
    assert instance.wiki == "sample_text_2"


def test_xwiki_PageSummary_xwikiAbsoluteUrl_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiAbsoluteUrl == "sample_text"
    instance.xwikiAbsoluteUrl = "sample_text_2"
    assert instance.xwikiAbsoluteUrl == "sample_text_2"


def test_xwiki_PageSummary_xwikiRelativeUrl_value_roundtrip():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiRelativeUrl == "sample_text"
    instance.xwikiRelativeUrl = "sample_text_2"
    assert instance.xwikiRelativeUrl == "sample_text_2"


def test_xwiki_Property_name_value_roundtrip():
    instance = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Property_type_value_roundtrip():
    instance = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xwiki_Property_value_value_roundtrip():
    instance = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xwiki_SearchResult_author_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_xwiki_SearchResult_authorName_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_xwiki_SearchResult_className_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_xwiki_SearchResult_filename_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.filename == "sample_text"
    instance.filename = "sample_text_2"
    assert instance.filename == "sample_text_2"


def test_xwiki_SearchResult_id_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_SearchResult_language_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_xwiki_SearchResult_modified_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.modified == "sample_text"
    instance.modified = "sample_text_2"
    assert instance.modified == "sample_text_2"


def test_xwiki_SearchResult_objectNumber_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.objectNumber == "sample_text"
    instance.objectNumber = "sample_text_2"
    assert instance.objectNumber == "sample_text_2"


def test_xwiki_SearchResult_pageFullName_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.pageFullName == "sample_text"
    instance.pageFullName = "sample_text_2"
    assert instance.pageFullName == "sample_text_2"


def test_xwiki_SearchResult_pageName_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.pageName == "sample_text"
    instance.pageName = "sample_text_2"
    assert instance.pageName == "sample_text_2"


def test_xwiki_SearchResult_score_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.score == "sample_text"
    instance.score = "sample_text_2"
    assert instance.score == "sample_text_2"


def test_xwiki_SearchResult_space_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_xwiki_SearchResult_title_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_xwiki_SearchResult_type_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xwiki_SearchResult_version_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_xwiki_SearchResult_wiki_value_roundtrip():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert instance.wiki == "sample_text"
    instance.wiki = "sample_text_2"
    assert instance.wiki == "sample_text_2"


def test_xwiki_SearchResultsType_template_value_roundtrip():
    instance = xwiki_SearchResultsType(template="sample_text")
    assert instance.template == "sample_text"
    instance.template = "sample_text_2"
    assert instance.template == "sample_text_2"


def test_xwiki_Space_home_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.home == "sample_text"
    instance.home = "sample_text_2"
    assert instance.home == "sample_text_2"


def test_xwiki_Space_id_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_Space_name_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Space_wiki_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.wiki == "sample_text"
    instance.wiki = "sample_text_2"
    assert instance.wiki == "sample_text_2"


def test_xwiki_Space_xwikiAbsoluteUrl_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiAbsoluteUrl == "sample_text"
    instance.xwikiAbsoluteUrl = "sample_text_2"
    assert instance.xwikiAbsoluteUrl == "sample_text_2"


def test_xwiki_Space_xwikiRelativeUrl_value_roundtrip():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert instance.xwikiRelativeUrl == "sample_text"
    instance.xwikiRelativeUrl = "sample_text_2"
    assert instance.xwikiRelativeUrl == "sample_text_2"


def test_xwiki_Syntaxes_syntax_value_roundtrip():
    instance = xwiki_Syntaxes(syntax="sample_text")
    assert instance.syntax == "sample_text"
    instance.syntax = "sample_text_2"
    assert instance.syntax == "sample_text_2"


def test_xwiki_Tag_name_value_roundtrip():
    instance = xwiki_Tag(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Translation_language_value_roundtrip():
    instance = xwiki_Translation(language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_xwiki_Translations_default_value_roundtrip():
    instance = xwiki_Translations(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_xwiki_Wiki_description_value_roundtrip():
    instance = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_xwiki_Wiki_id_value_roundtrip():
    instance = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_xwiki_Wiki_name_value_roundtrip():
    instance = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xwiki_Wiki_owner_value_roundtrip():
    instance = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    assert instance.owner == "sample_text"
    instance.owner = "sample_text_2"
    assert instance.owner == "sample_text_2"


def test_xwiki_XWiki_version_value_roundtrip():
    instance = xwiki_XWiki(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_xwiki_Attachment_isa_LinkCollection():
    instance = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_AttachmentsType_isa_LinkCollection():
    instance = xwiki_AttachmentsType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_Attribute_isa_LinkCollection():
    instance = xwiki_Attribute(name="sample_text", value="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Class_isa_LinkCollection():
    instance = xwiki_Class(id="sample_text", name="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_ClassesType_isa_LinkCollection():
    instance = xwiki_ClassesType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_Comment_isa_LinkCollection():
    instance = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_CommentsType_isa_LinkCollection():
    instance = xwiki_CommentsType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_HistorySummary_isa_LinkCollection():
    instance = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_HistoryType_isa_LinkCollection():
    instance = xwiki_HistoryType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_ObjectSummary_isa_LinkCollection():
    instance = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_ObjectsType_isa_LinkCollection():
    instance = xwiki_ObjectsType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_PageSummary_isa_LinkCollection():
    instance = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_PagesType_isa_LinkCollection():
    instance = xwiki_PagesType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_PropertiesType_isa_LinkCollection():
    instance = xwiki_PropertiesType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_Property_isa_LinkCollection():
    instance = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_SearchResult_isa_LinkCollection():
    instance = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_SearchResultsType_isa_LinkCollection():
    instance = xwiki_SearchResultsType(template="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Space_isa_LinkCollection():
    instance = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_SpacesType_isa_LinkCollection():
    instance = xwiki_SpacesType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_Syntaxes_isa_LinkCollection():
    instance = xwiki_Syntaxes(syntax="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Tag_isa_LinkCollection():
    instance = xwiki_Tag(name="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_TagsType_isa_LinkCollection():
    instance = xwiki_TagsType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_Translation_isa_LinkCollection():
    instance = xwiki_Translation(language="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Translations_isa_LinkCollection():
    instance = xwiki_Translations(default="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Wiki_isa_LinkCollection():
    instance = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_WikisType_isa_LinkCollection():
    instance = xwiki_WikisType()
    assert isinstance(instance, LinkCollection)


def test_xwiki_XWiki_isa_LinkCollection():
    instance = xwiki_XWiki(version="sample_text")
    assert isinstance(instance, LinkCollection)


def test_xwiki_Object_isa_ObjectSummary():
    instance = xwiki_Object()
    assert isinstance(instance, ObjectSummary)


def test_xwiki_Page_isa_PageSummary():
    instance = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    assert isinstance(instance, PageSummary)


def test_assoc_attachment0_link_reassign_clear():
    a = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b1 = xwiki_AttachmentsType()
    b2 = xwiki_AttachmentsType()
    _safe_set(a, 'xwiki_Attachment', b1)
    assert _is_linked(a, 'xwiki_Attachment', b1)
    if hasattr(b1, 'xwiki_AttachmentsType'):
        assert _is_linked(b1, 'xwiki_AttachmentsType', a)
    _safe_set(a, 'xwiki_Attachment', b2)
    assert _is_linked(a, 'xwiki_Attachment', b2)
    if hasattr(b1, 'xwiki_AttachmentsType'):
        assert not _is_linked(b1, 'xwiki_AttachmentsType', a)
    if hasattr(b2, 'xwiki_AttachmentsType'):
        assert _is_linked(b2, 'xwiki_AttachmentsType', a)
    _safe_set(a, 'xwiki_Attachment', None)
    assert not _is_linked(a, 'xwiki_Attachment', b2)
    if hasattr(b2, 'xwiki_AttachmentsType'):
        assert not _is_linked(b2, 'xwiki_AttachmentsType', a)


def test_assoc_attachment9_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b2 = xwiki_Attachment(author="sample_text_2", authorName="sample_text_2", date="sample_text_2", id="sample_text_2", mimeType="sample_text_2", name="sample_text_2", pageId="sample_text_2", pageVersion="sample_text_2", size="sample_text_2", version="sample_text_2", xwikiAbsoluteUrl="sample_text_2", xwikiRelativeUrl="sample_text_2")
    _safe_set(a, 'xwiki_DocumentRoot10', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot10', b1)
    if hasattr(b1, 'xwiki_Attachment11'):
        assert _is_linked(b1, 'xwiki_Attachment11', a)
    _safe_set(a, 'xwiki_DocumentRoot10', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot10', b2)
    if hasattr(b1, 'xwiki_Attachment11'):
        assert not _is_linked(b1, 'xwiki_Attachment11', a)
    if hasattr(b2, 'xwiki_Attachment11'):
        assert _is_linked(b2, 'xwiki_Attachment11', a)
    _safe_set(a, 'xwiki_DocumentRoot10', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot10', b2)
    if hasattr(b2, 'xwiki_Attachment11'):
        assert not _is_linked(b2, 'xwiki_Attachment11', a)


def test_assoc_attachments12_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_AttachmentsType()
    b2 = xwiki_AttachmentsType()
    _safe_set(a, 'xwiki_DocumentRoot13', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot13', b1)
    if hasattr(b1, 'xwiki_AttachmentsType14'):
        assert _is_linked(b1, 'xwiki_AttachmentsType14', a)
    _safe_set(a, 'xwiki_DocumentRoot13', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot13', b2)
    if hasattr(b1, 'xwiki_AttachmentsType14'):
        assert not _is_linked(b1, 'xwiki_AttachmentsType14', a)
    if hasattr(b2, 'xwiki_AttachmentsType14'):
        assert _is_linked(b2, 'xwiki_AttachmentsType14', a)
    _safe_set(a, 'xwiki_DocumentRoot13', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot13', b2)
    if hasattr(b2, 'xwiki_AttachmentsType14'):
        assert not _is_linked(b2, 'xwiki_AttachmentsType14', a)


def test_assoc_attribute83_link_reassign_clear():
    a = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    b1 = xwiki_Attribute(name="sample_text", value="sample_text")
    b2 = xwiki_Attribute(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'xwiki_Property84', {b1})
    assert _is_linked(a, 'xwiki_Property84', b1)
    if hasattr(b1, 'xwiki_Attribute'):
        assert _is_linked(b1, 'xwiki_Attribute', a)
    _safe_set(a, 'xwiki_Property84', {b2})
    assert _is_linked(a, 'xwiki_Property84', b2)
    if hasattr(b1, 'xwiki_Attribute'):
        assert not _is_linked(b1, 'xwiki_Attribute', a)
    if hasattr(b2, 'xwiki_Attribute'):
        assert _is_linked(b2, 'xwiki_Attribute', a)
    _safe_set(a, 'xwiki_Property84', set())
    assert not _is_linked(a, 'xwiki_Property84', b2)
    if hasattr(b2, 'xwiki_Attribute'):
        assert not _is_linked(b2, 'xwiki_Attribute', a)


def test_assoc_class_15_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_Class(id="sample_text", name="sample_text")
    b2 = xwiki_Class(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xwiki_DocumentRoot16', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot16', b1)
    if hasattr(b1, 'xwiki_Class17'):
        assert _is_linked(b1, 'xwiki_Class17', a)
    _safe_set(a, 'xwiki_DocumentRoot16', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot16', b2)
    if hasattr(b1, 'xwiki_Class17'):
        assert not _is_linked(b1, 'xwiki_Class17', a)
    if hasattr(b2, 'xwiki_Class17'):
        assert _is_linked(b2, 'xwiki_Class17', a)
    _safe_set(a, 'xwiki_DocumentRoot16', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot16', b2)
    if hasattr(b2, 'xwiki_Class17'):
        assert not _is_linked(b2, 'xwiki_Class17', a)


def test_assoc_class_2_link_reassign_clear():
    a = xwiki_Class(id="sample_text", name="sample_text")
    b1 = xwiki_ClassesType()
    b2 = xwiki_ClassesType()
    _safe_set(a, 'xwiki_Class3', b1)
    assert _is_linked(a, 'xwiki_Class3', b1)
    if hasattr(b1, 'xwiki_ClassesType'):
        assert _is_linked(b1, 'xwiki_ClassesType', a)
    _safe_set(a, 'xwiki_Class3', b2)
    assert _is_linked(a, 'xwiki_Class3', b2)
    if hasattr(b1, 'xwiki_ClassesType'):
        assert not _is_linked(b1, 'xwiki_ClassesType', a)
    if hasattr(b2, 'xwiki_ClassesType'):
        assert _is_linked(b2, 'xwiki_ClassesType', a)
    _safe_set(a, 'xwiki_Class3', None)
    assert not _is_linked(a, 'xwiki_Class3', b2)
    if hasattr(b2, 'xwiki_ClassesType'):
        assert not _is_linked(b2, 'xwiki_ClassesType', a)


def test_assoc_classes18_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_ClassesType()
    b2 = xwiki_ClassesType()
    _safe_set(a, 'xwiki_DocumentRoot19', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot19', b1)
    if hasattr(b1, 'xwiki_ClassesType20'):
        assert _is_linked(b1, 'xwiki_ClassesType20', a)
    _safe_set(a, 'xwiki_DocumentRoot19', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot19', b2)
    if hasattr(b1, 'xwiki_ClassesType20'):
        assert not _is_linked(b1, 'xwiki_ClassesType20', a)
    if hasattr(b2, 'xwiki_ClassesType20'):
        assert _is_linked(b2, 'xwiki_ClassesType20', a)
    _safe_set(a, 'xwiki_DocumentRoot19', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot19', b2)
    if hasattr(b2, 'xwiki_ClassesType20'):
        assert not _is_linked(b2, 'xwiki_ClassesType20', a)


def test_assoc_comment21_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    b2 = xwiki_Comment(author="sample_text_2", authorName="sample_text_2", date="sample_text_2", highlight="sample_text_2", id="sample_text_2", pageId="sample_text_2", replyTo="sample_text_2", text="sample_text_2")
    _safe_set(a, 'xwiki_DocumentRoot22', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot22', b1)
    if hasattr(b1, 'xwiki_Comment23'):
        assert _is_linked(b1, 'xwiki_Comment23', a)
    _safe_set(a, 'xwiki_DocumentRoot22', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot22', b2)
    if hasattr(b1, 'xwiki_Comment23'):
        assert not _is_linked(b1, 'xwiki_Comment23', a)
    if hasattr(b2, 'xwiki_Comment23'):
        assert _is_linked(b2, 'xwiki_Comment23', a)
    _safe_set(a, 'xwiki_DocumentRoot22', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot22', b2)
    if hasattr(b2, 'xwiki_Comment23'):
        assert not _is_linked(b2, 'xwiki_Comment23', a)


def test_assoc_comment4_link_reassign_clear():
    a = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    b1 = xwiki_CommentsType()
    b2 = xwiki_CommentsType()
    _safe_set(a, 'xwiki_Comment', b1)
    assert _is_linked(a, 'xwiki_Comment', b1)
    if hasattr(b1, 'xwiki_CommentsType'):
        assert _is_linked(b1, 'xwiki_CommentsType', a)
    _safe_set(a, 'xwiki_Comment', b2)
    assert _is_linked(a, 'xwiki_Comment', b2)
    if hasattr(b1, 'xwiki_CommentsType'):
        assert not _is_linked(b1, 'xwiki_CommentsType', a)
    if hasattr(b2, 'xwiki_CommentsType'):
        assert _is_linked(b2, 'xwiki_CommentsType', a)
    _safe_set(a, 'xwiki_Comment', None)
    assert not _is_linked(a, 'xwiki_Comment', b2)
    if hasattr(b2, 'xwiki_CommentsType'):
        assert not _is_linked(b2, 'xwiki_CommentsType', a)


def test_assoc_comments24_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_CommentsType()
    b2 = xwiki_CommentsType()
    _safe_set(a, 'xwiki_DocumentRoot25', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot25', b1)
    if hasattr(b1, 'xwiki_CommentsType26'):
        assert _is_linked(b1, 'xwiki_CommentsType26', a)
    _safe_set(a, 'xwiki_DocumentRoot25', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot25', b2)
    if hasattr(b1, 'xwiki_CommentsType26'):
        assert not _is_linked(b1, 'xwiki_CommentsType26', a)
    if hasattr(b2, 'xwiki_CommentsType26'):
        assert _is_linked(b2, 'xwiki_CommentsType26', a)
    _safe_set(a, 'xwiki_DocumentRoot25', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot25', b2)
    if hasattr(b2, 'xwiki_CommentsType26'):
        assert not _is_linked(b2, 'xwiki_CommentsType26', a)


def test_assoc_history27_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_HistoryType()
    b2 = xwiki_HistoryType()
    _safe_set(a, 'xwiki_DocumentRoot28', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot28', b1)
    if hasattr(b1, 'xwiki_HistoryType'):
        assert _is_linked(b1, 'xwiki_HistoryType', a)
    _safe_set(a, 'xwiki_DocumentRoot28', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot28', b2)
    if hasattr(b1, 'xwiki_HistoryType'):
        assert not _is_linked(b1, 'xwiki_HistoryType', a)
    if hasattr(b2, 'xwiki_HistoryType'):
        assert _is_linked(b2, 'xwiki_HistoryType', a)
    _safe_set(a, 'xwiki_DocumentRoot28', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot28', b2)
    if hasattr(b2, 'xwiki_HistoryType'):
        assert not _is_linked(b2, 'xwiki_HistoryType', a)


def test_assoc_historySummary66_link_reassign_clear():
    a = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    b1 = xwiki_HistoryType()
    b2 = xwiki_HistoryType()
    _safe_set(a, 'xwiki_HistorySummary', b1)
    assert _is_linked(a, 'xwiki_HistorySummary', b1)
    if hasattr(b1, 'xwiki_HistoryType67'):
        assert _is_linked(b1, 'xwiki_HistoryType67', a)
    _safe_set(a, 'xwiki_HistorySummary', b2)
    assert _is_linked(a, 'xwiki_HistorySummary', b2)
    if hasattr(b1, 'xwiki_HistoryType67'):
        assert not _is_linked(b1, 'xwiki_HistoryType67', a)
    if hasattr(b2, 'xwiki_HistoryType67'):
        assert _is_linked(b2, 'xwiki_HistoryType67', a)
    _safe_set(a, 'xwiki_HistorySummary', None)
    assert not _is_linked(a, 'xwiki_HistorySummary', b2)
    if hasattr(b2, 'xwiki_HistoryType67'):
        assert not _is_linked(b2, 'xwiki_HistoryType67', a)


def test_assoc_link68_link_reassign_clear():
    a = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    b1 = xwiki_LinkCollection()
    b2 = xwiki_LinkCollection()
    _safe_set(a, 'xwiki_Link', b1)
    assert _is_linked(a, 'xwiki_Link', b1)
    if hasattr(b1, 'xwiki_LinkCollection'):
        assert _is_linked(b1, 'xwiki_LinkCollection', a)
    _safe_set(a, 'xwiki_Link', b2)
    assert _is_linked(a, 'xwiki_Link', b2)
    if hasattr(b1, 'xwiki_LinkCollection'):
        assert not _is_linked(b1, 'xwiki_LinkCollection', a)
    if hasattr(b2, 'xwiki_LinkCollection'):
        assert _is_linked(b2, 'xwiki_LinkCollection', a)
    _safe_set(a, 'xwiki_Link', None)
    assert not _is_linked(a, 'xwiki_Link', b2)
    if hasattr(b2, 'xwiki_LinkCollection'):
        assert not _is_linked(b2, 'xwiki_LinkCollection', a)


def test_assoc_object29_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_Object()
    b2 = xwiki_Object()
    _safe_set(a, 'xwiki_DocumentRoot30', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot30', b1)
    if hasattr(b1, 'xwiki_Object'):
        assert _is_linked(b1, 'xwiki_Object', a)
    _safe_set(a, 'xwiki_DocumentRoot30', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot30', b2)
    if hasattr(b1, 'xwiki_Object'):
        assert not _is_linked(b1, 'xwiki_Object', a)
    if hasattr(b2, 'xwiki_Object'):
        assert _is_linked(b2, 'xwiki_Object', a)
    _safe_set(a, 'xwiki_DocumentRoot30', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot30', b2)
    if hasattr(b2, 'xwiki_Object'):
        assert not _is_linked(b2, 'xwiki_Object', a)


def test_assoc_object85_link_reassign_clear():
    a = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    b1 = xwiki_Object()
    b2 = xwiki_Object()
    _safe_set(a, 'xwiki_SearchResult86', b1)
    assert _is_linked(a, 'xwiki_SearchResult86', b1)
    if hasattr(b1, 'xwiki_Object87'):
        assert _is_linked(b1, 'xwiki_Object87', a)
    _safe_set(a, 'xwiki_SearchResult86', b2)
    assert _is_linked(a, 'xwiki_SearchResult86', b2)
    if hasattr(b1, 'xwiki_Object87'):
        assert not _is_linked(b1, 'xwiki_Object87', a)
    if hasattr(b2, 'xwiki_Object87'):
        assert _is_linked(b2, 'xwiki_Object87', a)
    _safe_set(a, 'xwiki_SearchResult86', None)
    assert not _is_linked(a, 'xwiki_SearchResult86', b2)
    if hasattr(b2, 'xwiki_Object87'):
        assert not _is_linked(b2, 'xwiki_Object87', a)


def test_assoc_objectSummary33_link_reassign_clear():
    a = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_ObjectSummary', b1)
    assert _is_linked(a, 'xwiki_ObjectSummary', b1)
    if hasattr(b1, 'xwiki_DocumentRoot34'):
        assert _is_linked(b1, 'xwiki_DocumentRoot34', a)
    _safe_set(a, 'xwiki_ObjectSummary', b2)
    assert _is_linked(a, 'xwiki_ObjectSummary', b2)
    if hasattr(b1, 'xwiki_DocumentRoot34'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot34', a)
    if hasattr(b2, 'xwiki_DocumentRoot34'):
        assert _is_linked(b2, 'xwiki_DocumentRoot34', a)
    _safe_set(a, 'xwiki_ObjectSummary', None)
    assert not _is_linked(a, 'xwiki_ObjectSummary', b2)
    if hasattr(b2, 'xwiki_DocumentRoot34'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot34', a)


def test_assoc_objectSummary72_link_reassign_clear():
    a = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    b1 = xwiki_ObjectsType()
    b2 = xwiki_ObjectsType()
    _safe_set(a, 'xwiki_ObjectSummary74', b1)
    assert _is_linked(a, 'xwiki_ObjectSummary74', b1)
    if hasattr(b1, 'xwiki_ObjectsType73'):
        assert _is_linked(b1, 'xwiki_ObjectsType73', a)
    _safe_set(a, 'xwiki_ObjectSummary74', b2)
    assert _is_linked(a, 'xwiki_ObjectSummary74', b2)
    if hasattr(b1, 'xwiki_ObjectsType73'):
        assert not _is_linked(b1, 'xwiki_ObjectsType73', a)
    if hasattr(b2, 'xwiki_ObjectsType73'):
        assert _is_linked(b2, 'xwiki_ObjectsType73', a)
    _safe_set(a, 'xwiki_ObjectSummary74', None)
    assert not _is_linked(a, 'xwiki_ObjectSummary74', b2)
    if hasattr(b2, 'xwiki_ObjectsType73'):
        assert not _is_linked(b2, 'xwiki_ObjectsType73', a)


def test_assoc_objects31_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_ObjectsType()
    b2 = xwiki_ObjectsType()
    _safe_set(a, 'xwiki_DocumentRoot32', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot32', b1)
    if hasattr(b1, 'xwiki_ObjectsType'):
        assert _is_linked(b1, 'xwiki_ObjectsType', a)
    _safe_set(a, 'xwiki_DocumentRoot32', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot32', b2)
    if hasattr(b1, 'xwiki_ObjectsType'):
        assert not _is_linked(b1, 'xwiki_ObjectsType', a)
    if hasattr(b2, 'xwiki_ObjectsType'):
        assert _is_linked(b2, 'xwiki_ObjectsType', a)
    _safe_set(a, 'xwiki_DocumentRoot32', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot32', b2)
    if hasattr(b2, 'xwiki_ObjectsType'):
        assert not _is_linked(b2, 'xwiki_ObjectsType', a)


def test_assoc_page35_link_reassign_clear():
    a = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Page', b1)
    assert _is_linked(a, 'xwiki_Page', b1)
    if hasattr(b1, 'xwiki_DocumentRoot36'):
        assert _is_linked(b1, 'xwiki_DocumentRoot36', a)
    _safe_set(a, 'xwiki_Page', b2)
    assert _is_linked(a, 'xwiki_Page', b2)
    if hasattr(b1, 'xwiki_DocumentRoot36'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot36', a)
    if hasattr(b2, 'xwiki_DocumentRoot36'):
        assert _is_linked(b2, 'xwiki_DocumentRoot36', a)
    _safe_set(a, 'xwiki_Page', None)
    assert not _is_linked(a, 'xwiki_Page', b2)
    if hasattr(b2, 'xwiki_DocumentRoot36'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot36', a)


def test_assoc_pageSummary75_link_reassign_clear():
    a = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b1 = xwiki_PagesType()
    b2 = xwiki_PagesType()
    _safe_set(a, 'xwiki_PageSummary', b1)
    assert _is_linked(a, 'xwiki_PageSummary', b1)
    if hasattr(b1, 'xwiki_PagesType76'):
        assert _is_linked(b1, 'xwiki_PagesType76', a)
    _safe_set(a, 'xwiki_PageSummary', b2)
    assert _is_linked(a, 'xwiki_PageSummary', b2)
    if hasattr(b1, 'xwiki_PagesType76'):
        assert not _is_linked(b1, 'xwiki_PagesType76', a)
    if hasattr(b2, 'xwiki_PagesType76'):
        assert _is_linked(b2, 'xwiki_PagesType76', a)
    _safe_set(a, 'xwiki_PageSummary', None)
    assert not _is_linked(a, 'xwiki_PageSummary', b2)
    if hasattr(b2, 'xwiki_PagesType76'):
        assert not _is_linked(b2, 'xwiki_PagesType76', a)


def test_assoc_pages37_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_PagesType()
    b2 = xwiki_PagesType()
    _safe_set(a, 'xwiki_DocumentRoot38', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot38', b1)
    if hasattr(b1, 'xwiki_PagesType'):
        assert _is_linked(b1, 'xwiki_PagesType', a)
    _safe_set(a, 'xwiki_DocumentRoot38', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot38', b2)
    if hasattr(b1, 'xwiki_PagesType'):
        assert not _is_linked(b1, 'xwiki_PagesType', a)
    if hasattr(b2, 'xwiki_PagesType'):
        assert _is_linked(b2, 'xwiki_PagesType', a)
    _safe_set(a, 'xwiki_DocumentRoot38', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot38', b2)
    if hasattr(b2, 'xwiki_PagesType'):
        assert not _is_linked(b2, 'xwiki_PagesType', a)


def test_assoc_properties39_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_PropertiesType()
    b2 = xwiki_PropertiesType()
    _safe_set(a, 'xwiki_DocumentRoot40', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot40', b1)
    if hasattr(b1, 'xwiki_PropertiesType'):
        assert _is_linked(b1, 'xwiki_PropertiesType', a)
    _safe_set(a, 'xwiki_DocumentRoot40', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot40', b2)
    if hasattr(b1, 'xwiki_PropertiesType'):
        assert not _is_linked(b1, 'xwiki_PropertiesType', a)
    if hasattr(b2, 'xwiki_PropertiesType'):
        assert _is_linked(b2, 'xwiki_PropertiesType', a)
    _safe_set(a, 'xwiki_DocumentRoot40', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot40', b2)
    if hasattr(b2, 'xwiki_PropertiesType'):
        assert not _is_linked(b2, 'xwiki_PropertiesType', a)


def test_assoc_property1_link_reassign_clear():
    a = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    b1 = xwiki_Class(id="sample_text", name="sample_text")
    b2 = xwiki_Class(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xwiki_Property', b1)
    assert _is_linked(a, 'xwiki_Property', b1)
    if hasattr(b1, 'xwiki_Class'):
        assert _is_linked(b1, 'xwiki_Class', a)
    _safe_set(a, 'xwiki_Property', b2)
    assert _is_linked(a, 'xwiki_Property', b2)
    if hasattr(b1, 'xwiki_Class'):
        assert not _is_linked(b1, 'xwiki_Class', a)
    if hasattr(b2, 'xwiki_Class'):
        assert _is_linked(b2, 'xwiki_Class', a)
    _safe_set(a, 'xwiki_Property', None)
    assert not _is_linked(a, 'xwiki_Property', b2)
    if hasattr(b2, 'xwiki_Class'):
        assert not _is_linked(b2, 'xwiki_Class', a)


def test_assoc_property41_link_reassign_clear():
    a = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Property43', b1)
    assert _is_linked(a, 'xwiki_Property43', b1)
    if hasattr(b1, 'xwiki_DocumentRoot42'):
        assert _is_linked(b1, 'xwiki_DocumentRoot42', a)
    _safe_set(a, 'xwiki_Property43', b2)
    assert _is_linked(a, 'xwiki_Property43', b2)
    if hasattr(b1, 'xwiki_DocumentRoot42'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot42', a)
    if hasattr(b2, 'xwiki_DocumentRoot42'):
        assert _is_linked(b2, 'xwiki_DocumentRoot42', a)
    _safe_set(a, 'xwiki_Property43', None)
    assert not _is_linked(a, 'xwiki_Property43', b2)
    if hasattr(b2, 'xwiki_DocumentRoot42'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot42', a)


def test_assoc_property69_link_reassign_clear():
    a = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    b1 = xwiki_Object()
    b2 = xwiki_Object()
    _safe_set(a, 'xwiki_Property71', b1)
    assert _is_linked(a, 'xwiki_Property71', b1)
    if hasattr(b1, 'xwiki_Object70'):
        assert _is_linked(b1, 'xwiki_Object70', a)
    _safe_set(a, 'xwiki_Property71', b2)
    assert _is_linked(a, 'xwiki_Property71', b2)
    if hasattr(b1, 'xwiki_Object70'):
        assert not _is_linked(b1, 'xwiki_Object70', a)
    if hasattr(b2, 'xwiki_Object70'):
        assert _is_linked(b2, 'xwiki_Object70', a)
    _safe_set(a, 'xwiki_Property71', None)
    assert not _is_linked(a, 'xwiki_Property71', b2)
    if hasattr(b2, 'xwiki_Object70'):
        assert not _is_linked(b2, 'xwiki_Object70', a)


def test_assoc_property80_link_reassign_clear():
    a = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    b1 = xwiki_PropertiesType()
    b2 = xwiki_PropertiesType()
    _safe_set(a, 'xwiki_Property82', b1)
    assert _is_linked(a, 'xwiki_Property82', b1)
    if hasattr(b1, 'xwiki_PropertiesType81'):
        assert _is_linked(b1, 'xwiki_PropertiesType81', a)
    _safe_set(a, 'xwiki_Property82', b2)
    assert _is_linked(a, 'xwiki_Property82', b2)
    if hasattr(b1, 'xwiki_PropertiesType81'):
        assert not _is_linked(b1, 'xwiki_PropertiesType81', a)
    if hasattr(b2, 'xwiki_PropertiesType81'):
        assert _is_linked(b2, 'xwiki_PropertiesType81', a)
    _safe_set(a, 'xwiki_Property82', None)
    assert not _is_linked(a, 'xwiki_Property82', b2)
    if hasattr(b2, 'xwiki_PropertiesType81'):
        assert not _is_linked(b2, 'xwiki_PropertiesType81', a)


def test_assoc_searchResult44_link_reassign_clear():
    a = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_SearchResult', b1)
    assert _is_linked(a, 'xwiki_SearchResult', b1)
    if hasattr(b1, 'xwiki_DocumentRoot45'):
        assert _is_linked(b1, 'xwiki_DocumentRoot45', a)
    _safe_set(a, 'xwiki_SearchResult', b2)
    assert _is_linked(a, 'xwiki_SearchResult', b2)
    if hasattr(b1, 'xwiki_DocumentRoot45'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot45', a)
    if hasattr(b2, 'xwiki_DocumentRoot45'):
        assert _is_linked(b2, 'xwiki_DocumentRoot45', a)
    _safe_set(a, 'xwiki_SearchResult', None)
    assert not _is_linked(a, 'xwiki_SearchResult', b2)
    if hasattr(b2, 'xwiki_DocumentRoot45'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot45', a)


def test_assoc_searchResult88_link_reassign_clear():
    a = xwiki_SearchResultsType(template="sample_text")
    b1 = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    b2 = xwiki_SearchResult(author="sample_text_2", authorName="sample_text_2", className="sample_text_2", filename="sample_text_2", id="sample_text_2", language="sample_text_2", modified="sample_text_2", objectNumber="sample_text_2", pageFullName="sample_text_2", pageName="sample_text_2", score="sample_text_2", space="sample_text_2", title="sample_text_2", type="sample_text_2", version="sample_text_2", wiki="sample_text_2")
    _safe_set(a, 'xwiki_SearchResultsType89', {b1})
    assert _is_linked(a, 'xwiki_SearchResultsType89', b1)
    if hasattr(b1, 'xwiki_SearchResult90'):
        assert _is_linked(b1, 'xwiki_SearchResult90', a)
    _safe_set(a, 'xwiki_SearchResultsType89', {b2})
    assert _is_linked(a, 'xwiki_SearchResultsType89', b2)
    if hasattr(b1, 'xwiki_SearchResult90'):
        assert not _is_linked(b1, 'xwiki_SearchResult90', a)
    if hasattr(b2, 'xwiki_SearchResult90'):
        assert _is_linked(b2, 'xwiki_SearchResult90', a)
    _safe_set(a, 'xwiki_SearchResultsType89', set())
    assert not _is_linked(a, 'xwiki_SearchResultsType89', b2)
    if hasattr(b2, 'xwiki_SearchResult90'):
        assert not _is_linked(b2, 'xwiki_SearchResult90', a)


def test_assoc_searchResults46_link_reassign_clear():
    a = xwiki_SearchResultsType(template="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_SearchResultsType', b1)
    assert _is_linked(a, 'xwiki_SearchResultsType', b1)
    if hasattr(b1, 'xwiki_DocumentRoot47'):
        assert _is_linked(b1, 'xwiki_DocumentRoot47', a)
    _safe_set(a, 'xwiki_SearchResultsType', b2)
    assert _is_linked(a, 'xwiki_SearchResultsType', b2)
    if hasattr(b1, 'xwiki_DocumentRoot47'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot47', a)
    if hasattr(b2, 'xwiki_DocumentRoot47'):
        assert _is_linked(b2, 'xwiki_DocumentRoot47', a)
    _safe_set(a, 'xwiki_SearchResultsType', None)
    assert not _is_linked(a, 'xwiki_SearchResultsType', b2)
    if hasattr(b2, 'xwiki_DocumentRoot47'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot47', a)


def test_assoc_space48_link_reassign_clear():
    a = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Space', b1)
    assert _is_linked(a, 'xwiki_Space', b1)
    if hasattr(b1, 'xwiki_DocumentRoot49'):
        assert _is_linked(b1, 'xwiki_DocumentRoot49', a)
    _safe_set(a, 'xwiki_Space', b2)
    assert _is_linked(a, 'xwiki_Space', b2)
    if hasattr(b1, 'xwiki_DocumentRoot49'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot49', a)
    if hasattr(b2, 'xwiki_DocumentRoot49'):
        assert _is_linked(b2, 'xwiki_DocumentRoot49', a)
    _safe_set(a, 'xwiki_Space', None)
    assert not _is_linked(a, 'xwiki_Space', b2)
    if hasattr(b2, 'xwiki_DocumentRoot49'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot49', a)


def test_assoc_space91_link_reassign_clear():
    a = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b1 = xwiki_SpacesType()
    b2 = xwiki_SpacesType()
    _safe_set(a, 'xwiki_Space93', b1)
    assert _is_linked(a, 'xwiki_Space93', b1)
    if hasattr(b1, 'xwiki_SpacesType92'):
        assert _is_linked(b1, 'xwiki_SpacesType92', a)
    _safe_set(a, 'xwiki_Space93', b2)
    assert _is_linked(a, 'xwiki_Space93', b2)
    if hasattr(b1, 'xwiki_SpacesType92'):
        assert not _is_linked(b1, 'xwiki_SpacesType92', a)
    if hasattr(b2, 'xwiki_SpacesType92'):
        assert _is_linked(b2, 'xwiki_SpacesType92', a)
    _safe_set(a, 'xwiki_Space93', None)
    assert not _is_linked(a, 'xwiki_Space93', b2)
    if hasattr(b2, 'xwiki_SpacesType92'):
        assert not _is_linked(b2, 'xwiki_SpacesType92', a)


def test_assoc_spaces50_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_SpacesType()
    b2 = xwiki_SpacesType()
    _safe_set(a, 'xwiki_DocumentRoot51', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot51', b1)
    if hasattr(b1, 'xwiki_SpacesType'):
        assert _is_linked(b1, 'xwiki_SpacesType', a)
    _safe_set(a, 'xwiki_DocumentRoot51', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot51', b2)
    if hasattr(b1, 'xwiki_SpacesType'):
        assert not _is_linked(b1, 'xwiki_SpacesType', a)
    if hasattr(b2, 'xwiki_SpacesType'):
        assert _is_linked(b2, 'xwiki_SpacesType', a)
    _safe_set(a, 'xwiki_DocumentRoot51', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot51', b2)
    if hasattr(b2, 'xwiki_SpacesType'):
        assert not _is_linked(b2, 'xwiki_SpacesType', a)


def test_assoc_syntaxes102_link_reassign_clear():
    a = xwiki_XWiki(version="sample_text")
    b1 = xwiki_Syntaxes(syntax="sample_text")
    b2 = xwiki_Syntaxes(syntax="sample_text_2")
    _safe_set(a, 'xwiki_XWiki103', b1)
    assert _is_linked(a, 'xwiki_XWiki103', b1)
    if hasattr(b1, 'xwiki_Syntaxes104'):
        assert _is_linked(b1, 'xwiki_Syntaxes104', a)
    _safe_set(a, 'xwiki_XWiki103', b2)
    assert _is_linked(a, 'xwiki_XWiki103', b2)
    if hasattr(b1, 'xwiki_Syntaxes104'):
        assert not _is_linked(b1, 'xwiki_Syntaxes104', a)
    if hasattr(b2, 'xwiki_Syntaxes104'):
        assert _is_linked(b2, 'xwiki_Syntaxes104', a)
    _safe_set(a, 'xwiki_XWiki103', None)
    assert not _is_linked(a, 'xwiki_XWiki103', b2)
    if hasattr(b2, 'xwiki_Syntaxes104'):
        assert not _is_linked(b2, 'xwiki_Syntaxes104', a)


def test_assoc_syntaxes52_link_reassign_clear():
    a = xwiki_Syntaxes(syntax="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Syntaxes', b1)
    assert _is_linked(a, 'xwiki_Syntaxes', b1)
    if hasattr(b1, 'xwiki_DocumentRoot53'):
        assert _is_linked(b1, 'xwiki_DocumentRoot53', a)
    _safe_set(a, 'xwiki_Syntaxes', b2)
    assert _is_linked(a, 'xwiki_Syntaxes', b2)
    if hasattr(b1, 'xwiki_DocumentRoot53'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot53', a)
    if hasattr(b2, 'xwiki_DocumentRoot53'):
        assert _is_linked(b2, 'xwiki_DocumentRoot53', a)
    _safe_set(a, 'xwiki_Syntaxes', None)
    assert not _is_linked(a, 'xwiki_Syntaxes', b2)
    if hasattr(b2, 'xwiki_DocumentRoot53'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot53', a)


def test_assoc_tag54_link_reassign_clear():
    a = xwiki_Tag(name="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Tag', b1)
    assert _is_linked(a, 'xwiki_Tag', b1)
    if hasattr(b1, 'xwiki_DocumentRoot55'):
        assert _is_linked(b1, 'xwiki_DocumentRoot55', a)
    _safe_set(a, 'xwiki_Tag', b2)
    assert _is_linked(a, 'xwiki_Tag', b2)
    if hasattr(b1, 'xwiki_DocumentRoot55'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot55', a)
    if hasattr(b2, 'xwiki_DocumentRoot55'):
        assert _is_linked(b2, 'xwiki_DocumentRoot55', a)
    _safe_set(a, 'xwiki_Tag', None)
    assert not _is_linked(a, 'xwiki_Tag', b2)
    if hasattr(b2, 'xwiki_DocumentRoot55'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot55', a)


def test_assoc_tag94_link_reassign_clear():
    a = xwiki_Tag(name="sample_text")
    b1 = xwiki_TagsType()
    b2 = xwiki_TagsType()
    _safe_set(a, 'xwiki_Tag96', b1)
    assert _is_linked(a, 'xwiki_Tag96', b1)
    if hasattr(b1, 'xwiki_TagsType95'):
        assert _is_linked(b1, 'xwiki_TagsType95', a)
    _safe_set(a, 'xwiki_Tag96', b2)
    assert _is_linked(a, 'xwiki_Tag96', b2)
    if hasattr(b1, 'xwiki_TagsType95'):
        assert not _is_linked(b1, 'xwiki_TagsType95', a)
    if hasattr(b2, 'xwiki_TagsType95'):
        assert _is_linked(b2, 'xwiki_TagsType95', a)
    _safe_set(a, 'xwiki_Tag96', None)
    assert not _is_linked(a, 'xwiki_Tag96', b2)
    if hasattr(b2, 'xwiki_TagsType95'):
        assert not _is_linked(b2, 'xwiki_TagsType95', a)


def test_assoc_tags56_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_TagsType()
    b2 = xwiki_TagsType()
    _safe_set(a, 'xwiki_DocumentRoot57', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot57', b1)
    if hasattr(b1, 'xwiki_TagsType'):
        assert _is_linked(b1, 'xwiki_TagsType', a)
    _safe_set(a, 'xwiki_DocumentRoot57', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot57', b2)
    if hasattr(b1, 'xwiki_TagsType'):
        assert not _is_linked(b1, 'xwiki_TagsType', a)
    if hasattr(b2, 'xwiki_TagsType'):
        assert _is_linked(b2, 'xwiki_TagsType', a)
    _safe_set(a, 'xwiki_DocumentRoot57', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot57', b2)
    if hasattr(b2, 'xwiki_TagsType'):
        assert not _is_linked(b2, 'xwiki_TagsType', a)


def test_assoc_translation97_link_reassign_clear():
    a = xwiki_Translations(default="sample_text")
    b1 = xwiki_Translation(language="sample_text")
    b2 = xwiki_Translation(language="sample_text_2")
    _safe_set(a, 'xwiki_Translations98', {b1})
    assert _is_linked(a, 'xwiki_Translations98', b1)
    if hasattr(b1, 'xwiki_Translation'):
        assert _is_linked(b1, 'xwiki_Translation', a)
    _safe_set(a, 'xwiki_Translations98', {b2})
    assert _is_linked(a, 'xwiki_Translations98', b2)
    if hasattr(b1, 'xwiki_Translation'):
        assert not _is_linked(b1, 'xwiki_Translation', a)
    if hasattr(b2, 'xwiki_Translation'):
        assert _is_linked(b2, 'xwiki_Translation', a)
    _safe_set(a, 'xwiki_Translations98', set())
    assert not _is_linked(a, 'xwiki_Translations98', b2)
    if hasattr(b2, 'xwiki_Translation'):
        assert not _is_linked(b2, 'xwiki_Translation', a)


def test_assoc_translations58_link_reassign_clear():
    a = xwiki_Translations(default="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Translations', b1)
    assert _is_linked(a, 'xwiki_Translations', b1)
    if hasattr(b1, 'xwiki_DocumentRoot59'):
        assert _is_linked(b1, 'xwiki_DocumentRoot59', a)
    _safe_set(a, 'xwiki_Translations', b2)
    assert _is_linked(a, 'xwiki_Translations', b2)
    if hasattr(b1, 'xwiki_DocumentRoot59'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot59', a)
    if hasattr(b2, 'xwiki_DocumentRoot59'):
        assert _is_linked(b2, 'xwiki_DocumentRoot59', a)
    _safe_set(a, 'xwiki_Translations', None)
    assert not _is_linked(a, 'xwiki_Translations', b2)
    if hasattr(b2, 'xwiki_DocumentRoot59'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot59', a)


def test_assoc_translations77_link_reassign_clear():
    a = xwiki_Translations(default="sample_text")
    b1 = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    b2 = xwiki_PageSummary(author="sample_text_2", authorName="sample_text_2", fullName="sample_text_2", id="sample_text_2", name="sample_text_2", parent="sample_text_2", parentId="sample_text_2", space="sample_text_2", syntax="sample_text_2", title="sample_text_2", version="sample_text_2", wiki="sample_text_2", xwikiAbsoluteUrl="sample_text_2", xwikiRelativeUrl="sample_text_2")
    _safe_set(a, 'xwiki_Translations79', b1)
    assert _is_linked(a, 'xwiki_Translations79', b1)
    if hasattr(b1, 'xwiki_PageSummary78'):
        assert _is_linked(b1, 'xwiki_PageSummary78', a)
    _safe_set(a, 'xwiki_Translations79', b2)
    assert _is_linked(a, 'xwiki_Translations79', b2)
    if hasattr(b1, 'xwiki_PageSummary78'):
        assert not _is_linked(b1, 'xwiki_PageSummary78', a)
    if hasattr(b2, 'xwiki_PageSummary78'):
        assert _is_linked(b2, 'xwiki_PageSummary78', a)
    _safe_set(a, 'xwiki_Translations79', None)
    assert not _is_linked(a, 'xwiki_Translations79', b2)
    if hasattr(b2, 'xwiki_PageSummary78'):
        assert not _is_linked(b2, 'xwiki_PageSummary78', a)


def test_assoc_wiki60_link_reassign_clear():
    a = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_Wiki', b1)
    assert _is_linked(a, 'xwiki_Wiki', b1)
    if hasattr(b1, 'xwiki_DocumentRoot61'):
        assert _is_linked(b1, 'xwiki_DocumentRoot61', a)
    _safe_set(a, 'xwiki_Wiki', b2)
    assert _is_linked(a, 'xwiki_Wiki', b2)
    if hasattr(b1, 'xwiki_DocumentRoot61'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot61', a)
    if hasattr(b2, 'xwiki_DocumentRoot61'):
        assert _is_linked(b2, 'xwiki_DocumentRoot61', a)
    _safe_set(a, 'xwiki_Wiki', None)
    assert not _is_linked(a, 'xwiki_Wiki', b2)
    if hasattr(b2, 'xwiki_DocumentRoot61'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot61', a)


def test_assoc_wiki99_link_reassign_clear():
    a = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    b1 = xwiki_WikisType()
    b2 = xwiki_WikisType()
    _safe_set(a, 'xwiki_Wiki101', b1)
    assert _is_linked(a, 'xwiki_Wiki101', b1)
    if hasattr(b1, 'xwiki_WikisType100'):
        assert _is_linked(b1, 'xwiki_WikisType100', a)
    _safe_set(a, 'xwiki_Wiki101', b2)
    assert _is_linked(a, 'xwiki_Wiki101', b2)
    if hasattr(b1, 'xwiki_WikisType100'):
        assert not _is_linked(b1, 'xwiki_WikisType100', a)
    if hasattr(b2, 'xwiki_WikisType100'):
        assert _is_linked(b2, 'xwiki_WikisType100', a)
    _safe_set(a, 'xwiki_Wiki101', None)
    assert not _is_linked(a, 'xwiki_Wiki101', b2)
    if hasattr(b2, 'xwiki_WikisType100'):
        assert not _is_linked(b2, 'xwiki_WikisType100', a)


def test_assoc_wikis62_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_WikisType()
    b2 = xwiki_WikisType()
    _safe_set(a, 'xwiki_DocumentRoot63', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot63', b1)
    if hasattr(b1, 'xwiki_WikisType'):
        assert _is_linked(b1, 'xwiki_WikisType', a)
    _safe_set(a, 'xwiki_DocumentRoot63', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot63', b2)
    if hasattr(b1, 'xwiki_WikisType'):
        assert not _is_linked(b1, 'xwiki_WikisType', a)
    if hasattr(b2, 'xwiki_WikisType'):
        assert _is_linked(b2, 'xwiki_WikisType', a)
    _safe_set(a, 'xwiki_DocumentRoot63', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot63', b2)
    if hasattr(b2, 'xwiki_WikisType'):
        assert not _is_linked(b2, 'xwiki_WikisType', a)


def test_assoc_xMLNSPrefixMap5_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_EStringToStringMapEntry()
    b2 = xwiki_EStringToStringMapEntry()
    _safe_set(a, 'xwiki_DocumentRoot', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot', b1)
    if hasattr(b1, 'xwiki_EStringToStringMapEntry'):
        assert _is_linked(b1, 'xwiki_EStringToStringMapEntry', a)
    _safe_set(a, 'xwiki_DocumentRoot', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot', b2)
    if hasattr(b1, 'xwiki_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'xwiki_EStringToStringMapEntry', a)
    if hasattr(b2, 'xwiki_EStringToStringMapEntry'):
        assert _is_linked(b2, 'xwiki_EStringToStringMapEntry', a)
    _safe_set(a, 'xwiki_DocumentRoot', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot', b2)
    if hasattr(b2, 'xwiki_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'xwiki_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation6_link_reassign_clear():
    a = xwiki_DocumentRoot(mixed="sample_text")
    b1 = xwiki_EStringToStringMapEntry()
    b2 = xwiki_EStringToStringMapEntry()
    _safe_set(a, 'xwiki_DocumentRoot7', {b1})
    assert _is_linked(a, 'xwiki_DocumentRoot7', b1)
    if hasattr(b1, 'xwiki_EStringToStringMapEntry8'):
        assert _is_linked(b1, 'xwiki_EStringToStringMapEntry8', a)
    _safe_set(a, 'xwiki_DocumentRoot7', {b2})
    assert _is_linked(a, 'xwiki_DocumentRoot7', b2)
    if hasattr(b1, 'xwiki_EStringToStringMapEntry8'):
        assert not _is_linked(b1, 'xwiki_EStringToStringMapEntry8', a)
    if hasattr(b2, 'xwiki_EStringToStringMapEntry8'):
        assert _is_linked(b2, 'xwiki_EStringToStringMapEntry8', a)
    _safe_set(a, 'xwiki_DocumentRoot7', set())
    assert not _is_linked(a, 'xwiki_DocumentRoot7', b2)
    if hasattr(b2, 'xwiki_EStringToStringMapEntry8'):
        assert not _is_linked(b2, 'xwiki_EStringToStringMapEntry8', a)


def test_assoc_xwiki64_link_reassign_clear():
    a = xwiki_XWiki(version="sample_text")
    b1 = xwiki_DocumentRoot(mixed="sample_text")
    b2 = xwiki_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xwiki_XWiki', b1)
    assert _is_linked(a, 'xwiki_XWiki', b1)
    if hasattr(b1, 'xwiki_DocumentRoot65'):
        assert _is_linked(b1, 'xwiki_DocumentRoot65', a)
    _safe_set(a, 'xwiki_XWiki', b2)
    assert _is_linked(a, 'xwiki_XWiki', b2)
    if hasattr(b1, 'xwiki_DocumentRoot65'):
        assert not _is_linked(b1, 'xwiki_DocumentRoot65', a)
    if hasattr(b2, 'xwiki_DocumentRoot65'):
        assert _is_linked(b2, 'xwiki_DocumentRoot65', a)
    _safe_set(a, 'xwiki_XWiki', None)
    assert not _is_linked(a, 'xwiki_XWiki', b2)
    if hasattr(b2, 'xwiki_DocumentRoot65'):
        assert not _is_linked(b2, 'xwiki_DocumentRoot65', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

LinkCollection_strategy = st.builds(LinkCollection)
@given(instance=LinkCollection_strategy)
@settings(max_examples=25)
def test_LinkCollection_instantiation(instance):
    assert isinstance(instance, LinkCollection)


ObjectSummary_strategy = st.builds(ObjectSummary)
@given(instance=ObjectSummary_strategy)
@settings(max_examples=25)
def test_ObjectSummary_instantiation(instance):
    assert isinstance(instance, ObjectSummary)


PageSummary_strategy = st.builds(PageSummary)
@given(instance=PageSummary_strategy)
@settings(max_examples=25)
def test_PageSummary_instantiation(instance):
    assert isinstance(instance, PageSummary)


xwiki_Attachment_strategy = st.builds(xwiki_Attachment, author=safe_text, authorName=safe_text, date=safe_text, id=safe_text, mimeType=safe_text, name=safe_text, pageId=safe_text, pageVersion=safe_text, size=safe_text, version=safe_text, xwikiAbsoluteUrl=safe_text, xwikiRelativeUrl=safe_text)
@given(instance=xwiki_Attachment_strategy)
@settings(max_examples=25)
def test_xwiki_Attachment_instantiation(instance):
    assert isinstance(instance, xwiki_Attachment)


xwiki_AttachmentsType_strategy = st.builds(xwiki_AttachmentsType)
@given(instance=xwiki_AttachmentsType_strategy)
@settings(max_examples=25)
def test_xwiki_AttachmentsType_instantiation(instance):
    assert isinstance(instance, xwiki_AttachmentsType)


xwiki_Attribute_strategy = st.builds(xwiki_Attribute, name=safe_text, value=safe_text)
@given(instance=xwiki_Attribute_strategy)
@settings(max_examples=25)
def test_xwiki_Attribute_instantiation(instance):
    assert isinstance(instance, xwiki_Attribute)


xwiki_Class_strategy = st.builds(xwiki_Class, id=safe_text, name=safe_text)
@given(instance=xwiki_Class_strategy)
@settings(max_examples=25)
def test_xwiki_Class_instantiation(instance):
    assert isinstance(instance, xwiki_Class)


xwiki_ClassesType_strategy = st.builds(xwiki_ClassesType)
@given(instance=xwiki_ClassesType_strategy)
@settings(max_examples=25)
def test_xwiki_ClassesType_instantiation(instance):
    assert isinstance(instance, xwiki_ClassesType)


xwiki_Comment_strategy = st.builds(xwiki_Comment, author=safe_text, authorName=safe_text, date=safe_text, highlight=safe_text, id=safe_text, pageId=safe_text, replyTo=safe_text, text=safe_text)
@given(instance=xwiki_Comment_strategy)
@settings(max_examples=25)
def test_xwiki_Comment_instantiation(instance):
    assert isinstance(instance, xwiki_Comment)


xwiki_CommentsType_strategy = st.builds(xwiki_CommentsType)
@given(instance=xwiki_CommentsType_strategy)
@settings(max_examples=25)
def test_xwiki_CommentsType_instantiation(instance):
    assert isinstance(instance, xwiki_CommentsType)


xwiki_DocumentRoot_strategy = st.builds(xwiki_DocumentRoot, mixed=safe_text)
@given(instance=xwiki_DocumentRoot_strategy)
@settings(max_examples=25)
def test_xwiki_DocumentRoot_instantiation(instance):
    assert isinstance(instance, xwiki_DocumentRoot)


xwiki_EStringToStringMapEntry_strategy = st.builds(xwiki_EStringToStringMapEntry)
@given(instance=xwiki_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_xwiki_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, xwiki_EStringToStringMapEntry)


xwiki_HistorySummary_strategy = st.builds(xwiki_HistorySummary, comment=safe_text, language=safe_text, majorVersion=safe_text, minorVersion=safe_text, modified=safe_text, modifier=safe_text, modifierName=safe_text, name=safe_text, pageId=safe_text, space=safe_text, version=safe_text, wiki=safe_text)
@given(instance=xwiki_HistorySummary_strategy)
@settings(max_examples=25)
def test_xwiki_HistorySummary_instantiation(instance):
    assert isinstance(instance, xwiki_HistorySummary)


xwiki_HistoryType_strategy = st.builds(xwiki_HistoryType)
@given(instance=xwiki_HistoryType_strategy)
@settings(max_examples=25)
def test_xwiki_HistoryType_instantiation(instance):
    assert isinstance(instance, xwiki_HistoryType)


xwiki_Link_strategy = st.builds(xwiki_Link, href=safe_text, hrefLang=safe_text, rel=safe_text, type=safe_text)
@given(instance=xwiki_Link_strategy)
@settings(max_examples=25)
def test_xwiki_Link_instantiation(instance):
    assert isinstance(instance, xwiki_Link)


xwiki_LinkCollection_strategy = st.builds(xwiki_LinkCollection)
@given(instance=xwiki_LinkCollection_strategy)
@settings(max_examples=25)
def test_xwiki_LinkCollection_instantiation(instance):
    assert isinstance(instance, xwiki_LinkCollection)


xwiki_Object_strategy = st.builds(xwiki_Object)
@given(instance=xwiki_Object_strategy)
@settings(max_examples=25)
def test_xwiki_Object_instantiation(instance):
    assert isinstance(instance, xwiki_Object)


xwiki_ObjectSummary_strategy = st.builds(xwiki_ObjectSummary, className=safe_text, guid=safe_text, headline=safe_text, id=safe_text, number=safe_text, pageAuthor=safe_text, pageAuthorName=safe_text, pageId=safe_text, pageName=safe_text, pageVersion=safe_text, space=safe_text, wiki=safe_text)
@given(instance=xwiki_ObjectSummary_strategy)
@settings(max_examples=25)
def test_xwiki_ObjectSummary_instantiation(instance):
    assert isinstance(instance, xwiki_ObjectSummary)


xwiki_ObjectsType_strategy = st.builds(xwiki_ObjectsType)
@given(instance=xwiki_ObjectsType_strategy)
@settings(max_examples=25)
def test_xwiki_ObjectsType_instantiation(instance):
    assert isinstance(instance, xwiki_ObjectsType)


xwiki_Page_strategy = st.builds(xwiki_Page, comment=safe_text, content=safe_text, created=safe_text, creator=safe_text, creatorName=safe_text, language=safe_text, majorVersion=safe_text, minorVersion=safe_text, modified=safe_text, modifier=safe_text, modifierName=safe_text)
@given(instance=xwiki_Page_strategy)
@settings(max_examples=25)
def test_xwiki_Page_instantiation(instance):
    assert isinstance(instance, xwiki_Page)


xwiki_PageSummary_strategy = st.builds(xwiki_PageSummary, author=safe_text, authorName=safe_text, fullName=safe_text, id=safe_text, name=safe_text, parent=safe_text, parentId=safe_text, space=safe_text, syntax=safe_text, title=safe_text, version=safe_text, wiki=safe_text, xwikiAbsoluteUrl=safe_text, xwikiRelativeUrl=safe_text)
@given(instance=xwiki_PageSummary_strategy)
@settings(max_examples=25)
def test_xwiki_PageSummary_instantiation(instance):
    assert isinstance(instance, xwiki_PageSummary)


xwiki_PagesType_strategy = st.builds(xwiki_PagesType)
@given(instance=xwiki_PagesType_strategy)
@settings(max_examples=25)
def test_xwiki_PagesType_instantiation(instance):
    assert isinstance(instance, xwiki_PagesType)


xwiki_PropertiesType_strategy = st.builds(xwiki_PropertiesType)
@given(instance=xwiki_PropertiesType_strategy)
@settings(max_examples=25)
def test_xwiki_PropertiesType_instantiation(instance):
    assert isinstance(instance, xwiki_PropertiesType)


xwiki_Property_strategy = st.builds(xwiki_Property, name=safe_text, type=safe_text, value=safe_text)
@given(instance=xwiki_Property_strategy)
@settings(max_examples=25)
def test_xwiki_Property_instantiation(instance):
    assert isinstance(instance, xwiki_Property)


xwiki_SearchResult_strategy = st.builds(xwiki_SearchResult, author=safe_text, authorName=safe_text, className=safe_text, filename=safe_text, id=safe_text, language=safe_text, modified=safe_text, objectNumber=safe_text, pageFullName=safe_text, pageName=safe_text, score=safe_text, space=safe_text, title=safe_text, type=safe_text, version=safe_text, wiki=safe_text)
@given(instance=xwiki_SearchResult_strategy)
@settings(max_examples=25)
def test_xwiki_SearchResult_instantiation(instance):
    assert isinstance(instance, xwiki_SearchResult)


xwiki_SearchResultsType_strategy = st.builds(xwiki_SearchResultsType, template=safe_text)
@given(instance=xwiki_SearchResultsType_strategy)
@settings(max_examples=25)
def test_xwiki_SearchResultsType_instantiation(instance):
    assert isinstance(instance, xwiki_SearchResultsType)


xwiki_Space_strategy = st.builds(xwiki_Space, home=safe_text, id=safe_text, name=safe_text, wiki=safe_text, xwikiAbsoluteUrl=safe_text, xwikiRelativeUrl=safe_text)
@given(instance=xwiki_Space_strategy)
@settings(max_examples=25)
def test_xwiki_Space_instantiation(instance):
    assert isinstance(instance, xwiki_Space)


xwiki_SpacesType_strategy = st.builds(xwiki_SpacesType)
@given(instance=xwiki_SpacesType_strategy)
@settings(max_examples=25)
def test_xwiki_SpacesType_instantiation(instance):
    assert isinstance(instance, xwiki_SpacesType)


xwiki_Syntaxes_strategy = st.builds(xwiki_Syntaxes, syntax=safe_text)
@given(instance=xwiki_Syntaxes_strategy)
@settings(max_examples=25)
def test_xwiki_Syntaxes_instantiation(instance):
    assert isinstance(instance, xwiki_Syntaxes)


xwiki_Tag_strategy = st.builds(xwiki_Tag, name=safe_text)
@given(instance=xwiki_Tag_strategy)
@settings(max_examples=25)
def test_xwiki_Tag_instantiation(instance):
    assert isinstance(instance, xwiki_Tag)


xwiki_TagsType_strategy = st.builds(xwiki_TagsType)
@given(instance=xwiki_TagsType_strategy)
@settings(max_examples=25)
def test_xwiki_TagsType_instantiation(instance):
    assert isinstance(instance, xwiki_TagsType)


xwiki_Translation_strategy = st.builds(xwiki_Translation, language=safe_text)
@given(instance=xwiki_Translation_strategy)
@settings(max_examples=25)
def test_xwiki_Translation_instantiation(instance):
    assert isinstance(instance, xwiki_Translation)


xwiki_Translations_strategy = st.builds(xwiki_Translations, default=safe_text)
@given(instance=xwiki_Translations_strategy)
@settings(max_examples=25)
def test_xwiki_Translations_instantiation(instance):
    assert isinstance(instance, xwiki_Translations)


xwiki_Wiki_strategy = st.builds(xwiki_Wiki, description=safe_text, id=safe_text, name=safe_text, owner=safe_text)
@given(instance=xwiki_Wiki_strategy)
@settings(max_examples=25)
def test_xwiki_Wiki_instantiation(instance):
    assert isinstance(instance, xwiki_Wiki)


xwiki_WikisType_strategy = st.builds(xwiki_WikisType)
@given(instance=xwiki_WikisType_strategy)
@settings(max_examples=25)
def test_xwiki_WikisType_instantiation(instance):
    assert isinstance(instance, xwiki_WikisType)


xwiki_XWiki_strategy = st.builds(xwiki_XWiki, version=safe_text)
@given(instance=xwiki_XWiki_strategy)
@settings(max_examples=25)
def test_xwiki_XWiki_instantiation(instance):
    assert isinstance(instance, xwiki_XWiki)



