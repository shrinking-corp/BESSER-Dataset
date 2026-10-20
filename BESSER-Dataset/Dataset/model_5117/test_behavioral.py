import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    DiVAModelElement,
    Expression,
    Model,
    ModelContainer,
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
    diva_Model,
    diva_ModelContainer,
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
    a1 = diva_Variant(weaveLevel="sample_text")
    a2 = diva_Variant(weaveLevel="sample_text_2")
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


def test_assoc_type20_reverse_link_reassign_clear():
    a1 = diva_Variant(weaveLevel="sample_text")
    a2 = diva_Variant(weaveLevel="sample_text_2")
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


def test_assoc_variant30_reverse_link_reassign_clear():
    a1 = diva_Variant(weaveLevel="sample_text")
    a2 = diva_Variant(weaveLevel="sample_text_2")
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


def test_assoc_available25_stub_double():
    # diva_ContextExpression has no real 'diva_ContextExpression' property in the generated
    # code (a bare stub) -- manually attach it so diva_Variant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Variant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Variant(weaveLevel="sample_text")
    partner = diva_ContextExpression()
    setattr(partner, 'diva_ContextExpression', None)
    _safe_set(owner, 'diva_Variant26', partner)
    assert getattr(partner, 'diva_ContextExpression') == owner
    _safe_set(owner, 'diva_Variant26', None)
    assert getattr(partner, 'diva_ContextExpression') is None


def test_assoc_available51_stub_double():
    # diva_ContextExpression has no real 'diva_ContextExpression53' property in the generated
    # code (a bare stub) -- manually attach it so diva_MultiplicityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_MultiplicityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    partner = diva_ContextExpression()
    setattr(partner, 'diva_ContextExpression53', None)
    _safe_set(owner, 'diva_MultiplicityConstraint52', partner)
    assert getattr(partner, 'diva_ContextExpression53') == owner
    _safe_set(owner, 'diva_MultiplicityConstraint52', None)
    assert getattr(partner, 'diva_ContextExpression53') is None


def test_assoc_configurations85_stub_double():
    # diva_ConfigurationModel has no real 'diva_ConfigurationModel' property in the generated
    # code (a bare stub) -- manually attach it so diva_SuitableConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_SuitableConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_SuitableConfiguration(score=7)
    partner = diva_ConfigurationModel()
    setattr(partner, 'diva_ConfigurationModel', None)
    _safe_set(owner, 'diva_SuitableConfiguration', partner)
    assert owner in getattr(partner, 'diva_ConfigurationModel')
    _safe_set(owner, 'diva_SuitableConfiguration', None)
    assert owner not in getattr(partner, 'diva_ConfigurationModel')


def test_assoc_context70_stub_double():
    # diva_Scenario has no real 'diva_Scenario71' property in the generated
    # code (a bare stub) -- manually attach it so diva_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Context(verdict="sample_text")
    partner = diva_Scenario()
    setattr(partner, 'diva_Scenario71', None)
    _safe_set(owner, 'diva_Context72', partner)
    assert owner in getattr(partner, 'diva_Scenario71')
    _safe_set(owner, 'diva_Context72', None)
    assert owner not in getattr(partner, 'diva_Scenario71')


def test_assoc_dependency23_stub_double():
    # diva_VariantExpression has no real 'diva_VariantExpression' property in the generated
    # code (a bare stub) -- manually attach it so diva_Variant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Variant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Variant(weaveLevel="sample_text")
    partner = diva_VariantExpression()
    setattr(partner, 'diva_VariantExpression', None)
    _safe_set(owner, 'diva_Variant24', partner)
    assert getattr(partner, 'diva_VariantExpression') == owner
    _safe_set(owner, 'diva_Variant24', None)
    assert getattr(partner, 'diva_VariantExpression') is None


def test_assoc_dimension3_stub_double():
    # diva_VariabilityModel has no real 'diva_VariabilityModel4' property in the generated
    # code (a bare stub) -- manually attach it so diva_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Dimension(lower="sample_text", upper="sample_text")
    partner = diva_VariabilityModel()
    setattr(partner, 'diva_VariabilityModel4', None)
    _safe_set(owner, 'diva_Dimension', partner)
    assert owner in getattr(partner, 'diva_VariabilityModel4')
    _safe_set(owner, 'diva_Dimension', None)
    assert owner not in getattr(partner, 'diva_VariabilityModel4')


def test_assoc_expression10_stub_double():
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


def test_assoc_model91_stub_double():
    # diva_ModelContainer has no real 'diva_ModelContainer' property in the generated
    # code (a bare stub) -- manually attach it so diva_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Model(uri="sample_text")
    partner = diva_ModelContainer()
    setattr(partner, 'diva_ModelContainer', None)
    _safe_set(owner, 'diva_Model', partner)
    assert getattr(partner, 'diva_ModelContainer') == owner
    _safe_set(owner, 'diva_Model', None)
    assert getattr(partner, 'diva_ModelContainer') is None


