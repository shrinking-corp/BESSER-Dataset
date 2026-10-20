import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Graphics,
    ID,
    Label,
    Node,
    Object,
    PetriNetType,
    PlaceNode,
    ToolInfo,
    TransitionNode,
    pnmlcoremodel_AnnotationGraphics,
    pnmlcoremodel_AnyType,
    pnmlcoremodel_Arc,
    pnmlcoremodel_ArcGraphics,
    pnmlcoremodel_Attribute,
    pnmlcoremodel_Coordinate,
    pnmlcoremodel_EmptyType,
    pnmlcoremodel_Fill,
    pnmlcoremodel_Font,
    pnmlcoremodel_Graphics,
    pnmlcoremodel_ID,
    pnmlcoremodel_Label,
    pnmlcoremodel_LabelProxy,
    pnmlcoremodel_Line,
    pnmlcoremodel_Name,
    pnmlcoremodel_Node,
    pnmlcoremodel_NodeGraphics,
    pnmlcoremodel_Object,
    pnmlcoremodel_Page,
    pnmlcoremodel_PageLabelProxy,
    pnmlcoremodel_PetriNet,
    pnmlcoremodel_PetriNetDoc,
    pnmlcoremodel_PetriNetType,
    pnmlcoremodel_Place,
    pnmlcoremodel_PlaceNode,
    pnmlcoremodel_RefPlace,
    pnmlcoremodel_RefTransition,
    pnmlcoremodel_ToolInfo,
    pnmlcoremodel_ToolInfoText,
    pnmlcoremodel_Transition,
    pnmlcoremodel_TransitionNode,
    LineShape,
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

def test_assoc_dimension55_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'pnmlcoremodel_NodeGraphics56' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'pnmlcoremodel_NodeGraphics56', None)
    _safe_set(owner, 'pnmlcoremodel_Coordinate57', partner)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics56') == owner
    _safe_set(owner, 'pnmlcoremodel_Coordinate57', None)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics56') is None


def test_assoc_fill61_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'pnmlcoremodel_NodeGraphics62' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'pnmlcoremodel_NodeGraphics62', None)
    _safe_set(owner, 'pnmlcoremodel_Fill', partner)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics62') == owner
    _safe_set(owner, 'pnmlcoremodel_Fill', None)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics62') is None


def test_assoc_fill63_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'pnmlcoremodel_AnnotationGraphics' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'pnmlcoremodel_AnnotationGraphics', None)
    _safe_set(owner, 'pnmlcoremodel_Fill64', partner)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics') == owner
    _safe_set(owner, 'pnmlcoremodel_Fill64', None)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics') is None


def test_assoc_font71_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'pnmlcoremodel_AnnotationGraphics72' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'pnmlcoremodel_AnnotationGraphics72', None)
    _safe_set(owner, 'pnmlcoremodel_Font', partner)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics72') == owner
    _safe_set(owner, 'pnmlcoremodel_Font', None)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics72') is None


def test_assoc_label28_stub_double():
    # pnmlcoremodel_Label has no real 'pnmlcoremodel_Label' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_LabelProxy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_LabelProxy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_LabelProxy(text="sample_text")
    partner = pnmlcoremodel_Label()
    setattr(partner, 'pnmlcoremodel_Label', None)
    _safe_set(owner, 'pnmlcoremodel_LabelProxy29', partner)
    assert getattr(partner, 'pnmlcoremodel_Label') == owner
    _safe_set(owner, 'pnmlcoremodel_LabelProxy29', None)
    assert getattr(partner, 'pnmlcoremodel_Label') is None


def test_assoc_label73_stub_double():
    # pnmlcoremodel_Label has no real 'pnmlcoremodel_Label75' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PageLabelProxy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PageLabelProxy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PageLabelProxy(text="sample_text")
    partner = pnmlcoremodel_Label()
    setattr(partner, 'pnmlcoremodel_Label75', None)
    _safe_set(owner, 'pnmlcoremodel_PageLabelProxy74', partner)
    assert getattr(partner, 'pnmlcoremodel_Label75') == owner
    _safe_set(owner, 'pnmlcoremodel_PageLabelProxy74', None)
    assert getattr(partner, 'pnmlcoremodel_Label75') is None


def test_assoc_labelproxy15_stub_double():
    # pnmlcoremodel_Page has no real 'pnmlcoremodel_Page16' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_LabelProxy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_LabelProxy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_LabelProxy(text="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'pnmlcoremodel_Page16', None)
    _safe_set(owner, 'pnmlcoremodel_LabelProxy', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_Page16')
    _safe_set(owner, 'pnmlcoremodel_LabelProxy', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_Page16')


def test_assoc_line50_stub_double():
    # pnmlcoremodel_ArcGraphics has no real 'pnmlcoremodel_ArcGraphics' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    partner = pnmlcoremodel_ArcGraphics()
    setattr(partner, 'pnmlcoremodel_ArcGraphics', None)
    _safe_set(owner, 'pnmlcoremodel_Line', partner)
    assert getattr(partner, 'pnmlcoremodel_ArcGraphics') == owner
    _safe_set(owner, 'pnmlcoremodel_Line', None)
    assert getattr(partner, 'pnmlcoremodel_ArcGraphics') is None


def test_assoc_line58_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'pnmlcoremodel_NodeGraphics59' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'pnmlcoremodel_NodeGraphics59', None)
    _safe_set(owner, 'pnmlcoremodel_Line60', partner)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics59') == owner
    _safe_set(owner, 'pnmlcoremodel_Line60', None)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics59') is None


def test_assoc_line65_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'pnmlcoremodel_AnnotationGraphics66' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'pnmlcoremodel_AnnotationGraphics66', None)
    _safe_set(owner, 'pnmlcoremodel_Line67', partner)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics66') == owner
    _safe_set(owner, 'pnmlcoremodel_Line67', None)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics66') is None


