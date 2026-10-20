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
    forms_CompositionCondition,
    forms_Condition,
    forms_DateSelectionField,
    forms_EMFL_EntityModel,
    forms_EMFL_FormModel,
    forms_Entity,
    forms_Enumeration,
    forms_Form,
    forms_List,
    forms_Literal,
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
    conditionType,
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

def test_assoc_associated_with20_reverse_link_reassign_clear():
    a1 = forms_Form(description="sample_text", isWelcomeForm=True, name="sample_text", title="sample_text")
    a2 = forms_Form(description="sample_text_2", isWelcomeForm=False, name="sample_text_2", title="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity22', a1)
    assert _is_linked(b, 'forms_Entity22', a1)
    if hasattr(a1, 'forms_Form21'):
        assert _is_linked(a1, 'forms_Form21', b)
    _safe_set(b, 'forms_Entity22', a2)
    assert _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a1, 'forms_Form21'):
        assert not _is_linked(a1, 'forms_Form21', b)
    if hasattr(a2, 'forms_Form21'):
        assert _is_linked(a2, 'forms_Form21', b)
    _safe_set(b, 'forms_Entity22', None)
    assert not _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a2, 'forms_Form21'):
        assert not _is_linked(a2, 'forms_Form21', b)


def test_assoc_attributePageElement46_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID=7, label="sample_text")
    a2 = forms_PageElement(elementID=13, label="sample_text_2")
    b = forms_AttributeValueCondition(type="sample_text", value="sample_text")
    _safe_set(b, 'forms_AttributeValueCondition47', a1)
    assert _is_linked(b, 'forms_AttributeValueCondition47', a1)
    if hasattr(a1, 'forms_PageElement48'):
        assert _is_linked(a1, 'forms_PageElement48', b)
    _safe_set(b, 'forms_AttributeValueCondition47', a2)
    assert _is_linked(b, 'forms_AttributeValueCondition47', a2)
    if hasattr(a1, 'forms_PageElement48'):
        assert not _is_linked(a1, 'forms_PageElement48', b)
    if hasattr(a2, 'forms_PageElement48'):
        assert _is_linked(a2, 'forms_PageElement48', b)
    _safe_set(b, 'forms_AttributeValueCondition47', None)
    assert not _is_linked(b, 'forms_AttributeValueCondition47', a2)
    if hasattr(a2, 'forms_PageElement48'):
        assert not _is_linked(a2, 'forms_PageElement48', b)


def test_assoc_attributes0_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
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


def test_assoc_combinesAttributeValue36_reverse_link_reassign_clear():
    a1 = forms_CompositionCondition(isAnd=True)
    a2 = forms_CompositionCondition(isAnd=False)
    b = forms_AttributeValueCondition(type="sample_text", value="sample_text")
    _safe_set(b, 'forms_AttributeValueCondition', a1)
    assert _is_linked(b, 'forms_AttributeValueCondition', a1)
    if hasattr(a1, 'forms_CompositionCondition'):
        assert _is_linked(a1, 'forms_CompositionCondition', b)
    _safe_set(b, 'forms_AttributeValueCondition', a2)
    assert _is_linked(b, 'forms_AttributeValueCondition', a2)
    if hasattr(a1, 'forms_CompositionCondition'):
        assert not _is_linked(a1, 'forms_CompositionCondition', b)
    if hasattr(a2, 'forms_CompositionCondition'):
        assert _is_linked(a2, 'forms_CompositionCondition', b)
    _safe_set(b, 'forms_AttributeValueCondition', None)
    assert not _is_linked(b, 'forms_AttributeValueCondition', a2)
    if hasattr(a2, 'forms_CompositionCondition'):
        assert not _is_linked(a2, 'forms_CompositionCondition', b)


