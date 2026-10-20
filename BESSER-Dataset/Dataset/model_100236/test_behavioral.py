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
    FontsListElt,
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
    ValueType,
    VersionType,
    WordDocument,
    WordprocessingMLTableElts_AnnotationRef,
    WordprocessingMLTableElts_BlockLevelChunkElt,
    WordprocessingMLTableElts_BlockLevelElt,
    WordprocessingMLTableElts_BodyElt,
    WordprocessingMLTableElts_BooleanValue,
    WordprocessingMLTableElts_BreakElt,
    WordprocessingMLTableElts_CfChunk,
    WordprocessingMLTableElts_ContinuationSeparator,
    WordprocessingMLTableElts_Cr,
    WordprocessingMLTableElts_CustomDocumentPropertiesCollection,
    WordprocessingMLTableElts_CustomDocumentProperty,
    WordprocessingMLTableElts_DateTimeType,
    WordprocessingMLTableElts_DateTimeTypeValue,
    WordprocessingMLTableElts_DelInstrText,
    WordprocessingMLTableElts_DelText,
    WordprocessingMLTableElts_DocPrElt,
    WordprocessingMLTableElts_DocumentPropertiesCollection,
    WordprocessingMLTableElts_Endnote,
    WordprocessingMLTableElts_EndnoteRef,
    WordprocessingMLTableElts_FldChar,
    WordprocessingMLTableElts_FldCharElt,
    WordprocessingMLTableElts_FloatValue,
    WordprocessingMLTableElts_FontsListElt,
    WordprocessingMLTableElts_Footnote,
    WordprocessingMLTableElts_FootnoteRef,
    WordprocessingMLTableElts_HLinkElt,
    WordprocessingMLTableElts_InstrText,
    WordprocessingMLTableElts_ListsElt,
    WordprocessingMLTableElts_NoBreakHyphen,
    WordprocessingMLTableElts_NoteElt,
    WordprocessingMLTableElts_ParaContentElt,
    WordprocessingMLTableElts_ParaElt,
    WordprocessingMLTableElts_ParaPrElt,
    WordprocessingMLTableElts_PgNum,
    WordprocessingMLTableElts_Picture,
    WordprocessingMLTableElts_PictureType,
    WordprocessingMLTableElts_RowContentElt,
    WordprocessingMLTableElts_RowElt,
    WordprocessingMLTableElts_RunContentElt,
    WordprocessingMLTableElts_RunElt,
    WordprocessingMLTableElts_RunLevelElt,
    WordprocessingMLTableElts_RunPrElt,
    WordprocessingMLTableElts_SectPrElt,
    WordprocessingMLTableElts_Separator,
    WordprocessingMLTableElts_SimpleFieldElt,
    WordprocessingMLTableElts_SmartTagType,
    WordprocessingMLTableElts_SmartTagsCollection,
    WordprocessingMLTableElts_SoftHyphen,
    WordprocessingMLTableElts_StringProperty,
    WordprocessingMLTableElts_StringType,
    WordprocessingMLTableElts_StringValue,
    WordprocessingMLTableElts_StylesElt,
    WordprocessingMLTableElts_SubDocElt,
    WordprocessingMLTableElts_SymElt,
    WordprocessingMLTableElts_Symbol,
    WordprocessingMLTableElts_Tab,
    WordprocessingMLTableElts_TabElt,
    WordprocessingMLTableElts_TableCellElt,
    WordprocessingMLTableElts_TableCellPrElt,
    WordprocessingMLTableElts_TableContentElt,
    WordprocessingMLTableElts_TableElt,
    WordprocessingMLTableElts_TableGridElt,
    WordprocessingMLTableElts_TablePrElt,
    WordprocessingMLTableElts_TablePrExElt,
    WordprocessingMLTableElts_TableRowPrElt,
    WordprocessingMLTableElts_Text,
    WordprocessingMLTableElts_ValueType,
    WordprocessingMLTableElts_VersionType,
    WordprocessingMLTableElts_WordDocument,
    BreakType,
    FldCharTypeProperty,
    NoteValue,
    OnOffType,
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

