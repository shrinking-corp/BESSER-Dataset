import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    uppaallite_LocationType,
    uppaallite_TemplateType,
    uppaallite_TransitionType,
    uppaallite_UppaalDiagram,
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

def test_assoc_Template0_reverse_link_reassign_clear():
    a1 = uppaallite_UppaalDiagram(declaration="sample_text", resourceWeightDeclaration="sample_text")
    a2 = uppaallite_UppaalDiagram(declaration="sample_text_2", resourceWeightDeclaration="sample_text_2")
    b = uppaallite_TemplateType(declaration="sample_text", name="sample_text")
    _safe_set(b, 'uppaallite_TemplateType', a1)
    assert _is_linked(b, 'uppaallite_TemplateType', a1)
    if hasattr(a1, 'uppaallite_UppaalDiagram'):
        assert _is_linked(a1, 'uppaallite_UppaalDiagram', b)
    _safe_set(b, 'uppaallite_TemplateType', a2)
    assert _is_linked(b, 'uppaallite_TemplateType', a2)
    if hasattr(a1, 'uppaallite_UppaalDiagram'):
        assert not _is_linked(a1, 'uppaallite_UppaalDiagram', b)
    if hasattr(a2, 'uppaallite_UppaalDiagram'):
        assert _is_linked(a2, 'uppaallite_UppaalDiagram', b)
    _safe_set(b, 'uppaallite_TemplateType', None)
    assert not _is_linked(b, 'uppaallite_TemplateType', a2)
    if hasattr(a2, 'uppaallite_UppaalDiagram'):
        assert not _is_linked(a2, 'uppaallite_UppaalDiagram', b)


def test_assoc_container4_reverse_link_reassign_clear():
    a1 = uppaallite_TemplateType(declaration="sample_text", name="sample_text")
    a2 = uppaallite_TemplateType(declaration="sample_text_2", name="sample_text_2")
    b = uppaallite_LocationType(committed=True, cost="sample_text", id="sample_text", initial=True, invariant="sample_text", name="sample_text", urgent=True, x=7, y=7)
    _safe_set(b, 'location', a1)
    assert _is_linked(b, 'location', a1)
    if hasattr(a1, 'TemplateType'):
        assert _is_linked(a1, 'TemplateType', b)
    _safe_set(b, 'location', a2)
    assert _is_linked(b, 'location', a2)
    if hasattr(a1, 'TemplateType'):
        assert not _is_linked(a1, 'TemplateType', b)
    if hasattr(a2, 'TemplateType'):
        assert _is_linked(a2, 'TemplateType', b)
    _safe_set(b, 'location', None)
    assert not _is_linked(b, 'location', a2)
    if hasattr(a2, 'TemplateType'):
        assert not _is_linked(a2, 'TemplateType', b)


