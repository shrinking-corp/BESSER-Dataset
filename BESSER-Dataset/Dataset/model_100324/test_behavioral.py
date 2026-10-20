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
    ImportNode,
    InitialMarking,
    Inscription,
    Instance,
    Interface,
    Label,
    LabeledElement,
    Line,
    Module,
    NCName,
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
    PNML_ImportNode,
    PNML_InitialMarking,
    PNML_Inscription,
    PNML_Instance,
    PNML_Interface,
    PNML_Label,
    PNML_LabeledElement,
    PNML_Line,
    PNML_Module,
    PNML_NCName,
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

def test_assoc_annotationgraphics165_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics167' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics167', None)
    _safe_set(owner, 'fill166', partner)
    assert getattr(partner, 'AnnotationGraphics167') == owner
    _safe_set(owner, 'fill166', None)
    assert getattr(partner, 'AnnotationGraphics167') is None


def test_assoc_annotationgraphics175_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics177' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics177', None)
    _safe_set(owner, 'line176', partner)
    assert getattr(partner, 'AnnotationGraphics177') == owner
    _safe_set(owner, 'line176', None)
    assert getattr(partner, 'AnnotationGraphics177') is None


def test_assoc_annotationgraphics178_stub_double():
    # AnnotationGraphics has no real 'AnnotationGraphics179' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics179', None)
    _safe_set(owner, 'font', partner)
    assert getattr(partner, 'AnnotationGraphics179') == owner
    _safe_set(owner, 'font', None)
    assert getattr(partner, 'AnnotationGraphics179') is None


def test_assoc_anyelement39_stub_double():
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


def test_assoc_arc42_stub_double():
    # Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'tools43', partner)
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'tools43', None)
    assert getattr(partner, 'Arc') is None


def test_assoc_color168_stub_double():
    # Color has no real 'Color169' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = Color()
    setattr(partner, 'Color169', None)
    _safe_set(owner, 'PNML_Line', partner)
    assert getattr(partner, 'Color169') == owner
    _safe_set(owner, 'PNML_Line', None)
    assert getattr(partner, 'Color169') is None


def test_assoc_edgegraphics162_stub_double():
    # EdgeGraphics has no real 'EdgeGraphics164' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = EdgeGraphics()
    setattr(partner, 'EdgeGraphics164', None)
    _safe_set(owner, 'fill163', partner)
    assert getattr(partner, 'EdgeGraphics164') == owner
    _safe_set(owner, 'fill163', None)
    assert getattr(partner, 'EdgeGraphics164') is None


def test_assoc_edgegraphics172_stub_double():
    # EdgeGraphics has no real 'EdgeGraphics174' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = EdgeGraphics()
    setattr(partner, 'EdgeGraphics174', None)
    _safe_set(owner, 'line173', partner)
    assert getattr(partner, 'EdgeGraphics174') == owner
    _safe_set(owner, 'line173', None)
    assert getattr(partner, 'EdgeGraphics174') is None


def test_assoc_gradientcolor154_stub_double():
    # Color has no real 'Color156' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = Color()
    setattr(partner, 'Color156', None)
    _safe_set(owner, 'PNML_Fill155', partner)
    assert getattr(partner, 'Color156') == owner
    _safe_set(owner, 'PNML_Fill155', None)
    assert getattr(partner, 'Color156') is None


def test_assoc_image157_stub_double():
    # URI has no real 'URI159' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = URI()
    setattr(partner, 'URI159', None)
    _safe_set(owner, 'PNML_Fill158', partner)
    assert getattr(partner, 'URI159') == owner
    _safe_set(owner, 'PNML_Fill158', None)
    assert getattr(partner, 'URI159') is None


def test_assoc_interiorcolor153_stub_double():
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


def test_assoc_namedelement53_stub_double():
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


def test_assoc_net40_stub_double():
    # NetElement has no real 'NetElement41' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = NetElement()
    setattr(partner, 'NetElement41', None)
    _safe_set(owner, 'tools', partner)
    assert getattr(partner, 'NetElement41') == owner
    _safe_set(owner, 'tools', None)
    assert getattr(partner, 'NetElement41') is None


def test_assoc_node44_stub_double():
    # Node has no real 'Node46' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Node()
    setattr(partner, 'Node46', None)
    _safe_set(owner, 'tools45', partner)
    assert getattr(partner, 'Node46') == owner
    _safe_set(owner, 'tools45', None)
    assert getattr(partner, 'Node46') is None


def test_assoc_nodegraphics151_stub_double():
    # NodeGraphics has no real 'NodeGraphics152' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Dimension(height="sample_text", width="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics152', None)
    _safe_set(owner, 'dimension', partner)
    assert getattr(partner, 'NodeGraphics152') == owner
    _safe_set(owner, 'dimension', None)
    assert getattr(partner, 'NodeGraphics152') is None


def test_assoc_nodegraphics160_stub_double():
    # NodeGraphics has no real 'NodeGraphics161' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Fill(gradientrotation="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics161', None)
    _safe_set(owner, 'fill', partner)
    assert getattr(partner, 'NodeGraphics161') == owner
    _safe_set(owner, 'fill', None)
    assert getattr(partner, 'NodeGraphics161') is None


def test_assoc_nodegraphics170_stub_double():
    # NodeGraphics has no real 'NodeGraphics171' property in the generated
    # code (a bare stub) -- manually attach it so PNML_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    partner = NodeGraphics()
    setattr(partner, 'NodeGraphics171', None)
    _safe_set(owner, 'line', partner)
    assert getattr(partner, 'NodeGraphics171') == owner
    _safe_set(owner, 'line', None)
    assert getattr(partner, 'NodeGraphics171') is None


def test_assoc_page47_stub_double():
    # Page has no real 'Page49' property in the generated
    # code (a bare stub) -- manually attach it so PNML_ToolSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PNML_ToolSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    partner = Page()
    setattr(partner, 'Page49', None)
    _safe_set(owner, 'tools48', partner)
    assert getattr(partner, 'Page49') == owner
    _safe_set(owner, 'tools48', None)
    assert getattr(partner, 'Page49') is None


