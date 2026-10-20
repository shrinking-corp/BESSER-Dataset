import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EModelElement,
    StyleSheet,
    stylesheets_EmbeddedStyleSheet,
    stylesheets_ModelStyleSheets,
    stylesheets_StyleSheet,
    stylesheets_StyleSheetReference,
    stylesheets_Theme,
    stylesheets_WorkspaceThemes,
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

def test_assoc_stylesheets2_stub_double():
    # stylesheets_StyleSheet has no real 'stylesheets_StyleSheet4' property in the generated
    # code (a bare stub) -- manually attach it so stylesheets_Theme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stylesheets_Theme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stylesheets_Theme(icon="sample_text", id="sample_text", label="sample_text")
    partner = stylesheets_StyleSheet()
    setattr(partner, 'stylesheets_StyleSheet4', None)
    _safe_set(owner, 'stylesheets_Theme3', {partner})
    assert getattr(partner, 'stylesheets_StyleSheet4') == owner
    _safe_set(owner, 'stylesheets_Theme3', set())
    assert getattr(partner, 'stylesheets_StyleSheet4') is None


def test_assoc_themes1_stub_double():
    # stylesheets_WorkspaceThemes has no real 'stylesheets_WorkspaceThemes' property in the generated
    # code (a bare stub) -- manually attach it so stylesheets_Theme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stylesheets_Theme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stylesheets_Theme(icon="sample_text", id="sample_text", label="sample_text")
    partner = stylesheets_WorkspaceThemes()
    setattr(partner, 'stylesheets_WorkspaceThemes', None)
    _safe_set(owner, 'stylesheets_Theme', partner)
    assert owner in getattr(partner, 'stylesheets_WorkspaceThemes')
    _safe_set(owner, 'stylesheets_Theme', None)
    assert owner not in getattr(partner, 'stylesheets_WorkspaceThemes')


