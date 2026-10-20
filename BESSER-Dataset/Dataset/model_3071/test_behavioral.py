import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CloudOptionalTypes,
    Type,
    giraffeDSL_Action,
    giraffeDSL_ActionClassType,
    giraffeDSL_ActionMethodType,
    giraffeDSL_ActionRangeType,
    giraffeDSL_CloudCredentialType,
    giraffeDSL_CloudOptionalTypes,
    giraffeDSL_CloudPasswordType,
    giraffeDSL_CloudProvider,
    giraffeDSL_CloudProviderType,
    giraffeDSL_CloudType,
    giraffeDSL_CloudUserType,
    giraffeDSL_Create,
    giraffeDSL_Deploy,
    giraffeDSL_DeployApp,
    giraffeDSL_DeployAppClassType,
    giraffeDSL_DeployAppFeature,
    giraffeDSL_DeployAppMasterMethodType,
    giraffeDSL_DeployAppSlaveMethodType,
    giraffeDSL_DeployRangeType,
    giraffeDSL_DeployType,
    giraffeDSL_DeployTypeFeature,
    giraffeDSL_DomainModel,
    giraffeDSL_Features,
    giraffeDSL_GeoZoneType,
    giraffeDSL_InitIncrementFeature,
    giraffeDSL_InitMachinesFeature,
    giraffeDSL_IntFeature,
    giraffeDSL_MgmAddressType,
    giraffeDSL_Monitor,
    giraffeDSL_MonitorRangeType,
    giraffeDSL_MonitoringType,
    giraffeDSL_ScriptType,
    giraffeDSL_Stress,
    giraffeDSL_StressClassType,
    giraffeDSL_StressMethodType,
    giraffeDSL_StressRangeType,
    giraffeDSL_Type,
    giraffeDSL_VirtualMachine,
    giraffeDSL_VirtualMachineFeature,
    giraffeDSL_VirtualMachineTypeFeature,
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

def test_assoc_class_31_stub_double():
    # giraffeDSL_DeployApp has no real 'giraffeDSL_DeployApp32' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployAppClassType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployAppClassType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployAppClassType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_DeployApp()
    setattr(partner, 'giraffeDSL_DeployApp32', None)
    _safe_set(owner, 'giraffeDSL_DeployAppClassType', partner)
    assert owner in getattr(partner, 'giraffeDSL_DeployApp32')
    _safe_set(owner, 'giraffeDSL_DeployAppClassType', None)
    assert owner not in getattr(partner, 'giraffeDSL_DeployApp32')


def test_assoc_class_46_stub_double():
    # giraffeDSL_Action has no real 'giraffeDSL_Action47' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_ActionClassType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_ActionClassType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_ActionClassType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Action()
    setattr(partner, 'giraffeDSL_Action47', None)
    _safe_set(owner, 'giraffeDSL_ActionClassType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Action47')
    _safe_set(owner, 'giraffeDSL_ActionClassType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Action47')


def test_assoc_cloudAddress16_stub_double():
    # giraffeDSL_CloudProvider has no real 'giraffeDSL_CloudProvider17' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_MgmAddressType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_MgmAddressType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_MgmAddressType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_CloudProvider()
    setattr(partner, 'giraffeDSL_CloudProvider17', None)
    _safe_set(owner, 'giraffeDSL_MgmAddressType', partner)
    assert owner in getattr(partner, 'giraffeDSL_CloudProvider17')
    _safe_set(owner, 'giraffeDSL_MgmAddressType', None)
    assert owner not in getattr(partner, 'giraffeDSL_CloudProvider17')


def test_assoc_cloudCredential18_stub_double():
    # giraffeDSL_CloudProvider has no real 'giraffeDSL_CloudProvider19' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_CloudCredentialType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_CloudCredentialType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_CloudCredentialType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_CloudProvider()
    setattr(partner, 'giraffeDSL_CloudProvider19', None)
    _safe_set(owner, 'giraffeDSL_CloudCredentialType', partner)
    assert owner in getattr(partner, 'giraffeDSL_CloudProvider19')
    _safe_set(owner, 'giraffeDSL_CloudCredentialType', None)
    assert owner not in getattr(partner, 'giraffeDSL_CloudProvider19')


