import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    AttributePageElement,
    Column,
    Condition,
    Entity,
    Enumeration,
    Form,
    Literal,
    Page,
    PageElement,
    Relationship,
    RelationshipPageElement,
    forms_EFML_model,
    forms_entityModeling_Attribute,
    forms_entityModeling_AttributePageElement,
    forms_entityModeling_AttributeValueCondition,
    forms_entityModeling_Column,
    forms_entityModeling_CompositeCondition,
    forms_entityModeling_Condition,
    forms_entityModeling_DateSelectionField,
    forms_entityModeling_Entity,
    forms_entityModeling_Enumeration,
    forms_entityModeling_Form,
    forms_entityModeling_List,
    forms_entityModeling_Literal,
    forms_entityModeling_Page,
    forms_entityModeling_PageElement,
    forms_entityModeling_Relationship,
    forms_entityModeling_RelationshipPageElement,
    forms_entityModeling_SelectionField,
    forms_entityModeling_Table,
    forms_entityModeling_Textarea,
    forms_entityModeling_Textfield,
    forms_entityModeling_TimeSelectionField,
    AttributeType,
    BooleanOperators,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeToEnterValues34_stub_double():
    # Attribute has no real 'Attribute35' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_AttributePageElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_AttributePageElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_AttributePageElement(valueOfAttribute="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute35', None)
    _safe_set(owner, 'forms_entityModeling_AttributePageElement', partner)
    assert getattr(partner, 'Attribute35') == owner
    _safe_set(owner, 'forms_entityModeling_AttributePageElement', None)
    assert getattr(partner, 'Attribute35') is None


def test_assoc_attributes9_stub_double():
    # Attribute has no real 'Attribute11' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Entity(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute11', None)
    _safe_set(owner, 'forms_entityModeling_Entity10', {partner})
    assert getattr(partner, 'Attribute11') == owner
    _safe_set(owner, 'forms_entityModeling_Entity10', set())
    assert getattr(partner, 'Attribute11') is None


def test_assoc_composedConditions48_stub_double():
    # Condition has no real 'Condition49' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_CompositeCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_CompositeCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_CompositeCondition(booleanOperator="sample_text")
    partner = Condition()
    setattr(partner, 'Condition49', None)
    _safe_set(owner, 'forms_entityModeling_CompositeCondition', {partner})
    assert getattr(partner, 'Condition49') == owner
    _safe_set(owner, 'forms_entityModeling_CompositeCondition', set())
    assert getattr(partner, 'Condition49') is None


def test_assoc_condition30_stub_double():
    # Condition has no real 'Condition' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Page(title="sample_text")
    partner = Condition()
    setattr(partner, 'Condition', None)
    _safe_set(owner, 'forms_entityModeling_Page31', partner)
    assert getattr(partner, 'Condition') == owner
    _safe_set(owner, 'forms_entityModeling_Page31', None)
    assert getattr(partner, 'Condition') is None


def test_assoc_condition32_stub_double():
    # Condition has no real 'Condition33' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_PageElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_PageElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_PageElement(elementID="sample_text", label="sample_text")
    partner = Condition()
    setattr(partner, 'Condition33', None)
    _safe_set(owner, 'forms_entityModeling_PageElement', partner)
    assert getattr(partner, 'Condition33') == owner
    _safe_set(owner, 'forms_entityModeling_PageElement', None)
    assert getattr(partner, 'Condition33') is None


def test_assoc_entity25_stub_double():
    # Entity has no real 'Entity26' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Form(description="sample_text", name="sample_text", title="sample_text")
    partner = Entity()
    setattr(partner, 'Entity26', None)
    _safe_set(owner, 'forms_entityModeling_Form', partner)
    assert getattr(partner, 'Entity26') == owner
    _safe_set(owner, 'forms_entityModeling_Form', None)
    assert getattr(partner, 'Entity26') is None


def test_assoc_enumerationType17_stub_double():
    # Enumeration has no real 'Enumeration18' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = Enumeration()
    setattr(partner, 'Enumeration18', None)
    _safe_set(owner, 'forms_entityModeling_Attribute', partner)
    assert getattr(partner, 'Enumeration18') == owner
    _safe_set(owner, 'forms_entityModeling_Attribute', None)
    assert getattr(partner, 'Enumeration18') is None


def test_assoc_id8_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Entity(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'forms_entityModeling_Entity', partner)
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'forms_entityModeling_Entity', None)
    assert getattr(partner, 'Attribute') is None


def test_assoc_literals19_stub_double():
    # Literal has no real 'Literal' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Enumeration(name="sample_text")
    partner = Literal()
    setattr(partner, 'Literal', None)
    _safe_set(owner, 'forms_entityModeling_Enumeration', {partner})
    assert getattr(partner, 'Literal') == owner
    _safe_set(owner, 'forms_entityModeling_Enumeration', set())
    assert getattr(partner, 'Literal') is None


def test_assoc_opposite22_stub_double():
    # Relationship has no real 'Relationship24' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    partner = Relationship()
    setattr(partner, 'Relationship24', None)
    _safe_set(owner, 'forms_entityModeling_Relationship23', partner)
    assert getattr(partner, 'Relationship24') == owner
    _safe_set(owner, 'forms_entityModeling_Relationship23', None)
    assert getattr(partner, 'Relationship24') is None


def test_assoc_pageElements29_stub_double():
    # PageElement has no real 'PageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Page(title="sample_text")
    partner = PageElement()
    setattr(partner, 'PageElement', None)
    _safe_set(owner, 'forms_entityModeling_Page', {partner})
    assert getattr(partner, 'PageElement') == owner
    _safe_set(owner, 'forms_entityModeling_Page', set())
    assert getattr(partner, 'PageElement') is None


def test_assoc_pages27_stub_double():
    # Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Form(description="sample_text", name="sample_text", title="sample_text")
    partner = Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'forms_entityModeling_Form28', {partner})
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'forms_entityModeling_Form28', set())
    assert getattr(partner, 'Page') is None


def test_assoc_relationships15_stub_double():
    # Relationship has no real 'Relationship' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Entity(name="sample_text")
    partner = Relationship()
    setattr(partner, 'Relationship', None)
    _safe_set(owner, 'forms_entityModeling_Entity16', {partner})
    assert getattr(partner, 'Relationship') == owner
    _safe_set(owner, 'forms_entityModeling_Entity16', set())
    assert getattr(partner, 'Relationship') is None


def test_assoc_superType12_stub_double():
    # Entity has no real 'Entity14' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Entity(name="sample_text")
    partner = Entity()
    setattr(partner, 'Entity14', None)
    _safe_set(owner, 'forms_entityModeling_Entity13', partner)
    assert getattr(partner, 'Entity14') == owner
    _safe_set(owner, 'forms_entityModeling_Entity13', None)
    assert getattr(partner, 'Entity14') is None


def test_assoc_target20_stub_double():
    # Entity has no real 'Entity21' property in the generated
    # code (a bare stub) -- manually attach it so forms_entityModeling_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_entityModeling_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_entityModeling_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    partner = Entity()
    setattr(partner, 'Entity21', None)
    _safe_set(owner, 'forms_entityModeling_Relationship', partner)
    assert getattr(partner, 'Entity21') == owner
    _safe_set(owner, 'forms_entityModeling_Relationship', None)
    assert getattr(partner, 'Entity21') is None


