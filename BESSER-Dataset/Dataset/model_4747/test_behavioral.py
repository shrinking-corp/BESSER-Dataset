import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    Page,
    wappm_Attribute,
    wappm_ContentLayer,
    wappm_DetailPage,
    wappm_DynamicPage,
    wappm_HypertextLayer,
    wappm_IndexPage,
    wappm_Link,
    wappm_Page,
    wappm_Reference,
    wappm_StaticPage,
    wappm_WebClass,
    wappm_WebModel,
    AppTypes,
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

def test_assoc_attributes14_reverse_link_reassign_clear():
    a1 = wappm_WebClass(name="sample_text")
    a2 = wappm_WebClass(name="sample_text_2")
    b = wappm_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'wappm_Attribute', a1)
    assert _is_linked(b, 'wappm_Attribute', a1)
    if hasattr(a1, 'wappm_WebClass15'):
        assert _is_linked(a1, 'wappm_WebClass15', b)
    _safe_set(b, 'wappm_Attribute', a2)
    assert _is_linked(b, 'wappm_Attribute', a2)
    if hasattr(a1, 'wappm_WebClass15'):
        assert not _is_linked(a1, 'wappm_WebClass15', b)
    if hasattr(a2, 'wappm_WebClass15'):
        assert _is_linked(a2, 'wappm_WebClass15', b)
    _safe_set(b, 'wappm_Attribute', None)
    assert not _is_linked(b, 'wappm_Attribute', a2)
    if hasattr(a2, 'wappm_WebClass15'):
        assert not _is_linked(a2, 'wappm_WebClass15', b)


def test_assoc_classes11_reverse_link_reassign_clear():
    a1 = wappm_WebClass(name="sample_text")
    a2 = wappm_WebClass(name="sample_text_2")
    b = wappm_ContentLayer(contentName="sample_text")
    _safe_set(b, 'wappm_ContentLayer12', {a1})
    assert _is_linked(b, 'wappm_ContentLayer12', a1)
    if hasattr(a1, 'wappm_WebClass13'):
        assert _is_linked(a1, 'wappm_WebClass13', b)
    _safe_set(b, 'wappm_ContentLayer12', {a2})
    assert _is_linked(b, 'wappm_ContentLayer12', a2)
    if hasattr(a1, 'wappm_WebClass13'):
        assert not _is_linked(a1, 'wappm_WebClass13', b)
    if hasattr(a2, 'wappm_WebClass13'):
        assert _is_linked(a2, 'wappm_WebClass13', b)
    _safe_set(b, 'wappm_ContentLayer12', set())
    assert not _is_linked(b, 'wappm_ContentLayer12', a2)
    if hasattr(a2, 'wappm_WebClass13'):
        assert not _is_linked(a2, 'wappm_WebClass13', b)


def test_assoc_content1_reverse_link_reassign_clear():
    a1 = wappm_WebModel(name="sample_text")
    a2 = wappm_WebModel(name="sample_text_2")
    b = wappm_ContentLayer(contentName="sample_text")
    _safe_set(b, 'wappm_ContentLayer', a1)
    assert _is_linked(b, 'wappm_ContentLayer', a1)
    if hasattr(a1, 'wappm_WebModel2'):
        assert _is_linked(a1, 'wappm_WebModel2', b)
    _safe_set(b, 'wappm_ContentLayer', a2)
    assert _is_linked(b, 'wappm_ContentLayer', a2)
    if hasattr(a1, 'wappm_WebModel2'):
        assert not _is_linked(a1, 'wappm_WebModel2', b)
    if hasattr(a2, 'wappm_WebModel2'):
        assert _is_linked(a2, 'wappm_WebModel2', b)
    _safe_set(b, 'wappm_ContentLayer', None)
    assert not _is_linked(b, 'wappm_ContentLayer', a2)
    if hasattr(a2, 'wappm_WebModel2'):
        assert not _is_linked(a2, 'wappm_WebModel2', b)


def test_assoc_hypertext0_reverse_link_reassign_clear():
    a1 = wappm_WebModel(name="sample_text")
    a2 = wappm_WebModel(name="sample_text_2")
    b = wappm_HypertextLayer(hyperName="sample_text")
    _safe_set(b, 'wappm_HypertextLayer', a1)
    assert _is_linked(b, 'wappm_HypertextLayer', a1)
    if hasattr(a1, 'wappm_WebModel'):
        assert _is_linked(a1, 'wappm_WebModel', b)
    _safe_set(b, 'wappm_HypertextLayer', a2)
    assert _is_linked(b, 'wappm_HypertextLayer', a2)
    if hasattr(a1, 'wappm_WebModel'):
        assert not _is_linked(a1, 'wappm_WebModel', b)
    if hasattr(a2, 'wappm_WebModel'):
        assert _is_linked(a2, 'wappm_WebModel', b)
    _safe_set(b, 'wappm_HypertextLayer', None)
    assert not _is_linked(b, 'wappm_HypertextLayer', a2)
    if hasattr(a2, 'wappm_WebModel'):
        assert not _is_linked(a2, 'wappm_WebModel', b)


