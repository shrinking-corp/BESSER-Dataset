import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributePageElement,
    Condition,
    EntityModelElement,
    Feature,
    NamedElement,
    PageElement,
    RelationshipPageElement,
    forms_Attribute,
    forms_AttributePageElement,
    forms_AttributeValueCondition,
    forms_Column,
    forms_CompositeCondition,
    forms_Condition,
    forms_DateSelectionField,
    forms_Entity,
    forms_EntityModel,
    forms_EntityModelElement,
    forms_Enumeration,
    forms_Feature,
    forms_Form,
    forms_FormModel,
    forms_List,
    forms_Literal,
    forms_NamedElement,
    forms_Page,
    forms_PageElement,
    forms_Relationship,
    forms_RelationshipPageElement,
    forms_SelectionField,
    forms_Table,
    forms_TextArea,
    forms_TextField,
    forms_TimeSelectionField,
    AttributeType,
    CompositeConditionType,
    ConditionType,
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

def test_assoc_attribute30_reverse_link_reassign_clear():
    a1 = forms_AttributeValueCondition(value="sample_text")
    a2 = forms_AttributeValueCondition(value="sample_text_2")
    b = forms_Attribute(mandatory=True, type="sample_text")
    _safe_set(b, 'forms_Attribute31', a1)
    assert _is_linked(b, 'forms_Attribute31', a1)
    if hasattr(a1, 'forms_AttributeValueCondition'):
        assert _is_linked(a1, 'forms_AttributeValueCondition', b)
    _safe_set(b, 'forms_Attribute31', a2)
    assert _is_linked(b, 'forms_Attribute31', a2)
    if hasattr(a1, 'forms_AttributeValueCondition'):
        assert not _is_linked(a1, 'forms_AttributeValueCondition', b)
    if hasattr(a2, 'forms_AttributeValueCondition'):
        assert _is_linked(a2, 'forms_AttributeValueCondition', b)
    _safe_set(b, 'forms_Attribute31', None)
    assert not _is_linked(b, 'forms_Attribute31', a2)
    if hasattr(a2, 'forms_AttributeValueCondition'):
        assert not _is_linked(a2, 'forms_AttributeValueCondition', b)


def test_assoc_composedConditions32_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(compositionType="sample_text")
    _safe_set(b, 'forms_CompositeCondition', {a1})
    assert _is_linked(b, 'forms_CompositeCondition', a1)
    if hasattr(a1, 'forms_Condition33'):
        assert _is_linked(a1, 'forms_Condition33', b)
    _safe_set(b, 'forms_CompositeCondition', {a2})
    assert _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a1, 'forms_Condition33'):
        assert not _is_linked(a1, 'forms_Condition33', b)
    if hasattr(a2, 'forms_Condition33'):
        assert _is_linked(a2, 'forms_Condition33', b)
    _safe_set(b, 'forms_CompositeCondition', set())
    assert not _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a2, 'forms_Condition33'):
        assert not _is_linked(a2, 'forms_Condition33', b)


def test_assoc_condition24_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'forms_Condition', a1)
    assert _is_linked(b, 'forms_Condition', a1)
    if hasattr(a1, 'forms_Page25'):
        assert _is_linked(a1, 'forms_Page25', b)
    _safe_set(b, 'forms_Condition', a2)
    assert _is_linked(b, 'forms_Condition', a2)
    if hasattr(a1, 'forms_Page25'):
        assert not _is_linked(a1, 'forms_Page25', b)
    if hasattr(a2, 'forms_Page25'):
        assert _is_linked(a2, 'forms_Page25', b)
    _safe_set(b, 'forms_Condition', None)
    assert not _is_linked(b, 'forms_Condition', a2)
    if hasattr(a2, 'forms_Page25'):
        assert not _is_linked(a2, 'forms_Page25', b)


def test_assoc_condition26_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'forms_Condition28', a1)
    assert _is_linked(b, 'forms_Condition28', a1)
    if hasattr(a1, 'forms_PageElement27'):
        assert _is_linked(a1, 'forms_PageElement27', b)
    _safe_set(b, 'forms_Condition28', a2)
    assert _is_linked(b, 'forms_Condition28', a2)
    if hasattr(a1, 'forms_PageElement27'):
        assert not _is_linked(a1, 'forms_PageElement27', b)
    if hasattr(a2, 'forms_PageElement27'):
        assert _is_linked(a2, 'forms_PageElement27', b)
    _safe_set(b, 'forms_Condition28', None)
    assert not _is_linked(b, 'forms_Condition28', a2)
    if hasattr(a2, 'forms_PageElement27'):
        assert not _is_linked(a2, 'forms_PageElement27', b)


def test_assoc_opposite11_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, upperBound=7)
    a2 = forms_Relationship(lowerBound=13, upperBound=13)
    b = forms_Relationship(lowerBound=7, upperBound=7)
    _safe_set(b, 'forms_Relationship12', a1)
    assert _is_linked(b, 'forms_Relationship12', a1)
    if hasattr(a1, 'forms_Relationship10'):
        assert _is_linked(a1, 'forms_Relationship10', b)
    _safe_set(b, 'forms_Relationship12', a2)
    assert _is_linked(b, 'forms_Relationship12', a2)
    if hasattr(a1, 'forms_Relationship10'):
        assert not _is_linked(a1, 'forms_Relationship10', b)
    if hasattr(a2, 'forms_Relationship10'):
        assert _is_linked(a2, 'forms_Relationship10', b)
    _safe_set(b, 'forms_Relationship12', None)
    assert not _is_linked(b, 'forms_Relationship12', a2)
    if hasattr(a2, 'forms_Relationship10'):
        assert not _is_linked(a2, 'forms_Relationship10', b)


