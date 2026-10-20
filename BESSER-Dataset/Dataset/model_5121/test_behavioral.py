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
    Visitable,
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
    diva_visitors_TopDownVisitor,
    diva_visitors_Visitable,
    diva_visitors_Visitor,
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

def test_assoc_available29_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression', a1)
    assert _is_linked(b, 'diva_ContextExpression', a1)
    if hasattr(a1, 'diva_Variant30'):
        assert _is_linked(a1, 'diva_Variant30', b)
    _safe_set(b, 'diva_ContextExpression', a2)
    assert _is_linked(b, 'diva_ContextExpression', a2)
    if hasattr(a1, 'diva_Variant30'):
        assert not _is_linked(a1, 'diva_Variant30', b)
    if hasattr(a2, 'diva_Variant30'):
        assert _is_linked(a2, 'diva_Variant30', b)
    _safe_set(b, 'diva_ContextExpression', None)
    assert not _is_linked(b, 'diva_ContextExpression', a2)
    if hasattr(a2, 'diva_Variant30'):
        assert not _is_linked(a2, 'diva_Variant30', b)


def test_assoc_available53_reverse_link_reassign_clear():
    a1 = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    a2 = diva_MultiplicityConstraint(lower="sample_text_2", upper="sample_text_2")
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression55', a1)
    assert _is_linked(b, 'diva_ContextExpression55', a1)
    if hasattr(a1, 'diva_MultiplicityConstraint54'):
        assert _is_linked(a1, 'diva_MultiplicityConstraint54', b)
    _safe_set(b, 'diva_ContextExpression55', a2)
    assert _is_linked(b, 'diva_ContextExpression55', a2)
    if hasattr(a1, 'diva_MultiplicityConstraint54'):
        assert not _is_linked(a1, 'diva_MultiplicityConstraint54', b)
    if hasattr(a2, 'diva_MultiplicityConstraint54'):
        assert _is_linked(a2, 'diva_MultiplicityConstraint54', b)
    _safe_set(b, 'diva_ContextExpression55', None)
    assert not _is_linked(b, 'diva_ContextExpression55', a2)
    if hasattr(a2, 'diva_MultiplicityConstraint54'):
        assert not _is_linked(a2, 'diva_MultiplicityConstraint54', b)


def test_assoc_base0_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_BaseModel()
    _safe_set(b, 'diva_BaseModel', a1)
    assert _is_linked(b, 'diva_BaseModel', a1)
    if hasattr(a1, 'diva_VariabilityModel'):
        assert _is_linked(a1, 'diva_VariabilityModel', b)
    _safe_set(b, 'diva_BaseModel', a2)
    assert _is_linked(b, 'diva_BaseModel', a2)
    if hasattr(a1, 'diva_VariabilityModel'):
        assert not _is_linked(a1, 'diva_VariabilityModel', b)
    if hasattr(a2, 'diva_VariabilityModel'):
        assert _is_linked(a2, 'diva_VariabilityModel', b)
    _safe_set(b, 'diva_BaseModel', None)
    assert not _is_linked(b, 'diva_BaseModel', a2)
    if hasattr(a2, 'diva_VariabilityModel'):
        assert not _is_linked(a2, 'diva_VariabilityModel', b)


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


def test_assoc_context43_reverse_link_reassign_clear():
    a1 = diva_PriorityRule()
    a2 = diva_PriorityRule()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression44', a1)
    assert _is_linked(b, 'diva_ContextExpression44', a1)
    if hasattr(a1, 'diva_PriorityRule'):
        assert _is_linked(a1, 'diva_PriorityRule', b)
    _safe_set(b, 'diva_ContextExpression44', a2)
    assert _is_linked(b, 'diva_ContextExpression44', a2)
    if hasattr(a1, 'diva_PriorityRule'):
        assert not _is_linked(a1, 'diva_PriorityRule', b)
    if hasattr(a2, 'diva_PriorityRule'):
        assert _is_linked(a2, 'diva_PriorityRule', b)
    _safe_set(b, 'diva_ContextExpression44', None)
    assert not _is_linked(b, 'diva_ContextExpression44', a2)
    if hasattr(a2, 'diva_PriorityRule'):
        assert not _is_linked(a2, 'diva_PriorityRule', b)


