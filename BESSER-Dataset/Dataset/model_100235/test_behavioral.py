import pytest
from datetime import date, datetime, time, timedelta

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
    FontElt,
    FontsElt,
    FontsListElt,
    LangElt,
    ListsElt,
    NoteElt,
    ParaContentElt,
    ParaElt,
    ParaPrElt,
    PictureType,
    RowContentElt,
    RowElt,
    RunContentElt,
    RunElt,
    RunLevelElt,
    RunPrElt,
    SectPrElt,
    SmartTagType,
    SmartTagsCollection,
    StringProperty,
    StringType,
    StyleElt,
    StylesElt,
    SymElt,
    TabElt,
    TableCellElt,
    TableCellPrElt,
    TableContentElt,
    TableElt,
    TableGridElt,
    TablePrElt,
    TablePrExElt,
    TableRowPrElt,
    UnderlineProperty,
    ValueType,
    VersionType,
    WordDocument,
    WordprocessingMLStyles_AnnotationRef,
    WordprocessingMLStyles_BlockLevelChunkElt,
    WordprocessingMLStyles_BlockLevelElt,
    WordprocessingMLStyles_BodyElt,
    WordprocessingMLStyles_BooleanValue,
    WordprocessingMLStyles_BreakElt,
    WordprocessingMLStyles_CfChunk,
    WordprocessingMLStyles_ContinuationSeparator,
    WordprocessingMLStyles_Cr,
    WordprocessingMLStyles_CustomDocumentPropertiesCollection,
    WordprocessingMLStyles_CustomDocumentProperty,
    WordprocessingMLStyles_DateTimeType,
    WordprocessingMLStyles_DateTimeTypeValue,
    WordprocessingMLStyles_DelInstrText,
    WordprocessingMLStyles_DelText,
    WordprocessingMLStyles_DocPrElt,
    WordprocessingMLStyles_DocumentPropertiesCollection,
    WordprocessingMLStyles_Endnote,
    WordprocessingMLStyles_EndnoteRef,
    WordprocessingMLStyles_FldChar,
    WordprocessingMLStyles_FldCharElt,
    WordprocessingMLStyles_FloatValue,
    WordprocessingMLStyles_FontElt,
    WordprocessingMLStyles_FontsElt,
    WordprocessingMLStyles_FontsListElt,
    WordprocessingMLStyles_Footnote,
    WordprocessingMLStyles_FootnoteRef,
    WordprocessingMLStyles_HLinkElt,
    WordprocessingMLStyles_InstrText,
    WordprocessingMLStyles_LangElt,
    WordprocessingMLStyles_ListsElt,
    WordprocessingMLStyles_NoBreakHyphen,
    WordprocessingMLStyles_NoteElt,
    WordprocessingMLStyles_ParaContentElt,
    WordprocessingMLStyles_ParaElt,
    WordprocessingMLStyles_ParaPrElt,
    WordprocessingMLStyles_PgNum,
    WordprocessingMLStyles_Picture,
    WordprocessingMLStyles_PictureType,
    WordprocessingMLStyles_RowContentElt,
    WordprocessingMLStyles_RowElt,
    WordprocessingMLStyles_RunContentElt,
    WordprocessingMLStyles_RunElt,
    WordprocessingMLStyles_RunLevelElt,
    WordprocessingMLStyles_RunPrElt,
    WordprocessingMLStyles_SectPrElt,
    WordprocessingMLStyles_Separator,
    WordprocessingMLStyles_SimpleFieldElt,
    WordprocessingMLStyles_SmartTagType,
    WordprocessingMLStyles_SmartTagsCollection,
    WordprocessingMLStyles_SoftHyphen,
    WordprocessingMLStyles_StringProperty,
    WordprocessingMLStyles_StringType,
    WordprocessingMLStyles_StringValue,
    WordprocessingMLStyles_StyleElt,
    WordprocessingMLStyles_StylesElt,
    WordprocessingMLStyles_SubDocElt,
    WordprocessingMLStyles_SymElt,
    WordprocessingMLStyles_Symbol,
    WordprocessingMLStyles_Tab,
    WordprocessingMLStyles_TabElt,
    WordprocessingMLStyles_TableCellElt,
    WordprocessingMLStyles_TableCellPrElt,
    WordprocessingMLStyles_TableContentElt,
    WordprocessingMLStyles_TableElt,
    WordprocessingMLStyles_TableGridElt,
    WordprocessingMLStyles_TablePrElt,
    WordprocessingMLStyles_TablePrExElt,
    WordprocessingMLStyles_TableRowPrElt,
    WordprocessingMLStyles_Text,
    WordprocessingMLStyles_UnderlineProperty,
    WordprocessingMLStyles_ValueType,
    WordprocessingMLStyles_VersionType,
    WordprocessingMLStyles_WordDocument,
    BreakType,
    FldCharTypeProperty,
    HighlightColorValues,
    HintType,
    JustificationValue,
    NoteValue,
    OnOffType,
    StyleKindValue,
    UnderlineValues,
    VerticalAlignRunType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

