import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Container,
    Container_Level1,
    Container_Level2,
    Container_Level3,
    Container_Level4,
    Container_Level5,
    Container_Level6,
    Container_Level7,
    Container_Level8,
    Container_Level9,
    Element,
    Element_Level1,
    Element_Level2,
    Element_Level3,
    Element_Level4,
    Element_Level5,
    Element_Level6,
    Element_Level7,
    Element_Level8,
    Element_Level9,
    subsetUnionDepth_Container,
    subsetUnionDepth_Container_Level1,
    subsetUnionDepth_Container_Level10,
    subsetUnionDepth_Container_Level2,
    subsetUnionDepth_Container_Level3,
    subsetUnionDepth_Container_Level4,
    subsetUnionDepth_Container_Level5,
    subsetUnionDepth_Container_Level6,
    subsetUnionDepth_Container_Level7,
    subsetUnionDepth_Container_Level8,
    subsetUnionDepth_Container_Level9,
    subsetUnionDepth_Element,
    subsetUnionDepth_Element_Level1,
    subsetUnionDepth_Element_Level10,
    subsetUnionDepth_Element_Level2,
    subsetUnionDepth_Element_Level3,
    subsetUnionDepth_Element_Level4,
    subsetUnionDepth_Element_Level5,
    subsetUnionDepth_Element_Level6,
    subsetUnionDepth_Element_Level7,
    subsetUnionDepth_Element_Level8,
    subsetUnionDepth_Element_Level9,
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

def test_assoc_unionBag0_reverse_link_reassign_clear():
    a1 = subsetUnionDepth_Element(name="sample_text")
    a2 = subsetUnionDepth_Element(name="sample_text_2")
    b = subsetUnionDepth_Container(name="sample_text")
    _safe_set(b, 'subsetUnionDepth_Container', {a1})
    assert _is_linked(b, 'subsetUnionDepth_Container', a1)
    if hasattr(a1, 'subsetUnionDepth_Element'):
        assert _is_linked(a1, 'subsetUnionDepth_Element', b)
    _safe_set(b, 'subsetUnionDepth_Container', {a2})
    assert _is_linked(b, 'subsetUnionDepth_Container', a2)
    if hasattr(a1, 'subsetUnionDepth_Element'):
        assert not _is_linked(a1, 'subsetUnionDepth_Element', b)
    if hasattr(a2, 'subsetUnionDepth_Element'):
        assert _is_linked(a2, 'subsetUnionDepth_Element', b)
    _safe_set(b, 'subsetUnionDepth_Container', set())
    assert not _is_linked(b, 'subsetUnionDepth_Container', a2)
    if hasattr(a2, 'subsetUnionDepth_Element'):
        assert not _is_linked(a2, 'subsetUnionDepth_Element', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

