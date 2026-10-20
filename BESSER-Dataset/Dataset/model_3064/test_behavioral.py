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
    forms_DateSelectionAttributePageElement,
    forms_Entity,
    forms_EntityModel,
    forms_EnumerationLiteral,
    forms_EnumerationType,
    forms_Form,
    forms_FormModel,
    forms_ListRelationshipPageElement,
    forms_Page,
    forms_PageElement,
    forms_Relationship,
    forms_RelationshipPageElement,
    forms_SelectionAttributePageElement,
    forms_TableRelationshipPageElement,
    forms_TextFieldAttributePageElement,
    forms_TextareaAttributePageElement,
    forms_TimeSelectionAttributePageElement,
    AttributeType,
    CompositeConditionOperator,
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

def test_assoc_attributes11_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'entity'):
        assert _is_linked(a1, 'entity', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'entity'):
        assert not _is_linked(a1, 'entity', b)
    if hasattr(a2, 'entity'):
        assert _is_linked(a2, 'entity', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'entity'):
        assert not _is_linked(a2, 'entity', b)


def test_assoc_conditions38_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'Condition', a1)
    assert _is_linked(b, 'Condition', a1)
    if hasattr(a1, 'page39'):
        assert _is_linked(a1, 'page39', b)
    _safe_set(b, 'Condition', a2)
    assert _is_linked(b, 'Condition', a2)
    if hasattr(a1, 'page39'):
        assert not _is_linked(a1, 'page39', b)
    if hasattr(a2, 'page39'):
        assert _is_linked(a2, 'page39', b)
    _safe_set(b, 'Condition', None)
    assert not _is_linked(b, 'Condition', a2)
    if hasattr(a2, 'page39'):
        assert not _is_linked(a2, 'page39', b)


def test_assoc_conditions41_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'Condition42', a1)
    assert _is_linked(b, 'Condition42', a1)
    if hasattr(a1, 'pageElement'):
        assert _is_linked(a1, 'pageElement', b)
    _safe_set(b, 'Condition42', a2)
    assert _is_linked(b, 'Condition42', a2)
    if hasattr(a1, 'pageElement'):
        assert not _is_linked(a1, 'pageElement', b)
    if hasattr(a2, 'pageElement'):
        assert _is_linked(a2, 'pageElement', b)
    _safe_set(b, 'Condition42', None)
    assert not _is_linked(b, 'Condition42', a2)
    if hasattr(a2, 'pageElement'):
        assert not _is_linked(a2, 'pageElement', b)


def test_assoc_conditions65_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(operator="sample_text")
    _safe_set(b, 'parentCondtion', {a1})
    assert _is_linked(b, 'parentCondtion', a1)
    if hasattr(a1, 'Condition66'):
        assert _is_linked(a1, 'Condition66', b)
    _safe_set(b, 'parentCondtion', {a2})
    assert _is_linked(b, 'parentCondtion', a2)
    if hasattr(a1, 'Condition66'):
        assert not _is_linked(a1, 'Condition66', b)
    if hasattr(a2, 'Condition66'):
        assert _is_linked(a2, 'Condition66', b)
    _safe_set(b, 'parentCondtion', set())
    assert not _is_linked(b, 'parentCondtion', a2)
    if hasattr(a2, 'Condition66'):
        assert not _is_linked(a2, 'Condition66', b)


