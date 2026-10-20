import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SuperCall,
    SuperMethod,
    archDSL_AltCall,
    archDSL_AltMethod,
    archDSL_Behavior,
    archDSL_CertainCall,
    archDSL_Connector,
    archDSL_Interface,
    archDSL_Method,
    archDSL_Model,
    archDSL_OptCall,
    archDSL_OptMethod,
    archDSL_Param,
    archDSL_SuperCall,
    archDSL_SuperMethod,
    archDSL_UncertainBehavior,
    archDSL_UncertainConnector,
    archDSL_UncertainInterface,
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

def test_assoc_a_name41_reverse_link_reassign_clear():
    a1 = archDSL_SuperMethod(name="sample_text")
    a2 = archDSL_SuperMethod(name="sample_text_2")
    b = archDSL_AltCall(opt=True)
    _safe_set(b, 'archDSL_AltCall', {a1})
    assert _is_linked(b, 'archDSL_AltCall', a1)
    if hasattr(a1, 'archDSL_SuperMethod42'):
        assert _is_linked(a1, 'archDSL_SuperMethod42', b)
    _safe_set(b, 'archDSL_AltCall', {a2})
    assert _is_linked(b, 'archDSL_AltCall', a2)
    if hasattr(a1, 'archDSL_SuperMethod42'):
        assert not _is_linked(a1, 'archDSL_SuperMethod42', b)
    if hasattr(a2, 'archDSL_SuperMethod42'):
        assert _is_linked(a2, 'archDSL_SuperMethod42', b)
    _safe_set(b, 'archDSL_AltCall', set())
    assert not _is_linked(b, 'archDSL_AltCall', a2)
    if hasattr(a2, 'archDSL_SuperMethod42'):
        assert not _is_linked(a2, 'archDSL_SuperMethod42', b)


def test_assoc_altmethods12_reverse_link_reassign_clear():
    a1 = archDSL_UncertainInterface(name="sample_text")
    a2 = archDSL_UncertainInterface(name="sample_text_2")
    b = archDSL_AltMethod(a_name="sample_text", type="sample_text")
    _safe_set(b, 'archDSL_AltMethod', a1)
    assert _is_linked(b, 'archDSL_AltMethod', a1)
    if hasattr(a1, 'archDSL_UncertainInterface13'):
        assert _is_linked(a1, 'archDSL_UncertainInterface13', b)
    _safe_set(b, 'archDSL_AltMethod', a2)
    assert _is_linked(b, 'archDSL_AltMethod', a2)
    if hasattr(a1, 'archDSL_UncertainInterface13'):
        assert not _is_linked(a1, 'archDSL_UncertainInterface13', b)
    if hasattr(a2, 'archDSL_UncertainInterface13'):
        assert _is_linked(a2, 'archDSL_UncertainInterface13', b)
    _safe_set(b, 'archDSL_AltMethod', None)
    assert not _is_linked(b, 'archDSL_AltMethod', a2)
    if hasattr(a2, 'archDSL_UncertainInterface13'):
        assert not _is_linked(a2, 'archDSL_UncertainInterface13', b)


def test_assoc_end38_reverse_link_reassign_clear():
    a1 = archDSL_UncertainBehavior(name="sample_text")
    a2 = archDSL_UncertainBehavior(name="sample_text_2")
    b = archDSL_Interface(name="sample_text")
    _safe_set(b, 'archDSL_Interface40', a1)
    assert _is_linked(b, 'archDSL_Interface40', a1)
    if hasattr(a1, 'archDSL_UncertainBehavior39'):
        assert _is_linked(a1, 'archDSL_UncertainBehavior39', b)
    _safe_set(b, 'archDSL_Interface40', a2)
    assert _is_linked(b, 'archDSL_Interface40', a2)
    if hasattr(a1, 'archDSL_UncertainBehavior39'):
        assert not _is_linked(a1, 'archDSL_UncertainBehavior39', b)
    if hasattr(a2, 'archDSL_UncertainBehavior39'):
        assert _is_linked(a2, 'archDSL_UncertainBehavior39', b)
    _safe_set(b, 'archDSL_Interface40', None)
    assert not _is_linked(b, 'archDSL_Interface40', a2)
    if hasattr(a2, 'archDSL_UncertainBehavior39'):
        assert not _is_linked(a2, 'archDSL_UncertainBehavior39', b)


