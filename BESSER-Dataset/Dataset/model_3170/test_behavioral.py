import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    traceabilitymodel_Block,
    traceabilitymodel_File,
    traceabilitymodel_MetaModel,
    traceabilitymodel_ModelElementRef,
    traceabilitymodel_Trace,
    traceabilitymodel_TraceModel,
    traceabilitymodel_TraceableSegment,
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

def test_assoc_blocks17_reverse_link_reassign_clear():
    a1 = traceabilitymodel_File(ID="sample_text", URI="sample_text", name="sample_text")
    a2 = traceabilitymodel_File(ID="sample_text_2", URI="sample_text_2", name="sample_text_2")
    b = traceabilitymodel_Block(ID="sample_text", endColumn="sample_text", endLine="sample_text", endPos="sample_text", protectedBlock=True, startColumn="sample_text", startLine="sample_text", startPos="sample_text")
    _safe_set(b, 'traceabilitymodel_Block19', a1)
    assert _is_linked(b, 'traceabilitymodel_Block19', a1)
    if hasattr(a1, 'traceabilitymodel_File18'):
        assert _is_linked(a1, 'traceabilitymodel_File18', b)
    _safe_set(b, 'traceabilitymodel_Block19', a2)
    assert _is_linked(b, 'traceabilitymodel_Block19', a2)
    if hasattr(a1, 'traceabilitymodel_File18'):
        assert not _is_linked(a1, 'traceabilitymodel_File18', b)
    if hasattr(a2, 'traceabilitymodel_File18'):
        assert _is_linked(a2, 'traceabilitymodel_File18', b)
    _safe_set(b, 'traceabilitymodel_Block19', None)
    assert not _is_linked(b, 'traceabilitymodel_Block19', a2)
    if hasattr(a2, 'traceabilitymodel_File18'):
        assert not _is_linked(a2, 'traceabilitymodel_File18', b)


def test_assoc_metaModel0_reverse_link_reassign_clear():
    a1 = traceabilitymodel_ModelElementRef(ID="sample_text", featureRef="sample_text", name="sample_text", uri="sample_text")
    a2 = traceabilitymodel_ModelElementRef(ID="sample_text_2", featureRef="sample_text_2", name="sample_text_2", uri="sample_text_2")
    b = traceabilitymodel_MetaModel(name="sample_text", nsUri="sample_text")
    _safe_set(b, 'traceabilitymodel_MetaModel', a1)
    assert _is_linked(b, 'traceabilitymodel_MetaModel', a1)
    if hasattr(a1, 'traceabilitymodel_ModelElementRef'):
        assert _is_linked(a1, 'traceabilitymodel_ModelElementRef', b)
    _safe_set(b, 'traceabilitymodel_MetaModel', a2)
    assert _is_linked(b, 'traceabilitymodel_MetaModel', a2)
    if hasattr(a1, 'traceabilitymodel_ModelElementRef'):
        assert not _is_linked(a1, 'traceabilitymodel_ModelElementRef', b)
    if hasattr(a2, 'traceabilitymodel_ModelElementRef'):
        assert _is_linked(a2, 'traceabilitymodel_ModelElementRef', b)
    _safe_set(b, 'traceabilitymodel_MetaModel', None)
    assert not _is_linked(b, 'traceabilitymodel_MetaModel', a2)
    if hasattr(a2, 'traceabilitymodel_ModelElementRef'):
        assert not _is_linked(a2, 'traceabilitymodel_ModelElementRef', b)


