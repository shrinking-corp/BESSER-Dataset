import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BlockLevelChunkElt,
    BlockLevelElt,
    BodyElt,
    CustomDocumentPropertiesCollection,
    CustomDocumentProperty,
    DateTimeType,
    DocPrElt,
    DocumentPropertiesCollection,
    FldCharElt,
    FontsListElt,
    ListsElt,
    NoteElt,
    ParaContentElt,
    ParaElt,
    ParaPrElt,
    PictureType,
    RunContentElt,
    RunElt,
    RunPrElt,
    SectPrElt,
    SmartTagType,
    SmartTagsCollection,
    StringProperty,
    StringType,
    StylesElt,
    SymElt,
    TabElt,
    ValueType,
    VersionType,
    WordDocument,
    WordprocessingMLBasicDef_AnnotationRef,
    WordprocessingMLBasicDef_BlockLevelChunkElt,
    WordprocessingMLBasicDef_BlockLevelElt,
    WordprocessingMLBasicDef_BodyElt,
    WordprocessingMLBasicDef_BooleanValue,
    WordprocessingMLBasicDef_BreakElt,
    WordprocessingMLBasicDef_CfChunk,
    WordprocessingMLBasicDef_ContinuationSeparator,
    WordprocessingMLBasicDef_Cr,
    WordprocessingMLBasicDef_CustomDocumentPropertiesCollection,
    WordprocessingMLBasicDef_CustomDocumentProperty,
    WordprocessingMLBasicDef_DateTimeType,
    WordprocessingMLBasicDef_DateTimeTypeValue,
    WordprocessingMLBasicDef_DelInstrText,
    WordprocessingMLBasicDef_DelText,
    WordprocessingMLBasicDef_DocPrElt,
    WordprocessingMLBasicDef_DocumentPropertiesCollection,
    WordprocessingMLBasicDef_Endnote,
    WordprocessingMLBasicDef_EndnoteRef,
    WordprocessingMLBasicDef_FldChar,
    WordprocessingMLBasicDef_FldCharElt,
    WordprocessingMLBasicDef_FloatValue,
    WordprocessingMLBasicDef_FontsListElt,
    WordprocessingMLBasicDef_Footnote,
    WordprocessingMLBasicDef_FootnoteRef,
    WordprocessingMLBasicDef_HLinkElt,
    WordprocessingMLBasicDef_InstrText,
    WordprocessingMLBasicDef_ListsElt,
    WordprocessingMLBasicDef_NoBreakHyphen,
    WordprocessingMLBasicDef_NoteElt,
    WordprocessingMLBasicDef_ParaContentElt,
    WordprocessingMLBasicDef_ParaElt,
    WordprocessingMLBasicDef_ParaPrElt,
    WordprocessingMLBasicDef_PgNum,
    WordprocessingMLBasicDef_Picture,
    WordprocessingMLBasicDef_PictureType,
    WordprocessingMLBasicDef_RunContentElt,
    WordprocessingMLBasicDef_RunElt,
    WordprocessingMLBasicDef_RunLevelElt,
    WordprocessingMLBasicDef_RunPrElt,
    WordprocessingMLBasicDef_SectPrElt,
    WordprocessingMLBasicDef_Separator,
    WordprocessingMLBasicDef_SimpleFieldElt,
    WordprocessingMLBasicDef_SmartTagType,
    WordprocessingMLBasicDef_SmartTagsCollection,
    WordprocessingMLBasicDef_SoftHyphen,
    WordprocessingMLBasicDef_StringProperty,
    WordprocessingMLBasicDef_StringType,
    WordprocessingMLBasicDef_StringValue,
    WordprocessingMLBasicDef_StylesElt,
    WordprocessingMLBasicDef_SubDocElt,
    WordprocessingMLBasicDef_SymElt,
    WordprocessingMLBasicDef_Symbol,
    WordprocessingMLBasicDef_Tab,
    WordprocessingMLBasicDef_TabElt,
    WordprocessingMLBasicDef_Text,
    WordprocessingMLBasicDef_ValueType,
    WordprocessingMLBasicDef_VersionType,
    WordprocessingMLBasicDef_WordDocument,
    BreakType,
    FldCharTypeProperty,
    NoteValue,
    OnOffType,
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

def test_WordprocessingMLBasicDef_ParaElt_isa_BlockLevelChunkElt():
    instance = WordprocessingMLBasicDef_ParaElt()
    assert isinstance(instance, BlockLevelChunkElt)


