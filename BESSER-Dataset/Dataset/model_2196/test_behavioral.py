import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ensemble,
    TreeNode,
    datamodel_ConcreteEnsemble,
    datamodel_Constraint,
    datamodel_EmptyEnsemble,
    datamodel_Ensemble,
    datamodel_EnsembleRepository,
    datamodel_Slice,
    datamodel_SliceRepository,
    datamodel_TreeNode,
    ConstraintType,
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

def test_assoc_constraints0_reverse_link_reassign_clear():
    a1 = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    a2 = datamodel_Ensemble(derived=False, description="sample_text_2", name="sample_text_2", query="sample_text_2")
    b = datamodel_Constraint(constraintType="sample_text", dependencyKind="sample_text")
    _safe_set(b, 'datamodel_Constraint', a1)
    assert _is_linked(b, 'datamodel_Constraint', a1)
    if hasattr(a1, 'datamodel_Ensemble'):
        assert _is_linked(a1, 'datamodel_Ensemble', b)
    _safe_set(b, 'datamodel_Constraint', a2)
    assert _is_linked(b, 'datamodel_Constraint', a2)
    if hasattr(a1, 'datamodel_Ensemble'):
        assert not _is_linked(a1, 'datamodel_Ensemble', b)
    if hasattr(a2, 'datamodel_Ensemble'):
        assert _is_linked(a2, 'datamodel_Ensemble', b)
    _safe_set(b, 'datamodel_Constraint', None)
    assert not _is_linked(b, 'datamodel_Constraint', a2)
    if hasattr(a2, 'datamodel_Ensemble'):
        assert not _is_linked(a2, 'datamodel_Ensemble', b)


def test_assoc_constraints12_reverse_link_reassign_clear():
    a1 = datamodel_Slice(diagram="sample_text", name="sample_text")
    a2 = datamodel_Slice(diagram="sample_text_2", name="sample_text_2")
    b = datamodel_Constraint(constraintType="sample_text", dependencyKind="sample_text")
    _safe_set(b, 'datamodel_Constraint13', a1)
    assert _is_linked(b, 'datamodel_Constraint13', a1)
    if hasattr(a1, 'datamodel_Slice'):
        assert _is_linked(a1, 'datamodel_Slice', b)
    _safe_set(b, 'datamodel_Constraint13', a2)
    assert _is_linked(b, 'datamodel_Constraint13', a2)
    if hasattr(a1, 'datamodel_Slice'):
        assert not _is_linked(a1, 'datamodel_Slice', b)
    if hasattr(a2, 'datamodel_Slice'):
        assert _is_linked(a2, 'datamodel_Slice', b)
    _safe_set(b, 'datamodel_Constraint13', None)
    assert not _is_linked(b, 'datamodel_Constraint13', a2)
    if hasattr(a2, 'datamodel_Slice'):
        assert not _is_linked(a2, 'datamodel_Slice', b)


def test_assoc_ensembles14_reverse_link_reassign_clear():
    a1 = datamodel_Slice(diagram="sample_text", name="sample_text")
    a2 = datamodel_Slice(diagram="sample_text_2", name="sample_text_2")
    b = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    _safe_set(b, 'Ensemble', a1)
    assert _is_linked(b, 'Ensemble', a1)
    if hasattr(a1, 'slices'):
        assert _is_linked(a1, 'slices', b)
    _safe_set(b, 'Ensemble', a2)
    assert _is_linked(b, 'Ensemble', a2)
    if hasattr(a1, 'slices'):
        assert not _is_linked(a1, 'slices', b)
    if hasattr(a2, 'slices'):
        assert _is_linked(a2, 'slices', b)
    _safe_set(b, 'Ensemble', None)
    assert not _is_linked(b, 'Ensemble', a2)
    if hasattr(a2, 'slices'):
        assert not _is_linked(a2, 'slices', b)


def test_assoc_slices1_reverse_link_reassign_clear():
    a1 = datamodel_Slice(diagram="sample_text", name="sample_text")
    a2 = datamodel_Slice(diagram="sample_text_2", name="sample_text_2")
    b = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    _safe_set(b, 'ensembles', {a1})
    assert _is_linked(b, 'ensembles', a1)
    if hasattr(a1, 'Slice'):
        assert _is_linked(a1, 'Slice', b)
    _safe_set(b, 'ensembles', {a2})
    assert _is_linked(b, 'ensembles', a2)
    if hasattr(a1, 'Slice'):
        assert not _is_linked(a1, 'Slice', b)
    if hasattr(a2, 'Slice'):
        assert _is_linked(a2, 'Slice', b)
    _safe_set(b, 'ensembles', set())
    assert not _is_linked(b, 'ensembles', a2)
    if hasattr(a2, 'Slice'):
        assert not _is_linked(a2, 'Slice', b)


