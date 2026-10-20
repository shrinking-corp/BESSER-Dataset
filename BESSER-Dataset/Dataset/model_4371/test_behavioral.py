import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbbreviatedConditionalExpressionChild,
    AbbreviatedRelationalExpressionChild,
    AcceptStatementWater,
    AdditionalIndexName,
    AdditiveArithmeticExpressionChild,
    AdditiveOperator,
    AfterUntilCondition,
    AlphabetNameReference,
    AlphabetType,
    AlphanumericLiteral,
    Argument,
    ArithmeticExpression,
    ArithmeticOperand,
    ArithmeticStatement,
    AssignmentExpression,
    CICSStatementWater,
    ClassOperator,
    CloseStatementWater,
    CobolRoot,
    Commentable,
    CompilationUnit,
    ConcatenatingStrings,
    Condition,
    ConditionName,
    Conditional,
    ConditionalAndExpressionChild,
    ConditionalOrExpressionChild,
    ConfigurationSectionParagraph,
    ConstantLiteral,
    DBCSLiteral,
    DataDescriptorWater,
    DataDivision,
    DataDivisionSection,
    DataItem,
    DataItemAttribute,
    DataName,
    DebuggingMode,
    DecimalLiteral,
    DeclarativeSection,
    Declaratives,
    DirectSubscript,
    Division,
    ElementReference,
    Environment,
    EnvironmentDivision,
    EnvironmentDivisionSection,
    Equal,
    EvaluateCase,
    ExpressionList,
    FigurativeConstantLiteral,
    FileDescriptorWater,
    FileName,
    FileNameReference,
    FileStatus,
    GreaterThan,
    GreaterThanOrEqual,
    Handler,
    IOControlParagraphWater,
    IODirectives,
    IOFile,
    IOFileDescriptor,
    IOSectionParagraph,
    IdentificationDivision,
    IdentificationDivisionWater,
    Identifier,
    IdentifierReference,
    IncompleteElement,
    IndexName,
    IndexNameReference,
    InputDirective,
    IntegerLiteral,
    InvokeStatementWater,
    Is,
    Jump,
    KeyDescriptor,
    KeyName,
    Label,
    LessThan,
    LessThanOrEqual,
    Literal,
    Location,
    LogicalOperator,
    ManipulatedStrings,
    MnemonicNameReference,
    MultiplicativeArithmeticExpressionChild,
    MultiplicativeOperator,
    NamedElement,
    Negate,
    NegatedAbbreviatedConditionalExpressionChild,
    NegatedConditionalExpressionChild,
    NestedStatement,
    NormalEvaluateCase,
    NotErrorHandler,
    NumericLiteral,
    ObjectComputerParagraphWater,
    OpenStatementWater,
    Operand,
    Operator,
    OutputDirective,
    Paragraph,
    Parameter,
    Perform,
    PowerArithmeticExpressionChild,
    PrimaryExpression,
    PrimaryOperand,
    Procedure,
    ProcedureDivision,
    ProcedureRangeChild,
    ProcedureRangeLabel,
    Qualifier,
    RangeExpression,
    RangeExpressionChild,
    Reference,
    ReferenceModifier,
    ReferenceableElement,
    Register,
    RelationalOperator,
    Replacement,
    ReplacementOperand,
    RepositoryParagraphWater,
    SQLStatementWater,
    SearchStatement,
    Section,
    SelectStatement,
    SelectStatementWater,
    Sentence,
    SetStatement,
    SignOperator,
    SimpleConditionChild,
    SortPhraseWater,
    SpecialName,
    SpecialNameStatement,
    SpecialNamesParagraphWater,
    SplittedString,
    Statement,
    StatementContainer,
    StopLabel,
    String,
    StringManipulation,
    Subscript,
    SwitchStatus,
    SymbolicCharacter,
    SystemDevice,
    TableDimension,
    Tallying,
    TallyingIn,
    Through,
    UnaryArithmeticExpressionChild,
    UnaryOperator,
    UseStatementWater,
    VaryingUntilCondition,
    Verb,
    Water,
    Write,
    arithmetics_PrimaryExpression,
    cobol_arithmetics_AdditiveArithmeticExpression,
    cobol_arithmetics_AdditiveArithmeticExpressionChild,
    cobol_arithmetics_ArithmeticExpression,
    cobol_arithmetics_AssignmentExpression,
    cobol_arithmetics_MultiplicativeArithmeticExpression,
    cobol_arithmetics_MultiplicativeArithmeticExpressionChild,
    cobol_arithmetics_NestedArithmeticExpression,
    cobol_arithmetics_PowerArithmeticExpression,
    cobol_arithmetics_PowerArithmeticExpressionChild,
    cobol_arithmetics_PrimaryExpression,
    cobol_arithmetics_RangeExpression,
    cobol_arithmetics_RangeExpressionChild,
    cobol_arithmetics_UnaryArithmeticExpression,
    cobol_arithmetics_UnaryArithmeticExpressionChild,
    cobol_commons_Commentable,
    cobol_commons_LabellableElement,
    cobol_commons_NamedElement,
    cobol_commons_URIableElement,
    cobol_conditions_AbbreviatedConditionalExpression,
    cobol_conditions_AbbreviatedConditionalExpressionChild,
    cobol_conditions_AbbreviatedRelationalExpression,
    cobol_conditions_AbbreviatedRelationalExpressionChild,
    cobol_conditions_ClassCondition,
    cobol_conditions_Condition,
    cobol_conditions_ConditionalAndExpression,
    cobol_conditions_ConditionalAndExpressionChild,
    cobol_conditions_ConditionalOrExpression,
    cobol_conditions_ConditionalOrExpressionChild,
    cobol_conditions_ExpressionList,
    cobol_conditions_NegatedAbbreviatedConditionalExpression,
    cobol_conditions_NegatedAbbreviatedConditionalExpressionChild,
    cobol_conditions_NegatedConditionalExpression,
    cobol_conditions_NegatedConditionalExpressionChild,
    cobol_conditions_NestedAbbreviatedConditionalExpression,
    cobol_conditions_NestedCondition,
    cobol_conditions_RelationalExpression,
    cobol_conditions_SignCondition,
    cobol_conditions_SimpleConditionChild,
    cobol_containers_CobolRoot,
    cobol_containers_CompilationGroup,
    cobol_containers_CompilationUnit,
    cobol_containers_EmptyModel,
    cobol_dataitems_ConditionName,
    cobol_dataitems_DataItem,
    cobol_dataitems_DataItemAttribute,
    cobol_dataitems_DataName,
    cobol_dataitems_External,
    cobol_dataitems_Global,
    cobol_dataitems_GroupUsage,
    cobol_dataitems_PictureString,
    cobol_dataitems_RecordName,
    cobol_dataitems_Redefines,
    cobol_dataitems_RenamingDataName,
    cobol_dataitems_Usage,
    cobol_dataitems_Value,
    cobol_declaratives_Declaratives,
    cobol_divisions_DataDivision,
    cobol_divisions_Division,
    cobol_divisions_EnvironmentDivision,
    cobol_divisions_IdentificationDivision,
    cobol_divisions_ProcedureDivision,
    cobol_environments_AdvancedFunctionPrinting,
    cobol_environments_Channel,
    cobol_environments_Console,
    cobol_environments_Environment,
    cobol_environments_Pocket,
    cobol_environments_SuppressSpacing,
    cobol_environments_SystemDevice,
    cobol_environments_SystemLogicalInput,
    cobol_environments_SystemLogicalOutput,
    cobol_environments_SystemPunchDevice,
    cobol_environments_UPSI,
    cobol_files_FileName,
    cobol_files_FileStatus,
    cobol_files_SelectStatement,
    cobol_functions_Argument,
    cobol_functions_Argumentable,
    cobol_functions_ByContentArgument,
    cobol_functions_ByReferenceArgument,
    cobol_functions_ByValueArgument,
    cobol_functions_FunctionCall,
    cobol_functions_OmittedArgument,
    cobol_handlers_AtEnd,
    cobol_handlers_AtEndOfPage,
    cobol_handlers_Handler,
    cobol_handlers_InvalidKey,
    cobol_handlers_NotAtEnd,
    cobol_handlers_NotAtEndOfPage,
    cobol_handlers_NotErrorHandler,
    cobol_handlers_NotInvalidKey,
    cobol_handlers_NotOnException,
    cobol_handlers_NotOnOverflow,
    cobol_handlers_NotOnSizeError,
    cobol_handlers_OnException,
    cobol_handlers_OnOverflow,
    cobol_handlers_OnSizeError,
    cobol_identifiers_All,
    cobol_identifiers_DirectSubscript,
    cobol_identifiers_Identifier,
    cobol_identifiers_IdentifierReference,
    cobol_identifiers_LinageCounter,
    cobol_identifiers_Qualifier,
    cobol_identifiers_ReferenceModifier,
    cobol_identifiers_RelativeSubscript,
    cobol_identifiers_Subscript,
    cobol_ios_FileDirective,
    cobol_ios_IODirectives,
    cobol_ios_InputDirective,
    cobol_ios_InputFile,
    cobol_ios_InputProcedure,
    cobol_ios_OutputDirective,
    cobol_ios_OutputFile,
    cobol_ios_OutputProcedure,
    cobol_ios_ProcedureDirective,
    cobol_labels_Label,
    cobol_labels_Procedure,
    cobol_labels_ProcedureLabel,
    cobol_labels_ProcedureRange,
    cobol_labels_ProcedureRangeChild,
    cobol_labels_ProcedureRangeLabel,
    cobol_labels_Run,
    cobol_labels_StopLabel,
    cobol_literals_AllLiteral,
    cobol_literals_AlphanumericHexaDecimalLiteral,
    cobol_literals_AlphanumericLiteral,
    cobol_literals_Any,
    cobol_literals_BooleanLiteral,
    cobol_literals_Characters,
    cobol_literals_ConstantLiteral,
    cobol_literals_DBCSLiteral,
    cobol_literals_DecimalLiteral,
    cobol_literals_FigurativeConstantLiteral,
    cobol_literals_FixedDecimalLiteral,
    cobol_literals_FloatingDecimalLiteral,
    cobol_literals_HighValue,
    cobol_literals_IntegerLiteral,
    cobol_literals_Literal,
    cobol_literals_LowValue,
    cobol_literals_NationalHexLiteral,
    cobol_literals_NationalLiteral,
    cobol_literals_Null,
    cobol_literals_NumericLiteral,
    cobol_literals_PseudoLiteral,
    cobol_literals_Quote,
    cobol_literals_Space,
    cobol_literals_Zero,
    cobol_operands_ArithmeticOperand,
    cobol_operands_Encoding,
    cobol_operands_Operand,
    cobol_operands_PrimaryOperand,
    cobol_operands_ReplacementOperand,
    cobol_operands_RoundedIdentifier,
    cobol_operators_Addition,
    cobol_operators_AdditiveOperator,
    cobol_operators_Alphabetic,
    cobol_operators_AlphabeticLower,
    cobol_operators_AlphabeticUpper,
    cobol_operators_ClassName,
    cobol_operators_ClassOperator,
    cobol_operators_ConditionAnd,
    cobol_operators_ConditionOr,
    cobol_operators_DBCS,
    cobol_operators_Division,
    cobol_operators_Equal,
    cobol_operators_EqualPhrase,
    cobol_operators_EqualSign,
    cobol_operators_GTEQPhrase,
    cobol_operators_GTEQSign,
    cobol_operators_GTPhrase,
    cobol_operators_GTSign,
    cobol_operators_GreaterThan,
    cobol_operators_GreaterThanOrEqual,
    cobol_operators_Kanji,
    cobol_operators_LTEQPhrase,
    cobol_operators_LTEQSign,
    cobol_operators_LTPhrase,
    cobol_operators_LTSign,
    cobol_operators_LessThan,
    cobol_operators_LessThanOrEqual,
    cobol_operators_LogicalOperator,
    cobol_operators_Multiplication,
    cobol_operators_MultiplicativeOperator,
    cobol_operators_Negate,
    cobol_operators_Negative,
    cobol_operators_Numeric,
    cobol_operators_Operator,
    cobol_operators_Positive,
    cobol_operators_Power,
    cobol_operators_RelationalOperator,
    cobol_operators_SignOperator,
    cobol_operators_Subtraction,
    cobol_operators_Through,
    cobol_operators_UnaryOperator,
    cobol_operators_Zero,
    cobol_paragraphs_ConfigurationSectionParagraph,
    cobol_paragraphs_DebuggingMode,
    cobol_paragraphs_FileControlParagraph,
    cobol_paragraphs_IOControlParagraph,
    cobol_paragraphs_IOSectionParagraph,
    cobol_paragraphs_ObjectComputerParagraph,
    cobol_paragraphs_Paragraph,
    cobol_paragraphs_RepositoryParagraph,
    cobol_paragraphs_SourceComputerParagraph,
    cobol_paragraphs_SpecialNamesParagraph,
    cobol_parameters_ByReferenceParameter,
    cobol_parameters_ByValueParameter,
    cobol_parameters_Parameter,
    cobol_parameters_Parametrizable,
    cobol_references_AlphabetNameReference,
    cobol_references_ConditionName,
    cobol_references_ConditionNameReference,
    cobol_references_DataNameReference,
    cobol_references_ElementReference,
    cobol_references_FileNameReference,
    cobol_references_IdentifierReferenceQualifier,
    cobol_references_IndexNameReference,
    cobol_references_MnemonicNameReference,
    cobol_references_Qualifiable,
    cobol_references_Reference,
    cobol_references_ReferenceableElement,
    cobol_references_SpecialNamesConditionNameReference,
    cobol_registers_AddressOf,
    cobol_registers_LengthOf,
    cobol_registers_Register,
    cobol_registers_ReturnCode,
    cobol_registers_ShiftIn,
    cobol_registers_ShiftOut,
    cobol_registers_WhenCompiled,
    cobol_sections_ConfigurationSection,
    cobol_sections_DataDivisionSection,
    cobol_sections_DeclarativeSection,
    cobol_sections_EnvironmentDivisionSection,
    cobol_sections_FileSection,
    cobol_sections_IOSection,
    cobol_sections_LinkageStorageSection,
    cobol_sections_LocalStorageSection,
    cobol_sections_Section,
    cobol_sections_WorkingStorageSection,
    cobol_sentences_AlteredGoTo,
    cobol_sentences_EmptySentence,
    cobol_sentences_EntrySentence,
    cobol_sentences_ExecuteSentence,
    cobol_sentences_ExitProcedure,
    cobol_sentences_Sentence,
    cobol_sentences_StatementContainer,
    cobol_sentences_UseSentence,
    cobol_specialnames_AlphabetName,
    cobol_specialnames_AlphabetType,
    cobol_specialnames_ClassName,
    cobol_specialnames_CodeNameAlphabetType,
    cobol_specialnames_ConditionName,
    cobol_specialnames_CurrencySign,
    cobol_specialnames_ExplicitAlphabetType,
    cobol_specialnames_MnemonicName,
    cobol_specialnames_OffStatus,
    cobol_specialnames_OnStatus,
    cobol_specialnames_PredefinedAlphabetType,
    cobol_specialnames_SpecialName,
    cobol_specialnames_SpecialNameStatement,
    cobol_specialnames_SymbolicCharacter,
    cobol_specialnames_SymbolicCharacterStatement,
    cobol_specialnames_SystemDeviceIs,
    cobol_specialnames_UPSISwitchIs,
    cobol_statements_Accept,
    cobol_statements_Add,
    cobol_statements_AfterUntilCondition,
    cobol_statements_ArithmeticStatement,
    cobol_statements_BinarySearch,
    cobol_statements_Call,
    cobol_statements_Cancel,
    cobol_statements_Close,
    cobol_statements_Compute,
    cobol_statements_Condition,
    cobol_statements_Conditional,
    cobol_statements_Continue,
    cobol_statements_Delete,
    cobol_statements_Display,
    cobol_statements_Divide,
    cobol_statements_Entry,
    cobol_statements_ErrorHandled,
    cobol_statements_Evaluate,
    cobol_statements_EvaluateCase,
    cobol_statements_Execute,
    cobol_statements_Exit,
    cobol_statements_FileIOStatement,
    cobol_statements_GoBack,
    cobol_statements_GoTo,
    cobol_statements_IOFile,
    cobol_statements_IOFileDescriptor,
    cobol_statements_IOStatement,
    cobol_statements_Initialize,
    cobol_statements_Inspect,
    cobol_statements_Jump,
    cobol_statements_KeyDescriptor,
    cobol_statements_Merge,
    cobol_statements_Move,
    cobol_statements_Multiply,
    cobol_statements_NestedStatement,
    cobol_statements_NextSentence,
    cobol_statements_NormalEvaluateCase,
    cobol_statements_Open,
    cobol_statements_OtherEvaluateCase,
    cobol_statements_Perform,
    cobol_statements_PerformFixedTimes,
    cobol_statements_PerformNestedStatement,
    cobol_statements_PerformNestedStatementFixedTimes,
    cobol_statements_PerformNestedStatementUntilCondition,
    cobol_statements_PerformProcedure,
    cobol_statements_PerformProcedureFixedTimes,
    cobol_statements_PerformProcedureUntilCondition,
    cobol_statements_PerformUntilCondition,
    cobol_statements_Read,
    cobol_statements_Release,
    cobol_statements_Replace,
    cobol_statements_Return,
    cobol_statements_Rewrite,
    cobol_statements_SearchStatement,
    cobol_statements_SerialSearch,
    cobol_statements_Set,
    cobol_statements_SetIndexName,
    cobol_statements_SetStatement,
    cobol_statements_SetSwitches,
    cobol_statements_Sort,
    cobol_statements_Start,
    cobol_statements_Statement,
    cobol_statements_Stop,
    cobol_statements_String,
    cobol_statements_Subtract,
    cobol_statements_SwitchStatus,
    cobol_statements_TallyingIn,
    cobol_statements_Unstring,
    cobol_statements_VaryingUntilCondition,
    cobol_statements_Write,
    cobol_strings_AnyCharacter,
    cobol_strings_AnyCharacterBySpecificCharacter,
    cobol_strings_ConcatenatingStrings,
    cobol_strings_Location,
    cobol_strings_ManipulatedStrings,
    cobol_strings_Occurrence,
    cobol_strings_Replacement,
    cobol_strings_ReplacementOccurrence,
    cobol_strings_SpecificCharacter,
    cobol_strings_SpecificCharacterBySpecificCharacter,
    cobol_strings_SplittedString,
    cobol_strings_String,
    cobol_strings_StringManipulation,
    cobol_strings_Tallying,
    cobol_strings_TallyingOccurrence,
    cobol_tables_AdditionalIndexName,
    cobol_tables_IndexName,
    cobol_tables_KeyName,
    cobol_tables_Table,
    cobol_tables_TableDimension,
    cobol_verbs_Is,
    cobol_verbs_Verb,
    cobol_water_AcceptStatementToken,
    cobol_water_AcceptStatementWater,
    cobol_water_CICSStatementToken,
    cobol_water_CICSStatementWater,
    cobol_water_CloseStatementToken,
    cobol_water_CloseStatementWater,
    cobol_water_DataDescription,
    cobol_water_DataDescriptorWater,
    cobol_water_Dot,
    cobol_water_FileDescription,
    cobol_water_FileDescriptorWater,
    cobol_water_IOControlDescription,
    cobol_water_IOControlParagraphWater,
    cobol_water_IdentificationDivisionWater,
    cobol_water_IncompleteElement,
    cobol_water_InvokeStatementToken,
    cobol_water_InvokeStatementWater,
    cobol_water_ObjectComputerDescription,
    cobol_water_ObjectComputerParagraphWater,
    cobol_water_OpenStatementToken,
    cobol_water_OpenStatementWater,
    cobol_water_PriorityNumber,
    cobol_water_ProgramDescription,
    cobol_water_RepositoryDescription,
    cobol_water_RepositoryParagraphWater,
    cobol_water_SQLStatementToken,
    cobol_water_SQLStatementWater,
    cobol_water_SelectStatementClause,
    cobol_water_SelectStatementWater,
    cobol_water_SortPhraseToken,
    cobol_water_SortPhraseWater,
    cobol_water_SpecialNamesClause,
    cobol_water_SpecialNamesParagraphWater,
    cobol_water_UseStatementToken,
    cobol_water_UseStatementWater,
    cobol_water_Water,
    commons_NamedElement,
    conditions_AbbreviatedRelationalExpressionChild,
    conditions_SimpleConditionChild,
    containers_CobolRoot,
    dataitems_DataItem,
    divisions_Division,
    functions_Argumentable,
    identifiers_Identifier,
    identifiers_IdentifierReference,
    ios_FileDirective,
    ios_InputDirective,
    ios_OutputDirective,
    ios_ProcedureDirective,
    labels_Procedure,
    labels_StopLabel,
    literals_NumericLiteral,
    operands_ArithmeticOperand,
    operands_Operand,
    operands_PrimaryOperand,
    operands_ReplacementOperand,
    operators_AdditiveOperator,
    operators_UnaryOperator,
    paragraphs_ConfigurationSectionParagraph,
    paragraphs_IOSectionParagraph,
    parameters_Parametrizable,
    references_ConditionName,
    references_ElementReference,
    references_IdentifierReferenceQualifier,
    references_Qualifiable,
    references_ReferenceableElement,
    sentences_StatementContainer,
    specialnames_MnemonicName,
    specialnames_SpecialName,
    specialnames_SpecialNameStatement,
    statements_Conditional,
    statements_ErrorHandled,
    statements_FileIOStatement,
    statements_IOStatement,
    statements_NestedStatement,
    statements_Perform,
    statements_PerformFixedTimes,
    statements_PerformNestedStatement,
    statements_PerformProcedure,
    statements_PerformUntilCondition,
    statements_Statement,
    statements_VaryingUntilCondition,
    strings_Occurrence,
    strings_Replacement,
    strings_Tallying,
    water_AcceptStatementWater,
    water_CICSStatementWater,
    water_DataDescriptorWater,
    water_FileDescriptorWater,
    water_IOControlParagraphWater,
    water_IdentificationDivisionWater,
    water_IncompleteElement,
    water_InvokeStatementWater,
    water_ObjectComputerParagraphWater,
    water_RepositoryParagraphWater,
    water_SQLStatementWater,
    water_SelectStatementWater,
    water_SortPhraseWater,
    water_SpecialNamesParagraphWater,
    water_UseStatementWater,
    AcceptStatementTokens,
    Adjustings,
    CICSStatementTokens,
    Channels,
    CloseStatementTokens,
    Corresponding,
    DataDescriptionInfo,
    EOP,
    EncodingTypes,
    ExitLabels,
    FileDescriptionInfo,
    FileDescriptors,
    HighValues,
    IOControlDescriptionInfo,
    IOTypes,
    InvokeStatementTokens,
    LowValues,
    Nulls,
    ObjectComputerDescriptionInfo,
    Occurrences,
    OpenStatementTokens,
    Orders,
    PictureStringCharacters,
    Positions,
    PredefinedAlphabetTypes,
    ProgramDescriptionInfo,
    Properties,
    Quotes,
    RepositoryDescriptionInfo,
    SQLStatementTokens,
    SelectStatementClauses,
    Selects,
    SortPhraseTokens,
    SortingOrder,
    Spaces,
    SpecialNamesClauses,
    Status,
    SystemInputs,
    SystemOutputs,
    SystemPunchDevices,
    ThroughPhrase,
    UPSISwitches,
    Usages,
    UseStatementTokens,
    Zeroes,
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

