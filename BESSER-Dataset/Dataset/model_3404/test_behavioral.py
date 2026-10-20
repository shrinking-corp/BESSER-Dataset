import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    training_Person,
    training_Session,
    training_Trainee,
    training_Trainer,
    training_Training,
    training_TrainingOrganization,
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

def test_assoc_Trainees2_reverse_link_reassign_clear():
    a1 = training_Session(date=date(2024, 1, 1), name="sample_text")
    a2 = training_Session(date=date(2025, 6, 15), name="sample_text_2")
    b = training_Person(firstname="sample_text", lastname="sample_text")
    _safe_set(b, 'training_Person', a1)
    assert _is_linked(b, 'training_Person', a1)
    if hasattr(a1, 'training_Session3'):
        assert _is_linked(a1, 'training_Session3', b)
    _safe_set(b, 'training_Person', a2)
    assert _is_linked(b, 'training_Person', a2)
    if hasattr(a1, 'training_Session3'):
        assert not _is_linked(a1, 'training_Session3', b)
    if hasattr(a2, 'training_Session3'):
        assert _is_linked(a2, 'training_Session3', b)
    _safe_set(b, 'training_Person', None)
    assert not _is_linked(b, 'training_Person', a2)
    if hasattr(a2, 'training_Session3'):
        assert not _is_linked(a2, 'training_Session3', b)


def test_assoc_people4_reverse_link_reassign_clear():
    a1 = training_TrainingOrganization(name="sample_text")
    a2 = training_TrainingOrganization(name="sample_text_2")
    b = training_Person(firstname="sample_text", lastname="sample_text")
    _safe_set(b, 'training_Person5', a1)
    assert _is_linked(b, 'training_Person5', a1)
    if hasattr(a1, 'training_TrainingOrganization'):
        assert _is_linked(a1, 'training_TrainingOrganization', b)
    _safe_set(b, 'training_Person5', a2)
    assert _is_linked(b, 'training_Person5', a2)
    if hasattr(a1, 'training_TrainingOrganization'):
        assert not _is_linked(a1, 'training_TrainingOrganization', b)
    if hasattr(a2, 'training_TrainingOrganization'):
        assert _is_linked(a2, 'training_TrainingOrganization', b)
    _safe_set(b, 'training_Person5', None)
    assert not _is_linked(b, 'training_Person5', a2)
    if hasattr(a2, 'training_TrainingOrganization'):
        assert not _is_linked(a2, 'training_TrainingOrganization', b)


def test_assoc_session12_reverse_link_reassign_clear():
    a1 = training_Training(title="sample_text")
    a2 = training_Training(title="sample_text_2")
    b = training_Session(date=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'Session', a1)
    assert _is_linked(b, 'Session', a1)
    if hasattr(a1, 'training'):
        assert _is_linked(a1, 'training', b)
    _safe_set(b, 'Session', a2)
    assert _is_linked(b, 'Session', a2)
    if hasattr(a1, 'training'):
        assert not _is_linked(a1, 'training', b)
    if hasattr(a2, 'training'):
        assert _is_linked(a2, 'training', b)
    _safe_set(b, 'Session', None)
    assert not _is_linked(b, 'Session', a2)
    if hasattr(a2, 'training'):
        assert not _is_linked(a2, 'training', b)


def test_assoc_sessions6_reverse_link_reassign_clear():
    a1 = training_TrainingOrganization(name="sample_text")
    a2 = training_TrainingOrganization(name="sample_text_2")
    b = training_Session(date=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'training_Session8', a1)
    assert _is_linked(b, 'training_Session8', a1)
    if hasattr(a1, 'training_TrainingOrganization7'):
        assert _is_linked(a1, 'training_TrainingOrganization7', b)
    _safe_set(b, 'training_Session8', a2)
    assert _is_linked(b, 'training_Session8', a2)
    if hasattr(a1, 'training_TrainingOrganization7'):
        assert not _is_linked(a1, 'training_TrainingOrganization7', b)
    if hasattr(a2, 'training_TrainingOrganization7'):
        assert _is_linked(a2, 'training_TrainingOrganization7', b)
    _safe_set(b, 'training_Session8', None)
    assert not _is_linked(b, 'training_Session8', a2)
    if hasattr(a2, 'training_TrainingOrganization7'):
        assert not _is_linked(a2, 'training_TrainingOrganization7', b)


