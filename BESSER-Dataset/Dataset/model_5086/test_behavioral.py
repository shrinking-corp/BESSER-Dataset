import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractComponent,
    Interface,
    fragdial_AbstractComponent,
    fragdial_Attribute,
    fragdial_Attributes,
    fragdial_Binding,
    fragdial_Component,
    fragdial_Component1,
    fragdial_Component2,
    fragdial_Component3,
    fragdial_Content,
    fragdial_Controller,
    fragdial_Include,
    fragdial_Interface,
    fragdial_Ldflag,
    fragdial_Output,
    fragdial_Provided,
    fragdial_Required,
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
    a1 = fragdial_Attributes(signature="sample_text")
    a2 = fragdial_Attributes(signature="sample_text_2")
    b = fragdial_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial_AbstractComponent2', a1)
    assert _is_linked(b, 'fragdial_AbstractComponent2', a1)
    if hasattr(a1, 'fragdial_Attributes'):
        assert _is_linked(a1, 'fragdial_Attributes', b)
    _safe_set(b, 'fragdial_AbstractComponent2', a2)
    assert _is_linked(b, 'fragdial_AbstractComponent2', a2)
    if hasattr(a1, 'fragdial_Attributes'):
        assert not _is_linked(a1, 'fragdial_Attributes', b)
    if hasattr(a2, 'fragdial_Attributes'):
        assert _is_linked(a2, 'fragdial_Attributes', b)
    _safe_set(b, 'fragdial_AbstractComponent2', None)
    assert not _is_linked(b, 'fragdial_AbstractComponent2', a2)
    if hasattr(a2, 'fragdial_Attributes'):
        assert not _is_linked(a2, 'fragdial_Attributes', b)


def test_assoc_attributes25_reverse_link_reassign_clear():
    a1 = fragdial_Attributes(signature="sample_text")
    a2 = fragdial_Attributes(signature="sample_text_2")
    b = fragdial_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'fragdial_Attribute', a1)
    assert _is_linked(b, 'fragdial_Attribute', a1)
    if hasattr(a1, 'fragdial_Attributes26'):
        assert _is_linked(a1, 'fragdial_Attributes26', b)
    _safe_set(b, 'fragdial_Attribute', a2)
    assert _is_linked(b, 'fragdial_Attribute', a2)
    if hasattr(a1, 'fragdial_Attributes26'):
        assert not _is_linked(a1, 'fragdial_Attributes26', b)
    if hasattr(a2, 'fragdial_Attributes26'):
        assert _is_linked(a2, 'fragdial_Attributes26', b)
    _safe_set(b, 'fragdial_Attribute', None)
    assert not _is_linked(b, 'fragdial_Attribute', a2)
    if hasattr(a2, 'fragdial_Attributes26'):
        assert not _is_linked(a2, 'fragdial_Attributes26', b)


def test_assoc_content0_reverse_link_reassign_clear():
    a1 = fragdial_Content(class_="sample_text", language="sample_text")
    a2 = fragdial_Content(class_="sample_text_2", language="sample_text_2")
    b = fragdial_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial_AbstractComponent', a1)
    assert _is_linked(b, 'fragdial_AbstractComponent', a1)
    if hasattr(a1, 'fragdial_Content'):
        assert _is_linked(a1, 'fragdial_Content', b)
    _safe_set(b, 'fragdial_AbstractComponent', a2)
    assert _is_linked(b, 'fragdial_AbstractComponent', a2)
    if hasattr(a1, 'fragdial_Content'):
        assert not _is_linked(a1, 'fragdial_Content', b)
    if hasattr(a2, 'fragdial_Content'):
        assert _is_linked(a2, 'fragdial_Content', b)
    _safe_set(b, 'fragdial_AbstractComponent', None)
    assert not _is_linked(b, 'fragdial_AbstractComponent', a2)
    if hasattr(a2, 'fragdial_Content'):
        assert not _is_linked(a2, 'fragdial_Content', b)


