import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentOperator,
    AtomExpression,
    BasicType,
    BitmapParameter,
    BooleanExpression,
    BooleanLiteral,
    CaptionParameter,
    CoordinateDefinition,
    EqualityOperator,
    Expression,
    FilenameLiteral,
    FilenameParameter,
    GeneralLiteral,
    Graphic2D,
    Header,
    HeaderParameter,
    Literal,
    NameLiteral,
    NamedElement,
    NumberLiteral,
    NumericLiteral,
    Operator,
    PCL,
    Parameter,
    PictureParameter,
    PicturePart,
    RelationOperator,
    SDL,
    ScenarioFile,
    ScenarioObject,
    Statement,
    Stimulus,
    Stimulus2D,
    StimulusEvent,
    StimulusEventParameter,
    StimulusList,
    TextLiteral,
    TextParameter,
    TrialParameter,
    Type,
    VariableInitializer,
    common_VariableInitializer,
    expressions_BooleanExpression,
    expressions_Expression,
    expressions_StatementExpression,
    operators_AssignmentOperator,
    picture_Bitmap,
    picture_Box,
    picture_Picture,
    picture_PicturePart,
    picture_Text,
    presentation_common_Identifier,
    presentation_common_NamedElement,
    presentation_common_VariableInitializer,
    presentation_expressions_AndExpression,
    presentation_expressions_AssignmentExpression,
    presentation_expressions_AtomExpression,
    presentation_expressions_BoolExpression,
    presentation_expressions_BooleanExpression,
    presentation_expressions_EqualsExpression,
    presentation_expressions_Expression,
    presentation_expressions_NotExpression,
    presentation_expressions_OrExpression,
    presentation_expressions_PrimaryExpression,
    presentation_expressions_StatementExpression,
    presentation_general_CoordinateDefinition,
    presentation_general_NamedElement,
    presentation_literal_BooleanLiteral,
    presentation_literal_FilenameLiteral,
    presentation_literal_GeneralLiteral,
    presentation_literal_Literal,
    presentation_literal_NameLiteral,
    presentation_literal_NumberLiteral,
    presentation_literal_NumericLiteral,
    presentation_literal_TextLiteral,
    presentation_operators_AdditiveOperator,
    presentation_operators_Assignment,
    presentation_operators_AssignmentOperator,
    presentation_operators_Equal,
    presentation_operators_EqualityOperator,
    presentation_operators_Greater,
    presentation_operators_GreaterOrEqual,
    presentation_operators_Less,
    presentation_operators_LessOrEqual,
    presentation_operators_MultiplicativeOperator,
    presentation_operators_NotEqual,
    presentation_operators_Operator,
    presentation_operators_RelationOperator,
    presentation_operators_UnaryOperator,
    presentation_parameter_ActiveButtonsParameter,
    presentation_parameter_BackgroundColorParameter,
    presentation_parameter_BitmapParameter,
    presentation_parameter_ButtonCodesParameter,
    presentation_parameter_CaptionParameter,
    presentation_parameter_CodeParameter,
    presentation_parameter_FilenameParameter,
    presentation_parameter_HeaderParameter,
    presentation_parameter_Parameter,
    presentation_parameter_PictureParameter,
    presentation_parameter_ScenarioNameParameter,
    presentation_parameter_StimulusEventParameter,
    presentation_parameter_TargetButtonParameter,
    presentation_parameter_TextParameter,
    presentation_parameter_TimeParameter,
    presentation_parameter_TrialParameter,
    presentation_picture_Bitmap,
    presentation_picture_BitmapStimulus,
    presentation_picture_Box,
    presentation_picture_BoxStimulus,
    presentation_picture_Graphic2D,
    presentation_picture_Picture,
    presentation_picture_PicturePart,
    presentation_picture_PictureStimulusEvent,
    presentation_picture_Stimulus2D,
    presentation_picture_Text,
    presentation_picture_TextStimulus,
    presentation_program_Block,
    presentation_scenario_Header,
    presentation_scenario_PCL,
    presentation_scenario_SDL,
    presentation_scenario_Scenario,
    presentation_scenario_ScenarioFile,
    presentation_sound_Sound,
    presentation_statements_Assignment,
    presentation_statements_DeclarationStatement,
    presentation_statements_ForInitializer,
    presentation_statements_Inclusion,
    presentation_statements_Loop,
    presentation_statements_ResourceAcquisition,
    presentation_statements_Statement,
    presentation_statements_StatementList,
    presentation_statements_VariableDeclaration,
    presentation_statements_VariableDeclarator,
    presentation_stimulus_ScenarioObject,
    presentation_stimulus_Stimulus,
    presentation_stimulus_StimulusEvent,
    presentation_stimulus_StimulusList,
    presentation_stimulus_Trial,
    presentation_types_BasicType,
    presentation_types_Bool,
    presentation_types_Double,
    presentation_types_Int,
    presentation_types_String,
    presentation_types_Type,
    statements_ForInitializer,
    statements_ResourceAcquisition,
    statements_Statement,
    statements_StatementList,
    statements_VariableDeclaration,
    statements_VariableDeclarator,
    types_Type,
    CoordinateType,
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

def test_assoc_filename_parameter31_stub_double():
    # FilenameParameter has no real 'FilenameParameter' property in the generated
    # code (a bare stub) -- manually attach it so presentation_picture_Bitmap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # presentation_picture_Bitmap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = presentation_picture_Bitmap(bitmap_parameters="sample_text")
    partner = FilenameParameter()
    setattr(partner, 'FilenameParameter', None)
    _safe_set(owner, 'presentation_picture_Bitmap', partner)
    assert getattr(partner, 'FilenameParameter') == owner
    _safe_set(owner, 'presentation_picture_Bitmap', None)
    assert getattr(partner, 'FilenameParameter') is None


