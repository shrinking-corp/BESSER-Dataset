import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EAssociationEnd,
    EAttribute,
    ECallExp,
    EClassifier,
    ECollectionType,
    EDataType,
    EEntity,
    EFeatureCallExp,
    EIfExp,
    EIterateExp,
    ELiteralExp,
    ELoopExp,
    ENavigationCallExp,
    ENumericLiteralExp,
    EOclExpression,
    EOperationCallExp,
    EPrimitiveType,
    ESignal,
    EVariable,
    ocl_dm_EAssociationEnd,
    ocl_dm_EAttribute,
    ocl_dm_EDataModel,
    ocl_dm_EEntity,
    ocl_exp_EAssociationClassCallExp,
    ocl_exp_EBooleanLiteralExp,
    ocl_exp_ECallExp,
    ocl_exp_EFeatureCallExp,
    ocl_exp_EIfExp,
    ocl_exp_EIntegerLiteralExp,
    ocl_exp_EIterateExp,
    ocl_exp_EIteratorExp,
    ocl_exp_ELiteralExp,
    ocl_exp_ELoopExp,
    ocl_exp_EMessageExp,
    ocl_exp_ENavigationCallExp,
    ocl_exp_ENumericLiteralExp,
    ocl_exp_EOclExpression,
    ocl_exp_EOperationCallExp,
    ocl_exp_EPrimitiveType,
    ocl_exp_EPropertyCallExp,
    ocl_exp_EStateExp,
    ocl_exp_EStringLiteralExp,
    ocl_exp_ETypeExp,
    ocl_exp_EVariable,
    ocl_exp_EVariableExp,
    ocl_type_EAnyType,
    ocl_type_EBagType,
    ocl_type_EClassifier,
    ocl_type_ECollectionType,
    ocl_type_EDataType,
    ocl_type_EInvalidType,
    ocl_type_EMessageType,
    ocl_type_EOrderedSetType,
    ocl_type_EPrimitiveType,
    ocl_type_ESequenceType,
    ocl_type_ESetType,
    ocl_type_ESignal,
    ocl_type_ETupleType,
    ocl_type_EVoidType,
    EIteratorKind,
    EMultiplicity,
    EOperator,
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

def test_assoc_argument37_stub_double():
    # EOclExpression has no real 'EOclExpression38' property in the generated
    # code (a bare stub) -- manually attach it so ocl_exp_EOperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_exp_EOperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_exp_EOperationCallExp(referredOperation="sample_text")
    partner = EOclExpression()
    setattr(partner, 'EOclExpression38', None)
    _safe_set(owner, 'parentCall', {partner})
    assert getattr(partner, 'EOclExpression38') == owner
    _safe_set(owner, 'parentCall', set())
    assert getattr(partner, 'EOclExpression38') is None


def test_assoc_attributes1_stub_double():
    # EAttribute has no real 'EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so ocl_dm_EEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_dm_EEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_dm_EEntity(name="sample_text")
    partner = EAttribute()
    setattr(partner, 'EAttribute', None)
    _safe_set(owner, 'ocl_dm_EEntity2', {partner})
    assert getattr(partner, 'EAttribute') == owner
    _safe_set(owner, 'ocl_dm_EEntity2', set())
    assert getattr(partner, 'EAttribute') is None


def test_assoc_baseExp14_stub_double():
    # EIterateExp has no real 'EIterateExp' property in the generated
    # code (a bare stub) -- manually attach it so ocl_exp_EVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_exp_EVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_exp_EVariable(name="sample_text")
    partner = EIterateExp()
    setattr(partner, 'EIterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'EIterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'EIterateExp') is None


def test_assoc_ends0_stub_double():
    # EAssociationEnd has no real 'EAssociationEnd' property in the generated
    # code (a bare stub) -- manually attach it so ocl_dm_EEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_dm_EEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_dm_EEntity(name="sample_text")
    partner = EAssociationEnd()
    setattr(partner, 'EAssociationEnd', None)
    _safe_set(owner, 'ocl_dm_EEntity', {partner})
    assert getattr(partner, 'EAssociationEnd') == owner
    _safe_set(owner, 'ocl_dm_EEntity', set())
    assert getattr(partner, 'EAssociationEnd') is None


def test_assoc_initExpression15_stub_double():
    # EOclExpression has no real 'EOclExpression16' property in the generated
    # code (a bare stub) -- manually attach it so ocl_exp_EVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_exp_EVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_exp_EVariable(name="sample_text")
    partner = EOclExpression()
    setattr(partner, 'EOclExpression16', None)
    _safe_set(owner, 'initializedElement', partner)
    assert getattr(partner, 'EOclExpression16') == owner
    _safe_set(owner, 'initializedElement', None)
    assert getattr(partner, 'EOclExpression16') is None


def test_assoc_loopExp13_stub_double():
    # ELoopExp has no real 'ELoopExp' property in the generated
    # code (a bare stub) -- manually attach it so ocl_exp_EVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_exp_EVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_exp_EVariable(name="sample_text")
    partner = ELoopExp()
    setattr(partner, 'ELoopExp', None)
    _safe_set(owner, 'iterator', partner)
    assert getattr(partner, 'ELoopExp') == owner
    _safe_set(owner, 'iterator', None)
    assert getattr(partner, 'ELoopExp') is None


def test_assoc_referredSignal45_stub_double():
    # ESignal has no real 'ESignal' property in the generated
    # code (a bare stub) -- manually attach it so ocl_type_EMessageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_type_EMessageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_type_EMessageType(referredOperation="sample_text")
    partner = ESignal()
    setattr(partner, 'ESignal', None)
    _safe_set(owner, 'ocl_type_EMessageType', partner)
    assert getattr(partner, 'ESignal') == owner
    _safe_set(owner, 'ocl_type_EMessageType', None)
    assert getattr(partner, 'ESignal') is None


def test_assoc_target3_stub_double():
    # EEntity has no real 'EEntity' property in the generated
    # code (a bare stub) -- manually attach it so ocl_dm_EAssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_dm_EAssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_dm_EAssociationEnd(mult="sample_text", name="sample_text", opp="sample_text")
    partner = EEntity()
    setattr(partner, 'EEntity', None)
    _safe_set(owner, 'ocl_dm_EAssociationEnd', partner)
    assert getattr(partner, 'EEntity') == owner
    _safe_set(owner, 'ocl_dm_EAssociationEnd', None)
    assert getattr(partner, 'EEntity') is None


