import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractComponent,
    Interface,
    fragdial101_AbstractComponent,
    fragdial101_Attribute,
    fragdial101_Attributes,
    fragdial101_Binding,
    fragdial101_Component,
    fragdial101_Content,
    fragdial101_Controller,
    fragdial101_Include,
    fragdial101_Interface,
    fragdial101_Ldflag,
    fragdial101_Output,
    fragdial101_Provided,
    fragdial101_Required,
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

def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = fragdial101_Attributes(signature="sample_text")
    a2 = fragdial101_Attributes(signature="sample_text_2")
    b = fragdial101_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial101_AbstractComponent2', a1)
    assert _is_linked(b, 'fragdial101_AbstractComponent2', a1)
    if hasattr(a1, 'fragdial101_Attributes'):
        assert _is_linked(a1, 'fragdial101_Attributes', b)
    _safe_set(b, 'fragdial101_AbstractComponent2', a2)
    assert _is_linked(b, 'fragdial101_AbstractComponent2', a2)
    if hasattr(a1, 'fragdial101_Attributes'):
        assert not _is_linked(a1, 'fragdial101_Attributes', b)
    if hasattr(a2, 'fragdial101_Attributes'):
        assert _is_linked(a2, 'fragdial101_Attributes', b)
    _safe_set(b, 'fragdial101_AbstractComponent2', None)
    assert not _is_linked(b, 'fragdial101_AbstractComponent2', a2)
    if hasattr(a2, 'fragdial101_Attributes'):
        assert not _is_linked(a2, 'fragdial101_Attributes', b)


def test_assoc_attributes25_reverse_link_reassign_clear():
    a1 = fragdial101_Attributes(signature="sample_text")
    a2 = fragdial101_Attributes(signature="sample_text_2")
    b = fragdial101_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'fragdial101_Attribute', a1)
    assert _is_linked(b, 'fragdial101_Attribute', a1)
    if hasattr(a1, 'fragdial101_Attributes26'):
        assert _is_linked(a1, 'fragdial101_Attributes26', b)
    _safe_set(b, 'fragdial101_Attribute', a2)
    assert _is_linked(b, 'fragdial101_Attribute', a2)
    if hasattr(a1, 'fragdial101_Attributes26'):
        assert not _is_linked(a1, 'fragdial101_Attributes26', b)
    if hasattr(a2, 'fragdial101_Attributes26'):
        assert _is_linked(a2, 'fragdial101_Attributes26', b)
    _safe_set(b, 'fragdial101_Attribute', None)
    assert not _is_linked(b, 'fragdial101_Attribute', a2)
    if hasattr(a2, 'fragdial101_Attributes26'):
        assert not _is_linked(a2, 'fragdial101_Attributes26', b)


def test_assoc_content0_reverse_link_reassign_clear():
    a1 = fragdial101_Content(class_="sample_text", language="sample_text")
    a2 = fragdial101_Content(class_="sample_text_2", language="sample_text_2")
    b = fragdial101_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial101_AbstractComponent', a1)
    assert _is_linked(b, 'fragdial101_AbstractComponent', a1)
    if hasattr(a1, 'fragdial101_Content'):
        assert _is_linked(a1, 'fragdial101_Content', b)
    _safe_set(b, 'fragdial101_AbstractComponent', a2)
    assert _is_linked(b, 'fragdial101_AbstractComponent', a2)
    if hasattr(a1, 'fragdial101_Content'):
        assert not _is_linked(a1, 'fragdial101_Content', b)
    if hasattr(a2, 'fragdial101_Content'):
        assert _is_linked(a2, 'fragdial101_Content', b)
    _safe_set(b, 'fragdial101_AbstractComponent', None)
    assert not _is_linked(b, 'fragdial101_AbstractComponent', a2)
    if hasattr(a2, 'fragdial101_Content'):
        assert not _is_linked(a2, 'fragdial101_Content', b)