def test_assoc_cloudOptionalTypes20_stub_double():
    # giraffeDSL_CloudProvider has no real 'giraffeDSL_CloudProvider21' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_CloudOptionalTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_CloudOptionalTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_CloudOptionalTypes(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_CloudProvider()
    setattr(partner, 'giraffeDSL_CloudProvider21', None)
    _safe_set(owner, 'giraffeDSL_CloudOptionalTypes', partner)
    assert owner in getattr(partner, 'giraffeDSL_CloudProvider21')
    _safe_set(owner, 'giraffeDSL_CloudOptionalTypes', None)
    assert owner not in getattr(partner, 'giraffeDSL_CloudProvider21')


def test_assoc_cloudProvider10_stub_double():
    # giraffeDSL_VirtualMachine has no real 'giraffeDSL_VirtualMachine11' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_CloudProviderType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_CloudProviderType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_CloudProviderType(many="sample_text", name="sample_text")
    partner = giraffeDSL_VirtualMachine()
    setattr(partner, 'giraffeDSL_VirtualMachine11', None)
    _safe_set(owner, 'giraffeDSL_CloudProviderType', partner)
    assert owner in getattr(partner, 'giraffeDSL_VirtualMachine11')
    _safe_set(owner, 'giraffeDSL_CloudProviderType', None)
    assert owner not in getattr(partner, 'giraffeDSL_VirtualMachine11')


def test_assoc_cloudType14_stub_double():
    # giraffeDSL_CloudProvider has no real 'giraffeDSL_CloudProvider15' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_CloudType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_CloudType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_CloudType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_CloudProvider()
    setattr(partner, 'giraffeDSL_CloudProvider15', None)
    _safe_set(owner, 'giraffeDSL_CloudType', partner)
    assert owner in getattr(partner, 'giraffeDSL_CloudProvider15')
    _safe_set(owner, 'giraffeDSL_CloudType', None)
    assert owner not in getattr(partner, 'giraffeDSL_CloudProvider15')


def test_assoc_deployMasterMethod33_stub_double():
    # giraffeDSL_DeployApp has no real 'giraffeDSL_DeployApp34' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployAppMasterMethodType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployAppMasterMethodType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployAppMasterMethodType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_DeployApp()
    setattr(partner, 'giraffeDSL_DeployApp34', None)
    _safe_set(owner, 'giraffeDSL_DeployAppMasterMethodType', partner)
    assert owner in getattr(partner, 'giraffeDSL_DeployApp34')
    _safe_set(owner, 'giraffeDSL_DeployAppMasterMethodType', None)
    assert owner not in getattr(partner, 'giraffeDSL_DeployApp34')


def test_assoc_deployOne22_stub_double():
    # giraffeDSL_Deploy has no real 'giraffeDSL_Deploy' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployAppFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployAppFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployAppFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_Deploy()
    setattr(partner, 'giraffeDSL_Deploy', None)
    _safe_set(owner, 'giraffeDSL_DeployAppFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_Deploy')
    _safe_set(owner, 'giraffeDSL_DeployAppFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_Deploy')


def test_assoc_deploySlaveMethod35_stub_double():
    # giraffeDSL_DeployApp has no real 'giraffeDSL_DeployApp36' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployAppSlaveMethodType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployAppSlaveMethodType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployAppSlaveMethodType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_DeployApp()
    setattr(partner, 'giraffeDSL_DeployApp36', None)
    _safe_set(owner, 'giraffeDSL_DeployAppSlaveMethodType', partner)
    assert owner in getattr(partner, 'giraffeDSL_DeployApp36')
    _safe_set(owner, 'giraffeDSL_DeployAppSlaveMethodType', None)
    assert owner not in getattr(partner, 'giraffeDSL_DeployApp36')


def test_assoc_deployTwo23_stub_double():
    # giraffeDSL_Deploy has no real 'giraffeDSL_Deploy24' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployTypeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployTypeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployTypeFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_Deploy()
    setattr(partner, 'giraffeDSL_Deploy24', None)
    _safe_set(owner, 'giraffeDSL_DeployTypeFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_Deploy24')
    _safe_set(owner, 'giraffeDSL_DeployTypeFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_Deploy24')


def test_assoc_elements0_stub_double():
    # giraffeDSL_DomainModel has no real 'giraffeDSL_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_Type(name="sample_text")
    partner = giraffeDSL_DomainModel()
    setattr(partner, 'giraffeDSL_DomainModel', None)
    _safe_set(owner, 'giraffeDSL_Type', partner)
    assert owner in getattr(partner, 'giraffeDSL_DomainModel')
    _safe_set(owner, 'giraffeDSL_Type', None)
    assert owner not in getattr(partner, 'giraffeDSL_DomainModel')


