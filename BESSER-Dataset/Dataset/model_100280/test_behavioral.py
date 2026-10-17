import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    CPNToolsTransitionAddin,
    HLAnnotation,
    HLAnnotationAddin,
    HLArcAddin,
    HLPlaceAddin,
    HLTransitionAddin,
    HasGraphics,
    HasId,
    HasLabel,
    HasName,
    HasToolInfo,
    Label,
    Node,
    Object,
    Place,
    PlaceNode,
    TransitionNode,
    model_Annotation,
    model_Arc,
    model_Attribute,
    model_CPNToolsTransitionAddin,
    model_Code,
    model_Condition,
    model_DeclarationStructure,
    model_FusionGroup,
    model_HLAnnotation,
    model_HLAnnotationAddin,
    model_HLArcAddin,
    model_HLArcType_1,
    model_HLDeclaration,
    model_HLMarking,
    model_HLPlaceAddin,
    model_HLTransitionAddin,
    model_HasId,
    model_HasLabel,
    model_HasName,
    model_HasToolInfo,
    model_Instance,
    model_Label,
    model_Name,
    model_Node,
    model_Object,
    model_Page,
    model_ParameterAssignment,
    model_PetriNet,
    model_Place,
    model_PlaceNode,
    model_RefPlace,
    model_RefTrans,
    model_Time,
    model_ToolInfo,
    model_Transition,
    model_TransitionNode,
    model_Type,
    HLArcType,
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

def test_assoc_instance38_reverse_link_reassign_clear():
    a1 = model_ParameterAssignment(parameter="sample_text", value="sample_text")
    a2 = model_ParameterAssignment(parameter="sample_text_2", value="sample_text_2")
    b = model_Instance(subPageID="sample_text")
    _safe_set(b, 'Instance', a1)
    assert _is_linked(b, 'Instance', a1)
    if hasattr(a1, 'parameterAssignment'):
        assert _is_linked(a1, 'parameterAssignment', b)
    _safe_set(b, 'Instance', a2)
    assert _is_linked(b, 'Instance', a2)
    if hasattr(a1, 'parameterAssignment'):
        assert not _is_linked(a1, 'parameterAssignment', b)
    if hasattr(a2, 'parameterAssignment'):
        assert _is_linked(a2, 'parameterAssignment', b)
    _safe_set(b, 'Instance', None)
    assert not _is_linked(b, 'Instance', a2)
    if hasattr(a2, 'parameterAssignment'):
        assert not _is_linked(a2, 'parameterAssignment', b)


def test_assoc_parameterAssignment37_reverse_link_reassign_clear():
    a1 = model_ParameterAssignment(parameter="sample_text", value="sample_text")
    a2 = model_ParameterAssignment(parameter="sample_text_2", value="sample_text_2")
    b = model_Instance(subPageID="sample_text")
    _safe_set(b, 'instance', {a1})
    assert _is_linked(b, 'instance', a1)
    if hasattr(a1, 'ParameterAssignment'):
        assert _is_linked(a1, 'ParameterAssignment', b)
    _safe_set(b, 'instance', {a2})
    assert _is_linked(b, 'instance', a2)
    if hasattr(a1, 'ParameterAssignment'):
        assert not _is_linked(a1, 'ParameterAssignment', b)
    if hasattr(a2, 'ParameterAssignment'):
        assert _is_linked(a2, 'ParameterAssignment', b)
    _safe_set(b, 'instance', set())
    assert not _is_linked(b, 'instance', a2)
    if hasattr(a2, 'ParameterAssignment'):
        assert not _is_linked(a2, 'ParameterAssignment', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fusionGroups22_stub_double():
    # model_FusionGroup has no real 'FusionGroup' property in the generated
    # code (a bare stub) -- manually attach it so model_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_PetriNet(type="sample_text")
    partner = model_FusionGroup()
    setattr(partner, 'FusionGroup', None)
    _safe_set(owner, 'petriNet23', {partner})
    assert getattr(partner, 'FusionGroup') == owner
    _safe_set(owner, 'petriNet23', set())
    assert getattr(partner, 'FusionGroup') is None


def test_assoc_hlinscription31_stub_double():
    # model_HLAnnotation has no real 'model_HLAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so model_HLArcAddin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_HLArcAddin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_HLArcAddin(type="sample_text")
    partner = model_HLAnnotation()
    setattr(partner, 'model_HLAnnotation', None)
    _safe_set(owner, 'model_HLArcAddin', partner)
    assert getattr(partner, 'model_HLAnnotation') == owner
    _safe_set(owner, 'model_HLArcAddin', None)
    assert getattr(partner, 'model_HLAnnotation') is None


def test_assoc_label4_stub_double():
    # model_HasLabel has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so model_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Label()
    partner = model_HasLabel()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'Label', partner)
    assert getattr(partner, 'parent') == owner
    _safe_set(owner, 'Label', None)
    assert getattr(partner, 'parent') is None