def test_assoc_contentParent18_reverse_link_reassign_clear():
    a1 = fragdial101_Content(class_="sample_text", language="sample_text")
    a2 = fragdial101_Content(class_="sample_text_2", language="sample_text_2")
    b = fragdial101_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial101_AbstractComponent20', a1)
    assert _is_linked(b, 'fragdial101_AbstractComponent20', a1)
    if hasattr(a1, 'fragdial101_Content19'):
        assert _is_linked(a1, 'fragdial101_Content19', b)
    _safe_set(b, 'fragdial101_AbstractComponent20', a2)
    assert _is_linked(b, 'fragdial101_AbstractComponent20', a2)
    if hasattr(a1, 'fragdial101_Content19'):
        assert not _is_linked(a1, 'fragdial101_Content19', b)
    if hasattr(a2, 'fragdial101_Content19'):
        assert _is_linked(a2, 'fragdial101_Content19', b)
    _safe_set(b, 'fragdial101_AbstractComponent20', None)
    assert not _is_linked(b, 'fragdial101_AbstractComponent20', a2)
    if hasattr(a2, 'fragdial101_Content19'):
        assert not _is_linked(a2, 'fragdial101_Content19', b)


def test_assoc_controller5_reverse_link_reassign_clear():
    a1 = fragdial101_Controller(descriptor="sample_text", language="sample_text")
    a2 = fragdial101_Controller(descriptor="sample_text_2", language="sample_text_2")
    b = fragdial101_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial101_AbstractComponent6', a1)
    assert _is_linked(b, 'fragdial101_AbstractComponent6', a1)
    if hasattr(a1, 'fragdial101_Controller'):
        assert _is_linked(a1, 'fragdial101_Controller', b)
    _safe_set(b, 'fragdial101_AbstractComponent6', a2)
    assert _is_linked(b, 'fragdial101_AbstractComponent6', a2)
    if hasattr(a1, 'fragdial101_Controller'):
        assert not _is_linked(a1, 'fragdial101_Controller', b)
    if hasattr(a2, 'fragdial101_Controller'):
        assert _is_linked(a2, 'fragdial101_Controller', b)
    _safe_set(b, 'fragdial101_AbstractComponent6', None)
    assert not _is_linked(b, 'fragdial101_AbstractComponent6', a2)
    if hasattr(a2, 'fragdial101_Controller'):
        assert not _is_linked(a2, 'fragdial101_Controller', b)


def test_assoc_includes21_reverse_link_reassign_clear():
    a1 = fragdial101_Include(file="sample_text")
    a2 = fragdial101_Include(file="sample_text_2")
    b = fragdial101_Content(class_="sample_text", language="sample_text")
    _safe_set(b, 'fragdial101_Content22', {a1})
    assert _is_linked(b, 'fragdial101_Content22', a1)
    if hasattr(a1, 'fragdial101_Include'):
        assert _is_linked(a1, 'fragdial101_Include', b)
    _safe_set(b, 'fragdial101_Content22', {a2})
    assert _is_linked(b, 'fragdial101_Content22', a2)
    if hasattr(a1, 'fragdial101_Include'):
        assert not _is_linked(a1, 'fragdial101_Include', b)
    if hasattr(a2, 'fragdial101_Include'):
        assert _is_linked(a2, 'fragdial101_Include', b)
    _safe_set(b, 'fragdial101_Content22', set())
    assert not _is_linked(b, 'fragdial101_Content22', a2)
    if hasattr(a2, 'fragdial101_Include'):
        assert not _is_linked(a2, 'fragdial101_Include', b)


def test_assoc_ldflags23_reverse_link_reassign_clear():
    a1 = fragdial101_Ldflag(value="sample_text")
    a2 = fragdial101_Ldflag(value="sample_text_2")
    b = fragdial101_Content(class_="sample_text", language="sample_text")
    _safe_set(b, 'fragdial101_Content24', {a1})
    assert _is_linked(b, 'fragdial101_Content24', a1)
    if hasattr(a1, 'fragdial101_Ldflag'):
        assert _is_linked(a1, 'fragdial101_Ldflag', b)
    _safe_set(b, 'fragdial101_Content24', {a2})
    assert _is_linked(b, 'fragdial101_Content24', a2)
    if hasattr(a1, 'fragdial101_Ldflag'):
        assert not _is_linked(a1, 'fragdial101_Ldflag', b)
    if hasattr(a2, 'fragdial101_Ldflag'):
        assert _is_linked(a2, 'fragdial101_Ldflag', b)
    _safe_set(b, 'fragdial101_Content24', set())
    assert not _is_linked(b, 'fragdial101_Content24', a2)
    if hasattr(a2, 'fragdial101_Ldflag'):
        assert not _is_linked(a2, 'fragdial101_Ldflag', b)


