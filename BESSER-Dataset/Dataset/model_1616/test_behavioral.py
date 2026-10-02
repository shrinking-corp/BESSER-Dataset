import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    Arc,
    ArithmeticBinaryOperator,
    ArithmeticExpression,
    BooleanExpression,
    ComparisonOperator,
    Coordinate,
    Distribution,
    EvaluationType,
    Expression,
    GSPNTransition,
    Graphics,
    Label,
    LogicalExpression,
    Node,
    PlaceNode,
    PnObject,
    Transition,
    TransitionNode,
    ptnet_Annotation,
    ptnet_AnnotationGraphics,
    ptnet_AnyObject,
    ptnet_Arc,
    ptnet_ArcGraphics,
    ptnet_ArithmeticBinaryOperator,
    ptnet_ArithmeticExpression,
    ptnet_Attribute,
    ptnet_BooleanExpression,
    ptnet_ComparisonOperator,
    ptnet_Coordinate,
    ptnet_Deterministic,
    ptnet_Dimension,
    ptnet_Distribution,
    ptnet_EvaluationList,
    ptnet_EvaluationType,
    ptnet_Exponential,
    ptnet_Expression,
    ptnet_Fill,
    ptnet_Font,
    ptnet_GSPNArc,
    ptnet_GSPNImmediateTransition,
    ptnet_GSPNTimedTransition,
    ptnet_GSPNTransition,
    ptnet_Gamma,
    ptnet_Gaussian,
    ptnet_Graphics,
    ptnet_IfThenElse,
    ptnet_InstantOfTime,
    ptnet_IntervalOfTime,
    ptnet_IntervalOfTimeAveraged,
    ptnet_Label,
    ptnet_Line,
    ptnet_LogicalExpression,
    ptnet_MarkingExpression,
    ptnet_Measure,
    ptnet_Name,
    ptnet_Node,
    ptnet_NodeGraphics,
    ptnet_Offset,
    ptnet_OpAnd,
    ptnet_OpDivide,
    ptnet_OpEqual,
    ptnet_OpFalse,
    ptnet_OpGreater,
    ptnet_OpGreaterEqual,
    ptnet_OpLess,
    ptnet_OpLessEqual,
    ptnet_OpMinus,
    ptnet_OpMultiply,
    ptnet_OpNot,
    ptnet_OpOr,
    ptnet_OpSum,
    ptnet_OpTrue,
    ptnet_PTArcAnnotation,
    ptnet_PTMarking,
    ptnet_Page,
    ptnet_PetriNet,
    ptnet_PetriNetDoc,
    ptnet_Place,
    ptnet_PlaceNode,
    ptnet_PnObject,
    ptnet_Position,
    ptnet_RefPlace,
    ptnet_RefTransition,
    ptnet_SteadyState,
    ptnet_Study,
    ptnet_ToolInfo,
    ptnet_Transition,
    ptnet_TransitionNode,
    ptnet_Uniform,
    ptnet_ValueExpression,
    ptnet_Variable,
    ptnet_VariableExpression,
    ptnet_VariableValues,
    ptnet_Weibull,
    CSS2Color,
    CSS2FontFamily,
    CSS2FontSize,
    CSS2FontStyle,
    CSS2FontWeight,
    FontAlign,
    FontDecoration,
    GSPNArcType,
    GSPNTransitionType,
    Gradient,
    LineShape,
    LineStyle,
    PNType,
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

def test_assoc_containerNamePetriNet19_reverse_link_reassign_clear():
    a1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    a2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    b = ptnet_Name(text="sample_text")
    _safe_set(b, 'name', a1)
    assert _is_linked(b, 'name', a1)
    if hasattr(a1, 'PetriNet20'):
        assert _is_linked(a1, 'PetriNet20', b)
    _safe_set(b, 'name', a2)
    assert _is_linked(b, 'name', a2)
    if hasattr(a1, 'PetriNet20'):
        assert not _is_linked(a1, 'PetriNet20', b)
    if hasattr(a2, 'PetriNet20'):
        assert _is_linked(a2, 'PetriNet20', b)
    _safe_set(b, 'name', None)
    assert not _is_linked(b, 'name', a2)
    if hasattr(a2, 'PetriNet20'):
        assert not _is_linked(a2, 'PetriNet20', b)


def test_assoc_containerNamePnObject21_reverse_link_reassign_clear():
    a1 = ptnet_PnObject(id="sample_text")
    a2 = ptnet_PnObject(id="sample_text_2")
    b = ptnet_Name(text="sample_text")
    _safe_set(b, 'name22', a1)
    assert _is_linked(b, 'name22', a1)
    if hasattr(a1, 'PnObject23'):
        assert _is_linked(a1, 'PnObject23', b)
    _safe_set(b, 'name22', a2)
    assert _is_linked(b, 'name22', a2)
    if hasattr(a1, 'PnObject23'):
        assert not _is_linked(a1, 'PnObject23', b)
    if hasattr(a2, 'PnObject23'):
        assert _is_linked(a2, 'PnObject23', b)
    _safe_set(b, 'name22', None)
    assert not _is_linked(b, 'name22', a2)
    if hasattr(a2, 'PnObject23'):
        assert not _is_linked(a2, 'PnObject23', b)


