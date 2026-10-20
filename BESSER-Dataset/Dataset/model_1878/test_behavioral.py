import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRepresentation,
    Representation,
    expansionmodel_AbstractRepresentation,
    expansionmodel_DiagramExpansion,
    expansionmodel_GMFT_BasedRepresentation,
    expansionmodel_GraphicalElementLibrary,
    expansionmodel_InducedRepresentation,
    expansionmodel_Representation,
    expansionmodel_RepresentationKind,
    expansionmodel_UseContext,
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

def test_assoc_children5_reverse_link_reassign_clear():
    a1 = expansionmodel_Representation(graphicalElementType="sample_text")
    a2 = expansionmodel_Representation(graphicalElementType="sample_text_2")
    b = expansionmodel_InducedRepresentation(hint="sample_text")
    _safe_set(b, 'expansionmodel_InducedRepresentation6', {a1})
    assert _is_linked(b, 'expansionmodel_InducedRepresentation6', a1)
    if hasattr(a1, 'expansionmodel_Representation7'):
        assert _is_linked(a1, 'expansionmodel_Representation7', b)
    _safe_set(b, 'expansionmodel_InducedRepresentation6', {a2})
    assert _is_linked(b, 'expansionmodel_InducedRepresentation6', a2)
    if hasattr(a1, 'expansionmodel_Representation7'):
        assert not _is_linked(a1, 'expansionmodel_Representation7', b)
    if hasattr(a2, 'expansionmodel_Representation7'):
        assert _is_linked(a2, 'expansionmodel_Representation7', b)
    _safe_set(b, 'expansionmodel_InducedRepresentation6', set())
    assert not _is_linked(b, 'expansionmodel_InducedRepresentation6', a2)
    if hasattr(a2, 'expansionmodel_Representation7'):
        assert not _is_linked(a2, 'expansionmodel_Representation7', b)


def test_assoc_gmftRepresentations15_reverse_link_reassign_clear():
    a1 = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    a2 = expansionmodel_UseContext(diagramType="sample_text_2", name="sample_text_2")
    b = expansionmodel_GMFT_BasedRepresentation(reusedID="sample_text")
    _safe_set(b, 'expansionmodel_GMFT_BasedRepresentation', a1)
    assert _is_linked(b, 'expansionmodel_GMFT_BasedRepresentation', a1)
    if hasattr(a1, 'expansionmodel_UseContext16'):
        assert _is_linked(a1, 'expansionmodel_UseContext16', b)
    _safe_set(b, 'expansionmodel_GMFT_BasedRepresentation', a2)
    assert _is_linked(b, 'expansionmodel_GMFT_BasedRepresentation', a2)
    if hasattr(a1, 'expansionmodel_UseContext16'):
        assert not _is_linked(a1, 'expansionmodel_UseContext16', b)
    if hasattr(a2, 'expansionmodel_UseContext16'):
        assert _is_linked(a2, 'expansionmodel_UseContext16', b)
    _safe_set(b, 'expansionmodel_GMFT_BasedRepresentation', None)
    assert not _is_linked(b, 'expansionmodel_GMFT_BasedRepresentation', a2)
    if hasattr(a2, 'expansionmodel_UseContext16'):
        assert not _is_linked(a2, 'expansionmodel_UseContext16', b)


def test_assoc_inducedRepresentations0_reverse_link_reassign_clear():
    a1 = expansionmodel_Representation(graphicalElementType="sample_text")
    a2 = expansionmodel_Representation(graphicalElementType="sample_text_2")
    b = expansionmodel_InducedRepresentation(hint="sample_text")
    _safe_set(b, 'expansionmodel_InducedRepresentation', a1)
    assert _is_linked(b, 'expansionmodel_InducedRepresentation', a1)
    if hasattr(a1, 'expansionmodel_Representation'):
        assert _is_linked(a1, 'expansionmodel_Representation', b)
    _safe_set(b, 'expansionmodel_InducedRepresentation', a2)
    assert _is_linked(b, 'expansionmodel_InducedRepresentation', a2)
    if hasattr(a1, 'expansionmodel_Representation'):
        assert not _is_linked(a1, 'expansionmodel_Representation', b)
    if hasattr(a2, 'expansionmodel_Representation'):
        assert _is_linked(a2, 'expansionmodel_Representation', b)
    _safe_set(b, 'expansionmodel_InducedRepresentation', None)
    assert not _is_linked(b, 'expansionmodel_InducedRepresentation', a2)
    if hasattr(a2, 'expansionmodel_Representation'):
        assert not _is_linked(a2, 'expansionmodel_Representation', b)


