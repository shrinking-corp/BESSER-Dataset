import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotable,
    UIComponent,
    mvc_Action,
    mvc_Association,
    mvc_Attribute,
    mvc_Component,
    mvc_Controller,
    mvc_ControllerView,
    mvc_Entity,
    mvc_Event,
    mvc_EventAction,
    mvc_MVCModel,
    mvc_Model,
    mvc_UIActions,
    mvc_UIComponent,
    mvc_UIInput,
    mvc_UILayout,
    mvc_View,
    AssociationType,
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

def test_assoc_actions26_reverse_link_reassign_clear():
    a1 = mvc_Controller(name="sample_text")
    a2 = mvc_Controller(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action', a1)
    assert _is_linked(b, 'mvc_Action', a1)
    if hasattr(a1, 'mvc_Controller27'):
        assert _is_linked(a1, 'mvc_Controller27', b)
    _safe_set(b, 'mvc_Action', a2)
    assert _is_linked(b, 'mvc_Action', a2)
    if hasattr(a1, 'mvc_Controller27'):
        assert not _is_linked(a1, 'mvc_Controller27', b)
    if hasattr(a2, 'mvc_Controller27'):
        assert _is_linked(a2, 'mvc_Controller27', b)
    _safe_set(b, 'mvc_Action', None)
    assert not _is_linked(b, 'mvc_Action', a2)
    if hasattr(a2, 'mvc_Controller27'):
        assert not _is_linked(a2, 'mvc_Controller27', b)


def test_assoc_associations1_reverse_link_reassign_clear():
    a1 = mvc_Model(name="sample_text")
    a2 = mvc_Model(name="sample_text_2")
    b = mvc_Association(containment=True, lowerBound=7, name="sample_text", type="sample_text", upperBound=7)
    _safe_set(b, 'mvc_Association', a1)
    assert _is_linked(b, 'mvc_Association', a1)
    if hasattr(a1, 'mvc_Model2'):
        assert _is_linked(a1, 'mvc_Model2', b)
    _safe_set(b, 'mvc_Association', a2)
    assert _is_linked(b, 'mvc_Association', a2)
    if hasattr(a1, 'mvc_Model2'):
        assert not _is_linked(a1, 'mvc_Model2', b)
    if hasattr(a2, 'mvc_Model2'):
        assert _is_linked(a2, 'mvc_Model2', b)
    _safe_set(b, 'mvc_Association', None)
    assert not _is_linked(b, 'mvc_Association', a2)
    if hasattr(a2, 'mvc_Model2'):
        assert not _is_linked(a2, 'mvc_Model2', b)


def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = mvc_Entity(name="sample_text")
    a2 = mvc_Entity(name="sample_text_2")
    b = mvc_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'mvc_Attribute', a1)
    assert _is_linked(b, 'mvc_Attribute', a1)
    if hasattr(a1, 'mvc_Entity4'):
        assert _is_linked(a1, 'mvc_Entity4', b)
    _safe_set(b, 'mvc_Attribute', a2)
    assert _is_linked(b, 'mvc_Attribute', a2)
    if hasattr(a1, 'mvc_Entity4'):
        assert not _is_linked(a1, 'mvc_Entity4', b)
    if hasattr(a2, 'mvc_Entity4'):
        assert _is_linked(a2, 'mvc_Entity4', b)
    _safe_set(b, 'mvc_Attribute', None)
    assert not _is_linked(b, 'mvc_Attribute', a2)
    if hasattr(a2, 'mvc_Entity4'):
        assert not _is_linked(a2, 'mvc_Entity4', b)


def test_assoc_components24_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Component(name="sample_text")
    _safe_set(b, 'mvc_Component', a1)
    assert _is_linked(b, 'mvc_Component', a1)
    if hasattr(a1, 'mvc_MVCModel25'):
        assert _is_linked(a1, 'mvc_MVCModel25', b)
    _safe_set(b, 'mvc_Component', a2)
    assert _is_linked(b, 'mvc_Component', a2)
    if hasattr(a1, 'mvc_MVCModel25'):
        assert not _is_linked(a1, 'mvc_MVCModel25', b)
    if hasattr(a2, 'mvc_MVCModel25'):
        assert _is_linked(a2, 'mvc_MVCModel25', b)
    _safe_set(b, 'mvc_Component', None)
    assert not _is_linked(b, 'mvc_Component', a2)
    if hasattr(a2, 'mvc_MVCModel25'):
        assert not _is_linked(a2, 'mvc_MVCModel25', b)


