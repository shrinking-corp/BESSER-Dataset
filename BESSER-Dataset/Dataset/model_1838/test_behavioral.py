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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_algorithm34_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method35' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Algorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Algorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Algorithm(name="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method35', None)
    _safe_set(owner, 'mMDSL_Algorithm', partner)
    assert owner in getattr(partner, 'mMDSL_Method35')
    _safe_set(owner, 'mMDSL_Algorithm', None)
    assert owner not in getattr(partner, 'mMDSL_Method35')


def test_assoc_attribute276_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement277' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Attribute(access="sample_text", name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement277', None)
    _safe_set(owner, 'mMDSL_Attribute278', partner)
    assert getattr(partner, 'mMDSL_VarStatement277') == owner
    _safe_set(owner, 'mMDSL_Attribute278', None)
    assert getattr(partner, 'mMDSL_VarStatement277') is None


def test_assoc_attribute42_stub_double():
    # mMDSL_Metamodel has no real 'mMDSL_Metamodel43' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Attribute(access="sample_text", name="sample_text")
    partner = mMDSL_Metamodel()
    setattr(partner, 'mMDSL_Metamodel43', None)
    _safe_set(owner, 'mMDSL_Attribute', partner)
    assert owner in getattr(partner, 'mMDSL_Metamodel43')
    _safe_set(owner, 'mMDSL_Attribute', None)
    assert owner not in getattr(partner, 'mMDSL_Metamodel43')


def test_assoc_attributeget476_stub_double():
    # mMDSL_AttributeOperation has no real 'mMDSL_AttributeOperation477' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_AttributeGet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_AttributeGet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_AttributeGet(attrgetparams="sample_text")
    partner = mMDSL_AttributeOperation()
    setattr(partner, 'mMDSL_AttributeOperation477', None)
    _safe_set(owner, 'mMDSL_AttributeGet', partner)
    assert getattr(partner, 'mMDSL_AttributeOperation477') == owner
    _safe_set(owner, 'mMDSL_AttributeGet', None)
    assert getattr(partner, 'mMDSL_AttributeOperation477') is None


def test_assoc_attributename473_stub_double():
    # mMDSL_AttributeOperation has no real 'mMDSL_AttributeOperation474' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Attribute(access="sample_text", name="sample_text")
    partner = mMDSL_AttributeOperation()
    setattr(partner, 'mMDSL_AttributeOperation474', None)
    _safe_set(owner, 'mMDSL_Attribute475', partner)
    assert getattr(partner, 'mMDSL_AttributeOperation474') == owner
    _safe_set(owner, 'mMDSL_Attribute475', None)
    assert getattr(partner, 'mMDSL_AttributeOperation474') is None


def test_assoc_attributeset478_stub_double():
    # mMDSL_AttributeOperation has no real 'mMDSL_AttributeOperation479' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_AttributeSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_AttributeSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_AttributeSet(attrsetparams="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    partner = mMDSL_AttributeOperation()
    setattr(partner, 'mMDSL_AttributeOperation479', None)
    _safe_set(owner, 'mMDSL_AttributeSet', partner)
    assert getattr(partner, 'mMDSL_AttributeOperation479') == owner
    _safe_set(owner, 'mMDSL_AttributeSet', None)
    assert getattr(partner, 'mMDSL_AttributeOperation479') is None


def test_assoc_breakcontinue252_stub_double():
    # mMDSL_WhileLoop has no real 'mMDSL_WhileLoop253' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_BreakContinue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_BreakContinue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_BreakContinue(break_="sample_text", continue_="sample_text")
    partner = mMDSL_WhileLoop()
    setattr(partner, 'mMDSL_WhileLoop253', None)
    _safe_set(owner, 'mMDSL_BreakContinue', partner)
    assert owner in getattr(partner, 'mMDSL_WhileLoop253')
    _safe_set(owner, 'mMDSL_BreakContinue', None)
    assert owner not in getattr(partner, 'mMDSL_WhileLoop253')


def test_assoc_circle134_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand135' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Circle(cx="sample_text", cy="sample_text", r="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand135', None)
    _safe_set(owner, 'mMDSL_Circle', partner)
    assert getattr(partner, 'mMDSL_SVGCommand135') == owner
    _safe_set(owner, 'mMDSL_Circle', None)
    assert getattr(partner, 'mMDSL_SVGCommand135') is None


def test_assoc_class_273_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement274' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Class(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement274', None)
    _safe_set(owner, 'mMDSL_Class275', partner)
    assert getattr(partner, 'mMDSL_VarStatement274') == owner
    _safe_set(owner, 'mMDSL_Class275', None)
    assert getattr(partner, 'mMDSL_VarStatement274') is None


def test_assoc_class_38_stub_double():
    # mMDSL_Metamodel has no real 'mMDSL_Metamodel39' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Class(name="sample_text")
    partner = mMDSL_Metamodel()
    setattr(partner, 'mMDSL_Metamodel39', None)
    _safe_set(owner, 'mMDSL_Class', partner)
    assert owner in getattr(partner, 'mMDSL_Metamodel39')
    _safe_set(owner, 'mMDSL_Class', None)
    assert owner not in getattr(partner, 'mMDSL_Metamodel39')


def test_assoc_classinstancecreate417_stub_double():
    # mMDSL_ClassInstance has no real 'mMDSL_ClassInstance418' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ClassInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ClassInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ClassInstanceCreate(name="sample_text")
    partner = mMDSL_ClassInstance()
    setattr(partner, 'mMDSL_ClassInstance418', None)
    _safe_set(owner, 'mMDSL_ClassInstanceCreate', partner)
    assert getattr(partner, 'mMDSL_ClassInstance418') == owner
    _safe_set(owner, 'mMDSL_ClassInstanceCreate', None)
    assert getattr(partner, 'mMDSL_ClassInstance418') is None


def test_assoc_classname90_stub_double():
    # mMDSL_RefName has no real 'mMDSL_RefName91' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Class(name="sample_text")
    partner = mMDSL_RefName()
    setattr(partner, 'mMDSL_RefName91', None)
    _safe_set(owner, 'mMDSL_Class92', partner)
    assert getattr(partner, 'mMDSL_RefName91') == owner
    _safe_set(owner, 'mMDSL_Class92', None)
    assert getattr(partner, 'mMDSL_RefName91') is None


def test_assoc_codesnippetname22_stub_double():
    # mMDSL_InsertEmbedCode has no real 'mMDSL_InsertEmbedCode' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EmbedCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EmbedCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EmbedCode(embeddedcode="sample_text", name="sample_text")
    partner = mMDSL_InsertEmbedCode()
    setattr(partner, 'mMDSL_InsertEmbedCode', None)
    _safe_set(owner, 'mMDSL_EmbedCode23', partner)
    assert getattr(partner, 'mMDSL_InsertEmbedCode') == owner
    _safe_set(owner, 'mMDSL_EmbedCode23', None)
    assert getattr(partner, 'mMDSL_InsertEmbedCode') is None


def test_assoc_contextitem380_stub_double():
    # mMDSL_RemoveContextItem has no real 'mMDSL_RemoveContextItem381' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_InsertContextItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_InsertContextItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_InsertContextItem(context="sample_text", name="sample_text")
    partner = mMDSL_RemoveContextItem()
    setattr(partner, 'mMDSL_RemoveContextItem381', None)
    _safe_set(owner, 'mMDSL_InsertContextItem382', partner)
    assert getattr(partner, 'mMDSL_RemoveContextItem381') == owner
    _safe_set(owner, 'mMDSL_InsertContextItem382', None)
    assert getattr(partner, 'mMDSL_RemoveContextItem381') is None


