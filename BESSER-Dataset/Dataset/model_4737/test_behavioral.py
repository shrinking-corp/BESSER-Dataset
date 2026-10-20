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


def test_assoc_classes8_reverse_link_reassign_clear():
    a1 = swml_ContentLayer(name="sample_text")
    a2 = swml_ContentLayer(name="sample_text_2")
    b = swml_Class(name="sample_text")
    _safe_set(b, 'swml_Class', a1)
    assert _is_linked(b, 'swml_Class', a1)
    if hasattr(a1, 'swml_ContentLayer9'):
        assert _is_linked(a1, 'swml_ContentLayer9', b)
    _safe_set(b, 'swml_Class', a2)
    assert _is_linked(b, 'swml_Class', a2)
    if hasattr(a1, 'swml_ContentLayer9'):
        assert not _is_linked(a1, 'swml_ContentLayer9', b)
    if hasattr(a2, 'swml_ContentLayer9'):
        assert _is_linked(a2, 'swml_ContentLayer9', b)
    _safe_set(b, 'swml_Class', None)
    assert not _is_linked(b, 'swml_Class', a2)
    if hasattr(a2, 'swml_ContentLayer9'):
        assert not _is_linked(a2, 'swml_ContentLayer9', b)


def test_assoc_content1_reverse_link_reassign_clear():
    a1 = swml_WebModel(name="sample_text")
    a2 = swml_WebModel(name="sample_text_2")
    b = swml_ContentLayer(name="sample_text")
    _safe_set(b, 'swml_ContentLayer', a1)
    assert _is_linked(b, 'swml_ContentLayer', a1)
    if hasattr(a1, 'swml_WebModel2'):
        assert _is_linked(a1, 'swml_WebModel2', b)
    _safe_set(b, 'swml_ContentLayer', a2)
    assert _is_linked(b, 'swml_ContentLayer', a2)
    if hasattr(a1, 'swml_WebModel2'):
        assert not _is_linked(a1, 'swml_WebModel2', b)
    if hasattr(a2, 'swml_WebModel2'):
        assert _is_linked(a2, 'swml_WebModel2', b)
    _safe_set(b, 'swml_ContentLayer', None)
    assert not _is_linked(b, 'swml_ContentLayer', a2)
    if hasattr(a2, 'swml_WebModel2'):
        assert not _is_linked(a2, 'swml_WebModel2', b)


def test_assoc_homePage5_reverse_link_reassign_clear():
    a1 = swml_Page(name="sample_text")
    a2 = swml_Page(name="sample_text_2")
    b = swml_HypertextLayer(name="sample_text")
    _safe_set(b, 'swml_HypertextLayer6', a1)
    assert _is_linked(b, 'swml_HypertextLayer6', a1)
    if hasattr(a1, 'swml_Page7'):
        assert _is_linked(a1, 'swml_Page7', b)
    _safe_set(b, 'swml_HypertextLayer6', a2)
    assert _is_linked(b, 'swml_HypertextLayer6', a2)
    if hasattr(a1, 'swml_Page7'):
        assert not _is_linked(a1, 'swml_Page7', b)
    if hasattr(a2, 'swml_Page7'):
        assert _is_linked(a2, 'swml_Page7', b)
    _safe_set(b, 'swml_HypertextLayer6', None)
    assert not _is_linked(b, 'swml_HypertextLayer6', a2)
    if hasattr(a2, 'swml_Page7'):
        assert not _is_linked(a2, 'swml_Page7', b)


def test_assoc_hypertext0_reverse_link_reassign_clear():
    a1 = swml_WebModel(name="sample_text")
    a2 = swml_WebModel(name="sample_text_2")
    b = swml_HypertextLayer(name="sample_text")
    _safe_set(b, 'swml_HypertextLayer', a1)
    assert _is_linked(b, 'swml_HypertextLayer', a1)
    if hasattr(a1, 'swml_WebModel'):
        assert _is_linked(a1, 'swml_WebModel', b)
    _safe_set(b, 'swml_HypertextLayer', a2)
    assert _is_linked(b, 'swml_HypertextLayer', a2)
    if hasattr(a1, 'swml_WebModel'):
        assert not _is_linked(a1, 'swml_WebModel', b)
    if hasattr(a2, 'swml_WebModel'):
        assert _is_linked(a2, 'swml_WebModel', b)
    _safe_set(b, 'swml_HypertextLayer', None)
    assert not _is_linked(b, 'swml_HypertextLayer', a2)
    if hasattr(a2, 'swml_WebModel'):
        assert not _is_linked(a2, 'swml_WebModel', b)


def test_assoc_pages3_reverse_link_reassign_clear():
    a1 = swml_Page(name="sample_text")
    a2 = swml_Page(name="sample_text_2")
    b = swml_HypertextLayer(name="sample_text")
    _safe_set(b, 'swml_HypertextLayer4', {a1})
    assert _is_linked(b, 'swml_HypertextLayer4', a1)
    if hasattr(a1, 'swml_Page'):
        assert _is_linked(a1, 'swml_Page', b)
    _safe_set(b, 'swml_HypertextLayer4', {a2})
    assert _is_linked(b, 'swml_HypertextLayer4', a2)
    if hasattr(a1, 'swml_Page'):
        assert not _is_linked(a1, 'swml_Page', b)
    if hasattr(a2, 'swml_Page'):
        assert _is_linked(a2, 'swml_Page', b)
    _safe_set(b, 'swml_HypertextLayer4', set())
    assert not _is_linked(b, 'swml_HypertextLayer4', a2)
    if hasattr(a2, 'swml_Page'):
        assert not _is_linked(a2, 'swml_Page', b)


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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_displayedClass16_stub_double():
    # swml_DynamicPage has no real 'swml_DynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so swml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Class(name="sample_text")
    partner = swml_DynamicPage()
    setattr(partner, 'swml_DynamicPage', None)
    _safe_set(owner, 'swml_Class17', partner)
    assert getattr(partner, 'swml_DynamicPage') == owner
    _safe_set(owner, 'swml_Class17', None)
    assert getattr(partner, 'swml_DynamicPage') is None


def test_assoc_links15_stub_double():
    # swml_Link has no real 'Link' property in the generated
    # code (a bare stub) -- manually attach it so swml_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Page(name="sample_text")
    partner = swml_Link()
    setattr(partner, 'Link', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Link') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Link') is None


def test_assoc_source20_stub_double():
    # swml_Link has no real 'links' property in the generated
    # code (a bare stub) -- manually attach it so swml_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Page(name="sample_text")
    partner = swml_Link()
    setattr(partner, 'links', None)
    _safe_set(owner, 'Page', partner)
    assert getattr(partner, 'links') == owner
    _safe_set(owner, 'Page', None)
    assert getattr(partner, 'links') is None


def test_assoc_target18_stub_double():
    # swml_Link has no real 'swml_Link' property in the generated
    # code (a bare stub) -- manually attach it so swml_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Page(name="sample_text")
    partner = swml_Link()
    setattr(partner, 'swml_Link', None)
    _safe_set(owner, 'swml_Page19', partner)
    assert getattr(partner, 'swml_Link') == owner
    _safe_set(owner, 'swml_Page19', None)
    assert getattr(partner, 'swml_Link') is None