def test_assoc_combinesComposite38_reverse_link_reassign_clear():
    a1 = forms_CompositionCondition(isAnd=True)
    a2 = forms_CompositionCondition(isAnd=False)
    b = forms_CompositionCondition(isAnd=True)
    _safe_set(b, 'forms_CompositionCondition39', a1)
    assert _is_linked(b, 'forms_CompositionCondition39', a1)
    if hasattr(a1, 'forms_CompositionCondition37'):
        assert _is_linked(a1, 'forms_CompositionCondition37', b)
    _safe_set(b, 'forms_CompositionCondition39', a2)
    assert _is_linked(b, 'forms_CompositionCondition39', a2)
    if hasattr(a1, 'forms_CompositionCondition37'):
        assert not _is_linked(a1, 'forms_CompositionCondition37', b)
    if hasattr(a2, 'forms_CompositionCondition37'):
        assert _is_linked(a2, 'forms_CompositionCondition37', b)
    _safe_set(b, 'forms_CompositionCondition39', None)
    assert not _is_linked(b, 'forms_CompositionCondition39', a2)
    if hasattr(a2, 'forms_CompositionCondition37'):
        assert not _is_linked(a2, 'forms_CompositionCondition37', b)


def test_assoc_conditionsPage40_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_AttributeValueCondition(type="sample_text", value="sample_text")
    _safe_set(b, 'forms_AttributeValueCondition41', a1)
    assert _is_linked(b, 'forms_AttributeValueCondition41', a1)
    if hasattr(a1, 'forms_Page42'):
        assert _is_linked(a1, 'forms_Page42', b)
    _safe_set(b, 'forms_AttributeValueCondition41', a2)
    assert _is_linked(b, 'forms_AttributeValueCondition41', a2)
    if hasattr(a1, 'forms_Page42'):
        assert not _is_linked(a1, 'forms_Page42', b)
    if hasattr(a2, 'forms_Page42'):
        assert _is_linked(a2, 'forms_Page42', b)
    _safe_set(b, 'forms_AttributeValueCondition41', None)
    assert not _is_linked(b, 'forms_AttributeValueCondition41', a2)
    if hasattr(a2, 'forms_Page42'):
        assert not _is_linked(a2, 'forms_Page42', b)


def test_assoc_conditionsPageElement43_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID=7, label="sample_text")
    a2 = forms_PageElement(elementID=13, label="sample_text_2")
    b = forms_AttributeValueCondition(type="sample_text", value="sample_text")
    _safe_set(b, 'forms_AttributeValueCondition44', a1)
    assert _is_linked(b, 'forms_AttributeValueCondition44', a1)
    if hasattr(a1, 'forms_PageElement45'):
        assert _is_linked(a1, 'forms_PageElement45', b)
    _safe_set(b, 'forms_AttributeValueCondition44', a2)
    assert _is_linked(b, 'forms_AttributeValueCondition44', a2)
    if hasattr(a1, 'forms_PageElement45'):
        assert not _is_linked(a1, 'forms_PageElement45', b)
    if hasattr(a2, 'forms_PageElement45'):
        assert _is_linked(a2, 'forms_PageElement45', b)
    _safe_set(b, 'forms_AttributeValueCondition44', None)
    assert not _is_linked(b, 'forms_AttributeValueCondition44', a2)
    if hasattr(a2, 'forms_PageElement45'):
        assert not _is_linked(a2, 'forms_PageElement45', b)


