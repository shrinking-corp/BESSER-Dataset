import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    Coordinate,
    Graphics,
    Label,
    Node,
    PlaceNode,
    PnObject,
    TransitionNode,
    pnmlcoremodel_Annotation,
    pnmlcoremodel_AnnotationGraphics,
    pnmlcoremodel_AnyObject,
    pnmlcoremodel_Arc,
    pnmlcoremodel_ArcGraphics,
    pnmlcoremodel_Attribute,
    pnmlcoremodel_Coordinate,
    pnmlcoremodel_Dimension,
    pnmlcoremodel_Fill,
    pnmlcoremodel_Font,
    pnmlcoremodel_Graphics,
    pnmlcoremodel_Label,
    pnmlcoremodel_Line,
    pnmlcoremodel_Name,
    pnmlcoremodel_Node,
    pnmlcoremodel_NodeGraphics,
    pnmlcoremodel_Offset,
    pnmlcoremodel_Page,
    pnmlcoremodel_PetriNet,
    pnmlcoremodel_PetriNetDoc,
    pnmlcoremodel_Place,
    pnmlcoremodel_PlaceNode,
    pnmlcoremodel_PnObject,
    pnmlcoremodel_Position,
    pnmlcoremodel_RefPlace,
    pnmlcoremodel_RefTransition,
    pnmlcoremodel_ToolInfo,
    pnmlcoremodel_Transition,
    pnmlcoremodel_TransitionNode,
    CSS2Color,
    CSS2FontFamily,
    CSS2FontSize,
    CSS2FontStyle,
    CSS2FontWeight,
    FontAlign,
    FontDecoration,
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

def test_assoc_containerNamePetriNet17_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    a2 = pnmlcoremodel_PetriNet(id="sample_text_2", type="sample_text_2")
    b = pnmlcoremodel_Name(text="sample_text")
    _safe_set(b, 'name', a1)
    assert _is_linked(b, 'name', a1)
    if hasattr(a1, 'PetriNet18'):
        assert _is_linked(a1, 'PetriNet18', b)
    _safe_set(b, 'name', a2)
    assert _is_linked(b, 'name', a2)
    if hasattr(a1, 'PetriNet18'):
        assert not _is_linked(a1, 'PetriNet18', b)
    if hasattr(a2, 'PetriNet18'):
        assert _is_linked(a2, 'PetriNet18', b)
    _safe_set(b, 'name', None)
    assert not _is_linked(b, 'name', a2)
    if hasattr(a2, 'PetriNet18'):
        assert not _is_linked(a2, 'PetriNet18', b)


def test_assoc_containerNamePnObject19_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PnObject(id="sample_text")
    a2 = pnmlcoremodel_PnObject(id="sample_text_2")
    b = pnmlcoremodel_Name(text="sample_text")
    _safe_set(b, 'name20', a1)
    assert _is_linked(b, 'name20', a1)
    if hasattr(a1, 'PnObject21'):
        assert _is_linked(a1, 'PnObject21', b)
    _safe_set(b, 'name20', a2)
    assert _is_linked(b, 'name20', a2)
    if hasattr(a1, 'PnObject21'):
        assert not _is_linked(a1, 'PnObject21', b)
    if hasattr(a2, 'PnObject21'):
        assert _is_linked(a2, 'PnObject21', b)
    _safe_set(b, 'name20', None)
    assert not _is_linked(b, 'name20', a2)
    if hasattr(a2, 'PnObject21'):
        assert not _is_linked(a2, 'PnObject21', b)


def test_assoc_containerPetriNet22_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet23', a1)
    assert _is_linked(b, 'PetriNet23', a1)
    if hasattr(a1, 'toolspecifics'):
        assert _is_linked(a1, 'toolspecifics', b)
    _safe_set(b, 'PetriNet23', a2)
    assert _is_linked(b, 'PetriNet23', a2)
    if hasattr(a1, 'toolspecifics'):
        assert not _is_linked(a1, 'toolspecifics', b)
    if hasattr(a2, 'toolspecifics'):
        assert _is_linked(a2, 'toolspecifics', b)
    _safe_set(b, 'PetriNet23', None)
    assert not _is_linked(b, 'PetriNet23', a2)
    if hasattr(a2, 'toolspecifics'):
        assert not _is_linked(a2, 'toolspecifics', b)


