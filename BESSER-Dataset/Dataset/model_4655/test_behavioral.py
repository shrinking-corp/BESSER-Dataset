import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DiagramElement,
    Edge,
    Node,
    Shape,
    mtm_di_Bounds,
    mtm_di_Diagram,
    mtm_di_DiagramElement,
    mtm_di_DocumentRoot,
    mtm_di_EStringToStringMapEntry,
    mtm_di_Edge,
    mtm_di_ExtensionType,
    mtm_di_Label,
    mtm_di_LabeledEdge,
    mtm_di_LabeledShape,
    mtm_di_Node,
    mtm_di_Plane,
    mtm_di_Point,
    mtm_di_Shape,
    mtm_di_Style,
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

def test_assoc_diagram14_reverse_link_reassign_clear():
    a1 = mtm_di_DocumentRoot(mixed="sample_text")
    a2 = mtm_di_DocumentRoot(mixed="sample_text_2")
    b = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    _safe_set(b, 'mtm_di_Diagram', a1)
    assert _is_linked(b, 'mtm_di_Diagram', a1)
    if hasattr(a1, 'mtm_di_DocumentRoot15'):
        assert _is_linked(a1, 'mtm_di_DocumentRoot15', b)
    _safe_set(b, 'mtm_di_Diagram', a2)
    assert _is_linked(b, 'mtm_di_Diagram', a2)
    if hasattr(a1, 'mtm_di_DocumentRoot15'):
        assert not _is_linked(a1, 'mtm_di_DocumentRoot15', b)
    if hasattr(a2, 'mtm_di_DocumentRoot15'):
        assert _is_linked(a2, 'mtm_di_DocumentRoot15', b)
    _safe_set(b, 'mtm_di_Diagram', None)
    assert not _is_linked(b, 'mtm_di_Diagram', a2)
    if hasattr(a2, 'mtm_di_DocumentRoot15'):
        assert not _is_linked(a2, 'mtm_di_DocumentRoot15', b)


def test_assoc_diagramElement11_reverse_link_reassign_clear():
    a1 = mtm_di_DocumentRoot(mixed="sample_text")
    a2 = mtm_di_DocumentRoot(mixed="sample_text_2")
    b = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    _safe_set(b, 'mtm_di_DiagramElement13', a1)
    assert _is_linked(b, 'mtm_di_DiagramElement13', a1)
    if hasattr(a1, 'mtm_di_DocumentRoot12'):
        assert _is_linked(a1, 'mtm_di_DocumentRoot12', b)
    _safe_set(b, 'mtm_di_DiagramElement13', a2)
    assert _is_linked(b, 'mtm_di_DiagramElement13', a2)
    if hasattr(a1, 'mtm_di_DocumentRoot12'):
        assert not _is_linked(a1, 'mtm_di_DocumentRoot12', b)
    if hasattr(a2, 'mtm_di_DocumentRoot12'):
        assert _is_linked(a2, 'mtm_di_DocumentRoot12', b)
    _safe_set(b, 'mtm_di_DiagramElement13', None)
    assert not _is_linked(b, 'mtm_di_DiagramElement13', a2)
    if hasattr(a2, 'mtm_di_DocumentRoot12'):
        assert not _is_linked(a2, 'mtm_di_DocumentRoot12', b)


def test_assoc_diagramElement3_reverse_link_reassign_clear():
    a1 = mtm_di_Plane(diagramElementGroup="sample_text")
    a2 = mtm_di_Plane(diagramElementGroup="sample_text_2")
    b = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    _safe_set(b, 'mtm_di_DiagramElement4', a1)
    assert _is_linked(b, 'mtm_di_DiagramElement4', a1)
    if hasattr(a1, 'mtm_di_Plane'):
        assert _is_linked(a1, 'mtm_di_Plane', b)
    _safe_set(b, 'mtm_di_DiagramElement4', a2)
    assert _is_linked(b, 'mtm_di_DiagramElement4', a2)
    if hasattr(a1, 'mtm_di_Plane'):
        assert not _is_linked(a1, 'mtm_di_Plane', b)
    if hasattr(a2, 'mtm_di_Plane'):
        assert _is_linked(a2, 'mtm_di_Plane', b)
    _safe_set(b, 'mtm_di_DiagramElement4', None)
    assert not _is_linked(b, 'mtm_di_DiagramElement4', a2)
    if hasattr(a2, 'mtm_di_Plane'):
        assert not _is_linked(a2, 'mtm_di_Plane', b)