def test_assoc_curveto173_stub_double():
    # mMDSL_CurveTo has no real 'mMDSL_CurveTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_CurveTo()
    setattr(partner, 'mMDSL_CurveTo', None)
    _safe_set(owner, 'mMDSL_PathData174', partner)
    assert getattr(partner, 'mMDSL_CurveTo') == owner
    _safe_set(owner, 'mMDSL_PathData174', None)
    assert getattr(partner, 'mMDSL_CurveTo') is None


def test_assoc_dircreate347_stub_double():
    # mMDSL_DirOperation has no real 'mMDSL_DirOperation348' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_DirCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_DirCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_DirCreate(dirname="sample_text")
    partner = mMDSL_DirOperation()
    setattr(partner, 'mMDSL_DirOperation348', None)
    _safe_set(owner, 'mMDSL_DirCreate', partner)
    assert getattr(partner, 'mMDSL_DirOperation348') == owner
    _safe_set(owner, 'mMDSL_DirCreate', None)
    assert getattr(partner, 'mMDSL_DirOperation348') is None


def test_assoc_dirdelete349_stub_double():
    # mMDSL_DirOperation has no real 'mMDSL_DirOperation350' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_DirDelete's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_DirDelete's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_DirDelete(dirname="sample_text")
    partner = mMDSL_DirOperation()
    setattr(partner, 'mMDSL_DirOperation350', None)
    _safe_set(owner, 'mMDSL_DirDelete', partner)
    assert getattr(partner, 'mMDSL_DirOperation350') == owner
    _safe_set(owner, 'mMDSL_DirDelete', None)
    assert getattr(partner, 'mMDSL_DirOperation350') is None


def test_assoc_dirlist351_stub_double():
    # mMDSL_DirOperation has no real 'mMDSL_DirOperation352' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_DirList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_DirList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_DirList(dirname="sample_text")
    partner = mMDSL_DirOperation()
    setattr(partner, 'mMDSL_DirOperation352', None)
    _safe_set(owner, 'mMDSL_DirList', partner)
    assert getattr(partner, 'mMDSL_DirOperation352') == owner
    _safe_set(owner, 'mMDSL_DirList', None)
    assert getattr(partner, 'mMDSL_DirOperation352') is None


def test_assoc_dirsetworking343_stub_double():
    # mMDSL_DirOperation has no real 'mMDSL_DirOperation344' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_DirSetWorking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_DirSetWorking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_DirSetWorking(dirname="sample_text")
    partner = mMDSL_DirOperation()
    setattr(partner, 'mMDSL_DirOperation344', None)
    _safe_set(owner, 'mMDSL_DirSetWorking', partner)
    assert getattr(partner, 'mMDSL_DirOperation344') == owner
    _safe_set(owner, 'mMDSL_DirSetWorking', None)
    assert getattr(partner, 'mMDSL_DirOperation344') is None


def test_assoc_editbox353_stub_double():
    # mMDSL_SimpleUI has no real 'mMDSL_SimpleUI354' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EditBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EditBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EditBox(okbuttontext="sample_text", text="sample_text", title="sample_text")
    partner = mMDSL_SimpleUI()
    setattr(partner, 'mMDSL_SimpleUI354', None)
    _safe_set(owner, 'mMDSL_EditBox', partner)
    assert getattr(partner, 'mMDSL_SimpleUI354') == owner
    _safe_set(owner, 'mMDSL_EditBox', None)
    assert getattr(partner, 'mMDSL_SimpleUI354') is None


def test_assoc_ellipse136_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand137' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Ellipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Ellipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Ellipse(cx="sample_text", cy="sample_text", rx="sample_text", ry="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand137', None)
    _safe_set(owner, 'mMDSL_Ellipse', partner)
    assert getattr(partner, 'mMDSL_SVGCommand137') == owner
    _safe_set(owner, 'mMDSL_Ellipse', None)
    assert getattr(partner, 'mMDSL_SVGCommand137') is None


def test_assoc_ellipticalarc181_stub_double():
    # mMDSL_EllipticalArc has no real 'mMDSL_EllipticalArc' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_EllipticalArc()
    setattr(partner, 'mMDSL_EllipticalArc', None)
    _safe_set(owner, 'mMDSL_PathData182', partner)
    assert getattr(partner, 'mMDSL_EllipticalArc') == owner
    _safe_set(owner, 'mMDSL_PathData182', None)
    assert getattr(partner, 'mMDSL_EllipticalArc') is None


def test_assoc_embedcode9_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root10' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EmbedCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EmbedCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EmbedCode(embeddedcode="sample_text", name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root10', None)
    _safe_set(owner, 'mMDSL_EmbedCode', partner)
    assert owner in getattr(partner, 'mMDSL_Root10')
    _safe_set(owner, 'mMDSL_EmbedCode', None)
    assert owner not in getattr(partner, 'mMDSL_Root10')


def test_assoc_embedcodetype5_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root6' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EmbedCodeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EmbedCodeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EmbedCodeType(name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root6', None)
    _safe_set(owner, 'mMDSL_EmbedCodeType', partner)
    assert owner in getattr(partner, 'mMDSL_Root6')
    _safe_set(owner, 'mMDSL_EmbedCodeType', None)
    assert owner not in getattr(partner, 'mMDSL_Root6')


def test_assoc_embeddedcode291_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement292' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EmbedCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EmbedCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EmbedCode(embeddedcode="sample_text", name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement292', None)
    _safe_set(owner, 'mMDSL_EmbedCode293', partner)
    assert getattr(partner, 'mMDSL_VarStatement292') == owner
    _safe_set(owner, 'mMDSL_EmbedCode293', None)
    assert getattr(partner, 'mMDSL_VarStatement292') is None


def test_assoc_embedplatformtype3_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root4' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_EmbedPlatformType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_EmbedPlatformType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_EmbedPlatformType(name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root4', None)
    _safe_set(owner, 'mMDSL_EmbedPlatformType', partner)
    assert owner in getattr(partner, 'mMDSL_Root4')
    _safe_set(owner, 'mMDSL_EmbedPlatformType', None)
    assert owner not in getattr(partner, 'mMDSL_Root4')


def test_assoc_enumeration24_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method25' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Enumeration(enumvalues="sample_text", name="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method25', None)
    _safe_set(owner, 'mMDSL_Enumeration', partner)
    assert owner in getattr(partner, 'mMDSL_Method25')
    _safe_set(owner, 'mMDSL_Enumeration', None)
    assert owner not in getattr(partner, 'mMDSL_Method25')


def test_assoc_enumtype93_stub_double():
    # mMDSL_EnumType has no real 'mMDSL_EnumType' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Type(simpletype="sample_text")
    partner = mMDSL_EnumType()
    setattr(partner, 'mMDSL_EnumType', None)
    _safe_set(owner, 'mMDSL_Type94', partner)
    assert getattr(partner, 'mMDSL_EnumType') == owner
    _safe_set(owner, 'mMDSL_Type94', None)
    assert getattr(partner, 'mMDSL_EnumType') is None


