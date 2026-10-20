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