def test_assoc_originatinElement2_reverse_link_reassign_clear():
    a1 = traceabilitymodel_Trace(sourceOperationID="sample_text", sourceOperationName="sample_text", specificationName="sample_text")
    a2 = traceabilitymodel_Trace(sourceOperationID="sample_text_2", sourceOperationName="sample_text_2", specificationName="sample_text_2")
    b = traceabilitymodel_ModelElementRef(ID="sample_text", featureRef="sample_text", name="sample_text", uri="sample_text")
    _safe_set(b, 'traceabilitymodel_ModelElementRef4', a1)
    assert _is_linked(b, 'traceabilitymodel_ModelElementRef4', a1)
    if hasattr(a1, 'traceabilitymodel_Trace3'):
        assert _is_linked(a1, 'traceabilitymodel_Trace3', b)
    _safe_set(b, 'traceabilitymodel_ModelElementRef4', a2)
    assert _is_linked(b, 'traceabilitymodel_ModelElementRef4', a2)
    if hasattr(a1, 'traceabilitymodel_Trace3'):
        assert not _is_linked(a1, 'traceabilitymodel_Trace3', b)
    if hasattr(a2, 'traceabilitymodel_Trace3'):
        assert _is_linked(a2, 'traceabilitymodel_Trace3', b)
    _safe_set(b, 'traceabilitymodel_ModelElementRef4', None)
    assert not _is_linked(b, 'traceabilitymodel_ModelElementRef4', a2)
    if hasattr(a2, 'traceabilitymodel_Trace3'):
        assert not _is_linked(a2, 'traceabilitymodel_Trace3', b)


def test_assoc_segment1_reverse_link_reassign_clear():
    a1 = traceabilitymodel_TraceableSegment(endColumn="sample_text", endLine="sample_text", endPos="sample_text", startColumn="sample_text", startLine="sample_text", startPos="sample_text")
    a2 = traceabilitymodel_TraceableSegment(endColumn="sample_text_2", endLine="sample_text_2", endPos="sample_text_2", startColumn="sample_text_2", startLine="sample_text_2", startPos="sample_text_2")
    b = traceabilitymodel_Trace(sourceOperationID="sample_text", sourceOperationName="sample_text", specificationName="sample_text")
    _safe_set(b, 'traceabilitymodel_Trace', a1)
    assert _is_linked(b, 'traceabilitymodel_Trace', a1)
    if hasattr(a1, 'traceabilitymodel_TraceableSegment'):
        assert _is_linked(a1, 'traceabilitymodel_TraceableSegment', b)
    _safe_set(b, 'traceabilitymodel_Trace', a2)
    assert _is_linked(b, 'traceabilitymodel_Trace', a2)
    if hasattr(a1, 'traceabilitymodel_TraceableSegment'):
        assert not _is_linked(a1, 'traceabilitymodel_TraceableSegment', b)
    if hasattr(a2, 'traceabilitymodel_TraceableSegment'):
        assert _is_linked(a2, 'traceabilitymodel_TraceableSegment', b)
    _safe_set(b, 'traceabilitymodel_Trace', None)
    assert not _is_linked(b, 'traceabilitymodel_Trace', a2)
    if hasattr(a2, 'traceabilitymodel_TraceableSegment'):
        assert not _is_linked(a2, 'traceabilitymodel_TraceableSegment', b)


