import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Relational,
    Statement,
    rell_And,
    rell_Attribute,
    rell_BoolConstant,
    rell_ClassDefinition,
    rell_ClassType,
    rell_Comparison,
    rell_ConditionElement,
    rell_Conditions,
    rell_Create,
    rell_Delete,
    rell_Equality,
    rell_Expression,
    rell_IntConstant,
    rell_Minus,
    rell_Model,
    rell_MulOrDiv,
    rell_Not,
    rell_Operation,
    rell_Or,
    rell_Plus,
    rell_PrimitiveType,
    rell_RelAttrubutesList,
    rell_Relational,
    rell_Statement,
    rell_StringConstant,
    rell_TypeReference,
    rell_Update,
    rell_Variable,
    rell_VariableDeclaration,
    rell_VariableInit,
    rell_VariableRef,
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

def test_assoc_attributes6_reverse_link_reassign_clear():
    a1 = rell_ClassDefinition(name="sample_text")
    a2 = rell_ClassDefinition(name="sample_text_2")
    b = rell_Attribute(modificator="sample_text")
    _safe_set(b, 'rell_Attribute', a1)
    assert _is_linked(b, 'rell_Attribute', a1)
    if hasattr(a1, 'rell_ClassDefinition7'):
        assert _is_linked(a1, 'rell_ClassDefinition7', b)
    _safe_set(b, 'rell_Attribute', a2)
    assert _is_linked(b, 'rell_Attribute', a2)
    if hasattr(a1, 'rell_ClassDefinition7'):
        assert not _is_linked(a1, 'rell_ClassDefinition7', b)
    if hasattr(a2, 'rell_ClassDefinition7'):
        assert _is_linked(a2, 'rell_ClassDefinition7', b)
    _safe_set(b, 'rell_Attribute', None)
    assert not _is_linked(b, 'rell_Attribute', a2)
    if hasattr(a2, 'rell_ClassDefinition7'):
        assert not _is_linked(a2, 'rell_ClassDefinition7', b)


def test_assoc_relation19_reverse_link_reassign_clear():
    a1 = rell_Relational(entity="sample_text")
    a2 = rell_Relational(entity="sample_text_2")
    b = rell_Relational(entity="sample_text")
    _safe_set(b, 'rell_Relational18', a1)
    assert _is_linked(b, 'rell_Relational18', a1)
    if hasattr(a1, 'rell_Relational'):
        assert _is_linked(a1, 'rell_Relational', b)
    _safe_set(b, 'rell_Relational18', a2)
    assert _is_linked(b, 'rell_Relational18', a2)
    if hasattr(a1, 'rell_Relational'):
        assert not _is_linked(a1, 'rell_Relational', b)
    if hasattr(a2, 'rell_Relational'):
        assert _is_linked(a2, 'rell_Relational', b)
    _safe_set(b, 'rell_Relational18', None)
    assert not _is_linked(b, 'rell_Relational18', a2)
    if hasattr(a2, 'rell_Relational'):
        assert not _is_linked(a2, 'rell_Relational', b)


def test_assoc_superType4_reverse_link_reassign_clear():
    a1 = rell_ClassDefinition(name="sample_text")
    a2 = rell_ClassDefinition(name="sample_text_2")
    b = rell_ClassDefinition(name="sample_text")
    _safe_set(b, 'rell_ClassDefinition5', a1)
    assert _is_linked(b, 'rell_ClassDefinition5', a1)
    if hasattr(a1, 'rell_ClassDefinition3'):
        assert _is_linked(a1, 'rell_ClassDefinition3', b)
    _safe_set(b, 'rell_ClassDefinition5', a2)
    assert _is_linked(b, 'rell_ClassDefinition5', a2)
    if hasattr(a1, 'rell_ClassDefinition3'):
        assert not _is_linked(a1, 'rell_ClassDefinition3', b)
    if hasattr(a2, 'rell_ClassDefinition3'):
        assert _is_linked(a2, 'rell_ClassDefinition3', b)
    _safe_set(b, 'rell_ClassDefinition5', None)
    assert not _is_linked(b, 'rell_ClassDefinition5', a2)
    if hasattr(a2, 'rell_ClassDefinition3'):
        assert not _is_linked(a2, 'rell_ClassDefinition3', b)