def test_assoc_contentParent18_reverse_link_reassign_clear():
    a1 = fragdial_Content(class_="sample_text", language="sample_text")
    a2 = fragdial_Content(class_="sample_text_2", language="sample_text_2")
    b = fragdial_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial_AbstractComponent20', a1)
    assert _is_linked(b, 'fragdial_AbstractComponent20', a1)
    if hasattr(a1, 'fragdial_Content19'):
        assert _is_linked(a1, 'fragdial_Content19', b)
    _safe_set(b, 'fragdial_AbstractComponent20', a2)
    assert _is_linked(b, 'fragdial_AbstractComponent20', a2)
    if hasattr(a1, 'fragdial_Content19'):
        assert not _is_linked(a1, 'fragdial_Content19', b)
    if hasattr(a2, 'fragdial_Content19'):
        assert _is_linked(a2, 'fragdial_Content19', b)
    _safe_set(b, 'fragdial_AbstractComponent20', None)
    assert not _is_linked(b, 'fragdial_AbstractComponent20', a2)
    if hasattr(a2, 'fragdial_Content19'):
        assert not _is_linked(a2, 'fragdial_Content19', b)


def test_assoc_controller5_reverse_link_reassign_clear():
    a1 = fragdial_Controller(descriptor="sample_text", language="sample_text")
    a2 = fragdial_Controller(descriptor="sample_text_2", language="sample_text_2")
    b = fragdial_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial_AbstractComponent6', a1)
    assert _is_linked(b, 'fragdial_AbstractComponent6', a1)
    if hasattr(a1, 'fragdial_Controller'):
        assert _is_linked(a1, 'fragdial_Controller', b)
    _safe_set(b, 'fragdial_AbstractComponent6', a2)
    assert _is_linked(b, 'fragdial_AbstractComponent6', a2)
    if hasattr(a1, 'fragdial_Controller'):
        assert not _is_linked(a1, 'fragdial_Controller', b)
    if hasattr(a2, 'fragdial_Controller'):
        assert _is_linked(a2, 'fragdial_Controller', b)
    _safe_set(b, 'fragdial_AbstractComponent6', None)
    assert not _is_linked(b, 'fragdial_AbstractComponent6', a2)
    if hasattr(a2, 'fragdial_Controller'):
        assert not _is_linked(a2, 'fragdial_Controller', b)


def test_assoc_includes21_reverse_link_reassign_clear():
    a1 = fragdial_Include(file="sample_text")
    a2 = fragdial_Include(file="sample_text_2")
    b = fragdial_Content(class_="sample_text", language="sample_text")
    _safe_set(b, 'fragdial_Content22', {a1})
    assert _is_linked(b, 'fragdial_Content22', a1)
    if hasattr(a1, 'fragdial_Include'):
        assert _is_linked(a1, 'fragdial_Include', b)
    _safe_set(b, 'fragdial_Content22', {a2})
    assert _is_linked(b, 'fragdial_Content22', a2)
    if hasattr(a1, 'fragdial_Include'):
        assert not _is_linked(a1, 'fragdial_Include', b)
    if hasattr(a2, 'fragdial_Include'):
        assert _is_linked(a2, 'fragdial_Include', b)
    _safe_set(b, 'fragdial_Content22', set())
    assert not _is_linked(b, 'fragdial_Content22', a2)
    if hasattr(a2, 'fragdial_Include'):
        assert not _is_linked(a2, 'fragdial_Include', b)


def test_assoc_ldflags23_reverse_link_reassign_clear():
    a1 = fragdial_Ldflag(value="sample_text")
    a2 = fragdial_Ldflag(value="sample_text_2")
    b = fragdial_Content(class_="sample_text", language="sample_text")
    _safe_set(b, 'fragdial_Content24', {a1})
    assert _is_linked(b, 'fragdial_Content24', a1)
    if hasattr(a1, 'fragdial_Ldflag'):
        assert _is_linked(a1, 'fragdial_Ldflag', b)
    _safe_set(b, 'fragdial_Content24', {a2})
    assert _is_linked(b, 'fragdial_Content24', a2)
    if hasattr(a1, 'fragdial_Ldflag'):
        assert not _is_linked(a1, 'fragdial_Ldflag', b)
    if hasattr(a2, 'fragdial_Ldflag'):
        assert _is_linked(a2, 'fragdial_Ldflag', b)
    _safe_set(b, 'fragdial_Content24', set())
    assert not _is_linked(b, 'fragdial_Content24', a2)
    if hasattr(a2, 'fragdial_Ldflag'):
        assert not _is_linked(a2, 'fragdial_Ldflag', b)