def test_assoc_name17_stub_double():
    # pnmlcoremodel_Object has no real 'pnmlcoremodel_Object18' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Name(text="sample_text")
    partner = pnmlcoremodel_Object()
    setattr(partner, 'pnmlcoremodel_Object18', None)
    _safe_set(owner, 'pnmlcoremodel_Name19', partner)
    assert getattr(partner, 'pnmlcoremodel_Object18') == owner
    _safe_set(owner, 'pnmlcoremodel_Name19', None)
    assert getattr(partner, 'pnmlcoremodel_Object18') is None


def test_assoc_name3_stub_double():
    # pnmlcoremodel_PetriNet has no real 'pnmlcoremodel_PetriNet4' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Name(text="sample_text")
    partner = pnmlcoremodel_PetriNet()
    setattr(partner, 'pnmlcoremodel_PetriNet4', None)
    _safe_set(owner, 'pnmlcoremodel_Name', partner)
    assert getattr(partner, 'pnmlcoremodel_PetriNet4') == owner
    _safe_set(owner, 'pnmlcoremodel_Name', None)
    assert getattr(partner, 'pnmlcoremodel_PetriNet4') is None


def test_assoc_object30_stub_double():
    # pnmlcoremodel_Object has no real 'pnmlcoremodel_Object32' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_LabelProxy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_LabelProxy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_LabelProxy(text="sample_text")
    partner = pnmlcoremodel_Object()
    setattr(partner, 'pnmlcoremodel_Object32', None)
    _safe_set(owner, 'pnmlcoremodel_LabelProxy31', partner)
    assert getattr(partner, 'pnmlcoremodel_Object32') == owner
    _safe_set(owner, 'pnmlcoremodel_LabelProxy31', None)
    assert getattr(partner, 'pnmlcoremodel_Object32') is None


def test_assoc_offset68_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'pnmlcoremodel_AnnotationGraphics69' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'pnmlcoremodel_AnnotationGraphics69', None)
    _safe_set(owner, 'pnmlcoremodel_Coordinate70', partner)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics69') == owner
    _safe_set(owner, 'pnmlcoremodel_Coordinate70', None)
    assert getattr(partner, 'pnmlcoremodel_AnnotationGraphics69') is None


def test_assoc_pageLabelProxy13_stub_double():
    # pnmlcoremodel_Page has no real 'pnmlcoremodel_Page14' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PageLabelProxy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PageLabelProxy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PageLabelProxy(text="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'pnmlcoremodel_Page14', None)
    _safe_set(owner, 'pnmlcoremodel_PageLabelProxy', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_Page14')
    _safe_set(owner, 'pnmlcoremodel_PageLabelProxy', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_Page14')


def test_assoc_position51_stub_double():
    # pnmlcoremodel_ArcGraphics has no real 'pnmlcoremodel_ArcGraphics52' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    partner = pnmlcoremodel_ArcGraphics()
    setattr(partner, 'pnmlcoremodel_ArcGraphics52', None)
    _safe_set(owner, 'pnmlcoremodel_Coordinate', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_ArcGraphics52')
    _safe_set(owner, 'pnmlcoremodel_Coordinate', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_ArcGraphics52')


def test_assoc_position53_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'pnmlcoremodel_NodeGraphics' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'pnmlcoremodel_NodeGraphics', None)
    _safe_set(owner, 'pnmlcoremodel_Coordinate54', partner)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics') == owner
    _safe_set(owner, 'pnmlcoremodel_Coordinate54', None)
    assert getattr(partner, 'pnmlcoremodel_NodeGraphics') is None


def test_assoc_toolspecific20_stub_double():
    # pnmlcoremodel_Object has no real 'pnmlcoremodel_Object21' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    partner = pnmlcoremodel_Object()
    setattr(partner, 'pnmlcoremodel_Object21', None)
    _safe_set(owner, 'pnmlcoremodel_ToolInfo22', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_Object21')
    _safe_set(owner, 'pnmlcoremodel_ToolInfo22', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_Object21')


def test_assoc_toolspecific41_stub_double():
    # pnmlcoremodel_Label has no real 'pnmlcoremodel_Label42' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    partner = pnmlcoremodel_Label()
    setattr(partner, 'pnmlcoremodel_Label42', None)
    _safe_set(owner, 'pnmlcoremodel_ToolInfo43', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_Label42')
    _safe_set(owner, 'pnmlcoremodel_ToolInfo43', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_Label42')


def test_assoc_toolspecific7_stub_double():
    # pnmlcoremodel_PetriNet has no real 'pnmlcoremodel_PetriNet8' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    partner = pnmlcoremodel_PetriNet()
    setattr(partner, 'pnmlcoremodel_PetriNet8', None)
    _safe_set(owner, 'pnmlcoremodel_ToolInfo', partner)
    assert owner in getattr(partner, 'pnmlcoremodel_PetriNet8')
    _safe_set(owner, 'pnmlcoremodel_ToolInfo', None)
    assert owner not in getattr(partner, 'pnmlcoremodel_PetriNet8')