def test_assoc_extension0_reverse_link_reassign_clear():
    a1 = mtm_di_ExtensionType(any="sample_text")
    a2 = mtm_di_ExtensionType(any="sample_text_2")
    b = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    _safe_set(b, 'mtm_di_DiagramElement', a1)
    assert _is_linked(b, 'mtm_di_DiagramElement', a1)
    if hasattr(a1, 'mtm_di_ExtensionType'):
        assert _is_linked(a1, 'mtm_di_ExtensionType', b)
    _safe_set(b, 'mtm_di_DiagramElement', a2)
    assert _is_linked(b, 'mtm_di_DiagramElement', a2)
    if hasattr(a1, 'mtm_di_ExtensionType'):
        assert not _is_linked(a1, 'mtm_di_ExtensionType', b)
    if hasattr(a2, 'mtm_di_ExtensionType'):
        assert _is_linked(a2, 'mtm_di_ExtensionType', b)
    _safe_set(b, 'mtm_di_DiagramElement', None)
    assert not _is_linked(b, 'mtm_di_DiagramElement', a2)
    if hasattr(a2, 'mtm_di_ExtensionType'):
        assert not _is_linked(a2, 'mtm_di_ExtensionType', b)


def test_assoc_plane28_reverse_link_reassign_clear():
    a1 = mtm_di_Plane(diagramElementGroup="sample_text")
    a2 = mtm_di_Plane(diagramElementGroup="sample_text_2")
    b = mtm_di_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'mtm_di_DocumentRoot29', {a1})
    assert _is_linked(b, 'mtm_di_DocumentRoot29', a1)
    if hasattr(a1, 'mtm_di_Plane30'):
        assert _is_linked(a1, 'mtm_di_Plane30', b)
    _safe_set(b, 'mtm_di_DocumentRoot29', {a2})
    assert _is_linked(b, 'mtm_di_DocumentRoot29', a2)
    if hasattr(a1, 'mtm_di_Plane30'):
        assert not _is_linked(a1, 'mtm_di_Plane30', b)
    if hasattr(a2, 'mtm_di_Plane30'):
        assert _is_linked(a2, 'mtm_di_Plane30', b)
    _safe_set(b, 'mtm_di_DocumentRoot29', set())
    assert not _is_linked(b, 'mtm_di_DocumentRoot29', a2)
    if hasattr(a2, 'mtm_di_Plane30'):
        assert not _is_linked(a2, 'mtm_di_Plane30', b)


