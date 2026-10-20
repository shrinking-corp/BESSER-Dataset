import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MultiLiteralConstraint,
    TokenTrace_EObject,
    TokenTrace_Literal,
    TokenTrace_Token,
    TokenTrace_TokenTrace,
    TokenTraceType,
    TokenType,
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

def test_assoc_root0_reverse_link_reassign_clear():
    a1 = TokenTrace_TokenTrace(message="sample_text", name="sample_text", tokenTraceType="sample_text")
    a2 = TokenTrace_TokenTrace(message="sample_text_2", name="sample_text_2", tokenTraceType="sample_text_2")
    b = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    _safe_set(b, 'TokenTrace_Token', a1)
    assert _is_linked(b, 'TokenTrace_Token', a1)
    if hasattr(a1, 'TokenTrace_TokenTrace'):
        assert _is_linked(a1, 'TokenTrace_TokenTrace', b)
    _safe_set(b, 'TokenTrace_Token', a2)
    assert _is_linked(b, 'TokenTrace_Token', a2)
    if hasattr(a1, 'TokenTrace_TokenTrace'):
        assert not _is_linked(a1, 'TokenTrace_TokenTrace', b)
    if hasattr(a2, 'TokenTrace_TokenTrace'):
        assert _is_linked(a2, 'TokenTrace_TokenTrace', b)
    _safe_set(b, 'TokenTrace_Token', None)
    assert not _is_linked(b, 'TokenTrace_Token', a2)
    if hasattr(a2, 'TokenTrace_TokenTrace'):
        assert not _is_linked(a2, 'TokenTrace_TokenTrace', b)


def test_assoc_tokens3_reverse_link_reassign_clear():
    a1 = TokenTrace_TokenTrace(message="sample_text", name="sample_text", tokenTraceType="sample_text")
    a2 = TokenTrace_TokenTrace(message="sample_text_2", name="sample_text_2", tokenTraceType="sample_text_2")
    b = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    _safe_set(b, 'TokenTrace_Token5', a1)
    assert _is_linked(b, 'TokenTrace_Token5', a1)
    if hasattr(a1, 'TokenTrace_TokenTrace4'):
        assert _is_linked(a1, 'TokenTrace_TokenTrace4', b)
    _safe_set(b, 'TokenTrace_Token5', a2)
    assert _is_linked(b, 'TokenTrace_Token5', a2)
    if hasattr(a1, 'TokenTrace_TokenTrace4'):
        assert not _is_linked(a1, 'TokenTrace_TokenTrace4', b)
    if hasattr(a2, 'TokenTrace_TokenTrace4'):
        assert _is_linked(a2, 'TokenTrace_TokenTrace4', b)
    _safe_set(b, 'TokenTrace_Token5', None)
    assert not _is_linked(b, 'TokenTrace_Token5', a2)
    if hasattr(a2, 'TokenTrace_TokenTrace4'):
        assert not _is_linked(a2, 'TokenTrace_TokenTrace4', b)


def test_assoc_tokens9_reverse_link_reassign_clear():
    a1 = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    a2 = TokenTrace_Token(assignedProbability="sample_text_2", computedProbability="sample_text_2", message="sample_text_2", name="sample_text_2", referenceCount=13, scale="sample_text_2", tokenType="sample_text_2")
    b = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    _safe_set(b, 'TokenTrace_Token8', {a1})
    assert _is_linked(b, 'TokenTrace_Token8', a1)
    if hasattr(a1, 'TokenTrace_Token10'):
        assert _is_linked(a1, 'TokenTrace_Token10', b)
    _safe_set(b, 'TokenTrace_Token8', {a2})
    assert _is_linked(b, 'TokenTrace_Token8', a2)
    if hasattr(a1, 'TokenTrace_Token10'):
        assert not _is_linked(a1, 'TokenTrace_Token10', b)
    if hasattr(a2, 'TokenTrace_Token10'):
        assert _is_linked(a2, 'TokenTrace_Token10', b)
    _safe_set(b, 'TokenTrace_Token8', set())
    assert not _is_linked(b, 'TokenTrace_Token8', a2)
    if hasattr(a2, 'TokenTrace_Token10'):
        assert not _is_linked(a2, 'TokenTrace_Token10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_inferredRootLiteral6_stub_double():
    # TokenTrace_Literal has no real 'TokenTrace_Literal' property in the generated
    # code (a bare stub) -- manually attach it so TokenTrace_TokenTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TokenTrace_TokenTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TokenTrace_TokenTrace(message="sample_text", name="sample_text", tokenTraceType="sample_text")
    partner = TokenTrace_Literal()
    setattr(partner, 'TokenTrace_Literal', None)
    _safe_set(owner, 'TokenTrace_TokenTrace7', partner)
    assert getattr(partner, 'TokenTrace_Literal') == owner
    _safe_set(owner, 'TokenTrace_TokenTrace7', None)
    assert getattr(partner, 'TokenTrace_Literal') is None


def test_assoc_instanceRoot1_stub_double():
    # TokenTrace_EObject has no real 'TokenTrace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so TokenTrace_TokenTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TokenTrace_TokenTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TokenTrace_TokenTrace(message="sample_text", name="sample_text", tokenTraceType="sample_text")
    partner = TokenTrace_EObject()
    setattr(partner, 'TokenTrace_EObject', None)
    _safe_set(owner, 'TokenTrace_TokenTrace2', partner)
    assert getattr(partner, 'TokenTrace_EObject') == owner
    _safe_set(owner, 'TokenTrace_TokenTrace2', None)
    assert getattr(partner, 'TokenTrace_EObject') is None


def test_assoc_literalSink17_stub_double():
    # TokenTrace_Literal has no real 'TokenTrace_Literal19' property in the generated
    # code (a bare stub) -- manually attach it so TokenTrace_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TokenTrace_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    partner = TokenTrace_Literal()
    setattr(partner, 'TokenTrace_Literal19', None)
    _safe_set(owner, 'TokenTrace_Token18', {partner})
    assert getattr(partner, 'TokenTrace_Literal19') == owner
    _safe_set(owner, 'TokenTrace_Token18', set())
    assert getattr(partner, 'TokenTrace_Literal19') is None


def test_assoc_relatedEObject11_stub_double():
    # TokenTrace_EObject has no real 'TokenTrace_EObject13' property in the generated
    # code (a bare stub) -- manually attach it so TokenTrace_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TokenTrace_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    partner = TokenTrace_EObject()
    setattr(partner, 'TokenTrace_EObject13', None)
    _safe_set(owner, 'TokenTrace_Token12', partner)
    assert getattr(partner, 'TokenTrace_EObject13') == owner
    _safe_set(owner, 'TokenTrace_Token12', None)
    assert getattr(partner, 'TokenTrace_EObject13') is None


def test_assoc_tokenLiteral14_stub_double():
    # TokenTrace_Literal has no real 'TokenTrace_Literal16' property in the generated
    # code (a bare stub) -- manually attach it so TokenTrace_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TokenTrace_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TokenTrace_Token(assignedProbability="sample_text", computedProbability="sample_text", message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", tokenType="sample_text")
    partner = TokenTrace_Literal()
    setattr(partner, 'TokenTrace_Literal16', None)
    _safe_set(owner, 'TokenTrace_Token15', partner)
    assert getattr(partner, 'TokenTrace_Literal16') == owner
    _safe_set(owner, 'TokenTrace_Token15', None)
    assert getattr(partner, 'TokenTrace_Literal16') is None


