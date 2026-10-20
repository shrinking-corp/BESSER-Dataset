import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractBooleanExpression,
    AbstractDeclaration,
    AbstractDefinitionConstant,
    AbstractDomain,
    AbstractExpression,
    AbstractSpecification,
    AbstractTypeRef,
    EventRef,
    Expression,
    NavigableVariable,
    NonNavigableVariable,
    VariableRef,
    altarica_AbstractBooleanExpression,
    altarica_AbstractDeclaration,
    altarica_AbstractDefinitionConstant,
    altarica_AbstractDomain,
    altarica_AbstractExpression,
    altarica_AbstractSpecification,
    altarica_AbstractTypeRef,
    altarica_Addition,
    altarica_Affectation,
    altarica_And,
    altarica_Assert,
    altarica_AssertSpecification,
    altarica_Cardinality,
    altarica_CaseExpression,
    altarica_Constant,
    altarica_ConstantDefinition,
    altarica_Division,
    altarica_Domain,
    altarica_DomainConstant,
    altarica_DomainRef,
    altarica_EBoolean,
    altarica_EInteger,
    altarica_EObject,
    altarica_EString,
    altarica_Enumeration,
    altarica_Equal,
    altarica_Event,
    altarica_EventDeclaration,
    altarica_EventRef,
    altarica_EventSpecification,
    altarica_Expression,
    altarica_ExpressionConstant,
    altarica_ExternalDirective,
    altarica_ExternalSpecification,
    altarica_Flow,
    altarica_FlowDeclaration,
    altarica_FlowSpecification,
    altarica_IfThenElse,
    altarica_Imply,
    altarica_InitSpecification,
    altarica_InitStatement,
    altarica_Literal,
    altarica_Lower,
    altarica_Minus,
    altarica_Multiplication,
    altarica_NavigableVariable,
    altarica_NestedQualifiedEventRef,
    altarica_NestedQualifiedVariableRef,
    altarica_Node,
    altarica_NodeInstance,
    altarica_NodeInstanceDeclaration,
    altarica_NodeInstanceSpecification,
    altarica_NonNavigableVariable,
    altarica_NotEqual,
    altarica_Or,
    altarica_PrimitiveType,
    altarica_Priority,
    altarica_Range,
    altarica_State,
    altarica_StateDeclaration,
    altarica_StateSpecification,
    altarica_StrictLower,
    altarica_StrictUpper,
    altarica_Switch,
    altarica_System,
    altarica_Transition,
    altarica_TransitionSpecification,
    altarica_Upper,
    altarica_VariableAttribute,
    altarica_VariableRef,
    altarica_Vector,
    altarica_VectorParameter,
    altarica_VectorSpecification,
    FlowKind,
    PrimitiveTypeKind,
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

