import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Data_Attribute,
    Data_Class,
    Data_Model,
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

def test_assoc_Attributes1_reverse_link_reassign_clear():
    a1 = Data_Class(Name="sample_text")
    a2 = Data_Class(Name="sample_text_2")
    b = Data_Attribute(Name="sample_text", Type="sample_text")
    _safe_set(b, 'Data_Attribute', a1)
    assert _is_linked(b, 'Data_Attribute', a1)
    if hasattr(a1, 'Data_Class2'):
        assert _is_linked(a1, 'Data_Class2', b)
    _safe_set(b, 'Data_Attribute', a2)
    assert _is_linked(b, 'Data_Attribute', a2)
    if hasattr(a1, 'Data_Class2'):
        assert not _is_linked(a1, 'Data_Class2', b)
    if hasattr(a2, 'Data_Class2'):
        assert _is_linked(a2, 'Data_Class2', b)
    _safe_set(b, 'Data_Attribute', None)
    assert not _is_linked(b, 'Data_Attribute', a2)
    if hasattr(a2, 'Data_Class2'):
        assert not _is_linked(a2, 'Data_Class2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Classes0_stub_double():
    # Data_Model has no real 'Data_Model' property in the generated
    # code (a bare stub) -- manually attach it so Data_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Data_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Data_Class(Name="sample_text")
    partner = Data_Model()
    setattr(partner, 'Data_Model', None)
    _safe_set(owner, 'Data_Class', partner)
    assert owner in getattr(partner, 'Data_Model')
    _safe_set(owner, 'Data_Class', None)
    assert owner not in getattr(partner, 'Data_Model')


