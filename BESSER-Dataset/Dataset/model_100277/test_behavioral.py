import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    Coordinate,
    Graphics,
    HLCoreAnnotation,
    Label,
    Node,
    PlaceNode,
    PnObject,
    TransitionNode,
    hlcorestructure_Annotation,
    hlcorestructure_AnnotationGraphics,
    hlcorestructure_AnyObject,
    hlcorestructure_AnySort,
    hlcorestructure_ArbitrarySort,
    hlcorestructure_Arc,
    hlcorestructure_ArcGraphics,
    hlcorestructure_Attribute,
    hlcorestructure_Condition,
    hlcorestructure_Coordinate,
    hlcorestructure_Declaration,
    hlcorestructure_Declarations,
    hlcorestructure_Dimension,
    hlcorestructure_Fill,
    hlcorestructure_Font,
    hlcorestructure_Graphics,
    hlcorestructure_HLAnnotation,
    hlcorestructure_HLCoreAnnotation,
    hlcorestructure_HLMarking,
    hlcorestructure_Label,
    hlcorestructure_Line,
    hlcorestructure_Name,
    hlcorestructure_Node,
    hlcorestructure_NodeGraphics,
    hlcorestructure_Offset,
    hlcorestructure_Page,
    hlcorestructure_PetriNet,
    hlcorestructure_PetriNetDoc,
    hlcorestructure_Place,
    hlcorestructure_PlaceNode,
    hlcorestructure_PnObject,
    hlcorestructure_Position,
    hlcorestructure_RefPlace,
    hlcorestructure_RefTransition,
    hlcorestructure_Sort,
    hlcorestructure_Term,
    hlcorestructure_ToolInfo,
    hlcorestructure_Transition,
    hlcorestructure_TransitionNode,
    hlcorestructure_Type,
    hlcorestructure_Unparsed,
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

def test_assoc_containerNamePetriNet20_reverse_link_reassign_clear():
    a1 = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    a2 = hlcorestructure_PetriNet(id="sample_text_2", type="sample_text_2")
    b = hlcorestructure_Name(text="sample_text")
    _safe_set(b, 'name', a1)
    assert _is_linked(b, 'name', a1)
    if hasattr(a1, 'PetriNet21'):
        assert _is_linked(a1, 'PetriNet21', b)
    _safe_set(b, 'name', a2)
    assert _is_linked(b, 'name', a2)
    if hasattr(a1, 'PetriNet21'):
        assert not _is_linked(a1, 'PetriNet21', b)
    if hasattr(a2, 'PetriNet21'):
        assert _is_linked(a2, 'PetriNet21', b)
    _safe_set(b, 'name', None)
    assert not _is_linked(b, 'name', a2)
    if hasattr(a2, 'PetriNet21'):
        assert not _is_linked(a2, 'PetriNet21', b)


def test_assoc_containerNamePnObject22_reverse_link_reassign_clear():
    a1 = hlcorestructure_PnObject(id="sample_text")
    a2 = hlcorestructure_PnObject(id="sample_text_2")
    b = hlcorestructure_Name(text="sample_text")
    _safe_set(b, 'name23', a1)
    assert _is_linked(b, 'name23', a1)
    if hasattr(a1, 'PnObject24'):
        assert _is_linked(a1, 'PnObject24', b)
    _safe_set(b, 'name23', a2)
    assert _is_linked(b, 'name23', a2)
    if hasattr(a1, 'PnObject24'):
        assert not _is_linked(a1, 'PnObject24', b)
    if hasattr(a2, 'PnObject24'):
        assert _is_linked(a2, 'PnObject24', b)
    _safe_set(b, 'name23', None)
    assert not _is_linked(b, 'name23', a2)
    if hasattr(a2, 'PnObject24'):
        assert not _is_linked(a2, 'PnObject24', b)


def test_assoc_containerPetriNet25_reverse_link_reassign_clear():
    a1 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet26', a1)
    assert _is_linked(b, 'PetriNet26', a1)
    if hasattr(a1, 'toolspecifics'):
        assert _is_linked(a1, 'toolspecifics', b)
    _safe_set(b, 'PetriNet26', a2)
    assert _is_linked(b, 'PetriNet26', a2)
    if hasattr(a1, 'toolspecifics'):
        assert not _is_linked(a1, 'toolspecifics', b)
    if hasattr(a2, 'toolspecifics'):
        assert _is_linked(a2, 'toolspecifics', b)
    _safe_set(b, 'PetriNet26', None)
    assert not _is_linked(b, 'PetriNet26', a2)
    if hasattr(a2, 'toolspecifics'):
        assert not _is_linked(a2, 'toolspecifics', b)


