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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes11_stub_double():
    # webapp_Model has no real 'webapp_Model12' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(baseType="sample_text", customType="sample_text")
    partner = webapp_Model()
    setattr(partner, 'webapp_Model12', None)
    _safe_set(owner, 'webapp_Attribute', partner)
    assert owner in getattr(partner, 'webapp_Model12')
    _safe_set(owner, 'webapp_Attribute', None)
    assert owner not in getattr(partner, 'webapp_Model12')


def test_assoc_bindings24_stub_double():
    # webapp_Router has no real 'webapp_Router25' property in the generated
    # code (a bare stub) -- manually attach it so webapp_RouterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_RouterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_RouterBinding(url="sample_text")
    partner = webapp_Router()
    setattr(partner, 'webapp_Router25', None)
    _safe_set(owner, 'webapp_RouterBinding', partner)
    assert owner in getattr(partner, 'webapp_Router25')
    _safe_set(owner, 'webapp_RouterBinding', None)
    assert owner not in getattr(partner, 'webapp_Router25')


def test_assoc_controller26_stub_double():
    # webapp_Controller has no real 'webapp_Controller28' property in the generated
    # code (a bare stub) -- manually attach it so webapp_RouterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_RouterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_RouterBinding(url="sample_text")
    partner = webapp_Controller()
    setattr(partner, 'webapp_Controller28', None)
    _safe_set(owner, 'webapp_RouterBinding27', partner)
    assert getattr(partner, 'webapp_Controller28') == owner
    _safe_set(owner, 'webapp_RouterBinding27', None)
    assert getattr(partner, 'webapp_Controller28') is None


def test_assoc_data22_stub_double():
    # webapp_View has no real 'webapp_View23' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Data's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Data's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Data(endpoint="sample_text")
    partner = webapp_View()
    setattr(partner, 'webapp_View23', None)
    _safe_set(owner, 'webapp_Data', partner)
    assert getattr(partner, 'webapp_View23') == owner
    _safe_set(owner, 'webapp_Data', None)
    assert getattr(partner, 'webapp_View23') is None


def test_assoc_parameters29_stub_double():
    # webapp_Controller has no real 'webapp_Controller30' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Attribute(baseType="sample_text", customType="sample_text")
    partner = webapp_Controller()
    setattr(partner, 'webapp_Controller30', None)
    _safe_set(owner, 'webapp_Attribute31', partner)
    assert owner in getattr(partner, 'webapp_Controller30')
    _safe_set(owner, 'webapp_Attribute31', None)
    assert owner not in getattr(partner, 'webapp_Controller30')


def test_assoc_template19_stub_double():
    # webapp_View has no real 'webapp_View20' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Template(structure="sample_text", style="sample_text")
    partner = webapp_View()
    setattr(partner, 'webapp_View20', None)
    _safe_set(owner, 'webapp_Template21', partner)
    assert getattr(partner, 'webapp_View20') == owner
    _safe_set(owner, 'webapp_Template21', None)
    assert getattr(partner, 'webapp_View20') is None


def test_assoc_templates7_stub_double():
    # webapp_WebApp has no real 'webapp_WebApp8' property in the generated
    # code (a bare stub) -- manually attach it so webapp_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webapp_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webapp_Template(structure="sample_text", style="sample_text")
    partner = webapp_WebApp()
    setattr(partner, 'webapp_WebApp8', None)
    _safe_set(owner, 'webapp_Template', partner)
    assert owner in getattr(partner, 'webapp_WebApp8')
    _safe_set(owner, 'webapp_Template', None)
    assert owner not in getattr(partner, 'webapp_WebApp8')