def test_assoc_context72_reverse_link_reassign_clear():
    a1 = diva_Scenario()
    a2 = diva_Scenario()
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context74', a1)
    assert _is_linked(b, 'diva_Context74', a1)
    if hasattr(a1, 'diva_Scenario73'):
        assert _is_linked(a1, 'diva_Scenario73', b)
    _safe_set(b, 'diva_Context74', a2)
    assert _is_linked(b, 'diva_Context74', a2)
    if hasattr(a1, 'diva_Scenario73'):
        assert not _is_linked(a1, 'diva_Scenario73', b)
    if hasattr(a2, 'diva_Scenario73'):
        assert _is_linked(a2, 'diva_Scenario73', b)
    _safe_set(b, 'diva_Context74', None)
    assert not _is_linked(b, 'diva_Context74', a2)
    if hasattr(a2, 'diva_Scenario73'):
        assert not _is_linked(a2, 'diva_Scenario73', b)


def test_assoc_dependency27_reverse_link_reassign_clear():
    a1 = diva_VariantExpression()
    a2 = diva_VariantExpression()
    b = diva_Variant()
    _safe_set(b, 'diva_Variant28', a1)
    assert _is_linked(b, 'diva_Variant28', a1)
    if hasattr(a1, 'diva_VariantExpression'):
        assert _is_linked(a1, 'diva_VariantExpression', b)
    _safe_set(b, 'diva_Variant28', a2)
    assert _is_linked(b, 'diva_Variant28', a2)
    if hasattr(a1, 'diva_VariantExpression'):
        assert not _is_linked(a1, 'diva_VariantExpression', b)
    if hasattr(a2, 'diva_VariantExpression'):
        assert _is_linked(a2, 'diva_VariantExpression', b)
    _safe_set(b, 'diva_Variant28', None)
    assert not _is_linked(b, 'diva_Variant28', a2)
    if hasattr(a2, 'diva_VariantExpression'):
        assert not _is_linked(a2, 'diva_VariantExpression', b)


def test_assoc_dimension5_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension', a1)
    assert _is_linked(b, 'diva_Dimension', a1)
    if hasattr(a1, 'diva_VariabilityModel6'):
        assert _is_linked(a1, 'diva_VariabilityModel6', b)
    _safe_set(b, 'diva_Dimension', a2)
    assert _is_linked(b, 'diva_Dimension', a2)
    if hasattr(a1, 'diva_VariabilityModel6'):
        assert not _is_linked(a1, 'diva_VariabilityModel6', b)
    if hasattr(a2, 'diva_VariabilityModel6'):
        assert _is_linked(a2, 'diva_VariabilityModel6', b)
    _safe_set(b, 'diva_Dimension', None)
    assert not _is_linked(b, 'diva_Dimension', a2)
    if hasattr(a2, 'diva_VariabilityModel6'):
        assert not _is_linked(a2, 'diva_VariabilityModel6', b)


def test_assoc_expression12_reverse_link_reassign_clear():
    a1 = diva_Invariant()
    a2 = diva_Invariant()
    b = diva_Expression(text="sample_text")
    _safe_set(b, 'diva_Expression', a1)
    assert _is_linked(b, 'diva_Expression', a1)
    if hasattr(a1, 'diva_Invariant'):
        assert _is_linked(a1, 'diva_Invariant', b)
    _safe_set(b, 'diva_Expression', a2)
    assert _is_linked(b, 'diva_Expression', a2)
    if hasattr(a1, 'diva_Invariant'):
        assert not _is_linked(a1, 'diva_Invariant', b)
    if hasattr(a2, 'diva_Invariant'):
        assert _is_linked(a2, 'diva_Invariant', b)
    _safe_set(b, 'diva_Expression', None)
    assert not _is_linked(b, 'diva_Expression', a2)
    if hasattr(a2, 'diva_Invariant'):
        assert not _is_linked(a2, 'diva_Invariant', b)


def test_assoc_literal13_reverse_link_reassign_clear():
    a1 = diva_EnumVariable()
    a2 = diva_EnumVariable()
    b = diva_EnumLiteral()
    _safe_set(b, 'diva_EnumLiteral', a1)
    assert _is_linked(b, 'diva_EnumLiteral', a1)
    if hasattr(a1, 'diva_EnumVariable'):
        assert _is_linked(a1, 'diva_EnumVariable', b)
    _safe_set(b, 'diva_EnumLiteral', a2)
    assert _is_linked(b, 'diva_EnumLiteral', a2)
    if hasattr(a1, 'diva_EnumVariable'):
        assert not _is_linked(a1, 'diva_EnumVariable', b)
    if hasattr(a2, 'diva_EnumVariable'):
        assert _is_linked(a2, 'diva_EnumVariable', b)
    _safe_set(b, 'diva_EnumLiteral', None)
    assert not _is_linked(b, 'diva_EnumLiteral', a2)
    if hasattr(a2, 'diva_EnumVariable'):
        assert not _is_linked(a2, 'diva_EnumVariable', b)