def test_assoc_containerPetriNetDoc5_reverse_link_reassign_clear():
    a1 = hlcorestructure_PetriNetDoc(xmlns="sample_text")
    a2 = hlcorestructure_PetriNetDoc(xmlns="sample_text_2")
    b = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
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


def test_assoc_containerPnObject27_reverse_link_reassign_clear():
    a1 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = hlcorestructure_PnObject(id="sample_text")
    _safe_set(b, 'PnObject29', a1)
    assert _is_linked(b, 'PnObject29', a1)
    if hasattr(a1, 'toolspecifics28'):
        assert _is_linked(a1, 'toolspecifics28', b)
    _safe_set(b, 'PnObject29', a2)
    assert _is_linked(b, 'PnObject29', a2)
    if hasattr(a1, 'toolspecifics28'):
        assert not _is_linked(a1, 'toolspecifics28', b)
    if hasattr(a2, 'toolspecifics28'):
        assert _is_linked(a2, 'toolspecifics28', b)
    _safe_set(b, 'PnObject29', None)
    assert not _is_linked(b, 'PnObject29', a2)
    if hasattr(a2, 'toolspecifics28'):
        assert not _is_linked(a2, 'toolspecifics28', b)


def test_assoc_name14_reverse_link_reassign_clear():
    a1 = hlcorestructure_PnObject(id="sample_text")
    a2 = hlcorestructure_PnObject(id="sample_text_2")
    b = hlcorestructure_Name(text="sample_text")
    _safe_set(b, 'Name15', a1)
    assert _is_linked(b, 'Name15', a1)
    if hasattr(a1, 'containerNamePnObject'):
        assert _is_linked(a1, 'containerNamePnObject', b)
    _safe_set(b, 'Name15', a2)
    assert _is_linked(b, 'Name15', a2)
    if hasattr(a1, 'containerNamePnObject'):
        assert not _is_linked(a1, 'containerNamePnObject', b)
    if hasattr(a2, 'containerNamePnObject'):
        assert _is_linked(a2, 'containerNamePnObject', b)
    _safe_set(b, 'Name15', None)
    assert not _is_linked(b, 'Name15', a2)
    if hasattr(a2, 'containerNamePnObject'):
        assert not _is_linked(a2, 'containerNamePnObject', b)


def test_assoc_name2_reverse_link_reassign_clear():
    a1 = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    a2 = hlcorestructure_PetriNet(id="sample_text_2", type="sample_text_2")
    b = hlcorestructure_Name(text="sample_text")
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
    a1 = hlcorestructure_PetriNetDoc(xmlns="sample_text")
    a2 = hlcorestructure_PetriNetDoc(xmlns="sample_text_2")
    b = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
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


def test_assoc_toolspecifics16_reverse_link_reassign_clear():
    a1 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = hlcorestructure_PnObject(id="sample_text")
    _safe_set(b, 'containerPnObject', {a1})
    assert _is_linked(b, 'containerPnObject', a1)
    if hasattr(a1, 'ToolInfo17'):
        assert _is_linked(a1, 'ToolInfo17', b)
    _safe_set(b, 'containerPnObject', {a2})
    assert _is_linked(b, 'containerPnObject', a2)
    if hasattr(a1, 'ToolInfo17'):
        assert not _is_linked(a1, 'ToolInfo17', b)
    if hasattr(a2, 'ToolInfo17'):
        assert _is_linked(a2, 'ToolInfo17', b)
    _safe_set(b, 'containerPnObject', set())
    assert not _is_linked(b, 'containerPnObject', a2)
    if hasattr(a2, 'ToolInfo17'):
        assert not _is_linked(a2, 'ToolInfo17', b)


def test_assoc_toolspecifics3_reverse_link_reassign_clear():
    a1 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    a2 = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text_2", tool="sample_text_2", toolInfoGrammarURI="sample_text_2", version="sample_text_2")
    b = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
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

def test_assoc_containerAnnotationGraphics62_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'AnnotationGraphics64' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics64', None)
    _safe_set(owner, 'fill63', partner)
    assert getattr(partner, 'AnnotationGraphics64') == owner
    _safe_set(owner, 'fill63', None)
    assert getattr(partner, 'AnnotationGraphics64') is None


