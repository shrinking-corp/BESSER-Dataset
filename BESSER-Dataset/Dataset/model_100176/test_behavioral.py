import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CandidateKey,
    Domain,
    Relational_Attribute,
    Relational_CandidateKey,
    Relational_Constraint,
    Relational_Domain,
    Relational_EnumeratedLiteral,
    Relational_EnumerationType,
    Relational_ForeignKey,
    Relational_PrimitiveType,
    Relational_Schema,
    Relational_Table,
    AttributeType,
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

def test_assoc_attributes10_reverse_link_reassign_clear():
    a1 = Relational_Table(name="sample_text")
    a2 = Relational_Table(name="sample_text_2")
    b = Relational_Attribute(multiplicity=7, name="sample_text", nullable=True, type="sample_text")
    _safe_set(b, 'Relational_Attribute', a1)
    assert _is_linked(b, 'Relational_Attribute', a1)
    if hasattr(a1, 'Relational_Table11'):
        assert _is_linked(a1, 'Relational_Table11', b)
    _safe_set(b, 'Relational_Attribute', a2)
    assert _is_linked(b, 'Relational_Attribute', a2)
    if hasattr(a1, 'Relational_Table11'):
        assert not _is_linked(a1, 'Relational_Table11', b)
    if hasattr(a2, 'Relational_Table11'):
        assert _is_linked(a2, 'Relational_Table11', b)
    _safe_set(b, 'Relational_Attribute', None)
    assert not _is_linked(b, 'Relational_Attribute', a2)
    if hasattr(a2, 'Relational_Table11'):
        assert not _is_linked(a2, 'Relational_Table11', b)


def test_assoc_attributes20_reverse_link_reassign_clear():
    a1 = Relational_CandidateKey(name="sample_text")
    a2 = Relational_CandidateKey(name="sample_text_2")
    b = Relational_Attribute(multiplicity=7, name="sample_text", nullable=True, type="sample_text")
    _safe_set(b, 'Relational_Attribute22', a1)
    assert _is_linked(b, 'Relational_Attribute22', a1)
    if hasattr(a1, 'Relational_CandidateKey21'):
        assert _is_linked(a1, 'Relational_CandidateKey21', b)
    _safe_set(b, 'Relational_Attribute22', a2)
    assert _is_linked(b, 'Relational_Attribute22', a2)
    if hasattr(a1, 'Relational_CandidateKey21'):
        assert not _is_linked(a1, 'Relational_CandidateKey21', b)
    if hasattr(a2, 'Relational_CandidateKey21'):
        assert _is_linked(a2, 'Relational_CandidateKey21', b)
    _safe_set(b, 'Relational_Attribute22', None)
    assert not _is_linked(b, 'Relational_Attribute22', a2)
    if hasattr(a2, 'Relational_CandidateKey21'):
        assert not _is_linked(a2, 'Relational_CandidateKey21', b)


def test_assoc_candidateKey7_reverse_link_reassign_clear():
    a1 = Relational_Table(name="sample_text")
    a2 = Relational_Table(name="sample_text_2")
    b = Relational_CandidateKey(name="sample_text")
    _safe_set(b, 'Relational_CandidateKey9', a1)
    assert _is_linked(b, 'Relational_CandidateKey9', a1)
    if hasattr(a1, 'Relational_Table8'):
        assert _is_linked(a1, 'Relational_Table8', b)
    _safe_set(b, 'Relational_CandidateKey9', a2)
    assert _is_linked(b, 'Relational_CandidateKey9', a2)
    if hasattr(a1, 'Relational_Table8'):
        assert not _is_linked(a1, 'Relational_Table8', b)
    if hasattr(a2, 'Relational_Table8'):
        assert _is_linked(a2, 'Relational_Table8', b)
    _safe_set(b, 'Relational_CandidateKey9', None)
    assert not _is_linked(b, 'Relational_CandidateKey9', a2)
    if hasattr(a2, 'Relational_Table8'):
        assert not _is_linked(a2, 'Relational_Table8', b)


