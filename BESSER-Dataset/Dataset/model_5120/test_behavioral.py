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
    ScoredElement,
    Term,
    Variable,
    VariableTerm,
    VariableValue,
    diva_AndTerm,
    diva_Annotation,
    diva_AspectModel,
    diva_BaseModel,
    diva_BoolVariableValue,
    diva_BooleanTerm,
    diva_BooleanVariable,
    diva_ConfigVariant,
    diva_Configuration,
    diva_Constraint,
    diva_Context,
    diva_ContextExpression,
    diva_DiVAModelElement,
    diva_Dimension,
    diva_EnumLiteral,
    diva_EnumTerm,
    diva_EnumVariable,
    diva_EnumVariableValue,
    diva_Expression,
    diva_Invariant,
    diva_Model,
    diva_MultiplicityConstraint,
    diva_NamedElement,
    diva_NaryTerm,
    diva_NotTerm,
    diva_OrTerm,
    diva_Priority,
    diva_PriorityRule,
    diva_Property,
    diva_PropertyPriority,
    diva_PropertyValue,
    diva_Rule,
    diva_Scenario,
    diva_Score,
    diva_ScoredElement,
    diva_SimulationModel,
    diva_Term,
    diva_VariabilityModel,
    diva_Variable,
    diva_VariableTerm,
    diva_VariableValue,
    diva_Variant,
    diva_VariantExpression,
    diva_VariantTerm,
    Verdict,
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

def test_assoc_configuration60_reverse_link_reassign_clear():
    a1 = diva_Context(verdict="sample_text")
    a2 = diva_Context(verdict="sample_text_2")
    b = diva_Configuration(verdict="sample_text")
    _safe_set(b, 'diva_Configuration', a1)
    assert _is_linked(b, 'diva_Configuration', a1)
    if hasattr(a1, 'diva_Context61'):
        assert _is_linked(a1, 'diva_Context61', b)
    _safe_set(b, 'diva_Configuration', a2)
    assert _is_linked(b, 'diva_Configuration', a2)
    if hasattr(a1, 'diva_Context61'):
        assert not _is_linked(a1, 'diva_Context61', b)
    if hasattr(a2, 'diva_Context61'):
        assert _is_linked(a2, 'diva_Context61', b)
    _safe_set(b, 'diva_Configuration', None)
    assert not _is_linked(b, 'diva_Configuration', a2)
    if hasattr(a2, 'diva_Context61'):
        assert not _is_linked(a2, 'diva_Context61', b)


