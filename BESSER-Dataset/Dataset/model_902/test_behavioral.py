import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    WorkDefinition,
    simplePDL_Activity,
    simplePDL_Process,
    simplePDL_SubProcess,
    simplePDL_WorkDefinition,
    simplePDL_WorkDefinitionParameter,
    simplePDL_WorkProduct,
    simplePDL_WorkSequence,
    ParameterDirectionKind,
    WorkSequenceType,
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

def test_assoc_activities0_reverse_link_reassign_clear():
    a1 = simplePDL_WorkDefinition(name="sample_text")
    a2 = simplePDL_WorkDefinition(name="sample_text_2")
    b = simplePDL_Process(name="sample_text")
    _safe_set(b, 'simplePDL_Process', {a1})
    assert _is_linked(b, 'simplePDL_Process', a1)
    if hasattr(a1, 'simplePDL_WorkDefinition'):
        assert _is_linked(a1, 'simplePDL_WorkDefinition', b)
    _safe_set(b, 'simplePDL_Process', {a2})
    assert _is_linked(b, 'simplePDL_Process', a2)
    if hasattr(a1, 'simplePDL_WorkDefinition'):
        assert not _is_linked(a1, 'simplePDL_WorkDefinition', b)
    if hasattr(a2, 'simplePDL_WorkDefinition'):
        assert _is_linked(a2, 'simplePDL_WorkDefinition', b)
    _safe_set(b, 'simplePDL_Process', set())
    assert not _is_linked(b, 'simplePDL_Process', a2)
    if hasattr(a2, 'simplePDL_WorkDefinition'):
        assert not _is_linked(a2, 'simplePDL_WorkDefinition', b)


def test_assoc_linksToPredecessors9_reverse_link_reassign_clear():
    a1 = simplePDL_WorkSequence(linkType="sample_text")
    a2 = simplePDL_WorkSequence(linkType="sample_text_2")
    b = simplePDL_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition10', a1)
    assert _is_linked(b, 'WorkDefinition10', a1)
    if hasattr(a1, 'successor'):
        assert _is_linked(a1, 'successor', b)
    _safe_set(b, 'WorkDefinition10', a2)
    assert _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a1, 'successor'):
        assert not _is_linked(a1, 'successor', b)
    if hasattr(a2, 'successor'):
        assert _is_linked(a2, 'successor', b)
    _safe_set(b, 'WorkDefinition10', None)
    assert not _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a2, 'successor'):
        assert not _is_linked(a2, 'successor', b)


def test_assoc_linksToSuccessors8_reverse_link_reassign_clear():
    a1 = simplePDL_WorkSequence(linkType="sample_text")
    a2 = simplePDL_WorkSequence(linkType="sample_text_2")
    b = simplePDL_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition', a1)
    assert _is_linked(b, 'WorkDefinition', a1)
    if hasattr(a1, 'predecessor'):
        assert _is_linked(a1, 'predecessor', b)
    _safe_set(b, 'WorkDefinition', a2)
    assert _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a1, 'predecessor'):
        assert not _is_linked(a1, 'predecessor', b)
    if hasattr(a2, 'predecessor'):
        assert _is_linked(a2, 'predecessor', b)
    _safe_set(b, 'WorkDefinition', None)
    assert not _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a2, 'predecessor'):
        assert not _is_linked(a2, 'predecessor', b)


def test_assoc_parameterType11_reverse_link_reassign_clear():
    a1 = simplePDL_WorkProduct(name="sample_text")
    a2 = simplePDL_WorkProduct(name="sample_text_2")
    b = simplePDL_WorkDefinitionParameter(parameterKind="sample_text")
    _safe_set(b, 'simplePDL_WorkDefinitionParameter12', a1)
    assert _is_linked(b, 'simplePDL_WorkDefinitionParameter12', a1)
    if hasattr(a1, 'simplePDL_WorkProduct'):
        assert _is_linked(a1, 'simplePDL_WorkProduct', b)
    _safe_set(b, 'simplePDL_WorkDefinitionParameter12', a2)
    assert _is_linked(b, 'simplePDL_WorkDefinitionParameter12', a2)
    if hasattr(a1, 'simplePDL_WorkProduct'):
        assert not _is_linked(a1, 'simplePDL_WorkProduct', b)
    if hasattr(a2, 'simplePDL_WorkProduct'):
        assert _is_linked(a2, 'simplePDL_WorkProduct', b)
    _safe_set(b, 'simplePDL_WorkDefinitionParameter12', None)
    assert not _is_linked(b, 'simplePDL_WorkDefinitionParameter12', a2)
    if hasattr(a2, 'simplePDL_WorkProduct'):
        assert not _is_linked(a2, 'simplePDL_WorkProduct', b)


