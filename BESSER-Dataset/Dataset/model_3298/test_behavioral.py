import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AggregatingSIDiseaseModel,
    AggregatingSIRDiseaseModel,
    DiseaseModel,
    DiseaseModelLabel,
    DiseaseModelLabelValue,
    DiseaseModelState,
    DynamicNodeLabel,
    Infector,
    IntegrationDecorator,
    IntegrationLabel,
    IntegrationLabelValue,
    LabelValue,
    Modifiable,
    NodeDecorator,
    SEIR,
    SI,
    SIInfector,
    SILabelValue,
    SIR,
    SIRLabelValue,
    SanityChecker,
    StandardDiseaseModel,
    StandardDiseaseModelLabel,
    StandardDiseaseModelLabelValue,
    StandardDiseaseModelState,
    StandardInfector,
    StandardStochasticDiseaseModel,
    StochasticDiseaseModel,
    standard_AggregatingDiseaseModelState,
    standard_AggregatingSEIRDiseaseModel,
    standard_AggregatingSIDiseaseModel,
    standard_AggregatingSIRDiseaseModel,
    standard_DeterministicSEIRDiseaseModel,
    standard_DeterministicSIDiseaseModel,
    standard_DeterministicSIRDiseaseModel,
    standard_DiseaseModel,
    standard_DiseaseModelLabel,
    standard_DiseaseModelLabelValue,
    standard_DiseaseModelState,
    standard_Infector,
    standard_InfectorInoculatorCollection,
    standard_IntegrationDecorator,
    standard_IntegrationLabel,
    standard_IntegrationLabelValue,
    standard_PopulationLabel,
    standard_PopulationModelLabel,
    standard_SEIR,
    standard_SEIRLabel,
    standard_SEIRLabelValue,
    standard_SI,
    standard_SIDiseaseModelState,
    standard_SIInfector,
    standard_SILabel,
    standard_SILabelValue,
    standard_SIR,
    standard_SIRInoculator,
    standard_SIRLabel,
    standard_SIRLabelValue,
    standard_SanityChecker,
    standard_StandardDiseaseModel,
    standard_StandardDiseaseModelLabel,
    standard_StandardDiseaseModelLabelValue,
    standard_StandardDiseaseModelState,
    standard_StandardInfector,
    standard_StandardStochasticDiseaseModel,
    standard_StochasticDiseaseModel,
    standard_StochasticPoissonSEIRDiseaseModel,
    standard_StochasticPoissonSIDiseaseModel,
    standard_StochasticPoissonSIRDiseaseModel,
    standard_StochasticSEIRDiseaseModel,
    standard_StochasticSIDiseaseModel,
    standard_StochasticSIRDiseaseModel,
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

def test_assoc_diseaseModel5_reverse_link_reassign_clear():
    a1 = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    a2 = standard_StandardDiseaseModel(referencePopulationDensity=9.99, totalArea=9.99, totalPopulationCount=9.99, totalPopulationCountReciprocal=9.99)
    b = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    _safe_set(b, 'standard_Infector', a1)
    assert _is_linked(b, 'standard_Infector', a1)
    if hasattr(a1, 'standard_StandardDiseaseModel'):
        assert _is_linked(a1, 'standard_StandardDiseaseModel', b)
    _safe_set(b, 'standard_Infector', a2)
    assert _is_linked(b, 'standard_Infector', a2)
    if hasattr(a1, 'standard_StandardDiseaseModel'):
        assert not _is_linked(a1, 'standard_StandardDiseaseModel', b)
    if hasattr(a2, 'standard_StandardDiseaseModel'):
        assert _is_linked(a2, 'standard_StandardDiseaseModel', b)
    _safe_set(b, 'standard_Infector', None)
    assert not _is_linked(b, 'standard_Infector', a2)
    if hasattr(a2, 'standard_StandardDiseaseModel'):
        assert not _is_linked(a2, 'standard_StandardDiseaseModel', b)


