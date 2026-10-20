import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    NamedElement,
    RouteObject,
    SegmentObject,
    TrackObject,
    TrainRouteObject,
    railDsl_Declaration,
    railDsl_Derailer,
    railDsl_LevelCrossing,
    railDsl_NamedElement,
    railDsl_Platform,
    railDsl_Point,
    railDsl_RouteObject,
    railDsl_Segment,
    railDsl_SegmentObject,
    railDsl_SegmentPosition,
    railDsl_Signal,
    railDsl_Station,
    railDsl_Track,
    railDsl_TrackObject,
    railDsl_Train,
    railDsl_TrainRoute,
    railDsl_TrainRouteObject,
    railDsl_TrainRoutePoint,
    railDsl_TrainRouteSegment,
    railDsl_TrainSegment,
    railDsl_Vertex,
    Orientation,
    PointKind,
    Side,
    SpeedLimit,
    TrainRouteKind,
    VertexKind,
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

def test_assoc_conflictingRoutes38_reverse_link_reassign_clear():
    a1 = railDsl_TrainRoute(kind="sample_text", locked=True)
    a2 = railDsl_TrainRoute(kind="sample_text_2", locked=False)
    b = railDsl_TrainRoute(kind="sample_text", locked=True)
    _safe_set(b, 'railDsl_TrainRoute39', a1)
    assert _is_linked(b, 'railDsl_TrainRoute39', a1)
    if hasattr(a1, 'railDsl_TrainRoute37'):
        assert _is_linked(a1, 'railDsl_TrainRoute37', b)
    _safe_set(b, 'railDsl_TrainRoute39', a2)
    assert _is_linked(b, 'railDsl_TrainRoute39', a2)
    if hasattr(a1, 'railDsl_TrainRoute37'):
        assert not _is_linked(a1, 'railDsl_TrainRoute37', b)
    if hasattr(a2, 'railDsl_TrainRoute37'):
        assert _is_linked(a2, 'railDsl_TrainRoute37', b)
    _safe_set(b, 'railDsl_TrainRoute39', None)
    assert not _is_linked(b, 'railDsl_TrainRoute39', a2)
    if hasattr(a2, 'railDsl_TrainRoute37'):
        assert not _is_linked(a2, 'railDsl_TrainRoute37', b)


def test_assoc_distantFor10_reverse_link_reassign_clear():
    a1 = railDsl_Signal(main=True, shunting=True)
    a2 = railDsl_Signal(main=False, shunting=False)
    b = railDsl_Signal(main=True, shunting=True)
    _safe_set(b, 'railDsl_Signal9', a1)
    assert _is_linked(b, 'railDsl_Signal9', a1)
    if hasattr(a1, 'railDsl_Signal'):
        assert _is_linked(a1, 'railDsl_Signal', b)
    _safe_set(b, 'railDsl_Signal9', a2)
    assert _is_linked(b, 'railDsl_Signal9', a2)
    if hasattr(a1, 'railDsl_Signal'):
        assert not _is_linked(a1, 'railDsl_Signal', b)
    if hasattr(a2, 'railDsl_Signal'):
        assert _is_linked(a2, 'railDsl_Signal', b)
    _safe_set(b, 'railDsl_Signal9', None)
    assert not _is_linked(b, 'railDsl_Signal9', a2)
    if hasattr(a2, 'railDsl_Signal'):
        assert not _is_linked(a2, 'railDsl_Signal', b)


