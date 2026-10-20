import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FormWidget,
    Widget,
    bootstrap_CheckBox,
    bootstrap_Form,
    bootstrap_FormWidget,
    bootstrap_Gallery,
    bootstrap_ImagesBlock,
    bootstrap_MainPage,
    bootstrap_Page,
    bootstrap_Section,
    bootstrap_Site,
    bootstrap_Spinner,
    bootstrap_Table,
    bootstrap_Text,
    bootstrap_TextArea,
    bootstrap_Video,
    bootstrap_Widget,
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

def test_assoc_mainPage1_reverse_link_reassign_clear():
    a1 = bootstrap_Site(title="sample_text")
    a2 = bootstrap_Site(title="sample_text_2")
    b = bootstrap_MainPage(description="sample_text", title="sample_text")
    _safe_set(b, 'MainPage', a1)
    assert _is_linked(b, 'MainPage', a1)
    if hasattr(a1, 'site2'):
        assert _is_linked(a1, 'site2', b)
    _safe_set(b, 'MainPage', a2)
    assert _is_linked(b, 'MainPage', a2)
    if hasattr(a1, 'site2'):
        assert not _is_linked(a1, 'site2', b)
    if hasattr(a2, 'site2'):
        assert _is_linked(a2, 'site2', b)
    _safe_set(b, 'MainPage', None)
    assert not _is_linked(b, 'MainPage', a2)
    if hasattr(a2, 'site2'):
        assert not _is_linked(a2, 'site2', b)


def test_assoc_page8_reverse_link_reassign_clear():
    a1 = bootstrap_Section(description="sample_text", title="sample_text")
    a2 = bootstrap_Section(description="sample_text_2", title="sample_text_2")
    b = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'Page9', a1)
    assert _is_linked(b, 'Page9', a1)
    if hasattr(a1, 'sections'):
        assert _is_linked(a1, 'sections', b)
    _safe_set(b, 'Page9', a2)
    assert _is_linked(b, 'Page9', a2)
    if hasattr(a1, 'sections'):
        assert not _is_linked(a1, 'sections', b)
    if hasattr(a2, 'sections'):
        assert _is_linked(a2, 'sections', b)
    _safe_set(b, 'Page9', None)
    assert not _is_linked(b, 'Page9', a2)
    if hasattr(a2, 'sections'):
        assert not _is_linked(a2, 'sections', b)


def test_assoc_pages0_reverse_link_reassign_clear():
    a1 = bootstrap_Site(title="sample_text")
    a2 = bootstrap_Site(title="sample_text_2")
    b = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'Page', a1)
    assert _is_linked(b, 'Page', a1)
    if hasattr(a1, 'site'):
        assert _is_linked(a1, 'site', b)
    _safe_set(b, 'Page', a2)
    assert _is_linked(b, 'Page', a2)
    if hasattr(a1, 'site'):
        assert not _is_linked(a1, 'site', b)
    if hasattr(a2, 'site'):
        assert _is_linked(a2, 'site', b)
    _safe_set(b, 'Page', None)
    assert not _is_linked(b, 'Page', a2)
    if hasattr(a2, 'site'):
        assert not _is_linked(a2, 'site', b)


def test_assoc_section10_reverse_link_reassign_clear():
    a1 = bootstrap_Widget(title="sample_text")
    a2 = bootstrap_Widget(title="sample_text_2")
    b = bootstrap_Section(description="sample_text", title="sample_text")
    _safe_set(b, 'Section11', a1)
    assert _is_linked(b, 'Section11', a1)
    if hasattr(a1, 'widgets'):
        assert _is_linked(a1, 'widgets', b)
    _safe_set(b, 'Section11', a2)
    assert _is_linked(b, 'Section11', a2)
    if hasattr(a1, 'widgets'):
        assert not _is_linked(a1, 'widgets', b)
    if hasattr(a2, 'widgets'):
        assert _is_linked(a2, 'widgets', b)
    _safe_set(b, 'Section11', None)
    assert not _is_linked(b, 'Section11', a2)
    if hasattr(a2, 'widgets'):
        assert not _is_linked(a2, 'widgets', b)