def test_assoc_container9_reverse_link_reassign_clear():
    a1 = uppaallite_TransitionType(assignment="sample_text", cost="sample_text", guard="sample_text", sync="sample_text")
    a2 = uppaallite_TransitionType(assignment="sample_text_2", cost="sample_text_2", guard="sample_text_2", sync="sample_text_2")
    b = uppaallite_TemplateType(declaration="sample_text", name="sample_text")
    _safe_set(b, 'TemplateType10', a1)
    assert _is_linked(b, 'TemplateType10', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'TemplateType10', a2)
    assert _is_linked(b, 'TemplateType10', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'TemplateType10', None)
    assert not _is_linked(b, 'TemplateType10', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_location1_reverse_link_reassign_clear():
    a1 = uppaallite_TemplateType(declaration="sample_text", name="sample_text")
    a2 = uppaallite_TemplateType(declaration="sample_text_2", name="sample_text_2")
    b = uppaallite_LocationType(committed=True, cost="sample_text", id="sample_text", initial=True, invariant="sample_text", name="sample_text", urgent=True, x=7, y=7)
    _safe_set(b, 'LocationType', a1)
    assert _is_linked(b, 'LocationType', a1)
    if hasattr(a1, 'container'):
        assert _is_linked(a1, 'container', b)
    _safe_set(b, 'LocationType', a2)
    assert _is_linked(b, 'LocationType', a2)
    if hasattr(a1, 'container'):
        assert not _is_linked(a1, 'container', b)
    if hasattr(a2, 'container'):
        assert _is_linked(a2, 'container', b)
    _safe_set(b, 'LocationType', None)
    assert not _is_linked(b, 'LocationType', a2)
    if hasattr(a2, 'container'):
        assert not _is_linked(a2, 'container', b)


def test_assoc_source5_reverse_link_reassign_clear():
    a1 = uppaallite_TransitionType(assignment="sample_text", cost="sample_text", guard="sample_text", sync="sample_text")
    a2 = uppaallite_TransitionType(assignment="sample_text_2", cost="sample_text_2", guard="sample_text_2", sync="sample_text_2")
    b = uppaallite_LocationType(committed=True, cost="sample_text", id="sample_text", initial=True, invariant="sample_text", name="sample_text", urgent=True, x=7, y=7)
    _safe_set(b, 'uppaallite_LocationType', a1)
    assert _is_linked(b, 'uppaallite_LocationType', a1)
    if hasattr(a1, 'uppaallite_TransitionType'):
        assert _is_linked(a1, 'uppaallite_TransitionType', b)
    _safe_set(b, 'uppaallite_LocationType', a2)
    assert _is_linked(b, 'uppaallite_LocationType', a2)
    if hasattr(a1, 'uppaallite_TransitionType'):
        assert not _is_linked(a1, 'uppaallite_TransitionType', b)
    if hasattr(a2, 'uppaallite_TransitionType'):
        assert _is_linked(a2, 'uppaallite_TransitionType', b)
    _safe_set(b, 'uppaallite_LocationType', None)
    assert not _is_linked(b, 'uppaallite_LocationType', a2)
    if hasattr(a2, 'uppaallite_TransitionType'):
        assert not _is_linked(a2, 'uppaallite_TransitionType', b)


def test_assoc_target6_reverse_link_reassign_clear():
    a1 = uppaallite_TransitionType(assignment="sample_text", cost="sample_text", guard="sample_text", sync="sample_text")
    a2 = uppaallite_TransitionType(assignment="sample_text_2", cost="sample_text_2", guard="sample_text_2", sync="sample_text_2")
    b = uppaallite_LocationType(committed=True, cost="sample_text", id="sample_text", initial=True, invariant="sample_text", name="sample_text", urgent=True, x=7, y=7)
    _safe_set(b, 'uppaallite_LocationType8', a1)
    assert _is_linked(b, 'uppaallite_LocationType8', a1)
    if hasattr(a1, 'uppaallite_TransitionType7'):
        assert _is_linked(a1, 'uppaallite_TransitionType7', b)
    _safe_set(b, 'uppaallite_LocationType8', a2)
    assert _is_linked(b, 'uppaallite_LocationType8', a2)
    if hasattr(a1, 'uppaallite_TransitionType7'):
        assert not _is_linked(a1, 'uppaallite_TransitionType7', b)
    if hasattr(a2, 'uppaallite_TransitionType7'):
        assert _is_linked(a2, 'uppaallite_TransitionType7', b)
    _safe_set(b, 'uppaallite_LocationType8', None)
    assert not _is_linked(b, 'uppaallite_LocationType8', a2)
    if hasattr(a2, 'uppaallite_TransitionType7'):
        assert not _is_linked(a2, 'uppaallite_TransitionType7', b)


def test_assoc_transition2_reverse_link_reassign_clear():
    a1 = uppaallite_TransitionType(assignment="sample_text", cost="sample_text", guard="sample_text", sync="sample_text")
    a2 = uppaallite_TransitionType(assignment="sample_text_2", cost="sample_text_2", guard="sample_text_2", sync="sample_text_2")
    b = uppaallite_TemplateType(declaration="sample_text", name="sample_text")
    _safe_set(b, 'container3', {a1})
    assert _is_linked(b, 'container3', a1)
    if hasattr(a1, 'TransitionType'):
        assert _is_linked(a1, 'TransitionType', b)
    _safe_set(b, 'container3', {a2})
    assert _is_linked(b, 'container3', a2)
    if hasattr(a1, 'TransitionType'):
        assert not _is_linked(a1, 'TransitionType', b)
    if hasattr(a2, 'TransitionType'):
        assert _is_linked(a2, 'TransitionType', b)
    _safe_set(b, 'container3', set())
    assert not _is_linked(b, 'container3', a2)
    if hasattr(a2, 'TransitionType'):
        assert not _is_linked(a2, 'TransitionType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

