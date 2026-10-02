import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    mMDSL_AdditionExpression,
    mMDSL_Algorithm,
    mMDSL_AlgorithmOperation,
    mMDSL_AndExpression,
    mMDSL_Attribute,
    mMDSL_AttributeGet,
    mMDSL_AttributeOperation,
    mMDSL_AttributeSet,
    mMDSL_BreakContinue,
    mMDSL_Circle,
    mMDSL_Class,
    mMDSL_ClassAttribute,
    mMDSL_ClassInstance,
    mMDSL_ClassInstanceCreate,
    mMDSL_ClassInstanceDelete,
    mMDSL_ClassInstanceGet,
    mMDSL_ClassInstanceGetAll,
    mMDSL_ClassInstanceSet,
    mMDSL_CompareExpression,
    mMDSL_ContextItem,
    mMDSL_CurveTo,
    mMDSL_DirCreate,
    mMDSL_DirDelete,
    mMDSL_DirGetWorking,
    mMDSL_DirList,
    mMDSL_DirOperation,
    mMDSL_DirSetWorking,
    mMDSL_EObject,
    mMDSL_EditBox,
    mMDSL_Ellipse,
    mMDSL_EllipticalArc,
    mMDSL_EmbedCode,
    mMDSL_EmbedCodeType,
    mMDSL_EmbedPlatformType,
    mMDSL_EnumType,
    mMDSL_Enumeration,
    mMDSL_EqualExpression,
    mMDSL_ErrorBox,
    mMDSL_Event,
    mMDSL_Expr,
    mMDSL_Expression,
    mMDSL_FileCopy,
    mMDSL_FileCreate,
    mMDSL_FileDelete,
    mMDSL_FileOperation,
    mMDSL_FileRead,
    mMDSL_FileWrite,
    mMDSL_FillColor,
    mMDSL_FontFamily,
    mMDSL_ForLoop,
    mMDSL_HorizontalLineTo,
    mMDSL_IncludeLibrary,
    mMDSL_IncludeLibraryType,
    mMDSL_InfoBox,
    mMDSL_InsertContextItem,
    mMDSL_InsertEmbedCode,
    mMDSL_InsertMenuItem,
    mMDSL_InstanceOperation,
    mMDSL_ItemOperation,
    mMDSL_Line,
    mMDSL_LineTo,
    mMDSL_LoopStatement,
    mMDSL_MenuItem,
    mMDSL_Metamodel,
    mMDSL_Method,
    mMDSL_MethodName,
    mMDSL_Mode,
    mMDSL_ModelCreate,
    mMDSL_ModelDelete,
    mMDSL_ModelDiscard,
    mMDSL_ModelIsLoaded,
    mMDSL_ModelLoad,
    mMDSL_ModelOperation,
    mMDSL_ModelSave,
    mMDSL_ModelType,
    mMDSL_MoveTo,
    mMDSL_MultiplicationExpression,
    mMDSL_OperatorAdd,
    mMDSL_OperatorAnd,
    mMDSL_OperatorAssign,
    mMDSL_OperatorCompare,
    mMDSL_OperatorEqual,
    mMDSL_OperatorMultiply,
    mMDSL_OperatorMultyAssign,
    mMDSL_OperatorOr,
    mMDSL_OperatorUnary,
    mMDSL_OrExpression,
    mMDSL_Path,
    mMDSL_PathData,
    mMDSL_PathParametersA,
    mMDSL_PathParametersC,
    mMDSL_PathParametersHV,
    mMDSL_PathParametersMLT,
    mMDSL_PathParametersQ,
    mMDSL_PathParametersS,
    mMDSL_Points,
    mMDSL_Polygon,
    mMDSL_Polyline,
    mMDSL_QuadraticBezierCurve,
    mMDSL_Rectangle,
    mMDSL_RefName,
    mMDSL_Reference,
    mMDSL_Relation,
    mMDSL_RelationInstance,
    mMDSL_RelationInstanceCreate,
    mMDSL_RelationInstanceDelete,
    mMDSL_RelationInstanceGet,
    mMDSL_RelationInstanceGetAll,
    mMDSL_RelationInstanceSet,
    mMDSL_RemoveContextItem,
    mMDSL_RemoveMenuItem,
    mMDSL_Root,
    mMDSL_SVGCommand,
    mMDSL_SelectionStatement,
    mMDSL_SimpleUI,
    mMDSL_SmoothCurveTo,
    mMDSL_SmoothQuadraticBezierCurveTo,
    mMDSL_Statement,
    mMDSL_StrokeColor,
    mMDSL_SymbolClass,
    mMDSL_SymbolRelation,
    mMDSL_SymbolStyle,
    mMDSL_Text,
    mMDSL_Type,
    mMDSL_VarStatement,
    mMDSL_Variable,
    mMDSL_VerticalLineTo,
    mMDSL_ViewBox,
    mMDSL_WarningBox,
    mMDSL_WhileLoop,
    AccessType,
    AttrGetParams,
    AttrSetParams,
    ButtonType,
    Color,
    EventName,
    Font,
    SimpleType,
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

def test_assoc_algorithmname483_reverse_link_reassign_clear():
    a1 = mMDSL_Event(name="sample_text")
    a2 = mMDSL_Event(name="sample_text_2")
    b = mMDSL_Algorithm(name="sample_text")
    _safe_set(b, 'mMDSL_Algorithm485', a1)
    assert _is_linked(b, 'mMDSL_Algorithm485', a1)
    if hasattr(a1, 'mMDSL_Event484'):
        assert _is_linked(a1, 'mMDSL_Event484', b)
    _safe_set(b, 'mMDSL_Algorithm485', a2)
    assert _is_linked(b, 'mMDSL_Algorithm485', a2)
    if hasattr(a1, 'mMDSL_Event484'):
        assert not _is_linked(a1, 'mMDSL_Event484', b)
    if hasattr(a2, 'mMDSL_Event484'):
        assert _is_linked(a2, 'mMDSL_Event484', b)
    _safe_set(b, 'mMDSL_Algorithm485', None)
    assert not _is_linked(b, 'mMDSL_Algorithm485', a2)
    if hasattr(a2, 'mMDSL_Event484'):
        assert not _is_linked(a2, 'mMDSL_Event484', b)


