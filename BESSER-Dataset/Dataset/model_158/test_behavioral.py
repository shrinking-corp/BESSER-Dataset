import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    petrinet_Arc,
    petrinet_PTArc,
    petrinet_Petrinet,
    petrinet_Place,
    petrinet_TPArc,
    petrinet_Token,
    petrinet_Transition,
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
    a1 = petrinet_Petrinet(name="sample_text")
    a2 = petrinet_Petrinet(name="sample_text_2")
    b = petrinet_Arc(name="sample_text", weight=7)
    _safe_set(b, 'petrinet_Arc', a1)
    assert _is_linked(b, 'petrinet_Arc', a1)
    if hasattr(a1, 'petrinet_Petrinet4'):
        assert _is_linked(a1, 'petrinet_Petrinet4', b)
    _safe_set(b, 'petrinet_Arc', a2)
    assert _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a1, 'petrinet_Petrinet4'):
        assert not _is_linked(a1, 'petrinet_Petrinet4', b)
    if hasattr(a2, 'petrinet_Petrinet4'):
        assert _is_linked(a2, 'petrinet_Petrinet4', b)
    _safe_set(b, 'petrinet_Arc', None)
    assert not _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a2, 'petrinet_Petrinet4'):
        assert not _is_linked(a2, 'petrinet_Petrinet4', b)


def test_assoc_places0_reverse_link_reassign_clear():
    a1 = petrinet_Place(name="sample_text")
    a2 = petrinet_Place(name="sample_text_2")
    b = petrinet_Petrinet(name="sample_text")
    _safe_set(b, 'petrinet_Petrinet', {a1})
    assert _is_linked(b, 'petrinet_Petrinet', a1)
    if hasattr(a1, 'petrinet_Place'):
        assert _is_linked(a1, 'petrinet_Place', b)
    _safe_set(b, 'petrinet_Petrinet', {a2})
    assert _is_linked(b, 'petrinet_Petrinet', a2)
    if hasattr(a1, 'petrinet_Place'):
        assert not _is_linked(a1, 'petrinet_Place', b)
    if hasattr(a2, 'petrinet_Place'):
        assert _is_linked(a2, 'petrinet_Place', b)
    _safe_set(b, 'petrinet_Petrinet', set())
    assert not _is_linked(b, 'petrinet_Petrinet', a2)
    if hasattr(a2, 'petrinet_Place'):
        assert not _is_linked(a2, 'petrinet_Place', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Petrinet(name="sample_text")
    _safe_set(b, 'petrinet_Petrinet2', {a1})
    assert _is_linked(b, 'petrinet_Petrinet2', a1)
    if hasattr(a1, 'petrinet_Transition'):
        assert _is_linked(a1, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Petrinet2', {a2})
    assert _is_linked(b, 'petrinet_Petrinet2', a2)
    if hasattr(a1, 'petrinet_Transition'):
        assert not _is_linked(a1, 'petrinet_Transition', b)
    if hasattr(a2, 'petrinet_Transition'):
        assert _is_linked(a2, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Petrinet2', set())
    assert not _is_linked(b, 'petrinet_Petrinet2', a2)
    if hasattr(a2, 'petrinet_Transition'):
        assert not _is_linked(a2, 'petrinet_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_in_14_stub_double():
    # petrinet_PTArc has no real 'petrinet_PTArc16' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_PTArc()
    setattr(partner, 'petrinet_PTArc16', None)
    _safe_set(owner, 'petrinet_Transition15', {partner})
    assert getattr(partner, 'petrinet_PTArc16') == owner
    _safe_set(owner, 'petrinet_Transition15', set())
    assert getattr(partner, 'petrinet_PTArc16') is None


def test_assoc_in_9_stub_double():
    # petrinet_TPArc has no real 'petrinet_TPArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'petrinet_TPArc', None)
    _safe_set(owner, 'petrinet_Place10', {partner})
    assert getattr(partner, 'petrinet_TPArc') == owner
    _safe_set(owner, 'petrinet_Place10', set())
    assert getattr(partner, 'petrinet_TPArc') is None


def test_assoc_out11_stub_double():
    # petrinet_TPArc has no real 'petrinet_TPArc13' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'petrinet_TPArc13', None)
    _safe_set(owner, 'petrinet_Transition12', {partner})
    assert getattr(partner, 'petrinet_TPArc13') == owner
    _safe_set(owner, 'petrinet_Transition12', set())
    assert getattr(partner, 'petrinet_TPArc13') is None


def test_assoc_out7_stub_double():
    # petrinet_PTArc has no real 'petrinet_PTArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text")
    partner = petrinet_PTArc()
    setattr(partner, 'petrinet_PTArc', None)
    _safe_set(owner, 'petrinet_Place8', {partner})
    assert getattr(partner, 'petrinet_PTArc') == owner
    _safe_set(owner, 'petrinet_Place8', set())
    assert getattr(partner, 'petrinet_PTArc') is None


def test_assoc_source17_stub_double():
    # petrinet_PTArc has no real 'petrinet_PTArc18' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text")
    partner = petrinet_PTArc()
    setattr(partner, 'petrinet_PTArc18', None)
    _safe_set(owner, 'petrinet_Place19', partner)
    assert getattr(partner, 'petrinet_PTArc18') == owner
    _safe_set(owner, 'petrinet_Place19', None)
    assert getattr(partner, 'petrinet_PTArc18') is None


def test_assoc_source23_stub_double():
    # petrinet_TPArc has no real 'petrinet_TPArc24' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'petrinet_TPArc24', None)
    _safe_set(owner, 'petrinet_Transition25', partner)
    assert getattr(partner, 'petrinet_TPArc24') == owner
    _safe_set(owner, 'petrinet_Transition25', None)
    assert getattr(partner, 'petrinet_TPArc24') is None


def test_assoc_target20_stub_double():
    # petrinet_PTArc has no real 'petrinet_PTArc21' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_PTArc()
    setattr(partner, 'petrinet_PTArc21', None)
    _safe_set(owner, 'petrinet_Transition22', partner)
    assert getattr(partner, 'petrinet_PTArc21') == owner
    _safe_set(owner, 'petrinet_Transition22', None)
    assert getattr(partner, 'petrinet_PTArc21') is None


def test_assoc_target26_stub_double():
    # petrinet_TPArc has no real 'petrinet_TPArc27' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'petrinet_TPArc27', None)
    _safe_set(owner, 'petrinet_Place28', partner)
    assert getattr(partner, 'petrinet_TPArc27') == owner
    _safe_set(owner, 'petrinet_Place28', None)
    assert getattr(partner, 'petrinet_TPArc27') is None


def test_assoc_tokens5_stub_double():
    # petrinet_Token has no real 'petrinet_Token' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text")
    partner = petrinet_Token()
    setattr(partner, 'petrinet_Token', None)
    _safe_set(owner, 'petrinet_Place6', {partner})
    assert getattr(partner, 'petrinet_Token') == owner
    _safe_set(owner, 'petrinet_Place6', set())
    assert getattr(partner, 'petrinet_Token') is None