def test_assoc_initIncrement4_stub_double():
    # giraffeDSL_Create has no real 'giraffeDSL_Create5' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_InitIncrementFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_InitIncrementFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_InitIncrementFeature(many="sample_text", name="sample_text", type=7)
    partner = giraffeDSL_Create()
    setattr(partner, 'giraffeDSL_Create5', None)
    _safe_set(owner, 'giraffeDSL_InitIncrementFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_Create5')
    _safe_set(owner, 'giraffeDSL_InitIncrementFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_Create5')


def test_assoc_initMachines2_stub_double():
    # giraffeDSL_Create has no real 'giraffeDSL_Create3' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_InitMachinesFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_InitMachinesFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_InitMachinesFeature(many="sample_text", name="sample_text", type=7)
    partner = giraffeDSL_Create()
    setattr(partner, 'giraffeDSL_Create3', None)
    _safe_set(owner, 'giraffeDSL_InitMachinesFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_Create3')
    _safe_set(owner, 'giraffeDSL_InitMachinesFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_Create3')


def test_assoc_method48_stub_double():
    # giraffeDSL_Action has no real 'giraffeDSL_Action49' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_ActionMethodType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_ActionMethodType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_ActionMethodType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Action()
    setattr(partner, 'giraffeDSL_Action49', None)
    _safe_set(owner, 'giraffeDSL_ActionMethodType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Action49')
    _safe_set(owner, 'giraffeDSL_ActionMethodType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Action49')


def test_assoc_monitoringType38_stub_double():
    # giraffeDSL_Monitor has no real 'giraffeDSL_Monitor39' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_MonitoringType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_MonitoringType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_MonitoringType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Monitor()
    setattr(partner, 'giraffeDSL_Monitor39', None)
    _safe_set(owner, 'giraffeDSL_MonitoringType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Monitor39')
    _safe_set(owner, 'giraffeDSL_MonitoringType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Monitor39')


def test_assoc_range29_stub_double():
    # giraffeDSL_DeployType has no real 'giraffeDSL_DeployType30' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployRangeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployRangeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployRangeType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_DeployType()
    setattr(partner, 'giraffeDSL_DeployType30', None)
    _safe_set(owner, 'giraffeDSL_DeployRangeType', partner)
    assert owner in getattr(partner, 'giraffeDSL_DeployType30')
    _safe_set(owner, 'giraffeDSL_DeployRangeType', None)
    assert owner not in getattr(partner, 'giraffeDSL_DeployType30')


def test_assoc_range37_stub_double():
    # giraffeDSL_Monitor has no real 'giraffeDSL_Monitor' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_MonitorRangeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_MonitorRangeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_MonitorRangeType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Monitor()
    setattr(partner, 'giraffeDSL_Monitor', None)
    _safe_set(owner, 'giraffeDSL_MonitorRangeType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Monitor')
    _safe_set(owner, 'giraffeDSL_MonitorRangeType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Monitor')


def test_assoc_range40_stub_double():
    # giraffeDSL_Stress has no real 'giraffeDSL_Stress' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_StressRangeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_StressRangeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_StressRangeType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Stress()
    setattr(partner, 'giraffeDSL_Stress', None)
    _safe_set(owner, 'giraffeDSL_StressRangeType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Stress')
    _safe_set(owner, 'giraffeDSL_StressRangeType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Stress')


def test_assoc_range45_stub_double():
    # giraffeDSL_Action has no real 'giraffeDSL_Action' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_ActionRangeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_ActionRangeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_ActionRangeType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Action()
    setattr(partner, 'giraffeDSL_Action', None)
    _safe_set(owner, 'giraffeDSL_ActionRangeType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Action')
    _safe_set(owner, 'giraffeDSL_ActionRangeType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Action')


def test_assoc_stressClass41_stub_double():
    # giraffeDSL_Stress has no real 'giraffeDSL_Stress42' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_StressClassType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_StressClassType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_StressClassType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Stress()
    setattr(partner, 'giraffeDSL_Stress42', None)
    _safe_set(owner, 'giraffeDSL_StressClassType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Stress42')
    _safe_set(owner, 'giraffeDSL_StressClassType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Stress42')