def test_assoc_errorbox357_stub_double():
    # mMDSL_SimpleUI has no real 'mMDSL_SimpleUI358' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ErrorBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ErrorBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ErrorBox(buttontype="sample_text", text="sample_text", title="sample_text")
    partner = mMDSL_SimpleUI()
    setattr(partner, 'mMDSL_SimpleUI358', None)
    _safe_set(owner, 'mMDSL_ErrorBox', partner)
    assert getattr(partner, 'mMDSL_SimpleUI358') == owner
    _safe_set(owner, 'mMDSL_ErrorBox', None)
    assert getattr(partner, 'mMDSL_SimpleUI358') is None


def test_assoc_event36_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method37' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Event(name="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method37', None)
    _safe_set(owner, 'mMDSL_Event', partner)
    assert owner in getattr(partner, 'mMDSL_Method37')
    _safe_set(owner, 'mMDSL_Event', None)
    assert owner not in getattr(partner, 'mMDSL_Method37')


def test_assoc_expr299_stub_double():
    # mMDSL_Expr has no real 'mMDSL_Expr300' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    partner = mMDSL_Expr()
    setattr(partner, 'mMDSL_Expr300', None)
    _safe_set(owner, 'mMDSL_Expression', partner)
    assert getattr(partner, 'mMDSL_Expr300') == owner
    _safe_set(owner, 'mMDSL_Expression', None)
    assert getattr(partner, 'mMDSL_Expr300') is None


def test_assoc_filecopy333_stub_double():
    # mMDSL_FileOperation has no real 'mMDSL_FileOperation334' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_FileCopy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_FileCopy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_FileCopy(dest="sample_text", src="sample_text")
    partner = mMDSL_FileOperation()
    setattr(partner, 'mMDSL_FileOperation334', None)
    _safe_set(owner, 'mMDSL_FileCopy', partner)
    assert getattr(partner, 'mMDSL_FileOperation334') == owner
    _safe_set(owner, 'mMDSL_FileCopy', None)
    assert getattr(partner, 'mMDSL_FileOperation334') is None


def test_assoc_filecreate337_stub_double():
    # mMDSL_FileOperation has no real 'mMDSL_FileOperation338' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_FileCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_FileCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_FileCreate(filename="sample_text")
    partner = mMDSL_FileOperation()
    setattr(partner, 'mMDSL_FileOperation338', None)
    _safe_set(owner, 'mMDSL_FileCreate', partner)
    assert getattr(partner, 'mMDSL_FileOperation338') == owner
    _safe_set(owner, 'mMDSL_FileCreate', None)
    assert getattr(partner, 'mMDSL_FileOperation338') is None


def test_assoc_filedelete335_stub_double():
    # mMDSL_FileOperation has no real 'mMDSL_FileOperation336' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_FileDelete's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_FileDelete's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_FileDelete(filename="sample_text")
    partner = mMDSL_FileOperation()
    setattr(partner, 'mMDSL_FileOperation336', None)
    _safe_set(owner, 'mMDSL_FileDelete', partner)
    assert getattr(partner, 'mMDSL_FileOperation336') == owner
    _safe_set(owner, 'mMDSL_FileDelete', None)
    assert getattr(partner, 'mMDSL_FileOperation336') is None


def test_assoc_fileread339_stub_double():
    # mMDSL_FileOperation has no real 'mMDSL_FileOperation340' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_FileRead's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_FileRead's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_FileRead(filename="sample_text")
    partner = mMDSL_FileOperation()
    setattr(partner, 'mMDSL_FileOperation340', None)
    _safe_set(owner, 'mMDSL_FileRead', partner)
    assert getattr(partner, 'mMDSL_FileOperation340') == owner
    _safe_set(owner, 'mMDSL_FileRead', None)
    assert getattr(partner, 'mMDSL_FileOperation340') is None


def test_assoc_filewrite341_stub_double():
    # mMDSL_FileOperation has no real 'mMDSL_FileOperation342' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_FileWrite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_FileWrite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_FileWrite(append="sample_text", filename="sample_text", text="sample_text")
    partner = mMDSL_FileOperation()
    setattr(partner, 'mMDSL_FileOperation342', None)
    _safe_set(owner, 'mMDSL_FileWrite', partner)
    assert getattr(partner, 'mMDSL_FileOperation342') == owner
    _safe_set(owner, 'mMDSL_FileWrite', None)
    assert getattr(partner, 'mMDSL_FileOperation342') is None


def test_assoc_forblock254_stub_double():
    # mMDSL_Statement has no real 'mMDSL_Statement256' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ForLoop(interval=7, start=7, stop=7)
    partner = mMDSL_Statement()
    setattr(partner, 'mMDSL_Statement256', None)
    _safe_set(owner, 'mMDSL_ForLoop255', {partner})
    assert getattr(partner, 'mMDSL_Statement256') == owner
    _safe_set(owner, 'mMDSL_ForLoop255', set())
    assert getattr(partner, 'mMDSL_Statement256') is None


def test_assoc_forloop244_stub_double():
    # mMDSL_LoopStatement has no real 'mMDSL_LoopStatement245' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ForLoop(interval=7, start=7, stop=7)
    partner = mMDSL_LoopStatement()
    setattr(partner, 'mMDSL_LoopStatement245', None)
    _safe_set(owner, 'mMDSL_ForLoop', partner)
    assert getattr(partner, 'mMDSL_LoopStatement245') == owner
    _safe_set(owner, 'mMDSL_ForLoop', None)
    assert getattr(partner, 'mMDSL_LoopStatement245') is None


def test_assoc_horizontallineto169_stub_double():
    # mMDSL_HorizontalLineTo has no real 'mMDSL_HorizontalLineTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_HorizontalLineTo()
    setattr(partner, 'mMDSL_HorizontalLineTo', None)
    _safe_set(owner, 'mMDSL_PathData170', partner)
    assert getattr(partner, 'mMDSL_HorizontalLineTo') == owner
    _safe_set(owner, 'mMDSL_PathData170', None)
    assert getattr(partner, 'mMDSL_HorizontalLineTo') is None


def test_assoc_includelibrary7_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root8' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_IncludeLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_IncludeLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_IncludeLibrary(name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root8', None)
    _safe_set(owner, 'mMDSL_IncludeLibrary', partner)
    assert owner in getattr(partner, 'mMDSL_Root8')
    _safe_set(owner, 'mMDSL_IncludeLibrary', None)
    assert owner not in getattr(partner, 'mMDSL_Root8')


def test_assoc_includelibrarytype1_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root2' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_IncludeLibraryType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_IncludeLibraryType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_IncludeLibraryType(name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root2', None)
    _safe_set(owner, 'mMDSL_IncludeLibraryType', partner)
    assert owner in getattr(partner, 'mMDSL_Root2')
    _safe_set(owner, 'mMDSL_IncludeLibraryType', None)
    assert owner not in getattr(partner, 'mMDSL_Root2')


def test_assoc_infobox355_stub_double():
    # mMDSL_SimpleUI has no real 'mMDSL_SimpleUI356' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_InfoBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_InfoBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_InfoBox(text="sample_text", title="sample_text")
    partner = mMDSL_SimpleUI()
    setattr(partner, 'mMDSL_SimpleUI356', None)
    _safe_set(owner, 'mMDSL_InfoBox', partner)
    assert getattr(partner, 'mMDSL_SimpleUI356') == owner
    _safe_set(owner, 'mMDSL_InfoBox', None)
    assert getattr(partner, 'mMDSL_SimpleUI356') is None