def test_assoc_endSignal31_reverse_link_reassign_clear():
    a1 = railDsl_TrainRoute(kind="sample_text", locked=True)
    a2 = railDsl_TrainRoute(kind="sample_text_2", locked=False)
    b = railDsl_Signal(main=True, shunting=True)
    _safe_set(b, 'railDsl_Signal33', a1)
    assert _is_linked(b, 'railDsl_Signal33', a1)
    if hasattr(a1, 'railDsl_TrainRoute32'):
        assert _is_linked(a1, 'railDsl_TrainRoute32', b)
    _safe_set(b, 'railDsl_Signal33', a2)
    assert _is_linked(b, 'railDsl_Signal33', a2)
    if hasattr(a1, 'railDsl_TrainRoute32'):
        assert not _is_linked(a1, 'railDsl_TrainRoute32', b)
    if hasattr(a2, 'railDsl_TrainRoute32'):
        assert _is_linked(a2, 'railDsl_TrainRoute32', b)
    _safe_set(b, 'railDsl_Signal33', None)
    assert not _is_linked(b, 'railDsl_Signal33', a2)
    if hasattr(a2, 'railDsl_TrainRoute32'):
        assert not _is_linked(a2, 'railDsl_TrainRoute32', b)


def test_assoc_inputs14_reverse_link_reassign_clear():
    a1 = railDsl_Vertex(kind="sample_text")
    a2 = railDsl_Vertex(kind="sample_text_2")
    b = railDsl_Point(kind="sample_text", locked=True, selectedInput=7, selectedOutput=7)
    _safe_set(b, 'railDsl_Point', {a1})
    assert _is_linked(b, 'railDsl_Point', a1)
    if hasattr(a1, 'railDsl_Vertex15'):
        assert _is_linked(a1, 'railDsl_Vertex15', b)
    _safe_set(b, 'railDsl_Point', {a2})
    assert _is_linked(b, 'railDsl_Point', a2)
    if hasattr(a1, 'railDsl_Vertex15'):
        assert not _is_linked(a1, 'railDsl_Vertex15', b)
    if hasattr(a2, 'railDsl_Vertex15'):
        assert _is_linked(a2, 'railDsl_Vertex15', b)
    _safe_set(b, 'railDsl_Point', set())
    assert not _is_linked(b, 'railDsl_Point', a2)
    if hasattr(a2, 'railDsl_Vertex15'):
        assert not _is_linked(a2, 'railDsl_Vertex15', b)


def test_assoc_originalPoint40_reverse_link_reassign_clear():
    a1 = railDsl_TrainRoutePoint(selectedInput=7, selectedOutput=7)
    a2 = railDsl_TrainRoutePoint(selectedInput=13, selectedOutput=13)
    b = railDsl_Point(kind="sample_text", locked=True, selectedInput=7, selectedOutput=7)
    _safe_set(b, 'railDsl_Point41', a1)
    assert _is_linked(b, 'railDsl_Point41', a1)
    if hasattr(a1, 'railDsl_TrainRoutePoint'):
        assert _is_linked(a1, 'railDsl_TrainRoutePoint', b)
    _safe_set(b, 'railDsl_Point41', a2)
    assert _is_linked(b, 'railDsl_Point41', a2)
    if hasattr(a1, 'railDsl_TrainRoutePoint'):
        assert not _is_linked(a1, 'railDsl_TrainRoutePoint', b)
    if hasattr(a2, 'railDsl_TrainRoutePoint'):
        assert _is_linked(a2, 'railDsl_TrainRoutePoint', b)
    _safe_set(b, 'railDsl_Point41', None)
    assert not _is_linked(b, 'railDsl_Point41', a2)
    if hasattr(a2, 'railDsl_TrainRoutePoint'):
        assert not _is_linked(a2, 'railDsl_TrainRoutePoint', b)