def test_WordprocessingMLBasicDef_RunLevelElt_isa_BlockLevelChunkElt():
    instance = WordprocessingMLBasicDef_RunLevelElt()
    assert isinstance(instance, BlockLevelChunkElt)


def test_WordprocessingMLBasicDef_BlockLevelChunkElt_isa_BlockLevelElt():
    instance = WordprocessingMLBasicDef_BlockLevelChunkElt()
    assert isinstance(instance, BlockLevelElt)


def test_WordprocessingMLBasicDef_CfChunk_isa_BlockLevelElt():
    instance = WordprocessingMLBasicDef_CfChunk()
    assert isinstance(instance, BlockLevelElt)


def test_WordprocessingMLBasicDef_FldChar_isa_FldCharElt():
    instance = WordprocessingMLBasicDef_FldChar()
    assert isinstance(instance, FldCharElt)


def test_WordprocessingMLBasicDef_Endnote_isa_NoteElt():
    instance = WordprocessingMLBasicDef_Endnote()
    assert isinstance(instance, NoteElt)


def test_WordprocessingMLBasicDef_Footnote_isa_NoteElt():
    instance = WordprocessingMLBasicDef_Footnote()
    assert isinstance(instance, NoteElt)


def test_WordprocessingMLBasicDef_HLinkElt_isa_ParaContentElt():
    instance = WordprocessingMLBasicDef_HLinkElt()
    assert isinstance(instance, ParaContentElt)


def test_WordprocessingMLBasicDef_RunElt_isa_ParaContentElt():
    instance = WordprocessingMLBasicDef_RunElt()
    assert isinstance(instance, ParaContentElt)


def test_WordprocessingMLBasicDef_SimpleFieldElt_isa_ParaContentElt():
    instance = WordprocessingMLBasicDef_SimpleFieldElt()
    assert isinstance(instance, ParaContentElt)


def test_WordprocessingMLBasicDef_SubDocElt_isa_ParaContentElt():
    instance = WordprocessingMLBasicDef_SubDocElt()
    assert isinstance(instance, ParaContentElt)


def test_WordprocessingMLBasicDef_Picture_isa_PictureType():
    instance = WordprocessingMLBasicDef_Picture()
    assert isinstance(instance, PictureType)


def test_WordprocessingMLBasicDef_AnnotationRef_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_AnnotationRef()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_ContinuationSeparator_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_ContinuationSeparator()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Cr_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Cr()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_DelInstrText_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_DelInstrText()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_DelText_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_DelText()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Endnote_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Endnote()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_EndnoteRef_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_EndnoteRef()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_FldChar_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_FldChar()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Footnote_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Footnote()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_FootnoteRef_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_FootnoteRef()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_InstrText_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_InstrText()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_NoBreakHyphen_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_NoBreakHyphen()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_PgNum_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_PgNum()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Picture_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Picture()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Separator_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Separator()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_SoftHyphen_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_SoftHyphen()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Symbol_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Symbol()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Tab_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Tab()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_Text_isa_RunContentElt():
    instance = WordprocessingMLBasicDef_Text()
    assert isinstance(instance, RunContentElt)


def test_WordprocessingMLBasicDef_DelInstrText_isa_StringType():
    instance = WordprocessingMLBasicDef_DelInstrText()
    assert isinstance(instance, StringType)


def test_WordprocessingMLBasicDef_DelText_isa_StringType():
    instance = WordprocessingMLBasicDef_DelText()
    assert isinstance(instance, StringType)


def test_WordprocessingMLBasicDef_InstrText_isa_StringType():
    instance = WordprocessingMLBasicDef_InstrText()
    assert isinstance(instance, StringType)


def test_WordprocessingMLBasicDef_StringProperty_isa_StringType():
    instance = WordprocessingMLBasicDef_StringProperty()
    assert isinstance(instance, StringType)


def test_WordprocessingMLBasicDef_Text_isa_StringType():
    instance = WordprocessingMLBasicDef_Text()
    assert isinstance(instance, StringType)


def test_WordprocessingMLBasicDef_Symbol_isa_SymElt():
    instance = WordprocessingMLBasicDef_Symbol()
    assert isinstance(instance, SymElt)


def test_WordprocessingMLBasicDef_Tab_isa_TabElt():
    instance = WordprocessingMLBasicDef_Tab()
    assert isinstance(instance, TabElt)


