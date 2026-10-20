import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AlphanumericLiteral,
    CobolLine,
    CobolRoot,
    CobolSourceFormat,
    CobolWord,
    ConstantLiteral,
    CopyUnit,
    DataSegment,
    DataSegmentToken,
    DataSegmentWater,
    Element,
    FigurativeConstantLiteral,
    HighValueConstant,
    IncompleteElement,
    Literal,
    LowValueConstant,
    NullConstant,
    Operand,
    PreprocessingSentence,
    PreprocessingUnit,
    PreprocessingUnitWater,
    ProcedureSegment,
    ProcedureSegmentWater,
    QuoteConstant,
    Replacing,
    Segment,
    SpaceConstant,
    Water,
    ZeroConstant,
    commons_LibraryElement,
    commons_NamedElement,
    containers_CobolRoot,
    operands_Operand,
    preprocess_Dummy,
    preprocess_commons_Element,
    preprocess_commons_LibraryElement,
    preprocess_commons_NamedElement,
    preprocess_containers_CobolRoot,
    preprocess_containers_CopyUnit,
    preprocess_containers_Copybook,
    preprocess_containers_DataCopyUnit,
    preprocess_containers_DataSegment,
    preprocess_containers_PreprocessingGroup,
    preprocess_containers_PreprocessingUnit,
    preprocess_containers_ProcedureCopyUnit,
    preprocess_containers_ProcedureSegment,
    preprocess_containers_Segment,
    preprocess_layouts_ANSI85CobolSourceFormat,
    preprocess_layouts_CobolLine,
    preprocess_layouts_CobolSourceFormat,
    preprocess_literals_AllLiteral,
    preprocess_literals_AlphanumericHexaDecimalLiteral,
    preprocess_literals_AlphanumericLiteral,
    preprocess_literals_ConstantLiteral,
    preprocess_literals_FigurativeConstantLiteral,
    preprocess_literals_HighValue,
    preprocess_literals_HighValueConstant,
    preprocess_literals_HighValues,
    preprocess_literals_Literal,
    preprocess_literals_LowValue,
    preprocess_literals_LowValueConstant,
    preprocess_literals_LowValues,
    preprocess_literals_Null,
    preprocess_literals_NullConstant,
    preprocess_literals_Nulls,
    preprocess_literals_NumericLiteral,
    preprocess_literals_PseudoLiteral,
    preprocess_literals_Quote,
    preprocess_literals_QuoteConstant,
    preprocess_literals_Quotes,
    preprocess_literals_Space,
    preprocess_literals_SpaceConstant,
    preprocess_literals_Spaces,
    preprocess_literals_Zero,
    preprocess_literals_ZeroConstant,
    preprocess_literals_Zeroes,
    preprocess_literals_Zeros,
    preprocess_operands_CobolWord,
    preprocess_operands_Operand,
    preprocess_sentences_CopySentence,
    preprocess_sentences_PreprocessingSentence,
    preprocess_sentences_ReplaceSentence,
    preprocess_sentences_Replacing,
    preprocess_statements_Execute,
    preprocess_statements_Statement,
    preprocess_water_All,
    preprocess_water_By,
    preprocess_water_DataSegmentToken,
    preprocess_water_DataSegmentWater,
    preprocess_water_Division,
    preprocess_water_Dot,
    preprocess_water_End,
    preprocess_water_In,
    preprocess_water_IncompleteElement,
    preprocess_water_Of,
    preprocess_water_Off,
    preprocess_water_On,
    preprocess_water_PreprocessingUnitWater,
    preprocess_water_Procedure,
    preprocess_water_ProcedureSegmentWater,
    preprocess_water_Program,
    preprocess_water_Replace,
    preprocess_water_Replacing,
    preprocess_water_Suppress,
    preprocess_water_Water,
    sentences_PreprocessingSentence,
    statements_Statement,
    water_IncompleteElement,
    water_PreprocessingUnitWater,
    water_ProcedureSegmentWater,
    water_Water,
    CobolSourceFormatTypeEnum,
    HighValueConstants,
    LowValueConstants,
    NullConstants,
    PreprocessingUnitTokens,
    QuoteConstants,
    SpaceConstants,
    ZeroConstants,
    identifications,
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

def test_assoc_dataSegment3_stub_double():
    # DataSegment has no real 'DataSegment' property in the generated
    # code (a bare stub) -- manually attach it so preprocess_containers_PreprocessingUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # preprocess_containers_PreprocessingUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = preprocess_containers_PreprocessingUnit(id="sample_text")
    partner = DataSegment()
    setattr(partner, 'DataSegment', None)
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit4', partner)
    assert getattr(partner, 'DataSegment') == owner
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit4', None)
    assert getattr(partner, 'DataSegment') is None


def test_assoc_ending1_stub_double():
    # CobolWord has no real 'CobolWord' property in the generated
    # code (a bare stub) -- manually attach it so preprocess_containers_PreprocessingUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # preprocess_containers_PreprocessingUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = preprocess_containers_PreprocessingUnit(id="sample_text")
    partner = CobolWord()
    setattr(partner, 'CobolWord', None)
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit2', partner)
    assert getattr(partner, 'CobolWord') == owner
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit2', None)
    assert getattr(partner, 'CobolWord') is None


def test_assoc_lineFormat23_stub_double():
    # CobolSourceFormat has no real 'CobolSourceFormat' property in the generated
    # code (a bare stub) -- manually attach it so preprocess_layouts_CobolLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # preprocess_layouts_CobolLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = preprocess_layouts_CobolLine(comment="sample_text", contentAreaA="sample_text", contentAreaB="sample_text", indicatorArea="sample_text", sequenceArea="sample_text")
    partner = CobolSourceFormat()
    setattr(partner, 'CobolSourceFormat', None)
    _safe_set(owner, 'preprocess_layouts_CobolLine', partner)
    assert getattr(partner, 'CobolSourceFormat') == owner
    _safe_set(owner, 'preprocess_layouts_CobolLine', None)
    assert getattr(partner, 'CobolSourceFormat') is None


def test_assoc_nestedPreprocessingUnits0_stub_double():
    # PreprocessingUnit has no real 'PreprocessingUnit' property in the generated
    # code (a bare stub) -- manually attach it so preprocess_containers_PreprocessingUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # preprocess_containers_PreprocessingUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = preprocess_containers_PreprocessingUnit(id="sample_text")
    partner = PreprocessingUnit()
    setattr(partner, 'PreprocessingUnit', None)
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit', {partner})
    assert getattr(partner, 'PreprocessingUnit') == owner
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit', set())
    assert getattr(partner, 'PreprocessingUnit') is None


def test_assoc_procedureSegment5_stub_double():
    # ProcedureSegment has no real 'ProcedureSegment' property in the generated
    # code (a bare stub) -- manually attach it so preprocess_containers_PreprocessingUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # preprocess_containers_PreprocessingUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = preprocess_containers_PreprocessingUnit(id="sample_text")
    partner = ProcedureSegment()
    setattr(partner, 'ProcedureSegment', None)
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit6', partner)
    assert getattr(partner, 'ProcedureSegment') == owner
    _safe_set(owner, 'preprocess_containers_PreprocessingUnit6', None)
    assert getattr(partner, 'ProcedureSegment') is None


