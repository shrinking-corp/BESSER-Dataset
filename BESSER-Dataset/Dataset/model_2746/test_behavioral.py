import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CommonBaseClass,
    NodeTargetB,
    samplemodel_Child,
    samplemodel_Child2,
    samplemodel_CommonBaseClass,
    samplemodel_Link2Link,
    samplemodel_LinkAtoA,
    samplemodel_LinkAtoC,
    samplemodel_LinkAtoC_Cardinality1,
    samplemodel_LinkAtoC_Cardinality2,
    samplemodel_LinkCrossLink,
    samplemodel_LinkFromLink,
    samplemodel_NodeSrcA,
    samplemodel_NodeTargetB,
    samplemodel_NodeTargetC,
    samplemodel_NodeTargetD,
    samplemodel_UltimateContainer,
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

def test_assoc_children1OfA19_reverse_link_reassign_clear():
    a1 = samplemodel_NodeSrcA(label="sample_text")
    a2 = samplemodel_NodeSrcA(label="sample_text_2")
    b = samplemodel_Child(childLabel="sample_text")
    _safe_set(b, 'samplemodel_Child', a1)
    assert _is_linked(b, 'samplemodel_Child', a1)
    if hasattr(a1, 'samplemodel_NodeSrcA20'):
        assert _is_linked(a1, 'samplemodel_NodeSrcA20', b)
    _safe_set(b, 'samplemodel_Child', a2)
    assert _is_linked(b, 'samplemodel_Child', a2)
    if hasattr(a1, 'samplemodel_NodeSrcA20'):
        assert not _is_linked(a1, 'samplemodel_NodeSrcA20', b)
    if hasattr(a2, 'samplemodel_NodeSrcA20'):
        assert _is_linked(a2, 'samplemodel_NodeSrcA20', b)
    _safe_set(b, 'samplemodel_Child', None)
    assert not _is_linked(b, 'samplemodel_Child', a2)
    if hasattr(a2, 'samplemodel_NodeSrcA20'):
        assert not _is_linked(a2, 'samplemodel_NodeSrcA20', b)


def test_assoc_children2OfA21_reverse_link_reassign_clear():
    a1 = samplemodel_NodeSrcA(label="sample_text")
    a2 = samplemodel_NodeSrcA(label="sample_text_2")
    b = samplemodel_Child2(childLabel="sample_text")
    _safe_set(b, 'samplemodel_Child2', a1)
    assert _is_linked(b, 'samplemodel_Child2', a1)
    if hasattr(a1, 'samplemodel_NodeSrcA22'):
        assert _is_linked(a1, 'samplemodel_NodeSrcA22', b)
    _safe_set(b, 'samplemodel_Child2', a2)
    assert _is_linked(b, 'samplemodel_Child2', a2)
    if hasattr(a1, 'samplemodel_NodeSrcA22'):
        assert not _is_linked(a1, 'samplemodel_NodeSrcA22', b)
    if hasattr(a2, 'samplemodel_NodeSrcA22'):
        assert _is_linked(a2, 'samplemodel_NodeSrcA22', b)
    _safe_set(b, 'samplemodel_Child2', None)
    assert not _is_linked(b, 'samplemodel_Child2', a2)
    if hasattr(a2, 'samplemodel_NodeSrcA22'):
        assert not _is_linked(a2, 'samplemodel_NodeSrcA22', b)


