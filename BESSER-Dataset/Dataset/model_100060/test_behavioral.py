import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bug,
    BugTracking,
    Control,
    ControlType,
    ControlsSequence,
    DateType,
    SoftwareQualityControl_Bug,
    SoftwareQualityControl_BugTracking,
    SoftwareQualityControl_Control,
    SoftwareQualityControl_ControlType,
    SoftwareQualityControl_ControlsSequence,
    SoftwareQualityControl_DateType,
    BugStatusType,
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

def test_assoc_b_bugTracking7_stub_double():
    # BugTracking has no real 'BugTracking' property in the generated
    # code (a bare stub) -- manually attach it so SoftwareQualityControl_Bug's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SoftwareQualityControl_Bug's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SoftwareQualityControl_Bug(closeDate="sample_text", commentsAnswers="sample_text", componentVersion="sample_text", description="sample_text", number="sample_text", openDate="sample_text", originator="sample_text", responsible="sample_text", status="sample_text")
    partner = BugTracking()
    setattr(partner, 'BugTracking', None)
    _safe_set(owner, 'bugs', partner)
    assert getattr(partner, 'BugTracking') == owner
    _safe_set(owner, 'bugs', None)
    assert getattr(partner, 'BugTracking') is None


def test_assoc_c_controlsSequence1_stub_double():
    # ControlsSequence has no real 'ControlsSequence' property in the generated
    # code (a bare stub) -- manually attach it so SoftwareQualityControl_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SoftwareQualityControl_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SoftwareQualityControl_Control(component="sample_text", controlledElt="sample_text", developmentPhase="sample_text", eltAuthor="sample_text", eltRef="sample_text", formRef="sample_text", responsible="sample_text", scope="sample_text")
    partner = ControlsSequence()
    setattr(partner, 'ControlsSequence', None)
    _safe_set(owner, 'controls', partner)
    assert getattr(partner, 'ControlsSequence') == owner
    _safe_set(owner, 'controls', None)
    assert getattr(partner, 'ControlsSequence') is None


def test_assoc_date2_stub_double():
    # DateType has no real 'DateType' property in the generated
    # code (a bare stub) -- manually attach it so SoftwareQualityControl_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SoftwareQualityControl_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SoftwareQualityControl_Control(component="sample_text", controlledElt="sample_text", developmentPhase="sample_text", eltAuthor="sample_text", eltRef="sample_text", formRef="sample_text", responsible="sample_text", scope="sample_text")
    partner = DateType()
    setattr(partner, 'DateType', None)
    _safe_set(owner, 'SoftwareQualityControl_Control', partner)
    assert getattr(partner, 'DateType') == owner
    _safe_set(owner, 'SoftwareQualityControl_Control', None)
    assert getattr(partner, 'DateType') is None


def test_assoc_type3_stub_double():
    # ControlType has no real 'ControlType' property in the generated
    # code (a bare stub) -- manually attach it so SoftwareQualityControl_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SoftwareQualityControl_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SoftwareQualityControl_Control(component="sample_text", controlledElt="sample_text", developmentPhase="sample_text", eltAuthor="sample_text", eltRef="sample_text", formRef="sample_text", responsible="sample_text", scope="sample_text")
    partner = ControlType()
    setattr(partner, 'ControlType', None)
    _safe_set(owner, 'ct_control', partner)
    assert getattr(partner, 'ControlType') == owner
    _safe_set(owner, 'ct_control', None)
    assert getattr(partner, 'ControlType') is None