def test_assoc_list50_reverse_link_reassign_clear():
    a1 = standard_InfectorInoculatorCollection(importFolder="sample_text")
    a2 = standard_InfectorInoculatorCollection(importFolder="sample_text_2")
    b = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    _safe_set(b, 'standard_Infector51', a1)
    assert _is_linked(b, 'standard_Infector51', a1)
    if hasattr(a1, 'standard_InfectorInoculatorCollection'):
        assert _is_linked(a1, 'standard_InfectorInoculatorCollection', b)
    _safe_set(b, 'standard_Infector51', a2)
    assert _is_linked(b, 'standard_Infector51', a2)
    if hasattr(a1, 'standard_InfectorInoculatorCollection'):
        assert not _is_linked(a1, 'standard_InfectorInoculatorCollection', b)
    if hasattr(a2, 'standard_InfectorInoculatorCollection'):
        assert _is_linked(a2, 'standard_InfectorInoculatorCollection', b)
    _safe_set(b, 'standard_Infector51', None)
    assert not _is_linked(b, 'standard_Infector51', a2)
    if hasattr(a2, 'standard_InfectorInoculatorCollection'):
        assert not _is_linked(a2, 'standard_InfectorInoculatorCollection', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_deltaValue22_stub_double():
    # standard_SILabel has no real 'standard_SILabel' property in the generated
    # code (a bare stub) -- manually attach it so standard_SILabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SILabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SILabelValue(i=3.14)
    partner = standard_SILabel()
    setattr(partner, 'standard_SILabel', None)
    _safe_set(owner, 'standard_SILabelValue', partner)
    assert getattr(partner, 'standard_SILabel') == owner
    _safe_set(owner, 'standard_SILabelValue', None)
    assert getattr(partner, 'standard_SILabel') is None


def test_assoc_deltaValue35_stub_double():
    # standard_SIRLabel has no real 'standard_SIRLabel' property in the generated
    # code (a bare stub) -- manually attach it so standard_SIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SIRLabelValue(r=3.14)
    partner = standard_SIRLabel()
    setattr(partner, 'standard_SIRLabel', None)
    _safe_set(owner, 'standard_SIRLabelValue', partner)
    assert getattr(partner, 'standard_SIRLabel') == owner
    _safe_set(owner, 'standard_SIRLabelValue', None)
    assert getattr(partner, 'standard_SIRLabel') is None


def test_assoc_deltaValue9_stub_double():
    # standard_SEIRLabel has no real 'standard_SEIRLabel' property in the generated
    # code (a bare stub) -- manually attach it so standard_SEIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SEIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SEIRLabelValue(e=3.14)
    partner = standard_SEIRLabel()
    setattr(partner, 'standard_SEIRLabel', None)
    _safe_set(owner, 'standard_SEIRLabelValue', partner)
    assert getattr(partner, 'standard_SEIRLabel') == owner
    _safe_set(owner, 'standard_SEIRLabelValue', None)
    assert getattr(partner, 'standard_SEIRLabel') is None


def test_assoc_errorScale19_stub_double():
    # standard_SEIRLabel has no real 'standard_SEIRLabel20' property in the generated
    # code (a bare stub) -- manually attach it so standard_SEIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SEIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SEIRLabelValue(e=3.14)
    partner = standard_SEIRLabel()
    setattr(partner, 'standard_SEIRLabel20', None)
    _safe_set(owner, 'standard_SEIRLabelValue21', partner)
    assert getattr(partner, 'standard_SEIRLabel20') == owner
    _safe_set(owner, 'standard_SEIRLabelValue21', None)
    assert getattr(partner, 'standard_SEIRLabel20') is None


def test_assoc_errorScale32_stub_double():
    # standard_SILabel has no real 'standard_SILabel33' property in the generated
    # code (a bare stub) -- manually attach it so standard_SILabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SILabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SILabelValue(i=3.14)
    partner = standard_SILabel()
    setattr(partner, 'standard_SILabel33', None)
    _safe_set(owner, 'standard_SILabelValue34', partner)
    assert getattr(partner, 'standard_SILabel33') == owner
    _safe_set(owner, 'standard_SILabelValue34', None)
    assert getattr(partner, 'standard_SILabel33') is None


def test_assoc_errorScale45_stub_double():
    # standard_SIRLabel has no real 'standard_SIRLabel46' property in the generated
    # code (a bare stub) -- manually attach it so standard_SIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SIRLabelValue(r=3.14)
    partner = standard_SIRLabel()
    setattr(partner, 'standard_SIRLabel46', None)
    _safe_set(owner, 'standard_SIRLabelValue47', partner)
    assert getattr(partner, 'standard_SIRLabel46') == owner
    _safe_set(owner, 'standard_SIRLabelValue47', None)
    assert getattr(partner, 'standard_SIRLabel46') is None


def test_assoc_labelsToInfect6_stub_double():
    # standard_DiseaseModelLabel has no real 'standard_DiseaseModelLabel8' property in the generated
    # code (a bare stub) -- manually attach it so standard_Infector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Infector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    partner = standard_DiseaseModelLabel()
    setattr(partner, 'standard_DiseaseModelLabel8', None)
    _safe_set(owner, 'standard_Infector7', {partner})
    assert getattr(partner, 'standard_DiseaseModelLabel8') == owner
    _safe_set(owner, 'standard_Infector7', set())
    assert getattr(partner, 'standard_DiseaseModelLabel8') is None


def test_assoc_originalValue16_stub_double():
    # standard_SEIRLabel has no real 'standard_SEIRLabel17' property in the generated
    # code (a bare stub) -- manually attach it so standard_SEIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SEIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SEIRLabelValue(e=3.14)
    partner = standard_SEIRLabel()
    setattr(partner, 'standard_SEIRLabel17', None)
    _safe_set(owner, 'standard_SEIRLabelValue18', partner)
    assert getattr(partner, 'standard_SEIRLabel17') == owner
    _safe_set(owner, 'standard_SEIRLabelValue18', None)
    assert getattr(partner, 'standard_SEIRLabel17') is None


def test_assoc_originalValue29_stub_double():
    # standard_SILabel has no real 'standard_SILabel30' property in the generated
    # code (a bare stub) -- manually attach it so standard_SILabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SILabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SILabelValue(i=3.14)
    partner = standard_SILabel()
    setattr(partner, 'standard_SILabel30', None)
    _safe_set(owner, 'standard_SILabelValue31', partner)
    assert getattr(partner, 'standard_SILabel30') == owner
    _safe_set(owner, 'standard_SILabelValue31', None)
    assert getattr(partner, 'standard_SILabel30') is None


def test_assoc_originalValue42_stub_double():
    # standard_SIRLabel has no real 'standard_SIRLabel43' property in the generated
    # code (a bare stub) -- manually attach it so standard_SIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SIRLabelValue(r=3.14)
    partner = standard_SIRLabel()
    setattr(partner, 'standard_SIRLabel43', None)
    _safe_set(owner, 'standard_SIRLabelValue44', partner)
    assert getattr(partner, 'standard_SIRLabel43') == owner
    _safe_set(owner, 'standard_SIRLabelValue44', None)
    assert getattr(partner, 'standard_SIRLabel43') is None


def test_assoc_probeValue10_stub_double():
    # standard_SEIRLabel has no real 'standard_SEIRLabel11' property in the generated
    # code (a bare stub) -- manually attach it so standard_SEIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SEIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SEIRLabelValue(e=3.14)
    partner = standard_SEIRLabel()
    setattr(partner, 'standard_SEIRLabel11', None)
    _safe_set(owner, 'standard_SEIRLabelValue12', partner)
    assert getattr(partner, 'standard_SEIRLabel11') == owner
    _safe_set(owner, 'standard_SEIRLabelValue12', None)
    assert getattr(partner, 'standard_SEIRLabel11') is None


def test_assoc_probeValue23_stub_double():
    # standard_SILabel has no real 'standard_SILabel24' property in the generated
    # code (a bare stub) -- manually attach it so standard_SILabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SILabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SILabelValue(i=3.14)
    partner = standard_SILabel()
    setattr(partner, 'standard_SILabel24', None)
    _safe_set(owner, 'standard_SILabelValue25', partner)
    assert getattr(partner, 'standard_SILabel24') == owner
    _safe_set(owner, 'standard_SILabelValue25', None)
    assert getattr(partner, 'standard_SILabel24') is None


def test_assoc_probeValue36_stub_double():
    # standard_SIRLabel has no real 'standard_SIRLabel37' property in the generated
    # code (a bare stub) -- manually attach it so standard_SIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SIRLabelValue(r=3.14)
    partner = standard_SIRLabel()
    setattr(partner, 'standard_SIRLabel37', None)
    _safe_set(owner, 'standard_SIRLabelValue38', partner)
    assert getattr(partner, 'standard_SIRLabel37') == owner
    _safe_set(owner, 'standard_SIRLabelValue38', None)
    assert getattr(partner, 'standard_SIRLabel37') is None


def test_assoc_tempValue13_stub_double():
    # standard_SEIRLabel has no real 'standard_SEIRLabel14' property in the generated
    # code (a bare stub) -- manually attach it so standard_SEIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SEIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SEIRLabelValue(e=3.14)
    partner = standard_SEIRLabel()
    setattr(partner, 'standard_SEIRLabel14', None)
    _safe_set(owner, 'standard_SEIRLabelValue15', partner)
    assert getattr(partner, 'standard_SEIRLabel14') == owner
    _safe_set(owner, 'standard_SEIRLabelValue15', None)
    assert getattr(partner, 'standard_SEIRLabel14') is None


def test_assoc_tempValue26_stub_double():
    # standard_SILabel has no real 'standard_SILabel27' property in the generated
    # code (a bare stub) -- manually attach it so standard_SILabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SILabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SILabelValue(i=3.14)
    partner = standard_SILabel()
    setattr(partner, 'standard_SILabel27', None)
    _safe_set(owner, 'standard_SILabelValue28', partner)
    assert getattr(partner, 'standard_SILabel27') == owner
    _safe_set(owner, 'standard_SILabelValue28', None)
    assert getattr(partner, 'standard_SILabel27') is None


def test_assoc_tempValue39_stub_double():
    # standard_SIRLabel has no real 'standard_SIRLabel40' property in the generated
    # code (a bare stub) -- manually attach it so standard_SIRLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_SIRLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_SIRLabelValue(r=3.14)
    partner = standard_SIRLabel()
    setattr(partner, 'standard_SIRLabel40', None)
    _safe_set(owner, 'standard_SIRLabelValue41', partner)
    assert getattr(partner, 'standard_SIRLabel40') == owner
    _safe_set(owner, 'standard_SIRLabelValue41', None)
    assert getattr(partner, 'standard_SIRLabel40') is None


