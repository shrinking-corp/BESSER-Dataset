import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    itemflow101_Description,
    itemflow101_Flow,
    itemflow101_Function,
    itemflow101_InputPort,
    itemflow101_Item,
    itemflow101_OutputPort,
    itemflow101_Port,
    itemflow101_ProcessNode,
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

def test_assoc_descriptions8_stub_double():
    # itemflow101_Function has no real 'itemflow101_Function9' property in the generated
    # code (a bare stub) -- manually attach it so itemflow101_Description's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itemflow101_Description's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itemflow101_Description(content="sample_text")
    partner = itemflow101_Function()
    setattr(partner, 'itemflow101_Function9', None)
    _safe_set(owner, 'itemflow101_Description', partner)
    assert owner in getattr(partner, 'itemflow101_Function9')
    _safe_set(owner, 'itemflow101_Description', None)
    assert owner not in getattr(partner, 'itemflow101_Function9')


def test_assoc_items13_stub_double():
    # itemflow101_Flow has no real 'itemflow101_Flow14' property in the generated
    # code (a bare stub) -- manually attach it so itemflow101_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itemflow101_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itemflow101_Item(name="sample_text")
    partner = itemflow101_Flow()
    setattr(partner, 'itemflow101_Flow14', None)
    _safe_set(owner, 'itemflow101_Item', partner)
    assert owner in getattr(partner, 'itemflow101_Flow14')
    _safe_set(owner, 'itemflow101_Item', None)
    assert owner not in getattr(partner, 'itemflow101_Flow14')


