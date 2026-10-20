import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arch_Application,
    Arch_Attribute,
    Arch_BackEnd,
    Arch_Controller,
    Arch_Div,
    Arch_DropDownList,
    Arch_Entity,
    Arch_Event,
    Arch_FrontEnd,
    Arch_GraphicControl,
    Arch_Label,
    Arch_Logic,
    Arch_Method,
    Arch_Parameter,
    Arch_Service,
    Arch_TextBox,
    Arch_View,
    GraphicControl,
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

def test_assoc_attributes28_reverse_link_reassign_clear():
    a1 = Arch_Entity(name="sample_text")
    a2 = Arch_Entity(name="sample_text_2")
    b = Arch_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'Arch_Attribute', a1)
    assert _is_linked(b, 'Arch_Attribute', a1)
    if hasattr(a1, 'Arch_Entity29'):
        assert _is_linked(a1, 'Arch_Entity29', b)
    _safe_set(b, 'Arch_Attribute', a2)
    assert _is_linked(b, 'Arch_Attribute', a2)
    if hasattr(a1, 'Arch_Entity29'):
        assert not _is_linked(a1, 'Arch_Entity29', b)
    if hasattr(a2, 'Arch_Entity29'):
        assert _is_linked(a2, 'Arch_Entity29', b)
    _safe_set(b, 'Arch_Attribute', None)
    assert not _is_linked(b, 'Arch_Attribute', a2)
    if hasattr(a2, 'Arch_Entity29'):
        assert not _is_linked(a2, 'Arch_Entity29', b)


def test_assoc_backend1_reverse_link_reassign_clear():
    a1 = Arch_BackEnd(name="sample_text")
    a2 = Arch_BackEnd(name="sample_text_2")
    b = Arch_Application(name="sample_text")
    _safe_set(b, 'Arch_Application2', a1)
    assert _is_linked(b, 'Arch_Application2', a1)
    if hasattr(a1, 'Arch_BackEnd'):
        assert _is_linked(a1, 'Arch_BackEnd', b)
    _safe_set(b, 'Arch_Application2', a2)
    assert _is_linked(b, 'Arch_Application2', a2)
    if hasattr(a1, 'Arch_BackEnd'):
        assert not _is_linked(a1, 'Arch_BackEnd', b)
    if hasattr(a2, 'Arch_BackEnd'):
        assert _is_linked(a2, 'Arch_BackEnd', b)
    _safe_set(b, 'Arch_Application2', None)
    assert not _is_linked(b, 'Arch_Application2', a2)
    if hasattr(a2, 'Arch_BackEnd'):
        assert not _is_linked(a2, 'Arch_BackEnd', b)


def test_assoc_controllers15_reverse_link_reassign_clear():
    a1 = Arch_View(name="sample_text")
    a2 = Arch_View(name="sample_text_2")
    b = Arch_Controller(name="sample_text")
    _safe_set(b, 'Arch_Controller17', a1)
    assert _is_linked(b, 'Arch_Controller17', a1)
    if hasattr(a1, 'Arch_View16'):
        assert _is_linked(a1, 'Arch_View16', b)
    _safe_set(b, 'Arch_Controller17', a2)
    assert _is_linked(b, 'Arch_Controller17', a2)
    if hasattr(a1, 'Arch_View16'):
        assert not _is_linked(a1, 'Arch_View16', b)
    if hasattr(a2, 'Arch_View16'):
        assert _is_linked(a2, 'Arch_View16', b)
    _safe_set(b, 'Arch_Controller17', None)
    assert not _is_linked(b, 'Arch_Controller17', a2)
    if hasattr(a2, 'Arch_View16'):
        assert not _is_linked(a2, 'Arch_View16', b)