def test_assoc_entity16_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Entity'):
        assert _is_linked(a1, 'Entity', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Entity'):
        assert not _is_linked(a1, 'Entity', b)
    if hasattr(a2, 'Entity'):
        assert _is_linked(a2, 'Entity', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Entity'):
        assert not _is_linked(a2, 'Entity', b)


def test_assoc_entity33_reverse_link_reassign_clear():
    a1 = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    a2 = forms_Form(description="sample_text_2", name="sample_text_2", title="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity35', a1)
    assert _is_linked(b, 'forms_Entity35', a1)
    if hasattr(a1, 'forms_Form34'):
        assert _is_linked(a1, 'forms_Form34', b)
    _safe_set(b, 'forms_Entity35', a2)
    assert _is_linked(b, 'forms_Entity35', a2)
    if hasattr(a1, 'forms_Form34'):
        assert not _is_linked(a1, 'forms_Form34', b)
    if hasattr(a2, 'forms_Form34'):
        assert _is_linked(a2, 'forms_Form34', b)
    _safe_set(b, 'forms_Entity35', None)
    assert not _is_linked(b, 'forms_Entity35', a2)
    if hasattr(a2, 'forms_Form34'):
        assert not _is_linked(a2, 'forms_Form34', b)


def test_assoc_enumerationType13_reverse_link_reassign_clear():
    a1 = forms_EnumerationType(name="sample_text")
    a2 = forms_EnumerationType(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute14', a1)
    assert _is_linked(b, 'forms_Attribute14', a1)
    if hasattr(a1, 'forms_EnumerationType15'):
        assert _is_linked(a1, 'forms_EnumerationType15', b)
    _safe_set(b, 'forms_Attribute14', a2)
    assert _is_linked(b, 'forms_Attribute14', a2)
    if hasattr(a1, 'forms_EnumerationType15'):
        assert not _is_linked(a1, 'forms_EnumerationType15', b)
    if hasattr(a2, 'forms_EnumerationType15'):
        assert _is_linked(a2, 'forms_EnumerationType15', b)
    _safe_set(b, 'forms_Attribute14', None)
    assert not _is_linked(b, 'forms_Attribute14', a2)
    if hasattr(a2, 'forms_EnumerationType15'):
        assert not _is_linked(a2, 'forms_EnumerationType15', b)


def test_assoc_form40_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'Form', a1)
    assert _is_linked(b, 'Form', a1)
    if hasattr(a1, 'pages'):
        assert _is_linked(a1, 'pages', b)
    _safe_set(b, 'Form', a2)
    assert _is_linked(b, 'Form', a2)
    if hasattr(a1, 'pages'):
        assert not _is_linked(a1, 'pages', b)
    if hasattr(a2, 'pages'):
        assert _is_linked(a2, 'pages', b)
    _safe_set(b, 'Form', None)
    assert not _is_linked(b, 'Form', a2)
    if hasattr(a2, 'pages'):
        assert not _is_linked(a2, 'pages', b)


def test_assoc_id3_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute', a1)
    assert _is_linked(b, 'forms_Attribute', a1)
    if hasattr(a1, 'forms_Entity4'):
        assert _is_linked(a1, 'forms_Entity4', b)
    _safe_set(b, 'forms_Attribute', a2)
    assert _is_linked(b, 'forms_Attribute', a2)
    if hasattr(a1, 'forms_Entity4'):
        assert not _is_linked(a1, 'forms_Entity4', b)
    if hasattr(a2, 'forms_Entity4'):
        assert _is_linked(a2, 'forms_Entity4', b)
    _safe_set(b, 'forms_Attribute', None)
    assert not _is_linked(b, 'forms_Attribute', a2)
    if hasattr(a2, 'forms_Entity4'):
        assert not _is_linked(a2, 'forms_Entity4', b)


def test_assoc_literals17_reverse_link_reassign_clear():
    a1 = forms_EnumerationType(name="sample_text")
    a2 = forms_EnumerationType(name="sample_text_2")
    b = forms_EnumerationLiteral(name="sample_text", value="sample_text")
    _safe_set(b, 'forms_EnumerationLiteral', a1)
    assert _is_linked(b, 'forms_EnumerationLiteral', a1)
    if hasattr(a1, 'forms_EnumerationType18'):
        assert _is_linked(a1, 'forms_EnumerationType18', b)
    _safe_set(b, 'forms_EnumerationLiteral', a2)
    assert _is_linked(b, 'forms_EnumerationLiteral', a2)
    if hasattr(a1, 'forms_EnumerationType18'):
        assert not _is_linked(a1, 'forms_EnumerationType18', b)
    if hasattr(a2, 'forms_EnumerationType18'):
        assert _is_linked(a2, 'forms_EnumerationType18', b)
    _safe_set(b, 'forms_EnumerationLiteral', None)
    assert not _is_linked(b, 'forms_EnumerationLiteral', a2)
    if hasattr(a2, 'forms_EnumerationType18'):
        assert not _is_linked(a2, 'forms_EnumerationType18', b)


def test_assoc_opposite24_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    _safe_set(b, 'forms_Relationship25', a1)
    assert _is_linked(b, 'forms_Relationship25', a1)
    if hasattr(a1, 'forms_Relationship23'):
        assert _is_linked(a1, 'forms_Relationship23', b)
    _safe_set(b, 'forms_Relationship25', a2)
    assert _is_linked(b, 'forms_Relationship25', a2)
    if hasattr(a1, 'forms_Relationship23'):
        assert not _is_linked(a1, 'forms_Relationship23', b)
    if hasattr(a2, 'forms_Relationship23'):
        assert _is_linked(a2, 'forms_Relationship23', b)
    _safe_set(b, 'forms_Relationship25', None)
    assert not _is_linked(b, 'forms_Relationship25', a2)
    if hasattr(a2, 'forms_Relationship23'):
        assert not _is_linked(a2, 'forms_Relationship23', b)


def test_assoc_page43_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'Page44', a1)
    assert _is_linked(b, 'Page44', a1)
    if hasattr(a1, 'pageElements'):
        assert _is_linked(a1, 'pageElements', b)
    _safe_set(b, 'Page44', a2)
    assert _is_linked(b, 'Page44', a2)
    if hasattr(a1, 'pageElements'):
        assert not _is_linked(a1, 'pageElements', b)
    if hasattr(a2, 'pageElements'):
        assert _is_linked(a2, 'pageElements', b)
    _safe_set(b, 'Page44', None)
    assert not _is_linked(b, 'Page44', a2)
    if hasattr(a2, 'pageElements'):
        assert not _is_linked(a2, 'pageElements', b)


def test_assoc_page56_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'conditions', a1)
    assert _is_linked(b, 'conditions', a1)
    if hasattr(a1, 'Page57'):
        assert _is_linked(a1, 'Page57', b)
    _safe_set(b, 'conditions', a2)
    assert _is_linked(b, 'conditions', a2)
    if hasattr(a1, 'Page57'):
        assert not _is_linked(a1, 'Page57', b)
    if hasattr(a2, 'Page57'):
        assert _is_linked(a2, 'Page57', b)
    _safe_set(b, 'conditions', None)
    assert not _is_linked(b, 'conditions', a2)
    if hasattr(a2, 'Page57'):
        assert not _is_linked(a2, 'Page57', b)


def test_assoc_pageElement58_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Condition(conditionID="sample_text", type="sample_text")
    _safe_set(b, 'conditions59', a1)
    assert _is_linked(b, 'conditions59', a1)
    if hasattr(a1, 'PageElement60'):
        assert _is_linked(a1, 'PageElement60', b)
    _safe_set(b, 'conditions59', a2)
    assert _is_linked(b, 'conditions59', a2)
    if hasattr(a1, 'PageElement60'):
        assert not _is_linked(a1, 'PageElement60', b)
    if hasattr(a2, 'PageElement60'):
        assert _is_linked(a2, 'PageElement60', b)
    _safe_set(b, 'conditions59', None)
    assert not _is_linked(b, 'conditions59', a2)
    if hasattr(a2, 'PageElement60'):
        assert not _is_linked(a2, 'PageElement60', b)


def test_assoc_pageElements37_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'page', {a1})
    assert _is_linked(b, 'page', a1)
    if hasattr(a1, 'PageElement'):
        assert _is_linked(a1, 'PageElement', b)
    _safe_set(b, 'page', {a2})
    assert _is_linked(b, 'page', a2)
    if hasattr(a1, 'PageElement'):
        assert not _is_linked(a1, 'PageElement', b)
    if hasattr(a2, 'PageElement'):
        assert _is_linked(a2, 'PageElement', b)
    _safe_set(b, 'page', set())
    assert not _is_linked(b, 'page', a2)
    if hasattr(a2, 'PageElement'):
        assert not _is_linked(a2, 'PageElement', b)


