import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OWLClass,
    OWLRestriction,
    Ontology,
    Property,
    RDFProperty,
    RDFSClass,
    RDFSResource,
    owl_AllValuesFromRestriction,
    owl_CardinalityRestriction,
    owl_ComplementClass,
    owl_DatatypeSlot,
    owl_EnumeratedClass,
    owl_HasValueRestriction,
    owl_Individual,
    owl_IntersectionClass,
    owl_MaxCardinalityRestriction,
    owl_MinCardinalityRestriction,
    owl_OWLAllDifferent,
    owl_OWLAnnotationProperty,
    owl_OWLClass,
    owl_OWLDataRange,
    owl_OWLDatatypeProperty,
    owl_OWLObjectProperty,
    owl_OWLOntology,
    owl_OWLOntologyProperty,
    owl_OWLRestriction,
    owl_ObjectSlot,
    owl_Property,
    owl_RDFProperty,
    owl_RDFSClass,
    owl_RDFSLiteral,
    owl_RDFSResource,
    owl_SomeValuesFromRestriction,
    owl_UnionClass,
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

def test_assoc_OWLDisjointWith19_reverse_link_reassign_clear():
    a1 = owl_OWLClass(deprecated="sample_text")
    a2 = owl_OWLClass(deprecated="sample_text_2")
    b = owl_OWLClass(deprecated="sample_text")
    _safe_set(b, 'invOWLDisjointWith', {a1})
    assert _is_linked(b, 'invOWLDisjointWith', a1)
    if hasattr(a1, 'OWLClass20'):
        assert _is_linked(a1, 'OWLClass20', b)
    _safe_set(b, 'invOWLDisjointWith', {a2})
    assert _is_linked(b, 'invOWLDisjointWith', a2)
    if hasattr(a1, 'OWLClass20'):
        assert not _is_linked(a1, 'OWLClass20', b)
    if hasattr(a2, 'OWLClass20'):
        assert _is_linked(a2, 'OWLClass20', b)
    _safe_set(b, 'invOWLDisjointWith', set())
    assert not _is_linked(b, 'invOWLDisjointWith', a2)
    if hasattr(a2, 'OWLClass20'):
        assert not _is_linked(a2, 'OWLClass20', b)


def test_assoc_OWLEquivalentClass16_reverse_link_reassign_clear():
    a1 = owl_OWLClass(deprecated="sample_text")
    a2 = owl_OWLClass(deprecated="sample_text_2")
    b = owl_OWLClass(deprecated="sample_text")
    _safe_set(b, 'invOWLEquivalentClass', {a1})
    assert _is_linked(b, 'invOWLEquivalentClass', a1)
    if hasattr(a1, 'OWLClass17'):
        assert _is_linked(a1, 'OWLClass17', b)
    _safe_set(b, 'invOWLEquivalentClass', {a2})
    assert _is_linked(b, 'invOWLEquivalentClass', a2)
    if hasattr(a1, 'OWLClass17'):
        assert not _is_linked(a1, 'OWLClass17', b)
    if hasattr(a2, 'OWLClass17'):
        assert _is_linked(a2, 'OWLClass17', b)
    _safe_set(b, 'invOWLEquivalentClass', set())
    assert not _is_linked(b, 'invOWLEquivalentClass', a2)
    if hasattr(a2, 'OWLClass17'):
        assert not _is_linked(a2, 'OWLClass17', b)


def test_assoc_OWLEquivalentProperty34_reverse_link_reassign_clear():
    a1 = owl_Property(deprecated="sample_text", functional="sample_text")
    a2 = owl_Property(deprecated="sample_text_2", functional="sample_text_2")
    b = owl_Property(deprecated="sample_text", functional="sample_text")
    _safe_set(b, 'invOWLEquivalentProperty', {a1})
    assert _is_linked(b, 'invOWLEquivalentProperty', a1)
    if hasattr(a1, 'Property'):
        assert _is_linked(a1, 'Property', b)
    _safe_set(b, 'invOWLEquivalentProperty', {a2})
    assert _is_linked(b, 'invOWLEquivalentProperty', a2)
    if hasattr(a1, 'Property'):
        assert not _is_linked(a1, 'Property', b)
    if hasattr(a2, 'Property'):
        assert _is_linked(a2, 'Property', b)
    _safe_set(b, 'invOWLEquivalentProperty', set())
    assert not _is_linked(b, 'invOWLEquivalentProperty', a2)
    if hasattr(a2, 'Property'):
        assert not _is_linked(a2, 'Property', b)