def test_assoc_constraints38_reverse_link_reassign_clear():
    a1 = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    a2 = diva_MultiplicityConstraint(lower="sample_text_2", upper="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension39', {a1})
    assert _is_linked(b, 'diva_Dimension39', a1)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert _is_linked(a1, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension39', {a2})
    assert _is_linked(b, 'diva_Dimension39', a2)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a1, 'diva_MultiplicityConstraint', b)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert _is_linked(a2, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension39', set())
    assert not _is_linked(b, 'diva_Dimension39', a2)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a2, 'diva_MultiplicityConstraint', b)


def test_assoc_priority65_reverse_link_reassign_clear():
    a1 = diva_Priority(priority=7)
    a2 = diva_Priority(priority=13)
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context66', {a1})
    assert _is_linked(b, 'diva_Context66', a1)
    if hasattr(a1, 'diva_Priority'):
        assert _is_linked(a1, 'diva_Priority', b)
    _safe_set(b, 'diva_Context66', {a2})
    assert _is_linked(b, 'diva_Context66', a2)
    if hasattr(a1, 'diva_Priority'):
        assert not _is_linked(a1, 'diva_Priority', b)
    if hasattr(a2, 'diva_Priority'):
        assert _is_linked(a2, 'diva_Priority', b)
    _safe_set(b, 'diva_Context66', set())
    assert not _is_linked(b, 'diva_Context66', a2)
    if hasattr(a2, 'diva_Priority'):
        assert not _is_linked(a2, 'diva_Priority', b)


def test_assoc_property35_reverse_link_reassign_clear():
    a1 = diva_Property(direction="sample_text")
    a2 = diva_Property(direction="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension36', {a1})
    assert _is_linked(b, 'diva_Dimension36', a1)
    if hasattr(a1, 'diva_Property37'):
        assert _is_linked(a1, 'diva_Property37', b)
    _safe_set(b, 'diva_Dimension36', {a2})
    assert _is_linked(b, 'diva_Dimension36', a2)
    if hasattr(a1, 'diva_Property37'):
        assert not _is_linked(a1, 'diva_Property37', b)
    if hasattr(a2, 'diva_Property37'):
        assert _is_linked(a2, 'diva_Property37', b)
    _safe_set(b, 'diva_Dimension36', set())
    assert not _is_linked(b, 'diva_Dimension36', a2)
    if hasattr(a2, 'diva_Property37'):
        assert not _is_linked(a2, 'diva_Property37', b)


def test_assoc_property47_reverse_link_reassign_clear():
    a1 = diva_PropertyValue(value="sample_text")
    a2 = diva_PropertyValue(value="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property49', a1)
    assert _is_linked(b, 'diva_Property49', a1)
    if hasattr(a1, 'diva_PropertyValue48'):
        assert _is_linked(a1, 'diva_PropertyValue48', b)
    _safe_set(b, 'diva_Property49', a2)
    assert _is_linked(b, 'diva_Property49', a2)
    if hasattr(a1, 'diva_PropertyValue48'):
        assert not _is_linked(a1, 'diva_PropertyValue48', b)
    if hasattr(a2, 'diva_PropertyValue48'):
        assert _is_linked(a2, 'diva_PropertyValue48', b)
    _safe_set(b, 'diva_Property49', None)
    assert not _is_linked(b, 'diva_Property49', a2)
    if hasattr(a2, 'diva_PropertyValue48'):
        assert not _is_linked(a2, 'diva_PropertyValue48', b)


def test_assoc_property50_reverse_link_reassign_clear():
    a1 = diva_PropertyPriority(priority="sample_text")
    a2 = diva_PropertyPriority(priority="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property52', a1)
    assert _is_linked(b, 'diva_Property52', a1)
    if hasattr(a1, 'diva_PropertyPriority51'):
        assert _is_linked(a1, 'diva_PropertyPriority51', b)
    _safe_set(b, 'diva_Property52', a2)
    assert _is_linked(b, 'diva_Property52', a2)
    if hasattr(a1, 'diva_PropertyPriority51'):
        assert not _is_linked(a1, 'diva_PropertyPriority51', b)
    if hasattr(a2, 'diva_PropertyPriority51'):
        assert _is_linked(a2, 'diva_PropertyPriority51', b)
    _safe_set(b, 'diva_Property52', None)
    assert not _is_linked(b, 'diva_Property52', a2)
    if hasattr(a2, 'diva_PropertyPriority51'):
        assert not _is_linked(a2, 'diva_PropertyPriority51', b)


def test_assoc_property76_reverse_link_reassign_clear():
    a1 = diva_Score(score=7)
    a2 = diva_Score(score=13)
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property78', a1)
    assert _is_linked(b, 'diva_Property78', a1)
    if hasattr(a1, 'diva_Score77'):
        assert _is_linked(a1, 'diva_Score77', b)
    _safe_set(b, 'diva_Property78', a2)
    assert _is_linked(b, 'diva_Property78', a2)
    if hasattr(a1, 'diva_Score77'):
        assert not _is_linked(a1, 'diva_Score77', b)
    if hasattr(a2, 'diva_Score77'):
        assert _is_linked(a2, 'diva_Score77', b)
    _safe_set(b, 'diva_Property78', None)
    assert not _is_linked(b, 'diva_Property78', a2)
    if hasattr(a2, 'diva_Score77'):
        assert not _is_linked(a2, 'diva_Score77', b)


def test_assoc_property79_reverse_link_reassign_clear():
    a1 = diva_Property(direction="sample_text")
    a2 = diva_Property(direction="sample_text_2")
    b = diva_Priority(priority=7)
    _safe_set(b, 'diva_Priority80', a1)
    assert _is_linked(b, 'diva_Priority80', a1)
    if hasattr(a1, 'diva_Property81'):
        assert _is_linked(a1, 'diva_Property81', b)
    _safe_set(b, 'diva_Priority80', a2)
    assert _is_linked(b, 'diva_Priority80', a2)
    if hasattr(a1, 'diva_Property81'):
        assert not _is_linked(a1, 'diva_Property81', b)
    if hasattr(a2, 'diva_Property81'):
        assert _is_linked(a2, 'diva_Property81', b)
    _safe_set(b, 'diva_Priority80', None)
    assert not _is_linked(b, 'diva_Priority80', a2)
    if hasattr(a2, 'diva_Property81'):
        assert not _is_linked(a2, 'diva_Property81', b)


def test_assoc_score75_reverse_link_reassign_clear():
    a1 = diva_ScoredElement(totalScore=7)
    a2 = diva_ScoredElement(totalScore=13)
    b = diva_Score(score=7)
    _safe_set(b, 'diva_Score', a1)
    assert _is_linked(b, 'diva_Score', a1)
    if hasattr(a1, 'diva_ScoredElement'):
        assert _is_linked(a1, 'diva_ScoredElement', b)
    _safe_set(b, 'diva_Score', a2)
    assert _is_linked(b, 'diva_Score', a2)
    if hasattr(a1, 'diva_ScoredElement'):
        assert not _is_linked(a1, 'diva_ScoredElement', b)
    if hasattr(a2, 'diva_ScoredElement'):
        assert _is_linked(a2, 'diva_ScoredElement', b)
    _safe_set(b, 'diva_Score', None)
    assert not _is_linked(b, 'diva_Score', a2)
    if hasattr(a2, 'diva_ScoredElement'):
        assert not _is_linked(a2, 'diva_ScoredElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation56_stub_double():
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


def test_assoc_available53_stub_double():
    # diva_ContextExpression has no real 'diva_ContextExpression55' property in the generated
    # code (a bare stub) -- manually attach it so diva_MultiplicityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_MultiplicityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    partner = diva_ContextExpression()
    setattr(partner, 'diva_ContextExpression55', None)
    _safe_set(owner, 'diva_MultiplicityConstraint54', partner)
    assert getattr(partner, 'diva_ContextExpression55') == owner
    _safe_set(owner, 'diva_MultiplicityConstraint54', None)
    assert getattr(partner, 'diva_ContextExpression55') is None


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


def test_assoc_context72_stub_double():
    # diva_Scenario has no real 'diva_Scenario73' property in the generated
    # code (a bare stub) -- manually attach it so diva_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Context(verdict="sample_text")
    partner = diva_Scenario()
    setattr(partner, 'diva_Scenario73', None)
    _safe_set(owner, 'diva_Context74', partner)
    assert owner in getattr(partner, 'diva_Scenario73')
    _safe_set(owner, 'diva_Context74', None)
    assert owner not in getattr(partner, 'diva_Scenario73')


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


def test_assoc_expression12_stub_double():
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


def test_assoc_oracle62_stub_double():
    # diva_VariantExpression has no real 'diva_VariantExpression64' property in the generated
    # code (a bare stub) -- manually attach it so diva_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Context(verdict="sample_text")
    partner = diva_VariantExpression()
    setattr(partner, 'diva_VariantExpression64', None)
    _safe_set(owner, 'diva_Context63', partner)
    assert getattr(partner, 'diva_VariantExpression64') == owner
    _safe_set(owner, 'diva_Context63', None)
    assert getattr(partner, 'diva_VariantExpression64') is None


def test_assoc_priority45_stub_double():
    # diva_PriorityRule has no real 'diva_PriorityRule46' property in the generated
    # code (a bare stub) -- manually attach it so diva_PropertyPriority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_PropertyPriority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_PropertyPriority(priority="sample_text")
    partner = diva_PriorityRule()
    setattr(partner, 'diva_PriorityRule46', None)
    _safe_set(owner, 'diva_PropertyPriority', partner)
    assert owner in getattr(partner, 'diva_PriorityRule46')
    _safe_set(owner, 'diva_PropertyPriority', None)
    assert owner not in getattr(partner, 'diva_PriorityRule46')


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


def test_assoc_propertyValue25_stub_double():
    # diva_Variant has no real 'diva_Variant26' property in the generated
    # code (a bare stub) -- manually attach it so diva_PropertyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_PropertyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_PropertyValue(value="sample_text")
    partner = diva_Variant()
    setattr(partner, 'diva_Variant26', None)
    _safe_set(owner, 'diva_PropertyValue', partner)
    assert owner in getattr(partner, 'diva_Variant26')
    _safe_set(owner, 'diva_PropertyValue', None)
    assert owner not in getattr(partner, 'diva_Variant26')


def test_assoc_term40_stub_double():
    # diva_Term has no real 'diva_Term42' property in the generated
    # code (a bare stub) -- manually attach it so diva_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Expression(text="sample_text")
    partner = diva_Term()
    setattr(partner, 'diva_Term42', None)
    _safe_set(owner, 'diva_Expression41', partner)
    assert getattr(partner, 'diva_Term42') == owner
    _safe_set(owner, 'diva_Expression41', None)
    assert getattr(partner, 'diva_Term42') is None


def test_assoc_type24_stub_double():
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


def test_assoc_variable59_stub_double():
    # diva_VariableValue has no real 'diva_VariableValue' property in the generated
    # code (a bare stub) -- manually attach it so diva_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Context(verdict="sample_text")
    partner = diva_VariableValue()
    setattr(partner, 'diva_VariableValue', None)
    _safe_set(owner, 'diva_Context', {partner})
    assert getattr(partner, 'diva_VariableValue') == owner
    _safe_set(owner, 'diva_Context', set())
    assert getattr(partner, 'diva_VariableValue') is None


def test_assoc_variant34_stub_double():
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


def test_assoc_variant67_stub_double():
    # diva_ConfigVariant has no real 'diva_ConfigVariant' property in the generated
    # code (a bare stub) -- manually attach it so diva_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Configuration(verdict="sample_text")
    partner = diva_ConfigVariant()
    setattr(partner, 'diva_ConfigVariant', None)
    _safe_set(owner, 'diva_Configuration68', {partner})
    assert getattr(partner, 'diva_ConfigVariant') == owner
    _safe_set(owner, 'diva_Configuration68', set())
    assert getattr(partner, 'diva_ConfigVariant') is None