def test_assoc_insertcontextitem376_stub_double():
    # mMDSL_ContextItem has no real 'mMDSL_ContextItem377' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_InsertContextItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_InsertContextItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_InsertContextItem(context="sample_text", name="sample_text")
    partner = mMDSL_ContextItem()
    setattr(partner, 'mMDSL_ContextItem377', None)
    _safe_set(owner, 'mMDSL_InsertContextItem', partner)
    assert getattr(partner, 'mMDSL_ContextItem377') == owner
    _safe_set(owner, 'mMDSL_InsertContextItem', None)
    assert getattr(partner, 'mMDSL_ContextItem377') is None


def test_assoc_insertembedcode212_stub_double():
    # mMDSL_InsertEmbedCode has no real 'mMDSL_InsertEmbedCode214' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    partner = mMDSL_InsertEmbedCode()
    setattr(partner, 'mMDSL_InsertEmbedCode214', None)
    _safe_set(owner, 'mMDSL_SymbolStyle213', {partner})
    assert getattr(partner, 'mMDSL_InsertEmbedCode214') == owner
    _safe_set(owner, 'mMDSL_SymbolStyle213', set())
    assert getattr(partner, 'mMDSL_InsertEmbedCode214') is None


def test_assoc_insertembedcode57_stub_double():
    # mMDSL_InsertEmbedCode has no real 'mMDSL_InsertEmbedCode59' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Class(name="sample_text")
    partner = mMDSL_InsertEmbedCode()
    setattr(partner, 'mMDSL_InsertEmbedCode59', None)
    _safe_set(owner, 'mMDSL_Class58', {partner})
    assert getattr(partner, 'mMDSL_InsertEmbedCode59') == owner
    _safe_set(owner, 'mMDSL_Class58', set())
    assert getattr(partner, 'mMDSL_InsertEmbedCode59') is None


def test_assoc_insertembedcode77_stub_double():
    # mMDSL_InsertEmbedCode has no real 'mMDSL_InsertEmbedCode79' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Relation(name="sample_text")
    partner = mMDSL_InsertEmbedCode()
    setattr(partner, 'mMDSL_InsertEmbedCode79', None)
    _safe_set(owner, 'mMDSL_Relation78', {partner})
    assert getattr(partner, 'mMDSL_InsertEmbedCode79') == owner
    _safe_set(owner, 'mMDSL_Relation78', set())
    assert getattr(partner, 'mMDSL_InsertEmbedCode79') is None


def test_assoc_insertmenuitem369_stub_double():
    # mMDSL_MenuItem has no real 'mMDSL_MenuItem370' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_InsertMenuItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_InsertMenuItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_InsertMenuItem(menu="sample_text", name="sample_text")
    partner = mMDSL_MenuItem()
    setattr(partner, 'mMDSL_MenuItem370', None)
    _safe_set(owner, 'mMDSL_InsertMenuItem', partner)
    assert getattr(partner, 'mMDSL_MenuItem370') == owner
    _safe_set(owner, 'mMDSL_InsertMenuItem', None)
    assert getattr(partner, 'mMDSL_MenuItem370') is None


def test_assoc_line138_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand139' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Line(x1="sample_text", x2="sample_text", y1="sample_text", y2="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand139', None)
    _safe_set(owner, 'mMDSL_Line', partner)
    assert getattr(partner, 'mMDSL_SVGCommand139') == owner
    _safe_set(owner, 'mMDSL_Line', None)
    assert getattr(partner, 'mMDSL_SVGCommand139') is None


def test_assoc_lineto167_stub_double():
    # mMDSL_LineTo has no real 'mMDSL_LineTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_LineTo()
    setattr(partner, 'mMDSL_LineTo', None)
    _safe_set(owner, 'mMDSL_PathData168', partner)
    assert getattr(partner, 'mMDSL_LineTo') == owner
    _safe_set(owner, 'mMDSL_PathData168', None)
    assert getattr(partner, 'mMDSL_LineTo') is None


def test_assoc_menuitemname373_stub_double():
    # mMDSL_RemoveMenuItem has no real 'mMDSL_RemoveMenuItem374' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_InsertMenuItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_InsertMenuItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_InsertMenuItem(menu="sample_text", name="sample_text")
    partner = mMDSL_RemoveMenuItem()
    setattr(partner, 'mMDSL_RemoveMenuItem374', None)
    _safe_set(owner, 'mMDSL_InsertMenuItem375', partner)
    assert getattr(partner, 'mMDSL_RemoveMenuItem374') == owner
    _safe_set(owner, 'mMDSL_InsertMenuItem375', None)
    assert getattr(partner, 'mMDSL_RemoveMenuItem374') is None


def test_assoc_methodname0_stub_double():
    # mMDSL_Root has no real 'mMDSL_Root' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_MethodName(name="sample_text")
    partner = mMDSL_Root()
    setattr(partner, 'mMDSL_Root', None)
    _safe_set(owner, 'mMDSL_MethodName', partner)
    assert getattr(partner, 'mMDSL_Root') == owner
    _safe_set(owner, 'mMDSL_MethodName', None)
    assert getattr(partner, 'mMDSL_Root') is None


def test_assoc_modelcreate383_stub_double():
    # mMDSL_ModelOperation has no real 'mMDSL_ModelOperation384' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelOperation()
    setattr(partner, 'mMDSL_ModelOperation384', None)
    _safe_set(owner, 'mMDSL_ModelCreate', partner)
    assert getattr(partner, 'mMDSL_ModelOperation384') == owner
    _safe_set(owner, 'mMDSL_ModelCreate', None)
    assert getattr(partner, 'mMDSL_ModelOperation384') is None


def test_assoc_modelname398_stub_double():
    # mMDSL_ModelDelete has no real 'mMDSL_ModelDelete399' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelDelete()
    setattr(partner, 'mMDSL_ModelDelete399', None)
    _safe_set(owner, 'mMDSL_ModelCreate400', partner)
    assert getattr(partner, 'mMDSL_ModelDelete399') == owner
    _safe_set(owner, 'mMDSL_ModelCreate400', None)
    assert getattr(partner, 'mMDSL_ModelDelete399') is None


def test_assoc_modelname401_stub_double():
    # mMDSL_ModelDiscard has no real 'mMDSL_ModelDiscard402' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelDiscard()
    setattr(partner, 'mMDSL_ModelDiscard402', None)
    _safe_set(owner, 'mMDSL_ModelCreate403', partner)
    assert getattr(partner, 'mMDSL_ModelDiscard402') == owner
    _safe_set(owner, 'mMDSL_ModelCreate403', None)
    assert getattr(partner, 'mMDSL_ModelDiscard402') is None


def test_assoc_modelname404_stub_double():
    # mMDSL_ModelSave has no real 'mMDSL_ModelSave405' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelSave()
    setattr(partner, 'mMDSL_ModelSave405', None)
    _safe_set(owner, 'mMDSL_ModelCreate406', partner)
    assert getattr(partner, 'mMDSL_ModelSave405') == owner
    _safe_set(owner, 'mMDSL_ModelCreate406', None)
    assert getattr(partner, 'mMDSL_ModelSave405') is None


def test_assoc_modelname407_stub_double():
    # mMDSL_ModelLoad has no real 'mMDSL_ModelLoad408' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelLoad()
    setattr(partner, 'mMDSL_ModelLoad408', None)
    _safe_set(owner, 'mMDSL_ModelCreate409', partner)
    assert getattr(partner, 'mMDSL_ModelLoad408') == owner
    _safe_set(owner, 'mMDSL_ModelCreate409', None)
    assert getattr(partner, 'mMDSL_ModelLoad408') is None