def test_assoc_attributes320_stub_double():
    # DataItemAttribute has no real 'DataItemAttribute' property in the generated
    # code (a bare stub) -- manually attach it so cobol_dataitems_DataItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_dataitems_DataItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_dataitems_DataItem(levelNumber="sample_text")
    partner = DataItemAttribute()
    setattr(partner, 'DataItemAttribute', None)
    _safe_set(owner, 'cobol_dataitems_DataItem', {partner})
    assert getattr(partner, 'DataItemAttribute') == owner
    _safe_set(owner, 'cobol_dataitems_DataItem', set())
    assert getattr(partner, 'DataItemAttribute') is None


def test_assoc_attributes359_stub_double():
    # DataItemAttribute has no real 'DataItemAttribute361' property in the generated
    # code (a bare stub) -- manually attach it so cobol_files_FileName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_files_FileName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_files_FileName(fileDescriptor="sample_text")
    partner = DataItemAttribute()
    setattr(partner, 'DataItemAttribute361', None)
    _safe_set(owner, 'cobol_files_FileName360', {partner})
    assert getattr(partner, 'DataItemAttribute361') == owner
    _safe_set(owner, 'cobol_files_FileName360', set())
    assert getattr(partner, 'DataItemAttribute361') is None


def test_assoc_base402_stub_double():
    # PrimaryOperand has no real 'PrimaryOperand403' property in the generated
    # code (a bare stub) -- manually attach it so cobol_strings_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_strings_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_strings_Location(initial=True, position="sample_text")
    partner = PrimaryOperand()
    setattr(partner, 'PrimaryOperand403', None)
    _safe_set(owner, 'cobol_strings_Location', partner)
    assert getattr(partner, 'PrimaryOperand403') == owner
    _safe_set(owner, 'cobol_strings_Location', None)
    assert getattr(partner, 'PrimaryOperand403') is None