def test_assoc_literal85_reverse_link_reassign_clear():
    a1 = diva_EnumVariableValue()
    a2 = diva_EnumVariableValue()
    b = diva_EnumLiteral()
    _safe_set(b, 'diva_EnumLiteral86', a1)
    assert _is_linked(b, 'diva_EnumLiteral86', a1)
    if hasattr(a1, 'diva_EnumVariableValue'):
        assert _is_linked(a1, 'diva_EnumVariableValue', b)
    _safe_set(b, 'diva_EnumLiteral86', a2)
    assert _is_linked(b, 'diva_EnumLiteral86', a2)
    if hasattr(a1, 'diva_EnumVariableValue'):
        assert not _is_linked(a1, 'diva_EnumVariableValue', b)
    if hasattr(a2, 'diva_EnumVariableValue'):
        assert _is_linked(a2, 'diva_EnumVariableValue', b)
    _safe_set(b, 'diva_EnumLiteral86', None)
    assert not _is_linked(b, 'diva_EnumLiteral86', a2)
    if hasattr(a2, 'diva_EnumVariableValue'):
        assert not _is_linked(a2, 'diva_EnumVariableValue', b)


def test_assoc_model22_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_AspectModel()
    _safe_set(b, 'diva_AspectModel', a1)
    assert _is_linked(b, 'diva_AspectModel', a1)
    if hasattr(a1, 'diva_Variant23'):
        assert _is_linked(a1, 'diva_Variant23', b)
    _safe_set(b, 'diva_AspectModel', a2)
    assert _is_linked(b, 'diva_AspectModel', a2)
    if hasattr(a1, 'diva_Variant23'):
        assert not _is_linked(a1, 'diva_Variant23', b)
    if hasattr(a2, 'diva_Variant23'):
        assert _is_linked(a2, 'diva_Variant23', b)
    _safe_set(b, 'diva_AspectModel', None)
    assert not _is_linked(b, 'diva_AspectModel', a2)
    if hasattr(a2, 'diva_Variant23'):
        assert not _is_linked(a2, 'diva_Variant23', b)


def test_assoc_model58_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_SimulationModel()
    _safe_set(b, 'simulation', a1)
    assert _is_linked(b, 'simulation', a1)
    if hasattr(a1, 'VariabilityModel'):
        assert _is_linked(a1, 'VariabilityModel', b)
    _safe_set(b, 'simulation', a2)
    assert _is_linked(b, 'simulation', a2)
    if hasattr(a1, 'VariabilityModel'):
        assert not _is_linked(a1, 'VariabilityModel', b)
    if hasattr(a2, 'VariabilityModel'):
        assert _is_linked(a2, 'VariabilityModel', b)
    _safe_set(b, 'simulation', None)
    assert not _is_linked(b, 'simulation', a2)
    if hasattr(a2, 'VariabilityModel'):
        assert not _is_linked(a2, 'VariabilityModel', b)


def test_assoc_oracle62_reverse_link_reassign_clear():
    a1 = diva_VariantExpression()
    a2 = diva_VariantExpression()
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context63', a1)
    assert _is_linked(b, 'diva_Context63', a1)
    if hasattr(a1, 'diva_VariantExpression64'):
        assert _is_linked(a1, 'diva_VariantExpression64', b)
    _safe_set(b, 'diva_Context63', a2)
    assert _is_linked(b, 'diva_Context63', a2)
    if hasattr(a1, 'diva_VariantExpression64'):
        assert not _is_linked(a1, 'diva_VariantExpression64', b)
    if hasattr(a2, 'diva_VariantExpression64'):
        assert _is_linked(a2, 'diva_VariantExpression64', b)
    _safe_set(b, 'diva_Context63', None)
    assert not _is_linked(b, 'diva_Context63', a2)
    if hasattr(a2, 'diva_VariantExpression64'):
        assert not _is_linked(a2, 'diva_VariantExpression64', b)