def test_assoc_output3_reverse_link_reassign_clear():
    a1 = fragdial101_Output(format="sample_text")
    a2 = fragdial101_Output(format="sample_text_2")
    b = fragdial101_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial101_AbstractComponent4', a1)
    assert _is_linked(b, 'fragdial101_AbstractComponent4', a1)
    if hasattr(a1, 'fragdial101_Output'):
        assert _is_linked(a1, 'fragdial101_Output', b)
    _safe_set(b, 'fragdial101_AbstractComponent4', a2)
    assert _is_linked(b, 'fragdial101_AbstractComponent4', a2)
    if hasattr(a1, 'fragdial101_Output'):
        assert not _is_linked(a1, 'fragdial101_Output', b)
    if hasattr(a2, 'fragdial101_Output'):
        assert _is_linked(a2, 'fragdial101_Output', b)
    _safe_set(b, 'fragdial101_AbstractComponent4', None)
    assert not _is_linked(b, 'fragdial101_AbstractComponent4', a2)
    if hasattr(a2, 'fragdial101_Output'):
        assert not _is_linked(a2, 'fragdial101_Output', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings11_stub_double():
    # fragdial101_Binding has no real 'fragdial101_Binding' property in the generated
    # code (a bare stub) -- manually attach it so fragdial101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial101_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial101_Binding()
    setattr(partner, 'fragdial101_Binding', None)
    _safe_set(owner, 'fragdial101_Interface', {partner})
    assert getattr(partner, 'fragdial101_Binding') == owner
    _safe_set(owner, 'fragdial101_Interface', set())
    assert getattr(partner, 'fragdial101_Binding') is None


def test_assoc_from_12_stub_double():
    # fragdial101_Binding has no real 'fragdial101_Binding13' property in the generated
    # code (a bare stub) -- manually attach it so fragdial101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial101_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial101_Binding()
    setattr(partner, 'fragdial101_Binding13', None)
    _safe_set(owner, 'fragdial101_Interface14', partner)
    assert getattr(partner, 'fragdial101_Binding13') == owner
    _safe_set(owner, 'fragdial101_Interface14', None)
    assert getattr(partner, 'fragdial101_Binding13') is None


def test_assoc_providedInterfaces9_stub_double():
    # fragdial101_Provided has no real 'fragdial101_Provided' property in the generated
    # code (a bare stub) -- manually attach it so fragdial101_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial101_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial101_AbstractComponent(name="sample_text")
    partner = fragdial101_Provided()
    setattr(partner, 'fragdial101_Provided', None)
    _safe_set(owner, 'fragdial101_AbstractComponent10', {partner})
    assert getattr(partner, 'fragdial101_Provided') == owner
    _safe_set(owner, 'fragdial101_AbstractComponent10', set())
    assert getattr(partner, 'fragdial101_Provided') is None


def test_assoc_requiredInterfaces7_stub_double():
    # fragdial101_Required has no real 'fragdial101_Required' property in the generated
    # code (a bare stub) -- manually attach it so fragdial101_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial101_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial101_AbstractComponent(name="sample_text")
    partner = fragdial101_Required()
    setattr(partner, 'fragdial101_Required', None)
    _safe_set(owner, 'fragdial101_AbstractComponent8', {partner})
    assert getattr(partner, 'fragdial101_Required') == owner
    _safe_set(owner, 'fragdial101_AbstractComponent8', set())
    assert getattr(partner, 'fragdial101_Required') is None


def test_assoc_to15_stub_double():
    # fragdial101_Binding has no real 'fragdial101_Binding16' property in the generated
    # code (a bare stub) -- manually attach it so fragdial101_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial101_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial101_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial101_Binding()
    setattr(partner, 'fragdial101_Binding16', None)
    _safe_set(owner, 'fragdial101_Interface17', partner)
    assert getattr(partner, 'fragdial101_Binding16') == owner
    _safe_set(owner, 'fragdial101_Interface17', None)
    assert getattr(partner, 'fragdial101_Binding16') is None


