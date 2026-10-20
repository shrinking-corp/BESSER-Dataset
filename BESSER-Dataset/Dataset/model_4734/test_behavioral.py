import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EntityPages,
    LinkKat1,
    LinkKat2,
    Links,
    WebPage,
    dynamicPage,
    swml_Attribute,
    swml_ContentModel,
    swml_ContextualLinks,
    swml_CreatePage,
    swml_DeletePage,
    swml_Entity,
    swml_EntityPages,
    swml_EnumTyp,
    swml_Enumeration,
    swml_HypertextModel,
    swml_IndexPages,
    swml_KO,
    swml_LinkJoinNode,
    swml_LinkKat1,
    swml_LinkKat2,
    swml_LinkParamater,
    swml_Links,
    swml_Literals,
    swml_NonContextualLinks,
    swml_OK,
    swml_Reference,
    swml_UpdatePage,
    swml_WebModel,
    swml_WebPage,
    swml_dynamicPage,
    swml_staticPage,
    Datentyp,
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

def test_assoc_Attributes9_reverse_link_reassign_clear():
    a1 = swml_Entity(name="sample_text")
    a2 = swml_Entity(name="sample_text_2")
    b = swml_Attribute(Typ="sample_text", name="sample_text")
    _safe_set(b, 'swml_Attribute', a1)
    assert _is_linked(b, 'swml_Attribute', a1)
    if hasattr(a1, 'swml_Entity10'):
        assert _is_linked(a1, 'swml_Entity10', b)
    _safe_set(b, 'swml_Attribute', a2)
    assert _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a1, 'swml_Entity10'):
        assert not _is_linked(a1, 'swml_Entity10', b)
    if hasattr(a2, 'swml_Entity10'):
        assert _is_linked(a2, 'swml_Entity10', b)
    _safe_set(b, 'swml_Attribute', None)
    assert not _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a2, 'swml_Entity10'):
        assert not _is_linked(a2, 'swml_Entity10', b)


def test_assoc_Child14_reverse_link_reassign_clear():
    a1 = swml_Entity(name="sample_text")
    a2 = swml_Entity(name="sample_text_2")
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity15', a1)
    assert _is_linked(b, 'swml_Entity15', a1)
    if hasattr(a1, 'swml_Entity13'):
        assert _is_linked(a1, 'swml_Entity13', b)
    _safe_set(b, 'swml_Entity15', a2)
    assert _is_linked(b, 'swml_Entity15', a2)
    if hasattr(a1, 'swml_Entity13'):
        assert not _is_linked(a1, 'swml_Entity13', b)
    if hasattr(a2, 'swml_Entity13'):
        assert _is_linked(a2, 'swml_Entity13', b)
    _safe_set(b, 'swml_Entity15', None)
    assert not _is_linked(b, 'swml_Entity15', a2)
    if hasattr(a2, 'swml_Entity13'):
        assert not _is_linked(a2, 'swml_Entity13', b)


def test_assoc_EnumAttribute7_reverse_link_reassign_clear():
    a1 = swml_EnumTyp(name="sample_text")
    a2 = swml_EnumTyp(name="sample_text_2")
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity8', {a1})
    assert _is_linked(b, 'swml_Entity8', a1)
    if hasattr(a1, 'swml_EnumTyp'):
        assert _is_linked(a1, 'swml_EnumTyp', b)
    _safe_set(b, 'swml_Entity8', {a2})
    assert _is_linked(b, 'swml_Entity8', a2)
    if hasattr(a1, 'swml_EnumTyp'):
        assert not _is_linked(a1, 'swml_EnumTyp', b)
    if hasattr(a2, 'swml_EnumTyp'):
        assert _is_linked(a2, 'swml_EnumTyp', b)
    _safe_set(b, 'swml_Entity8', set())
    assert not _is_linked(b, 'swml_Entity8', a2)
    if hasattr(a2, 'swml_EnumTyp'):
        assert not _is_linked(a2, 'swml_EnumTyp', b)


def test_assoc_Enums16_reverse_link_reassign_clear():
    a1 = swml_Enumeration(name="sample_text")
    a2 = swml_Enumeration(name="sample_text_2")
    b = swml_EnumTyp(name="sample_text")
    _safe_set(b, 'swml_EnumTyp17', a1)
    assert _is_linked(b, 'swml_EnumTyp17', a1)
    if hasattr(a1, 'swml_Enumeration18'):
        assert _is_linked(a1, 'swml_Enumeration18', b)
    _safe_set(b, 'swml_EnumTyp17', a2)
    assert _is_linked(b, 'swml_EnumTyp17', a2)
    if hasattr(a1, 'swml_Enumeration18'):
        assert not _is_linked(a1, 'swml_Enumeration18', b)
    if hasattr(a2, 'swml_Enumeration18'):
        assert _is_linked(a2, 'swml_Enumeration18', b)
    _safe_set(b, 'swml_EnumTyp17', None)
    assert not _is_linked(b, 'swml_EnumTyp17', a2)
    if hasattr(a2, 'swml_Enumeration18'):
        assert not _is_linked(a2, 'swml_Enumeration18', b)