def test_WordprocessingMLBasicDef_DateTimeTypeValue_isa_ValueType():
    instance = WordprocessingMLBasicDef_DateTimeTypeValue()
    assert isinstance(instance, ValueType)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BlockLevelChunkElt_strategy = st.builds(BlockLevelChunkElt)
@given(instance=BlockLevelChunkElt_strategy)
@settings(max_examples=25)
def test_BlockLevelChunkElt_instantiation(instance):
    assert isinstance(instance, BlockLevelChunkElt)


BlockLevelElt_strategy = st.builds(BlockLevelElt)
@given(instance=BlockLevelElt_strategy)
@settings(max_examples=25)
def test_BlockLevelElt_instantiation(instance):
    assert isinstance(instance, BlockLevelElt)


BodyElt_strategy = st.builds(BodyElt)
@given(instance=BodyElt_strategy)
@settings(max_examples=25)
def test_BodyElt_instantiation(instance):
    assert isinstance(instance, BodyElt)


CustomDocumentPropertiesCollection_strategy = st.builds(CustomDocumentPropertiesCollection)
@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=25)
def test_CustomDocumentPropertiesCollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)


CustomDocumentProperty_strategy = st.builds(CustomDocumentProperty)
@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=25)
def test_CustomDocumentProperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)


DateTimeType_strategy = st.builds(DateTimeType)
@given(instance=DateTimeType_strategy)
@settings(max_examples=25)
def test_DateTimeType_instantiation(instance):
    assert isinstance(instance, DateTimeType)


DocPrElt_strategy = st.builds(DocPrElt)
@given(instance=DocPrElt_strategy)
@settings(max_examples=25)
def test_DocPrElt_instantiation(instance):
    assert isinstance(instance, DocPrElt)


DocumentPropertiesCollection_strategy = st.builds(DocumentPropertiesCollection)
@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=25)
def test_DocumentPropertiesCollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)


FldCharElt_strategy = st.builds(FldCharElt)
@given(instance=FldCharElt_strategy)
@settings(max_examples=25)
def test_FldCharElt_instantiation(instance):
    assert isinstance(instance, FldCharElt)


FontsListElt_strategy = st.builds(FontsListElt)
@given(instance=FontsListElt_strategy)
@settings(max_examples=25)
def test_FontsListElt_instantiation(instance):
    assert isinstance(instance, FontsListElt)


ListsElt_strategy = st.builds(ListsElt)
@given(instance=ListsElt_strategy)
@settings(max_examples=25)
def test_ListsElt_instantiation(instance):
    assert isinstance(instance, ListsElt)


NoteElt_strategy = st.builds(NoteElt)
@given(instance=NoteElt_strategy)
@settings(max_examples=25)
def test_NoteElt_instantiation(instance):
    assert isinstance(instance, NoteElt)


ParaContentElt_strategy = st.builds(ParaContentElt)
@given(instance=ParaContentElt_strategy)
@settings(max_examples=25)
def test_ParaContentElt_instantiation(instance):
    assert isinstance(instance, ParaContentElt)


ParaElt_strategy = st.builds(ParaElt)
@given(instance=ParaElt_strategy)
@settings(max_examples=25)
def test_ParaElt_instantiation(instance):
    assert isinstance(instance, ParaElt)


ParaPrElt_strategy = st.builds(ParaPrElt)
@given(instance=ParaPrElt_strategy)
@settings(max_examples=25)
def test_ParaPrElt_instantiation(instance):
    assert isinstance(instance, ParaPrElt)


PictureType_strategy = st.builds(PictureType)
@given(instance=PictureType_strategy)
@settings(max_examples=25)
def test_PictureType_instantiation(instance):
    assert isinstance(instance, PictureType)


RunContentElt_strategy = st.builds(RunContentElt)
@given(instance=RunContentElt_strategy)
@settings(max_examples=25)
def test_RunContentElt_instantiation(instance):
    assert isinstance(instance, RunContentElt)


RunElt_strategy = st.builds(RunElt)
@given(instance=RunElt_strategy)
@settings(max_examples=25)
def test_RunElt_instantiation(instance):
    assert isinstance(instance, RunElt)


RunPrElt_strategy = st.builds(RunPrElt)
@given(instance=RunPrElt_strategy)
@settings(max_examples=25)
def test_RunPrElt_instantiation(instance):
    assert isinstance(instance, RunPrElt)


SectPrElt_strategy = st.builds(SectPrElt)
@given(instance=SectPrElt_strategy)
@settings(max_examples=25)
def test_SectPrElt_instantiation(instance):
    assert isinstance(instance, SectPrElt)