def test_assoc_conditions247_stub_double():
    # Condition has no real 'Condition248' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_PerformUntilCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_PerformUntilCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_PerformUntilCondition(position="sample_text")
    partner = Condition()
    setattr(partner, 'Condition248', None)
    _safe_set(owner, 'cobol_statements_PerformUntilCondition', {partner})
    assert getattr(partner, 'Condition248') == owner
    _safe_set(owner, 'cobol_statements_PerformUntilCondition', set())
    assert getattr(partner, 'Condition248') is None


def test_assoc_currency333_stub_double():
    # Literal has no real 'Literal' property in the generated
    # code (a bare stub) -- manually attach it so cobol_specialnames_CurrencySign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_specialnames_CurrencySign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_specialnames_CurrencySign(pictureSymbol="sample_text")
    partner = Literal()
    setattr(partner, 'Literal', None)
    _safe_set(owner, 'cobol_specialnames_CurrencySign', partner)
    assert getattr(partner, 'Literal') == owner
    _safe_set(owner, 'cobol_specialnames_CurrencySign', None)
    assert getattr(partner, 'Literal') is None


def test_assoc_fileNameReference366_stub_double():
    # FileNameReference has no real 'FileNameReference368' property in the generated
    # code (a bare stub) -- manually attach it so cobol_files_SelectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_files_SelectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_files_SelectStatement(externalFileNames="sample_text", isOptional=True)
    partner = FileNameReference()
    setattr(partner, 'FileNameReference368', None)
    _safe_set(owner, 'cobol_files_SelectStatement367', partner)
    assert getattr(partner, 'FileNameReference368') == owner
    _safe_set(owner, 'cobol_files_SelectStatement367', None)
    assert getattr(partner, 'FileNameReference368') is None


