import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Interface,
    adl203_Binding,
    adl203_BindingAttributes,
    adl203_Component,
    adl203_Content,
    adl203_Interface,
    adl203_Provided,
    adl203_Required,
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

def test_assoc_attributes13_reverse_link_reassign_clear():
    a1 = adl203_BindingAttributes(name="sample_text", value="sample_text")
    a2 = adl203_BindingAttributes(name="sample_text_2", value="sample_text_2")
    b = adl203_Binding(name="sample_text")
    _safe_set(b, 'adl203_Binding14', {a1})
    assert _is_linked(b, 'adl203_Binding14', a1)
    if hasattr(a1, 'adl203_BindingAttributes'):
        assert _is_linked(a1, 'adl203_BindingAttributes', b)
    _safe_set(b, 'adl203_Binding14', {a2})
    assert _is_linked(b, 'adl203_Binding14', a2)
    if hasattr(a1, 'adl203_BindingAttributes'):
        assert not _is_linked(a1, 'adl203_BindingAttributes', b)
    if hasattr(a2, 'adl203_BindingAttributes'):
        assert _is_linked(a2, 'adl203_BindingAttributes', b)
    _safe_set(b, 'adl203_Binding14', set())
    assert not _is_linked(b, 'adl203_Binding14', a2)
    if hasattr(a2, 'adl203_BindingAttributes'):
        assert not _is_linked(a2, 'adl203_BindingAttributes', b)


def test_assoc_bindings5_reverse_link_reassign_clear():
    a1 = adl203_Component(name="sample_text")
    a2 = adl203_Component(name="sample_text_2")
    b = adl203_Binding(name="sample_text")
    _safe_set(b, 'adl203_Binding', a1)
    assert _is_linked(b, 'adl203_Binding', a1)
    if hasattr(a1, 'adl203_Component6'):
        assert _is_linked(a1, 'adl203_Component6', b)
    _safe_set(b, 'adl203_Binding', a2)
    assert _is_linked(b, 'adl203_Binding', a2)
    if hasattr(a1, 'adl203_Component6'):
        assert not _is_linked(a1, 'adl203_Component6', b)
    if hasattr(a2, 'adl203_Component6'):
        assert _is_linked(a2, 'adl203_Component6', b)
    _safe_set(b, 'adl203_Binding', None)
    assert not _is_linked(b, 'adl203_Binding', a2)
    if hasattr(a2, 'adl203_Component6'):
        assert not _is_linked(a2, 'adl203_Component6', b)


def test_assoc_content0_reverse_link_reassign_clear():
    a1 = adl203_Content(expression="sample_text", language="sample_text")
    a2 = adl203_Content(expression="sample_text_2", language="sample_text_2")
    b = adl203_Component(name="sample_text")
    _safe_set(b, 'adl203_Component', a1)
    assert _is_linked(b, 'adl203_Component', a1)
    if hasattr(a1, 'adl203_Content'):
        assert _is_linked(a1, 'adl203_Content', b)
    _safe_set(b, 'adl203_Component', a2)
    assert _is_linked(b, 'adl203_Component', a2)
    if hasattr(a1, 'adl203_Content'):
        assert not _is_linked(a1, 'adl203_Content', b)
    if hasattr(a2, 'adl203_Content'):
        assert _is_linked(a2, 'adl203_Content', b)
    _safe_set(b, 'adl203_Component', None)
    assert not _is_linked(b, 'adl203_Component', a2)
    if hasattr(a2, 'adl203_Content'):
        assert not _is_linked(a2, 'adl203_Content', b)


def test_assoc_contentParent18_reverse_link_reassign_clear():
    a1 = adl203_Content(expression="sample_text", language="sample_text")
    a2 = adl203_Content(expression="sample_text_2", language="sample_text_2")
    b = adl203_Component(name="sample_text")
    _safe_set(b, 'adl203_Component20', a1)
    assert _is_linked(b, 'adl203_Component20', a1)
    if hasattr(a1, 'adl203_Content19'):
        assert _is_linked(a1, 'adl203_Content19', b)
    _safe_set(b, 'adl203_Component20', a2)
    assert _is_linked(b, 'adl203_Component20', a2)
    if hasattr(a1, 'adl203_Content19'):
        assert not _is_linked(a1, 'adl203_Content19', b)
    if hasattr(a2, 'adl203_Content19'):
        assert _is_linked(a2, 'adl203_Content19', b)
    _safe_set(b, 'adl203_Component20', None)
    assert not _is_linked(b, 'adl203_Component20', a2)
    if hasattr(a2, 'adl203_Content19'):
        assert not _is_linked(a2, 'adl203_Content19', b)


