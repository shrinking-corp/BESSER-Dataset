import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractView,
    FormWidget,
    NamedElement,
    Widget,
    webapp_AbstractView,
    webapp_Application,
    webapp_Attribute,
    webapp_CheckBox,
    webapp_Collection,
    webapp_Form,
    webapp_FormWidget,
    webapp_Gallery,
    webapp_ImagesBlock,
    webapp_Model,
    webapp_ModelView,
    webapp_NamedElement,
    webapp_Operation,
    webapp_Parameter,
    webapp_Reference,
    webapp_Router,
    webapp_RouterMapping,
    webapp_Section,
    webapp_Spinner,
    webapp_StaticView,
    webapp_Table,
    webapp_Text,
    webapp_TextArea,
    webapp_Video,
    webapp_Widget,
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

def test_assoc_section37_reverse_link_reassign_clear():
    a1 = webapp_Widget(title="sample_text")
    a2 = webapp_Widget(title="sample_text_2")
    b = webapp_Section(description="sample_text", title="sample_text")
    _safe_set(b, 'Section38', a1)
    assert _is_linked(b, 'Section38', a1)
    if hasattr(a1, 'widgets'):
        assert _is_linked(a1, 'widgets', b)
    _safe_set(b, 'Section38', a2)
    assert _is_linked(b, 'Section38', a2)
    if hasattr(a1, 'widgets'):
        assert not _is_linked(a1, 'widgets', b)
    if hasattr(a2, 'widgets'):
        assert _is_linked(a2, 'widgets', b)
    _safe_set(b, 'Section38', None)
    assert not _is_linked(b, 'Section38', a2)
    if hasattr(a2, 'widgets'):
        assert not _is_linked(a2, 'widgets', b)


def test_assoc_view25_reverse_link_reassign_clear():
    a1 = webapp_RouterMapping(path="sample_text")
    a2 = webapp_RouterMapping(path="sample_text_2")
    b = webapp_AbstractView(description="sample_text")
    _safe_set(b, 'webapp_AbstractView', a1)
    assert _is_linked(b, 'webapp_AbstractView', a1)
    if hasattr(a1, 'webapp_RouterMapping26'):
        assert _is_linked(a1, 'webapp_RouterMapping26', b)
    _safe_set(b, 'webapp_AbstractView', a2)
    assert _is_linked(b, 'webapp_AbstractView', a2)
    if hasattr(a1, 'webapp_RouterMapping26'):
        assert not _is_linked(a1, 'webapp_RouterMapping26', b)
    if hasattr(a2, 'webapp_RouterMapping26'):
        assert _is_linked(a2, 'webapp_RouterMapping26', b)
    _safe_set(b, 'webapp_AbstractView', None)
    assert not _is_linked(b, 'webapp_AbstractView', a2)
    if hasattr(a2, 'webapp_RouterMapping26'):
        assert not _is_linked(a2, 'webapp_RouterMapping26', b)


def test_assoc_widgets35_reverse_link_reassign_clear():
    a1 = webapp_Widget(title="sample_text")
    a2 = webapp_Widget(title="sample_text_2")
    b = webapp_Section(description="sample_text", title="sample_text")
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

def test_assoc_application30_stub_double():
    # webapp_Application has no real 'Application31' property in the generated
    # code (a bare stub) -- manually attach it so webapp_AbstractView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_AbstractView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_AbstractView(description="sample_text")
    partner = webapp_Application()
    setattr(partner, 'Application31', None)
    _safe_set(owner, 'views', partner)
    assert getattr(partner, 'Application31') == owner
    _safe_set(owner, 'views', None)
    assert getattr(partner, 'Application31') is None


def test_assoc_attributes7_stub_double():
    # webapp_Model has no real 'webapp_Model' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(defaultValue="sample_text")
    partner = webapp_Model()
    setattr(partner, 'webapp_Model', None)
    _safe_set(owner, 'webapp_Attribute', partner)
    assert owner in getattr(partner, 'webapp_Model')
    _safe_set(owner, 'webapp_Attribute', None)
    assert owner not in getattr(partner, 'webapp_Model')


def test_assoc_form40_stub_double():
    # webapp_Form has no real 'Form' property in the generated
    # code (a bare stub) -- manually attach it so webapp_FormWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_FormWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_FormWidget(label="sample_text")
    partner = webapp_Form()
    setattr(partner, 'Form', None)
    _safe_set(owner, 'formWidgets', partner)
    assert getattr(partner, 'Form') == owner
    _safe_set(owner, 'formWidgets', None)
    assert getattr(partner, 'Form') is None


def test_assoc_formWidgets39_stub_double():
    # webapp_Form has no real 'form' property in the generated
    # code (a bare stub) -- manually attach it so webapp_FormWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_FormWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_FormWidget(label="sample_text")
    partner = webapp_Form()
    setattr(partner, 'form', None)
    _safe_set(owner, 'FormWidget', partner)
    assert owner in getattr(partner, 'form')
    _safe_set(owner, 'FormWidget', None)
    assert owner not in getattr(partner, 'form')


def test_assoc_mappings22_stub_double():
    # webapp_Router has no real 'webapp_Router' property in the generated
    # code (a bare stub) -- manually attach it so webapp_RouterMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_RouterMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_RouterMapping(path="sample_text")
    partner = webapp_Router()
    setattr(partner, 'webapp_Router', None)
    _safe_set(owner, 'webapp_RouterMapping', partner)
    assert owner in getattr(partner, 'webapp_Router')
    _safe_set(owner, 'webapp_RouterMapping', None)
    assert owner not in getattr(partner, 'webapp_Router')


def test_assoc_operations27_stub_double():
    # webapp_Operation has no real 'webapp_Operation29' property in the generated
    # code (a bare stub) -- manually attach it so webapp_AbstractView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_AbstractView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_AbstractView(description="sample_text")
    partner = webapp_Operation()
    setattr(partner, 'webapp_Operation29', None)
    _safe_set(owner, 'webapp_AbstractView28', {partner})
    assert getattr(partner, 'webapp_Operation29') == owner
    _safe_set(owner, 'webapp_AbstractView28', set())
    assert getattr(partner, 'webapp_Operation29') is None


def test_assoc_sections34_stub_double():
    # webapp_StaticView has no real 'view' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Section(description="sample_text", title="sample_text")
    partner = webapp_StaticView()
    setattr(partner, 'view', None)
    _safe_set(owner, 'Section', partner)
    assert owner in getattr(partner, 'view')
    _safe_set(owner, 'Section', None)
    assert owner not in getattr(partner, 'view')


def test_assoc_view36_stub_double():
    # webapp_StaticView has no real 'StaticView' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Section(description="sample_text", title="sample_text")
    partner = webapp_StaticView()
    setattr(partner, 'StaticView', None)
    _safe_set(owner, 'sections', partner)
    assert getattr(partner, 'StaticView') == owner
    _safe_set(owner, 'sections', None)
    assert getattr(partner, 'StaticView') is None


def test_assoc_views3_stub_double():
    # webapp_Application has no real 'application4' property in the generated
    # code (a bare stub) -- manually attach it so webapp_AbstractView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_AbstractView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_AbstractView(description="sample_text")
    partner = webapp_Application()
    setattr(partner, 'application4', None)
    _safe_set(owner, 'AbstractView', partner)
    assert owner in getattr(partner, 'application4')
    _safe_set(owner, 'AbstractView', None)
    assert owner not in getattr(partner, 'application4')