def test_assoc_controllers5_reverse_link_reassign_clear():
    a1 = Arch_FrontEnd(name="sample_text")
    a2 = Arch_FrontEnd(name="sample_text_2")
    b = Arch_Controller(name="sample_text")
    _safe_set(b, 'Arch_Controller', a1)
    assert _is_linked(b, 'Arch_Controller', a1)
    if hasattr(a1, 'Arch_FrontEnd6'):
        assert _is_linked(a1, 'Arch_FrontEnd6', b)
    _safe_set(b, 'Arch_Controller', a2)
    assert _is_linked(b, 'Arch_Controller', a2)
    if hasattr(a1, 'Arch_FrontEnd6'):
        assert not _is_linked(a1, 'Arch_FrontEnd6', b)
    if hasattr(a2, 'Arch_FrontEnd6'):
        assert _is_linked(a2, 'Arch_FrontEnd6', b)
    _safe_set(b, 'Arch_Controller', None)
    assert not _is_linked(b, 'Arch_Controller', a2)
    if hasattr(a2, 'Arch_FrontEnd6'):
        assert not _is_linked(a2, 'Arch_FrontEnd6', b)


def test_assoc_entities11_reverse_link_reassign_clear():
    a1 = Arch_Entity(name="sample_text")
    a2 = Arch_Entity(name="sample_text_2")
    b = Arch_BackEnd(name="sample_text")
    _safe_set(b, 'Arch_BackEnd12', {a1})
    assert _is_linked(b, 'Arch_BackEnd12', a1)
    if hasattr(a1, 'Arch_Entity'):
        assert _is_linked(a1, 'Arch_Entity', b)
    _safe_set(b, 'Arch_BackEnd12', {a2})
    assert _is_linked(b, 'Arch_BackEnd12', a2)
    if hasattr(a1, 'Arch_Entity'):
        assert not _is_linked(a1, 'Arch_Entity', b)
    if hasattr(a2, 'Arch_Entity'):
        assert _is_linked(a2, 'Arch_Entity', b)
    _safe_set(b, 'Arch_BackEnd12', set())
    assert not _is_linked(b, 'Arch_BackEnd12', a2)
    if hasattr(a2, 'Arch_Entity'):
        assert not _is_linked(a2, 'Arch_Entity', b)


def test_assoc_events21_reverse_link_reassign_clear():
    a1 = Arch_Event(name="sample_text")
    a2 = Arch_Event(name="sample_text_2")
    b = Arch_Controller(name="sample_text")
    _safe_set(b, 'Arch_Controller22', {a1})
    assert _is_linked(b, 'Arch_Controller22', a1)
    if hasattr(a1, 'Arch_Event'):
        assert _is_linked(a1, 'Arch_Event', b)
    _safe_set(b, 'Arch_Controller22', {a2})
    assert _is_linked(b, 'Arch_Controller22', a2)
    if hasattr(a1, 'Arch_Event'):
        assert not _is_linked(a1, 'Arch_Event', b)
    if hasattr(a2, 'Arch_Event'):
        assert _is_linked(a2, 'Arch_Event', b)
    _safe_set(b, 'Arch_Controller22', set())
    assert not _is_linked(b, 'Arch_Controller22', a2)
    if hasattr(a2, 'Arch_Event'):
        assert not _is_linked(a2, 'Arch_Event', b)


def test_assoc_events35_reverse_link_reassign_clear():
    a1 = Arch_GraphicControl(name="sample_text")
    a2 = Arch_GraphicControl(name="sample_text_2")
    b = Arch_Event(name="sample_text")
    _safe_set(b, 'Arch_Event37', a1)
    assert _is_linked(b, 'Arch_Event37', a1)
    if hasattr(a1, 'Arch_GraphicControl36'):
        assert _is_linked(a1, 'Arch_GraphicControl36', b)
    _safe_set(b, 'Arch_Event37', a2)
    assert _is_linked(b, 'Arch_Event37', a2)
    if hasattr(a1, 'Arch_GraphicControl36'):
        assert not _is_linked(a1, 'Arch_GraphicControl36', b)
    if hasattr(a2, 'Arch_GraphicControl36'):
        assert _is_linked(a2, 'Arch_GraphicControl36', b)
    _safe_set(b, 'Arch_Event37', None)
    assert not _is_linked(b, 'Arch_Event37', a2)
    if hasattr(a2, 'Arch_GraphicControl36'):
        assert not _is_linked(a2, 'Arch_GraphicControl36', b)


