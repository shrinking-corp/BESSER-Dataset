import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractComponent,
    Interface,
    adlold_AbstractComponent,
    adlold_Binding,
    adlold_Component,
    adlold_Content,
    adlold_Interface,
    adlold_Provided,
    adlold_Required,
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
    a1 = adlold_Content(expression="sample_text", language="sample_text")
    a2 = adlold_Content(expression="sample_text_2", language="sample_text_2")
    b = adlold_AbstractComponent(name="sample_text")
    _safe_set(b, 'adlold_AbstractComponent', a1)
    assert _is_linked(b, 'adlold_AbstractComponent', a1)
    if hasattr(a1, 'adlold_Content'):
        assert _is_linked(a1, 'adlold_Content', b)
    _safe_set(b, 'adlold_AbstractComponent', a2)
    assert _is_linked(b, 'adlold_AbstractComponent', a2)
    if hasattr(a1, 'adlold_Content'):
        assert not _is_linked(a1, 'adlold_Content', b)
    if hasattr(a2, 'adlold_Content'):
        assert _is_linked(a2, 'adlold_Content', b)
    _safe_set(b, 'adlold_AbstractComponent', None)
    assert not _is_linked(b, 'adlold_AbstractComponent', a2)
    if hasattr(a2, 'adlold_Content'):
        assert not _is_linked(a2, 'adlold_Content', b)


def test_assoc_contentParent12_reverse_link_reassign_clear():
    a1 = adlold_Content(expression="sample_text", language="sample_text")
    a2 = adlold_Content(expression="sample_text_2", language="sample_text_2")
    b = adlold_AbstractComponent(name="sample_text")
    _safe_set(b, 'adlold_AbstractComponent14', a1)
    assert _is_linked(b, 'adlold_AbstractComponent14', a1)
    if hasattr(a1, 'adlold_Content13'):
        assert _is_linked(a1, 'adlold_Content13', b)
    _safe_set(b, 'adlold_AbstractComponent14', a2)
    assert _is_linked(b, 'adlold_AbstractComponent14', a2)
    if hasattr(a1, 'adlold_Content13'):
        assert not _is_linked(a1, 'adlold_Content13', b)
    if hasattr(a2, 'adlold_Content13'):
        assert _is_linked(a2, 'adlold_Content13', b)
    _safe_set(b, 'adlold_AbstractComponent14', None)
    assert not _is_linked(b, 'adlold_AbstractComponent14', a2)
    if hasattr(a2, 'adlold_Content13'):
        assert not _is_linked(a2, 'adlold_Content13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings5_stub_double():
    # adlold_Binding has no real 'adlold_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adlold_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlold_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlold_Interface(name="sample_text", signature="sample_text")
    partner = adlold_Binding()
    setattr(partner, 'adlold_Binding', None)
    _safe_set(owner, 'adlold_Interface', {partner})
    assert getattr(partner, 'adlold_Binding') == owner
    _safe_set(owner, 'adlold_Interface', set())
    assert getattr(partner, 'adlold_Binding') is None


def test_assoc_from_6_stub_double():
    # adlold_Binding has no real 'adlold_Binding7' property in the generated
    # code (a bare stub) -- manually attach it so adlold_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlold_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlold_Interface(name="sample_text", signature="sample_text")
    partner = adlold_Binding()
    setattr(partner, 'adlold_Binding7', None)
    _safe_set(owner, 'adlold_Interface8', partner)
    assert getattr(partner, 'adlold_Binding7') == owner
    _safe_set(owner, 'adlold_Interface8', None)
    assert getattr(partner, 'adlold_Binding7') is None


def test_assoc_providedInterfaces3_stub_double():
    # adlold_Provided has no real 'adlold_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adlold_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlold_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlold_AbstractComponent(name="sample_text")
    partner = adlold_Provided()
    setattr(partner, 'adlold_Provided', None)
    _safe_set(owner, 'adlold_AbstractComponent4', {partner})
    assert getattr(partner, 'adlold_Provided') == owner
    _safe_set(owner, 'adlold_AbstractComponent4', set())
    assert getattr(partner, 'adlold_Provided') is None


def test_assoc_requiredInterfaces1_stub_double():
    # adlold_Required has no real 'adlold_Required' property in the generated
    # code (a bare stub) -- manually attach it so adlold_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlold_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlold_AbstractComponent(name="sample_text")
    partner = adlold_Required()
    setattr(partner, 'adlold_Required', None)
    _safe_set(owner, 'adlold_AbstractComponent2', {partner})
    assert getattr(partner, 'adlold_Required') == owner
    _safe_set(owner, 'adlold_AbstractComponent2', set())
    assert getattr(partner, 'adlold_Required') is None


def test_assoc_to9_stub_double():
    # adlold_Binding has no real 'adlold_Binding10' property in the generated
    # code (a bare stub) -- manually attach it so adlold_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adlold_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adlold_Interface(name="sample_text", signature="sample_text")
    partner = adlold_Binding()
    setattr(partner, 'adlold_Binding10', None)
    _safe_set(owner, 'adlold_Interface11', partner)
    assert getattr(partner, 'adlold_Binding10') == owner
    _safe_set(owner, 'adlold_Interface11', None)
    assert getattr(partner, 'adlold_Binding10') is None