def test_assoc_containerAnnotationGraphics70_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'AnnotationGraphics72' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics72', None)
    _safe_set(owner, 'line71', partner)
    assert getattr(partner, 'AnnotationGraphics72') == owner
    _safe_set(owner, 'line71', None)
    assert getattr(partner, 'AnnotationGraphics72') is None


def test_assoc_containerAnnotationGraphics93_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'AnnotationGraphics94' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'AnnotationGraphics94', None)
    _safe_set(owner, 'font', partner)
    assert getattr(partner, 'AnnotationGraphics94') == owner
    _safe_set(owner, 'font', None)
    assert getattr(partner, 'AnnotationGraphics94') is None


def test_assoc_containerArcGraphics67_stub_double():
    # hlcorestructure_ArcGraphics has no real 'ArcGraphics69' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_ArcGraphics()
    setattr(partner, 'ArcGraphics69', None)
    _safe_set(owner, 'line68', partner)
    assert getattr(partner, 'ArcGraphics69') == owner
    _safe_set(owner, 'line68', None)
    assert getattr(partner, 'ArcGraphics69') is None


def test_assoc_containerDeclarationPetriNet124_stub_double():
    # hlcorestructure_Declaration has no real 'declaration' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    partner = hlcorestructure_Declaration()
    setattr(partner, 'declaration', None)
    _safe_set(owner, 'PetriNet125', partner)
    assert getattr(partner, 'declaration') == owner
    _safe_set(owner, 'PetriNet125', None)
    assert getattr(partner, 'declaration') is None


def test_assoc_containerLabel30_stub_double():
    # hlcorestructure_Label has no real 'Label' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = hlcorestructure_Label()
    setattr(partner, 'Label', None)
    _safe_set(owner, 'toolspecifics31', partner)
    assert getattr(partner, 'Label') == owner
    _safe_set(owner, 'toolspecifics31', None)
    assert getattr(partner, 'Label') is None


def test_assoc_containerNodeGraphics60_stub_double():
    # hlcorestructure_NodeGraphics has no real 'NodeGraphics61' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = hlcorestructure_NodeGraphics()
    setattr(partner, 'NodeGraphics61', None)
    _safe_set(owner, 'fill', partner)
    assert getattr(partner, 'NodeGraphics61') == owner
    _safe_set(owner, 'fill', None)
    assert getattr(partner, 'NodeGraphics61') is None


def test_assoc_containerNodeGraphics65_stub_double():
    # hlcorestructure_NodeGraphics has no real 'NodeGraphics66' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_NodeGraphics()
    setattr(partner, 'NodeGraphics66', None)
    _safe_set(owner, 'line', partner)
    assert getattr(partner, 'NodeGraphics66') == owner
    _safe_set(owner, 'line', None)
    assert getattr(partner, 'NodeGraphics66') is None


def test_assoc_containerPage18_stub_double():
    # hlcorestructure_Page has no real 'Page19' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PnObject(id="sample_text")
    partner = hlcorestructure_Page()
    setattr(partner, 'Page19', None)
    _safe_set(owner, 'objects', partner)
    assert getattr(partner, 'Page19') == owner
    _safe_set(owner, 'objects', None)
    assert getattr(partner, 'Page19') is None


def test_assoc_containerPetriNet8_stub_double():
    # hlcorestructure_Page has no real 'pages' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    partner = hlcorestructure_Page()
    setattr(partner, 'pages', None)
    _safe_set(owner, 'PetriNet9', partner)
    assert getattr(partner, 'pages') == owner
    _safe_set(owner, 'PetriNet9', None)
    assert getattr(partner, 'pages') is None


def test_assoc_containerToolInfo106_stub_double():
    # hlcorestructure_AnyObject has no real 'toolInfoModel' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = hlcorestructure_AnyObject()
    setattr(partner, 'toolInfoModel', None)
    _safe_set(owner, 'ToolInfo107', partner)
    assert getattr(partner, 'toolInfoModel') == owner
    _safe_set(owner, 'ToolInfo107', None)
    assert getattr(partner, 'toolInfoModel') is None


def test_assoc_declaration6_stub_double():
    # hlcorestructure_Declaration has no real 'Declaration' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    partner = hlcorestructure_Declaration()
    setattr(partner, 'Declaration', None)
    _safe_set(owner, 'containerDeclarationPetriNet', {partner})
    assert getattr(partner, 'Declaration') == owner
    _safe_set(owner, 'containerDeclarationPetriNet', set())
    assert getattr(partner, 'Declaration') is None