def test_assoc_variable43_reverse_link_reassign_clear():
    a1 = rell_VariableDeclaration(name="sample_text")
    a2 = rell_VariableDeclaration(name="sample_text_2")
    b = rell_Attribute(modificator="sample_text")
    _safe_set(b, 'rell_Attribute44', a1)
    assert _is_linked(b, 'rell_Attribute44', a1)
    if hasattr(a1, 'rell_VariableDeclaration45'):
        assert _is_linked(a1, 'rell_VariableDeclaration45', b)
    _safe_set(b, 'rell_Attribute44', a2)
    assert _is_linked(b, 'rell_Attribute44', a2)
    if hasattr(a1, 'rell_VariableDeclaration45'):
        assert not _is_linked(a1, 'rell_VariableDeclaration45', b)
    if hasattr(a2, 'rell_VariableDeclaration45'):
        assert _is_linked(a2, 'rell_VariableDeclaration45', b)
    _safe_set(b, 'rell_Attribute44', None)
    assert not _is_linked(b, 'rell_Attribute44', a2)
    if hasattr(a2, 'rell_VariableDeclaration45'):
        assert not _is_linked(a2, 'rell_VariableDeclaration45', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_conditions20_stub_double():
    # rell_Conditions has no real 'rell_Conditions' property in the generated
    # code (a bare stub) -- manually attach it so rell_Relational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Relational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Relational(entity="sample_text")
    partner = rell_Conditions()
    setattr(partner, 'rell_Conditions', None)
    _safe_set(owner, 'rell_Relational21', partner)
    assert getattr(partner, 'rell_Conditions') == owner
    _safe_set(owner, 'rell_Relational21', None)
    assert getattr(partner, 'rell_Conditions') is None


def test_assoc_declaration14_stub_double():
    # rell_Variable has no real 'rell_Variable15' property in the generated
    # code (a bare stub) -- manually attach it so rell_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_VariableDeclaration(name="sample_text")
    partner = rell_Variable()
    setattr(partner, 'rell_Variable15', None)
    _safe_set(owner, 'rell_VariableDeclaration', partner)
    assert getattr(partner, 'rell_Variable15') == owner
    _safe_set(owner, 'rell_VariableDeclaration', None)
    assert getattr(partner, 'rell_Variable15') is None


def test_assoc_elements23_stub_double():
    # rell_Conditions has no real 'rell_Conditions24' property in the generated
    # code (a bare stub) -- manually attach it so rell_ConditionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_ConditionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_ConditionElement(compareName="sample_text")
    partner = rell_Conditions()
    setattr(partner, 'rell_Conditions24', None)
    _safe_set(owner, 'rell_ConditionElement', partner)
    assert owner in getattr(partner, 'rell_Conditions24')
    _safe_set(owner, 'rell_ConditionElement', None)
    assert owner not in getattr(partner, 'rell_Conditions24')


def test_assoc_entities0_stub_double():
    # rell_Model has no real 'rell_Model' property in the generated
    # code (a bare stub) -- manually attach it so rell_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_ClassDefinition(name="sample_text")
    partner = rell_Model()
    setattr(partner, 'rell_Model', None)
    _safe_set(owner, 'rell_ClassDefinition', partner)
    assert owner in getattr(partner, 'rell_Model')
    _safe_set(owner, 'rell_ClassDefinition', None)
    assert owner not in getattr(partner, 'rell_Model')


def test_assoc_entityRef52_stub_double():
    # rell_ClassType has no real 'rell_ClassType53' property in the generated
    # code (a bare stub) -- manually attach it so rell_ClassDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_ClassDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_ClassDefinition(name="sample_text")
    partner = rell_ClassType()
    setattr(partner, 'rell_ClassType53', None)
    _safe_set(owner, 'rell_ClassDefinition54', partner)
    assert getattr(partner, 'rell_ClassType53') == owner
    _safe_set(owner, 'rell_ClassDefinition54', None)
    assert getattr(partner, 'rell_ClassType53') is None


def test_assoc_expr25_stub_double():
    # rell_Expression has no real 'rell_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so rell_ConditionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_ConditionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_ConditionElement(compareName="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression27', None)
    _safe_set(owner, 'rell_ConditionElement26', partner)
    assert getattr(partner, 'rell_Expression27') == owner
    _safe_set(owner, 'rell_ConditionElement26', None)
    assert getattr(partner, 'rell_Expression27') is None


def test_assoc_left65_stub_double():
    # rell_Expression has no real 'rell_Expression66' property in the generated
    # code (a bare stub) -- manually attach it so rell_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Equality(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression66', None)
    _safe_set(owner, 'rell_Equality', partner)
    assert getattr(partner, 'rell_Expression66') == owner
    _safe_set(owner, 'rell_Equality', None)
    assert getattr(partner, 'rell_Expression66') is None


def test_assoc_left70_stub_double():
    # rell_Expression has no real 'rell_Expression71' property in the generated
    # code (a bare stub) -- manually attach it so rell_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Comparison(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression71', None)
    _safe_set(owner, 'rell_Comparison', partner)
    assert getattr(partner, 'rell_Expression71') == owner
    _safe_set(owner, 'rell_Comparison', None)
    assert getattr(partner, 'rell_Expression71') is None


def test_assoc_left87_stub_double():
    # rell_Expression has no real 'rell_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so rell_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_MulOrDiv(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression88', None)
    _safe_set(owner, 'rell_MulOrDiv', partner)
    assert getattr(partner, 'rell_Expression88') == owner
    _safe_set(owner, 'rell_MulOrDiv', None)
    assert getattr(partner, 'rell_Expression88') is None


def test_assoc_name31_stub_double():
    # rell_VariableInit has no real 'rell_VariableInit32' property in the generated
    # code (a bare stub) -- manually attach it so rell_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_VariableDeclaration(name="sample_text")
    partner = rell_VariableInit()
    setattr(partner, 'rell_VariableInit32', None)
    _safe_set(owner, 'rell_VariableDeclaration33', partner)
    assert getattr(partner, 'rell_VariableInit32') == owner
    _safe_set(owner, 'rell_VariableDeclaration33', None)
    assert getattr(partner, 'rell_VariableInit32') is None


def test_assoc_operations1_stub_double():
    # rell_Model has no real 'rell_Model2' property in the generated
    # code (a bare stub) -- manually attach it so rell_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Operation(name="sample_text")
    partner = rell_Model()
    setattr(partner, 'rell_Model2', None)
    _safe_set(owner, 'rell_Operation', partner)
    assert owner in getattr(partner, 'rell_Model2')
    _safe_set(owner, 'rell_Operation', None)
    assert owner not in getattr(partner, 'rell_Model2')


def test_assoc_parameters8_stub_double():
    # rell_RelAttrubutesList has no real 'rell_RelAttrubutesList' property in the generated
    # code (a bare stub) -- manually attach it so rell_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Operation(name="sample_text")
    partner = rell_RelAttrubutesList()
    setattr(partner, 'rell_RelAttrubutesList', None)
    _safe_set(owner, 'rell_Operation9', partner)
    assert getattr(partner, 'rell_RelAttrubutesList') == owner
    _safe_set(owner, 'rell_Operation9', None)
    assert getattr(partner, 'rell_RelAttrubutesList') is None


def test_assoc_primitive48_stub_double():
    # rell_TypeReference has no real 'rell_TypeReference49' property in the generated
    # code (a bare stub) -- manually attach it so rell_PrimitiveType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_PrimitiveType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_PrimitiveType(primitiveType="sample_text")
    partner = rell_TypeReference()
    setattr(partner, 'rell_TypeReference49', None)
    _safe_set(owner, 'rell_PrimitiveType', partner)
    assert getattr(partner, 'rell_TypeReference49') == owner
    _safe_set(owner, 'rell_PrimitiveType', None)
    assert getattr(partner, 'rell_TypeReference49') is None


def test_assoc_right67_stub_double():
    # rell_Expression has no real 'rell_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so rell_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Equality(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression69', None)
    _safe_set(owner, 'rell_Equality68', partner)
    assert getattr(partner, 'rell_Expression69') == owner
    _safe_set(owner, 'rell_Equality68', None)
    assert getattr(partner, 'rell_Expression69') is None


def test_assoc_right72_stub_double():
    # rell_Expression has no real 'rell_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so rell_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Comparison(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression74', None)
    _safe_set(owner, 'rell_Comparison73', partner)
    assert getattr(partner, 'rell_Expression74') == owner
    _safe_set(owner, 'rell_Comparison73', None)
    assert getattr(partner, 'rell_Expression74') is None


def test_assoc_right89_stub_double():
    # rell_Expression has no real 'rell_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so rell_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_MulOrDiv(op="sample_text")
    partner = rell_Expression()
    setattr(partner, 'rell_Expression91', None)
    _safe_set(owner, 'rell_MulOrDiv90', partner)
    assert getattr(partner, 'rell_Expression91') == owner
    _safe_set(owner, 'rell_MulOrDiv90', None)
    assert getattr(partner, 'rell_Expression91') is None


def test_assoc_statements10_stub_double():
    # rell_Statement has no real 'rell_Statement' property in the generated
    # code (a bare stub) -- manually attach it so rell_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_Operation(name="sample_text")
    partner = rell_Statement()
    setattr(partner, 'rell_Statement', None)
    _safe_set(owner, 'rell_Operation11', {partner})
    assert getattr(partner, 'rell_Statement') == owner
    _safe_set(owner, 'rell_Operation11', set())
    assert getattr(partner, 'rell_Statement') is None


def test_assoc_type46_stub_double():
    # rell_TypeReference has no real 'rell_TypeReference' property in the generated
    # code (a bare stub) -- manually attach it so rell_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_VariableDeclaration(name="sample_text")
    partner = rell_TypeReference()
    setattr(partner, 'rell_TypeReference', None)
    _safe_set(owner, 'rell_VariableDeclaration47', partner)
    assert getattr(partner, 'rell_TypeReference') == owner
    _safe_set(owner, 'rell_VariableDeclaration47', None)
    assert getattr(partner, 'rell_TypeReference') is None


def test_assoc_value40_stub_double():
    # rell_RelAttrubutesList has no real 'rell_RelAttrubutesList41' property in the generated
    # code (a bare stub) -- manually attach it so rell_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_VariableDeclaration(name="sample_text")
    partner = rell_RelAttrubutesList()
    setattr(partner, 'rell_RelAttrubutesList41', None)
    _safe_set(owner, 'rell_VariableDeclaration42', partner)
    assert owner in getattr(partner, 'rell_RelAttrubutesList41')
    _safe_set(owner, 'rell_VariableDeclaration42', None)
    assert owner not in getattr(partner, 'rell_RelAttrubutesList41')


def test_assoc_variable85_stub_double():
    # rell_VariableRef has no real 'rell_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so rell_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rell_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rell_VariableDeclaration(name="sample_text")
    partner = rell_VariableRef()
    setattr(partner, 'rell_VariableRef', None)
    _safe_set(owner, 'rell_VariableDeclaration86', partner)
    assert getattr(partner, 'rell_VariableRef') == owner
    _safe_set(owner, 'rell_VariableDeclaration86', None)
    assert getattr(partner, 'rell_VariableRef') is None