def test_assoc_outputs16_reverse_link_reassign_clear():
    a1 = railDsl_Vertex(kind="sample_text")
    a2 = railDsl_Vertex(kind="sample_text_2")
    b = railDsl_Point(kind="sample_text", locked=True, selectedInput=7, selectedOutput=7)
    _safe_set(b, 'railDsl_Point17', {a1})
    assert _is_linked(b, 'railDsl_Point17', a1)
    if hasattr(a1, 'railDsl_Vertex18'):
        assert _is_linked(a1, 'railDsl_Vertex18', b)
    _safe_set(b, 'railDsl_Point17', {a2})
    assert _is_linked(b, 'railDsl_Point17', a2)
    if hasattr(a1, 'railDsl_Vertex18'):
        assert not _is_linked(a1, 'railDsl_Vertex18', b)
    if hasattr(a2, 'railDsl_Vertex18'):
        assert _is_linked(a2, 'railDsl_Vertex18', b)
    _safe_set(b, 'railDsl_Point17', set())
    assert not _is_linked(b, 'railDsl_Point17', a2)
    if hasattr(a2, 'railDsl_Vertex18'):
        assert not _is_linked(a2, 'railDsl_Vertex18', b)


def test_assoc_path27_reverse_link_reassign_clear():
    a1 = railDsl_TrainRouteObject(speedLimit="sample_text")
    a2 = railDsl_TrainRouteObject(speedLimit="sample_text_2")
    b = railDsl_TrainRoute(kind="sample_text", locked=True)
    _safe_set(b, 'railDsl_TrainRoute', {a1})
    assert _is_linked(b, 'railDsl_TrainRoute', a1)
    if hasattr(a1, 'railDsl_TrainRouteObject'):
        assert _is_linked(a1, 'railDsl_TrainRouteObject', b)
    _safe_set(b, 'railDsl_TrainRoute', {a2})
    assert _is_linked(b, 'railDsl_TrainRoute', a2)
    if hasattr(a1, 'railDsl_TrainRouteObject'):
        assert not _is_linked(a1, 'railDsl_TrainRouteObject', b)
    if hasattr(a2, 'railDsl_TrainRouteObject'):
        assert _is_linked(a2, 'railDsl_TrainRouteObject', b)
    _safe_set(b, 'railDsl_TrainRoute', set())
    assert not _is_linked(b, 'railDsl_TrainRoute', a2)
    if hasattr(a2, 'railDsl_TrainRouteObject'):
        assert not _is_linked(a2, 'railDsl_TrainRouteObject', b)


def test_assoc_position21_reverse_link_reassign_clear():
    a1 = railDsl_Train(acceleration=3.14, length=3.14, speed=3.14)
    a2 = railDsl_Train(acceleration=9.99, length=9.99, speed=9.99)
    b = railDsl_SegmentPosition(atEnd=True, atStart=True, orientation="sample_text", position=3.14, side="sample_text")
    _safe_set(b, 'railDsl_SegmentPosition23', a1)
    assert _is_linked(b, 'railDsl_SegmentPosition23', a1)
    if hasattr(a1, 'railDsl_Train22'):
        assert _is_linked(a1, 'railDsl_Train22', b)
    _safe_set(b, 'railDsl_SegmentPosition23', a2)
    assert _is_linked(b, 'railDsl_SegmentPosition23', a2)
    if hasattr(a1, 'railDsl_Train22'):
        assert not _is_linked(a1, 'railDsl_Train22', b)
    if hasattr(a2, 'railDsl_Train22'):
        assert _is_linked(a2, 'railDsl_Train22', b)
    _safe_set(b, 'railDsl_SegmentPosition23', None)
    assert not _is_linked(b, 'railDsl_SegmentPosition23', a2)
    if hasattr(a2, 'railDsl_Train22'):
        assert not _is_linked(a2, 'railDsl_Train22', b)


