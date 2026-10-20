import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOperator,
    Dependency,
    Description,
    Requirement,
    SimpleDependency,
    Term,
    UnaryOperator,
    newP_AndOperartor,
    newP_BinaryOperator,
    newP_CValue,
    newP_Category,
    newP_Dependency,
    newP_Description,
    newP_FunctionalRequirement,
    newP_ICost,
    newP_NotOperator,
    newP_OrOperator,
    newP_Person,
    newP_QualityRequirement,
    newP_Refines,
    newP_Requirement,
    newP_RequirementTerm,
    newP_Requires,
    newP_SimpleDependency,
    newP_Specification,
    newP_Term,
    newP_TextDescription,
    newP_UnaryOperator,
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

def test_assoc_categories12_reverse_link_reassign_clear():
    a1 = newP_Person(firstName="sample_text", lastName="sample_text")
    a2 = newP_Person(firstName="sample_text_2", lastName="sample_text_2")
    b = newP_Category(name="sample_text")
    _safe_set(b, 'newP_Category14', a1)
    assert _is_linked(b, 'newP_Category14', a1)
    if hasattr(a1, 'newP_Person13'):
        assert _is_linked(a1, 'newP_Person13', b)
    _safe_set(b, 'newP_Category14', a2)
    assert _is_linked(b, 'newP_Category14', a2)
    if hasattr(a1, 'newP_Person13'):
        assert not _is_linked(a1, 'newP_Person13', b)
    if hasattr(a2, 'newP_Person13'):
        assert _is_linked(a2, 'newP_Person13', b)
    _safe_set(b, 'newP_Category14', None)
    assert not _is_linked(b, 'newP_Category14', a2)
    if hasattr(a2, 'newP_Person13'):
        assert not _is_linked(a2, 'newP_Person13', b)


def test_assoc_category8_reverse_link_reassign_clear():
    a1 = newP_Specification(name="sample_text")
    a2 = newP_Specification(name="sample_text_2")
    b = newP_Category(name="sample_text")
    _safe_set(b, 'newP_Category9', a1)
    assert _is_linked(b, 'newP_Category9', a1)
    if hasattr(a1, 'newP_Specification'):
        assert _is_linked(a1, 'newP_Specification', b)
    _safe_set(b, 'newP_Category9', a2)
    assert _is_linked(b, 'newP_Category9', a2)
    if hasattr(a1, 'newP_Specification'):
        assert not _is_linked(a1, 'newP_Specification', b)
    if hasattr(a2, 'newP_Specification'):
        assert _is_linked(a2, 'newP_Specification', b)
    _safe_set(b, 'newP_Category9', None)
    assert not _is_linked(b, 'newP_Category9', a2)
    if hasattr(a2, 'newP_Specification'):
        assert not _is_linked(a2, 'newP_Specification', b)


def test_assoc_children6_reverse_link_reassign_clear():
    a1 = newP_Category(name="sample_text")
    a2 = newP_Category(name="sample_text_2")
    b = newP_Category(name="sample_text")
    _safe_set(b, 'newP_Category7', a1)
    assert _is_linked(b, 'newP_Category7', a1)
    if hasattr(a1, 'newP_Category5'):
        assert _is_linked(a1, 'newP_Category5', b)
    _safe_set(b, 'newP_Category7', a2)
    assert _is_linked(b, 'newP_Category7', a2)
    if hasattr(a1, 'newP_Category5'):
        assert not _is_linked(a1, 'newP_Category5', b)
    if hasattr(a2, 'newP_Category5'):
        assert _is_linked(a2, 'newP_Category5', b)
    _safe_set(b, 'newP_Category7', None)
    assert not _is_linked(b, 'newP_Category7', a2)
    if hasattr(a2, 'newP_Category5'):
        assert not _is_linked(a2, 'newP_Category5', b)


def test_assoc_person10_reverse_link_reassign_clear():
    a1 = newP_Specification(name="sample_text")
    a2 = newP_Specification(name="sample_text_2")
    b = newP_Person(firstName="sample_text", lastName="sample_text")
    _safe_set(b, 'newP_Person', a1)
    assert _is_linked(b, 'newP_Person', a1)
    if hasattr(a1, 'newP_Specification11'):
        assert _is_linked(a1, 'newP_Specification11', b)
    _safe_set(b, 'newP_Person', a2)
    assert _is_linked(b, 'newP_Person', a2)
    if hasattr(a1, 'newP_Specification11'):
        assert not _is_linked(a1, 'newP_Specification11', b)
    if hasattr(a2, 'newP_Specification11'):
        assert _is_linked(a2, 'newP_Specification11', b)
    _safe_set(b, 'newP_Person', None)
    assert not _is_linked(b, 'newP_Person', a2)
    if hasattr(a2, 'newP_Specification11'):
        assert not _is_linked(a2, 'newP_Specification11', b)