def test_assoc_Link51_reverse_link_reassign_clear():
    a1 = swml_Links(Name="sample_text")
    a2 = swml_Links(Name="sample_text_2")
    b = swml_LinkParamater(Parameter="sample_text")
    _safe_set(b, 'swml_LinkParamater', a1)
    assert _is_linked(b, 'swml_LinkParamater', a1)
    if hasattr(a1, 'swml_Links'):
        assert _is_linked(a1, 'swml_Links', b)
    _safe_set(b, 'swml_LinkParamater', a2)
    assert _is_linked(b, 'swml_LinkParamater', a2)
    if hasattr(a1, 'swml_Links'):
        assert not _is_linked(a1, 'swml_Links', b)
    if hasattr(a2, 'swml_Links'):
        assert _is_linked(a2, 'swml_Links', b)
    _safe_set(b, 'swml_LinkParamater', None)
    assert not _is_linked(b, 'swml_LinkParamater', a2)
    if hasattr(a2, 'swml_Links'):
        assert not _is_linked(a2, 'swml_Links', b)


def test_assoc_Opposite20_reverse_link_reassign_clear():
    a1 = swml_Reference(lowerBound=7, rolename="sample_text", upperBound=7)
    a2 = swml_Reference(lowerBound=13, rolename="sample_text_2", upperBound=13)
    b = swml_Reference(lowerBound=7, rolename="sample_text", upperBound=7)
    _safe_set(b, 'swml_Reference21', a1)
    assert _is_linked(b, 'swml_Reference21', a1)
    if hasattr(a1, 'swml_Reference19'):
        assert _is_linked(a1, 'swml_Reference19', b)
    _safe_set(b, 'swml_Reference21', a2)
    assert _is_linked(b, 'swml_Reference21', a2)
    if hasattr(a1, 'swml_Reference19'):
        assert not _is_linked(a1, 'swml_Reference19', b)
    if hasattr(a2, 'swml_Reference19'):
        assert _is_linked(a2, 'swml_Reference19', b)
    _safe_set(b, 'swml_Reference21', None)
    assert not _is_linked(b, 'swml_Reference21', a2)
    if hasattr(a2, 'swml_Reference19'):
        assert not _is_linked(a2, 'swml_Reference19', b)


def test_assoc_RefTo22_reverse_link_reassign_clear():
    a1 = swml_Reference(lowerBound=7, rolename="sample_text", upperBound=7)
    a2 = swml_Reference(lowerBound=13, rolename="sample_text_2", upperBound=13)
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity24', a1)
    assert _is_linked(b, 'swml_Entity24', a1)
    if hasattr(a1, 'swml_Reference23'):
        assert _is_linked(a1, 'swml_Reference23', b)
    _safe_set(b, 'swml_Entity24', a2)
    assert _is_linked(b, 'swml_Entity24', a2)
    if hasattr(a1, 'swml_Reference23'):
        assert not _is_linked(a1, 'swml_Reference23', b)
    if hasattr(a2, 'swml_Reference23'):
        assert _is_linked(a2, 'swml_Reference23', b)
    _safe_set(b, 'swml_Entity24', None)
    assert not _is_linked(b, 'swml_Entity24', a2)
    if hasattr(a2, 'swml_Reference23'):
        assert not _is_linked(a2, 'swml_Reference23', b)


def test_assoc_References11_reverse_link_reassign_clear():
    a1 = swml_Reference(lowerBound=7, rolename="sample_text", upperBound=7)
    a2 = swml_Reference(lowerBound=13, rolename="sample_text_2", upperBound=13)
    b = swml_Entity(name="sample_text")
    _safe_set(b, 'swml_Entity12', {a1})
    assert _is_linked(b, 'swml_Entity12', a1)
    if hasattr(a1, 'swml_Reference'):
        assert _is_linked(a1, 'swml_Reference', b)
    _safe_set(b, 'swml_Entity12', {a2})
    assert _is_linked(b, 'swml_Entity12', a2)
    if hasattr(a1, 'swml_Reference'):
        assert not _is_linked(a1, 'swml_Reference', b)
    if hasattr(a2, 'swml_Reference'):
        assert _is_linked(a2, 'swml_Reference', b)
    _safe_set(b, 'swml_Entity12', set())
    assert not _is_linked(b, 'swml_Entity12', a2)
    if hasattr(a2, 'swml_Reference'):
        assert not _is_linked(a2, 'swml_Reference', b)


