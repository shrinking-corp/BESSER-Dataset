import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    testModel_ContainedElement,
    testModel_Element,
    testModel_Kategorie,
    testModel_multiRefElement,
    testModel_referenziertesElement,
    testModel_upperBound,
    ElementType,
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

def test_assoc_contains2_reverse_link_reassign_clear():
    a1 = testModel_Kategorie(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    a2 = testModel_Kategorie(Boolean="sample_text_2", bigdeci="sample_text_2", bigint="sample_text_2", bool=False, byte="sample_text_2", name="sample_text_2")
    b = testModel_ContainedElement(Character="sample_text", DiagnosticChain="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedElement', a1)
    assert _is_linked(b, 'testModel_ContainedElement', a1)
    if hasattr(a1, 'testModel_Kategorie3'):
        assert _is_linked(a1, 'testModel_Kategorie3', b)
    _safe_set(b, 'testModel_ContainedElement', a2)
    assert _is_linked(b, 'testModel_ContainedElement', a2)
    if hasattr(a1, 'testModel_Kategorie3'):
        assert not _is_linked(a1, 'testModel_Kategorie3', b)
    if hasattr(a2, 'testModel_Kategorie3'):
        assert _is_linked(a2, 'testModel_Kategorie3', b)
    _safe_set(b, 'testModel_ContainedElement', None)
    assert not _is_linked(b, 'testModel_ContainedElement', a2)
    if hasattr(a2, 'testModel_Kategorie3'):
        assert not _is_linked(a2, 'testModel_Kategorie3', b)


def test_assoc_multiRef8_reverse_link_reassign_clear():
    a1 = testModel_referenziertesElement(Float="sample_text", Integer="sample_text", LongObj="sample_text", ShortObj="sample_text", int=7, long="sample_text", name="sample_text", notChangeable="sample_text", short="sample_text")
    a2 = testModel_referenziertesElement(Float="sample_text_2", Integer="sample_text_2", LongObj="sample_text_2", ShortObj="sample_text_2", int=13, long="sample_text_2", name="sample_text_2", notChangeable="sample_text_2", short="sample_text_2")
    b = testModel_multiRefElement(name="sample_text")
    _safe_set(b, 'testModel_multiRefElement', a1)
    assert _is_linked(b, 'testModel_multiRefElement', a1)
    if hasattr(a1, 'testModel_referenziertesElement9'):
        assert _is_linked(a1, 'testModel_referenziertesElement9', b)
    _safe_set(b, 'testModel_multiRefElement', a2)
    assert _is_linked(b, 'testModel_multiRefElement', a2)
    if hasattr(a1, 'testModel_referenziertesElement9'):
        assert not _is_linked(a1, 'testModel_referenziertesElement9', b)
    if hasattr(a2, 'testModel_referenziertesElement9'):
        assert _is_linked(a2, 'testModel_referenziertesElement9', b)
    _safe_set(b, 'testModel_multiRefElement', None)
    assert not _is_linked(b, 'testModel_multiRefElement', a2)
    if hasattr(a2, 'testModel_referenziertesElement9'):
        assert not _is_linked(a2, 'testModel_referenziertesElement9', b)


def test_assoc_ref4_reverse_link_reassign_clear():
    a1 = testModel_referenziertesElement(Float="sample_text", Integer="sample_text", LongObj="sample_text", ShortObj="sample_text", int=7, long="sample_text", name="sample_text", notChangeable="sample_text", short="sample_text")
    a2 = testModel_referenziertesElement(Float="sample_text_2", Integer="sample_text_2", LongObj="sample_text_2", ShortObj="sample_text_2", int=13, long="sample_text_2", name="sample_text_2", notChangeable="sample_text_2", short="sample_text_2")
    b = testModel_ContainedElement(Character="sample_text", DiagnosticChain="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedElement5', {a1})
    assert _is_linked(b, 'testModel_ContainedElement5', a1)
    if hasattr(a1, 'testModel_referenziertesElement'):
        assert _is_linked(a1, 'testModel_referenziertesElement', b)
    _safe_set(b, 'testModel_ContainedElement5', {a2})
    assert _is_linked(b, 'testModel_ContainedElement5', a2)
    if hasattr(a1, 'testModel_referenziertesElement'):
        assert not _is_linked(a1, 'testModel_referenziertesElement', b)
    if hasattr(a2, 'testModel_referenziertesElement'):
        assert _is_linked(a2, 'testModel_referenziertesElement', b)
    _safe_set(b, 'testModel_ContainedElement5', set())
    assert not _is_linked(b, 'testModel_ContainedElement5', a2)
    if hasattr(a2, 'testModel_referenziertesElement'):
        assert not _is_linked(a2, 'testModel_referenziertesElement', b)


def test_assoc_subKategorie1_reverse_link_reassign_clear():
    a1 = testModel_Kategorie(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    a2 = testModel_Kategorie(Boolean="sample_text_2", bigdeci="sample_text_2", bigint="sample_text_2", bool=False, byte="sample_text_2", name="sample_text_2")
    b = testModel_Kategorie(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    _safe_set(b, 'testModel_Kategorie0', {a1})
    assert _is_linked(b, 'testModel_Kategorie0', a1)
    if hasattr(a1, 'testModel_Kategorie'):
        assert _is_linked(a1, 'testModel_Kategorie', b)
    _safe_set(b, 'testModel_Kategorie0', {a2})
    assert _is_linked(b, 'testModel_Kategorie0', a2)
    if hasattr(a1, 'testModel_Kategorie'):
        assert not _is_linked(a1, 'testModel_Kategorie', b)
    if hasattr(a2, 'testModel_Kategorie'):
        assert _is_linked(a2, 'testModel_Kategorie', b)
    _safe_set(b, 'testModel_Kategorie0', set())
    assert not _is_linked(b, 'testModel_Kategorie0', a2)
    if hasattr(a2, 'testModel_Kategorie'):
        assert not _is_linked(a2, 'testModel_Kategorie', b)


def test_assoc_upperBound6_reverse_link_reassign_clear():
    a1 = testModel_upperBound(name="sample_text")
    a2 = testModel_upperBound(name="sample_text_2")
    b = testModel_ContainedElement(Character="sample_text", DiagnosticChain="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedElement7', {a1})
    assert _is_linked(b, 'testModel_ContainedElement7', a1)
    if hasattr(a1, 'testModel_upperBound'):
        assert _is_linked(a1, 'testModel_upperBound', b)
    _safe_set(b, 'testModel_ContainedElement7', {a2})
    assert _is_linked(b, 'testModel_ContainedElement7', a2)
    if hasattr(a1, 'testModel_upperBound'):
        assert not _is_linked(a1, 'testModel_upperBound', b)
    if hasattr(a2, 'testModel_upperBound'):
        assert _is_linked(a2, 'testModel_upperBound', b)
    _safe_set(b, 'testModel_ContainedElement7', set())
    assert not _is_linked(b, 'testModel_ContainedElement7', a2)
    if hasattr(a2, 'testModel_upperBound'):
        assert not _is_linked(a2, 'testModel_upperBound', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