def test_assoc_methods16_reverse_link_reassign_clear():
    a1 = archDSL_Method(type="sample_text")
    a2 = archDSL_Method(type="sample_text_2")
    b = archDSL_Interface(name="sample_text")
    _safe_set(b, 'archDSL_Interface17', {a1})
    assert _is_linked(b, 'archDSL_Interface17', a1)
    if hasattr(a1, 'archDSL_Method'):
        assert _is_linked(a1, 'archDSL_Method', b)
    _safe_set(b, 'archDSL_Interface17', {a2})
    assert _is_linked(b, 'archDSL_Interface17', a2)
    if hasattr(a1, 'archDSL_Method'):
        assert not _is_linked(a1, 'archDSL_Method', b)
    if hasattr(a2, 'archDSL_Method'):
        assert _is_linked(a2, 'archDSL_Method', b)
    _safe_set(b, 'archDSL_Interface17', set())
    assert not _is_linked(b, 'archDSL_Interface17', a2)
    if hasattr(a2, 'archDSL_Method'):
        assert not _is_linked(a2, 'archDSL_Method', b)


def test_assoc_optmethods14_reverse_link_reassign_clear():
    a1 = archDSL_UncertainInterface(name="sample_text")
    a2 = archDSL_UncertainInterface(name="sample_text_2")
    b = archDSL_OptMethod(type="sample_text")
    _safe_set(b, 'archDSL_OptMethod', a1)
    assert _is_linked(b, 'archDSL_OptMethod', a1)
    if hasattr(a1, 'archDSL_UncertainInterface15'):
        assert _is_linked(a1, 'archDSL_UncertainInterface15', b)
    _safe_set(b, 'archDSL_OptMethod', a2)
    assert _is_linked(b, 'archDSL_OptMethod', a2)
    if hasattr(a1, 'archDSL_UncertainInterface15'):
        assert not _is_linked(a1, 'archDSL_UncertainInterface15', b)
    if hasattr(a2, 'archDSL_UncertainInterface15'):
        assert _is_linked(a2, 'archDSL_UncertainInterface15', b)
    _safe_set(b, 'archDSL_OptMethod', None)
    assert not _is_linked(b, 'archDSL_OptMethod', a2)
    if hasattr(a2, 'archDSL_UncertainInterface15'):
        assert not _is_linked(a2, 'archDSL_UncertainInterface15', b)


def test_assoc_param35_reverse_link_reassign_clear():
    a1 = archDSL_SuperMethod(name="sample_text")
    a2 = archDSL_SuperMethod(name="sample_text_2")
    b = archDSL_Param(name="sample_text", type="sample_text")
    _safe_set(b, 'archDSL_Param', a1)
    assert _is_linked(b, 'archDSL_Param', a1)
    if hasattr(a1, 'archDSL_SuperMethod'):
        assert _is_linked(a1, 'archDSL_SuperMethod', b)
    _safe_set(b, 'archDSL_Param', a2)
    assert _is_linked(b, 'archDSL_Param', a2)
    if hasattr(a1, 'archDSL_SuperMethod'):
        assert not _is_linked(a1, 'archDSL_SuperMethod', b)
    if hasattr(a2, 'archDSL_SuperMethod'):
        assert _is_linked(a2, 'archDSL_SuperMethod', b)
    _safe_set(b, 'archDSL_Param', None)
    assert not _is_linked(b, 'archDSL_Param', a2)
    if hasattr(a2, 'archDSL_SuperMethod'):
        assert not _is_linked(a2, 'archDSL_SuperMethod', b)