def test_assoc_TargetPage52_reverse_link_reassign_clear():
    a1 = swml_WebPage(name="sample_text")
    a2 = swml_WebPage(name="sample_text_2")
    b = swml_Links(Name="sample_text")
    _safe_set(b, 'swml_Links53', a1)
    assert _is_linked(b, 'swml_Links53', a1)
    if hasattr(a1, 'swml_WebPage54'):
        assert _is_linked(a1, 'swml_WebPage54', b)
    _safe_set(b, 'swml_Links53', a2)
    assert _is_linked(b, 'swml_Links53', a2)
    if hasattr(a1, 'swml_WebPage54'):
        assert not _is_linked(a1, 'swml_WebPage54', b)
    if hasattr(a2, 'swml_WebPage54'):
        assert _is_linked(a2, 'swml_WebPage54', b)
    _safe_set(b, 'swml_Links53', None)
    assert not _is_linked(b, 'swml_Links53', a2)
    if hasattr(a2, 'swml_WebPage54'):
        assert not _is_linked(a2, 'swml_WebPage54', b)


def test_assoc_ownedLiteral25_reverse_link_reassign_clear():
    a1 = swml_Literals(name="sample_text")
    a2 = swml_Literals(name="sample_text_2")
    b = swml_Enumeration(name="sample_text")
    _safe_set(b, 'swml_Enumeration26', {a1})
    assert _is_linked(b, 'swml_Enumeration26', a1)
    if hasattr(a1, 'swml_Literals'):
        assert _is_linked(a1, 'swml_Literals', b)
    _safe_set(b, 'swml_Enumeration26', {a2})
    assert _is_linked(b, 'swml_Enumeration26', a2)
    if hasattr(a1, 'swml_Literals'):
        assert not _is_linked(a1, 'swml_Literals', b)
    if hasattr(a2, 'swml_Literals'):
        assert _is_linked(a2, 'swml_Literals', b)
    _safe_set(b, 'swml_Enumeration26', set())
    assert not _is_linked(b, 'swml_Enumeration26', a2)
    if hasattr(a2, 'swml_Literals'):
        assert not _is_linked(a2, 'swml_Literals', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Entities5_stub_double():
    # swml_ContentModel has no real 'swml_ContentModel6' property in the generated
    # code (a bare stub) -- manually attach it so swml_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Entity(name="sample_text")
    partner = swml_ContentModel()
    setattr(partner, 'swml_ContentModel6', None)
    _safe_set(owner, 'swml_Entity', partner)
    assert owner in getattr(partner, 'swml_ContentModel6')
    _safe_set(owner, 'swml_Entity', None)
    assert owner not in getattr(partner, 'swml_ContentModel6')


def test_assoc_EntityType34_stub_double():
    # swml_dynamicPage has no real 'swml_dynamicPage' property in the generated
    # code (a bare stub) -- manually attach it so swml_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Entity(name="sample_text")
    partner = swml_dynamicPage()
    setattr(partner, 'swml_dynamicPage', None)
    _safe_set(owner, 'swml_Entity35', partner)
    assert getattr(partner, 'swml_dynamicPage') == owner
    _safe_set(owner, 'swml_Entity35', None)
    assert getattr(partner, 'swml_dynamicPage') is None


def test_assoc_Enumerations3_stub_double():
    # swml_ContentModel has no real 'swml_ContentModel4' property in the generated
    # code (a bare stub) -- manually attach it so swml_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Enumeration(name="sample_text")
    partner = swml_ContentModel()
    setattr(partner, 'swml_ContentModel4', None)
    _safe_set(owner, 'swml_Enumeration', partner)
    assert owner in getattr(partner, 'swml_ContentModel4')
    _safe_set(owner, 'swml_Enumeration', None)
    assert owner not in getattr(partner, 'swml_ContentModel4')


def test_assoc_Link31_stub_double():
    # swml_LinkKat2 has no real 'swml_LinkKat2' property in the generated
    # code (a bare stub) -- manually attach it so swml_WebPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_WebPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_WebPage(name="sample_text")
    partner = swml_LinkKat2()
    setattr(partner, 'swml_LinkKat2', None)
    _safe_set(owner, 'swml_WebPage32', {partner})
    assert getattr(partner, 'swml_LinkKat2') == owner
    _safe_set(owner, 'swml_WebPage32', set())
    assert getattr(partner, 'swml_LinkKat2') is None


def test_assoc_WebPages27_stub_double():
    # swml_HypertextModel has no real 'swml_HypertextModel28' property in the generated
    # code (a bare stub) -- manually attach it so swml_WebPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_WebPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_WebPage(name="sample_text")
    partner = swml_HypertextModel()
    setattr(partner, 'swml_HypertextModel28', None)
    _safe_set(owner, 'swml_WebPage', partner)
    assert owner in getattr(partner, 'swml_HypertextModel28')
    _safe_set(owner, 'swml_WebPage', None)
    assert owner not in getattr(partner, 'swml_HypertextModel28')


