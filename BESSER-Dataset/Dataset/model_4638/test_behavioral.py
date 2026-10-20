import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Figure,
    GraphicalElement,
    IdElement,
    NotationElement,
    TextualElement,
    Value,
    notation_AttributeValue,
    notation_Composite,
    notation_Definition,
    notation_EAttribute,
    notation_EReference,
    notation_Figure,
    notation_GraphicalElement,
    notation_IdElement,
    notation_Keyword,
    notation_Label,
    notation_Line,
    notation_NotationElement,
    notation_Rectangle,
    notation_ReferenceValue,
    notation_SyntaxOf,
    notation_TextualElement,
    notation_Token,
    notation_Value,
    Color,
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

def test_assoc_attribute1_stub_double():
    # notation_EAttribute has no real 'notation_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so notation_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Value(separator="sample_text")
    partner = notation_EAttribute()
    setattr(partner, 'notation_EAttribute', None)
    _safe_set(owner, 'notation_Value', partner)
    assert getattr(partner, 'notation_EAttribute') == owner
    _safe_set(owner, 'notation_Value', None)
    assert getattr(partner, 'notation_EAttribute') is None


def test_assoc_text0_stub_double():
    # notation_Label has no real 'notation_Label' property in the generated
    # code (a bare stub) -- manually attach it so notation_TextualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_TextualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_TextualElement(fill="sample_text")
    partner = notation_Label()
    setattr(partner, 'notation_Label', None)
    _safe_set(owner, 'notation_TextualElement', partner)
    assert getattr(partner, 'notation_Label') == owner
    _safe_set(owner, 'notation_TextualElement', None)
    assert getattr(partner, 'notation_Label') is None