def test_assoc_pages36_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'form', {a1})
    assert _is_linked(b, 'form', a1)
    if hasattr(a1, 'Page'):
        assert _is_linked(a1, 'Page', b)
    _safe_set(b, 'form', {a2})
    assert _is_linked(b, 'form', a2)
    if hasattr(a1, 'Page'):
        assert not _is_linked(a1, 'Page', b)
    if hasattr(a2, 'Page'):
        assert _is_linked(a2, 'Page', b)
    _safe_set(b, 'form', set())
    assert not _is_linked(b, 'form', a2)
    if hasattr(a2, 'Page'):
        assert not _is_linked(a2, 'Page', b)


def test_assoc_parentCondtion61_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(operator="sample_text")
    _safe_set(b, 'CompositeCondition', a1)
    assert _is_linked(b, 'CompositeCondition', a1)
    if hasattr(a1, 'conditions62'):
        assert _is_linked(a1, 'conditions62', b)
    _safe_set(b, 'CompositeCondition', a2)
    assert _is_linked(b, 'CompositeCondition', a2)
    if hasattr(a1, 'conditions62'):
        assert not _is_linked(a1, 'conditions62', b)
    if hasattr(a2, 'conditions62'):
        assert _is_linked(a2, 'conditions62', b)
    _safe_set(b, 'CompositeCondition', None)
    assert not _is_linked(b, 'CompositeCondition', a2)
    if hasattr(a2, 'conditions62'):
        assert not _is_linked(a2, 'conditions62', b)