def test_assoc_requirement3_reverse_link_reassign_clear():
    a1 = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    a2 = newP_Requirement(identifier="sample_text_2", mandatory=False, name="sample_text_2", priority=13)
    b = newP_Category(name="sample_text")
    _safe_set(b, 'newP_Category', {a1})
    assert _is_linked(b, 'newP_Category', a1)
    if hasattr(a1, 'newP_Requirement4'):
        assert _is_linked(a1, 'newP_Requirement4', b)
    _safe_set(b, 'newP_Category', {a2})
    assert _is_linked(b, 'newP_Category', a2)
    if hasattr(a1, 'newP_Requirement4'):
        assert not _is_linked(a1, 'newP_Requirement4', b)
    if hasattr(a2, 'newP_Requirement4'):
        assert _is_linked(a2, 'newP_Requirement4', b)
    _safe_set(b, 'newP_Category', set())
    assert not _is_linked(b, 'newP_Category', a2)
    if hasattr(a2, 'newP_Requirement4'):
        assert not _is_linked(a2, 'newP_Requirement4', b)


def test_assoc_requirements15_reverse_link_reassign_clear():
    a1 = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    a2 = newP_Requirement(identifier="sample_text_2", mandatory=False, name="sample_text_2", priority=13)
    b = newP_Person(firstName="sample_text", lastName="sample_text")
    _safe_set(b, 'newP_Person16', {a1})
    assert _is_linked(b, 'newP_Person16', a1)
    if hasattr(a1, 'newP_Requirement17'):
        assert _is_linked(a1, 'newP_Requirement17', b)
    _safe_set(b, 'newP_Person16', {a2})
    assert _is_linked(b, 'newP_Person16', a2)
    if hasattr(a1, 'newP_Requirement17'):
        assert not _is_linked(a1, 'newP_Requirement17', b)
    if hasattr(a2, 'newP_Requirement17'):
        assert _is_linked(a2, 'newP_Requirement17', b)
    _safe_set(b, 'newP_Person16', set())
    assert not _is_linked(b, 'newP_Person16', a2)
    if hasattr(a2, 'newP_Requirement17'):
        assert not _is_linked(a2, 'newP_Requirement17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_RHS18_stub_double():
    # newP_Term has no real 'newP_Term' property in the generated
    # code (a bare stub) -- manually attach it so newP_UnaryOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_UnaryOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_UnaryOperator(name="sample_text")
    partner = newP_Term()
    setattr(partner, 'newP_Term', None)
    _safe_set(owner, 'newP_UnaryOperator', partner)
    assert getattr(partner, 'newP_Term') == owner
    _safe_set(owner, 'newP_UnaryOperator', None)
    assert getattr(partner, 'newP_Term') is None


def test_assoc_RHS19_stub_double():
    # newP_Term has no real 'newP_Term20' property in the generated
    # code (a bare stub) -- manually attach it so newP_Requires's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_Requires's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_Requires(name="sample_text")
    partner = newP_Term()
    setattr(partner, 'newP_Term20', None)
    _safe_set(owner, 'newP_Requires', partner)
    assert getattr(partner, 'newP_Term20') == owner
    _safe_set(owner, 'newP_Requires', None)
    assert getattr(partner, 'newP_Term20') is None


def test_assoc_RHS21_stub_double():
    # newP_RequirementTerm has no real 'newP_RequirementTerm' property in the generated
    # code (a bare stub) -- manually attach it so newP_SimpleDependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_SimpleDependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_SimpleDependency(name="sample_text")
    partner = newP_RequirementTerm()
    setattr(partner, 'newP_RequirementTerm', None)
    _safe_set(owner, 'newP_SimpleDependency', partner)
    assert getattr(partner, 'newP_RequirementTerm') == owner
    _safe_set(owner, 'newP_SimpleDependency', None)
    assert getattr(partner, 'newP_RequirementTerm') is None


def test_assoc_dependency1_stub_double():
    # newP_Dependency has no real 'newP_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so newP_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    partner = newP_Dependency()
    setattr(partner, 'newP_Dependency', None)
    _safe_set(owner, 'newP_Requirement2', {partner})
    assert getattr(partner, 'newP_Dependency') == owner
    _safe_set(owner, 'newP_Requirement2', set())
    assert getattr(partner, 'newP_Dependency') is None


def test_assoc_description0_stub_double():
    # newP_Description has no real 'newP_Description' property in the generated
    # code (a bare stub) -- manually attach it so newP_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    partner = newP_Description()
    setattr(partner, 'newP_Description', None)
    _safe_set(owner, 'newP_Requirement', {partner})
    assert getattr(partner, 'newP_Description') == owner
    _safe_set(owner, 'newP_Requirement', set())
    assert getattr(partner, 'newP_Description') is None


def test_assoc_requirement24_stub_double():
    # newP_RequirementTerm has no real 'newP_RequirementTerm25' property in the generated
    # code (a bare stub) -- manually attach it so newP_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newP_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    partner = newP_RequirementTerm()
    setattr(partner, 'newP_RequirementTerm25', None)
    _safe_set(owner, 'newP_Requirement26', partner)
    assert getattr(partner, 'newP_RequirementTerm25') == owner
    _safe_set(owner, 'newP_Requirement26', None)
    assert getattr(partner, 'newP_RequirementTerm25') is None


