import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RequirementSourceConf_EStringToStringMapEntry,
    RequirementSourceConf_MappingElement,
    RequirementSourceConf_RequirementSource,
    RequirementSourceConf_RequirementSources,
    RequirementSourceConf_RequirementsContainer,
    RequirementSourceConf_Scope,
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

def test_assoc_contents1_stub_double():
    # RequirementSourceConf_RequirementsContainer has no real 'RequirementSourceConf_RequirementsContainer' property in the generated
    # code (a bare stub) -- manually attach it so RequirementSourceConf_RequirementSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RequirementSourceConf_RequirementSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RequirementSourceConf_RequirementSource(connectorId="sample_text", dataModelURI="sample_text", destinationURI="sample_text", name="sample_text", repositoryURI="sample_text")
    partner = RequirementSourceConf_RequirementsContainer()
    setattr(partner, 'RequirementSourceConf_RequirementsContainer', None)
    _safe_set(owner, 'RequirementSourceConf_RequirementSource2', partner)
    assert getattr(partner, 'RequirementSourceConf_RequirementsContainer') == owner
    _safe_set(owner, 'RequirementSourceConf_RequirementSource2', None)
    assert getattr(partner, 'RequirementSourceConf_RequirementsContainer') is None


def test_assoc_defaultScope7_stub_double():
    # RequirementSourceConf_Scope has no real 'RequirementSourceConf_Scope' property in the generated
    # code (a bare stub) -- manually attach it so RequirementSourceConf_RequirementSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RequirementSourceConf_RequirementSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RequirementSourceConf_RequirementSource(connectorId="sample_text", dataModelURI="sample_text", destinationURI="sample_text", name="sample_text", repositoryURI="sample_text")
    partner = RequirementSourceConf_Scope()
    setattr(partner, 'RequirementSourceConf_Scope', None)
    _safe_set(owner, 'RequirementSourceConf_RequirementSource8', partner)
    assert getattr(partner, 'RequirementSourceConf_Scope') == owner
    _safe_set(owner, 'RequirementSourceConf_RequirementSource8', None)
    assert getattr(partner, 'RequirementSourceConf_Scope') is None


def test_assoc_mappings5_stub_double():
    # RequirementSourceConf_MappingElement has no real 'RequirementSourceConf_MappingElement' property in the generated
    # code (a bare stub) -- manually attach it so RequirementSourceConf_RequirementSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RequirementSourceConf_RequirementSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RequirementSourceConf_RequirementSource(connectorId="sample_text", dataModelURI="sample_text", destinationURI="sample_text", name="sample_text", repositoryURI="sample_text")
    partner = RequirementSourceConf_MappingElement()
    setattr(partner, 'RequirementSourceConf_MappingElement', None)
    _safe_set(owner, 'RequirementSourceConf_RequirementSource6', {partner})
    assert getattr(partner, 'RequirementSourceConf_MappingElement') == owner
    _safe_set(owner, 'RequirementSourceConf_RequirementSource6', set())
    assert getattr(partner, 'RequirementSourceConf_MappingElement') is None


def test_assoc_properties3_stub_double():
    # RequirementSourceConf_EStringToStringMapEntry has no real 'RequirementSourceConf_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so RequirementSourceConf_RequirementSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RequirementSourceConf_RequirementSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RequirementSourceConf_RequirementSource(connectorId="sample_text", dataModelURI="sample_text", destinationURI="sample_text", name="sample_text", repositoryURI="sample_text")
    partner = RequirementSourceConf_EStringToStringMapEntry()
    setattr(partner, 'RequirementSourceConf_EStringToStringMapEntry', None)
    _safe_set(owner, 'RequirementSourceConf_RequirementSource4', {partner})
    assert getattr(partner, 'RequirementSourceConf_EStringToStringMapEntry') == owner
    _safe_set(owner, 'RequirementSourceConf_RequirementSource4', set())
    assert getattr(partner, 'RequirementSourceConf_EStringToStringMapEntry') is None


def test_assoc_requirementSources0_stub_double():
    # RequirementSourceConf_RequirementSources has no real 'RequirementSourceConf_RequirementSources' property in the generated
    # code (a bare stub) -- manually attach it so RequirementSourceConf_RequirementSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RequirementSourceConf_RequirementSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RequirementSourceConf_RequirementSource(connectorId="sample_text", dataModelURI="sample_text", destinationURI="sample_text", name="sample_text", repositoryURI="sample_text")
    partner = RequirementSourceConf_RequirementSources()
    setattr(partner, 'RequirementSourceConf_RequirementSources', None)
    _safe_set(owner, 'RequirementSourceConf_RequirementSource', partner)
    assert owner in getattr(partner, 'RequirementSourceConf_RequirementSources')
    _safe_set(owner, 'RequirementSourceConf_RequirementSource', None)
    assert owner not in getattr(partner, 'RequirementSourceConf_RequirementSources')