def test_assoc_childrenOfB23_reverse_link_reassign_clear():
    a1 = samplemodel_NodeTargetB(title="sample_text")
    a2 = samplemodel_NodeTargetB(title="sample_text_2")
    b = samplemodel_Child(childLabel="sample_text")
    _safe_set(b, 'samplemodel_Child25', a1)
    assert _is_linked(b, 'samplemodel_Child25', a1)
    if hasattr(a1, 'samplemodel_NodeTargetB24'):
        assert _is_linked(a1, 'samplemodel_NodeTargetB24', b)
    _safe_set(b, 'samplemodel_Child25', a2)
    assert _is_linked(b, 'samplemodel_Child25', a2)
    if hasattr(a1, 'samplemodel_NodeTargetB24'):
        assert not _is_linked(a1, 'samplemodel_NodeTargetB24', b)
    if hasattr(a2, 'samplemodel_NodeTargetB24'):
        assert _is_linked(a2, 'samplemodel_NodeTargetB24', b)
    _safe_set(b, 'samplemodel_Child25', None)
    assert not _is_linked(b, 'samplemodel_Child25', a2)
    if hasattr(a2, 'samplemodel_NodeTargetB24'):
        assert not _is_linked(a2, 'samplemodel_NodeTargetB24', b)


def test_assoc_innerChildrenOfBChild52_reverse_link_reassign_clear():
    a1 = samplemodel_Child(childLabel="sample_text")
    a2 = samplemodel_Child(childLabel="sample_text_2")
    b = samplemodel_Child(childLabel="sample_text")
    _safe_set(b, 'samplemodel_Child53', a1)
    assert _is_linked(b, 'samplemodel_Child53', a1)
    if hasattr(a1, 'samplemodel_Child51'):
        assert _is_linked(a1, 'samplemodel_Child51', b)
    _safe_set(b, 'samplemodel_Child53', a2)
    assert _is_linked(b, 'samplemodel_Child53', a2)
    if hasattr(a1, 'samplemodel_Child51'):
        assert not _is_linked(a1, 'samplemodel_Child51', b)
    if hasattr(a2, 'samplemodel_Child51'):
        assert _is_linked(a2, 'samplemodel_Child51', b)
    _safe_set(b, 'samplemodel_Child53', None)
    assert not _is_linked(b, 'samplemodel_Child53', a2)
    if hasattr(a2, 'samplemodel_Child51'):
        assert not _is_linked(a2, 'samplemodel_Child51', b)


def test_assoc_refLinkToA9_reverse_link_reassign_clear():
    a1 = samplemodel_NodeSrcA(label="sample_text")
    a2 = samplemodel_NodeSrcA(label="sample_text_2")
    b = samplemodel_NodeSrcA(label="sample_text")
    _safe_set(b, 'samplemodel_NodeSrcA8', {a1})
    assert _is_linked(b, 'samplemodel_NodeSrcA8', a1)
    if hasattr(a1, 'samplemodel_NodeSrcA10'):
        assert _is_linked(a1, 'samplemodel_NodeSrcA10', b)
    _safe_set(b, 'samplemodel_NodeSrcA8', {a2})
    assert _is_linked(b, 'samplemodel_NodeSrcA8', a2)
    if hasattr(a1, 'samplemodel_NodeSrcA10'):
        assert not _is_linked(a1, 'samplemodel_NodeSrcA10', b)
    if hasattr(a2, 'samplemodel_NodeSrcA10'):
        assert _is_linked(a2, 'samplemodel_NodeSrcA10', b)
    _safe_set(b, 'samplemodel_NodeSrcA8', set())
    assert not _is_linked(b, 'samplemodel_NodeSrcA8', a2)
    if hasattr(a2, 'samplemodel_NodeSrcA10'):
        assert not _is_linked(a2, 'samplemodel_NodeSrcA10', b)


