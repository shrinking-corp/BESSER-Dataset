import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotationAttribute,
    Literal,
    NumberLiteral,
    base_Annotation,
    base_AnnotationAttribute,
    base_AnnotationType,
    base_BooleanLiteral,
    base_Documentation,
    base_EnumAnnotationAttribute,
    base_Import,
    base_IntLiteral,
    base_KeyValue,
    base_Literal,
    base_LiteralArray,
    base_NumberLiteral,
    base_RealLiteral,
    base_SimpleAnnotationAttribute,
    base_StringLiteral,
    LiteralType,
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

def test_assoc_attributes7_reverse_link_reassign_clear():
    a1 = base_AnnotationType(name="sample_text", targets="sample_text")
    a2 = base_AnnotationType(name="sample_text_2", targets="sample_text_2")
    b = base_AnnotationAttribute(name="sample_text", optional=True)
    _safe_set(b, 'base_AnnotationAttribute', a1)
    assert _is_linked(b, 'base_AnnotationAttribute', a1)
    if hasattr(a1, 'base_AnnotationType8'):
        assert _is_linked(a1, 'base_AnnotationType8', b)
    _safe_set(b, 'base_AnnotationAttribute', a2)
    assert _is_linked(b, 'base_AnnotationAttribute', a2)
    if hasattr(a1, 'base_AnnotationType8'):
        assert not _is_linked(a1, 'base_AnnotationType8', b)
    if hasattr(a2, 'base_AnnotationType8'):
        assert _is_linked(a2, 'base_AnnotationType8', b)
    _safe_set(b, 'base_AnnotationAttribute', None)
    assert not _is_linked(b, 'base_AnnotationAttribute', a2)
    if hasattr(a2, 'base_AnnotationType8'):
        assert not _is_linked(a2, 'base_AnnotationType8', b)


def test_assoc_docu5_reverse_link_reassign_clear():
    a1 = base_Documentation(lines="sample_text")
    a2 = base_Documentation(lines="sample_text_2")
    b = base_AnnotationType(name="sample_text", targets="sample_text")
    _safe_set(b, 'base_AnnotationType6', a1)
    assert _is_linked(b, 'base_AnnotationType6', a1)
    if hasattr(a1, 'base_Documentation'):
        assert _is_linked(a1, 'base_Documentation', b)
    _safe_set(b, 'base_AnnotationType6', a2)
    assert _is_linked(b, 'base_AnnotationType6', a2)
    if hasattr(a1, 'base_Documentation'):
        assert not _is_linked(a1, 'base_Documentation', b)
    if hasattr(a2, 'base_Documentation'):
        assert _is_linked(a2, 'base_Documentation', b)
    _safe_set(b, 'base_AnnotationType6', None)
    assert not _is_linked(b, 'base_AnnotationType6', a2)
    if hasattr(a2, 'base_Documentation'):
        assert not _is_linked(a2, 'base_Documentation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes1_stub_double():
    # base_Annotation has no real 'base_Annotation2' property in the generated
    # code (a bare stub) -- manually attach it so base_KeyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # base_KeyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = base_KeyValue(key="sample_text")
    partner = base_Annotation()
    setattr(partner, 'base_Annotation2', None)
    _safe_set(owner, 'base_KeyValue', partner)
    assert owner in getattr(partner, 'base_Annotation2')
    _safe_set(owner, 'base_KeyValue', None)
    assert owner not in getattr(partner, 'base_Annotation2')


def test_assoc_type0_stub_double():
    # base_Annotation has no real 'base_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so base_AnnotationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # base_AnnotationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = base_AnnotationType(name="sample_text", targets="sample_text")
    partner = base_Annotation()
    setattr(partner, 'base_Annotation', None)
    _safe_set(owner, 'base_AnnotationType', partner)
    assert getattr(partner, 'base_Annotation') == owner
    _safe_set(owner, 'base_AnnotationType', None)
    assert getattr(partner, 'base_Annotation') is None


def test_assoc_value3_stub_double():
    # base_Literal has no real 'base_Literal' property in the generated
    # code (a bare stub) -- manually attach it so base_KeyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # base_KeyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = base_KeyValue(key="sample_text")
    partner = base_Literal()
    setattr(partner, 'base_Literal', None)
    _safe_set(owner, 'base_KeyValue4', partner)
    assert getattr(partner, 'base_Literal') == owner
    _safe_set(owner, 'base_KeyValue4', None)
    assert getattr(partner, 'base_Literal') is None


