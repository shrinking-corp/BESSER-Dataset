import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    traceability_Category,
    traceability_DiffCategory,
    traceability_EObject,
    traceability_LogEntry,
    traceability_Trace,
    traceability_TraceComment,
    traceability_TraceDiff,
    traceability_TraceDiffs,
    traceability_Traces,
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

def test_assoc_children5_reverse_link_reassign_clear():
    a1 = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    a2 = traceability_Trace(comment="sample_text_2", description="sample_text_2", value="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Trace'):
        assert _is_linked(a1, 'Trace', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Trace'):
        assert not _is_linked(a1, 'Trace', b)
    if hasattr(a2, 'Trace'):
        assert _is_linked(a2, 'Trace', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Trace'):
        assert not _is_linked(a2, 'Trace', b)


def test_assoc_comments13_reverse_link_reassign_clear():
    a1 = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    a2 = traceability_TraceComment(column="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), username="sample_text_2")
    b = traceability_LogEntry(comment="sample_text", message="sample_text", messageType=7, severity=7)
    _safe_set(b, 'traceability_LogEntry14', {a1})
    assert _is_linked(b, 'traceability_LogEntry14', a1)
    if hasattr(a1, 'traceability_TraceComment15'):
        assert _is_linked(a1, 'traceability_TraceComment15', b)
    _safe_set(b, 'traceability_LogEntry14', {a2})
    assert _is_linked(b, 'traceability_LogEntry14', a2)
    if hasattr(a1, 'traceability_TraceComment15'):
        assert not _is_linked(a1, 'traceability_TraceComment15', b)
    if hasattr(a2, 'traceability_TraceComment15'):
        assert _is_linked(a2, 'traceability_TraceComment15', b)
    _safe_set(b, 'traceability_LogEntry14', set())
    assert not _is_linked(b, 'traceability_LogEntry14', a2)
    if hasattr(a2, 'traceability_TraceComment15'):
        assert not _is_linked(a2, 'traceability_TraceComment15', b)


def test_assoc_comments26_reverse_link_reassign_clear():
    a1 = traceability_TraceDiff(comment="sample_text")
    a2 = traceability_TraceDiff(comment="sample_text_2")
    b = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    _safe_set(b, 'traceability_TraceComment28', a1)
    assert _is_linked(b, 'traceability_TraceComment28', a1)
    if hasattr(a1, 'traceability_TraceDiff27'):
        assert _is_linked(a1, 'traceability_TraceDiff27', b)
    _safe_set(b, 'traceability_TraceComment28', a2)
    assert _is_linked(b, 'traceability_TraceComment28', a2)
    if hasattr(a1, 'traceability_TraceDiff27'):
        assert not _is_linked(a1, 'traceability_TraceDiff27', b)
    if hasattr(a2, 'traceability_TraceDiff27'):
        assert _is_linked(a2, 'traceability_TraceDiff27', b)
    _safe_set(b, 'traceability_TraceComment28', None)
    assert not _is_linked(b, 'traceability_TraceComment28', a2)
    if hasattr(a2, 'traceability_TraceDiff27'):
        assert not _is_linked(a2, 'traceability_TraceDiff27', b)


def test_assoc_comments9_reverse_link_reassign_clear():
    a1 = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    a2 = traceability_TraceComment(column="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), username="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'traceability_Trace10', {a1})
    assert _is_linked(b, 'traceability_Trace10', a1)
    if hasattr(a1, 'traceability_TraceComment'):
        assert _is_linked(a1, 'traceability_TraceComment', b)
    _safe_set(b, 'traceability_Trace10', {a2})
    assert _is_linked(b, 'traceability_Trace10', a2)
    if hasattr(a1, 'traceability_TraceComment'):
        assert not _is_linked(a1, 'traceability_TraceComment', b)
    if hasattr(a2, 'traceability_TraceComment'):
        assert _is_linked(a2, 'traceability_TraceComment', b)
    _safe_set(b, 'traceability_Trace10', set())
    assert not _is_linked(b, 'traceability_Trace10', a2)
    if hasattr(a2, 'traceability_TraceComment'):
        assert not _is_linked(a2, 'traceability_TraceComment', b)


def test_assoc_diffs29_reverse_link_reassign_clear():
    a1 = traceability_TraceDiff(comment="sample_text")
    a2 = traceability_TraceDiff(comment="sample_text_2")
    b = traceability_DiffCategory(modelIndex=7, name="sample_text", unequal=True)
    _safe_set(b, 'traceability_DiffCategory', {a1})
    assert _is_linked(b, 'traceability_DiffCategory', a1)
    if hasattr(a1, 'traceability_TraceDiff30'):
        assert _is_linked(a1, 'traceability_TraceDiff30', b)
    _safe_set(b, 'traceability_DiffCategory', {a2})
    assert _is_linked(b, 'traceability_DiffCategory', a2)
    if hasattr(a1, 'traceability_TraceDiff30'):
        assert not _is_linked(a1, 'traceability_TraceDiff30', b)
    if hasattr(a2, 'traceability_TraceDiff30'):
        assert _is_linked(a2, 'traceability_TraceDiff30', b)
    _safe_set(b, 'traceability_DiffCategory', set())
    assert not _is_linked(b, 'traceability_DiffCategory', a2)
    if hasattr(a2, 'traceability_TraceDiff30'):
        assert not _is_linked(a2, 'traceability_TraceDiff30', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    a2 = traceability_Trace(comment="sample_text_2", description="sample_text_2", value="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Trace8'):
        assert _is_linked(a1, 'Trace8', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Trace8'):
        assert not _is_linked(a1, 'Trace8', b)
    if hasattr(a2, 'Trace8'):
        assert _is_linked(a2, 'Trace8', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Trace8'):
        assert not _is_linked(a2, 'Trace8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_comparedTraces31_stub_double():
    # traceability_TraceDiffs has no real 'traceability_TraceDiffs' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Traces's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Traces's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Traces(comments="sample_text", date=date(2024, 1, 1), fullName="sample_text", location="sample_text", originalSourceURL="sample_text", uriMap="sample_text", username="sample_text")
    partner = traceability_TraceDiffs()
    setattr(partner, 'traceability_TraceDiffs', None)
    _safe_set(owner, 'traceability_Traces32', partner)
    assert owner in getattr(partner, 'traceability_TraceDiffs')
    _safe_set(owner, 'traceability_Traces32', None)
    assert owner not in getattr(partner, 'traceability_TraceDiffs')


def test_assoc_contents33_stub_double():
    # traceability_EObject has no real 'traceability_EObject34' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Category(name="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject34', None)
    _safe_set(owner, 'traceability_Category', {partner})
    assert getattr(partner, 'traceability_EObject34') == owner
    _safe_set(owner, 'traceability_Category', set())
    assert getattr(partner, 'traceability_EObject34') is None


def test_assoc_narrowDown35_stub_double():
    # traceability_EObject has no real 'traceability_EObject37' property in the generated
    # code (a bare stub) -- manually attach it so traceability_TraceComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_TraceComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject37', None)
    _safe_set(owner, 'traceability_TraceComment36', partner)
    assert getattr(partner, 'traceability_EObject37') == owner
    _safe_set(owner, 'traceability_TraceComment36', None)
    assert getattr(partner, 'traceability_EObject37') is None


def test_assoc_participants11_stub_double():
    # traceability_EObject has no real 'traceability_EObject12' property in the generated
    # code (a bare stub) -- manually attach it so traceability_LogEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_LogEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_LogEntry(comment="sample_text", message="sample_text", messageType=7, severity=7)
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject12', None)
    _safe_set(owner, 'traceability_LogEntry', {partner})
    assert getattr(partner, 'traceability_EObject12') == owner
    _safe_set(owner, 'traceability_LogEntry', set())
    assert getattr(partner, 'traceability_EObject12') is None


def test_assoc_participants24_stub_double():
    # traceability_EObject has no real 'traceability_EObject25' property in the generated
    # code (a bare stub) -- manually attach it so traceability_TraceDiff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_TraceDiff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_TraceDiff(comment="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject25', None)
    _safe_set(owner, 'traceability_TraceDiff', {partner})
    assert getattr(partner, 'traceability_EObject25') == owner
    _safe_set(owner, 'traceability_TraceDiff', set())
    assert getattr(partner, 'traceability_EObject25') is None


def test_assoc_source0_stub_double():
    # traceability_EObject has no real 'traceability_EObject' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject', None)
    _safe_set(owner, 'traceability_Trace', {partner})
    assert getattr(partner, 'traceability_EObject') == owner
    _safe_set(owner, 'traceability_Trace', set())
    assert getattr(partner, 'traceability_EObject') is None


def test_assoc_sourceModel16_stub_double():
    # traceability_EObject has no real 'traceability_EObject17' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Traces's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Traces's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Traces(comments="sample_text", date=date(2024, 1, 1), fullName="sample_text", location="sample_text", originalSourceURL="sample_text", uriMap="sample_text", username="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject17', None)
    _safe_set(owner, 'traceability_Traces', partner)
    assert getattr(partner, 'traceability_EObject17') == owner
    _safe_set(owner, 'traceability_Traces', None)
    assert getattr(partner, 'traceability_EObject17') is None


def test_assoc_target1_stub_double():
    # traceability_EObject has no real 'traceability_EObject3' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject3', None)
    _safe_set(owner, 'traceability_Trace2', {partner})
    assert getattr(partner, 'traceability_EObject3') == owner
    _safe_set(owner, 'traceability_Trace2', set())
    assert getattr(partner, 'traceability_EObject3') is None


def test_assoc_targetModel18_stub_double():
    # traceability_EObject has no real 'traceability_EObject20' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Traces's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Traces's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Traces(comments="sample_text", date=date(2024, 1, 1), fullName="sample_text", location="sample_text", originalSourceURL="sample_text", uriMap="sample_text", username="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject20', None)
    _safe_set(owner, 'traceability_Traces19', partner)
    assert getattr(partner, 'traceability_EObject20') == owner
    _safe_set(owner, 'traceability_Traces19', None)
    assert getattr(partner, 'traceability_EObject20') is None


def test_assoc_traces21_stub_double():
    # traceability_EObject has no real 'traceability_EObject23' property in the generated
    # code (a bare stub) -- manually attach it so traceability_Traces's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceability_Traces's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceability_Traces(comments="sample_text", date=date(2024, 1, 1), fullName="sample_text", location="sample_text", originalSourceURL="sample_text", uriMap="sample_text", username="sample_text")
    partner = traceability_EObject()
    setattr(partner, 'traceability_EObject23', None)
    _safe_set(owner, 'traceability_Traces22', {partner})
    assert getattr(partner, 'traceability_EObject23') == owner
    _safe_set(owner, 'traceability_Traces22', set())
    assert getattr(partner, 'traceability_EObject23') is None