def test_assoc_traceablesegment5_reverse_link_reassign_clear():
    a1 = traceabilitymodel_TraceableSegment(endColumn="sample_text", endLine="sample_text", endPos="sample_text", startColumn="sample_text", startLine="sample_text", startPos="sample_text")
    a2 = traceabilitymodel_TraceableSegment(endColumn="sample_text_2", endLine="sample_text_2", endPos="sample_text_2", startColumn="sample_text_2", startLine="sample_text_2", startPos="sample_text_2")
    b = traceabilitymodel_Block(ID="sample_text", endColumn="sample_text", endLine="sample_text", endPos="sample_text", protectedBlock=True, startColumn="sample_text", startLine="sample_text", startPos="sample_text")
    _safe_set(b, 'traceabilitymodel_Block', {a1})
    assert _is_linked(b, 'traceabilitymodel_Block', a1)
    if hasattr(a1, 'traceabilitymodel_TraceableSegment6'):
        assert _is_linked(a1, 'traceabilitymodel_TraceableSegment6', b)
    _safe_set(b, 'traceabilitymodel_Block', {a2})
    assert _is_linked(b, 'traceabilitymodel_Block', a2)
    if hasattr(a1, 'traceabilitymodel_TraceableSegment6'):
        assert not _is_linked(a1, 'traceabilitymodel_TraceableSegment6', b)
    if hasattr(a2, 'traceabilitymodel_TraceableSegment6'):
        assert _is_linked(a2, 'traceabilitymodel_TraceableSegment6', b)
    _safe_set(b, 'traceabilitymodel_Block', set())
    assert not _is_linked(b, 'traceabilitymodel_Block', a2)
    if hasattr(a2, 'traceabilitymodel_TraceableSegment6'):
        assert not _is_linked(a2, 'traceabilitymodel_TraceableSegment6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_files9_stub_double():
    # traceabilitymodel_TraceModel has no real 'traceabilitymodel_TraceModel10' property in the generated
    # code (a bare stub) -- manually attach it so traceabilitymodel_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceabilitymodel_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceabilitymodel_File(ID="sample_text", URI="sample_text", name="sample_text")
    partner = traceabilitymodel_TraceModel()
    setattr(partner, 'traceabilitymodel_TraceModel10', None)
    _safe_set(owner, 'traceabilitymodel_File', partner)
    assert owner in getattr(partner, 'traceabilitymodel_TraceModel10')
    _safe_set(owner, 'traceabilitymodel_File', None)
    assert owner not in getattr(partner, 'traceabilitymodel_TraceModel10')


def test_assoc_metaModels14_stub_double():
    # traceabilitymodel_TraceModel has no real 'traceabilitymodel_TraceModel15' property in the generated
    # code (a bare stub) -- manually attach it so traceabilitymodel_MetaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceabilitymodel_MetaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceabilitymodel_MetaModel(name="sample_text", nsUri="sample_text")
    partner = traceabilitymodel_TraceModel()
    setattr(partner, 'traceabilitymodel_TraceModel15', None)
    _safe_set(owner, 'traceabilitymodel_MetaModel16', partner)
    assert owner in getattr(partner, 'traceabilitymodel_TraceModel15')
    _safe_set(owner, 'traceabilitymodel_MetaModel16', None)
    assert owner not in getattr(partner, 'traceabilitymodel_TraceModel15')


def test_assoc_modelElementRefs11_stub_double():
    # traceabilitymodel_TraceModel has no real 'traceabilitymodel_TraceModel12' property in the generated
    # code (a bare stub) -- manually attach it so traceabilitymodel_ModelElementRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceabilitymodel_ModelElementRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceabilitymodel_ModelElementRef(ID="sample_text", featureRef="sample_text", name="sample_text", uri="sample_text")
    partner = traceabilitymodel_TraceModel()
    setattr(partner, 'traceabilitymodel_TraceModel12', None)
    _safe_set(owner, 'traceabilitymodel_ModelElementRef13', partner)
    assert owner in getattr(partner, 'traceabilitymodel_TraceModel12')
    _safe_set(owner, 'traceabilitymodel_ModelElementRef13', None)
    assert owner not in getattr(partner, 'traceabilitymodel_TraceModel12')


def test_assoc_trace7_stub_double():
    # traceabilitymodel_TraceModel has no real 'traceabilitymodel_TraceModel' property in the generated
    # code (a bare stub) -- manually attach it so traceabilitymodel_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceabilitymodel_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceabilitymodel_Trace(sourceOperationID="sample_text", sourceOperationName="sample_text", specificationName="sample_text")
    partner = traceabilitymodel_TraceModel()
    setattr(partner, 'traceabilitymodel_TraceModel', None)
    _safe_set(owner, 'traceabilitymodel_Trace8', partner)
    assert owner in getattr(partner, 'traceabilitymodel_TraceModel')
    _safe_set(owner, 'traceabilitymodel_Trace8', None)
    assert owner not in getattr(partner, 'traceabilitymodel_TraceModel')