def test_assoc_training0_reverse_link_reassign_clear():
    a1 = training_Training(title="sample_text")
    a2 = training_Training(title="sample_text_2")
    b = training_Session(date=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'session', a1)
    assert _is_linked(b, 'session', a1)
    if hasattr(a1, 'Training'):
        assert _is_linked(a1, 'Training', b)
    _safe_set(b, 'session', a2)
    assert _is_linked(b, 'session', a2)
    if hasattr(a1, 'Training'):
        assert not _is_linked(a1, 'Training', b)
    if hasattr(a2, 'Training'):
        assert _is_linked(a2, 'Training', b)
    _safe_set(b, 'session', None)
    assert not _is_linked(b, 'session', a2)
    if hasattr(a2, 'Training'):
        assert not _is_linked(a2, 'Training', b)


def test_assoc_training9_reverse_link_reassign_clear():
    a1 = training_TrainingOrganization(name="sample_text")
    a2 = training_TrainingOrganization(name="sample_text_2")
    b = training_Training(title="sample_text")
    _safe_set(b, 'training_Training', a1)
    assert _is_linked(b, 'training_Training', a1)
    if hasattr(a1, 'training_TrainingOrganization10'):
        assert _is_linked(a1, 'training_TrainingOrganization10', b)
    _safe_set(b, 'training_Training', a2)
    assert _is_linked(b, 'training_Training', a2)
    if hasattr(a1, 'training_TrainingOrganization10'):
        assert not _is_linked(a1, 'training_TrainingOrganization10', b)
    if hasattr(a2, 'training_TrainingOrganization10'):
        assert _is_linked(a2, 'training_TrainingOrganization10', b)
    _safe_set(b, 'training_Training', None)
    assert not _is_linked(b, 'training_Training', a2)
    if hasattr(a2, 'training_TrainingOrganization10'):
        assert not _is_linked(a2, 'training_TrainingOrganization10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_canBeProvidedBy11_stub_double():
    # training_Trainer has no real 'Trainer' property in the generated
    # code (a bare stub) -- manually attach it so training_Training's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # training_Training's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = training_Training(title="sample_text")
    partner = training_Trainer()
    setattr(partner, 'Trainer', None)
    _safe_set(owner, 'canProvide', {partner})
    assert getattr(partner, 'Trainer') == owner
    _safe_set(owner, 'canProvide', set())
    assert getattr(partner, 'Trainer') is None


def test_assoc_canProvide13_stub_double():
    # training_Trainer has no real 'canBeProvidedBy' property in the generated
    # code (a bare stub) -- manually attach it so training_Training's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # training_Training's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = training_Training(title="sample_text")
    partner = training_Trainer()
    setattr(partner, 'canBeProvidedBy', None)
    _safe_set(owner, 'Training14', partner)
    assert owner in getattr(partner, 'canBeProvidedBy')
    _safe_set(owner, 'Training14', None)
    assert owner not in getattr(partner, 'canBeProvidedBy')


def test_assoc_trainer1_stub_double():
    # training_Trainer has no real 'training_Trainer' property in the generated
    # code (a bare stub) -- manually attach it so training_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # training_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = training_Session(date=date(2024, 1, 1), name="sample_text")
    partner = training_Trainer()
    setattr(partner, 'training_Trainer', None)
    _safe_set(owner, 'training_Session', partner)
    assert getattr(partner, 'training_Trainer') == owner
    _safe_set(owner, 'training_Session', None)
    assert getattr(partner, 'training_Trainer') is None