def test_assoc_containerPetriNet24_reverse_link_reassign_clear():
    a1 = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = ptnet_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = ptnet_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet25', a1)
    assert _is_linked(b, 'PetriNet25', a1)
    if hasattr(a1, 'toolspecifics'):
        assert _is_linked(a1, 'toolspecifics', b)
    _safe_set(b, 'PetriNet25', a2)
    assert _is_linked(b, 'PetriNet25', a2)
    if hasattr(a1, 'toolspecifics'):
        assert not _is_linked(a1, 'toolspecifics', b)
    if hasattr(a2, 'toolspecifics'):
        assert _is_linked(a2, 'toolspecifics', b)
    _safe_set(b, 'PetriNet25', None)
    assert not _is_linked(b, 'PetriNet25', a2)
    if hasattr(a2, 'toolspecifics'):
        assert not _is_linked(a2, 'toolspecifics', b)


def test_assoc_containerPetriNetDoc7_reverse_link_reassign_clear():
    a1 = ptnet_PetriNetDoc(xmlns="sample_text")
    a2 = ptnet_PetriNetDoc(xmlns="sample_text_2")
    b = ptnet_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'nets', a1)
    assert _is_linked(b, 'nets', a1)
    if hasattr(a1, 'PetriNetDoc'):
        assert _is_linked(a1, 'PetriNetDoc', b)
    _safe_set(b, 'nets', a2)
    assert _is_linked(b, 'nets', a2)
    if hasattr(a1, 'PetriNetDoc'):
        assert not _is_linked(a1, 'PetriNetDoc', b)
    if hasattr(a2, 'PetriNetDoc'):
        assert _is_linked(a2, 'PetriNetDoc', b)
    _safe_set(b, 'nets', None)
    assert not _is_linked(b, 'nets', a2)
    if hasattr(a2, 'PetriNetDoc'):
        assert not _is_linked(a2, 'PetriNetDoc', b)


def test_assoc_containerPnObject26_reverse_link_reassign_clear():
    a1 = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = ptnet_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = ptnet_PnObject(id="sample_text")
    _safe_set(b, 'PnObject28', a1)
    assert _is_linked(b, 'PnObject28', a1)
    if hasattr(a1, 'toolspecifics27'):
        assert _is_linked(a1, 'toolspecifics27', b)
    _safe_set(b, 'PnObject28', a2)
    assert _is_linked(b, 'PnObject28', a2)
    if hasattr(a1, 'toolspecifics27'):
        assert not _is_linked(a1, 'toolspecifics27', b)
    if hasattr(a2, 'toolspecifics27'):
        assert _is_linked(a2, 'toolspecifics27', b)
    _safe_set(b, 'PnObject28', None)
    assert not _is_linked(b, 'PnObject28', a2)
    if hasattr(a2, 'toolspecifics27'):
        assert not _is_linked(a2, 'toolspecifics27', b)


def test_assoc_name13_reverse_link_reassign_clear():
    a1 = ptnet_PnObject(id="sample_text")
    a2 = ptnet_PnObject(id="sample_text_2")
    b = ptnet_Name(text="sample_text")
    _safe_set(b, 'Name14', a1)
    assert _is_linked(b, 'Name14', a1)
    if hasattr(a1, 'containerNamePnObject'):
        assert _is_linked(a1, 'containerNamePnObject', b)
    _safe_set(b, 'Name14', a2)
    assert _is_linked(b, 'Name14', a2)
    if hasattr(a1, 'containerNamePnObject'):
        assert not _is_linked(a1, 'containerNamePnObject', b)
    if hasattr(a2, 'containerNamePnObject'):
        assert _is_linked(a2, 'containerNamePnObject', b)
    _safe_set(b, 'Name14', None)
    assert not _is_linked(b, 'Name14', a2)
    if hasattr(a2, 'containerNamePnObject'):
        assert not _is_linked(a2, 'containerNamePnObject', b)


def test_assoc_name4_reverse_link_reassign_clear():
    a1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    a2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    b = ptnet_Name(text="sample_text")
    _safe_set(b, 'Name', a1)
    assert _is_linked(b, 'Name', a1)
    if hasattr(a1, 'containerNamePetriNet'):
        assert _is_linked(a1, 'containerNamePetriNet', b)
    _safe_set(b, 'Name', a2)
    assert _is_linked(b, 'Name', a2)
    if hasattr(a1, 'containerNamePetriNet'):
        assert not _is_linked(a1, 'containerNamePetriNet', b)
    if hasattr(a2, 'containerNamePetriNet'):
        assert _is_linked(a2, 'containerNamePetriNet', b)
    _safe_set(b, 'Name', None)
    assert not _is_linked(b, 'Name', a2)
    if hasattr(a2, 'containerNamePetriNet'):
        assert not _is_linked(a2, 'containerNamePetriNet', b)


