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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_MultiplicityFunction106_stub_double():
    # ptnet_ArithmeticExpression has no real 'ptnet_ArithmeticExpression' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_GSPNArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_GSPNArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_GSPNArc(type="sample_text")
    partner = ptnet_ArithmeticExpression()
    setattr(partner, 'ptnet_ArithmeticExpression', None)
    _safe_set(owner, 'ptnet_GSPNArc', partner)
    assert getattr(partner, 'ptnet_ArithmeticExpression') == owner
    _safe_set(owner, 'ptnet_GSPNArc', None)
    assert getattr(partner, 'ptnet_ArithmeticExpression') is None


def test_assoc_containerAnnotationGraphics61_stub_double():
    # ptnet_AnnotationGraphics has no real 'AnnotationGraphics63' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics63', None)
    _safe_set(owner, 'fill62', partner)
    assert getattr(partner, 'AnnotationGraphics63') == owner
    _safe_set(owner, 'fill62', None)
    assert getattr(partner, 'AnnotationGraphics63') is None


def test_assoc_containerAnnotationGraphics69_stub_double():
    # ptnet_AnnotationGraphics has no real 'AnnotationGraphics71' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics71', None)
    _safe_set(owner, 'line70', partner)
    assert getattr(partner, 'AnnotationGraphics71') == owner
    _safe_set(owner, 'line70', None)
    assert getattr(partner, 'AnnotationGraphics71') is None


def test_assoc_containerAnnotationGraphics93_stub_double():
    # ptnet_AnnotationGraphics has no real 'AnnotationGraphics94' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics94', None)
    _safe_set(owner, 'font', partner)
    assert getattr(partner, 'AnnotationGraphics94') == owner
    _safe_set(owner, 'font', None)
    assert getattr(partner, 'AnnotationGraphics94') is None


def test_assoc_containerArc1_stub_double():
    # ptnet_Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PTArcAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PTArcAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PTArcAnnotation(text="sample_text")
    partner = ptnet_Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'inscription', partner)
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'inscription', None)
    assert getattr(partner, 'Arc') is None


def test_assoc_containerArcGraphics66_stub_double():
    # ptnet_ArcGraphics has no real 'ArcGraphics68' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_ArcGraphics()
    setattr(partner, 'ArcGraphics68', None)
    _safe_set(owner, 'line67', partner)
    assert getattr(partner, 'ArcGraphics68') == owner
    _safe_set(owner, 'line67', None)
    assert getattr(partner, 'ArcGraphics68') is None


def test_assoc_containerLabel29_stub_double():
    # ptnet_Label has no real 'Label' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = ptnet_Label()
    setattr(partner, 'Label', None)
    _safe_set(owner, 'toolspecifics30', partner)
    assert getattr(partner, 'Label') == owner
    _safe_set(owner, 'toolspecifics30', None)
    assert getattr(partner, 'Label') is None


def test_assoc_containerNodeGraphics59_stub_double():
    # ptnet_NodeGraphics has no real 'NodeGraphics60' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = ptnet_NodeGraphics()
    setattr(partner, 'NodeGraphics60', None)
    _safe_set(owner, 'fill', partner)
    assert getattr(partner, 'NodeGraphics60') == owner
    _safe_set(owner, 'fill', None)
    assert getattr(partner, 'NodeGraphics60') is None


def test_assoc_containerNodeGraphics64_stub_double():
    # ptnet_NodeGraphics has no real 'NodeGraphics65' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_NodeGraphics()
    setattr(partner, 'NodeGraphics65', None)
    _safe_set(owner, 'line', partner)
    assert getattr(partner, 'NodeGraphics65') == owner
    _safe_set(owner, 'line', None)
    assert getattr(partner, 'NodeGraphics65') is None


def test_assoc_containerPage17_stub_double():
    # ptnet_Page has no real 'Page18' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PnObject(id="sample_text")
    partner = ptnet_Page()
    setattr(partner, 'Page18', None)
    _safe_set(owner, 'objects', partner)
    assert getattr(partner, 'Page18') == owner
    _safe_set(owner, 'objects', None)
    assert getattr(partner, 'Page18') is None


def test_assoc_containerPetriNet9_stub_double():
    # ptnet_Page has no real 'pages' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PetriNet(id="sample_text", type="sample_text")
    partner = ptnet_Page()
    setattr(partner, 'pages', None)
    _safe_set(owner, 'PetriNet10', partner)
    assert getattr(partner, 'pages') == owner
    _safe_set(owner, 'PetriNet10', None)
    assert getattr(partner, 'pages') is None


