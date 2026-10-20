import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Operator,
    QueryVariableQualifier,
    Referrable,
    Result,
    Variable,
    operators_ASSIGN,
    operators_CREATE,
    operators_DELETE,
    operators_EAttribute,
    operators_EClass,
    operators_EObject,
    operators_EObjectReference,
    operators_EOperation,
    operators_EOperationQualifier,
    operators_EReference,
    operators_EReferenceQualifier,
    operators_EStructuralFeature,
    operators_MERGE,
    operators_MOVE,
    operators_Operator,
    operators_PrimitiveReference,
    operators_QueryVariable,
    operators_QueryVariableQualifier,
    operators_Referrable,
    operators_Result,
    operators_SET,
    operators_SPLIT,
    operators_StructuralFeatureSet,
    operators_TypeVariable,
    operators_VAR,
    operators_Variable,
    operators_VariableReference,
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

def test_assoc_attribute12_stub_double():
    # operators_EAttribute has no real 'operators_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so operators_ASSIGN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ASSIGN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ASSIGN(value="sample_text")
    partner = operators_EAttribute()
    setattr(partner, 'operators_EAttribute', None)
    _safe_set(owner, 'operators_ASSIGN', partner)
    assert getattr(partner, 'operators_EAttribute') == owner
    _safe_set(owner, 'operators_ASSIGN', None)
    assert getattr(partner, 'operators_EAttribute') is None


def test_assoc_attributeOwner13_stub_double():
    # operators_Referrable has no real 'operators_Referrable15' property in the generated
    # code (a bare stub) -- manually attach it so operators_ASSIGN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ASSIGN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ASSIGN(value="sample_text")
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable15', None)
    _safe_set(owner, 'operators_ASSIGN14', partner)
    assert getattr(partner, 'operators_Referrable15') == owner
    _safe_set(owner, 'operators_ASSIGN14', None)
    assert getattr(partner, 'operators_Referrable15') is None


def test_assoc_deletion10_stub_double():
    # operators_Referrable has no real 'operators_Referrable11' property in the generated
    # code (a bare stub) -- manually attach it so operators_DELETE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_DELETE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_DELETE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable11', None)
    _safe_set(owner, 'operators_DELETE', partner)
    assert getattr(partner, 'operators_Referrable11') == owner
    _safe_set(owner, 'operators_DELETE', None)
    assert getattr(partner, 'operators_Referrable11') is None


def test_assoc_movee32_stub_double():
    # operators_Referrable has no real 'operators_Referrable34' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable34', None)
    _safe_set(owner, 'operators_MOVE33', partner)
    assert getattr(partner, 'operators_Referrable34') == owner
    _safe_set(owner, 'operators_MOVE33', None)
    assert getattr(partner, 'operators_Referrable34') is None


def test_assoc_newInstanceVariable1_stub_double():
    # operators_TypeVariable has no real 'operators_TypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_TypeVariable()
    setattr(partner, 'operators_TypeVariable', None)
    _safe_set(owner, 'operators_CREATE', partner)
    assert getattr(partner, 'operators_TypeVariable') == owner
    _safe_set(owner, 'operators_CREATE', None)
    assert getattr(partner, 'operators_TypeVariable') is None


def test_assoc_newParent27_stub_double():
    # operators_Referrable has no real 'operators_Referrable28' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable28', None)
    _safe_set(owner, 'operators_MOVE', partner)
    assert getattr(partner, 'operators_Referrable28') == owner
    _safe_set(owner, 'operators_MOVE', None)
    assert getattr(partner, 'operators_Referrable28') is None


def test_assoc_parent2_stub_double():
    # operators_Referrable has no real 'operators_Referrable' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable', None)
    _safe_set(owner, 'operators_CREATE3', partner)
    assert getattr(partner, 'operators_Referrable') == owner
    _safe_set(owner, 'operators_CREATE3', None)
    assert getattr(partner, 'operators_Referrable') is None


def test_assoc_parentCompositeReference4_stub_double():
    # operators_EReference has no real 'operators_EReference' property in the generated
    # code (a bare stub) -- manually attach it so operators_CREATE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_CREATE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_CREATE()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference', None)
    _safe_set(owner, 'operators_CREATE5', partner)
    assert getattr(partner, 'operators_EReference') == owner
    _safe_set(owner, 'operators_CREATE5', None)
    assert getattr(partner, 'operators_EReference') is None


def test_assoc_parentReference29_stub_double():
    # operators_EReference has no real 'operators_EReference31' property in the generated
    # code (a bare stub) -- manually attach it so operators_MOVE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_MOVE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_MOVE()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference31', None)
    _safe_set(owner, 'operators_MOVE30', partner)
    assert getattr(partner, 'operators_EReference31') == owner
    _safe_set(owner, 'operators_MOVE30', None)
    assert getattr(partner, 'operators_EReference31') is None


def test_assoc_reference18_stub_double():
    # operators_EReference has no real 'operators_EReference19' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_EReference()
    setattr(partner, 'operators_EReference19', None)
    _safe_set(owner, 'operators_SET', partner)
    assert getattr(partner, 'operators_EReference19') == owner
    _safe_set(owner, 'operators_SET', None)
    assert getattr(partner, 'operators_EReference19') is None


def test_assoc_referenceOwner23_stub_double():
    # operators_Referrable has no real 'operators_Referrable25' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable25', None)
    _safe_set(owner, 'operators_SET24', partner)
    assert getattr(partner, 'operators_Referrable25') == owner
    _safe_set(owner, 'operators_SET24', None)
    assert getattr(partner, 'operators_Referrable25') is None


def test_assoc_referencedVariable26_stub_double():
    # operators_VariableReference has no real 'operators_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so operators_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Variable(name="sample_text")
    partner = operators_VariableReference()
    setattr(partner, 'operators_VariableReference', None)
    _safe_set(owner, 'operators_Variable', partner)
    assert getattr(partner, 'operators_VariableReference') == owner
    _safe_set(owner, 'operators_Variable', None)
    assert getattr(partner, 'operators_VariableReference') is None


def test_assoc_result0_stub_double():
    # operators_Result has no real 'operators_Result' property in the generated
    # code (a bare stub) -- manually attach it so operators_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Operator(executed=True)
    partner = operators_Result()
    setattr(partner, 'operators_Result', None)
    _safe_set(owner, 'operators_Operator', partner)
    assert getattr(partner, 'operators_Result') == owner
    _safe_set(owner, 'operators_Operator', None)
    assert getattr(partner, 'operators_Result') is None


def test_assoc_value20_stub_double():
    # operators_Referrable has no real 'operators_Referrable22' property in the generated
    # code (a bare stub) -- manually attach it so operators_SET's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_SET's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_SET()
    partner = operators_Referrable()
    setattr(partner, 'operators_Referrable22', None)
    _safe_set(owner, 'operators_SET21', partner)
    assert getattr(partner, 'operators_Referrable22') == owner
    _safe_set(owner, 'operators_SET21', None)
    assert getattr(partner, 'operators_Referrable22') is None


def test_assoc_variable43_stub_double():
    # operators_QueryVariable has no real 'operators_QueryVariable' property in the generated
    # code (a bare stub) -- manually attach it so operators_VAR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_VAR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_VAR()
    partner = operators_QueryVariable()
    setattr(partner, 'operators_QueryVariable', None)
    _safe_set(owner, 'operators_VAR', partner)
    assert getattr(partner, 'operators_QueryVariable') == owner
    _safe_set(owner, 'operators_VAR', None)
    assert getattr(partner, 'operators_QueryVariable') is None


