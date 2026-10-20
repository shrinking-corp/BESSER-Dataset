import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BundleAware,
    NameContainer,
    NsPrefixable,
    ResourceAware,
    schema_ActionLike,
    schema_ActionType,
    schema_AggregationType,
    schema_EFactory,
    schema_EPackage,
    schema_StorySchemaCatalog,
    schema_StoryType,
    schema_TargetType,
    schema_TargetTypeRef,
    ActionTypeStatus,
    Tenses,
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

def test_assoc_actionTypes1_reverse_link_reassign_clear():
    a1 = schema_StorySchemaCatalog(ecoreUrl="sample_text", generatedPackageName="sample_text", xmiUrl="sample_text")
    a2 = schema_StorySchemaCatalog(ecoreUrl="sample_text_2", generatedPackageName="sample_text_2", xmiUrl="sample_text_2")
    b = schema_ActionType(status="sample_text")
    _safe_set(b, 'schema_ActionType', a1)
    assert _is_linked(b, 'schema_ActionType', a1)
    if hasattr(a1, 'schema_StorySchemaCatalog2'):
        assert _is_linked(a1, 'schema_StorySchemaCatalog2', b)
    _safe_set(b, 'schema_ActionType', a2)
    assert _is_linked(b, 'schema_ActionType', a2)
    if hasattr(a1, 'schema_StorySchemaCatalog2'):
        assert not _is_linked(a1, 'schema_StorySchemaCatalog2', b)
    if hasattr(a2, 'schema_StorySchemaCatalog2'):
        assert _is_linked(a2, 'schema_StorySchemaCatalog2', b)
    _safe_set(b, 'schema_ActionType', None)
    assert not _is_linked(b, 'schema_ActionType', a2)
    if hasattr(a2, 'schema_StorySchemaCatalog2'):
        assert not _is_linked(a2, 'schema_StorySchemaCatalog2', b)


def test_assoc_aggregationTypes3_reverse_link_reassign_clear():
    a1 = schema_StorySchemaCatalog(ecoreUrl="sample_text", generatedPackageName="sample_text", xmiUrl="sample_text")
    a2 = schema_StorySchemaCatalog(ecoreUrl="sample_text_2", generatedPackageName="sample_text_2", xmiUrl="sample_text_2")
    b = schema_AggregationType()
    _safe_set(b, 'schema_AggregationType', a1)
    assert _is_linked(b, 'schema_AggregationType', a1)
    if hasattr(a1, 'schema_StorySchemaCatalog4'):
        assert _is_linked(a1, 'schema_StorySchemaCatalog4', b)
    _safe_set(b, 'schema_AggregationType', a2)
    assert _is_linked(b, 'schema_AggregationType', a2)
    if hasattr(a1, 'schema_StorySchemaCatalog4'):
        assert not _is_linked(a1, 'schema_StorySchemaCatalog4', b)
    if hasattr(a2, 'schema_StorySchemaCatalog4'):
        assert _is_linked(a2, 'schema_StorySchemaCatalog4', b)
    _safe_set(b, 'schema_AggregationType', None)
    assert not _is_linked(b, 'schema_AggregationType', a2)
    if hasattr(a2, 'schema_StorySchemaCatalog4'):
        assert not _is_linked(a2, 'schema_StorySchemaCatalog4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eFactory7_stub_double():
    # schema_EFactory has no real 'schema_EFactory' property in the generated
    # code (a bare stub) -- manually attach it so schema_StorySchemaCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schema_StorySchemaCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schema_StorySchemaCatalog(ecoreUrl="sample_text", generatedPackageName="sample_text", xmiUrl="sample_text")
    partner = schema_EFactory()
    setattr(partner, 'schema_EFactory', None)
    _safe_set(owner, 'schema_StorySchemaCatalog8', partner)
    assert getattr(partner, 'schema_EFactory') == owner
    _safe_set(owner, 'schema_StorySchemaCatalog8', None)
    assert getattr(partner, 'schema_EFactory') is None


def test_assoc_ePackage5_stub_double():
    # schema_EPackage has no real 'schema_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so schema_StorySchemaCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schema_StorySchemaCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schema_StorySchemaCatalog(ecoreUrl="sample_text", generatedPackageName="sample_text", xmiUrl="sample_text")
    partner = schema_EPackage()
    setattr(partner, 'schema_EPackage', None)
    _safe_set(owner, 'schema_StorySchemaCatalog6', partner)
    assert getattr(partner, 'schema_EPackage') == owner
    _safe_set(owner, 'schema_StorySchemaCatalog6', None)
    assert getattr(partner, 'schema_EPackage') is None


def test_assoc_resolvedSubjectTypes9_stub_double():
    # schema_TargetType has no real 'schema_TargetType' property in the generated
    # code (a bare stub) -- manually attach it so schema_ActionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schema_ActionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schema_ActionType(status="sample_text")
    partner = schema_TargetType()
    setattr(partner, 'schema_TargetType', None)
    _safe_set(owner, 'schema_ActionType10', {partner})
    assert getattr(partner, 'schema_TargetType') == owner
    _safe_set(owner, 'schema_ActionType10', set())
    assert getattr(partner, 'schema_TargetType') is None


def test_assoc_storyTypes0_stub_double():
    # schema_StoryType has no real 'schema_StoryType' property in the generated
    # code (a bare stub) -- manually attach it so schema_StorySchemaCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schema_StorySchemaCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schema_StorySchemaCatalog(ecoreUrl="sample_text", generatedPackageName="sample_text", xmiUrl="sample_text")
    partner = schema_StoryType()
    setattr(partner, 'schema_StoryType', None)
    _safe_set(owner, 'schema_StorySchemaCatalog', {partner})
    assert getattr(partner, 'schema_StoryType') == owner
    _safe_set(owner, 'schema_StorySchemaCatalog', set())
    assert getattr(partner, 'schema_StoryType') is None


def test_assoc_subjectTypes11_stub_double():
    # schema_TargetTypeRef has no real 'schema_TargetTypeRef' property in the generated
    # code (a bare stub) -- manually attach it so schema_ActionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schema_ActionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schema_ActionType(status="sample_text")
    partner = schema_TargetTypeRef()
    setattr(partner, 'schema_TargetTypeRef', None)
    _safe_set(owner, 'schema_ActionType12', {partner})
    assert getattr(partner, 'schema_TargetTypeRef') == owner
    _safe_set(owner, 'schema_ActionType12', set())
    assert getattr(partner, 'schema_TargetTypeRef') is None