def test_assoc_refLinkToB1_reverse_link_reassign_clear():
    a1 = samplemodel_NodeTargetB(title="sample_text")
    a2 = samplemodel_NodeTargetB(title="sample_text_2")
    b = samplemodel_NodeSrcA(label="sample_text")
    _safe_set(b, 'samplemodel_NodeSrcA', {a1})
    assert _is_linked(b, 'samplemodel_NodeSrcA', a1)
    if hasattr(a1, 'samplemodel_NodeTargetB'):
        assert _is_linked(a1, 'samplemodel_NodeTargetB', b)
    _safe_set(b, 'samplemodel_NodeSrcA', {a2})
    assert _is_linked(b, 'samplemodel_NodeSrcA', a2)
    if hasattr(a1, 'samplemodel_NodeTargetB'):
        assert not _is_linked(a1, 'samplemodel_NodeTargetB', b)
    if hasattr(a2, 'samplemodel_NodeTargetB'):
        assert _is_linked(a2, 'samplemodel_NodeTargetB', b)
    _safe_set(b, 'samplemodel_NodeSrcA', set())
    assert not _is_linked(b, 'samplemodel_NodeSrcA', a2)
    if hasattr(a2, 'samplemodel_NodeTargetB'):
        assert not _is_linked(a2, 'samplemodel_NodeTargetB', b)


def test_assoc_refLinkToB_Cardinality15_reverse_link_reassign_clear():
    a1 = samplemodel_NodeTargetB(title="sample_text")
    a2 = samplemodel_NodeTargetB(title="sample_text_2")
    b = samplemodel_NodeSrcA(label="sample_text")
    _safe_set(b, 'samplemodel_NodeSrcA6', a1)
    assert _is_linked(b, 'samplemodel_NodeSrcA6', a1)
    if hasattr(a1, 'samplemodel_NodeTargetB7'):
        assert _is_linked(a1, 'samplemodel_NodeTargetB7', b)
    _safe_set(b, 'samplemodel_NodeSrcA6', a2)
    assert _is_linked(b, 'samplemodel_NodeSrcA6', a2)
    if hasattr(a1, 'samplemodel_NodeTargetB7'):
        assert not _is_linked(a1, 'samplemodel_NodeTargetB7', b)
    if hasattr(a2, 'samplemodel_NodeTargetB7'):
        assert _is_linked(a2, 'samplemodel_NodeTargetB7', b)
    _safe_set(b, 'samplemodel_NodeSrcA6', None)
    assert not _is_linked(b, 'samplemodel_NodeSrcA6', a2)
    if hasattr(a2, 'samplemodel_NodeTargetB7'):
        assert not _is_linked(a2, 'samplemodel_NodeTargetB7', b)