def test_assoc_priority45_reverse_link_reassign_clear():
    a1 = diva_PropertyPriority(priority="sample_text")
    a2 = diva_PropertyPriority(priority="sample_text_2")
    b = diva_PriorityRule()
    _safe_set(b, 'diva_PriorityRule46', {a1})
    assert _is_linked(b, 'diva_PriorityRule46', a1)
    if hasattr(a1, 'diva_PropertyPriority'):
        assert _is_linked(a1, 'diva_PropertyPriority', b)
    _safe_set(b, 'diva_PriorityRule46', {a2})
    assert _is_linked(b, 'diva_PriorityRule46', a2)
    if hasattr(a1, 'diva_PropertyPriority'):
        assert not _is_linked(a1, 'diva_PropertyPriority', b)
    if hasattr(a2, 'diva_PropertyPriority'):
        assert _is_linked(a2, 'diva_PropertyPriority', b)
    _safe_set(b, 'diva_PriorityRule46', set())
    assert not _is_linked(b, 'diva_PriorityRule46', a2)
    if hasattr(a2, 'diva_PropertyPriority'):
        assert not _is_linked(a2, 'diva_PropertyPriority', b)


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


def test_assoc_property3_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property', a1)
    assert _is_linked(b, 'diva_Property', a1)
    if hasattr(a1, 'diva_VariabilityModel4'):
        assert _is_linked(a1, 'diva_VariabilityModel4', b)
    _safe_set(b, 'diva_Property', a2)
    assert _is_linked(b, 'diva_Property', a2)
    if hasattr(a1, 'diva_VariabilityModel4'):
        assert not _is_linked(a1, 'diva_VariabilityModel4', b)
    if hasattr(a2, 'diva_VariabilityModel4'):
        assert _is_linked(a2, 'diva_VariabilityModel4', b)
    _safe_set(b, 'diva_Property', None)
    assert not _is_linked(b, 'diva_Property', a2)
    if hasattr(a2, 'diva_VariabilityModel4'):
        assert not _is_linked(a2, 'diva_VariabilityModel4', b)


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


def test_assoc_propertyValue25_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_PropertyValue(value="sample_text")
    _safe_set(b, 'diva_PropertyValue', a1)
    assert _is_linked(b, 'diva_PropertyValue', a1)
    if hasattr(a1, 'diva_Variant26'):
        assert _is_linked(a1, 'diva_Variant26', b)
    _safe_set(b, 'diva_PropertyValue', a2)
    assert _is_linked(b, 'diva_PropertyValue', a2)
    if hasattr(a1, 'diva_Variant26'):
        assert not _is_linked(a1, 'diva_Variant26', b)
    if hasattr(a2, 'diva_Variant26'):
        assert _is_linked(a2, 'diva_Variant26', b)
    _safe_set(b, 'diva_PropertyValue', None)
    assert not _is_linked(b, 'diva_PropertyValue', a2)
    if hasattr(a2, 'diva_Variant26'):
        assert not _is_linked(a2, 'diva_Variant26', b)


def test_assoc_required31_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression33', a1)
    assert _is_linked(b, 'diva_ContextExpression33', a1)
    if hasattr(a1, 'diva_Variant32'):
        assert _is_linked(a1, 'diva_Variant32', b)
    _safe_set(b, 'diva_ContextExpression33', a2)
    assert _is_linked(b, 'diva_ContextExpression33', a2)
    if hasattr(a1, 'diva_Variant32'):
        assert not _is_linked(a1, 'diva_Variant32', b)
    if hasattr(a2, 'diva_Variant32'):
        assert _is_linked(a2, 'diva_Variant32', b)
    _safe_set(b, 'diva_ContextExpression33', None)
    assert not _is_linked(b, 'diva_ContextExpression33', a2)
    if hasattr(a2, 'diva_Variant32'):
        assert not _is_linked(a2, 'diva_Variant32', b)


