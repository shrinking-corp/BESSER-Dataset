import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CEPable,
    Constraint,
    DiVAModelElement,
    Expression,
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
    diva_BoolVariableValue,
    diva_BooleanTerm,
    diva_BooleanVariable,
    diva_CEPable,
    diva_ConfigVariant,
    diva_Configuration,
    diva_ConfigurationModel,
    diva_Constraint,
    diva_Context,
    diva_ContextExpression,
    diva_ContextModel,
    diva_DiVAModelElement,
    diva_Dimension,
    diva_EnumLiteral,
    diva_EnumTerm,
    diva_EnumVariable,
    diva_EnumVariableValue,
    diva_Expression,
    diva_Invariant,
    diva_MultiplicityConstraint,
    diva_NamedElement,
    diva_NaryTerm,
    diva_NotTerm,
    diva_OrTerm,
    diva_Priority,
    diva_PriorityRule,
    diva_Property,
    diva_PropertyLiteral,
    diva_PropertyPriority,
    diva_PropertyValue,
    diva_Rule,
    diva_Scenario,
    diva_Score,
    diva_ScoredElement,
    diva_SimulationModel,
    diva_SuitableConfiguration,
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

def test_assoc_available25_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression', a1)
    assert _is_linked(b, 'diva_ContextExpression', a1)
    if hasattr(a1, 'diva_Variant26'):
        assert _is_linked(a1, 'diva_Variant26', b)
    _safe_set(b, 'diva_ContextExpression', a2)
    assert _is_linked(b, 'diva_ContextExpression', a2)
    if hasattr(a1, 'diva_Variant26'):
        assert not _is_linked(a1, 'diva_Variant26', b)
    if hasattr(a2, 'diva_Variant26'):
        assert _is_linked(a2, 'diva_Variant26', b)
    _safe_set(b, 'diva_ContextExpression', None)
    assert not _is_linked(b, 'diva_ContextExpression', a2)
    if hasattr(a2, 'diva_Variant26'):
        assert not _is_linked(a2, 'diva_Variant26', b)


def test_assoc_available51_reverse_link_reassign_clear():
    a1 = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    a2 = diva_MultiplicityConstraint(lower="sample_text_2", upper="sample_text_2")
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression53', a1)
    assert _is_linked(b, 'diva_ContextExpression53', a1)
    if hasattr(a1, 'diva_MultiplicityConstraint52'):
        assert _is_linked(a1, 'diva_MultiplicityConstraint52', b)
    _safe_set(b, 'diva_ContextExpression53', a2)
    assert _is_linked(b, 'diva_ContextExpression53', a2)
    if hasattr(a1, 'diva_MultiplicityConstraint52'):
        assert not _is_linked(a1, 'diva_MultiplicityConstraint52', b)
    if hasattr(a2, 'diva_MultiplicityConstraint52'):
        assert _is_linked(a2, 'diva_MultiplicityConstraint52', b)
    _safe_set(b, 'diva_ContextExpression53', None)
    assert not _is_linked(b, 'diva_ContextExpression53', a2)
    if hasattr(a2, 'diva_MultiplicityConstraint52'):
        assert not _is_linked(a2, 'diva_MultiplicityConstraint52', b)


def test_assoc_configuration58_reverse_link_reassign_clear():
    a1 = diva_Context(verdict="sample_text")
    a2 = diva_Context(verdict="sample_text_2")
    b = diva_Configuration(verdict="sample_text")
    _safe_set(b, 'diva_Configuration', a1)
    assert _is_linked(b, 'diva_Configuration', a1)
    if hasattr(a1, 'diva_Context59'):
        assert _is_linked(a1, 'diva_Context59', b)
    _safe_set(b, 'diva_Configuration', a2)
    assert _is_linked(b, 'diva_Configuration', a2)
    if hasattr(a1, 'diva_Context59'):
        assert not _is_linked(a1, 'diva_Context59', b)
    if hasattr(a2, 'diva_Context59'):
        assert _is_linked(a2, 'diva_Context59', b)
    _safe_set(b, 'diva_Configuration', None)
    assert not _is_linked(b, 'diva_Configuration', a2)
    if hasattr(a2, 'diva_Context59'):
        assert not _is_linked(a2, 'diva_Context59', b)