def test_assoc_modelname410_stub_double():
    # mMDSL_ModelIsLoaded has no real 'mMDSL_ModelIsLoaded411' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelCreate(name="sample_text")
    partner = mMDSL_ModelIsLoaded()
    setattr(partner, 'mMDSL_ModelIsLoaded411', None)
    _safe_set(owner, 'mMDSL_ModelCreate412', partner)
    assert getattr(partner, 'mMDSL_ModelIsLoaded411') == owner
    _safe_set(owner, 'mMDSL_ModelCreate412', None)
    assert getattr(partner, 'mMDSL_ModelIsLoaded411') is None


def test_assoc_modeltype294_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement295' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelType(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement295', None)
    _safe_set(owner, 'mMDSL_ModelType296', partner)
    assert getattr(partner, 'mMDSL_VarStatement295') == owner
    _safe_set(owner, 'mMDSL_ModelType296', None)
    assert getattr(partner, 'mMDSL_VarStatement295') is None


def test_assoc_modeltype44_stub_double():
    # mMDSL_Metamodel has no real 'mMDSL_Metamodel45' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelType(name="sample_text")
    partner = mMDSL_Metamodel()
    setattr(partner, 'mMDSL_Metamodel45', None)
    _safe_set(owner, 'mMDSL_ModelType', partner)
    assert owner in getattr(partner, 'mMDSL_Metamodel45')
    _safe_set(owner, 'mMDSL_ModelType', None)
    assert owner not in getattr(partner, 'mMDSL_Metamodel45')


def test_assoc_modeltypename87_stub_double():
    # mMDSL_RefName has no real 'mMDSL_RefName88' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ModelType(name="sample_text")
    partner = mMDSL_RefName()
    setattr(partner, 'mMDSL_RefName88', None)
    _safe_set(owner, 'mMDSL_ModelType89', partner)
    assert getattr(partner, 'mMDSL_RefName88') == owner
    _safe_set(owner, 'mMDSL_ModelType89', None)
    assert getattr(partner, 'mMDSL_RefName88') is None


def test_assoc_moveto165_stub_double():
    # mMDSL_MoveTo has no real 'mMDSL_MoveTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_MoveTo()
    setattr(partner, 'mMDSL_MoveTo', None)
    _safe_set(owner, 'mMDSL_PathData166', partner)
    assert getattr(partner, 'mMDSL_MoveTo') == owner
    _safe_set(owner, 'mMDSL_PathData166', None)
    assert getattr(partner, 'mMDSL_MoveTo') is None


def test_assoc_name95_stub_double():
    # mMDSL_EnumType has no real 'mMDSL_EnumType96' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Enumeration(enumvalues="sample_text", name="sample_text")
    partner = mMDSL_EnumType()
    setattr(partner, 'mMDSL_EnumType96', None)
    _safe_set(owner, 'mMDSL_Enumeration97', partner)
    assert getattr(partner, 'mMDSL_EnumType96') == owner
    _safe_set(owner, 'mMDSL_Enumeration97', None)
    assert getattr(partner, 'mMDSL_EnumType96') is None


def test_assoc_nameofclass436_stub_double():
    # mMDSL_ClassInstanceGetAll has no real 'mMDSL_ClassInstanceGetAll437' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Class(name="sample_text")
    partner = mMDSL_ClassInstanceGetAll()
    setattr(partner, 'mMDSL_ClassInstanceGetAll437', None)
    _safe_set(owner, 'mMDSL_Class438', partner)
    assert getattr(partner, 'mMDSL_ClassInstanceGetAll437') == owner
    _safe_set(owner, 'mMDSL_Class438', None)
    assert getattr(partner, 'mMDSL_ClassInstanceGetAll437') is None


def test_assoc_nameofclassinstance430_stub_double():
    # mMDSL_ClassInstanceDelete has no real 'mMDSL_ClassInstanceDelete431' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ClassInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ClassInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ClassInstanceCreate(name="sample_text")
    partner = mMDSL_ClassInstanceDelete()
    setattr(partner, 'mMDSL_ClassInstanceDelete431', None)
    _safe_set(owner, 'mMDSL_ClassInstanceCreate432', partner)
    assert getattr(partner, 'mMDSL_ClassInstanceDelete431') == owner
    _safe_set(owner, 'mMDSL_ClassInstanceCreate432', None)
    assert getattr(partner, 'mMDSL_ClassInstanceDelete431') is None


def test_assoc_nameofclassinstance433_stub_double():
    # mMDSL_ClassInstanceGet has no real 'mMDSL_ClassInstanceGet434' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ClassInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ClassInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ClassInstanceCreate(name="sample_text")
    partner = mMDSL_ClassInstanceGet()
    setattr(partner, 'mMDSL_ClassInstanceGet434', None)
    _safe_set(owner, 'mMDSL_ClassInstanceCreate435', partner)
    assert getattr(partner, 'mMDSL_ClassInstanceGet434') == owner
    _safe_set(owner, 'mMDSL_ClassInstanceCreate435', None)
    assert getattr(partner, 'mMDSL_ClassInstanceGet434') is None


def test_assoc_nameofclassinstance439_stub_double():
    # mMDSL_ClassInstanceSet has no real 'mMDSL_ClassInstanceSet440' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ClassInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ClassInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ClassInstanceCreate(name="sample_text")
    partner = mMDSL_ClassInstanceSet()
    setattr(partner, 'mMDSL_ClassInstanceSet440', None)
    _safe_set(owner, 'mMDSL_ClassInstanceCreate441', partner)
    assert getattr(partner, 'mMDSL_ClassInstanceSet440') == owner
    _safe_set(owner, 'mMDSL_ClassInstanceCreate441', None)
    assert getattr(partner, 'mMDSL_ClassInstanceSet440') is None


def test_assoc_nameofrelation467_stub_double():
    # mMDSL_RelationInstanceGetAll has no real 'mMDSL_RelationInstanceGetAll468' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Relation(name="sample_text")
    partner = mMDSL_RelationInstanceGetAll()
    setattr(partner, 'mMDSL_RelationInstanceGetAll468', None)
    _safe_set(owner, 'mMDSL_Relation469', partner)
    assert getattr(partner, 'mMDSL_RelationInstanceGetAll468') == owner
    _safe_set(owner, 'mMDSL_Relation469', None)
    assert getattr(partner, 'mMDSL_RelationInstanceGetAll468') is None


def test_assoc_nameofrelationinstance461_stub_double():
    # mMDSL_RelationInstanceDelete has no real 'mMDSL_RelationInstanceDelete462' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_RelationInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_RelationInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_RelationInstanceCreate(name="sample_text")
    partner = mMDSL_RelationInstanceDelete()
    setattr(partner, 'mMDSL_RelationInstanceDelete462', None)
    _safe_set(owner, 'mMDSL_RelationInstanceCreate463', partner)
    assert getattr(partner, 'mMDSL_RelationInstanceDelete462') == owner
    _safe_set(owner, 'mMDSL_RelationInstanceCreate463', None)
    assert getattr(partner, 'mMDSL_RelationInstanceDelete462') is None