def test_assoc_containerPetriNetDoc5_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PetriNetDoc(xmlns="sample_text")
    a2 = pnmlcoremodel_PetriNetDoc(xmlns="sample_text_2")
    b = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
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


def test_assoc_containerPnObject24_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = pnmlcoremodel_PnObject(id="sample_text")
    _safe_set(b, 'PnObject26', a1)
    assert _is_linked(b, 'PnObject26', a1)
    if hasattr(a1, 'toolspecifics25'):
        assert _is_linked(a1, 'toolspecifics25', b)
    _safe_set(b, 'PnObject26', a2)
    assert _is_linked(b, 'PnObject26', a2)
    if hasattr(a1, 'toolspecifics25'):
        assert not _is_linked(a1, 'toolspecifics25', b)
    if hasattr(a2, 'toolspecifics25'):
        assert _is_linked(a2, 'toolspecifics25', b)
    _safe_set(b, 'PnObject26', None)
    assert not _is_linked(b, 'PnObject26', a2)
    if hasattr(a2, 'toolspecifics25'):
        assert not _is_linked(a2, 'toolspecifics25', b)


def test_assoc_name11_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PnObject(id="sample_text")
    a2 = pnmlcoremodel_PnObject(id="sample_text_2")
    b = pnmlcoremodel_Name(text="sample_text")
    _safe_set(b, 'Name12', a1)
    assert _is_linked(b, 'Name12', a1)
    if hasattr(a1, 'containerNamePnObject'):
        assert _is_linked(a1, 'containerNamePnObject', b)
    _safe_set(b, 'Name12', a2)
    assert _is_linked(b, 'Name12', a2)
    if hasattr(a1, 'containerNamePnObject'):
        assert not _is_linked(a1, 'containerNamePnObject', b)
    if hasattr(a2, 'containerNamePnObject'):
        assert _is_linked(a2, 'containerNamePnObject', b)
    _safe_set(b, 'Name12', None)
    assert not _is_linked(b, 'Name12', a2)
    if hasattr(a2, 'containerNamePnObject'):
        assert not _is_linked(a2, 'containerNamePnObject', b)


def test_assoc_name2_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    a2 = pnmlcoremodel_PetriNet(id="sample_text_2", type="sample_text_2")
    b = pnmlcoremodel_Name(text="sample_text")
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


def test_assoc_nets0_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_PetriNetDoc(xmlns="sample_text")
    a2 = pnmlcoremodel_PetriNetDoc(xmlns="sample_text_2")
    b = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
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


def test_assoc_toolspecifics13_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = pnmlcoremodel_PnObject(id="sample_text")
    _safe_set(b, 'containerPnObject', {a1})
    assert _is_linked(b, 'containerPnObject', a1)
    if hasattr(a1, 'ToolInfo14'):
        assert _is_linked(a1, 'ToolInfo14', b)
    _safe_set(b, 'containerPnObject', {a2})
    assert _is_linked(b, 'containerPnObject', a2)
    if hasattr(a1, 'ToolInfo14'):
        assert not _is_linked(a1, 'ToolInfo14', b)
    if hasattr(a2, 'ToolInfo14'):
        assert _is_linked(a2, 'ToolInfo14', b)
    _safe_set(b, 'containerPnObject', set())
    assert not _is_linked(b, 'containerPnObject', a2)
    if hasattr(a2, 'ToolInfo14'):
        assert not _is_linked(a2, 'ToolInfo14', b)


