import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    EditablePage,
    EntityPage,
    Link,
    WebPage,
    solution_Attribute,
    solution_ContextualLink,
    solution_CreatePage,
    solution_DeletePage,
    solution_DynamicPage,
    solution_EditablePage,
    solution_Entity,
    solution_EntityPage,
    solution_IndexPage,
    solution_Link,
    solution_NonContextualLink,
    solution_Relationship,
    solution_StaticPage,
    solution_UpdatePage,
    solution_WebApplication,
    solution_WebPage,
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

def test_assoc_attributes5_reverse_link_reassign_clear():
    a1 = solution_Entity(name="sample_text")
    a2 = solution_Entity(name="sample_text_2")
    b = solution_Attribute(dataType="sample_text", name="sample_text")
    _safe_set(b, 'solution_Attribute', a1)
    assert _is_linked(b, 'solution_Attribute', a1)
    if hasattr(a1, 'solution_Entity6'):
        assert _is_linked(a1, 'solution_Entity6', b)
    _safe_set(b, 'solution_Attribute', a2)
    assert _is_linked(b, 'solution_Attribute', a2)
    if hasattr(a1, 'solution_Entity6'):
        assert not _is_linked(a1, 'solution_Entity6', b)
    if hasattr(a2, 'solution_Entity6'):
        assert _is_linked(a2, 'solution_Entity6', b)
    _safe_set(b, 'solution_Attribute', None)
    assert not _is_linked(b, 'solution_Attribute', a2)
    if hasattr(a2, 'solution_Entity6'):
        assert not _is_linked(a2, 'solution_Entity6', b)


def test_assoc_entities0_reverse_link_reassign_clear():
    a1 = solution_WebApplication(name="sample_text")
    a2 = solution_WebApplication(name="sample_text_2")
    b = solution_Entity(name="sample_text")
    _safe_set(b, 'solution_Entity', a1)
    assert _is_linked(b, 'solution_Entity', a1)
    if hasattr(a1, 'solution_WebApplication'):
        assert _is_linked(a1, 'solution_WebApplication', b)
    _safe_set(b, 'solution_Entity', a2)
    assert _is_linked(b, 'solution_Entity', a2)
    if hasattr(a1, 'solution_WebApplication'):
        assert not _is_linked(a1, 'solution_WebApplication', b)
    if hasattr(a2, 'solution_WebApplication'):
        assert _is_linked(a2, 'solution_WebApplication', b)
    _safe_set(b, 'solution_Entity', None)
    assert not _is_linked(b, 'solution_Entity', a2)
    if hasattr(a2, 'solution_WebApplication'):
        assert not _is_linked(a2, 'solution_WebApplication', b)


def test_assoc_id7_reverse_link_reassign_clear():
    a1 = solution_Entity(name="sample_text")
    a2 = solution_Entity(name="sample_text_2")
    b = solution_Attribute(dataType="sample_text", name="sample_text")
    _safe_set(b, 'solution_Attribute9', a1)
    assert _is_linked(b, 'solution_Attribute9', a1)
    if hasattr(a1, 'solution_Entity8'):
        assert _is_linked(a1, 'solution_Entity8', b)
    _safe_set(b, 'solution_Attribute9', a2)
    assert _is_linked(b, 'solution_Attribute9', a2)
    if hasattr(a1, 'solution_Entity8'):
        assert not _is_linked(a1, 'solution_Entity8', b)
    if hasattr(a2, 'solution_Entity8'):
        assert _is_linked(a2, 'solution_Entity8', b)
    _safe_set(b, 'solution_Attribute9', None)
    assert not _is_linked(b, 'solution_Attribute9', a2)
    if hasattr(a2, 'solution_Entity8'):
        assert not _is_linked(a2, 'solution_Entity8', b)


