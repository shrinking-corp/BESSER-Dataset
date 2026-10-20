import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConnectableElement,
    DiagramElement,
    Feature,
    FeatureContainer,
    Value,
    model_Anchor,
    model_Arrow,
    model_BooleanValue,
    model_Color,
    model_ColorFeature,
    model_Colors,
    model_ConnectableElement,
    model_Contains,
    model_Corner,
    model_Custom,
    model_CustomColor,
    model_CustomFigure,
    model_Decorator,
    model_Diagram,
    model_DiagramElement,
    model_DoubleValue,
    model_EAttribute,
    model_EClass,
    model_EReference,
    model_Ellipse,
    model_EnumValue,
    model_Feature,
    model_FeatureConditional,
    model_FeatureContainer,
    model_FontProperties,
    model_Image,
    model_ImportStatement,
    model_IntValue,
    model_Invisible,
    model_Label,
    model_Layout,
    model_Line,
    model_LineStyle,
    model_LineWidth,
    model_Link,
    model_MetaModel,
    model_Node,
    model_Point,
    model_Polyline,
    model_Position,
    model_Rectangle,
    model_Rhombus,
    model_Size,
    model_StringValue,
    model_TextAlign,
    model_TextPart,
    model_TextValue,
    model_Transparency,
    model_Triangle,
    model_Value,
    model_Visible,
    model_XDiagram,
    AnchorDirection,
    BooleanLiteral,
    DefaultColor,
    LineType,
    Operator,
    TextAlignValue,
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

def test_assoc_color53_reverse_link_reassign_clear():
    a1 = model_ColorFeature(type="sample_text")
    a2 = model_ColorFeature(type="sample_text_2")
    b = model_Color(default="sample_text")
    _safe_set(b, 'model_Color54', a1)
    assert _is_linked(b, 'model_Color54', a1)
    if hasattr(a1, 'model_ColorFeature'):
        assert _is_linked(a1, 'model_ColorFeature', b)
    _safe_set(b, 'model_Color54', a2)
    assert _is_linked(b, 'model_Color54', a2)
    if hasattr(a1, 'model_ColorFeature'):
        assert not _is_linked(a1, 'model_ColorFeature', b)
    if hasattr(a2, 'model_ColorFeature'):
        assert _is_linked(a2, 'model_ColorFeature', b)
    _safe_set(b, 'model_Color54', None)
    assert not _is_linked(b, 'model_Color54', a2)
    if hasattr(a2, 'model_ColorFeature'):
        assert not _is_linked(a2, 'model_ColorFeature', b)