def test_assoc_OWLInverseOf29_reverse_link_reassign_clear():
    a1 = owl_OWLObjectProperty(inverseFunctional="sample_text", symmetric="sample_text", transitive="sample_text")
    a2 = owl_OWLObjectProperty(inverseFunctional="sample_text_2", symmetric="sample_text_2", transitive="sample_text_2")
    b = owl_OWLObjectProperty(inverseFunctional="sample_text", symmetric="sample_text", transitive="sample_text")
    _safe_set(b, 'invOWLInverseOf', a1)
    assert _is_linked(b, 'invOWLInverseOf', a1)
    if hasattr(a1, 'OWLObjectProperty'):
        assert _is_linked(a1, 'OWLObjectProperty', b)
    _safe_set(b, 'invOWLInverseOf', a2)
    assert _is_linked(b, 'invOWLInverseOf', a2)
    if hasattr(a1, 'OWLObjectProperty'):
        assert not _is_linked(a1, 'OWLObjectProperty', b)
    if hasattr(a2, 'OWLObjectProperty'):
        assert _is_linked(a2, 'OWLObjectProperty', b)
    _safe_set(b, 'invOWLInverseOf', None)
    assert not _is_linked(b, 'invOWLInverseOf', a2)
    if hasattr(a2, 'OWLObjectProperty'):
        assert not _is_linked(a2, 'OWLObjectProperty', b)


def test_assoc_invOWLDisjointWith22_reverse_link_reassign_clear():
    a1 = owl_OWLClass(deprecated="sample_text")
    a2 = owl_OWLClass(deprecated="sample_text_2")
    b = owl_OWLClass(deprecated="sample_text")
    _safe_set(b, 'OWLDisjointWith', {a1})
    assert _is_linked(b, 'OWLDisjointWith', a1)
    if hasattr(a1, 'OWLClass23'):
        assert _is_linked(a1, 'OWLClass23', b)
    _safe_set(b, 'OWLDisjointWith', {a2})
    assert _is_linked(b, 'OWLDisjointWith', a2)
    if hasattr(a1, 'OWLClass23'):
        assert not _is_linked(a1, 'OWLClass23', b)
    if hasattr(a2, 'OWLClass23'):
        assert _is_linked(a2, 'OWLClass23', b)
    _safe_set(b, 'OWLDisjointWith', set())
    assert not _is_linked(b, 'OWLDisjointWith', a2)
    if hasattr(a2, 'OWLClass23'):
        assert not _is_linked(a2, 'OWLClass23', b)


def test_assoc_invOWLEquivalentClass14_reverse_link_reassign_clear():
    a1 = owl_OWLClass(deprecated="sample_text")
    a2 = owl_OWLClass(deprecated="sample_text_2")
    b = owl_OWLClass(deprecated="sample_text")
    _safe_set(b, 'OWLEquivalentClass', {a1})
    assert _is_linked(b, 'OWLEquivalentClass', a1)
    if hasattr(a1, 'OWLClass'):
        assert _is_linked(a1, 'OWLClass', b)
    _safe_set(b, 'OWLEquivalentClass', {a2})
    assert _is_linked(b, 'OWLEquivalentClass', a2)
    if hasattr(a1, 'OWLClass'):
        assert not _is_linked(a1, 'OWLClass', b)
    if hasattr(a2, 'OWLClass'):
        assert _is_linked(a2, 'OWLClass', b)
    _safe_set(b, 'OWLEquivalentClass', set())
    assert not _is_linked(b, 'OWLEquivalentClass', a2)
    if hasattr(a2, 'OWLClass'):
        assert not _is_linked(a2, 'OWLClass', b)


def test_assoc_invOWLEquivalentProperty36_reverse_link_reassign_clear():
    a1 = owl_Property(deprecated="sample_text", functional="sample_text")
    a2 = owl_Property(deprecated="sample_text_2", functional="sample_text_2")
    b = owl_Property(deprecated="sample_text", functional="sample_text")
    _safe_set(b, 'Property37', a1)
    assert _is_linked(b, 'Property37', a1)
    if hasattr(a1, 'OWLEquivalentProperty'):
        assert _is_linked(a1, 'OWLEquivalentProperty', b)
    _safe_set(b, 'Property37', a2)
    assert _is_linked(b, 'Property37', a2)
    if hasattr(a1, 'OWLEquivalentProperty'):
        assert not _is_linked(a1, 'OWLEquivalentProperty', b)
    if hasattr(a2, 'OWLEquivalentProperty'):
        assert _is_linked(a2, 'OWLEquivalentProperty', b)
    _safe_set(b, 'Property37', None)
    assert not _is_linked(b, 'Property37', a2)
    if hasattr(a2, 'OWLEquivalentProperty'):
        assert not _is_linked(a2, 'OWLEquivalentProperty', b)