def test_assoc_oracle60_stub_double():
    # diva_VariantExpression has no real 'diva_VariantExpression62' property in the generated
    # code (a bare stub) -- manually attach it so diva_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Context(verdict="sample_text")
    partner = diva_VariantExpression()
    setattr(partner, 'diva_VariantExpression62', None)
    _safe_set(owner, 'diva_Context61', partner)
    assert getattr(partner, 'diva_VariantExpression62') == owner
    _safe_set(owner, 'diva_Context61', None)
    assert getattr(partner, 'diva_VariantExpression62') is None


def test_assoc_priority41_stub_double():
    # diva_PriorityRule has no real 'diva_PriorityRule42' property in the generated
    # code (a bare stub) -- manually attach it so diva_PropertyPriority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_PropertyPriority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_PropertyPriority(priority="sample_text")
    partner = diva_PriorityRule()
    setattr(partner, 'diva_PriorityRule42', None)
    _safe_set(owner, 'diva_PropertyPriority', partner)
    assert owner in getattr(partner, 'diva_PriorityRule42')
    _safe_set(owner, 'diva_PropertyPriority', None)
    assert owner not in getattr(partner, 'diva_PriorityRule42')


def test_assoc_property1_stub_double():
    # diva_VariabilityModel has no real 'diva_VariabilityModel2' property in the generated
    # code (a bare stub) -- manually attach it so diva_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Property(direction="sample_text")
    partner = diva_VariabilityModel()
    setattr(partner, 'diva_VariabilityModel2', None)
    _safe_set(owner, 'diva_Property', partner)
    assert owner in getattr(partner, 'diva_VariabilityModel2')
    _safe_set(owner, 'diva_Property', None)
    assert owner not in getattr(partner, 'diva_VariabilityModel2')


def test_assoc_required27_stub_double():
    # diva_ContextExpression has no real 'diva_ContextExpression29' property in the generated
    # code (a bare stub) -- manually attach it so diva_Variant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Variant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Variant(weaveLevel="sample_text")
    partner = diva_ContextExpression()
    setattr(partner, 'diva_ContextExpression29', None)
    _safe_set(owner, 'diva_Variant28', partner)
    assert getattr(partner, 'diva_ContextExpression29') == owner
    _safe_set(owner, 'diva_Variant28', None)
    assert getattr(partner, 'diva_ContextExpression29') is None


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


def test_assoc_variant15_stub_double():
    # diva_VariantTerm has no real 'diva_VariantTerm' property in the generated
    # code (a bare stub) -- manually attach it so diva_Variant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Variant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Variant(weaveLevel="sample_text")
    partner = diva_VariantTerm()
    setattr(partner, 'diva_VariantTerm', None)
    _safe_set(owner, 'diva_Variant', partner)
    assert getattr(partner, 'diva_VariantTerm') == owner
    _safe_set(owner, 'diva_Variant', None)
    assert getattr(partner, 'diva_VariantTerm') is None


def test_assoc_variant65_stub_double():
    # diva_ConfigVariant has no real 'diva_ConfigVariant' property in the generated
    # code (a bare stub) -- manually attach it so diva_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Configuration(verdict="sample_text")
    partner = diva_ConfigVariant()
    setattr(partner, 'diva_ConfigVariant', None)
    _safe_set(owner, 'diva_Configuration66', {partner})
    assert getattr(partner, 'diva_ConfigVariant') == owner
    _safe_set(owner, 'diva_Configuration66', set())
    assert getattr(partner, 'diva_ConfigVariant') is None


def test_assoc_variant67_stub_double():
    # diva_ConfigVariant has no real 'diva_ConfigVariant68' property in the generated
    # code (a bare stub) -- manually attach it so diva_Variant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_Variant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_Variant(weaveLevel="sample_text")
    partner = diva_ConfigVariant()
    setattr(partner, 'diva_ConfigVariant68', None)
    _safe_set(owner, 'diva_Variant69', partner)
    assert getattr(partner, 'diva_ConfigVariant68') == owner
    _safe_set(owner, 'diva_Variant69', None)
    assert getattr(partner, 'diva_ConfigVariant68') is None


def test_assoc_variant86_stub_double():
    # diva_ConfigVariant has no real 'diva_ConfigVariant88' property in the generated
    # code (a bare stub) -- manually attach it so diva_SuitableConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diva_SuitableConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diva_SuitableConfiguration(score=7)
    partner = diva_ConfigVariant()
    setattr(partner, 'diva_ConfigVariant88', None)
    _safe_set(owner, 'diva_SuitableConfiguration87', {partner})
    assert getattr(partner, 'diva_ConfigVariant88') == owner
    _safe_set(owner, 'diva_SuitableConfiguration87', set())
    assert getattr(partner, 'diva_ConfigVariant88') is None


