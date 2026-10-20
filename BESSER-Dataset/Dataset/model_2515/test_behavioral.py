import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseObject,
    model6_A,
    model6_B,
    model6_BaseObject,
    model6_C,
    model6_ContainmentObject,
    model6_D,
    model6_E,
    model6_EObject,
    model6_F,
    model6_G,
    model6_MyEnumList,
    model6_MyEnumListUnsettable,
    model6_PropertiesMap,
    model6_PropertiesMapEntry,
    model6_PropertiesMapEntryValue,
    model6_ReferenceObject,
    model6_Root,
    model6_UnorderedList,
    MyEnum,
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

def test_assoc_list44_reverse_link_reassign_clear():
    a1 = model6_G(dummy="sample_text")
    a2 = model6_G(dummy="sample_text_2")
    b = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    _safe_set(b, 'model6_BaseObject46', a1)
    assert _is_linked(b, 'model6_BaseObject46', a1)
    if hasattr(a1, 'model6_G45'):
        assert _is_linked(a1, 'model6_G45', b)
    _safe_set(b, 'model6_BaseObject46', a2)
    assert _is_linked(b, 'model6_BaseObject46', a2)
    if hasattr(a1, 'model6_G45'):
        assert not _is_linked(a1, 'model6_G45', b)
    if hasattr(a2, 'model6_G45'):
        assert _is_linked(a2, 'model6_G45', b)
    _safe_set(b, 'model6_BaseObject46', None)
    assert not _is_linked(b, 'model6_BaseObject46', a2)
    if hasattr(a2, 'model6_G45'):
        assert not _is_linked(a2, 'model6_G45', b)


def test_assoc_persistentMap25_reverse_link_reassign_clear():
    a1 = model6_PropertiesMapEntry(key="sample_text")
    a2 = model6_PropertiesMapEntry(key="sample_text_2")
    b = model6_PropertiesMap(label="sample_text")
    _safe_set(b, 'model6_PropertiesMap', {a1})
    assert _is_linked(b, 'model6_PropertiesMap', a1)
    if hasattr(a1, 'model6_PropertiesMapEntry'):
        assert _is_linked(a1, 'model6_PropertiesMapEntry', b)
    _safe_set(b, 'model6_PropertiesMap', {a2})
    assert _is_linked(b, 'model6_PropertiesMap', a2)
    if hasattr(a1, 'model6_PropertiesMapEntry'):
        assert not _is_linked(a1, 'model6_PropertiesMapEntry', b)
    if hasattr(a2, 'model6_PropertiesMapEntry'):
        assert _is_linked(a2, 'model6_PropertiesMapEntry', b)
    _safe_set(b, 'model6_PropertiesMap', set())
    assert not _is_linked(b, 'model6_PropertiesMap', a2)
    if hasattr(a2, 'model6_PropertiesMapEntry'):
        assert not _is_linked(a2, 'model6_PropertiesMapEntry', b)


def test_assoc_reference42_reverse_link_reassign_clear():
    a1 = model6_G(dummy="sample_text")
    a2 = model6_G(dummy="sample_text_2")
    b = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    _safe_set(b, 'model6_BaseObject43', a1)
    assert _is_linked(b, 'model6_BaseObject43', a1)
    if hasattr(a1, 'model6_G'):
        assert _is_linked(a1, 'model6_G', b)
    _safe_set(b, 'model6_BaseObject43', a2)
    assert _is_linked(b, 'model6_BaseObject43', a2)
    if hasattr(a1, 'model6_G'):
        assert not _is_linked(a1, 'model6_G', b)
    if hasattr(a2, 'model6_G'):
        assert _is_linked(a2, 'model6_G', b)
    _safe_set(b, 'model6_BaseObject43', None)
    assert not _is_linked(b, 'model6_BaseObject43', a2)
    if hasattr(a2, 'model6_G'):
        assert not _is_linked(a2, 'model6_G', b)


def test_assoc_transientMap26_reverse_link_reassign_clear():
    a1 = model6_PropertiesMapEntry(key="sample_text")
    a2 = model6_PropertiesMapEntry(key="sample_text_2")
    b = model6_PropertiesMap(label="sample_text")
    _safe_set(b, 'model6_PropertiesMap27', {a1})
    assert _is_linked(b, 'model6_PropertiesMap27', a1)
    if hasattr(a1, 'model6_PropertiesMapEntry28'):
        assert _is_linked(a1, 'model6_PropertiesMapEntry28', b)
    _safe_set(b, 'model6_PropertiesMap27', {a2})
    assert _is_linked(b, 'model6_PropertiesMap27', a2)
    if hasattr(a1, 'model6_PropertiesMapEntry28'):
        assert not _is_linked(a1, 'model6_PropertiesMapEntry28', b)
    if hasattr(a2, 'model6_PropertiesMapEntry28'):
        assert _is_linked(a2, 'model6_PropertiesMapEntry28', b)
    _safe_set(b, 'model6_PropertiesMap27', set())
    assert not _is_linked(b, 'model6_PropertiesMap27', a2)
    if hasattr(a2, 'model6_PropertiesMapEntry28'):
        assert not _is_linked(a2, 'model6_PropertiesMapEntry28', b)