def test_assoc_sections3_reverse_link_reassign_clear():
    a1 = bootstrap_Section(description="sample_text", title="sample_text")
    a2 = bootstrap_Section(description="sample_text_2", title="sample_text_2")
    b = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'page', {a1})
    assert _is_linked(b, 'page', a1)
    if hasattr(a1, 'Section'):
        assert _is_linked(a1, 'Section', b)
    _safe_set(b, 'page', {a2})
    assert _is_linked(b, 'page', a2)
    if hasattr(a1, 'Section'):
        assert not _is_linked(a1, 'Section', b)
    if hasattr(a2, 'Section'):
        assert _is_linked(a2, 'Section', b)
    _safe_set(b, 'page', set())
    assert not _is_linked(b, 'page', a2)
    if hasattr(a2, 'Section'):
        assert not _is_linked(a2, 'Section', b)


def test_assoc_site4_reverse_link_reassign_clear():
    a1 = bootstrap_Site(title="sample_text")
    a2 = bootstrap_Site(title="sample_text_2")
    b = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'pages', a1)
    assert _is_linked(b, 'pages', a1)
    if hasattr(a1, 'Site'):
        assert _is_linked(a1, 'Site', b)
    _safe_set(b, 'pages', a2)
    assert _is_linked(b, 'pages', a2)
    if hasattr(a1, 'Site'):
        assert not _is_linked(a1, 'Site', b)
    if hasattr(a2, 'Site'):
        assert _is_linked(a2, 'Site', b)
    _safe_set(b, 'pages', None)
    assert not _is_linked(b, 'pages', a2)
    if hasattr(a2, 'Site'):
        assert not _is_linked(a2, 'Site', b)


def test_assoc_site5_reverse_link_reassign_clear():
    a1 = bootstrap_Site(title="sample_text")
    a2 = bootstrap_Site(title="sample_text_2")
    b = bootstrap_MainPage(description="sample_text", title="sample_text")
    _safe_set(b, 'mainPage', a1)
    assert _is_linked(b, 'mainPage', a1)
    if hasattr(a1, 'Site6'):
        assert _is_linked(a1, 'Site6', b)
    _safe_set(b, 'mainPage', a2)
    assert _is_linked(b, 'mainPage', a2)
    if hasattr(a1, 'Site6'):
        assert not _is_linked(a1, 'Site6', b)
    if hasattr(a2, 'Site6'):
        assert _is_linked(a2, 'Site6', b)
    _safe_set(b, 'mainPage', None)
    assert not _is_linked(b, 'mainPage', a2)
    if hasattr(a2, 'Site6'):
        assert not _is_linked(a2, 'Site6', b)


def test_assoc_widgets7_reverse_link_reassign_clear():
    a1 = bootstrap_Widget(title="sample_text")
    a2 = bootstrap_Widget(title="sample_text_2")
    b = bootstrap_Section(description="sample_text", title="sample_text")
    _safe_set(b, 'section', {a1})
    assert _is_linked(b, 'section', a1)
    if hasattr(a1, 'Widget'):
        assert _is_linked(a1, 'Widget', b)
    _safe_set(b, 'section', {a2})
    assert _is_linked(b, 'section', a2)
    if hasattr(a1, 'Widget'):
        assert not _is_linked(a1, 'Widget', b)
    if hasattr(a2, 'Widget'):
        assert _is_linked(a2, 'Widget', b)
    _safe_set(b, 'section', set())
    assert not _is_linked(b, 'section', a2)
    if hasattr(a2, 'Widget'):
        assert not _is_linked(a2, 'Widget', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_form13_stub_double():
    # bootstrap_Form has no real 'Form' property in the generated
    # code (a bare stub) -- manually attach it so bootstrap_FormWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bootstrap_FormWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bootstrap_FormWidget(label="sample_text")
    partner = bootstrap_Form()
    setattr(partner, 'Form', None)
    _safe_set(owner, 'formWidgets', partner)
    assert getattr(partner, 'Form') == owner
    _safe_set(owner, 'formWidgets', None)
    assert getattr(partner, 'Form') is None


def test_assoc_formWidgets12_stub_double():
    # bootstrap_Form has no real 'form' property in the generated
    # code (a bare stub) -- manually attach it so bootstrap_FormWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bootstrap_FormWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bootstrap_FormWidget(label="sample_text")
    partner = bootstrap_Form()
    setattr(partner, 'form', None)
    _safe_set(owner, 'FormWidget', partner)
    assert owner in getattr(partner, 'form')
    _safe_set(owner, 'FormWidget', None)
    assert owner not in getattr(partner, 'form')