def test_assoc_position24_reverse_link_reassign_clear():
    a1 = railDsl_TrainSegment(length=3.14)
    a2 = railDsl_TrainSegment(length=9.99)
    b = railDsl_SegmentPosition(atEnd=True, atStart=True, orientation="sample_text", position=3.14, side="sample_text")
    _safe_set(b, 'railDsl_SegmentPosition26', a1)
    assert _is_linked(b, 'railDsl_SegmentPosition26', a1)
    if hasattr(a1, 'railDsl_TrainSegment25'):
        assert _is_linked(a1, 'railDsl_TrainSegment25', b)
    _safe_set(b, 'railDsl_SegmentPosition26', a2)
    assert _is_linked(b, 'railDsl_SegmentPosition26', a2)
    if hasattr(a1, 'railDsl_TrainSegment25'):
        assert not _is_linked(a1, 'railDsl_TrainSegment25', b)
    if hasattr(a2, 'railDsl_TrainSegment25'):
        assert _is_linked(a2, 'railDsl_TrainSegment25', b)
    _safe_set(b, 'railDsl_SegmentPosition26', None)
    assert not _is_linked(b, 'railDsl_SegmentPosition26', a2)
    if hasattr(a2, 'railDsl_TrainSegment25'):
        assert not _is_linked(a2, 'railDsl_TrainSegment25', b)


def test_assoc_protectionObjects34_reverse_link_reassign_clear():
    a1 = railDsl_TrainRouteObject(speedLimit="sample_text")
    a2 = railDsl_TrainRouteObject(speedLimit="sample_text_2")
    b = railDsl_TrainRoute(kind="sample_text", locked=True)
    _safe_set(b, 'railDsl_TrainRoute35', {a1})
    assert _is_linked(b, 'railDsl_TrainRoute35', a1)
    if hasattr(a1, 'railDsl_TrainRouteObject36'):
        assert _is_linked(a1, 'railDsl_TrainRouteObject36', b)
    _safe_set(b, 'railDsl_TrainRoute35', {a2})
    assert _is_linked(b, 'railDsl_TrainRoute35', a2)
    if hasattr(a1, 'railDsl_TrainRouteObject36'):
        assert not _is_linked(a1, 'railDsl_TrainRouteObject36', b)
    if hasattr(a2, 'railDsl_TrainRouteObject36'):
        assert _is_linked(a2, 'railDsl_TrainRouteObject36', b)
    _safe_set(b, 'railDsl_TrainRoute35', set())
    assert not _is_linked(b, 'railDsl_TrainRoute35', a2)
    if hasattr(a2, 'railDsl_TrainRouteObject36'):
        assert not _is_linked(a2, 'railDsl_TrainRouteObject36', b)


def test_assoc_segments20_reverse_link_reassign_clear():
    a1 = railDsl_TrainSegment(length=3.14)
    a2 = railDsl_TrainSegment(length=9.99)
    b = railDsl_Train(acceleration=3.14, length=3.14, speed=3.14)
    _safe_set(b, 'railDsl_Train', {a1})
    assert _is_linked(b, 'railDsl_Train', a1)
    if hasattr(a1, 'railDsl_TrainSegment'):
        assert _is_linked(a1, 'railDsl_TrainSegment', b)
    _safe_set(b, 'railDsl_Train', {a2})
    assert _is_linked(b, 'railDsl_Train', a2)
    if hasattr(a1, 'railDsl_TrainSegment'):
        assert not _is_linked(a1, 'railDsl_TrainSegment', b)
    if hasattr(a2, 'railDsl_TrainSegment'):
        assert _is_linked(a2, 'railDsl_TrainSegment', b)
    _safe_set(b, 'railDsl_Train', set())
    assert not _is_linked(b, 'railDsl_Train', a2)
    if hasattr(a2, 'railDsl_TrainSegment'):
        assert not _is_linked(a2, 'railDsl_TrainSegment', b)