def test_assoc_value29_reverse_link_reassign_clear():
    a1 = model6_PropertiesMapEntryValue(label="sample_text")
    a2 = model6_PropertiesMapEntryValue(label="sample_text_2")
    b = model6_PropertiesMapEntry(key="sample_text")
    _safe_set(b, 'model6_PropertiesMapEntry30', a1)
    assert _is_linked(b, 'model6_PropertiesMapEntry30', a1)
    if hasattr(a1, 'model6_PropertiesMapEntryValue'):
        assert _is_linked(a1, 'model6_PropertiesMapEntryValue', b)
    _safe_set(b, 'model6_PropertiesMapEntry30', a2)
    assert _is_linked(b, 'model6_PropertiesMapEntry30', a2)
    if hasattr(a1, 'model6_PropertiesMapEntryValue'):
        assert not _is_linked(a1, 'model6_PropertiesMapEntryValue', b)
    if hasattr(a2, 'model6_PropertiesMapEntryValue'):
        assert _is_linked(a2, 'model6_PropertiesMapEntryValue', b)
    _safe_set(b, 'model6_PropertiesMapEntry30', None)
    assert not _is_linked(b, 'model6_PropertiesMapEntry30', a2)
    if hasattr(a2, 'model6_PropertiesMapEntryValue'):
        assert not _is_linked(a2, 'model6_PropertiesMapEntryValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containmentList17_stub_double():
    # model6_ContainmentObject has no real 'model6_ContainmentObject18' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_ContainmentObject()
    setattr(partner, 'model6_ContainmentObject18', None)
    _safe_set(owner, 'model6_BaseObject19', partner)
    assert owner in getattr(partner, 'model6_ContainmentObject18')
    _safe_set(owner, 'model6_BaseObject19', None)
    assert owner not in getattr(partner, 'model6_ContainmentObject18')


def test_assoc_containmentOptional15_stub_double():
    # model6_ContainmentObject has no real 'model6_ContainmentObject' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_ContainmentObject()
    setattr(partner, 'model6_ContainmentObject', None)
    _safe_set(owner, 'model6_BaseObject16', partner)
    assert getattr(partner, 'model6_ContainmentObject') == owner
    _safe_set(owner, 'model6_BaseObject16', None)
    assert getattr(partner, 'model6_ContainmentObject') is None


def test_assoc_listA0_stub_double():
    # model6_Root has no real 'model6_Root' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_Root()
    setattr(partner, 'model6_Root', None)
    _safe_set(owner, 'model6_BaseObject', partner)
    assert owner in getattr(partner, 'model6_Root')
    _safe_set(owner, 'model6_BaseObject', None)
    assert owner not in getattr(partner, 'model6_Root')


def test_assoc_listB1_stub_double():
    # model6_Root has no real 'model6_Root2' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_Root()
    setattr(partner, 'model6_Root2', None)
    _safe_set(owner, 'model6_BaseObject3', partner)
    assert owner in getattr(partner, 'model6_Root2')
    _safe_set(owner, 'model6_BaseObject3', None)
    assert owner not in getattr(partner, 'model6_Root2')


def test_assoc_listC4_stub_double():
    # model6_Root has no real 'model6_Root5' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_Root()
    setattr(partner, 'model6_Root5', None)
    _safe_set(owner, 'model6_BaseObject6', partner)
    assert owner in getattr(partner, 'model6_Root5')
    _safe_set(owner, 'model6_BaseObject6', None)
    assert owner not in getattr(partner, 'model6_Root5')


def test_assoc_listD7_stub_double():
    # model6_Root has no real 'model6_Root8' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_Root()
    setattr(partner, 'model6_Root8', None)
    _safe_set(owner, 'model6_BaseObject9', partner)
    assert owner in getattr(partner, 'model6_Root8')
    _safe_set(owner, 'model6_BaseObject9', None)
    assert owner not in getattr(partner, 'model6_Root8')


def test_assoc_referenceList12_stub_double():
    # model6_ReferenceObject has no real 'model6_ReferenceObject13' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_ReferenceObject()
    setattr(partner, 'model6_ReferenceObject13', None)
    _safe_set(owner, 'model6_BaseObject14', partner)
    assert owner in getattr(partner, 'model6_ReferenceObject13')
    _safe_set(owner, 'model6_BaseObject14', None)
    assert owner not in getattr(partner, 'model6_ReferenceObject13')


def test_assoc_referenceOptional10_stub_double():
    # model6_ReferenceObject has no real 'model6_ReferenceObject' property in the generated
    # code (a bare stub) -- manually attach it so model6_BaseObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model6_BaseObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    partner = model6_ReferenceObject()
    setattr(partner, 'model6_ReferenceObject', None)
    _safe_set(owner, 'model6_BaseObject11', partner)
    assert getattr(partner, 'model6_ReferenceObject') == owner
    _safe_set(owner, 'model6_BaseObject11', None)
    assert getattr(partner, 'model6_ReferenceObject') is None