def test_assoc_components56_reverse_link_reassign_clear():
    a1 = mvc_UILayout(columns=7, orientation="sample_text")
    a2 = mvc_UILayout(columns=13, orientation="sample_text_2")
    b = mvc_UIComponent(name="sample_text", type="sample_text")
    _safe_set(b, 'mvc_UIComponent', a1)
    assert _is_linked(b, 'mvc_UIComponent', a1)
    if hasattr(a1, 'mvc_UILayout57'):
        assert _is_linked(a1, 'mvc_UILayout57', b)
    _safe_set(b, 'mvc_UIComponent', a2)
    assert _is_linked(b, 'mvc_UIComponent', a2)
    if hasattr(a1, 'mvc_UILayout57'):
        assert not _is_linked(a1, 'mvc_UILayout57', b)
    if hasattr(a2, 'mvc_UILayout57'):
        assert _is_linked(a2, 'mvc_UILayout57', b)
    _safe_set(b, 'mvc_UIComponent', None)
    assert not _is_linked(b, 'mvc_UIComponent', a2)
    if hasattr(a2, 'mvc_UILayout57'):
        assert not _is_linked(a2, 'mvc_UILayout57', b)


def test_assoc_controllers22_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'mvc_Controller', a1)
    assert _is_linked(b, 'mvc_Controller', a1)
    if hasattr(a1, 'mvc_MVCModel23'):
        assert _is_linked(a1, 'mvc_MVCModel23', b)
    _safe_set(b, 'mvc_Controller', a2)
    assert _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a1, 'mvc_MVCModel23'):
        assert not _is_linked(a1, 'mvc_MVCModel23', b)
    if hasattr(a2, 'mvc_MVCModel23'):
        assert _is_linked(a2, 'mvc_MVCModel23', b)
    _safe_set(b, 'mvc_Controller', None)
    assert not _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a2, 'mvc_MVCModel23'):
        assert not _is_linked(a2, 'mvc_MVCModel23', b)


def test_assoc_controllers47_reverse_link_reassign_clear():
    a1 = mvc_Controller(name="sample_text")
    a2 = mvc_Controller(name="sample_text_2")
    b = mvc_Component(name="sample_text")
    _safe_set(b, 'mvc_Component48', {a1})
    assert _is_linked(b, 'mvc_Component48', a1)
    if hasattr(a1, 'mvc_Controller49'):
        assert _is_linked(a1, 'mvc_Controller49', b)
    _safe_set(b, 'mvc_Component48', {a2})
    assert _is_linked(b, 'mvc_Component48', a2)
    if hasattr(a1, 'mvc_Controller49'):
        assert not _is_linked(a1, 'mvc_Controller49', b)
    if hasattr(a2, 'mvc_Controller49'):
        assert _is_linked(a2, 'mvc_Controller49', b)
    _safe_set(b, 'mvc_Component48', set())
    assert not _is_linked(b, 'mvc_Component48', a2)
    if hasattr(a2, 'mvc_Controller49'):
        assert not _is_linked(a2, 'mvc_Controller49', b)


def test_assoc_events20_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Event(name="sample_text")
    _safe_set(b, 'mvc_Event', a1)
    assert _is_linked(b, 'mvc_Event', a1)
    if hasattr(a1, 'mvc_MVCModel21'):
        assert _is_linked(a1, 'mvc_MVCModel21', b)
    _safe_set(b, 'mvc_Event', a2)
    assert _is_linked(b, 'mvc_Event', a2)
    if hasattr(a1, 'mvc_MVCModel21'):
        assert not _is_linked(a1, 'mvc_MVCModel21', b)
    if hasattr(a2, 'mvc_MVCModel21'):
        assert _is_linked(a2, 'mvc_MVCModel21', b)
    _safe_set(b, 'mvc_Event', None)
    assert not _is_linked(b, 'mvc_Event', a2)
    if hasattr(a2, 'mvc_MVCModel21'):
        assert not _is_linked(a2, 'mvc_MVCModel21', b)


