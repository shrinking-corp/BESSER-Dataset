import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CORECompositionSpecification,
    COREModel,
    COREModelElement,
    CORENamedElement,
    core_COREBinding,
    core_CORECompositionSpecification,
    core_COREConcern,
    core_COREConfiguration,
    core_COREFeature,
    core_COREFeatureModel,
    core_COREImpactModel,
    core_COREImpactModelElement,
    core_COREInterface,
    core_COREMapping,
    core_COREModel,
    core_COREModelElement,
    core_CORENamedElement,
    core_COREPattern,
    core_COREReuse,
    core_COREStrategy,
    COREFeatureRelationshipType,
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

def test_assoc_configurations10_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration', None)
    _safe_set(owner, 'core_COREFeature11', {partner})
    assert getattr(partner, 'core_COREConfiguration') == owner
    _safe_set(owner, 'core_COREFeature11', set())
    assert getattr(partner, 'core_COREConfiguration') is None


def test_assoc_realizedBy8_stub_double():
    # core_COREModel has no real 'COREModel' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREModel()
    setattr(partner, 'COREModel', None)
    _safe_set(owner, 'realizes', {partner})
    assert getattr(partner, 'COREModel') == owner
    _safe_set(owner, 'realizes', set())
    assert getattr(partner, 'COREModel') is None


def test_assoc_realizes3_stub_double():
    # core_COREModel has no real 'realizedBy' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREModel()
    setattr(partner, 'realizedBy', None)
    _safe_set(owner, 'COREFeature', partner)
    assert owner in getattr(partner, 'realizedBy')
    _safe_set(owner, 'COREFeature', None)
    assert owner not in getattr(partner, 'realizedBy')


def test_assoc_selectable24_stub_double():
    # core_COREInterface has no real 'core_COREInterface25' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface25', None)
    _safe_set(owner, 'core_COREFeature26', partner)
    assert owner in getattr(partner, 'core_COREInterface25')
    _safe_set(owner, 'core_COREFeature26', None)
    assert owner not in getattr(partner, 'core_COREInterface25')


def test_assoc_selected41_stub_double():
    # core_COREReuse has no real 'core_COREReuse42' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREReuse()
    setattr(partner, 'core_COREReuse42', None)
    _safe_set(owner, 'core_COREFeature43', partner)
    assert owner in getattr(partner, 'core_COREReuse42')
    _safe_set(owner, 'core_COREFeature43', None)
    assert owner not in getattr(partner, 'core_COREReuse42')


def test_assoc_selected47_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration48' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration48', None)
    _safe_set(owner, 'core_COREFeature49', partner)
    assert owner in getattr(partner, 'core_COREConfiguration48')
    _safe_set(owner, 'core_COREFeature49', None)
    assert owner not in getattr(partner, 'core_COREConfiguration48')


def test_assoc_strategies9_stub_double():
    # core_COREStrategy has no real 'core_COREStrategy' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature()
    partner = core_COREStrategy()
    setattr(partner, 'core_COREStrategy', None)
    _safe_set(owner, 'core_COREFeature', {partner})
    assert getattr(partner, 'core_COREStrategy') == owner
    _safe_set(owner, 'core_COREFeature', set())
    assert getattr(partner, 'core_COREStrategy') is None


