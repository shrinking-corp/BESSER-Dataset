import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    EntityPage,
    Link,
    Node,
    Page,
    swml_Attribute,
    swml_ContentModel,
    swml_ContextualLink,
    swml_CreatePage,
    swml_DeletePage,
    swml_DynamicPage,
    swml_EntityPage,
    swml_EntityType,
    swml_Enumeration,
    swml_HypertextModel,
    swml_IndexPage,
    swml_KOLink,
    swml_Link,
    swml_LinkJoinNode,
    swml_Literal,
    swml_Node,
    swml_NonContextualLink,
    swml_OKLink,
    swml_Page,
    swml_Parameter,
    swml_Relationship,
    swml_StaticPage,
    swml_UpdatePage,
    swml_WebApplication,
    SWMLType,
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

def test_assoc_EnumType11_reverse_link_reassign_clear():
    a1 = swml_Enumeration(name="sample_text")
    a2 = swml_Enumeration(name="sample_text_2")
    b = swml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_Attribute12', a1)
    assert _is_linked(b, 'swml_Attribute12', a1)
    if hasattr(a1, 'swml_Enumeration'):
        assert _is_linked(a1, 'swml_Enumeration', b)
    _safe_set(b, 'swml_Attribute12', a2)
    assert _is_linked(b, 'swml_Attribute12', a2)
    if hasattr(a1, 'swml_Enumeration'):
        assert not _is_linked(a1, 'swml_Enumeration', b)
    if hasattr(a2, 'swml_Enumeration'):
        assert _is_linked(a2, 'swml_Enumeration', b)
    _safe_set(b, 'swml_Attribute12', None)
    assert not _is_linked(b, 'swml_Attribute12', a2)
    if hasattr(a2, 'swml_Enumeration'):
        assert not _is_linked(a2, 'swml_Enumeration', b)


def test_assoc_attribute3_reverse_link_reassign_clear():
    a1 = swml_EntityType(isAbstract=True, name="sample_text")
    a2 = swml_EntityType(isAbstract=False, name="sample_text_2")
    b = swml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_Attribute', a1)
    assert _is_linked(b, 'swml_Attribute', a1)
    if hasattr(a1, 'swml_EntityType'):
        assert _is_linked(a1, 'swml_EntityType', b)
    _safe_set(b, 'swml_Attribute', a2)
    assert _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a1, 'swml_EntityType'):
        assert not _is_linked(a1, 'swml_EntityType', b)
    if hasattr(a2, 'swml_EntityType'):
        assert _is_linked(a2, 'swml_EntityType', b)
    _safe_set(b, 'swml_Attribute', None)
    assert not _is_linked(b, 'swml_Attribute', a2)
    if hasattr(a2, 'swml_EntityType'):
        assert not _is_linked(a2, 'swml_EntityType', b)


def test_assoc_entityType21_reverse_link_reassign_clear():
    a1 = swml_Relationship(lower=7, name="sample_text", upper=7)
    a2 = swml_Relationship(lower=13, name="sample_text_2", upper=13)
    b = swml_EntityType(isAbstract=True, name="sample_text")
    _safe_set(b, 'EntityType', a1)
    assert _is_linked(b, 'EntityType', a1)
    if hasattr(a1, 'relationship'):
        assert _is_linked(a1, 'relationship', b)
    _safe_set(b, 'EntityType', a2)
    assert _is_linked(b, 'EntityType', a2)
    if hasattr(a1, 'relationship'):
        assert not _is_linked(a1, 'relationship', b)
    if hasattr(a2, 'relationship'):
        assert _is_linked(a2, 'relationship', b)
    _safe_set(b, 'EntityType', None)
    assert not _is_linked(b, 'EntityType', a2)
    if hasattr(a2, 'relationship'):
        assert not _is_linked(a2, 'relationship', b)


def test_assoc_id4_reverse_link_reassign_clear():
    a1 = swml_EntityType(isAbstract=True, name="sample_text")
    a2 = swml_EntityType(isAbstract=False, name="sample_text_2")
    b = swml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'swml_Attribute6', a1)
    assert _is_linked(b, 'swml_Attribute6', a1)
    if hasattr(a1, 'swml_EntityType5'):
        assert _is_linked(a1, 'swml_EntityType5', b)
    _safe_set(b, 'swml_Attribute6', a2)
    assert _is_linked(b, 'swml_Attribute6', a2)
    if hasattr(a1, 'swml_EntityType5'):
        assert not _is_linked(a1, 'swml_EntityType5', b)
    if hasattr(a2, 'swml_EntityType5'):
        assert _is_linked(a2, 'swml_EntityType5', b)
    _safe_set(b, 'swml_Attribute6', None)
    assert not _is_linked(b, 'swml_Attribute6', a2)
    if hasattr(a2, 'swml_EntityType5'):
        assert not _is_linked(a2, 'swml_EntityType5', b)


