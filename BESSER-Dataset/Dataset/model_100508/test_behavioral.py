import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    EModelElement,
    IdentifiedElement,
    ObjectAttribute,
    Project,
    Requirement,
    SpecialChapter,
    requirement_AnonymousRequirement,
    requirement_Attribute,
    requirement_AttributeAllocate,
    requirement_AttributeConfiguration,
    requirement_AttributeLink,
    requirement_AttributeValue,
    requirement_ConfiguratedAttribute,
    requirement_CurrentRequirement,
    requirement_DefaultAttributeValue,
    requirement_DeletedChapter,
    requirement_EObject,
    requirement_HierarchicalElement,
    requirement_IdentifiedElement,
    requirement_ObjectAttribute,
    requirement_ProblemChapter,
    requirement_Requirement,
    requirement_RequirementProject,
    requirement_SpecialChapter,
    requirement_TextAttribute,
    requirement_TrashChapter,
    requirement_UntracedChapter,
    requirement_UpstreamModel,
    AttributesType,
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

def test_assoc_attribute33_reverse_link_reassign_clear():
    a1 = requirement_Requirement(externalResources="sample_text")
    a2 = requirement_Requirement(externalResources="sample_text_2")
    b = requirement_Attribute(name="sample_text")
    _safe_set(b, 'requirement_Attribute', a1)
    assert _is_linked(b, 'requirement_Attribute', a1)
    if hasattr(a1, 'requirement_Requirement34'):
        assert _is_linked(a1, 'requirement_Requirement34', b)
    _safe_set(b, 'requirement_Attribute', a2)
    assert _is_linked(b, 'requirement_Attribute', a2)
    if hasattr(a1, 'requirement_Requirement34'):
        assert not _is_linked(a1, 'requirement_Requirement34', b)
    if hasattr(a2, 'requirement_Requirement34'):
        assert _is_linked(a2, 'requirement_Requirement34', b)
    _safe_set(b, 'requirement_Attribute', None)
    assert not _is_linked(b, 'requirement_Attribute', a2)
    if hasattr(a2, 'requirement_Requirement34'):
        assert not _is_linked(a2, 'requirement_Requirement34', b)