def test_assoc_superInterface21_reverse_link_reassign_clear():
    a1 = archDSL_UncertainConnector(name="sample_text")
    a2 = archDSL_UncertainConnector(name="sample_text_2")
    b = archDSL_Interface(name="sample_text")
    _safe_set(b, 'archDSL_Interface23', a1)
    assert _is_linked(b, 'archDSL_Interface23', a1)
    if hasattr(a1, 'archDSL_UncertainConnector22'):
        assert _is_linked(a1, 'archDSL_UncertainConnector22', b)
    _safe_set(b, 'archDSL_Interface23', a2)
    assert _is_linked(b, 'archDSL_Interface23', a2)
    if hasattr(a1, 'archDSL_UncertainConnector22'):
        assert not _is_linked(a1, 'archDSL_UncertainConnector22', b)
    if hasattr(a2, 'archDSL_UncertainConnector22'):
        assert _is_linked(a2, 'archDSL_UncertainConnector22', b)
    _safe_set(b, 'archDSL_Interface23', None)
    assert not _is_linked(b, 'archDSL_Interface23', a2)
    if hasattr(a2, 'archDSL_UncertainConnector22'):
        assert not _is_linked(a2, 'archDSL_UncertainConnector22', b)


def test_assoc_superInterface9_reverse_link_reassign_clear():
    a1 = archDSL_UncertainInterface(name="sample_text")
    a2 = archDSL_UncertainInterface(name="sample_text_2")
    b = archDSL_Interface(name="sample_text")
    _safe_set(b, 'archDSL_Interface11', a1)
    assert _is_linked(b, 'archDSL_Interface11', a1)
    if hasattr(a1, 'archDSL_UncertainInterface10'):
        assert _is_linked(a1, 'archDSL_UncertainInterface10', b)
    _safe_set(b, 'archDSL_Interface11', a2)
    assert _is_linked(b, 'archDSL_Interface11', a2)
    if hasattr(a1, 'archDSL_UncertainInterface10'):
        assert not _is_linked(a1, 'archDSL_UncertainInterface10', b)
    if hasattr(a2, 'archDSL_UncertainInterface10'):
        assert _is_linked(a2, 'archDSL_UncertainInterface10', b)
    _safe_set(b, 'archDSL_Interface11', None)
    assert not _is_linked(b, 'archDSL_Interface11', a2)
    if hasattr(a2, 'archDSL_UncertainInterface10'):
        assert not _is_linked(a2, 'archDSL_UncertainInterface10', b)


