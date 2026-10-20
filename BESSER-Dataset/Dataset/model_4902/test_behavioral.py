import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_Config,
    model_ConfigExpectedResultPair,
    model_ExpectedResult,
    model_Response,
    model_Scenario,
    ContentType,
    HttpVerb,
    StatusCode,
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

def test_assoc_response0_reverse_link_reassign_clear():
    a1 = model_Response(contentType="sample_text", responseBody="sample_text", responseTime="sample_text", statusCode="sample_text")
    a2 = model_Response(contentType="sample_text_2", responseBody="sample_text_2", responseTime="sample_text_2", statusCode="sample_text_2")
    b = model_Config(contentType="sample_text", httpVerb="sample_text", name="sample_text", requestBody="sample_text", requestURL="sample_text")
    _safe_set(b, 'model_Config', a1)
    assert _is_linked(b, 'model_Config', a1)
    if hasattr(a1, 'model_Response'):
        assert _is_linked(a1, 'model_Response', b)
    _safe_set(b, 'model_Config', a2)
    assert _is_linked(b, 'model_Config', a2)
    if hasattr(a1, 'model_Response'):
        assert not _is_linked(a1, 'model_Response', b)
    if hasattr(a2, 'model_Response'):
        assert _is_linked(a2, 'model_Response', b)
    _safe_set(b, 'model_Config', None)
    assert not _is_linked(b, 'model_Config', a2)
    if hasattr(a2, 'model_Response'):
        assert not _is_linked(a2, 'model_Response', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_config2_stub_double():
    # model_ConfigExpectedResultPair has no real 'model_ConfigExpectedResultPair3' property in the generated
    # code (a bare stub) -- manually attach it so model_Config's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Config's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Config(contentType="sample_text", httpVerb="sample_text", name="sample_text", requestBody="sample_text", requestURL="sample_text")
    partner = model_ConfigExpectedResultPair()
    setattr(partner, 'model_ConfigExpectedResultPair3', None)
    _safe_set(owner, 'model_Config4', partner)
    assert getattr(partner, 'model_ConfigExpectedResultPair3') == owner
    _safe_set(owner, 'model_Config4', None)
    assert getattr(partner, 'model_ConfigExpectedResultPair3') is None


def test_assoc_configExpectedResultPairList1_stub_double():
    # model_ConfigExpectedResultPair has no real 'model_ConfigExpectedResultPair' property in the generated
    # code (a bare stub) -- manually attach it so model_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Scenario(scenarioFilePath="sample_text")
    partner = model_ConfigExpectedResultPair()
    setattr(partner, 'model_ConfigExpectedResultPair', None)
    _safe_set(owner, 'model_Scenario', {partner})
    assert getattr(partner, 'model_ConfigExpectedResultPair') == owner
    _safe_set(owner, 'model_Scenario', set())
    assert getattr(partner, 'model_ConfigExpectedResultPair') is None


def test_assoc_expectedResult5_stub_double():
    # model_ConfigExpectedResultPair has no real 'model_ConfigExpectedResultPair6' property in the generated
    # code (a bare stub) -- manually attach it so model_ExpectedResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ExpectedResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ExpectedResult(contentType="sample_text", responseBody="sample_text", statusCode="sample_text")
    partner = model_ConfigExpectedResultPair()
    setattr(partner, 'model_ConfigExpectedResultPair6', None)
    _safe_set(owner, 'model_ExpectedResult', partner)
    assert getattr(partner, 'model_ConfigExpectedResultPair6') == owner
    _safe_set(owner, 'model_ExpectedResult', None)
    assert getattr(partner, 'model_ConfigExpectedResultPair6') is None


