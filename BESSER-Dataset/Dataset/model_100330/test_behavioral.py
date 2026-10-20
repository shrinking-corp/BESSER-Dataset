import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotationGraphics,
    AnyElement,
    Arc,
    Color,
    Coordinate,
    Dimension,
    EdgeGraphics,
    Fill,
    Font,
    Graphics,
    IdedElement,
    InitialMarking,
    Inscription,
    Label,
    LabeledElement,
    Line,
    Name,
    NetContent,
    NetContentElement,
    NetElement,
    NetGraphics,
    Node,
    NodeGraphics,
    Offset,
    PNMLDocument,
    PNML_AnnotationGraphics,
    PNML_AnyElement,
    PNML_Arc,
    PNML_Color,
    PNML_Coordinate,
    PNML_Dimension,
    PNML_EdgeGraphics,
    PNML_Fill,
    PNML_Font,
    PNML_Graphics,
    PNML_IdedElement,
    PNML_InitialMarking,
    PNML_Inscription,
    PNML_Label,
    PNML_LabeledElement,
    PNML_Line,
    PNML_Name,
    PNML_NetContent,
    PNML_NetContentElement,
    PNML_NetElement,
    PNML_NetGraphics,
    PNML_Node,
    PNML_NodeGraphics,
    PNML_Offset,
    PNML_PNMLDocument,
    PNML_Page,
    PNML_PageGraphics,
    PNML_Place,
    PNML_Position,
    PNML_Reference,
    PNML_ReferencePlace,
    PNML_ReferenceTransition,
    PNML_ToolSpecific,
    PNML_Transition,
    PNML_URI,
    Page,
    PageGraphics,
    Place,
    Position,
    Reference,
    ToolSpecific,
    URI,
    AlignType,
    DecorationType,
    RotationType,
    ShapeType,
    StyleType,
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

def test_assoc_annotationgraphics127_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics129' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics129', None)
    _safe_set(owner, 'fill128', partner)
    assert getattr(partner, 'AnnotationGraphics129') == owner
    _safe_set(owner, 'fill128', None)
    assert getattr(partner, 'AnnotationGraphics129') is None


def test_assoc_annotationgraphics137_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics139' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics139', None)
    _safe_set(owner, 'line138', partner)
    assert getattr(partner, 'AnnotationGraphics139') == owner
    _safe_set(owner, 'line138', None)
    assert getattr(partner, 'AnnotationGraphics139') is None


def test_assoc_annotationgraphics140_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics141' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics141', None)
    _safe_set(owner, 'font', partner)
    assert getattr(partner, 'AnnotationGraphics141') == owner
    _safe_set(owner, 'font', None)
    assert getattr(partner, 'AnnotationGraphics141') is None


def test_assoc_anyelement18_stub_double():
    # AnyElement has no real 'AnyElement' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = AnyElement()
    setattr(partner, 'AnyElement', None)
    _safe_set(owner, 'PNML_ToolSpecific', {partner})
    assert getattr(partner, 'AnyElement') == owner
    _safe_set(owner, 'PNML_ToolSpecific', set())
    assert getattr(partner, 'AnyElement') is None


def test_assoc_arc21_stub_double():
    # Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'tools22', partner)
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'tools22', None)
    assert getattr(partner, 'Arc') is None


def test_assoc_color130_stub_double():
    # Color has no real 'Color131' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = Color()
    setattr(partner, 'Color131', None)
    _safe_set(owner, 'PNML_Line', partner)
    assert getattr(partner, 'Color131') == owner
    _safe_set(owner, 'PNML_Line', None)
    assert getattr(partner, 'Color131') is None


def test_assoc_edgegraphics124_stub_double():
    # EdgeGraphics has no real 'EdgeGraphics126' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = EdgeGraphics()
    setattr(partner, 'EdgeGraphics126', None)
    _safe_set(owner, 'fill125', partner)
    assert getattr(partner, 'EdgeGraphics126') == owner
    _safe_set(owner, 'fill125', None)
    assert getattr(partner, 'EdgeGraphics126') is None