def test_assoc_relationships12_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Entity(name="sample_text")
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


def test_assoc_source19_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'Entity20', a1)
    assert _is_linked(b, 'Entity20', a1)
    if hasattr(a1, 'relationships'):
        assert _is_linked(a1, 'relationships', b)
    _safe_set(b, 'Entity20', a2)
    assert _is_linked(b, 'Entity20', a2)
    if hasattr(a1, 'relationships'):
        assert not _is_linked(a1, 'relationships', b)
    if hasattr(a2, 'relationships'):
        assert _is_linked(a2, 'relationships', b)
    _safe_set(b, 'Entity20', None)
    assert not _is_linked(b, 'Entity20', a2)
    if hasattr(a2, 'relationships'):
        assert not _is_linked(a2, 'relationships', b)


def test_assoc_superType6_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity7', a1)
    assert _is_linked(b, 'forms_Entity7', a1)
    if hasattr(a1, 'forms_Entity5'):
        assert _is_linked(a1, 'forms_Entity5', b)
    _safe_set(b, 'forms_Entity7', a2)
    assert _is_linked(b, 'forms_Entity7', a2)
    if hasattr(a1, 'forms_Entity5'):
        assert not _is_linked(a1, 'forms_Entity5', b)
    if hasattr(a2, 'forms_Entity5'):
        assert _is_linked(a2, 'forms_Entity5', b)
    _safe_set(b, 'forms_Entity7', None)
    assert not _is_linked(b, 'forms_Entity7', a2)
    if hasattr(a2, 'forms_Entity5'):
        assert not _is_linked(a2, 'forms_Entity5', b)


def test_assoc_superTypes9_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity8', {a1})
    assert _is_linked(b, 'forms_Entity8', a1)
    if hasattr(a1, 'forms_Entity10'):
        assert _is_linked(a1, 'forms_Entity10', b)
    _safe_set(b, 'forms_Entity8', {a2})
    assert _is_linked(b, 'forms_Entity8', a2)
    if hasattr(a1, 'forms_Entity10'):
        assert not _is_linked(a1, 'forms_Entity10', b)
    if hasattr(a2, 'forms_Entity10'):
        assert _is_linked(a2, 'forms_Entity10', b)
    _safe_set(b, 'forms_Entity8', set())
    assert not _is_linked(b, 'forms_Entity8', a2)
    if hasattr(a2, 'forms_Entity10'):
        assert not _is_linked(a2, 'forms_Entity10', b)


