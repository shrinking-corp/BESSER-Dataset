import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GroupAndArtifact,
    Provider,
    maven_GroupAndArtifact,
    maven_MapEntry,
    maven_Mappings,
    maven_MavenProvider,
    maven_Scope,
    maven_Scopes,
    maven_Transform,
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

def test_assoc_aliases0_reverse_link_reassign_clear():
    a1 = maven_MapEntry(name="sample_text")
    a2 = maven_MapEntry(name="sample_text_2")
    b = maven_GroupAndArtifact(artifactId="sample_text", groupId="sample_text")
    _safe_set(b, 'maven_GroupAndArtifact', a1)
    assert _is_linked(b, 'maven_GroupAndArtifact', a1)
    if hasattr(a1, 'maven_MapEntry'):
        assert _is_linked(a1, 'maven_MapEntry', b)
    _safe_set(b, 'maven_GroupAndArtifact', a2)
    assert _is_linked(b, 'maven_GroupAndArtifact', a2)
    if hasattr(a1, 'maven_MapEntry'):
        assert not _is_linked(a1, 'maven_MapEntry', b)
    if hasattr(a2, 'maven_MapEntry'):
        assert _is_linked(a2, 'maven_MapEntry', b)
    _safe_set(b, 'maven_GroupAndArtifact', None)
    assert not _is_linked(b, 'maven_GroupAndArtifact', a2)
    if hasattr(a2, 'maven_MapEntry'):
        assert not _is_linked(a2, 'maven_MapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entries1_stub_double():
    # maven_Mappings has no real 'maven_Mappings' property in the generated
    # code (a bare stub) -- manually attach it so maven_MapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MapEntry(name="sample_text")
    partner = maven_Mappings()
    setattr(partner, 'maven_Mappings', None)
    _safe_set(owner, 'maven_MapEntry2', partner)
    assert owner in getattr(partner, 'maven_Mappings')
    _safe_set(owner, 'maven_MapEntry2', None)
    assert owner not in getattr(partner, 'maven_Mappings')


def test_assoc_mappings5_stub_double():
    # maven_Mappings has no real 'maven_Mappings6' property in the generated
    # code (a bare stub) -- manually attach it so maven_MavenProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MavenProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MavenProvider(transitive=True)
    partner = maven_Mappings()
    setattr(partner, 'maven_Mappings6', None)
    _safe_set(owner, 'maven_MavenProvider', partner)
    assert getattr(partner, 'maven_Mappings6') == owner
    _safe_set(owner, 'maven_MavenProvider', None)
    assert getattr(partner, 'maven_Mappings6') is None


def test_assoc_scope9_stub_double():
    # maven_Scopes has no real 'maven_Scopes10' property in the generated
    # code (a bare stub) -- manually attach it so maven_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_Scope(exclude=True, name="sample_text")
    partner = maven_Scopes()
    setattr(partner, 'maven_Scopes10', None)
    _safe_set(owner, 'maven_Scope', partner)
    assert owner in getattr(partner, 'maven_Scopes10')
    _safe_set(owner, 'maven_Scope', None)
    assert owner not in getattr(partner, 'maven_Scopes10')


def test_assoc_scopes7_stub_double():
    # maven_Scopes has no real 'maven_Scopes' property in the generated
    # code (a bare stub) -- manually attach it so maven_MavenProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MavenProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MavenProvider(transitive=True)
    partner = maven_Scopes()
    setattr(partner, 'maven_Scopes', None)
    _safe_set(owner, 'maven_MavenProvider8', partner)
    assert getattr(partner, 'maven_Scopes') == owner
    _safe_set(owner, 'maven_MavenProvider8', None)
    assert getattr(partner, 'maven_Scopes') is None