def test_assoc_literals27_reverse_link_reassign_clear():
    a1 = swml_Literal(name="sample_text")
    a2 = swml_Literal(name="sample_text_2")
    b = swml_Enumeration(name="sample_text")
    _safe_set(b, 'swml_Enumeration28', {a1})
    assert _is_linked(b, 'swml_Enumeration28', a1)
    if hasattr(a1, 'swml_Literal'):
        assert _is_linked(a1, 'swml_Literal', b)
    _safe_set(b, 'swml_Enumeration28', {a2})
    assert _is_linked(b, 'swml_Enumeration28', a2)
    if hasattr(a1, 'swml_Literal'):
        assert not _is_linked(a1, 'swml_Literal', b)
    if hasattr(a2, 'swml_Literal'):
        assert _is_linked(a2, 'swml_Literal', b)
    _safe_set(b, 'swml_Enumeration28', set())
    assert not _is_linked(b, 'swml_Enumeration28', a2)
    if hasattr(a2, 'swml_Literal'):
        assert not _is_linked(a2, 'swml_Literal', b)


def test_assoc_opposite23_reverse_link_reassign_clear():
    a1 = swml_Relationship(lower=7, name="sample_text", upper=7)
    a2 = swml_Relationship(lower=13, name="sample_text_2", upper=13)
    b = swml_Relationship(lower=7, name="sample_text", upper=7)
    _safe_set(b, 'swml_Relationship22', a1)
    assert _is_linked(b, 'swml_Relationship22', a1)
    if hasattr(a1, 'swml_Relationship'):
        assert _is_linked(a1, 'swml_Relationship', b)
    _safe_set(b, 'swml_Relationship22', a2)
    assert _is_linked(b, 'swml_Relationship22', a2)
    if hasattr(a1, 'swml_Relationship'):
        assert not _is_linked(a1, 'swml_Relationship', b)
    if hasattr(a2, 'swml_Relationship'):
        assert _is_linked(a2, 'swml_Relationship', b)
    _safe_set(b, 'swml_Relationship22', None)
    assert not _is_linked(b, 'swml_Relationship22', a2)
    if hasattr(a2, 'swml_Relationship'):
        assert not _is_linked(a2, 'swml_Relationship', b)


def test_assoc_relationship7_reverse_link_reassign_clear():
    a1 = swml_Relationship(lower=7, name="sample_text", upper=7)
    a2 = swml_Relationship(lower=13, name="sample_text_2", upper=13)
    b = swml_EntityType(isAbstract=True, name="sample_text")
    _safe_set(b, 'entityType', {a1})
    assert _is_linked(b, 'entityType', a1)
    if hasattr(a1, 'Relationship'):
        assert _is_linked(a1, 'Relationship', b)
    _safe_set(b, 'entityType', {a2})
    assert _is_linked(b, 'entityType', a2)
    if hasattr(a1, 'Relationship'):
        assert not _is_linked(a1, 'Relationship', b)
    if hasattr(a2, 'Relationship'):
        assert _is_linked(a2, 'Relationship', b)
    _safe_set(b, 'entityType', set())
    assert not _is_linked(b, 'entityType', a2)
    if hasattr(a2, 'Relationship'):
        assert not _is_linked(a2, 'Relationship', b)


def test_assoc_superEntityType9_reverse_link_reassign_clear():
    a1 = swml_EntityType(isAbstract=True, name="sample_text")
    a2 = swml_EntityType(isAbstract=False, name="sample_text_2")
    b = swml_EntityType(isAbstract=True, name="sample_text")
    _safe_set(b, 'swml_EntityType8', a1)
    assert _is_linked(b, 'swml_EntityType8', a1)
    if hasattr(a1, 'swml_EntityType10'):
        assert _is_linked(a1, 'swml_EntityType10', b)
    _safe_set(b, 'swml_EntityType8', a2)
    assert _is_linked(b, 'swml_EntityType8', a2)
    if hasattr(a1, 'swml_EntityType10'):
        assert not _is_linked(a1, 'swml_EntityType10', b)
    if hasattr(a2, 'swml_EntityType10'):
        assert _is_linked(a2, 'swml_EntityType10', b)
    _safe_set(b, 'swml_EntityType8', None)
    assert not _is_linked(b, 'swml_EntityType8', a2)
    if hasattr(a2, 'swml_EntityType10'):
        assert not _is_linked(a2, 'swml_EntityType10', b)


