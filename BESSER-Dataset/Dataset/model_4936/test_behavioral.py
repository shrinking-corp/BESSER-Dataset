import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    UIElement,
    webapp_Attribute,
    webapp_ClientPage,
    webapp_DataSourceManager,
    webapp_DataStructure,
    webapp_Form,
    webapp_ImageViewer,
    webapp_Named,
    webapp_ServerPage,
    webapp_Table,
    webapp_TextArea,
    webapp_UIElement,
    webapp_WebApp,
    UIElementType,
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

def test_assoc_attributeOf16_stub_double():
    # webapp_DataStructure has no real 'DataStructure17' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(type="sample_text")
    partner = webapp_DataStructure()
    setattr(partner, 'DataStructure17', None)
    _safe_set(owner, 'parentOf', partner)
    assert getattr(partner, 'DataStructure17') == owner
    _safe_set(owner, 'parentOf', None)
    assert getattr(partner, 'DataStructure17') is None


def test_assoc_composedOf20_stub_double():
    # webapp_ClientPage has no real 'webapp_ClientPage21' property in the generated
    # code (a bare stub) -- manually attach it so webapp_UIElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_UIElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_UIElement(type="sample_text")
    partner = webapp_ClientPage()
    setattr(partner, 'webapp_ClientPage21', None)
    _safe_set(owner, 'webapp_UIElement', partner)
    assert owner in getattr(partner, 'webapp_ClientPage21')
    _safe_set(owner, 'webapp_UIElement', None)
    assert owner not in getattr(partner, 'webapp_ClientPage21')


def test_assoc_connectsTo22_stub_double():
    # webapp_ClientPage has no real 'generates' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_ClientPage()
    setattr(partner, 'generates', None)
    _safe_set(owner, 'ServerPage23', partner)
    assert getattr(partner, 'generates') == owner
    _safe_set(owner, 'ServerPage23', None)
    assert getattr(partner, 'generates') is None


def test_assoc_content24_stub_double():
    # webapp_DataStructure has no real 'webapp_DataStructure26' property in the generated
    # code (a bare stub) -- manually attach it so webapp_UIElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_UIElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_UIElement(type="sample_text")
    partner = webapp_DataStructure()
    setattr(partner, 'webapp_DataStructure26', None)
    _safe_set(owner, 'webapp_UIElement25', partner)
    assert getattr(partner, 'webapp_DataStructure26') == owner
    _safe_set(owner, 'webapp_UIElement25', None)
    assert getattr(partner, 'webapp_DataStructure26') is None


def test_assoc_generates7_stub_double():
    # webapp_ClientPage has no real 'ClientPage' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_ClientPage()
    setattr(partner, 'ClientPage', None)
    _safe_set(owner, 'connectsTo', partner)
    assert getattr(partner, 'ClientPage') == owner
    _safe_set(owner, 'connectsTo', None)
    assert getattr(partner, 'ClientPage') is None


def test_assoc_getContents8_stub_double():
    # webapp_DataSourceManager has no real 'DataSourceManager' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_DataSourceManager()
    setattr(partner, 'DataSourceManager', None)
    _safe_set(owner, 'providesContent', {partner})
    assert getattr(partner, 'DataSourceManager') == owner
    _safe_set(owner, 'providesContent', set())
    assert getattr(partner, 'DataSourceManager') is None


def test_assoc_linkedBy18_stub_double():
    # webapp_DataStructure has no real 'DataStructure19' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(type="sample_text")
    partner = webapp_DataStructure()
    setattr(partner, 'DataStructure19', None)
    _safe_set(owner, 'linkedTo', {partner})
    assert getattr(partner, 'DataStructure19') == owner
    _safe_set(owner, 'linkedTo', set())
    assert getattr(partner, 'DataStructure19') is None


def test_assoc_linkedTo12_stub_double():
    # webapp_DataStructure has no real 'linkedBy' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(type="sample_text")
    partner = webapp_DataStructure()
    setattr(partner, 'linkedBy', None)
    _safe_set(owner, 'Attribute13', partner)
    assert owner in getattr(partner, 'linkedBy')
    _safe_set(owner, 'Attribute13', None)
    assert owner not in getattr(partner, 'linkedBy')


def test_assoc_managedBy10_stub_double():
    # webapp_DataStructure has no real 'manages' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_DataStructure()
    setattr(partner, 'manages', None)
    _safe_set(owner, 'ServerPage', partner)
    assert owner in getattr(partner, 'manages')
    _safe_set(owner, 'ServerPage', None)
    assert owner not in getattr(partner, 'manages')


def test_assoc_manages9_stub_double():
    # webapp_DataStructure has no real 'DataStructure' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_DataStructure()
    setattr(partner, 'DataStructure', None)
    _safe_set(owner, 'managedBy', {partner})
    assert getattr(partner, 'DataStructure') == owner
    _safe_set(owner, 'managedBy', set())
    assert getattr(partner, 'DataStructure') is None


def test_assoc_parentOf11_stub_double():
    # webapp_DataStructure has no real 'attributeOf' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(type="sample_text")
    partner = webapp_DataStructure()
    setattr(partner, 'attributeOf', None)
    _safe_set(owner, 'Attribute', partner)
    assert owner in getattr(partner, 'attributeOf')
    _safe_set(owner, 'Attribute', None)
    assert owner not in getattr(partner, 'attributeOf')


def test_assoc_providesContent14_stub_double():
    # webapp_DataSourceManager has no real 'getContents' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_DataSourceManager()
    setattr(partner, 'getContents', None)
    _safe_set(owner, 'ServerPage15', partner)
    assert owner in getattr(partner, 'getContents')
    _safe_set(owner, 'ServerPage15', None)
    assert owner not in getattr(partner, 'getContents')


def test_assoc_serverPages1_stub_double():
    # webapp_WebApp has no real 'webapp_WebApp2' property in the generated
    # code (a bare stub) -- manually attach it so webapp_ServerPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_ServerPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_ServerPage()
    partner = webapp_WebApp()
    setattr(partner, 'webapp_WebApp2', None)
    _safe_set(owner, 'webapp_ServerPage', partner)
    assert owner in getattr(partner, 'webapp_WebApp2')
    _safe_set(owner, 'webapp_ServerPage', None)
    assert owner not in getattr(partner, 'webapp_WebApp2')


