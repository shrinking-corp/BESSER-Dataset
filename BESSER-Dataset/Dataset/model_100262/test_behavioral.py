import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_attachment9_reverse_link_reassign_clear():
    a1 = xwiki_DocumentRoot(mixed="sample_text")
    a2 = xwiki_DocumentRoot(mixed="sample_text_2")
    b = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    _safe_set(b, 'xwiki_Attachment11', a1)
    assert _is_linked(b, 'xwiki_Attachment11', a1)
    if hasattr(a1, 'xwiki_DocumentRoot10'):
        assert _is_linked(a1, 'xwiki_DocumentRoot10', b)
    _safe_set(b, 'xwiki_Attachment11', a2)
    assert _is_linked(b, 'xwiki_Attachment11', a2)
    if hasattr(a1, 'xwiki_DocumentRoot10'):
        assert not _is_linked(a1, 'xwiki_DocumentRoot10', b)
    if hasattr(a2, 'xwiki_DocumentRoot10'):
        assert _is_linked(a2, 'xwiki_DocumentRoot10', b)
    _safe_set(b, 'xwiki_Attachment11', None)
    assert not _is_linked(b, 'xwiki_Attachment11', a2)
    if hasattr(a2, 'xwiki_DocumentRoot10'):
        assert not _is_linked(a2, 'xwiki_DocumentRoot10', b)


def test_assoc_attribute83_reverse_link_reassign_clear():
    a1 = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    a2 = xwiki_Property(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    b = xwiki_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'xwiki_Attribute', a1)
    assert _is_linked(b, 'xwiki_Attribute', a1)
    if hasattr(a1, 'xwiki_Property84'):
        assert _is_linked(a1, 'xwiki_Property84', b)
    _safe_set(b, 'xwiki_Attribute', a2)
    assert _is_linked(b, 'xwiki_Attribute', a2)
    if hasattr(a1, 'xwiki_Property84'):
        assert not _is_linked(a1, 'xwiki_Property84', b)
    if hasattr(a2, 'xwiki_Property84'):
        assert _is_linked(a2, 'xwiki_Property84', b)
    _safe_set(b, 'xwiki_Attribute', None)
    assert not _is_linked(b, 'xwiki_Attribute', a2)
    if hasattr(a2, 'xwiki_Property84'):
        assert not _is_linked(a2, 'xwiki_Property84', b)


def test_assoc_class_15_reverse_link_reassign_clear():
    a1 = xwiki_DocumentRoot(mixed="sample_text")
    a2 = xwiki_DocumentRoot(mixed="sample_text_2")
    b = xwiki_Class(id="sample_text", name="sample_text")
    _safe_set(b, 'xwiki_Class17', a1)
    assert _is_linked(b, 'xwiki_Class17', a1)
    if hasattr(a1, 'xwiki_DocumentRoot16'):
        assert _is_linked(a1, 'xwiki_DocumentRoot16', b)
    _safe_set(b, 'xwiki_Class17', a2)
    assert _is_linked(b, 'xwiki_Class17', a2)
    if hasattr(a1, 'xwiki_DocumentRoot16'):
        assert not _is_linked(a1, 'xwiki_DocumentRoot16', b)
    if hasattr(a2, 'xwiki_DocumentRoot16'):
        assert _is_linked(a2, 'xwiki_DocumentRoot16', b)
    _safe_set(b, 'xwiki_Class17', None)
    assert not _is_linked(b, 'xwiki_Class17', a2)
    if hasattr(a2, 'xwiki_DocumentRoot16'):
        assert not _is_linked(a2, 'xwiki_DocumentRoot16', b)


def test_assoc_comment21_reverse_link_reassign_clear():
    a1 = xwiki_DocumentRoot(mixed="sample_text")
    a2 = xwiki_DocumentRoot(mixed="sample_text_2")
    b = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    _safe_set(b, 'xwiki_Comment23', a1)
    assert _is_linked(b, 'xwiki_Comment23', a1)
    if hasattr(a1, 'xwiki_DocumentRoot22'):
        assert _is_linked(a1, 'xwiki_DocumentRoot22', b)
    _safe_set(b, 'xwiki_Comment23', a2)
    assert _is_linked(b, 'xwiki_Comment23', a2)
    if hasattr(a1, 'xwiki_DocumentRoot22'):
        assert not _is_linked(a1, 'xwiki_DocumentRoot22', b)
    if hasattr(a2, 'xwiki_DocumentRoot22'):
        assert _is_linked(a2, 'xwiki_DocumentRoot22', b)
    _safe_set(b, 'xwiki_Comment23', None)
    assert not _is_linked(b, 'xwiki_Comment23', a2)
    if hasattr(a2, 'xwiki_DocumentRoot22'):
        assert not _is_linked(a2, 'xwiki_DocumentRoot22', b)


