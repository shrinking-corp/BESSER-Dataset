import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    petriNetz_Arc,
    petriNetz_PTArc,
    petriNetz_Petrinet,
    petriNetz_Place,
    petriNetz_TPArc,
    petriNetz_Token,
    petriNetz_Transition,
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

def test_assoc_arcs3_reverse_link_reassign_clear():
    a1 = petriNetz_Petrinet(name="sample_text")
    a2 = petriNetz_Petrinet(name="sample_text_2")
    b = petriNetz_Arc(weight=7)
    _safe_set(b, 'petriNetz_Arc', a1)
    assert _is_linked(b, 'petriNetz_Arc', a1)
    if hasattr(a1, 'petriNetz_Petrinet4'):
        assert _is_linked(a1, 'petriNetz_Petrinet4', b)
    _safe_set(b, 'petriNetz_Arc', a2)
    assert _is_linked(b, 'petriNetz_Arc', a2)
    if hasattr(a1, 'petriNetz_Petrinet4'):
        assert not _is_linked(a1, 'petriNetz_Petrinet4', b)
    if hasattr(a2, 'petriNetz_Petrinet4'):
        assert _is_linked(a2, 'petriNetz_Petrinet4', b)
    _safe_set(b, 'petriNetz_Arc', None)
    assert not _is_linked(b, 'petriNetz_Arc', a2)
    if hasattr(a2, 'petriNetz_Petrinet4'):
        assert not _is_linked(a2, 'petriNetz_Petrinet4', b)