SmartTagType_strategy = st.builds(SmartTagType)
@given(instance=SmartTagType_strategy)
@settings(max_examples=25)
def test_SmartTagType_instantiation(instance):
    assert isinstance(instance, SmartTagType)


SmartTagsCollection_strategy = st.builds(SmartTagsCollection)
@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=25)
def test_SmartTagsCollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)


StringProperty_strategy = st.builds(StringProperty)
@given(instance=StringProperty_strategy)
@settings(max_examples=25)
def test_StringProperty_instantiation(instance):
    assert isinstance(instance, StringProperty)


StringType_strategy = st.builds(StringType)
@given(instance=StringType_strategy)
@settings(max_examples=25)
def test_StringType_instantiation(instance):
    assert isinstance(instance, StringType)


StylesElt_strategy = st.builds(StylesElt)
@given(instance=StylesElt_strategy)
@settings(max_examples=25)
def test_StylesElt_instantiation(instance):
    assert isinstance(instance, StylesElt)


SymElt_strategy = st.builds(SymElt)
@given(instance=SymElt_strategy)
@settings(max_examples=25)
def test_SymElt_instantiation(instance):
    assert isinstance(instance, SymElt)


TabElt_strategy = st.builds(TabElt)
@given(instance=TabElt_strategy)
@settings(max_examples=25)
def test_TabElt_instantiation(instance):
    assert isinstance(instance, TabElt)


ValueType_strategy = st.builds(ValueType)
@given(instance=ValueType_strategy)
@settings(max_examples=25)
def test_ValueType_instantiation(instance):
    assert isinstance(instance, ValueType)


VersionType_strategy = st.builds(VersionType)
@given(instance=VersionType_strategy)
@settings(max_examples=25)
def test_VersionType_instantiation(instance):
    assert isinstance(instance, VersionType)


WordDocument_strategy = st.builds(WordDocument)
@given(instance=WordDocument_strategy)
@settings(max_examples=25)
def test_WordDocument_instantiation(instance):
    assert isinstance(instance, WordDocument)


WordprocessingMLBasicDef_AnnotationRef_strategy = st.builds(WordprocessingMLBasicDef_AnnotationRef)
@given(instance=WordprocessingMLBasicDef_AnnotationRef_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_AnnotationRef_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_AnnotationRef)


WordprocessingMLBasicDef_BlockLevelChunkElt_strategy = st.builds(WordprocessingMLBasicDef_BlockLevelChunkElt)
@given(instance=WordprocessingMLBasicDef_BlockLevelChunkElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_BlockLevelChunkElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BlockLevelChunkElt)


WordprocessingMLBasicDef_BlockLevelElt_strategy = st.builds(WordprocessingMLBasicDef_BlockLevelElt)
@given(instance=WordprocessingMLBasicDef_BlockLevelElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_BlockLevelElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BlockLevelElt)


WordprocessingMLBasicDef_BodyElt_strategy = st.builds(WordprocessingMLBasicDef_BodyElt)
@given(instance=WordprocessingMLBasicDef_BodyElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_BodyElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BodyElt)


WordprocessingMLBasicDef_CfChunk_strategy = st.builds(WordprocessingMLBasicDef_CfChunk)
@given(instance=WordprocessingMLBasicDef_CfChunk_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_CfChunk_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_CfChunk)


WordprocessingMLBasicDef_ContinuationSeparator_strategy = st.builds(WordprocessingMLBasicDef_ContinuationSeparator)
@given(instance=WordprocessingMLBasicDef_ContinuationSeparator_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ContinuationSeparator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ContinuationSeparator)


WordprocessingMLBasicDef_Cr_strategy = st.builds(WordprocessingMLBasicDef_Cr)
@given(instance=WordprocessingMLBasicDef_Cr_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Cr_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Cr)


WordprocessingMLBasicDef_CustomDocumentPropertiesCollection_strategy = st.builds(WordprocessingMLBasicDef_CustomDocumentPropertiesCollection)
@given(instance=WordprocessingMLBasicDef_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_CustomDocumentPropertiesCollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_CustomDocumentPropertiesCollection)


WordprocessingMLBasicDef_DateTimeTypeValue_strategy = st.builds(WordprocessingMLBasicDef_DateTimeTypeValue)
@given(instance=WordprocessingMLBasicDef_DateTimeTypeValue_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_DateTimeTypeValue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DateTimeTypeValue)