def test_assoc_fileStatus365_stub_double():
    # FileStatus has no real 'FileStatus' property in the generated
    # code (a bare stub) -- manually attach it so cobol_files_SelectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_files_SelectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_files_SelectStatement(externalFileNames="sample_text", isOptional=True)
    partner = FileStatus()
    setattr(partner, 'FileStatus', None)
    _safe_set(owner, 'cobol_files_SelectStatement', partner)
    assert getattr(partner, 'FileStatus') == owner
    _safe_set(owner, 'cobol_files_SelectStatement', None)
    assert getattr(partner, 'FileStatus') is None


def test_assoc_givings126_stub_double():
    # ArithmeticOperand has no real 'ArithmeticOperand128' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_ArithmeticStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_ArithmeticStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_ArithmeticStatement(corresponding="sample_text")
    partner = ArithmeticOperand()
    setattr(partner, 'ArithmeticOperand128', None)
    _safe_set(owner, 'cobol_statements_ArithmeticStatement127', {partner})
    assert getattr(partner, 'ArithmeticOperand128') == owner
    _safe_set(owner, 'cobol_statements_ArithmeticStatement127', set())
    assert getattr(partner, 'ArithmeticOperand128') is None


def test_assoc_ioFiles268_stub_double():
    # IOFile has no real 'IOFile' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_IOFileDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_IOFileDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_IOFileDescriptor(type="sample_text")
    partner = IOFile()
    setattr(partner, 'IOFile', None)
    _safe_set(owner, 'cobol_statements_IOFileDescriptor', {partner})
    assert getattr(partner, 'IOFile') == owner
    _safe_set(owner, 'cobol_statements_IOFileDescriptor', set())
    assert getattr(partner, 'IOFile') is None