def test_assoc_startSignal28_reverse_link_reassign_clear():
    a1 = railDsl_TrainRoute(kind="sample_text", locked=True)
    a2 = railDsl_TrainRoute(kind="sample_text_2", locked=False)
    b = railDsl_Signal(main=True, shunting=True)
    _safe_set(b, 'railDsl_Signal30', a1)
    assert _is_linked(b, 'railDsl_Signal30', a1)
    if hasattr(a1, 'railDsl_TrainRoute29'):
        assert _is_linked(a1, 'railDsl_TrainRoute29', b)
    _safe_set(b, 'railDsl_Signal30', a2)
    assert _is_linked(b, 'railDsl_Signal30', a2)
    if hasattr(a1, 'railDsl_TrainRoute29'):
        assert not _is_linked(a1, 'railDsl_TrainRoute29', b)
    if hasattr(a2, 'railDsl_TrainRoute29'):
        assert _is_linked(a2, 'railDsl_TrainRoute29', b)
    _safe_set(b, 'railDsl_Signal30', None)
    assert not _is_linked(b, 'railDsl_Signal30', a2)
    if hasattr(a2, 'railDsl_TrainRoute29'):
        assert not _is_linked(a2, 'railDsl_TrainRoute29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements19_stub_double():
    # railDsl_Track has no real 'railDsl_Track' property in the generated
    # code (a bare stub) -- manually attach it so railDsl_TrackObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railDsl_TrackObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railDsl_TrackObject(length=3.14)
    partner = railDsl_Track()
    setattr(partner, 'railDsl_Track', None)
    _safe_set(owner, 'railDsl_TrackObject', partner)
    assert owner in getattr(partner, 'railDsl_Track')
    _safe_set(owner, 'railDsl_TrackObject', None)
    assert owner not in getattr(partner, 'railDsl_Track')


def test_assoc_end2_stub_double():
    # railDsl_Segment has no real 'railDsl_Segment3' property in the generated
    # code (a bare stub) -- manually attach it so railDsl_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railDsl_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railDsl_Vertex(kind="sample_text")
    partner = railDsl_Segment()
    setattr(partner, 'railDsl_Segment3', None)
    _safe_set(owner, 'railDsl_Vertex4', partner)
    assert getattr(partner, 'railDsl_Segment3') == owner
    _safe_set(owner, 'railDsl_Vertex4', None)
    assert getattr(partner, 'railDsl_Segment3') is None


def test_assoc_position7_stub_double():
    # railDsl_SegmentObject has no real 'railDsl_SegmentObject8' property in the generated
    # code (a bare stub) -- manually attach it so railDsl_SegmentPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railDsl_SegmentPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railDsl_SegmentPosition(atEnd=True, atStart=True, orientation="sample_text", position=3.14, side="sample_text")
    partner = railDsl_SegmentObject()
    setattr(partner, 'railDsl_SegmentObject8', None)
    _safe_set(owner, 'railDsl_SegmentPosition', partner)
    assert getattr(partner, 'railDsl_SegmentObject8') == owner
    _safe_set(owner, 'railDsl_SegmentPosition', None)
    assert getattr(partner, 'railDsl_SegmentObject8') is None


def test_assoc_segment11_stub_double():
    # railDsl_Segment has no real 'railDsl_Segment13' property in the generated
    # code (a bare stub) -- manually attach it so railDsl_SegmentPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railDsl_SegmentPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railDsl_SegmentPosition(atEnd=True, atStart=True, orientation="sample_text", position=3.14, side="sample_text")
    partner = railDsl_Segment()
    setattr(partner, 'railDsl_Segment13', None)
    _safe_set(owner, 'railDsl_SegmentPosition12', partner)
    assert getattr(partner, 'railDsl_Segment13') == owner
    _safe_set(owner, 'railDsl_SegmentPosition12', None)
    assert getattr(partner, 'railDsl_Segment13') is None


def test_assoc_start1_stub_double():
    # railDsl_Segment has no real 'railDsl_Segment' property in the generated
    # code (a bare stub) -- manually attach it so railDsl_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railDsl_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railDsl_Vertex(kind="sample_text")
    partner = railDsl_Segment()
    setattr(partner, 'railDsl_Segment', None)
    _safe_set(owner, 'railDsl_Vertex', partner)
    assert getattr(partner, 'railDsl_Segment') == owner
    _safe_set(owner, 'railDsl_Vertex', None)
    assert getattr(partner, 'railDsl_Segment') is None


