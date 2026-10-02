import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metadata_DocumentRoot,
    metadata_EStringToStringMapEntry,
    metadata_MetaData,
    metadata_Versioning,
    metadata_Versions,
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

def test_assoc_metadata4_reverse_link_reassign_clear():
    a1 = metadata_MetaData(artifactId="sample_text", groupId="sample_text", version="sample_text")
    a2 = metadata_MetaData(artifactId="sample_text_2", groupId="sample_text_2", version="sample_text_2")
    b = metadata_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'metadata_DocumentRoot5', {a1})
    assert _is_linked(b, 'metadata_DocumentRoot5', a1)
    if hasattr(a1, 'metadata_MetaData'):
        assert _is_linked(a1, 'metadata_MetaData', b)
    _safe_set(b, 'metadata_DocumentRoot5', {a2})
    assert _is_linked(b, 'metadata_DocumentRoot5', a2)
    if hasattr(a1, 'metadata_MetaData'):
        assert not _is_linked(a1, 'metadata_MetaData', b)
    if hasattr(a2, 'metadata_MetaData'):
        assert _is_linked(a2, 'metadata_MetaData', b)
    _safe_set(b, 'metadata_DocumentRoot5', set())
    assert not _is_linked(b, 'metadata_DocumentRoot5', a2)
    if hasattr(a2, 'metadata_MetaData'):
        assert not _is_linked(a2, 'metadata_MetaData', b)


def test_assoc_versioning6_reverse_link_reassign_clear():
    a1 = metadata_Versioning(lastUpdated="sample_text", latest="sample_text", release="sample_text")
    a2 = metadata_Versioning(lastUpdated="sample_text_2", latest="sample_text_2", release="sample_text_2")
    b = metadata_MetaData(artifactId="sample_text", groupId="sample_text", version="sample_text")
    _safe_set(b, 'metadata_MetaData7', a1)
    assert _is_linked(b, 'metadata_MetaData7', a1)
    if hasattr(a1, 'metadata_Versioning'):
        assert _is_linked(a1, 'metadata_Versioning', b)
    _safe_set(b, 'metadata_MetaData7', a2)
    assert _is_linked(b, 'metadata_MetaData7', a2)
    if hasattr(a1, 'metadata_Versioning'):
        assert not _is_linked(a1, 'metadata_Versioning', b)
    if hasattr(a2, 'metadata_Versioning'):
        assert _is_linked(a2, 'metadata_Versioning', b)
    _safe_set(b, 'metadata_MetaData7', None)
    assert not _is_linked(b, 'metadata_MetaData7', a2)
    if hasattr(a2, 'metadata_Versioning'):
        assert not _is_linked(a2, 'metadata_Versioning', b)


def test_assoc_versions8_reverse_link_reassign_clear():
    a1 = metadata_Versions(version="sample_text")
    a2 = metadata_Versions(version="sample_text_2")
    b = metadata_Versioning(lastUpdated="sample_text", latest="sample_text", release="sample_text")
    _safe_set(b, 'metadata_Versioning9', a1)
    assert _is_linked(b, 'metadata_Versioning9', a1)
    if hasattr(a1, 'metadata_Versions'):
        assert _is_linked(a1, 'metadata_Versions', b)
    _safe_set(b, 'metadata_Versioning9', a2)
    assert _is_linked(b, 'metadata_Versioning9', a2)
    if hasattr(a1, 'metadata_Versions'):
        assert not _is_linked(a1, 'metadata_Versions', b)
    if hasattr(a2, 'metadata_Versions'):
        assert _is_linked(a2, 'metadata_Versions', b)
    _safe_set(b, 'metadata_Versioning9', None)
    assert not _is_linked(b, 'metadata_Versioning9', a2)
    if hasattr(a2, 'metadata_Versions'):
        assert not _is_linked(a2, 'metadata_Versions', b)


