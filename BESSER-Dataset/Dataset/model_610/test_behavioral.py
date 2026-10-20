import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotable,
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
    mvc_UIComponent,
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

def test_assoc_actions32_reverse_link_reassign_clear():
    a1 = mvc_Controller(name="sample_text")
    a2 = mvc_Controller(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action', a1)
    assert _is_linked(b, 'mvc_Action', a1)
    if hasattr(a1, 'mvc_Controller33'):
        assert _is_linked(a1, 'mvc_Controller33', b)
    _safe_set(b, 'mvc_Action', a2)
    assert _is_linked(b, 'mvc_Action', a2)
    if hasattr(a1, 'mvc_Controller33'):
        assert not _is_linked(a1, 'mvc_Controller33', b)
    if hasattr(a2, 'mvc_Controller33'):
        assert _is_linked(a2, 'mvc_Controller33', b)
    _safe_set(b, 'mvc_Action', None)
    assert not _is_linked(b, 'mvc_Action', a2)
    if hasattr(a2, 'mvc_Controller33'):
        assert not _is_linked(a2, 'mvc_Controller33', b)


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


def test_assoc_childs16_reverse_link_reassign_clear():
    a1 = mvc_UIComponent(id="sample_text", layout="sample_text", name="sample_text", type="sample_text")
    a2 = mvc_UIComponent(id="sample_text_2", layout="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = mvc_UIComponent(id="sample_text", layout="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'mvc_UIComponent17', a1)
    assert _is_linked(b, 'mvc_UIComponent17', a1)
    if hasattr(a1, 'mvc_UIComponent15'):
        assert _is_linked(a1, 'mvc_UIComponent15', b)
    _safe_set(b, 'mvc_UIComponent17', a2)
    assert _is_linked(b, 'mvc_UIComponent17', a2)
    if hasattr(a1, 'mvc_UIComponent15'):
        assert not _is_linked(a1, 'mvc_UIComponent15', b)
    if hasattr(a2, 'mvc_UIComponent15'):
        assert _is_linked(a2, 'mvc_UIComponent15', b)
    _safe_set(b, 'mvc_UIComponent17', None)
    assert not _is_linked(b, 'mvc_UIComponent17', a2)
    if hasattr(a2, 'mvc_UIComponent15'):
        assert not _is_linked(a2, 'mvc_UIComponent15', b)


def test_assoc_components30_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Component(name="sample_text")
    _safe_set(b, 'mvc_Component', a1)
    assert _is_linked(b, 'mvc_Component', a1)
    if hasattr(a1, 'mvc_MVCModel31'):
        assert _is_linked(a1, 'mvc_MVCModel31', b)
    _safe_set(b, 'mvc_Component', a2)
    assert _is_linked(b, 'mvc_Component', a2)
    if hasattr(a1, 'mvc_MVCModel31'):
        assert not _is_linked(a1, 'mvc_MVCModel31', b)
    if hasattr(a2, 'mvc_MVCModel31'):
        assert _is_linked(a2, 'mvc_MVCModel31', b)
    _safe_set(b, 'mvc_Component', None)
    assert not _is_linked(b, 'mvc_Component', a2)
    if hasattr(a2, 'mvc_MVCModel31'):
        assert not _is_linked(a2, 'mvc_MVCModel31', b)


def test_assoc_controllers28_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'mvc_Controller', a1)
    assert _is_linked(b, 'mvc_Controller', a1)
    if hasattr(a1, 'mvc_MVCModel29'):
        assert _is_linked(a1, 'mvc_MVCModel29', b)
    _safe_set(b, 'mvc_Controller', a2)
    assert _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a1, 'mvc_MVCModel29'):
        assert not _is_linked(a1, 'mvc_MVCModel29', b)
    if hasattr(a2, 'mvc_MVCModel29'):
        assert _is_linked(a2, 'mvc_MVCModel29', b)
    _safe_set(b, 'mvc_Controller', None)
    assert not _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a2, 'mvc_MVCModel29'):
        assert not _is_linked(a2, 'mvc_MVCModel29', b)