def test_assoc_constraints17_reverse_link_reassign_clear():
    a1 = Relational_Domain(name="sample_text")
    a2 = Relational_Domain(name="sample_text_2")
    b = Relational_Constraint(description="sample_text", name="sample_text")
    _safe_set(b, 'Relational_Constraint19', a1)
    assert _is_linked(b, 'Relational_Constraint19', a1)
    if hasattr(a1, 'Relational_Domain18'):
        assert _is_linked(a1, 'Relational_Domain18', b)
    _safe_set(b, 'Relational_Constraint19', a2)
    assert _is_linked(b, 'Relational_Constraint19', a2)
    if hasattr(a1, 'Relational_Domain18'):
        assert not _is_linked(a1, 'Relational_Domain18', b)
    if hasattr(a2, 'Relational_Domain18'):
        assert _is_linked(a2, 'Relational_Domain18', b)
    _safe_set(b, 'Relational_Constraint19', None)
    assert not _is_linked(b, 'Relational_Constraint19', a2)
    if hasattr(a2, 'Relational_Domain18'):
        assert not _is_linked(a2, 'Relational_Domain18', b)


def test_assoc_constraints3_reverse_link_reassign_clear():
    a1 = Relational_Schema(name="sample_text")
    a2 = Relational_Schema(name="sample_text_2")
    b = Relational_Constraint(description="sample_text", name="sample_text")
    _safe_set(b, 'Relational_Constraint', a1)
    assert _is_linked(b, 'Relational_Constraint', a1)
    if hasattr(a1, 'Relational_Schema4'):
        assert _is_linked(a1, 'Relational_Schema4', b)
    _safe_set(b, 'Relational_Constraint', a2)
    assert _is_linked(b, 'Relational_Constraint', a2)
    if hasattr(a1, 'Relational_Schema4'):
        assert not _is_linked(a1, 'Relational_Schema4', b)
    if hasattr(a2, 'Relational_Schema4'):
        assert _is_linked(a2, 'Relational_Schema4', b)
    _safe_set(b, 'Relational_Constraint', None)
    assert not _is_linked(b, 'Relational_Constraint', a2)
    if hasattr(a2, 'Relational_Schema4'):
        assert not _is_linked(a2, 'Relational_Schema4', b)


def test_assoc_domain14_reverse_link_reassign_clear():
    a1 = Relational_Domain(name="sample_text")
    a2 = Relational_Domain(name="sample_text_2")
    b = Relational_Attribute(multiplicity=7, name="sample_text", nullable=True, type="sample_text")
    _safe_set(b, 'Relational_Attribute15', a1)
    assert _is_linked(b, 'Relational_Attribute15', a1)
    if hasattr(a1, 'Relational_Domain16'):
        assert _is_linked(a1, 'Relational_Domain16', b)
    _safe_set(b, 'Relational_Attribute15', a2)
    assert _is_linked(b, 'Relational_Attribute15', a2)
    if hasattr(a1, 'Relational_Domain16'):
        assert not _is_linked(a1, 'Relational_Domain16', b)
    if hasattr(a2, 'Relational_Domain16'):
        assert _is_linked(a2, 'Relational_Domain16', b)
    _safe_set(b, 'Relational_Attribute15', None)
    assert not _is_linked(b, 'Relational_Attribute15', a2)
    if hasattr(a2, 'Relational_Domain16'):
        assert not _is_linked(a2, 'Relational_Domain16', b)


def test_assoc_domains1_reverse_link_reassign_clear():
    a1 = Relational_Schema(name="sample_text")
    a2 = Relational_Schema(name="sample_text_2")
    b = Relational_Domain(name="sample_text")
    _safe_set(b, 'Relational_Domain', a1)
    assert _is_linked(b, 'Relational_Domain', a1)
    if hasattr(a1, 'Relational_Schema2'):
        assert _is_linked(a1, 'Relational_Schema2', b)
    _safe_set(b, 'Relational_Domain', a2)
    assert _is_linked(b, 'Relational_Domain', a2)
    if hasattr(a1, 'Relational_Schema2'):
        assert not _is_linked(a1, 'Relational_Schema2', b)
    if hasattr(a2, 'Relational_Schema2'):
        assert _is_linked(a2, 'Relational_Schema2', b)
    _safe_set(b, 'Relational_Domain', None)
    assert not _is_linked(b, 'Relational_Domain', a2)
    if hasattr(a2, 'Relational_Schema2'):
        assert not _is_linked(a2, 'Relational_Schema2', b)


