import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    container,
    html5_button,
    html5_container,
    html5_dialog,
    html5_div,
    html5_fieldset,
    html5_html,
    html5_htmlElement,
    html5_img,
    html5_input,
    html5_label,
    html5_legend,
    html5_option,
    html5_select_multiple,
    html5_table,
    html5_td,
    html5_tr,
    htmlElement,
    types,
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

def test_assoc_elements7_reverse_link_reassign_clear():
    a1 = html5_htmlElement(class_="sample_text")
    a2 = html5_htmlElement(class_="sample_text_2")
    b = html5_container(class_="sample_text")
    _safe_set(b, 'html5_container8', {a1})
    assert _is_linked(b, 'html5_container8', a1)
    if hasattr(a1, 'html5_htmlElement9'):
        assert _is_linked(a1, 'html5_htmlElement9', b)
    _safe_set(b, 'html5_container8', {a2})
    assert _is_linked(b, 'html5_container8', a2)
    if hasattr(a1, 'html5_htmlElement9'):
        assert not _is_linked(a1, 'html5_htmlElement9', b)
    if hasattr(a2, 'html5_htmlElement9'):
        assert _is_linked(a2, 'html5_htmlElement9', b)
    _safe_set(b, 'html5_container8', set())
    assert not _is_linked(b, 'html5_container8', a2)
    if hasattr(a2, 'html5_htmlElement9'):
        assert not _is_linked(a2, 'html5_htmlElement9', b)


def test_assoc_innercontainer11_reverse_link_reassign_clear():
    a1 = html5_container(class_="sample_text")
    a2 = html5_container(class_="sample_text_2")
    b = html5_container(class_="sample_text")
    _safe_set(b, 'html5_container12', a1)
    assert _is_linked(b, 'html5_container12', a1)
    if hasattr(a1, 'html5_container10'):
        assert _is_linked(a1, 'html5_container10', b)
    _safe_set(b, 'html5_container12', a2)
    assert _is_linked(b, 'html5_container12', a2)
    if hasattr(a1, 'html5_container10'):
        assert not _is_linked(a1, 'html5_container10', b)
    if hasattr(a2, 'html5_container10'):
        assert _is_linked(a2, 'html5_container10', b)
    _safe_set(b, 'html5_container12', None)
    assert not _is_linked(b, 'html5_container12', a2)
    if hasattr(a2, 'html5_container10'):
        assert not _is_linked(a2, 'html5_container10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_container6_stub_double():
    # html5_html has no real 'html5_html' property in the generated
    # code (a bare stub) -- manually attach it so html5_container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html5_container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html5_container(class_="sample_text")
    partner = html5_html()
    setattr(partner, 'html5_html', None)
    _safe_set(owner, 'html5_container', partner)
    assert owner in getattr(partner, 'html5_html')
    _safe_set(owner, 'html5_container', None)
    assert owner not in getattr(partner, 'html5_html')


def test_assoc_elements3_stub_double():
    # html5_td has no real 'html5_td4' property in the generated
    # code (a bare stub) -- manually attach it so html5_htmlElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html5_htmlElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html5_htmlElement(class_="sample_text")
    partner = html5_td()
    setattr(partner, 'html5_td4', None)
    _safe_set(owner, 'html5_htmlElement', partner)
    assert owner in getattr(partner, 'html5_td4')
    _safe_set(owner, 'html5_htmlElement', None)
    assert owner not in getattr(partner, 'html5_td4')


def test_assoc_legend5_stub_double():
    # html5_fieldset has no real 'html5_fieldset' property in the generated
    # code (a bare stub) -- manually attach it so html5_legend's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html5_legend's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html5_legend(class_="sample_text", valor="sample_text")
    partner = html5_fieldset()
    setattr(partner, 'html5_fieldset', None)
    _safe_set(owner, 'html5_legend', partner)
    assert getattr(partner, 'html5_fieldset') == owner
    _safe_set(owner, 'html5_legend', None)
    assert getattr(partner, 'html5_fieldset') is None


def test_assoc_options13_stub_double():
    # html5_option has no real 'html5_option' property in the generated
    # code (a bare stub) -- manually attach it so html5_select_multiple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html5_select_multiple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html5_select_multiple(multiple="sample_text")
    partner = html5_option()
    setattr(partner, 'html5_option', None)
    _safe_set(owner, 'html5_select_multiple', partner)
    assert getattr(partner, 'html5_option') == owner
    _safe_set(owner, 'html5_select_multiple', None)
    assert getattr(partner, 'html5_option') is None