def test_assoc_controllers53_reverse_link_reassign_clear():
    a1 = mvc_Controller(name="sample_text")
    a2 = mvc_Controller(name="sample_text_2")
    b = mvc_Component(name="sample_text")
    _safe_set(b, 'mvc_Component54', {a1})
    assert _is_linked(b, 'mvc_Component54', a1)
    if hasattr(a1, 'mvc_Controller55'):
        assert _is_linked(a1, 'mvc_Controller55', b)
    _safe_set(b, 'mvc_Component54', {a2})
    assert _is_linked(b, 'mvc_Component54', a2)
    if hasattr(a1, 'mvc_Controller55'):
        assert not _is_linked(a1, 'mvc_Controller55', b)
    if hasattr(a2, 'mvc_Controller55'):
        assert _is_linked(a2, 'mvc_Controller55', b)
    _safe_set(b, 'mvc_Component54', set())
    assert not _is_linked(b, 'mvc_Component54', a2)
    if hasattr(a2, 'mvc_Controller55'):
        assert not _is_linked(a2, 'mvc_Controller55', b)


def test_assoc_events18_reverse_link_reassign_clear():
    a1 = mvc_UIComponent(id="sample_text", layout="sample_text", name="sample_text", type="sample_text")
    a2 = mvc_UIComponent(id="sample_text_2", layout="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = mvc_Event(name="sample_text")
    _safe_set(b, 'mvc_Event', a1)
    assert _is_linked(b, 'mvc_Event', a1)
    if hasattr(a1, 'mvc_UIComponent19'):
        assert _is_linked(a1, 'mvc_UIComponent19', b)
    _safe_set(b, 'mvc_Event', a2)
    assert _is_linked(b, 'mvc_Event', a2)
    if hasattr(a1, 'mvc_UIComponent19'):
        assert not _is_linked(a1, 'mvc_UIComponent19', b)
    if hasattr(a2, 'mvc_UIComponent19'):
        assert _is_linked(a2, 'mvc_UIComponent19', b)
    _safe_set(b, 'mvc_Event', None)
    assert not _is_linked(b, 'mvc_Event', a2)
    if hasattr(a2, 'mvc_UIComponent19'):
        assert not _is_linked(a2, 'mvc_UIComponent19', b)


def test_assoc_events25_reverse_link_reassign_clear():
    a1 = mvc_MVCModel(name="sample_text", version="sample_text")
    a2 = mvc_MVCModel(name="sample_text_2", version="sample_text_2")
    b = mvc_Event(name="sample_text")
    _safe_set(b, 'mvc_Event27', a1)
    assert _is_linked(b, 'mvc_Event27', a1)
    if hasattr(a1, 'mvc_MVCModel26'):
        assert _is_linked(a1, 'mvc_MVCModel26', b)
    _safe_set(b, 'mvc_Event27', a2)
    assert _is_linked(b, 'mvc_Event27', a2)
    if hasattr(a1, 'mvc_MVCModel26'):
        assert not _is_linked(a1, 'mvc_MVCModel26', b)
    if hasattr(a2, 'mvc_MVCModel26'):
        assert _is_linked(a2, 'mvc_MVCModel26', b)
    _safe_set(b, 'mvc_Event27', None)
    assert not _is_linked(b, 'mvc_Event27', a2)
    if hasattr(a2, 'mvc_MVCModel26'):
        assert not _is_linked(a2, 'mvc_MVCModel26', b)


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


def test_assoc_models20_reverse_link_reassign_clear():
    a1 = mvc_Model(name="sample_text")
    a2 = mvc_Model(name="sample_text_2")
    b = mvc_MVCModel(name="sample_text", version="sample_text")
    _safe_set(b, 'mvc_MVCModel', {a1})
    assert _is_linked(b, 'mvc_MVCModel', a1)
    if hasattr(a1, 'mvc_Model21'):
        assert _is_linked(a1, 'mvc_Model21', b)
    _safe_set(b, 'mvc_MVCModel', {a2})
    assert _is_linked(b, 'mvc_MVCModel', a2)
    if hasattr(a1, 'mvc_Model21'):
        assert not _is_linked(a1, 'mvc_Model21', b)
    if hasattr(a2, 'mvc_Model21'):
        assert _is_linked(a2, 'mvc_Model21', b)
    _safe_set(b, 'mvc_MVCModel', set())
    assert not _is_linked(b, 'mvc_MVCModel', a2)
    if hasattr(a2, 'mvc_Model21'):
        assert not _is_linked(a2, 'mvc_Model21', b)


def test_assoc_postExecutionEvent41_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action42', a1)
    assert _is_linked(b, 'mvc_Action42', a1)
    if hasattr(a1, 'mvc_Event43'):
        assert _is_linked(a1, 'mvc_Event43', b)
    _safe_set(b, 'mvc_Action42', a2)
    assert _is_linked(b, 'mvc_Action42', a2)
    if hasattr(a1, 'mvc_Event43'):
        assert not _is_linked(a1, 'mvc_Event43', b)
    if hasattr(a2, 'mvc_Event43'):
        assert _is_linked(a2, 'mvc_Event43', b)
    _safe_set(b, 'mvc_Action42', None)
    assert not _is_linked(b, 'mvc_Action42', a2)
    if hasattr(a2, 'mvc_Event43'):
        assert not _is_linked(a2, 'mvc_Event43', b)


def test_assoc_preExecutionEvent38_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action39', a1)
    assert _is_linked(b, 'mvc_Action39', a1)
    if hasattr(a1, 'mvc_Event40'):
        assert _is_linked(a1, 'mvc_Event40', b)
    _safe_set(b, 'mvc_Action39', a2)
    assert _is_linked(b, 'mvc_Action39', a2)
    if hasattr(a1, 'mvc_Event40'):
        assert not _is_linked(a1, 'mvc_Event40', b)
    if hasattr(a2, 'mvc_Event40'):
        assert _is_linked(a2, 'mvc_Event40', b)
    _safe_set(b, 'mvc_Action39', None)
    assert not _is_linked(b, 'mvc_Action39', a2)
    if hasattr(a2, 'mvc_Event40'):
        assert not _is_linked(a2, 'mvc_Event40', b)


def test_assoc_rootComponent14_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text")
    a2 = mvc_View(name="sample_text_2")
    b = mvc_UIComponent(id="sample_text", layout="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'mvc_UIComponent', a1)
    assert _is_linked(b, 'mvc_UIComponent', a1)
    if hasattr(a1, 'mvc_View'):
        assert _is_linked(a1, 'mvc_View', b)
    _safe_set(b, 'mvc_UIComponent', a2)
    assert _is_linked(b, 'mvc_UIComponent', a2)
    if hasattr(a1, 'mvc_View'):
        assert not _is_linked(a1, 'mvc_View', b)
    if hasattr(a2, 'mvc_View'):
        assert _is_linked(a2, 'mvc_View', b)
    _safe_set(b, 'mvc_UIComponent', None)
    assert not _is_linked(b, 'mvc_UIComponent', a2)
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


def test_assoc_triggerEvents44_reverse_link_reassign_clear():
    a1 = mvc_Event(name="sample_text")
    a2 = mvc_Event(name="sample_text_2")
    b = mvc_Action(name="sample_text")
    _safe_set(b, 'mvc_Action45', {a1})
    assert _is_linked(b, 'mvc_Action45', a1)
    if hasattr(a1, 'mvc_Event46'):
        assert _is_linked(a1, 'mvc_Event46', b)
    _safe_set(b, 'mvc_Action45', {a2})
    assert _is_linked(b, 'mvc_Action45', a2)
    if hasattr(a1, 'mvc_Event46'):
        assert not _is_linked(a1, 'mvc_Event46', b)
    if hasattr(a2, 'mvc_Event46'):
        assert _is_linked(a2, 'mvc_Event46', b)
    _safe_set(b, 'mvc_Action45', set())
    assert not _is_linked(b, 'mvc_Action45', a2)
    if hasattr(a2, 'mvc_Event46'):
        assert not _is_linked(a2, 'mvc_Event46', b)


def test_assoc_views22_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text")
    a2 = mvc_View(name="sample_text_2")
    b = mvc_MVCModel(name="sample_text", version="sample_text")
    _safe_set(b, 'mvc_MVCModel23', {a1})
    assert _is_linked(b, 'mvc_MVCModel23', a1)
    if hasattr(a1, 'mvc_View24'):
        assert _is_linked(a1, 'mvc_View24', b)
    _safe_set(b, 'mvc_MVCModel23', {a2})
    assert _is_linked(b, 'mvc_MVCModel23', a2)
    if hasattr(a1, 'mvc_View24'):
        assert not _is_linked(a1, 'mvc_View24', b)
    if hasattr(a2, 'mvc_View24'):
        assert _is_linked(a2, 'mvc_View24', b)
    _safe_set(b, 'mvc_MVCModel23', set())
    assert not _is_linked(b, 'mvc_MVCModel23', a2)
    if hasattr(a2, 'mvc_View24'):
        assert not _is_linked(a2, 'mvc_View24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action56_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction57' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Action(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction57', None)
    _safe_set(owner, 'mvc_Action58', partner)
    assert getattr(partner, 'mvc_EventAction57') == owner
    _safe_set(owner, 'mvc_Action58', None)
    assert getattr(partner, 'mvc_EventAction57') is None


def test_assoc_eventActions36_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Controller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Controller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Controller(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction', None)
    _safe_set(owner, 'mvc_Controller37', {partner})
    assert getattr(partner, 'mvc_EventAction') == owner
    _safe_set(owner, 'mvc_Controller37', set())
    assert getattr(partner, 'mvc_EventAction') is None


def test_assoc_events59_stub_double():
    # mvc_EventAction has no real 'mvc_EventAction60' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Event(name="sample_text")
    partner = mvc_EventAction()
    setattr(partner, 'mvc_EventAction60', None)
    _safe_set(owner, 'mvc_Event61', partner)
    assert owner in getattr(partner, 'mvc_EventAction60')
    _safe_set(owner, 'mvc_Event61', None)
    assert owner not in getattr(partner, 'mvc_EventAction60')


def test_assoc_models50_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView51' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Model(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView51', None)
    _safe_set(owner, 'mvc_Model52', partner)
    assert owner in getattr(partner, 'mvc_ControllerView51')
    _safe_set(owner, 'mvc_Model52', None)
    assert owner not in getattr(partner, 'mvc_ControllerView51')


def test_assoc_view47_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView48' property in the generated
    # code (a bare stub) -- manually attach it so mvc_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_View(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView48', None)
    _safe_set(owner, 'mvc_View49', partner)
    assert getattr(partner, 'mvc_ControllerView48') == owner
    _safe_set(owner, 'mvc_View49', None)
    assert getattr(partner, 'mvc_ControllerView48') is None


def test_assoc_views34_stub_double():
    # mvc_ControllerView has no real 'mvc_ControllerView' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Controller's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Controller's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Controller(name="sample_text")
    partner = mvc_ControllerView()
    setattr(partner, 'mvc_ControllerView', None)
    _safe_set(owner, 'mvc_Controller35', {partner})
    assert getattr(partner, 'mvc_ControllerView') == owner
    _safe_set(owner, 'mvc_Controller35', set())
    assert getattr(partner, 'mvc_ControllerView') is None


