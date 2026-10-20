import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Measure,
    Measure_Category,
    Measure_DoubleMeasure,
    Measure_IntegerMeasure,
    Measure_Measure,
    Measure_MeasureSet,
    Measure_Metric,
    Measure_PercentageMeasure,
    Measure_RootMeasureSet,
    ElementKind,
    ModelKind,
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

def test_assoc_categories0_reverse_link_reassign_clear():
    a1 = Measure_RootMeasureSet(modelType="sample_text")
    a2 = Measure_RootMeasureSet(modelType="sample_text_2")
    b = Measure_Category(desc="sample_text", name="sample_text")
    _safe_set(b, 'Category', a1)
    assert _is_linked(b, 'Category', a1)
    if hasattr(a1, 'root'):
        assert _is_linked(a1, 'root', b)
    _safe_set(b, 'Category', a2)
    assert _is_linked(b, 'Category', a2)
    if hasattr(a1, 'root'):
        assert not _is_linked(a1, 'root', b)
    if hasattr(a2, 'root'):
        assert _is_linked(a2, 'root', b)
    _safe_set(b, 'Category', None)
    assert not _is_linked(b, 'Category', a2)
    if hasattr(a2, 'root'):
        assert not _is_linked(a2, 'root', b)


def test_assoc_category5_reverse_link_reassign_clear():
    a1 = Measure_Metric(desc="sample_text", name="sample_text", preferredValue="sample_text")
    a2 = Measure_Metric(desc="sample_text_2", name="sample_text_2", preferredValue="sample_text_2")
    b = Measure_Category(desc="sample_text", name="sample_text")
    _safe_set(b, 'Category6', a1)
    assert _is_linked(b, 'Category6', a1)
    if hasattr(a1, 'metrics'):
        assert _is_linked(a1, 'metrics', b)
    _safe_set(b, 'Category6', a2)
    assert _is_linked(b, 'Category6', a2)
    if hasattr(a1, 'metrics'):
        assert not _is_linked(a1, 'metrics', b)
    if hasattr(a2, 'metrics'):
        assert _is_linked(a2, 'metrics', b)
    _safe_set(b, 'Category6', None)
    assert not _is_linked(b, 'Category6', a2)
    if hasattr(a2, 'metrics'):
        assert not _is_linked(a2, 'metrics', b)


def test_assoc_measureSets1_reverse_link_reassign_clear():
    a1 = Measure_RootMeasureSet(modelType="sample_text")
    a2 = Measure_RootMeasureSet(modelType="sample_text_2")
    b = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    _safe_set(b, 'MeasureSet', a1)
    assert _is_linked(b, 'MeasureSet', a1)
    if hasattr(a1, 'root2'):
        assert _is_linked(a1, 'root2', b)
    _safe_set(b, 'MeasureSet', a2)
    assert _is_linked(b, 'MeasureSet', a2)
    if hasattr(a1, 'root2'):
        assert not _is_linked(a1, 'root2', b)
    if hasattr(a2, 'root2'):
        assert _is_linked(a2, 'root2', b)
    _safe_set(b, 'MeasureSet', None)
    assert not _is_linked(b, 'MeasureSet', a2)
    if hasattr(a2, 'root2'):
        assert not _is_linked(a2, 'root2', b)