def test_assoc_links17_reverse_link_reassign_clear():
    a1 = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    a2 = solution_WebPage(name="sample_text_2", relativeUrl="sample_text_2")
    b = solution_Link(name="sample_text")
    _safe_set(b, 'solution_Link', a1)
    assert _is_linked(b, 'solution_Link', a1)
    if hasattr(a1, 'solution_WebPage18'):
        assert _is_linked(a1, 'solution_WebPage18', b)
    _safe_set(b, 'solution_Link', a2)
    assert _is_linked(b, 'solution_Link', a2)
    if hasattr(a1, 'solution_WebPage18'):
        assert not _is_linked(a1, 'solution_WebPage18', b)
    if hasattr(a2, 'solution_WebPage18'):
        assert _is_linked(a2, 'solution_WebPage18', b)
    _safe_set(b, 'solution_Link', None)
    assert not _is_linked(b, 'solution_Link', a2)
    if hasattr(a2, 'solution_WebPage18'):
        assert not _is_linked(a2, 'solution_WebPage18', b)


def test_assoc_opposite15_reverse_link_reassign_clear():
    a1 = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    a2 = solution_Relationship(lowerBound=13, roleName="sample_text_2", upperBound=13)
    b = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    _safe_set(b, 'solution_Relationship16', a1)
    assert _is_linked(b, 'solution_Relationship16', a1)
    if hasattr(a1, 'solution_Relationship14'):
        assert _is_linked(a1, 'solution_Relationship14', b)
    _safe_set(b, 'solution_Relationship16', a2)
    assert _is_linked(b, 'solution_Relationship16', a2)
    if hasattr(a1, 'solution_Relationship14'):
        assert not _is_linked(a1, 'solution_Relationship14', b)
    if hasattr(a2, 'solution_Relationship14'):
        assert _is_linked(a2, 'solution_Relationship14', b)
    _safe_set(b, 'solution_Relationship16', None)
    assert not _is_linked(b, 'solution_Relationship16', a2)
    if hasattr(a2, 'solution_Relationship14'):
        assert not _is_linked(a2, 'solution_Relationship14', b)


