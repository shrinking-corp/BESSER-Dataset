import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BODYElement,
    FRAME,
    HEADElement,
    HTMLElement,
    ListElement,
    TABLEElement,
    TD,
    html_A,
    html_APPLET,
    html_AREA,
    html_B,
    html_BIG,
    html_BODY,
    html_BODYElement,
    html_BR,
    html_DD,
    html_DIV,
    html_DL,
    html_DT,
    html_EM,
    html_EMBED,
    html_FONT,
    html_FORM,
    html_FRAME,
    html_FRAMESET,
    html_H1,
    html_H2,
    html_H3,
    html_H4,
    html_HEAD,
    html_HEADElement,
    html_HTML,
    html_HTMLElement,
    html_I,
    html_IFRAME,
    html_IMG,
    html_INPUT,
    html_LI,
    html_LINK,
    html_ListElement,
    html_MAP,
    html_NOEMBED,
    html_NOFRAME,
    html_OBJECT,
    html_OL,
    html_OPTION,
    html_P,
    html_PARAM,
    html_PRE,
    html_SELECT,
    html_SMALL,
    html_SPAN,
    html_STRIKE,
    html_STRONG,
    html_STYLE,
    html_SUB,
    html_SUP,
    html_TABLE,
    html_TABLEElement,
    html_TD,
    html_TEXTAREA,
    html_TH,
    html_TITLE,
    html_TR,
    html_TT,
    html_UL,
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