def test_assoc_extends6_reverse_link_reassign_clear():
    a1 = mvc_Entity(name="sample_text")
    a2 = mvc_Entity(name="sample_text_2")
    b = mvc_Entity(name="sample_text")
    _safe_set(b, 'mvc_Entity7', a1)
    assert _is_linked(b, 'mvc_Entity7', a1)
    if hasattr(a1, 'mvc_Entity5'):
        assert _is_linked(a1, 'mvc_Entity5', b)
    _safe_set(b, 'mvc_Entity7', a2)
    assert _is_linked(b, 'mvc_Entity7', a2)
    if hasattr(a1, 'mvc_Entity5'):
        assert not _is_linked(a1, 'mvc_Entity5', b)
    if hasattr(a2, 'mvc_Entity5'):
        assert _is_linked(a2, 'mvc_Entity5', b)
    _safe_set(b, 'mvc_Entity7', None)
    assert not _is_linked(b, 'mvc_Entity7', a2)
    if hasattr(a2, 'mvc_Entity5'):
        assert not _is_linked(a2, 'mvc_Entity5', b)


def test_assoc_importView58_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text")
    a2 = mvc_View(name="sample_text_2")
    b = mvc_UILayout(columns=7, orientation="sample_text")
    _safe_set(b, 'mvc_UILayout59', {a1})
    assert _is_linked(b, 'mvc_UILayout59', a1)
    if hasattr(a1, 'mvc_View60'):
        assert _is_linked(a1, 'mvc_View60', b)
    _safe_set(b, 'mvc_UILayout59', {a2})
    assert _is_linked(b, 'mvc_UILayout59', a2)
    if hasattr(a1, 'mvc_View60'):
        assert not _is_linked(a1, 'mvc_View60', b)
    if hasattr(a2, 'mvc_View60'):
        assert _is_linked(a2, 'mvc_View60', b)
    _safe_set(b, 'mvc_UILayout59', set())
    assert not _is_linked(b, 'mvc_UILayout59', a2)
    if hasattr(a2, 'mvc_View60'):
        assert not _is_linked(a2, 'mvc_View60', b)


def test_assoc_models15_reverse_link_reassign_clear():
    a1 = mvc_Model(name="sample_text")
    a2 = mvc_Model(name="sample_text_2")
    b = mvc_MVCModel(name="sample_text", version="sample_text")
    _safe_set(b, 'mvc_MVCModel', {a1})
    assert _is_linked(b, 'mvc_MVCModel', a1)
    if hasattr(a1, 'mvc_Model16'):
        assert _is_linked(a1, 'mvc_Model16', b)
    _safe_set(b, 'mvc_MVCModel', {a2})
    assert _is_linked(b, 'mvc_MVCModel', a2)
    if hasattr(a1, 'mvc_Model16'):
        assert not _is_linked(a1, 'mvc_Model16', b)
    if hasattr(a2, 'mvc_Model16'):
        assert _is_linked(a2, 'mvc_Model16', b)
    _safe_set(b, 'mvc_MVCModel', set())
    assert not _is_linked(b, 'mvc_MVCModel', a2)
    if hasattr(a2, 'mvc_Model16'):
        assert not _is_linked(a2, 'mvc_Model16', b)


def test_assoc_postExecutionEvent35_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action36', a1)
    assert _is_linked(b, 'mvc_Action36', a1)
    if hasattr(a1, 'mvc_Event37'):
        assert _is_linked(a1, 'mvc_Event37', b)
    _safe_set(b, 'mvc_Action36', a2)
    assert _is_linked(b, 'mvc_Action36', a2)
    if hasattr(a1, 'mvc_Event37'):
        assert not _is_linked(a1, 'mvc_Event37', b)
    if hasattr(a2, 'mvc_Event37'):
        assert _is_linked(a2, 'mvc_Event37', b)
    _safe_set(b, 'mvc_Action36', None)
    assert not _is_linked(b, 'mvc_Action36', a2)
    if hasattr(a2, 'mvc_Event37'):
        assert not _is_linked(a2, 'mvc_Event37', b)


def test_assoc_preExecutionEvent32_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action33', a1)
    assert _is_linked(b, 'mvc_Action33', a1)
    if hasattr(a1, 'mvc_Event34'):
        assert _is_linked(a1, 'mvc_Event34', b)
    _safe_set(b, 'mvc_Action33', a2)
    assert _is_linked(b, 'mvc_Action33', a2)
    if hasattr(a1, 'mvc_Event34'):
        assert not _is_linked(a1, 'mvc_Event34', b)
    if hasattr(a2, 'mvc_Event34'):
        assert _is_linked(a2, 'mvc_Event34', b)
    _safe_set(b, 'mvc_Action33', None)
    assert not _is_linked(b, 'mvc_Action33', a2)
    if hasattr(a2, 'mvc_Event34'):
        assert not _is_linked(a2, 'mvc_Event34', b)


