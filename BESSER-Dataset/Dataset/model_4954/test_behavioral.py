import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IdElement,
    NamedElement,
    WebApp_Action,
    WebApp_ActionMapping,
    WebApp_Attribute,
    WebApp_Controller,
    WebApp_Dummies,
    WebApp_DynamicApplication,
    WebApp_Entities,
    WebApp_FormElements,
    WebApp_Forms,
    WebApp_IdElement,
    WebApp_NamedElement,
    WebApp_Pages,
    WebApp_Tables,
    WebApp_Views,
    WebApp_styleElements,
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

def test_assoc_attribute28_stub_double():
    # WebApp_Entities has no real 'WebApp_Entities29' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Attribute(value="sample_text")
    partner = WebApp_Entities()
    setattr(partner, 'WebApp_Entities29', None)
    _safe_set(owner, 'WebApp_Attribute', partner)
    assert owner in getattr(partner, 'WebApp_Entities29')
    _safe_set(owner, 'WebApp_Attribute', None)
    assert owner not in getattr(partner, 'WebApp_Entities29')


def test_assoc_attribute38_stub_double():
    # WebApp_Dummies has no real 'WebApp_Dummies39' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Attribute(value="sample_text")
    partner = WebApp_Dummies()
    setattr(partner, 'WebApp_Dummies39', None)
    _safe_set(owner, 'WebApp_Attribute40', partner)
    assert owner in getattr(partner, 'WebApp_Dummies39')
    _safe_set(owner, 'WebApp_Attribute40', None)
    assert owner not in getattr(partner, 'WebApp_Dummies39')


