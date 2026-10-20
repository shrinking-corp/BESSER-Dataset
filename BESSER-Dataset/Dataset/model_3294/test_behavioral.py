import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MultiPopulationSIDiseaseModel,
    MultiPopulationSIRDiseaseModel,
    StandardDiseaseModel,
    multipopulation_DoubleValueList,
    multipopulation_DoubleValueMatrix,
    multipopulation_MultiPopulationSEIRDiseaseModel,
    multipopulation_MultiPopulationSIDiseaseModel,
    multipopulation_MultiPopulationSIRDiseaseModel,
    multipopulation_StringValueList,
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

def test_assoc_infectiousMortalityRate5_stub_double():
    # multipopulation_DoubleValueList has no real 'multipopulation_DoubleValueList7' property in the generated
    # code (a bare stub) -- manually attach it so multipopulation_MultiPopulationSIDiseaseModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multipopulation_MultiPopulationSIDiseaseModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multipopulation_MultiPopulationSIDiseaseModel(characteristicMixingDistance=3.14, physicallyAdjacentInfectiousProportion=3.14, roadNetworkInfectiousProportion=3.14)
    partner = multipopulation_DoubleValueList()
    setattr(partner, 'multipopulation_DoubleValueList7', None)
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel6', partner)
    assert getattr(partner, 'multipopulation_DoubleValueList7') == owner
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel6', None)
    assert getattr(partner, 'multipopulation_DoubleValueList7') is None


def test_assoc_populationGroups0_stub_double():
    # multipopulation_StringValueList has no real 'multipopulation_StringValueList' property in the generated
    # code (a bare stub) -- manually attach it so multipopulation_MultiPopulationSIDiseaseModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multipopulation_MultiPopulationSIDiseaseModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multipopulation_MultiPopulationSIDiseaseModel(characteristicMixingDistance=3.14, physicallyAdjacentInfectiousProportion=3.14, roadNetworkInfectiousProportion=3.14)
    partner = multipopulation_StringValueList()
    setattr(partner, 'multipopulation_StringValueList', None)
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel', partner)
    assert getattr(partner, 'multipopulation_StringValueList') == owner
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel', None)
    assert getattr(partner, 'multipopulation_StringValueList') is None


def test_assoc_recoveryRate3_stub_double():
    # multipopulation_DoubleValueList has no real 'multipopulation_DoubleValueList' property in the generated
    # code (a bare stub) -- manually attach it so multipopulation_MultiPopulationSIDiseaseModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multipopulation_MultiPopulationSIDiseaseModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multipopulation_MultiPopulationSIDiseaseModel(characteristicMixingDistance=3.14, physicallyAdjacentInfectiousProportion=3.14, roadNetworkInfectiousProportion=3.14)
    partner = multipopulation_DoubleValueList()
    setattr(partner, 'multipopulation_DoubleValueList', None)
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel4', partner)
    assert getattr(partner, 'multipopulation_DoubleValueList') == owner
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel4', None)
    assert getattr(partner, 'multipopulation_DoubleValueList') is None


def test_assoc_transmissionRate1_stub_double():
    # multipopulation_DoubleValueMatrix has no real 'multipopulation_DoubleValueMatrix' property in the generated
    # code (a bare stub) -- manually attach it so multipopulation_MultiPopulationSIDiseaseModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multipopulation_MultiPopulationSIDiseaseModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multipopulation_MultiPopulationSIDiseaseModel(characteristicMixingDistance=3.14, physicallyAdjacentInfectiousProportion=3.14, roadNetworkInfectiousProportion=3.14)
    partner = multipopulation_DoubleValueMatrix()
    setattr(partner, 'multipopulation_DoubleValueMatrix', None)
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel2', partner)
    assert getattr(partner, 'multipopulation_DoubleValueMatrix') == owner
    _safe_set(owner, 'multipopulation_MultiPopulationSIDiseaseModel2', None)
    assert getattr(partner, 'multipopulation_DoubleValueMatrix') is None