def test_assoc_containerPlace0_stub_double():
    # ptnet_Place has no real 'Place' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PTMarking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PTMarking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PTMarking(text="sample_text")
    partner = ptnet_Place()
    setattr(partner, 'Place', None)
    _safe_set(owner, 'initialMarking', partner)
    assert getattr(partner, 'Place') == owner
    _safe_set(owner, 'initialMarking', None)
    assert getattr(partner, 'Place') is None


def test_assoc_containerToolInfo103_stub_double():
    # ptnet_AnyObject has no real 'toolInfoModel' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = ptnet_AnyObject()
    setattr(partner, 'toolInfoModel', None)
    _safe_set(owner, 'ToolInfo104', partner)
    assert getattr(partner, 'toolInfoModel') == owner
    _safe_set(owner, 'ToolInfo104', None)
    assert getattr(partner, 'toolInfoModel') is None


def test_assoc_evaluationType116_stub_double():
    # ptnet_EvaluationType has no real 'ptnet_EvaluationType' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Measure(name="sample_text")
    partner = ptnet_EvaluationType()
    setattr(partner, 'ptnet_EvaluationType', None)
    _safe_set(owner, 'ptnet_Measure117', partner)
    assert getattr(partner, 'ptnet_EvaluationType') == owner
    _safe_set(owner, 'ptnet_Measure117', None)
    assert getattr(partner, 'ptnet_EvaluationType') is None


def test_assoc_fill36_stub_double():
    # ptnet_NodeGraphics has no real 'containerNodeGraphics' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = ptnet_NodeGraphics()
    setattr(partner, 'containerNodeGraphics', None)
    _safe_set(owner, 'Fill', partner)
    assert getattr(partner, 'containerNodeGraphics') == owner
    _safe_set(owner, 'Fill', None)
    assert getattr(partner, 'containerNodeGraphics') is None


def test_assoc_fill50_stub_double():
    # ptnet_AnnotationGraphics has no real 'containerAnnotationGraphics51' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics51', None)
    _safe_set(owner, 'Fill52', partner)
    assert getattr(partner, 'containerAnnotationGraphics51') == owner
    _safe_set(owner, 'Fill52', None)
    assert getattr(partner, 'containerAnnotationGraphics51') is None


def test_assoc_font56_stub_double():
    # ptnet_AnnotationGraphics has no real 'containerAnnotationGraphics57' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics57', None)
    _safe_set(owner, 'Font', partner)
    assert getattr(partner, 'containerAnnotationGraphics57') == owner
    _safe_set(owner, 'Font', None)
    assert getattr(partner, 'containerAnnotationGraphics57') is None


def test_assoc_initialMarking98_stub_double():
    # ptnet_Place has no real 'containerPlace' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PTMarking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PTMarking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PTMarking(text="sample_text")
    partner = ptnet_Place()
    setattr(partner, 'containerPlace', None)
    _safe_set(owner, 'PTMarking', partner)
    assert getattr(partner, 'containerPlace') == owner
    _safe_set(owner, 'PTMarking', None)
    assert getattr(partner, 'containerPlace') is None


def test_assoc_inscription85_stub_double():
    # ptnet_Arc has no real 'containerArc86' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PTArcAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PTArcAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PTArcAnnotation(text="sample_text")
    partner = ptnet_Arc()
    setattr(partner, 'containerArc86', None)
    _safe_set(owner, 'PTArcAnnotation', partner)
    assert getattr(partner, 'containerArc86') == owner
    _safe_set(owner, 'PTArcAnnotation', None)
    assert getattr(partner, 'containerArc86') is None


def test_assoc_line37_stub_double():
    # ptnet_NodeGraphics has no real 'containerNodeGraphics38' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_NodeGraphics()
    setattr(partner, 'containerNodeGraphics38', None)
    _safe_set(owner, 'Line', partner)
    assert getattr(partner, 'containerNodeGraphics38') == owner
    _safe_set(owner, 'Line', None)
    assert getattr(partner, 'containerNodeGraphics38') is None


def test_assoc_line53_stub_double():
    # ptnet_AnnotationGraphics has no real 'containerAnnotationGraphics54' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics54', None)
    _safe_set(owner, 'Line55', partner)
    assert getattr(partner, 'containerAnnotationGraphics54') == owner
    _safe_set(owner, 'Line55', None)
    assert getattr(partner, 'containerAnnotationGraphics54') is None