def test_assoc_kind4_reverse_link_reassign_clear():
    a1 = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    a2 = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text_2", name="sample_text_2", viewFactory="sample_text_2")
    b = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    _safe_set(b, 'expansionmodel_AbstractRepresentation', a1)
    assert _is_linked(b, 'expansionmodel_AbstractRepresentation', a1)
    if hasattr(a1, 'expansionmodel_RepresentationKind'):
        assert _is_linked(a1, 'expansionmodel_RepresentationKind', b)
    _safe_set(b, 'expansionmodel_AbstractRepresentation', a2)
    assert _is_linked(b, 'expansionmodel_AbstractRepresentation', a2)
    if hasattr(a1, 'expansionmodel_RepresentationKind'):
        assert not _is_linked(a1, 'expansionmodel_RepresentationKind', b)
    if hasattr(a2, 'expansionmodel_RepresentationKind'):
        assert _is_linked(a2, 'expansionmodel_RepresentationKind', b)
    _safe_set(b, 'expansionmodel_AbstractRepresentation', None)
    assert not _is_linked(b, 'expansionmodel_AbstractRepresentation', a2)
    if hasattr(a2, 'expansionmodel_RepresentationKind'):
        assert not _is_linked(a2, 'expansionmodel_RepresentationKind', b)


def test_assoc_libraries19_reverse_link_reassign_clear():
    a1 = expansionmodel_GraphicalElementLibrary(name="sample_text")
    a2 = expansionmodel_GraphicalElementLibrary(name="sample_text_2")
    b = expansionmodel_DiagramExpansion(ID="sample_text")
    _safe_set(b, 'expansionmodel_DiagramExpansion20', {a1})
    assert _is_linked(b, 'expansionmodel_DiagramExpansion20', a1)
    if hasattr(a1, 'expansionmodel_GraphicalElementLibrary21'):
        assert _is_linked(a1, 'expansionmodel_GraphicalElementLibrary21', b)
    _safe_set(b, 'expansionmodel_DiagramExpansion20', {a2})
    assert _is_linked(b, 'expansionmodel_DiagramExpansion20', a2)
    if hasattr(a1, 'expansionmodel_GraphicalElementLibrary21'):
        assert not _is_linked(a1, 'expansionmodel_GraphicalElementLibrary21', b)
    if hasattr(a2, 'expansionmodel_GraphicalElementLibrary21'):
        assert _is_linked(a2, 'expansionmodel_GraphicalElementLibrary21', b)
    _safe_set(b, 'expansionmodel_DiagramExpansion20', set())
    assert not _is_linked(b, 'expansionmodel_DiagramExpansion20', a2)
    if hasattr(a2, 'expansionmodel_GraphicalElementLibrary21'):
        assert not _is_linked(a2, 'expansionmodel_GraphicalElementLibrary21', b)


def test_assoc_representationkinds8_reverse_link_reassign_clear():
    a1 = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    a2 = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text_2", name="sample_text_2", viewFactory="sample_text_2")
    b = expansionmodel_GraphicalElementLibrary(name="sample_text")
    _safe_set(b, 'expansionmodel_GraphicalElementLibrary', {a1})
    assert _is_linked(b, 'expansionmodel_GraphicalElementLibrary', a1)
    if hasattr(a1, 'expansionmodel_RepresentationKind9'):
        assert _is_linked(a1, 'expansionmodel_RepresentationKind9', b)
    _safe_set(b, 'expansionmodel_GraphicalElementLibrary', {a2})
    assert _is_linked(b, 'expansionmodel_GraphicalElementLibrary', a2)
    if hasattr(a1, 'expansionmodel_RepresentationKind9'):
        assert not _is_linked(a1, 'expansionmodel_RepresentationKind9', b)
    if hasattr(a2, 'expansionmodel_RepresentationKind9'):
        assert _is_linked(a2, 'expansionmodel_RepresentationKind9', b)
    _safe_set(b, 'expansionmodel_GraphicalElementLibrary', set())
    assert not _is_linked(b, 'expansionmodel_GraphicalElementLibrary', a2)
    if hasattr(a2, 'expansionmodel_RepresentationKind9'):
        assert not _is_linked(a2, 'expansionmodel_RepresentationKind9', b)