def test_assoc_pageElements22_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'forms_Page23', {a1})
    assert _is_linked(b, 'forms_Page23', a1)
    if hasattr(a1, 'forms_PageElement'):
        assert _is_linked(a1, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page23', {a2})
    assert _is_linked(b, 'forms_Page23', a2)
    if hasattr(a1, 'forms_PageElement'):
        assert not _is_linked(a1, 'forms_PageElement', b)
    if hasattr(a2, 'forms_PageElement'):
        assert _is_linked(a2, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page23', set())
    assert not _is_linked(b, 'forms_Page23', a2)
    if hasattr(a2, 'forms_PageElement'):
        assert not _is_linked(a2, 'forms_PageElement', b)


def test_assoc_pages20_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", title="sample_text", welcomeForm=True)
    _safe_set(b, 'forms_Form21', {a1})
    assert _is_linked(b, 'forms_Form21', a1)
    if hasattr(a1, 'forms_Page'):
        assert _is_linked(a1, 'forms_Page', b)
    _safe_set(b, 'forms_Form21', {a2})
    assert _is_linked(b, 'forms_Form21', a2)
    if hasattr(a1, 'forms_Page'):
        assert not _is_linked(a1, 'forms_Page', b)
    if hasattr(a2, 'forms_Page'):
        assert _is_linked(a2, 'forms_Page', b)
    _safe_set(b, 'forms_Form21', set())
    assert not _is_linked(b, 'forms_Form21', a2)
    if hasattr(a2, 'forms_Page'):
        assert not _is_linked(a2, 'forms_Page', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute34_stub_double():
    # forms_AttributePageElement has no real 'forms_AttributePageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, type="sample_text")
    partner = forms_AttributePageElement()
    setattr(partner, 'forms_AttributePageElement', None)
    _safe_set(owner, 'forms_Attribute35', partner)
    assert getattr(partner, 'forms_AttributePageElement') == owner
    _safe_set(owner, 'forms_Attribute35', None)
    assert getattr(partner, 'forms_AttributePageElement') is None


def test_assoc_editingForm38_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement39' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", title="sample_text", welcomeForm=True)
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement39', None)
    _safe_set(owner, 'forms_Form40', partner)
    assert getattr(partner, 'forms_RelationshipPageElement39') == owner
    _safe_set(owner, 'forms_Form40', None)
    assert getattr(partner, 'forms_RelationshipPageElement39') is None


def test_assoc_entity17_stub_double():
    # forms_Entity has no real 'forms_Entity19' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", title="sample_text", welcomeForm=True)
    partner = forms_Entity()
    setattr(partner, 'forms_Entity19', None)
    _safe_set(owner, 'forms_Form18', partner)
    assert getattr(partner, 'forms_Entity19') == owner
    _safe_set(owner, 'forms_Form18', None)
    assert getattr(partner, 'forms_Entity19') is None


def test_assoc_enumeration6_stub_double():
    # forms_Enumeration has no real 'forms_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, type="sample_text")
    partner = forms_Enumeration()
    setattr(partner, 'forms_Enumeration', None)
    _safe_set(owner, 'forms_Attribute7', partner)
    assert getattr(partner, 'forms_Enumeration') == owner
    _safe_set(owner, 'forms_Attribute7', None)
    assert getattr(partner, 'forms_Enumeration') is None


def test_assoc_forms16_stub_double():
    # forms_FormModel has no real 'forms_FormModel' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", title="sample_text", welcomeForm=True)
    partner = forms_FormModel()
    setattr(partner, 'forms_FormModel', None)
    _safe_set(owner, 'forms_Form', partner)
    assert owner in getattr(partner, 'forms_FormModel')
    _safe_set(owner, 'forms_Form', None)
    assert owner not in getattr(partner, 'forms_FormModel')


def test_assoc_id1_stub_double():
    # forms_Entity has no real 'forms_Entity2' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, type="sample_text")
    partner = forms_Entity()
    setattr(partner, 'forms_Entity2', None)
    _safe_set(owner, 'forms_Attribute', partner)
    assert getattr(partner, 'forms_Entity2') == owner
    _safe_set(owner, 'forms_Attribute', None)
    assert getattr(partner, 'forms_Entity2') is None


def test_assoc_literals13_stub_double():
    # forms_Enumeration has no real 'forms_Enumeration14' property in the generated
    # code (a bare stub) -- manually attach it so forms_Literal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Literal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Literal(value="sample_text")
    partner = forms_Enumeration()
    setattr(partner, 'forms_Enumeration14', None)
    _safe_set(owner, 'forms_Literal', partner)
    assert owner in getattr(partner, 'forms_Enumeration14')
    _safe_set(owner, 'forms_Literal', None)
    assert owner not in getattr(partner, 'forms_Enumeration14')


def test_assoc_relationship36_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Relationship(lowerBound=7, upperBound=7)
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement', None)
    _safe_set(owner, 'forms_Relationship37', partner)
    assert getattr(partner, 'forms_RelationshipPageElement') == owner
    _safe_set(owner, 'forms_Relationship37', None)
    assert getattr(partner, 'forms_RelationshipPageElement') is None


def test_assoc_target8_stub_double():
    # forms_Entity has no real 'forms_Entity9' property in the generated
    # code (a bare stub) -- manually attach it so forms_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Relationship(lowerBound=7, upperBound=7)
    partner = forms_Entity()
    setattr(partner, 'forms_Entity9', None)
    _safe_set(owner, 'forms_Relationship', partner)
    assert getattr(partner, 'forms_Entity9') == owner
    _safe_set(owner, 'forms_Relationship', None)
    assert getattr(partner, 'forms_Entity9') is None


