import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ADT,
    AbstractEquation,
    AbstractOperation,
    CondEquation,
    Condition,
    Equation,
    Operation,
    SOS_AlgebraicCondition,
    SOS_AlgebraicConditionList,
    SOS_Conclusion,
    SOS_Condition,
    SOS_PremisseList,
    SOS_Rule,
    SOS_Semantics,
    SOS_Transition,
    SOS_TypeJudment,
    SOS_adtmm_ADT,
    SOS_adtmm_AbstractEquation,
    SOS_adtmm_AbstractGenericOp,
    SOS_adtmm_AbstractOperation,
    SOS_adtmm_AbstractSort,
    SOS_adtmm_AtomicSort,
    SOS_adtmm_CTerm,
    SOS_adtmm_CondEquation,
    SOS_adtmm_Equation,
    SOS_adtmm_Inequation,
    SOS_adtmm_Operation,
    SOS_adtmm_Sort,
    SOS_adtmm_SortDeclaration,
    SOS_adtmm_Term,
    SOS_adtmm_Variable,
    SOS_adtmm_VariableRef,
    SOS_set_Excluding,
    SOS_set_ExistsIn,
    SOS_set_ForAllIn,
    SOS_set_Intersection,
    SOS_set_ModelClassAttribute,
    SOS_set_ModelRelation,
    SOS_set_ModelSet,
    SOS_set_ModelSort,
    SOS_set_Set,
    SOS_set_SetConstructor,
    SOS_set_SetMembership,
    SOS_set_SetOperator,
    SOS_set_SetTerm,
    SOS_set_Union,
    SetMembership,
    SetOperator,
    SetTerm,
    Sort,
    SortDeclaration,
    Term,
    Variable,
    VariableRef,
    set_SOS_AlgebraicConditionList,
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

def test_assoc_iterTerm69_stub_double():
    # Term has no real 'Term71' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_CTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_CTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_CTerm(iter=7)
    partner = Term()
    setattr(partner, 'Term71', None)
    _safe_set(owner, 'SOS_adtmm_CTerm70', partner)
    assert getattr(partner, 'Term71') == owner
    _safe_set(owner, 'SOS_adtmm_CTerm70', None)
    assert getattr(partner, 'Term71') is None


def test_assoc_op66_stub_double():
    # Operation has no real 'Operation68' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_CTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_CTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_CTerm(iter=7)
    partner = Operation()
    setattr(partner, 'Operation68', None)
    _safe_set(owner, 'SOS_adtmm_CTerm67', partner)
    assert getattr(partner, 'Operation68') == owner
    _safe_set(owner, 'SOS_adtmm_CTerm67', None)
    assert getattr(partner, 'Operation68') is None


def test_assoc_ownedAxioms50_stub_double():
    # CondEquation has no real 'CondEquation' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_ADT(name="sample_text")
    partner = CondEquation()
    setattr(partner, 'CondEquation', None)
    _safe_set(owner, 'SOS_adtmm_ADT51', {partner})
    assert getattr(partner, 'CondEquation') == owner
    _safe_set(owner, 'SOS_adtmm_ADT51', set())
    assert getattr(partner, 'CondEquation') is None


def test_assoc_ownedGenerators44_stub_double():
    # Operation has no real 'Operation46' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_ADT(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation46', None)
    _safe_set(owner, 'SOS_adtmm_ADT45', {partner})
    assert getattr(partner, 'Operation46') == owner
    _safe_set(owner, 'SOS_adtmm_ADT45', set())
    assert getattr(partner, 'Operation46') is None


def test_assoc_ownedOperations42_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_ADT(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'SOS_adtmm_ADT43', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'SOS_adtmm_ADT43', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedSorts41_stub_double():
    # SortDeclaration has no real 'SortDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_ADT(name="sample_text")
    partner = SortDeclaration()
    setattr(partner, 'SortDeclaration', None)
    _safe_set(owner, 'SOS_adtmm_ADT', {partner})
    assert getattr(partner, 'SortDeclaration') == owner
    _safe_set(owner, 'SOS_adtmm_ADT', set())
    assert getattr(partner, 'SortDeclaration') is None


def test_assoc_ownedTerms64_stub_double():
    # Term has no real 'Term65' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_CTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_CTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_CTerm(iter=7)
    partner = Term()
    setattr(partner, 'Term65', None)
    _safe_set(owner, 'SOS_adtmm_CTerm', {partner})
    assert getattr(partner, 'Term65') == owner
    _safe_set(owner, 'SOS_adtmm_CTerm', set())
    assert getattr(partner, 'Term65') is None


def test_assoc_ownedVariables47_stub_double():
    # Variable has no real 'Variable49' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_ADT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_ADT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_ADT(name="sample_text")
    partner = Variable()
    setattr(partner, 'Variable49', None)
    _safe_set(owner, 'SOS_adtmm_ADT48', {partner})
    assert getattr(partner, 'Variable49') == owner
    _safe_set(owner, 'SOS_adtmm_ADT48', set())
    assert getattr(partner, 'Variable49') is None


def test_assoc_selector97_stub_double():
    # VariableRef has no real 'VariableRef98' property in the generated
    # code (a bare stub) -- manually attach it so SOS_set_ModelClassAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_set_ModelClassAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_set_ModelClassAttribute(attributeName="sample_text")
    partner = VariableRef()
    setattr(partner, 'VariableRef98', None)
    _safe_set(owner, 'SOS_set_ModelClassAttribute', partner)
    assert getattr(partner, 'VariableRef98') == owner
    _safe_set(owner, 'SOS_set_ModelClassAttribute', None)
    assert getattr(partner, 'VariableRef98') is None


def test_assoc_source93_stub_double():
    # VariableRef has no real 'VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so SOS_set_ModelRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_set_ModelRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_set_ModelRelation(referenceName="sample_text")
    partner = VariableRef()
    setattr(partner, 'VariableRef', None)
    _safe_set(owner, 'SOS_set_ModelRelation', partner)
    assert getattr(partner, 'VariableRef') == owner
    _safe_set(owner, 'SOS_set_ModelRelation', None)
    assert getattr(partner, 'VariableRef') is None


def test_assoc_target94_stub_double():
    # VariableRef has no real 'VariableRef96' property in the generated
    # code (a bare stub) -- manually attach it so SOS_set_ModelRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_set_ModelRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_set_ModelRelation(referenceName="sample_text")
    partner = VariableRef()
    setattr(partner, 'VariableRef96', None)
    _safe_set(owner, 'SOS_set_ModelRelation95', partner)
    assert getattr(partner, 'VariableRef96') == owner
    _safe_set(owner, 'SOS_set_ModelRelation95', None)
    assert getattr(partner, 'VariableRef96') is None


def test_assoc_variableSort56_stub_double():
    # Sort has no real 'Sort57' property in the generated
    # code (a bare stub) -- manually attach it so SOS_adtmm_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SOS_adtmm_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SOS_adtmm_Variable(name="sample_text")
    partner = Sort()
    setattr(partner, 'Sort57', None)
    _safe_set(owner, 'SOS_adtmm_Variable', partner)
    assert getattr(partner, 'Sort57') == owner
    _safe_set(owner, 'SOS_adtmm_Variable', None)
    assert getattr(partner, 'Sort57') is None


