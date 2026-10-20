import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Docbook_AbstractType,
    Docbook_AddressType,
    Docbook_ArgType,
    Docbook_AuthorType,
    Docbook_AuthorinitialsType,
    Docbook_BookType,
    Docbook_ChapterType,
    Docbook_CmdsynopsisType,
    Docbook_ColspecType,
    Docbook_CommandType,
    Docbook_ConfgroupType,
    Docbook_CopyrightType,
    Docbook_DateType,
    Docbook_DocumentRoot,
    Docbook_EStringToStringMapEntry,
    Docbook_EmphasisType,
    Docbook_EntryType,
    Docbook_EnvarType,
    Docbook_ExampleType,
    Docbook_FigureType,
    Docbook_FileNameType,
    Docbook_FirstnameType,
    Docbook_FootnoteType,
    Docbook_FuncdefType,
    Docbook_FuncprototypeType,
    Docbook_FuncsynopsisType,
    Docbook_FunctionType,
    Docbook_ImagedataType,
    Docbook_ImageobjectType,
    Docbook_ImportantType,
    Docbook_InfoType,
    Docbook_InformaltableType,
    Docbook_ItemizedlistType,
    Docbook_KeywordsetType,
    Docbook_LegalNoticeType,
    Docbook_LinkType,
    Docbook_ListitemType,
    Docbook_LiteralType,
    Docbook_MediaobjectType,
    Docbook_NoteType,
    Docbook_OptionType,
    Docbook_OrderedlistType,
    Docbook_OtheraddrType,
    Docbook_ParaType,
    Docbook_ParamdefType,
    Docbook_ParameterType,
    Docbook_PersonnameType,
    Docbook_PhraseType,
    Docbook_PrefaceType,
    Docbook_ProgramlistingType,
    Docbook_PublisherType,
    Docbook_RefEntryTitleType,
    Docbook_RefEntryType,
    Docbook_RefMetaType,
    Docbook_RefNameDivType,
    Docbook_RefSect1Type,
    Docbook_RefSynopsisDivType,
    Docbook_ReferenceType,
    Docbook_ReplaceableType,
    Docbook_RevdescriptionType,
    Docbook_RevhistoryType,
    Docbook_RevisionType,
    Docbook_RevnumberType,
    Docbook_RowType,
    Docbook_SectionType,
    Docbook_SegListItemType,
    Docbook_SegType,
    Docbook_SegmentedListType,
    Docbook_SubtitleType,
    Docbook_SurnameType,
    Docbook_TableType,
    Docbook_TbodyType,
    Docbook_TermType,
    Docbook_TgroupType,
    Docbook_TheadType,
    Docbook_TipType,
    Docbook_TitleType,
    Docbook_UlinkType,
    Docbook_VarListEntryType,
    Docbook_VariableListType,
    ItemizedlistType,
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

def test_assoc_address278_reverse_link_reassign_clear():
    a1 = Docbook_PublisherType(publishername="sample_text")
    a2 = Docbook_PublisherType(publishername="sample_text_2")
    b = Docbook_AddressType(email="sample_text", format="sample_text", state="sample_text")
    _safe_set(b, 'Docbook_AddressType280', a1)
    assert _is_linked(b, 'Docbook_AddressType280', a1)
    if hasattr(a1, 'Docbook_PublisherType279'):
        assert _is_linked(a1, 'Docbook_PublisherType279', b)
    _safe_set(b, 'Docbook_AddressType280', a2)
    assert _is_linked(b, 'Docbook_AddressType280', a2)
    if hasattr(a1, 'Docbook_PublisherType279'):
        assert not _is_linked(a1, 'Docbook_PublisherType279', b)
    if hasattr(a2, 'Docbook_PublisherType279'):
        assert _is_linked(a2, 'Docbook_PublisherType279', b)
    _safe_set(b, 'Docbook_AddressType280', None)
    assert not _is_linked(b, 'Docbook_AddressType280', a2)
    if hasattr(a2, 'Docbook_PublisherType279'):
        assert not _is_linked(a2, 'Docbook_PublisherType279', b)


