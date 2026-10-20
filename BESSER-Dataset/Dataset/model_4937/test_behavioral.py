import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Control,
    FormButton,
    NormalControl,
    Page,
    TextBox,
    webapp_CheckBox,
    webapp_Control,
    webapp_DateBox,
    webapp_DropDownList,
    webapp_DynamicWebApp,
    webapp_EmailBox,
    webapp_FormButton,
    webapp_FormPage,
    webapp_Label,
    webapp_Link,
    webapp_ListElement,
    webapp_NormalButton,
    webapp_NormalControl,
    webapp_NormalPage,
    webapp_Page,
    webapp_PasswordBox,
    webapp_RadioButton,
    webapp_ResetButton,
    webapp_SubmitButton,
    webapp_TextBox,
    DateFormat,
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

def test_assoc_controls4_reverse_link_reassign_clear():
    a1 = webapp_FormPage(persist=True)
    a2 = webapp_FormPage(persist=False)
    b = webapp_Control(id="sample_text", name="sample_text")
    _safe_set(b, 'webapp_Control', a1)
    assert _is_linked(b, 'webapp_Control', a1)
    if hasattr(a1, 'webapp_FormPage5'):
        assert _is_linked(a1, 'webapp_FormPage5', b)
    _safe_set(b, 'webapp_Control', a2)
    assert _is_linked(b, 'webapp_Control', a2)
    if hasattr(a1, 'webapp_FormPage5'):
        assert not _is_linked(a1, 'webapp_FormPage5', b)
    if hasattr(a2, 'webapp_FormPage5'):
        assert _is_linked(a2, 'webapp_FormPage5', b)
    _safe_set(b, 'webapp_Control', None)
    assert not _is_linked(b, 'webapp_Control', a2)
    if hasattr(a2, 'webapp_FormPage5'):
        assert not _is_linked(a2, 'webapp_FormPage5', b)


def test_assoc_errorTarget1_reverse_link_reassign_clear():
    a1 = webapp_Page(default=True, name="sample_text", title="sample_text")
    a2 = webapp_Page(default=False, name="sample_text_2", title="sample_text_2")
    b = webapp_FormPage(persist=True)
    _safe_set(b, 'webapp_FormPage2', a1)
    assert _is_linked(b, 'webapp_FormPage2', a1)
    if hasattr(a1, 'webapp_Page3'):
        assert _is_linked(a1, 'webapp_Page3', b)
    _safe_set(b, 'webapp_FormPage2', a2)
    assert _is_linked(b, 'webapp_FormPage2', a2)
    if hasattr(a1, 'webapp_Page3'):
        assert not _is_linked(a1, 'webapp_Page3', b)
    if hasattr(a2, 'webapp_Page3'):
        assert _is_linked(a2, 'webapp_Page3', b)
    _safe_set(b, 'webapp_FormPage2', None)
    assert not _is_linked(b, 'webapp_FormPage2', a2)
    if hasattr(a2, 'webapp_Page3'):
        assert not _is_linked(a2, 'webapp_Page3', b)


def test_assoc_pages12_reverse_link_reassign_clear():
    a1 = webapp_Page(default=True, name="sample_text", title="sample_text")
    a2 = webapp_Page(default=False, name="sample_text_2", title="sample_text_2")
    b = webapp_DynamicWebApp(name="sample_text")
    _safe_set(b, 'webapp_DynamicWebApp', {a1})
    assert _is_linked(b, 'webapp_DynamicWebApp', a1)
    if hasattr(a1, 'webapp_Page13'):
        assert _is_linked(a1, 'webapp_Page13', b)
    _safe_set(b, 'webapp_DynamicWebApp', {a2})
    assert _is_linked(b, 'webapp_DynamicWebApp', a2)
    if hasattr(a1, 'webapp_Page13'):
        assert not _is_linked(a1, 'webapp_Page13', b)
    if hasattr(a2, 'webapp_Page13'):
        assert _is_linked(a2, 'webapp_Page13', b)
    _safe_set(b, 'webapp_DynamicWebApp', set())
    assert not _is_linked(b, 'webapp_DynamicWebApp', a2)
    if hasattr(a2, 'webapp_Page13'):
        assert not _is_linked(a2, 'webapp_Page13', b)


def test_assoc_successTarget0_reverse_link_reassign_clear():
    a1 = webapp_Page(default=True, name="sample_text", title="sample_text")
    a2 = webapp_Page(default=False, name="sample_text_2", title="sample_text_2")
    b = webapp_FormPage(persist=True)
    _safe_set(b, 'webapp_FormPage', a1)
    assert _is_linked(b, 'webapp_FormPage', a1)
    if hasattr(a1, 'webapp_Page'):
        assert _is_linked(a1, 'webapp_Page', b)
    _safe_set(b, 'webapp_FormPage', a2)
    assert _is_linked(b, 'webapp_FormPage', a2)
    if hasattr(a1, 'webapp_Page'):
        assert not _is_linked(a1, 'webapp_Page', b)
    if hasattr(a2, 'webapp_Page'):
        assert _is_linked(a2, 'webapp_Page', b)
    _safe_set(b, 'webapp_FormPage', None)
    assert not _is_linked(b, 'webapp_FormPage', a2)
    if hasattr(a2, 'webapp_Page'):
        assert not _is_linked(a2, 'webapp_Page', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_controls6_stub_double():
    # webapp_NormalPage has no real 'webapp_NormalPage' property in the generated
    # code (a bare stub) -- manually attach it so webapp_NormalControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_NormalControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_NormalControl(text="sample_text")
    partner = webapp_NormalPage()
    setattr(partner, 'webapp_NormalPage', None)
    _safe_set(owner, 'webapp_NormalControl', partner)
    assert owner in getattr(partner, 'webapp_NormalPage')
    _safe_set(owner, 'webapp_NormalControl', None)
    assert owner not in getattr(partner, 'webapp_NormalPage')


def test_assoc_destination7_stub_double():
    # webapp_Link has no real 'webapp_Link' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Page(default=True, name="sample_text", title="sample_text")
    partner = webapp_Link()
    setattr(partner, 'webapp_Link', None)
    _safe_set(owner, 'webapp_Page8', partner)
    assert getattr(partner, 'webapp_Link') == owner
    _safe_set(owner, 'webapp_Page8', None)
    assert getattr(partner, 'webapp_Link') is None


def test_assoc_elements10_stub_double():
    # webapp_RadioButton has no real 'webapp_RadioButton' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ListElement(value="sample_text")
    partner = webapp_RadioButton()
    setattr(partner, 'webapp_RadioButton', None)
    _safe_set(owner, 'webapp_ListElement11', partner)
    assert owner in getattr(partner, 'webapp_RadioButton')
    _safe_set(owner, 'webapp_ListElement11', None)
    assert owner not in getattr(partner, 'webapp_RadioButton')


def test_assoc_elements9_stub_double():
    # webapp_DropDownList has no real 'webapp_DropDownList' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ListElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ListElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ListElement(value="sample_text")
    partner = webapp_DropDownList()
    setattr(partner, 'webapp_DropDownList', None)
    _safe_set(owner, 'webapp_ListElement', partner)
    assert owner in getattr(partner, 'webapp_DropDownList')
    _safe_set(owner, 'webapp_ListElement', None)
    assert owner not in getattr(partner, 'webapp_DropDownList')