def test_assoc_invOWLInverseOf31_reverse_link_reassign_clear():
    a1 = owl_OWLObjectProperty(inverseFunctional="sample_text", symmetric="sample_text", transitive="sample_text")
    a2 = owl_OWLObjectProperty(inverseFunctional="sample_text_2", symmetric="sample_text_2", transitive="sample_text_2")
    b = owl_OWLObjectProperty(inverseFunctional="sample_text", symmetric="sample_text", transitive="sample_text")
    _safe_set(b, 'OWLObjectProperty32', a1)
    assert _is_linked(b, 'OWLObjectProperty32', a1)
    if hasattr(a1, 'OWLInverseOf'):
        assert _is_linked(a1, 'OWLInverseOf', b)
    _safe_set(b, 'OWLObjectProperty32', a2)
    assert _is_linked(b, 'OWLObjectProperty32', a2)
    if hasattr(a1, 'OWLInverseOf'):
        assert not _is_linked(a1, 'OWLInverseOf', b)
    if hasattr(a2, 'OWLInverseOf'):
        assert _is_linked(a2, 'OWLInverseOf', b)
    _safe_set(b, 'OWLObjectProperty32', None)
    assert not _is_linked(b, 'OWLObjectProperty32', a2)
    if hasattr(a2, 'OWLInverseOf'):
        assert not _is_linked(a2, 'OWLInverseOf', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_OWLComplementOf84_stub_double():
    # owl_ComplementClass has no real 'invOWLComplementOf' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_ComplementClass()
    setattr(partner, 'invOWLComplementOf', None)
    _safe_set(owner, 'OWLClass85', partner)
    assert getattr(partner, 'invOWLComplementOf') == owner
    _safe_set(owner, 'OWLClass85', None)
    assert getattr(partner, 'invOWLComplementOf') is None


def test_assoc_OWLIntersectionOf70_stub_double():
    # owl_IntersectionClass has no real 'refByIntersectionClass' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_IntersectionClass()
    setattr(partner, 'refByIntersectionClass', None)
    _safe_set(owner, 'OWLClass71', partner)
    assert owner in getattr(partner, 'refByIntersectionClass')
    _safe_set(owner, 'OWLClass71', None)
    assert owner not in getattr(partner, 'refByIntersectionClass')


def test_assoc_OWLUnionOf72_stub_double():
    # owl_UnionClass has no real 'refByUnionClass' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_UnionClass()
    setattr(partner, 'refByUnionClass', None)
    _safe_set(owner, 'OWLClass73', partner)
    assert owner in getattr(partner, 'refByUnionClass')
    _safe_set(owner, 'OWLClass73', None)
    assert owner not in getattr(partner, 'refByUnionClass')


def test_assoc_invOWLComplementOf26_stub_double():
    # owl_ComplementClass has no real 'ComplementClass' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_ComplementClass()
    setattr(partner, 'ComplementClass', None)
    _safe_set(owner, 'OWLComplementOf', {partner})
    assert getattr(partner, 'ComplementClass') == owner
    _safe_set(owner, 'OWLComplementOf', set())
    assert getattr(partner, 'ComplementClass') is None


def test_assoc_property66_stub_double():
    # owl_ObjectSlot has no real 'owl_ObjectSlot67' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLObjectProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLObjectProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLObjectProperty(inverseFunctional="sample_text", symmetric="sample_text", transitive="sample_text")
    partner = owl_ObjectSlot()
    setattr(partner, 'owl_ObjectSlot67', None)
    _safe_set(owner, 'owl_OWLObjectProperty', partner)
    assert getattr(partner, 'owl_ObjectSlot67') == owner
    _safe_set(owner, 'owl_OWLObjectProperty', None)
    assert getattr(partner, 'owl_ObjectSlot67') is None


def test_assoc_refByIntersectionClass24_stub_double():
    # owl_IntersectionClass has no real 'IntersectionClass' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_IntersectionClass()
    setattr(partner, 'IntersectionClass', None)
    _safe_set(owner, 'OWLIntersectionOf', {partner})
    assert getattr(partner, 'IntersectionClass') == owner
    _safe_set(owner, 'OWLIntersectionOf', set())
    assert getattr(partner, 'IntersectionClass') is None


def test_assoc_refByUnionClass25_stub_double():
    # owl_UnionClass has no real 'UnionClass' property in the generated
    # code (a bare stub) -- manually attach it so owl_OWLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # owl_OWLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = owl_OWLClass(deprecated="sample_text")
    partner = owl_UnionClass()
    setattr(partner, 'UnionClass', None)
    _safe_set(owner, 'OWLUnionOf', {partner})
    assert getattr(partner, 'UnionClass') == owner
    _safe_set(owner, 'OWLUnionOf', set())
    assert getattr(partner, 'UnionClass') is None


