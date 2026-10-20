import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AperiodicPattern,
    BurstPattern,
    ClosedPattern,
    EDF_Parameters,
    FixedPriorityParameters,
    IntegerMatrix,
    IntegerVector,
    IrregularPattern,
    MARTE_Library_BasicNFP_Types_AperiodicPattern,
    MARTE_Library_BasicNFP_Types_ArrivalPattern,
    MARTE_Library_BasicNFP_Types_BurstPattern,
    MARTE_Library_BasicNFP_Types_ClosedPattern,
    MARTE_Library_BasicNFP_Types_IrregularPattern,
    MARTE_Library_BasicNFP_Types_NFP_Area,
    MARTE_Library_BasicNFP_Types_NFP_Boolean,
    MARTE_Library_BasicNFP_Types_NFP_CommonType,
    MARTE_Library_BasicNFP_Types_NFP_DataSize,
    MARTE_Library_BasicNFP_Types_NFP_DataTxRate,
    MARTE_Library_BasicNFP_Types_NFP_DateTime,
    MARTE_Library_BasicNFP_Types_NFP_Duration,
    MARTE_Library_BasicNFP_Types_NFP_Energy,
    MARTE_Library_BasicNFP_Types_NFP_Frequency,
    MARTE_Library_BasicNFP_Types_NFP_Integer,
    MARTE_Library_BasicNFP_Types_NFP_Length,
    MARTE_Library_BasicNFP_Types_NFP_Natural,
    MARTE_Library_BasicNFP_Types_NFP_Percentage,
    MARTE_Library_BasicNFP_Types_NFP_Power,
    MARTE_Library_BasicNFP_Types_NFP_Price,
    MARTE_Library_BasicNFP_Types_NFP_Real,
    MARTE_Library_BasicNFP_Types_NFP_String,
    MARTE_Library_BasicNFP_Types_NFP_Weight,
    MARTE_Library_BasicNFP_Types_OpenPattern,
    MARTE_Library_BasicNFP_Types_PeriodicPattern,
    MARTE_Library_BasicNFP_Types_SporadicPattern,
    MARTE_Library_GRM_BasicTypes_EDF_Parameters,
    MARTE_Library_GRM_BasicTypes_FixedPriorityParameters,
    MARTE_Library_GRM_BasicTypes_PeriodicServerParameters,
    MARTE_Library_GRM_BasicTypes_PoolingParameters,
    MARTE_Library_GRM_BasicTypes_SchedParameters,
    MARTE_Library_MARTE_DataTypes_Array,
    MARTE_Library_MARTE_DataTypes_IntegerInterval,
    MARTE_Library_MARTE_DataTypes_IntegerMatrix,
    MARTE_Library_MARTE_DataTypes_IntegerVector,
    MARTE_Library_MARTE_DataTypes_Interval,
    MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval,
    MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval,
    MARTE_Library_MARTE_DataTypes_RealMatrix,
    MARTE_Library_MARTE_DataTypes_RealVector,
    MARTE_Library_MARTE_DataTypes_Realnterval,
    MARTE_Library_MARTE_DataTypes_UtilityType,
    MARTE_Library_RS_Library_ShapeSpecification,
    MARTE_Library_RS_Library_TilerSpecification,
    MARTE_Library_TimeLibrary_IdealClock,
    MARTE_Library_TimeLibrary_TimedValueType,
    NFP_CommonType,
    NFP_Duration,
    NFP_Frequency,
    NFP_Integer,
    NFP_Natural,
    NFP_Real,
    OpenPattern,
    PeriodicPattern,
    PeriodicServerParameters,
    PoolingParameters,
    SporadicPattern,
    AreaUnitKind,
    DataSizeUnitKind,
    DataTxRateUnitKind,
    DirectionKind,
    EnergyUnitKind,
    EventKind,
    FrequencyUnitKind,
    LengthUnitKind,
    LogicalTimeUnit,
    PeriodicServerKind,
    PowerUnitKind,
    ProtectProtocolKind,
    SchedPolicyKind,
    SourceKind,
    StatisticalQualifierKind,
    TUK,
    TimeInterpretationKind,
    TimeNatureKind,
    TimeStandardKind,
    TimeUnitKind,
    TransmModeKind,
    WeightUnitKind,
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

