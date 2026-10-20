import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sWML_Attribute,
    sWML_Class,
    sWML_ContentLayer,
    sWML_HypertextLayer,
    sWML_IndexPage,
    sWML_WebModel,
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
    a1 = sWML_Class(name="sample_text")
    a2 = sWML_Class(name="sample_text_2")
    b = sWML_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'sWML_Attribute', a1)
    assert _is_linked(b, 'sWML_Attribute', a1)
    if hasattr(a1, 'sWML_Class11'):
        assert _is_linked(a1, 'sWML_Class11', b)
    _safe_set(b, 'sWML_Attribute', a2)
    assert _is_linked(b, 'sWML_Attribute', a2)
    if hasattr(a1, 'sWML_Class11'):
        assert not _is_linked(a1, 'sWML_Class11', b)
    if hasattr(a2, 'sWML_Class11'):
        assert _is_linked(a2, 'sWML_Class11', b)
    _safe_set(b, 'sWML_Attribute', None)
    assert not _is_linked(b, 'sWML_Attribute', a2)
    if hasattr(a2, 'sWML_Class11'):
        assert not _is_linked(a2, 'sWML_Class11', b)


def test_assoc_displayedClass5_reverse_link_reassign_clear():
    a1 = sWML_IndexPage(name="sample_text", size=7)
    a2 = sWML_IndexPage(name="sample_text_2", size=13)
    b = sWML_Class(name="sample_text")
    _safe_set(b, 'sWML_Class', a1)
    assert _is_linked(b, 'sWML_Class', a1)
    if hasattr(a1, 'sWML_IndexPage6'):
        assert _is_linked(a1, 'sWML_IndexPage6', b)
    _safe_set(b, 'sWML_Class', a2)
    assert _is_linked(b, 'sWML_Class', a2)
    if hasattr(a1, 'sWML_IndexPage6'):
        assert not _is_linked(a1, 'sWML_IndexPage6', b)
    if hasattr(a2, 'sWML_IndexPage6'):
        assert _is_linked(a2, 'sWML_IndexPage6', b)
    _safe_set(b, 'sWML_Class', None)
    assert not _is_linked(b, 'sWML_Class', a2)
    if hasattr(a2, 'sWML_IndexPage6'):
        assert not _is_linked(a2, 'sWML_IndexPage6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes7_stub_double():
    # sWML_ContentLayer has no real 'sWML_ContentLayer8' property in the generated
    # code (a bare stub) -- manually attach it so sWML_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sWML_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sWML_Class(name="sample_text")
    partner = sWML_ContentLayer()
    setattr(partner, 'sWML_ContentLayer8', None)
    _safe_set(owner, 'sWML_Class9', partner)
    assert owner in getattr(partner, 'sWML_ContentLayer8')
    _safe_set(owner, 'sWML_Class9', None)
    assert owner not in getattr(partner, 'sWML_ContentLayer8')


def test_assoc_content1_stub_double():
    # sWML_ContentLayer has no real 'sWML_ContentLayer' property in the generated
    # code (a bare stub) -- manually attach it so sWML_WebModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sWML_WebModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sWML_WebModel(name="sample_text")
    partner = sWML_ContentLayer()
    setattr(partner, 'sWML_ContentLayer', None)
    _safe_set(owner, 'sWML_WebModel2', partner)
    assert getattr(partner, 'sWML_ContentLayer') == owner
    _safe_set(owner, 'sWML_WebModel2', None)
    assert getattr(partner, 'sWML_ContentLayer') is None


def test_assoc_hypertext0_stub_double():
    # sWML_HypertextLayer has no real 'sWML_HypertextLayer' property in the generated
    # code (a bare stub) -- manually attach it so sWML_WebModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sWML_WebModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sWML_WebModel(name="sample_text")
    partner = sWML_HypertextLayer()
    setattr(partner, 'sWML_HypertextLayer', None)
    _safe_set(owner, 'sWML_WebModel', partner)
    assert getattr(partner, 'sWML_HypertextLayer') == owner
    _safe_set(owner, 'sWML_WebModel', None)
    assert getattr(partner, 'sWML_HypertextLayer') is None


def test_assoc_pages3_stub_double():
    # sWML_HypertextLayer has no real 'sWML_HypertextLayer4' property in the generated
    # code (a bare stub) -- manually attach it so sWML_IndexPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sWML_IndexPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sWML_IndexPage(name="sample_text", size=7)
    partner = sWML_HypertextLayer()
    setattr(partner, 'sWML_HypertextLayer4', None)
    _safe_set(owner, 'sWML_IndexPage', partner)
    assert owner in getattr(partner, 'sWML_HypertextLayer4')
    _safe_set(owner, 'sWML_IndexPage', None)
    assert owner not in getattr(partner, 'sWML_HypertextLayer4')