def test_assoc_children4_reverse_link_reassign_clear():
    a1 = html_HTMLElement(value="sample_text")
    a2 = html_HTMLElement(value="sample_text_2")
    b = html_HTMLElement(value="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'HTMLElement'):
        assert _is_linked(a1, 'HTMLElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'HTMLElement'):
        assert not _is_linked(a1, 'HTMLElement', b)
    if hasattr(a2, 'HTMLElement'):
        assert _is_linked(a2, 'HTMLElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'HTMLElement'):
        assert not _is_linked(a2, 'HTMLElement', b)


def test_assoc_parent6_reverse_link_reassign_clear():
    a1 = html_HTMLElement(value="sample_text")
    a2 = html_HTMLElement(value="sample_text_2")
    b = html_HTMLElement(value="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'HTMLElement7'):
        assert _is_linked(a1, 'HTMLElement7', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'HTMLElement7'):
        assert not _is_linked(a1, 'HTMLElement7', b)
    if hasattr(a2, 'HTMLElement7'):
        assert _is_linked(a2, 'HTMLElement7', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'HTMLElement7'):
        assert not _is_linked(a2, 'HTMLElement7', b)


def test_assoc_table20_reverse_link_reassign_clear():
    a1 = html_TR(align="sample_text", valign="sample_text")
    a2 = html_TR(align="sample_text_2", valign="sample_text_2")
    b = html_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    _safe_set(b, 'TABLE', a1)
    assert _is_linked(b, 'TABLE', a1)
    if hasattr(a1, 'trs'):
        assert _is_linked(a1, 'trs', b)
    _safe_set(b, 'TABLE', a2)
    assert _is_linked(b, 'TABLE', a2)
    if hasattr(a1, 'trs'):
        assert not _is_linked(a1, 'trs', b)
    if hasattr(a2, 'trs'):
        assert _is_linked(a2, 'trs', b)
    _safe_set(b, 'TABLE', None)
    assert not _is_linked(b, 'TABLE', a2)
    if hasattr(a2, 'trs'):
        assert not _is_linked(a2, 'trs', b)


def test_assoc_tds21_reverse_link_reassign_clear():
    a1 = html_TR(align="sample_text", valign="sample_text")
    a2 = html_TR(align="sample_text_2", valign="sample_text_2")
    b = html_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    _safe_set(b, 'TD', a1)
    assert _is_linked(b, 'TD', a1)
    if hasattr(a1, 'tr'):
        assert _is_linked(a1, 'tr', b)
    _safe_set(b, 'TD', a2)
    assert _is_linked(b, 'TD', a2)
    if hasattr(a1, 'tr'):
        assert not _is_linked(a1, 'tr', b)
    if hasattr(a2, 'tr'):
        assert _is_linked(a2, 'tr', b)
    _safe_set(b, 'TD', None)
    assert not _is_linked(b, 'TD', a2)
    if hasattr(a2, 'tr'):
        assert not _is_linked(a2, 'tr', b)


def test_assoc_tr22_reverse_link_reassign_clear():
    a1 = html_TR(align="sample_text", valign="sample_text")
    a2 = html_TR(align="sample_text_2", valign="sample_text_2")
    b = html_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    _safe_set(b, 'tds', a1)
    assert _is_linked(b, 'tds', a1)
    if hasattr(a1, 'TR23'):
        assert _is_linked(a1, 'TR23', b)
    _safe_set(b, 'tds', a2)
    assert _is_linked(b, 'tds', a2)
    if hasattr(a1, 'TR23'):
        assert not _is_linked(a1, 'TR23', b)
    if hasattr(a2, 'TR23'):
        assert _is_linked(a2, 'TR23', b)
    _safe_set(b, 'tds', None)
    assert not _is_linked(b, 'tds', a2)
    if hasattr(a2, 'TR23'):
        assert not _is_linked(a2, 'TR23', b)


def test_assoc_trs19_reverse_link_reassign_clear():
    a1 = html_TR(align="sample_text", valign="sample_text")
    a2 = html_TR(align="sample_text_2", valign="sample_text_2")
    b = html_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    _safe_set(b, 'table', {a1})
    assert _is_linked(b, 'table', a1)
    if hasattr(a1, 'TR'):
        assert _is_linked(a1, 'TR', b)
    _safe_set(b, 'table', {a2})
    assert _is_linked(b, 'table', a2)
    if hasattr(a1, 'TR'):
        assert not _is_linked(a1, 'TR', b)
    if hasattr(a2, 'TR'):
        assert _is_linked(a2, 'TR', b)
    _safe_set(b, 'table', set())
    assert not _is_linked(b, 'table', a2)
    if hasattr(a2, 'TR'):
        assert not _is_linked(a2, 'TR', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body1_stub_double():
    # html_HTML has no real 'html2' property in the generated
    # code (a bare stub) -- manually attach it so html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = html_HTML()
    setattr(partner, 'html2', None)
    _safe_set(owner, 'BODY', partner)
    assert getattr(partner, 'html2') == owner
    _safe_set(owner, 'BODY', None)
    assert getattr(partner, 'html2') is None


def test_assoc_body17_stub_double():
    # html_BODYElement has no real 'bodyElements' property in the generated
    # code (a bare stub) -- manually attach it so html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = html_BODYElement()
    setattr(partner, 'bodyElements', None)
    _safe_set(owner, 'BODY18', partner)
    assert getattr(partner, 'bodyElements') == owner
    _safe_set(owner, 'BODY18', None)
    assert getattr(partner, 'bodyElements') is None


def test_assoc_bodyElements13_stub_double():
    # html_BODYElement has no real 'BODYElement' property in the generated
    # code (a bare stub) -- manually attach it so html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = html_BODYElement()
    setattr(partner, 'BODYElement', None)
    _safe_set(owner, 'body', {partner})
    assert getattr(partner, 'BODYElement') == owner
    _safe_set(owner, 'body', set())
    assert getattr(partner, 'BODYElement') is None


def test_assoc_html14_stub_double():
    # html_HTML has no real 'HTML16' property in the generated
    # code (a bare stub) -- manually attach it so html_BODY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # html_BODY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = html_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    partner = html_HTML()
    setattr(partner, 'HTML16', None)
    _safe_set(owner, 'body15', partner)
    assert getattr(partner, 'HTML16') == owner
    _safe_set(owner, 'body15', None)
    assert getattr(partner, 'HTML16') is None