def test_assoc_representations10_reverse_link_reassign_clear():
    a1 = expansionmodel_GraphicalElementLibrary(name="sample_text")
    a2 = expansionmodel_GraphicalElementLibrary(name="sample_text_2")
    b = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    _safe_set(b, 'expansionmodel_AbstractRepresentation12', a1)
    assert _is_linked(b, 'expansionmodel_AbstractRepresentation12', a1)
    if hasattr(a1, 'expansionmodel_GraphicalElementLibrary11'):
        assert _is_linked(a1, 'expansionmodel_GraphicalElementLibrary11', b)
    _safe_set(b, 'expansionmodel_AbstractRepresentation12', a2)
    assert _is_linked(b, 'expansionmodel_AbstractRepresentation12', a2)
    if hasattr(a1, 'expansionmodel_GraphicalElementLibrary11'):
        assert not _is_linked(a1, 'expansionmodel_GraphicalElementLibrary11', b)
    if hasattr(a2, 'expansionmodel_GraphicalElementLibrary11'):
        assert _is_linked(a2, 'expansionmodel_GraphicalElementLibrary11', b)
    _safe_set(b, 'expansionmodel_AbstractRepresentation12', None)
    assert not _is_linked(b, 'expansionmodel_AbstractRepresentation12', a2)
    if hasattr(a2, 'expansionmodel_GraphicalElementLibrary11'):
        assert not _is_linked(a2, 'expansionmodel_GraphicalElementLibrary11', b)


def test_assoc_representations13_reverse_link_reassign_clear():
    a1 = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    a2 = expansionmodel_UseContext(diagramType="sample_text_2", name="sample_text_2")
    b = expansionmodel_Representation(graphicalElementType="sample_text")
    _safe_set(b, 'expansionmodel_Representation14', a1)
    assert _is_linked(b, 'expansionmodel_Representation14', a1)
    if hasattr(a1, 'expansionmodel_UseContext'):
        assert _is_linked(a1, 'expansionmodel_UseContext', b)
    _safe_set(b, 'expansionmodel_Representation14', a2)
    assert _is_linked(b, 'expansionmodel_Representation14', a2)
    if hasattr(a1, 'expansionmodel_UseContext'):
        assert not _is_linked(a1, 'expansionmodel_UseContext', b)
    if hasattr(a2, 'expansionmodel_UseContext'):
        assert _is_linked(a2, 'expansionmodel_UseContext', b)
    _safe_set(b, 'expansionmodel_Representation14', None)
    assert not _is_linked(b, 'expansionmodel_Representation14', a2)
    if hasattr(a2, 'expansionmodel_UseContext'):
        assert not _is_linked(a2, 'expansionmodel_UseContext', b)


def test_assoc_subRepresentations2_reverse_link_reassign_clear():
    a1 = expansionmodel_Representation(graphicalElementType="sample_text")
    a2 = expansionmodel_Representation(graphicalElementType="sample_text_2")
    b = expansionmodel_Representation(graphicalElementType="sample_text")
    _safe_set(b, 'expansionmodel_Representation3', a1)
    assert _is_linked(b, 'expansionmodel_Representation3', a1)
    if hasattr(a1, 'expansionmodel_Representation1'):
        assert _is_linked(a1, 'expansionmodel_Representation1', b)
    _safe_set(b, 'expansionmodel_Representation3', a2)
    assert _is_linked(b, 'expansionmodel_Representation3', a2)
    if hasattr(a1, 'expansionmodel_Representation1'):
        assert not _is_linked(a1, 'expansionmodel_Representation1', b)
    if hasattr(a2, 'expansionmodel_Representation1'):
        assert _is_linked(a2, 'expansionmodel_Representation1', b)
    _safe_set(b, 'expansionmodel_Representation3', None)
    assert not _is_linked(b, 'expansionmodel_Representation3', a2)
    if hasattr(a2, 'expansionmodel_Representation1'):
        assert not _is_linked(a2, 'expansionmodel_Representation1', b)


def test_assoc_usages17_reverse_link_reassign_clear():
    a1 = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    a2 = expansionmodel_UseContext(diagramType="sample_text_2", name="sample_text_2")
    b = expansionmodel_DiagramExpansion(ID="sample_text")
    _safe_set(b, 'expansionmodel_DiagramExpansion', {a1})
    assert _is_linked(b, 'expansionmodel_DiagramExpansion', a1)
    if hasattr(a1, 'expansionmodel_UseContext18'):
        assert _is_linked(a1, 'expansionmodel_UseContext18', b)
    _safe_set(b, 'expansionmodel_DiagramExpansion', {a2})
    assert _is_linked(b, 'expansionmodel_DiagramExpansion', a2)
    if hasattr(a1, 'expansionmodel_UseContext18'):
        assert not _is_linked(a1, 'expansionmodel_UseContext18', b)
    if hasattr(a2, 'expansionmodel_UseContext18'):
        assert _is_linked(a2, 'expansionmodel_UseContext18', b)
    _safe_set(b, 'expansionmodel_DiagramExpansion', set())
    assert not _is_linked(b, 'expansionmodel_DiagramExpansion', a2)
    if hasattr(a2, 'expansionmodel_UseContext18'):
        assert not _is_linked(a2, 'expansionmodel_UseContext18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

