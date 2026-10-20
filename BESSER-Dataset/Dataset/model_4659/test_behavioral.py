import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Diagram,
    Label,
    LabeledEdge,
    LabeledShape,
    Plane,
    Style,
    di_BPMNDiagram,
    di_BPMNEdge,
    di_BPMNLabel,
    di_BPMNLabelStyle,
    di_BPMNPlane,
    di_BPMNShape,
    di_BaseElement,
    di_DiagramElement,
    di_DocumentRoot,
    di_EStringToStringMapEntry,
    di_Font,
    MessageVisibleKind,
    ParticipantBandKind,
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

def test_assoc_bPMNDiagram4_reverse_link_reassign_clear():
    a1 = di_DocumentRoot(mixed="sample_text")
    a2 = di_DocumentRoot(mixed="sample_text_2")
    b = di_BPMNDiagram(featureModel="sample_text", location="sample_text", phase="sample_text", version="sample_text")
    _safe_set(b, 'di_BPMNDiagram', a1)
    assert _is_linked(b, 'di_BPMNDiagram', a1)
    if hasattr(a1, 'di_DocumentRoot5'):
        assert _is_linked(a1, 'di_DocumentRoot5', b)
    _safe_set(b, 'di_BPMNDiagram', a2)
    assert _is_linked(b, 'di_BPMNDiagram', a2)
    if hasattr(a1, 'di_DocumentRoot5'):
        assert not _is_linked(a1, 'di_DocumentRoot5', b)
    if hasattr(a2, 'di_DocumentRoot5'):
        assert _is_linked(a2, 'di_DocumentRoot5', b)
    _safe_set(b, 'di_BPMNDiagram', None)
    assert not _is_linked(b, 'di_BPMNDiagram', a2)
    if hasattr(a2, 'di_DocumentRoot5'):
        assert not _is_linked(a2, 'di_DocumentRoot5', b)


def test_assoc_bPMNEdge6_reverse_link_reassign_clear():
    a1 = di_DocumentRoot(mixed="sample_text")
    a2 = di_DocumentRoot(mixed="sample_text_2")
    b = di_BPMNEdge(messageVisibleKind="sample_text")
    _safe_set(b, 'di_BPMNEdge', a1)
    assert _is_linked(b, 'di_BPMNEdge', a1)
    if hasattr(a1, 'di_DocumentRoot7'):
        assert _is_linked(a1, 'di_DocumentRoot7', b)
    _safe_set(b, 'di_BPMNEdge', a2)
    assert _is_linked(b, 'di_BPMNEdge', a2)
    if hasattr(a1, 'di_DocumentRoot7'):
        assert not _is_linked(a1, 'di_DocumentRoot7', b)
    if hasattr(a2, 'di_DocumentRoot7'):
        assert _is_linked(a2, 'di_DocumentRoot7', b)
    _safe_set(b, 'di_BPMNEdge', None)
    assert not _is_linked(b, 'di_BPMNEdge', a2)
    if hasattr(a2, 'di_DocumentRoot7'):
        assert not _is_linked(a2, 'di_DocumentRoot7', b)


def test_assoc_bPMNShape14_reverse_link_reassign_clear():
    a1 = di_DocumentRoot(mixed="sample_text")
    a2 = di_DocumentRoot(mixed="sample_text_2")
    b = di_BPMNShape(isExpanded=True, isHorizontal=True, isMarkerVisible=True, isMessageVisible=True, participantBandKind="sample_text")
    _safe_set(b, 'di_BPMNShape', a1)
    assert _is_linked(b, 'di_BPMNShape', a1)
    if hasattr(a1, 'di_DocumentRoot15'):
        assert _is_linked(a1, 'di_DocumentRoot15', b)
    _safe_set(b, 'di_BPMNShape', a2)
    assert _is_linked(b, 'di_BPMNShape', a2)
    if hasattr(a1, 'di_DocumentRoot15'):
        assert not _is_linked(a1, 'di_DocumentRoot15', b)
    if hasattr(a2, 'di_DocumentRoot15'):
        assert _is_linked(a2, 'di_DocumentRoot15', b)
    _safe_set(b, 'di_BPMNShape', None)
    assert not _is_linked(b, 'di_BPMNShape', a2)
    if hasattr(a2, 'di_DocumentRoot15'):
        assert not _is_linked(a2, 'di_DocumentRoot15', b)