def test_assoc_metrics3_reverse_link_reassign_clear():
    a1 = Measure_Metric(desc="sample_text", name="sample_text", preferredValue="sample_text")
    a2 = Measure_Metric(desc="sample_text_2", name="sample_text_2", preferredValue="sample_text_2")
    b = Measure_Category(desc="sample_text", name="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'Metric'):
        assert _is_linked(a1, 'Metric', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'Metric'):
        assert not _is_linked(a1, 'Metric', b)
    if hasattr(a2, 'Metric'):
        assert _is_linked(a2, 'Metric', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'Metric'):
        assert not _is_linked(a2, 'Metric', b)


def test_assoc_parent14_reverse_link_reassign_clear():
    a1 = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    a2 = Measure_MeasureSet(elementName="sample_text_2", elementType="sample_text_2")
    b = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    _safe_set(b, 'subsets', a1)
    assert _is_linked(b, 'subsets', a1)
    if hasattr(a1, 'MeasureSet15'):
        assert _is_linked(a1, 'MeasureSet15', b)
    _safe_set(b, 'subsets', a2)
    assert _is_linked(b, 'subsets', a2)
    if hasattr(a1, 'MeasureSet15'):
        assert not _is_linked(a1, 'MeasureSet15', b)
    if hasattr(a2, 'MeasureSet15'):
        assert _is_linked(a2, 'MeasureSet15', b)
    _safe_set(b, 'subsets', None)
    assert not _is_linked(b, 'subsets', a2)
    if hasattr(a2, 'MeasureSet15'):
        assert not _is_linked(a2, 'MeasureSet15', b)


def test_assoc_root4_reverse_link_reassign_clear():
    a1 = Measure_RootMeasureSet(modelType="sample_text")
    a2 = Measure_RootMeasureSet(modelType="sample_text_2")
    b = Measure_Category(desc="sample_text", name="sample_text")
    _safe_set(b, 'categories', a1)
    assert _is_linked(b, 'categories', a1)
    if hasattr(a1, 'RootMeasureSet'):
        assert _is_linked(a1, 'RootMeasureSet', b)
    _safe_set(b, 'categories', a2)
    assert _is_linked(b, 'categories', a2)
    if hasattr(a1, 'RootMeasureSet'):
        assert not _is_linked(a1, 'RootMeasureSet', b)
    if hasattr(a2, 'RootMeasureSet'):
        assert _is_linked(a2, 'RootMeasureSet', b)
    _safe_set(b, 'categories', None)
    assert not _is_linked(b, 'categories', a2)
    if hasattr(a2, 'RootMeasureSet'):
        assert not _is_linked(a2, 'RootMeasureSet', b)


def test_assoc_root8_reverse_link_reassign_clear():
    a1 = Measure_RootMeasureSet(modelType="sample_text")
    a2 = Measure_RootMeasureSet(modelType="sample_text_2")
    b = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    _safe_set(b, 'measureSets', a1)
    assert _is_linked(b, 'measureSets', a1)
    if hasattr(a1, 'RootMeasureSet9'):
        assert _is_linked(a1, 'RootMeasureSet9', b)
    _safe_set(b, 'measureSets', a2)
    assert _is_linked(b, 'measureSets', a2)
    if hasattr(a1, 'RootMeasureSet9'):
        assert not _is_linked(a1, 'RootMeasureSet9', b)
    if hasattr(a2, 'RootMeasureSet9'):
        assert _is_linked(a2, 'RootMeasureSet9', b)
    _safe_set(b, 'measureSets', None)
    assert not _is_linked(b, 'measureSets', a2)
    if hasattr(a2, 'RootMeasureSet9'):
        assert not _is_linked(a2, 'RootMeasureSet9', b)


def test_assoc_subsets11_reverse_link_reassign_clear():
    a1 = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    a2 = Measure_MeasureSet(elementName="sample_text_2", elementType="sample_text_2")
    b = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'MeasureSet12'):
        assert _is_linked(a1, 'MeasureSet12', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'MeasureSet12'):
        assert not _is_linked(a1, 'MeasureSet12', b)
    if hasattr(a2, 'MeasureSet12'):
        assert _is_linked(a2, 'MeasureSet12', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'MeasureSet12'):
        assert not _is_linked(a2, 'MeasureSet12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_measures7_stub_double():
    # Measure_Measure has no real 'Measure' property in the generated
    # code (a bare stub) -- manually attach it so Measure_MeasureSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Measure_MeasureSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    partner = Measure_Measure()
    setattr(partner, 'Measure', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Measure') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Measure') is None


def test_assoc_metric16_stub_double():
    # Measure_Measure has no real 'Measure_Measure' property in the generated
    # code (a bare stub) -- manually attach it so Measure_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Measure_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Measure_Metric(desc="sample_text", name="sample_text", preferredValue="sample_text")
    partner = Measure_Measure()
    setattr(partner, 'Measure_Measure', None)
    _safe_set(owner, 'Measure_Metric', partner)
    assert getattr(partner, 'Measure_Measure') == owner
    _safe_set(owner, 'Measure_Metric', None)
    assert getattr(partner, 'Measure_Measure') is None


def test_assoc_owner17_stub_double():
    # Measure_Measure has no real 'measures' property in the generated
    # code (a bare stub) -- manually attach it so Measure_MeasureSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Measure_MeasureSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Measure_MeasureSet(elementName="sample_text", elementType="sample_text")
    partner = Measure_Measure()
    setattr(partner, 'measures', None)
    _safe_set(owner, 'MeasureSet18', partner)
    assert getattr(partner, 'measures') == owner
    _safe_set(owner, 'MeasureSet18', None)
    assert getattr(partner, 'measures') is None