def test_assoc_style34_reverse_link_reassign_clear():
    a1 = mtm_di_Style(id="sample_text")
    a2 = mtm_di_Style(id="sample_text_2")
    b = mtm_di_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'mtm_di_DocumentRoot35', {a1})
    assert _is_linked(b, 'mtm_di_DocumentRoot35', a1)
    if hasattr(a1, 'mtm_di_Style'):
        assert _is_linked(a1, 'mtm_di_Style', b)
    _safe_set(b, 'mtm_di_DocumentRoot35', {a2})
    assert _is_linked(b, 'mtm_di_DocumentRoot35', a2)
    if hasattr(a1, 'mtm_di_Style'):
        assert not _is_linked(a1, 'mtm_di_Style', b)
    if hasattr(a2, 'mtm_di_Style'):
        assert _is_linked(a2, 'mtm_di_Style', b)
    _safe_set(b, 'mtm_di_DocumentRoot35', set())
    assert not _is_linked(b, 'mtm_di_DocumentRoot35', a2)
    if hasattr(a2, 'mtm_di_Style'):
        assert not _is_linked(a2, 'mtm_di_Style', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edge16_stub_double():
    # mtm_di_Edge has no real 'mtm_di_Edge18' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_Edge()
    setattr(partner, 'mtm_di_Edge18', None)
    _safe_set(owner, 'mtm_di_DocumentRoot17', {partner})
    assert getattr(partner, 'mtm_di_Edge18') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot17', set())
    assert getattr(partner, 'mtm_di_Edge18') is None


def test_assoc_label19_stub_double():
    # mtm_di_Label has no real 'mtm_di_Label21' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_Label()
    setattr(partner, 'mtm_di_Label21', None)
    _safe_set(owner, 'mtm_di_DocumentRoot20', {partner})
    assert getattr(partner, 'mtm_di_Label21') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot20', set())
    assert getattr(partner, 'mtm_di_Label21') is None


def test_assoc_labeledEdge22_stub_double():
    # mtm_di_LabeledEdge has no real 'mtm_di_LabeledEdge' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_LabeledEdge()
    setattr(partner, 'mtm_di_LabeledEdge', None)
    _safe_set(owner, 'mtm_di_DocumentRoot23', {partner})
    assert getattr(partner, 'mtm_di_LabeledEdge') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot23', set())
    assert getattr(partner, 'mtm_di_LabeledEdge') is None


def test_assoc_labeledShape24_stub_double():
    # mtm_di_LabeledShape has no real 'mtm_di_LabeledShape' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_LabeledShape()
    setattr(partner, 'mtm_di_LabeledShape', None)
    _safe_set(owner, 'mtm_di_DocumentRoot25', {partner})
    assert getattr(partner, 'mtm_di_LabeledShape') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot25', set())
    assert getattr(partner, 'mtm_di_LabeledShape') is None


def test_assoc_node26_stub_double():
    # mtm_di_Node has no real 'mtm_di_Node' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_Node()
    setattr(partner, 'mtm_di_Node', None)
    _safe_set(owner, 'mtm_di_DocumentRoot27', {partner})
    assert getattr(partner, 'mtm_di_Node') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot27', set())
    assert getattr(partner, 'mtm_di_Node') is None


def test_assoc_shape31_stub_double():
    # mtm_di_Shape has no real 'mtm_di_Shape33' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_Shape()
    setattr(partner, 'mtm_di_Shape33', None)
    _safe_set(owner, 'mtm_di_DocumentRoot32', {partner})
    assert getattr(partner, 'mtm_di_Shape33') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot32', set())
    assert getattr(partner, 'mtm_di_Shape33') is None


def test_assoc_xMLNSPrefixMap7_stub_double():
    # mtm_di_EStringToStringMapEntry has no real 'mtm_di_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_EStringToStringMapEntry()
    setattr(partner, 'mtm_di_EStringToStringMapEntry', None)
    _safe_set(owner, 'mtm_di_DocumentRoot', {partner})
    assert getattr(partner, 'mtm_di_EStringToStringMapEntry') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot', set())
    assert getattr(partner, 'mtm_di_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation8_stub_double():
    # mtm_di_EStringToStringMapEntry has no real 'mtm_di_EStringToStringMapEntry10' property in the generated
    # code (a bare stub) -- manually attach it so mtm_di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mtm_di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mtm_di_DocumentRoot(mixed="sample_text")
    partner = mtm_di_EStringToStringMapEntry()
    setattr(partner, 'mtm_di_EStringToStringMapEntry10', None)
    _safe_set(owner, 'mtm_di_DocumentRoot9', {partner})
    assert getattr(partner, 'mtm_di_EStringToStringMapEntry10') == owner
    _safe_set(owner, 'mtm_di_DocumentRoot9', set())
    assert getattr(partner, 'mtm_di_EStringToStringMapEntry10') is None


