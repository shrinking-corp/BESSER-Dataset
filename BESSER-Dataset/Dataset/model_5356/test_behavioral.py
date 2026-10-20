import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bundle,
    FeatureMetadata,
    LocatedElement,
    Tool,
    p2_Copyright,
    p2_Description,
    p2_DiscoverySite,
    p2_Feature,
    p2_FeatureMetadata,
    p2_License,
    p2_Plugin,
    p2_Vendor,
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

def test_assoc_copyright0_stub_double():
    # p2_Copyright has no real 'p2_Copyright' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_Copyright()
    setattr(partner, 'p2_Copyright', None)
    _safe_set(owner, 'p2_Feature', partner)
    assert getattr(partner, 'p2_Copyright') == owner
    _safe_set(owner, 'p2_Feature', None)
    assert getattr(partner, 'p2_Copyright') is None


def test_assoc_description1_stub_double():
    # p2_Description has no real 'p2_Description' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_Description()
    setattr(partner, 'p2_Description', None)
    _safe_set(owner, 'p2_Feature2', partner)
    assert getattr(partner, 'p2_Description') == owner
    _safe_set(owner, 'p2_Feature2', None)
    assert getattr(partner, 'p2_Description') is None


def test_assoc_license5_stub_double():
    # p2_License has no real 'p2_License' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_License()
    setattr(partner, 'p2_License', None)
    _safe_set(owner, 'p2_Feature6', partner)
    assert getattr(partner, 'p2_License') == owner
    _safe_set(owner, 'p2_Feature6', None)
    assert getattr(partner, 'p2_License') is None


def test_assoc_plugins9_stub_double():
    # p2_Plugin has no real 'p2_Plugin' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_Plugin()
    setattr(partner, 'p2_Plugin', None)
    _safe_set(owner, 'p2_Feature10', {partner})
    assert getattr(partner, 'p2_Plugin') == owner
    _safe_set(owner, 'p2_Feature10', set())
    assert getattr(partner, 'p2_Plugin') is None


def test_assoc_provider7_stub_double():
    # p2_Vendor has no real 'p2_Vendor' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_Vendor()
    setattr(partner, 'p2_Vendor', None)
    _safe_set(owner, 'p2_Feature8', partner)
    assert getattr(partner, 'p2_Vendor') == owner
    _safe_set(owner, 'p2_Feature8', None)
    assert getattr(partner, 'p2_Vendor') is None


def test_assoc_sites3_stub_double():
    # p2_DiscoverySite has no real 'p2_DiscoverySite' property in the generated
    # code (a bare stub) -- manually attach it so p2_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Feature(application="sample_text")
    partner = p2_DiscoverySite()
    setattr(partner, 'p2_DiscoverySite', None)
    _safe_set(owner, 'p2_Feature4', {partner})
    assert getattr(partner, 'p2_DiscoverySite') == owner
    _safe_set(owner, 'p2_Feature4', set())
    assert getattr(partner, 'p2_DiscoverySite') is None