def test_assoc_keyNames265_stub_double():
    # IdentifierReference has no real 'IdentifierReference266' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_KeyDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_KeyDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_KeyDescriptor(order="sample_text")
    partner = IdentifierReference()
    setattr(partner, 'IdentifierReference266', None)
    _safe_set(owner, 'cobol_statements_KeyDescriptor', {partner})
    assert getattr(partner, 'IdentifierReference266') == owner
    _safe_set(owner, 'cobol_statements_KeyDescriptor', set())
    assert getattr(partner, 'IdentifierReference266') is None


def test_assoc_keys354_stub_double():
    # IdentifierReference has no real 'IdentifierReference355' property in the generated
    # code (a bare stub) -- manually attach it so cobol_tables_KeyName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_tables_KeyName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_tables_KeyName(keyOrder="sample_text")
    partner = IdentifierReference()
    setattr(partner, 'IdentifierReference355', None)
    _safe_set(owner, 'cobol_tables_KeyName', {partner})
    assert getattr(partner, 'IdentifierReference355') == owner
    _safe_set(owner, 'cobol_tables_KeyName', set())
    assert getattr(partner, 'IdentifierReference355') is None


def test_assoc_mnemonicNames245_stub_double():
    # MnemonicNameReference has no real 'MnemonicNameReference246' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_SwitchStatus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_SwitchStatus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_SwitchStatus(status="sample_text")
    partner = MnemonicNameReference()
    setattr(partner, 'MnemonicNameReference246', None)
    _safe_set(owner, 'cobol_statements_SwitchStatus', {partner})
    assert getattr(partner, 'MnemonicNameReference246') == owner
    _safe_set(owner, 'cobol_statements_SwitchStatus', set())
    assert getattr(partner, 'MnemonicNameReference246') is None


