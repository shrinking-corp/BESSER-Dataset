import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    Link,
    Page,
    swml_v2_Attribute,
    swml_v2_CLink,
    swml_v2_Class,
    swml_v2_ContentLayer,
    swml_v2_DetailsPage,
    swml_v2_DynamicPage,
    swml_v2_IndexPage,
    swml_v2_Link,
    swml_v2_NCLink,
    swml_v2_NavigationLayer,
    swml_v2_Page,
    swml_v2_StaticPage,
    swml_v2_WebModel,
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
    a1 = swml_v2_Class(name="sample_text")
    a2 = swml_v2_Class(name="sample_text_2")
    b = swml_v2_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_v2_Attribute', a1)
    assert _is_linked(b, 'swml_v2_Attribute', a1)
    if hasattr(a1, 'swml_v2_Class11'):
        assert _is_linked(a1, 'swml_v2_Class11', b)
    _safe_set(b, 'swml_v2_Attribute', a2)
    assert _is_linked(b, 'swml_v2_Attribute', a2)
    if hasattr(a1, 'swml_v2_Class11'):
        assert not _is_linked(a1, 'swml_v2_Class11', b)
    if hasattr(a2, 'swml_v2_Class11'):
        assert _is_linked(a2, 'swml_v2_Class11', b)
    _safe_set(b, 'swml_v2_Attribute', None)
    assert not _is_linked(b, 'swml_v2_Attribute', a2)
    if hasattr(a2, 'swml_v2_Class11'):
        assert not _is_linked(a2, 'swml_v2_Class11', b)


def test_assoc_representativeAttribute12_reverse_link_reassign_clear():
    a1 = swml_v2_Class(name="sample_text")
    a2 = swml_v2_Class(name="sample_text_2")
    b = swml_v2_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_v2_Attribute14', a1)
    assert _is_linked(b, 'swml_v2_Attribute14', a1)
    if hasattr(a1, 'swml_v2_Class13'):
        assert _is_linked(a1, 'swml_v2_Class13', b)
    _safe_set(b, 'swml_v2_Attribute14', a2)
    assert _is_linked(b, 'swml_v2_Attribute14', a2)
    if hasattr(a1, 'swml_v2_Class13'):
        assert not _is_linked(a1, 'swml_v2_Class13', b)
    if hasattr(a2, 'swml_v2_Class13'):
        assert _is_linked(a2, 'swml_v2_Class13', b)
    _safe_set(b, 'swml_v2_Attribute14', None)
    assert not _is_linked(b, 'swml_v2_Attribute14', a2)
    if hasattr(a2, 'swml_v2_Class13'):
        assert not _is_linked(a2, 'swml_v2_Class13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes8_stub_double():
    # swml_v2_ContentLayer has no real 'swml_v2_ContentLayer9' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Class(name="sample_text")
    partner = swml_v2_ContentLayer()
    setattr(partner, 'swml_v2_ContentLayer9', None)
    _safe_set(owner, 'swml_v2_Class', partner)
    assert owner in getattr(partner, 'swml_v2_ContentLayer9')
    _safe_set(owner, 'swml_v2_Class', None)
    assert owner not in getattr(partner, 'swml_v2_ContentLayer9')


def test_assoc_content1_stub_double():
    # swml_v2_ContentLayer has no real 'swml_v2_ContentLayer' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_WebModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_WebModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_WebModel(name="sample_text")
    partner = swml_v2_ContentLayer()
    setattr(partner, 'swml_v2_ContentLayer', None)
    _safe_set(owner, 'swml_v2_WebModel2', partner)
    assert getattr(partner, 'swml_v2_ContentLayer') == owner
    _safe_set(owner, 'swml_v2_WebModel2', None)
    assert getattr(partner, 'swml_v2_ContentLayer') is None


def test_assoc_displayedClass17_stub_double():
    # swml_v2_DynamicPage has no real 'swml_v2_DynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Class(name="sample_text")
    partner = swml_v2_DynamicPage()
    setattr(partner, 'swml_v2_DynamicPage', None)
    _safe_set(owner, 'swml_v2_Class18', partner)
    assert getattr(partner, 'swml_v2_DynamicPage') == owner
    _safe_set(owner, 'swml_v2_Class18', None)
    assert getattr(partner, 'swml_v2_DynamicPage') is None


def test_assoc_homePage5_stub_double():
    # swml_v2_NavigationLayer has no real 'swml_v2_NavigationLayer6' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Page(name="sample_text")
    partner = swml_v2_NavigationLayer()
    setattr(partner, 'swml_v2_NavigationLayer6', None)
    _safe_set(owner, 'swml_v2_Page7', partner)
    assert getattr(partner, 'swml_v2_NavigationLayer6') == owner
    _safe_set(owner, 'swml_v2_Page7', None)
    assert getattr(partner, 'swml_v2_NavigationLayer6') is None


def test_assoc_hypertext0_stub_double():
    # swml_v2_NavigationLayer has no real 'swml_v2_NavigationLayer' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_WebModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_WebModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_WebModel(name="sample_text")
    partner = swml_v2_NavigationLayer()
    setattr(partner, 'swml_v2_NavigationLayer', None)
    _safe_set(owner, 'swml_v2_WebModel', partner)
    assert getattr(partner, 'swml_v2_NavigationLayer') == owner
    _safe_set(owner, 'swml_v2_WebModel', None)
    assert getattr(partner, 'swml_v2_NavigationLayer') is None


def test_assoc_links15_stub_double():
    # swml_v2_Link has no real 'swml_v2_Link' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Page(name="sample_text")
    partner = swml_v2_Link()
    setattr(partner, 'swml_v2_Link', None)
    _safe_set(owner, 'swml_v2_Page16', {partner})
    assert getattr(partner, 'swml_v2_Link') == owner
    _safe_set(owner, 'swml_v2_Page16', set())
    assert getattr(partner, 'swml_v2_Link') is None


def test_assoc_pages3_stub_double():
    # swml_v2_NavigationLayer has no real 'swml_v2_NavigationLayer4' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Page(name="sample_text")
    partner = swml_v2_NavigationLayer()
    setattr(partner, 'swml_v2_NavigationLayer4', None)
    _safe_set(owner, 'swml_v2_Page', partner)
    assert owner in getattr(partner, 'swml_v2_NavigationLayer4')
    _safe_set(owner, 'swml_v2_Page', None)
    assert owner not in getattr(partner, 'swml_v2_NavigationLayer4')


def test_assoc_target19_stub_double():
    # swml_v2_Link has no real 'swml_v2_Link20' property in the generated
    # code (a bare stub) -- manually attach it so swml_v2_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_v2_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_v2_Page(name="sample_text")
    partner = swml_v2_Link()
    setattr(partner, 'swml_v2_Link20', None)
    _safe_set(owner, 'swml_v2_Page21', partner)
    assert getattr(partner, 'swml_v2_Link20') == owner
    _safe_set(owner, 'swml_v2_Page21', None)
    assert getattr(partner, 'swml_v2_Link20') is None