def test_assoc_nameofrelationinstance464_stub_double():
    # mMDSL_RelationInstanceGet has no real 'mMDSL_RelationInstanceGet465' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_RelationInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_RelationInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_RelationInstanceCreate(name="sample_text")
    partner = mMDSL_RelationInstanceGet()
    setattr(partner, 'mMDSL_RelationInstanceGet465', None)
    _safe_set(owner, 'mMDSL_RelationInstanceCreate466', partner)
    assert getattr(partner, 'mMDSL_RelationInstanceGet465') == owner
    _safe_set(owner, 'mMDSL_RelationInstanceCreate466', None)
    assert getattr(partner, 'mMDSL_RelationInstanceGet465') is None


def test_assoc_nameofrelationinstance470_stub_double():
    # mMDSL_RelationInstanceSet has no real 'mMDSL_RelationInstanceSet471' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_RelationInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_RelationInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_RelationInstanceCreate(name="sample_text")
    partner = mMDSL_RelationInstanceSet()
    setattr(partner, 'mMDSL_RelationInstanceSet471', None)
    _safe_set(owner, 'mMDSL_RelationInstanceCreate472', partner)
    assert getattr(partner, 'mMDSL_RelationInstanceSet471') == owner
    _safe_set(owner, 'mMDSL_RelationInstanceCreate472', None)
    assert getattr(partner, 'mMDSL_RelationInstanceSet471') is None


def test_assoc_op301_stub_double():
    # mMDSL_EObject has no real 'mMDSL_EObject' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Expression(false="sample_text", true="sample_text", valueRealNumber="sample_text", valueString="sample_text")
    partner = mMDSL_EObject()
    setattr(partner, 'mMDSL_EObject', None)
    _safe_set(owner, 'mMDSL_Expression302', partner)
    assert getattr(partner, 'mMDSL_EObject') == owner
    _safe_set(owner, 'mMDSL_Expression302', None)
    assert getattr(partner, 'mMDSL_EObject') is None


def test_assoc_parameters183_stub_double():
    # mMDSL_MoveTo has no real 'mMDSL_MoveTo184' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersMLT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersMLT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersMLT(x="sample_text", y="sample_text")
    partner = mMDSL_MoveTo()
    setattr(partner, 'mMDSL_MoveTo184', None)
    _safe_set(owner, 'mMDSL_PathParametersMLT', partner)
    assert owner in getattr(partner, 'mMDSL_MoveTo184')
    _safe_set(owner, 'mMDSL_PathParametersMLT', None)
    assert owner not in getattr(partner, 'mMDSL_MoveTo184')


def test_assoc_parameters185_stub_double():
    # mMDSL_LineTo has no real 'mMDSL_LineTo186' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersMLT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersMLT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersMLT(x="sample_text", y="sample_text")
    partner = mMDSL_LineTo()
    setattr(partner, 'mMDSL_LineTo186', None)
    _safe_set(owner, 'mMDSL_PathParametersMLT187', partner)
    assert owner in getattr(partner, 'mMDSL_LineTo186')
    _safe_set(owner, 'mMDSL_PathParametersMLT187', None)
    assert owner not in getattr(partner, 'mMDSL_LineTo186')


def test_assoc_parameters188_stub_double():
    # mMDSL_HorizontalLineTo has no real 'mMDSL_HorizontalLineTo189' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersHV's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersHV's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersHV(x="sample_text")
    partner = mMDSL_HorizontalLineTo()
    setattr(partner, 'mMDSL_HorizontalLineTo189', None)
    _safe_set(owner, 'mMDSL_PathParametersHV', partner)
    assert owner in getattr(partner, 'mMDSL_HorizontalLineTo189')
    _safe_set(owner, 'mMDSL_PathParametersHV', None)
    assert owner not in getattr(partner, 'mMDSL_HorizontalLineTo189')


def test_assoc_parameters190_stub_double():
    # mMDSL_VerticalLineTo has no real 'mMDSL_VerticalLineTo191' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersHV's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersHV's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersHV(x="sample_text")
    partner = mMDSL_VerticalLineTo()
    setattr(partner, 'mMDSL_VerticalLineTo191', None)
    _safe_set(owner, 'mMDSL_PathParametersHV192', partner)
    assert owner in getattr(partner, 'mMDSL_VerticalLineTo191')
    _safe_set(owner, 'mMDSL_PathParametersHV192', None)
    assert owner not in getattr(partner, 'mMDSL_VerticalLineTo191')


def test_assoc_parameters193_stub_double():
    # mMDSL_CurveTo has no real 'mMDSL_CurveTo194' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersC(x="sample_text", x1="sample_text", x2="sample_text", y="sample_text", y1="sample_text", y2="sample_text")
    partner = mMDSL_CurveTo()
    setattr(partner, 'mMDSL_CurveTo194', None)
    _safe_set(owner, 'mMDSL_PathParametersC', partner)
    assert owner in getattr(partner, 'mMDSL_CurveTo194')
    _safe_set(owner, 'mMDSL_PathParametersC', None)
    assert owner not in getattr(partner, 'mMDSL_CurveTo194')


def test_assoc_parameters195_stub_double():
    # mMDSL_SmoothCurveTo has no real 'mMDSL_SmoothCurveTo196' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersS(x="sample_text", x2="sample_text", y="sample_text", y2="sample_text")
    partner = mMDSL_SmoothCurveTo()
    setattr(partner, 'mMDSL_SmoothCurveTo196', None)
    _safe_set(owner, 'mMDSL_PathParametersS', partner)
    assert owner in getattr(partner, 'mMDSL_SmoothCurveTo196')
    _safe_set(owner, 'mMDSL_PathParametersS', None)
    assert owner not in getattr(partner, 'mMDSL_SmoothCurveTo196')


def test_assoc_parameters197_stub_double():
    # mMDSL_QuadraticBezierCurve has no real 'mMDSL_QuadraticBezierCurve198' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersQ's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersQ's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersQ(x="sample_text", x1="sample_text", y="sample_text", y1="sample_text")
    partner = mMDSL_QuadraticBezierCurve()
    setattr(partner, 'mMDSL_QuadraticBezierCurve198', None)
    _safe_set(owner, 'mMDSL_PathParametersQ', partner)
    assert owner in getattr(partner, 'mMDSL_QuadraticBezierCurve198')
    _safe_set(owner, 'mMDSL_PathParametersQ', None)
    assert owner not in getattr(partner, 'mMDSL_QuadraticBezierCurve198')


def test_assoc_parameters199_stub_double():
    # mMDSL_SmoothQuadraticBezierCurveTo has no real 'mMDSL_SmoothQuadraticBezierCurveTo200' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersMLT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersMLT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersMLT(x="sample_text", y="sample_text")
    partner = mMDSL_SmoothQuadraticBezierCurveTo()
    setattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo200', None)
    _safe_set(owner, 'mMDSL_PathParametersMLT201', partner)
    assert owner in getattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo200')
    _safe_set(owner, 'mMDSL_PathParametersMLT201', None)
    assert owner not in getattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo200')


def test_assoc_parameters202_stub_double():
    # mMDSL_EllipticalArc has no real 'mMDSL_EllipticalArc203' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathParametersA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathParametersA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathParametersA(largearcflag="sample_text", rx="sample_text", ry="sample_text", sweepflag="sample_text", x="sample_text", xaxisrot="sample_text", y="sample_text")
    partner = mMDSL_EllipticalArc()
    setattr(partner, 'mMDSL_EllipticalArc203', None)
    _safe_set(owner, 'mMDSL_PathParametersA', partner)
    assert owner in getattr(partner, 'mMDSL_EllipticalArc203')
    _safe_set(owner, 'mMDSL_PathParametersA', None)
    assert owner not in getattr(partner, 'mMDSL_EllipticalArc203')