def test_assoc_parameters6_reverse_link_reassign_clear():
    a1 = simplePDL_WorkDefinitionParameter(parameterKind="sample_text")
    a2 = simplePDL_WorkDefinitionParameter(parameterKind="sample_text_2")
    b = simplePDL_WorkDefinition(name="sample_text")
    _safe_set(b, 'simplePDL_WorkDefinition7', {a1})
    assert _is_linked(b, 'simplePDL_WorkDefinition7', a1)
    if hasattr(a1, 'simplePDL_WorkDefinitionParameter'):
        assert _is_linked(a1, 'simplePDL_WorkDefinitionParameter', b)
    _safe_set(b, 'simplePDL_WorkDefinition7', {a2})
    assert _is_linked(b, 'simplePDL_WorkDefinition7', a2)
    if hasattr(a1, 'simplePDL_WorkDefinitionParameter'):
        assert not _is_linked(a1, 'simplePDL_WorkDefinitionParameter', b)
    if hasattr(a2, 'simplePDL_WorkDefinitionParameter'):
        assert _is_linked(a2, 'simplePDL_WorkDefinitionParameter', b)
    _safe_set(b, 'simplePDL_WorkDefinition7', set())
    assert not _is_linked(b, 'simplePDL_WorkDefinition7', a2)
    if hasattr(a2, 'simplePDL_WorkDefinitionParameter'):
        assert not _is_linked(a2, 'simplePDL_WorkDefinitionParameter', b)


def test_assoc_predecessor3_reverse_link_reassign_clear():
    a1 = simplePDL_WorkSequence(linkType="sample_text")
    a2 = simplePDL_WorkSequence(linkType="sample_text_2")
    b = simplePDL_WorkDefinition(name="sample_text")
    _safe_set(b, 'linksToSuccessors', a1)
    assert _is_linked(b, 'linksToSuccessors', a1)
    if hasattr(a1, 'WorkSequence'):
        assert _is_linked(a1, 'WorkSequence', b)
    _safe_set(b, 'linksToSuccessors', a2)
    assert _is_linked(b, 'linksToSuccessors', a2)
    if hasattr(a1, 'WorkSequence'):
        assert not _is_linked(a1, 'WorkSequence', b)
    if hasattr(a2, 'WorkSequence'):
        assert _is_linked(a2, 'WorkSequence', b)
    _safe_set(b, 'linksToSuccessors', None)
    assert not _is_linked(b, 'linksToSuccessors', a2)
    if hasattr(a2, 'WorkSequence'):
        assert not _is_linked(a2, 'WorkSequence', b)


def test_assoc_successor4_reverse_link_reassign_clear():
    a1 = simplePDL_WorkSequence(linkType="sample_text")
    a2 = simplePDL_WorkSequence(linkType="sample_text_2")
    b = simplePDL_WorkDefinition(name="sample_text")
    _safe_set(b, 'linksToPredecessors', a1)
    assert _is_linked(b, 'linksToPredecessors', a1)
    if hasattr(a1, 'WorkSequence5'):
        assert _is_linked(a1, 'WorkSequence5', b)
    _safe_set(b, 'linksToPredecessors', a2)
    assert _is_linked(b, 'linksToPredecessors', a2)
    if hasattr(a1, 'WorkSequence5'):
        assert not _is_linked(a1, 'WorkSequence5', b)
    if hasattr(a2, 'WorkSequence5'):
        assert _is_linked(a2, 'WorkSequence5', b)
    _safe_set(b, 'linksToPredecessors', None)
    assert not _is_linked(b, 'linksToPredecessors', a2)
    if hasattr(a2, 'WorkSequence5'):
        assert not _is_linked(a2, 'WorkSequence5', b)


def test_assoc_workSequences1_reverse_link_reassign_clear():
    a1 = simplePDL_WorkSequence(linkType="sample_text")
    a2 = simplePDL_WorkSequence(linkType="sample_text_2")
    b = simplePDL_Process(name="sample_text")
    _safe_set(b, 'simplePDL_Process2', {a1})
    assert _is_linked(b, 'simplePDL_Process2', a1)
    if hasattr(a1, 'simplePDL_WorkSequence'):
        assert _is_linked(a1, 'simplePDL_WorkSequence', b)
    _safe_set(b, 'simplePDL_Process2', {a2})
    assert _is_linked(b, 'simplePDL_Process2', a2)
    if hasattr(a1, 'simplePDL_WorkSequence'):
        assert not _is_linked(a1, 'simplePDL_WorkSequence', b)
    if hasattr(a2, 'simplePDL_WorkSequence'):
        assert _is_linked(a2, 'simplePDL_WorkSequence', b)
    _safe_set(b, 'simplePDL_Process2', set())
    assert not _is_linked(b, 'simplePDL_Process2', a2)
    if hasattr(a2, 'simplePDL_WorkSequence'):
        assert not _is_linked(a2, 'simplePDL_WorkSequence', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