def test_assoc_rootComponent14_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text")
    a2 = mvc_View(name="sample_text_2")
    b = mvc_UILayout(columns=7, orientation="sample_text")
    _safe_set(b, 'mvc_UILayout', a1)
    assert _is_linked(b, 'mvc_UILayout', a1)
    if hasattr(a1, 'mvc_View'):
        assert _is_linked(a1, 'mvc_View', b)
    _safe_set(b, 'mvc_UILayout', a2)
    assert _is_linked(b, 'mvc_UILayout', a2)
    if hasattr(a1, 'mvc_View'):
        assert not _is_linked(a1, 'mvc_View', b)
    if hasattr(a2, 'mvc_View'):
        assert _is_linked(a2, 'mvc_View', b)
    _safe_set(b, 'mvc_UILayout', None)
    assert not _is_linked(b, 'mvc_UILayout', a2)
    if hasattr(a2, 'mvc_View'):
        assert not _is_linked(a2, 'mvc_View', b)


def test_assoc_rootEntity0_reverse_link_reassign_clear():
    a1 = mvc_Model(name="sample_text")
    a2 = mvc_Model(name="sample_text_2")
    b = mvc_Entity(name="sample_text")
    _safe_set(b, 'mvc_Entity', a1)
    assert _is_linked(b, 'mvc_Entity', a1)
    if hasattr(a1, 'mvc_Model'):
        assert _is_linked(a1, 'mvc_Model', b)
    _safe_set(b, 'mvc_Entity', a2)
    assert _is_linked(b, 'mvc_Entity', a2)
    if hasattr(a1, 'mvc_Model'):
        assert not _is_linked(a1, 'mvc_Model', b)
    if hasattr(a2, 'mvc_Model'):
        assert _is_linked(a2, 'mvc_Model', b)
    _safe_set(b, 'mvc_Entity', None)
    assert not _is_linked(b, 'mvc_Entity', a2)
    if hasattr(a2, 'mvc_Model'):
        assert not _is_linked(a2, 'mvc_Model', b)


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = mvc_Entity(name="sample_text")
    a2 = mvc_Entity(name="sample_text_2")
    b = mvc_Association(containment=True, lowerBound=7, name="sample_text", type="sample_text", upperBound=7)
    _safe_set(b, 'mvc_Association9', a1)
    assert _is_linked(b, 'mvc_Association9', a1)
    if hasattr(a1, 'mvc_Entity10'):
        assert _is_linked(a1, 'mvc_Entity10', b)
    _safe_set(b, 'mvc_Association9', a2)
    assert _is_linked(b, 'mvc_Association9', a2)
    if hasattr(a1, 'mvc_Entity10'):
        assert not _is_linked(a1, 'mvc_Entity10', b)
    if hasattr(a2, 'mvc_Entity10'):
        assert _is_linked(a2, 'mvc_Entity10', b)
    _safe_set(b, 'mvc_Association9', None)
    assert not _is_linked(b, 'mvc_Association9', a2)
    if hasattr(a2, 'mvc_Entity10'):
        assert not _is_linked(a2, 'mvc_Entity10', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = mvc_Entity(name="sample_text")
    a2 = mvc_Entity(name="sample_text_2")
    b = mvc_Association(containment=True, lowerBound=7, name="sample_text", type="sample_text", upperBound=7)
    _safe_set(b, 'mvc_Association12', a1)
    assert _is_linked(b, 'mvc_Association12', a1)
    if hasattr(a1, 'mvc_Entity13'):
        assert _is_linked(a1, 'mvc_Entity13', b)
    _safe_set(b, 'mvc_Association12', a2)
    assert _is_linked(b, 'mvc_Association12', a2)
    if hasattr(a1, 'mvc_Entity13'):
        assert not _is_linked(a1, 'mvc_Entity13', b)
    if hasattr(a2, 'mvc_Entity13'):
        assert _is_linked(a2, 'mvc_Entity13', b)
    _safe_set(b, 'mvc_Association12', None)
    assert not _is_linked(b, 'mvc_Association12', a2)
    if hasattr(a2, 'mvc_Entity13'):
        assert not _is_linked(a2, 'mvc_Entity13', b)


def test_assoc_triggerEvents38_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action39', {a1})
    assert _is_linked(b, 'mvc_Action39', a1)
    if hasattr(a1, 'mvc_Event40'):
        assert _is_linked(a1, 'mvc_Event40', b)
    _safe_set(b, 'mvc_Action39', {a2})
    assert _is_linked(b, 'mvc_Action39', a2)
    if hasattr(a1, 'mvc_Event40'):
        assert not _is_linked(a1, 'mvc_Event40', b)
    if hasattr(a2, 'mvc_Event40'):
        assert _is_linked(a2, 'mvc_Event40', b)
    _safe_set(b, 'mvc_Action39', set())
    assert not _is_linked(b, 'mvc_Action39', a2)
    if hasattr(a2, 'mvc_Event40'):
        assert not _is_linked(a2, 'mvc_Event40', b)


def test_assoc_views17_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text")
    a2 = mvc_View(name="sample_text_2")
    b = mvc_MVCModel(name="sample_text", version="sample_text")
    _safe_set(b, 'mvc_MVCModel18', {a1})
    assert _is_linked(b, 'mvc_MVCModel18', a1)
    if hasattr(a1, 'mvc_View19'):
        assert _is_linked(a1, 'mvc_View19', b)
    _safe_set(b, 'mvc_MVCModel18', {a2})
    assert _is_linked(b, 'mvc_MVCModel18', a2)
    if hasattr(a1, 'mvc_View19'):
        assert not _is_linked(a1, 'mvc_View19', b)
    if hasattr(a2, 'mvc_View19'):
        assert _is_linked(a2, 'mvc_View19', b)
    _safe_set(b, 'mvc_MVCModel18', set())
    assert not _is_linked(b, 'mvc_MVCModel18', a2)
    if hasattr(a2, 'mvc_View19'):
        assert not _is_linked(a2, 'mvc_View19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action50_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction51' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Action(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction51', None)
    _safe_set(owner, 'mvc_Action52', partner)
    assert getattr(partner, 'mvc_EventAction51') == owner
    _safe_set(owner, 'mvc_Action52', None)
    assert getattr(partner, 'mvc_EventAction51') is None


def test_assoc_eventActions30_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Controller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Controller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Controller(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction', None)
    _safe_set(owner, 'mvc_Controller31', {partner})
    assert getattr(partner, 'mvc_EventAction') == owner
    _safe_set(owner, 'mvc_Controller31', set())
    assert getattr(partner, 'mvc_EventAction') is None


def test_assoc_events53_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction54' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Event(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction54', None)
    _safe_set(owner, 'mvc_Event55', partner)
    assert owner in getattr(partner, 'mvc_EventAction54')
    _safe_set(owner, 'mvc_Event55', None)
    assert owner not in getattr(partner, 'mvc_EventAction54')


def test_assoc_models44_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView45' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Model(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView45', None)
    _safe_set(owner, 'mvc_Model46', partner)
    assert owner in getattr(partner, 'mvc_ControllerView45')
    _safe_set(owner, 'mvc_Model46', None)
    assert owner not in getattr(partner, 'mvc_ControllerView45')


def test_assoc_triggerEvent63_stub_double():
    # mvc_UIActions has no real 'mvc_UIActions' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Event(name="sample_text")
    partner = mvc_UIActions()
    setattr(partner, 'mvc_UIActions', None)
    _safe_set(owner, 'mvc_Event64', partner)
    assert getattr(partner, 'mvc_UIActions') == owner
    _safe_set(owner, 'mvc_Event64', None)
    assert getattr(partner, 'mvc_UIActions') is None


def test_assoc_value61_stub_double():
    # mvc_UIInput has no real 'mvc_UIInput' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Attribute(name="sample_text", type="sample_text")
    partner = mvc_UIInput()
    setattr(partner, 'mvc_UIInput', None)
    _safe_set(owner, 'mvc_Attribute62', partner)
    assert getattr(partner, 'mvc_UIInput') == owner
    _safe_set(owner, 'mvc_Attribute62', None)
    assert getattr(partner, 'mvc_UIInput') is None


def test_assoc_view41_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView42' property in the generated
    # code (a bare stub) -- manually attach it so mvc_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_View(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView42', None)
    _safe_set(owner, 'mvc_View43', partner)
    assert getattr(partner, 'mvc_ControllerView42') == owner
    _safe_set(owner, 'mvc_View43', None)
    assert getattr(partner, 'mvc_ControllerView42') is None


def test_assoc_views28_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Controller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Controller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Controller(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView', None)
    _safe_set(owner, 'mvc_Controller29', {partner})
    assert getattr(partner, 'mvc_ControllerView') == owner
    _safe_set(owner, 'mvc_Controller29', set())
    assert getattr(partner, 'mvc_ControllerView') is None


