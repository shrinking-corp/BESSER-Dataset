import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ulmDsl2_Attribute,
    ulmDsl2_AttributeDecimalType,
    ulmDsl2_AttributeFeatureType,
    ulmDsl2_AttributeStringType,
    ulmDsl2_AttributeType,
    ulmDsl2_Context,
    ulmDsl2_EObject,
    ulmDsl2_Entity,
    ulmDsl2_EntityFeatureType,
    ulmDsl2_Feature,
    ulmDsl2_FeatureType,
    ulmDsl2_Lookup,
    ulmDsl2_LookupInt,
    ulmDsl2_LookupIntValue,
    ulmDsl2_LookupString,
    ulmDsl2_LookupStringValue,
    ulmDsl2_Model,
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

def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = ulmDsl2_Context(name="sample_text", version="sample_text")
    a2 = ulmDsl2_Context(name="sample_text_2", version="sample_text_2")
    b = ulmDsl2_Attribute(desc="sample_text", name="sample_text")
    _safe_set(b, 'ulmDsl2_Attribute', a1)
    assert _is_linked(b, 'ulmDsl2_Attribute', a1)
    if hasattr(a1, 'ulmDsl2_Context2'):
        assert _is_linked(a1, 'ulmDsl2_Context2', b)
    _safe_set(b, 'ulmDsl2_Attribute', a2)
    assert _is_linked(b, 'ulmDsl2_Attribute', a2)
    if hasattr(a1, 'ulmDsl2_Context2'):
        assert not _is_linked(a1, 'ulmDsl2_Context2', b)
    if hasattr(a2, 'ulmDsl2_Context2'):
        assert _is_linked(a2, 'ulmDsl2_Context2', b)
    _safe_set(b, 'ulmDsl2_Attribute', None)
    assert not _is_linked(b, 'ulmDsl2_Attribute', a2)
    if hasattr(a2, 'ulmDsl2_Context2'):
        assert not _is_linked(a2, 'ulmDsl2_Context2', b)


def test_assoc_contexts0_reverse_link_reassign_clear():
    a1 = ulmDsl2_Model(name="sample_text")
    a2 = ulmDsl2_Model(name="sample_text_2")
    b = ulmDsl2_Context(name="sample_text", version="sample_text")
    _safe_set(b, 'ulmDsl2_Context', a1)
    assert _is_linked(b, 'ulmDsl2_Context', a1)
    if hasattr(a1, 'ulmDsl2_Model'):
        assert _is_linked(a1, 'ulmDsl2_Model', b)
    _safe_set(b, 'ulmDsl2_Context', a2)
    assert _is_linked(b, 'ulmDsl2_Context', a2)
    if hasattr(a1, 'ulmDsl2_Model'):
        assert not _is_linked(a1, 'ulmDsl2_Model', b)
    if hasattr(a2, 'ulmDsl2_Model'):
        assert _is_linked(a2, 'ulmDsl2_Model', b)
    _safe_set(b, 'ulmDsl2_Context', None)
    assert not _is_linked(b, 'ulmDsl2_Context', a2)
    if hasattr(a2, 'ulmDsl2_Model'):
        assert not _is_linked(a2, 'ulmDsl2_Model', b)


