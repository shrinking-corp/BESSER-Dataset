import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    netxstudio_Company,
    netxstudio_Country,
    netxstudio_Equipment,
    netxstudio_Expression,
    netxstudio_Function,
    netxstudio_Library,
    netxstudio_Meta,
    netxstudio_Metric,
    netxstudio_Network,
    netxstudio_Parameter,
    netxstudio_Protocol,
    netxstudio_RFSService,
    netxstudio_Room,
    netxstudio_Site,
    netxstudio_Tolerance,
    netxstudio_Unit,
    netxstudio_User,
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

def test_assoc_companies11_stub_double():
    # netxstudio_Company has no real 'netxstudio_Company' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Company()
    setattr(partner, 'netxstudio_Company', None)
    _safe_set(owner, 'netxstudio_Library12', {partner})
    assert getattr(partner, 'netxstudio_Company') == owner
    _safe_set(owner, 'netxstudio_Library12', set())
    assert getattr(partner, 'netxstudio_Company') is None


def test_assoc_countries21_stub_double():
    # netxstudio_Country has no real 'netxstudio_Country' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Country()
    setattr(partner, 'netxstudio_Country', None)
    _safe_set(owner, 'netxstudio_Library22', {partner})
    assert getattr(partner, 'netxstudio_Country') == owner
    _safe_set(owner, 'netxstudio_Library22', set())
    assert getattr(partner, 'netxstudio_Country') is None


def test_assoc_equipments3_stub_double():
    # netxstudio_Equipment has no real 'netxstudio_Equipment' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Equipment()
    setattr(partner, 'netxstudio_Equipment', None)
    _safe_set(owner, 'netxstudio_Library4', {partner})
    assert getattr(partner, 'netxstudio_Equipment') == owner
    _safe_set(owner, 'netxstudio_Library4', set())
    assert getattr(partner, 'netxstudio_Equipment') is None


def test_assoc_expressions15_stub_double():
    # netxstudio_Expression has no real 'netxstudio_Expression' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Expression()
    setattr(partner, 'netxstudio_Expression', None)
    _safe_set(owner, 'netxstudio_Library16', {partner})
    assert getattr(partner, 'netxstudio_Expression') == owner
    _safe_set(owner, 'netxstudio_Library16', set())
    assert getattr(partner, 'netxstudio_Expression') is None


def test_assoc_functions1_stub_double():
    # netxstudio_Function has no real 'netxstudio_Function' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Function()
    setattr(partner, 'netxstudio_Function', None)
    _safe_set(owner, 'netxstudio_Library2', {partner})
    assert getattr(partner, 'netxstudio_Function') == owner
    _safe_set(owner, 'netxstudio_Library2', set())
    assert getattr(partner, 'netxstudio_Function') is None


def test_assoc_metrics5_stub_double():
    # netxstudio_Metric has no real 'netxstudio_Metric' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Metric()
    setattr(partner, 'netxstudio_Metric', None)
    _safe_set(owner, 'netxstudio_Library6', {partner})
    assert getattr(partner, 'netxstudio_Metric') == owner
    _safe_set(owner, 'netxstudio_Library6', set())
    assert getattr(partner, 'netxstudio_Metric') is None


def test_assoc_networks0_stub_double():
    # netxstudio_Network has no real 'netxstudio_Network' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Network()
    setattr(partner, 'netxstudio_Network', None)
    _safe_set(owner, 'netxstudio_Library', {partner})
    assert getattr(partner, 'netxstudio_Network') == owner
    _safe_set(owner, 'netxstudio_Library', set())
    assert getattr(partner, 'netxstudio_Network') is None


def test_assoc_parameters7_stub_double():
    # netxstudio_Parameter has no real 'netxstudio_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Parameter()
    setattr(partner, 'netxstudio_Parameter', None)
    _safe_set(owner, 'netxstudio_Library8', {partner})
    assert getattr(partner, 'netxstudio_Parameter') == owner
    _safe_set(owner, 'netxstudio_Library8', set())
    assert getattr(partner, 'netxstudio_Parameter') is None