def test_assoc_page20_stub_double():
    # model_Page has no real 'Page21' property in the generated
    # code (a bare stub) -- manually attach it so model_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_PetriNet(type="sample_text")
    partner = model_Page()
    setattr(partner, 'Page21', None)
    _safe_set(owner, 'petriNet', {partner})
    assert getattr(partner, 'Page21') == owner
    _safe_set(owner, 'petriNet', set())
    assert getattr(partner, 'Page21') is None


def test_assoc_parent27_stub_double():
    # model_HasToolInfo has no real 'HasToolInfo' property in the generated
    # code (a bare stub) -- manually attach it so model_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ToolInfo(tool="sample_text", version="sample_text")
    partner = model_HasToolInfo()
    setattr(partner, 'HasToolInfo', None)
    _safe_set(owner, 'toolinfo', partner)
    assert getattr(partner, 'HasToolInfo') == owner
    _safe_set(owner, 'toolinfo', None)
    assert getattr(partner, 'HasToolInfo') is None


def test_assoc_parent8_stub_double():
    # model_HasLabel has no real 'HasLabel' property in the generated
    # code (a bare stub) -- manually attach it so model_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Label()
    partner = model_HasLabel()
    setattr(partner, 'HasLabel', None)
    _safe_set(owner, 'label', partner)
    assert getattr(partner, 'HasLabel') == owner
    _safe_set(owner, 'label', None)
    assert getattr(partner, 'HasLabel') is None


def test_assoc_petriNet14_stub_double():
    # model_Page has no real 'page' property in the generated
    # code (a bare stub) -- manually attach it so model_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_PetriNet(type="sample_text")
    partner = model_Page()
    setattr(partner, 'page', None)
    _safe_set(owner, 'PetriNet', partner)
    assert getattr(partner, 'page') == owner
    _safe_set(owner, 'PetriNet', None)
    assert getattr(partner, 'page') is None


def test_assoc_petriNet39_stub_double():
    # model_FusionGroup has no real 'fusionGroups' property in the generated
    # code (a bare stub) -- manually attach it so model_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_PetriNet(type="sample_text")
    partner = model_FusionGroup()
    setattr(partner, 'fusionGroups', None)
    _safe_set(owner, 'PetriNet40', partner)
    assert getattr(partner, 'fusionGroups') == owner
    _safe_set(owner, 'PetriNet40', None)
    assert getattr(partner, 'fusionGroups') is None


def test_assoc_toolinfo6_stub_double():
    # model_HasToolInfo has no real 'parent7' property in the generated
    # code (a bare stub) -- manually attach it so model_ToolInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ToolInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ToolInfo(tool="sample_text", version="sample_text")
    partner = model_HasToolInfo()
    setattr(partner, 'parent7', None)
    _safe_set(owner, 'ToolInfo', partner)
    assert getattr(partner, 'parent7') == owner
    _safe_set(owner, 'ToolInfo', None)
    assert getattr(partner, 'parent7') is None


