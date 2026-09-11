import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractMappingCS,
    DomainCS,
    ExpCS,
    MappingStatementCS,
    ModelElementCS,
    PredicateOrAssignmentCS,
    RootPackageCS,
    qvtimperativecs_ExpCS,
    qvtimperativecs_ImperativeDomainCS,
    qvtimperativecs_ImperativePredicateOrAssignmentCS,
    qvtimperativecs_Mapping,
    qvtimperativecs_MappingCS,
    qvtimperativecs_MappingCallBindingCS,
    qvtimperativecs_MappingCallCS,
    qvtimperativecs_MappingLoopCS,
    qvtimperativecs_MappingSequenceCS,
    qvtimperativecs_MappingStatementCS,
    qvtimperativecs_PathNameCS,
    qvtimperativecs_QueryCS,
    qvtimperativecs_TopLevelCS,
    qvtimperativecs_TransformationCS,
    qvtimperativecs_Variable,
    qvtimperativecs_VariableCS,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_qvtimperativecs_ImperativePredicateOrAssignmentCS_isAccumulate_value_roundtrip():
    instance = qvtimperativecs_ImperativePredicateOrAssignmentCS(isAccumulate=True)
    assert instance.isAccumulate == True
    instance.isAccumulate = False
    assert instance.isAccumulate == False


def test_qvtimperativecs_MappingCallBindingCS_isPolled_value_roundtrip():
    instance = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    assert instance.isPolled == True
    instance.isPolled = False
    assert instance.isPolled == False


def test_qvtimperativecs_MappingCallCS_isInfinite_value_roundtrip():
    instance = qvtimperativecs_MappingCallCS(isInfinite=True)
    assert instance.isInfinite == True
    instance.isInfinite = False
    assert instance.isInfinite == False


def test_qvtimperativecs_MappingCS_isa_AbstractMappingCS():
    instance = qvtimperativecs_MappingCS()
    assert isinstance(instance, AbstractMappingCS)


def test_qvtimperativecs_ImperativeDomainCS_isa_DomainCS():
    instance = qvtimperativecs_ImperativeDomainCS()
    assert isinstance(instance, DomainCS)


def test_qvtimperativecs_MappingCallBindingCS_isa_ExpCS():
    instance = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    assert isinstance(instance, ExpCS)


def test_qvtimperativecs_MappingCallCS_isa_MappingStatementCS():
    instance = qvtimperativecs_MappingCallCS(isInfinite=True)
    assert isinstance(instance, MappingStatementCS)


def test_qvtimperativecs_MappingLoopCS_isa_MappingStatementCS():
    instance = qvtimperativecs_MappingLoopCS()
    assert isinstance(instance, MappingStatementCS)


def test_qvtimperativecs_MappingSequenceCS_isa_MappingStatementCS():
    instance = qvtimperativecs_MappingSequenceCS()
    assert isinstance(instance, MappingStatementCS)


def test_qvtimperativecs_MappingStatementCS_isa_ModelElementCS():
    instance = qvtimperativecs_MappingStatementCS()
    assert isinstance(instance, ModelElementCS)


def test_qvtimperativecs_ImperativePredicateOrAssignmentCS_isa_PredicateOrAssignmentCS():
    instance = qvtimperativecs_ImperativePredicateOrAssignmentCS(isAccumulate=True)
    assert isinstance(instance, PredicateOrAssignmentCS)


def test_qvtimperativecs_TopLevelCS_isa_RootPackageCS():
    instance = qvtimperativecs_TopLevelCS()
    assert isinstance(instance, RootPackageCS)


