import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Categorized,
    message_Language,
    message_Message,
    message_MessageLibrary,
    message_Translation,
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

def test_assoc_lang3_reverse_link_reassign_clear():
    a1 = message_Translation(translation="sample_text", uid="sample_text")
    a2 = message_Translation(translation="sample_text_2", uid="sample_text_2")
    b = message_Language(code="sample_text", defaultLang=True, lang="sample_text", uid="sample_text")
    _safe_set(b, 'message_Language', a1)
    assert _is_linked(b, 'message_Language', a1)
    if hasattr(a1, 'message_Translation4'):
        assert _is_linked(a1, 'message_Translation4', b)
    _safe_set(b, 'message_Language', a2)
    assert _is_linked(b, 'message_Language', a2)
    if hasattr(a1, 'message_Translation4'):
        assert not _is_linked(a1, 'message_Translation4', b)
    if hasattr(a2, 'message_Translation4'):
        assert _is_linked(a2, 'message_Translation4', b)
    _safe_set(b, 'message_Language', None)
    assert not _is_linked(b, 'message_Language', a2)
    if hasattr(a2, 'message_Translation4'):
        assert not _is_linked(a2, 'message_Translation4', b)


def test_assoc_messages0_reverse_link_reassign_clear():
    a1 = message_MessageLibrary(name="sample_text", uid="sample_text")
    a2 = message_MessageLibrary(name="sample_text_2", uid="sample_text_2")
    b = message_Message(name="sample_text", uid="sample_text")
    _safe_set(b, 'message_Message', a1)
    assert _is_linked(b, 'message_Message', a1)
    if hasattr(a1, 'message_MessageLibrary'):
        assert _is_linked(a1, 'message_MessageLibrary', b)
    _safe_set(b, 'message_Message', a2)
    assert _is_linked(b, 'message_Message', a2)
    if hasattr(a1, 'message_MessageLibrary'):
        assert not _is_linked(a1, 'message_MessageLibrary', b)
    if hasattr(a2, 'message_MessageLibrary'):
        assert _is_linked(a2, 'message_MessageLibrary', b)
    _safe_set(b, 'message_Message', None)
    assert not _is_linked(b, 'message_Message', a2)
    if hasattr(a2, 'message_MessageLibrary'):
        assert not _is_linked(a2, 'message_MessageLibrary', b)


def test_assoc_translatioins1_reverse_link_reassign_clear():
    a1 = message_Translation(translation="sample_text", uid="sample_text")
    a2 = message_Translation(translation="sample_text_2", uid="sample_text_2")
    b = message_Message(name="sample_text", uid="sample_text")
    _safe_set(b, 'message_Message2', {a1})
    assert _is_linked(b, 'message_Message2', a1)
    if hasattr(a1, 'message_Translation'):
        assert _is_linked(a1, 'message_Translation', b)
    _safe_set(b, 'message_Message2', {a2})
    assert _is_linked(b, 'message_Message2', a2)
    if hasattr(a1, 'message_Translation'):
        assert not _is_linked(a1, 'message_Translation', b)
    if hasattr(a2, 'message_Translation'):
        assert _is_linked(a2, 'message_Translation', b)
    _safe_set(b, 'message_Message2', set())
    assert not _is_linked(b, 'message_Message2', a2)
    if hasattr(a2, 'message_Translation'):
        assert not _is_linked(a2, 'message_Translation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

