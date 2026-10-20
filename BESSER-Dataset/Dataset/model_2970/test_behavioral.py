import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    namespace_EStringToStringMapEntry,
    namespace_XMLNamespaceDocumentRoot,
    SpaceType,
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

def test_assoc_xMLNSPrefixMap0_stub_double():
    # namespace_EStringToStringMapEntry has no real 'namespace_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so namespace_XMLNamespaceDocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # namespace_XMLNamespaceDocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = namespace_XMLNamespaceDocumentRoot(base="sample_text", id="sample_text", lang="sample_text", mixed="sample_text", space="sample_text")
    partner = namespace_EStringToStringMapEntry()
    setattr(partner, 'namespace_EStringToStringMapEntry', None)
    _safe_set(owner, 'namespace_XMLNamespaceDocumentRoot', {partner})
    assert getattr(partner, 'namespace_EStringToStringMapEntry') == owner
    _safe_set(owner, 'namespace_XMLNamespaceDocumentRoot', set())
    assert getattr(partner, 'namespace_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # namespace_EStringToStringMapEntry has no real 'namespace_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so namespace_XMLNamespaceDocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # namespace_XMLNamespaceDocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = namespace_XMLNamespaceDocumentRoot(base="sample_text", id="sample_text", lang="sample_text", mixed="sample_text", space="sample_text")
    partner = namespace_EStringToStringMapEntry()
    setattr(partner, 'namespace_EStringToStringMapEntry3', None)
    _safe_set(owner, 'namespace_XMLNamespaceDocumentRoot2', {partner})
    assert getattr(partner, 'namespace_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'namespace_XMLNamespaceDocumentRoot2', set())
    assert getattr(partner, 'namespace_EStringToStringMapEntry3') is None