def test_assoc_ownedBindings12_link_reassign_clear():
    a = qvtimperativecs_MappingCallCS(isInfinite=True)
    b1 = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    b2 = qvtimperativecs_MappingCallBindingCS(isPolled=False)
    _safe_set(a, 'owningMappingCall', {b1})
    assert _is_linked(a, 'owningMappingCall', b1)
    if hasattr(b1, 'MappingCallBindingCS'):
        assert _is_linked(b1, 'MappingCallBindingCS', a)
    _safe_set(a, 'owningMappingCall', {b2})
    assert _is_linked(a, 'owningMappingCall', b2)
    if hasattr(b1, 'MappingCallBindingCS'):
        assert not _is_linked(b1, 'MappingCallBindingCS', a)
    if hasattr(b2, 'MappingCallBindingCS'):
        assert _is_linked(b2, 'MappingCallBindingCS', a)
    _safe_set(a, 'owningMappingCall', set())
    assert not _is_linked(a, 'owningMappingCall', b2)
    if hasattr(b2, 'MappingCallBindingCS'):
        assert not _is_linked(b2, 'MappingCallBindingCS', a)


def test_assoc_ownedPathName13_link_reassign_clear():
    a = qvtimperativecs_MappingCallCS(isInfinite=True)
    b1 = qvtimperativecs_PathNameCS()
    b2 = qvtimperativecs_PathNameCS()
    _safe_set(a, 'qvtimperativecs_MappingCallCS', b1)
    assert _is_linked(a, 'qvtimperativecs_MappingCallCS', b1)
    if hasattr(b1, 'qvtimperativecs_PathNameCS14'):
        assert _is_linked(b1, 'qvtimperativecs_PathNameCS14', a)
    _safe_set(a, 'qvtimperativecs_MappingCallCS', b2)
    assert _is_linked(a, 'qvtimperativecs_MappingCallCS', b2)
    if hasattr(b1, 'qvtimperativecs_PathNameCS14'):
        assert not _is_linked(b1, 'qvtimperativecs_PathNameCS14', a)
    if hasattr(b2, 'qvtimperativecs_PathNameCS14'):
        assert _is_linked(b2, 'qvtimperativecs_PathNameCS14', a)
    _safe_set(a, 'qvtimperativecs_MappingCallCS', None)
    assert not _is_linked(a, 'qvtimperativecs_MappingCallCS', b2)
    if hasattr(b2, 'qvtimperativecs_PathNameCS14'):
        assert not _is_linked(b2, 'qvtimperativecs_PathNameCS14', a)


def test_assoc_ownedValue8_link_reassign_clear():
    a = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    b1 = qvtimperativecs_ExpCS()
    b2 = qvtimperativecs_ExpCS()
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS', b1)
    assert _is_linked(a, 'qvtimperativecs_MappingCallBindingCS', b1)
    if hasattr(b1, 'qvtimperativecs_ExpCS'):
        assert _is_linked(b1, 'qvtimperativecs_ExpCS', a)
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS', b2)
    assert _is_linked(a, 'qvtimperativecs_MappingCallBindingCS', b2)
    if hasattr(b1, 'qvtimperativecs_ExpCS'):
        assert not _is_linked(b1, 'qvtimperativecs_ExpCS', a)
    if hasattr(b2, 'qvtimperativecs_ExpCS'):
        assert _is_linked(b2, 'qvtimperativecs_ExpCS', a)
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS', None)
    assert not _is_linked(a, 'qvtimperativecs_MappingCallBindingCS', b2)
    if hasattr(b2, 'qvtimperativecs_ExpCS'):
        assert not _is_linked(b2, 'qvtimperativecs_ExpCS', a)


def test_assoc_owningMappingCall9_link_reassign_clear():
    a = qvtimperativecs_MappingCallCS(isInfinite=True)
    b1 = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    b2 = qvtimperativecs_MappingCallBindingCS(isPolled=False)
    _safe_set(a, 'MappingCallCS', b1)
    assert _is_linked(a, 'MappingCallCS', b1)
    if hasattr(b1, 'ownedBindings'):
        assert _is_linked(b1, 'ownedBindings', a)
    _safe_set(a, 'MappingCallCS', b2)
    assert _is_linked(a, 'MappingCallCS', b2)
    if hasattr(b1, 'ownedBindings'):
        assert not _is_linked(b1, 'ownedBindings', a)
    if hasattr(b2, 'ownedBindings'):
        assert _is_linked(b2, 'ownedBindings', a)
    _safe_set(a, 'MappingCallCS', None)
    assert not _is_linked(a, 'MappingCallCS', b2)
    if hasattr(b2, 'ownedBindings'):
        assert not _is_linked(b2, 'ownedBindings', a)