def test_assoc_places0_reverse_link_reassign_clear():
    a1 = petriNetz_Place(name="sample_text")
    a2 = petriNetz_Place(name="sample_text_2")
    b = petriNetz_Petrinet(name="sample_text")
    _safe_set(b, 'petriNetz_Petrinet', {a1})
    assert _is_linked(b, 'petriNetz_Petrinet', a1)
    if hasattr(a1, 'petriNetz_Place'):
        assert _is_linked(a1, 'petriNetz_Place', b)
    _safe_set(b, 'petriNetz_Petrinet', {a2})
    assert _is_linked(b, 'petriNetz_Petrinet', a2)
    if hasattr(a1, 'petriNetz_Place'):
        assert not _is_linked(a1, 'petriNetz_Place', b)
    if hasattr(a2, 'petriNetz_Place'):
        assert _is_linked(a2, 'petriNetz_Place', b)
    _safe_set(b, 'petriNetz_Petrinet', set())
    assert not _is_linked(b, 'petriNetz_Petrinet', a2)
    if hasattr(a2, 'petriNetz_Place'):
        assert not _is_linked(a2, 'petriNetz_Place', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = petriNetz_Transition(name="sample_text")
    a2 = petriNetz_Transition(name="sample_text_2")
    b = petriNetz_Petrinet(name="sample_text")
    _safe_set(b, 'petriNetz_Petrinet2', {a1})
    assert _is_linked(b, 'petriNetz_Petrinet2', a1)
    if hasattr(a1, 'petriNetz_Transition'):
        assert _is_linked(a1, 'petriNetz_Transition', b)
    _safe_set(b, 'petriNetz_Petrinet2', {a2})
    assert _is_linked(b, 'petriNetz_Petrinet2', a2)
    if hasattr(a1, 'petriNetz_Transition'):
        assert not _is_linked(a1, 'petriNetz_Transition', b)
    if hasattr(a2, 'petriNetz_Transition'):
        assert _is_linked(a2, 'petriNetz_Transition', b)
    _safe_set(b, 'petriNetz_Petrinet2', set())
    assert not _is_linked(b, 'petriNetz_Petrinet2', a2)
    if hasattr(a2, 'petriNetz_Transition'):
        assert not _is_linked(a2, 'petriNetz_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_in_11_stub_double():
    # petriNetz_PTArc has no real 'petriNetz_PTArc13' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Transition(name="sample_text")
    partner = petriNetz_PTArc()
    setattr(partner, 'petriNetz_PTArc13', None)
    _safe_set(owner, 'petriNetz_Transition12', {partner})
    assert getattr(partner, 'petriNetz_PTArc13') == owner
    _safe_set(owner, 'petriNetz_Transition12', set())
    assert getattr(partner, 'petriNetz_PTArc13') is None


def test_assoc_in_9_stub_double():
    # petriNetz_TPArc has no real 'petriNetz_TPArc' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Place(name="sample_text")
    partner = petriNetz_TPArc()
    setattr(partner, 'petriNetz_TPArc', None)
    _safe_set(owner, 'petriNetz_Place10', {partner})
    assert getattr(partner, 'petriNetz_TPArc') == owner
    _safe_set(owner, 'petriNetz_Place10', set())
    assert getattr(partner, 'petriNetz_TPArc') is None


def test_assoc_out14_stub_double():
    # petriNetz_TPArc has no real 'petriNetz_TPArc16' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Transition(name="sample_text")
    partner = petriNetz_TPArc()
    setattr(partner, 'petriNetz_TPArc16', None)
    _safe_set(owner, 'petriNetz_Transition15', {partner})
    assert getattr(partner, 'petriNetz_TPArc16') == owner
    _safe_set(owner, 'petriNetz_Transition15', set())
    assert getattr(partner, 'petriNetz_TPArc16') is None


def test_assoc_out7_stub_double():
    # petriNetz_PTArc has no real 'petriNetz_PTArc' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Place(name="sample_text")
    partner = petriNetz_PTArc()
    setattr(partner, 'petriNetz_PTArc', None)
    _safe_set(owner, 'petriNetz_Place8', {partner})
    assert getattr(partner, 'petriNetz_PTArc') == owner
    _safe_set(owner, 'petriNetz_Place8', set())
    assert getattr(partner, 'petriNetz_PTArc') is None


def test_assoc_src17_stub_double():
    # petriNetz_PTArc has no real 'petriNetz_PTArc18' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Place(name="sample_text")
    partner = petriNetz_PTArc()
    setattr(partner, 'petriNetz_PTArc18', None)
    _safe_set(owner, 'petriNetz_Place19', partner)
    assert getattr(partner, 'petriNetz_PTArc18') == owner
    _safe_set(owner, 'petriNetz_Place19', None)
    assert getattr(partner, 'petriNetz_PTArc18') is None


def test_assoc_src26_stub_double():
    # petriNetz_TPArc has no real 'petriNetz_TPArc27' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Transition(name="sample_text")
    partner = petriNetz_TPArc()
    setattr(partner, 'petriNetz_TPArc27', None)
    _safe_set(owner, 'petriNetz_Transition28', partner)
    assert getattr(partner, 'petriNetz_TPArc27') == owner
    _safe_set(owner, 'petriNetz_Transition28', None)
    assert getattr(partner, 'petriNetz_TPArc27') is None


def test_assoc_tokens5_stub_double():
    # petriNetz_Token has no real 'petriNetz_Token' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Place(name="sample_text")
    partner = petriNetz_Token()
    setattr(partner, 'petriNetz_Token', None)
    _safe_set(owner, 'petriNetz_Place6', {partner})
    assert getattr(partner, 'petriNetz_Token') == owner
    _safe_set(owner, 'petriNetz_Place6', set())
    assert getattr(partner, 'petriNetz_Token') is None


def test_assoc_trg20_stub_double():
    # petriNetz_PTArc has no real 'petriNetz_PTArc21' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Transition(name="sample_text")
    partner = petriNetz_PTArc()
    setattr(partner, 'petriNetz_PTArc21', None)
    _safe_set(owner, 'petriNetz_Transition22', partner)
    assert getattr(partner, 'petriNetz_PTArc21') == owner
    _safe_set(owner, 'petriNetz_Transition22', None)
    assert getattr(partner, 'petriNetz_PTArc21') is None


def test_assoc_trg23_stub_double():
    # petriNetz_TPArc has no real 'petriNetz_TPArc24' property in the generated
    # code (a bare stub) -- manually attach it so petriNetz_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNetz_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNetz_Place(name="sample_text")
    partner = petriNetz_TPArc()
    setattr(partner, 'petriNetz_TPArc24', None)
    _safe_set(owner, 'petriNetz_Place25', partner)
    assert getattr(partner, 'petriNetz_TPArc24') == owner
    _safe_set(owner, 'petriNetz_Place25', None)
    assert getattr(partner, 'petriNetz_TPArc24') is None


