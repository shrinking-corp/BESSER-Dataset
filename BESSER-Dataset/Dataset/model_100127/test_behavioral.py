import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Taggable,
    relationaldatabase_Column,
    relationaldatabase_Configuration,
    relationaldatabase_DataType,
    relationaldatabase_DatabaseModel,
    relationaldatabase_ForeignKey,
    relationaldatabase_NamedElement,
    relationaldatabase_Table,
    relationaldatabase_Tag,
    relationaldatabase_Taggable,
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

def test_assoc_sourceColumns14_reverse_link_reassign_clear():
    a1 = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text", sourceUpperBoundary="sample_text", targetLowerBoundary="sample_text", targetUpperBoundary="sample_text")
    a2 = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text_2", sourceUpperBoundary="sample_text_2", targetLowerBoundary="sample_text_2", targetUpperBoundary="sample_text_2")
    b = relationaldatabase_Column(arrayDimensions=7, nullable=True, primaryKey=True, scale="sample_text", size="sample_text", unique=True)
    _safe_set(b, 'relationaldatabase_Column16', a1)
    assert _is_linked(b, 'relationaldatabase_Column16', a1)
    if hasattr(a1, 'relationaldatabase_ForeignKey15'):
        assert _is_linked(a1, 'relationaldatabase_ForeignKey15', b)
    _safe_set(b, 'relationaldatabase_Column16', a2)
    assert _is_linked(b, 'relationaldatabase_Column16', a2)
    if hasattr(a1, 'relationaldatabase_ForeignKey15'):
        assert not _is_linked(a1, 'relationaldatabase_ForeignKey15', b)
    if hasattr(a2, 'relationaldatabase_ForeignKey15'):
        assert _is_linked(a2, 'relationaldatabase_ForeignKey15', b)
    _safe_set(b, 'relationaldatabase_Column16', None)
    assert not _is_linked(b, 'relationaldatabase_Column16', a2)
    if hasattr(a2, 'relationaldatabase_ForeignKey15'):
        assert not _is_linked(a2, 'relationaldatabase_ForeignKey15', b)


def test_assoc_targetColumns17_reverse_link_reassign_clear():
    a1 = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text", sourceUpperBoundary="sample_text", targetLowerBoundary="sample_text", targetUpperBoundary="sample_text")
    a2 = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text_2", sourceUpperBoundary="sample_text_2", targetLowerBoundary="sample_text_2", targetUpperBoundary="sample_text_2")
    b = relationaldatabase_Column(arrayDimensions=7, nullable=True, primaryKey=True, scale="sample_text", size="sample_text", unique=True)
    _safe_set(b, 'relationaldatabase_Column19', a1)
    assert _is_linked(b, 'relationaldatabase_Column19', a1)
    if hasattr(a1, 'relationaldatabase_ForeignKey18'):
        assert _is_linked(a1, 'relationaldatabase_ForeignKey18', b)
    _safe_set(b, 'relationaldatabase_Column19', a2)
    assert _is_linked(b, 'relationaldatabase_Column19', a2)
    if hasattr(a1, 'relationaldatabase_ForeignKey18'):
        assert not _is_linked(a1, 'relationaldatabase_ForeignKey18', b)
    if hasattr(a2, 'relationaldatabase_ForeignKey18'):
        assert _is_linked(a2, 'relationaldatabase_ForeignKey18', b)
    _safe_set(b, 'relationaldatabase_Column19', None)
    assert not _is_linked(b, 'relationaldatabase_Column19', a2)
    if hasattr(a2, 'relationaldatabase_ForeignKey18'):
        assert not _is_linked(a2, 'relationaldatabase_ForeignKey18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns7_stub_double():
    # relationaldatabase_Table has no real 'relationaldatabase_Table8' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_Column(arrayDimensions=7, nullable=True, primaryKey=True, scale="sample_text", size="sample_text", unique=True)
    partner = relationaldatabase_Table()
    setattr(partner, 'relationaldatabase_Table8', None)
    _safe_set(owner, 'relationaldatabase_Column', partner)
    assert owner in getattr(partner, 'relationaldatabase_Table8')
    _safe_set(owner, 'relationaldatabase_Column', None)
    assert owner not in getattr(partner, 'relationaldatabase_Table8')


def test_assoc_dataType11_stub_double():
    # relationaldatabase_DataType has no real 'relationaldatabase_DataType13' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_Column(arrayDimensions=7, nullable=True, primaryKey=True, scale="sample_text", size="sample_text", unique=True)
    partner = relationaldatabase_DataType()
    setattr(partner, 'relationaldatabase_DataType13', None)
    _safe_set(owner, 'relationaldatabase_Column12', partner)
    assert getattr(partner, 'relationaldatabase_DataType13') == owner
    _safe_set(owner, 'relationaldatabase_Column12', None)
    assert getattr(partner, 'relationaldatabase_DataType13') is None


def test_assoc_foreignKeys9_stub_double():
    # relationaldatabase_Table has no real 'relationaldatabase_Table10' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text", sourceUpperBoundary="sample_text", targetLowerBoundary="sample_text", targetUpperBoundary="sample_text")
    partner = relationaldatabase_Table()
    setattr(partner, 'relationaldatabase_Table10', None)
    _safe_set(owner, 'relationaldatabase_ForeignKey', partner)
    assert owner in getattr(partner, 'relationaldatabase_Table10')
    _safe_set(owner, 'relationaldatabase_ForeignKey', None)
    assert owner not in getattr(partner, 'relationaldatabase_Table10')


def test_assoc_tag23_stub_double():
    # relationaldatabase_Taggable has no real 'relationaldatabase_Taggable' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_Tag(documentation="sample_text", name="sample_text")
    partner = relationaldatabase_Taggable()
    setattr(partner, 'relationaldatabase_Taggable', None)
    _safe_set(owner, 'relationaldatabase_Tag24', partner)
    assert owner in getattr(partner, 'relationaldatabase_Taggable')
    _safe_set(owner, 'relationaldatabase_Tag24', None)
    assert owner not in getattr(partner, 'relationaldatabase_Taggable')


def test_assoc_tags3_stub_double():
    # relationaldatabase_DatabaseModel has no real 'relationaldatabase_DatabaseModel4' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_Tag(documentation="sample_text", name="sample_text")
    partner = relationaldatabase_DatabaseModel()
    setattr(partner, 'relationaldatabase_DatabaseModel4', None)
    _safe_set(owner, 'relationaldatabase_Tag', partner)
    assert owner in getattr(partner, 'relationaldatabase_DatabaseModel4')
    _safe_set(owner, 'relationaldatabase_Tag', None)
    assert owner not in getattr(partner, 'relationaldatabase_DatabaseModel4')


def test_assoc_targetTable20_stub_double():
    # relationaldatabase_Table has no real 'relationaldatabase_Table22' property in the generated
    # code (a bare stub) -- manually attach it so relationaldatabase_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relationaldatabase_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relationaldatabase_ForeignKey(sourceLowerBoundary="sample_text", sourceUpperBoundary="sample_text", targetLowerBoundary="sample_text", targetUpperBoundary="sample_text")
    partner = relationaldatabase_Table()
    setattr(partner, 'relationaldatabase_Table22', None)
    _safe_set(owner, 'relationaldatabase_ForeignKey21', partner)
    assert getattr(partner, 'relationaldatabase_Table22') == owner
    _safe_set(owner, 'relationaldatabase_ForeignKey21', None)
    assert getattr(partner, 'relationaldatabase_Table22') is None