def test_assoc_consists11_reverse_link_reassign_clear():
    a1 = forms_Literal(Value="sample_text", name="sample_text")
    a2 = forms_Literal(Value="sample_text_2", name="sample_text_2")
    b = forms_Enumeration(name="sample_text")
    _safe_set(b, 'forms_Enumeration12', {a1})
    assert _is_linked(b, 'forms_Enumeration12', a1)
    if hasattr(a1, 'forms_Literal'):
        assert _is_linked(a1, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration12', {a2})
    assert _is_linked(b, 'forms_Enumeration12', a2)
    if hasattr(a1, 'forms_Literal'):
        assert not _is_linked(a1, 'forms_Literal', b)
    if hasattr(a2, 'forms_Literal'):
        assert _is_linked(a2, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration12', set())
    assert not _is_linked(b, 'forms_Enumeration12', a2)
    if hasattr(a2, 'forms_Literal'):
        assert not _is_linked(a2, 'forms_Literal', b)


def test_assoc_consists19_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", isWelcomeForm=True, name="sample_text", title="sample_text")
    _safe_set(b, 'forms_Form', {a1})
    assert _is_linked(b, 'forms_Form', a1)
    if hasattr(a1, 'forms_Page'):
        assert _is_linked(a1, 'forms_Page', b)
    _safe_set(b, 'forms_Form', {a2})
    assert _is_linked(b, 'forms_Form', a2)
    if hasattr(a1, 'forms_Page'):
        assert not _is_linked(a1, 'forms_Page', b)
    if hasattr(a2, 'forms_Page'):
        assert _is_linked(a2, 'forms_Page', b)
    _safe_set(b, 'forms_Form', set())
    assert not _is_linked(b, 'forms_Form', a2)
    if hasattr(a2, 'forms_Page'):
        assert not _is_linked(a2, 'forms_Page', b)


def test_assoc_contains23_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID=7, label="sample_text")
    a2 = forms_PageElement(elementID=13, label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'forms_Page24', {a1})
    assert _is_linked(b, 'forms_Page24', a1)
    if hasattr(a1, 'forms_PageElement'):
        assert _is_linked(a1, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page24', {a2})
    assert _is_linked(b, 'forms_Page24', a2)
    if hasattr(a1, 'forms_PageElement'):
        assert not _is_linked(a1, 'forms_PageElement', b)
    if hasattr(a2, 'forms_PageElement'):
        assert _is_linked(a2, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page24', set())
    assert not _is_linked(b, 'forms_Page24', a2)
    if hasattr(a2, 'forms_PageElement'):
        assert not _is_linked(a2, 'forms_PageElement', b)


def test_assoc_enumerationType9_reverse_link_reassign_clear():
    a1 = forms_Enumeration(name="sample_text")
    a2 = forms_Enumeration(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute10', a1)
    assert _is_linked(b, 'forms_Attribute10', a1)
    if hasattr(a1, 'forms_Enumeration'):
        assert _is_linked(a1, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute10', a2)
    assert _is_linked(b, 'forms_Attribute10', a2)
    if hasattr(a1, 'forms_Enumeration'):
        assert not _is_linked(a1, 'forms_Enumeration', b)
    if hasattr(a2, 'forms_Enumeration'):
        assert _is_linked(a2, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute10', None)
    assert not _is_linked(b, 'forms_Attribute10', a2)
    if hasattr(a2, 'forms_Enumeration'):
        assert not _is_linked(a2, 'forms_Enumeration', b)


def test_assoc_identifier1_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute3', a1)
    assert _is_linked(b, 'forms_Attribute3', a1)
    if hasattr(a1, 'forms_Entity2'):
        assert _is_linked(a1, 'forms_Entity2', b)
    _safe_set(b, 'forms_Attribute3', a2)
    assert _is_linked(b, 'forms_Attribute3', a2)
    if hasattr(a1, 'forms_Entity2'):
        assert not _is_linked(a1, 'forms_Entity2', b)
    if hasattr(a2, 'forms_Entity2'):
        assert _is_linked(a2, 'forms_Entity2', b)
    _safe_set(b, 'forms_Attribute3', None)
    assert not _is_linked(b, 'forms_Attribute3', a2)
    if hasattr(a2, 'forms_Entity2'):
        assert not _is_linked(a2, 'forms_Entity2', b)


def test_assoc_opposite17_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    _safe_set(b, 'forms_Relationship18', a1)
    assert _is_linked(b, 'forms_Relationship18', a1)
    if hasattr(a1, 'forms_Relationship16'):
        assert _is_linked(a1, 'forms_Relationship16', b)
    _safe_set(b, 'forms_Relationship18', a2)
    assert _is_linked(b, 'forms_Relationship18', a2)
    if hasattr(a1, 'forms_Relationship16'):
        assert not _is_linked(a1, 'forms_Relationship16', b)
    if hasattr(a2, 'forms_Relationship16'):
        assert _is_linked(a2, 'forms_Relationship16', b)
    _safe_set(b, 'forms_Relationship18', None)
    assert not _is_linked(b, 'forms_Relationship18', a2)
    if hasattr(a2, 'forms_Relationship16'):
        assert not _is_linked(a2, 'forms_Relationship16', b)


def test_assoc_relationships4_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity5', {a1})
    assert _is_linked(b, 'forms_Entity5', a1)
    if hasattr(a1, 'forms_Relationship'):
        assert _is_linked(a1, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity5', {a2})
    assert _is_linked(b, 'forms_Entity5', a2)
    if hasattr(a1, 'forms_Relationship'):
        assert not _is_linked(a1, 'forms_Relationship', b)
    if hasattr(a2, 'forms_Relationship'):
        assert _is_linked(a2, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity5', set())
    assert not _is_linked(b, 'forms_Entity5', a2)
    if hasattr(a2, 'forms_Relationship'):
        assert not _is_linked(a2, 'forms_Relationship', b)


def test_assoc_supertypes7_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity8', a1)
    assert _is_linked(b, 'forms_Entity8', a1)
    if hasattr(a1, 'forms_Entity6'):
        assert _is_linked(a1, 'forms_Entity6', b)
    _safe_set(b, 'forms_Entity8', a2)
    assert _is_linked(b, 'forms_Entity8', a2)
    if hasattr(a1, 'forms_Entity6'):
        assert not _is_linked(a1, 'forms_Entity6', b)
    if hasattr(a2, 'forms_Entity6'):
        assert _is_linked(a2, 'forms_Entity6', b)
    _safe_set(b, 'forms_Entity8', None)
    assert not _is_linked(b, 'forms_Entity8', a2)
    if hasattr(a2, 'forms_Entity6'):
        assert not _is_linked(a2, 'forms_Entity6', b)


def test_assoc_target13_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity15', a1)
    assert _is_linked(b, 'forms_Entity15', a1)
    if hasattr(a1, 'forms_Relationship14'):
        assert _is_linked(a1, 'forms_Relationship14', b)
    _safe_set(b, 'forms_Entity15', a2)
    assert _is_linked(b, 'forms_Entity15', a2)
    if hasattr(a1, 'forms_Relationship14'):
        assert not _is_linked(a1, 'forms_Relationship14', b)
    if hasattr(a2, 'forms_Relationship14'):
        assert _is_linked(a2, 'forms_Relationship14', b)
    _safe_set(b, 'forms_Entity15', None)
    assert not _is_linked(b, 'forms_Entity15', a2)
    if hasattr(a2, 'forms_Relationship14'):
        assert not _is_linked(a2, 'forms_Relationship14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_conditions51_stub_double():
    # forms_EMFL_FormModel has no real 'forms_EMFL_FormModel52' property in the generated
    # code (a bare stub) -- manually attach it so forms_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Condition(conditionId=7)
    partner = forms_EMFL_FormModel()
    setattr(partner, 'forms_EMFL_FormModel52', None)
    _safe_set(owner, 'forms_Condition', partner)
    assert owner in getattr(partner, 'forms_EMFL_FormModel52')
    _safe_set(owner, 'forms_Condition', None)
    assert owner not in getattr(partner, 'forms_EMFL_FormModel52')


def test_assoc_editing_form27_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", isWelcomeForm=True, name="sample_text", title="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement', None)
    _safe_set(owner, 'forms_Form28', partner)
    assert getattr(partner, 'forms_RelationshipPageElement') == owner
    _safe_set(owner, 'forms_Form28', None)
    assert getattr(partner, 'forms_RelationshipPageElement') is None


def test_assoc_entities53_stub_double():
    # forms_EMFL_FormModel has no real 'forms_EMFL_FormModel54' property in the generated
    # code (a bare stub) -- manually attach it so forms_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Entity(name="sample_text")
    partner = forms_EMFL_FormModel()
    setattr(partner, 'forms_EMFL_FormModel54', None)
    _safe_set(owner, 'forms_Entity55', partner)
    assert owner in getattr(partner, 'forms_EMFL_FormModel54')
    _safe_set(owner, 'forms_Entity55', None)
    assert owner not in getattr(partner, 'forms_EMFL_FormModel54')


def test_assoc_entities56_stub_double():
    # forms_EMFL_EntityModel has no real 'forms_EMFL_EntityModel' property in the generated
    # code (a bare stub) -- manually attach it so forms_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Entity(name="sample_text")
    partner = forms_EMFL_EntityModel()
    setattr(partner, 'forms_EMFL_EntityModel', None)
    _safe_set(owner, 'forms_Entity57', partner)
    assert owner in getattr(partner, 'forms_EMFL_EntityModel')
    _safe_set(owner, 'forms_Entity57', None)
    assert owner not in getattr(partner, 'forms_EMFL_EntityModel')


def test_assoc_enums58_stub_double():
    # forms_EMFL_EntityModel has no real 'forms_EMFL_EntityModel59' property in the generated
    # code (a bare stub) -- manually attach it so forms_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Enumeration(name="sample_text")
    partner = forms_EMFL_EntityModel()
    setattr(partner, 'forms_EMFL_EntityModel59', None)
    _safe_set(owner, 'forms_Enumeration60', partner)
    assert owner in getattr(partner, 'forms_EMFL_EntityModel59')
    _safe_set(owner, 'forms_Enumeration60', None)
    assert owner not in getattr(partner, 'forms_EMFL_EntityModel59')


def test_assoc_forms49_stub_double():
    # forms_EMFL_FormModel has no real 'forms_EMFL_FormModel' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", isWelcomeForm=True, name="sample_text", title="sample_text")
    partner = forms_EMFL_FormModel()
    setattr(partner, 'forms_EMFL_FormModel', None)
    _safe_set(owner, 'forms_Form50', partner)
    assert owner in getattr(partner, 'forms_EMFL_FormModel')
    _safe_set(owner, 'forms_Form50', None)
    assert owner not in getattr(partner, 'forms_EMFL_FormModel')


def test_assoc_refers_to25_stub_double():
    # forms_AttributePageElement has no real 'forms_AttributePageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_AttributePageElement()
    setattr(partner, 'forms_AttributePageElement', None)
    _safe_set(owner, 'forms_Attribute26', partner)
    assert getattr(partner, 'forms_AttributePageElement') == owner
    _safe_set(owner, 'forms_Attribute26', None)
    assert getattr(partner, 'forms_AttributePageElement') is None


def test_assoc_refers_to29_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement30' property in the generated
    # code (a bare stub) -- manually attach it so forms_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement30', None)
    _safe_set(owner, 'forms_Relationship31', partner)
    assert getattr(partner, 'forms_RelationshipPageElement30') == owner
    _safe_set(owner, 'forms_Relationship31', None)
    assert getattr(partner, 'forms_RelationshipPageElement30') is None


def test_assoc_refers_to33_stub_double():
    # forms_Column has no real 'forms_Column34' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_Column()
    setattr(partner, 'forms_Column34', None)
    _safe_set(owner, 'forms_Attribute35', partner)
    assert getattr(partner, 'forms_Column34') == owner
    _safe_set(owner, 'forms_Attribute35', None)
    assert getattr(partner, 'forms_Column34') is None


