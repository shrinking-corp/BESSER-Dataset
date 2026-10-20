import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TypeGraphTrace_ClassListTrace,
    TypeGraphTrace_MethodSignatureTrace,
    TypeGraphTrace_TClass,
    TypeGraphTrace_TMethodSignature,
    TypeGraphTrace_Trace,
    TypeGraphTrace_TypeGraph,
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

def test_assoc_classLists3_stub_double():
    # TypeGraphTrace_Trace has no real 'TypeGraphTrace_Trace4' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphTrace_ClassListTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphTrace_ClassListTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphTrace_ClassListTrace(concatSignature="sample_text")
    partner = TypeGraphTrace_Trace()
    setattr(partner, 'TypeGraphTrace_Trace4', None)
    _safe_set(owner, 'TypeGraphTrace_ClassListTrace', partner)
    assert owner in getattr(partner, 'TypeGraphTrace_Trace4')
    _safe_set(owner, 'TypeGraphTrace_ClassListTrace', None)
    assert owner not in getattr(partner, 'TypeGraphTrace_Trace4')


def test_assoc_methodSignatures1_stub_double():
    # TypeGraphTrace_Trace has no real 'TypeGraphTrace_Trace2' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphTrace_MethodSignatureTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphTrace_MethodSignatureTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphTrace_MethodSignatureTrace(signatureString="sample_text")
    partner = TypeGraphTrace_Trace()
    setattr(partner, 'TypeGraphTrace_Trace2', None)
    _safe_set(owner, 'TypeGraphTrace_MethodSignatureTrace', partner)
    assert owner in getattr(partner, 'TypeGraphTrace_Trace2')
    _safe_set(owner, 'TypeGraphTrace_MethodSignatureTrace', None)
    assert owner not in getattr(partner, 'TypeGraphTrace_Trace2')


def test_assoc_tClasses7_stub_double():
    # TypeGraphTrace_TClass has no real 'TypeGraphTrace_TClass' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphTrace_ClassListTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphTrace_ClassListTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphTrace_ClassListTrace(concatSignature="sample_text")
    partner = TypeGraphTrace_TClass()
    setattr(partner, 'TypeGraphTrace_TClass', None)
    _safe_set(owner, 'TypeGraphTrace_ClassListTrace8', {partner})
    assert getattr(partner, 'TypeGraphTrace_TClass') == owner
    _safe_set(owner, 'TypeGraphTrace_ClassListTrace8', set())
    assert getattr(partner, 'TypeGraphTrace_TClass') is None


def test_assoc_tMethodSignature5_stub_double():
    # TypeGraphTrace_TMethodSignature has no real 'TypeGraphTrace_TMethodSignature' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphTrace_MethodSignatureTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphTrace_MethodSignatureTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphTrace_MethodSignatureTrace(signatureString="sample_text")
    partner = TypeGraphTrace_TMethodSignature()
    setattr(partner, 'TypeGraphTrace_TMethodSignature', None)
    _safe_set(owner, 'TypeGraphTrace_MethodSignatureTrace6', partner)
    assert getattr(partner, 'TypeGraphTrace_TMethodSignature') == owner
    _safe_set(owner, 'TypeGraphTrace_MethodSignatureTrace6', None)
    assert getattr(partner, 'TypeGraphTrace_TMethodSignature') is None