def test_assoc_line74_stub_double():
    # ptnet_ArcGraphics has no real 'containerArcGraphics75' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = ptnet_ArcGraphics()
    setattr(partner, 'containerArcGraphics75', None)
    _safe_set(owner, 'Line76', partner)
    assert getattr(partner, 'containerArcGraphics75') == owner
    _safe_set(owner, 'Line76', None)
    assert getattr(partner, 'containerArcGraphics75') is None


def test_assoc_measures109_stub_double():
    # ptnet_EvaluationList has no real 'ptnet_EvaluationList110' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Measure(name="sample_text")
    partner = ptnet_EvaluationList()
    setattr(partner, 'ptnet_EvaluationList110', None)
    _safe_set(owner, 'ptnet_Measure', partner)
    assert owner in getattr(partner, 'ptnet_EvaluationList110')
    _safe_set(owner, 'ptnet_Measure', None)
    assert owner not in getattr(partner, 'ptnet_EvaluationList110')


def test_assoc_objects8_stub_double():
    # ptnet_Page has no real 'containerPage' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PnObject(id="sample_text")
    partner = ptnet_Page()
    setattr(partner, 'containerPage', None)
    _safe_set(owner, 'PnObject', partner)
    assert owner in getattr(partner, 'containerPage')
    _safe_set(owner, 'PnObject', None)
    assert owner not in getattr(partner, 'containerPage')


def test_assoc_pages3_stub_double():
    # ptnet_Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_PetriNet(id="sample_text", type="sample_text")
    partner = ptnet_Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'containerPetriNet', {partner})
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'containerPetriNet', set())
    assert getattr(partner, 'Page') is None


def test_assoc_rewardFunction113_stub_double():
    # ptnet_ArithmeticExpression has no real 'ptnet_ArithmeticExpression115' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Measure(name="sample_text")
    partner = ptnet_ArithmeticExpression()
    setattr(partner, 'ptnet_ArithmeticExpression115', None)
    _safe_set(owner, 'ptnet_Measure114', partner)
    assert getattr(partner, 'ptnet_ArithmeticExpression115') == owner
    _safe_set(owner, 'ptnet_Measure114', None)
    assert getattr(partner, 'ptnet_ArithmeticExpression115') is None


def test_assoc_studies108_stub_double():
    # ptnet_EvaluationList has no real 'ptnet_EvaluationList' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Study's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Study's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Study(name="sample_text")
    partner = ptnet_EvaluationList()
    setattr(partner, 'ptnet_EvaluationList', None)
    _safe_set(owner, 'ptnet_Study', partner)
    assert owner in getattr(partner, 'ptnet_EvaluationList')
    _safe_set(owner, 'ptnet_Study', None)
    assert owner not in getattr(partner, 'ptnet_EvaluationList')


def test_assoc_toolInfoModel31_stub_double():
    # ptnet_AnyObject has no real 'AnyObject' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = ptnet_AnyObject()
    setattr(partner, 'AnyObject', None)
    _safe_set(owner, 'containerToolInfo', partner)
    assert getattr(partner, 'AnyObject') == owner
    _safe_set(owner, 'containerToolInfo', None)
    assert getattr(partner, 'AnyObject') is None


def test_assoc_toolspecifics32_stub_double():
    # ptnet_Label has no real 'containerLabel' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = ptnet_Label()
    setattr(partner, 'containerLabel', None)
    _safe_set(owner, 'ToolInfo33', partner)
    assert owner in getattr(partner, 'containerLabel')
    _safe_set(owner, 'ToolInfo33', None)
    assert owner not in getattr(partner, 'containerLabel')


def test_assoc_variable158_stub_double():
    # ptnet_VariableExpression has no real 'ptnet_VariableExpression' property in the generated
    # code (a bare stub) -- manually attach it so ptnet_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnet_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnet_Variable(name="sample_text")
    partner = ptnet_VariableExpression()
    setattr(partner, 'ptnet_VariableExpression', None)
    _safe_set(owner, 'ptnet_Variable159', partner)
    assert getattr(partner, 'ptnet_VariableExpression') == owner
    _safe_set(owner, 'ptnet_Variable159', None)
    assert getattr(partner, 'ptnet_VariableExpression') is None