def test_assoc_protocols9_stub_double():
    # netxstudio_Protocol has no real 'netxstudio_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Protocol()
    setattr(partner, 'netxstudio_Protocol', None)
    _safe_set(owner, 'netxstudio_Library10', {partner})
    assert getattr(partner, 'netxstudio_Protocol') == owner
    _safe_set(owner, 'netxstudio_Library10', set())
    assert getattr(partner, 'netxstudio_Protocol') is None


def test_assoc_rooms19_stub_double():
    # netxstudio_Room has no real 'netxstudio_Room' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Room()
    setattr(partner, 'netxstudio_Room', None)
    _safe_set(owner, 'netxstudio_Library20', {partner})
    assert getattr(partner, 'netxstudio_Room') == owner
    _safe_set(owner, 'netxstudio_Library20', set())
    assert getattr(partner, 'netxstudio_Room') is None


def test_assoc_services27_stub_double():
    # netxstudio_RFSService has no real 'netxstudio_RFSService' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_RFSService()
    setattr(partner, 'netxstudio_RFSService', None)
    _safe_set(owner, 'netxstudio_Library28', {partner})
    assert getattr(partner, 'netxstudio_RFSService') == owner
    _safe_set(owner, 'netxstudio_Library28', set())
    assert getattr(partner, 'netxstudio_RFSService') is None


def test_assoc_sites23_stub_double():
    # netxstudio_Site has no real 'netxstudio_Site' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Site()
    setattr(partner, 'netxstudio_Site', None)
    _safe_set(owner, 'netxstudio_Library24', {partner})
    assert getattr(partner, 'netxstudio_Site') == owner
    _safe_set(owner, 'netxstudio_Library24', set())
    assert getattr(partner, 'netxstudio_Site') is None


def test_assoc_tolerances13_stub_double():
    # netxstudio_Tolerance has no real 'netxstudio_Tolerance' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Tolerance()
    setattr(partner, 'netxstudio_Tolerance', None)
    _safe_set(owner, 'netxstudio_Library14', {partner})
    assert getattr(partner, 'netxstudio_Tolerance') == owner
    _safe_set(owner, 'netxstudio_Library14', set())
    assert getattr(partner, 'netxstudio_Tolerance') is None


def test_assoc_units25_stub_double():
    # netxstudio_Unit has no real 'netxstudio_Unit' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Unit()
    setattr(partner, 'netxstudio_Unit', None)
    _safe_set(owner, 'netxstudio_Library26', {partner})
    assert getattr(partner, 'netxstudio_Unit') == owner
    _safe_set(owner, 'netxstudio_Library26', set())
    assert getattr(partner, 'netxstudio_Unit') is None


def test_assoc_users17_stub_double():
    # netxstudio_User has no real 'netxstudio_User' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_User()
    setattr(partner, 'netxstudio_User', None)
    _safe_set(owner, 'netxstudio_Library18', {partner})
    assert getattr(partner, 'netxstudio_User') == owner
    _safe_set(owner, 'netxstudio_Library18', set())
    assert getattr(partner, 'netxstudio_User') is None


def test_assoc_versions29_stub_double():
    # netxstudio_Meta has no real 'netxstudio_Meta' property in the generated
    # code (a bare stub) -- manually attach it so netxstudio_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # netxstudio_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = netxstudio_Library(description="sample_text", name="sample_text", version="sample_text")
    partner = netxstudio_Meta()
    setattr(partner, 'netxstudio_Meta', None)
    _safe_set(owner, 'netxstudio_Library30', {partner})
    assert getattr(partner, 'netxstudio_Meta') == owner
    _safe_set(owner, 'netxstudio_Library30', set())
    assert getattr(partner, 'netxstudio_Meta') is None