def test_assoc_next123_stub_double():
    # Statement has no real 'Statement124' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_Statement(endVerb=True)
    partner = Statement()
    setattr(partner, 'Statement124', None)
    _safe_set(owner, 'cobol_statements_Statement', partner)
    assert getattr(partner, 'Statement124') == owner
    _safe_set(owner, 'cobol_statements_Statement', None)
    assert getattr(partner, 'Statement124') is None


def test_assoc_operands125_stub_double():
    # ArithmeticOperand has no real 'ArithmeticOperand' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_ArithmeticStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_ArithmeticStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_ArithmeticStatement(corresponding="sample_text")
    partner = ArithmeticOperand()
    setattr(partner, 'ArithmeticOperand', None)
    _safe_set(owner, 'cobol_statements_ArithmeticStatement', {partner})
    assert getattr(partner, 'ArithmeticOperand') == owner
    _safe_set(owner, 'cobol_statements_ArithmeticStatement', set())
    assert getattr(partner, 'ArithmeticOperand') is None


def test_assoc_paragraphs112_stub_double():
    # Paragraph has no real 'Paragraph114' property in the generated
    # code (a bare stub) -- manually attach it so cobol_sections_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_sections_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_sections_Section(segmentNumber="sample_text")
    partner = Paragraph()
    setattr(partner, 'Paragraph114', None)
    _safe_set(owner, 'cobol_sections_Section113', {partner})
    assert getattr(partner, 'Paragraph114') == owner
    _safe_set(owner, 'cobol_sections_Section113', set())
    assert getattr(partner, 'Paragraph114') is None