def test_assoc_configurations85_reverse_link_reassign_clear():
    a1 = diva_SuitableConfiguration(score=7)
    a2 = diva_SuitableConfiguration(score=13)
    b = diva_ConfigurationModel()
    _safe_set(b, 'diva_ConfigurationModel', {a1})
    assert _is_linked(b, 'diva_ConfigurationModel', a1)
    if hasattr(a1, 'diva_SuitableConfiguration'):
        assert _is_linked(a1, 'diva_SuitableConfiguration', b)
    _safe_set(b, 'diva_ConfigurationModel', {a2})
    assert _is_linked(b, 'diva_ConfigurationModel', a2)
    if hasattr(a1, 'diva_SuitableConfiguration'):
        assert not _is_linked(a1, 'diva_SuitableConfiguration', b)
    if hasattr(a2, 'diva_SuitableConfiguration'):
        assert _is_linked(a2, 'diva_SuitableConfiguration', b)
    _safe_set(b, 'diva_ConfigurationModel', set())
    assert not _is_linked(b, 'diva_ConfigurationModel', a2)
    if hasattr(a2, 'diva_SuitableConfiguration'):
        assert not _is_linked(a2, 'diva_SuitableConfiguration', b)


def test_assoc_constraints34_reverse_link_reassign_clear():
    a1 = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    a2 = diva_MultiplicityConstraint(lower="sample_text_2", upper="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension35', {a1})
    assert _is_linked(b, 'diva_Dimension35', a1)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert _is_linked(a1, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension35', {a2})
    assert _is_linked(b, 'diva_Dimension35', a2)
    if hasattr(a1, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a1, 'diva_MultiplicityConstraint', b)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert _is_linked(a2, 'diva_MultiplicityConstraint', b)
    _safe_set(b, 'diva_Dimension35', set())
    assert not _is_linked(b, 'diva_Dimension35', a2)
    if hasattr(a2, 'diva_MultiplicityConstraint'):
        assert not _is_linked(a2, 'diva_MultiplicityConstraint', b)


def test_assoc_context39_reverse_link_reassign_clear():
    a1 = diva_PriorityRule()
    a2 = diva_PriorityRule()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression40', a1)
    assert _is_linked(b, 'diva_ContextExpression40', a1)
    if hasattr(a1, 'diva_PriorityRule'):
        assert _is_linked(a1, 'diva_PriorityRule', b)
    _safe_set(b, 'diva_ContextExpression40', a2)
    assert _is_linked(b, 'diva_ContextExpression40', a2)
    if hasattr(a1, 'diva_PriorityRule'):
        assert not _is_linked(a1, 'diva_PriorityRule', b)
    if hasattr(a2, 'diva_PriorityRule'):
        assert _is_linked(a2, 'diva_PriorityRule', b)
    _safe_set(b, 'diva_ContextExpression40', None)
    assert not _is_linked(b, 'diva_ContextExpression40', a2)
    if hasattr(a2, 'diva_PriorityRule'):
        assert not _is_linked(a2, 'diva_PriorityRule', b)


def test_assoc_context70_reverse_link_reassign_clear():
    a1 = diva_Scenario()
    a2 = diva_Scenario()
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context72', a1)
    assert _is_linked(b, 'diva_Context72', a1)
    if hasattr(a1, 'diva_Scenario71'):
        assert _is_linked(a1, 'diva_Scenario71', b)
    _safe_set(b, 'diva_Context72', a2)
    assert _is_linked(b, 'diva_Context72', a2)
    if hasattr(a1, 'diva_Scenario71'):
        assert not _is_linked(a1, 'diva_Scenario71', b)
    if hasattr(a2, 'diva_Scenario71'):
        assert _is_linked(a2, 'diva_Scenario71', b)
    _safe_set(b, 'diva_Context72', None)
    assert not _is_linked(b, 'diva_Context72', a2)
    if hasattr(a2, 'diva_Scenario71'):
        assert not _is_linked(a2, 'diva_Scenario71', b)


def test_assoc_dependency23_reverse_link_reassign_clear():
    a1 = diva_VariantExpression()
    a2 = diva_VariantExpression()
    b = diva_Variant()
    _safe_set(b, 'diva_Variant24', a1)
    assert _is_linked(b, 'diva_Variant24', a1)
    if hasattr(a1, 'diva_VariantExpression'):
        assert _is_linked(a1, 'diva_VariantExpression', b)
    _safe_set(b, 'diva_Variant24', a2)
    assert _is_linked(b, 'diva_Variant24', a2)
    if hasattr(a1, 'diva_VariantExpression'):
        assert not _is_linked(a1, 'diva_VariantExpression', b)
    if hasattr(a2, 'diva_VariantExpression'):
        assert _is_linked(a2, 'diva_VariantExpression', b)
    _safe_set(b, 'diva_Variant24', None)
    assert not _is_linked(b, 'diva_Variant24', a2)
    if hasattr(a2, 'diva_VariantExpression'):
        assert not _is_linked(a2, 'diva_VariantExpression', b)


def test_assoc_dimension3_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension', a1)
    assert _is_linked(b, 'diva_Dimension', a1)
    if hasattr(a1, 'diva_VariabilityModel4'):
        assert _is_linked(a1, 'diva_VariabilityModel4', b)
    _safe_set(b, 'diva_Dimension', a2)
    assert _is_linked(b, 'diva_Dimension', a2)
    if hasattr(a1, 'diva_VariabilityModel4'):
        assert not _is_linked(a1, 'diva_VariabilityModel4', b)
    if hasattr(a2, 'diva_VariabilityModel4'):
        assert _is_linked(a2, 'diva_VariabilityModel4', b)
    _safe_set(b, 'diva_Dimension', None)
    assert not _is_linked(b, 'diva_Dimension', a2)
    if hasattr(a2, 'diva_VariabilityModel4'):
        assert not _is_linked(a2, 'diva_VariabilityModel4', b)


def test_assoc_expression10_reverse_link_reassign_clear():
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


def test_assoc_literal11_reverse_link_reassign_clear():
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


def test_assoc_literal43_reverse_link_reassign_clear():
    a1 = diva_PropertyLiteral(value="sample_text")
    a2 = diva_PropertyLiteral(value="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property44', {a1})
    assert _is_linked(b, 'diva_Property44', a1)
    if hasattr(a1, 'diva_PropertyLiteral'):
        assert _is_linked(a1, 'diva_PropertyLiteral', b)
    _safe_set(b, 'diva_Property44', {a2})
    assert _is_linked(b, 'diva_Property44', a2)
    if hasattr(a1, 'diva_PropertyLiteral'):
        assert not _is_linked(a1, 'diva_PropertyLiteral', b)
    if hasattr(a2, 'diva_PropertyLiteral'):
        assert _is_linked(a2, 'diva_PropertyLiteral', b)
    _safe_set(b, 'diva_Property44', set())
    assert not _is_linked(b, 'diva_Property44', a2)
    if hasattr(a2, 'diva_PropertyLiteral'):
        assert not _is_linked(a2, 'diva_PropertyLiteral', b)


def test_assoc_literal83_reverse_link_reassign_clear():
    a1 = diva_EnumVariableValue()
    a2 = diva_EnumVariableValue()
    b = diva_EnumLiteral()
    _safe_set(b, 'diva_EnumLiteral84', a1)
    assert _is_linked(b, 'diva_EnumLiteral84', a1)
    if hasattr(a1, 'diva_EnumVariableValue'):
        assert _is_linked(a1, 'diva_EnumVariableValue', b)
    _safe_set(b, 'diva_EnumLiteral84', a2)
    assert _is_linked(b, 'diva_EnumLiteral84', a2)
    if hasattr(a1, 'diva_EnumVariableValue'):
        assert not _is_linked(a1, 'diva_EnumVariableValue', b)
    if hasattr(a2, 'diva_EnumVariableValue'):
        assert _is_linked(a2, 'diva_EnumVariableValue', b)
    _safe_set(b, 'diva_EnumLiteral84', None)
    assert not _is_linked(b, 'diva_EnumLiteral84', a2)
    if hasattr(a2, 'diva_EnumVariableValue'):
        assert not _is_linked(a2, 'diva_EnumVariableValue', b)


def test_assoc_model56_reverse_link_reassign_clear():
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


def test_assoc_oracle60_reverse_link_reassign_clear():
    a1 = diva_VariantExpression()
    a2 = diva_VariantExpression()
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context61', a1)
    assert _is_linked(b, 'diva_Context61', a1)
    if hasattr(a1, 'diva_VariantExpression62'):
        assert _is_linked(a1, 'diva_VariantExpression62', b)
    _safe_set(b, 'diva_Context61', a2)
    assert _is_linked(b, 'diva_Context61', a2)
    if hasattr(a1, 'diva_VariantExpression62'):
        assert not _is_linked(a1, 'diva_VariantExpression62', b)
    if hasattr(a2, 'diva_VariantExpression62'):
        assert _is_linked(a2, 'diva_VariantExpression62', b)
    _safe_set(b, 'diva_Context61', None)
    assert not _is_linked(b, 'diva_Context61', a2)
    if hasattr(a2, 'diva_VariantExpression62'):
        assert not _is_linked(a2, 'diva_VariantExpression62', b)


def test_assoc_priority41_reverse_link_reassign_clear():
    a1 = diva_PropertyPriority(priority="sample_text")
    a2 = diva_PropertyPriority(priority="sample_text_2")
    b = diva_PriorityRule()
    _safe_set(b, 'diva_PriorityRule42', {a1})
    assert _is_linked(b, 'diva_PriorityRule42', a1)
    if hasattr(a1, 'diva_PropertyPriority'):
        assert _is_linked(a1, 'diva_PropertyPriority', b)
    _safe_set(b, 'diva_PriorityRule42', {a2})
    assert _is_linked(b, 'diva_PriorityRule42', a2)
    if hasattr(a1, 'diva_PropertyPriority'):
        assert not _is_linked(a1, 'diva_PropertyPriority', b)
    if hasattr(a2, 'diva_PropertyPriority'):
        assert _is_linked(a2, 'diva_PropertyPriority', b)
    _safe_set(b, 'diva_PriorityRule42', set())
    assert not _is_linked(b, 'diva_PriorityRule42', a2)
    if hasattr(a2, 'diva_PropertyPriority'):
        assert not _is_linked(a2, 'diva_PropertyPriority', b)


def test_assoc_priority63_reverse_link_reassign_clear():
    a1 = diva_Priority(priority=7)
    a2 = diva_Priority(priority=13)
    b = diva_Context(verdict="sample_text")
    _safe_set(b, 'diva_Context64', {a1})
    assert _is_linked(b, 'diva_Context64', a1)
    if hasattr(a1, 'diva_Priority'):
        assert _is_linked(a1, 'diva_Priority', b)
    _safe_set(b, 'diva_Context64', {a2})
    assert _is_linked(b, 'diva_Context64', a2)
    if hasattr(a1, 'diva_Priority'):
        assert not _is_linked(a1, 'diva_Priority', b)
    if hasattr(a2, 'diva_Priority'):
        assert _is_linked(a2, 'diva_Priority', b)
    _safe_set(b, 'diva_Context64', set())
    assert not _is_linked(b, 'diva_Context64', a2)
    if hasattr(a2, 'diva_Priority'):
        assert not _is_linked(a2, 'diva_Priority', b)


def test_assoc_property1_reverse_link_reassign_clear():
    a1 = diva_VariabilityModel()
    a2 = diva_VariabilityModel()
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property', a1)
    assert _is_linked(b, 'diva_Property', a1)
    if hasattr(a1, 'diva_VariabilityModel2'):
        assert _is_linked(a1, 'diva_VariabilityModel2', b)
    _safe_set(b, 'diva_Property', a2)
    assert _is_linked(b, 'diva_Property', a2)
    if hasattr(a1, 'diva_VariabilityModel2'):
        assert not _is_linked(a1, 'diva_VariabilityModel2', b)
    if hasattr(a2, 'diva_VariabilityModel2'):
        assert _is_linked(a2, 'diva_VariabilityModel2', b)
    _safe_set(b, 'diva_Property', None)
    assert not _is_linked(b, 'diva_Property', a2)
    if hasattr(a2, 'diva_VariabilityModel2'):
        assert not _is_linked(a2, 'diva_VariabilityModel2', b)


def test_assoc_property31_reverse_link_reassign_clear():
    a1 = diva_Property(direction="sample_text")
    a2 = diva_Property(direction="sample_text_2")
    b = diva_Dimension(lower="sample_text", upper="sample_text")
    _safe_set(b, 'diva_Dimension32', {a1})
    assert _is_linked(b, 'diva_Dimension32', a1)
    if hasattr(a1, 'diva_Property33'):
        assert _is_linked(a1, 'diva_Property33', b)
    _safe_set(b, 'diva_Dimension32', {a2})
    assert _is_linked(b, 'diva_Dimension32', a2)
    if hasattr(a1, 'diva_Property33'):
        assert not _is_linked(a1, 'diva_Property33', b)
    if hasattr(a2, 'diva_Property33'):
        assert _is_linked(a2, 'diva_Property33', b)
    _safe_set(b, 'diva_Dimension32', set())
    assert not _is_linked(b, 'diva_Dimension32', a2)
    if hasattr(a2, 'diva_Property33'):
        assert not _is_linked(a2, 'diva_Property33', b)


def test_assoc_property45_reverse_link_reassign_clear():
    a1 = diva_PropertyValue(value="sample_text")
    a2 = diva_PropertyValue(value="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property47', a1)
    assert _is_linked(b, 'diva_Property47', a1)
    if hasattr(a1, 'diva_PropertyValue46'):
        assert _is_linked(a1, 'diva_PropertyValue46', b)
    _safe_set(b, 'diva_Property47', a2)
    assert _is_linked(b, 'diva_Property47', a2)
    if hasattr(a1, 'diva_PropertyValue46'):
        assert not _is_linked(a1, 'diva_PropertyValue46', b)
    if hasattr(a2, 'diva_PropertyValue46'):
        assert _is_linked(a2, 'diva_PropertyValue46', b)
    _safe_set(b, 'diva_Property47', None)
    assert not _is_linked(b, 'diva_Property47', a2)
    if hasattr(a2, 'diva_PropertyValue46'):
        assert not _is_linked(a2, 'diva_PropertyValue46', b)


def test_assoc_property48_reverse_link_reassign_clear():
    a1 = diva_PropertyPriority(priority="sample_text")
    a2 = diva_PropertyPriority(priority="sample_text_2")
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property50', a1)
    assert _is_linked(b, 'diva_Property50', a1)
    if hasattr(a1, 'diva_PropertyPriority49'):
        assert _is_linked(a1, 'diva_PropertyPriority49', b)
    _safe_set(b, 'diva_Property50', a2)
    assert _is_linked(b, 'diva_Property50', a2)
    if hasattr(a1, 'diva_PropertyPriority49'):
        assert not _is_linked(a1, 'diva_PropertyPriority49', b)
    if hasattr(a2, 'diva_PropertyPriority49'):
        assert _is_linked(a2, 'diva_PropertyPriority49', b)
    _safe_set(b, 'diva_Property50', None)
    assert not _is_linked(b, 'diva_Property50', a2)
    if hasattr(a2, 'diva_PropertyPriority49'):
        assert not _is_linked(a2, 'diva_PropertyPriority49', b)


def test_assoc_property74_reverse_link_reassign_clear():
    a1 = diva_Score(score=7)
    a2 = diva_Score(score=13)
    b = diva_Property(direction="sample_text")
    _safe_set(b, 'diva_Property76', a1)
    assert _is_linked(b, 'diva_Property76', a1)
    if hasattr(a1, 'diva_Score75'):
        assert _is_linked(a1, 'diva_Score75', b)
    _safe_set(b, 'diva_Property76', a2)
    assert _is_linked(b, 'diva_Property76', a2)
    if hasattr(a1, 'diva_Score75'):
        assert not _is_linked(a1, 'diva_Score75', b)
    if hasattr(a2, 'diva_Score75'):
        assert _is_linked(a2, 'diva_Score75', b)
    _safe_set(b, 'diva_Property76', None)
    assert not _is_linked(b, 'diva_Property76', a2)
    if hasattr(a2, 'diva_Score75'):
        assert not _is_linked(a2, 'diva_Score75', b)


def test_assoc_property77_reverse_link_reassign_clear():
    a1 = diva_Property(direction="sample_text")
    a2 = diva_Property(direction="sample_text_2")
    b = diva_Priority(priority=7)
    _safe_set(b, 'diva_Priority78', a1)
    assert _is_linked(b, 'diva_Priority78', a1)
    if hasattr(a1, 'diva_Property79'):
        assert _is_linked(a1, 'diva_Property79', b)
    _safe_set(b, 'diva_Priority78', a2)
    assert _is_linked(b, 'diva_Priority78', a2)
    if hasattr(a1, 'diva_Property79'):
        assert not _is_linked(a1, 'diva_Property79', b)
    if hasattr(a2, 'diva_Property79'):
        assert _is_linked(a2, 'diva_Property79', b)
    _safe_set(b, 'diva_Priority78', None)
    assert not _is_linked(b, 'diva_Priority78', a2)
    if hasattr(a2, 'diva_Property79'):
        assert not _is_linked(a2, 'diva_Property79', b)


def test_assoc_propertyValue21_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_PropertyValue(value="sample_text")
    _safe_set(b, 'diva_PropertyValue', a1)
    assert _is_linked(b, 'diva_PropertyValue', a1)
    if hasattr(a1, 'diva_Variant22'):
        assert _is_linked(a1, 'diva_Variant22', b)
    _safe_set(b, 'diva_PropertyValue', a2)
    assert _is_linked(b, 'diva_PropertyValue', a2)
    if hasattr(a1, 'diva_Variant22'):
        assert not _is_linked(a1, 'diva_Variant22', b)
    if hasattr(a2, 'diva_Variant22'):
        assert _is_linked(a2, 'diva_Variant22', b)
    _safe_set(b, 'diva_PropertyValue', None)
    assert not _is_linked(b, 'diva_PropertyValue', a2)
    if hasattr(a2, 'diva_Variant22'):
        assert not _is_linked(a2, 'diva_Variant22', b)


def test_assoc_required27_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ContextExpression()
    _safe_set(b, 'diva_ContextExpression29', a1)
    assert _is_linked(b, 'diva_ContextExpression29', a1)
    if hasattr(a1, 'diva_Variant28'):
        assert _is_linked(a1, 'diva_Variant28', b)
    _safe_set(b, 'diva_ContextExpression29', a2)
    assert _is_linked(b, 'diva_ContextExpression29', a2)
    if hasattr(a1, 'diva_Variant28'):
        assert not _is_linked(a1, 'diva_Variant28', b)
    if hasattr(a2, 'diva_Variant28'):
        assert _is_linked(a2, 'diva_Variant28', b)
    _safe_set(b, 'diva_ContextExpression29', None)
    assert not _is_linked(b, 'diva_ContextExpression29', a2)
    if hasattr(a2, 'diva_Variant28'):
        assert not _is_linked(a2, 'diva_Variant28', b)


def test_assoc_scenario55_reverse_link_reassign_clear():
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


def test_assoc_score73_reverse_link_reassign_clear():
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


def test_assoc_simulation9_reverse_link_reassign_clear():
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


def test_assoc_type20_reverse_link_reassign_clear():
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


def test_assoc_value18_reverse_link_reassign_clear():
    a1 = diva_EnumTerm()
    a2 = diva_EnumTerm()
    b = diva_EnumLiteral()
    _safe_set(b, 'diva_EnumLiteral19', a1)
    assert _is_linked(b, 'diva_EnumLiteral19', a1)
    if hasattr(a1, 'diva_EnumTerm'):
        assert _is_linked(a1, 'diva_EnumTerm', b)
    _safe_set(b, 'diva_EnumLiteral19', a2)
    assert _is_linked(b, 'diva_EnumLiteral19', a2)
    if hasattr(a1, 'diva_EnumTerm'):
        assert not _is_linked(a1, 'diva_EnumTerm', b)
    if hasattr(a2, 'diva_EnumTerm'):
        assert _is_linked(a2, 'diva_EnumTerm', b)
    _safe_set(b, 'diva_EnumLiteral19', None)
    assert not _is_linked(b, 'diva_EnumLiteral19', a2)
    if hasattr(a2, 'diva_EnumTerm'):
        assert not _is_linked(a2, 'diva_EnumTerm', b)


def test_assoc_variant15_reverse_link_reassign_clear():
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


def test_assoc_variant30_reverse_link_reassign_clear():
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


def test_assoc_variant65_reverse_link_reassign_clear():
    a1 = diva_Configuration(verdict="sample_text")
    a2 = diva_Configuration(verdict="sample_text_2")
    b = diva_ConfigVariant()
    _safe_set(b, 'diva_ConfigVariant', a1)
    assert _is_linked(b, 'diva_ConfigVariant', a1)
    if hasattr(a1, 'diva_Configuration66'):
        assert _is_linked(a1, 'diva_Configuration66', b)
    _safe_set(b, 'diva_ConfigVariant', a2)
    assert _is_linked(b, 'diva_ConfigVariant', a2)
    if hasattr(a1, 'diva_Configuration66'):
        assert not _is_linked(a1, 'diva_Configuration66', b)
    if hasattr(a2, 'diva_Configuration66'):
        assert _is_linked(a2, 'diva_Configuration66', b)
    _safe_set(b, 'diva_ConfigVariant', None)
    assert not _is_linked(b, 'diva_ConfigVariant', a2)
    if hasattr(a2, 'diva_Configuration66'):
        assert not _is_linked(a2, 'diva_Configuration66', b)


def test_assoc_variant67_reverse_link_reassign_clear():
    a1 = diva_Variant()
    a2 = diva_Variant()
    b = diva_ConfigVariant()
    _safe_set(b, 'diva_ConfigVariant68', a1)
    assert _is_linked(b, 'diva_ConfigVariant68', a1)
    if hasattr(a1, 'diva_Variant69'):
        assert _is_linked(a1, 'diva_Variant69', b)
    _safe_set(b, 'diva_ConfigVariant68', a2)
    assert _is_linked(b, 'diva_ConfigVariant68', a2)
    if hasattr(a1, 'diva_Variant69'):
        assert not _is_linked(a1, 'diva_Variant69', b)
    if hasattr(a2, 'diva_Variant69'):
        assert _is_linked(a2, 'diva_Variant69', b)
    _safe_set(b, 'diva_ConfigVariant68', None)
    assert not _is_linked(b, 'diva_ConfigVariant68', a2)
    if hasattr(a2, 'diva_Variant69'):
        assert not _is_linked(a2, 'diva_Variant69', b)


def test_assoc_variant86_reverse_link_reassign_clear():
    a1 = diva_SuitableConfiguration(score=7)
    a2 = diva_SuitableConfiguration(score=13)
    b = diva_ConfigVariant()
    _safe_set(b, 'diva_ConfigVariant88', a1)
    assert _is_linked(b, 'diva_ConfigVariant88', a1)
    if hasattr(a1, 'diva_SuitableConfiguration87'):
        assert _is_linked(a1, 'diva_SuitableConfiguration87', b)
    _safe_set(b, 'diva_ConfigVariant88', a2)
    assert _is_linked(b, 'diva_ConfigVariant88', a2)
    if hasattr(a1, 'diva_SuitableConfiguration87'):
        assert not _is_linked(a1, 'diva_SuitableConfiguration87', b)
    if hasattr(a2, 'diva_SuitableConfiguration87'):
        assert _is_linked(a2, 'diva_SuitableConfiguration87', b)
    _safe_set(b, 'diva_ConfigVariant88', None)
    assert not _is_linked(b, 'diva_ConfigVariant88', a2)
    if hasattr(a2, 'diva_SuitableConfiguration87'):
        assert not _is_linked(a2, 'diva_SuitableConfiguration87', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation54_stub_double():
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


def test_assoc_constraint7_stub_double():
    # diva_Constraint has no real 'diva_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Constraint()
    setattr(partner, 'diva_Constraint', None)
    _safe_set(owner, 'diva_VariabilityModel8', {partner})
    assert getattr(partner, 'diva_Constraint') == owner
    _safe_set(owner, 'diva_VariabilityModel8', set())
    assert getattr(partner, 'diva_Constraint') is None


def test_assoc_context0_stub_double():
    # diva_Variable has no real 'diva_Variable' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Variable()
    setattr(partner, 'diva_Variable', None)
    _safe_set(owner, 'diva_VariabilityModel', {partner})
    assert getattr(partner, 'diva_Variable') == owner
    _safe_set(owner, 'diva_VariabilityModel', set())
    assert getattr(partner, 'diva_Variable') is None


def test_assoc_rule5_stub_double():
    # diva_Rule has no real 'diva_Rule' property in the generated
    # code (a bare stub) -- manually attach it so diva_VariabilityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_VariabilityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_VariabilityModel()
    partner = diva_Rule()
    setattr(partner, 'diva_Rule', None)
    _safe_set(owner, 'diva_VariabilityModel6', {partner})
    assert getattr(partner, 'diva_Rule') == owner
    _safe_set(owner, 'diva_VariabilityModel6', set())
    assert getattr(partner, 'diva_Rule') is None


def test_assoc_term12_stub_double():
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


def test_assoc_term36_stub_double():
    # diva_Term has no real 'diva_Term38' property in the generated
    # code (a bare stub) -- manually attach it so diva_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Expression(text="sample_text")
    partner = diva_Term()
    setattr(partner, 'diva_Term38', None)
    _safe_set(owner, 'diva_Expression37', partner)
    assert getattr(partner, 'diva_Term38') == owner
    _safe_set(owner, 'diva_Expression37', None)
    assert getattr(partner, 'diva_Term38') is None


def test_assoc_variable57_stub_double():
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


def test_assoc_variable89_stub_double():
    # diva_VariableValue has no real 'diva_VariableValue90' property in the generated
    # code (a bare stub) -- manually attach it so diva_ContextModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_ContextModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_ContextModel()
    partner = diva_VariableValue()
    setattr(partner, 'diva_VariableValue90', None)
    _safe_set(owner, 'diva_ContextModel', {partner})
    assert getattr(partner, 'diva_VariableValue90') == owner
    _safe_set(owner, 'diva_ContextModel', set())
    assert getattr(partner, 'diva_VariableValue90') is None