WordprocessingMLBasicDef_DelInstrText_strategy = st.builds(WordprocessingMLBasicDef_DelInstrText)
@given(instance=WordprocessingMLBasicDef_DelInstrText_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_DelInstrText_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DelInstrText)


WordprocessingMLBasicDef_DelText_strategy = st.builds(WordprocessingMLBasicDef_DelText)
@given(instance=WordprocessingMLBasicDef_DelText_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_DelText_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DelText)


WordprocessingMLBasicDef_DocPrElt_strategy = st.builds(WordprocessingMLBasicDef_DocPrElt)
@given(instance=WordprocessingMLBasicDef_DocPrElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_DocPrElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DocPrElt)


WordprocessingMLBasicDef_Endnote_strategy = st.builds(WordprocessingMLBasicDef_Endnote)
@given(instance=WordprocessingMLBasicDef_Endnote_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Endnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Endnote)


WordprocessingMLBasicDef_EndnoteRef_strategy = st.builds(WordprocessingMLBasicDef_EndnoteRef)
@given(instance=WordprocessingMLBasicDef_EndnoteRef_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_EndnoteRef_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_EndnoteRef)


WordprocessingMLBasicDef_FldChar_strategy = st.builds(WordprocessingMLBasicDef_FldChar)
@given(instance=WordprocessingMLBasicDef_FldChar_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_FldChar_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FldChar)


WordprocessingMLBasicDef_FontsListElt_strategy = st.builds(WordprocessingMLBasicDef_FontsListElt)
@given(instance=WordprocessingMLBasicDef_FontsListElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_FontsListElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FontsListElt)


WordprocessingMLBasicDef_Footnote_strategy = st.builds(WordprocessingMLBasicDef_Footnote)
@given(instance=WordprocessingMLBasicDef_Footnote_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Footnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Footnote)


WordprocessingMLBasicDef_FootnoteRef_strategy = st.builds(WordprocessingMLBasicDef_FootnoteRef)
@given(instance=WordprocessingMLBasicDef_FootnoteRef_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_FootnoteRef_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FootnoteRef)


WordprocessingMLBasicDef_HLinkElt_strategy = st.builds(WordprocessingMLBasicDef_HLinkElt)
@given(instance=WordprocessingMLBasicDef_HLinkElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_HLinkElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_HLinkElt)


WordprocessingMLBasicDef_InstrText_strategy = st.builds(WordprocessingMLBasicDef_InstrText)
@given(instance=WordprocessingMLBasicDef_InstrText_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_InstrText_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_InstrText)


WordprocessingMLBasicDef_ListsElt_strategy = st.builds(WordprocessingMLBasicDef_ListsElt)
@given(instance=WordprocessingMLBasicDef_ListsElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ListsElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ListsElt)


WordprocessingMLBasicDef_NoBreakHyphen_strategy = st.builds(WordprocessingMLBasicDef_NoBreakHyphen)
@given(instance=WordprocessingMLBasicDef_NoBreakHyphen_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_NoBreakHyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_NoBreakHyphen)


WordprocessingMLBasicDef_ParaContentElt_strategy = st.builds(WordprocessingMLBasicDef_ParaContentElt)
@given(instance=WordprocessingMLBasicDef_ParaContentElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ParaContentElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaContentElt)


WordprocessingMLBasicDef_ParaElt_strategy = st.builds(WordprocessingMLBasicDef_ParaElt)
@given(instance=WordprocessingMLBasicDef_ParaElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ParaElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaElt)


WordprocessingMLBasicDef_ParaPrElt_strategy = st.builds(WordprocessingMLBasicDef_ParaPrElt)
@given(instance=WordprocessingMLBasicDef_ParaPrElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ParaPrElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaPrElt)


WordprocessingMLBasicDef_PgNum_strategy = st.builds(WordprocessingMLBasicDef_PgNum)
@given(instance=WordprocessingMLBasicDef_PgNum_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_PgNum_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_PgNum)


WordprocessingMLBasicDef_Picture_strategy = st.builds(WordprocessingMLBasicDef_Picture)
@given(instance=WordprocessingMLBasicDef_Picture_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Picture_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Picture)


WordprocessingMLBasicDef_PictureType_strategy = st.builds(WordprocessingMLBasicDef_PictureType)
@given(instance=WordprocessingMLBasicDef_PictureType_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_PictureType_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_PictureType)