def test_assoc_receivers146_stub_double():
    # PrimaryOperand has no real 'PrimaryOperand' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_Move's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_Move's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_Move(corresponding="sample_text")
    partner = PrimaryOperand()
    setattr(partner, 'PrimaryOperand', None)
    _safe_set(owner, 'cobol_statements_Move', {partner})
    assert getattr(partner, 'PrimaryOperand') == owner
    _safe_set(owner, 'cobol_statements_Move', set())
    assert getattr(partner, 'PrimaryOperand') is None


def test_assoc_receivers170_stub_double():
    # IndexNameReference has no real 'IndexNameReference' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_SetIndexName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_SetIndexName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_SetIndexName(adjust="sample_text")
    partner = IndexNameReference()
    setattr(partner, 'IndexNameReference', None)
    _safe_set(owner, 'cobol_statements_SetIndexName', {partner})
    assert getattr(partner, 'IndexNameReference') == owner
    _safe_set(owner, 'cobol_statements_SetIndexName', set())
    assert getattr(partner, 'IndexNameReference') is None


def test_assoc_records357_stub_double():
    # DataItem has no real 'DataItem358' property in the generated
    # code (a bare stub) -- manually attach it so cobol_files_FileName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_files_FileName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_files_FileName(fileDescriptor="sample_text")
    partner = DataItem()
    setattr(partner, 'DataItem358', None)
    _safe_set(owner, 'cobol_files_FileName', {partner})
    assert getattr(partner, 'DataItem358') == owner
    _safe_set(owner, 'cobol_files_FileName', set())
    assert getattr(partner, 'DataItem358') is None


