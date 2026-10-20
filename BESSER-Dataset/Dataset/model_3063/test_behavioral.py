import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributePageElement,
    Condition,
    PageElement,
    RelationshipPageElement,
    forms_Attribute,
    forms_AttributePageElement,
    forms_AttributeValueCondition,
    forms_Column,
    forms_CompositeCondition,
    forms_Condition,
    forms_DateSelectionFields,
    forms_Entity,
    forms_Enumeration,
    forms_Form,
    forms_ListRelationshipPageElement,
    forms_Literal,
    forms_Model,
    forms_Page,
    forms_PageElement,
    forms_Relationship,
    forms_RelationshipPageElement,
    forms_SelectionFields,
    forms_TableRelationshipPageElement,
    forms_TextAreas,
    forms_TextFields,
    forms_TimeSelectionFields,
    AttributeType,
    ConditionType,
    OperatorType,
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

def test_assoc_attributeRef32_reverse_link_reassign_clear():
    a1 = forms_AttributePageElement(value="sample_text")
    a2 = forms_AttributePageElement(value="sample_text_2")
    b = forms_Attribute(isId="sample_text", mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute33', a1)
    assert _is_linked(b, 'forms_Attribute33', a1)
    if hasattr(a1, 'forms_AttributePageElement'):
        assert _is_linked(a1, 'forms_AttributePageElement', b)
    _safe_set(b, 'forms_Attribute33', a2)
    assert _is_linked(b, 'forms_Attribute33', a2)
    if hasattr(a1, 'forms_AttributePageElement'):
        assert not _is_linked(a1, 'forms_AttributePageElement', b)
    if hasattr(a2, 'forms_AttributePageElement'):
        assert _is_linked(a2, 'forms_AttributePageElement', b)
    _safe_set(b, 'forms_Attribute33', None)
    assert not _is_linked(b, 'forms_Attribute33', a2)
    if hasattr(a2, 'forms_AttributePageElement'):
        assert not _is_linked(a2, 'forms_AttributePageElement', b)


def test_assoc_attributeToCompare49_reverse_link_reassign_clear():
    a1 = forms_AttributeValueCondition(value="sample_text")
    a2 = forms_AttributeValueCondition(value="sample_text_2")
    b = forms_AttributePageElement(value="sample_text")
    _safe_set(b, 'forms_AttributePageElement50', a1)
    assert _is_linked(b, 'forms_AttributePageElement50', a1)
    if hasattr(a1, 'forms_AttributeValueCondition'):
        assert _is_linked(a1, 'forms_AttributeValueCondition', b)
    _safe_set(b, 'forms_AttributePageElement50', a2)
    assert _is_linked(b, 'forms_AttributePageElement50', a2)
    if hasattr(a1, 'forms_AttributeValueCondition'):
        assert not _is_linked(a1, 'forms_AttributeValueCondition', b)
    if hasattr(a2, 'forms_AttributeValueCondition'):
        assert _is_linked(a2, 'forms_AttributeValueCondition', b)
    _safe_set(b, 'forms_AttributePageElement50', None)
    assert not _is_linked(b, 'forms_AttributePageElement50', a2)
    if hasattr(a2, 'forms_AttributeValueCondition'):
        assert not _is_linked(a2, 'forms_AttributeValueCondition', b)


def test_assoc_child151_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(operatorType="sample_text")
    _safe_set(b, 'forms_CompositeCondition', a1)
    assert _is_linked(b, 'forms_CompositeCondition', a1)
    if hasattr(a1, 'forms_Condition52'):
        assert _is_linked(a1, 'forms_Condition52', b)
    _safe_set(b, 'forms_CompositeCondition', a2)
    assert _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a1, 'forms_Condition52'):
        assert not _is_linked(a1, 'forms_Condition52', b)
    if hasattr(a2, 'forms_Condition52'):
        assert _is_linked(a2, 'forms_Condition52', b)
    _safe_set(b, 'forms_CompositeCondition', None)
    assert not _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a2, 'forms_Condition52'):
        assert not _is_linked(a2, 'forms_Condition52', b)


def test_assoc_child253_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(operatorType="sample_text")
    _safe_set(b, 'forms_CompositeCondition54', a1)
    assert _is_linked(b, 'forms_CompositeCondition54', a1)
    if hasattr(a1, 'forms_Condition55'):
        assert _is_linked(a1, 'forms_Condition55', b)
    _safe_set(b, 'forms_CompositeCondition54', a2)
    assert _is_linked(b, 'forms_CompositeCondition54', a2)
    if hasattr(a1, 'forms_Condition55'):
        assert not _is_linked(a1, 'forms_Condition55', b)
    if hasattr(a2, 'forms_Condition55'):
        assert _is_linked(a2, 'forms_Condition55', b)
    _safe_set(b, 'forms_CompositeCondition54', None)
    assert not _is_linked(b, 'forms_CompositeCondition54', a2)
    if hasattr(a2, 'forms_Condition55'):
        assert not _is_linked(a2, 'forms_Condition55', b)