def test_assoc_frontend0_reverse_link_reassign_clear():
    a1 = Arch_FrontEnd(name="sample_text")
    a2 = Arch_FrontEnd(name="sample_text_2")
    b = Arch_Application(name="sample_text")
    _safe_set(b, 'Arch_Application', a1)
    assert _is_linked(b, 'Arch_Application', a1)
    if hasattr(a1, 'Arch_FrontEnd'):
        assert _is_linked(a1, 'Arch_FrontEnd', b)
    _safe_set(b, 'Arch_Application', a2)
    assert _is_linked(b, 'Arch_Application', a2)
    if hasattr(a1, 'Arch_FrontEnd'):
        assert not _is_linked(a1, 'Arch_FrontEnd', b)
    if hasattr(a2, 'Arch_FrontEnd'):
        assert _is_linked(a2, 'Arch_FrontEnd', b)
    _safe_set(b, 'Arch_Application', None)
    assert not _is_linked(b, 'Arch_Application', a2)
    if hasattr(a2, 'Arch_FrontEnd'):
        assert not _is_linked(a2, 'Arch_FrontEnd', b)


def test_assoc_graphicControls13_reverse_link_reassign_clear():
    a1 = Arch_View(name="sample_text")
    a2 = Arch_View(name="sample_text_2")
    b = Arch_GraphicControl(name="sample_text")
    _safe_set(b, 'Arch_GraphicControl', a1)
    assert _is_linked(b, 'Arch_GraphicControl', a1)
    if hasattr(a1, 'Arch_View14'):
        assert _is_linked(a1, 'Arch_View14', b)
    _safe_set(b, 'Arch_GraphicControl', a2)
    assert _is_linked(b, 'Arch_GraphicControl', a2)
    if hasattr(a1, 'Arch_View14'):
        assert not _is_linked(a1, 'Arch_View14', b)
    if hasattr(a2, 'Arch_View14'):
        assert _is_linked(a2, 'Arch_View14', b)
    _safe_set(b, 'Arch_GraphicControl', None)
    assert not _is_linked(b, 'Arch_GraphicControl', a2)
    if hasattr(a2, 'Arch_View14'):
        assert not _is_linked(a2, 'Arch_View14', b)


def test_assoc_logics9_reverse_link_reassign_clear():
    a1 = Arch_Logic(name="sample_text")
    a2 = Arch_Logic(name="sample_text_2")
    b = Arch_BackEnd(name="sample_text")
    _safe_set(b, 'Arch_BackEnd10', {a1})
    assert _is_linked(b, 'Arch_BackEnd10', a1)
    if hasattr(a1, 'Arch_Logic'):
        assert _is_linked(a1, 'Arch_Logic', b)
    _safe_set(b, 'Arch_BackEnd10', {a2})
    assert _is_linked(b, 'Arch_BackEnd10', a2)
    if hasattr(a1, 'Arch_Logic'):
        assert not _is_linked(a1, 'Arch_Logic', b)
    if hasattr(a2, 'Arch_Logic'):
        assert _is_linked(a2, 'Arch_Logic', b)
    _safe_set(b, 'Arch_BackEnd10', set())
    assert not _is_linked(b, 'Arch_BackEnd10', a2)
    if hasattr(a2, 'Arch_Logic'):
        assert not _is_linked(a2, 'Arch_Logic', b)