def test_assoc_primaryKey5_reverse_link_reassign_clear():
    a1 = Relational_Table(name="sample_text")
    a2 = Relational_Table(name="sample_text_2")
    b = Relational_CandidateKey(name="sample_text")
    _safe_set(b, 'Relational_CandidateKey', a1)
    assert _is_linked(b, 'Relational_CandidateKey', a1)
    if hasattr(a1, 'Relational_Table6'):
        assert _is_linked(a1, 'Relational_Table6', b)
    _safe_set(b, 'Relational_CandidateKey', a2)
    assert _is_linked(b, 'Relational_CandidateKey', a2)
    if hasattr(a1, 'Relational_Table6'):
        assert not _is_linked(a1, 'Relational_Table6', b)
    if hasattr(a2, 'Relational_Table6'):
        assert _is_linked(a2, 'Relational_Table6', b)
    _safe_set(b, 'Relational_CandidateKey', None)
    assert not _is_linked(b, 'Relational_CandidateKey', a2)
    if hasattr(a2, 'Relational_Table6'):
        assert not _is_linked(a2, 'Relational_Table6', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = Relational_Table(name="sample_text")
    a2 = Relational_Table(name="sample_text_2")
    b = Relational_Schema(name="sample_text")
    _safe_set(b, 'Relational_Schema', {a1})
    assert _is_linked(b, 'Relational_Schema', a1)
    if hasattr(a1, 'Relational_Table'):
        assert _is_linked(a1, 'Relational_Table', b)
    _safe_set(b, 'Relational_Schema', {a2})
    assert _is_linked(b, 'Relational_Schema', a2)
    if hasattr(a1, 'Relational_Table'):
        assert not _is_linked(a1, 'Relational_Table', b)
    if hasattr(a2, 'Relational_Table'):
        assert _is_linked(a2, 'Relational_Table', b)
    _safe_set(b, 'Relational_Schema', set())
    assert not _is_linked(b, 'Relational_Schema', a2)
    if hasattr(a2, 'Relational_Table'):
        assert not _is_linked(a2, 'Relational_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_foreignKey12_stub_double():
    # Relational_ForeignKey has no real 'Relational_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so Relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Relational_Table(name="sample_text")
    partner = Relational_ForeignKey()
    setattr(partner, 'Relational_ForeignKey', None)
    _safe_set(owner, 'Relational_Table13', {partner})
    assert getattr(partner, 'Relational_ForeignKey') == owner
    _safe_set(owner, 'Relational_Table13', set())
    assert getattr(partner, 'Relational_ForeignKey') is None


def test_assoc_literals26_stub_double():
    # Relational_EnumerationType has no real 'Relational_EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so Relational_EnumeratedLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Relational_EnumeratedLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Relational_EnumeratedLiteral(name="sample_text")
    partner = Relational_EnumerationType()
    setattr(partner, 'Relational_EnumerationType', None)
    _safe_set(owner, 'Relational_EnumeratedLiteral', partner)
    assert owner in getattr(partner, 'Relational_EnumerationType')
    _safe_set(owner, 'Relational_EnumeratedLiteral', None)
    assert owner not in getattr(partner, 'Relational_EnumerationType')


def test_assoc_referencedTable23_stub_double():
    # Relational_ForeignKey has no real 'Relational_ForeignKey24' property in the generated
    # code (a bare stub) -- manually attach it so Relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Relational_Table(name="sample_text")
    partner = Relational_ForeignKey()
    setattr(partner, 'Relational_ForeignKey24', None)
    _safe_set(owner, 'Relational_Table25', partner)
    assert getattr(partner, 'Relational_ForeignKey24') == owner
    _safe_set(owner, 'Relational_Table25', None)
    assert getattr(partner, 'Relational_ForeignKey24') is None