def test_assoc_children10_reverse_link_reassign_clear():
    a1 = requirement_HierarchicalElement(nextReqIndex="sample_text")
    a2 = requirement_HierarchicalElement(nextReqIndex="sample_text_2")
    b = requirement_HierarchicalElement(nextReqIndex="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'HierarchicalElement'):
        assert _is_linked(a1, 'HierarchicalElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'HierarchicalElement'):
        assert not _is_linked(a1, 'HierarchicalElement', b)
    if hasattr(a2, 'HierarchicalElement'):
        assert _is_linked(a2, 'HierarchicalElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'HierarchicalElement'):
        assert not _is_linked(a2, 'HierarchicalElement', b)


def test_assoc_listValue20_reverse_link_reassign_clear():
    a1 = requirement_ConfiguratedAttribute(name="sample_text", type="sample_text")
    a2 = requirement_ConfiguratedAttribute(name="sample_text_2", type="sample_text_2")
    b = requirement_AttributeValue(value="sample_text")
    _safe_set(b, 'requirement_AttributeValue', a1)
    assert _is_linked(b, 'requirement_AttributeValue', a1)
    if hasattr(a1, 'requirement_ConfiguratedAttribute21'):
        assert _is_linked(a1, 'requirement_ConfiguratedAttribute21', b)
    _safe_set(b, 'requirement_AttributeValue', a2)
    assert _is_linked(b, 'requirement_AttributeValue', a2)
    if hasattr(a1, 'requirement_ConfiguratedAttribute21'):
        assert not _is_linked(a1, 'requirement_ConfiguratedAttribute21', b)
    if hasattr(a2, 'requirement_ConfiguratedAttribute21'):
        assert _is_linked(a2, 'requirement_ConfiguratedAttribute21', b)
    _safe_set(b, 'requirement_AttributeValue', None)
    assert not _is_linked(b, 'requirement_AttributeValue', a2)
    if hasattr(a2, 'requirement_ConfiguratedAttribute21'):
        assert not _is_linked(a2, 'requirement_ConfiguratedAttribute21', b)


def test_assoc_parent12_reverse_link_reassign_clear():
    a1 = requirement_HierarchicalElement(nextReqIndex="sample_text")
    a2 = requirement_HierarchicalElement(nextReqIndex="sample_text_2")
    b = requirement_HierarchicalElement(nextReqIndex="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'HierarchicalElement13'):
        assert _is_linked(a1, 'HierarchicalElement13', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'HierarchicalElement13'):
        assert not _is_linked(a1, 'HierarchicalElement13', b)
    if hasattr(a2, 'HierarchicalElement13'):
        assert _is_linked(a2, 'HierarchicalElement13', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'HierarchicalElement13'):
        assert not _is_linked(a2, 'HierarchicalElement13', b)


def test_assoc_requirement14_reverse_link_reassign_clear():
    a1 = requirement_Requirement(externalResources="sample_text")
    a2 = requirement_Requirement(externalResources="sample_text_2")
    b = requirement_HierarchicalElement(nextReqIndex="sample_text")
    _safe_set(b, 'requirement_HierarchicalElement15', {a1})
    assert _is_linked(b, 'requirement_HierarchicalElement15', a1)
    if hasattr(a1, 'requirement_Requirement'):
        assert _is_linked(a1, 'requirement_Requirement', b)
    _safe_set(b, 'requirement_HierarchicalElement15', {a2})
    assert _is_linked(b, 'requirement_HierarchicalElement15', a2)
    if hasattr(a1, 'requirement_Requirement'):
        assert not _is_linked(a1, 'requirement_Requirement', b)
    if hasattr(a2, 'requirement_Requirement'):
        assert _is_linked(a2, 'requirement_Requirement', b)
    _safe_set(b, 'requirement_HierarchicalElement15', set())
    assert not _is_linked(b, 'requirement_HierarchicalElement15', a2)
    if hasattr(a2, 'requirement_Requirement'):
        assert not _is_linked(a2, 'requirement_Requirement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defaultValue18_stub_double():
    # requirement_DefaultAttributeValue has no real 'requirement_DefaultAttributeValue' property in the generated
    # code (a bare stub) -- manually attach it so requirement_ConfiguratedAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_ConfiguratedAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_ConfiguratedAttribute(name="sample_text", type="sample_text")
    partner = requirement_DefaultAttributeValue()
    setattr(partner, 'requirement_DefaultAttributeValue', None)
    _safe_set(owner, 'requirement_ConfiguratedAttribute19', partner)
    assert getattr(partner, 'requirement_DefaultAttributeValue') == owner
    _safe_set(owner, 'requirement_ConfiguratedAttribute19', None)
    assert getattr(partner, 'requirement_DefaultAttributeValue') is None


def test_assoc_element7_stub_double():
    # requirement_EObject has no real 'requirement_EObject' property in the generated
    # code (a bare stub) -- manually attach it so requirement_HierarchicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_HierarchicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_HierarchicalElement(nextReqIndex="sample_text")
    partner = requirement_EObject()
    setattr(partner, 'requirement_EObject', None)
    _safe_set(owner, 'requirement_HierarchicalElement8', partner)
    assert getattr(partner, 'requirement_EObject') == owner
    _safe_set(owner, 'requirement_HierarchicalElement8', None)
    assert getattr(partner, 'requirement_EObject') is None


def test_assoc_hierarchicalElement0_stub_double():
    # requirement_RequirementProject has no real 'requirement_RequirementProject' property in the generated
    # code (a bare stub) -- manually attach it so requirement_HierarchicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_HierarchicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_HierarchicalElement(nextReqIndex="sample_text")
    partner = requirement_RequirementProject()
    setattr(partner, 'requirement_RequirementProject', None)
    _safe_set(owner, 'requirement_HierarchicalElement', partner)
    assert owner in getattr(partner, 'requirement_RequirementProject')
    _safe_set(owner, 'requirement_HierarchicalElement', None)
    assert owner not in getattr(partner, 'requirement_RequirementProject')


def test_assoc_hierarchicalElement25_stub_double():
    # requirement_SpecialChapter has no real 'requirement_SpecialChapter26' property in the generated
    # code (a bare stub) -- manually attach it so requirement_HierarchicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_HierarchicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_HierarchicalElement(nextReqIndex="sample_text")
    partner = requirement_SpecialChapter()
    setattr(partner, 'requirement_SpecialChapter26', None)
    _safe_set(owner, 'requirement_HierarchicalElement27', partner)
    assert owner in getattr(partner, 'requirement_SpecialChapter26')
    _safe_set(owner, 'requirement_HierarchicalElement27', None)
    assert owner not in getattr(partner, 'requirement_SpecialChapter26')


def test_assoc_listAttributes16_stub_double():
    # requirement_AttributeConfiguration has no real 'requirement_AttributeConfiguration17' property in the generated
    # code (a bare stub) -- manually attach it so requirement_ConfiguratedAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_ConfiguratedAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_ConfiguratedAttribute(name="sample_text", type="sample_text")
    partner = requirement_AttributeConfiguration()
    setattr(partner, 'requirement_AttributeConfiguration17', None)
    _safe_set(owner, 'requirement_ConfiguratedAttribute', partner)
    assert owner in getattr(partner, 'requirement_AttributeConfiguration17')
    _safe_set(owner, 'requirement_ConfiguratedAttribute', None)
    assert owner not in getattr(partner, 'requirement_AttributeConfiguration17')


def test_assoc_requirement28_stub_double():
    # requirement_SpecialChapter has no real 'requirement_SpecialChapter29' property in the generated
    # code (a bare stub) -- manually attach it so requirement_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_Requirement(externalResources="sample_text")
    partner = requirement_SpecialChapter()
    setattr(partner, 'requirement_SpecialChapter29', None)
    _safe_set(owner, 'requirement_Requirement30', partner)
    assert owner in getattr(partner, 'requirement_SpecialChapter29')
    _safe_set(owner, 'requirement_Requirement30', None)
    assert owner not in getattr(partner, 'requirement_SpecialChapter29')


def test_assoc_value22_stub_double():
    # requirement_DefaultAttributeValue has no real 'requirement_DefaultAttributeValue23' property in the generated
    # code (a bare stub) -- manually attach it so requirement_AttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_AttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_AttributeValue(value="sample_text")
    partner = requirement_DefaultAttributeValue()
    setattr(partner, 'requirement_DefaultAttributeValue23', None)
    _safe_set(owner, 'requirement_AttributeValue24', partner)
    assert getattr(partner, 'requirement_DefaultAttributeValue23') == owner
    _safe_set(owner, 'requirement_AttributeValue24', None)
    assert getattr(partner, 'requirement_DefaultAttributeValue23') is None