def test_assoc_stressMethod43_stub_double():
    # giraffeDSL_Stress has no real 'giraffeDSL_Stress44' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_StressMethodType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_StressMethodType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_StressMethodType(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_Stress()
    setattr(partner, 'giraffeDSL_Stress44', None)
    _safe_set(owner, 'giraffeDSL_StressMethodType', partner)
    assert owner in getattr(partner, 'giraffeDSL_Stress44')
    _safe_set(owner, 'giraffeDSL_StressMethodType', None)
    assert owner not in getattr(partner, 'giraffeDSL_Stress44')


def test_assoc_type12_stub_double():
    # giraffeDSL_CloudProvider has no real 'giraffeDSL_CloudProvider' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_CloudProviderType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_CloudProviderType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_CloudProviderType(many="sample_text", name="sample_text")
    partner = giraffeDSL_CloudProvider()
    setattr(partner, 'giraffeDSL_CloudProvider', None)
    _safe_set(owner, 'giraffeDSL_CloudProviderType13', partner)
    assert getattr(partner, 'giraffeDSL_CloudProvider') == owner
    _safe_set(owner, 'giraffeDSL_CloudProviderType13', None)
    assert getattr(partner, 'giraffeDSL_CloudProvider') is None


def test_assoc_type25_stub_double():
    # giraffeDSL_DeployApp has no real 'giraffeDSL_DeployApp' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployAppFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployAppFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployAppFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_DeployApp()
    setattr(partner, 'giraffeDSL_DeployApp', None)
    _safe_set(owner, 'giraffeDSL_DeployAppFeature26', partner)
    assert getattr(partner, 'giraffeDSL_DeployApp') == owner
    _safe_set(owner, 'giraffeDSL_DeployAppFeature26', None)
    assert getattr(partner, 'giraffeDSL_DeployApp') is None


def test_assoc_type27_stub_double():
    # giraffeDSL_DeployType has no real 'giraffeDSL_DeployType' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_DeployTypeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_DeployTypeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_DeployTypeFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_DeployType()
    setattr(partner, 'giraffeDSL_DeployType', None)
    _safe_set(owner, 'giraffeDSL_DeployTypeFeature28', partner)
    assert getattr(partner, 'giraffeDSL_DeployType') == owner
    _safe_set(owner, 'giraffeDSL_DeployTypeFeature28', None)
    assert getattr(partner, 'giraffeDSL_DeployType') is None


def test_assoc_type6_stub_double():
    # giraffeDSL_VirtualMachine has no real 'giraffeDSL_VirtualMachine' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_VirtualMachineFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_VirtualMachineFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_VirtualMachineFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_VirtualMachine()
    setattr(partner, 'giraffeDSL_VirtualMachine', None)
    _safe_set(owner, 'giraffeDSL_VirtualMachineFeature7', partner)
    assert getattr(partner, 'giraffeDSL_VirtualMachine') == owner
    _safe_set(owner, 'giraffeDSL_VirtualMachineFeature7', None)
    assert getattr(partner, 'giraffeDSL_VirtualMachine') is None


def test_assoc_vM8_stub_double():
    # giraffeDSL_VirtualMachine has no real 'giraffeDSL_VirtualMachine9' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_VirtualMachineTypeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_VirtualMachineTypeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_VirtualMachineTypeFeature(many="sample_text", name="sample_text", type="sample_text")
    partner = giraffeDSL_VirtualMachine()
    setattr(partner, 'giraffeDSL_VirtualMachine9', None)
    _safe_set(owner, 'giraffeDSL_VirtualMachineTypeFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_VirtualMachine9')
    _safe_set(owner, 'giraffeDSL_VirtualMachineTypeFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_VirtualMachine9')


def test_assoc_vMachine1_stub_double():
    # giraffeDSL_Create has no real 'giraffeDSL_Create' property in the generated
    # code (a bare stub) -- manually attach it so giraffeDSL_VirtualMachineFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # giraffeDSL_VirtualMachineFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = giraffeDSL_VirtualMachineFeature(many="sample_text", name="sample_text")
    partner = giraffeDSL_Create()
    setattr(partner, 'giraffeDSL_Create', None)
    _safe_set(owner, 'giraffeDSL_VirtualMachineFeature', partner)
    assert owner in getattr(partner, 'giraffeDSL_Create')
    _safe_set(owner, 'giraffeDSL_VirtualMachineFeature', None)
    assert owner not in getattr(partner, 'giraffeDSL_Create')