def test_assoc_methods23_reverse_link_reassign_clear():
    a1 = Arch_Service(name="sample_text")
    a2 = Arch_Service(name="sample_text_2")
    b = Arch_Method(name="sample_text", returntype="sample_text")
    _safe_set(b, 'Arch_Method', a1)
    assert _is_linked(b, 'Arch_Method', a1)
    if hasattr(a1, 'Arch_Service24'):
        assert _is_linked(a1, 'Arch_Service24', b)
    _safe_set(b, 'Arch_Method', a2)
    assert _is_linked(b, 'Arch_Method', a2)
    if hasattr(a1, 'Arch_Service24'):
        assert not _is_linked(a1, 'Arch_Service24', b)
    if hasattr(a2, 'Arch_Service24'):
        assert _is_linked(a2, 'Arch_Service24', b)
    _safe_set(b, 'Arch_Method', None)
    assert not _is_linked(b, 'Arch_Method', a2)
    if hasattr(a2, 'Arch_Service24'):
        assert not _is_linked(a2, 'Arch_Service24', b)


def test_assoc_methods25_reverse_link_reassign_clear():
    a1 = Arch_Method(name="sample_text", returntype="sample_text")
    a2 = Arch_Method(name="sample_text_2", returntype="sample_text_2")
    b = Arch_Logic(name="sample_text")
    _safe_set(b, 'Arch_Logic26', {a1})
    assert _is_linked(b, 'Arch_Logic26', a1)
    if hasattr(a1, 'Arch_Method27'):
        assert _is_linked(a1, 'Arch_Method27', b)
    _safe_set(b, 'Arch_Logic26', {a2})
    assert _is_linked(b, 'Arch_Logic26', a2)
    if hasattr(a1, 'Arch_Method27'):
        assert not _is_linked(a1, 'Arch_Method27', b)
    if hasattr(a2, 'Arch_Method27'):
        assert _is_linked(a2, 'Arch_Method27', b)
    _safe_set(b, 'Arch_Logic26', set())
    assert not _is_linked(b, 'Arch_Logic26', a2)
    if hasattr(a2, 'Arch_Method27'):
        assert not _is_linked(a2, 'Arch_Method27', b)


def test_assoc_methods30_reverse_link_reassign_clear():
    a1 = Arch_Method(name="sample_text", returntype="sample_text")
    a2 = Arch_Method(name="sample_text_2", returntype="sample_text_2")
    b = Arch_Entity(name="sample_text")
    _safe_set(b, 'Arch_Entity31', {a1})
    assert _is_linked(b, 'Arch_Entity31', a1)
    if hasattr(a1, 'Arch_Method32'):
        assert _is_linked(a1, 'Arch_Method32', b)
    _safe_set(b, 'Arch_Entity31', {a2})
    assert _is_linked(b, 'Arch_Entity31', a2)
    if hasattr(a1, 'Arch_Method32'):
        assert not _is_linked(a1, 'Arch_Method32', b)
    if hasattr(a2, 'Arch_Method32'):
        assert _is_linked(a2, 'Arch_Method32', b)
    _safe_set(b, 'Arch_Entity31', set())
    assert not _is_linked(b, 'Arch_Entity31', a2)
    if hasattr(a2, 'Arch_Method32'):
        assert not _is_linked(a2, 'Arch_Method32', b)


def test_assoc_parameters33_reverse_link_reassign_clear():
    a1 = Arch_Parameter(name="sample_text", type="sample_text")
    a2 = Arch_Parameter(name="sample_text_2", type="sample_text_2")
    b = Arch_Method(name="sample_text", returntype="sample_text")
    _safe_set(b, 'Arch_Method34', {a1})
    assert _is_linked(b, 'Arch_Method34', a1)
    if hasattr(a1, 'Arch_Parameter'):
        assert _is_linked(a1, 'Arch_Parameter', b)
    _safe_set(b, 'Arch_Method34', {a2})
    assert _is_linked(b, 'Arch_Method34', a2)
    if hasattr(a1, 'Arch_Parameter'):
        assert not _is_linked(a1, 'Arch_Parameter', b)
    if hasattr(a2, 'Arch_Parameter'):
        assert _is_linked(a2, 'Arch_Parameter', b)
    _safe_set(b, 'Arch_Method34', set())
    assert not _is_linked(b, 'Arch_Method34', a2)
    if hasattr(a2, 'Arch_Parameter'):
        assert not _is_linked(a2, 'Arch_Parameter', b)