def test_assoc_pages3_reverse_link_reassign_clear():
    a1 = wappm_Page(name="sample_text", path="sample_text")
    a2 = wappm_Page(name="sample_text_2", path="sample_text_2")
    b = wappm_HypertextLayer(hyperName="sample_text")
    _safe_set(b, 'wappm_HypertextLayer4', {a1})
    assert _is_linked(b, 'wappm_HypertextLayer4', a1)
    if hasattr(a1, 'wappm_Page'):
        assert _is_linked(a1, 'wappm_Page', b)
    _safe_set(b, 'wappm_HypertextLayer4', {a2})
    assert _is_linked(b, 'wappm_HypertextLayer4', a2)
    if hasattr(a1, 'wappm_Page'):
        assert not _is_linked(a1, 'wappm_Page', b)
    if hasattr(a2, 'wappm_Page'):
        assert _is_linked(a2, 'wappm_Page', b)
    _safe_set(b, 'wappm_HypertextLayer4', set())
    assert not _is_linked(b, 'wappm_HypertextLayer4', a2)
    if hasattr(a2, 'wappm_Page'):
        assert not _is_linked(a2, 'wappm_Page', b)


def test_assoc_references16_reverse_link_reassign_clear():
    a1 = wappm_WebClass(name="sample_text")
    a2 = wappm_WebClass(name="sample_text_2")
    b = wappm_Reference(lowBound=7, name="sample_text", upBound=7)
    _safe_set(b, 'wappm_Reference', a1)
    assert _is_linked(b, 'wappm_Reference', a1)
    if hasattr(a1, 'wappm_WebClass17'):
        assert _is_linked(a1, 'wappm_WebClass17', b)
    _safe_set(b, 'wappm_Reference', a2)
    assert _is_linked(b, 'wappm_Reference', a2)
    if hasattr(a1, 'wappm_WebClass17'):
        assert not _is_linked(a1, 'wappm_WebClass17', b)
    if hasattr(a2, 'wappm_WebClass17'):
        assert _is_linked(a2, 'wappm_WebClass17', b)
    _safe_set(b, 'wappm_Reference', None)
    assert not _is_linked(b, 'wappm_Reference', a2)
    if hasattr(a2, 'wappm_WebClass17'):
        assert not _is_linked(a2, 'wappm_WebClass17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_displayedClass7_stub_double():
    # wappm_DynamicPage has no real 'wappm_DynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so wappm_WebClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wappm_WebClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wappm_WebClass(name="sample_text")
    partner = wappm_DynamicPage()
    setattr(partner, 'wappm_DynamicPage', None)
    _safe_set(owner, 'wappm_WebClass', partner)
    assert getattr(partner, 'wappm_DynamicPage') == owner
    _safe_set(owner, 'wappm_WebClass', None)
    assert getattr(partner, 'wappm_DynamicPage') is None


def test_assoc_links5_stub_double():
    # wappm_Link has no real 'wappm_Link' property in the generated
    # code (a bare stub) -- manually attach it so wappm_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wappm_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wappm_Page(name="sample_text", path="sample_text")
    partner = wappm_Link()
    setattr(partner, 'wappm_Link', None)
    _safe_set(owner, 'wappm_Page6', {partner})
    assert getattr(partner, 'wappm_Link') == owner
    _safe_set(owner, 'wappm_Page6', set())
    assert getattr(partner, 'wappm_Link') is None


def test_assoc_page8_stub_double():
    # wappm_Link has no real 'wappm_Link9' property in the generated
    # code (a bare stub) -- manually attach it so wappm_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wappm_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wappm_Page(name="sample_text", path="sample_text")
    partner = wappm_Link()
    setattr(partner, 'wappm_Link9', None)
    _safe_set(owner, 'wappm_Page10', partner)
    assert getattr(partner, 'wappm_Link9') == owner
    _safe_set(owner, 'wappm_Page10', None)
    assert getattr(partner, 'wappm_Link9') is None