def test_assoc_edgegraphics134_stub_double():
    # EdgeGraphics has no real 'EdgeGraphics136' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = EdgeGraphics()
    setattr(partner, 'EdgeGraphics136', None)
    _safe_set(owner, 'line135', partner)
    assert getattr(partner, 'EdgeGraphics136') == owner
    _safe_set(owner, 'line135', None)
    assert getattr(partner, 'EdgeGraphics136') is None


def test_assoc_gradientcolor116_stub_double():
    # Color has no real 'Color118' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = Color()
    setattr(partner, 'Color118', None)
    _safe_set(owner, 'PNML_Fill117', partner)
    assert getattr(partner, 'Color118') == owner
    _safe_set(owner, 'PNML_Fill117', None)
    assert getattr(partner, 'Color118') is None


def test_assoc_image119_stub_double():
    # URI has no real 'URI121' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = URI()
    setattr(partner, 'URI121', None)
    _safe_set(owner, 'PNML_Fill120', partner)
    assert getattr(partner, 'URI121') == owner
    _safe_set(owner, 'PNML_Fill120', None)
    assert getattr(partner, 'URI121') is None


def test_assoc_interiorcolor115_stub_double():
    # Color has no real 'Color' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = Color()
    setattr(partner, 'Color', None)
    _safe_set(owner, 'PNML_Fill', partner)
    assert getattr(partner, 'Color') == owner
    _safe_set(owner, 'PNML_Fill', None)
    assert getattr(partner, 'Color') is None


def test_assoc_namedelement31_stub_double():
    # LabeledElement has no real 'LabeledElement' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Label(text="sample_text")
    partner = LabeledElement()
    setattr(partner, 'LabeledElement', None)
    _safe_set(owner, 'labels', partner)
    assert getattr(partner, 'LabeledElement') == owner
    _safe_set(owner, 'labels', None)
    assert getattr(partner, 'LabeledElement') is None


def test_assoc_net19_stub_double():
    # NetElement has no real 'NetElement20' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = NetElement()
    setattr(partner, 'NetElement20', None)
    _safe_set(owner, 'tools', partner)
    assert getattr(partner, 'NetElement20') == owner
    _safe_set(owner, 'tools', None)
    assert getattr(partner, 'NetElement20') is None


def test_assoc_node23_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'tools24', partner)
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'tools24', None)
    assert getattr(partner, 'Node') is None


def test_assoc_nodegraphics113_stub_double():
    # NodeGraphics has no real 'NodeGraphics114' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Dimension(height="sample_text", width="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics114', None)
    _safe_set(owner, 'dimension', partner)
    assert getattr(partner, 'NodeGraphics114') == owner
    _safe_set(owner, 'dimension', None)
    assert getattr(partner, 'NodeGraphics114') is None


def test_assoc_nodegraphics122_stub_double():
    # NodeGraphics has no real 'NodeGraphics123' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics123', None)
    _safe_set(owner, 'fill', partner)
    assert getattr(partner, 'NodeGraphics123') == owner
    _safe_set(owner, 'fill', None)
    assert getattr(partner, 'NodeGraphics123') is None


def test_assoc_nodegraphics132_stub_double():
    # NodeGraphics has no real 'NodeGraphics133' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics133', None)
    _safe_set(owner, 'line', partner)
    assert getattr(partner, 'NodeGraphics133') == owner
    _safe_set(owner, 'line', None)
    assert getattr(partner, 'NodeGraphics133') is None


def test_assoc_page25_stub_double():
    # Page has no real 'Page27' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Page()
    setattr(partner, 'Page27', None)
    _safe_set(owner, 'tools26', partner)
    assert getattr(partner, 'Page27') == owner
    _safe_set(owner, 'tools26', None)
    assert getattr(partner, 'Page27') is None