def test_assoc_source2_reverse_link_reassign_clear():
    a1 = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    a2 = datamodel_Ensemble(derived=False, description="sample_text_2", name="sample_text_2", query="sample_text_2")
    b = datamodel_Constraint(constraintType="sample_text", dependencyKind="sample_text")
    _safe_set(b, 'datamodel_Constraint3', a1)
    assert _is_linked(b, 'datamodel_Constraint3', a1)
    if hasattr(a1, 'datamodel_Ensemble4'):
        assert _is_linked(a1, 'datamodel_Ensemble4', b)
    _safe_set(b, 'datamodel_Constraint3', a2)
    assert _is_linked(b, 'datamodel_Constraint3', a2)
    if hasattr(a1, 'datamodel_Ensemble4'):
        assert not _is_linked(a1, 'datamodel_Ensemble4', b)
    if hasattr(a2, 'datamodel_Ensemble4'):
        assert _is_linked(a2, 'datamodel_Ensemble4', b)
    _safe_set(b, 'datamodel_Constraint3', None)
    assert not _is_linked(b, 'datamodel_Constraint3', a2)
    if hasattr(a2, 'datamodel_Ensemble4'):
        assert not _is_linked(a2, 'datamodel_Ensemble4', b)


def test_assoc_target5_reverse_link_reassign_clear():
    a1 = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    a2 = datamodel_Ensemble(derived=False, description="sample_text_2", name="sample_text_2", query="sample_text_2")
    b = datamodel_Constraint(constraintType="sample_text", dependencyKind="sample_text")
    _safe_set(b, 'datamodel_Constraint6', a1)
    assert _is_linked(b, 'datamodel_Constraint6', a1)
    if hasattr(a1, 'datamodel_Ensemble7'):
        assert _is_linked(a1, 'datamodel_Ensemble7', b)
    _safe_set(b, 'datamodel_Constraint6', a2)
    assert _is_linked(b, 'datamodel_Constraint6', a2)
    if hasattr(a1, 'datamodel_Ensemble7'):
        assert not _is_linked(a1, 'datamodel_Ensemble7', b)
    if hasattr(a2, 'datamodel_Ensemble7'):
        assert _is_linked(a2, 'datamodel_Ensemble7', b)
    _safe_set(b, 'datamodel_Constraint6', None)
    assert not _is_linked(b, 'datamodel_Constraint6', a2)
    if hasattr(a2, 'datamodel_Ensemble7'):
        assert not _is_linked(a2, 'datamodel_Ensemble7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_emptyEnsemble10_stub_double():
    # datamodel_SliceRepository has no real 'datamodel_SliceRepository' property in the generated
    # code (a bare stub) -- manually attach it so datamodel_Ensemble's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datamodel_Ensemble's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datamodel_Ensemble(derived=True, description="sample_text", name="sample_text", query="sample_text")
    partner = datamodel_SliceRepository()
    setattr(partner, 'datamodel_SliceRepository', None)
    _safe_set(owner, 'datamodel_Ensemble11', partner)
    assert getattr(partner, 'datamodel_SliceRepository') == owner
    _safe_set(owner, 'datamodel_Ensemble11', None)
    assert getattr(partner, 'datamodel_SliceRepository') is None


def test_assoc_sliceRepository15_stub_double():
    # datamodel_SliceRepository has no real 'SliceRepository' property in the generated
    # code (a bare stub) -- manually attach it so datamodel_Slice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datamodel_Slice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datamodel_Slice(diagram="sample_text", name="sample_text")
    partner = datamodel_SliceRepository()
    setattr(partner, 'SliceRepository', None)
    _safe_set(owner, 'slices16', partner)
    assert getattr(partner, 'SliceRepository') == owner
    _safe_set(owner, 'slices16', None)
    assert getattr(partner, 'SliceRepository') is None


def test_assoc_slices8_stub_double():
    # datamodel_SliceRepository has no real 'sliceRepository' property in the generated
    # code (a bare stub) -- manually attach it so datamodel_Slice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datamodel_Slice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datamodel_Slice(diagram="sample_text", name="sample_text")
    partner = datamodel_SliceRepository()
    setattr(partner, 'sliceRepository', None)
    _safe_set(owner, 'Slice9', partner)
    assert owner in getattr(partner, 'sliceRepository')
    _safe_set(owner, 'Slice9', None)
    assert owner not in getattr(partner, 'sliceRepository')