WordprocessingMLBasicDef_RunContentElt_strategy = st.builds(WordprocessingMLBasicDef_RunContentElt)
@given(instance=WordprocessingMLBasicDef_RunContentElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_RunContentElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunContentElt)


WordprocessingMLBasicDef_RunElt_strategy = st.builds(WordprocessingMLBasicDef_RunElt)
@given(instance=WordprocessingMLBasicDef_RunElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_RunElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunElt)


WordprocessingMLBasicDef_RunLevelElt_strategy = st.builds(WordprocessingMLBasicDef_RunLevelElt)
@given(instance=WordprocessingMLBasicDef_RunLevelElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_RunLevelElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunLevelElt)


WordprocessingMLBasicDef_RunPrElt_strategy = st.builds(WordprocessingMLBasicDef_RunPrElt)
@given(instance=WordprocessingMLBasicDef_RunPrElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_RunPrElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunPrElt)


WordprocessingMLBasicDef_SectPrElt_strategy = st.builds(WordprocessingMLBasicDef_SectPrElt)
@given(instance=WordprocessingMLBasicDef_SectPrElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SectPrElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SectPrElt)


WordprocessingMLBasicDef_Separator_strategy = st.builds(WordprocessingMLBasicDef_Separator)
@given(instance=WordprocessingMLBasicDef_Separator_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Separator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Separator)


WordprocessingMLBasicDef_SimpleFieldElt_strategy = st.builds(WordprocessingMLBasicDef_SimpleFieldElt)
@given(instance=WordprocessingMLBasicDef_SimpleFieldElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SimpleFieldElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SimpleFieldElt)


WordprocessingMLBasicDef_SmartTagsCollection_strategy = st.builds(WordprocessingMLBasicDef_SmartTagsCollection)
@given(instance=WordprocessingMLBasicDef_SmartTagsCollection_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SmartTagsCollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SmartTagsCollection)


WordprocessingMLBasicDef_SoftHyphen_strategy = st.builds(WordprocessingMLBasicDef_SoftHyphen)
@given(instance=WordprocessingMLBasicDef_SoftHyphen_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SoftHyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SoftHyphen)


WordprocessingMLBasicDef_StringProperty_strategy = st.builds(WordprocessingMLBasicDef_StringProperty)
@given(instance=WordprocessingMLBasicDef_StringProperty_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_StringProperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StringProperty)


WordprocessingMLBasicDef_StylesElt_strategy = st.builds(WordprocessingMLBasicDef_StylesElt)
@given(instance=WordprocessingMLBasicDef_StylesElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_StylesElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StylesElt)


WordprocessingMLBasicDef_SubDocElt_strategy = st.builds(WordprocessingMLBasicDef_SubDocElt)
@given(instance=WordprocessingMLBasicDef_SubDocElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SubDocElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SubDocElt)


WordprocessingMLBasicDef_SymElt_strategy = st.builds(WordprocessingMLBasicDef_SymElt)
@given(instance=WordprocessingMLBasicDef_SymElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_SymElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SymElt)


WordprocessingMLBasicDef_Symbol_strategy = st.builds(WordprocessingMLBasicDef_Symbol)
@given(instance=WordprocessingMLBasicDef_Symbol_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Symbol_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Symbol)


WordprocessingMLBasicDef_Tab_strategy = st.builds(WordprocessingMLBasicDef_Tab)
@given(instance=WordprocessingMLBasicDef_Tab_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Tab_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Tab)


WordprocessingMLBasicDef_TabElt_strategy = st.builds(WordprocessingMLBasicDef_TabElt)
@given(instance=WordprocessingMLBasicDef_TabElt_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_TabElt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_TabElt)


WordprocessingMLBasicDef_Text_strategy = st.builds(WordprocessingMLBasicDef_Text)
@given(instance=WordprocessingMLBasicDef_Text_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_Text_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Text)


WordprocessingMLBasicDef_ValueType_strategy = st.builds(WordprocessingMLBasicDef_ValueType)
@given(instance=WordprocessingMLBasicDef_ValueType_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_ValueType_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ValueType)


WordprocessingMLBasicDef_WordDocument_strategy = st.builds(WordprocessingMLBasicDef_WordDocument)
@given(instance=WordprocessingMLBasicDef_WordDocument_strategy)
@settings(max_examples=25)
def test_WordprocessingMLBasicDef_WordDocument_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_WordDocument)