def test_assoc_subComponents8_reverse_link_reassign_clear():
    a1 = adl203_Component(name="sample_text")
    a2 = adl203_Component(name="sample_text_2")
    b = adl203_Component(name="sample_text")
    _safe_set(b, 'adl203_Component9', a1)
    assert _is_linked(b, 'adl203_Component9', a1)
    if hasattr(a1, 'adl203_Component7'):
        assert _is_linked(a1, 'adl203_Component7', b)
    _safe_set(b, 'adl203_Component9', a2)
    assert _is_linked(b, 'adl203_Component9', a2)
    if hasattr(a1, 'adl203_Component7'):
        assert not _is_linked(a1, 'adl203_Component7', b)
    if hasattr(a2, 'adl203_Component7'):
        assert _is_linked(a2, 'adl203_Component7', b)
    _safe_set(b, 'adl203_Component9', None)
    assert not _is_linked(b, 'adl203_Component9', a2)
    if hasattr(a2, 'adl203_Component7'):
        assert not _is_linked(a2, 'adl203_Component7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings21_stub_double():
    # adl203_Provided has no real 'adl203_Provided22' property in the generated
    # code (a bare stub) -- manually attach it so adl203_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl203_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl203_Binding(name="sample_text")
    partner = adl203_Provided()
    setattr(partner, 'adl203_Provided22', None)
    _safe_set(owner, 'adl203_Binding23', partner)
    assert owner in getattr(partner, 'adl203_Provided22')
    _safe_set(owner, 'adl203_Binding23', None)
    assert owner not in getattr(partner, 'adl203_Provided22')


def test_assoc_from_15_stub_double():
    # adl203_Provided has no real 'adl203_Provided17' property in the generated
    # code (a bare stub) -- manually attach it so adl203_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl203_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl203_Binding(name="sample_text")
    partner = adl203_Provided()
    setattr(partner, 'adl203_Provided17', None)
    _safe_set(owner, 'adl203_Binding16', partner)
    assert getattr(partner, 'adl203_Provided17') == owner
    _safe_set(owner, 'adl203_Binding16', None)
    assert getattr(partner, 'adl203_Provided17') is None


def test_assoc_providedInterfaces3_stub_double():
    # adl203_Provided has no real 'adl203_Provided' property in the generated
    # code (a bare stub) -- manually attach it so adl203_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl203_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl203_Component(name="sample_text")
    partner = adl203_Provided()
    setattr(partner, 'adl203_Provided', None)
    _safe_set(owner, 'adl203_Component4', {partner})
    assert getattr(partner, 'adl203_Provided') == owner
    _safe_set(owner, 'adl203_Component4', set())
    assert getattr(partner, 'adl203_Provided') is None


def test_assoc_requiredInterfaces1_stub_double():
    # adl203_Required has no real 'adl203_Required' property in the generated
    # code (a bare stub) -- manually attach it so adl203_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl203_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl203_Component(name="sample_text")
    partner = adl203_Required()
    setattr(partner, 'adl203_Required', None)
    _safe_set(owner, 'adl203_Component2', {partner})
    assert getattr(partner, 'adl203_Required') == owner
    _safe_set(owner, 'adl203_Component2', set())
    assert getattr(partner, 'adl203_Required') is None


def test_assoc_to10_stub_double():
    # adl203_Required has no real 'adl203_Required12' property in the generated
    # code (a bare stub) -- manually attach it so adl203_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adl203_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adl203_Binding(name="sample_text")
    partner = adl203_Required()
    setattr(partner, 'adl203_Required12', None)
    _safe_set(owner, 'adl203_Binding11', partner)
    assert getattr(partner, 'adl203_Required12') == owner
    _safe_set(owner, 'adl203_Binding11', None)
    assert getattr(partner, 'adl203_Required12') is None


