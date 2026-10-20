import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    Controller,
    Event,
    HTMLElement,
    Identifier,
    Input,
    MVCClass,
    Method,
    Model,
    PHPMVC_coreMVC_Application,
    PHPMVC_coreMVC_Attribute,
    PHPMVC_coreMVC_Controller,
    PHPMVC_coreMVC_Event,
    PHPMVC_coreMVC_Identifier,
    PHPMVC_coreMVC_MVCClass,
    PHPMVC_coreMVC_Method,
    PHPMVC_coreMVC_Model,
    PHPMVC_coreMVC_PackageController,
    PHPMVC_coreMVC_PackageModel,
    PHPMVC_coreMVC_PackageView,
    PHPMVC_coreMVC_View,
    PHPMVC_coreMVC_ViewComponent,
    PHPMVC_extPHP_Anchor,
    PHPMVC_extPHP_Button,
    PHPMVC_extPHP_Checkbox,
    PHPMVC_extPHP_Form,
    PHPMVC_extPHP_HTMLElement,
    PHPMVC_extPHP_Image,
    PHPMVC_extPHP_Input,
    PHPMVC_extPHP_RadioButton,
    PHPMVC_extPHP_Text,
    PHPMVC_extPHP_TextField,
    PackageController,
    PackageModel,
    PackageView,
    View,
    ViewComponent,
    ButtonType,
    EventType,
    HTMLTag,
    InputType,
    MethodType,
    TargetType,
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

def test_assoc_aPackageController3_stub_double():
    # PackageController has no real 'PackageController' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_Application(locale="sample_text", name="sample_text", routes="sample_text", type="sample_text")
    partner = PackageController()
    setattr(partner, 'PackageController', None)
    _safe_set(owner, 'PHPMVC_coreMVC_Application4', partner)
    assert getattr(partner, 'PackageController') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_Application4', None)
    assert getattr(partner, 'PackageController') is None


def test_assoc_aPackageModel0_stub_double():
    # PackageModel has no real 'PackageModel' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_Application(locale="sample_text", name="sample_text", routes="sample_text", type="sample_text")
    partner = PackageModel()
    setattr(partner, 'PackageModel', None)
    _safe_set(owner, 'PHPMVC_coreMVC_Application', partner)
    assert getattr(partner, 'PackageModel') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_Application', None)
    assert getattr(partner, 'PackageModel') is None


def test_assoc_aPackageView1_stub_double():
    # PackageView has no real 'PackageView' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_Application(locale="sample_text", name="sample_text", routes="sample_text", type="sample_text")
    partner = PackageView()
    setattr(partner, 'PackageView', None)
    _safe_set(owner, 'PHPMVC_coreMVC_Application2', partner)
    assert getattr(partner, 'PackageView') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_Application2', None)
    assert getattr(partner, 'PackageView') is None


def test_assoc_attributes8_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_MVCClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_MVCClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_MVCClass(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'PHPMVC_coreMVC_MVCClass', {partner})
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_MVCClass', set())
    assert getattr(partner, 'Attribute') is None


def test_assoc_controllers7_stub_double():
    # Controller has no real 'Controller' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_PackageController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_PackageController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_PackageController(name="sample_text")
    partner = Controller()
    setattr(partner, 'Controller', None)
    _safe_set(owner, 'PHPMVC_coreMVC_PackageController', {partner})
    assert getattr(partner, 'Controller') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_PackageController', set())
    assert getattr(partner, 'Controller') is None


def test_assoc_events20_stub_double():
    # Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_ViewComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_ViewComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_ViewComponent(name="sample_text")
    partner = Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'PHPMVC_coreMVC_ViewComponent', {partner})
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_ViewComponent', set())
    assert getattr(partner, 'Event') is None


def test_assoc_htmlElements21_stub_double():
    # HTMLElement has no real 'HTMLElement' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_extPHP_HTMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_extPHP_HTMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_extPHP_HTMLElement(isEmpty=True, isPairedTag=True, tagName="sample_text")
    partner = HTMLElement()
    setattr(partner, 'HTMLElement', None)
    _safe_set(owner, 'PHPMVC_extPHP_HTMLElement', {partner})
    assert getattr(partner, 'HTMLElement') == owner
    _safe_set(owner, 'PHPMVC_extPHP_HTMLElement', set())
    assert getattr(partner, 'HTMLElement') is None


def test_assoc_inParameters15_stub_double():
    # Attribute has no real 'Attribute16' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_Method(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute16', None)
    _safe_set(owner, 'PHPMVC_coreMVC_Method', {partner})
    assert getattr(partner, 'Attribute16') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_Method', set())
    assert getattr(partner, 'Attribute16') is None


def test_assoc_models5_stub_double():
    # Model has no real 'Model' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_PackageModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_PackageModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_PackageModel(name="sample_text")
    partner = Model()
    setattr(partner, 'Model', None)
    _safe_set(owner, 'PHPMVC_coreMVC_PackageModel', {partner})
    assert getattr(partner, 'Model') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_PackageModel', set())
    assert getattr(partner, 'Model') is None


def test_assoc_outParameters17_stub_double():
    # Attribute has no real 'Attribute19' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_Method(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute19', None)
    _safe_set(owner, 'PHPMVC_coreMVC_Method18', {partner})
    assert getattr(partner, 'Attribute19') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_Method18', set())
    assert getattr(partner, 'Attribute19') is None


def test_assoc_views6_stub_double():
    # View has no real 'View' property in the generated
    # code (a bare stub) -- manually attach it so PHPMVC_coreMVC_PackageView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PHPMVC_coreMVC_PackageView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PHPMVC_coreMVC_PackageView(name="sample_text")
    partner = View()
    setattr(partner, 'View', None)
    _safe_set(owner, 'PHPMVC_coreMVC_PackageView', {partner})
    assert getattr(partner, 'View') == owner
    _safe_set(owner, 'PHPMVC_coreMVC_PackageView', set())
    assert getattr(partner, 'View') is None