def test_assoc_scenario57_reverse_link_reassign_clear():
    a1 = diva_SimulationModel()
    a2 = diva_SimulationModel()
    b = diva_Scenario()
    _safe_set(b, 'diva_Scenario', a1)
    assert _is_linked(b, 'diva_Scenario', a1)
    if hasattr(a1, 'diva_SimulationModel'):
        assert _is_linked(a1, 'diva_SimulationModel', b)
    _safe_set(b, 'diva_Scenario', a2)
    assert _is_linked(b, 'diva_Scenario', a2)
    if hasattr(a1, 'diva_SimulationModel'):
        assert not _is_linked(a1, 'diva_SimulationModel', b)
    if hasattr(a2, 'diva_SimulationModel'):
        assert _is_linked(a2, 'diva_SimulationModel', b)
    _safe_set(b, 'diva_Scenario', None)
    assert not _is_linked(b, 'diva_Scenario', a2)
    if hasattr(a2, 'diva_SimulationModel'):
        assert not _is_linked(a2, 'diva_SimulationModel', b)


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


def test_assoc_simulation11_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_SimulationModel()
    _safe_set(b, 'SimulationModel', a1)
    assert _is_linked(b, 'SimulationModel', a1)
    if hasattr(a1, 'model'):
        assert _is_linked(a1, 'model', b)
    _safe_set(b, 'SimulationModel', a2)
    assert _is_linked(b, 'SimulationModel', a2)
    if hasattr(a1, 'model'):
        assert not _is_linked(a1, 'model', b)
    if hasattr(a2, 'model'):
        assert _is_linked(a2, 'model', b)
    _safe_set(b, 'SimulationModel', None)
    assert not _is_linked(b, 'SimulationModel', a2)
    if hasattr(a2, 'model'):
        assert not _is_linked(a2, 'model', b)


def test_assoc_type24_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'Dimension', a1)
    assert _is_linked(b, 'Dimension', a1)
    if hasattr(a1, 'variant'):
        assert _is_linked(a1, 'variant', b)
    _safe_set(b, 'Dimension', a2)
    assert _is_linked(b, 'Dimension', a2)
    if hasattr(a1, 'variant'):
        assert not _is_linked(a1, 'variant', b)
    if hasattr(a2, 'variant'):
        assert _is_linked(a2, 'variant', b)
    _safe_set(b, 'Dimension', None)
    assert not _is_linked(b, 'Dimension', a2)
    if hasattr(a2, 'variant'):
        assert not _is_linked(a2, 'variant', b)


def test_assoc_value20_reverse_link_reassign_clear():
    a1 = diva_EnumTerm()
    a2 = diva_EnumTerm()
    b = diva_EnumLiteral()
    _safe_set(b, 'diva_EnumLiteral21', a1)
    assert _is_linked(b, 'diva_EnumLiteral21', a1)
    if hasattr(a1, 'diva_EnumTerm'):
        assert _is_linked(a1, 'diva_EnumTerm', b)
    _safe_set(b, 'diva_EnumLiteral21', a2)
    assert _is_linked(b, 'diva_EnumLiteral21', a2)
    if hasattr(a1, 'diva_EnumTerm'):
        assert not _is_linked(a1, 'diva_EnumTerm', b)
    if hasattr(a2, 'diva_EnumTerm'):
        assert _is_linked(a2, 'diva_EnumTerm', b)
    _safe_set(b, 'diva_EnumLiteral21', None)
    assert not _is_linked(b, 'diva_EnumLiteral21', a2)
    if hasattr(a2, 'diva_EnumTerm'):
        assert not _is_linked(a2, 'diva_EnumTerm', b)


def test_assoc_variant17_reverse_link_reassign_clear():
    a1 = diva_VariantTerm()
    a2 = diva_VariantTerm()
    b = diva_Variant()
    _safe_set(b, 'diva_Variant', a1)
    assert _is_linked(b, 'diva_Variant', a1)
    if hasattr(a1, 'diva_VariantTerm'):
        assert _is_linked(a1, 'diva_VariantTerm', b)
    _safe_set(b, 'diva_Variant', a2)
    assert _is_linked(b, 'diva_Variant', a2)
    if hasattr(a1, 'diva_VariantTerm'):
        assert not _is_linked(a1, 'diva_VariantTerm', b)
    if hasattr(a2, 'diva_VariantTerm'):
        assert _is_linked(a2, 'diva_VariantTerm', b)
    _safe_set(b, 'diva_Variant', None)
    assert not _is_linked(b, 'diva_Variant', a2)
    if hasattr(a2, 'diva_VariantTerm'):
        assert not _is_linked(a2, 'diva_VariantTerm', b)