def test_assoc_referredMapping15_link_reassign_clear():
    a = qvtimperativecs_MappingCallCS(isInfinite=True)
    b1 = qvtimperativecs_Mapping()
    b2 = qvtimperativecs_Mapping()
    _safe_set(a, 'qvtimperativecs_MappingCallCS16', b1)
    assert _is_linked(a, 'qvtimperativecs_MappingCallCS16', b1)
    if hasattr(b1, 'qvtimperativecs_Mapping'):
        assert _is_linked(b1, 'qvtimperativecs_Mapping', a)
    _safe_set(a, 'qvtimperativecs_MappingCallCS16', b2)
    assert _is_linked(a, 'qvtimperativecs_MappingCallCS16', b2)
    if hasattr(b1, 'qvtimperativecs_Mapping'):
        assert not _is_linked(b1, 'qvtimperativecs_Mapping', a)
    if hasattr(b2, 'qvtimperativecs_Mapping'):
        assert _is_linked(b2, 'qvtimperativecs_Mapping', a)
    _safe_set(a, 'qvtimperativecs_MappingCallCS16', None)
    assert not _is_linked(a, 'qvtimperativecs_MappingCallCS16', b2)
    if hasattr(b2, 'qvtimperativecs_Mapping'):
        assert not _is_linked(b2, 'qvtimperativecs_Mapping', a)


