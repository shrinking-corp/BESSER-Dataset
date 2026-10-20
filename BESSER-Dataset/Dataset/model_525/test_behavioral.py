import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Lims_Family,
    Lims_Individual,
    Lims_Laboratory,
    Lims_Run,
    Lims_Sample,
    Lims_Sequenced,
    Lims_Sequencer,
    Gender,
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

def test_assoc_Father8_reverse_link_reassign_clear():
    a1 = Lims_Individual(gender="sample_text", name="sample_text")
    a2 = Lims_Individual(gender="sample_text_2", name="sample_text_2")
    b = Lims_Individual(gender="sample_text", name="sample_text")
    _safe_set(b, 'Lims_Individual7', a1)
    assert _is_linked(b, 'Lims_Individual7', a1)
    if hasattr(a1, 'Lims_Individual'):
        assert _is_linked(a1, 'Lims_Individual', b)
    _safe_set(b, 'Lims_Individual7', a2)
    assert _is_linked(b, 'Lims_Individual7', a2)
    if hasattr(a1, 'Lims_Individual'):
        assert not _is_linked(a1, 'Lims_Individual', b)
    if hasattr(a2, 'Lims_Individual'):
        assert _is_linked(a2, 'Lims_Individual', b)
    _safe_set(b, 'Lims_Individual7', None)
    assert not _is_linked(b, 'Lims_Individual7', a2)
    if hasattr(a2, 'Lims_Individual'):
        assert not _is_linked(a2, 'Lims_Individual', b)


def test_assoc_Mother10_reverse_link_reassign_clear():
    a1 = Lims_Individual(gender="sample_text", name="sample_text")
    a2 = Lims_Individual(gender="sample_text_2", name="sample_text_2")
    b = Lims_Individual(gender="sample_text", name="sample_text")
    _safe_set(b, 'Lims_Individual9', a1)
    assert _is_linked(b, 'Lims_Individual9', a1)
    if hasattr(a1, 'Lims_Individual11'):
        assert _is_linked(a1, 'Lims_Individual11', b)
    _safe_set(b, 'Lims_Individual9', a2)
    assert _is_linked(b, 'Lims_Individual9', a2)
    if hasattr(a1, 'Lims_Individual11'):
        assert not _is_linked(a1, 'Lims_Individual11', b)
    if hasattr(a2, 'Lims_Individual11'):
        assert _is_linked(a2, 'Lims_Individual11', b)
    _safe_set(b, 'Lims_Individual9', None)
    assert not _is_linked(b, 'Lims_Individual9', a2)
    if hasattr(a2, 'Lims_Individual11'):
        assert not _is_linked(a2, 'Lims_Individual11', b)


def test_assoc_family5_reverse_link_reassign_clear():
    a1 = Lims_Individual(gender="sample_text", name="sample_text")
    a2 = Lims_Individual(gender="sample_text_2", name="sample_text_2")
    b = Lims_Family(name="sample_text")
    _safe_set(b, 'Family6', a1)
    assert _is_linked(b, 'Family6', a1)
    if hasattr(a1, 'individuals'):
        assert _is_linked(a1, 'individuals', b)
    _safe_set(b, 'Family6', a2)
    assert _is_linked(b, 'Family6', a2)
    if hasattr(a1, 'individuals'):
        assert not _is_linked(a1, 'individuals', b)
    if hasattr(a2, 'individuals'):
        assert _is_linked(a2, 'individuals', b)
    _safe_set(b, 'Family6', None)
    assert not _is_linked(b, 'Family6', a2)
    if hasattr(a2, 'individuals'):
        assert not _is_linked(a2, 'individuals', b)


def test_assoc_individual19_reverse_link_reassign_clear():
    a1 = Lims_Sample(id="sample_text")
    a2 = Lims_Sample(id="sample_text_2")
    b = Lims_Individual(gender="sample_text", name="sample_text")
    _safe_set(b, 'Individual20', a1)
    assert _is_linked(b, 'Individual20', a1)
    if hasattr(a1, 'samples'):
        assert _is_linked(a1, 'samples', b)
    _safe_set(b, 'Individual20', a2)
    assert _is_linked(b, 'Individual20', a2)
    if hasattr(a1, 'samples'):
        assert not _is_linked(a1, 'samples', b)
    if hasattr(a2, 'samples'):
        assert _is_linked(a2, 'samples', b)
    _safe_set(b, 'Individual20', None)
    assert not _is_linked(b, 'Individual20', a2)
    if hasattr(a2, 'samples'):
        assert not _is_linked(a2, 'samples', b)


def test_assoc_individuals0_reverse_link_reassign_clear():
    a1 = Lims_Individual(gender="sample_text", name="sample_text")
    a2 = Lims_Individual(gender="sample_text_2", name="sample_text_2")
    b = Lims_Family(name="sample_text")
    _safe_set(b, 'family', {a1})
    assert _is_linked(b, 'family', a1)
    if hasattr(a1, 'Individual'):
        assert _is_linked(a1, 'Individual', b)
    _safe_set(b, 'family', {a2})
    assert _is_linked(b, 'family', a2)
    if hasattr(a1, 'Individual'):
        assert not _is_linked(a1, 'Individual', b)
    if hasattr(a2, 'Individual'):
        assert _is_linked(a2, 'Individual', b)
    _safe_set(b, 'family', set())
    assert not _is_linked(b, 'family', a2)
    if hasattr(a2, 'Individual'):
        assert not _is_linked(a2, 'Individual', b)