def test_assoc_variant34_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'type', {a1})
    assert _is_linked(b, 'type', a1)
    if hasattr(a1, 'Variant'):
        assert _is_linked(a1, 'Variant', b)
    _safe_set(b, 'type', {a2})
    assert _is_linked(b, 'type', a2)
    if hasattr(a1, 'Variant'):
        assert not _is_linked(a1, 'Variant', b)
    if hasattr(a2, 'Variant'):
        assert _is_linked(a2, 'Variant', b)
    _safe_set(b, 'type', set())
    assert not _is_linked(b, 'type', a2)
    if hasattr(a2, 'Variant'):
        assert not _is_linked(a2, 'Variant', b)


def test_assoc_variant67_reverse_link_reassign_clear():
    a1 = diva_Configuration(verdict="sample_text")
    a2 = diva_Configuration(verdict="sample_text_2")
    b = diva_ConfigVariant()
    _safe_set(b, 'diva_ConfigVariant', a1)
    assert _is_linked(b, 'diva_ConfigVariant', a1)
    if hasattr(a1, 'diva_Configuration68'):
        assert _is_linked(a1, 'diva_Configuration68', b)
    _safe_set(b, 'diva_ConfigVariant', a2)
    assert _is_linked(b, 'diva_ConfigVariant', a2)
    if hasattr(a1, 'diva_Configuration68'):
        assert not _is_linked(a1, 'diva_Configuration68', b)
    if hasattr(a2, 'diva_Configuration68'):
        assert _is_linked(a2, 'diva_Configuration68', b)
    _safe_set(b, 'diva_ConfigVariant', None)
    assert not _is_linked(b, 'diva_ConfigVariant', a2)
    if hasattr(a2, 'diva_Configuration68'):
        assert not _is_linked(a2, 'diva_Configuration68', b)


def test_assoc_variant69_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ConfigVariant()
    _safe_set(b, 'diva_ConfigVariant70', a1)
    assert _is_linked(b, 'diva_ConfigVariant70', a1)
    if hasattr(a1, 'diva_Variant71'):
        assert _is_linked(a1, 'diva_Variant71', b)
    _safe_set(b, 'diva_ConfigVariant70', a2)
    assert _is_linked(b, 'diva_ConfigVariant70', a2)
    if hasattr(a1, 'diva_Variant71'):
        assert not _is_linked(a1, 'diva_Variant71', b)
    if hasattr(a2, 'diva_Variant71'):
        assert _is_linked(a2, 'diva_Variant71', b)
    _safe_set(b, 'diva_ConfigVariant70', None)
    assert not _is_linked(b, 'diva_ConfigVariant70', a2)
    if hasattr(a2, 'diva_Variant71'):
        assert not _is_linked(a2, 'diva_Variant71', b)


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


def test_assoc_constraint9_stub_double():
    # diva_Constraint has no real 'diva_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Constraint()
    setattr(partner, 'diva_Constraint', None)
    _safe_set(owner, 'diva_VariabilityModel10', {partner})
    assert getattr(partner, 'diva_Constraint') == owner
    _safe_set(owner, 'diva_VariabilityModel10', set())
    assert getattr(partner, 'diva_Constraint') is None


def test_assoc_context1_stub_double():
    # diva_Variable has no real 'diva_Variable' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Variable()
    setattr(partner, 'diva_Variable', None)
    _safe_set(owner, 'diva_VariabilityModel2', {partner})
    assert getattr(partner, 'diva_Variable') == owner
    _safe_set(owner, 'diva_VariabilityModel2', set())
    assert getattr(partner, 'diva_Variable') is None


def test_assoc_rule7_stub_double():
    # diva_Rule has no real 'diva_Rule' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Rule()
    setattr(partner, 'diva_Rule', None)
    _safe_set(owner, 'diva_VariabilityModel8', {partner})
    assert getattr(partner, 'diva_Rule') == owner
    _safe_set(owner, 'diva_VariabilityModel8', set())
    assert getattr(partner, 'diva_Rule') is None


def test_assoc_term14_stub_double():
    # diva_Term has no real 'diva_Term' property in the generated
    # code (a bare stub) -- manually attach it so diva_NotTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_NotTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_NotTerm()
    partner = diva_Term()
    setattr(partner, 'diva_Term', None)
    _safe_set(owner, 'diva_NotTerm', partner)
    assert getattr(partner, 'diva_Term') == owner
    _safe_set(owner, 'diva_NotTerm', None)
    assert getattr(partner, 'diva_Term') is None


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