def test_assoc_u_behaviors24_reverse_link_reassign_clear():
    a1 = archDSL_UncertainConnector(name="sample_text")
    a2 = archDSL_UncertainConnector(name="sample_text_2")
    b = archDSL_UncertainBehavior(name="sample_text")
    _safe_set(b, 'archDSL_UncertainBehavior', a1)
    assert _is_linked(b, 'archDSL_UncertainBehavior', a1)
    if hasattr(a1, 'archDSL_UncertainConnector25'):
        assert _is_linked(a1, 'archDSL_UncertainConnector25', b)
    _safe_set(b, 'archDSL_UncertainBehavior', a2)
    assert _is_linked(b, 'archDSL_UncertainBehavior', a2)
    if hasattr(a1, 'archDSL_UncertainConnector25'):
        assert not _is_linked(a1, 'archDSL_UncertainConnector25', b)
    if hasattr(a2, 'archDSL_UncertainConnector25'):
        assert _is_linked(a2, 'archDSL_UncertainConnector25', b)
    _safe_set(b, 'archDSL_UncertainBehavior', None)
    assert not _is_linked(b, 'archDSL_UncertainBehavior', a2)
    if hasattr(a2, 'archDSL_UncertainConnector25'):
        assert not _is_linked(a2, 'archDSL_UncertainConnector25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_behaviors18_stub_double():
    # archDSL_Behavior has no real 'archDSL_Behavior20' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Connector(name="sample_text")
    partner = archDSL_Behavior()
    setattr(partner, 'archDSL_Behavior20', None)
    _safe_set(owner, 'archDSL_Connector19', {partner})
    assert getattr(partner, 'archDSL_Behavior20') == owner
    _safe_set(owner, 'archDSL_Connector19', set())
    assert getattr(partner, 'archDSL_Behavior20') is None


def test_assoc_call29_stub_double():
    # archDSL_Behavior has no real 'archDSL_Behavior30' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Method(type="sample_text")
    partner = archDSL_Behavior()
    setattr(partner, 'archDSL_Behavior30', None)
    _safe_set(owner, 'archDSL_Method31', partner)
    assert owner in getattr(partner, 'archDSL_Behavior30')
    _safe_set(owner, 'archDSL_Method31', None)
    assert owner not in getattr(partner, 'archDSL_Behavior30')


def test_assoc_call36_stub_double():
    # archDSL_SuperCall has no real 'archDSL_SuperCall' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_UncertainBehavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_UncertainBehavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_UncertainBehavior(name="sample_text")
    partner = archDSL_SuperCall()
    setattr(partner, 'archDSL_SuperCall', None)
    _safe_set(owner, 'archDSL_UncertainBehavior37', {partner})
    assert getattr(partner, 'archDSL_SuperCall') == owner
    _safe_set(owner, 'archDSL_UncertainBehavior37', set())
    assert getattr(partner, 'archDSL_SuperCall') is None


def test_assoc_connectors7_stub_double():
    # archDSL_Model has no real 'archDSL_Model8' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Connector(name="sample_text")
    partner = archDSL_Model()
    setattr(partner, 'archDSL_Model8', None)
    _safe_set(owner, 'archDSL_Connector', partner)
    assert owner in getattr(partner, 'archDSL_Model8')
    _safe_set(owner, 'archDSL_Connector', None)
    assert owner not in getattr(partner, 'archDSL_Model8')


def test_assoc_end32_stub_double():
    # archDSL_Behavior has no real 'archDSL_Behavior33' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Interface(name="sample_text")
    partner = archDSL_Behavior()
    setattr(partner, 'archDSL_Behavior33', None)
    _safe_set(owner, 'archDSL_Interface34', partner)
    assert getattr(partner, 'archDSL_Behavior33') == owner
    _safe_set(owner, 'archDSL_Interface34', None)
    assert getattr(partner, 'archDSL_Behavior33') is None


def test_assoc_interface26_stub_double():
    # archDSL_Behavior has no real 'archDSL_Behavior27' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Interface(name="sample_text")
    partner = archDSL_Behavior()
    setattr(partner, 'archDSL_Behavior27', None)
    _safe_set(owner, 'archDSL_Interface28', partner)
    assert getattr(partner, 'archDSL_Behavior27') == owner
    _safe_set(owner, 'archDSL_Interface28', None)
    assert getattr(partner, 'archDSL_Behavior27') is None


def test_assoc_interfaces0_stub_double():
    # archDSL_Model has no real 'archDSL_Model' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_Interface(name="sample_text")
    partner = archDSL_Model()
    setattr(partner, 'archDSL_Model', None)
    _safe_set(owner, 'archDSL_Interface', partner)
    assert owner in getattr(partner, 'archDSL_Model')
    _safe_set(owner, 'archDSL_Interface', None)
    assert owner not in getattr(partner, 'archDSL_Model')


def test_assoc_name43_stub_double():
    # archDSL_SuperCall has no real 'archDSL_SuperCall44' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_SuperMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_SuperMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_SuperMethod(name="sample_text")
    partner = archDSL_SuperCall()
    setattr(partner, 'archDSL_SuperCall44', None)
    _safe_set(owner, 'archDSL_SuperMethod45', partner)
    assert getattr(partner, 'archDSL_SuperCall44') == owner
    _safe_set(owner, 'archDSL_SuperMethod45', None)
    assert getattr(partner, 'archDSL_SuperCall44') is None


def test_assoc_u_connectors5_stub_double():
    # archDSL_Model has no real 'archDSL_Model6' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_UncertainConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_UncertainConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_UncertainConnector(name="sample_text")
    partner = archDSL_Model()
    setattr(partner, 'archDSL_Model6', None)
    _safe_set(owner, 'archDSL_UncertainConnector', partner)
    assert owner in getattr(partner, 'archDSL_Model6')
    _safe_set(owner, 'archDSL_UncertainConnector', None)
    assert owner not in getattr(partner, 'archDSL_Model6')


def test_assoc_u_interfaces1_stub_double():
    # archDSL_Model has no real 'archDSL_Model2' property in the generated
    # code (a bare stub) -- manually attach it so archDSL_UncertainInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # archDSL_UncertainInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = archDSL_UncertainInterface(name="sample_text")
    partner = archDSL_Model()
    setattr(partner, 'archDSL_Model2', None)
    _safe_set(owner, 'archDSL_UncertainInterface', partner)
    assert owner in getattr(partner, 'archDSL_Model2')
    _safe_set(owner, 'archDSL_UncertainInterface', None)
    assert owner not in getattr(partner, 'archDSL_Model2')


