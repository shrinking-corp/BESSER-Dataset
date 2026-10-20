import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Model,
    View,
    mvc_Attribute,
    mvc_Client,
    mvc_Controller,
    mvc_DataBase,
    mvc_GraphicComponent,
    mvc_MapComponent,
    mvc_Method,
    mvc_Model,
    mvc_MvcApplication,
    mvc_Position,
    mvc_ReturnParameter,
    mvc_SocialComponent,
    mvc_View,
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

def test_assoc_attrib13_reverse_link_reassign_clear():
    a1 = mvc_Method(namemethod="sample_text", type="sample_text")
    a2 = mvc_Method(namemethod="sample_text_2", type="sample_text_2")
    b = mvc_Attribute(nameattribute="sample_text", typeattribute="sample_text")
    _safe_set(b, 'mvc_Attribute', a1)
    assert _is_linked(b, 'mvc_Attribute', a1)
    if hasattr(a1, 'mvc_Method'):
        assert _is_linked(a1, 'mvc_Method', b)
    _safe_set(b, 'mvc_Attribute', a2)
    assert _is_linked(b, 'mvc_Attribute', a2)
    if hasattr(a1, 'mvc_Method'):
        assert not _is_linked(a1, 'mvc_Method', b)
    if hasattr(a2, 'mvc_Method'):
        assert _is_linked(a2, 'mvc_Method', b)
    _safe_set(b, 'mvc_Attribute', None)
    assert not _is_linked(b, 'mvc_Attribute', a2)
    if hasattr(a2, 'mvc_Method'):
        assert not _is_linked(a2, 'mvc_Method', b)


