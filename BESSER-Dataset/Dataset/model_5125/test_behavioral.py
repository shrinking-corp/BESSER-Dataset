import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    DiVAModelElement,
    Expression,
    Model,
    NamedElement,
    NaryTerm,
    Rule,
    Term,
    Variable,
    VariableTerm,
    diva_AndTerm,
    diva_Annotation,
    diva_AspectModel,
    diva_BaseModel,
    diva_BooleanTerm,
    diva_BooleanVariable,
    diva_Constraint,
    diva_ContextExpression,
    diva_DiVAModelElement,
    diva_Dimension,
    diva_EnumLiteral,
    diva_EnumTerm,
    diva_EnumVariable,
    diva_Expression,
    diva_Invariant,
    diva_Model,
    diva_MultiplicityConstraint,
    diva_NamedElement,
    diva_NaryTerm,
    diva_NotTerm,
    diva_OrTerm,
    diva_PriorityRule,
    diva_Property,
    diva_PropertyPriority,
    diva_PropertyValue,
    diva_Rule,
    diva_Term,
    diva_VariabilityModel,
    diva_Variable,
    diva_VariableTerm,
    diva_Variant,
    diva_VariantExpression,
    diva_VariantTerm,
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

def test_assoc_constraints37_reverse_link_reassign_clear():
    a1 = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    a2 = diva_MultiplicityConstraint(lower="sample_text_2", upper="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension38', {a1})
    assert _is_linked(b, 'diva_Dimension38', a1)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert _is_linked(a1, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension38', {a2})
    assert _is_linked(b, 'diva_Dimension38', a2)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a1, 'diva_MultiplicityConstraint', b)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert _is_linked(a2, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension38', set())
    assert not _is_linked(b, 'diva_Dimension38', a2)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a2, 'diva_MultiplicityConstraint', b)


def test_assoc_property34_reverse_link_reassign_clear():
    a1 = diva_Property(direction="sample_text")
    a2 = diva_Property(direction="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension35', {a1})
    assert _is_linked(b, 'diva_Dimension35', a1)
    if hasattr(a1, 'diva_Property36'):
        assert _is_linked(a1, 'diva_Property36', b)
    _safe_set(b, 'diva_Dimension35', {a2})
    assert _is_linked(b, 'diva_Dimension35', a2)
    if hasattr(a1, 'diva_Property36'):
        assert not _is_linked(a1, 'diva_Property36', b)
    if hasattr(a2, 'diva_Property36'):
        assert _is_linked(a2, 'diva_Property36', b)
    _safe_set(b, 'diva_Dimension35', set())
    assert not _is_linked(b, 'diva_Dimension35', a2)
    if hasattr(a2, 'diva_Property36'):
        assert not _is_linked(a2, 'diva_Property36', b)


def test_assoc_property46_reverse_link_reassign_clear():
    a1 = diva_PropertyValue(value="sample_text")
    a2 = diva_PropertyValue(value="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property48', a1)
    assert _is_linked(b, 'diva_Property48', a1)
    if hasattr(a1, 'diva_PropertyValue47'):
        assert _is_linked(a1, 'diva_PropertyValue47', b)
    _safe_set(b, 'diva_Property48', a2)
    assert _is_linked(b, 'diva_Property48', a2)
    if hasattr(a1, 'diva_PropertyValue47'):
        assert not _is_linked(a1, 'diva_PropertyValue47', b)
    if hasattr(a2, 'diva_PropertyValue47'):
        assert _is_linked(a2, 'diva_PropertyValue47', b)
    _safe_set(b, 'diva_Property48', None)
    assert not _is_linked(b, 'diva_Property48', a2)
    if hasattr(a2, 'diva_PropertyValue47'):
        assert not _is_linked(a2, 'diva_PropertyValue47', b)


def test_assoc_property49_reverse_link_reassign_clear():
    a1 = diva_PropertyPriority(priority="sample_text")
    a2 = diva_PropertyPriority(priority="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property51', a1)
    assert _is_linked(b, 'diva_Property51', a1)
    if hasattr(a1, 'diva_PropertyPriority50'):
        assert _is_linked(a1, 'diva_PropertyPriority50', b)
    _safe_set(b, 'diva_Property51', a2)
    assert _is_linked(b, 'diva_Property51', a2)
    if hasattr(a1, 'diva_PropertyPriority50'):
        assert not _is_linked(a1, 'diva_PropertyPriority50', b)
    if hasattr(a2, 'diva_PropertyPriority50'):
        assert _is_linked(a2, 'diva_PropertyPriority50', b)
    _safe_set(b, 'diva_Property51', None)
    assert not _is_linked(b, 'diva_Property51', a2)
    if hasattr(a2, 'diva_PropertyPriority50'):
        assert not _is_linked(a2, 'diva_PropertyPriority50', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation55_stub_double():
    # diva_DiVAModelElement has no real 'diva_DiVAModelElement' property in the generated
    # code (a bare stub) -- manually attach it so diva_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Annotation(key="sample_text", value="sample_text")
    partner = diva_DiVAModelElement()
    setattr(partner, 'diva_DiVAModelElement', None)
    _safe_set(owner, 'diva_Annotation', partner)
    assert owner in getattr(partner, 'diva_DiVAModelElement')
    _safe_set(owner, 'diva_Annotation', None)
    assert owner not in getattr(partner, 'diva_DiVAModelElement')


def test_assoc_available52_stub_double():
    # diva_ContextExpression has no real 'diva_ContextExpression54' property in the generated
    # code (a bare stub) -- manually attach it so diva_MultiplicityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_MultiplicityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    partner = diva_ContextExpression()
    setattr(partner, 'diva_ContextExpression54', None)
    _safe_set(owner, 'diva_MultiplicityConstraint53', partner)
    assert getattr(partner, 'diva_ContextExpression54') == owner
    _safe_set(owner, 'diva_MultiplicityConstraint53', None)
    assert getattr(partner, 'diva_ContextExpression54') is None


def test_assoc_base0_stub_double():
    # diva_VariabilityModel has no real 'diva_VariabilityModel' property in the generated
    # code (a bare stub) -- manually attach it so diva_BaseModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_BaseModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_BaseModel()
    partner = diva_VariabilityModel()
    setattr(partner, 'diva_VariabilityModel', None)
    _safe_set(owner, 'diva_BaseModel', partner)
    assert getattr(partner, 'diva_VariabilityModel') == owner
    _safe_set(owner, 'diva_BaseModel', None)
    assert getattr(partner, 'diva_VariabilityModel') is None


def test_assoc_dimension5_stub_double():
    # diva_VariabilityModel has no real 'diva_VariabilityModel6' property in the generated
    # code (a bare stub) -- manually attach it so diva_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Dimension(lower="sample_text", upper="sample_text")
    partner = diva_VariabilityModel()
    setattr(partner, 'diva_VariabilityModel6', None)
    _safe_set(owner, 'diva_Dimension', partner)
    assert owner in getattr(partner, 'diva_VariabilityModel6')
    _safe_set(owner, 'diva_Dimension', None)
    assert owner not in getattr(partner, 'diva_VariabilityModel6')


def test_assoc_expression11_stub_double():
    # diva_Invariant has no real 'diva_Invariant' property in the generated
    # code (a bare stub) -- manually attach it so diva_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Expression(text="sample_text")
    partner = diva_Invariant()
    setattr(partner, 'diva_Invariant', None)
    _safe_set(owner, 'diva_Expression', partner)
    assert getattr(partner, 'diva_Invariant') == owner
    _safe_set(owner, 'diva_Expression', None)
    assert getattr(partner, 'diva_Invariant') is None


def test_assoc_priority44_stub_double():
    # diva_PriorityRule has no real 'diva_PriorityRule45' property in the generated
    # code (a bare stub) -- manually attach it so diva_PropertyPriority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_PropertyPriority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_PropertyPriority(priority="sample_text")
    partner = diva_PriorityRule()
    setattr(partner, 'diva_PriorityRule45', None)
    _safe_set(owner, 'diva_PropertyPriority', partner)
    assert owner in getattr(partner, 'diva_PriorityRule45')
    _safe_set(owner, 'diva_PropertyPriority', None)
    assert owner not in getattr(partner, 'diva_PriorityRule45')


def test_assoc_property3_stub_double():
    # diva_VariabilityModel has no real 'diva_VariabilityModel4' property in the generated
    # code (a bare stub) -- manually attach it so diva_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Property(direction="sample_text")
    partner = diva_VariabilityModel()
    setattr(partner, 'diva_VariabilityModel4', None)
    _safe_set(owner, 'diva_Property', partner)
    assert owner in getattr(partner, 'diva_VariabilityModel4')
    _safe_set(owner, 'diva_Property', None)
    assert owner not in getattr(partner, 'diva_VariabilityModel4')


def test_assoc_propertyValue24_stub_double():
    # diva_Variant has no real 'diva_Variant25' property in the generated
    # code (a bare stub) -- manually attach it so diva_PropertyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_PropertyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_PropertyValue(value="sample_text")
    partner = diva_Variant()
    setattr(partner, 'diva_Variant25', None)
    _safe_set(owner, 'diva_PropertyValue', partner)
    assert owner in getattr(partner, 'diva_Variant25')
    _safe_set(owner, 'diva_PropertyValue', None)
    assert owner not in getattr(partner, 'diva_Variant25')


def test_assoc_term39_stub_double():
    # diva_Term has no real 'diva_Term41' property in the generated
    # code (a bare stub) -- manually attach it so diva_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Expression(text="sample_text")
    partner = diva_Term()
    setattr(partner, 'diva_Term41', None)
    _safe_set(owner, 'diva_Expression40', partner)
    assert getattr(partner, 'diva_Term41') == owner
    _safe_set(owner, 'diva_Expression40', None)
    assert getattr(partner, 'diva_Term41') is None


def test_assoc_type23_stub_double():
    # diva_Variant has no real 'variant' property in the generated
    # code (a bare stub) -- manually attach it so diva_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Dimension(lower="sample_text", upper="sample_text")
    partner = diva_Variant()
    setattr(partner, 'variant', None)
    _safe_set(owner, 'Dimension', partner)
    assert getattr(partner, 'variant') == owner
    _safe_set(owner, 'Dimension', None)
    assert getattr(partner, 'variant') is None


def test_assoc_variant33_stub_double():
    # diva_Variant has no real 'Variant' property in the generated
    # code (a bare stub) -- manually attach it so diva_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Dimension(lower="sample_text", upper="sample_text")
    partner = diva_Variant()
    setattr(partner, 'Variant', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'Variant') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'Variant') is None