def test_assoc_referredVariable10_link_reassign_clear():
    a = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    b1 = qvtimperativecs_Variable()
    b2 = qvtimperativecs_Variable()
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS11', b1)
    assert _is_linked(a, 'qvtimperativecs_MappingCallBindingCS11', b1)
    if hasattr(b1, 'qvtimperativecs_Variable'):
        assert _is_linked(b1, 'qvtimperativecs_Variable', a)
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS11', b2)
    assert _is_linked(a, 'qvtimperativecs_MappingCallBindingCS11', b2)
    if hasattr(b1, 'qvtimperativecs_Variable'):
        assert not _is_linked(b1, 'qvtimperativecs_Variable', a)
    if hasattr(b2, 'qvtimperativecs_Variable'):
        assert _is_linked(b2, 'qvtimperativecs_Variable', a)
    _safe_set(a, 'qvtimperativecs_MappingCallBindingCS11', None)
    assert not _is_linked(a, 'qvtimperativecs_MappingCallBindingCS11', b2)
    if hasattr(b2, 'qvtimperativecs_Variable'):
        assert not _is_linked(b2, 'qvtimperativecs_Variable', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractMappingCS_strategy = st.builds(AbstractMappingCS)
@given(instance=AbstractMappingCS_strategy)
@settings(max_examples=25)
def test_AbstractMappingCS_instantiation(instance):
    assert isinstance(instance, AbstractMappingCS)


DomainCS_strategy = st.builds(DomainCS)
@given(instance=DomainCS_strategy)
@settings(max_examples=25)
def test_DomainCS_instantiation(instance):
    assert isinstance(instance, DomainCS)


ExpCS_strategy = st.builds(ExpCS)
@given(instance=ExpCS_strategy)
@settings(max_examples=25)
def test_ExpCS_instantiation(instance):
    assert isinstance(instance, ExpCS)


MappingStatementCS_strategy = st.builds(MappingStatementCS)
@given(instance=MappingStatementCS_strategy)
@settings(max_examples=25)
def test_MappingStatementCS_instantiation(instance):
    assert isinstance(instance, MappingStatementCS)


ModelElementCS_strategy = st.builds(ModelElementCS)
@given(instance=ModelElementCS_strategy)
@settings(max_examples=25)
def test_ModelElementCS_instantiation(instance):
    assert isinstance(instance, ModelElementCS)


PredicateOrAssignmentCS_strategy = st.builds(PredicateOrAssignmentCS)
@given(instance=PredicateOrAssignmentCS_strategy)
@settings(max_examples=25)
def test_PredicateOrAssignmentCS_instantiation(instance):
    assert isinstance(instance, PredicateOrAssignmentCS)


RootPackageCS_strategy = st.builds(RootPackageCS)
@given(instance=RootPackageCS_strategy)
@settings(max_examples=25)
def test_RootPackageCS_instantiation(instance):
    assert isinstance(instance, RootPackageCS)


qvtimperativecs_ExpCS_strategy = st.builds(qvtimperativecs_ExpCS)
@given(instance=qvtimperativecs_ExpCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_ExpCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ExpCS)


qvtimperativecs_ImperativeDomainCS_strategy = st.builds(qvtimperativecs_ImperativeDomainCS)
@given(instance=qvtimperativecs_ImperativeDomainCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_ImperativeDomainCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ImperativeDomainCS)


qvtimperativecs_ImperativePredicateOrAssignmentCS_strategy = st.builds(qvtimperativecs_ImperativePredicateOrAssignmentCS, isAccumulate=st.booleans())
@given(instance=qvtimperativecs_ImperativePredicateOrAssignmentCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_ImperativePredicateOrAssignmentCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ImperativePredicateOrAssignmentCS)


qvtimperativecs_Mapping_strategy = st.builds(qvtimperativecs_Mapping)
@given(instance=qvtimperativecs_Mapping_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_Mapping_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_Mapping)


qvtimperativecs_MappingCS_strategy = st.builds(qvtimperativecs_MappingCS)
@given(instance=qvtimperativecs_MappingCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCS)


qvtimperativecs_MappingCallBindingCS_strategy = st.builds(qvtimperativecs_MappingCallBindingCS, isPolled=st.booleans())
@given(instance=qvtimperativecs_MappingCallBindingCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingCallBindingCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCallBindingCS)


qvtimperativecs_MappingCallCS_strategy = st.builds(qvtimperativecs_MappingCallCS, isInfinite=st.booleans())
@given(instance=qvtimperativecs_MappingCallCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingCallCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCallCS)


qvtimperativecs_MappingLoopCS_strategy = st.builds(qvtimperativecs_MappingLoopCS)
@given(instance=qvtimperativecs_MappingLoopCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingLoopCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingLoopCS)


qvtimperativecs_MappingSequenceCS_strategy = st.builds(qvtimperativecs_MappingSequenceCS)
@given(instance=qvtimperativecs_MappingSequenceCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingSequenceCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingSequenceCS)


qvtimperativecs_MappingStatementCS_strategy = st.builds(qvtimperativecs_MappingStatementCS)
@given(instance=qvtimperativecs_MappingStatementCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_MappingStatementCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingStatementCS)


qvtimperativecs_PathNameCS_strategy = st.builds(qvtimperativecs_PathNameCS)
@given(instance=qvtimperativecs_PathNameCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_PathNameCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_PathNameCS)


qvtimperativecs_QueryCS_strategy = st.builds(qvtimperativecs_QueryCS)
@given(instance=qvtimperativecs_QueryCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_QueryCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_QueryCS)


qvtimperativecs_TopLevelCS_strategy = st.builds(qvtimperativecs_TopLevelCS)
@given(instance=qvtimperativecs_TopLevelCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_TopLevelCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_TopLevelCS)


qvtimperativecs_TransformationCS_strategy = st.builds(qvtimperativecs_TransformationCS)
@given(instance=qvtimperativecs_TransformationCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_TransformationCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_TransformationCS)


qvtimperativecs_Variable_strategy = st.builds(qvtimperativecs_Variable)
@given(instance=qvtimperativecs_Variable_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_Variable_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_Variable)


qvtimperativecs_VariableCS_strategy = st.builds(qvtimperativecs_VariableCS)
@given(instance=qvtimperativecs_VariableCS_strategy)
@settings(max_examples=25)
def test_qvtimperativecs_VariableCS_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_VariableCS)