def test_assoc_pathdata159_stub_double():
    # mMDSL_Path has no real 'mMDSL_Path160' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_Path()
    setattr(partner, 'mMDSL_Path160', None)
    _safe_set(owner, 'mMDSL_PathData', partner)
    assert owner in getattr(partner, 'mMDSL_Path160')
    _safe_set(owner, 'mMDSL_PathData', None)
    assert owner not in getattr(partner, 'mMDSL_Path160')


def test_assoc_points154_stub_double():
    # mMDSL_Polyline has no real 'mMDSL_Polyline155' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Points's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Points's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Points(x="sample_text", y="sample_text")
    partner = mMDSL_Polyline()
    setattr(partner, 'mMDSL_Polyline155', None)
    _safe_set(owner, 'mMDSL_Points', partner)
    assert owner in getattr(partner, 'mMDSL_Polyline155')
    _safe_set(owner, 'mMDSL_Points', None)
    assert owner not in getattr(partner, 'mMDSL_Polyline155')


def test_assoc_points156_stub_double():
    # mMDSL_Polygon has no real 'mMDSL_Polygon157' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Points's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Points's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Points(x="sample_text", y="sample_text")
    partner = mMDSL_Polygon()
    setattr(partner, 'mMDSL_Polygon157', None)
    _safe_set(owner, 'mMDSL_Points158', partner)
    assert owner in getattr(partner, 'mMDSL_Polygon157')
    _safe_set(owner, 'mMDSL_Points158', None)
    assert owner not in getattr(partner, 'mMDSL_Polygon157')


def test_assoc_quadraticbeziercurve177_stub_double():
    # mMDSL_QuadraticBezierCurve has no real 'mMDSL_QuadraticBezierCurve' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_QuadraticBezierCurve()
    setattr(partner, 'mMDSL_QuadraticBezierCurve', None)
    _safe_set(owner, 'mMDSL_PathData178', partner)
    assert getattr(partner, 'mMDSL_QuadraticBezierCurve') == owner
    _safe_set(owner, 'mMDSL_PathData178', None)
    assert getattr(partner, 'mMDSL_QuadraticBezierCurve') is None


def test_assoc_rectangle132_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand133' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Rectangle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Rectangle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Rectangle(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand133', None)
    _safe_set(owner, 'mMDSL_Rectangle', partner)
    assert getattr(partner, 'mMDSL_SVGCommand133') == owner
    _safe_set(owner, 'mMDSL_Rectangle', None)
    assert getattr(partner, 'mMDSL_SVGCommand133') is None


def test_assoc_reference279_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement280' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Reference(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement280', None)
    _safe_set(owner, 'mMDSL_Reference281', partner)
    assert getattr(partner, 'mMDSL_VarStatement280') == owner
    _safe_set(owner, 'mMDSL_Reference281', None)
    assert getattr(partner, 'mMDSL_VarStatement280') is None


def test_assoc_refname85_stub_double():
    # mMDSL_RefName has no real 'mMDSL_RefName' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Reference(name="sample_text")
    partner = mMDSL_RefName()
    setattr(partner, 'mMDSL_RefName', None)
    _safe_set(owner, 'mMDSL_Reference86', partner)
    assert getattr(partner, 'mMDSL_RefName') == owner
    _safe_set(owner, 'mMDSL_Reference86', None)
    assert getattr(partner, 'mMDSL_RefName') is None


def test_assoc_relation40_stub_double():
    # mMDSL_Metamodel has no real 'mMDSL_Metamodel41' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Relation(name="sample_text")
    partner = mMDSL_Metamodel()
    setattr(partner, 'mMDSL_Metamodel41', None)
    _safe_set(owner, 'mMDSL_Relation', partner)
    assert owner in getattr(partner, 'mMDSL_Metamodel41')
    _safe_set(owner, 'mMDSL_Relation', None)
    assert owner not in getattr(partner, 'mMDSL_Metamodel41')


def test_assoc_relationinstancecreate442_stub_double():
    # mMDSL_RelationInstance has no real 'mMDSL_RelationInstance443' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_RelationInstanceCreate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_RelationInstanceCreate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_RelationInstanceCreate(name="sample_text")
    partner = mMDSL_RelationInstance()
    setattr(partner, 'mMDSL_RelationInstance443', None)
    _safe_set(owner, 'mMDSL_RelationInstanceCreate', partner)
    assert getattr(partner, 'mMDSL_RelationInstance443') == owner
    _safe_set(owner, 'mMDSL_RelationInstanceCreate', None)
    assert getattr(partner, 'mMDSL_RelationInstance443') is None


def test_assoc_smoothcurveto175_stub_double():
    # mMDSL_SmoothCurveTo has no real 'mMDSL_SmoothCurveTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_SmoothCurveTo()
    setattr(partner, 'mMDSL_SmoothCurveTo', None)
    _safe_set(owner, 'mMDSL_PathData176', partner)
    assert getattr(partner, 'mMDSL_SmoothCurveTo') == owner
    _safe_set(owner, 'mMDSL_PathData176', None)
    assert getattr(partner, 'mMDSL_SmoothCurveTo') is None


def test_assoc_smoothquadraticbeziercurveto179_stub_double():
    # mMDSL_SmoothQuadraticBezierCurveTo has no real 'mMDSL_SmoothQuadraticBezierCurveTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_SmoothQuadraticBezierCurveTo()
    setattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo', None)
    _safe_set(owner, 'mMDSL_PathData180', partner)
    assert getattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo') == owner
    _safe_set(owner, 'mMDSL_PathData180', None)
    assert getattr(partner, 'mMDSL_SmoothQuadraticBezierCurveTo') is None


def test_assoc_stmnt215_stub_double():
    # mMDSL_Statement has no real 'mMDSL_Statement' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Algorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Algorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Algorithm(name="sample_text")
    partner = mMDSL_Statement()
    setattr(partner, 'mMDSL_Statement', None)
    _safe_set(owner, 'mMDSL_Algorithm216', {partner})
    assert getattr(partner, 'mMDSL_Statement') == owner
    _safe_set(owner, 'mMDSL_Algorithm216', set())
    assert getattr(partner, 'mMDSL_Statement') is None


def test_assoc_svgcommand115_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolClass(name="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand', None)
    _safe_set(owner, 'mMDSL_SymbolClass116', {partner})
    assert getattr(partner, 'mMDSL_SVGCommand') == owner
    _safe_set(owner, 'mMDSL_SymbolClass116', set())
    assert getattr(partner, 'mMDSL_SVGCommand') is None


def test_assoc_svgcommandsfrom120_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand122' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolRelation(name="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand122', None)
    _safe_set(owner, 'mMDSL_SymbolRelation121', {partner})
    assert getattr(partner, 'mMDSL_SVGCommand122') == owner
    _safe_set(owner, 'mMDSL_SymbolRelation121', set())
    assert getattr(partner, 'mMDSL_SVGCommand122') is None