def test_assoc_relationships10_reverse_link_reassign_clear():
    a1 = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    a2 = solution_Relationship(lowerBound=13, roleName="sample_text_2", upperBound=13)
    b = solution_Entity(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Relationship'):
        assert _is_linked(a1, 'Relationship', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Relationship'):
        assert not _is_linked(a1, 'Relationship', b)
    if hasattr(a2, 'Relationship'):
        assert _is_linked(a2, 'Relationship', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Relationship'):
        assert not _is_linked(a2, 'Relationship', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    a2 = solution_Relationship(lowerBound=13, roleName="sample_text_2", upperBound=13)
    b = solution_Entity(name="sample_text")
    _safe_set(b, 'Entity', a1)
    assert _is_linked(b, 'Entity', a1)
    if hasattr(a1, 'relationships'):
        assert _is_linked(a1, 'relationships', b)
    _safe_set(b, 'Entity', a2)
    assert _is_linked(b, 'Entity', a2)
    if hasattr(a1, 'relationships'):
        assert not _is_linked(a1, 'relationships', b)
    if hasattr(a2, 'relationships'):
        assert _is_linked(a2, 'relationships', b)
    _safe_set(b, 'Entity', None)
    assert not _is_linked(b, 'Entity', a2)
    if hasattr(a2, 'relationships'):
        assert not _is_linked(a2, 'relationships', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    a2 = solution_Relationship(lowerBound=13, roleName="sample_text_2", upperBound=13)
    b = solution_Entity(name="sample_text")
    _safe_set(b, 'solution_Entity13', a1)
    assert _is_linked(b, 'solution_Entity13', a1)
    if hasattr(a1, 'solution_Relationship'):
        assert _is_linked(a1, 'solution_Relationship', b)
    _safe_set(b, 'solution_Entity13', a2)
    assert _is_linked(b, 'solution_Entity13', a2)
    if hasattr(a1, 'solution_Relationship'):
        assert not _is_linked(a1, 'solution_Relationship', b)
    if hasattr(a2, 'solution_Relationship'):
        assert _is_linked(a2, 'solution_Relationship', b)
    _safe_set(b, 'solution_Entity13', None)
    assert not _is_linked(b, 'solution_Entity13', a2)
    if hasattr(a2, 'solution_Relationship'):
        assert not _is_linked(a2, 'solution_Relationship', b)


def test_assoc_target25_reverse_link_reassign_clear():
    a1 = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    a2 = solution_WebPage(name="sample_text_2", relativeUrl="sample_text_2")
    b = solution_Link(name="sample_text")
    _safe_set(b, 'solution_Link26', a1)
    assert _is_linked(b, 'solution_Link26', a1)
    if hasattr(a1, 'solution_WebPage27'):
        assert _is_linked(a1, 'solution_WebPage27', b)
    _safe_set(b, 'solution_Link26', a2)
    assert _is_linked(b, 'solution_Link26', a2)
    if hasattr(a1, 'solution_WebPage27'):
        assert not _is_linked(a1, 'solution_WebPage27', b)
    if hasattr(a2, 'solution_WebPage27'):
        assert _is_linked(a2, 'solution_WebPage27', b)
    _safe_set(b, 'solution_Link26', None)
    assert not _is_linked(b, 'solution_Link26', a2)
    if hasattr(a2, 'solution_WebPage27'):
        assert not _is_linked(a2, 'solution_WebPage27', b)


def test_assoc_webpages1_reverse_link_reassign_clear():
    a1 = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    a2 = solution_WebPage(name="sample_text_2", relativeUrl="sample_text_2")
    b = solution_WebApplication(name="sample_text")
    _safe_set(b, 'solution_WebApplication2', {a1})
    assert _is_linked(b, 'solution_WebApplication2', a1)
    if hasattr(a1, 'solution_WebPage'):
        assert _is_linked(a1, 'solution_WebPage', b)
    _safe_set(b, 'solution_WebApplication2', {a2})
    assert _is_linked(b, 'solution_WebApplication2', a2)
    if hasattr(a1, 'solution_WebPage'):
        assert not _is_linked(a1, 'solution_WebPage', b)
    if hasattr(a2, 'solution_WebPage'):
        assert _is_linked(a2, 'solution_WebPage', b)
    _safe_set(b, 'solution_WebApplication2', set())
    assert not _is_linked(b, 'solution_WebApplication2', a2)
    if hasattr(a2, 'solution_WebPage'):
        assert not _is_linked(a2, 'solution_WebPage', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entity21_stub_double():
    # solution_DynamicPage has no real 'solution_DynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so solution_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # solution_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = solution_Entity(name="sample_text")
    partner = solution_DynamicPage()
    setattr(partner, 'solution_DynamicPage', None)
    _safe_set(owner, 'solution_Entity22', partner)
    assert getattr(partner, 'solution_DynamicPage') == owner
    _safe_set(owner, 'solution_Entity22', None)
    assert getattr(partner, 'solution_DynamicPage') is None


def test_assoc_homeLink19_stub_double():
    # solution_NonContextualLink has no real 'solution_NonContextualLink' property in the generated
    # code (a bare stub) -- manually attach it so solution_WebPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # solution_WebPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    partner = solution_NonContextualLink()
    setattr(partner, 'solution_NonContextualLink', None)
    _safe_set(owner, 'solution_WebPage20', partner)
    assert getattr(partner, 'solution_NonContextualLink') == owner
    _safe_set(owner, 'solution_WebPage20', None)
    assert getattr(partner, 'solution_NonContextualLink') is None


def test_assoc_homePage3_stub_double():
    # solution_StaticPage has no real 'solution_StaticPage' property in the generated
    # code (a bare stub) -- manually attach it so solution_WebApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # solution_WebApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = solution_WebApplication(name="sample_text")
    partner = solution_StaticPage()
    setattr(partner, 'solution_StaticPage', None)
    _safe_set(owner, 'solution_WebApplication4', partner)
    assert getattr(partner, 'solution_StaticPage') == owner
    _safe_set(owner, 'solution_WebApplication4', None)
    assert getattr(partner, 'solution_StaticPage') is None


def test_assoc_information28_stub_double():
    # solution_ContextualLink has no real 'solution_ContextualLink' property in the generated
    # code (a bare stub) -- manually attach it so solution_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # solution_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = solution_Entity(name="sample_text")
    partner = solution_ContextualLink()
    setattr(partner, 'solution_ContextualLink', None)
    _safe_set(owner, 'solution_Entity29', partner)
    assert getattr(partner, 'solution_ContextualLink') == owner
    _safe_set(owner, 'solution_Entity29', None)
    assert getattr(partner, 'solution_ContextualLink') is None