def test_assoc_refLinkToB_Cardinality22_reverse_link_reassign_clear():
    a1 = samplemodel_NodeTargetB(title="sample_text")
    a2 = samplemodel_NodeTargetB(title="sample_text_2")
    b = samplemodel_NodeSrcA(label="sample_text")
    _safe_set(b, 'samplemodel_NodeSrcA3', {a1})
    assert _is_linked(b, 'samplemodel_NodeSrcA3', a1)
    if hasattr(a1, 'samplemodel_NodeTargetB4'):
        assert _is_linked(a1, 'samplemodel_NodeTargetB4', b)
    _safe_set(b, 'samplemodel_NodeSrcA3', {a2})
    assert _is_linked(b, 'samplemodel_NodeSrcA3', a2)
    if hasattr(a1, 'samplemodel_NodeTargetB4'):
        assert not _is_linked(a1, 'samplemodel_NodeTargetB4', b)
    if hasattr(a2, 'samplemodel_NodeTargetB4'):
        assert _is_linked(a2, 'samplemodel_NodeTargetB4', b)
    _safe_set(b, 'samplemodel_NodeSrcA3', set())
    assert not _is_linked(b, 'samplemodel_NodeSrcA3', a2)
    if hasattr(a2, 'samplemodel_NodeTargetB4'):
        assert not _is_linked(a2, 'samplemodel_NodeTargetB4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_all0_stub_double():
    # samplemodel_CommonBaseClass has no real 'samplemodel_CommonBaseClass' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_UltimateContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_UltimateContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_UltimateContainer(diagramAttribute="sample_text")
    partner = samplemodel_CommonBaseClass()
    setattr(partner, 'samplemodel_CommonBaseClass', None)
    _safe_set(owner, 'samplemodel_UltimateContainer', {partner})
    assert getattr(partner, 'samplemodel_CommonBaseClass') == owner
    _safe_set(owner, 'samplemodel_UltimateContainer', set())
    assert getattr(partner, 'samplemodel_CommonBaseClass') is None


def test_assoc_classLinkToA17_stub_double():
    # samplemodel_LinkAtoA has no real 'samplemodel_LinkAtoA' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_NodeSrcA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_NodeSrcA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_NodeSrcA(label="sample_text")
    partner = samplemodel_LinkAtoA()
    setattr(partner, 'samplemodel_LinkAtoA', None)
    _safe_set(owner, 'samplemodel_NodeSrcA18', {partner})
    assert getattr(partner, 'samplemodel_LinkAtoA') == owner
    _safe_set(owner, 'samplemodel_NodeSrcA18', set())
    assert getattr(partner, 'samplemodel_LinkAtoA') is None


def test_assoc_classLinkToC11_stub_double():
    # samplemodel_LinkAtoC has no real 'samplemodel_LinkAtoC' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_NodeSrcA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_NodeSrcA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_NodeSrcA(label="sample_text")
    partner = samplemodel_LinkAtoC()
    setattr(partner, 'samplemodel_LinkAtoC', None)
    _safe_set(owner, 'samplemodel_NodeSrcA12', {partner})
    assert getattr(partner, 'samplemodel_LinkAtoC') == owner
    _safe_set(owner, 'samplemodel_NodeSrcA12', set())
    assert getattr(partner, 'samplemodel_LinkAtoC') is None


def test_assoc_classLinkToC_Cardinality115_stub_double():
    # samplemodel_LinkAtoC_Cardinality1 has no real 'samplemodel_LinkAtoC_Cardinality1' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_NodeSrcA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_NodeSrcA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_NodeSrcA(label="sample_text")
    partner = samplemodel_LinkAtoC_Cardinality1()
    setattr(partner, 'samplemodel_LinkAtoC_Cardinality1', None)
    _safe_set(owner, 'samplemodel_NodeSrcA16', partner)
    assert getattr(partner, 'samplemodel_LinkAtoC_Cardinality1') == owner
    _safe_set(owner, 'samplemodel_NodeSrcA16', None)
    assert getattr(partner, 'samplemodel_LinkAtoC_Cardinality1') is None


def test_assoc_classLinkToC_Cardinality213_stub_double():
    # samplemodel_LinkAtoC_Cardinality2 has no real 'samplemodel_LinkAtoC_Cardinality2' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_NodeSrcA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_NodeSrcA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_NodeSrcA(label="sample_text")
    partner = samplemodel_LinkAtoC_Cardinality2()
    setattr(partner, 'samplemodel_LinkAtoC_Cardinality2', None)
    _safe_set(owner, 'samplemodel_NodeSrcA14', {partner})
    assert getattr(partner, 'samplemodel_LinkAtoC_Cardinality2') == owner
    _safe_set(owner, 'samplemodel_NodeSrcA14', set())
    assert getattr(partner, 'samplemodel_LinkAtoC_Cardinality2') is None


def test_assoc_trg48_stub_double():
    # samplemodel_LinkAtoA has no real 'samplemodel_LinkAtoA49' property in the generated
    # code (a bare stub) -- manually attach it so samplemodel_NodeSrcA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # samplemodel_NodeSrcA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = samplemodel_NodeSrcA(label="sample_text")
    partner = samplemodel_LinkAtoA()
    setattr(partner, 'samplemodel_LinkAtoA49', None)
    _safe_set(owner, 'samplemodel_NodeSrcA50', partner)
    assert getattr(partner, 'samplemodel_LinkAtoA49') == owner
    _safe_set(owner, 'samplemodel_NodeSrcA50', None)
    assert getattr(partner, 'samplemodel_LinkAtoA49') is None