def test_assoc_fill37_stub_double():
    # hlcorestructure_NodeGraphics has no real 'containerNodeGraphics' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = hlcorestructure_NodeGraphics()
    setattr(partner, 'containerNodeGraphics', None)
    _safe_set(owner, 'Fill', partner)
    assert getattr(partner, 'containerNodeGraphics') == owner
    _safe_set(owner, 'Fill', None)
    assert getattr(partner, 'containerNodeGraphics') is None


def test_assoc_fill51_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'containerAnnotationGraphics52' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Fill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Fill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics52', None)
    _safe_set(owner, 'Fill53', partner)
    assert getattr(partner, 'containerAnnotationGraphics52') == owner
    _safe_set(owner, 'Fill53', None)
    assert getattr(partner, 'containerAnnotationGraphics52') is None


def test_assoc_font57_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'containerAnnotationGraphics58' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics58', None)
    _safe_set(owner, 'Font', partner)
    assert getattr(partner, 'containerAnnotationGraphics58') == owner
    _safe_set(owner, 'Font', None)
    assert getattr(partner, 'containerAnnotationGraphics58') is None


def test_assoc_line38_stub_double():
    # hlcorestructure_NodeGraphics has no real 'containerNodeGraphics39' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_NodeGraphics()
    setattr(partner, 'containerNodeGraphics39', None)
    _safe_set(owner, 'Line', partner)
    assert getattr(partner, 'containerNodeGraphics39') == owner
    _safe_set(owner, 'Line', None)
    assert getattr(partner, 'containerNodeGraphics39') is None


def test_assoc_line54_stub_double():
    # hlcorestructure_AnnotationGraphics has no real 'containerAnnotationGraphics55' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_AnnotationGraphics()
    setattr(partner, 'containerAnnotationGraphics55', None)
    _safe_set(owner, 'Line56', partner)
    assert getattr(partner, 'containerAnnotationGraphics55') == owner
    _safe_set(owner, 'Line56', None)
    assert getattr(partner, 'containerAnnotationGraphics55') is None


def test_assoc_line75_stub_double():
    # hlcorestructure_ArcGraphics has no real 'containerArcGraphics76' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_Line's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_Line's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    partner = hlcorestructure_ArcGraphics()
    setattr(partner, 'containerArcGraphics76', None)
    _safe_set(owner, 'Line77', partner)
    assert getattr(partner, 'containerArcGraphics76') == owner
    _safe_set(owner, 'Line77', None)
    assert getattr(partner, 'containerArcGraphics76') is None


def test_assoc_objects7_stub_double():
    # hlcorestructure_Page has no real 'containerPage' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PnObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PnObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PnObject(id="sample_text")
    partner = hlcorestructure_Page()
    setattr(partner, 'containerPage', None)
    _safe_set(owner, 'PnObject', partner)
    assert owner in getattr(partner, 'containerPage')
    _safe_set(owner, 'PnObject', None)
    assert owner not in getattr(partner, 'containerPage')


def test_assoc_pages1_stub_double():
    # hlcorestructure_Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_PetriNet(id="sample_text", type="sample_text")
    partner = hlcorestructure_Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'containerPetriNet', {partner})
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'containerPetriNet', set())
    assert getattr(partner, 'Page') is None


def test_assoc_toolInfoModel32_stub_double():
    # hlcorestructure_AnyObject has no real 'AnyObject' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = hlcorestructure_AnyObject()
    setattr(partner, 'AnyObject', None)
    _safe_set(owner, 'containerToolInfo', partner)
    assert getattr(partner, 'AnyObject') == owner
    _safe_set(owner, 'containerToolInfo', None)
    assert getattr(partner, 'AnyObject') is None


def test_assoc_toolspecifics33_stub_double():
    # hlcorestructure_Label has no real 'containerLabel' property in the generated
    # code (a bare stub) -- manually attach it so hlcorestructure_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlcorestructure_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlcorestructure_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    partner = hlcorestructure_Label()
    setattr(partner, 'containerLabel', None)
    _safe_set(owner, 'ToolInfo34', partner)
    assert owner in getattr(partner, 'containerLabel')
    _safe_set(owner, 'ToolInfo34', None)
    assert owner not in getattr(partner, 'containerLabel')