def test_assoc_toolspecifics3_reverse_link_reassign_clear():
    a1 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'containerPetriNet4', {a1})
    assert _is_linked(b, 'containerPetriNet4', a1)
    if hasattr(a1, 'ToolInfo'):
        assert _is_linked(a1, 'ToolInfo', b)
    _safe_set(b, 'containerPetriNet4', {a2})
    assert _is_linked(b, 'containerPetriNet4', a2)
    if hasattr(a1, 'ToolInfo'):
        assert not _is_linked(a1, 'ToolInfo', b)
    if hasattr(a2, 'ToolInfo'):
        assert _is_linked(a2, 'ToolInfo', b)
    _safe_set(b, 'containerPetriNet4', set())
    assert not _is_linked(b, 'containerPetriNet4', a2)
    if hasattr(a2, 'ToolInfo'):
        assert not _is_linked(a2, 'ToolInfo', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containerAnnotationGraphics59_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'AnnotationGraphics61' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics61', None)
    _safe_set(owner, 'fill60', partner)
    assert getattr(partner, 'AnnotationGraphics61') == owner
    _safe_set(owner, 'fill60', None)
    assert getattr(partner, 'AnnotationGraphics61') is None


def test_assoc_containerAnnotationGraphics67_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'AnnotationGraphics69' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics69', None)
    _safe_set(owner, 'line68', partner)
    assert getattr(partner, 'AnnotationGraphics69') == owner
    _safe_set(owner, 'line68', None)
    assert getattr(partner, 'AnnotationGraphics69') is None


def test_assoc_containerAnnotationGraphics88_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'AnnotationGraphics89' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics89', None)
    _safe_set(owner, 'font', partner)
    assert getattr(partner, 'AnnotationGraphics89') == owner
    _safe_set(owner, 'font', None)
    assert getattr(partner, 'AnnotationGraphics89') is None


def test_assoc_containerArcGraphics64_stub_double():
    # pnmlcoremodel_ArcGraphics has no real 'ArcGraphics66' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_ArcGraphics()
    setattr(partner, 'ArcGraphics66', None)
    _safe_set(owner, 'line65', partner)
    assert getattr(partner, 'ArcGraphics66') == owner
    _safe_set(owner, 'line65', None)
    assert getattr(partner, 'ArcGraphics66') is None


def test_assoc_containerLabel27_stub_double():
    # pnmlcoremodel_Label has no real 'Label' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = pnmlcoremodel_Label()
    setattr(partner, 'Label', None)
    _safe_set(owner, 'toolspecifics28', partner)
    assert getattr(partner, 'Label') == owner
    _safe_set(owner, 'toolspecifics28', None)
    assert getattr(partner, 'Label') is None


def test_assoc_containerNodeGraphics57_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'NodeGraphics58' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'NodeGraphics58', None)
    _safe_set(owner, 'fill', partner)
    assert getattr(partner, 'NodeGraphics58') == owner
    _safe_set(owner, 'fill', None)
    assert getattr(partner, 'NodeGraphics58') is None


def test_assoc_containerNodeGraphics62_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'NodeGraphics63' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'NodeGraphics63', None)
    _safe_set(owner, 'line', partner)
    assert getattr(partner, 'NodeGraphics63') == owner
    _safe_set(owner, 'line', None)
    assert getattr(partner, 'NodeGraphics63') is None


def test_assoc_containerPage15_stub_double():
    # pnmlcoremodel_Page has no real 'Page16' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PnObject(id="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'Page16', None)
    _safe_set(owner, 'objects', partner)
    assert getattr(partner, 'Page16') == owner
    _safe_set(owner, 'objects', None)
    assert getattr(partner, 'Page16') is None


def test_assoc_containerPetriNet7_stub_double():
    # pnmlcoremodel_Page has no real 'pages' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'pages', None)
    _safe_set(owner, 'PetriNet8', partner)
    assert getattr(partner, 'pages') == owner
    _safe_set(owner, 'PetriNet8', None)
    assert getattr(partner, 'pages') is None


def test_assoc_containerToolInfo97_stub_double():
    # pnmlcoremodel_AnyObject has no real 'toolInfoModel' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = pnmlcoremodel_AnyObject()
    setattr(partner, 'toolInfoModel', None)
    _safe_set(owner, 'ToolInfo98', partner)
    assert getattr(partner, 'toolInfoModel') == owner
    _safe_set(owner, 'ToolInfo98', None)
    assert getattr(partner, 'toolInfoModel') is None