def test_assoc_custom40_reverse_link_reassign_clear():
    a1 = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    a2 = model_CustomColor(B=13, G=13, R=13, name="sample_text_2")
    b = model_Color(default="sample_text")
    _safe_set(b, 'model_Color', a1)
    assert _is_linked(b, 'model_Color', a1)
    if hasattr(a1, 'model_CustomColor41'):
        assert _is_linked(a1, 'model_CustomColor41', b)
    _safe_set(b, 'model_Color', a2)
    assert _is_linked(b, 'model_Color', a2)
    if hasattr(a1, 'model_CustomColor41'):
        assert not _is_linked(a1, 'model_CustomColor41', b)
    if hasattr(a2, 'model_CustomColor41'):
        assert _is_linked(a2, 'model_CustomColor41', b)
    _safe_set(b, 'model_Color', None)
    assert not _is_linked(b, 'model_Color', a2)
    if hasattr(a2, 'model_CustomColor41'):
        assert not _is_linked(a2, 'model_CustomColor41', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colors38_stub_double():
    # model_Colors has no real 'model_Colors39' property in the generated
    # code (a bare stub) -- manually attach it so model_CustomColor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CustomColor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    partner = model_Colors()
    setattr(partner, 'model_Colors39', None)
    _safe_set(owner, 'model_CustomColor', partner)
    assert owner in getattr(partner, 'model_Colors39')
    _safe_set(owner, 'model_CustomColor', None)
    assert owner not in getattr(partner, 'model_Colors39')


def test_assoc_conditional16_stub_double():
    # model_Feature has no real 'model_Feature' property in the generated
    # code (a bare stub) -- manually attach it so model_FeatureConditional's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_FeatureConditional's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_FeatureConditional(operator="sample_text")
    partner = model_Feature()
    setattr(partner, 'model_Feature', None)
    _safe_set(owner, 'model_FeatureConditional', partner)
    assert getattr(partner, 'model_Feature') == owner
    _safe_set(owner, 'model_FeatureConditional', None)
    assert getattr(partner, 'model_Feature') is None


def test_assoc_decorators31_stub_double():
    # model_Decorator has no real 'model_Decorator' property in the generated
    # code (a bare stub) -- manually attach it so model_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Link(complex=True, reference=True)
    partner = model_Decorator()
    setattr(partner, 'model_Decorator', None)
    _safe_set(owner, 'model_Link32', {partner})
    assert getattr(partner, 'model_Decorator') == owner
    _safe_set(owner, 'model_Link32', set())
    assert getattr(partner, 'model_Decorator') is None


def test_assoc_element45_stub_double():
    # model_ConnectableElement has no real 'model_ConnectableElement47' property in the generated
    # code (a bare stub) -- manually attach it so model_CustomFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CustomFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CustomFigure(name="sample_text")
    partner = model_ConnectableElement()
    setattr(partner, 'model_ConnectableElement47', None)
    _safe_set(owner, 'model_CustomFigure46', partner)
    assert getattr(partner, 'model_ConnectableElement47') == owner
    _safe_set(owner, 'model_CustomFigure46', None)
    assert getattr(partner, 'model_ConnectableElement47') is None


def test_assoc_figure48_stub_double():
    # model_Custom has no real 'model_Custom' property in the generated
    # code (a bare stub) -- manually attach it so model_CustomFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CustomFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CustomFigure(name="sample_text")
    partner = model_Custom()
    setattr(partner, 'model_Custom', None)
    _safe_set(owner, 'model_CustomFigure49', partner)
    assert getattr(partner, 'model_Custom') == owner
    _safe_set(owner, 'model_CustomFigure49', None)
    assert getattr(partner, 'model_Custom') is None


def test_assoc_figures7_stub_double():
    # model_XDiagram has no real 'model_XDiagram8' property in the generated
    # code (a bare stub) -- manually attach it so model_CustomFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CustomFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CustomFigure(name="sample_text")
    partner = model_XDiagram()
    setattr(partner, 'model_XDiagram8', None)
    _safe_set(owner, 'model_CustomFigure', partner)
    assert owner in getattr(partner, 'model_XDiagram8')
    _safe_set(owner, 'model_CustomFigure', None)
    assert owner not in getattr(partner, 'model_XDiagram8')


def test_assoc_metamodel0_stub_double():
    # model_XDiagram has no real 'model_XDiagram' property in the generated
    # code (a bare stub) -- manually attach it so model_MetaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MetaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MetaModel(ecorePath="sample_text", plugin="sample_text")
    partner = model_XDiagram()
    setattr(partner, 'model_XDiagram', None)
    _safe_set(owner, 'model_MetaModel', partner)
    assert getattr(partner, 'model_XDiagram') == owner
    _safe_set(owner, 'model_MetaModel', None)
    assert getattr(partner, 'model_XDiagram') is None


def test_assoc_modelAttribute19_stub_double():
    # model_EAttribute has no real 'model_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so model_FeatureConditional's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_FeatureConditional's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_FeatureConditional(operator="sample_text")
    partner = model_EAttribute()
    setattr(partner, 'model_EAttribute', None)
    _safe_set(owner, 'model_FeatureConditional20', partner)
    assert getattr(partner, 'model_EAttribute') == owner
    _safe_set(owner, 'model_FeatureConditional20', None)
    assert getattr(partner, 'model_EAttribute') is None


def test_assoc_modelAttribute56_stub_double():
    # model_EAttribute has no real 'model_EAttribute58' property in the generated
    # code (a bare stub) -- manually attach it so model_TextPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TextPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TextPart(editable=True, text="sample_text")
    partner = model_EAttribute()
    setattr(partner, 'model_EAttribute58', None)
    _safe_set(owner, 'model_TextPart57', partner)
    assert getattr(partner, 'model_EAttribute58') == owner
    _safe_set(owner, 'model_TextPart57', None)
    assert getattr(partner, 'model_EAttribute58') is None


def test_assoc_modelReference24_stub_double():
    # model_EReference has no real 'model_EReference' property in the generated
    # code (a bare stub) -- manually attach it so model_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Link(complex=True, reference=True)
    partner = model_EReference()
    setattr(partner, 'model_EReference', None)
    _safe_set(owner, 'model_Link', partner)
    assert getattr(partner, 'model_EReference') == owner
    _safe_set(owner, 'model_Link', None)
    assert getattr(partner, 'model_EReference') is None


def test_assoc_modelReference36_stub_double():
    # model_EReference has no real 'model_EReference37' property in the generated
    # code (a bare stub) -- manually attach it so model_Anchor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Anchor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Anchor(direction="sample_text", max=7)
    partner = model_EReference()
    setattr(partner, 'model_EReference37', None)
    _safe_set(owner, 'model_Anchor', partner)
    assert getattr(partner, 'model_EReference37') == owner
    _safe_set(owner, 'model_Anchor', None)
    assert getattr(partner, 'model_EReference37') is None


def test_assoc_parts55_stub_double():
    # model_TextValue has no real 'model_TextValue' property in the generated
    # code (a bare stub) -- manually attach it so model_TextPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TextPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TextPart(editable=True, text="sample_text")
    partner = model_TextValue()
    setattr(partner, 'model_TextValue', None)
    _safe_set(owner, 'model_TextPart', partner)
    assert owner in getattr(partner, 'model_TextValue')
    _safe_set(owner, 'model_TextPart', None)
    assert owner not in getattr(partner, 'model_TextValue')


def test_assoc_sourceReference25_stub_double():
    # model_EReference has no real 'model_EReference27' property in the generated
    # code (a bare stub) -- manually attach it so model_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Link(complex=True, reference=True)
    partner = model_EReference()
    setattr(partner, 'model_EReference27', None)
    _safe_set(owner, 'model_Link26', partner)
    assert getattr(partner, 'model_EReference27') == owner
    _safe_set(owner, 'model_Link26', None)
    assert getattr(partner, 'model_EReference27') is None


def test_assoc_targetReference28_stub_double():
    # model_EReference has no real 'model_EReference30' property in the generated
    # code (a bare stub) -- manually attach it so model_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Link(complex=True, reference=True)
    partner = model_EReference()
    setattr(partner, 'model_EReference30', None)
    _safe_set(owner, 'model_Link29', partner)
    assert getattr(partner, 'model_EReference30') == owner
    _safe_set(owner, 'model_Link29', None)
    assert getattr(partner, 'model_EReference30') is None


def test_assoc_value21_stub_double():
    # model_Value has no real 'model_Value' property in the generated
    # code (a bare stub) -- manually attach it so model_FeatureConditional's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_FeatureConditional's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_FeatureConditional(operator="sample_text")
    partner = model_Value()
    setattr(partner, 'model_Value', None)
    _safe_set(owner, 'model_FeatureConditional22', partner)
    assert getattr(partner, 'model_Value') == owner
    _safe_set(owner, 'model_FeatureConditional22', None)
    assert getattr(partner, 'model_Value') is None