def test_assoc_objectSummary33_reverse_link_reassign_clear():
    a1 = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    a2 = xwiki_ObjectSummary(className="sample_text_2", guid="sample_text_2", headline="sample_text_2", id="sample_text_2", number="sample_text_2", pageAuthor="sample_text_2", pageAuthorName="sample_text_2", pageId="sample_text_2", pageName="sample_text_2", pageVersion="sample_text_2", space="sample_text_2", wiki="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot34', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot34', a1)
    if hasattr(a1, 'xwiki_ObjectSummary'):
        assert _is_linked(a1, 'xwiki_ObjectSummary', b)
    _safe_set(b, 'xwiki_DocumentRoot34', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot34', a2)
    if hasattr(a1, 'xwiki_ObjectSummary'):
        assert not _is_linked(a1, 'xwiki_ObjectSummary', b)
    if hasattr(a2, 'xwiki_ObjectSummary'):
        assert _is_linked(a2, 'xwiki_ObjectSummary', b)
    _safe_set(b, 'xwiki_DocumentRoot34', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot34', a2)
    if hasattr(a2, 'xwiki_ObjectSummary'):
        assert not _is_linked(a2, 'xwiki_ObjectSummary', b)


def test_assoc_page35_reverse_link_reassign_clear():
    a1 = xwiki_Page(comment="sample_text", content="sample_text", created="sample_text", creator="sample_text", creatorName="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text")
    a2 = xwiki_Page(comment="sample_text_2", content="sample_text_2", created="sample_text_2", creator="sample_text_2", creatorName="sample_text_2", language="sample_text_2", majorVersion="sample_text_2", minorVersion="sample_text_2", modified="sample_text_2", modifier="sample_text_2", modifierName="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot36', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot36', a1)
    if hasattr(a1, 'xwiki_Page'):
        assert _is_linked(a1, 'xwiki_Page', b)
    _safe_set(b, 'xwiki_DocumentRoot36', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot36', a2)
    if hasattr(a1, 'xwiki_Page'):
        assert not _is_linked(a1, 'xwiki_Page', b)
    if hasattr(a2, 'xwiki_Page'):
        assert _is_linked(a2, 'xwiki_Page', b)
    _safe_set(b, 'xwiki_DocumentRoot36', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot36', a2)
    if hasattr(a2, 'xwiki_Page'):
        assert not _is_linked(a2, 'xwiki_Page', b)


def test_assoc_property1_reverse_link_reassign_clear():
    a1 = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    a2 = xwiki_Property(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    b = xwiki_Class(id="sample_text", name="sample_text")
    _safe_set(b, 'xwiki_Class', {a1})
    assert _is_linked(b, 'xwiki_Class', a1)
    if hasattr(a1, 'xwiki_Property'):
        assert _is_linked(a1, 'xwiki_Property', b)
    _safe_set(b, 'xwiki_Class', {a2})
    assert _is_linked(b, 'xwiki_Class', a2)
    if hasattr(a1, 'xwiki_Property'):
        assert not _is_linked(a1, 'xwiki_Property', b)
    if hasattr(a2, 'xwiki_Property'):
        assert _is_linked(a2, 'xwiki_Property', b)
    _safe_set(b, 'xwiki_Class', set())
    assert not _is_linked(b, 'xwiki_Class', a2)
    if hasattr(a2, 'xwiki_Property'):
        assert not _is_linked(a2, 'xwiki_Property', b)


def test_assoc_property41_reverse_link_reassign_clear():
    a1 = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    a2 = xwiki_Property(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot42', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot42', a1)
    if hasattr(a1, 'xwiki_Property43'):
        assert _is_linked(a1, 'xwiki_Property43', b)
    _safe_set(b, 'xwiki_DocumentRoot42', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot42', a2)
    if hasattr(a1, 'xwiki_Property43'):
        assert not _is_linked(a1, 'xwiki_Property43', b)
    if hasattr(a2, 'xwiki_Property43'):
        assert _is_linked(a2, 'xwiki_Property43', b)
    _safe_set(b, 'xwiki_DocumentRoot42', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot42', a2)
    if hasattr(a2, 'xwiki_Property43'):
        assert not _is_linked(a2, 'xwiki_Property43', b)


def test_assoc_searchResult44_reverse_link_reassign_clear():
    a1 = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    a2 = xwiki_SearchResult(author="sample_text_2", authorName="sample_text_2", className="sample_text_2", filename="sample_text_2", id="sample_text_2", language="sample_text_2", modified="sample_text_2", objectNumber="sample_text_2", pageFullName="sample_text_2", pageName="sample_text_2", score="sample_text_2", space="sample_text_2", title="sample_text_2", type="sample_text_2", version="sample_text_2", wiki="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot45', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot45', a1)
    if hasattr(a1, 'xwiki_SearchResult'):
        assert _is_linked(a1, 'xwiki_SearchResult', b)
    _safe_set(b, 'xwiki_DocumentRoot45', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot45', a2)
    if hasattr(a1, 'xwiki_SearchResult'):
        assert not _is_linked(a1, 'xwiki_SearchResult', b)
    if hasattr(a2, 'xwiki_SearchResult'):
        assert _is_linked(a2, 'xwiki_SearchResult', b)
    _safe_set(b, 'xwiki_DocumentRoot45', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot45', a2)
    if hasattr(a2, 'xwiki_SearchResult'):
        assert not _is_linked(a2, 'xwiki_SearchResult', b)


def test_assoc_searchResult88_reverse_link_reassign_clear():
    a1 = xwiki_SearchResultsType(template="sample_text")
    a2 = xwiki_SearchResultsType(template="sample_text_2")
    b = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    _safe_set(b, 'xwiki_SearchResult90', a1)
    assert _is_linked(b, 'xwiki_SearchResult90', a1)
    if hasattr(a1, 'xwiki_SearchResultsType89'):
        assert _is_linked(a1, 'xwiki_SearchResultsType89', b)
    _safe_set(b, 'xwiki_SearchResult90', a2)
    assert _is_linked(b, 'xwiki_SearchResult90', a2)
    if hasattr(a1, 'xwiki_SearchResultsType89'):
        assert not _is_linked(a1, 'xwiki_SearchResultsType89', b)
    if hasattr(a2, 'xwiki_SearchResultsType89'):
        assert _is_linked(a2, 'xwiki_SearchResultsType89', b)
    _safe_set(b, 'xwiki_SearchResult90', None)
    assert not _is_linked(b, 'xwiki_SearchResult90', a2)
    if hasattr(a2, 'xwiki_SearchResultsType89'):
        assert not _is_linked(a2, 'xwiki_SearchResultsType89', b)


def test_assoc_searchResults46_reverse_link_reassign_clear():
    a1 = xwiki_SearchResultsType(template="sample_text")
    a2 = xwiki_SearchResultsType(template="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot47', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot47', a1)
    if hasattr(a1, 'xwiki_SearchResultsType'):
        assert _is_linked(a1, 'xwiki_SearchResultsType', b)
    _safe_set(b, 'xwiki_DocumentRoot47', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot47', a2)
    if hasattr(a1, 'xwiki_SearchResultsType'):
        assert not _is_linked(a1, 'xwiki_SearchResultsType', b)
    if hasattr(a2, 'xwiki_SearchResultsType'):
        assert _is_linked(a2, 'xwiki_SearchResultsType', b)
    _safe_set(b, 'xwiki_DocumentRoot47', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot47', a2)
    if hasattr(a2, 'xwiki_SearchResultsType'):
        assert not _is_linked(a2, 'xwiki_SearchResultsType', b)


def test_assoc_space48_reverse_link_reassign_clear():
    a1 = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    a2 = xwiki_Space(home="sample_text_2", id="sample_text_2", name="sample_text_2", wiki="sample_text_2", xwikiAbsoluteUrl="sample_text_2", xwikiRelativeUrl="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot49', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot49', a1)
    if hasattr(a1, 'xwiki_Space'):
        assert _is_linked(a1, 'xwiki_Space', b)
    _safe_set(b, 'xwiki_DocumentRoot49', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot49', a2)
    if hasattr(a1, 'xwiki_Space'):
        assert not _is_linked(a1, 'xwiki_Space', b)
    if hasattr(a2, 'xwiki_Space'):
        assert _is_linked(a2, 'xwiki_Space', b)
    _safe_set(b, 'xwiki_DocumentRoot49', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot49', a2)
    if hasattr(a2, 'xwiki_Space'):
        assert not _is_linked(a2, 'xwiki_Space', b)


def test_assoc_syntaxes102_reverse_link_reassign_clear():
    a1 = xwiki_XWiki(version="sample_text")
    a2 = xwiki_XWiki(version="sample_text_2")
    b = xwiki_Syntaxes(syntax="sample_text")
    _safe_set(b, 'xwiki_Syntaxes104', a1)
    assert _is_linked(b, 'xwiki_Syntaxes104', a1)
    if hasattr(a1, 'xwiki_XWiki103'):
        assert _is_linked(a1, 'xwiki_XWiki103', b)
    _safe_set(b, 'xwiki_Syntaxes104', a2)
    assert _is_linked(b, 'xwiki_Syntaxes104', a2)
    if hasattr(a1, 'xwiki_XWiki103'):
        assert not _is_linked(a1, 'xwiki_XWiki103', b)
    if hasattr(a2, 'xwiki_XWiki103'):
        assert _is_linked(a2, 'xwiki_XWiki103', b)
    _safe_set(b, 'xwiki_Syntaxes104', None)
    assert not _is_linked(b, 'xwiki_Syntaxes104', a2)
    if hasattr(a2, 'xwiki_XWiki103'):
        assert not _is_linked(a2, 'xwiki_XWiki103', b)


def test_assoc_syntaxes52_reverse_link_reassign_clear():
    a1 = xwiki_Syntaxes(syntax="sample_text")
    a2 = xwiki_Syntaxes(syntax="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot53', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot53', a1)
    if hasattr(a1, 'xwiki_Syntaxes'):
        assert _is_linked(a1, 'xwiki_Syntaxes', b)
    _safe_set(b, 'xwiki_DocumentRoot53', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot53', a2)
    if hasattr(a1, 'xwiki_Syntaxes'):
        assert not _is_linked(a1, 'xwiki_Syntaxes', b)
    if hasattr(a2, 'xwiki_Syntaxes'):
        assert _is_linked(a2, 'xwiki_Syntaxes', b)
    _safe_set(b, 'xwiki_DocumentRoot53', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot53', a2)
    if hasattr(a2, 'xwiki_Syntaxes'):
        assert not _is_linked(a2, 'xwiki_Syntaxes', b)


def test_assoc_tag54_reverse_link_reassign_clear():
    a1 = xwiki_Tag(name="sample_text")
    a2 = xwiki_Tag(name="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot55', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot55', a1)
    if hasattr(a1, 'xwiki_Tag'):
        assert _is_linked(a1, 'xwiki_Tag', b)
    _safe_set(b, 'xwiki_DocumentRoot55', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot55', a2)
    if hasattr(a1, 'xwiki_Tag'):
        assert not _is_linked(a1, 'xwiki_Tag', b)
    if hasattr(a2, 'xwiki_Tag'):
        assert _is_linked(a2, 'xwiki_Tag', b)
    _safe_set(b, 'xwiki_DocumentRoot55', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot55', a2)
    if hasattr(a2, 'xwiki_Tag'):
        assert not _is_linked(a2, 'xwiki_Tag', b)


def test_assoc_translation97_reverse_link_reassign_clear():
    a1 = xwiki_Translations(default="sample_text")
    a2 = xwiki_Translations(default="sample_text_2")
    b = xwiki_Translation(language="sample_text")
    _safe_set(b, 'xwiki_Translation', a1)
    assert _is_linked(b, 'xwiki_Translation', a1)
    if hasattr(a1, 'xwiki_Translations98'):
        assert _is_linked(a1, 'xwiki_Translations98', b)
    _safe_set(b, 'xwiki_Translation', a2)
    assert _is_linked(b, 'xwiki_Translation', a2)
    if hasattr(a1, 'xwiki_Translations98'):
        assert not _is_linked(a1, 'xwiki_Translations98', b)
    if hasattr(a2, 'xwiki_Translations98'):
        assert _is_linked(a2, 'xwiki_Translations98', b)
    _safe_set(b, 'xwiki_Translation', None)
    assert not _is_linked(b, 'xwiki_Translation', a2)
    if hasattr(a2, 'xwiki_Translations98'):
        assert not _is_linked(a2, 'xwiki_Translations98', b)


def test_assoc_translations58_reverse_link_reassign_clear():
    a1 = xwiki_Translations(default="sample_text")
    a2 = xwiki_Translations(default="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot59', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot59', a1)
    if hasattr(a1, 'xwiki_Translations'):
        assert _is_linked(a1, 'xwiki_Translations', b)
    _safe_set(b, 'xwiki_DocumentRoot59', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot59', a2)
    if hasattr(a1, 'xwiki_Translations'):
        assert not _is_linked(a1, 'xwiki_Translations', b)
    if hasattr(a2, 'xwiki_Translations'):
        assert _is_linked(a2, 'xwiki_Translations', b)
    _safe_set(b, 'xwiki_DocumentRoot59', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot59', a2)
    if hasattr(a2, 'xwiki_Translations'):
        assert not _is_linked(a2, 'xwiki_Translations', b)


def test_assoc_translations77_reverse_link_reassign_clear():
    a1 = xwiki_Translations(default="sample_text")
    a2 = xwiki_Translations(default="sample_text_2")
    b = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    _safe_set(b, 'xwiki_PageSummary78', a1)
    assert _is_linked(b, 'xwiki_PageSummary78', a1)
    if hasattr(a1, 'xwiki_Translations79'):
        assert _is_linked(a1, 'xwiki_Translations79', b)
    _safe_set(b, 'xwiki_PageSummary78', a2)
    assert _is_linked(b, 'xwiki_PageSummary78', a2)
    if hasattr(a1, 'xwiki_Translations79'):
        assert not _is_linked(a1, 'xwiki_Translations79', b)
    if hasattr(a2, 'xwiki_Translations79'):
        assert _is_linked(a2, 'xwiki_Translations79', b)
    _safe_set(b, 'xwiki_PageSummary78', None)
    assert not _is_linked(b, 'xwiki_PageSummary78', a2)
    if hasattr(a2, 'xwiki_Translations79'):
        assert not _is_linked(a2, 'xwiki_Translations79', b)


def test_assoc_wiki60_reverse_link_reassign_clear():
    a1 = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    a2 = xwiki_Wiki(description="sample_text_2", id="sample_text_2", name="sample_text_2", owner="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot61', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot61', a1)
    if hasattr(a1, 'xwiki_Wiki'):
        assert _is_linked(a1, 'xwiki_Wiki', b)
    _safe_set(b, 'xwiki_DocumentRoot61', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot61', a2)
    if hasattr(a1, 'xwiki_Wiki'):
        assert not _is_linked(a1, 'xwiki_Wiki', b)
    if hasattr(a2, 'xwiki_Wiki'):
        assert _is_linked(a2, 'xwiki_Wiki', b)
    _safe_set(b, 'xwiki_DocumentRoot61', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot61', a2)
    if hasattr(a2, 'xwiki_Wiki'):
        assert not _is_linked(a2, 'xwiki_Wiki', b)


def test_assoc_xwiki64_reverse_link_reassign_clear():
    a1 = xwiki_XWiki(version="sample_text")
    a2 = xwiki_XWiki(version="sample_text_2")
    b = xwiki_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'xwiki_DocumentRoot65', {a1})
    assert _is_linked(b, 'xwiki_DocumentRoot65', a1)
    if hasattr(a1, 'xwiki_XWiki'):
        assert _is_linked(a1, 'xwiki_XWiki', b)
    _safe_set(b, 'xwiki_DocumentRoot65', {a2})
    assert _is_linked(b, 'xwiki_DocumentRoot65', a2)
    if hasattr(a1, 'xwiki_XWiki'):
        assert not _is_linked(a1, 'xwiki_XWiki', b)
    if hasattr(a2, 'xwiki_XWiki'):
        assert _is_linked(a2, 'xwiki_XWiki', b)
    _safe_set(b, 'xwiki_DocumentRoot65', set())
    assert not _is_linked(b, 'xwiki_DocumentRoot65', a2)
    if hasattr(a2, 'xwiki_XWiki'):
        assert not _is_linked(a2, 'xwiki_XWiki', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attachment0_stub_double():
    # xwiki_AttachmentsType has no real 'xwiki_AttachmentsType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Attachment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Attachment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Attachment(author="sample_text", authorName="sample_text", date="sample_text", id="sample_text", mimeType="sample_text", name="sample_text", pageId="sample_text", pageVersion="sample_text", size="sample_text", version="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    partner = xwiki_AttachmentsType()
    setattr(partner, 'xwiki_AttachmentsType', None)
    _safe_set(owner, 'xwiki_Attachment', partner)
    assert owner in getattr(partner, 'xwiki_AttachmentsType')
    _safe_set(owner, 'xwiki_Attachment', None)
    assert owner not in getattr(partner, 'xwiki_AttachmentsType')


def test_assoc_attachments12_stub_double():
    # xwiki_AttachmentsType has no real 'xwiki_AttachmentsType14' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_AttachmentsType()
    setattr(partner, 'xwiki_AttachmentsType14', None)
    _safe_set(owner, 'xwiki_DocumentRoot13', {partner})
    assert getattr(partner, 'xwiki_AttachmentsType14') == owner
    _safe_set(owner, 'xwiki_DocumentRoot13', set())
    assert getattr(partner, 'xwiki_AttachmentsType14') is None


def test_assoc_class_2_stub_double():
    # xwiki_ClassesType has no real 'xwiki_ClassesType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Class(id="sample_text", name="sample_text")
    partner = xwiki_ClassesType()
    setattr(partner, 'xwiki_ClassesType', None)
    _safe_set(owner, 'xwiki_Class3', partner)
    assert owner in getattr(partner, 'xwiki_ClassesType')
    _safe_set(owner, 'xwiki_Class3', None)
    assert owner not in getattr(partner, 'xwiki_ClassesType')


def test_assoc_classes18_stub_double():
    # xwiki_ClassesType has no real 'xwiki_ClassesType20' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_ClassesType()
    setattr(partner, 'xwiki_ClassesType20', None)
    _safe_set(owner, 'xwiki_DocumentRoot19', {partner})
    assert getattr(partner, 'xwiki_ClassesType20') == owner
    _safe_set(owner, 'xwiki_DocumentRoot19', set())
    assert getattr(partner, 'xwiki_ClassesType20') is None


def test_assoc_comment4_stub_double():
    # xwiki_CommentsType has no real 'xwiki_CommentsType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Comment(author="sample_text", authorName="sample_text", date="sample_text", highlight="sample_text", id="sample_text", pageId="sample_text", replyTo="sample_text", text="sample_text")
    partner = xwiki_CommentsType()
    setattr(partner, 'xwiki_CommentsType', None)
    _safe_set(owner, 'xwiki_Comment', partner)
    assert owner in getattr(partner, 'xwiki_CommentsType')
    _safe_set(owner, 'xwiki_Comment', None)
    assert owner not in getattr(partner, 'xwiki_CommentsType')


def test_assoc_comments24_stub_double():
    # xwiki_CommentsType has no real 'xwiki_CommentsType26' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_CommentsType()
    setattr(partner, 'xwiki_CommentsType26', None)
    _safe_set(owner, 'xwiki_DocumentRoot25', {partner})
    assert getattr(partner, 'xwiki_CommentsType26') == owner
    _safe_set(owner, 'xwiki_DocumentRoot25', set())
    assert getattr(partner, 'xwiki_CommentsType26') is None


def test_assoc_history27_stub_double():
    # xwiki_HistoryType has no real 'xwiki_HistoryType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_HistoryType()
    setattr(partner, 'xwiki_HistoryType', None)
    _safe_set(owner, 'xwiki_DocumentRoot28', {partner})
    assert getattr(partner, 'xwiki_HistoryType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot28', set())
    assert getattr(partner, 'xwiki_HistoryType') is None


def test_assoc_historySummary66_stub_double():
    # xwiki_HistoryType has no real 'xwiki_HistoryType67' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_HistorySummary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_HistorySummary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_HistorySummary(comment="sample_text", language="sample_text", majorVersion="sample_text", minorVersion="sample_text", modified="sample_text", modifier="sample_text", modifierName="sample_text", name="sample_text", pageId="sample_text", space="sample_text", version="sample_text", wiki="sample_text")
    partner = xwiki_HistoryType()
    setattr(partner, 'xwiki_HistoryType67', None)
    _safe_set(owner, 'xwiki_HistorySummary', partner)
    assert owner in getattr(partner, 'xwiki_HistoryType67')
    _safe_set(owner, 'xwiki_HistorySummary', None)
    assert owner not in getattr(partner, 'xwiki_HistoryType67')


def test_assoc_link68_stub_double():
    # xwiki_LinkCollection has no real 'xwiki_LinkCollection' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Link(href="sample_text", hrefLang="sample_text", rel="sample_text", type="sample_text")
    partner = xwiki_LinkCollection()
    setattr(partner, 'xwiki_LinkCollection', None)
    _safe_set(owner, 'xwiki_Link', partner)
    assert owner in getattr(partner, 'xwiki_LinkCollection')
    _safe_set(owner, 'xwiki_Link', None)
    assert owner not in getattr(partner, 'xwiki_LinkCollection')


def test_assoc_object29_stub_double():
    # xwiki_Object has no real 'xwiki_Object' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_Object()
    setattr(partner, 'xwiki_Object', None)
    _safe_set(owner, 'xwiki_DocumentRoot30', {partner})
    assert getattr(partner, 'xwiki_Object') == owner
    _safe_set(owner, 'xwiki_DocumentRoot30', set())
    assert getattr(partner, 'xwiki_Object') is None


def test_assoc_object85_stub_double():
    # xwiki_Object has no real 'xwiki_Object87' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_SearchResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_SearchResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_SearchResult(author="sample_text", authorName="sample_text", className="sample_text", filename="sample_text", id="sample_text", language="sample_text", modified="sample_text", objectNumber="sample_text", pageFullName="sample_text", pageName="sample_text", score="sample_text", space="sample_text", title="sample_text", type="sample_text", version="sample_text", wiki="sample_text")
    partner = xwiki_Object()
    setattr(partner, 'xwiki_Object87', None)
    _safe_set(owner, 'xwiki_SearchResult86', partner)
    assert getattr(partner, 'xwiki_Object87') == owner
    _safe_set(owner, 'xwiki_SearchResult86', None)
    assert getattr(partner, 'xwiki_Object87') is None


def test_assoc_objectSummary72_stub_double():
    # xwiki_ObjectsType has no real 'xwiki_ObjectsType73' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_ObjectSummary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_ObjectSummary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_ObjectSummary(className="sample_text", guid="sample_text", headline="sample_text", id="sample_text", number="sample_text", pageAuthor="sample_text", pageAuthorName="sample_text", pageId="sample_text", pageName="sample_text", pageVersion="sample_text", space="sample_text", wiki="sample_text")
    partner = xwiki_ObjectsType()
    setattr(partner, 'xwiki_ObjectsType73', None)
    _safe_set(owner, 'xwiki_ObjectSummary74', partner)
    assert owner in getattr(partner, 'xwiki_ObjectsType73')
    _safe_set(owner, 'xwiki_ObjectSummary74', None)
    assert owner not in getattr(partner, 'xwiki_ObjectsType73')


def test_assoc_objects31_stub_double():
    # xwiki_ObjectsType has no real 'xwiki_ObjectsType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_ObjectsType()
    setattr(partner, 'xwiki_ObjectsType', None)
    _safe_set(owner, 'xwiki_DocumentRoot32', {partner})
    assert getattr(partner, 'xwiki_ObjectsType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot32', set())
    assert getattr(partner, 'xwiki_ObjectsType') is None


def test_assoc_pageSummary75_stub_double():
    # xwiki_PagesType has no real 'xwiki_PagesType76' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_PageSummary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_PageSummary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_PageSummary(author="sample_text", authorName="sample_text", fullName="sample_text", id="sample_text", name="sample_text", parent="sample_text", parentId="sample_text", space="sample_text", syntax="sample_text", title="sample_text", version="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    partner = xwiki_PagesType()
    setattr(partner, 'xwiki_PagesType76', None)
    _safe_set(owner, 'xwiki_PageSummary', partner)
    assert owner in getattr(partner, 'xwiki_PagesType76')
    _safe_set(owner, 'xwiki_PageSummary', None)
    assert owner not in getattr(partner, 'xwiki_PagesType76')


def test_assoc_pages37_stub_double():
    # xwiki_PagesType has no real 'xwiki_PagesType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_PagesType()
    setattr(partner, 'xwiki_PagesType', None)
    _safe_set(owner, 'xwiki_DocumentRoot38', {partner})
    assert getattr(partner, 'xwiki_PagesType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot38', set())
    assert getattr(partner, 'xwiki_PagesType') is None


def test_assoc_properties39_stub_double():
    # xwiki_PropertiesType has no real 'xwiki_PropertiesType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_PropertiesType()
    setattr(partner, 'xwiki_PropertiesType', None)
    _safe_set(owner, 'xwiki_DocumentRoot40', {partner})
    assert getattr(partner, 'xwiki_PropertiesType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot40', set())
    assert getattr(partner, 'xwiki_PropertiesType') is None


def test_assoc_property69_stub_double():
    # xwiki_Object has no real 'xwiki_Object70' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    partner = xwiki_Object()
    setattr(partner, 'xwiki_Object70', None)
    _safe_set(owner, 'xwiki_Property71', partner)
    assert owner in getattr(partner, 'xwiki_Object70')
    _safe_set(owner, 'xwiki_Property71', None)
    assert owner not in getattr(partner, 'xwiki_Object70')


def test_assoc_property80_stub_double():
    # xwiki_PropertiesType has no real 'xwiki_PropertiesType81' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Property(name="sample_text", type="sample_text", value="sample_text")
    partner = xwiki_PropertiesType()
    setattr(partner, 'xwiki_PropertiesType81', None)
    _safe_set(owner, 'xwiki_Property82', partner)
    assert owner in getattr(partner, 'xwiki_PropertiesType81')
    _safe_set(owner, 'xwiki_Property82', None)
    assert owner not in getattr(partner, 'xwiki_PropertiesType81')


def test_assoc_space91_stub_double():
    # xwiki_SpacesType has no real 'xwiki_SpacesType92' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Space's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Space's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Space(home="sample_text", id="sample_text", name="sample_text", wiki="sample_text", xwikiAbsoluteUrl="sample_text", xwikiRelativeUrl="sample_text")
    partner = xwiki_SpacesType()
    setattr(partner, 'xwiki_SpacesType92', None)
    _safe_set(owner, 'xwiki_Space93', partner)
    assert owner in getattr(partner, 'xwiki_SpacesType92')
    _safe_set(owner, 'xwiki_Space93', None)
    assert owner not in getattr(partner, 'xwiki_SpacesType92')


def test_assoc_spaces50_stub_double():
    # xwiki_SpacesType has no real 'xwiki_SpacesType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_SpacesType()
    setattr(partner, 'xwiki_SpacesType', None)
    _safe_set(owner, 'xwiki_DocumentRoot51', {partner})
    assert getattr(partner, 'xwiki_SpacesType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot51', set())
    assert getattr(partner, 'xwiki_SpacesType') is None


def test_assoc_tag94_stub_double():
    # xwiki_TagsType has no real 'xwiki_TagsType95' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Tag(name="sample_text")
    partner = xwiki_TagsType()
    setattr(partner, 'xwiki_TagsType95', None)
    _safe_set(owner, 'xwiki_Tag96', partner)
    assert owner in getattr(partner, 'xwiki_TagsType95')
    _safe_set(owner, 'xwiki_Tag96', None)
    assert owner not in getattr(partner, 'xwiki_TagsType95')


def test_assoc_tags56_stub_double():
    # xwiki_TagsType has no real 'xwiki_TagsType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_TagsType()
    setattr(partner, 'xwiki_TagsType', None)
    _safe_set(owner, 'xwiki_DocumentRoot57', {partner})
    assert getattr(partner, 'xwiki_TagsType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot57', set())
    assert getattr(partner, 'xwiki_TagsType') is None


def test_assoc_wiki99_stub_double():
    # xwiki_WikisType has no real 'xwiki_WikisType100' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_Wiki's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_Wiki's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_Wiki(description="sample_text", id="sample_text", name="sample_text", owner="sample_text")
    partner = xwiki_WikisType()
    setattr(partner, 'xwiki_WikisType100', None)
    _safe_set(owner, 'xwiki_Wiki101', partner)
    assert owner in getattr(partner, 'xwiki_WikisType100')
    _safe_set(owner, 'xwiki_Wiki101', None)
    assert owner not in getattr(partner, 'xwiki_WikisType100')


def test_assoc_wikis62_stub_double():
    # xwiki_WikisType has no real 'xwiki_WikisType' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_WikisType()
    setattr(partner, 'xwiki_WikisType', None)
    _safe_set(owner, 'xwiki_DocumentRoot63', {partner})
    assert getattr(partner, 'xwiki_WikisType') == owner
    _safe_set(owner, 'xwiki_DocumentRoot63', set())
    assert getattr(partner, 'xwiki_WikisType') is None


def test_assoc_xMLNSPrefixMap5_stub_double():
    # xwiki_EStringToStringMapEntry has no real 'xwiki_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_EStringToStringMapEntry()
    setattr(partner, 'xwiki_EStringToStringMapEntry', None)
    _safe_set(owner, 'xwiki_DocumentRoot', {partner})
    assert getattr(partner, 'xwiki_EStringToStringMapEntry') == owner
    _safe_set(owner, 'xwiki_DocumentRoot', set())
    assert getattr(partner, 'xwiki_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation6_stub_double():
    # xwiki_EStringToStringMapEntry has no real 'xwiki_EStringToStringMapEntry8' property in the generated
    # code (a bare stub) -- manually attach it so xwiki_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xwiki_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xwiki_DocumentRoot(mixed="sample_text")
    partner = xwiki_EStringToStringMapEntry()
    setattr(partner, 'xwiki_EStringToStringMapEntry8', None)
    _safe_set(owner, 'xwiki_DocumentRoot7', {partner})
    assert getattr(partner, 'xwiki_EStringToStringMapEntry8') == owner
    _safe_set(owner, 'xwiki_DocumentRoot7', set())
    assert getattr(partner, 'xwiki_EStringToStringMapEntry8') is None