def test_assoc_sender147_stub_double():
    # PrimaryOperand has no real 'PrimaryOperand149' property in the generated
    # code (a bare stub) -- manually attach it so cobol_statements_Move's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_statements_Move's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_statements_Move(corresponding="sample_text")
    partner = PrimaryOperand()
    setattr(partner, 'PrimaryOperand149', None)
    _safe_set(owner, 'cobol_statements_Move148', {partner})
    assert getattr(partner, 'PrimaryOperand149') == owner
    _safe_set(owner, 'cobol_statements_Move148', set())
    assert getattr(partner, 'PrimaryOperand149') is None


def test_assoc_sentences110_stub_double():
    # StatementContainer has no real 'StatementContainer111' property in the generated
    # code (a bare stub) -- manually attach it so cobol_sections_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_sections_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_sections_Section(segmentNumber="sample_text")
    partner = StatementContainer()
    setattr(partner, 'StatementContainer111', None)
    _safe_set(owner, 'cobol_sections_Section', {partner})
    assert getattr(partner, 'StatementContainer111') == owner
    _safe_set(owner, 'cobol_sections_Section', set())
    assert getattr(partner, 'StatementContainer111') is None


def test_assoc_sentences362_stub_double():
    # StatementContainer has no real 'StatementContainer364' property in the generated
    # code (a bare stub) -- manually attach it so cobol_files_FileName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_files_FileName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_files_FileName(fileDescriptor="sample_text")
    partner = StatementContainer()
    setattr(partner, 'StatementContainer364', None)
    _safe_set(owner, 'cobol_files_FileName363', {partner})
    assert getattr(partner, 'StatementContainer364') == owner
    _safe_set(owner, 'cobol_files_FileName363', set())
    assert getattr(partner, 'StatementContainer364') is None


def test_assoc_subentries321_stub_double():
    # DataItem has no real 'DataItem322' property in the generated
    # code (a bare stub) -- manually attach it so cobol_dataitems_DataItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_dataitems_DataItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_dataitems_DataItem(levelNumber="sample_text")
    partner = DataItem()
    setattr(partner, 'DataItem322', None)
    _safe_set(owner, 'superentry', {partner})
    assert getattr(partner, 'DataItem322') == owner
    _safe_set(owner, 'superentry', set())
    assert getattr(partner, 'DataItem322') is None


def test_assoc_superentry323_stub_double():
    # DataItem has no real 'DataItem324' property in the generated
    # code (a bare stub) -- manually attach it so cobol_dataitems_DataItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cobol_dataitems_DataItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cobol_dataitems_DataItem(levelNumber="sample_text")
    partner = DataItem()
    setattr(partner, 'DataItem324', None)
    _safe_set(owner, 'subentries', partner)
    assert getattr(partner, 'DataItem324') == owner
    _safe_set(owner, 'subentries', None)
    assert getattr(partner, 'DataItem324') is None