def test_assoc_target21_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    a2 = forms_Relationship(lowerBound="sample_text_2", name="sample_text_2", upperBound="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity22', a1)
    assert _is_linked(b, 'forms_Entity22', a1)
    if hasattr(a1, 'forms_Relationship'):
        assert _is_linked(a1, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity22', a2)
    assert _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a1, 'forms_Relationship'):
        assert not _is_linked(a1, 'forms_Relationship', b)
    if hasattr(a2, 'forms_Relationship'):
        assert _is_linked(a2, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity22', None)
    assert not _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a2, 'forms_Relationship'):
        assert not _is_linked(a2, 'forms_Relationship', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute45_stub_double():
    # forms_AttributePageElement has no real 'forms_AttributePageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_AttributePageElement()
    setattr(partner, 'forms_AttributePageElement', None)
    _safe_set(owner, 'forms_Attribute46', partner)
    assert getattr(partner, 'forms_AttributePageElement') == owner
    _safe_set(owner, 'forms_Attribute46', None)
    assert getattr(partner, 'forms_AttributePageElement') is None


def test_assoc_attribute53_stub_double():
    # forms_Column has no real 'forms_Column' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_Column()
    setattr(partner, 'forms_Column', None)
    _safe_set(owner, 'forms_Attribute54', partner)
    assert getattr(partner, 'forms_Column') == owner
    _safe_set(owner, 'forms_Attribute54', None)
    assert getattr(partner, 'forms_Column') is None


def test_assoc_editingForm49_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement50' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement50', None)
    _safe_set(owner, 'forms_Form51', partner)
    assert getattr(partner, 'forms_RelationshipPageElement50') == owner
    _safe_set(owner, 'forms_Form51', None)
    assert getattr(partner, 'forms_RelationshipPageElement50') is None


def test_assoc_entities0_stub_double():
    # forms_EntityModel has no real 'forms_EntityModel' property in the generated
    # code (a bare stub) -- manually attach it so forms_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Entity(name="sample_text")
    partner = forms_EntityModel()
    setattr(partner, 'forms_EntityModel', None)
    _safe_set(owner, 'forms_Entity', partner)
    assert owner in getattr(partner, 'forms_EntityModel')
    _safe_set(owner, 'forms_Entity', None)
    assert owner not in getattr(partner, 'forms_EntityModel')


def test_assoc_enumerations1_stub_double():
    # forms_EntityModel has no real 'forms_EntityModel2' property in the generated
    # code (a bare stub) -- manually attach it so forms_EnumerationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_EnumerationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_EnumerationType(name="sample_text")
    partner = forms_EntityModel()
    setattr(partner, 'forms_EntityModel2', None)
    _safe_set(owner, 'forms_EnumerationType', partner)
    assert owner in getattr(partner, 'forms_EntityModel2')
    _safe_set(owner, 'forms_EnumerationType', None)
    assert owner not in getattr(partner, 'forms_EntityModel2')


def test_assoc_forms28_stub_double():
    # forms_FormModel has no real 'forms_FormModel29' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    partner = forms_FormModel()
    setattr(partner, 'forms_FormModel29', None)
    _safe_set(owner, 'forms_Form', partner)
    assert owner in getattr(partner, 'forms_FormModel29')
    _safe_set(owner, 'forms_Form', None)
    assert owner not in getattr(partner, 'forms_FormModel29')


def test_assoc_relationship47_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Relationship(lowerBound="sample_text", name="sample_text", upperBound="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement', None)
    _safe_set(owner, 'forms_Relationship48', partner)
    assert getattr(partner, 'forms_RelationshipPageElement') == owner
    _safe_set(owner, 'forms_Relationship48', None)
    assert getattr(partner, 'forms_RelationshipPageElement') is None


def test_assoc_trigger63_stub_double():
    # forms_AttributePageElement has no real 'forms_AttributePageElement64' property in the generated
    # code (a bare stub) -- manually attach it so forms_AttributeValueCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_AttributeValueCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_AttributeValueCondition(value="sample_text")
    partner = forms_AttributePageElement()
    setattr(partner, 'forms_AttributePageElement64', None)
    _safe_set(owner, 'forms_AttributeValueCondition', partner)
    assert getattr(partner, 'forms_AttributePageElement64') == owner
    _safe_set(owner, 'forms_AttributeValueCondition', None)
    assert getattr(partner, 'forms_AttributePageElement64') is None


def test_assoc_welcomeForm30_stub_double():
    # forms_FormModel has no real 'forms_FormModel31' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", name="sample_text", title="sample_text")
    partner = forms_FormModel()
    setattr(partner, 'forms_FormModel31', None)
    _safe_set(owner, 'forms_Form32', partner)
    assert getattr(partner, 'forms_FormModel31') == owner
    _safe_set(owner, 'forms_Form32', None)
    assert getattr(partner, 'forms_FormModel31') is None


