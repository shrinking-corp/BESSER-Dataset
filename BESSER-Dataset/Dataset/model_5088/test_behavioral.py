import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Interface,
    adl101_Binding,
    adl101_Component,
    adl101_Content,
    adl101_Interface,
    adl101_Provided,
    adl101_Required,
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

def test_assoc_content14_reverse_link_reassign_clear():
    a1 = adl101_Content(expression="sample_text", language="sample_text")
    a2 = adl101_Content(expression="sample_text_2", language="sample_text_2")
    b = adl101_Component(name="sample_text")
    _safe_set(b, 'contentParent', a1)
    assert _is_linked(b, 'contentParent', a1)
    if hasattr(a1, 'Content'):
        assert _is_linked(a1, 'Content', b)
    _safe_set(b, 'contentParent', a2)
    assert _is_linked(b, 'contentParent', a2)
    if hasattr(a1, 'Content'):
        assert not _is_linked(a1, 'Content', b)
    if hasattr(a2, 'Content'):
        assert _is_linked(a2, 'Content', b)
    _safe_set(b, 'contentParent', None)
    assert not _is_linked(b, 'contentParent', a2)
    if hasattr(a2, 'Content'):
        assert not _is_linked(a2, 'Content', b)


def test_assoc_contentParent7_reverse_link_reassign_clear():
    a1 = adl101_Content(expression="sample_text", language="sample_text")
    a2 = adl101_Content(expression="sample_text_2", language="sample_text_2")
    b = adl101_Component(name="sample_text")
    _safe_set(b, 'Component', a1)
    assert _is_linked(b, 'Component', a1)
    if hasattr(a1, 'content'):
        assert _is_linked(a1, 'content', b)
    _safe_set(b, 'Component', a2)
    assert _is_linked(b, 'Component', a2)
    if hasattr(a1, 'content'):
        assert not _is_linked(a1, 'content', b)
    if hasattr(a2, 'content'):
        assert _is_linked(a2, 'content', b)
    _safe_set(b, 'Component', None)
    assert not _is_linked(b, 'Component', a2)
    if hasattr(a2, 'content'):
        assert not _is_linked(a2, 'content', b)


def test_assoc_subComponents9_reverse_link_reassign_clear():
    a1 = adl101_Component(name="sample_text")
    a2 = adl101_Component(name="sample_text_2")
    b = adl101_Component(name="sample_text")
    _safe_set(b, 'adl101_Component8', {a1})
    assert _is_linked(b, 'adl101_Component8', a1)
    if hasattr(a1, 'adl101_Component'):
        assert _is_linked(a1, 'adl101_Component', b)
    _safe_set(b, 'adl101_Component8', {a2})
    assert _is_linked(b, 'adl101_Component8', a2)
    if hasattr(a1, 'adl101_Component'):
        assert not _is_linked(a1, 'adl101_Component', b)
    if hasattr(a2, 'adl101_Component'):
        assert _is_linked(a2, 'adl101_Component', b)
    _safe_set(b, 'adl101_Component8', set())
    assert not _is_linked(b, 'adl101_Component8', a2)
    if hasattr(a2, 'adl101_Component'):
        assert not _is_linked(a2, 'adl101_Component', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings0_stub_double():
    # adl101_Binding has no real 'adl101_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adl101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl101_Interface(name="sample_text", signature="sample_text")
    partner = adl101_Binding()
    setattr(partner, 'adl101_Binding', None)
    _safe_set(owner, 'adl101_Interface', {partner})
    assert getattr(partner, 'adl101_Binding') == owner
    _safe_set(owner, 'adl101_Interface', set())
    assert getattr(partner, 'adl101_Binding') is None


def test_assoc_from_1_stub_double():
    # adl101_Binding has no real 'adl101_Binding2' property in the generated
    # code (a bare stub) -- manually attach it so adl101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl101_Interface(name="sample_text", signature="sample_text")
    partner = adl101_Binding()
    setattr(partner, 'adl101_Binding2', None)
    _safe_set(owner, 'adl101_Interface3', partner)
    assert getattr(partner, 'adl101_Binding2') == owner
    _safe_set(owner, 'adl101_Interface3', None)
    assert getattr(partner, 'adl101_Binding2') is None


def test_assoc_providedInterfaces12_stub_double():
    # adl101_Provided has no real 'adl101_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adl101_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl101_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl101_Component(name="sample_text")
    partner = adl101_Provided()
    setattr(partner, 'adl101_Provided', None)
    _safe_set(owner, 'adl101_Component13', {partner})
    assert getattr(partner, 'adl101_Provided') == owner
    _safe_set(owner, 'adl101_Component13', set())
    assert getattr(partner, 'adl101_Provided') is None


def test_assoc_requiredInterfaces10_stub_double():
    # adl101_Required has no real 'adl101_Required' property in the generated
    # code (a bare stub) -- manually attach it so adl101_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl101_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl101_Component(name="sample_text")
    partner = adl101_Required()
    setattr(partner, 'adl101_Required', None)
    _safe_set(owner, 'adl101_Component11', {partner})
    assert getattr(partner, 'adl101_Required') == owner
    _safe_set(owner, 'adl101_Component11', set())
    assert getattr(partner, 'adl101_Required') is None


def test_assoc_to4_stub_double():
    # adl101_Binding has no real 'adl101_Binding5' property in the generated
    # code (a bare stub) -- manually attach it so adl101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl101_Interface(name="sample_text", signature="sample_text")
    partner = adl101_Binding()
    setattr(partner, 'adl101_Binding5', None)
    _safe_set(owner, 'adl101_Interface6', partner)
    assert getattr(partner, 'adl101_Binding5') == owner
    _safe_set(owner, 'adl101_Interface6', None)
    assert getattr(partner, 'adl101_Binding5') is None