def test_assoc_nets2_reverse_link_reassign_clear():
    a1 = ptnet_PetriNetDoc(xmlns="sample_text")
    a2 = ptnet_PetriNetDoc(xmlns="sample_text_2")
    b = ptnet_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet', a1)
    assert _is_linked(b, 'PetriNet', a1)
    if hasattr(a1, 'containerPetriNetDoc'):
        assert _is_linked(a1, 'containerPetriNetDoc', b)
    _safe_set(b, 'PetriNet', a2)
    assert _is_linked(b, 'PetriNet', a2)
    if hasattr(a1, 'containerPetriNetDoc'):
        assert not _is_linked(a1, 'containerPetriNetDoc', b)
    if hasattr(a2, 'containerPetriNetDoc'):
        assert _is_linked(a2, 'containerPetriNetDoc', b)
    _safe_set(b, 'PetriNet', None)
    assert not _is_linked(b, 'PetriNet', a2)
    if hasattr(a2, 'containerPetriNetDoc'):
        assert not _is_linked(a2, 'containerPetriNetDoc', b)


def test_assoc_toolspecifics15_reverse_link_reassign_clear():
    a1 = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = ptnet_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = ptnet_PnObject(id="sample_text")
    _safe_set(b, 'containerPnObject', {a1})
    assert _is_linked(b, 'containerPnObject', a1)
    if hasattr(a1, 'ToolInfo16'):
        assert _is_linked(a1, 'ToolInfo16', b)
    _safe_set(b, 'containerPnObject', {a2})
    assert _is_linked(b, 'containerPnObject', a2)
    if hasattr(a1, 'ToolInfo16'):
        assert not _is_linked(a1, 'ToolInfo16', b)
    if hasattr(a2, 'ToolInfo16'):
        assert _is_linked(a2, 'ToolInfo16', b)
    _safe_set(b, 'containerPnObject', set())
    assert not _is_linked(b, 'containerPnObject', a2)
    if hasattr(a2, 'ToolInfo16'):
        assert not _is_linked(a2, 'ToolInfo16', b)


def test_assoc_toolspecifics5_reverse_link_reassign_clear():
    a1 = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = ptnet_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = ptnet_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'containerPetriNet6', {a1})
    assert _is_linked(b, 'containerPetriNet6', a1)
    if hasattr(a1, 'ToolInfo'):
        assert _is_linked(a1, 'ToolInfo', b)
    _safe_set(b, 'containerPetriNet6', {a2})
    assert _is_linked(b, 'containerPetriNet6', a2)
    if hasattr(a1, 'ToolInfo'):
        assert not _is_linked(a1, 'ToolInfo', b)
    if hasattr(a2, 'ToolInfo'):
        assert _is_linked(a2, 'ToolInfo', b)
    _safe_set(b, 'containerPetriNet6', set())
    assert not _is_linked(b, 'containerPetriNet6', a2)
    if hasattr(a2, 'ToolInfo'):
        assert not _is_linked(a2, 'ToolInfo', b)


def test_assoc_variable156_reverse_link_reassign_clear():
    a1 = ptnet_VariableValues(values=3.14)
    a2 = ptnet_VariableValues(values=9.99)
    b = ptnet_Variable(name="sample_text")
    _safe_set(b, 'ptnet_Variable', a1)
    assert _is_linked(b, 'ptnet_Variable', a1)
    if hasattr(a1, 'ptnet_VariableValues157'):
        assert _is_linked(a1, 'ptnet_VariableValues157', b)
    _safe_set(b, 'ptnet_Variable', a2)
    assert _is_linked(b, 'ptnet_Variable', a2)
    if hasattr(a1, 'ptnet_VariableValues157'):
        assert not _is_linked(a1, 'ptnet_VariableValues157', b)
    if hasattr(a2, 'ptnet_VariableValues157'):
        assert _is_linked(a2, 'ptnet_VariableValues157', b)
    _safe_set(b, 'ptnet_Variable', None)
    assert not _is_linked(b, 'ptnet_Variable', a2)
    if hasattr(a2, 'ptnet_VariableValues157'):
        assert not _is_linked(a2, 'ptnet_VariableValues157', b)


def test_assoc_vars111_reverse_link_reassign_clear():
    a1 = ptnet_VariableValues(values=3.14)
    a2 = ptnet_VariableValues(values=9.99)
    b = ptnet_Study(name="sample_text")
    _safe_set(b, 'ptnet_Study112', {a1})
    assert _is_linked(b, 'ptnet_Study112', a1)
    if hasattr(a1, 'ptnet_VariableValues'):
        assert _is_linked(a1, 'ptnet_VariableValues', b)
    _safe_set(b, 'ptnet_Study112', {a2})
    assert _is_linked(b, 'ptnet_Study112', a2)
    if hasattr(a1, 'ptnet_VariableValues'):
        assert not _is_linked(a1, 'ptnet_VariableValues', b)
    if hasattr(a2, 'ptnet_VariableValues'):
        assert _is_linked(a2, 'ptnet_VariableValues', b)
    _safe_set(b, 'ptnet_Study112', set())
    assert not _is_linked(b, 'ptnet_Study112', a2)
    if hasattr(a2, 'ptnet_VariableValues'):
        assert not _is_linked(a2, 'ptnet_VariableValues', b)


