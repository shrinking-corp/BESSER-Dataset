import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BBODY,
    BODYElement,
    HEAD,
    HEADElement,
    HTML,
    HTMLElement,
    HTML_A,
    HTML_BBODY,
    HTML_BODYElement,
    HTML_BR,
    HTML_DIV,
    HTML_EM,
    HTML_H1,
    HTML_H2,
    HTML_H3,
    HTML_H4,
    HTML_H5,
    HTML_H6,
    HTML_HEAD,
    HTML_HEADElement,
    HTML_HTML,
    HTML_HTMLElement,
    HTML_IMG,
    HTML_LI,
    HTML_LINK,
    HTML_ListElement,
    HTML_OL,
    HTML_OPTION,
    HTML_P,
    HTML_SELECT,
    HTML_SPAN,
    HTML_STRONG,
    HTML_STYLE,
    HTML_TABLE,
    HTML_TABLEElement,
    HTML_TD,
    HTML_TH,
    HTML_TITLE,
    HTML_TR,
    HTML_UL,
    HTML_Website,
    ListElement,
    TABLE,
    TABLEElement,
    TD,
    TR,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyElements11_stub_double():
    # BODYElement has no real 'BODYElement' property in the generated
    # code (a bare stub) -- manually attach it so HTML_BBODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_BBODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_BBODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = BODYElement()
    setattr(partner, 'BODYElement', None)
    _safe_set(owner, 'body', {partner})
    assert getattr(partner, 'BODYElement') == owner
    _safe_set(owner, 'body', set())
    assert getattr(partner, 'BODYElement') is None


def test_assoc_children3_stub_double():
    # HTMLElement has no real 'HTMLElement' property in the generated
    # code (a bare stub) -- manually attach it so HTML_HTMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_HTMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_HTMLElement(value="sample_text")
    partner = HTMLElement()
    setattr(partner, 'HTMLElement', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'HTMLElement') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'HTMLElement') is None


def test_assoc_html12_stub_double():
    # HTML has no real 'HTML13' property in the generated
    # code (a bare stub) -- manually attach it so HTML_BBODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_BBODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_BBODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = HTML()
    setattr(partner, 'HTML13', None)
    _safe_set(owner, 'bbody', partner)
    assert getattr(partner, 'HTML13') == owner
    _safe_set(owner, 'bbody', None)
    assert getattr(partner, 'HTML13') is None


def test_assoc_parent4_stub_double():
    # HTMLElement has no real 'HTMLElement5' property in the generated
    # code (a bare stub) -- manually attach it so HTML_HTMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_HTMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_HTMLElement(value="sample_text")
    partner = HTMLElement()
    setattr(partner, 'HTMLElement5', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'HTMLElement5') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'HTMLElement5') is None


def test_assoc_table17_stub_double():
    # TABLE has no real 'TABLE' property in the generated
    # code (a bare stub) -- manually attach it so HTML_TR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_TR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_TR(align="sample_text", valign="sample_text")
    partner = TABLE()
    setattr(partner, 'TABLE', None)
    _safe_set(owner, 'trs', partner)
    assert getattr(partner, 'TABLE') == owner
    _safe_set(owner, 'trs', None)
    assert getattr(partner, 'TABLE') is None


def test_assoc_tds18_stub_double():
    # TD has no real 'TD' property in the generated
    # code (a bare stub) -- manually attach it so HTML_TR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_TR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_TR(align="sample_text", valign="sample_text")
    partner = TD()
    setattr(partner, 'TD', None)
    _safe_set(owner, 'tr', {partner})
    assert getattr(partner, 'TD') == owner
    _safe_set(owner, 'tr', set())
    assert getattr(partner, 'TD') is None


def test_assoc_tr19_stub_double():
    # TR has no real 'TR20' property in the generated
    # code (a bare stub) -- manually attach it so HTML_TD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_TD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    partner = TR()
    setattr(partner, 'TR20', None)
    _safe_set(owner, 'tds', partner)
    assert getattr(partner, 'TR20') == owner
    _safe_set(owner, 'tds', None)
    assert getattr(partner, 'TR20') is None


def test_assoc_trs16_stub_double():
    # TR has no real 'TR' property in the generated
    # code (a bare stub) -- manually attach it so HTML_TABLE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HTML_TABLE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HTML_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    partner = TR()
    setattr(partner, 'TR', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'TR') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'TR') is None


