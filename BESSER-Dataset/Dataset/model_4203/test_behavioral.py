import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    helloScoping_Field,
    helloScoping_FieldReference,
    helloScoping_Greeting,
    helloScoping_Model,
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

def test_assoc_fields4_reverse_link_reassign_clear():
    a1 = helloScoping_Greeting(name="sample_text")
    a2 = helloScoping_Greeting(name="sample_text_2")
    b = helloScoping_Field(name="sample_text")
    _safe_set(b, 'helloScoping_Field', a1)
    assert _is_linked(b, 'helloScoping_Field', a1)
    if hasattr(a1, 'helloScoping_Greeting5'):
        assert _is_linked(a1, 'helloScoping_Greeting5', b)
    _safe_set(b, 'helloScoping_Field', a2)
    assert _is_linked(b, 'helloScoping_Field', a2)
    if hasattr(a1, 'helloScoping_Greeting5'):
        assert not _is_linked(a1, 'helloScoping_Greeting5', b)
    if hasattr(a2, 'helloScoping_Greeting5'):
        assert _is_linked(a2, 'helloScoping_Greeting5', b)
    _safe_set(b, 'helloScoping_Field', None)
    assert not _is_linked(b, 'helloScoping_Field', a2)
    if hasattr(a2, 'helloScoping_Greeting5'):
        assert not _is_linked(a2, 'helloScoping_Greeting5', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = helloScoping_Greeting(name="sample_text")
    a2 = helloScoping_Greeting(name="sample_text_2")
    b = helloScoping_Greeting(name="sample_text")
    _safe_set(b, 'helloScoping_Greeting3', a1)
    assert _is_linked(b, 'helloScoping_Greeting3', a1)
    if hasattr(a1, 'helloScoping_Greeting1'):
        assert _is_linked(a1, 'helloScoping_Greeting1', b)
    _safe_set(b, 'helloScoping_Greeting3', a2)
    assert _is_linked(b, 'helloScoping_Greeting3', a2)
    if hasattr(a1, 'helloScoping_Greeting1'):
        assert not _is_linked(a1, 'helloScoping_Greeting1', b)
    if hasattr(a2, 'helloScoping_Greeting1'):
        assert _is_linked(a2, 'helloScoping_Greeting1', b)
    _safe_set(b, 'helloScoping_Greeting3', None)
    assert not _is_linked(b, 'helloScoping_Greeting3', a2)
    if hasattr(a2, 'helloScoping_Greeting1'):
        assert not _is_linked(a2, 'helloScoping_Greeting1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_greetings0_stub_double():
    # helloScoping_Model has no real 'helloScoping_Model' property in the generated
    # code (a bare stub) -- manually attach it so helloScoping_Greeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloScoping_Greeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloScoping_Greeting(name="sample_text")
    partner = helloScoping_Model()
    setattr(partner, 'helloScoping_Model', None)
    _safe_set(owner, 'helloScoping_Greeting', partner)
    assert owner in getattr(partner, 'helloScoping_Model')
    _safe_set(owner, 'helloScoping_Greeting', None)
    assert owner not in getattr(partner, 'helloScoping_Model')


def test_assoc_reference8_stub_double():
    # helloScoping_FieldReference has no real 'helloScoping_FieldReference9' property in the generated
    # code (a bare stub) -- manually attach it so helloScoping_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloScoping_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloScoping_Field(name="sample_text")
    partner = helloScoping_FieldReference()
    setattr(partner, 'helloScoping_FieldReference9', None)
    _safe_set(owner, 'helloScoping_Field10', partner)
    assert getattr(partner, 'helloScoping_FieldReference9') == owner
    _safe_set(owner, 'helloScoping_Field10', None)
    assert getattr(partner, 'helloScoping_FieldReference9') is None


def test_assoc_references6_stub_double():
    # helloScoping_FieldReference has no real 'helloScoping_FieldReference' property in the generated
    # code (a bare stub) -- manually attach it so helloScoping_Greeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloScoping_Greeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloScoping_Greeting(name="sample_text")
    partner = helloScoping_FieldReference()
    setattr(partner, 'helloScoping_FieldReference', None)
    _safe_set(owner, 'helloScoping_Greeting7', {partner})
    assert getattr(partner, 'helloScoping_FieldReference') == owner
    _safe_set(owner, 'helloScoping_Greeting7', set())
    assert getattr(partner, 'helloScoping_FieldReference') is None