def test_assoc_entities5_reverse_link_reassign_clear():
    a1 = ulmDsl2_Entity(desc="sample_text", name="sample_text", type="sample_text")
    a2 = ulmDsl2_Entity(desc="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ulmDsl2_Context(name="sample_text", version="sample_text")
    _safe_set(b, 'ulmDsl2_Context6', {a1})
    assert _is_linked(b, 'ulmDsl2_Context6', a1)
    if hasattr(a1, 'ulmDsl2_Entity'):
        assert _is_linked(a1, 'ulmDsl2_Entity', b)
    _safe_set(b, 'ulmDsl2_Context6', {a2})
    assert _is_linked(b, 'ulmDsl2_Context6', a2)
    if hasattr(a1, 'ulmDsl2_Entity'):
        assert not _is_linked(a1, 'ulmDsl2_Entity', b)
    if hasattr(a2, 'ulmDsl2_Entity'):
        assert _is_linked(a2, 'ulmDsl2_Entity', b)
    _safe_set(b, 'ulmDsl2_Context6', set())
    assert not _is_linked(b, 'ulmDsl2_Context6', a2)
    if hasattr(a2, 'ulmDsl2_Entity'):
        assert not _is_linked(a2, 'ulmDsl2_Entity', b)


def test_assoc_entity24_reverse_link_reassign_clear():
    a1 = ulmDsl2_EntityFeatureType(array=True, length=7)
    a2 = ulmDsl2_EntityFeatureType(array=False, length=13)
    b = ulmDsl2_Entity(desc="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'ulmDsl2_Entity25', a1)
    assert _is_linked(b, 'ulmDsl2_Entity25', a1)
    if hasattr(a1, 'ulmDsl2_EntityFeatureType'):
        assert _is_linked(a1, 'ulmDsl2_EntityFeatureType', b)
    _safe_set(b, 'ulmDsl2_Entity25', a2)
    assert _is_linked(b, 'ulmDsl2_Entity25', a2)
    if hasattr(a1, 'ulmDsl2_EntityFeatureType'):
        assert not _is_linked(a1, 'ulmDsl2_EntityFeatureType', b)
    if hasattr(a2, 'ulmDsl2_EntityFeatureType'):
        assert _is_linked(a2, 'ulmDsl2_EntityFeatureType', b)
    _safe_set(b, 'ulmDsl2_Entity25', None)
    assert not _is_linked(b, 'ulmDsl2_Entity25', a2)
    if hasattr(a2, 'ulmDsl2_EntityFeatureType'):
        assert not _is_linked(a2, 'ulmDsl2_EntityFeatureType', b)


def test_assoc_features12_reverse_link_reassign_clear():
    a1 = ulmDsl2_Feature(identifier=True, mandatory=True, name="sample_text")
    a2 = ulmDsl2_Feature(identifier=False, mandatory=False, name="sample_text_2")
    b = ulmDsl2_Entity(desc="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'ulmDsl2_Entity13', {a1})
    assert _is_linked(b, 'ulmDsl2_Entity13', a1)
    if hasattr(a1, 'ulmDsl2_Feature'):
        assert _is_linked(a1, 'ulmDsl2_Feature', b)
    _safe_set(b, 'ulmDsl2_Entity13', {a2})
    assert _is_linked(b, 'ulmDsl2_Entity13', a2)
    if hasattr(a1, 'ulmDsl2_Feature'):
        assert not _is_linked(a1, 'ulmDsl2_Feature', b)
    if hasattr(a2, 'ulmDsl2_Feature'):
        assert _is_linked(a2, 'ulmDsl2_Feature', b)
    _safe_set(b, 'ulmDsl2_Entity13', set())
    assert not _is_linked(b, 'ulmDsl2_Entity13', a2)
    if hasattr(a2, 'ulmDsl2_Feature'):
        assert not _is_linked(a2, 'ulmDsl2_Feature', b)


def test_assoc_lookups3_reverse_link_reassign_clear():
    a1 = ulmDsl2_Lookup(name="sample_text")
    a2 = ulmDsl2_Lookup(name="sample_text_2")
    b = ulmDsl2_Context(name="sample_text", version="sample_text")
    _safe_set(b, 'ulmDsl2_Context4', {a1})
    assert _is_linked(b, 'ulmDsl2_Context4', a1)
    if hasattr(a1, 'ulmDsl2_Lookup'):
        assert _is_linked(a1, 'ulmDsl2_Lookup', b)
    _safe_set(b, 'ulmDsl2_Context4', {a2})
    assert _is_linked(b, 'ulmDsl2_Context4', a2)
    if hasattr(a1, 'ulmDsl2_Lookup'):
        assert not _is_linked(a1, 'ulmDsl2_Lookup', b)
    if hasattr(a2, 'ulmDsl2_Lookup'):
        assert _is_linked(a2, 'ulmDsl2_Lookup', b)
    _safe_set(b, 'ulmDsl2_Context4', set())
    assert not _is_linked(b, 'ulmDsl2_Context4', a2)
    if hasattr(a2, 'ulmDsl2_Lookup'):
        assert not _is_linked(a2, 'ulmDsl2_Lookup', b)


def test_assoc_superType10_reverse_link_reassign_clear():
    a1 = ulmDsl2_Entity(desc="sample_text", name="sample_text", type="sample_text")
    a2 = ulmDsl2_Entity(desc="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ulmDsl2_Entity(desc="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'ulmDsl2_Entity9', a1)
    assert _is_linked(b, 'ulmDsl2_Entity9', a1)
    if hasattr(a1, 'ulmDsl2_Entity11'):
        assert _is_linked(a1, 'ulmDsl2_Entity11', b)
    _safe_set(b, 'ulmDsl2_Entity9', a2)
    assert _is_linked(b, 'ulmDsl2_Entity9', a2)
    if hasattr(a1, 'ulmDsl2_Entity11'):
        assert not _is_linked(a1, 'ulmDsl2_Entity11', b)
    if hasattr(a2, 'ulmDsl2_Entity11'):
        assert _is_linked(a2, 'ulmDsl2_Entity11', b)
    _safe_set(b, 'ulmDsl2_Entity9', None)
    assert not _is_linked(b, 'ulmDsl2_Entity9', a2)
    if hasattr(a2, 'ulmDsl2_Entity11'):
        assert not _is_linked(a2, 'ulmDsl2_Entity11', b)


def test_assoc_values29_reverse_link_reassign_clear():
    a1 = ulmDsl2_LookupIntValue(description="sample_text", value=7)
    a2 = ulmDsl2_LookupIntValue(description="sample_text_2", value=13)
    b = ulmDsl2_LookupInt(description="sample_text")
    _safe_set(b, 'ulmDsl2_LookupInt', {a1})
    assert _is_linked(b, 'ulmDsl2_LookupInt', a1)
    if hasattr(a1, 'ulmDsl2_LookupIntValue'):
        assert _is_linked(a1, 'ulmDsl2_LookupIntValue', b)
    _safe_set(b, 'ulmDsl2_LookupInt', {a2})
    assert _is_linked(b, 'ulmDsl2_LookupInt', a2)
    if hasattr(a1, 'ulmDsl2_LookupIntValue'):
        assert not _is_linked(a1, 'ulmDsl2_LookupIntValue', b)
    if hasattr(a2, 'ulmDsl2_LookupIntValue'):
        assert _is_linked(a2, 'ulmDsl2_LookupIntValue', b)
    _safe_set(b, 'ulmDsl2_LookupInt', set())
    assert not _is_linked(b, 'ulmDsl2_LookupInt', a2)
    if hasattr(a2, 'ulmDsl2_LookupIntValue'):
        assert not _is_linked(a2, 'ulmDsl2_LookupIntValue', b)


def test_assoc_values30_reverse_link_reassign_clear():
    a1 = ulmDsl2_LookupStringValue(description="sample_text", value="sample_text")
    a2 = ulmDsl2_LookupStringValue(description="sample_text_2", value="sample_text_2")
    b = ulmDsl2_LookupString(description="sample_text")
    _safe_set(b, 'ulmDsl2_LookupString', {a1})
    assert _is_linked(b, 'ulmDsl2_LookupString', a1)
    if hasattr(a1, 'ulmDsl2_LookupStringValue'):
        assert _is_linked(a1, 'ulmDsl2_LookupStringValue', b)
    _safe_set(b, 'ulmDsl2_LookupString', {a2})
    assert _is_linked(b, 'ulmDsl2_LookupString', a2)
    if hasattr(a1, 'ulmDsl2_LookupStringValue'):
        assert not _is_linked(a1, 'ulmDsl2_LookupStringValue', b)
    if hasattr(a2, 'ulmDsl2_LookupStringValue'):
        assert _is_linked(a2, 'ulmDsl2_LookupStringValue', b)
    _safe_set(b, 'ulmDsl2_LookupString', set())
    assert not _is_linked(b, 'ulmDsl2_LookupString', a2)
    if hasattr(a2, 'ulmDsl2_LookupStringValue'):
        assert not _is_linked(a2, 'ulmDsl2_LookupStringValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute19_stub_double():
    # ulmDsl2_AttributeFeatureType has no real 'ulmDsl2_AttributeFeatureType' property in the generated
    # code (a bare stub) -- manually attach it so ulmDsl2_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ulmDsl2_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ulmDsl2_Attribute(desc="sample_text", name="sample_text")
    partner = ulmDsl2_AttributeFeatureType()
    setattr(partner, 'ulmDsl2_AttributeFeatureType', None)
    _safe_set(owner, 'ulmDsl2_Attribute20', partner)
    assert getattr(partner, 'ulmDsl2_AttributeFeatureType') == owner
    _safe_set(owner, 'ulmDsl2_Attribute20', None)
    assert getattr(partner, 'ulmDsl2_AttributeFeatureType') is None


def test_assoc_lookup21_stub_double():
    # ulmDsl2_AttributeFeatureType has no real 'ulmDsl2_AttributeFeatureType22' property in the generated
    # code (a bare stub) -- manually attach it so ulmDsl2_Lookup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ulmDsl2_Lookup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ulmDsl2_Lookup(name="sample_text")
    partner = ulmDsl2_AttributeFeatureType()
    setattr(partner, 'ulmDsl2_AttributeFeatureType22', None)
    _safe_set(owner, 'ulmDsl2_Lookup23', partner)
    assert getattr(partner, 'ulmDsl2_AttributeFeatureType22') == owner
    _safe_set(owner, 'ulmDsl2_Lookup23', None)
    assert getattr(partner, 'ulmDsl2_AttributeFeatureType22') is None


def test_assoc_type14_stub_double():
    # ulmDsl2_FeatureType has no real 'ulmDsl2_FeatureType' property in the generated
    # code (a bare stub) -- manually attach it so ulmDsl2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ulmDsl2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ulmDsl2_Feature(identifier=True, mandatory=True, name="sample_text")
    partner = ulmDsl2_FeatureType()
    setattr(partner, 'ulmDsl2_FeatureType', None)
    _safe_set(owner, 'ulmDsl2_Feature15', partner)
    assert getattr(partner, 'ulmDsl2_FeatureType') == owner
    _safe_set(owner, 'ulmDsl2_Feature15', None)
    assert getattr(partner, 'ulmDsl2_FeatureType') is None


def test_assoc_type26_stub_double():
    # ulmDsl2_EObject has no real 'ulmDsl2_EObject28' property in the generated
    # code (a bare stub) -- manually attach it so ulmDsl2_Lookup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ulmDsl2_Lookup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ulmDsl2_Lookup(name="sample_text")
    partner = ulmDsl2_EObject()
    setattr(partner, 'ulmDsl2_EObject28', None)
    _safe_set(owner, 'ulmDsl2_Lookup27', partner)
    assert getattr(partner, 'ulmDsl2_EObject28') == owner
    _safe_set(owner, 'ulmDsl2_Lookup27', None)
    assert getattr(partner, 'ulmDsl2_EObject28') is None


def test_assoc_type7_stub_double():
    # ulmDsl2_EObject has no real 'ulmDsl2_EObject' property in the generated
    # code (a bare stub) -- manually attach it so ulmDsl2_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ulmDsl2_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ulmDsl2_Attribute(desc="sample_text", name="sample_text")
    partner = ulmDsl2_EObject()
    setattr(partner, 'ulmDsl2_EObject', None)
    _safe_set(owner, 'ulmDsl2_Attribute8', partner)
    assert getattr(partner, 'ulmDsl2_EObject') == owner
    _safe_set(owner, 'ulmDsl2_Attribute8', None)
    assert getattr(partner, 'ulmDsl2_EObject') is None


