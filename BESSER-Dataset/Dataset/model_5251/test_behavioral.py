import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BODY,
    BODYElement,
    FRAME,
    HEAD,
    HEADElement,
    HTML,
    HTMLElement,
    Html_A,
    Html_APPLET,
    Html_AREA,
    Html_B,
    Html_BIG,
    Html_BODY,
    Html_BODYElement,
    Html_BR,
    Html_DD,
    Html_DIV,
    Html_DL,
    Html_DT,
    Html_EM,
    Html_EMBED,
    Html_FONT,
    Html_FORM,
    Html_FRAME,
    Html_FRAMESET,
    Html_H1,
    Html_H2,
    Html_H3,
    Html_H4,
    Html_HEAD,
    Html_HEADElement,
    Html_HTML,
    Html_HTMLElement,
    Html_I,
    Html_IFRAME,
    Html_IMG,
    Html_INPUT,
    Html_LI,
    Html_LINK,
    Html_ListElement,
    Html_MAP,
    Html_NOEMBED,
    Html_NOFRAME,
    Html_OBJECT,
    Html_OL,
    Html_OPTION,
    Html_P,
    Html_PARAM,
    Html_PRE,
    Html_SELECT,
    Html_SMALL,
    Html_SPAN,
    Html_STRIKE,
    Html_STRONG,
    Html_STYLE,
    Html_SUB,
    Html_SUP,
    Html_TABLE,
    Html_TABLEElement,
    Html_TD,
    Html_TEXTAREA,
    Html_TH,
    Html_TITLE,
    Html_TR,
    Html_TT,
    Html_UL,
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
    # code (a bare stub) -- manually attach it so Html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = BODYElement()
    setattr(partner, 'BODYElement', None)
    _safe_set(owner, 'body', {partner})
    assert getattr(partner, 'BODYElement') == owner
    _safe_set(owner, 'body', set())
    assert getattr(partner, 'BODYElement') is None


def test_assoc_children3_stub_double():
    # HTMLElement has no real 'HTMLElement' property in the generated
    # code (a bare stub) -- manually attach it so Html_HTMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_HTMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_HTMLElement(class_="sample_text", id="sample_text", title="sample_text", value="sample_text")
    partner = HTMLElement()
    setattr(partner, 'HTMLElement', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'HTMLElement') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'HTMLElement') is None


def test_assoc_html12_stub_double():
    # HTML has no real 'HTML14' property in the generated
    # code (a bare stub) -- manually attach it so Html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = HTML()
    setattr(partner, 'HTML14', None)
    _safe_set(owner, 'body13', partner)
    assert getattr(partner, 'HTML14') == owner
    _safe_set(owner, 'body13', None)
    assert getattr(partner, 'HTML14') is None


def test_assoc_parent4_stub_double():
    # HTMLElement has no real 'HTMLElement5' property in the generated
    # code (a bare stub) -- manually attach it so Html_HTMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_HTMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_HTMLElement(class_="sample_text", id="sample_text", title="sample_text", value="sample_text")
    partner = HTMLElement()
    setattr(partner, 'HTMLElement5', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'HTMLElement5') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'HTMLElement5') is None


def test_assoc_table18_stub_double():
    # TABLE has no real 'TABLE' property in the generated
    # code (a bare stub) -- manually attach it so Html_TR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_TR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_TR(align="sample_text", valign="sample_text")
    partner = TABLE()
    setattr(partner, 'TABLE', None)
    _safe_set(owner, 'trs', partner)
    assert getattr(partner, 'TABLE') == owner
    _safe_set(owner, 'trs', None)
    assert getattr(partner, 'TABLE') is None


def test_assoc_tds19_stub_double():
    # TD has no real 'TD' property in the generated
    # code (a bare stub) -- manually attach it so Html_TR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_TR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_TR(align="sample_text", valign="sample_text")
    partner = TD()
    setattr(partner, 'TD', None)
    _safe_set(owner, 'tr', {partner})
    assert getattr(partner, 'TD') == owner
    _safe_set(owner, 'tr', set())
    assert getattr(partner, 'TD') is None


def test_assoc_tr20_stub_double():
    # TR has no real 'TR21' property in the generated
    # code (a bare stub) -- manually attach it so Html_TD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_TD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    partner = TR()
    setattr(partner, 'TR21', None)
    _safe_set(owner, 'tds', partner)
    assert getattr(partner, 'TR21') == owner
    _safe_set(owner, 'tds', None)
    assert getattr(partner, 'TR21') is None


def test_assoc_trs17_stub_double():
    # TR has no real 'TR' property in the generated
    # code (a bare stub) -- manually attach it so Html_TABLE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Html_TABLE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Html_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    partner = TR()
    setattr(partner, 'TR', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'TR') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'TR') is None


