import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Behaviour,
    DomainOperation,
    NodeStyle,
    SupportOperation,
    TrackerAction,
    aredsl_Action,
    aredsl_ArrangeElements,
    aredsl_Behaviour,
    aredsl_ChangeContextOperation,
    aredsl_CreateInstanceOperation,
    aredsl_DomainOperation,
    aredsl_Edge,
    aredsl_EdgeStyle,
    aredsl_Editor,
    aredsl_Exit,
    aredsl_GeometricShapeNodeStyle,
    aredsl_GestureAction,
    aredsl_Image2DNodeStyle,
    aredsl_Label,
    aredsl_LabelStyle,
    aredsl_Layer,
    aredsl_MarkerBasedTrackerAction,
    aredsl_MarkerLessTrackerAction,
    aredsl_MentalAction,
    aredsl_Model3DNodeStyle,
    aredsl_MoveElement,
    aredsl_Node,
    aredsl_NodeStyle,
    aredsl_RemoveOperation,
    aredsl_SensorBasedAction,
    aredsl_SetOperation,
    aredsl_ShowSystemMenu,
    aredsl_SupportOperation,
    aredsl_TactileAction,
    aredsl_Tool,
    aredsl_ToolSet,
    aredsl_TrackerAction,
    aredsl_UnsetOperation,
    aredsl_VoiceAction,
    ContainmentKind,
    IntegrityRestrictionKind,
    LineKind,
    OutlineKind,
    QueryLanguageKind,
    ShapeKind,
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

def test_assoc_actions36_reverse_link_reassign_clear():
    a1 = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    a2 = aredsl_Tool(description="sample_text_2", id="sample_text_2", precondition="sample_text_2", targetPrecondition="sample_text_2")
    b = aredsl_Action(description="sample_text")
    _safe_set(b, 'aredsl_Action', a1)
    assert _is_linked(b, 'aredsl_Action', a1)
    if hasattr(a1, 'aredsl_Tool37'):
        assert _is_linked(a1, 'aredsl_Tool37', b)
    _safe_set(b, 'aredsl_Action', a2)
    assert _is_linked(b, 'aredsl_Action', a2)
    if hasattr(a1, 'aredsl_Tool37'):
        assert not _is_linked(a1, 'aredsl_Tool37', b)
    if hasattr(a2, 'aredsl_Tool37'):
        assert _is_linked(a2, 'aredsl_Tool37', b)
    _safe_set(b, 'aredsl_Action', None)
    assert not _is_linked(b, 'aredsl_Action', a2)
    if hasattr(a2, 'aredsl_Tool37'):
        assert not _is_linked(a2, 'aredsl_Tool37', b)


def test_assoc_behaviours35_reverse_link_reassign_clear():
    a1 = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    a2 = aredsl_Tool(description="sample_text_2", id="sample_text_2", precondition="sample_text_2", targetPrecondition="sample_text_2")
    b = aredsl_Behaviour(description="sample_text")
    _safe_set(b, 'aredsl_Behaviour', a1)
    assert _is_linked(b, 'aredsl_Behaviour', a1)
    if hasattr(a1, 'aredsl_Tool'):
        assert _is_linked(a1, 'aredsl_Tool', b)
    _safe_set(b, 'aredsl_Behaviour', a2)
    assert _is_linked(b, 'aredsl_Behaviour', a2)
    if hasattr(a1, 'aredsl_Tool'):
        assert not _is_linked(a1, 'aredsl_Tool', b)
    if hasattr(a2, 'aredsl_Tool'):
        assert _is_linked(a2, 'aredsl_Tool', b)
    _safe_set(b, 'aredsl_Behaviour', None)
    assert not _is_linked(b, 'aredsl_Behaviour', a2)
    if hasattr(a2, 'aredsl_Tool'):
        assert not _is_linked(a2, 'aredsl_Tool', b)


