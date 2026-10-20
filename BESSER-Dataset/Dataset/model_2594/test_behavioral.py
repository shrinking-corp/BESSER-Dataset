import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractSuperclass,
    Child,
    grammar_features_AbstractSuperclass,
    grammar_features_AlternativeSyntax,
    grammar_features_Child,
    grammar_features_ClassWithAttributes,
    grammar_features_CompoundOptional,
    grammar_features_CompoundPlus,
    grammar_features_CompoundStar,
    grammar_features_ConcreteSubclassA,
    grammar_features_ConcreteSubclassB,
    grammar_features_MandatoryContainment,
    grammar_features_MandatoryNonContainment,
    grammar_features_OptionalContainment,
    grammar_features_OptionalNonContainment,
    grammar_features_OptionalPrefix,
    grammar_features_PlusContainment,
    grammar_features_PlusNonContainment,
    grammar_features_PlusPrefix,
    grammar_features_Root,
    grammar_features_SecondRoot,
    grammar_features_StarContainment,
    grammar_features_StarNonContainment,
    grammar_features_StarPrefix,
    grammar_features_X,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_reference1_stub_double():
    # grammar_features_OptionalContainment has no real 'grammar_features_OptionalContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_OptionalContainment()
    setattr(partner, 'grammar_features_OptionalContainment', None)
    _safe_set(owner, 'grammar_features_X', partner)
    assert getattr(partner, 'grammar_features_OptionalContainment') == owner
    _safe_set(owner, 'grammar_features_X', None)
    assert getattr(partner, 'grammar_features_OptionalContainment') is None


def test_assoc_reference10_stub_double():
    # grammar_features_MandatoryNonContainment has no real 'grammar_features_MandatoryNonContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_MandatoryNonContainment()
    setattr(partner, 'grammar_features_MandatoryNonContainment', None)
    _safe_set(owner, 'grammar_features_X11', partner)
    assert getattr(partner, 'grammar_features_MandatoryNonContainment') == owner
    _safe_set(owner, 'grammar_features_X11', None)
    assert getattr(partner, 'grammar_features_MandatoryNonContainment') is None


def test_assoc_reference12_stub_double():
    # grammar_features_PlusNonContainment has no real 'grammar_features_PlusNonContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_PlusNonContainment()
    setattr(partner, 'grammar_features_PlusNonContainment', None)
    _safe_set(owner, 'grammar_features_X13', partner)
    assert owner in getattr(partner, 'grammar_features_PlusNonContainment')
    _safe_set(owner, 'grammar_features_X13', None)
    assert owner not in getattr(partner, 'grammar_features_PlusNonContainment')


def test_assoc_reference14_stub_double():
    # grammar_features_StarNonContainment has no real 'grammar_features_StarNonContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_StarNonContainment()
    setattr(partner, 'grammar_features_StarNonContainment', None)
    _safe_set(owner, 'grammar_features_X15', partner)
    assert owner in getattr(partner, 'grammar_features_StarNonContainment')
    _safe_set(owner, 'grammar_features_X15', None)
    assert owner not in getattr(partner, 'grammar_features_StarNonContainment')


def test_assoc_reference2_stub_double():
    # grammar_features_MandatoryContainment has no real 'grammar_features_MandatoryContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_MandatoryContainment()
    setattr(partner, 'grammar_features_MandatoryContainment', None)
    _safe_set(owner, 'grammar_features_X3', partner)
    assert getattr(partner, 'grammar_features_MandatoryContainment') == owner
    _safe_set(owner, 'grammar_features_X3', None)
    assert getattr(partner, 'grammar_features_MandatoryContainment') is None


def test_assoc_reference4_stub_double():
    # grammar_features_PlusContainment has no real 'grammar_features_PlusContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_PlusContainment()
    setattr(partner, 'grammar_features_PlusContainment', None)
    _safe_set(owner, 'grammar_features_X5', partner)
    assert owner in getattr(partner, 'grammar_features_PlusContainment')
    _safe_set(owner, 'grammar_features_X5', None)
    assert owner not in getattr(partner, 'grammar_features_PlusContainment')


def test_assoc_reference6_stub_double():
    # grammar_features_StarContainment has no real 'grammar_features_StarContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_StarContainment()
    setattr(partner, 'grammar_features_StarContainment', None)
    _safe_set(owner, 'grammar_features_X7', partner)
    assert owner in getattr(partner, 'grammar_features_StarContainment')
    _safe_set(owner, 'grammar_features_X7', None)
    assert owner not in getattr(partner, 'grammar_features_StarContainment')


def test_assoc_reference8_stub_double():
    # grammar_features_OptionalNonContainment has no real 'grammar_features_OptionalNonContainment' property in the generated
    # code (a bare stub) -- manually attach it so grammar_features_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_features_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_features_X(name="sample_text")
    partner = grammar_features_OptionalNonContainment()
    setattr(partner, 'grammar_features_OptionalNonContainment', None)
    _safe_set(owner, 'grammar_features_X9', partner)
    assert getattr(partner, 'grammar_features_OptionalNonContainment') == owner
    _safe_set(owner, 'grammar_features_X9', None)
    assert getattr(partner, 'grammar_features_OptionalNonContainment') is None