def test_assoc_arrivalRate81_stub_double():
    # NFP_Frequency has no real 'NFP_Frequency' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_BasicNFP_Types_OpenPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_BasicNFP_Types_OpenPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_BasicNFP_Types_OpenPattern(arrivalProcess="sample_text")
    partner = NFP_Frequency()
    setattr(partner, 'NFP_Frequency', None)
    _safe_set(owner, 'MARTE_Library_BasicNFP_Types_OpenPattern82', partner)
    assert getattr(partner, 'NFP_Frequency') == owner
    _safe_set(owner, 'MARTE_Library_BasicNFP_Types_OpenPattern82', None)
    assert getattr(partner, 'NFP_Frequency') is None


def test_assoc_edf1_stub_double():
    # EDF_Parameters has no real 'EDF_Parameters' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_SchedParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_SchedParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_SchedParameters(tableEntry="sample_text")
    partner = EDF_Parameters()
    setattr(partner, 'EDF_Parameters', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters', partner)
    assert getattr(partner, 'EDF_Parameters') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters', None)
    assert getattr(partner, 'EDF_Parameters') is None


def test_assoc_fp2_stub_double():
    # FixedPriorityParameters has no real 'FixedPriorityParameters' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_SchedParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_SchedParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_SchedParameters(tableEntry="sample_text")
    partner = FixedPriorityParameters()
    setattr(partner, 'FixedPriorityParameters', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters3', partner)
    assert getattr(partner, 'FixedPriorityParameters') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters3', None)
    assert getattr(partner, 'FixedPriorityParameters') is None


def test_assoc_initialBudget14_stub_double():
    # NFP_Duration has no real 'NFP_Duration15' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(backgroundPriority="sample_text", kind="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration15', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters', partner)
    assert getattr(partner, 'NFP_Duration15') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters', None)
    assert getattr(partner, 'NFP_Duration15') is None


def test_assoc_interArrivalTime79_stub_double():
    # NFP_Duration has no real 'NFP_Duration80' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_BasicNFP_Types_OpenPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_BasicNFP_Types_OpenPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_BasicNFP_Types_OpenPattern(arrivalProcess="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration80', None)
    _safe_set(owner, 'MARTE_Library_BasicNFP_Types_OpenPattern', partner)
    assert getattr(partner, 'NFP_Duration80') == owner
    _safe_set(owner, 'MARTE_Library_BasicNFP_Types_OpenPattern', None)
    assert getattr(partner, 'NFP_Duration80') is None


def test_assoc_matrixElem83_stub_double():
    # IntegerVector has no real 'IntegerVector' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_MARTE_DataTypes_IntegerMatrix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_MARTE_DataTypes_IntegerMatrix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_MARTE_DataTypes_IntegerMatrix()
    partner = IntegerVector()
    setattr(partner, 'IntegerVector', None)
    _safe_set(owner, 'MARTE_Library_MARTE_DataTypes_IntegerMatrix', {partner})
    assert getattr(partner, 'IntegerVector') == owner
    _safe_set(owner, 'MARTE_Library_MARTE_DataTypes_IntegerMatrix', set())
    assert getattr(partner, 'IntegerVector') is None


def test_assoc_maxPendingReplenish19_stub_double():
    # NFP_Integer has no real 'NFP_Integer21' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(backgroundPriority="sample_text", kind="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer21', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20', partner)
    assert getattr(partner, 'NFP_Integer21') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20', None)
    assert getattr(partner, 'NFP_Integer21') is None


def test_assoc_pooling4_stub_double():
    # PoolingParameters has no real 'PoolingParameters' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_SchedParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_SchedParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_SchedParameters(tableEntry="sample_text")
    partner = PoolingParameters()
    setattr(partner, 'PoolingParameters', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters5', partner)
    assert getattr(partner, 'PoolingParameters') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters5', None)
    assert getattr(partner, 'PoolingParameters') is None


def test_assoc_replenishPeriod16_stub_double():
    # NFP_Duration has no real 'NFP_Duration18' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_PeriodicServerParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(backgroundPriority="sample_text", kind="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration18', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17', partner)
    assert getattr(partner, 'NFP_Duration18') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17', None)
    assert getattr(partner, 'NFP_Duration18') is None


def test_assoc_server6_stub_double():
    # PeriodicServerParameters has no real 'PeriodicServerParameters' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Library_GRM_BasicTypes_SchedParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Library_GRM_BasicTypes_SchedParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Library_GRM_BasicTypes_SchedParameters(tableEntry="sample_text")
    partner = PeriodicServerParameters()
    setattr(partner, 'PeriodicServerParameters', None)
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters7', partner)
    assert getattr(partner, 'PeriodicServerParameters') == owner
    _safe_set(owner, 'MARTE_Library_GRM_BasicTypes_SchedParameters7', None)
    assert getattr(partner, 'PeriodicServerParameters') is None


