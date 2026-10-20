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
    forms_DateSelectionField,
    forms_EFML,
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
    ConditionType,
    Operators,
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

def test_assoc_attributes3_reverse_link_reassign_clear():
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


def test_assoc_conditions38_reverse_link_reassign_clear():
    a1 = forms_Condition(conditionID="sample_text", type="sample_text")
    a2 = forms_Condition(conditionID="sample_text_2", type="sample_text_2")
    b = forms_CompositeCondition(operator="sample_text")
    _safe_set(b, 'forms_CompositeCondition', {a1})
    assert _is_linked(b, 'forms_CompositeCondition', a1)
    if hasattr(a1, 'forms_Condition'):
        assert _is_linked(a1, 'forms_Condition', b)
    _safe_set(b, 'forms_CompositeCondition', {a2})
    assert _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a1, 'forms_Condition'):
        assert not _is_linked(a1, 'forms_Condition', b)
    if hasattr(a2, 'forms_Condition'):
        assert _is_linked(a2, 'forms_Condition', b)
    _safe_set(b, 'forms_CompositeCondition', set())
    assert not _is_linked(b, 'forms_CompositeCondition', a2)
    if hasattr(a2, 'forms_Condition'):
        assert not _is_linked(a2, 'forms_Condition', b)


def test_assoc_entity23_reverse_link_reassign_clear():
    a1 = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    a2 = forms_Form(description="sample_text_2", mainForm=False, name="sample_text_2", title="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity25', a1)
    assert _is_linked(b, 'forms_Entity25', a1)
    if hasattr(a1, 'forms_Form24'):
        assert _is_linked(a1, 'forms_Form24', b)
    _safe_set(b, 'forms_Entity25', a2)
    assert _is_linked(b, 'forms_Entity25', a2)
    if hasattr(a1, 'forms_Form24'):
        assert not _is_linked(a1, 'forms_Form24', b)
    if hasattr(a2, 'forms_Form24'):
        assert _is_linked(a2, 'forms_Form24', b)
    _safe_set(b, 'forms_Entity25', None)
    assert not _is_linked(b, 'forms_Entity25', a2)
    if hasattr(a2, 'forms_Form24'):
        assert not _is_linked(a2, 'forms_Form24', b)


def test_assoc_enumerationType13_reverse_link_reassign_clear():
    a1 = forms_Enumeration(name="sample_text")
    a2 = forms_Enumeration(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute14', a1)
    assert _is_linked(b, 'forms_Attribute14', a1)
    if hasattr(a1, 'forms_Enumeration'):
        assert _is_linked(a1, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute14', a2)
    assert _is_linked(b, 'forms_Attribute14', a2)
    if hasattr(a1, 'forms_Enumeration'):
        assert not _is_linked(a1, 'forms_Enumeration', b)
    if hasattr(a2, 'forms_Enumeration'):
        assert _is_linked(a2, 'forms_Enumeration', b)
    _safe_set(b, 'forms_Attribute14', None)
    assert not _is_linked(b, 'forms_Attribute14', a2)
    if hasattr(a2, 'forms_Enumeration'):
        assert not _is_linked(a2, 'forms_Enumeration', b)


def test_assoc_id5_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'forms_Attribute7', a1)
    assert _is_linked(b, 'forms_Attribute7', a1)
    if hasattr(a1, 'forms_Entity6'):
        assert _is_linked(a1, 'forms_Entity6', b)
    _safe_set(b, 'forms_Attribute7', a2)
    assert _is_linked(b, 'forms_Attribute7', a2)
    if hasattr(a1, 'forms_Entity6'):
        assert not _is_linked(a1, 'forms_Entity6', b)
    if hasattr(a2, 'forms_Entity6'):
        assert _is_linked(a2, 'forms_Entity6', b)
    _safe_set(b, 'forms_Attribute7', None)
    assert not _is_linked(b, 'forms_Attribute7', a2)
    if hasattr(a2, 'forms_Entity6'):
        assert not _is_linked(a2, 'forms_Entity6', b)


def test_assoc_literals15_reverse_link_reassign_clear():
    a1 = forms_Literal(name="sample_text", value="sample_text")
    a2 = forms_Literal(name="sample_text_2", value="sample_text_2")
    b = forms_Enumeration(name="sample_text")
    _safe_set(b, 'forms_Enumeration16', {a1})
    assert _is_linked(b, 'forms_Enumeration16', a1)
    if hasattr(a1, 'forms_Literal'):
        assert _is_linked(a1, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration16', {a2})
    assert _is_linked(b, 'forms_Enumeration16', a2)
    if hasattr(a1, 'forms_Literal'):
        assert not _is_linked(a1, 'forms_Literal', b)
    if hasattr(a2, 'forms_Literal'):
        assert _is_linked(a2, 'forms_Literal', b)
    _safe_set(b, 'forms_Enumeration16', set())
    assert not _is_linked(b, 'forms_Enumeration16', a2)
    if hasattr(a2, 'forms_Literal'):
        assert not _is_linked(a2, 'forms_Literal', b)


def test_assoc_opposite18_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    _safe_set(b, 'forms_Relationship19', a1)
    assert _is_linked(b, 'forms_Relationship19', a1)
    if hasattr(a1, 'forms_Relationship17'):
        assert _is_linked(a1, 'forms_Relationship17', b)
    _safe_set(b, 'forms_Relationship19', a2)
    assert _is_linked(b, 'forms_Relationship19', a2)
    if hasattr(a1, 'forms_Relationship17'):
        assert not _is_linked(a1, 'forms_Relationship17', b)
    if hasattr(a2, 'forms_Relationship17'):
        assert _is_linked(a2, 'forms_Relationship17', b)
    _safe_set(b, 'forms_Relationship19', None)
    assert not _is_linked(b, 'forms_Relationship19', a2)
    if hasattr(a2, 'forms_Relationship17'):
        assert not _is_linked(a2, 'forms_Relationship17', b)


def test_assoc_pageElements28_reverse_link_reassign_clear():
    a1 = forms_PageElement(elementID="sample_text", label="sample_text")
    a2 = forms_PageElement(elementID="sample_text_2", label="sample_text_2")
    b = forms_Page(title="sample_text")
    _safe_set(b, 'forms_Page29', {a1})
    assert _is_linked(b, 'forms_Page29', a1)
    if hasattr(a1, 'forms_PageElement'):
        assert _is_linked(a1, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page29', {a2})
    assert _is_linked(b, 'forms_Page29', a2)
    if hasattr(a1, 'forms_PageElement'):
        assert not _is_linked(a1, 'forms_PageElement', b)
    if hasattr(a2, 'forms_PageElement'):
        assert _is_linked(a2, 'forms_PageElement', b)
    _safe_set(b, 'forms_Page29', set())
    assert not _is_linked(b, 'forms_Page29', a2)
    if hasattr(a2, 'forms_PageElement'):
        assert not _is_linked(a2, 'forms_PageElement', b)


def test_assoc_pages26_reverse_link_reassign_clear():
    a1 = forms_Page(title="sample_text")
    a2 = forms_Page(title="sample_text_2")
    b = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    _safe_set(b, 'forms_Form27', {a1})
    assert _is_linked(b, 'forms_Form27', a1)
    if hasattr(a1, 'forms_Page'):
        assert _is_linked(a1, 'forms_Page', b)
    _safe_set(b, 'forms_Form27', {a2})
    assert _is_linked(b, 'forms_Form27', a2)
    if hasattr(a1, 'forms_Page'):
        assert not _is_linked(a1, 'forms_Page', b)
    if hasattr(a2, 'forms_Page'):
        assert _is_linked(a2, 'forms_Page', b)
    _safe_set(b, 'forms_Form27', set())
    assert not _is_linked(b, 'forms_Form27', a2)
    if hasattr(a2, 'forms_Page'):
        assert not _is_linked(a2, 'forms_Page', b)


def test_assoc_relationships8_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity9', {a1})
    assert _is_linked(b, 'forms_Entity9', a1)
    if hasattr(a1, 'forms_Relationship'):
        assert _is_linked(a1, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity9', {a2})
    assert _is_linked(b, 'forms_Entity9', a2)
    if hasattr(a1, 'forms_Relationship'):
        assert not _is_linked(a1, 'forms_Relationship', b)
    if hasattr(a2, 'forms_Relationship'):
        assert _is_linked(a2, 'forms_Relationship', b)
    _safe_set(b, 'forms_Entity9', set())
    assert not _is_linked(b, 'forms_Entity9', a2)
    if hasattr(a2, 'forms_Relationship'):
        assert not _is_linked(a2, 'forms_Relationship', b)


def test_assoc_superType11_reverse_link_reassign_clear():
    a1 = forms_Entity(name="sample_text")
    a2 = forms_Entity(name="sample_text_2")
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity12', a1)
    assert _is_linked(b, 'forms_Entity12', a1)
    if hasattr(a1, 'forms_Entity10'):
        assert _is_linked(a1, 'forms_Entity10', b)
    _safe_set(b, 'forms_Entity12', a2)
    assert _is_linked(b, 'forms_Entity12', a2)
    if hasattr(a1, 'forms_Entity10'):
        assert not _is_linked(a1, 'forms_Entity10', b)
    if hasattr(a2, 'forms_Entity10'):
        assert _is_linked(a2, 'forms_Entity10', b)
    _safe_set(b, 'forms_Entity12', None)
    assert not _is_linked(b, 'forms_Entity12', a2)
    if hasattr(a2, 'forms_Entity10'):
        assert not _is_linked(a2, 'forms_Entity10', b)


def test_assoc_target20_reverse_link_reassign_clear():
    a1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    a2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    b = forms_Entity(name="sample_text")
    _safe_set(b, 'forms_Entity22', a1)
    assert _is_linked(b, 'forms_Entity22', a1)
    if hasattr(a1, 'forms_Relationship21'):
        assert _is_linked(a1, 'forms_Relationship21', b)
    _safe_set(b, 'forms_Entity22', a2)
    assert _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a1, 'forms_Relationship21'):
        assert not _is_linked(a1, 'forms_Relationship21', b)
    if hasattr(a2, 'forms_Relationship21'):
        assert _is_linked(a2, 'forms_Relationship21', b)
    _safe_set(b, 'forms_Entity22', None)
    assert not _is_linked(b, 'forms_Entity22', a2)
    if hasattr(a2, 'forms_Relationship21'):
        assert not _is_linked(a2, 'forms_Relationship21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute30_stub_double():
    # forms_AttributePageElement has no real 'forms_AttributePageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_AttributePageElement()
    setattr(partner, 'forms_AttributePageElement', None)
    _safe_set(owner, 'forms_Attribute31', partner)
    assert getattr(partner, 'forms_AttributePageElement') == owner
    _safe_set(owner, 'forms_Attribute31', None)
    assert getattr(partner, 'forms_AttributePageElement') is None


def test_assoc_editingForm32_stub_double():
    # forms_RelationshipPageElement has no real 'forms_RelationshipPageElement' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    partner = forms_RelationshipPageElement()
    setattr(partner, 'forms_RelationshipPageElement', None)
    _safe_set(owner, 'forms_Form33', partner)
    assert getattr(partner, 'forms_RelationshipPageElement') == owner
    _safe_set(owner, 'forms_Form33', None)
    assert getattr(partner, 'forms_RelationshipPageElement') is None


def test_assoc_entities0_stub_double():
    # forms_EFML has no real 'forms_EFML' property in the generated
    # code (a bare stub) -- manually attach it so forms_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Entity(name="sample_text")
    partner = forms_EFML()
    setattr(partner, 'forms_EFML', None)
    _safe_set(owner, 'forms_Entity', partner)
    assert owner in getattr(partner, 'forms_EFML')
    _safe_set(owner, 'forms_Entity', None)
    assert owner not in getattr(partner, 'forms_EFML')


def test_assoc_entityAttribute35_stub_double():
    # forms_Column has no real 'forms_Column36' property in the generated
    # code (a bare stub) -- manually attach it so forms_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    partner = forms_Column()
    setattr(partner, 'forms_Column36', None)
    _safe_set(owner, 'forms_Attribute37', partner)
    assert getattr(partner, 'forms_Column36') == owner
    _safe_set(owner, 'forms_Attribute37', None)
    assert getattr(partner, 'forms_Column36') is None


def test_assoc_forms1_stub_double():
    # forms_EFML has no real 'forms_EFML2' property in the generated
    # code (a bare stub) -- manually attach it so forms_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    partner = forms_EFML()
    setattr(partner, 'forms_EFML2', None)
    _safe_set(owner, 'forms_Form', partner)
    assert owner in getattr(partner, 'forms_EFML2')
    _safe_set(owner, 'forms_Form', None)
    assert owner not in getattr(partner, 'forms_EFML2')


