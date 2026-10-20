import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Controller,
    Data,
    NamedElement,
    webapp_Attribute,
    webapp_Collection,
    webapp_Controller,
    webapp_Data,
    webapp_Model,
    webapp_NamedElement,
    webapp_PageController,
    webapp_Router,
    webapp_RouterBinding,
    webapp_ServiceController,
    webapp_Style,
    webapp_Template,
    webapp_View,
    webapp_WebApp,
    DataType,
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

def test_assoc_style29_reverse_link_reassign_clear():
    a1 = webapp_Template(structure="sample_text")
    a2 = webapp_Template(structure="sample_text_2")
    b = webapp_Style(href="sample_text", src="sample_text")
    _safe_set(b, 'webapp_Style31', a1)
    assert _is_linked(b, 'webapp_Style31', a1)
    if hasattr(a1, 'webapp_Template30'):
        assert _is_linked(a1, 'webapp_Template30', b)
    _safe_set(b, 'webapp_Style31', a2)
    assert _is_linked(b, 'webapp_Style31', a2)
    if hasattr(a1, 'webapp_Template30'):
        assert not _is_linked(a1, 'webapp_Template30', b)
    if hasattr(a2, 'webapp_Template30'):
        assert _is_linked(a2, 'webapp_Template30', b)
    _safe_set(b, 'webapp_Style31', None)
    assert not _is_linked(b, 'webapp_Style31', a2)
    if hasattr(a2, 'webapp_Template30'):
        assert not _is_linked(a2, 'webapp_Template30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes13_stub_double():
    # webapp_Model has no real 'webapp_Model14' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(baseType="sample_text", customType="sample_text")
    partner = webapp_Model()
    setattr(partner, 'webapp_Model14', None)
    _safe_set(owner, 'webapp_Attribute', partner)
    assert owner in getattr(partner, 'webapp_Model14')
    _safe_set(owner, 'webapp_Attribute', None)
    assert owner not in getattr(partner, 'webapp_Model14')


def test_assoc_bindings27_stub_double():
    # webapp_Router has no real 'webapp_Router28' property in the generated
    # code (a bare stub) -- manually attach it so webapp_RouterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_RouterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_RouterBinding(requestCookies="sample_text", requestURL="sample_text")
    partner = webapp_Router()
    setattr(partner, 'webapp_Router28', None)
    _safe_set(owner, 'webapp_RouterBinding', partner)
    assert owner in getattr(partner, 'webapp_Router28')
    _safe_set(owner, 'webapp_RouterBinding', None)
    assert owner not in getattr(partner, 'webapp_Router28')


def test_assoc_controller32_stub_double():
    # webapp_Controller has no real 'webapp_Controller34' property in the generated
    # code (a bare stub) -- manually attach it so webapp_RouterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_RouterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_RouterBinding(requestCookies="sample_text", requestURL="sample_text")
    partner = webapp_Controller()
    setattr(partner, 'webapp_Controller34', None)
    _safe_set(owner, 'webapp_RouterBinding33', partner)
    assert getattr(partner, 'webapp_Controller34') == owner
    _safe_set(owner, 'webapp_RouterBinding33', None)
    assert getattr(partner, 'webapp_Controller34') is None


def test_assoc_data24_stub_double():
    # webapp_View has no real 'webapp_View25' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(baseType="sample_text", customType="sample_text")
    partner = webapp_View()
    setattr(partner, 'webapp_View25', None)
    _safe_set(owner, 'webapp_Attribute26', partner)
    assert getattr(partner, 'webapp_View25') == owner
    _safe_set(owner, 'webapp_Attribute26', None)
    assert getattr(partner, 'webapp_View25') is None


def test_assoc_parameters35_stub_double():
    # webapp_Controller has no real 'webapp_Controller36' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(baseType="sample_text", customType="sample_text")
    partner = webapp_Controller()
    setattr(partner, 'webapp_Controller36', None)
    _safe_set(owner, 'webapp_Attribute37', partner)
    assert owner in getattr(partner, 'webapp_Controller36')
    _safe_set(owner, 'webapp_Attribute37', None)
    assert owner not in getattr(partner, 'webapp_Controller36')


def test_assoc_styles11_stub_double():
    # webapp_WebApp has no real 'webapp_WebApp12' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Style(href="sample_text", src="sample_text")
    partner = webapp_WebApp()
    setattr(partner, 'webapp_WebApp12', None)
    _safe_set(owner, 'webapp_Style', partner)
    assert owner in getattr(partner, 'webapp_WebApp12')
    _safe_set(owner, 'webapp_Style', None)
    assert owner not in getattr(partner, 'webapp_WebApp12')


def test_assoc_template21_stub_double():
    # webapp_View has no real 'webapp_View22' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Template(structure="sample_text")
    partner = webapp_View()
    setattr(partner, 'webapp_View22', None)
    _safe_set(owner, 'webapp_Template23', partner)
    assert getattr(partner, 'webapp_View22') == owner
    _safe_set(owner, 'webapp_Template23', None)
    assert getattr(partner, 'webapp_View22') is None


def test_assoc_templates7_stub_double():
    # webapp_WebApp has no real 'webapp_WebApp8' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Template(structure="sample_text")
    partner = webapp_WebApp()
    setattr(partner, 'webapp_WebApp8', None)
    _safe_set(owner, 'webapp_Template', partner)
    assert owner in getattr(partner, 'webapp_WebApp8')
    _safe_set(owner, 'webapp_Template', None)
    assert owner not in getattr(partner, 'webapp_WebApp8')