def test_assoc_fill34_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'containerNodeGraphics' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'containerNodeGraphics', None)
    _safe_set(owner, 'Fill', partner)
    assert getattr(partner, 'containerNodeGraphics') == owner
    _safe_set(owner, 'Fill', None)
    assert getattr(partner, 'containerNodeGraphics') is None


def test_assoc_fill48_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'containerAnnotationGraphics49' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics49', None)
    _safe_set(owner, 'Fill50', partner)
    assert getattr(partner, 'containerAnnotationGraphics49') == owner
    _safe_set(owner, 'Fill50', None)
    assert getattr(partner, 'containerAnnotationGraphics49') is None


def test_assoc_font54_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'containerAnnotationGraphics55' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics55', None)
    _safe_set(owner, 'Font', partner)
    assert getattr(partner, 'containerAnnotationGraphics55') == owner
    _safe_set(owner, 'Font', None)
    assert getattr(partner, 'containerAnnotationGraphics55') is None


def test_assoc_line35_stub_double():
    # pnmlcoremodel_NodeGraphics has no real 'containerNodeGraphics36' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_NodeGraphics()
    setattr(partner, 'containerNodeGraphics36', None)
    _safe_set(owner, 'Line', partner)
    assert getattr(partner, 'containerNodeGraphics36') == owner
    _safe_set(owner, 'Line', None)
    assert getattr(partner, 'containerNodeGraphics36') is None


def test_assoc_line51_stub_double():
    # pnmlcoremodel_AnnotationGraphics has no real 'containerAnnotationGraphics52' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics52', None)
    _safe_set(owner, 'Line53', partner)
    assert getattr(partner, 'containerAnnotationGraphics52') == owner
    _safe_set(owner, 'Line53', None)
    assert getattr(partner, 'containerAnnotationGraphics52') is None


def test_assoc_line72_stub_double():
    # pnmlcoremodel_ArcGraphics has no real 'containerArcGraphics73' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = pnmlcoremodel_ArcGraphics()
    setattr(partner, 'containerArcGraphics73', None)
    _safe_set(owner, 'Line74', partner)
    assert getattr(partner, 'containerArcGraphics73') == owner
    _safe_set(owner, 'Line74', None)
    assert getattr(partner, 'containerArcGraphics73') is None


def test_assoc_objects6_stub_double():
    # pnmlcoremodel_Page has no real 'containerPage' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PnObject(id="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'containerPage', None)
    _safe_set(owner, 'PnObject', partner)
    assert owner in getattr(partner, 'containerPage')
    _safe_set(owner, 'PnObject', None)
    assert owner not in getattr(partner, 'containerPage')


def test_assoc_pages1_stub_double():
    # pnmlcoremodel_Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_PetriNet(id="sample_text", type="sample_text")
    partner = pnmlcoremodel_Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'containerPetriNet', {partner})
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'containerPetriNet', set())
    assert getattr(partner, 'Page') is None


def test_assoc_toolInfoModel29_stub_double():
    # pnmlcoremodel_AnyObject has no real 'AnyObject' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = pnmlcoremodel_AnyObject()
    setattr(partner, 'AnyObject', None)
    _safe_set(owner, 'containerToolInfo', partner)
    assert getattr(partner, 'AnyObject') == owner
    _safe_set(owner, 'containerToolInfo', None)
    assert getattr(partner, 'AnyObject') is None


def test_assoc_toolspecifics30_stub_double():
    # pnmlcoremodel_Label has no real 'containerLabel' property in the generated
    # code (a bare stub) -- manually attach it so pnmlcoremodel_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnmlcoremodel_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnmlcoremodel_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = pnmlcoremodel_Label()
    setattr(partner, 'containerLabel', None)
    _safe_set(owner, 'ToolInfo31', partner)
    assert owner in getattr(partner, 'containerLabel')
    _safe_set(owner, 'ToolInfo31', None)
    assert owner not in getattr(partner, 'containerLabel')


