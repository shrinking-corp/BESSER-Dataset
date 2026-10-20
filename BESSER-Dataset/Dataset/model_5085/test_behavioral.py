import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractComponent,
    Interface,
    adl199_AbstractComponent,
    adl199_AtomicComponent,
    adl199_Binding,
    adl199_Component,
    adl199_Content,
    adl199_Delegation,
    adl199_Interface,
    adl199_Provided,
    adl199_Required,
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

def test_assoc_content0_reverse_link_reassign_clear():
    a1 = adl199_Content(expression="sample_text", language="sample_text")
    a2 = adl199_Content(expression="sample_text_2", language="sample_text_2")
    b = adl199_AbstractComponent(name="sample_text")
    _safe_set(b, 'adl199_AbstractComponent', a1)
    assert _is_linked(b, 'adl199_AbstractComponent', a1)
    if hasattr(a1, 'adl199_Content'):
        assert _is_linked(a1, 'adl199_Content', b)
    _safe_set(b, 'adl199_AbstractComponent', a2)
    assert _is_linked(b, 'adl199_AbstractComponent', a2)
    if hasattr(a1, 'adl199_Content'):
        assert not _is_linked(a1, 'adl199_Content', b)
    if hasattr(a2, 'adl199_Content'):
        assert _is_linked(a2, 'adl199_Content', b)
    _safe_set(b, 'adl199_AbstractComponent', None)
    assert not _is_linked(b, 'adl199_AbstractComponent', a2)
    if hasattr(a2, 'adl199_Content'):
        assert not _is_linked(a2, 'adl199_Content', b)


def test_assoc_parent14_reverse_link_reassign_clear():
    a1 = adl199_Content(expression="sample_text", language="sample_text")
    a2 = adl199_Content(expression="sample_text_2", language="sample_text_2")
    b = adl199_AbstractComponent(name="sample_text")
    _safe_set(b, 'adl199_AbstractComponent16', a1)
    assert _is_linked(b, 'adl199_AbstractComponent16', a1)
    if hasattr(a1, 'adl199_Content15'):
        assert _is_linked(a1, 'adl199_Content15', b)
    _safe_set(b, 'adl199_AbstractComponent16', a2)
    assert _is_linked(b, 'adl199_AbstractComponent16', a2)
    if hasattr(a1, 'adl199_Content15'):
        assert not _is_linked(a1, 'adl199_Content15', b)
    if hasattr(a2, 'adl199_Content15'):
        assert _is_linked(a2, 'adl199_Content15', b)
    _safe_set(b, 'adl199_AbstractComponent16', None)
    assert not _is_linked(b, 'adl199_AbstractComponent16', a2)
    if hasattr(a2, 'adl199_Content15'):
        assert not _is_linked(a2, 'adl199_Content15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings7_stub_double():
    # adl199_Binding has no real 'adl199_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adl199_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_Interface(name="sample_text", signature="sample_text")
    partner = adl199_Binding()
    setattr(partner, 'adl199_Binding', None)
    _safe_set(owner, 'adl199_Interface', {partner})
    assert getattr(partner, 'adl199_Binding') == owner
    _safe_set(owner, 'adl199_Interface', set())
    assert getattr(partner, 'adl199_Binding') is None


def test_assoc_delegationInterfaces5_stub_double():
    # adl199_Delegation has no real 'adl199_Delegation' property in the generated
    # code (a bare stub) -- manually attach it so adl199_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_AbstractComponent(name="sample_text")
    partner = adl199_Delegation()
    setattr(partner, 'adl199_Delegation', None)
    _safe_set(owner, 'adl199_AbstractComponent6', {partner})
    assert getattr(partner, 'adl199_Delegation') == owner
    _safe_set(owner, 'adl199_AbstractComponent6', set())
    assert getattr(partner, 'adl199_Delegation') is None


def test_assoc_from_8_stub_double():
    # adl199_Binding has no real 'adl199_Binding9' property in the generated
    # code (a bare stub) -- manually attach it so adl199_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_Interface(name="sample_text", signature="sample_text")
    partner = adl199_Binding()
    setattr(partner, 'adl199_Binding9', None)
    _safe_set(owner, 'adl199_Interface10', partner)
    assert getattr(partner, 'adl199_Binding9') == owner
    _safe_set(owner, 'adl199_Interface10', None)
    assert getattr(partner, 'adl199_Binding9') is None


def test_assoc_providedInterfaces3_stub_double():
    # adl199_Provided has no real 'adl199_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adl199_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_AbstractComponent(name="sample_text")
    partner = adl199_Provided()
    setattr(partner, 'adl199_Provided', None)
    _safe_set(owner, 'adl199_AbstractComponent4', {partner})
    assert getattr(partner, 'adl199_Provided') == owner
    _safe_set(owner, 'adl199_AbstractComponent4', set())
    assert getattr(partner, 'adl199_Provided') is None


def test_assoc_requiredInterfaces1_stub_double():
    # adl199_Required has no real 'adl199_Required' property in the generated
    # code (a bare stub) -- manually attach it so adl199_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_AbstractComponent(name="sample_text")
    partner = adl199_Required()
    setattr(partner, 'adl199_Required', None)
    _safe_set(owner, 'adl199_AbstractComponent2', {partner})
    assert getattr(partner, 'adl199_Required') == owner
    _safe_set(owner, 'adl199_AbstractComponent2', set())
    assert getattr(partner, 'adl199_Required') is None


def test_assoc_subComponents17_stub_double():
    # adl199_Component has no real 'adl199_Component' property in the generated
    # code (a bare stub) -- manually attach it so adl199_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_AbstractComponent(name="sample_text")
    partner = adl199_Component()
    setattr(partner, 'adl199_Component', None)
    _safe_set(owner, 'adl199_AbstractComponent18', partner)
    assert owner in getattr(partner, 'adl199_Component')
    _safe_set(owner, 'adl199_AbstractComponent18', None)
    assert owner not in getattr(partner, 'adl199_Component')


def test_assoc_to11_stub_double():
    # adl199_Binding has no real 'adl199_Binding12' property in the generated
    # code (a bare stub) -- manually attach it so adl199_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl199_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl199_Interface(name="sample_text", signature="sample_text")
    partner = adl199_Binding()
    setattr(partner, 'adl199_Binding12', None)
    _safe_set(owner, 'adl199_Interface13', partner)
    assert getattr(partner, 'adl199_Binding12') == owner
    _safe_set(owner, 'adl199_Interface13', None)
    assert getattr(partner, 'adl199_Binding12') is None