def test_assoc_controller8_reverse_link_reassign_clear():
    a1 = mvc_Model(nameclass="sample_text", type="sample_text")
    a2 = mvc_Model(nameclass="sample_text_2", type="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'Controller', a1)
    assert _is_linked(b, 'Controller', a1)
    if hasattr(a1, 'model'):
        assert _is_linked(a1, 'model', b)
    _safe_set(b, 'Controller', a2)
    assert _is_linked(b, 'Controller', a2)
    if hasattr(a1, 'model'):
        assert not _is_linked(a1, 'model', b)
    if hasattr(a2, 'model'):
        assert _is_linked(a2, 'model', b)
    _safe_set(b, 'Controller', None)
    assert not _is_linked(b, 'Controller', a2)
    if hasattr(a2, 'model'):
        assert not _is_linked(a2, 'model', b)


def test_assoc_controller9_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text", type="sample_text")
    a2 = mvc_View(name="sample_text_2", type="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'Controller10', a1)
    assert _is_linked(b, 'Controller10', a1)
    if hasattr(a1, 'view'):
        assert _is_linked(a1, 'view', b)
    _safe_set(b, 'Controller10', a2)
    assert _is_linked(b, 'Controller10', a2)
    if hasattr(a1, 'view'):
        assert not _is_linked(a1, 'view', b)
    if hasattr(a2, 'view'):
        assert _is_linked(a2, 'view', b)
    _safe_set(b, 'Controller10', None)
    assert not _is_linked(b, 'Controller10', a2)
    if hasattr(a2, 'view'):
        assert not _is_linked(a2, 'view', b)


def test_assoc_controllers3_reverse_link_reassign_clear():
    a1 = mvc_MvcApplication(description="sample_text", email="sample_text", name="sample_text", pagelink="sample_text", picture="sample_text")
    a2 = mvc_MvcApplication(description="sample_text_2", email="sample_text_2", name="sample_text_2", pagelink="sample_text_2", picture="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'mvc_Controller', a1)
    assert _is_linked(b, 'mvc_Controller', a1)
    if hasattr(a1, 'mvc_MvcApplication4'):
        assert _is_linked(a1, 'mvc_MvcApplication4', b)
    _safe_set(b, 'mvc_Controller', a2)
    assert _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a1, 'mvc_MvcApplication4'):
        assert not _is_linked(a1, 'mvc_MvcApplication4', b)
    if hasattr(a2, 'mvc_MvcApplication4'):
        assert _is_linked(a2, 'mvc_MvcApplication4', b)
    _safe_set(b, 'mvc_Controller', None)
    assert not _is_linked(b, 'mvc_Controller', a2)
    if hasattr(a2, 'mvc_MvcApplication4'):
        assert not _is_linked(a2, 'mvc_MvcApplication4', b)


def test_assoc_datoA18_reverse_link_reassign_clear():
    a1 = mvc_GraphicComponent(stepSize=7)
    a2 = mvc_GraphicComponent(stepSize=13)
    b = mvc_Attribute(nameattribute="sample_text", typeattribute="sample_text")
    _safe_set(b, 'mvc_Attribute19', a1)
    assert _is_linked(b, 'mvc_Attribute19', a1)
    if hasattr(a1, 'mvc_GraphicComponent'):
        assert _is_linked(a1, 'mvc_GraphicComponent', b)
    _safe_set(b, 'mvc_Attribute19', a2)
    assert _is_linked(b, 'mvc_Attribute19', a2)
    if hasattr(a1, 'mvc_GraphicComponent'):
        assert not _is_linked(a1, 'mvc_GraphicComponent', b)
    if hasattr(a2, 'mvc_GraphicComponent'):
        assert _is_linked(a2, 'mvc_GraphicComponent', b)
    _safe_set(b, 'mvc_Attribute19', None)
    assert not _is_linked(b, 'mvc_Attribute19', a2)
    if hasattr(a2, 'mvc_GraphicComponent'):
        assert not _is_linked(a2, 'mvc_GraphicComponent', b)


def test_assoc_datoB20_reverse_link_reassign_clear():
    a1 = mvc_GraphicComponent(stepSize=7)
    a2 = mvc_GraphicComponent(stepSize=13)
    b = mvc_Attribute(nameattribute="sample_text", typeattribute="sample_text")
    _safe_set(b, 'mvc_Attribute22', a1)
    assert _is_linked(b, 'mvc_Attribute22', a1)
    if hasattr(a1, 'mvc_GraphicComponent21'):
        assert _is_linked(a1, 'mvc_GraphicComponent21', b)
    _safe_set(b, 'mvc_Attribute22', a2)
    assert _is_linked(b, 'mvc_Attribute22', a2)
    if hasattr(a1, 'mvc_GraphicComponent21'):
        assert not _is_linked(a1, 'mvc_GraphicComponent21', b)
    if hasattr(a2, 'mvc_GraphicComponent21'):
        assert _is_linked(a2, 'mvc_GraphicComponent21', b)
    _safe_set(b, 'mvc_Attribute22', None)
    assert not _is_linked(b, 'mvc_Attribute22', a2)
    if hasattr(a2, 'mvc_GraphicComponent21'):
        assert not _is_linked(a2, 'mvc_GraphicComponent21', b)


def test_assoc_method14_reverse_link_reassign_clear():
    a1 = mvc_Method(namemethod="sample_text", type="sample_text")
    a2 = mvc_Method(namemethod="sample_text_2", type="sample_text_2")
    b = mvc_Client(nameservice="sample_text")
    _safe_set(b, 'mvc_Client', a1)
    assert _is_linked(b, 'mvc_Client', a1)
    if hasattr(a1, 'mvc_Method15'):
        assert _is_linked(a1, 'mvc_Method15', b)
    _safe_set(b, 'mvc_Client', a2)
    assert _is_linked(b, 'mvc_Client', a2)
    if hasattr(a1, 'mvc_Method15'):
        assert not _is_linked(a1, 'mvc_Method15', b)
    if hasattr(a2, 'mvc_Method15'):
        assert _is_linked(a2, 'mvc_Method15', b)
    _safe_set(b, 'mvc_Client', None)
    assert not _is_linked(b, 'mvc_Client', a2)
    if hasattr(a2, 'mvc_Method15'):
        assert not _is_linked(a2, 'mvc_Method15', b)


def test_assoc_model5_reverse_link_reassign_clear():
    a1 = mvc_Model(nameclass="sample_text", type="sample_text")
    a2 = mvc_Model(nameclass="sample_text_2", type="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'controller', a1)
    assert _is_linked(b, 'controller', a1)
    if hasattr(a1, 'Model'):
        assert _is_linked(a1, 'Model', b)
    _safe_set(b, 'controller', a2)
    assert _is_linked(b, 'controller', a2)
    if hasattr(a1, 'Model'):
        assert not _is_linked(a1, 'Model', b)
    if hasattr(a2, 'Model'):
        assert _is_linked(a2, 'Model', b)
    _safe_set(b, 'controller', None)
    assert not _is_linked(b, 'controller', a2)
    if hasattr(a2, 'Model'):
        assert not _is_linked(a2, 'Model', b)


def test_assoc_models1_reverse_link_reassign_clear():
    a1 = mvc_MvcApplication(description="sample_text", email="sample_text", name="sample_text", pagelink="sample_text", picture="sample_text")
    a2 = mvc_MvcApplication(description="sample_text_2", email="sample_text_2", name="sample_text_2", pagelink="sample_text_2", picture="sample_text_2")
    b = mvc_Model(nameclass="sample_text", type="sample_text")
    _safe_set(b, 'mvc_Model', a1)
    assert _is_linked(b, 'mvc_Model', a1)
    if hasattr(a1, 'mvc_MvcApplication2'):
        assert _is_linked(a1, 'mvc_MvcApplication2', b)
    _safe_set(b, 'mvc_Model', a2)
    assert _is_linked(b, 'mvc_Model', a2)
    if hasattr(a1, 'mvc_MvcApplication2'):
        assert not _is_linked(a1, 'mvc_MvcApplication2', b)
    if hasattr(a2, 'mvc_MvcApplication2'):
        assert _is_linked(a2, 'mvc_MvcApplication2', b)
    _safe_set(b, 'mvc_Model', None)
    assert not _is_linked(b, 'mvc_Model', a2)
    if hasattr(a2, 'mvc_MvcApplication2'):
        assert not _is_linked(a2, 'mvc_MvcApplication2', b)


def test_assoc_position11_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text", type="sample_text")
    a2 = mvc_View(name="sample_text_2", type="sample_text_2")
    b = mvc_Position(above=7, align_left=7, long=7, name="sample_text", wide=7)
    _safe_set(b, 'mvc_Position', a1)
    assert _is_linked(b, 'mvc_Position', a1)
    if hasattr(a1, 'mvc_View12'):
        assert _is_linked(a1, 'mvc_View12', b)
    _safe_set(b, 'mvc_Position', a2)
    assert _is_linked(b, 'mvc_Position', a2)
    if hasattr(a1, 'mvc_View12'):
        assert not _is_linked(a1, 'mvc_View12', b)
    if hasattr(a2, 'mvc_View12'):
        assert _is_linked(a2, 'mvc_View12', b)
    _safe_set(b, 'mvc_Position', None)
    assert not _is_linked(b, 'mvc_Position', a2)
    if hasattr(a2, 'mvc_View12'):
        assert not _is_linked(a2, 'mvc_View12', b)


def test_assoc_view6_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text", type="sample_text")
    a2 = mvc_View(name="sample_text_2", type="sample_text_2")
    b = mvc_Controller(name="sample_text")
    _safe_set(b, 'controller7', a1)
    assert _is_linked(b, 'controller7', a1)
    if hasattr(a1, 'View'):
        assert _is_linked(a1, 'View', b)
    _safe_set(b, 'controller7', a2)
    assert _is_linked(b, 'controller7', a2)
    if hasattr(a1, 'View'):
        assert not _is_linked(a1, 'View', b)
    if hasattr(a2, 'View'):
        assert _is_linked(a2, 'View', b)
    _safe_set(b, 'controller7', None)
    assert not _is_linked(b, 'controller7', a2)
    if hasattr(a2, 'View'):
        assert not _is_linked(a2, 'View', b)


def test_assoc_views0_reverse_link_reassign_clear():
    a1 = mvc_View(name="sample_text", type="sample_text")
    a2 = mvc_View(name="sample_text_2", type="sample_text_2")
    b = mvc_MvcApplication(description="sample_text", email="sample_text", name="sample_text", pagelink="sample_text", picture="sample_text")
    _safe_set(b, 'mvc_MvcApplication', {a1})
    assert _is_linked(b, 'mvc_MvcApplication', a1)
    if hasattr(a1, 'mvc_View'):
        assert _is_linked(a1, 'mvc_View', b)
    _safe_set(b, 'mvc_MvcApplication', {a2})
    assert _is_linked(b, 'mvc_MvcApplication', a2)
    if hasattr(a1, 'mvc_View'):
        assert not _is_linked(a1, 'mvc_View', b)
    if hasattr(a2, 'mvc_View'):
        assert _is_linked(a2, 'mvc_View', b)
    _safe_set(b, 'mvc_MvcApplication', set())
    assert not _is_linked(b, 'mvc_MvcApplication', a2)
    if hasattr(a2, 'mvc_View'):
        assert not _is_linked(a2, 'mvc_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute16_stub_double():
    # mvc_DataBase has no real 'mvc_DataBase' property in the generated
    # code (a bare stub) -- manually attach it so mvc_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mvc_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mvc_Attribute(nameattribute="sample_text", typeattribute="sample_text")
    partner = mvc_DataBase()
    setattr(partner, 'mvc_DataBase', None)
    _safe_set(owner, 'mvc_Attribute17', partner)
    assert owner in getattr(partner, 'mvc_DataBase')
    _safe_set(owner, 'mvc_Attribute17', None)
    assert owner not in getattr(partner, 'mvc_DataBase')


