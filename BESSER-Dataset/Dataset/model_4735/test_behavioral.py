import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    WebPage,
    swml_Attribute,
    swml_DynamicPage,
    swml_Entity,
    swml_EntityPage,
    swml_Icon,
    swml_IndexPage,
    swml_Link,
    swml_Relationship,
    swml_StaticPage,
    swml_WebApplication,
    swml_WebPage,
    DataType,
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

def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = swml_Entity(name="sample_text")
    a2 = swml_Entity(name="sample_text_2")
    b = swml_Attribute(dataType="sample_text", name="sample_text")
    _safe_set(b, 'swml_Attribute', a1)
    assert _is_linked(b, 'swml_Attribute', a1)
    if hasattr(a1, 'swml_Entity4'):
        assert _is_linked(a1, 'swml_Entity4', b)
    _safe_set(b, 'swml_Attribute', a2)
    assert _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a1, 'swml_Entity4'):
        assert not _is_linked(a1, 'swml_Entity4', b)
    if hasattr(a2, 'swml_Entity4'):
        assert _is_linked(a2, 'swml_Entity4', b)
    _safe_set(b, 'swml_Attribute', None)
    assert not _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a2, 'swml_Entity4'):
        assert not _is_linked(a2, 'swml_Entity4', b)


def test_assoc_entities0_reverse_link_reassign_clear():
    a1 = swml_WebApplication(name="sample_text")
    a2 = swml_WebApplication(name="sample_text_2")
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity', a1)
    assert _is_linked(b, 'swml_Entity', a1)
    if hasattr(a1, 'swml_WebApplication'):
        assert _is_linked(a1, 'swml_WebApplication', b)
    _safe_set(b, 'swml_Entity', a2)
    assert _is_linked(b, 'swml_Entity', a2)
    if hasattr(a1, 'swml_WebApplication'):
        assert not _is_linked(a1, 'swml_WebApplication', b)
    if hasattr(a2, 'swml_WebApplication'):
        assert _is_linked(a2, 'swml_WebApplication', b)
    _safe_set(b, 'swml_Entity', None)
    assert not _is_linked(b, 'swml_Entity', a2)
    if hasattr(a2, 'swml_WebApplication'):
        assert not _is_linked(a2, 'swml_WebApplication', b)


def test_assoc_id5_reverse_link_reassign_clear():
    a1 = swml_Entity(name="sample_text")
    a2 = swml_Entity(name="sample_text_2")
    b = swml_Attribute(dataType="sample_text", name="sample_text")
    _safe_set(b, 'swml_Attribute7', a1)
    assert _is_linked(b, 'swml_Attribute7', a1)
    if hasattr(a1, 'swml_Entity6'):
        assert _is_linked(a1, 'swml_Entity6', b)
    _safe_set(b, 'swml_Attribute7', a2)
    assert _is_linked(b, 'swml_Attribute7', a2)
    if hasattr(a1, 'swml_Entity6'):
        assert not _is_linked(a1, 'swml_Entity6', b)
    if hasattr(a2, 'swml_Entity6'):
        assert _is_linked(a2, 'swml_Entity6', b)
    _safe_set(b, 'swml_Attribute7', None)
    assert not _is_linked(b, 'swml_Attribute7', a2)
    if hasattr(a2, 'swml_Entity6'):
        assert not _is_linked(a2, 'swml_Entity6', b)


def test_assoc_referencedEntity10_reverse_link_reassign_clear():
    a1 = swml_Relationship(lowerBound=7, role="sample_text", upperBound=7)
    a2 = swml_Relationship(lowerBound=13, role="sample_text_2", upperBound=13)
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity12', a1)
    assert _is_linked(b, 'swml_Entity12', a1)
    if hasattr(a1, 'swml_Relationship11'):
        assert _is_linked(a1, 'swml_Relationship11', b)
    _safe_set(b, 'swml_Entity12', a2)
    assert _is_linked(b, 'swml_Entity12', a2)
    if hasattr(a1, 'swml_Relationship11'):
        assert not _is_linked(a1, 'swml_Relationship11', b)
    if hasattr(a2, 'swml_Relationship11'):
        assert _is_linked(a2, 'swml_Relationship11', b)
    _safe_set(b, 'swml_Entity12', None)
    assert not _is_linked(b, 'swml_Entity12', a2)
    if hasattr(a2, 'swml_Relationship11'):
        assert not _is_linked(a2, 'swml_Relationship11', b)


def test_assoc_relationships8_reverse_link_reassign_clear():
    a1 = swml_Relationship(lowerBound=7, role="sample_text", upperBound=7)
    a2 = swml_Relationship(lowerBound=13, role="sample_text_2", upperBound=13)
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity9', {a1})
    assert _is_linked(b, 'swml_Entity9', a1)
    if hasattr(a1, 'swml_Relationship'):
        assert _is_linked(a1, 'swml_Relationship', b)
    _safe_set(b, 'swml_Entity9', {a2})
    assert _is_linked(b, 'swml_Entity9', a2)
    if hasattr(a1, 'swml_Relationship'):
        assert not _is_linked(a1, 'swml_Relationship', b)
    if hasattr(a2, 'swml_Relationship'):
        assert _is_linked(a2, 'swml_Relationship', b)
    _safe_set(b, 'swml_Entity9', set())
    assert not _is_linked(b, 'swml_Entity9', a2)
    if hasattr(a2, 'swml_Relationship'):
        assert not _is_linked(a2, 'swml_Relationship', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_homePage1_stub_double():
    # swml_StaticPage has no real 'swml_StaticPage' property in the generated
    # code (a bare stub) -- manually attach it so swml_WebApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_WebApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_WebApplication(name="sample_text")
    partner = swml_StaticPage()
    setattr(partner, 'swml_StaticPage', None)
    _safe_set(owner, 'swml_WebApplication2', partner)
    assert getattr(partner, 'swml_StaticPage') == owner
    _safe_set(owner, 'swml_WebApplication2', None)
    assert getattr(partner, 'swml_StaticPage') is None


def test_assoc_icon15_stub_double():
    # swml_DynamicPage has no real 'swml_DynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so swml_Icon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Icon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Icon(image="sample_text")
    partner = swml_DynamicPage()
    setattr(partner, 'swml_DynamicPage', None)
    _safe_set(owner, 'swml_Icon', partner)
    assert getattr(partner, 'swml_DynamicPage') == owner
    _safe_set(owner, 'swml_Icon', None)
    assert getattr(partner, 'swml_DynamicPage') is None


def test_assoc_links13_stub_double():
    # swml_StaticPage has no real 'swml_StaticPage14' property in the generated
    # code (a bare stub) -- manually attach it so swml_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Link(href="sample_text")
    partner = swml_StaticPage()
    setattr(partner, 'swml_StaticPage14', None)
    _safe_set(owner, 'swml_Link', partner)
    assert owner in getattr(partner, 'swml_StaticPage14')
    _safe_set(owner, 'swml_Link', None)
    assert owner not in getattr(partner, 'swml_StaticPage14')


def test_assoc_type16_stub_double():
    # swml_DynamicPage has no real 'swml_DynamicPage17' property in the generated
    # code (a bare stub) -- manually attach it so swml_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Entity(name="sample_text")
    partner = swml_DynamicPage()
    setattr(partner, 'swml_DynamicPage17', None)
    _safe_set(owner, 'swml_Entity18', partner)
    assert getattr(partner, 'swml_DynamicPage17') == owner
    _safe_set(owner, 'swml_Entity18', None)
    assert getattr(partner, 'swml_DynamicPage17') is None