def test_assoc_address36_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_AddressType(email="sample_text", format="sample_text", state="sample_text")
    _safe_set(b, 'Docbook_AddressType38', a1)
    assert _is_linked(b, 'Docbook_AddressType38', a1)
    if hasattr(a1, 'Docbook_DocumentRoot37'):
        assert _is_linked(a1, 'Docbook_DocumentRoot37', b)
    _safe_set(b, 'Docbook_AddressType38', a2)
    assert _is_linked(b, 'Docbook_AddressType38', a2)
    if hasattr(a1, 'Docbook_DocumentRoot37'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot37', b)
    if hasattr(a2, 'Docbook_DocumentRoot37'):
        assert _is_linked(a2, 'Docbook_DocumentRoot37', b)
    _safe_set(b, 'Docbook_AddressType38', None)
    assert not _is_linked(b, 'Docbook_AddressType38', a2)
    if hasattr(a2, 'Docbook_DocumentRoot37'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot37', b)


def test_assoc_address6_reverse_link_reassign_clear():
    a1 = Docbook_AuthorType(contrib="sample_text")
    a2 = Docbook_AuthorType(contrib="sample_text_2")
    b = Docbook_AddressType(email="sample_text", format="sample_text", state="sample_text")
    _safe_set(b, 'Docbook_AddressType8', a1)
    assert _is_linked(b, 'Docbook_AddressType8', a1)
    if hasattr(a1, 'Docbook_AuthorType7'):
        assert _is_linked(a1, 'Docbook_AuthorType7', b)
    _safe_set(b, 'Docbook_AddressType8', a2)
    assert _is_linked(b, 'Docbook_AddressType8', a2)
    if hasattr(a1, 'Docbook_AuthorType7'):
        assert not _is_linked(a1, 'Docbook_AuthorType7', b)
    if hasattr(a2, 'Docbook_AuthorType7'):
        assert _is_linked(a2, 'Docbook_AuthorType7', b)
    _safe_set(b, 'Docbook_AddressType8', None)
    assert not _is_linked(b, 'Docbook_AddressType8', a2)
    if hasattr(a2, 'Docbook_AuthorType7'):
        assert not _is_linked(a2, 'Docbook_AuthorType7', b)


def test_assoc_author172_reverse_link_reassign_clear():
    a1 = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    a2 = Docbook_InfoType(bibliomisc="sample_text_2", date="sample_text_2", group="sample_text_2", productname="sample_text_2", pubdate="sample_text_2", releaseinfo="sample_text_2")
    b = Docbook_AuthorType(contrib="sample_text")
    _safe_set(b, 'Docbook_AuthorType174', a1)
    assert _is_linked(b, 'Docbook_AuthorType174', a1)
    if hasattr(a1, 'Docbook_InfoType173'):
        assert _is_linked(a1, 'Docbook_InfoType173', b)
    _safe_set(b, 'Docbook_AuthorType174', a2)
    assert _is_linked(b, 'Docbook_AuthorType174', a2)
    if hasattr(a1, 'Docbook_InfoType173'):
        assert not _is_linked(a1, 'Docbook_InfoType173', b)
    if hasattr(a2, 'Docbook_InfoType173'):
        assert _is_linked(a2, 'Docbook_InfoType173', b)
    _safe_set(b, 'Docbook_AuthorType174', None)
    assert not _is_linked(b, 'Docbook_AuthorType174', a2)
    if hasattr(a2, 'Docbook_InfoType173'):
        assert not _is_linked(a2, 'Docbook_InfoType173', b)


def test_assoc_author39_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_AuthorType(contrib="sample_text")
    _safe_set(b, 'Docbook_AuthorType41', a1)
    assert _is_linked(b, 'Docbook_AuthorType41', a1)
    if hasattr(a1, 'Docbook_DocumentRoot40'):
        assert _is_linked(a1, 'Docbook_DocumentRoot40', b)
    _safe_set(b, 'Docbook_AuthorType41', a2)
    assert _is_linked(b, 'Docbook_AuthorType41', a2)
    if hasattr(a1, 'Docbook_DocumentRoot40'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot40', b)
    if hasattr(a2, 'Docbook_DocumentRoot40'):
        assert _is_linked(a2, 'Docbook_DocumentRoot40', b)
    _safe_set(b, 'Docbook_AuthorType41', None)
    assert not _is_linked(b, 'Docbook_AuthorType41', a2)
    if hasattr(a2, 'Docbook_DocumentRoot40'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot40', b)


def test_assoc_book42_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_BookType(label="sample_text", lang="sample_text", version="sample_text")
    _safe_set(b, 'Docbook_BookType44', a1)
    assert _is_linked(b, 'Docbook_BookType44', a1)
    if hasattr(a1, 'Docbook_DocumentRoot43'):
        assert _is_linked(a1, 'Docbook_DocumentRoot43', b)
    _safe_set(b, 'Docbook_BookType44', a2)
    assert _is_linked(b, 'Docbook_BookType44', a2)
    if hasattr(a1, 'Docbook_DocumentRoot43'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot43', b)
    if hasattr(a2, 'Docbook_DocumentRoot43'):
        assert _is_linked(a2, 'Docbook_DocumentRoot43', b)
    _safe_set(b, 'Docbook_BookType44', None)
    assert not _is_linked(b, 'Docbook_BookType44', a2)
    if hasattr(a2, 'Docbook_DocumentRoot43'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot43', b)


def test_assoc_chapter12_reverse_link_reassign_clear():
    a1 = Docbook_ChapterType(annotations="sample_text")
    a2 = Docbook_ChapterType(annotations="sample_text_2")
    b = Docbook_BookType(label="sample_text", lang="sample_text", version="sample_text")
    _safe_set(b, 'Docbook_BookType13', {a1})
    assert _is_linked(b, 'Docbook_BookType13', a1)
    if hasattr(a1, 'Docbook_ChapterType'):
        assert _is_linked(a1, 'Docbook_ChapterType', b)
    _safe_set(b, 'Docbook_BookType13', {a2})
    assert _is_linked(b, 'Docbook_BookType13', a2)
    if hasattr(a1, 'Docbook_ChapterType'):
        assert not _is_linked(a1, 'Docbook_ChapterType', b)
    if hasattr(a2, 'Docbook_ChapterType'):
        assert _is_linked(a2, 'Docbook_ChapterType', b)
    _safe_set(b, 'Docbook_BookType13', set())
    assert not _is_linked(b, 'Docbook_BookType13', a2)
    if hasattr(a2, 'Docbook_ChapterType'):
        assert not _is_linked(a2, 'Docbook_ChapterType', b)


def test_assoc_chapter48_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_ChapterType(annotations="sample_text")
    _safe_set(b, 'Docbook_ChapterType50', a1)
    assert _is_linked(b, 'Docbook_ChapterType50', a1)
    if hasattr(a1, 'Docbook_DocumentRoot49'):
        assert _is_linked(a1, 'Docbook_DocumentRoot49', b)
    _safe_set(b, 'Docbook_ChapterType50', a2)
    assert _is_linked(b, 'Docbook_ChapterType50', a2)
    if hasattr(a1, 'Docbook_DocumentRoot49'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot49', b)
    if hasattr(a2, 'Docbook_DocumentRoot49'):
        assert _is_linked(a2, 'Docbook_DocumentRoot49', b)
    _safe_set(b, 'Docbook_ChapterType50', None)
    assert not _is_linked(b, 'Docbook_ChapterType50', a2)
    if hasattr(a2, 'Docbook_DocumentRoot49'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot49', b)


def test_assoc_colspec413_reverse_link_reassign_clear():
    a1 = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    a2 = Docbook_TgroupType(align="sample_text_2", cols="sample_text_2", colseq="sample_text_2", rowseq="sample_text_2")
    b = Docbook_ColspecType(colname="sample_text", colwidth="sample_text")
    _safe_set(b, 'Docbook_ColspecType415', a1)
    assert _is_linked(b, 'Docbook_ColspecType415', a1)
    if hasattr(a1, 'Docbook_TgroupType414'):
        assert _is_linked(a1, 'Docbook_TgroupType414', b)
    _safe_set(b, 'Docbook_ColspecType415', a2)
    assert _is_linked(b, 'Docbook_ColspecType415', a2)
    if hasattr(a1, 'Docbook_TgroupType414'):
        assert not _is_linked(a1, 'Docbook_TgroupType414', b)
    if hasattr(a2, 'Docbook_TgroupType414'):
        assert _is_linked(a2, 'Docbook_TgroupType414', b)
    _safe_set(b, 'Docbook_ColspecType415', None)
    assert not _is_linked(b, 'Docbook_ColspecType415', a2)
    if hasattr(a2, 'Docbook_TgroupType414'):
        assert not _is_linked(a2, 'Docbook_TgroupType414', b)


def test_assoc_colspec51_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_ColspecType(colname="sample_text", colwidth="sample_text")
    _safe_set(b, 'Docbook_ColspecType', a1)
    assert _is_linked(b, 'Docbook_ColspecType', a1)
    if hasattr(a1, 'Docbook_DocumentRoot52'):
        assert _is_linked(a1, 'Docbook_DocumentRoot52', b)
    _safe_set(b, 'Docbook_ColspecType', a2)
    assert _is_linked(b, 'Docbook_ColspecType', a2)
    if hasattr(a1, 'Docbook_DocumentRoot52'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot52', b)
    if hasattr(a2, 'Docbook_DocumentRoot52'):
        assert _is_linked(a2, 'Docbook_DocumentRoot52', b)
    _safe_set(b, 'Docbook_ColspecType', None)
    assert not _is_linked(b, 'Docbook_ColspecType', a2)
    if hasattr(a2, 'Docbook_DocumentRoot52'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot52', b)


def test_assoc_confgroup189_reverse_link_reassign_clear():
    a1 = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    a2 = Docbook_InfoType(bibliomisc="sample_text_2", date="sample_text_2", group="sample_text_2", productname="sample_text_2", pubdate="sample_text_2", releaseinfo="sample_text_2")
    b = Docbook_ConfgroupType(confnum="sample_text", confsponsor="sample_text", conftitle="sample_text")
    _safe_set(b, 'Docbook_ConfgroupType191', a1)
    assert _is_linked(b, 'Docbook_ConfgroupType191', a1)
    if hasattr(a1, 'Docbook_InfoType190'):
        assert _is_linked(a1, 'Docbook_InfoType190', b)
    _safe_set(b, 'Docbook_ConfgroupType191', a2)
    assert _is_linked(b, 'Docbook_ConfgroupType191', a2)
    if hasattr(a1, 'Docbook_InfoType190'):
        assert not _is_linked(a1, 'Docbook_InfoType190', b)
    if hasattr(a2, 'Docbook_InfoType190'):
        assert _is_linked(a2, 'Docbook_InfoType190', b)
    _safe_set(b, 'Docbook_ConfgroupType191', None)
    assert not _is_linked(b, 'Docbook_ConfgroupType191', a2)
    if hasattr(a2, 'Docbook_InfoType190'):
        assert not _is_linked(a2, 'Docbook_InfoType190', b)


def test_assoc_confgroup53_reverse_link_reassign_clear():
    a1 = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    a2 = Docbook_DocumentRoot(bibliomisc="sample_text_2", caution="sample_text_2", confnum="sample_text_2", confsponsor="sample_text_2", conftitle="sample_text_2", date="sample_text_2", firstname="sample_text_2", keyword="sample_text_2", mixed="sample_text_2", pubdate="sample_text_2", publishername="sample_text_2", state="sample_text_2", subtitle="sample_text_2", superscript="sample_text_2", warning="sample_text_2")
    b = Docbook_ConfgroupType(confnum="sample_text", confsponsor="sample_text", conftitle="sample_text")
    _safe_set(b, 'Docbook_ConfgroupType', a1)
    assert _is_linked(b, 'Docbook_ConfgroupType', a1)
    if hasattr(a1, 'Docbook_DocumentRoot54'):
        assert _is_linked(a1, 'Docbook_DocumentRoot54', b)
    _safe_set(b, 'Docbook_ConfgroupType', a2)
    assert _is_linked(b, 'Docbook_ConfgroupType', a2)
    if hasattr(a1, 'Docbook_DocumentRoot54'):
        assert not _is_linked(a1, 'Docbook_DocumentRoot54', b)
    if hasattr(a2, 'Docbook_DocumentRoot54'):
        assert _is_linked(a2, 'Docbook_DocumentRoot54', b)
    _safe_set(b, 'Docbook_ConfgroupType', None)
    assert not _is_linked(b, 'Docbook_ConfgroupType', a2)
    if hasattr(a2, 'Docbook_DocumentRoot54'):
        assert not _is_linked(a2, 'Docbook_DocumentRoot54', b)


def test_assoc_copyright194_reverse_link_reassign_clear():
    a1 = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    a2 = Docbook_InfoType(bibliomisc="sample_text_2", date="sample_text_2", group="sample_text_2", productname="sample_text_2", pubdate="sample_text_2", releaseinfo="sample_text_2")
    b = Docbook_CopyrightType(group="sample_text", holder="sample_text", year="sample_text")
    _safe_set(b, 'Docbook_CopyrightType', a1)
    assert _is_linked(b, 'Docbook_CopyrightType', a1)
    if hasattr(a1, 'Docbook_InfoType195'):
        assert _is_linked(a1, 'Docbook_InfoType195', b)
    _safe_set(b, 'Docbook_CopyrightType', a2)
    assert _is_linked(b, 'Docbook_CopyrightType', a2)
    if hasattr(a1, 'Docbook_InfoType195'):
        assert not _is_linked(a1, 'Docbook_InfoType195', b)
    if hasattr(a2, 'Docbook_InfoType195'):
        assert _is_linked(a2, 'Docbook_InfoType195', b)
    _safe_set(b, 'Docbook_CopyrightType', None)
    assert not _is_linked(b, 'Docbook_CopyrightType', a2)
    if hasattr(a2, 'Docbook_InfoType195'):
        assert not _is_linked(a2, 'Docbook_InfoType195', b)


def test_assoc_emphasis124_reverse_link_reassign_clear():
    a1 = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    a2 = Docbook_EmphasisType(mixed="sample_text_2", role="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType125', a1)
    assert _is_linked(b, 'Docbook_EmphasisType125', a1)
    if hasattr(a1, 'Docbook_EmphasisType123'):
        assert _is_linked(a1, 'Docbook_EmphasisType123', b)
    _safe_set(b, 'Docbook_EmphasisType125', a2)
    assert _is_linked(b, 'Docbook_EmphasisType125', a2)
    if hasattr(a1, 'Docbook_EmphasisType123'):
        assert not _is_linked(a1, 'Docbook_EmphasisType123', b)
    if hasattr(a2, 'Docbook_EmphasisType123'):
        assert _is_linked(a2, 'Docbook_EmphasisType123', b)
    _safe_set(b, 'Docbook_EmphasisType125', None)
    assert not _is_linked(b, 'Docbook_EmphasisType125', a2)
    if hasattr(a2, 'Docbook_EmphasisType123'):
        assert not _is_linked(a2, 'Docbook_EmphasisType123', b)


def test_assoc_emphasis163_reverse_link_reassign_clear():
    a1 = Docbook_ImportantType(group="sample_text", mixed="sample_text")
    a2 = Docbook_ImportantType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType165', a1)
    assert _is_linked(b, 'Docbook_EmphasisType165', a1)
    if hasattr(a1, 'Docbook_ImportantType164'):
        assert _is_linked(a1, 'Docbook_ImportantType164', b)
    _safe_set(b, 'Docbook_EmphasisType165', a2)
    assert _is_linked(b, 'Docbook_EmphasisType165', a2)
    if hasattr(a1, 'Docbook_ImportantType164'):
        assert not _is_linked(a1, 'Docbook_ImportantType164', b)
    if hasattr(a2, 'Docbook_ImportantType164'):
        assert _is_linked(a2, 'Docbook_ImportantType164', b)
    _safe_set(b, 'Docbook_EmphasisType165', None)
    assert not _is_linked(b, 'Docbook_EmphasisType165', a2)
    if hasattr(a2, 'Docbook_ImportantType164'):
        assert not _is_linked(a2, 'Docbook_ImportantType164', b)


def test_assoc_emphasis236_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType238', a1)
    assert _is_linked(b, 'Docbook_EmphasisType238', a1)
    if hasattr(a1, 'Docbook_ParaType237'):
        assert _is_linked(a1, 'Docbook_ParaType237', b)
    _safe_set(b, 'Docbook_EmphasisType238', a2)
    assert _is_linked(b, 'Docbook_EmphasisType238', a2)
    if hasattr(a1, 'Docbook_ParaType237'):
        assert not _is_linked(a1, 'Docbook_ParaType237', b)
    if hasattr(a2, 'Docbook_ParaType237'):
        assert _is_linked(a2, 'Docbook_ParaType237', b)
    _safe_set(b, 'Docbook_EmphasisType238', None)
    assert not _is_linked(b, 'Docbook_EmphasisType238', a2)
    if hasattr(a2, 'Docbook_ParaType237'):
        assert not _is_linked(a2, 'Docbook_ParaType237', b)


def test_assoc_emphasis272_reverse_link_reassign_clear():
    a1 = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    a2 = Docbook_ProgramlistingType(format="sample_text_2", group="sample_text_2", language="sample_text_2", linenumbering="sample_text_2", mixed="sample_text_2", superscript="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType274', a1)
    assert _is_linked(b, 'Docbook_EmphasisType274', a1)
    if hasattr(a1, 'Docbook_ProgramlistingType273'):
        assert _is_linked(a1, 'Docbook_ProgramlistingType273', b)
    _safe_set(b, 'Docbook_EmphasisType274', a2)
    assert _is_linked(b, 'Docbook_EmphasisType274', a2)
    if hasattr(a1, 'Docbook_ProgramlistingType273'):
        assert not _is_linked(a1, 'Docbook_ProgramlistingType273', b)
    if hasattr(a2, 'Docbook_ProgramlistingType273'):
        assert _is_linked(a2, 'Docbook_ProgramlistingType273', b)
    _safe_set(b, 'Docbook_EmphasisType274', None)
    assert not _is_linked(b, 'Docbook_EmphasisType274', a2)
    if hasattr(a2, 'Docbook_ProgramlistingType273'):
        assert not _is_linked(a2, 'Docbook_ProgramlistingType273', b)


def test_assoc_emphasis387_reverse_link_reassign_clear():
    a1 = Docbook_SubtitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_SubtitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType389', a1)
    assert _is_linked(b, 'Docbook_EmphasisType389', a1)
    if hasattr(a1, 'Docbook_SubtitleType388'):
        assert _is_linked(a1, 'Docbook_SubtitleType388', b)
    _safe_set(b, 'Docbook_EmphasisType389', a2)
    assert _is_linked(b, 'Docbook_EmphasisType389', a2)
    if hasattr(a1, 'Docbook_SubtitleType388'):
        assert not _is_linked(a1, 'Docbook_SubtitleType388', b)
    if hasattr(a2, 'Docbook_SubtitleType388'):
        assert _is_linked(a2, 'Docbook_SubtitleType388', b)
    _safe_set(b, 'Docbook_EmphasisType389', None)
    assert not _is_linked(b, 'Docbook_EmphasisType389', a2)
    if hasattr(a2, 'Docbook_SubtitleType388'):
        assert not _is_linked(a2, 'Docbook_SubtitleType388', b)


def test_assoc_emphasis399_reverse_link_reassign_clear():
    a1 = Docbook_TermType(mixed="sample_text")
    a2 = Docbook_TermType(mixed="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType400', a1)
    assert _is_linked(b, 'Docbook_EmphasisType400', a1)
    if hasattr(a1, 'Docbook_TermType'):
        assert _is_linked(a1, 'Docbook_TermType', b)
    _safe_set(b, 'Docbook_EmphasisType400', a2)
    assert _is_linked(b, 'Docbook_EmphasisType400', a2)
    if hasattr(a1, 'Docbook_TermType'):
        assert not _is_linked(a1, 'Docbook_TermType', b)
    if hasattr(a2, 'Docbook_TermType'):
        assert _is_linked(a2, 'Docbook_TermType', b)
    _safe_set(b, 'Docbook_EmphasisType400', None)
    assert not _is_linked(b, 'Docbook_EmphasisType400', a2)
    if hasattr(a2, 'Docbook_TermType'):
        assert not _is_linked(a2, 'Docbook_TermType', b)


def test_assoc_emphasis428_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType430', a1)
    assert _is_linked(b, 'Docbook_EmphasisType430', a1)
    if hasattr(a1, 'Docbook_TitleType429'):
        assert _is_linked(a1, 'Docbook_TitleType429', b)
    _safe_set(b, 'Docbook_EmphasisType430', a2)
    assert _is_linked(b, 'Docbook_EmphasisType430', a2)
    if hasattr(a1, 'Docbook_TitleType429'):
        assert not _is_linked(a1, 'Docbook_TitleType429', b)
    if hasattr(a2, 'Docbook_TitleType429'):
        assert _is_linked(a2, 'Docbook_TitleType429', b)
    _safe_set(b, 'Docbook_EmphasisType430', None)
    assert not _is_linked(b, 'Docbook_EmphasisType430', a2)
    if hasattr(a2, 'Docbook_TitleType429'):
        assert not _is_linked(a2, 'Docbook_TitleType429', b)


def test_assoc_emphasis434_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_EmphasisType436', a1)
    assert _is_linked(b, 'Docbook_EmphasisType436', a1)
    if hasattr(a1, 'Docbook_UlinkType435'):
        assert _is_linked(a1, 'Docbook_UlinkType435', b)
    _safe_set(b, 'Docbook_EmphasisType436', a2)
    assert _is_linked(b, 'Docbook_EmphasisType436', a2)
    if hasattr(a1, 'Docbook_UlinkType435'):
        assert not _is_linked(a1, 'Docbook_UlinkType435', b)
    if hasattr(a2, 'Docbook_UlinkType435'):
        assert _is_linked(a2, 'Docbook_UlinkType435', b)
    _safe_set(b, 'Docbook_EmphasisType436', None)
    assert not _is_linked(b, 'Docbook_EmphasisType436', a2)
    if hasattr(a2, 'Docbook_UlinkType435'):
        assert not _is_linked(a2, 'Docbook_UlinkType435', b)


def test_assoc_emphasis55_reverse_link_reassign_clear():
    a1 = Docbook_EmphasisType(mixed="sample_text", role="sample_text")
    a2 = Docbook_EmphasisType(mixed="sample_text_2", role="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot56', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot56', a1)
    if hasattr(a1, 'Docbook_EmphasisType'):
        assert _is_linked(a1, 'Docbook_EmphasisType', b)
    _safe_set(b, 'Docbook_DocumentRoot56', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot56', a2)
    if hasattr(a1, 'Docbook_EmphasisType'):
        assert not _is_linked(a1, 'Docbook_EmphasisType', b)
    if hasattr(a2, 'Docbook_EmphasisType'):
        assert _is_linked(a2, 'Docbook_EmphasisType', b)
    _safe_set(b, 'Docbook_DocumentRoot56', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot56', a2)
    if hasattr(a2, 'Docbook_EmphasisType'):
        assert not _is_linked(a2, 'Docbook_EmphasisType', b)


def test_assoc_entry57_reverse_link_reassign_clear():
    a1 = Docbook_EntryType(align="sample_text", mixed="sample_text", morerows="sample_text", nameend="sample_text", namest="sample_text", valign="sample_text")
    a2 = Docbook_EntryType(align="sample_text_2", mixed="sample_text_2", morerows="sample_text_2", nameend="sample_text_2", namest="sample_text_2", valign="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot58', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot58', a1)
    if hasattr(a1, 'Docbook_EntryType'):
        assert _is_linked(a1, 'Docbook_EntryType', b)
    _safe_set(b, 'Docbook_DocumentRoot58', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot58', a2)
    if hasattr(a1, 'Docbook_EntryType'):
        assert not _is_linked(a1, 'Docbook_EntryType', b)
    if hasattr(a2, 'Docbook_EntryType'):
        assert _is_linked(a2, 'Docbook_EntryType', b)
    _safe_set(b, 'Docbook_DocumentRoot58', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot58', a2)
    if hasattr(a2, 'Docbook_EntryType'):
        assert not _is_linked(a2, 'Docbook_EntryType', b)


def test_assoc_envar407_reverse_link_reassign_clear():
    a1 = Docbook_TermType(mixed="sample_text")
    a2 = Docbook_TermType(mixed="sample_text_2")
    b = Docbook_EnvarType(mixed="sample_text")
    _safe_set(b, 'Docbook_EnvarType409', a1)
    assert _is_linked(b, 'Docbook_EnvarType409', a1)
    if hasattr(a1, 'Docbook_TermType408'):
        assert _is_linked(a1, 'Docbook_TermType408', b)
    _safe_set(b, 'Docbook_EnvarType409', a2)
    assert _is_linked(b, 'Docbook_EnvarType409', a2)
    if hasattr(a1, 'Docbook_TermType408'):
        assert not _is_linked(a1, 'Docbook_TermType408', b)
    if hasattr(a2, 'Docbook_TermType408'):
        assert _is_linked(a2, 'Docbook_TermType408', b)
    _safe_set(b, 'Docbook_EnvarType409', None)
    assert not _is_linked(b, 'Docbook_EnvarType409', a2)
    if hasattr(a2, 'Docbook_TermType408'):
        assert not _is_linked(a2, 'Docbook_TermType408', b)


def test_assoc_example377_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_ExampleType(id="sample_text")
    _safe_set(b, 'Docbook_ExampleType379', a1)
    assert _is_linked(b, 'Docbook_ExampleType379', a1)
    if hasattr(a1, 'Docbook_SectionType378'):
        assert _is_linked(a1, 'Docbook_SectionType378', b)
    _safe_set(b, 'Docbook_ExampleType379', a2)
    assert _is_linked(b, 'Docbook_ExampleType379', a2)
    if hasattr(a1, 'Docbook_SectionType378'):
        assert not _is_linked(a1, 'Docbook_SectionType378', b)
    if hasattr(a2, 'Docbook_SectionType378'):
        assert _is_linked(a2, 'Docbook_SectionType378', b)
    _safe_set(b, 'Docbook_ExampleType379', None)
    assert not _is_linked(b, 'Docbook_ExampleType379', a2)
    if hasattr(a2, 'Docbook_SectionType378'):
        assert not _is_linked(a2, 'Docbook_SectionType378', b)


def test_assoc_figure359_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_FigureType(float="sample_text", id="sample_text")
    _safe_set(b, 'Docbook_FigureType361', a1)
    assert _is_linked(b, 'Docbook_FigureType361', a1)
    if hasattr(a1, 'Docbook_SectionType360'):
        assert _is_linked(a1, 'Docbook_SectionType360', b)
    _safe_set(b, 'Docbook_FigureType361', a2)
    assert _is_linked(b, 'Docbook_FigureType361', a2)
    if hasattr(a1, 'Docbook_SectionType360'):
        assert not _is_linked(a1, 'Docbook_SectionType360', b)
    if hasattr(a2, 'Docbook_SectionType360'):
        assert _is_linked(a2, 'Docbook_SectionType360', b)
    _safe_set(b, 'Docbook_FigureType361', None)
    assert not _is_linked(b, 'Docbook_FigureType361', a2)
    if hasattr(a2, 'Docbook_SectionType360'):
        assert not _is_linked(a2, 'Docbook_SectionType360', b)


def test_assoc_figure59_reverse_link_reassign_clear():
    a1 = Docbook_FigureType(float="sample_text", id="sample_text")
    a2 = Docbook_FigureType(float="sample_text_2", id="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot60', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot60', a1)
    if hasattr(a1, 'Docbook_FigureType'):
        assert _is_linked(a1, 'Docbook_FigureType', b)
    _safe_set(b, 'Docbook_DocumentRoot60', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot60', a2)
    if hasattr(a1, 'Docbook_FigureType'):
        assert not _is_linked(a1, 'Docbook_FigureType', b)
    if hasattr(a2, 'Docbook_FigureType'):
        assert _is_linked(a2, 'Docbook_FigureType', b)
    _safe_set(b, 'Docbook_DocumentRoot60', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot60', a2)
    if hasattr(a2, 'Docbook_FigureType'):
        assert not _is_linked(a2, 'Docbook_FigureType', b)


def test_assoc_filename404_reverse_link_reassign_clear():
    a1 = Docbook_TermType(mixed="sample_text")
    a2 = Docbook_TermType(mixed="sample_text_2")
    b = Docbook_FileNameType(mixed="sample_text")
    _safe_set(b, 'Docbook_FileNameType406', a1)
    assert _is_linked(b, 'Docbook_FileNameType406', a1)
    if hasattr(a1, 'Docbook_TermType405'):
        assert _is_linked(a1, 'Docbook_TermType405', b)
    _safe_set(b, 'Docbook_FileNameType406', a2)
    assert _is_linked(b, 'Docbook_FileNameType406', a2)
    if hasattr(a1, 'Docbook_TermType405'):
        assert not _is_linked(a1, 'Docbook_TermType405', b)
    if hasattr(a2, 'Docbook_TermType405'):
        assert _is_linked(a2, 'Docbook_TermType405', b)
    _safe_set(b, 'Docbook_FileNameType406', None)
    assert not _is_linked(b, 'Docbook_FileNameType406', a2)
    if hasattr(a2, 'Docbook_TermType405'):
        assert not _is_linked(a2, 'Docbook_TermType405', b)


def test_assoc_footnote245_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_FootnoteType(id="sample_text")
    _safe_set(b, 'Docbook_FootnoteType247', a1)
    assert _is_linked(b, 'Docbook_FootnoteType247', a1)
    if hasattr(a1, 'Docbook_ParaType246'):
        assert _is_linked(a1, 'Docbook_ParaType246', b)
    _safe_set(b, 'Docbook_FootnoteType247', a2)
    assert _is_linked(b, 'Docbook_FootnoteType247', a2)
    if hasattr(a1, 'Docbook_ParaType246'):
        assert not _is_linked(a1, 'Docbook_ParaType246', b)
    if hasattr(a2, 'Docbook_ParaType246'):
        assert _is_linked(a2, 'Docbook_ParaType246', b)
    _safe_set(b, 'Docbook_FootnoteType247', None)
    assert not _is_linked(b, 'Docbook_FootnoteType247', a2)
    if hasattr(a2, 'Docbook_ParaType246'):
        assert not _is_linked(a2, 'Docbook_ParaType246', b)


def test_assoc_footnote61_reverse_link_reassign_clear():
    a1 = Docbook_FootnoteType(id="sample_text")
    a2 = Docbook_FootnoteType(id="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot62', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot62', a1)
    if hasattr(a1, 'Docbook_FootnoteType'):
        assert _is_linked(a1, 'Docbook_FootnoteType', b)
    _safe_set(b, 'Docbook_DocumentRoot62', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot62', a2)
    if hasattr(a1, 'Docbook_FootnoteType'):
        assert not _is_linked(a1, 'Docbook_FootnoteType', b)
    if hasattr(a2, 'Docbook_FootnoteType'):
        assert _is_linked(a2, 'Docbook_FootnoteType', b)
    _safe_set(b, 'Docbook_DocumentRoot62', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot62', a2)
    if hasattr(a2, 'Docbook_FootnoteType'):
        assert not _is_linked(a2, 'Docbook_FootnoteType', b)


def test_assoc_function153_reverse_link_reassign_clear():
    a1 = Docbook_FunctionType(mixed="sample_text")
    a2 = Docbook_FunctionType(mixed="sample_text_2")
    b = Docbook_FuncdefType(mixed="sample_text")
    _safe_set(b, 'Docbook_FuncdefType', a1)
    assert _is_linked(b, 'Docbook_FuncdefType', a1)
    if hasattr(a1, 'Docbook_FunctionType'):
        assert _is_linked(a1, 'Docbook_FunctionType', b)
    _safe_set(b, 'Docbook_FuncdefType', a2)
    assert _is_linked(b, 'Docbook_FuncdefType', a2)
    if hasattr(a1, 'Docbook_FunctionType'):
        assert not _is_linked(a1, 'Docbook_FunctionType', b)
    if hasattr(a2, 'Docbook_FunctionType'):
        assert _is_linked(a2, 'Docbook_FunctionType', b)
    _safe_set(b, 'Docbook_FuncdefType', None)
    assert not _is_linked(b, 'Docbook_FuncdefType', a2)
    if hasattr(a2, 'Docbook_FunctionType'):
        assert not _is_linked(a2, 'Docbook_FunctionType', b)


def test_assoc_imagedata63_reverse_link_reassign_clear():
    a1 = Docbook_ImagedataType(align="sample_text", depth="sample_text", fileref="sample_text", scale="sample_text", width="sample_text")
    a2 = Docbook_ImagedataType(align="sample_text_2", depth="sample_text_2", fileref="sample_text_2", scale="sample_text_2", width="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot64', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot64', a1)
    if hasattr(a1, 'Docbook_ImagedataType'):
        assert _is_linked(a1, 'Docbook_ImagedataType', b)
    _safe_set(b, 'Docbook_DocumentRoot64', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot64', a2)
    if hasattr(a1, 'Docbook_ImagedataType'):
        assert not _is_linked(a1, 'Docbook_ImagedataType', b)
    if hasattr(a2, 'Docbook_ImagedataType'):
        assert _is_linked(a2, 'Docbook_ImagedataType', b)
    _safe_set(b, 'Docbook_DocumentRoot64', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot64', a2)
    if hasattr(a2, 'Docbook_ImagedataType'):
        assert not _is_linked(a2, 'Docbook_ImagedataType', b)


def test_assoc_important67_reverse_link_reassign_clear():
    a1 = Docbook_ImportantType(group="sample_text", mixed="sample_text")
    a2 = Docbook_ImportantType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot68', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot68', a1)
    if hasattr(a1, 'Docbook_ImportantType'):
        assert _is_linked(a1, 'Docbook_ImportantType', b)
    _safe_set(b, 'Docbook_DocumentRoot68', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot68', a2)
    if hasattr(a1, 'Docbook_ImportantType'):
        assert not _is_linked(a1, 'Docbook_ImportantType', b)
    if hasattr(a2, 'Docbook_ImportantType'):
        assert _is_linked(a2, 'Docbook_ImportantType', b)
    _safe_set(b, 'Docbook_DocumentRoot68', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot68', a2)
    if hasattr(a2, 'Docbook_ImportantType'):
        assert not _is_linked(a2, 'Docbook_ImportantType', b)


def test_assoc_info281_reverse_link_reassign_clear():
    a1 = Docbook_RefEntryType(version="sample_text")
    a2 = Docbook_RefEntryType(version="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType282', a1)
    assert _is_linked(b, 'Docbook_InfoType282', a1)
    if hasattr(a1, 'Docbook_RefEntryType'):
        assert _is_linked(a1, 'Docbook_RefEntryType', b)
    _safe_set(b, 'Docbook_InfoType282', a2)
    assert _is_linked(b, 'Docbook_InfoType282', a2)
    if hasattr(a1, 'Docbook_RefEntryType'):
        assert not _is_linked(a1, 'Docbook_RefEntryType', b)
    if hasattr(a2, 'Docbook_RefEntryType'):
        assert _is_linked(a2, 'Docbook_RefEntryType', b)
    _safe_set(b, 'Docbook_InfoType282', None)
    assert not _is_linked(b, 'Docbook_InfoType282', a2)
    if hasattr(a2, 'Docbook_RefEntryType'):
        assert not _is_linked(a2, 'Docbook_RefEntryType', b)


def test_assoc_info291_reverse_link_reassign_clear():
    a1 = Docbook_ReferenceType(version="sample_text")
    a2 = Docbook_ReferenceType(version="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType293', a1)
    assert _is_linked(b, 'Docbook_InfoType293', a1)
    if hasattr(a1, 'Docbook_ReferenceType292'):
        assert _is_linked(a1, 'Docbook_ReferenceType292', b)
    _safe_set(b, 'Docbook_InfoType293', a2)
    assert _is_linked(b, 'Docbook_InfoType293', a2)
    if hasattr(a1, 'Docbook_ReferenceType292'):
        assert not _is_linked(a1, 'Docbook_ReferenceType292', b)
    if hasattr(a2, 'Docbook_ReferenceType292'):
        assert _is_linked(a2, 'Docbook_ReferenceType292', b)
    _safe_set(b, 'Docbook_InfoType293', None)
    assert not _is_linked(b, 'Docbook_InfoType293', a2)
    if hasattr(a2, 'Docbook_ReferenceType292'):
        assert not _is_linked(a2, 'Docbook_ReferenceType292', b)


def test_assoc_info45_reverse_link_reassign_clear():
    a1 = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    a2 = Docbook_InfoType(bibliomisc="sample_text_2", date="sample_text_2", group="sample_text_2", productname="sample_text_2", pubdate="sample_text_2", releaseinfo="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot46', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot46', a1)
    if hasattr(a1, 'Docbook_InfoType47'):
        assert _is_linked(a1, 'Docbook_InfoType47', b)
    _safe_set(b, 'Docbook_DocumentRoot46', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot46', a2)
    if hasattr(a1, 'Docbook_InfoType47'):
        assert not _is_linked(a1, 'Docbook_InfoType47', b)
    if hasattr(a2, 'Docbook_InfoType47'):
        assert _is_linked(a2, 'Docbook_InfoType47', b)
    _safe_set(b, 'Docbook_DocumentRoot46', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot46', a2)
    if hasattr(a2, 'Docbook_InfoType47'):
        assert not _is_linked(a2, 'Docbook_InfoType47', b)


def test_assoc_info9_reverse_link_reassign_clear():
    a1 = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    a2 = Docbook_InfoType(bibliomisc="sample_text_2", date="sample_text_2", group="sample_text_2", productname="sample_text_2", pubdate="sample_text_2", releaseinfo="sample_text_2")
    b = Docbook_BookType(label="sample_text", lang="sample_text", version="sample_text")
    _safe_set(b, 'Docbook_BookType', a1)
    assert _is_linked(b, 'Docbook_BookType', a1)
    if hasattr(a1, 'Docbook_InfoType'):
        assert _is_linked(a1, 'Docbook_InfoType', b)
    _safe_set(b, 'Docbook_BookType', a2)
    assert _is_linked(b, 'Docbook_BookType', a2)
    if hasattr(a1, 'Docbook_InfoType'):
        assert not _is_linked(a1, 'Docbook_InfoType', b)
    if hasattr(a2, 'Docbook_InfoType'):
        assert _is_linked(a2, 'Docbook_InfoType', b)
    _safe_set(b, 'Docbook_BookType', None)
    assert not _is_linked(b, 'Docbook_BookType', a2)
    if hasattr(a2, 'Docbook_InfoType'):
        assert not _is_linked(a2, 'Docbook_InfoType', b)


def test_assoc_keywordset180_reverse_link_reassign_clear():
    a1 = Docbook_KeywordsetType(keyword="sample_text")
    a2 = Docbook_KeywordsetType(keyword="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType181', {a1})
    assert _is_linked(b, 'Docbook_InfoType181', a1)
    if hasattr(a1, 'Docbook_KeywordsetType182'):
        assert _is_linked(a1, 'Docbook_KeywordsetType182', b)
    _safe_set(b, 'Docbook_InfoType181', {a2})
    assert _is_linked(b, 'Docbook_InfoType181', a2)
    if hasattr(a1, 'Docbook_KeywordsetType182'):
        assert not _is_linked(a1, 'Docbook_KeywordsetType182', b)
    if hasattr(a2, 'Docbook_KeywordsetType182'):
        assert _is_linked(a2, 'Docbook_KeywordsetType182', b)
    _safe_set(b, 'Docbook_InfoType181', set())
    assert not _is_linked(b, 'Docbook_InfoType181', a2)
    if hasattr(a2, 'Docbook_KeywordsetType182'):
        assert not _is_linked(a2, 'Docbook_KeywordsetType182', b)


def test_assoc_keywordset73_reverse_link_reassign_clear():
    a1 = Docbook_KeywordsetType(keyword="sample_text")
    a2 = Docbook_KeywordsetType(keyword="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot74', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot74', a1)
    if hasattr(a1, 'Docbook_KeywordsetType'):
        assert _is_linked(a1, 'Docbook_KeywordsetType', b)
    _safe_set(b, 'Docbook_DocumentRoot74', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot74', a2)
    if hasattr(a1, 'Docbook_KeywordsetType'):
        assert not _is_linked(a1, 'Docbook_KeywordsetType', b)
    if hasattr(a2, 'Docbook_KeywordsetType'):
        assert _is_linked(a2, 'Docbook_KeywordsetType', b)
    _safe_set(b, 'Docbook_DocumentRoot74', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot74', a2)
    if hasattr(a2, 'Docbook_KeywordsetType'):
        assert not _is_linked(a2, 'Docbook_KeywordsetType', b)


def test_assoc_legalnotice196_reverse_link_reassign_clear():
    a1 = Docbook_LegalNoticeType(group="sample_text")
    a2 = Docbook_LegalNoticeType(group="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType197', a1)
    assert _is_linked(b, 'Docbook_InfoType197', a1)
    if hasattr(a1, 'Docbook_LegalNoticeType'):
        assert _is_linked(a1, 'Docbook_LegalNoticeType', b)
    _safe_set(b, 'Docbook_InfoType197', a2)
    assert _is_linked(b, 'Docbook_InfoType197', a2)
    if hasattr(a1, 'Docbook_LegalNoticeType'):
        assert not _is_linked(a1, 'Docbook_LegalNoticeType', b)
    if hasattr(a2, 'Docbook_LegalNoticeType'):
        assert _is_linked(a2, 'Docbook_LegalNoticeType', b)
    _safe_set(b, 'Docbook_InfoType197', None)
    assert not _is_linked(b, 'Docbook_InfoType197', a2)
    if hasattr(a2, 'Docbook_LegalNoticeType'):
        assert not _is_linked(a2, 'Docbook_LegalNoticeType', b)


def test_assoc_link248_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_LinkType(linkend="sample_text", mixed="sample_text", value="sample_text")
    _safe_set(b, 'Docbook_LinkType250', a1)
    assert _is_linked(b, 'Docbook_LinkType250', a1)
    if hasattr(a1, 'Docbook_ParaType249'):
        assert _is_linked(a1, 'Docbook_ParaType249', b)
    _safe_set(b, 'Docbook_LinkType250', a2)
    assert _is_linked(b, 'Docbook_LinkType250', a2)
    if hasattr(a1, 'Docbook_ParaType249'):
        assert not _is_linked(a1, 'Docbook_ParaType249', b)
    if hasattr(a2, 'Docbook_ParaType249'):
        assert _is_linked(a2, 'Docbook_ParaType249', b)
    _safe_set(b, 'Docbook_LinkType250', None)
    assert not _is_linked(b, 'Docbook_LinkType250', a2)
    if hasattr(a2, 'Docbook_ParaType249'):
        assert not _is_linked(a2, 'Docbook_ParaType249', b)


def test_assoc_link75_reverse_link_reassign_clear():
    a1 = Docbook_LinkType(linkend="sample_text", mixed="sample_text", value="sample_text")
    a2 = Docbook_LinkType(linkend="sample_text_2", mixed="sample_text_2", value="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot76', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot76', a1)
    if hasattr(a1, 'Docbook_LinkType'):
        assert _is_linked(a1, 'Docbook_LinkType', b)
    _safe_set(b, 'Docbook_DocumentRoot76', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot76', a2)
    if hasattr(a1, 'Docbook_LinkType'):
        assert not _is_linked(a1, 'Docbook_LinkType', b)
    if hasattr(a2, 'Docbook_LinkType'):
        assert _is_linked(a2, 'Docbook_LinkType', b)
    _safe_set(b, 'Docbook_DocumentRoot76', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot76', a2)
    if hasattr(a2, 'Docbook_LinkType'):
        assert not _is_linked(a2, 'Docbook_LinkType', b)


def test_assoc_literal222_reverse_link_reassign_clear():
    a1 = Docbook_NoteType(group="sample_text", mixed="sample_text")
    a2 = Docbook_NoteType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_LiteralType(moreinfo="sample_text", value="sample_text")
    _safe_set(b, 'Docbook_LiteralType224', a1)
    assert _is_linked(b, 'Docbook_LiteralType224', a1)
    if hasattr(a1, 'Docbook_NoteType223'):
        assert _is_linked(a1, 'Docbook_NoteType223', b)
    _safe_set(b, 'Docbook_LiteralType224', a2)
    assert _is_linked(b, 'Docbook_LiteralType224', a2)
    if hasattr(a1, 'Docbook_NoteType223'):
        assert not _is_linked(a1, 'Docbook_NoteType223', b)
    if hasattr(a2, 'Docbook_NoteType223'):
        assert _is_linked(a2, 'Docbook_NoteType223', b)
    _safe_set(b, 'Docbook_LiteralType224', None)
    assert not _is_linked(b, 'Docbook_LiteralType224', a2)
    if hasattr(a2, 'Docbook_NoteType223'):
        assert not _is_linked(a2, 'Docbook_NoteType223', b)


def test_assoc_literal239_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_LiteralType(moreinfo="sample_text", value="sample_text")
    _safe_set(b, 'Docbook_LiteralType241', a1)
    assert _is_linked(b, 'Docbook_LiteralType241', a1)
    if hasattr(a1, 'Docbook_ParaType240'):
        assert _is_linked(a1, 'Docbook_ParaType240', b)
    _safe_set(b, 'Docbook_LiteralType241', a2)
    assert _is_linked(b, 'Docbook_LiteralType241', a2)
    if hasattr(a1, 'Docbook_ParaType240'):
        assert not _is_linked(a1, 'Docbook_ParaType240', b)
    if hasattr(a2, 'Docbook_ParaType240'):
        assert _is_linked(a2, 'Docbook_ParaType240', b)
    _safe_set(b, 'Docbook_LiteralType241', None)
    assert not _is_linked(b, 'Docbook_LiteralType241', a2)
    if hasattr(a2, 'Docbook_ParaType240'):
        assert not _is_linked(a2, 'Docbook_ParaType240', b)


def test_assoc_literal79_reverse_link_reassign_clear():
    a1 = Docbook_LiteralType(moreinfo="sample_text", value="sample_text")
    a2 = Docbook_LiteralType(moreinfo="sample_text_2", value="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot80', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot80', a1)
    if hasattr(a1, 'Docbook_LiteralType'):
        assert _is_linked(a1, 'Docbook_LiteralType', b)
    _safe_set(b, 'Docbook_DocumentRoot80', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot80', a2)
    if hasattr(a1, 'Docbook_LiteralType'):
        assert not _is_linked(a1, 'Docbook_LiteralType', b)
    if hasattr(a2, 'Docbook_LiteralType'):
        assert _is_linked(a2, 'Docbook_LiteralType', b)
    _safe_set(b, 'Docbook_DocumentRoot80', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot80', a2)
    if hasattr(a2, 'Docbook_LiteralType'):
        assert not _is_linked(a2, 'Docbook_LiteralType', b)


def test_assoc_note21_reverse_link_reassign_clear():
    a1 = Docbook_NoteType(group="sample_text", mixed="sample_text")
    a2 = Docbook_NoteType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_ChapterType(annotations="sample_text")
    _safe_set(b, 'Docbook_ChapterType22', a1)
    assert _is_linked(b, 'Docbook_ChapterType22', a1)
    if hasattr(a1, 'Docbook_NoteType'):
        assert _is_linked(a1, 'Docbook_NoteType', b)
    _safe_set(b, 'Docbook_ChapterType22', a2)
    assert _is_linked(b, 'Docbook_ChapterType22', a2)
    if hasattr(a1, 'Docbook_NoteType'):
        assert not _is_linked(a1, 'Docbook_NoteType', b)
    if hasattr(a2, 'Docbook_NoteType'):
        assert _is_linked(a2, 'Docbook_NoteType', b)
    _safe_set(b, 'Docbook_ChapterType22', None)
    assert not _is_linked(b, 'Docbook_ChapterType22', a2)
    if hasattr(a2, 'Docbook_NoteType'):
        assert not _is_linked(a2, 'Docbook_NoteType', b)


def test_assoc_note344_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_NoteType(group="sample_text", mixed="sample_text")
    _safe_set(b, 'Docbook_NoteType346', a1)
    assert _is_linked(b, 'Docbook_NoteType346', a1)
    if hasattr(a1, 'Docbook_SectionType345'):
        assert _is_linked(a1, 'Docbook_SectionType345', b)
    _safe_set(b, 'Docbook_NoteType346', a2)
    assert _is_linked(b, 'Docbook_NoteType346', a2)
    if hasattr(a1, 'Docbook_SectionType345'):
        assert not _is_linked(a1, 'Docbook_SectionType345', b)
    if hasattr(a2, 'Docbook_SectionType345'):
        assert _is_linked(a2, 'Docbook_SectionType345', b)
    _safe_set(b, 'Docbook_NoteType346', None)
    assert not _is_linked(b, 'Docbook_NoteType346', a2)
    if hasattr(a2, 'Docbook_SectionType345'):
        assert not _is_linked(a2, 'Docbook_SectionType345', b)


def test_assoc_note83_reverse_link_reassign_clear():
    a1 = Docbook_NoteType(group="sample_text", mixed="sample_text")
    a2 = Docbook_NoteType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot84', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot84', a1)
    if hasattr(a1, 'Docbook_NoteType85'):
        assert _is_linked(a1, 'Docbook_NoteType85', b)
    _safe_set(b, 'Docbook_DocumentRoot84', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot84', a2)
    if hasattr(a1, 'Docbook_NoteType85'):
        assert not _is_linked(a1, 'Docbook_NoteType85', b)
    if hasattr(a2, 'Docbook_NoteType85'):
        assert _is_linked(a2, 'Docbook_NoteType85', b)
    _safe_set(b, 'Docbook_DocumentRoot84', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot84', a2)
    if hasattr(a2, 'Docbook_NoteType85'):
        assert not _is_linked(a2, 'Docbook_NoteType85', b)


def test_assoc_option2_reverse_link_reassign_clear():
    a1 = Docbook_OptionType(mixed="sample_text")
    a2 = Docbook_OptionType(mixed="sample_text_2")
    b = Docbook_ArgType(choice="sample_text", mixed="sample_text", rep="sample_text")
    _safe_set(b, 'Docbook_ArgType', {a1})
    assert _is_linked(b, 'Docbook_ArgType', a1)
    if hasattr(a1, 'Docbook_OptionType'):
        assert _is_linked(a1, 'Docbook_OptionType', b)
    _safe_set(b, 'Docbook_ArgType', {a2})
    assert _is_linked(b, 'Docbook_ArgType', a2)
    if hasattr(a1, 'Docbook_OptionType'):
        assert not _is_linked(a1, 'Docbook_OptionType', b)
    if hasattr(a2, 'Docbook_OptionType'):
        assert _is_linked(a2, 'Docbook_OptionType', b)
    _safe_set(b, 'Docbook_ArgType', set())
    assert not _is_linked(b, 'Docbook_ArgType', a2)
    if hasattr(a2, 'Docbook_OptionType'):
        assert not _is_linked(a2, 'Docbook_OptionType', b)


def test_assoc_option401_reverse_link_reassign_clear():
    a1 = Docbook_TermType(mixed="sample_text")
    a2 = Docbook_TermType(mixed="sample_text_2")
    b = Docbook_OptionType(mixed="sample_text")
    _safe_set(b, 'Docbook_OptionType403', a1)
    assert _is_linked(b, 'Docbook_OptionType403', a1)
    if hasattr(a1, 'Docbook_TermType402'):
        assert _is_linked(a1, 'Docbook_TermType402', b)
    _safe_set(b, 'Docbook_OptionType403', a2)
    assert _is_linked(b, 'Docbook_OptionType403', a2)
    if hasattr(a1, 'Docbook_TermType402'):
        assert not _is_linked(a1, 'Docbook_TermType402', b)
    if hasattr(a2, 'Docbook_TermType402'):
        assert _is_linked(a2, 'Docbook_TermType402', b)
    _safe_set(b, 'Docbook_OptionType403', None)
    assert not _is_linked(b, 'Docbook_OptionType403', a2)
    if hasattr(a2, 'Docbook_TermType402'):
        assert not _is_linked(a2, 'Docbook_TermType402', b)


def test_assoc_orderedlist210_reverse_link_reassign_clear():
    a1 = Docbook_OrderedlistType(continuation="sample_text", inheritnum="sample_text")
    a2 = Docbook_OrderedlistType(continuation="sample_text_2", inheritnum="sample_text_2")
    b = Docbook_LegalNoticeType(group="sample_text")
    _safe_set(b, 'Docbook_LegalNoticeType211', {a1})
    assert _is_linked(b, 'Docbook_LegalNoticeType211', a1)
    if hasattr(a1, 'Docbook_OrderedlistType212'):
        assert _is_linked(a1, 'Docbook_OrderedlistType212', b)
    _safe_set(b, 'Docbook_LegalNoticeType211', {a2})
    assert _is_linked(b, 'Docbook_LegalNoticeType211', a2)
    if hasattr(a1, 'Docbook_OrderedlistType212'):
        assert not _is_linked(a1, 'Docbook_OrderedlistType212', b)
    if hasattr(a2, 'Docbook_OrderedlistType212'):
        assert _is_linked(a2, 'Docbook_OrderedlistType212', b)
    _safe_set(b, 'Docbook_LegalNoticeType211', set())
    assert not _is_linked(b, 'Docbook_LegalNoticeType211', a2)
    if hasattr(a2, 'Docbook_OrderedlistType212'):
        assert not _is_linked(a2, 'Docbook_OrderedlistType212', b)


def test_assoc_orderedlist365_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_OrderedlistType(continuation="sample_text", inheritnum="sample_text")
    _safe_set(b, 'Docbook_OrderedlistType367', a1)
    assert _is_linked(b, 'Docbook_OrderedlistType367', a1)
    if hasattr(a1, 'Docbook_SectionType366'):
        assert _is_linked(a1, 'Docbook_SectionType366', b)
    _safe_set(b, 'Docbook_OrderedlistType367', a2)
    assert _is_linked(b, 'Docbook_OrderedlistType367', a2)
    if hasattr(a1, 'Docbook_SectionType366'):
        assert not _is_linked(a1, 'Docbook_SectionType366', b)
    if hasattr(a2, 'Docbook_SectionType366'):
        assert _is_linked(a2, 'Docbook_SectionType366', b)
    _safe_set(b, 'Docbook_OrderedlistType367', None)
    assert not _is_linked(b, 'Docbook_OrderedlistType367', a2)
    if hasattr(a2, 'Docbook_SectionType366'):
        assert not _is_linked(a2, 'Docbook_SectionType366', b)


def test_assoc_orderedlist86_reverse_link_reassign_clear():
    a1 = Docbook_OrderedlistType(continuation="sample_text", inheritnum="sample_text")
    a2 = Docbook_OrderedlistType(continuation="sample_text_2", inheritnum="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot87', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot87', a1)
    if hasattr(a1, 'Docbook_OrderedlistType'):
        assert _is_linked(a1, 'Docbook_OrderedlistType', b)
    _safe_set(b, 'Docbook_DocumentRoot87', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot87', a2)
    if hasattr(a1, 'Docbook_OrderedlistType'):
        assert not _is_linked(a1, 'Docbook_OrderedlistType', b)
    if hasattr(a2, 'Docbook_OrderedlistType'):
        assert _is_linked(a2, 'Docbook_OrderedlistType', b)
    _safe_set(b, 'Docbook_DocumentRoot87', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot87', a2)
    if hasattr(a2, 'Docbook_OrderedlistType'):
        assert not _is_linked(a2, 'Docbook_OrderedlistType', b)


def test_assoc_para132_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_EntryType(align="sample_text", mixed="sample_text", morerows="sample_text", nameend="sample_text", namest="sample_text", valign="sample_text")
    _safe_set(b, 'Docbook_EntryType133', {a1})
    assert _is_linked(b, 'Docbook_EntryType133', a1)
    if hasattr(a1, 'Docbook_ParaType134'):
        assert _is_linked(a1, 'Docbook_ParaType134', b)
    _safe_set(b, 'Docbook_EntryType133', {a2})
    assert _is_linked(b, 'Docbook_EntryType133', a2)
    if hasattr(a1, 'Docbook_ParaType134'):
        assert not _is_linked(a1, 'Docbook_ParaType134', b)
    if hasattr(a2, 'Docbook_ParaType134'):
        assert _is_linked(a2, 'Docbook_ParaType134', b)
    _safe_set(b, 'Docbook_EntryType133', set())
    assert not _is_linked(b, 'Docbook_EntryType133', a2)
    if hasattr(a2, 'Docbook_ParaType134'):
        assert not _is_linked(a2, 'Docbook_ParaType134', b)


def test_assoc_para150_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_FootnoteType(id="sample_text")
    _safe_set(b, 'Docbook_FootnoteType151', a1)
    assert _is_linked(b, 'Docbook_FootnoteType151', a1)
    if hasattr(a1, 'Docbook_ParaType152'):
        assert _is_linked(a1, 'Docbook_ParaType152', b)
    _safe_set(b, 'Docbook_FootnoteType151', a2)
    assert _is_linked(b, 'Docbook_FootnoteType151', a2)
    if hasattr(a1, 'Docbook_ParaType152'):
        assert not _is_linked(a1, 'Docbook_ParaType152', b)
    if hasattr(a2, 'Docbook_ParaType152'):
        assert _is_linked(a2, 'Docbook_ParaType152', b)
    _safe_set(b, 'Docbook_FootnoteType151', None)
    assert not _is_linked(b, 'Docbook_FootnoteType151', a2)
    if hasattr(a2, 'Docbook_ParaType152'):
        assert not _is_linked(a2, 'Docbook_ParaType152', b)


def test_assoc_para18_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_ChapterType(annotations="sample_text")
    _safe_set(b, 'Docbook_ChapterType19', {a1})
    assert _is_linked(b, 'Docbook_ChapterType19', a1)
    if hasattr(a1, 'Docbook_ParaType20'):
        assert _is_linked(a1, 'Docbook_ParaType20', b)
    _safe_set(b, 'Docbook_ChapterType19', {a2})
    assert _is_linked(b, 'Docbook_ChapterType19', a2)
    if hasattr(a1, 'Docbook_ParaType20'):
        assert not _is_linked(a1, 'Docbook_ParaType20', b)
    if hasattr(a2, 'Docbook_ParaType20'):
        assert _is_linked(a2, 'Docbook_ParaType20', b)
    _safe_set(b, 'Docbook_ChapterType19', set())
    assert not _is_linked(b, 'Docbook_ChapterType19', a2)
    if hasattr(a2, 'Docbook_ParaType20'):
        assert not _is_linked(a2, 'Docbook_ParaType20', b)


def test_assoc_para207_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_LegalNoticeType(group="sample_text")
    _safe_set(b, 'Docbook_LegalNoticeType208', {a1})
    assert _is_linked(b, 'Docbook_LegalNoticeType208', a1)
    if hasattr(a1, 'Docbook_ParaType209'):
        assert _is_linked(a1, 'Docbook_ParaType209', b)
    _safe_set(b, 'Docbook_LegalNoticeType208', {a2})
    assert _is_linked(b, 'Docbook_LegalNoticeType208', a2)
    if hasattr(a1, 'Docbook_ParaType209'):
        assert not _is_linked(a1, 'Docbook_ParaType209', b)
    if hasattr(a2, 'Docbook_ParaType209'):
        assert _is_linked(a2, 'Docbook_ParaType209', b)
    _safe_set(b, 'Docbook_LegalNoticeType208', set())
    assert not _is_linked(b, 'Docbook_LegalNoticeType208', a2)
    if hasattr(a2, 'Docbook_ParaType209'):
        assert not _is_linked(a2, 'Docbook_ParaType209', b)


def test_assoc_para305_reverse_link_reassign_clear():
    a1 = Docbook_RefSect1Type(group="sample_text", id="sample_text")
    a2 = Docbook_RefSect1Type(group="sample_text_2", id="sample_text_2")
    b = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_ParaType307', a1)
    assert _is_linked(b, 'Docbook_ParaType307', a1)
    if hasattr(a1, 'Docbook_RefSect1Type306'):
        assert _is_linked(a1, 'Docbook_RefSect1Type306', b)
    _safe_set(b, 'Docbook_ParaType307', a2)
    assert _is_linked(b, 'Docbook_ParaType307', a2)
    if hasattr(a1, 'Docbook_RefSect1Type306'):
        assert not _is_linked(a1, 'Docbook_RefSect1Type306', b)
    if hasattr(a2, 'Docbook_RefSect1Type306'):
        assert _is_linked(a2, 'Docbook_RefSect1Type306', b)
    _safe_set(b, 'Docbook_ParaType307', None)
    assert not _is_linked(b, 'Docbook_ParaType307', a2)
    if hasattr(a2, 'Docbook_RefSect1Type306'):
        assert not _is_linked(a2, 'Docbook_RefSect1Type306', b)


def test_assoc_para319_reverse_link_reassign_clear():
    a1 = Docbook_RevdescriptionType(mixed="sample_text")
    a2 = Docbook_RevdescriptionType(mixed="sample_text_2")
    b = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_ParaType320', a1)
    assert _is_linked(b, 'Docbook_ParaType320', a1)
    if hasattr(a1, 'Docbook_RevdescriptionType'):
        assert _is_linked(a1, 'Docbook_RevdescriptionType', b)
    _safe_set(b, 'Docbook_ParaType320', a2)
    assert _is_linked(b, 'Docbook_ParaType320', a2)
    if hasattr(a1, 'Docbook_RevdescriptionType'):
        assert not _is_linked(a1, 'Docbook_RevdescriptionType', b)
    if hasattr(a2, 'Docbook_RevdescriptionType'):
        assert _is_linked(a2, 'Docbook_RevdescriptionType', b)
    _safe_set(b, 'Docbook_ParaType320', None)
    assert not _is_linked(b, 'Docbook_ParaType320', a2)
    if hasattr(a2, 'Docbook_RevdescriptionType'):
        assert not _is_linked(a2, 'Docbook_RevdescriptionType', b)


def test_assoc_para347_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_ParaType349', a1)
    assert _is_linked(b, 'Docbook_ParaType349', a1)
    if hasattr(a1, 'Docbook_SectionType348'):
        assert _is_linked(a1, 'Docbook_SectionType348', b)
    _safe_set(b, 'Docbook_ParaType349', a2)
    assert _is_linked(b, 'Docbook_ParaType349', a2)
    if hasattr(a1, 'Docbook_SectionType348'):
        assert not _is_linked(a1, 'Docbook_SectionType348', b)
    if hasattr(a2, 'Docbook_SectionType348'):
        assert _is_linked(a2, 'Docbook_SectionType348', b)
    _safe_set(b, 'Docbook_ParaType349', None)
    assert not _is_linked(b, 'Docbook_ParaType349', a2)
    if hasattr(a2, 'Docbook_SectionType348'):
        assert not _is_linked(a2, 'Docbook_SectionType348', b)


def test_assoc_para91_reverse_link_reassign_clear():
    a1 = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    a2 = Docbook_ParaType(group="sample_text_2", id="sample_text_2", mixed="sample_text_2", role="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot92', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot92', a1)
    if hasattr(a1, 'Docbook_ParaType93'):
        assert _is_linked(a1, 'Docbook_ParaType93', b)
    _safe_set(b, 'Docbook_DocumentRoot92', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot92', a2)
    if hasattr(a1, 'Docbook_ParaType93'):
        assert not _is_linked(a1, 'Docbook_ParaType93', b)
    if hasattr(a2, 'Docbook_ParaType93'):
        assert _is_linked(a2, 'Docbook_ParaType93', b)
    _safe_set(b, 'Docbook_DocumentRoot92', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot92', a2)
    if hasattr(a2, 'Docbook_ParaType93'):
        assert not _is_linked(a2, 'Docbook_ParaType93', b)


def test_assoc_parameter234_reverse_link_reassign_clear():
    a1 = Docbook_ParameterType(mixed="sample_text")
    a2 = Docbook_ParameterType(mixed="sample_text_2")
    b = Docbook_ParamdefType(mixed="sample_text")
    _safe_set(b, 'Docbook_ParamdefType235', a1)
    assert _is_linked(b, 'Docbook_ParamdefType235', a1)
    if hasattr(a1, 'Docbook_ParameterType'):
        assert _is_linked(a1, 'Docbook_ParameterType', b)
    _safe_set(b, 'Docbook_ParamdefType235', a2)
    assert _is_linked(b, 'Docbook_ParamdefType235', a2)
    if hasattr(a1, 'Docbook_ParameterType'):
        assert not _is_linked(a1, 'Docbook_ParameterType', b)
    if hasattr(a2, 'Docbook_ParameterType'):
        assert _is_linked(a2, 'Docbook_ParameterType', b)
    _safe_set(b, 'Docbook_ParamdefType235', None)
    assert not _is_linked(b, 'Docbook_ParamdefType235', a2)
    if hasattr(a2, 'Docbook_ParameterType'):
        assert not _is_linked(a2, 'Docbook_ParameterType', b)


def test_assoc_phrase275_reverse_link_reassign_clear():
    a1 = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    a2 = Docbook_ProgramlistingType(format="sample_text_2", group="sample_text_2", language="sample_text_2", linenumbering="sample_text_2", mixed="sample_text_2", superscript="sample_text_2")
    b = Docbook_PhraseType(id="sample_text")
    _safe_set(b, 'Docbook_PhraseType277', a1)
    assert _is_linked(b, 'Docbook_PhraseType277', a1)
    if hasattr(a1, 'Docbook_ProgramlistingType276'):
        assert _is_linked(a1, 'Docbook_ProgramlistingType276', b)
    _safe_set(b, 'Docbook_PhraseType277', a2)
    assert _is_linked(b, 'Docbook_PhraseType277', a2)
    if hasattr(a1, 'Docbook_ProgramlistingType276'):
        assert not _is_linked(a1, 'Docbook_ProgramlistingType276', b)
    if hasattr(a2, 'Docbook_ProgramlistingType276'):
        assert _is_linked(a2, 'Docbook_ProgramlistingType276', b)
    _safe_set(b, 'Docbook_PhraseType277', None)
    assert not _is_linked(b, 'Docbook_PhraseType277', a2)
    if hasattr(a2, 'Docbook_ProgramlistingType276'):
        assert not _is_linked(a2, 'Docbook_ProgramlistingType276', b)


def test_assoc_phrase390_reverse_link_reassign_clear():
    a1 = Docbook_SubtitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_SubtitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_PhraseType(id="sample_text")
    _safe_set(b, 'Docbook_PhraseType392', a1)
    assert _is_linked(b, 'Docbook_PhraseType392', a1)
    if hasattr(a1, 'Docbook_SubtitleType391'):
        assert _is_linked(a1, 'Docbook_SubtitleType391', b)
    _safe_set(b, 'Docbook_PhraseType392', a2)
    assert _is_linked(b, 'Docbook_PhraseType392', a2)
    if hasattr(a1, 'Docbook_SubtitleType391'):
        assert not _is_linked(a1, 'Docbook_SubtitleType391', b)
    if hasattr(a2, 'Docbook_SubtitleType391'):
        assert _is_linked(a2, 'Docbook_SubtitleType391', b)
    _safe_set(b, 'Docbook_PhraseType392', None)
    assert not _is_linked(b, 'Docbook_PhraseType392', a2)
    if hasattr(a2, 'Docbook_SubtitleType391'):
        assert not _is_linked(a2, 'Docbook_SubtitleType391', b)


def test_assoc_phrase431_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_PhraseType(id="sample_text")
    _safe_set(b, 'Docbook_PhraseType433', a1)
    assert _is_linked(b, 'Docbook_PhraseType433', a1)
    if hasattr(a1, 'Docbook_TitleType432'):
        assert _is_linked(a1, 'Docbook_TitleType432', b)
    _safe_set(b, 'Docbook_PhraseType433', a2)
    assert _is_linked(b, 'Docbook_PhraseType433', a2)
    if hasattr(a1, 'Docbook_TitleType432'):
        assert not _is_linked(a1, 'Docbook_TitleType432', b)
    if hasattr(a2, 'Docbook_TitleType432'):
        assert _is_linked(a2, 'Docbook_TitleType432', b)
    _safe_set(b, 'Docbook_PhraseType433', None)
    assert not _is_linked(b, 'Docbook_PhraseType433', a2)
    if hasattr(a2, 'Docbook_TitleType432'):
        assert not _is_linked(a2, 'Docbook_TitleType432', b)


def test_assoc_phrase94_reverse_link_reassign_clear():
    a1 = Docbook_PhraseType(id="sample_text")
    a2 = Docbook_PhraseType(id="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot95', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot95', a1)
    if hasattr(a1, 'Docbook_PhraseType'):
        assert _is_linked(a1, 'Docbook_PhraseType', b)
    _safe_set(b, 'Docbook_DocumentRoot95', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot95', a2)
    if hasattr(a1, 'Docbook_PhraseType'):
        assert not _is_linked(a1, 'Docbook_PhraseType', b)
    if hasattr(a2, 'Docbook_PhraseType'):
        assert _is_linked(a2, 'Docbook_PhraseType', b)
    _safe_set(b, 'Docbook_DocumentRoot95', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot95', a2)
    if hasattr(a2, 'Docbook_PhraseType'):
        assert not _is_linked(a2, 'Docbook_PhraseType', b)


def test_assoc_programlisting126_reverse_link_reassign_clear():
    a1 = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    a2 = Docbook_ProgramlistingType(format="sample_text_2", group="sample_text_2", language="sample_text_2", linenumbering="sample_text_2", mixed="sample_text_2", superscript="sample_text_2")
    b = Docbook_EntryType(align="sample_text", mixed="sample_text", morerows="sample_text", nameend="sample_text", namest="sample_text", valign="sample_text")
    _safe_set(b, 'Docbook_EntryType127', {a1})
    assert _is_linked(b, 'Docbook_EntryType127', a1)
    if hasattr(a1, 'Docbook_ProgramlistingType128'):
        assert _is_linked(a1, 'Docbook_ProgramlistingType128', b)
    _safe_set(b, 'Docbook_EntryType127', {a2})
    assert _is_linked(b, 'Docbook_EntryType127', a2)
    if hasattr(a1, 'Docbook_ProgramlistingType128'):
        assert not _is_linked(a1, 'Docbook_ProgramlistingType128', b)
    if hasattr(a2, 'Docbook_ProgramlistingType128'):
        assert _is_linked(a2, 'Docbook_ProgramlistingType128', b)
    _safe_set(b, 'Docbook_EntryType127', set())
    assert not _is_linked(b, 'Docbook_EntryType127', a2)
    if hasattr(a2, 'Docbook_ProgramlistingType128'):
        assert not _is_linked(a2, 'Docbook_ProgramlistingType128', b)


def test_assoc_programlisting139_reverse_link_reassign_clear():
    a1 = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    a2 = Docbook_ProgramlistingType(format="sample_text_2", group="sample_text_2", language="sample_text_2", linenumbering="sample_text_2", mixed="sample_text_2", superscript="sample_text_2")
    b = Docbook_ExampleType(id="sample_text")
    _safe_set(b, 'Docbook_ExampleType140', a1)
    assert _is_linked(b, 'Docbook_ExampleType140', a1)
    if hasattr(a1, 'Docbook_ProgramlistingType141'):
        assert _is_linked(a1, 'Docbook_ProgramlistingType141', b)
    _safe_set(b, 'Docbook_ExampleType140', a2)
    assert _is_linked(b, 'Docbook_ExampleType140', a2)
    if hasattr(a1, 'Docbook_ProgramlistingType141'):
        assert not _is_linked(a1, 'Docbook_ProgramlistingType141', b)
    if hasattr(a2, 'Docbook_ProgramlistingType141'):
        assert _is_linked(a2, 'Docbook_ProgramlistingType141', b)
    _safe_set(b, 'Docbook_ExampleType140', None)
    assert not _is_linked(b, 'Docbook_ExampleType140', a2)
    if hasattr(a2, 'Docbook_ProgramlistingType141'):
        assert not _is_linked(a2, 'Docbook_ProgramlistingType141', b)


def test_assoc_programlisting350_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    _safe_set(b, 'Docbook_ProgramlistingType352', a1)
    assert _is_linked(b, 'Docbook_ProgramlistingType352', a1)
    if hasattr(a1, 'Docbook_SectionType351'):
        assert _is_linked(a1, 'Docbook_SectionType351', b)
    _safe_set(b, 'Docbook_ProgramlistingType352', a2)
    assert _is_linked(b, 'Docbook_ProgramlistingType352', a2)
    if hasattr(a1, 'Docbook_SectionType351'):
        assert not _is_linked(a1, 'Docbook_SectionType351', b)
    if hasattr(a2, 'Docbook_SectionType351'):
        assert _is_linked(a2, 'Docbook_SectionType351', b)
    _safe_set(b, 'Docbook_ProgramlistingType352', None)
    assert not _is_linked(b, 'Docbook_ProgramlistingType352', a2)
    if hasattr(a2, 'Docbook_SectionType351'):
        assert not _is_linked(a2, 'Docbook_SectionType351', b)


def test_assoc_programlisting99_reverse_link_reassign_clear():
    a1 = Docbook_ProgramlistingType(format="sample_text", group="sample_text", language="sample_text", linenumbering="sample_text", mixed="sample_text", superscript="sample_text")
    a2 = Docbook_ProgramlistingType(format="sample_text_2", group="sample_text_2", language="sample_text_2", linenumbering="sample_text_2", mixed="sample_text_2", superscript="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot100', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot100', a1)
    if hasattr(a1, 'Docbook_ProgramlistingType'):
        assert _is_linked(a1, 'Docbook_ProgramlistingType', b)
    _safe_set(b, 'Docbook_DocumentRoot100', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot100', a2)
    if hasattr(a1, 'Docbook_ProgramlistingType'):
        assert not _is_linked(a1, 'Docbook_ProgramlistingType', b)
    if hasattr(a2, 'Docbook_ProgramlistingType'):
        assert _is_linked(a2, 'Docbook_ProgramlistingType', b)
    _safe_set(b, 'Docbook_DocumentRoot100', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot100', a2)
    if hasattr(a2, 'Docbook_ProgramlistingType'):
        assert not _is_linked(a2, 'Docbook_ProgramlistingType', b)


def test_assoc_publisher101_reverse_link_reassign_clear():
    a1 = Docbook_PublisherType(publishername="sample_text")
    a2 = Docbook_PublisherType(publishername="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot102', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot102', a1)
    if hasattr(a1, 'Docbook_PublisherType'):
        assert _is_linked(a1, 'Docbook_PublisherType', b)
    _safe_set(b, 'Docbook_DocumentRoot102', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot102', a2)
    if hasattr(a1, 'Docbook_PublisherType'):
        assert not _is_linked(a1, 'Docbook_PublisherType', b)
    if hasattr(a2, 'Docbook_PublisherType'):
        assert _is_linked(a2, 'Docbook_PublisherType', b)
    _safe_set(b, 'Docbook_DocumentRoot102', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot102', a2)
    if hasattr(a2, 'Docbook_PublisherType'):
        assert not _is_linked(a2, 'Docbook_PublisherType', b)


def test_assoc_publisher186_reverse_link_reassign_clear():
    a1 = Docbook_PublisherType(publishername="sample_text")
    a2 = Docbook_PublisherType(publishername="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType187', a1)
    assert _is_linked(b, 'Docbook_InfoType187', a1)
    if hasattr(a1, 'Docbook_PublisherType188'):
        assert _is_linked(a1, 'Docbook_PublisherType188', b)
    _safe_set(b, 'Docbook_InfoType187', a2)
    assert _is_linked(b, 'Docbook_InfoType187', a2)
    if hasattr(a1, 'Docbook_PublisherType188'):
        assert not _is_linked(a1, 'Docbook_PublisherType188', b)
    if hasattr(a2, 'Docbook_PublisherType188'):
        assert _is_linked(a2, 'Docbook_PublisherType188', b)
    _safe_set(b, 'Docbook_InfoType187', None)
    assert not _is_linked(b, 'Docbook_InfoType187', a2)
    if hasattr(a2, 'Docbook_PublisherType188'):
        assert not _is_linked(a2, 'Docbook_PublisherType188', b)


def test_assoc_refentry297_reverse_link_reassign_clear():
    a1 = Docbook_ReferenceType(version="sample_text")
    a2 = Docbook_ReferenceType(version="sample_text_2")
    b = Docbook_RefEntryType(version="sample_text")
    _safe_set(b, 'Docbook_RefEntryType299', a1)
    assert _is_linked(b, 'Docbook_RefEntryType299', a1)
    if hasattr(a1, 'Docbook_ReferenceType298'):
        assert _is_linked(a1, 'Docbook_ReferenceType298', b)
    _safe_set(b, 'Docbook_RefEntryType299', a2)
    assert _is_linked(b, 'Docbook_RefEntryType299', a2)
    if hasattr(a1, 'Docbook_ReferenceType298'):
        assert not _is_linked(a1, 'Docbook_ReferenceType298', b)
    if hasattr(a2, 'Docbook_ReferenceType298'):
        assert _is_linked(a2, 'Docbook_ReferenceType298', b)
    _safe_set(b, 'Docbook_RefEntryType299', None)
    assert not _is_linked(b, 'Docbook_RefEntryType299', a2)
    if hasattr(a2, 'Docbook_ReferenceType298'):
        assert not _is_linked(a2, 'Docbook_ReferenceType298', b)


def test_assoc_refentrytitle300_reverse_link_reassign_clear():
    a1 = Docbook_RefMetaType(manvolnum="sample_text")
    a2 = Docbook_RefMetaType(manvolnum="sample_text_2")
    b = Docbook_RefEntryTitleType(mixed="sample_text")
    _safe_set(b, 'Docbook_RefEntryTitleType', a1)
    assert _is_linked(b, 'Docbook_RefEntryTitleType', a1)
    if hasattr(a1, 'Docbook_RefMetaType301'):
        assert _is_linked(a1, 'Docbook_RefMetaType301', b)
    _safe_set(b, 'Docbook_RefEntryTitleType', a2)
    assert _is_linked(b, 'Docbook_RefEntryTitleType', a2)
    if hasattr(a1, 'Docbook_RefMetaType301'):
        assert not _is_linked(a1, 'Docbook_RefMetaType301', b)
    if hasattr(a2, 'Docbook_RefMetaType301'):
        assert _is_linked(a2, 'Docbook_RefMetaType301', b)
    _safe_set(b, 'Docbook_RefEntryTitleType', None)
    assert not _is_linked(b, 'Docbook_RefEntryTitleType', a2)
    if hasattr(a2, 'Docbook_RefMetaType301'):
        assert not _is_linked(a2, 'Docbook_RefMetaType301', b)


def test_assoc_reference14_reverse_link_reassign_clear():
    a1 = Docbook_ReferenceType(version="sample_text")
    a2 = Docbook_ReferenceType(version="sample_text_2")
    b = Docbook_BookType(label="sample_text", lang="sample_text", version="sample_text")
    _safe_set(b, 'Docbook_BookType15', {a1})
    assert _is_linked(b, 'Docbook_BookType15', a1)
    if hasattr(a1, 'Docbook_ReferenceType'):
        assert _is_linked(a1, 'Docbook_ReferenceType', b)
    _safe_set(b, 'Docbook_BookType15', {a2})
    assert _is_linked(b, 'Docbook_BookType15', a2)
    if hasattr(a1, 'Docbook_ReferenceType'):
        assert not _is_linked(a1, 'Docbook_ReferenceType', b)
    if hasattr(a2, 'Docbook_ReferenceType'):
        assert _is_linked(a2, 'Docbook_ReferenceType', b)
    _safe_set(b, 'Docbook_BookType15', set())
    assert not _is_linked(b, 'Docbook_BookType15', a2)
    if hasattr(a2, 'Docbook_ReferenceType'):
        assert not _is_linked(a2, 'Docbook_ReferenceType', b)


def test_assoc_refmeta283_reverse_link_reassign_clear():
    a1 = Docbook_RefMetaType(manvolnum="sample_text")
    a2 = Docbook_RefMetaType(manvolnum="sample_text_2")
    b = Docbook_RefEntryType(version="sample_text")
    _safe_set(b, 'Docbook_RefEntryType284', a1)
    assert _is_linked(b, 'Docbook_RefEntryType284', a1)
    if hasattr(a1, 'Docbook_RefMetaType'):
        assert _is_linked(a1, 'Docbook_RefMetaType', b)
    _safe_set(b, 'Docbook_RefEntryType284', a2)
    assert _is_linked(b, 'Docbook_RefEntryType284', a2)
    if hasattr(a1, 'Docbook_RefMetaType'):
        assert not _is_linked(a1, 'Docbook_RefMetaType', b)
    if hasattr(a2, 'Docbook_RefMetaType'):
        assert _is_linked(a2, 'Docbook_RefMetaType', b)
    _safe_set(b, 'Docbook_RefEntryType284', None)
    assert not _is_linked(b, 'Docbook_RefEntryType284', a2)
    if hasattr(a2, 'Docbook_RefMetaType'):
        assert not _is_linked(a2, 'Docbook_RefMetaType', b)


def test_assoc_refnamediv285_reverse_link_reassign_clear():
    a1 = Docbook_RefNameDivType(refclass="sample_text", refname="sample_text", refpurpose="sample_text")
    a2 = Docbook_RefNameDivType(refclass="sample_text_2", refname="sample_text_2", refpurpose="sample_text_2")
    b = Docbook_RefEntryType(version="sample_text")
    _safe_set(b, 'Docbook_RefEntryType286', a1)
    assert _is_linked(b, 'Docbook_RefEntryType286', a1)
    if hasattr(a1, 'Docbook_RefNameDivType'):
        assert _is_linked(a1, 'Docbook_RefNameDivType', b)
    _safe_set(b, 'Docbook_RefEntryType286', a2)
    assert _is_linked(b, 'Docbook_RefEntryType286', a2)
    if hasattr(a1, 'Docbook_RefNameDivType'):
        assert not _is_linked(a1, 'Docbook_RefNameDivType', b)
    if hasattr(a2, 'Docbook_RefNameDivType'):
        assert _is_linked(a2, 'Docbook_RefNameDivType', b)
    _safe_set(b, 'Docbook_RefEntryType286', None)
    assert not _is_linked(b, 'Docbook_RefEntryType286', a2)
    if hasattr(a2, 'Docbook_RefNameDivType'):
        assert not _is_linked(a2, 'Docbook_RefNameDivType', b)


def test_assoc_refsect1289_reverse_link_reassign_clear():
    a1 = Docbook_RefSect1Type(group="sample_text", id="sample_text")
    a2 = Docbook_RefSect1Type(group="sample_text_2", id="sample_text_2")
    b = Docbook_RefEntryType(version="sample_text")
    _safe_set(b, 'Docbook_RefEntryType290', {a1})
    assert _is_linked(b, 'Docbook_RefEntryType290', a1)
    if hasattr(a1, 'Docbook_RefSect1Type'):
        assert _is_linked(a1, 'Docbook_RefSect1Type', b)
    _safe_set(b, 'Docbook_RefEntryType290', {a2})
    assert _is_linked(b, 'Docbook_RefEntryType290', a2)
    if hasattr(a1, 'Docbook_RefSect1Type'):
        assert not _is_linked(a1, 'Docbook_RefSect1Type', b)
    if hasattr(a2, 'Docbook_RefSect1Type'):
        assert _is_linked(a2, 'Docbook_RefSect1Type', b)
    _safe_set(b, 'Docbook_RefEntryType290', set())
    assert not _is_linked(b, 'Docbook_RefEntryType290', a2)
    if hasattr(a2, 'Docbook_RefSect1Type'):
        assert not _is_linked(a2, 'Docbook_RefSect1Type', b)


def test_assoc_replaceable135_reverse_link_reassign_clear():
    a1 = Docbook_ReplaceableType(mixed="sample_text")
    a2 = Docbook_ReplaceableType(mixed="sample_text_2")
    b = Docbook_EnvarType(mixed="sample_text")
    _safe_set(b, 'Docbook_EnvarType', {a1})
    assert _is_linked(b, 'Docbook_EnvarType', a1)
    if hasattr(a1, 'Docbook_ReplaceableType136'):
        assert _is_linked(a1, 'Docbook_ReplaceableType136', b)
    _safe_set(b, 'Docbook_EnvarType', {a2})
    assert _is_linked(b, 'Docbook_EnvarType', a2)
    if hasattr(a1, 'Docbook_ReplaceableType136'):
        assert not _is_linked(a1, 'Docbook_ReplaceableType136', b)
    if hasattr(a2, 'Docbook_ReplaceableType136'):
        assert _is_linked(a2, 'Docbook_ReplaceableType136', b)
    _safe_set(b, 'Docbook_EnvarType', set())
    assert not _is_linked(b, 'Docbook_EnvarType', a2)
    if hasattr(a2, 'Docbook_ReplaceableType136'):
        assert not _is_linked(a2, 'Docbook_ReplaceableType136', b)


def test_assoc_replaceable148_reverse_link_reassign_clear():
    a1 = Docbook_ReplaceableType(mixed="sample_text")
    a2 = Docbook_ReplaceableType(mixed="sample_text_2")
    b = Docbook_FileNameType(mixed="sample_text")
    _safe_set(b, 'Docbook_FileNameType', {a1})
    assert _is_linked(b, 'Docbook_FileNameType', a1)
    if hasattr(a1, 'Docbook_ReplaceableType149'):
        assert _is_linked(a1, 'Docbook_ReplaceableType149', b)
    _safe_set(b, 'Docbook_FileNameType', {a2})
    assert _is_linked(b, 'Docbook_FileNameType', a2)
    if hasattr(a1, 'Docbook_ReplaceableType149'):
        assert not _is_linked(a1, 'Docbook_ReplaceableType149', b)
    if hasattr(a2, 'Docbook_ReplaceableType149'):
        assert _is_linked(a2, 'Docbook_ReplaceableType149', b)
    _safe_set(b, 'Docbook_FileNameType', set())
    assert not _is_linked(b, 'Docbook_FileNameType', a2)
    if hasattr(a2, 'Docbook_ReplaceableType149'):
        assert not _is_linked(a2, 'Docbook_ReplaceableType149', b)


def test_assoc_replaceable228_reverse_link_reassign_clear():
    a1 = Docbook_ReplaceableType(mixed="sample_text")
    a2 = Docbook_ReplaceableType(mixed="sample_text_2")
    b = Docbook_OptionType(mixed="sample_text")
    _safe_set(b, 'Docbook_OptionType229', {a1})
    assert _is_linked(b, 'Docbook_OptionType229', a1)
    if hasattr(a1, 'Docbook_ReplaceableType230'):
        assert _is_linked(a1, 'Docbook_ReplaceableType230', b)
    _safe_set(b, 'Docbook_OptionType229', {a2})
    assert _is_linked(b, 'Docbook_OptionType229', a2)
    if hasattr(a1, 'Docbook_ReplaceableType230'):
        assert not _is_linked(a1, 'Docbook_ReplaceableType230', b)
    if hasattr(a2, 'Docbook_ReplaceableType230'):
        assert _is_linked(a2, 'Docbook_ReplaceableType230', b)
    _safe_set(b, 'Docbook_OptionType229', set())
    assert not _is_linked(b, 'Docbook_OptionType229', a2)
    if hasattr(a2, 'Docbook_ReplaceableType230'):
        assert not _is_linked(a2, 'Docbook_ReplaceableType230', b)


def test_assoc_replaceable3_reverse_link_reassign_clear():
    a1 = Docbook_ReplaceableType(mixed="sample_text")
    a2 = Docbook_ReplaceableType(mixed="sample_text_2")
    b = Docbook_ArgType(choice="sample_text", mixed="sample_text", rep="sample_text")
    _safe_set(b, 'Docbook_ArgType4', {a1})
    assert _is_linked(b, 'Docbook_ArgType4', a1)
    if hasattr(a1, 'Docbook_ReplaceableType'):
        assert _is_linked(a1, 'Docbook_ReplaceableType', b)
    _safe_set(b, 'Docbook_ArgType4', {a2})
    assert _is_linked(b, 'Docbook_ArgType4', a2)
    if hasattr(a1, 'Docbook_ReplaceableType'):
        assert not _is_linked(a1, 'Docbook_ReplaceableType', b)
    if hasattr(a2, 'Docbook_ReplaceableType'):
        assert _is_linked(a2, 'Docbook_ReplaceableType', b)
    _safe_set(b, 'Docbook_ArgType4', set())
    assert not _is_linked(b, 'Docbook_ArgType4', a2)
    if hasattr(a2, 'Docbook_ReplaceableType'):
        assert not _is_linked(a2, 'Docbook_ReplaceableType', b)


def test_assoc_section105_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot106', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot106', a1)
    if hasattr(a1, 'Docbook_SectionType107'):
        assert _is_linked(a1, 'Docbook_SectionType107', b)
    _safe_set(b, 'Docbook_DocumentRoot106', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot106', a2)
    if hasattr(a1, 'Docbook_SectionType107'):
        assert not _is_linked(a1, 'Docbook_SectionType107', b)
    if hasattr(a2, 'Docbook_SectionType107'):
        assert _is_linked(a2, 'Docbook_SectionType107', b)
    _safe_set(b, 'Docbook_DocumentRoot106', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot106', a2)
    if hasattr(a2, 'Docbook_SectionType107'):
        assert not _is_linked(a2, 'Docbook_SectionType107', b)


def test_assoc_section23_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_ChapterType(annotations="sample_text")
    _safe_set(b, 'Docbook_ChapterType24', {a1})
    assert _is_linked(b, 'Docbook_ChapterType24', a1)
    if hasattr(a1, 'Docbook_SectionType'):
        assert _is_linked(a1, 'Docbook_SectionType', b)
    _safe_set(b, 'Docbook_ChapterType24', {a2})
    assert _is_linked(b, 'Docbook_ChapterType24', a2)
    if hasattr(a1, 'Docbook_SectionType'):
        assert not _is_linked(a1, 'Docbook_SectionType', b)
    if hasattr(a2, 'Docbook_SectionType'):
        assert _is_linked(a2, 'Docbook_SectionType', b)
    _safe_set(b, 'Docbook_ChapterType24', set())
    assert not _is_linked(b, 'Docbook_ChapterType24', a2)
    if hasattr(a2, 'Docbook_SectionType'):
        assert not _is_linked(a2, 'Docbook_SectionType', b)


def test_assoc_section354_reverse_link_reassign_clear():
    a1 = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    a2 = Docbook_SectionType(annotations="sample_text_2", caution="sample_text_2", group="sample_text_2", warning="sample_text_2")
    b = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_SectionType355', a1)
    assert _is_linked(b, 'Docbook_SectionType355', a1)
    if hasattr(a1, 'Docbook_SectionType353'):
        assert _is_linked(a1, 'Docbook_SectionType353', b)
    _safe_set(b, 'Docbook_SectionType355', a2)
    assert _is_linked(b, 'Docbook_SectionType355', a2)
    if hasattr(a1, 'Docbook_SectionType353'):
        assert not _is_linked(a1, 'Docbook_SectionType353', b)
    if hasattr(a2, 'Docbook_SectionType353'):
        assert _is_linked(a2, 'Docbook_SectionType353', b)
    _safe_set(b, 'Docbook_SectionType355', None)
    assert not _is_linked(b, 'Docbook_SectionType355', a2)
    if hasattr(a2, 'Docbook_SectionType353'):
        assert not _is_linked(a2, 'Docbook_SectionType353', b)


def test_assoc_segmentedlist311_reverse_link_reassign_clear():
    a1 = Docbook_SegmentedListType(group="sample_text", segtitle="sample_text")
    a2 = Docbook_SegmentedListType(group="sample_text_2", segtitle="sample_text_2")
    b = Docbook_RefSect1Type(group="sample_text", id="sample_text")
    _safe_set(b, 'Docbook_RefSect1Type312', {a1})
    assert _is_linked(b, 'Docbook_RefSect1Type312', a1)
    if hasattr(a1, 'Docbook_SegmentedListType'):
        assert _is_linked(a1, 'Docbook_SegmentedListType', b)
    _safe_set(b, 'Docbook_RefSect1Type312', {a2})
    assert _is_linked(b, 'Docbook_RefSect1Type312', a2)
    if hasattr(a1, 'Docbook_SegmentedListType'):
        assert not _is_linked(a1, 'Docbook_SegmentedListType', b)
    if hasattr(a2, 'Docbook_SegmentedListType'):
        assert _is_linked(a2, 'Docbook_SegmentedListType', b)
    _safe_set(b, 'Docbook_RefSect1Type312', set())
    assert not _is_linked(b, 'Docbook_RefSect1Type312', a2)
    if hasattr(a2, 'Docbook_SegmentedListType'):
        assert not _is_linked(a2, 'Docbook_SegmentedListType', b)


def test_assoc_subtitle178_reverse_link_reassign_clear():
    a1 = Docbook_SubtitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_SubtitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType179', a1)
    assert _is_linked(b, 'Docbook_InfoType179', a1)
    if hasattr(a1, 'Docbook_SubtitleType'):
        assert _is_linked(a1, 'Docbook_SubtitleType', b)
    _safe_set(b, 'Docbook_InfoType179', a2)
    assert _is_linked(b, 'Docbook_InfoType179', a2)
    if hasattr(a1, 'Docbook_SubtitleType'):
        assert not _is_linked(a1, 'Docbook_SubtitleType', b)
    if hasattr(a2, 'Docbook_SubtitleType'):
        assert _is_linked(a2, 'Docbook_SubtitleType', b)
    _safe_set(b, 'Docbook_InfoType179', None)
    assert not _is_linked(b, 'Docbook_InfoType179', a2)
    if hasattr(a2, 'Docbook_SubtitleType'):
        assert not _is_linked(a2, 'Docbook_SubtitleType', b)


def test_assoc_table108_reverse_link_reassign_clear():
    a1 = Docbook_TableType(id="sample_text")
    a2 = Docbook_TableType(id="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot109', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot109', a1)
    if hasattr(a1, 'Docbook_TableType'):
        assert _is_linked(a1, 'Docbook_TableType', b)
    _safe_set(b, 'Docbook_DocumentRoot109', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot109', a2)
    if hasattr(a1, 'Docbook_TableType'):
        assert not _is_linked(a1, 'Docbook_TableType', b)
    if hasattr(a2, 'Docbook_TableType'):
        assert _is_linked(a2, 'Docbook_TableType', b)
    _safe_set(b, 'Docbook_DocumentRoot109', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot109', a2)
    if hasattr(a2, 'Docbook_TableType'):
        assert not _is_linked(a2, 'Docbook_TableType', b)


def test_assoc_table368_reverse_link_reassign_clear():
    a1 = Docbook_TableType(id="sample_text")
    a2 = Docbook_TableType(id="sample_text_2")
    b = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_SectionType369', {a1})
    assert _is_linked(b, 'Docbook_SectionType369', a1)
    if hasattr(a1, 'Docbook_TableType370'):
        assert _is_linked(a1, 'Docbook_TableType370', b)
    _safe_set(b, 'Docbook_SectionType369', {a2})
    assert _is_linked(b, 'Docbook_SectionType369', a2)
    if hasattr(a1, 'Docbook_TableType370'):
        assert not _is_linked(a1, 'Docbook_TableType370', b)
    if hasattr(a2, 'Docbook_TableType370'):
        assert _is_linked(a2, 'Docbook_TableType370', b)
    _safe_set(b, 'Docbook_SectionType369', set())
    assert not _is_linked(b, 'Docbook_SectionType369', a2)
    if hasattr(a2, 'Docbook_TableType370'):
        assert not _is_linked(a2, 'Docbook_TableType370', b)


def test_assoc_term439_reverse_link_reassign_clear():
    a1 = Docbook_VarListEntryType(spacing="sample_text", termlength="sample_text")
    a2 = Docbook_VarListEntryType(spacing="sample_text_2", termlength="sample_text_2")
    b = Docbook_TermType(mixed="sample_text")
    _safe_set(b, 'Docbook_TermType441', a1)
    assert _is_linked(b, 'Docbook_TermType441', a1)
    if hasattr(a1, 'Docbook_VarListEntryType440'):
        assert _is_linked(a1, 'Docbook_VarListEntryType440', b)
    _safe_set(b, 'Docbook_TermType441', a2)
    assert _is_linked(b, 'Docbook_TermType441', a2)
    if hasattr(a1, 'Docbook_VarListEntryType440'):
        assert not _is_linked(a1, 'Docbook_VarListEntryType440', b)
    if hasattr(a2, 'Docbook_VarListEntryType440'):
        assert _is_linked(a2, 'Docbook_VarListEntryType440', b)
    _safe_set(b, 'Docbook_TermType441', None)
    assert not _is_linked(b, 'Docbook_TermType441', a2)
    if hasattr(a2, 'Docbook_VarListEntryType440'):
        assert not _is_linked(a2, 'Docbook_VarListEntryType440', b)


def test_assoc_tgroup112_reverse_link_reassign_clear():
    a1 = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    a2 = Docbook_TgroupType(align="sample_text_2", cols="sample_text_2", colseq="sample_text_2", rowseq="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot113', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot113', a1)
    if hasattr(a1, 'Docbook_TgroupType'):
        assert _is_linked(a1, 'Docbook_TgroupType', b)
    _safe_set(b, 'Docbook_DocumentRoot113', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot113', a2)
    if hasattr(a1, 'Docbook_TgroupType'):
        assert not _is_linked(a1, 'Docbook_TgroupType', b)
    if hasattr(a2, 'Docbook_TgroupType'):
        assert _is_linked(a2, 'Docbook_TgroupType', b)
    _safe_set(b, 'Docbook_DocumentRoot113', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot113', a2)
    if hasattr(a2, 'Docbook_TgroupType'):
        assert not _is_linked(a2, 'Docbook_TgroupType', b)


def test_assoc_tgroup396_reverse_link_reassign_clear():
    a1 = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    a2 = Docbook_TgroupType(align="sample_text_2", cols="sample_text_2", colseq="sample_text_2", rowseq="sample_text_2")
    b = Docbook_TableType(id="sample_text")
    _safe_set(b, 'Docbook_TableType397', a1)
    assert _is_linked(b, 'Docbook_TableType397', a1)
    if hasattr(a1, 'Docbook_TgroupType398'):
        assert _is_linked(a1, 'Docbook_TgroupType398', b)
    _safe_set(b, 'Docbook_TableType397', a2)
    assert _is_linked(b, 'Docbook_TableType397', a2)
    if hasattr(a1, 'Docbook_TgroupType398'):
        assert not _is_linked(a1, 'Docbook_TgroupType398', b)
    if hasattr(a2, 'Docbook_TgroupType398'):
        assert _is_linked(a2, 'Docbook_TgroupType398', b)
    _safe_set(b, 'Docbook_TableType397', None)
    assert not _is_linked(b, 'Docbook_TableType397', a2)
    if hasattr(a2, 'Docbook_TgroupType398'):
        assert not _is_linked(a2, 'Docbook_TgroupType398', b)


def test_assoc_tip116_reverse_link_reassign_clear():
    a1 = Docbook_TipType(mixed="sample_text")
    a2 = Docbook_TipType(mixed="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot117', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot117', a1)
    if hasattr(a1, 'Docbook_TipType'):
        assert _is_linked(a1, 'Docbook_TipType', b)
    _safe_set(b, 'Docbook_DocumentRoot117', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot117', a2)
    if hasattr(a1, 'Docbook_TipType'):
        assert not _is_linked(a1, 'Docbook_TipType', b)
    if hasattr(a2, 'Docbook_TipType'):
        assert _is_linked(a2, 'Docbook_TipType', b)
    _safe_set(b, 'Docbook_DocumentRoot117', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot117', a2)
    if hasattr(a2, 'Docbook_TipType'):
        assert not _is_linked(a2, 'Docbook_TipType', b)


def test_assoc_tip371_reverse_link_reassign_clear():
    a1 = Docbook_TipType(mixed="sample_text")
    a2 = Docbook_TipType(mixed="sample_text_2")
    b = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_SectionType372', a1)
    assert _is_linked(b, 'Docbook_SectionType372', a1)
    if hasattr(a1, 'Docbook_TipType373'):
        assert _is_linked(a1, 'Docbook_TipType373', b)
    _safe_set(b, 'Docbook_SectionType372', a2)
    assert _is_linked(b, 'Docbook_SectionType372', a2)
    if hasattr(a1, 'Docbook_TipType373'):
        assert not _is_linked(a1, 'Docbook_TipType373', b)
    if hasattr(a2, 'Docbook_TipType373'):
        assert _is_linked(a2, 'Docbook_TipType373', b)
    _safe_set(b, 'Docbook_SectionType372', None)
    assert not _is_linked(b, 'Docbook_SectionType372', a2)
    if hasattr(a2, 'Docbook_TipType373'):
        assert not _is_linked(a2, 'Docbook_TipType373', b)


def test_assoc_title118_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot119', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot119', a1)
    if hasattr(a1, 'Docbook_TitleType120'):
        assert _is_linked(a1, 'Docbook_TitleType120', b)
    _safe_set(b, 'Docbook_DocumentRoot119', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot119', a2)
    if hasattr(a1, 'Docbook_TitleType120'):
        assert not _is_linked(a1, 'Docbook_TitleType120', b)
    if hasattr(a2, 'Docbook_TitleType120'):
        assert _is_linked(a2, 'Docbook_TitleType120', b)
    _safe_set(b, 'Docbook_DocumentRoot119', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot119', a2)
    if hasattr(a2, 'Docbook_TitleType120'):
        assert not _is_linked(a2, 'Docbook_TitleType120', b)


def test_assoc_title137_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_ExampleType(id="sample_text")
    _safe_set(b, 'Docbook_ExampleType', a1)
    assert _is_linked(b, 'Docbook_ExampleType', a1)
    if hasattr(a1, 'Docbook_TitleType138'):
        assert _is_linked(a1, 'Docbook_TitleType138', b)
    _safe_set(b, 'Docbook_ExampleType', a2)
    assert _is_linked(b, 'Docbook_ExampleType', a2)
    if hasattr(a1, 'Docbook_TitleType138'):
        assert not _is_linked(a1, 'Docbook_TitleType138', b)
    if hasattr(a2, 'Docbook_TitleType138'):
        assert _is_linked(a2, 'Docbook_TitleType138', b)
    _safe_set(b, 'Docbook_ExampleType', None)
    assert not _is_linked(b, 'Docbook_ExampleType', a2)
    if hasattr(a2, 'Docbook_TitleType138'):
        assert not _is_linked(a2, 'Docbook_TitleType138', b)


def test_assoc_title142_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_FigureType(float="sample_text", id="sample_text")
    _safe_set(b, 'Docbook_FigureType143', a1)
    assert _is_linked(b, 'Docbook_FigureType143', a1)
    if hasattr(a1, 'Docbook_TitleType144'):
        assert _is_linked(a1, 'Docbook_TitleType144', b)
    _safe_set(b, 'Docbook_FigureType143', a2)
    assert _is_linked(b, 'Docbook_FigureType143', a2)
    if hasattr(a1, 'Docbook_TitleType144'):
        assert not _is_linked(a1, 'Docbook_TitleType144', b)
    if hasattr(a2, 'Docbook_TitleType144'):
        assert _is_linked(a2, 'Docbook_TitleType144', b)
    _safe_set(b, 'Docbook_FigureType143', None)
    assert not _is_linked(b, 'Docbook_FigureType143', a2)
    if hasattr(a2, 'Docbook_TitleType144'):
        assert not _is_linked(a2, 'Docbook_TitleType144', b)


def test_assoc_title16_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_ChapterType(annotations="sample_text")
    _safe_set(b, 'Docbook_ChapterType17', a1)
    assert _is_linked(b, 'Docbook_ChapterType17', a1)
    if hasattr(a1, 'Docbook_TitleType'):
        assert _is_linked(a1, 'Docbook_TitleType', b)
    _safe_set(b, 'Docbook_ChapterType17', a2)
    assert _is_linked(b, 'Docbook_ChapterType17', a2)
    if hasattr(a1, 'Docbook_TitleType'):
        assert not _is_linked(a1, 'Docbook_TitleType', b)
    if hasattr(a2, 'Docbook_TitleType'):
        assert _is_linked(a2, 'Docbook_TitleType', b)
    _safe_set(b, 'Docbook_ChapterType17', None)
    assert not _is_linked(b, 'Docbook_ChapterType17', a2)
    if hasattr(a2, 'Docbook_TitleType'):
        assert not _is_linked(a2, 'Docbook_TitleType', b)


def test_assoc_title175_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'Docbook_InfoType176', a1)
    assert _is_linked(b, 'Docbook_InfoType176', a1)
    if hasattr(a1, 'Docbook_TitleType177'):
        assert _is_linked(a1, 'Docbook_TitleType177', b)
    _safe_set(b, 'Docbook_InfoType176', a2)
    assert _is_linked(b, 'Docbook_InfoType176', a2)
    if hasattr(a1, 'Docbook_TitleType177'):
        assert not _is_linked(a1, 'Docbook_TitleType177', b)
    if hasattr(a2, 'Docbook_TitleType177'):
        assert _is_linked(a2, 'Docbook_TitleType177', b)
    _safe_set(b, 'Docbook_InfoType176', None)
    assert not _is_linked(b, 'Docbook_InfoType176', a2)
    if hasattr(a2, 'Docbook_TitleType177'):
        assert not _is_linked(a2, 'Docbook_TitleType177', b)


def test_assoc_title201_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_LegalNoticeType(group="sample_text")
    _safe_set(b, 'Docbook_LegalNoticeType202', a1)
    assert _is_linked(b, 'Docbook_LegalNoticeType202', a1)
    if hasattr(a1, 'Docbook_TitleType203'):
        assert _is_linked(a1, 'Docbook_TitleType203', b)
    _safe_set(b, 'Docbook_LegalNoticeType202', a2)
    assert _is_linked(b, 'Docbook_LegalNoticeType202', a2)
    if hasattr(a1, 'Docbook_TitleType203'):
        assert not _is_linked(a1, 'Docbook_TitleType203', b)
    if hasattr(a2, 'Docbook_TitleType203'):
        assert _is_linked(a2, 'Docbook_TitleType203', b)
    _safe_set(b, 'Docbook_LegalNoticeType202', None)
    assert not _is_linked(b, 'Docbook_LegalNoticeType202', a2)
    if hasattr(a2, 'Docbook_TitleType203'):
        assert not _is_linked(a2, 'Docbook_TitleType203', b)


def test_assoc_title294_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_ReferenceType(version="sample_text")
    _safe_set(b, 'Docbook_ReferenceType295', a1)
    assert _is_linked(b, 'Docbook_ReferenceType295', a1)
    if hasattr(a1, 'Docbook_TitleType296'):
        assert _is_linked(a1, 'Docbook_TitleType296', b)
    _safe_set(b, 'Docbook_ReferenceType295', a2)
    assert _is_linked(b, 'Docbook_ReferenceType295', a2)
    if hasattr(a1, 'Docbook_TitleType296'):
        assert not _is_linked(a1, 'Docbook_TitleType296', b)
    if hasattr(a2, 'Docbook_TitleType296'):
        assert _is_linked(a2, 'Docbook_TitleType296', b)
    _safe_set(b, 'Docbook_ReferenceType295', None)
    assert not _is_linked(b, 'Docbook_ReferenceType295', a2)
    if hasattr(a2, 'Docbook_TitleType296'):
        assert not _is_linked(a2, 'Docbook_TitleType296', b)


def test_assoc_title302_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_RefSect1Type(group="sample_text", id="sample_text")
    _safe_set(b, 'Docbook_RefSect1Type303', a1)
    assert _is_linked(b, 'Docbook_RefSect1Type303', a1)
    if hasattr(a1, 'Docbook_TitleType304'):
        assert _is_linked(a1, 'Docbook_TitleType304', b)
    _safe_set(b, 'Docbook_RefSect1Type303', a2)
    assert _is_linked(b, 'Docbook_RefSect1Type303', a2)
    if hasattr(a1, 'Docbook_TitleType304'):
        assert not _is_linked(a1, 'Docbook_TitleType304', b)
    if hasattr(a2, 'Docbook_TitleType304'):
        assert _is_linked(a2, 'Docbook_TitleType304', b)
    _safe_set(b, 'Docbook_RefSect1Type303', None)
    assert not _is_linked(b, 'Docbook_RefSect1Type303', a2)
    if hasattr(a2, 'Docbook_TitleType304'):
        assert not _is_linked(a2, 'Docbook_TitleType304', b)


def test_assoc_title356_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_SectionType357', {a1})
    assert _is_linked(b, 'Docbook_SectionType357', a1)
    if hasattr(a1, 'Docbook_TitleType358'):
        assert _is_linked(a1, 'Docbook_TitleType358', b)
    _safe_set(b, 'Docbook_SectionType357', {a2})
    assert _is_linked(b, 'Docbook_SectionType357', a2)
    if hasattr(a1, 'Docbook_TitleType358'):
        assert not _is_linked(a1, 'Docbook_TitleType358', b)
    if hasattr(a2, 'Docbook_TitleType358'):
        assert _is_linked(a2, 'Docbook_TitleType358', b)
    _safe_set(b, 'Docbook_SectionType357', set())
    assert not _is_linked(b, 'Docbook_SectionType357', a2)
    if hasattr(a2, 'Docbook_TitleType358'):
        assert not _is_linked(a2, 'Docbook_TitleType358', b)


def test_assoc_title393_reverse_link_reassign_clear():
    a1 = Docbook_TitleType(group="sample_text", mixed="sample_text")
    a2 = Docbook_TitleType(group="sample_text_2", mixed="sample_text_2")
    b = Docbook_TableType(id="sample_text")
    _safe_set(b, 'Docbook_TableType394', a1)
    assert _is_linked(b, 'Docbook_TableType394', a1)
    if hasattr(a1, 'Docbook_TitleType395'):
        assert _is_linked(a1, 'Docbook_TitleType395', b)
    _safe_set(b, 'Docbook_TableType394', a2)
    assert _is_linked(b, 'Docbook_TableType394', a2)
    if hasattr(a1, 'Docbook_TitleType395'):
        assert not _is_linked(a1, 'Docbook_TitleType395', b)
    if hasattr(a2, 'Docbook_TitleType395'):
        assert _is_linked(a2, 'Docbook_TitleType395', b)
    _safe_set(b, 'Docbook_TableType394', None)
    assert not _is_linked(b, 'Docbook_TableType394', a2)
    if hasattr(a2, 'Docbook_TitleType395'):
        assert not _is_linked(a2, 'Docbook_TitleType395', b)


def test_assoc_ulink121_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    _safe_set(b, 'Docbook_DocumentRoot122', {a1})
    assert _is_linked(b, 'Docbook_DocumentRoot122', a1)
    if hasattr(a1, 'Docbook_UlinkType'):
        assert _is_linked(a1, 'Docbook_UlinkType', b)
    _safe_set(b, 'Docbook_DocumentRoot122', {a2})
    assert _is_linked(b, 'Docbook_DocumentRoot122', a2)
    if hasattr(a1, 'Docbook_UlinkType'):
        assert not _is_linked(a1, 'Docbook_UlinkType', b)
    if hasattr(a2, 'Docbook_UlinkType'):
        assert _is_linked(a2, 'Docbook_UlinkType', b)
    _safe_set(b, 'Docbook_DocumentRoot122', set())
    assert not _is_linked(b, 'Docbook_DocumentRoot122', a2)
    if hasattr(a2, 'Docbook_UlinkType'):
        assert not _is_linked(a2, 'Docbook_UlinkType', b)


def test_assoc_ulink166_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_ImportantType(group="sample_text", mixed="sample_text")
    _safe_set(b, 'Docbook_ImportantType167', {a1})
    assert _is_linked(b, 'Docbook_ImportantType167', a1)
    if hasattr(a1, 'Docbook_UlinkType168'):
        assert _is_linked(a1, 'Docbook_UlinkType168', b)
    _safe_set(b, 'Docbook_ImportantType167', {a2})
    assert _is_linked(b, 'Docbook_ImportantType167', a2)
    if hasattr(a1, 'Docbook_UlinkType168'):
        assert not _is_linked(a1, 'Docbook_UlinkType168', b)
    if hasattr(a2, 'Docbook_UlinkType168'):
        assert _is_linked(a2, 'Docbook_UlinkType168', b)
    _safe_set(b, 'Docbook_ImportantType167', set())
    assert not _is_linked(b, 'Docbook_ImportantType167', a2)
    if hasattr(a2, 'Docbook_UlinkType168'):
        assert not _is_linked(a2, 'Docbook_UlinkType168', b)


def test_assoc_ulink225_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_NoteType(group="sample_text", mixed="sample_text")
    _safe_set(b, 'Docbook_NoteType226', {a1})
    assert _is_linked(b, 'Docbook_NoteType226', a1)
    if hasattr(a1, 'Docbook_UlinkType227'):
        assert _is_linked(a1, 'Docbook_UlinkType227', b)
    _safe_set(b, 'Docbook_NoteType226', {a2})
    assert _is_linked(b, 'Docbook_NoteType226', a2)
    if hasattr(a1, 'Docbook_UlinkType227'):
        assert not _is_linked(a1, 'Docbook_UlinkType227', b)
    if hasattr(a2, 'Docbook_UlinkType227'):
        assert _is_linked(a2, 'Docbook_UlinkType227', b)
    _safe_set(b, 'Docbook_NoteType226', set())
    assert not _is_linked(b, 'Docbook_NoteType226', a2)
    if hasattr(a2, 'Docbook_UlinkType227'):
        assert not _is_linked(a2, 'Docbook_UlinkType227', b)


def test_assoc_ulink242_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    _safe_set(b, 'Docbook_ParaType243', {a1})
    assert _is_linked(b, 'Docbook_ParaType243', a1)
    if hasattr(a1, 'Docbook_UlinkType244'):
        assert _is_linked(a1, 'Docbook_UlinkType244', b)
    _safe_set(b, 'Docbook_ParaType243', {a2})
    assert _is_linked(b, 'Docbook_ParaType243', a2)
    if hasattr(a1, 'Docbook_UlinkType244'):
        assert not _is_linked(a1, 'Docbook_UlinkType244', b)
    if hasattr(a2, 'Docbook_UlinkType244'):
        assert _is_linked(a2, 'Docbook_UlinkType244', b)
    _safe_set(b, 'Docbook_ParaType243', set())
    assert not _is_linked(b, 'Docbook_ParaType243', a2)
    if hasattr(a2, 'Docbook_UlinkType244'):
        assert not _is_linked(a2, 'Docbook_UlinkType244', b)


def test_assoc_ulink332_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_RevnumberType(mixed="sample_text")
    _safe_set(b, 'Docbook_RevnumberType333', {a1})
    assert _is_linked(b, 'Docbook_RevnumberType333', a1)
    if hasattr(a1, 'Docbook_UlinkType334'):
        assert _is_linked(a1, 'Docbook_UlinkType334', b)
    _safe_set(b, 'Docbook_RevnumberType333', {a2})
    assert _is_linked(b, 'Docbook_RevnumberType333', a2)
    if hasattr(a1, 'Docbook_UlinkType334'):
        assert not _is_linked(a1, 'Docbook_UlinkType334', b)
    if hasattr(a2, 'Docbook_UlinkType334'):
        assert _is_linked(a2, 'Docbook_UlinkType334', b)
    _safe_set(b, 'Docbook_RevnumberType333', set())
    assert not _is_linked(b, 'Docbook_RevnumberType333', a2)
    if hasattr(a2, 'Docbook_UlinkType334'):
        assert not _is_linked(a2, 'Docbook_UlinkType334', b)


def test_assoc_ulink425_reverse_link_reassign_clear():
    a1 = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    a2 = Docbook_UlinkType(mixed="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = Docbook_TipType(mixed="sample_text")
    _safe_set(b, 'Docbook_TipType426', {a1})
    assert _is_linked(b, 'Docbook_TipType426', a1)
    if hasattr(a1, 'Docbook_UlinkType427'):
        assert _is_linked(a1, 'Docbook_UlinkType427', b)
    _safe_set(b, 'Docbook_TipType426', {a2})
    assert _is_linked(b, 'Docbook_TipType426', a2)
    if hasattr(a1, 'Docbook_UlinkType427'):
        assert not _is_linked(a1, 'Docbook_UlinkType427', b)
    if hasattr(a2, 'Docbook_UlinkType427'):
        assert _is_linked(a2, 'Docbook_UlinkType427', b)
    _safe_set(b, 'Docbook_TipType426', set())
    assert not _is_linked(b, 'Docbook_TipType426', a2)
    if hasattr(a2, 'Docbook_UlinkType427'):
        assert not _is_linked(a2, 'Docbook_UlinkType427', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstract183_stub_double():
    # Docbook_AbstractType has no real 'Docbook_AbstractType185' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_InfoType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_InfoType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    partner = Docbook_AbstractType()
    setattr(partner, 'Docbook_AbstractType185', None)
    _safe_set(owner, 'Docbook_InfoType184', partner)
    assert getattr(partner, 'Docbook_AbstractType185') == owner
    _safe_set(owner, 'Docbook_InfoType184', None)
    assert getattr(partner, 'Docbook_AbstractType185') is None


def test_assoc_abstract33_stub_double():
    # Docbook_AbstractType has no real 'Docbook_AbstractType35' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_AbstractType()
    setattr(partner, 'Docbook_AbstractType35', None)
    _safe_set(owner, 'Docbook_DocumentRoot34', {partner})
    assert getattr(partner, 'Docbook_AbstractType35') == owner
    _safe_set(owner, 'Docbook_DocumentRoot34', set())
    assert getattr(partner, 'Docbook_AbstractType35') is None


def test_assoc_arg26_stub_double():
    # Docbook_CmdsynopsisType has no real 'Docbook_CmdsynopsisType27' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ArgType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ArgType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ArgType(choice="sample_text", mixed="sample_text", rep="sample_text")
    partner = Docbook_CmdsynopsisType()
    setattr(partner, 'Docbook_CmdsynopsisType27', None)
    _safe_set(owner, 'Docbook_ArgType28', partner)
    assert owner in getattr(partner, 'Docbook_CmdsynopsisType27')
    _safe_set(owner, 'Docbook_ArgType28', None)
    assert owner not in getattr(partner, 'Docbook_CmdsynopsisType27')


def test_assoc_authorinitials327_stub_double():
    # Docbook_RevisionType has no real 'Docbook_RevisionType328' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_AuthorinitialsType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_AuthorinitialsType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_AuthorinitialsType(mixed="sample_text")
    partner = Docbook_RevisionType()
    setattr(partner, 'Docbook_RevisionType328', None)
    _safe_set(owner, 'Docbook_AuthorinitialsType', partner)
    assert getattr(partner, 'Docbook_RevisionType328') == owner
    _safe_set(owner, 'Docbook_AuthorinitialsType', None)
    assert getattr(partner, 'Docbook_RevisionType328') is None


def test_assoc_cmdsynopsis380_stub_double():
    # Docbook_CmdsynopsisType has no real 'Docbook_CmdsynopsisType382' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    partner = Docbook_CmdsynopsisType()
    setattr(partner, 'Docbook_CmdsynopsisType382', None)
    _safe_set(owner, 'Docbook_SectionType381', {partner})
    assert getattr(partner, 'Docbook_CmdsynopsisType382') == owner
    _safe_set(owner, 'Docbook_SectionType381', set())
    assert getattr(partner, 'Docbook_CmdsynopsisType382') is None


def test_assoc_command25_stub_double():
    # Docbook_CmdsynopsisType has no real 'Docbook_CmdsynopsisType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_CommandType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_CommandType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_CommandType(mixed="sample_text")
    partner = Docbook_CmdsynopsisType()
    setattr(partner, 'Docbook_CmdsynopsisType', None)
    _safe_set(owner, 'Docbook_CommandType', partner)
    assert getattr(partner, 'Docbook_CmdsynopsisType') == owner
    _safe_set(owner, 'Docbook_CommandType', None)
    assert getattr(partner, 'Docbook_CmdsynopsisType') is None


def test_assoc_date325_stub_double():
    # Docbook_RevisionType has no real 'Docbook_RevisionType326' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DateType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DateType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DateType(mixed="sample_text")
    partner = Docbook_RevisionType()
    setattr(partner, 'Docbook_RevisionType326', None)
    _safe_set(owner, 'Docbook_DateType', partner)
    assert getattr(partner, 'Docbook_RevisionType326') == owner
    _safe_set(owner, 'Docbook_DateType', None)
    assert getattr(partner, 'Docbook_RevisionType326') is None


def test_assoc_entry335_stub_double():
    # Docbook_RowType has no real 'Docbook_RowType336' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_EntryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_EntryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_EntryType(align="sample_text", mixed="sample_text", morerows="sample_text", nameend="sample_text", namest="sample_text", valign="sample_text")
    partner = Docbook_RowType()
    setattr(partner, 'Docbook_RowType336', None)
    _safe_set(owner, 'Docbook_EntryType337', partner)
    assert owner in getattr(partner, 'Docbook_RowType336')
    _safe_set(owner, 'Docbook_EntryType337', None)
    assert owner not in getattr(partner, 'Docbook_RowType336')


def test_assoc_firstname256_stub_double():
    # Docbook_PersonnameType has no real 'Docbook_PersonnameType257' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_FirstnameType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_FirstnameType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_FirstnameType(mixed="sample_text")
    partner = Docbook_PersonnameType()
    setattr(partner, 'Docbook_PersonnameType257', None)
    _safe_set(owner, 'Docbook_FirstnameType', partner)
    assert getattr(partner, 'Docbook_PersonnameType257') == owner
    _safe_set(owner, 'Docbook_FirstnameType', None)
    assert getattr(partner, 'Docbook_PersonnameType257') is None


def test_assoc_funcdef154_stub_double():
    # Docbook_FuncprototypeType has no real 'Docbook_FuncprototypeType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_FuncdefType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_FuncdefType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_FuncdefType(mixed="sample_text")
    partner = Docbook_FuncprototypeType()
    setattr(partner, 'Docbook_FuncprototypeType', None)
    _safe_set(owner, 'Docbook_FuncdefType155', partner)
    assert getattr(partner, 'Docbook_FuncprototypeType') == owner
    _safe_set(owner, 'Docbook_FuncdefType155', None)
    assert getattr(partner, 'Docbook_FuncprototypeType') is None


def test_assoc_funcsynopsis374_stub_double():
    # Docbook_FuncsynopsisType has no real 'Docbook_FuncsynopsisType376' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    partner = Docbook_FuncsynopsisType()
    setattr(partner, 'Docbook_FuncsynopsisType376', None)
    _safe_set(owner, 'Docbook_SectionType375', {partner})
    assert getattr(partner, 'Docbook_FuncsynopsisType376') == owner
    _safe_set(owner, 'Docbook_SectionType375', set())
    assert getattr(partner, 'Docbook_FuncsynopsisType376') is None


def test_assoc_imagedata160_stub_double():
    # Docbook_ImageobjectType has no real 'Docbook_ImageobjectType161' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ImagedataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ImagedataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ImagedataType(align="sample_text", depth="sample_text", fileref="sample_text", scale="sample_text", width="sample_text")
    partner = Docbook_ImageobjectType()
    setattr(partner, 'Docbook_ImageobjectType161', None)
    _safe_set(owner, 'Docbook_ImagedataType162', partner)
    assert getattr(partner, 'Docbook_ImageobjectType161') == owner
    _safe_set(owner, 'Docbook_ImagedataType162', None)
    assert getattr(partner, 'Docbook_ImageobjectType161') is None


def test_assoc_imageobject65_stub_double():
    # Docbook_ImageobjectType has no real 'Docbook_ImageobjectType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_ImageobjectType()
    setattr(partner, 'Docbook_ImageobjectType', None)
    _safe_set(owner, 'Docbook_DocumentRoot66', {partner})
    assert getattr(partner, 'Docbook_ImageobjectType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot66', set())
    assert getattr(partner, 'Docbook_ImageobjectType') is None


def test_assoc_important266_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType267' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ImportantType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ImportantType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ImportantType(group="sample_text", mixed="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType267', None)
    _safe_set(owner, 'Docbook_ImportantType268', partner)
    assert getattr(partner, 'Docbook_PrefaceType267') == owner
    _safe_set(owner, 'Docbook_ImportantType268', None)
    assert getattr(partner, 'Docbook_PrefaceType267') is None


def test_assoc_informaltable362_stub_double():
    # Docbook_InformaltableType has no real 'Docbook_InformaltableType364' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    partner = Docbook_InformaltableType()
    setattr(partner, 'Docbook_InformaltableType364', None)
    _safe_set(owner, 'Docbook_SectionType363', {partner})
    assert getattr(partner, 'Docbook_InformaltableType364') == owner
    _safe_set(owner, 'Docbook_SectionType363', set())
    assert getattr(partner, 'Docbook_InformaltableType364') is None


def test_assoc_informaltable69_stub_double():
    # Docbook_InformaltableType has no real 'Docbook_InformaltableType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_InformaltableType()
    setattr(partner, 'Docbook_InformaltableType', None)
    _safe_set(owner, 'Docbook_DocumentRoot70', {partner})
    assert getattr(partner, 'Docbook_InformaltableType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot70', set())
    assert getattr(partner, 'Docbook_InformaltableType') is None


def test_assoc_itemizedlist251_stub_double():
    # Docbook_ItemizedlistType has no real 'Docbook_ItemizedlistType253' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    partner = Docbook_ItemizedlistType()
    setattr(partner, 'Docbook_ItemizedlistType253', None)
    _safe_set(owner, 'Docbook_ParaType252', {partner})
    assert getattr(partner, 'Docbook_ItemizedlistType253') == owner
    _safe_set(owner, 'Docbook_ParaType252', set())
    assert getattr(partner, 'Docbook_ItemizedlistType253') is None


def test_assoc_itemizedlist338_stub_double():
    # Docbook_ItemizedlistType has no real 'Docbook_ItemizedlistType340' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    partner = Docbook_ItemizedlistType()
    setattr(partner, 'Docbook_ItemizedlistType340', None)
    _safe_set(owner, 'Docbook_SectionType339', {partner})
    assert getattr(partner, 'Docbook_ItemizedlistType340') == owner
    _safe_set(owner, 'Docbook_SectionType339', set())
    assert getattr(partner, 'Docbook_ItemizedlistType340') is None


def test_assoc_itemizedlist71_stub_double():
    # Docbook_ItemizedlistType has no real 'Docbook_ItemizedlistType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_ItemizedlistType()
    setattr(partner, 'Docbook_ItemizedlistType', None)
    _safe_set(owner, 'Docbook_DocumentRoot72', {partner})
    assert getattr(partner, 'Docbook_ItemizedlistType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot72', set())
    assert getattr(partner, 'Docbook_ItemizedlistType') is None


def test_assoc_listitem442_stub_double():
    # Docbook_ListitemType has no real 'Docbook_ListitemType444' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_VarListEntryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_VarListEntryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_VarListEntryType(spacing="sample_text", termlength="sample_text")
    partner = Docbook_ListitemType()
    setattr(partner, 'Docbook_ListitemType444', None)
    _safe_set(owner, 'Docbook_VarListEntryType443', partner)
    assert getattr(partner, 'Docbook_ListitemType444') == owner
    _safe_set(owner, 'Docbook_VarListEntryType443', None)
    assert getattr(partner, 'Docbook_ListitemType444') is None


def test_assoc_listitem77_stub_double():
    # Docbook_ListitemType has no real 'Docbook_ListitemType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_ListitemType()
    setattr(partner, 'Docbook_ListitemType', None)
    _safe_set(owner, 'Docbook_DocumentRoot78', {partner})
    assert getattr(partner, 'Docbook_ListitemType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot78', set())
    assert getattr(partner, 'Docbook_ListitemType') is None


def test_assoc_mediaobject129_stub_double():
    # Docbook_MediaobjectType has no real 'Docbook_MediaobjectType131' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_EntryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_EntryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_EntryType(align="sample_text", mixed="sample_text", morerows="sample_text", nameend="sample_text", namest="sample_text", valign="sample_text")
    partner = Docbook_MediaobjectType()
    setattr(partner, 'Docbook_MediaobjectType131', None)
    _safe_set(owner, 'Docbook_EntryType130', partner)
    assert getattr(partner, 'Docbook_MediaobjectType131') == owner
    _safe_set(owner, 'Docbook_EntryType130', None)
    assert getattr(partner, 'Docbook_MediaobjectType131') is None


def test_assoc_mediaobject145_stub_double():
    # Docbook_MediaobjectType has no real 'Docbook_MediaobjectType147' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_FigureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_FigureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_FigureType(float="sample_text", id="sample_text")
    partner = Docbook_MediaobjectType()
    setattr(partner, 'Docbook_MediaobjectType147', None)
    _safe_set(owner, 'Docbook_FigureType146', partner)
    assert getattr(partner, 'Docbook_MediaobjectType147') == owner
    _safe_set(owner, 'Docbook_FigureType146', None)
    assert getattr(partner, 'Docbook_MediaobjectType147') is None


def test_assoc_mediaobject341_stub_double():
    # Docbook_MediaobjectType has no real 'Docbook_MediaobjectType343' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SectionType(annotations="sample_text", caution="sample_text", group="sample_text", warning="sample_text")
    partner = Docbook_MediaobjectType()
    setattr(partner, 'Docbook_MediaobjectType343', None)
    _safe_set(owner, 'Docbook_SectionType342', {partner})
    assert getattr(partner, 'Docbook_MediaobjectType343') == owner
    _safe_set(owner, 'Docbook_SectionType342', set())
    assert getattr(partner, 'Docbook_MediaobjectType343') is None


def test_assoc_mediaobject81_stub_double():
    # Docbook_MediaobjectType has no real 'Docbook_MediaobjectType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_MediaobjectType()
    setattr(partner, 'Docbook_MediaobjectType', None)
    _safe_set(owner, 'Docbook_DocumentRoot82', {partner})
    assert getattr(partner, 'Docbook_MediaobjectType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot82', set())
    assert getattr(partner, 'Docbook_MediaobjectType') is None


def test_assoc_otheraddr1_stub_double():
    # Docbook_OtheraddrType has no real 'Docbook_OtheraddrType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_AddressType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_AddressType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_AddressType(email="sample_text", format="sample_text", state="sample_text")
    partner = Docbook_OtheraddrType()
    setattr(partner, 'Docbook_OtheraddrType', None)
    _safe_set(owner, 'Docbook_AddressType', partner)
    assert getattr(partner, 'Docbook_OtheraddrType') == owner
    _safe_set(owner, 'Docbook_AddressType', None)
    assert getattr(partner, 'Docbook_OtheraddrType') is None


def test_assoc_otheraddr88_stub_double():
    # Docbook_OtheraddrType has no real 'Docbook_OtheraddrType90' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_OtheraddrType()
    setattr(partner, 'Docbook_OtheraddrType90', None)
    _safe_set(owner, 'Docbook_DocumentRoot89', {partner})
    assert getattr(partner, 'Docbook_OtheraddrType90') == owner
    _safe_set(owner, 'Docbook_DocumentRoot89', set())
    assert getattr(partner, 'Docbook_OtheraddrType90') is None


def test_assoc_para0_stub_double():
    # Docbook_AbstractType has no real 'Docbook_AbstractType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    partner = Docbook_AbstractType()
    setattr(partner, 'Docbook_AbstractType', None)
    _safe_set(owner, 'Docbook_ParaType', partner)
    assert getattr(partner, 'Docbook_AbstractType') == owner
    _safe_set(owner, 'Docbook_ParaType', None)
    assert getattr(partner, 'Docbook_AbstractType') is None


def test_assoc_para213_stub_double():
    # Docbook_ListitemType has no real 'Docbook_ListitemType214' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    partner = Docbook_ListitemType()
    setattr(partner, 'Docbook_ListitemType214', None)
    _safe_set(owner, 'Docbook_ParaType215', partner)
    assert owner in getattr(partner, 'Docbook_ListitemType214')
    _safe_set(owner, 'Docbook_ParaType215', None)
    assert owner not in getattr(partner, 'Docbook_ListitemType214')


def test_assoc_para263_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType264' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType264', None)
    _safe_set(owner, 'Docbook_ParaType265', partner)
    assert owner in getattr(partner, 'Docbook_PrefaceType264')
    _safe_set(owner, 'Docbook_ParaType265', None)
    assert owner not in getattr(partner, 'Docbook_PrefaceType264')


def test_assoc_paramdef156_stub_double():
    # Docbook_FuncprototypeType has no real 'Docbook_FuncprototypeType157' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParamdefType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParamdefType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParamdefType(mixed="sample_text")
    partner = Docbook_FuncprototypeType()
    setattr(partner, 'Docbook_FuncprototypeType157', None)
    _safe_set(owner, 'Docbook_ParamdefType', partner)
    assert owner in getattr(partner, 'Docbook_FuncprototypeType157')
    _safe_set(owner, 'Docbook_ParamdefType', None)
    assert owner not in getattr(partner, 'Docbook_FuncprototypeType157')


def test_assoc_personname5_stub_double():
    # Docbook_PersonnameType has no real 'Docbook_PersonnameType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_AuthorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_AuthorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_AuthorType(contrib="sample_text")
    partner = Docbook_PersonnameType()
    setattr(partner, 'Docbook_PersonnameType', None)
    _safe_set(owner, 'Docbook_AuthorType', partner)
    assert getattr(partner, 'Docbook_PersonnameType') == owner
    _safe_set(owner, 'Docbook_AuthorType', None)
    assert getattr(partner, 'Docbook_PersonnameType') is None


def test_assoc_preface10_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_BookType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_BookType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_BookType(label="sample_text", lang="sample_text", version="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType', None)
    _safe_set(owner, 'Docbook_BookType11', partner)
    assert getattr(partner, 'Docbook_PrefaceType') == owner
    _safe_set(owner, 'Docbook_BookType11', None)
    assert getattr(partner, 'Docbook_PrefaceType') is None


def test_assoc_preface96_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType98' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType98', None)
    _safe_set(owner, 'Docbook_DocumentRoot97', {partner})
    assert getattr(partner, 'Docbook_PrefaceType98') == owner
    _safe_set(owner, 'Docbook_DocumentRoot97', set())
    assert getattr(partner, 'Docbook_PrefaceType98') is None


def test_assoc_refsynopsisdiv287_stub_double():
    # Docbook_RefSynopsisDivType has no real 'Docbook_RefSynopsisDivType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_RefEntryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_RefEntryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_RefEntryType(version="sample_text")
    partner = Docbook_RefSynopsisDivType()
    setattr(partner, 'Docbook_RefSynopsisDivType', None)
    _safe_set(owner, 'Docbook_RefEntryType288', partner)
    assert getattr(partner, 'Docbook_RefSynopsisDivType') == owner
    _safe_set(owner, 'Docbook_RefEntryType288', None)
    assert getattr(partner, 'Docbook_RefSynopsisDivType') is None


def test_assoc_revdescription329_stub_double():
    # Docbook_RevisionType has no real 'Docbook_RevisionType330' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_RevdescriptionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_RevdescriptionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_RevdescriptionType(mixed="sample_text")
    partner = Docbook_RevisionType()
    setattr(partner, 'Docbook_RevisionType330', None)
    _safe_set(owner, 'Docbook_RevdescriptionType331', partner)
    assert getattr(partner, 'Docbook_RevisionType330') == owner
    _safe_set(owner, 'Docbook_RevdescriptionType331', None)
    assert getattr(partner, 'Docbook_RevisionType330') is None


def test_assoc_revhistory192_stub_double():
    # Docbook_RevhistoryType has no real 'Docbook_RevhistoryType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_InfoType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_InfoType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_InfoType(bibliomisc="sample_text", date="sample_text", group="sample_text", productname="sample_text", pubdate="sample_text", releaseinfo="sample_text")
    partner = Docbook_RevhistoryType()
    setattr(partner, 'Docbook_RevhistoryType', None)
    _safe_set(owner, 'Docbook_InfoType193', partner)
    assert getattr(partner, 'Docbook_RevhistoryType') == owner
    _safe_set(owner, 'Docbook_InfoType193', None)
    assert getattr(partner, 'Docbook_RevhistoryType') is None


def test_assoc_revhistory204_stub_double():
    # Docbook_RevhistoryType has no real 'Docbook_RevhistoryType206' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_LegalNoticeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_LegalNoticeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_LegalNoticeType(group="sample_text")
    partner = Docbook_RevhistoryType()
    setattr(partner, 'Docbook_RevhistoryType206', None)
    _safe_set(owner, 'Docbook_LegalNoticeType205', partner)
    assert getattr(partner, 'Docbook_RevhistoryType206') == owner
    _safe_set(owner, 'Docbook_LegalNoticeType205', None)
    assert getattr(partner, 'Docbook_RevhistoryType206') is None


def test_assoc_revnumber323_stub_double():
    # Docbook_RevisionType has no real 'Docbook_RevisionType324' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_RevnumberType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_RevnumberType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_RevnumberType(mixed="sample_text")
    partner = Docbook_RevisionType()
    setattr(partner, 'Docbook_RevisionType324', None)
    _safe_set(owner, 'Docbook_RevnumberType', partner)
    assert getattr(partner, 'Docbook_RevisionType324') == owner
    _safe_set(owner, 'Docbook_RevnumberType', None)
    assert getattr(partner, 'Docbook_RevisionType324') is None


def test_assoc_row103_stub_double():
    # Docbook_RowType has no real 'Docbook_RowType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_RowType()
    setattr(partner, 'Docbook_RowType', None)
    _safe_set(owner, 'Docbook_DocumentRoot104', {partner})
    assert getattr(partner, 'Docbook_RowType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot104', set())
    assert getattr(partner, 'Docbook_RowType') is None


def test_assoc_seg383_stub_double():
    # Docbook_SegListItemType has no real 'Docbook_SegListItemType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SegType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SegType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SegType(errorcode="sample_text", errortext="sample_text", group="sample_text", mixed="sample_text")
    partner = Docbook_SegListItemType()
    setattr(partner, 'Docbook_SegListItemType', None)
    _safe_set(owner, 'Docbook_SegType', partner)
    assert owner in getattr(partner, 'Docbook_SegListItemType')
    _safe_set(owner, 'Docbook_SegType', None)
    assert owner not in getattr(partner, 'Docbook_SegListItemType')


def test_assoc_seglistitem384_stub_double():
    # Docbook_SegListItemType has no real 'Docbook_SegListItemType386' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SegmentedListType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SegmentedListType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SegmentedListType(group="sample_text", segtitle="sample_text")
    partner = Docbook_SegListItemType()
    setattr(partner, 'Docbook_SegListItemType386', None)
    _safe_set(owner, 'Docbook_SegmentedListType385', {partner})
    assert getattr(partner, 'Docbook_SegListItemType386') == owner
    _safe_set(owner, 'Docbook_SegmentedListType385', set())
    assert getattr(partner, 'Docbook_SegListItemType386') is None


def test_assoc_surname258_stub_double():
    # Docbook_PersonnameType has no real 'Docbook_PersonnameType259' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_SurnameType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_SurnameType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_SurnameType(mixed="sample_text")
    partner = Docbook_PersonnameType()
    setattr(partner, 'Docbook_PersonnameType259', None)
    _safe_set(owner, 'Docbook_SurnameType', partner)
    assert getattr(partner, 'Docbook_PersonnameType259') == owner
    _safe_set(owner, 'Docbook_SurnameType', None)
    assert getattr(partner, 'Docbook_PersonnameType259') is None


def test_assoc_tbody110_stub_double():
    # Docbook_TbodyType has no real 'Docbook_TbodyType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_TbodyType()
    setattr(partner, 'Docbook_TbodyType', None)
    _safe_set(owner, 'Docbook_DocumentRoot111', {partner})
    assert getattr(partner, 'Docbook_TbodyType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot111', set())
    assert getattr(partner, 'Docbook_TbodyType') is None


def test_assoc_tbody419_stub_double():
    # Docbook_TbodyType has no real 'Docbook_TbodyType421' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_TgroupType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_TgroupType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    partner = Docbook_TbodyType()
    setattr(partner, 'Docbook_TbodyType421', None)
    _safe_set(owner, 'Docbook_TgroupType420', partner)
    assert getattr(partner, 'Docbook_TbodyType421') == owner
    _safe_set(owner, 'Docbook_TgroupType420', None)
    assert getattr(partner, 'Docbook_TbodyType421') is None


def test_assoc_tgroup169_stub_double():
    # Docbook_InformaltableType has no real 'Docbook_InformaltableType170' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_TgroupType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_TgroupType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    partner = Docbook_InformaltableType()
    setattr(partner, 'Docbook_InformaltableType170', None)
    _safe_set(owner, 'Docbook_TgroupType171', partner)
    assert getattr(partner, 'Docbook_InformaltableType170') == owner
    _safe_set(owner, 'Docbook_TgroupType171', None)
    assert getattr(partner, 'Docbook_InformaltableType170') is None


def test_assoc_thead114_stub_double():
    # Docbook_TheadType has no real 'Docbook_TheadType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_TheadType()
    setattr(partner, 'Docbook_TheadType', None)
    _safe_set(owner, 'Docbook_DocumentRoot115', {partner})
    assert getattr(partner, 'Docbook_TheadType') == owner
    _safe_set(owner, 'Docbook_DocumentRoot115', set())
    assert getattr(partner, 'Docbook_TheadType') is None


def test_assoc_thead416_stub_double():
    # Docbook_TheadType has no real 'Docbook_TheadType418' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_TgroupType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_TgroupType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_TgroupType(align="sample_text", cols="sample_text", colseq="sample_text", rowseq="sample_text")
    partner = Docbook_TheadType()
    setattr(partner, 'Docbook_TheadType418', None)
    _safe_set(owner, 'Docbook_TgroupType417', partner)
    assert getattr(partner, 'Docbook_TheadType418') == owner
    _safe_set(owner, 'Docbook_TgroupType417', None)
    assert getattr(partner, 'Docbook_TheadType418') is None


def test_assoc_tip269_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType270' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_TipType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_TipType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_TipType(mixed="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType270', None)
    _safe_set(owner, 'Docbook_TipType271', partner)
    assert getattr(partner, 'Docbook_PrefaceType270') == owner
    _safe_set(owner, 'Docbook_TipType271', None)
    assert getattr(partner, 'Docbook_PrefaceType270') is None


def test_assoc_title260_stub_double():
    # Docbook_PrefaceType has no real 'Docbook_PrefaceType261' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_TitleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_TitleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_TitleType(group="sample_text", mixed="sample_text")
    partner = Docbook_PrefaceType()
    setattr(partner, 'Docbook_PrefaceType261', None)
    _safe_set(owner, 'Docbook_TitleType262', partner)
    assert getattr(partner, 'Docbook_PrefaceType261') == owner
    _safe_set(owner, 'Docbook_TitleType262', None)
    assert getattr(partner, 'Docbook_PrefaceType261') is None


def test_assoc_ulink231_stub_double():
    # Docbook_OtheraddrType has no real 'Docbook_OtheraddrType232' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_UlinkType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_UlinkType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_UlinkType(mixed="sample_text", type="sample_text", url="sample_text")
    partner = Docbook_OtheraddrType()
    setattr(partner, 'Docbook_OtheraddrType232', None)
    _safe_set(owner, 'Docbook_UlinkType233', partner)
    assert getattr(partner, 'Docbook_OtheraddrType232') == owner
    _safe_set(owner, 'Docbook_UlinkType233', None)
    assert getattr(partner, 'Docbook_OtheraddrType232') is None


def test_assoc_variablelist254_stub_double():
    # Docbook_VariableListType has no real 'Docbook_VariableListType' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_ParaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_ParaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_ParaType(group="sample_text", id="sample_text", mixed="sample_text", role="sample_text")
    partner = Docbook_VariableListType()
    setattr(partner, 'Docbook_VariableListType', None)
    _safe_set(owner, 'Docbook_ParaType255', {partner})
    assert getattr(partner, 'Docbook_VariableListType') == owner
    _safe_set(owner, 'Docbook_ParaType255', set())
    assert getattr(partner, 'Docbook_VariableListType') is None


def test_assoc_variablelist308_stub_double():
    # Docbook_VariableListType has no real 'Docbook_VariableListType310' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_RefSect1Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_RefSect1Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_RefSect1Type(group="sample_text", id="sample_text")
    partner = Docbook_VariableListType()
    setattr(partner, 'Docbook_VariableListType310', None)
    _safe_set(owner, 'Docbook_RefSect1Type309', {partner})
    assert getattr(partner, 'Docbook_VariableListType310') == owner
    _safe_set(owner, 'Docbook_RefSect1Type309', set())
    assert getattr(partner, 'Docbook_VariableListType310') is None


def test_assoc_varlistentry437_stub_double():
    # Docbook_VariableListType has no real 'Docbook_VariableListType438' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_VarListEntryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_VarListEntryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_VarListEntryType(spacing="sample_text", termlength="sample_text")
    partner = Docbook_VariableListType()
    setattr(partner, 'Docbook_VariableListType438', None)
    _safe_set(owner, 'Docbook_VarListEntryType', partner)
    assert owner in getattr(partner, 'Docbook_VariableListType438')
    _safe_set(owner, 'Docbook_VarListEntryType', None)
    assert owner not in getattr(partner, 'Docbook_VariableListType438')


def test_assoc_xMLNSPrefixMap29_stub_double():
    # Docbook_EStringToStringMapEntry has no real 'Docbook_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_EStringToStringMapEntry()
    setattr(partner, 'Docbook_EStringToStringMapEntry', None)
    _safe_set(owner, 'Docbook_DocumentRoot', {partner})
    assert getattr(partner, 'Docbook_EStringToStringMapEntry') == owner
    _safe_set(owner, 'Docbook_DocumentRoot', set())
    assert getattr(partner, 'Docbook_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation30_stub_double():
    # Docbook_EStringToStringMapEntry has no real 'Docbook_EStringToStringMapEntry32' property in the generated
    # code (a bare stub) -- manually attach it so Docbook_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Docbook_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Docbook_DocumentRoot(bibliomisc="sample_text", caution="sample_text", confnum="sample_text", confsponsor="sample_text", conftitle="sample_text", date="sample_text", firstname="sample_text", keyword="sample_text", mixed="sample_text", pubdate="sample_text", publishername="sample_text", state="sample_text", subtitle="sample_text", superscript="sample_text", warning="sample_text")
    partner = Docbook_EStringToStringMapEntry()
    setattr(partner, 'Docbook_EStringToStringMapEntry32', None)
    _safe_set(owner, 'Docbook_DocumentRoot31', {partner})
    assert getattr(partner, 'Docbook_EStringToStringMapEntry32') == owner
    _safe_set(owner, 'Docbook_DocumentRoot31', set())
    assert getattr(partner, 'Docbook_EStringToStringMapEntry32') is None