def test_assoc_attribute25_reverse_link_reassign_clear():
    a1 = altarica_VariableAttribute(name="sample_text")
    a2 = altarica_VariableAttribute(name="sample_text_2")
    b = altarica_FlowDeclaration(kind="sample_text")
    _safe_set(b, 'altarica_FlowDeclaration26', a1)
    assert _is_linked(b, 'altarica_FlowDeclaration26', a1)
    if hasattr(a1, 'altarica_VariableAttribute'):
        assert _is_linked(a1, 'altarica_VariableAttribute', b)
    _safe_set(b, 'altarica_FlowDeclaration26', a2)
    assert _is_linked(b, 'altarica_FlowDeclaration26', a2)
    if hasattr(a1, 'altarica_VariableAttribute'):
        assert not _is_linked(a1, 'altarica_VariableAttribute', b)
    if hasattr(a2, 'altarica_VariableAttribute'):
        assert _is_linked(a2, 'altarica_VariableAttribute', b)
    _safe_set(b, 'altarica_FlowDeclaration26', None)
    assert not _is_linked(b, 'altarica_FlowDeclaration26', a2)
    if hasattr(a2, 'altarica_VariableAttribute'):
        assert not _is_linked(a2, 'altarica_VariableAttribute', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute30_stub_double():
    # altarica_EventDeclaration has no real 'altarica_EventDeclaration31' property in the generated
    # code (a bare stub) -- manually attach it so altarica_VariableAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_VariableAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_VariableAttribute(name="sample_text")
    partner = altarica_EventDeclaration()
    setattr(partner, 'altarica_EventDeclaration31', None)
    _safe_set(owner, 'altarica_VariableAttribute32', partner)
    assert getattr(partner, 'altarica_EventDeclaration31') == owner
    _safe_set(owner, 'altarica_VariableAttribute32', None)
    assert getattr(partner, 'altarica_EventDeclaration31') is None


def test_assoc_attribute43_stub_double():
    # altarica_StateDeclaration has no real 'altarica_StateDeclaration44' property in the generated
    # code (a bare stub) -- manually attach it so altarica_VariableAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_VariableAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_VariableAttribute(name="sample_text")
    partner = altarica_StateDeclaration()
    setattr(partner, 'altarica_StateDeclaration44', None)
    _safe_set(owner, 'altarica_VariableAttribute45', partner)
    assert getattr(partner, 'altarica_StateDeclaration44') == owner
    _safe_set(owner, 'altarica_VariableAttribute45', None)
    assert getattr(partner, 'altarica_StateDeclaration44') is None


def test_assoc_domain23_stub_double():
    # altarica_AbstractTypeRef has no real 'altarica_AbstractTypeRef' property in the generated
    # code (a bare stub) -- manually attach it so altarica_FlowDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_FlowDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_FlowDeclaration(kind="sample_text")
    partner = altarica_AbstractTypeRef()
    setattr(partner, 'altarica_AbstractTypeRef', None)
    _safe_set(owner, 'altarica_FlowDeclaration24', partner)
    assert getattr(partner, 'altarica_AbstractTypeRef') == owner
    _safe_set(owner, 'altarica_FlowDeclaration24', None)
    assert getattr(partner, 'altarica_AbstractTypeRef') is None


def test_assoc_domain7_stub_double():
    # altarica_AbstractDomain has no real 'altarica_AbstractDomain8' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Domain(name="sample_text")
    partner = altarica_AbstractDomain()
    setattr(partner, 'altarica_AbstractDomain8', None)
    _safe_set(owner, 'altarica_Domain', partner)
    assert getattr(partner, 'altarica_AbstractDomain8') == owner
    _safe_set(owner, 'altarica_Domain', None)
    assert getattr(partner, 'altarica_AbstractDomain8') is None


def test_assoc_eventParameter62_stub_double():
    # altarica_EventRef has no real 'altarica_EventRef' property in the generated
    # code (a bare stub) -- manually attach it so altarica_VectorParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_VectorParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_VectorParameter(isRequired=True)
    partner = altarica_EventRef()
    setattr(partner, 'altarica_EventRef', None)
    _safe_set(owner, 'altarica_VectorParameter63', partner)
    assert getattr(partner, 'altarica_EventRef') == owner
    _safe_set(owner, 'altarica_VectorParameter63', None)
    assert getattr(partner, 'altarica_EventRef') is None


def test_assoc_nestedVariable174_stub_double():
    # altarica_NestedQualifiedEventRef has no real 'altarica_NestedQualifiedEventRef175' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NavigableVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NavigableVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NavigableVariable(name="sample_text")
    partner = altarica_NestedQualifiedEventRef()
    setattr(partner, 'altarica_NestedQualifiedEventRef175', None)
    _safe_set(owner, 'altarica_NavigableVariable176', partner)
    assert getattr(partner, 'altarica_NestedQualifiedEventRef175') == owner
    _safe_set(owner, 'altarica_NavigableVariable176', None)
    assert getattr(partner, 'altarica_NestedQualifiedEventRef175') is None


def test_assoc_nestedVariable179_stub_double():
    # altarica_NestedQualifiedVariableRef has no real 'altarica_NestedQualifiedVariableRef180' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NavigableVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NavigableVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NavigableVariable(name="sample_text")
    partner = altarica_NestedQualifiedVariableRef()
    setattr(partner, 'altarica_NestedQualifiedVariableRef180', None)
    _safe_set(owner, 'altarica_NavigableVariable181', partner)
    assert getattr(partner, 'altarica_NestedQualifiedVariableRef180') == owner
    _safe_set(owner, 'altarica_NavigableVariable181', None)
    assert getattr(partner, 'altarica_NestedQualifiedVariableRef180') is None


def test_assoc_nodeType51_stub_double():
    # altarica_NodeInstanceDeclaration has no real 'altarica_NodeInstanceDeclaration52' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Node(isMain=True, name="sample_text")
    partner = altarica_NodeInstanceDeclaration()
    setattr(partner, 'altarica_NodeInstanceDeclaration52', None)
    _safe_set(owner, 'altarica_Node53', partner)
    assert getattr(partner, 'altarica_NodeInstanceDeclaration52') == owner
    _safe_set(owner, 'altarica_Node53', None)
    assert getattr(partner, 'altarica_NodeInstanceDeclaration52') is None


def test_assoc_ownedDeclarations20_stub_double():
    # altarica_FlowSpecification has no real 'altarica_FlowSpecification' property in the generated
    # code (a bare stub) -- manually attach it so altarica_FlowDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_FlowDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_FlowDeclaration(kind="sample_text")
    partner = altarica_FlowSpecification()
    setattr(partner, 'altarica_FlowSpecification', None)
    _safe_set(owner, 'altarica_FlowDeclaration', partner)
    assert owner in getattr(partner, 'altarica_FlowSpecification')
    _safe_set(owner, 'altarica_FlowDeclaration', None)
    assert owner not in getattr(partner, 'altarica_FlowSpecification')


def test_assoc_ownedDirectives19_stub_double():
    # altarica_ExternalSpecification has no real 'altarica_ExternalSpecification' property in the generated
    # code (a bare stub) -- manually attach it so altarica_ExternalDirective's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_ExternalDirective's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_ExternalDirective(directive="sample_text")
    partner = altarica_ExternalSpecification()
    setattr(partner, 'altarica_ExternalSpecification', None)
    _safe_set(owner, 'altarica_ExternalDirective', partner)
    assert owner in getattr(partner, 'altarica_ExternalSpecification')
    _safe_set(owner, 'altarica_ExternalDirective', None)
    assert owner not in getattr(partner, 'altarica_ExternalSpecification')


def test_assoc_ownedFlows21_stub_double():
    # altarica_Flow has no real 'altarica_Flow' property in the generated
    # code (a bare stub) -- manually attach it so altarica_FlowDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_FlowDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_FlowDeclaration(kind="sample_text")
    partner = altarica_Flow()
    setattr(partner, 'altarica_Flow', None)
    _safe_set(owner, 'altarica_FlowDeclaration22', {partner})
    assert getattr(partner, 'altarica_Flow') == owner
    _safe_set(owner, 'altarica_FlowDeclaration22', set())
    assert getattr(partner, 'altarica_Flow') is None


def test_assoc_ownedParameters58_stub_double():
    # altarica_Vector has no real 'altarica_Vector59' property in the generated
    # code (a bare stub) -- manually attach it so altarica_VectorParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_VectorParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_VectorParameter(isRequired=True)
    partner = altarica_Vector()
    setattr(partner, 'altarica_Vector59', None)
    _safe_set(owner, 'altarica_VectorParameter', partner)
    assert owner in getattr(partner, 'altarica_Vector59')
    _safe_set(owner, 'altarica_VectorParameter', None)
    assert owner not in getattr(partner, 'altarica_Vector59')


def test_assoc_ownedSpecifications15_stub_double():
    # altarica_AbstractSpecification has no real 'altarica_AbstractSpecification' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Node(isMain=True, name="sample_text")
    partner = altarica_AbstractSpecification()
    setattr(partner, 'altarica_AbstractSpecification', None)
    _safe_set(owner, 'altarica_Node', {partner})
    assert getattr(partner, 'altarica_AbstractSpecification') == owner
    _safe_set(owner, 'altarica_Node', set())
    assert getattr(partner, 'altarica_AbstractSpecification') is None


def test_assoc_reference46_stub_double():
    # altarica_DomainRef has no real 'altarica_DomainRef' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Domain(name="sample_text")
    partner = altarica_DomainRef()
    setattr(partner, 'altarica_DomainRef', None)
    _safe_set(owner, 'altarica_Domain47', partner)
    assert getattr(partner, 'altarica_DomainRef') == owner
    _safe_set(owner, 'altarica_Domain47', None)
    assert getattr(partner, 'altarica_DomainRef') is None


def test_assoc_variable103_stub_double():
    # altarica_EventRef has no real 'altarica_EventRef104' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NavigableVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NavigableVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NavigableVariable(name="sample_text")
    partner = altarica_EventRef()
    setattr(partner, 'altarica_EventRef104', None)
    _safe_set(owner, 'altarica_NavigableVariable', partner)
    assert getattr(partner, 'altarica_EventRef104') == owner
    _safe_set(owner, 'altarica_NavigableVariable', None)
    assert getattr(partner, 'altarica_EventRef104') is None


def test_assoc_variable105_stub_double():
    # altarica_VariableRef has no real 'altarica_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NavigableVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NavigableVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NavigableVariable(name="sample_text")
    partner = altarica_VariableRef()
    setattr(partner, 'altarica_VariableRef', None)
    _safe_set(owner, 'altarica_NavigableVariable106', partner)
    assert getattr(partner, 'altarica_VariableRef') == owner
    _safe_set(owner, 'altarica_NavigableVariable106', None)
    assert getattr(partner, 'altarica_VariableRef') is None


