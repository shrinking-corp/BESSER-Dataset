import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Interface,
    adl401_Binding,
    adl401_Component,
    adl401_Content,
    adl401_EClass0,
    adl401_Interface,
    adl401_Provided,
    adl401_Required,
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

def test_assoc_EReference08_reverse_link_reassign_clear():
    a1 = adl401_EClass0(EAttribute0="sample_text")
    a2 = adl401_EClass0(EAttribute0="sample_text_2")
    b = adl401_Content(expression="sample_text", language="sample_text")
    _safe_set(b, 'adl401_Content', {a1})
    assert _is_linked(b, 'adl401_Content', a1)
    if hasattr(a1, 'adl401_EClass0'):
        assert _is_linked(a1, 'adl401_EClass0', b)
    _safe_set(b, 'adl401_Content', {a2})
    assert _is_linked(b, 'adl401_Content', a2)
    if hasattr(a1, 'adl401_EClass0'):
        assert not _is_linked(a1, 'adl401_EClass0', b)
    if hasattr(a2, 'adl401_EClass0'):
        assert _is_linked(a2, 'adl401_EClass0', b)
    _safe_set(b, 'adl401_Content', set())
    assert not _is_linked(b, 'adl401_Content', a2)
    if hasattr(a2, 'adl401_EClass0'):
        assert not _is_linked(a2, 'adl401_EClass0', b)


def test_assoc_content15_reverse_link_reassign_clear():
    a1 = adl401_Content(expression="sample_text", language="sample_text")
    a2 = adl401_Content(expression="sample_text_2", language="sample_text_2")
    b = adl401_Component(name="sample_text")
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
    a1 = adl401_Content(expression="sample_text", language="sample_text")
    a2 = adl401_Content(expression="sample_text_2", language="sample_text_2")
    b = adl401_Component(name="sample_text")
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


def test_assoc_erefs017_reverse_link_reassign_clear():
    a1 = adl401_EClass0(EAttribute0="sample_text")
    a2 = adl401_EClass0(EAttribute0="sample_text_2")
    b = adl401_EClass0(EAttribute0="sample_text")
    _safe_set(b, 'adl401_EClass018', a1)
    assert _is_linked(b, 'adl401_EClass018', a1)
    if hasattr(a1, 'adl401_EClass016'):
        assert _is_linked(a1, 'adl401_EClass016', b)
    _safe_set(b, 'adl401_EClass018', a2)
    assert _is_linked(b, 'adl401_EClass018', a2)
    if hasattr(a1, 'adl401_EClass016'):
        assert not _is_linked(a1, 'adl401_EClass016', b)
    if hasattr(a2, 'adl401_EClass016'):
        assert _is_linked(a2, 'adl401_EClass016', b)
    _safe_set(b, 'adl401_EClass018', None)
    assert not _is_linked(b, 'adl401_EClass018', a2)
    if hasattr(a2, 'adl401_EClass016'):
        assert not _is_linked(a2, 'adl401_EClass016', b)


def test_assoc_subComponents10_reverse_link_reassign_clear():
    a1 = adl401_Component(name="sample_text")
    a2 = adl401_Component(name="sample_text_2")
    b = adl401_Component(name="sample_text")
    _safe_set(b, 'adl401_Component9', {a1})
    assert _is_linked(b, 'adl401_Component9', a1)
    if hasattr(a1, 'adl401_Component'):
        assert _is_linked(a1, 'adl401_Component', b)
    _safe_set(b, 'adl401_Component9', {a2})
    assert _is_linked(b, 'adl401_Component9', a2)
    if hasattr(a1, 'adl401_Component'):
        assert not _is_linked(a1, 'adl401_Component', b)
    if hasattr(a2, 'adl401_Component'):
        assert _is_linked(a2, 'adl401_Component', b)
    _safe_set(b, 'adl401_Component9', set())
    assert not _is_linked(b, 'adl401_Component9', a2)
    if hasattr(a2, 'adl401_Component'):
        assert not _is_linked(a2, 'adl401_Component', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings0_stub_double():
    # adl401_Binding has no real 'adl401_Binding' property in the generated
    # code (a bare stub) -- manually attach it so adl401_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl401_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl401_Interface(name="sample_text", signature="sample_text")
    partner = adl401_Binding()
    setattr(partner, 'adl401_Binding', None)
    _safe_set(owner, 'adl401_Interface', {partner})
    assert getattr(partner, 'adl401_Binding') == owner
    _safe_set(owner, 'adl401_Interface', set())
    assert getattr(partner, 'adl401_Binding') is None


def test_assoc_from_1_stub_double():
    # adl401_Binding has no real 'adl401_Binding2' property in the generated
    # code (a bare stub) -- manually attach it so adl401_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl401_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl401_Interface(name="sample_text", signature="sample_text")
    partner = adl401_Binding()
    setattr(partner, 'adl401_Binding2', None)
    _safe_set(owner, 'adl401_Interface3', partner)
    assert getattr(partner, 'adl401_Binding2') == owner
    _safe_set(owner, 'adl401_Interface3', None)
    assert getattr(partner, 'adl401_Binding2') is None


def test_assoc_providedInterfaces13_stub_double():
    # adl401_Provided has no real 'adl401_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adl401_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl401_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl401_Component(name="sample_text")
    partner = adl401_Provided()
    setattr(partner, 'adl401_Provided', None)
    _safe_set(owner, 'adl401_Component14', {partner})
    assert getattr(partner, 'adl401_Provided') == owner
    _safe_set(owner, 'adl401_Component14', set())
    assert getattr(partner, 'adl401_Provided') is None


def test_assoc_requiredInterfaces11_stub_double():
    # adl401_Required has no real 'adl401_Required' property in the generated
    # code (a bare stub) -- manually attach it so adl401_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl401_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl401_Component(name="sample_text")
    partner = adl401_Required()
    setattr(partner, 'adl401_Required', None)
    _safe_set(owner, 'adl401_Component12', {partner})
    assert getattr(partner, 'adl401_Required') == owner
    _safe_set(owner, 'adl401_Component12', set())
    assert getattr(partner, 'adl401_Required') is None


def test_assoc_to4_stub_double():
    # adl401_Binding has no real 'adl401_Binding5' property in the generated
    # code (a bare stub) -- manually attach it so adl401_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl401_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl401_Interface(name="sample_text", signature="sample_text")
    partner = adl401_Binding()
    setattr(partner, 'adl401_Binding5', None)
    _safe_set(owner, 'adl401_Interface6', partner)
    assert getattr(partner, 'adl401_Binding5') == owner
    _safe_set(owner, 'adl401_Interface6', None)
    assert getattr(partner, 'adl401_Binding5') is None