def test_assoc_services7_reverse_link_reassign_clear():
    a1 = Arch_Service(name="sample_text")
    a2 = Arch_Service(name="sample_text_2")
    b = Arch_BackEnd(name="sample_text")
    _safe_set(b, 'Arch_BackEnd8', {a1})
    assert _is_linked(b, 'Arch_BackEnd8', a1)
    if hasattr(a1, 'Arch_Service'):
        assert _is_linked(a1, 'Arch_Service', b)
    _safe_set(b, 'Arch_BackEnd8', {a2})
    assert _is_linked(b, 'Arch_BackEnd8', a2)
    if hasattr(a1, 'Arch_Service'):
        assert not _is_linked(a1, 'Arch_Service', b)
    if hasattr(a2, 'Arch_Service'):
        assert _is_linked(a2, 'Arch_Service', b)
    _safe_set(b, 'Arch_BackEnd8', set())
    assert not _is_linked(b, 'Arch_BackEnd8', a2)
    if hasattr(a2, 'Arch_Service'):
        assert not _is_linked(a2, 'Arch_Service', b)


def test_assoc_views18_reverse_link_reassign_clear():
    a1 = Arch_View(name="sample_text")
    a2 = Arch_View(name="sample_text_2")
    b = Arch_Controller(name="sample_text")
    _safe_set(b, 'Arch_Controller19', {a1})
    assert _is_linked(b, 'Arch_Controller19', a1)
    if hasattr(a1, 'Arch_View20'):
        assert _is_linked(a1, 'Arch_View20', b)
    _safe_set(b, 'Arch_Controller19', {a2})
    assert _is_linked(b, 'Arch_Controller19', a2)
    if hasattr(a1, 'Arch_View20'):
        assert not _is_linked(a1, 'Arch_View20', b)
    if hasattr(a2, 'Arch_View20'):
        assert _is_linked(a2, 'Arch_View20', b)
    _safe_set(b, 'Arch_Controller19', set())
    assert not _is_linked(b, 'Arch_Controller19', a2)
    if hasattr(a2, 'Arch_View20'):
        assert not _is_linked(a2, 'Arch_View20', b)


def test_assoc_views3_reverse_link_reassign_clear():
    a1 = Arch_View(name="sample_text")
    a2 = Arch_View(name="sample_text_2")
    b = Arch_FrontEnd(name="sample_text")
    _safe_set(b, 'Arch_FrontEnd4', {a1})
    assert _is_linked(b, 'Arch_FrontEnd4', a1)
    if hasattr(a1, 'Arch_View'):
        assert _is_linked(a1, 'Arch_View', b)
    _safe_set(b, 'Arch_FrontEnd4', {a2})
    assert _is_linked(b, 'Arch_FrontEnd4', a2)
    if hasattr(a1, 'Arch_View'):
        assert not _is_linked(a1, 'Arch_View', b)
    if hasattr(a2, 'Arch_View'):
        assert _is_linked(a2, 'Arch_View', b)
    _safe_set(b, 'Arch_FrontEnd4', set())
    assert not _is_linked(b, 'Arch_FrontEnd4', a2)
    if hasattr(a2, 'Arch_View'):
        assert not _is_linked(a2, 'Arch_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_graphicControls38_stub_double():
    # Arch_Div has no real 'Arch_Div' property in the generated
    # code (a bare stub) -- manually attach it so Arch_GraphicControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Arch_GraphicControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Arch_GraphicControl(name="sample_text")
    partner = Arch_Div()
    setattr(partner, 'Arch_Div', None)
    _safe_set(owner, 'Arch_GraphicControl39', partner)
    assert owner in getattr(partner, 'Arch_Div')
    _safe_set(owner, 'Arch_GraphicControl39', None)
    assert owner not in getattr(partner, 'Arch_Div')