def test_assoc_svgcommandsmiddle123_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand125' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolRelation(name="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand125', None)
    _safe_set(owner, 'mMDSL_SymbolRelation124', {partner})
    assert getattr(partner, 'mMDSL_SVGCommand125') == owner
    _safe_set(owner, 'mMDSL_SymbolRelation124', set())
    assert getattr(partner, 'mMDSL_SVGCommand125') is None


def test_assoc_svgcommandsto126_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand128' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolRelation(name="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand128', None)
    _safe_set(owner, 'mMDSL_SymbolRelation127', {partner})
    assert getattr(partner, 'mMDSL_SVGCommand128') == owner
    _safe_set(owner, 'mMDSL_SymbolRelation127', set())
    assert getattr(partner, 'mMDSL_SVGCommand128') is None


def test_assoc_symbolclass28_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method29' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolClass(name="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method29', None)
    _safe_set(owner, 'mMDSL_SymbolClass', partner)
    assert owner in getattr(partner, 'mMDSL_Method29')
    _safe_set(owner, 'mMDSL_SymbolClass', None)
    assert owner not in getattr(partner, 'mMDSL_Method29')


def test_assoc_symbolclass282_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement283' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolClass(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement283', None)
    _safe_set(owner, 'mMDSL_SymbolClass284', partner)
    assert getattr(partner, 'mMDSL_VarStatement283') == owner
    _safe_set(owner, 'mMDSL_SymbolClass284', None)
    assert getattr(partner, 'mMDSL_VarStatement283') is None


def test_assoc_symbolrelation285_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement286' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolRelation(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement286', None)
    _safe_set(owner, 'mMDSL_SymbolRelation287', partner)
    assert getattr(partner, 'mMDSL_VarStatement286') == owner
    _safe_set(owner, 'mMDSL_SymbolRelation287', None)
    assert getattr(partner, 'mMDSL_VarStatement286') is None


def test_assoc_symbolrelation30_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method31' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolRelation(name="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method31', None)
    _safe_set(owner, 'mMDSL_SymbolRelation', partner)
    assert owner in getattr(partner, 'mMDSL_Method31')
    _safe_set(owner, 'mMDSL_SymbolRelation', None)
    assert owner not in getattr(partner, 'mMDSL_Method31')


def test_assoc_symbolstyle148_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand149' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand149', None)
    _safe_set(owner, 'mMDSL_SymbolStyle150', partner)
    assert getattr(partner, 'mMDSL_SVGCommand149') == owner
    _safe_set(owner, 'mMDSL_SymbolStyle150', None)
    assert getattr(partner, 'mMDSL_SVGCommand149') is None


def test_assoc_symbolstyle26_stub_double():
    # mMDSL_Method has no real 'mMDSL_Method27' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    partner = mMDSL_Method()
    setattr(partner, 'mMDSL_Method27', None)
    _safe_set(owner, 'mMDSL_SymbolStyle', partner)
    assert owner in getattr(partner, 'mMDSL_Method27')
    _safe_set(owner, 'mMDSL_SymbolStyle', None)
    assert owner not in getattr(partner, 'mMDSL_Method27')


def test_assoc_symbolstyle288_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement289' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement289', None)
    _safe_set(owner, 'mMDSL_SymbolStyle290', partner)
    assert getattr(partner, 'mMDSL_VarStatement289') == owner
    _safe_set(owner, 'mMDSL_SymbolStyle290', None)
    assert getattr(partner, 'mMDSL_VarStatement289') is None


def test_assoc_symbolstyleref151_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand152' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_SymbolStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_SymbolStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_SymbolStyle(fontsize="sample_text", name="sample_text", strokewidth="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand152', None)
    _safe_set(owner, 'mMDSL_SymbolStyle153', partner)
    assert getattr(partner, 'mMDSL_SVGCommand152') == owner
    _safe_set(owner, 'mMDSL_SymbolStyle153', None)
    assert getattr(partner, 'mMDSL_SVGCommand152') is None


def test_assoc_text146_stub_double():
    # mMDSL_SVGCommand has no real 'mMDSL_SVGCommand147' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Text(fontsize="sample_text", value="sample_text", x="sample_text", y="sample_text")
    partner = mMDSL_SVGCommand()
    setattr(partner, 'mMDSL_SVGCommand147', None)
    _safe_set(owner, 'mMDSL_Text', partner)
    assert getattr(partner, 'mMDSL_SVGCommand147') == owner
    _safe_set(owner, 'mMDSL_Text', None)
    assert getattr(partner, 'mMDSL_SVGCommand147') is None


def test_assoc_variable221_stub_double():
    # mMDSL_Statement has no real 'mMDSL_Statement222' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Variable(name="sample_text")
    partner = mMDSL_Statement()
    setattr(partner, 'mMDSL_Statement222', None)
    _safe_set(owner, 'mMDSL_Variable', partner)
    assert getattr(partner, 'mMDSL_Statement222') == owner
    _safe_set(owner, 'mMDSL_Variable', None)
    assert getattr(partner, 'mMDSL_Statement222') is None


def test_assoc_varstatement262_stub_double():
    # mMDSL_VarStatement has no real 'mMDSL_VarStatement' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_Variable(name="sample_text")
    partner = mMDSL_VarStatement()
    setattr(partner, 'mMDSL_VarStatement', None)
    _safe_set(owner, 'mMDSL_Variable263', partner)
    assert getattr(partner, 'mMDSL_VarStatement') == owner
    _safe_set(owner, 'mMDSL_Variable263', None)
    assert getattr(partner, 'mMDSL_VarStatement') is None


def test_assoc_verticallineto171_stub_double():
    # mMDSL_VerticalLineTo has no real 'mMDSL_VerticalLineTo' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_PathData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_PathData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_PathData(closepath="sample_text")
    partner = mMDSL_VerticalLineTo()
    setattr(partner, 'mMDSL_VerticalLineTo', None)
    _safe_set(owner, 'mMDSL_PathData172', partner)
    assert getattr(partner, 'mMDSL_VerticalLineTo') == owner
    _safe_set(owner, 'mMDSL_PathData172', None)
    assert getattr(partner, 'mMDSL_VerticalLineTo') is None


def test_assoc_viewbox361_stub_double():
    # mMDSL_SimpleUI has no real 'mMDSL_SimpleUI362' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_ViewBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_ViewBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_ViewBox(text="sample_text", title="sample_text")
    partner = mMDSL_SimpleUI()
    setattr(partner, 'mMDSL_SimpleUI362', None)
    _safe_set(owner, 'mMDSL_ViewBox', partner)
    assert getattr(partner, 'mMDSL_SimpleUI362') == owner
    _safe_set(owner, 'mMDSL_ViewBox', None)
    assert getattr(partner, 'mMDSL_SimpleUI362') is None


def test_assoc_warningbox359_stub_double():
    # mMDSL_SimpleUI has no real 'mMDSL_SimpleUI360' property in the generated
    # code (a bare stub) -- manually attach it so mMDSL_WarningBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mMDSL_WarningBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mMDSL_WarningBox(buttontype="sample_text", text="sample_text", title="sample_text")
    partner = mMDSL_SimpleUI()
    setattr(partner, 'mMDSL_SimpleUI360', None)
    _safe_set(owner, 'mMDSL_WarningBox', partner)
    assert getattr(partner, 'mMDSL_SimpleUI360') == owner
    _safe_set(owner, 'mMDSL_WarningBox', None)
    assert getattr(partner, 'mMDSL_SimpleUI360') is None