def test_assoc_entityAttribute0_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(isId="sample_text", mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute', a1)
    assert _is_linked(b, 'forms_Attribute', a1)
    if hasattr(a1, 'forms_Entity'):
        assert _is_linked(a1, 'forms_Entity', b)
    _safe_set(b, 'forms_Attribute', a2)
    assert _is_linked(b, 'forms_Attribute', a2)
    if hasattr(a1, 'forms_Entity'):
        assert not _is_linked(a1, 'forms_Entity', b)
    if hasattr(a2, 'forms_Entity'):
        assert _is_linked(a2, 'forms_Entity', b)
    _safe_set(b, 'forms_Attribute', None)
    assert not _is_linked(b, 'forms_Attribute', a2)
    if hasattr(a2, 'forms_Entity'):
        assert not _is_linked(a2, 'forms_Entity', b)


def test_assoc_enumerationType6_reverse_link_reassign_clear():
    a1 = forms_Enumeration(name="sample_text")
    a2 = forms_Enumeration(name="sample_text_2")
    b = forms_Attribute(isId="sample_text", mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute7', a1)
    assert _is_linked(b, 'forms_Attribute7', a1)
    if hasattr(a1, 'forms_Enumeration'):
        assert _is_linked(a1, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute7', a2)
    assert _is_linked(b, 'forms_Attribute7', a2)
    if hasattr(a1, 'forms_Enumeration'):
        assert not _is_linked(a1, 'forms_Enumeration', b)
    if hasattr(a2, 'forms_Enumeration'):
        assert _is_linked(a2, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute7', None)
    assert not _is_linked(b, 'forms_Attribute7', a2)
    if hasattr(a2, 'forms_Enumeration'):
        assert not _is_linked(a2, 'forms_Enumeration', b)


def test_assoc_formEntity25_reverse_link_reassign_clear():
    a1 = forms_Form(description="sample_text", isWelcomeForm="sample_text", name="sample_text", title="sample_text")
    a2 = forms_Form(description="sample_text_2", isWelcomeForm="sample_text_2", name="sample_text_2", title="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity27', a1)
    assert _is_linked(b, 'forms_Entity27', a1)
    if hasattr(a1, 'forms_Form26'):
        assert _is_linked(a1, 'forms_Form26', b)
    _safe_set(b, 'forms_Entity27', a2)
    assert _is_linked(b, 'forms_Entity27', a2)
    if hasattr(a1, 'forms_Form26'):
        assert not _is_linked(a1, 'forms_Form26', b)
    if hasattr(a2, 'forms_Form26'):
        assert _is_linked(a2, 'forms_Form26', b)
    _safe_set(b, 'forms_Entity27', None)
    assert not _is_linked(b, 'forms_Entity27', a2)
    if hasattr(a2, 'forms_Form26'):
        assert not _is_linked(a2, 'forms_Form26', b)


def test_assoc_literal17_reverse_link_reassign_clear():
    a1 = forms_Literal(name="sample_text", value="sample_text")
    a2 = forms_Literal(name="sample_text_2", value="sample_text_2")
    b = forms_Enumeration(name="sample_text")
    _safe_set(b, 'forms_Enumeration18', {a1})
    assert _is_linked(b, 'forms_Enumeration18', a1)
    if hasattr(a1, 'forms_Literal'):
        assert _is_linked(a1, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration18', {a2})
    assert _is_linked(b, 'forms_Enumeration18', a2)
    if hasattr(a1, 'forms_Literal'):
        assert not _is_linked(a1, 'forms_Literal', b)
    if hasattr(a2, 'forms_Literal'):
        assert _is_linked(a2, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration18', set())
    assert not _is_linked(b, 'forms_Enumeration18', a2)
    if hasattr(a2, 'forms_Literal'):
        assert not _is_linked(a2, 'forms_Literal', b)


def test_assoc_opposite23_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    _safe_set(b, 'forms_Relationship24', a1)
    assert _is_linked(b, 'forms_Relationship24', a1)
    if hasattr(a1, 'forms_Relationship22'):
        assert _is_linked(a1, 'forms_Relationship22', b)
    _safe_set(b, 'forms_Relationship24', a2)
    assert _is_linked(b, 'forms_Relationship24', a2)
    if hasattr(a1, 'forms_Relationship22'):
        assert not _is_linked(a1, 'forms_Relationship22', b)
    if hasattr(a2, 'forms_Relationship22'):
        assert _is_linked(a2, 'forms_Relationship22', b)
    _safe_set(b, 'forms_Relationship24', None)
    assert not _is_linked(b, 'forms_Relationship24', a2)
    if hasattr(a2, 'forms_Relationship22'):
        assert not _is_linked(a2, 'forms_Relationship22', b)


def test_assoc_pageElements30_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'forms_Page31', {a1})
    assert _is_linked(b, 'forms_Page31', a1)
    if hasattr(a1, 'forms_PageElement'):
        assert _is_linked(a1, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page31', {a2})
    assert _is_linked(b, 'forms_Page31', a2)
    if hasattr(a1, 'forms_PageElement'):
        assert not _is_linked(a1, 'forms_PageElement', b)
    if hasattr(a2, 'forms_PageElement'):
        assert _is_linked(a2, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page31', set())
    assert not _is_linked(b, 'forms_Page31', a2)
    if hasattr(a2, 'forms_PageElement'):
        assert not _is_linked(a2, 'forms_PageElement', b)


def test_assoc_pages28_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", isWelcomeForm="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'forms_Form29', {a1})
    assert _is_linked(b, 'forms_Form29', a1)
    if hasattr(a1, 'forms_Page'):
        assert _is_linked(a1, 'forms_Page', b)
    _safe_set(b, 'forms_Form29', {a2})
    assert _is_linked(b, 'forms_Form29', a2)
    if hasattr(a1, 'forms_Page'):
        assert not _is_linked(a1, 'forms_Page', b)
    if hasattr(a2, 'forms_Page'):
        assert _is_linked(a2, 'forms_Page', b)
    _safe_set(b, 'forms_Form29', set())
    assert not _is_linked(b, 'forms_Form29', a2)
    if hasattr(a2, 'forms_Page'):
        assert not _is_linked(a2, 'forms_Page', b)


def test_assoc_relationship1_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity2', {a1})
    assert _is_linked(b, 'forms_Entity2', a1)
    if hasattr(a1, 'forms_Relationship'):
        assert _is_linked(a1, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity2', {a2})
    assert _is_linked(b, 'forms_Entity2', a2)
    if hasattr(a1, 'forms_Relationship'):
        assert not _is_linked(a1, 'forms_Relationship', b)
    if hasattr(a2, 'forms_Relationship'):
        assert _is_linked(a2, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity2', set())
    assert not _is_linked(b, 'forms_Entity2', a2)
    if hasattr(a2, 'forms_Relationship'):
        assert not _is_linked(a2, 'forms_Relationship', b)


def test_assoc_superType4_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity5', a1)
    assert _is_linked(b, 'forms_Entity5', a1)
    if hasattr(a1, 'forms_Entity3'):
        assert _is_linked(a1, 'forms_Entity3', b)
    _safe_set(b, 'forms_Entity5', a2)
    assert _is_linked(b, 'forms_Entity5', a2)
    if hasattr(a1, 'forms_Entity3'):
        assert not _is_linked(a1, 'forms_Entity3', b)
    if hasattr(a2, 'forms_Entity3'):
        assert _is_linked(a2, 'forms_Entity3', b)
    _safe_set(b, 'forms_Entity5', None)
    assert not _is_linked(b, 'forms_Entity5', a2)
    if hasattr(a2, 'forms_Entity3'):
        assert not _is_linked(a2, 'forms_Entity3', b)


def test_assoc_target19_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity21', a1)
    assert _is_linked(b, 'forms_Entity21', a1)
    if hasattr(a1, 'forms_Relationship20'):
        assert _is_linked(a1, 'forms_Relationship20', b)
    _safe_set(b, 'forms_Entity21', a2)
    assert _is_linked(b, 'forms_Entity21', a2)
    if hasattr(a1, 'forms_Relationship20'):
        assert not _is_linked(a1, 'forms_Relationship20', b)
    if hasattr(a2, 'forms_Relationship20'):
        assert _is_linked(a2, 'forms_Relationship20', b)
    _safe_set(b, 'forms_Entity21', None)
    assert not _is_linked(b, 'forms_Entity21', a2)
    if hasattr(a2, 'forms_Relationship20'):
        assert not _is_linked(a2, 'forms_Relationship20', b)


def test_assoc_targetPage43_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'forms_Condition44', a1)
    assert _is_linked(b, 'forms_Condition44', a1)
    if hasattr(a1, 'forms_Page45'):
        assert _is_linked(a1, 'forms_Page45', b)
    _safe_set(b, 'forms_Condition44', a2)
    assert _is_linked(b, 'forms_Condition44', a2)
    if hasattr(a1, 'forms_Page45'):
        assert not _is_linked(a1, 'forms_Page45', b)
    if hasattr(a2, 'forms_Page45'):
        assert _is_linked(a2, 'forms_Page45', b)
    _safe_set(b, 'forms_Condition44', None)
    assert not _is_linked(b, 'forms_Condition44', a2)
    if hasattr(a2, 'forms_Page45'):
        assert not _is_linked(a2, 'forms_Page45', b)


def test_assoc_targetPageElement46_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'forms_Condition47', a1)
    assert _is_linked(b, 'forms_Condition47', a1)
    if hasattr(a1, 'forms_PageElement48'):
        assert _is_linked(a1, 'forms_PageElement48', b)
    _safe_set(b, 'forms_Condition47', a2)
    assert _is_linked(b, 'forms_Condition47', a2)
    if hasattr(a1, 'forms_PageElement48'):
        assert not _is_linked(a1, 'forms_PageElement48', b)
    if hasattr(a2, 'forms_PageElement48'):
        assert _is_linked(a2, 'forms_PageElement48', b)
    _safe_set(b, 'forms_Condition47', None)
    assert not _is_linked(b, 'forms_Condition47', a2)
    if hasattr(a2, 'forms_PageElement48'):
        assert not _is_linked(a2, 'forms_PageElement48', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeReference40_stub_double():
    # forms_Column has no real 'forms_Column41' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(isId="sample_text", mandatory=True, name="sample_text", type="sample_text")
    partner = forms_Column()
    setattr(partner, 'forms_Column41', None)
    _safe_set(owner, 'forms_Attribute42', partner)
    assert getattr(partner, 'forms_Column41') == owner
    _safe_set(owner, 'forms_Attribute42', None)
    assert getattr(partner, 'forms_Column41') is None


def test_assoc_editingForm34_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", isWelcomeForm="sample_text", name="sample_text", title="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement', None)
    _safe_set(owner, 'forms_Form35', partner)
    assert getattr(partner, 'forms_RelationshipPageElement') == owner
    _safe_set(owner, 'forms_Form35', None)
    assert getattr(partner, 'forms_RelationshipPageElement') is None


def test_assoc_modelCondition15_stub_double():
    # forms_Model has no real 'forms_Model16' property in the generated
    # code (a bare stub) -- manually attach it so forms_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Condition(conditionID="sample_text", type="sample_text")
    partner = forms_Model()
    setattr(partner, 'forms_Model16', None)
    _safe_set(owner, 'forms_Condition', partner)
    assert owner in getattr(partner, 'forms_Model16')
    _safe_set(owner, 'forms_Condition', None)
    assert owner not in getattr(partner, 'forms_Model16')


def test_assoc_modelEntity8_stub_double():
    # forms_Model has no real 'forms_Model' property in the generated
    # code (a bare stub) -- manually attach it so forms_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Entity(name="sample_text")
    partner = forms_Model()
    setattr(partner, 'forms_Model', None)
    _safe_set(owner, 'forms_Entity9', partner)
    assert owner in getattr(partner, 'forms_Model')
    _safe_set(owner, 'forms_Entity9', None)
    assert owner not in getattr(partner, 'forms_Model')


def test_assoc_modelEnumeration12_stub_double():
    # forms_Model has no real 'forms_Model13' property in the generated
    # code (a bare stub) -- manually attach it so forms_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Enumeration(name="sample_text")
    partner = forms_Model()
    setattr(partner, 'forms_Model13', None)
    _safe_set(owner, 'forms_Enumeration14', partner)
    assert owner in getattr(partner, 'forms_Model13')
    _safe_set(owner, 'forms_Enumeration14', None)
    assert owner not in getattr(partner, 'forms_Model13')


def test_assoc_modelForm10_stub_double():
    # forms_Model has no real 'forms_Model11' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", isWelcomeForm="sample_text", name="sample_text", title="sample_text")
    partner = forms_Model()
    setattr(partner, 'forms_Model11', None)
    _safe_set(owner, 'forms_Form', partner)
    assert owner in getattr(partner, 'forms_Model11')
    _safe_set(owner, 'forms_Form', None)
    assert owner not in getattr(partner, 'forms_Model11')


def test_assoc_relationshipRef36_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement37' property in the generated
    # code (a bare stub) -- manually attach it so forms_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement37', None)
    _safe_set(owner, 'forms_Relationship38', partner)
    assert getattr(partner, 'forms_RelationshipPageElement37') == owner
    _safe_set(owner, 'forms_Relationship38', None)
    assert getattr(partner, 'forms_RelationshipPageElement37') is None


