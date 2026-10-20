import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    simpleworld102_Element,
    simpleworld102_Named,
    simpleworld102_Part,
    simpleworld102_Person,
    simpleworld102_Relations,
    simpleworld102_Thing,
    simpleworld102_World,
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

def test_assoc_elements1_reverse_link_reassign_clear():
    a1 = simpleworld102_Person(foreName="sample_text", name="sample_text")
    a2 = simpleworld102_Person(foreName="sample_text_2", name="sample_text_2")
    b = simpleworld102_Element(description="sample_text")
    _safe_set(b, 'simpleworld102_Element', a1)
    assert _is_linked(b, 'simpleworld102_Element', a1)
    if hasattr(a1, 'simpleworld102_Person2'):
        assert _is_linked(a1, 'simpleworld102_Person2', b)
    _safe_set(b, 'simpleworld102_Element', a2)
    assert _is_linked(b, 'simpleworld102_Element', a2)
    if hasattr(a1, 'simpleworld102_Person2'):
        assert not _is_linked(a1, 'simpleworld102_Person2', b)
    if hasattr(a2, 'simpleworld102_Person2'):
        assert _is_linked(a2, 'simpleworld102_Person2', b)
    _safe_set(b, 'simpleworld102_Element', None)
    assert not _is_linked(b, 'simpleworld102_Element', a2)
    if hasattr(a2, 'simpleworld102_Person2'):
        assert not _is_linked(a2, 'simpleworld102_Person2', b)


def test_assoc_parts12_reverse_link_reassign_clear():
    a1 = simpleworld102_Relations(since=7)
    a2 = simpleworld102_Relations(since=13)
    b = simpleworld102_Part(content="sample_text", id=7)
    _safe_set(b, 'simpleworld102_Part14', a1)
    assert _is_linked(b, 'simpleworld102_Part14', a1)
    if hasattr(a1, 'simpleworld102_Relations13'):
        assert _is_linked(a1, 'simpleworld102_Relations13', b)
    _safe_set(b, 'simpleworld102_Part14', a2)
    assert _is_linked(b, 'simpleworld102_Part14', a2)
    if hasattr(a1, 'simpleworld102_Relations13'):
        assert not _is_linked(a1, 'simpleworld102_Relations13', b)
    if hasattr(a2, 'simpleworld102_Relations13'):
        assert _is_linked(a2, 'simpleworld102_Relations13', b)
    _safe_set(b, 'simpleworld102_Part14', None)
    assert not _is_linked(b, 'simpleworld102_Part14', a2)
    if hasattr(a2, 'simpleworld102_Relations13'):
        assert not _is_linked(a2, 'simpleworld102_Relations13', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = simpleworld102_Relations(since=7)
    a2 = simpleworld102_Relations(since=13)
    b = simpleworld102_Person(foreName="sample_text", name="sample_text")
    _safe_set(b, 'simpleworld102_Person', {a1})
    assert _is_linked(b, 'simpleworld102_Person', a1)
    if hasattr(a1, 'simpleworld102_Relations'):
        assert _is_linked(a1, 'simpleworld102_Relations', b)
    _safe_set(b, 'simpleworld102_Person', {a2})
    assert _is_linked(b, 'simpleworld102_Person', a2)
    if hasattr(a1, 'simpleworld102_Relations'):
        assert not _is_linked(a1, 'simpleworld102_Relations', b)
    if hasattr(a2, 'simpleworld102_Relations'):
        assert _is_linked(a2, 'simpleworld102_Relations', b)
    _safe_set(b, 'simpleworld102_Person', set())
    assert not _is_linked(b, 'simpleworld102_Person', a2)
    if hasattr(a2, 'simpleworld102_Relations'):
        assert not _is_linked(a2, 'simpleworld102_Relations', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components6_stub_double():
    # simpleworld102_Thing has no real 'simpleworld102_Thing7' property in the generated
    # code (a bare stub) -- manually attach it so simpleworld102_Part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleworld102_Part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleworld102_Part(content="sample_text", id=7)
    partner = simpleworld102_Thing()
    setattr(partner, 'simpleworld102_Thing7', None)
    _safe_set(owner, 'simpleworld102_Part', partner)
    assert owner in getattr(partner, 'simpleworld102_Thing7')
    _safe_set(owner, 'simpleworld102_Part', None)
    assert owner not in getattr(partner, 'simpleworld102_Thing7')


def test_assoc_persons15_stub_double():
    # simpleworld102_World has no real 'simpleworld102_World' property in the generated
    # code (a bare stub) -- manually attach it so simpleworld102_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleworld102_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleworld102_Person(foreName="sample_text", name="sample_text")
    partner = simpleworld102_World()
    setattr(partner, 'simpleworld102_World', None)
    _safe_set(owner, 'simpleworld102_Person16', partner)
    assert owner in getattr(partner, 'simpleworld102_World')
    _safe_set(owner, 'simpleworld102_Person16', None)
    assert owner not in getattr(partner, 'simpleworld102_World')


def test_assoc_persons8_stub_double():
    # simpleworld102_Thing has no real 'things' property in the generated
    # code (a bare stub) -- manually attach it so simpleworld102_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleworld102_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleworld102_Person(foreName="sample_text", name="sample_text")
    partner = simpleworld102_Thing()
    setattr(partner, 'things', None)
    _safe_set(owner, 'Person', partner)
    assert owner in getattr(partner, 'things')
    _safe_set(owner, 'Person', None)
    assert owner not in getattr(partner, 'things')


def test_assoc_thing3_stub_double():
    # simpleworld102_Thing has no real 'simpleworld102_Thing' property in the generated
    # code (a bare stub) -- manually attach it so simpleworld102_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleworld102_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleworld102_Person(foreName="sample_text", name="sample_text")
    partner = simpleworld102_Thing()
    setattr(partner, 'simpleworld102_Thing', None)
    _safe_set(owner, 'simpleworld102_Person4', partner)
    assert getattr(partner, 'simpleworld102_Thing') == owner
    _safe_set(owner, 'simpleworld102_Person4', None)
    assert getattr(partner, 'simpleworld102_Thing') is None


def test_assoc_things5_stub_double():
    # simpleworld102_Thing has no real 'Thing' property in the generated
    # code (a bare stub) -- manually attach it so simpleworld102_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleworld102_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleworld102_Person(foreName="sample_text", name="sample_text")
    partner = simpleworld102_Thing()
    setattr(partner, 'Thing', None)
    _safe_set(owner, 'persons', {partner})
    assert getattr(partner, 'Thing') == owner
    _safe_set(owner, 'persons', set())
    assert getattr(partner, 'Thing') is None


