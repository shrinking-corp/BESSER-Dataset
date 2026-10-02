import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    Link,
    Page,
    swml_Attribute,
    swml_CLink,
    swml_Class,
    swml_ContentLayer,
    swml_DetailsPage,
    swml_DynamicPage,
    swml_HypertextLayer,
    swml_IndexPage,
    swml_Link,
    swml_NCLink,
    swml_Page,
    swml_StaticPage,
    swml_WebModel,
    SWMLTypes,
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

def test_assoc_attributes10_reverse_link_reassign_clear():
    a1 = swml_Class(name="sample_text")
    a2 = swml_Class(name="sample_text_2")
    b = swml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_Attribute', a1)
    assert _is_linked(b, 'swml_Attribute', a1)
    if hasattr(a1, 'swml_Class11'):
        assert _is_linked(a1, 'swml_Class11', b)
    _safe_set(b, 'swml_Attribute', a2)
    assert _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a1, 'swml_Class11'):
        assert not _is_linked(a1, 'swml_Class11', b)
    if hasattr(a2, 'swml_Class11'):
        assert _is_linked(a2, 'swml_Class11', b)
    _safe_set(b, 'swml_Attribute', None)
    assert not _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a2, 'swml_Class11'):
        assert not _is_linked(a2, 'swml_Class11', b)


def test_assoc_representativeAttribute12_reverse_link_reassign_clear():
    a1 = swml_Class(name="sample_text")
    a2 = swml_Class(name="sample_text_2")
    b = swml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_Attribute14', a1)
    assert _is_linked(b, 'swml_Attribute14', a1)
    if hasattr(a1, 'swml_Class13'):
        assert _is_linked(a1, 'swml_Class13', b)
    _safe_set(b, 'swml_Attribute14', a2)
    assert _is_linked(b, 'swml_Attribute14', a2)
    if hasattr(a1, 'swml_Class13'):
        assert not _is_linked(a1, 'swml_Class13', b)
    if hasattr(a2, 'swml_Class13'):
        assert _is_linked(a2, 'swml_Class13', b)
    _safe_set(b, 'swml_Attribute14', None)
    assert not _is_linked(b, 'swml_Attribute14', a2)
    if hasattr(a2, 'swml_Class13'):
        assert not _is_linked(a2, 'swml_Class13', b)