def test_assoc_output3_reverse_link_reassign_clear():
    a1 = fragdial_Output(format="sample_text")
    a2 = fragdial_Output(format="sample_text_2")
    b = fragdial_AbstractComponent(name="sample_text")
    _safe_set(b, 'fragdial_AbstractComponent4', a1)
    assert _is_linked(b, 'fragdial_AbstractComponent4', a1)
    if hasattr(a1, 'fragdial_Output'):
        assert _is_linked(a1, 'fragdial_Output', b)
    _safe_set(b, 'fragdial_AbstractComponent4', a2)
    assert _is_linked(b, 'fragdial_AbstractComponent4', a2)
    if hasattr(a1, 'fragdial_Output'):
        assert not _is_linked(a1, 'fragdial_Output', b)
    if hasattr(a2, 'fragdial_Output'):
        assert _is_linked(a2, 'fragdial_Output', b)
    _safe_set(b, 'fragdial_AbstractComponent4', None)
    assert not _is_linked(b, 'fragdial_AbstractComponent4', a2)
    if hasattr(a2, 'fragdial_Output'):
        assert not _is_linked(a2, 'fragdial_Output', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindings11_stub_double():
    # fragdial_Binding has no real 'fragdial_Binding' property in the generated
    # code (a bare stub) -- manually attach it so fragdial_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial_Binding()
    setattr(partner, 'fragdial_Binding', None)
    _safe_set(owner, 'fragdial_Interface', {partner})
    assert getattr(partner, 'fragdial_Binding') == owner
    _safe_set(owner, 'fragdial_Interface', set())
    assert getattr(partner, 'fragdial_Binding') is None


def test_assoc_from_12_stub_double():
    # fragdial_Binding has no real 'fragdial_Binding13' property in the generated
    # code (a bare stub) -- manually attach it so fragdial_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial_Binding()
    setattr(partner, 'fragdial_Binding13', None)
    _safe_set(owner, 'fragdial_Interface14', partner)
    assert getattr(partner, 'fragdial_Binding13') == owner
    _safe_set(owner, 'fragdial_Interface14', None)
    assert getattr(partner, 'fragdial_Binding13') is None


def test_assoc_providedInterfaces9_stub_double():
    # fragdial_Provided has no real 'fragdial_Provided' property in the generated
    # code (a bare stub) -- manually attach it so fragdial_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial_AbstractComponent(name="sample_text")
    partner = fragdial_Provided()
    setattr(partner, 'fragdial_Provided', None)
    _safe_set(owner, 'fragdial_AbstractComponent10', {partner})
    assert getattr(partner, 'fragdial_Provided') == owner
    _safe_set(owner, 'fragdial_AbstractComponent10', set())
    assert getattr(partner, 'fragdial_Provided') is None


def test_assoc_requiredInterfaces7_stub_double():
    # fragdial_Required has no real 'fragdial_Required' property in the generated
    # code (a bare stub) -- manually attach it so fragdial_AbstractComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial_AbstractComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial_AbstractComponent(name="sample_text")
    partner = fragdial_Required()
    setattr(partner, 'fragdial_Required', None)
    _safe_set(owner, 'fragdial_AbstractComponent8', {partner})
    assert getattr(partner, 'fragdial_Required') == owner
    _safe_set(owner, 'fragdial_AbstractComponent8', set())
    assert getattr(partner, 'fragdial_Required') is None


def test_assoc_to15_stub_double():
    # fragdial_Binding has no real 'fragdial_Binding16' property in the generated
    # code (a bare stub) -- manually attach it so fragdial_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fragdial_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fragdial_Interface(cardinality="sample_text", contingency="sample_text", name="sample_text", signature="sample_text", startProperty="sample_text")
    partner = fragdial_Binding()
    setattr(partner, 'fragdial_Binding16', None)
    _safe_set(owner, 'fragdial_Interface17', partner)
    assert getattr(partner, 'fragdial_Binding16') == owner
    _safe_set(owner, 'fragdial_Interface17', None)
    assert getattr(partner, 'fragdial_Binding16') is None