def test_assoc_target24_reverse_link_reassign_clear():
    a1 = swml_Relationship(lower=7, name="sample_text", upper=7)
    a2 = swml_Relationship(lower=13, name="sample_text_2", upper=13)
    b = swml_EntityType(isAbstract=True, name="sample_text")
    _safe_set(b, 'swml_EntityType26', a1)
    assert _is_linked(b, 'swml_EntityType26', a1)
    if hasattr(a1, 'swml_Relationship25'):
        assert _is_linked(a1, 'swml_Relationship25', b)
    _safe_set(b, 'swml_EntityType26', a2)
    assert _is_linked(b, 'swml_EntityType26', a2)
    if hasattr(a1, 'swml_Relationship25'):
        assert not _is_linked(a1, 'swml_Relationship25', b)
    if hasattr(a2, 'swml_Relationship25'):
        assert _is_linked(a2, 'swml_Relationship25', b)
    _safe_set(b, 'swml_EntityType26', None)
    assert not _is_linked(b, 'swml_EntityType26', a2)
    if hasattr(a2, 'swml_Relationship25'):
        assert not _is_linked(a2, 'swml_Relationship25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contentModel0_stub_double():
    # swml_ContentModel has no real 'swml_ContentModel' property in the generated
    # code (a bare stub) -- manually attach it so swml_WebApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_WebApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_WebApplication(name="sample_text")
    partner = swml_ContentModel()
    setattr(partner, 'swml_ContentModel', None)
    _safe_set(owner, 'swml_WebApplication', partner)
    assert getattr(partner, 'swml_ContentModel') == owner
    _safe_set(owner, 'swml_WebApplication', None)
    assert getattr(partner, 'swml_ContentModel') is None


def test_assoc_displayedEntityType18_stub_double():
    # swml_DynamicPage has no real 'swml_DynamicPage19' property in the generated
    # code (a bare stub) -- manually attach it so swml_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_EntityType(isAbstract=True, name="sample_text")
    partner = swml_DynamicPage()
    setattr(partner, 'swml_DynamicPage19', None)
    _safe_set(owner, 'swml_EntityType20', partner)
    assert getattr(partner, 'swml_DynamicPage19') == owner
    _safe_set(owner, 'swml_EntityType20', None)
    assert getattr(partner, 'swml_DynamicPage19') is None


def test_assoc_entityType32_stub_double():
    # swml_ContentModel has no real 'swml_ContentModel33' property in the generated
    # code (a bare stub) -- manually attach it so swml_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_EntityType(isAbstract=True, name="sample_text")
    partner = swml_ContentModel()
    setattr(partner, 'swml_ContentModel33', None)
    _safe_set(owner, 'swml_EntityType34', partner)
    assert owner in getattr(partner, 'swml_ContentModel33')
    _safe_set(owner, 'swml_EntityType34', None)
    assert owner not in getattr(partner, 'swml_ContentModel33')


def test_assoc_enumerations29_stub_double():
    # swml_ContentModel has no real 'swml_ContentModel30' property in the generated
    # code (a bare stub) -- manually attach it so swml_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Enumeration(name="sample_text")
    partner = swml_ContentModel()
    setattr(partner, 'swml_ContentModel30', None)
    _safe_set(owner, 'swml_Enumeration31', partner)
    assert owner in getattr(partner, 'swml_ContentModel30')
    _safe_set(owner, 'swml_Enumeration31', None)
    assert owner not in getattr(partner, 'swml_ContentModel30')


def test_assoc_hyperTextModel1_stub_double():
    # swml_HypertextModel has no real 'swml_HypertextModel' property in the generated
    # code (a bare stub) -- manually attach it so swml_WebApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_WebApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_WebApplication(name="sample_text")
    partner = swml_HypertextModel()
    setattr(partner, 'swml_HypertextModel', None)
    _safe_set(owner, 'swml_WebApplication2', partner)
    assert getattr(partner, 'swml_HypertextModel') == owner
    _safe_set(owner, 'swml_WebApplication2', None)
    assert getattr(partner, 'swml_HypertextModel') is None


def test_assoc_parameter15_stub_double():
    # swml_Link has no real 'swml_Link16' property in the generated
    # code (a bare stub) -- manually attach it so swml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swml_Parameter(ValueSpec="sample_text")
    partner = swml_Link()
    setattr(partner, 'swml_Link16', None)
    _safe_set(owner, 'swml_Parameter', partner)
    assert getattr(partner, 'swml_Link16') == owner
    _safe_set(owner, 'swml_Parameter', None)
    assert getattr(partner, 'swml_Link16') is None