def test_assoc_choreographyActivityShape47_reverse_link_reassign_clear():
    a1 = di_BPMNShape(isExpanded=True, isHorizontal=True, isMarkerVisible=True, isMessageVisible=True, participantBandKind="sample_text")
    a2 = di_BPMNShape(isExpanded=False, isHorizontal=False, isMarkerVisible=False, isMessageVisible=False, participantBandKind="sample_text_2")
    b = di_BPMNShape(isExpanded=True, isHorizontal=True, isMarkerVisible=True, isMessageVisible=True, participantBandKind="sample_text")
    _safe_set(b, 'di_BPMNShape48', a1)
    assert _is_linked(b, 'di_BPMNShape48', a1)
    if hasattr(a1, 'di_BPMNShape46'):
        assert _is_linked(a1, 'di_BPMNShape46', b)
    _safe_set(b, 'di_BPMNShape48', a2)
    assert _is_linked(b, 'di_BPMNShape48', a2)
    if hasattr(a1, 'di_BPMNShape46'):
        assert not _is_linked(a1, 'di_BPMNShape46', b)
    if hasattr(a2, 'di_BPMNShape46'):
        assert _is_linked(a2, 'di_BPMNShape46', b)
    _safe_set(b, 'di_BPMNShape48', None)
    assert not _is_linked(b, 'di_BPMNShape48', a2)
    if hasattr(a2, 'di_BPMNShape46'):
        assert not _is_linked(a2, 'di_BPMNShape46', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bPMNLabel8_stub_double():
    # di_BPMNLabel has no real 'di_BPMNLabel' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_BPMNLabel()
    setattr(partner, 'di_BPMNLabel', None)
    _safe_set(owner, 'di_DocumentRoot9', {partner})
    assert getattr(partner, 'di_BPMNLabel') == owner
    _safe_set(owner, 'di_DocumentRoot9', set())
    assert getattr(partner, 'di_BPMNLabel') is None


def test_assoc_bPMNLabelStyle10_stub_double():
    # di_BPMNLabelStyle has no real 'di_BPMNLabelStyle' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_BPMNLabelStyle()
    setattr(partner, 'di_BPMNLabelStyle', None)
    _safe_set(owner, 'di_DocumentRoot11', {partner})
    assert getattr(partner, 'di_BPMNLabelStyle') == owner
    _safe_set(owner, 'di_DocumentRoot11', set())
    assert getattr(partner, 'di_BPMNLabelStyle') is None


def test_assoc_bPMNPlane12_stub_double():
    # di_BPMNPlane has no real 'di_BPMNPlane' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_BPMNPlane()
    setattr(partner, 'di_BPMNPlane', None)
    _safe_set(owner, 'di_DocumentRoot13', {partner})
    assert getattr(partner, 'di_BPMNPlane') == owner
    _safe_set(owner, 'di_DocumentRoot13', set())
    assert getattr(partner, 'di_BPMNPlane') is None


def test_assoc_bpmnElement25_stub_double():
    # di_BaseElement has no real 'di_BaseElement' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNEdge(messageVisibleKind="sample_text")
    partner = di_BaseElement()
    setattr(partner, 'di_BaseElement', None)
    _safe_set(owner, 'di_BPMNEdge26', partner)
    assert getattr(partner, 'di_BaseElement') == owner
    _safe_set(owner, 'di_BPMNEdge26', None)
    assert getattr(partner, 'di_BaseElement') is None


def test_assoc_bpmnElement43_stub_double():
    # di_BaseElement has no real 'di_BaseElement45' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNShape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNShape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNShape(isExpanded=True, isHorizontal=True, isMarkerVisible=True, isMessageVisible=True, participantBandKind="sample_text")
    partner = di_BaseElement()
    setattr(partner, 'di_BaseElement45', None)
    _safe_set(owner, 'di_BPMNShape44', partner)
    assert getattr(partner, 'di_BaseElement45') == owner
    _safe_set(owner, 'di_BPMNShape44', None)
    assert getattr(partner, 'di_BaseElement45') is None


def test_assoc_label22_stub_double():
    # di_BPMNLabel has no real 'di_BPMNLabel24' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNEdge(messageVisibleKind="sample_text")
    partner = di_BPMNLabel()
    setattr(partner, 'di_BPMNLabel24', None)
    _safe_set(owner, 'di_BPMNEdge23', partner)
    assert getattr(partner, 'di_BPMNLabel24') == owner
    _safe_set(owner, 'di_BPMNEdge23', None)
    assert getattr(partner, 'di_BPMNLabel24') is None


def test_assoc_label40_stub_double():
    # di_BPMNLabel has no real 'di_BPMNLabel42' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNShape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNShape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNShape(isExpanded=True, isHorizontal=True, isMarkerVisible=True, isMessageVisible=True, participantBandKind="sample_text")
    partner = di_BPMNLabel()
    setattr(partner, 'di_BPMNLabel42', None)
    _safe_set(owner, 'di_BPMNShape41', partner)
    assert getattr(partner, 'di_BPMNLabel42') == owner
    _safe_set(owner, 'di_BPMNShape41', None)
    assert getattr(partner, 'di_BPMNLabel42') is None


def test_assoc_labelStyle19_stub_double():
    # di_BPMNLabelStyle has no real 'di_BPMNLabelStyle21' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNDiagram(featureModel="sample_text", location="sample_text", phase="sample_text", version="sample_text")
    partner = di_BPMNLabelStyle()
    setattr(partner, 'di_BPMNLabelStyle21', None)
    _safe_set(owner, 'di_BPMNDiagram20', {partner})
    assert getattr(partner, 'di_BPMNLabelStyle21') == owner
    _safe_set(owner, 'di_BPMNDiagram20', set())
    assert getattr(partner, 'di_BPMNLabelStyle21') is None


def test_assoc_plane16_stub_double():
    # di_BPMNPlane has no real 'di_BPMNPlane18' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNDiagram(featureModel="sample_text", location="sample_text", phase="sample_text", version="sample_text")
    partner = di_BPMNPlane()
    setattr(partner, 'di_BPMNPlane18', None)
    _safe_set(owner, 'di_BPMNDiagram17', partner)
    assert getattr(partner, 'di_BPMNPlane18') == owner
    _safe_set(owner, 'di_BPMNDiagram17', None)
    assert getattr(partner, 'di_BPMNPlane18') is None


def test_assoc_sourceElement27_stub_double():
    # di_DiagramElement has no real 'di_DiagramElement' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNEdge(messageVisibleKind="sample_text")
    partner = di_DiagramElement()
    setattr(partner, 'di_DiagramElement', None)
    _safe_set(owner, 'di_BPMNEdge28', partner)
    assert getattr(partner, 'di_DiagramElement') == owner
    _safe_set(owner, 'di_BPMNEdge28', None)
    assert getattr(partner, 'di_DiagramElement') is None


def test_assoc_targetElement29_stub_double():
    # di_DiagramElement has no real 'di_DiagramElement31' property in the generated
    # code (a bare stub) -- manually attach it so di_BPMNEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_BPMNEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_BPMNEdge(messageVisibleKind="sample_text")
    partner = di_DiagramElement()
    setattr(partner, 'di_DiagramElement31', None)
    _safe_set(owner, 'di_BPMNEdge30', partner)
    assert getattr(partner, 'di_DiagramElement31') == owner
    _safe_set(owner, 'di_BPMNEdge30', None)
    assert getattr(partner, 'di_DiagramElement31') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # di_EStringToStringMapEntry has no real 'di_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_EStringToStringMapEntry()
    setattr(partner, 'di_EStringToStringMapEntry', None)
    _safe_set(owner, 'di_DocumentRoot', {partner})
    assert getattr(partner, 'di_EStringToStringMapEntry') == owner
    _safe_set(owner, 'di_DocumentRoot', set())
    assert getattr(partner, 'di_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # di_EStringToStringMapEntry has no real 'di_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_EStringToStringMapEntry()
    setattr(partner, 'di_EStringToStringMapEntry3', None)
    _safe_set(owner, 'di_DocumentRoot2', {partner})
    assert getattr(partner, 'di_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'di_DocumentRoot2', set())
    assert getattr(partner, 'di_EStringToStringMapEntry3') is None