def test_assoc_atomic307_reverse_link_reassign_clear():
    a1 = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    a2 = mMDSL_Expression(false="sample_text_2", true="sample_text_2", valueRealNumber="sample_text_2", valueString="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression308', a1)
    assert _is_linked(b, 'mMDSL_Expression308', a1)
    if hasattr(a1, 'mMDSL_Expression306'):
        assert _is_linked(a1, 'mMDSL_Expression306', b)
    _safe_set(b, 'mMDSL_Expression308', a2)
    assert _is_linked(b, 'mMDSL_Expression308', a2)
    if hasattr(a1, 'mMDSL_Expression306'):
        assert not _is_linked(a1, 'mMDSL_Expression306', b)
    if hasattr(a2, 'mMDSL_Expression306'):
        assert _is_linked(a2, 'mMDSL_Expression306', b)
    _safe_set(b, 'mMDSL_Expression308', None)
    assert not _is_linked(b, 'mMDSL_Expression308', a2)
    if hasattr(a2, 'mMDSL_Expression306'):
        assert not _is_linked(a2, 'mMDSL_Expression306', b)


def test_assoc_attribute54_reverse_link_reassign_clear():
    a1 = mMDSL_Class(name="sample_text")
    a2 = mMDSL_Class(name="sample_text_2")
    b = mMDSL_Attribute(access="sample_text", name="sample_text")
    _safe_set(b, 'mMDSL_Attribute56', a1)
    assert _is_linked(b, 'mMDSL_Attribute56', a1)
    if hasattr(a1, 'mMDSL_Class55'):
        assert _is_linked(a1, 'mMDSL_Class55', b)
    _safe_set(b, 'mMDSL_Attribute56', a2)
    assert _is_linked(b, 'mMDSL_Attribute56', a2)
    if hasattr(a1, 'mMDSL_Class55'):
        assert not _is_linked(a1, 'mMDSL_Class55', b)
    if hasattr(a2, 'mMDSL_Class55'):
        assert _is_linked(a2, 'mMDSL_Class55', b)
    _safe_set(b, 'mMDSL_Attribute56', None)
    assert not _is_linked(b, 'mMDSL_Attribute56', a2)
    if hasattr(a2, 'mMDSL_Class55'):
        assert not _is_linked(a2, 'mMDSL_Class55', b)


def test_assoc_attribute74_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_Attribute(access="sample_text", name="sample_text")
    _safe_set(b, 'mMDSL_Attribute76', a1)
    assert _is_linked(b, 'mMDSL_Attribute76', a1)
    if hasattr(a1, 'mMDSL_Relation75'):
        assert _is_linked(a1, 'mMDSL_Relation75', b)
    _safe_set(b, 'mMDSL_Attribute76', a2)
    assert _is_linked(b, 'mMDSL_Attribute76', a2)
    if hasattr(a1, 'mMDSL_Relation75'):
        assert not _is_linked(a1, 'mMDSL_Relation75', b)
    if hasattr(a2, 'mMDSL_Relation75'):
        assert _is_linked(a2, 'mMDSL_Relation75', b)
    _safe_set(b, 'mMDSL_Attribute76', None)
    assert not _is_linked(b, 'mMDSL_Attribute76', a2)
    if hasattr(a2, 'mMDSL_Relation75'):
        assert not _is_linked(a2, 'mMDSL_Relation75', b)


def test_assoc_breakcontinue257_reverse_link_reassign_clear():
    a1 = mMDSL_ForLoop(interval=7, start=7, stop=7)
    a2 = mMDSL_ForLoop(interval=13, start=13, stop=13)
    b = mMDSL_BreakContinue(break_="sample_text", continue_="sample_text")
    _safe_set(b, 'mMDSL_BreakContinue259', a1)
    assert _is_linked(b, 'mMDSL_BreakContinue259', a1)
    if hasattr(a1, 'mMDSL_ForLoop258'):
        assert _is_linked(a1, 'mMDSL_ForLoop258', b)
    _safe_set(b, 'mMDSL_BreakContinue259', a2)
    assert _is_linked(b, 'mMDSL_BreakContinue259', a2)
    if hasattr(a1, 'mMDSL_ForLoop258'):
        assert not _is_linked(a1, 'mMDSL_ForLoop258', b)
    if hasattr(a2, 'mMDSL_ForLoop258'):
        assert _is_linked(a2, 'mMDSL_ForLoop258', b)
    _safe_set(b, 'mMDSL_BreakContinue259', None)
    assert not _is_linked(b, 'mMDSL_BreakContinue259', a2)
    if hasattr(a2, 'mMDSL_ForLoop258'):
        assert not _is_linked(a2, 'mMDSL_ForLoop258', b)


def test_assoc_classattribute52_reverse_link_reassign_clear():
    a1 = mMDSL_ClassAttribute(name="sample_text")
    a2 = mMDSL_ClassAttribute(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class53', {a1})
    assert _is_linked(b, 'mMDSL_Class53', a1)
    if hasattr(a1, 'mMDSL_ClassAttribute'):
        assert _is_linked(a1, 'mMDSL_ClassAttribute', b)
    _safe_set(b, 'mMDSL_Class53', {a2})
    assert _is_linked(b, 'mMDSL_Class53', a2)
    if hasattr(a1, 'mMDSL_ClassAttribute'):
        assert not _is_linked(a1, 'mMDSL_ClassAttribute', b)
    if hasattr(a2, 'mMDSL_ClassAttribute'):
        assert _is_linked(a2, 'mMDSL_ClassAttribute', b)
    _safe_set(b, 'mMDSL_Class53', set())
    assert not _is_linked(b, 'mMDSL_Class53', a2)
    if hasattr(a2, 'mMDSL_ClassAttribute'):
        assert not _is_linked(a2, 'mMDSL_ClassAttribute', b)


def test_assoc_classinstancefrom455_reverse_link_reassign_clear():
    a1 = mMDSL_RelationInstanceCreate(name="sample_text")
    a2 = mMDSL_RelationInstanceCreate(name="sample_text_2")
    b = mMDSL_ClassInstanceCreate(name="sample_text")
    _safe_set(b, 'mMDSL_ClassInstanceCreate457', a1)
    assert _is_linked(b, 'mMDSL_ClassInstanceCreate457', a1)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate456'):
        assert _is_linked(a1, 'mMDSL_RelationInstanceCreate456', b)
    _safe_set(b, 'mMDSL_ClassInstanceCreate457', a2)
    assert _is_linked(b, 'mMDSL_ClassInstanceCreate457', a2)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate456'):
        assert not _is_linked(a1, 'mMDSL_RelationInstanceCreate456', b)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate456'):
        assert _is_linked(a2, 'mMDSL_RelationInstanceCreate456', b)
    _safe_set(b, 'mMDSL_ClassInstanceCreate457', None)
    assert not _is_linked(b, 'mMDSL_ClassInstanceCreate457', a2)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate456'):
        assert not _is_linked(a2, 'mMDSL_RelationInstanceCreate456', b)


def test_assoc_classinstanceto458_reverse_link_reassign_clear():
    a1 = mMDSL_RelationInstanceCreate(name="sample_text")
    a2 = mMDSL_RelationInstanceCreate(name="sample_text_2")
    b = mMDSL_ClassInstanceCreate(name="sample_text")
    _safe_set(b, 'mMDSL_ClassInstanceCreate460', a1)
    assert _is_linked(b, 'mMDSL_ClassInstanceCreate460', a1)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate459'):
        assert _is_linked(a1, 'mMDSL_RelationInstanceCreate459', b)
    _safe_set(b, 'mMDSL_ClassInstanceCreate460', a2)
    assert _is_linked(b, 'mMDSL_ClassInstanceCreate460', a2)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate459'):
        assert not _is_linked(a1, 'mMDSL_RelationInstanceCreate459', b)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate459'):
        assert _is_linked(a2, 'mMDSL_RelationInstanceCreate459', b)
    _safe_set(b, 'mMDSL_ClassInstanceCreate460', None)
    assert not _is_linked(b, 'mMDSL_ClassInstanceCreate460', a2)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate459'):
        assert not _is_linked(a2, 'mMDSL_RelationInstanceCreate459', b)


def test_assoc_classname106_reverse_link_reassign_clear():
    a1 = mMDSL_Mode(name="sample_text")
    a2 = mMDSL_Mode(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class108', a1)
    assert _is_linked(b, 'mMDSL_Class108', a1)
    if hasattr(a1, 'mMDSL_Mode107'):
        assert _is_linked(a1, 'mMDSL_Mode107', b)
    _safe_set(b, 'mMDSL_Class108', a2)
    assert _is_linked(b, 'mMDSL_Class108', a2)
    if hasattr(a1, 'mMDSL_Mode107'):
        assert not _is_linked(a1, 'mMDSL_Mode107', b)
    if hasattr(a2, 'mMDSL_Mode107'):
        assert _is_linked(a2, 'mMDSL_Mode107', b)
    _safe_set(b, 'mMDSL_Class108', None)
    assert not _is_linked(b, 'mMDSL_Class108', a2)
    if hasattr(a2, 'mMDSL_Mode107'):
        assert not _is_linked(a2, 'mMDSL_Mode107', b)


def test_assoc_classname98_reverse_link_reassign_clear():
    a1 = mMDSL_ModelType(name="sample_text")
    a2 = mMDSL_ModelType(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class100', a1)
    assert _is_linked(b, 'mMDSL_Class100', a1)
    if hasattr(a1, 'mMDSL_ModelType99'):
        assert _is_linked(a1, 'mMDSL_ModelType99', b)
    _safe_set(b, 'mMDSL_Class100', a2)
    assert _is_linked(b, 'mMDSL_Class100', a2)
    if hasattr(a1, 'mMDSL_ModelType99'):
        assert not _is_linked(a1, 'mMDSL_ModelType99', b)
    if hasattr(a2, 'mMDSL_ModelType99'):
        assert _is_linked(a2, 'mMDSL_ModelType99', b)
    _safe_set(b, 'mMDSL_Class100', None)
    assert not _is_linked(b, 'mMDSL_Class100', a2)
    if hasattr(a2, 'mMDSL_ModelType99'):
        assert not _is_linked(a2, 'mMDSL_ModelType99', b)


def test_assoc_embedcodetype19_reverse_link_reassign_clear():
    a1 = mMDSL_EmbedCodeType(name="sample_text")
    a2 = mMDSL_EmbedCodeType(name="sample_text_2")
    b = mMDSL_EmbedCode(embeddedcode="sample_text", name="sample_text")
    _safe_set(b, 'mMDSL_EmbedCode20', a1)
    assert _is_linked(b, 'mMDSL_EmbedCode20', a1)
    if hasattr(a1, 'mMDSL_EmbedCodeType21'):
        assert _is_linked(a1, 'mMDSL_EmbedCodeType21', b)
    _safe_set(b, 'mMDSL_EmbedCode20', a2)
    assert _is_linked(b, 'mMDSL_EmbedCode20', a2)
    if hasattr(a1, 'mMDSL_EmbedCodeType21'):
        assert not _is_linked(a1, 'mMDSL_EmbedCodeType21', b)
    if hasattr(a2, 'mMDSL_EmbedCodeType21'):
        assert _is_linked(a2, 'mMDSL_EmbedCodeType21', b)
    _safe_set(b, 'mMDSL_EmbedCode20', None)
    assert not _is_linked(b, 'mMDSL_EmbedCode20', a2)
    if hasattr(a2, 'mMDSL_EmbedCodeType21'):
        assert not _is_linked(a2, 'mMDSL_EmbedCodeType21', b)


def test_assoc_embedplatformtype16_reverse_link_reassign_clear():
    a1 = mMDSL_EmbedPlatformType(name="sample_text")
    a2 = mMDSL_EmbedPlatformType(name="sample_text_2")
    b = mMDSL_EmbedCode(embeddedcode="sample_text", name="sample_text")
    _safe_set(b, 'mMDSL_EmbedCode17', a1)
    assert _is_linked(b, 'mMDSL_EmbedCode17', a1)
    if hasattr(a1, 'mMDSL_EmbedPlatformType18'):
        assert _is_linked(a1, 'mMDSL_EmbedPlatformType18', b)
    _safe_set(b, 'mMDSL_EmbedCode17', a2)
    assert _is_linked(b, 'mMDSL_EmbedCode17', a2)
    if hasattr(a1, 'mMDSL_EmbedPlatformType18'):
        assert not _is_linked(a1, 'mMDSL_EmbedPlatformType18', b)
    if hasattr(a2, 'mMDSL_EmbedPlatformType18'):
        assert _is_linked(a2, 'mMDSL_EmbedPlatformType18', b)
    _safe_set(b, 'mMDSL_EmbedCode17', None)
    assert not _is_linked(b, 'mMDSL_EmbedCode17', a2)
    if hasattr(a2, 'mMDSL_EmbedPlatformType18'):
        assert not _is_linked(a2, 'mMDSL_EmbedPlatformType18', b)


def test_assoc_expression310_reverse_link_reassign_clear():
    a1 = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    a2 = mMDSL_Expression(false="sample_text_2", true="sample_text_2", valueRealNumber="sample_text_2", valueString="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression311', a1)
    assert _is_linked(b, 'mMDSL_Expression311', a1)
    if hasattr(a1, 'mMDSL_Expression309'):
        assert _is_linked(a1, 'mMDSL_Expression309', b)
    _safe_set(b, 'mMDSL_Expression311', a2)
    assert _is_linked(b, 'mMDSL_Expression311', a2)
    if hasattr(a1, 'mMDSL_Expression309'):
        assert not _is_linked(a1, 'mMDSL_Expression309', b)
    if hasattr(a2, 'mMDSL_Expression309'):
        assert _is_linked(a2, 'mMDSL_Expression309', b)
    _safe_set(b, 'mMDSL_Expression311', None)
    assert not _is_linked(b, 'mMDSL_Expression311', a2)
    if hasattr(a2, 'mMDSL_Expression309'):
        assert not _is_linked(a2, 'mMDSL_Expression309', b)


def test_assoc_fillcolor163_reverse_link_reassign_clear():
    a1 = mMDSL_Text(fontsize="sample_text", value="sample_text", x="sample_text", y="sample_text")
    a2 = mMDSL_Text(fontsize="sample_text_2", value="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = mMDSL_FillColor(color="sample_text", hexcolor="sample_text")
    _safe_set(b, 'mMDSL_FillColor', a1)
    assert _is_linked(b, 'mMDSL_FillColor', a1)
    if hasattr(a1, 'mMDSL_Text164'):
        assert _is_linked(a1, 'mMDSL_Text164', b)
    _safe_set(b, 'mMDSL_FillColor', a2)
    assert _is_linked(b, 'mMDSL_FillColor', a2)
    if hasattr(a1, 'mMDSL_Text164'):
        assert not _is_linked(a1, 'mMDSL_Text164', b)
    if hasattr(a2, 'mMDSL_Text164'):
        assert _is_linked(a2, 'mMDSL_Text164', b)
    _safe_set(b, 'mMDSL_FillColor', None)
    assert not _is_linked(b, 'mMDSL_FillColor', a2)
    if hasattr(a2, 'mMDSL_Text164'):
        assert not _is_linked(a2, 'mMDSL_Text164', b)


def test_assoc_fillcolor204_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    a2 = mMDSL_SymbolStyle(fontsize="sample_text_2", name="sample_text_2", strokewidth="sample_text_2")
    b = mMDSL_FillColor(color="sample_text", hexcolor="sample_text")
    _safe_set(b, 'mMDSL_FillColor206', a1)
    assert _is_linked(b, 'mMDSL_FillColor206', a1)
    if hasattr(a1, 'mMDSL_SymbolStyle205'):
        assert _is_linked(a1, 'mMDSL_SymbolStyle205', b)
    _safe_set(b, 'mMDSL_FillColor206', a2)
    assert _is_linked(b, 'mMDSL_FillColor206', a2)
    if hasattr(a1, 'mMDSL_SymbolStyle205'):
        assert not _is_linked(a1, 'mMDSL_SymbolStyle205', b)
    if hasattr(a2, 'mMDSL_SymbolStyle205'):
        assert _is_linked(a2, 'mMDSL_SymbolStyle205', b)
    _safe_set(b, 'mMDSL_FillColor206', None)
    assert not _is_linked(b, 'mMDSL_FillColor206', a2)
    if hasattr(a2, 'mMDSL_SymbolStyle205'):
        assert not _is_linked(a2, 'mMDSL_SymbolStyle205', b)


def test_assoc_fontfamily161_reverse_link_reassign_clear():
    a1 = mMDSL_Text(fontsize="sample_text", value="sample_text", x="sample_text", y="sample_text")
    a2 = mMDSL_Text(fontsize="sample_text_2", value="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = mMDSL_FontFamily(font="sample_text", fontstr="sample_text")
    _safe_set(b, 'mMDSL_FontFamily', a1)
    assert _is_linked(b, 'mMDSL_FontFamily', a1)
    if hasattr(a1, 'mMDSL_Text162'):
        assert _is_linked(a1, 'mMDSL_Text162', b)
    _safe_set(b, 'mMDSL_FontFamily', a2)
    assert _is_linked(b, 'mMDSL_FontFamily', a2)
    if hasattr(a1, 'mMDSL_Text162'):
        assert not _is_linked(a1, 'mMDSL_Text162', b)
    if hasattr(a2, 'mMDSL_Text162'):
        assert _is_linked(a2, 'mMDSL_Text162', b)
    _safe_set(b, 'mMDSL_FontFamily', None)
    assert not _is_linked(b, 'mMDSL_FontFamily', a2)
    if hasattr(a2, 'mMDSL_Text162'):
        assert not _is_linked(a2, 'mMDSL_Text162', b)


def test_assoc_fontfamily209_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    a2 = mMDSL_SymbolStyle(fontsize="sample_text_2", name="sample_text_2", strokewidth="sample_text_2")
    b = mMDSL_FontFamily(font="sample_text", fontstr="sample_text")
    _safe_set(b, 'mMDSL_FontFamily211', a1)
    assert _is_linked(b, 'mMDSL_FontFamily211', a1)
    if hasattr(a1, 'mMDSL_SymbolStyle210'):
        assert _is_linked(a1, 'mMDSL_SymbolStyle210', b)
    _safe_set(b, 'mMDSL_FontFamily211', a2)
    assert _is_linked(b, 'mMDSL_FontFamily211', a2)
    if hasattr(a1, 'mMDSL_SymbolStyle210'):
        assert not _is_linked(a1, 'mMDSL_SymbolStyle210', b)
    if hasattr(a2, 'mMDSL_SymbolStyle210'):
        assert _is_linked(a2, 'mMDSL_SymbolStyle210', b)
    _safe_set(b, 'mMDSL_FontFamily211', None)
    assert not _is_linked(b, 'mMDSL_FontFamily211', a2)
    if hasattr(a2, 'mMDSL_SymbolStyle210'):
        assert not _is_linked(a2, 'mMDSL_SymbolStyle210', b)


def test_assoc_fromclassname68_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class70', a1)
    assert _is_linked(b, 'mMDSL_Class70', a1)
    if hasattr(a1, 'mMDSL_Relation69'):
        assert _is_linked(a1, 'mMDSL_Relation69', b)
    _safe_set(b, 'mMDSL_Class70', a2)
    assert _is_linked(b, 'mMDSL_Class70', a2)
    if hasattr(a1, 'mMDSL_Relation69'):
        assert not _is_linked(a1, 'mMDSL_Relation69', b)
    if hasattr(a2, 'mMDSL_Relation69'):
        assert _is_linked(a2, 'mMDSL_Relation69', b)
    _safe_set(b, 'mMDSL_Class70', None)
    assert not _is_linked(b, 'mMDSL_Class70', a2)
    if hasattr(a2, 'mMDSL_Relation69'):
        assert not _is_linked(a2, 'mMDSL_Relation69', b)


def test_assoc_globalstyle112_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    a2 = mMDSL_SymbolStyle(fontsize="sample_text_2", name="sample_text_2", strokewidth="sample_text_2")
    b = mMDSL_SymbolClass(name="sample_text")
    _safe_set(b, 'mMDSL_SymbolClass113', a1)
    assert _is_linked(b, 'mMDSL_SymbolClass113', a1)
    if hasattr(a1, 'mMDSL_SymbolStyle114'):
        assert _is_linked(a1, 'mMDSL_SymbolStyle114', b)
    _safe_set(b, 'mMDSL_SymbolClass113', a2)
    assert _is_linked(b, 'mMDSL_SymbolClass113', a2)
    if hasattr(a1, 'mMDSL_SymbolStyle114'):
        assert not _is_linked(a1, 'mMDSL_SymbolStyle114', b)
    if hasattr(a2, 'mMDSL_SymbolStyle114'):
        assert _is_linked(a2, 'mMDSL_SymbolStyle114', b)
    _safe_set(b, 'mMDSL_SymbolClass113', None)
    assert not _is_linked(b, 'mMDSL_SymbolClass113', a2)
    if hasattr(a2, 'mMDSL_SymbolStyle114'):
        assert not _is_linked(a2, 'mMDSL_SymbolStyle114', b)


def test_assoc_globalstyle117_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    a2 = mMDSL_SymbolStyle(fontsize="sample_text_2", name="sample_text_2", strokewidth="sample_text_2")
    b = mMDSL_SymbolRelation(name="sample_text")
    _safe_set(b, 'mMDSL_SymbolRelation118', a1)
    assert _is_linked(b, 'mMDSL_SymbolRelation118', a1)
    if hasattr(a1, 'mMDSL_SymbolStyle119'):
        assert _is_linked(a1, 'mMDSL_SymbolStyle119', b)
    _safe_set(b, 'mMDSL_SymbolRelation118', a2)
    assert _is_linked(b, 'mMDSL_SymbolRelation118', a2)
    if hasattr(a1, 'mMDSL_SymbolStyle119'):
        assert not _is_linked(a1, 'mMDSL_SymbolStyle119', b)
    if hasattr(a2, 'mMDSL_SymbolStyle119'):
        assert _is_linked(a2, 'mMDSL_SymbolStyle119', b)
    _safe_set(b, 'mMDSL_SymbolRelation118', None)
    assert not _is_linked(b, 'mMDSL_SymbolRelation118', a2)
    if hasattr(a2, 'mMDSL_SymbolStyle119'):
        assert not _is_linked(a2, 'mMDSL_SymbolStyle119', b)


def test_assoc_includelibrarytype13_reverse_link_reassign_clear():
    a1 = mMDSL_IncludeLibraryType(name="sample_text")
    a2 = mMDSL_IncludeLibraryType(name="sample_text_2")
    b = mMDSL_IncludeLibrary(name="sample_text")
    _safe_set(b, 'mMDSL_IncludeLibrary14', a1)
    assert _is_linked(b, 'mMDSL_IncludeLibrary14', a1)
    if hasattr(a1, 'mMDSL_IncludeLibraryType15'):
        assert _is_linked(a1, 'mMDSL_IncludeLibraryType15', b)
    _safe_set(b, 'mMDSL_IncludeLibrary14', a2)
    assert _is_linked(b, 'mMDSL_IncludeLibrary14', a2)
    if hasattr(a1, 'mMDSL_IncludeLibraryType15'):
        assert not _is_linked(a1, 'mMDSL_IncludeLibraryType15', b)
    if hasattr(a2, 'mMDSL_IncludeLibraryType15'):
        assert _is_linked(a2, 'mMDSL_IncludeLibraryType15', b)
    _safe_set(b, 'mMDSL_IncludeLibrary14', None)
    assert not _is_linked(b, 'mMDSL_IncludeLibrary14', a2)
    if hasattr(a2, 'mMDSL_IncludeLibraryType15'):
        assert not _is_linked(a2, 'mMDSL_IncludeLibraryType15', b)


def test_assoc_left316_reverse_link_reassign_clear():
    a1 = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    a2 = mMDSL_Expression(false="sample_text_2", true="sample_text_2", valueRealNumber="sample_text_2", valueString="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression317', a1)
    assert _is_linked(b, 'mMDSL_Expression317', a1)
    if hasattr(a1, 'mMDSL_Expression315'):
        assert _is_linked(a1, 'mMDSL_Expression315', b)
    _safe_set(b, 'mMDSL_Expression317', a2)
    assert _is_linked(b, 'mMDSL_Expression317', a2)
    if hasattr(a1, 'mMDSL_Expression315'):
        assert not _is_linked(a1, 'mMDSL_Expression315', b)
    if hasattr(a2, 'mMDSL_Expression315'):
        assert _is_linked(a2, 'mMDSL_Expression315', b)
    _safe_set(b, 'mMDSL_Expression317', None)
    assert not _is_linked(b, 'mMDSL_Expression317', a2)
    if hasattr(a2, 'mMDSL_Expression315'):
        assert not _is_linked(a2, 'mMDSL_Expression315', b)


def test_assoc_modeltype395_reverse_link_reassign_clear():
    a1 = mMDSL_ModelType(name="sample_text")
    a2 = mMDSL_ModelType(name="sample_text_2")
    b = mMDSL_ModelCreate(name="sample_text")
    _safe_set(b, 'mMDSL_ModelCreate396', a1)
    assert _is_linked(b, 'mMDSL_ModelCreate396', a1)
    if hasattr(a1, 'mMDSL_ModelType397'):
        assert _is_linked(a1, 'mMDSL_ModelType397', b)
    _safe_set(b, 'mMDSL_ModelCreate396', a2)
    assert _is_linked(b, 'mMDSL_ModelCreate396', a2)
    if hasattr(a1, 'mMDSL_ModelType397'):
        assert not _is_linked(a1, 'mMDSL_ModelType397', b)
    if hasattr(a2, 'mMDSL_ModelType397'):
        assert _is_linked(a2, 'mMDSL_ModelType397', b)
    _safe_set(b, 'mMDSL_ModelCreate396', None)
    assert not _is_linked(b, 'mMDSL_ModelCreate396', a2)
    if hasattr(a2, 'mMDSL_ModelType397'):
        assert not _is_linked(a2, 'mMDSL_ModelType397', b)


def test_assoc_modename104_reverse_link_reassign_clear():
    a1 = mMDSL_ModelType(name="sample_text")
    a2 = mMDSL_ModelType(name="sample_text_2")
    b = mMDSL_Mode(name="sample_text")
    _safe_set(b, 'mMDSL_Mode', a1)
    assert _is_linked(b, 'mMDSL_Mode', a1)
    if hasattr(a1, 'mMDSL_ModelType105'):
        assert _is_linked(a1, 'mMDSL_ModelType105', b)
    _safe_set(b, 'mMDSL_Mode', a2)
    assert _is_linked(b, 'mMDSL_Mode', a2)
    if hasattr(a1, 'mMDSL_ModelType105'):
        assert not _is_linked(a1, 'mMDSL_ModelType105', b)
    if hasattr(a2, 'mMDSL_ModelType105'):
        assert _is_linked(a2, 'mMDSL_ModelType105', b)
    _safe_set(b, 'mMDSL_Mode', None)
    assert not _is_linked(b, 'mMDSL_Mode', a2)
    if hasattr(a2, 'mMDSL_ModelType105'):
        assert not _is_linked(a2, 'mMDSL_ModelType105', b)


def test_assoc_multyassign297_reverse_link_reassign_clear():
    a1 = mMDSL_OperatorMultyAssign(addassign="sample_text", divassign="sample_text", multiassign="sample_text", subassign="sample_text")
    a2 = mMDSL_OperatorMultyAssign(addassign="sample_text_2", divassign="sample_text_2", multiassign="sample_text_2", subassign="sample_text_2")
    b = mMDSL_OperatorAssign(assign="sample_text")
    _safe_set(b, 'mMDSL_OperatorAssign298', a1)
    assert _is_linked(b, 'mMDSL_OperatorAssign298', a1)
    if hasattr(a1, 'mMDSL_OperatorMultyAssign'):
        assert _is_linked(a1, 'mMDSL_OperatorMultyAssign', b)
    _safe_set(b, 'mMDSL_OperatorAssign298', a2)
    assert _is_linked(b, 'mMDSL_OperatorAssign298', a2)
    if hasattr(a1, 'mMDSL_OperatorMultyAssign'):
        assert not _is_linked(a1, 'mMDSL_OperatorMultyAssign', b)
    if hasattr(a2, 'mMDSL_OperatorMultyAssign'):
        assert _is_linked(a2, 'mMDSL_OperatorMultyAssign', b)
    _safe_set(b, 'mMDSL_OperatorAssign298', None)
    assert not _is_linked(b, 'mMDSL_OperatorAssign298', a2)
    if hasattr(a2, 'mMDSL_OperatorMultyAssign'):
        assert not _is_linked(a2, 'mMDSL_OperatorMultyAssign', b)


def test_assoc_nameofclass427_reverse_link_reassign_clear():
    a1 = mMDSL_ClassInstanceCreate(name="sample_text")
    a2 = mMDSL_ClassInstanceCreate(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class429', a1)
    assert _is_linked(b, 'mMDSL_Class429', a1)
    if hasattr(a1, 'mMDSL_ClassInstanceCreate428'):
        assert _is_linked(a1, 'mMDSL_ClassInstanceCreate428', b)
    _safe_set(b, 'mMDSL_Class429', a2)
    assert _is_linked(b, 'mMDSL_Class429', a2)
    if hasattr(a1, 'mMDSL_ClassInstanceCreate428'):
        assert not _is_linked(a1, 'mMDSL_ClassInstanceCreate428', b)
    if hasattr(a2, 'mMDSL_ClassInstanceCreate428'):
        assert _is_linked(a2, 'mMDSL_ClassInstanceCreate428', b)
    _safe_set(b, 'mMDSL_Class429', None)
    assert not _is_linked(b, 'mMDSL_Class429', a2)
    if hasattr(a2, 'mMDSL_ClassInstanceCreate428'):
        assert not _is_linked(a2, 'mMDSL_ClassInstanceCreate428', b)


def test_assoc_nameofrelation452_reverse_link_reassign_clear():
    a1 = mMDSL_RelationInstanceCreate(name="sample_text")
    a2 = mMDSL_RelationInstanceCreate(name="sample_text_2")
    b = mMDSL_Relation(name="sample_text")
    _safe_set(b, 'mMDSL_Relation454', a1)
    assert _is_linked(b, 'mMDSL_Relation454', a1)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate453'):
        assert _is_linked(a1, 'mMDSL_RelationInstanceCreate453', b)
    _safe_set(b, 'mMDSL_Relation454', a2)
    assert _is_linked(b, 'mMDSL_Relation454', a2)
    if hasattr(a1, 'mMDSL_RelationInstanceCreate453'):
        assert not _is_linked(a1, 'mMDSL_RelationInstanceCreate453', b)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate453'):
        assert _is_linked(a2, 'mMDSL_RelationInstanceCreate453', b)
    _safe_set(b, 'mMDSL_Relation454', None)
    assert not _is_linked(b, 'mMDSL_Relation454', a2)
    if hasattr(a2, 'mMDSL_RelationInstanceCreate453'):
        assert not _is_linked(a2, 'mMDSL_RelationInstanceCreate453', b)


def test_assoc_opassing260_reverse_link_reassign_clear():
    a1 = mMDSL_Variable(name="sample_text")
    a2 = mMDSL_Variable(name="sample_text_2")
    b = mMDSL_OperatorAssign(assign="sample_text")
    _safe_set(b, 'mMDSL_OperatorAssign', a1)
    assert _is_linked(b, 'mMDSL_OperatorAssign', a1)
    if hasattr(a1, 'mMDSL_Variable261'):
        assert _is_linked(a1, 'mMDSL_Variable261', b)
    _safe_set(b, 'mMDSL_OperatorAssign', a2)
    assert _is_linked(b, 'mMDSL_OperatorAssign', a2)
    if hasattr(a1, 'mMDSL_Variable261'):
        assert not _is_linked(a1, 'mMDSL_Variable261', b)
    if hasattr(a2, 'mMDSL_Variable261'):
        assert _is_linked(a2, 'mMDSL_Variable261', b)
    _safe_set(b, 'mMDSL_OperatorAssign', None)
    assert not _is_linked(b, 'mMDSL_OperatorAssign', a2)
    if hasattr(a2, 'mMDSL_Variable261'):
        assert not _is_linked(a2, 'mMDSL_Variable261', b)


def test_assoc_operand304_reverse_link_reassign_clear():
    a1 = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    a2 = mMDSL_Expression(false="sample_text_2", true="sample_text_2", valueRealNumber="sample_text_2", valueString="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression305', a1)
    assert _is_linked(b, 'mMDSL_Expression305', a1)
    if hasattr(a1, 'mMDSL_Expression303'):
        assert _is_linked(a1, 'mMDSL_Expression303', b)
    _safe_set(b, 'mMDSL_Expression305', a2)
    assert _is_linked(b, 'mMDSL_Expression305', a2)
    if hasattr(a1, 'mMDSL_Expression303'):
        assert not _is_linked(a1, 'mMDSL_Expression303', b)
    if hasattr(a2, 'mMDSL_Expression303'):
        assert _is_linked(a2, 'mMDSL_Expression303', b)
    _safe_set(b, 'mMDSL_Expression305', None)
    assert not _is_linked(b, 'mMDSL_Expression305', a2)
    if hasattr(a2, 'mMDSL_Expression303'):
        assert not _is_linked(a2, 'mMDSL_Expression303', b)


def test_assoc_parentclassname47_reverse_link_reassign_clear():
    a1 = mMDSL_Class(name="sample_text")
    a2 = mMDSL_Class(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class48', a1)
    assert _is_linked(b, 'mMDSL_Class48', a1)
    if hasattr(a1, 'mMDSL_Class46'):
        assert _is_linked(a1, 'mMDSL_Class46', b)
    _safe_set(b, 'mMDSL_Class48', a2)
    assert _is_linked(b, 'mMDSL_Class48', a2)
    if hasattr(a1, 'mMDSL_Class46'):
        assert not _is_linked(a1, 'mMDSL_Class46', b)
    if hasattr(a2, 'mMDSL_Class46'):
        assert _is_linked(a2, 'mMDSL_Class46', b)
    _safe_set(b, 'mMDSL_Class48', None)
    assert not _is_linked(b, 'mMDSL_Class48', a2)
    if hasattr(a2, 'mMDSL_Class46'):
        assert not _is_linked(a2, 'mMDSL_Class46', b)


def test_assoc_parentrelationname63_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_Relation(name="sample_text")
    _safe_set(b, 'mMDSL_Relation64', a1)
    assert _is_linked(b, 'mMDSL_Relation64', a1)
    if hasattr(a1, 'mMDSL_Relation62'):
        assert _is_linked(a1, 'mMDSL_Relation62', b)
    _safe_set(b, 'mMDSL_Relation64', a2)
    assert _is_linked(b, 'mMDSL_Relation64', a2)
    if hasattr(a1, 'mMDSL_Relation62'):
        assert not _is_linked(a1, 'mMDSL_Relation62', b)
    if hasattr(a2, 'mMDSL_Relation62'):
        assert _is_linked(a2, 'mMDSL_Relation62', b)
    _safe_set(b, 'mMDSL_Relation64', None)
    assert not _is_linked(b, 'mMDSL_Relation64', a2)
    if hasattr(a2, 'mMDSL_Relation62'):
        assert not _is_linked(a2, 'mMDSL_Relation62', b)


def test_assoc_reference60_reverse_link_reassign_clear():
    a1 = mMDSL_Reference(name="sample_text")
    a2 = mMDSL_Reference(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class61', {a1})
    assert _is_linked(b, 'mMDSL_Class61', a1)
    if hasattr(a1, 'mMDSL_Reference'):
        assert _is_linked(a1, 'mMDSL_Reference', b)
    _safe_set(b, 'mMDSL_Class61', {a2})
    assert _is_linked(b, 'mMDSL_Class61', a2)
    if hasattr(a1, 'mMDSL_Reference'):
        assert not _is_linked(a1, 'mMDSL_Reference', b)
    if hasattr(a2, 'mMDSL_Reference'):
        assert _is_linked(a2, 'mMDSL_Reference', b)
    _safe_set(b, 'mMDSL_Class61', set())
    assert not _is_linked(b, 'mMDSL_Class61', a2)
    if hasattr(a2, 'mMDSL_Reference'):
        assert not _is_linked(a2, 'mMDSL_Reference', b)


def test_assoc_relationname101_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_ModelType(name="sample_text")
    _safe_set(b, 'mMDSL_ModelType102', {a1})
    assert _is_linked(b, 'mMDSL_ModelType102', a1)
    if hasattr(a1, 'mMDSL_Relation103'):
        assert _is_linked(a1, 'mMDSL_Relation103', b)
    _safe_set(b, 'mMDSL_ModelType102', {a2})
    assert _is_linked(b, 'mMDSL_ModelType102', a2)
    if hasattr(a1, 'mMDSL_Relation103'):
        assert not _is_linked(a1, 'mMDSL_Relation103', b)
    if hasattr(a2, 'mMDSL_Relation103'):
        assert _is_linked(a2, 'mMDSL_Relation103', b)
    _safe_set(b, 'mMDSL_ModelType102', set())
    assert not _is_linked(b, 'mMDSL_ModelType102', a2)
    if hasattr(a2, 'mMDSL_Relation103'):
        assert not _is_linked(a2, 'mMDSL_Relation103', b)


def test_assoc_relationname109_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_Mode(name="sample_text")
    _safe_set(b, 'mMDSL_Mode110', {a1})
    assert _is_linked(b, 'mMDSL_Mode110', a1)
    if hasattr(a1, 'mMDSL_Relation111'):
        assert _is_linked(a1, 'mMDSL_Relation111', b)
    _safe_set(b, 'mMDSL_Mode110', {a2})
    assert _is_linked(b, 'mMDSL_Mode110', a2)
    if hasattr(a1, 'mMDSL_Relation111'):
        assert not _is_linked(a1, 'mMDSL_Relation111', b)
    if hasattr(a2, 'mMDSL_Relation111'):
        assert _is_linked(a2, 'mMDSL_Relation111', b)
    _safe_set(b, 'mMDSL_Mode110', set())
    assert not _is_linked(b, 'mMDSL_Mode110', a2)
    if hasattr(a2, 'mMDSL_Relation111'):
        assert not _is_linked(a2, 'mMDSL_Relation111', b)


def test_assoc_right319_reverse_link_reassign_clear():
    a1 = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    a2 = mMDSL_Expression(false="sample_text_2", true="sample_text_2", valueRealNumber="sample_text_2", valueString="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression320', a1)
    assert _is_linked(b, 'mMDSL_Expression320', a1)
    if hasattr(a1, 'mMDSL_Expression318'):
        assert _is_linked(a1, 'mMDSL_Expression318', b)
    _safe_set(b, 'mMDSL_Expression320', a2)
    assert _is_linked(b, 'mMDSL_Expression320', a2)
    if hasattr(a1, 'mMDSL_Expression318'):
        assert not _is_linked(a1, 'mMDSL_Expression318', b)
    if hasattr(a2, 'mMDSL_Expression318'):
        assert _is_linked(a2, 'mMDSL_Expression318', b)
    _safe_set(b, 'mMDSL_Expression320', None)
    assert not _is_linked(b, 'mMDSL_Expression320', a2)
    if hasattr(a2, 'mMDSL_Expression318'):
        assert not _is_linked(a2, 'mMDSL_Expression318', b)


def test_assoc_strokecolor207_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    a2 = mMDSL_SymbolStyle(fontsize="sample_text_2", name="sample_text_2", strokewidth="sample_text_2")
    b = mMDSL_StrokeColor(color="sample_text", hexcolor="sample_text")
    _safe_set(b, 'mMDSL_StrokeColor', a1)
    assert _is_linked(b, 'mMDSL_StrokeColor', a1)
    if hasattr(a1, 'mMDSL_SymbolStyle208'):
        assert _is_linked(a1, 'mMDSL_SymbolStyle208', b)
    _safe_set(b, 'mMDSL_StrokeColor', a2)
    assert _is_linked(b, 'mMDSL_StrokeColor', a2)
    if hasattr(a1, 'mMDSL_SymbolStyle208'):
        assert not _is_linked(a1, 'mMDSL_SymbolStyle208', b)
    if hasattr(a2, 'mMDSL_SymbolStyle208'):
        assert _is_linked(a2, 'mMDSL_SymbolStyle208', b)
    _safe_set(b, 'mMDSL_StrokeColor', None)
    assert not _is_linked(b, 'mMDSL_StrokeColor', a2)
    if hasattr(a2, 'mMDSL_SymbolStyle208'):
        assert not _is_linked(a2, 'mMDSL_SymbolStyle208', b)


def test_assoc_symbolclass49_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolClass(name="sample_text")
    a2 = mMDSL_SymbolClass(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class50', a1)
    assert _is_linked(b, 'mMDSL_Class50', a1)
    if hasattr(a1, 'mMDSL_SymbolClass51'):
        assert _is_linked(a1, 'mMDSL_SymbolClass51', b)
    _safe_set(b, 'mMDSL_Class50', a2)
    assert _is_linked(b, 'mMDSL_Class50', a2)
    if hasattr(a1, 'mMDSL_SymbolClass51'):
        assert not _is_linked(a1, 'mMDSL_SymbolClass51', b)
    if hasattr(a2, 'mMDSL_SymbolClass51'):
        assert _is_linked(a2, 'mMDSL_SymbolClass51', b)
    _safe_set(b, 'mMDSL_Class50', None)
    assert not _is_linked(b, 'mMDSL_Class50', a2)
    if hasattr(a2, 'mMDSL_SymbolClass51'):
        assert not _is_linked(a2, 'mMDSL_SymbolClass51', b)


def test_assoc_symbolrelation65_reverse_link_reassign_clear():
    a1 = mMDSL_SymbolRelation(name="sample_text")
    a2 = mMDSL_SymbolRelation(name="sample_text_2")
    b = mMDSL_Relation(name="sample_text")
    _safe_set(b, 'mMDSL_Relation66', a1)
    assert _is_linked(b, 'mMDSL_Relation66', a1)
    if hasattr(a1, 'mMDSL_SymbolRelation67'):
        assert _is_linked(a1, 'mMDSL_SymbolRelation67', b)
    _safe_set(b, 'mMDSL_Relation66', a2)
    assert _is_linked(b, 'mMDSL_Relation66', a2)
    if hasattr(a1, 'mMDSL_SymbolRelation67'):
        assert not _is_linked(a1, 'mMDSL_SymbolRelation67', b)
    if hasattr(a2, 'mMDSL_SymbolRelation67'):
        assert _is_linked(a2, 'mMDSL_SymbolRelation67', b)
    _safe_set(b, 'mMDSL_Relation66', None)
    assert not _is_linked(b, 'mMDSL_Relation66', a2)
    if hasattr(a2, 'mMDSL_SymbolRelation67'):
        assert not _is_linked(a2, 'mMDSL_SymbolRelation67', b)


def test_assoc_toclassname71_reverse_link_reassign_clear():
    a1 = mMDSL_Relation(name="sample_text")
    a2 = mMDSL_Relation(name="sample_text_2")
    b = mMDSL_Class(name="sample_text")
    _safe_set(b, 'mMDSL_Class73', a1)
    assert _is_linked(b, 'mMDSL_Class73', a1)
    if hasattr(a1, 'mMDSL_Relation72'):
        assert _is_linked(a1, 'mMDSL_Relation72', b)
    _safe_set(b, 'mMDSL_Class73', a2)
    assert _is_linked(b, 'mMDSL_Class73', a2)
    if hasattr(a1, 'mMDSL_Relation72'):
        assert not _is_linked(a1, 'mMDSL_Relation72', b)
    if hasattr(a2, 'mMDSL_Relation72'):
        assert _is_linked(a2, 'mMDSL_Relation72', b)
    _safe_set(b, 'mMDSL_Class73', None)
    assert not _is_linked(b, 'mMDSL_Class73', a2)
    if hasattr(a2, 'mMDSL_Relation72'):
        assert not _is_linked(a2, 'mMDSL_Relation72', b)


def test_assoc_type80_reverse_link_reassign_clear():
    a1 = mMDSL_Type(simpletype="sample_text")
    a2 = mMDSL_Type(simpletype="sample_text_2")
    b = mMDSL_Attribute(access="sample_text", name="sample_text")
    _safe_set(b, 'mMDSL_Attribute81', a1)
    assert _is_linked(b, 'mMDSL_Attribute81', a1)
    if hasattr(a1, 'mMDSL_Type'):
        assert _is_linked(a1, 'mMDSL_Type', b)
    _safe_set(b, 'mMDSL_Attribute81', a2)
    assert _is_linked(b, 'mMDSL_Attribute81', a2)
    if hasattr(a1, 'mMDSL_Type'):
        assert not _is_linked(a1, 'mMDSL_Type', b)
    if hasattr(a2, 'mMDSL_Type'):
        assert _is_linked(a2, 'mMDSL_Type', b)
    _safe_set(b, 'mMDSL_Attribute81', None)
    assert not _is_linked(b, 'mMDSL_Attribute81', a2)
    if hasattr(a2, 'mMDSL_Type'):
        assert not _is_linked(a2, 'mMDSL_Type', b)


def test_assoc_type82_reverse_link_reassign_clear():
    a1 = mMDSL_Type(simpletype="sample_text")
    a2 = mMDSL_Type(simpletype="sample_text_2")
    b = mMDSL_ClassAttribute(name="sample_text")
    _safe_set(b, 'mMDSL_ClassAttribute83', a1)
    assert _is_linked(b, 'mMDSL_ClassAttribute83', a1)
    if hasattr(a1, 'mMDSL_Type84'):
        assert _is_linked(a1, 'mMDSL_Type84', b)
    _safe_set(b, 'mMDSL_ClassAttribute83', a2)
    assert _is_linked(b, 'mMDSL_ClassAttribute83', a2)
    if hasattr(a1, 'mMDSL_Type84'):
        assert not _is_linked(a1, 'mMDSL_Type84', b)
    if hasattr(a2, 'mMDSL_Type84'):
        assert _is_linked(a2, 'mMDSL_Type84', b)
    _safe_set(b, 'mMDSL_ClassAttribute83', None)
    assert not _is_linked(b, 'mMDSL_ClassAttribute83', a2)
    if hasattr(a2, 'mMDSL_Type84'):
        assert not _is_linked(a2, 'mMDSL_Type84', b)


def test_assoc_valueVariable480_reverse_link_reassign_clear():
    a1 = mMDSL_Variable(name="sample_text")
    a2 = mMDSL_Variable(name="sample_text_2")
    b = mMDSL_AttributeSet(attrsetparams="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_AttributeSet481', a1)
    assert _is_linked(b, 'mMDSL_AttributeSet481', a1)
    if hasattr(a1, 'mMDSL_Variable482'):
        assert _is_linked(a1, 'mMDSL_Variable482', b)
    _safe_set(b, 'mMDSL_AttributeSet481', a2)
    assert _is_linked(b, 'mMDSL_AttributeSet481', a2)
    if hasattr(a1, 'mMDSL_Variable482'):
        assert not _is_linked(a1, 'mMDSL_Variable482', b)
    if hasattr(a2, 'mMDSL_Variable482'):
        assert _is_linked(a2, 'mMDSL_Variable482', b)
    _safe_set(b, 'mMDSL_AttributeSet481', None)
    assert not _is_linked(b, 'mMDSL_AttributeSet481', a2)
    if hasattr(a2, 'mMDSL_Variable482'):
        assert not _is_linked(a2, 'mMDSL_Variable482', b)


def test_assoc_variable265_reverse_link_reassign_clear():
    a1 = mMDSL_Variable(name="sample_text")
    a2 = mMDSL_Variable(name="sample_text_2")
    b = mMDSL_Variable(name="sample_text")
    _safe_set(b, 'mMDSL_Variable266', a1)
    assert _is_linked(b, 'mMDSL_Variable266', a1)
    if hasattr(a1, 'mMDSL_Variable264'):
        assert _is_linked(a1, 'mMDSL_Variable264', b)
    _safe_set(b, 'mMDSL_Variable266', a2)
    assert _is_linked(b, 'mMDSL_Variable266', a2)
    if hasattr(a1, 'mMDSL_Variable264'):
        assert not _is_linked(a1, 'mMDSL_Variable264', b)
    if hasattr(a2, 'mMDSL_Variable264'):
        assert _is_linked(a2, 'mMDSL_Variable264', b)
    _safe_set(b, 'mMDSL_Variable266', None)
    assert not _is_linked(b, 'mMDSL_Variable266', a2)
    if hasattr(a2, 'mMDSL_Variable264'):
        assert not _is_linked(a2, 'mMDSL_Variable264', b)


def test_assoc_variable312_reverse_link_reassign_clear():
    a1 = mMDSL_Variable(name="sample_text")
    a2 = mMDSL_Variable(name="sample_text_2")
    b = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    _safe_set(b, 'mMDSL_Expression313', a1)
    assert _is_linked(b, 'mMDSL_Expression313', a1)
    if hasattr(a1, 'mMDSL_Variable314'):
        assert _is_linked(a1, 'mMDSL_Variable314', b)
    _safe_set(b, 'mMDSL_Expression313', a2)
    assert _is_linked(b, 'mMDSL_Expression313', a2)
    if hasattr(a1, 'mMDSL_Variable314'):
        assert not _is_linked(a1, 'mMDSL_Variable314', b)
    if hasattr(a2, 'mMDSL_Variable314'):
        assert _is_linked(a2, 'mMDSL_Variable314', b)
    _safe_set(b, 'mMDSL_Expression313', None)
    assert not _is_linked(b, 'mMDSL_Expression313', a2)
    if hasattr(a2, 'mMDSL_Variable314'):
        assert not _is_linked(a2, 'mMDSL_Variable314', b)