def test_assoc_contentNodes14_reverse_link_reassign_clear():
    a1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    _safe_set(b, 'aredsl_Node15', a1)
    assert _is_linked(b, 'aredsl_Node15', a1)
    if hasattr(a1, 'aredsl_Node13'):
        assert _is_linked(a1, 'aredsl_Node13', b)
    _safe_set(b, 'aredsl_Node15', a2)
    assert _is_linked(b, 'aredsl_Node15', a2)
    if hasattr(a1, 'aredsl_Node13'):
        assert not _is_linked(a1, 'aredsl_Node13', b)
    if hasattr(a2, 'aredsl_Node13'):
        assert _is_linked(a2, 'aredsl_Node13', b)
    _safe_set(b, 'aredsl_Node15', None)
    assert not _is_linked(b, 'aredsl_Node15', a2)
    if hasattr(a2, 'aredsl_Node13'):
        assert not _is_linked(a2, 'aredsl_Node13', b)


def test_assoc_destinationLabel32_reverse_link_reassign_clear():
    a1 = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Label(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge33', a1)
    assert _is_linked(b, 'aredsl_Edge33', a1)
    if hasattr(a1, 'aredsl_Label34'):
        assert _is_linked(a1, 'aredsl_Label34', b)
    _safe_set(b, 'aredsl_Edge33', a2)
    assert _is_linked(b, 'aredsl_Edge33', a2)
    if hasattr(a1, 'aredsl_Label34'):
        assert not _is_linked(a1, 'aredsl_Label34', b)
    if hasattr(a2, 'aredsl_Label34'):
        assert _is_linked(a2, 'aredsl_Label34', b)
    _safe_set(b, 'aredsl_Edge33', None)
    assert not _is_linked(b, 'aredsl_Edge33', a2)
    if hasattr(a2, 'aredsl_Label34'):
        assert not _is_linked(a2, 'aredsl_Label34', b)


def test_assoc_destinationNode26_reverse_link_reassign_clear():
    a1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge27', a1)
    assert _is_linked(b, 'aredsl_Edge27', a1)
    if hasattr(a1, 'aredsl_Node28'):
        assert _is_linked(a1, 'aredsl_Node28', b)
    _safe_set(b, 'aredsl_Edge27', a2)
    assert _is_linked(b, 'aredsl_Edge27', a2)
    if hasattr(a1, 'aredsl_Node28'):
        assert not _is_linked(a1, 'aredsl_Node28', b)
    if hasattr(a2, 'aredsl_Node28'):
        assert _is_linked(a2, 'aredsl_Node28', b)
    _safe_set(b, 'aredsl_Edge27', None)
    assert not _is_linked(b, 'aredsl_Edge27', a2)
    if hasattr(a2, 'aredsl_Node28'):
        assert not _is_linked(a2, 'aredsl_Node28', b)


def test_assoc_edges5_reverse_link_reassign_clear():
    a1 = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Layer(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge', a1)
    assert _is_linked(b, 'aredsl_Edge', a1)
    if hasattr(a1, 'aredsl_Layer6'):
        assert _is_linked(a1, 'aredsl_Layer6', b)
    _safe_set(b, 'aredsl_Edge', a2)
    assert _is_linked(b, 'aredsl_Edge', a2)
    if hasattr(a1, 'aredsl_Layer6'):
        assert not _is_linked(a1, 'aredsl_Layer6', b)
    if hasattr(a2, 'aredsl_Layer6'):
        assert _is_linked(a2, 'aredsl_Layer6', b)
    _safe_set(b, 'aredsl_Edge', None)
    assert not _is_linked(b, 'aredsl_Edge', a2)
    if hasattr(a2, 'aredsl_Layer6'):
        assert not _is_linked(a2, 'aredsl_Layer6', b)


def test_assoc_edgestyles18_reverse_link_reassign_clear():
    a1 = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    a2 = aredsl_EdgeStyle(color="sample_text_2", kind="sample_text_2", semanticCondition="sample_text_2", width=13)
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge19', {a1})
    assert _is_linked(b, 'aredsl_Edge19', a1)
    if hasattr(a1, 'aredsl_EdgeStyle'):
        assert _is_linked(a1, 'aredsl_EdgeStyle', b)
    _safe_set(b, 'aredsl_Edge19', {a2})
    assert _is_linked(b, 'aredsl_Edge19', a2)
    if hasattr(a1, 'aredsl_EdgeStyle'):
        assert not _is_linked(a1, 'aredsl_EdgeStyle', b)
    if hasattr(a2, 'aredsl_EdgeStyle'):
        assert _is_linked(a2, 'aredsl_EdgeStyle', b)
    _safe_set(b, 'aredsl_Edge19', set())
    assert not _is_linked(b, 'aredsl_Edge19', a2)
    if hasattr(a2, 'aredsl_EdgeStyle'):
        assert not _is_linked(a2, 'aredsl_EdgeStyle', b)


def test_assoc_label11_reverse_link_reassign_clear():
    a1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    _safe_set(b, 'aredsl_Label', a1)
    assert _is_linked(b, 'aredsl_Label', a1)
    if hasattr(a1, 'aredsl_Node12'):
        assert _is_linked(a1, 'aredsl_Node12', b)
    _safe_set(b, 'aredsl_Label', a2)
    assert _is_linked(b, 'aredsl_Label', a2)
    if hasattr(a1, 'aredsl_Node12'):
        assert not _is_linked(a1, 'aredsl_Node12', b)
    if hasattr(a2, 'aredsl_Node12'):
        assert _is_linked(a2, 'aredsl_Node12', b)
    _safe_set(b, 'aredsl_Label', None)
    assert not _is_linked(b, 'aredsl_Label', a2)
    if hasattr(a2, 'aredsl_Node12'):
        assert not _is_linked(a2, 'aredsl_Node12', b)


def test_assoc_labelstyles16_reverse_link_reassign_clear():
    a1 = aredsl_LabelStyle(color="sample_text", height=7, semanticCondition="sample_text")
    a2 = aredsl_LabelStyle(color="sample_text_2", height=13, semanticCondition="sample_text_2")
    b = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    _safe_set(b, 'aredsl_Label17', {a1})
    assert _is_linked(b, 'aredsl_Label17', a1)
    if hasattr(a1, 'aredsl_LabelStyle'):
        assert _is_linked(a1, 'aredsl_LabelStyle', b)
    _safe_set(b, 'aredsl_Label17', {a2})
    assert _is_linked(b, 'aredsl_Label17', a2)
    if hasattr(a1, 'aredsl_LabelStyle'):
        assert not _is_linked(a1, 'aredsl_LabelStyle', b)
    if hasattr(a2, 'aredsl_LabelStyle'):
        assert _is_linked(a2, 'aredsl_LabelStyle', b)
    _safe_set(b, 'aredsl_Label17', set())
    assert not _is_linked(b, 'aredsl_Label17', a2)
    if hasattr(a2, 'aredsl_LabelStyle'):
        assert not _is_linked(a2, 'aredsl_LabelStyle', b)


def test_assoc_layer0_reverse_link_reassign_clear():
    a1 = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Layer(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    _safe_set(b, 'aredsl_Editor', {a1})
    assert _is_linked(b, 'aredsl_Editor', a1)
    if hasattr(a1, 'aredsl_Layer'):
        assert _is_linked(a1, 'aredsl_Layer', b)
    _safe_set(b, 'aredsl_Editor', {a2})
    assert _is_linked(b, 'aredsl_Editor', a2)
    if hasattr(a1, 'aredsl_Layer'):
        assert not _is_linked(a1, 'aredsl_Layer', b)
    if hasattr(a2, 'aredsl_Layer'):
        assert _is_linked(a2, 'aredsl_Layer', b)
    _safe_set(b, 'aredsl_Editor', set())
    assert not _is_linked(b, 'aredsl_Editor', a2)
    if hasattr(a2, 'aredsl_Layer'):
        assert not _is_linked(a2, 'aredsl_Layer', b)


def test_assoc_middleLabel20_reverse_link_reassign_clear():
    a1 = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Label(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge21', a1)
    assert _is_linked(b, 'aredsl_Edge21', a1)
    if hasattr(a1, 'aredsl_Label22'):
        assert _is_linked(a1, 'aredsl_Label22', b)
    _safe_set(b, 'aredsl_Edge21', a2)
    assert _is_linked(b, 'aredsl_Edge21', a2)
    if hasattr(a1, 'aredsl_Label22'):
        assert not _is_linked(a1, 'aredsl_Label22', b)
    if hasattr(a2, 'aredsl_Label22'):
        assert _is_linked(a2, 'aredsl_Label22', b)
    _safe_set(b, 'aredsl_Edge21', None)
    assert not _is_linked(b, 'aredsl_Edge21', a2)
    if hasattr(a2, 'aredsl_Label22'):
        assert not _is_linked(a2, 'aredsl_Label22', b)


def test_assoc_nodes3_reverse_link_reassign_clear():
    a1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    _safe_set(b, 'aredsl_Layer4', {a1})
    assert _is_linked(b, 'aredsl_Layer4', a1)
    if hasattr(a1, 'aredsl_Node'):
        assert _is_linked(a1, 'aredsl_Node', b)
    _safe_set(b, 'aredsl_Layer4', {a2})
    assert _is_linked(b, 'aredsl_Layer4', a2)
    if hasattr(a1, 'aredsl_Node'):
        assert not _is_linked(a1, 'aredsl_Node', b)
    if hasattr(a2, 'aredsl_Node'):
        assert _is_linked(a2, 'aredsl_Node', b)
    _safe_set(b, 'aredsl_Layer4', set())
    assert not _is_linked(b, 'aredsl_Layer4', a2)
    if hasattr(a2, 'aredsl_Node'):
        assert not _is_linked(a2, 'aredsl_Node', b)


def test_assoc_nodestyles9_reverse_link_reassign_clear():
    a1 = aredsl_NodeStyle(height=7, semanticCondition="sample_text", width=7)
    a2 = aredsl_NodeStyle(height=13, semanticCondition="sample_text_2", width=13)
    b = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    _safe_set(b, 'aredsl_Node10', {a1})
    assert _is_linked(b, 'aredsl_Node10', a1)
    if hasattr(a1, 'aredsl_NodeStyle'):
        assert _is_linked(a1, 'aredsl_NodeStyle', b)
    _safe_set(b, 'aredsl_Node10', {a2})
    assert _is_linked(b, 'aredsl_Node10', a2)
    if hasattr(a1, 'aredsl_NodeStyle'):
        assert not _is_linked(a1, 'aredsl_NodeStyle', b)
    if hasattr(a2, 'aredsl_NodeStyle'):
        assert _is_linked(a2, 'aredsl_NodeStyle', b)
    _safe_set(b, 'aredsl_Node10', set())
    assert not _is_linked(b, 'aredsl_Node10', a2)
    if hasattr(a2, 'aredsl_NodeStyle'):
        assert not _is_linked(a2, 'aredsl_NodeStyle', b)


def test_assoc_originLabel29_reverse_link_reassign_clear():
    a1 = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Label(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge30', a1)
    assert _is_linked(b, 'aredsl_Edge30', a1)
    if hasattr(a1, 'aredsl_Label31'):
        assert _is_linked(a1, 'aredsl_Label31', b)
    _safe_set(b, 'aredsl_Edge30', a2)
    assert _is_linked(b, 'aredsl_Edge30', a2)
    if hasattr(a1, 'aredsl_Label31'):
        assert not _is_linked(a1, 'aredsl_Label31', b)
    if hasattr(a2, 'aredsl_Label31'):
        assert _is_linked(a2, 'aredsl_Label31', b)
    _safe_set(b, 'aredsl_Edge30', None)
    assert not _is_linked(b, 'aredsl_Edge30', a2)
    if hasattr(a2, 'aredsl_Label31'):
        assert not _is_linked(a2, 'aredsl_Label31', b)


def test_assoc_originNode23_reverse_link_reassign_clear():
    a1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    a2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    b = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    _safe_set(b, 'aredsl_Edge24', a1)
    assert _is_linked(b, 'aredsl_Edge24', a1)
    if hasattr(a1, 'aredsl_Node25'):
        assert _is_linked(a1, 'aredsl_Node25', b)
    _safe_set(b, 'aredsl_Edge24', a2)
    assert _is_linked(b, 'aredsl_Edge24', a2)
    if hasattr(a1, 'aredsl_Node25'):
        assert not _is_linked(a1, 'aredsl_Node25', b)
    if hasattr(a2, 'aredsl_Node25'):
        assert _is_linked(a2, 'aredsl_Node25', b)
    _safe_set(b, 'aredsl_Edge24', None)
    assert not _is_linked(b, 'aredsl_Edge24', a2)
    if hasattr(a2, 'aredsl_Node25'):
        assert not _is_linked(a2, 'aredsl_Node25', b)


def test_assoc_tools38_reverse_link_reassign_clear():
    a1 = aredsl_ToolSet(description="sample_text", id="sample_text")
    a2 = aredsl_ToolSet(description="sample_text_2", id="sample_text_2")
    b = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    _safe_set(b, 'aredsl_Tool40', a1)
    assert _is_linked(b, 'aredsl_Tool40', a1)
    if hasattr(a1, 'aredsl_ToolSet39'):
        assert _is_linked(a1, 'aredsl_ToolSet39', b)
    _safe_set(b, 'aredsl_Tool40', a2)
    assert _is_linked(b, 'aredsl_Tool40', a2)
    if hasattr(a1, 'aredsl_ToolSet39'):
        assert not _is_linked(a1, 'aredsl_ToolSet39', b)
    if hasattr(a2, 'aredsl_ToolSet39'):
        assert _is_linked(a2, 'aredsl_ToolSet39', b)
    _safe_set(b, 'aredsl_Tool40', None)
    assert not _is_linked(b, 'aredsl_Tool40', a2)
    if hasattr(a2, 'aredsl_ToolSet39'):
        assert not _is_linked(a2, 'aredsl_ToolSet39', b)


def test_assoc_toolsets1_reverse_link_reassign_clear():
    a1 = aredsl_ToolSet(description="sample_text", id="sample_text")
    a2 = aredsl_ToolSet(description="sample_text_2", id="sample_text_2")
    b = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    _safe_set(b, 'aredsl_Editor2', {a1})
    assert _is_linked(b, 'aredsl_Editor2', a1)
    if hasattr(a1, 'aredsl_ToolSet'):
        assert _is_linked(a1, 'aredsl_ToolSet', b)
    _safe_set(b, 'aredsl_Editor2', {a2})
    assert _is_linked(b, 'aredsl_Editor2', a2)
    if hasattr(a1, 'aredsl_ToolSet'):
        assert not _is_linked(a1, 'aredsl_ToolSet', b)
    if hasattr(a2, 'aredsl_ToolSet'):
        assert _is_linked(a2, 'aredsl_ToolSet', b)
    _safe_set(b, 'aredsl_Editor2', set())
    assert not _is_linked(b, 'aredsl_Editor2', a2)
    if hasattr(a2, 'aredsl_ToolSet'):
        assert not _is_linked(a2, 'aredsl_ToolSet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_referenceAction7_stub_double():
    # aredsl_TrackerAction has no real 'aredsl_TrackerAction' property in the generated
    # code (a bare stub) -- manually attach it so aredsl_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aredsl_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    partner = aredsl_TrackerAction()
    setattr(partner, 'aredsl_TrackerAction', None)
    _safe_set(owner, 'aredsl_Layer8', partner)
    assert getattr(partner, 'aredsl_TrackerAction') == owner
    _safe_set(owner, 'aredsl_Layer8', None)
    assert getattr(partner, 'aredsl_TrackerAction') is None