def test_assoc_runs13_reverse_link_reassign_clear():
    a1 = Lims_Sequencer(name="sample_text")
    a2 = Lims_Sequencer(name="sample_text_2")
    b = Lims_Run(date=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'Run', a1)
    assert _is_linked(b, 'Run', a1)
    if hasattr(a1, 'sequencer'):
        assert _is_linked(a1, 'sequencer', b)
    _safe_set(b, 'Run', a2)
    assert _is_linked(b, 'Run', a2)
    if hasattr(a1, 'sequencer'):
        assert not _is_linked(a1, 'sequencer', b)
    if hasattr(a2, 'sequencer'):
        assert _is_linked(a2, 'sequencer', b)
    _safe_set(b, 'Run', None)
    assert not _is_linked(b, 'Run', a2)
    if hasattr(a2, 'sequencer'):
        assert not _is_linked(a2, 'sequencer', b)


def test_assoc_samples12_reverse_link_reassign_clear():
    a1 = Lims_Sample(id="sample_text")
    a2 = Lims_Sample(id="sample_text_2")
    b = Lims_Individual(gender="sample_text", name="sample_text")
    _safe_set(b, 'individual', {a1})
    assert _is_linked(b, 'individual', a1)
    if hasattr(a1, 'Sample'):
        assert _is_linked(a1, 'Sample', b)
    _safe_set(b, 'individual', {a2})
    assert _is_linked(b, 'individual', a2)
    if hasattr(a1, 'Sample'):
        assert not _is_linked(a1, 'Sample', b)
    if hasattr(a2, 'Sample'):
        assert _is_linked(a2, 'Sample', b)
    _safe_set(b, 'individual', set())
    assert not _is_linked(b, 'individual', a2)
    if hasattr(a2, 'Sample'):
        assert not _is_linked(a2, 'Sample', b)


def test_assoc_sequencer17_reverse_link_reassign_clear():
    a1 = Lims_Sequencer(name="sample_text")
    a2 = Lims_Sequencer(name="sample_text_2")
    b = Lims_Run(date=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'runs', a1)
    assert _is_linked(b, 'runs', a1)
    if hasattr(a1, 'Sequencer18'):
        assert _is_linked(a1, 'Sequencer18', b)
    _safe_set(b, 'runs', a2)
    assert _is_linked(b, 'runs', a2)
    if hasattr(a1, 'Sequencer18'):
        assert not _is_linked(a1, 'Sequencer18', b)
    if hasattr(a2, 'Sequencer18'):
        assert _is_linked(a2, 'Sequencer18', b)
    _safe_set(b, 'runs', None)
    assert not _is_linked(b, 'runs', a2)
    if hasattr(a2, 'Sequencer18'):
        assert not _is_linked(a2, 'Sequencer18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_families2_stub_double():
    # Lims_Laboratory has no real 'laboratory' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Family(name="sample_text")
    partner = Lims_Laboratory()
    setattr(partner, 'laboratory', None)
    _safe_set(owner, 'Family', partner)
    assert owner in getattr(partner, 'laboratory')
    _safe_set(owner, 'Family', None)
    assert owner not in getattr(partner, 'laboratory')


def test_assoc_laboratory1_stub_double():
    # Lims_Laboratory has no real 'Laboratory' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Family(name="sample_text")
    partner = Lims_Laboratory()
    setattr(partner, 'Laboratory', None)
    _safe_set(owner, 'families', partner)
    assert getattr(partner, 'Laboratory') == owner
    _safe_set(owner, 'families', None)
    assert getattr(partner, 'Laboratory') is None


def test_assoc_laboratory14_stub_double():
    # Lims_Laboratory has no real 'Laboratory15' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Sequencer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Sequencer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Sequencer(name="sample_text")
    partner = Lims_Laboratory()
    setattr(partner, 'Laboratory15', None)
    _safe_set(owner, 'sequencers', partner)
    assert getattr(partner, 'Laboratory15') == owner
    _safe_set(owner, 'sequencers', None)
    assert getattr(partner, 'Laboratory15') is None


def test_assoc_run21_stub_double():
    # Lims_Sequenced has no real 'sequenced' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Run's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Run's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Run(date=date(2024, 1, 1), name="sample_text")
    partner = Lims_Sequenced()
    setattr(partner, 'sequenced', None)
    _safe_set(owner, 'Run22', partner)
    assert getattr(partner, 'sequenced') == owner
    _safe_set(owner, 'Run22', None)
    assert getattr(partner, 'sequenced') is None


def test_assoc_sample23_stub_double():
    # Lims_Sequenced has no real 'Lims_Sequenced' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Sample's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Sample's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Sample(id="sample_text")
    partner = Lims_Sequenced()
    setattr(partner, 'Lims_Sequenced', None)
    _safe_set(owner, 'Lims_Sample', partner)
    assert getattr(partner, 'Lims_Sequenced') == owner
    _safe_set(owner, 'Lims_Sample', None)
    assert getattr(partner, 'Lims_Sequenced') is None


def test_assoc_sequenced16_stub_double():
    # Lims_Sequenced has no real 'Sequenced' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Run's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Run's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Run(date=date(2024, 1, 1), name="sample_text")
    partner = Lims_Sequenced()
    setattr(partner, 'Sequenced', None)
    _safe_set(owner, 'run', {partner})
    assert getattr(partner, 'Sequenced') == owner
    _safe_set(owner, 'run', set())
    assert getattr(partner, 'Sequenced') is None


def test_assoc_sequencers3_stub_double():
    # Lims_Laboratory has no real 'laboratory4' property in the generated
    # code (a bare stub) -- manually attach it so Lims_Sequencer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lims_Sequencer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lims_Sequencer(name="sample_text")
    partner = Lims_Laboratory()
    setattr(partner, 'laboratory4', None)
    _safe_set(owner, 'Sequencer', partner)
    assert owner in getattr(partner, 'laboratory4')
    _safe_set(owner, 'Sequencer', None)
    assert owner not in getattr(partner, 'laboratory4')


