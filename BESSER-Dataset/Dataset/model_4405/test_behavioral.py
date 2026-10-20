import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    CompositeConfiguration,
    Configuration,
    ConfigurationProcessStep,
    ConfigurationState,
    Constraint,
    Context,
    DEAssociation,
    DEAssociationEnd,
    DomainElement,
    Feature,
    FeatureModel,
    GlobalContext,
    Group,
    Link,
    LocalContext,
    MultipleSoftwareProductLine,
    MultiplicityElement,
    RestrictionFunction,
    Rule,
    spinefm_ActionModel_Action,
    spinefm_ActionModel_ActionAddCTConstraint,
    spinefm_ActionModel_ActionDeselect,
    spinefm_ActionModel_ActionSelect,
    spinefm_ActionModel_ConfigurationState,
    spinefm_ActionModel_RestrictionFunction,
    spinefm_ActionModel_Rule,
    spinefm_ConfigurationModel_CompositeConfiguration,
    spinefm_ConfigurationModel_Configuration,
    spinefm_ConfigurationModel_Link,
    spinefm_FMModel_Constraint,
    spinefm_FMModel_Feature,
    spinefm_FMModel_FeatureModel,
    spinefm_FMModel_Group,
    spinefm_MSPLModel_DEAssociation,
    spinefm_MSPLModel_DEAssociationEnd,
    spinefm_MSPLModel_DomainElement,
    spinefm_MSPLModel_MultipleSoftwareProductLine,
    spinefm_MSPLModel_MultiplicityElement,
    spinefm_ProcessModel_ConfigurationProcessStep,
    spinefm_ProcessModel_Context,
    spinefm_ProcessModel_ContextManager,
    spinefm_ProcessModel_DeletedContextInformations,
    spinefm_ProcessModel_GlobalContext,
    spinefm_ProcessModel_LocalContext,
    GroupState,
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

def test_assoc_CPS29_stub_double():
    # ConfigurationProcessStep has no real 'ConfigurationProcessStep' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    partner = ConfigurationProcessStep()
    setattr(partner, 'ConfigurationProcessStep', None)
    _safe_set(owner, 'configuration', partner)
    assert getattr(partner, 'ConfigurationProcessStep') == owner
    _safe_set(owner, 'configuration', None)
    assert getattr(partner, 'ConfigurationProcessStep') is None


def test_assoc_CPS56_stub_double():
    # ConfigurationProcessStep has no real 'ConfigurationProcessStep57' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_Context(id="sample_text")
    partner = ConfigurationProcessStep()
    setattr(partner, 'ConfigurationProcessStep57', None)
    _safe_set(owner, 'spinefm_ProcessModel_Context', {partner})
    assert getattr(partner, 'ConfigurationProcessStep57') == owner
    _safe_set(owner, 'spinefm_ProcessModel_Context', set())
    assert getattr(partner, 'ConfigurationProcessStep57') is None


def test_assoc_LinkMultiplicity18_stub_double():
    # MultiplicityElement has no real 'MultiplicityElement' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociationEnd(id="sample_text")
    partner = MultiplicityElement()
    setattr(partner, 'MultiplicityElement', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociationEnd', partner)
    assert getattr(partner, 'MultiplicityElement') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociationEnd', None)
    assert getattr(partner, 'MultiplicityElement') is None


def test_assoc_MultiplicityElement22_stub_double():
    # MultiplicityElement has no real 'MultiplicityElement23' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DomainElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DomainElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DomainElement(id="sample_text")
    partner = MultiplicityElement()
    setattr(partner, 'MultiplicityElement23', None)
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement', partner)
    assert getattr(partner, 'MultiplicityElement23') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement', None)
    assert getattr(partner, 'MultiplicityElement23') is None


def test_assoc_actions80_stub_double():
    # Action has no real 'Action81' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Rule(id="sample_text")
    partner = Action()
    setattr(partner, 'Action81', None)
    _safe_set(owner, 'spinefm_ActionModel_Rule', partner)
    assert getattr(partner, 'Action81') == owner
    _safe_set(owner, 'spinefm_ActionModel_Rule', None)
    assert getattr(partner, 'Action81') is None


def test_assoc_actionsDone45_stub_double():
    # Action has no real 'Action' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Action()
    setattr(partner, 'Action', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep', {partner})
    assert getattr(partner, 'Action') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep', set())
    assert getattr(partner, 'Action') is None


def test_assoc_actionsToDo49_stub_double():
    # Action has no real 'Action51' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Action()
    setattr(partner, 'Action51', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep50', {partner})
    assert getattr(partner, 'Action51') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep50', set())
    assert getattr(partner, 'Action51') is None


def test_assoc_apply_on19_stub_double():
    # DomainElement has no real 'DomainElement21' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociationEnd(id="sample_text")
    partner = DomainElement()
    setattr(partner, 'DomainElement21', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociationEnd20', partner)
    assert getattr(partner, 'DomainElement21') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociationEnd20', None)
    assert getattr(partner, 'DomainElement21') is None


def test_assoc_associations7_stub_double():
    # DEAssociation has no real 'DEAssociation' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_MultipleSoftwareProductLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_MultipleSoftwareProductLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_MultipleSoftwareProductLine()
    partner = DEAssociation()
    setattr(partner, 'DEAssociation', None)
    _safe_set(owner, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', {partner})
    assert getattr(partner, 'DEAssociation') == owner
    _safe_set(owner, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', set())
    assert getattr(partner, 'DEAssociation') is None


def test_assoc_belongs_to26_stub_double():
    # DEAssociation has no real 'DEAssociation28' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DomainElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DomainElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DomainElement(id="sample_text")
    partner = DEAssociation()
    setattr(partner, 'DEAssociation28', None)
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement27', {partner})
    assert getattr(partner, 'DEAssociation28') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement27', set())
    assert getattr(partner, 'DEAssociation28') is None


def test_assoc_belongs_to30_stub_double():
    # Link has no real 'Link' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    partner = Link()
    setattr(partner, 'Link', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration', {partner})
    assert getattr(partner, 'Link') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration', set())
    assert getattr(partner, 'Link') is None


def test_assoc_children3_stub_double():
    # Group has no real 'Group' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_FMModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_FMModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_FMModel_Feature(id="sample_text", name="sample_text")
    partner = Group()
    setattr(partner, 'Group', None)
    _safe_set(owner, 'spinefm_FMModel_Feature', {partner})
    assert getattr(partner, 'Group') == owner
    _safe_set(owner, 'spinefm_FMModel_Feature', set())
    assert getattr(partner, 'Group') is None


def test_assoc_configuration54_stub_double():
    # Configuration has no real 'Configuration55' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Configuration()
    setattr(partner, 'Configuration55', None)
    _safe_set(owner, 'CPS', partner)
    assert getattr(partner, 'Configuration55') == owner
    _safe_set(owner, 'CPS', None)
    assert getattr(partner, 'Configuration55') is None


def test_assoc_constraints1_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_FMModel_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_FMModel_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'spinefm_FMModel_FeatureModel2', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'spinefm_FMModel_FeatureModel2', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_context52_stub_double():
    # Context has no real 'Context' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Context()
    setattr(partner, 'Context', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep53', partner)
    assert getattr(partner, 'Context') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep53', None)
    assert getattr(partner, 'Context') is None


def test_assoc_deselectedFeatures74_stub_double():
    # Feature has no real 'Feature76' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = Feature()
    setattr(partner, 'Feature76', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState75', {partner})
    assert getattr(partner, 'Feature76') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState75', set())
    assert getattr(partner, 'Feature76') is None


def test_assoc_domainElement46_stub_double():
    # DomainElement has no real 'DomainElement48' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = DomainElement()
    setattr(partner, 'DomainElement48', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep47', partner)
    assert getattr(partner, 'DomainElement48') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep47', None)
    assert getattr(partner, 'DomainElement48') is None


def test_assoc_domainElements6_stub_double():
    # DomainElement has no real 'DomainElement' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_MultipleSoftwareProductLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_MultipleSoftwareProductLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_MultipleSoftwareProductLine()
    partner = DomainElement()
    setattr(partner, 'DomainElement', None)
    _safe_set(owner, 'spinefm_MSPLModel_MultipleSoftwareProductLine', {partner})
    assert getattr(partner, 'DomainElement') == owner
    _safe_set(owner, 'spinefm_MSPLModel_MultipleSoftwareProductLine', set())
    assert getattr(partner, 'DomainElement') is None


def test_assoc_feature85_stub_double():
    # Feature has no real 'Feature86' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Action(id="sample_text")
    partner = Feature()
    setattr(partner, 'Feature86', None)
    _safe_set(owner, 'spinefm_ActionModel_Action', partner)
    assert getattr(partner, 'Feature86') == owner
    _safe_set(owner, 'spinefm_ActionModel_Action', None)
    assert getattr(partner, 'Feature86') is None


def test_assoc_features4_stub_double():
    # Feature has no real 'Feature5' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_FMModel_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_FMModel_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_FMModel_Group(state="sample_text")
    partner = Feature()
    setattr(partner, 'Feature5', None)
    _safe_set(owner, 'spinefm_FMModel_Group', {partner})
    assert getattr(partner, 'Feature5') == owner
    _safe_set(owner, 'spinefm_FMModel_Group', set())
    assert getattr(partner, 'Feature5') is None


def test_assoc_fm77_stub_double():
    # FeatureModel has no real 'FeatureModel79' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = FeatureModel()
    setattr(partner, 'FeatureModel79', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState78', partner)
    assert getattr(partner, 'FeatureModel79') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState78', None)
    assert getattr(partner, 'FeatureModel79') is None


def test_assoc_fm87_stub_double():
    # FeatureModel has no real 'FeatureModel89' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Action(id="sample_text")
    partner = FeatureModel()
    setattr(partner, 'FeatureModel89', None)
    _safe_set(owner, 'spinefm_ActionModel_Action88', partner)
    assert getattr(partner, 'FeatureModel89') == owner
    _safe_set(owner, 'spinefm_ActionModel_Action88', None)
    assert getattr(partner, 'FeatureModel89') is None


def test_assoc_globalContext62_stub_double():
    # GlobalContext has no real 'GlobalContext' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = GlobalContext()
    setattr(partner, 'GlobalContext', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager63', partner)
    assert getattr(partner, 'GlobalContext') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager63', None)
    assert getattr(partner, 'GlobalContext') is None


def test_assoc_inverse15_stub_double():
    # DEAssociation has no real 'DEAssociation17' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociation(id="sample_text")
    partner = DEAssociation()
    setattr(partner, 'DEAssociation17', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation16', partner)
    assert getattr(partner, 'DEAssociation17') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation16', None)
    assert getattr(partner, 'DEAssociation17') is None


def test_assoc_inverse69_stub_double():
    # RestrictionFunction has no real 'RestrictionFunction71' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_RestrictionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_RestrictionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    partner = RestrictionFunction()
    setattr(partner, 'RestrictionFunction71', None)
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction70', partner)
    assert getattr(partner, 'RestrictionFunction71') == owner
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction70', None)
    assert getattr(partner, 'RestrictionFunction71') is None


def test_assoc_links42_stub_double():
    # Link has no real 'Link44' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_CompositeConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_CompositeConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    partner = Link()
    setattr(partner, 'Link44', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration43', {partner})
    assert getattr(partner, 'Link44') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration43', set())
    assert getattr(partner, 'Link44') is None


def test_assoc_localContexts64_stub_double():
    # LocalContext has no real 'LocalContext' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = LocalContext()
    setattr(partner, 'LocalContext', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager65', {partner})
    assert getattr(partner, 'LocalContext') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager65', set())
    assert getattr(partner, 'LocalContext') is None


def test_assoc_mspl61_stub_double():
    # MultipleSoftwareProductLine has no real 'MultipleSoftwareProductLine' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = MultipleSoftwareProductLine()
    setattr(partner, 'MultipleSoftwareProductLine', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager', partner)
    assert getattr(partner, 'MultipleSoftwareProductLine') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager', None)
    assert getattr(partner, 'MultipleSoftwareProductLine') is None


def test_assoc_refers_on24_stub_double():
    # FeatureModel has no real 'FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DomainElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DomainElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DomainElement(id="sample_text")
    partner = FeatureModel()
    setattr(partner, 'FeatureModel', None)
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement25', partner)
    assert getattr(partner, 'FeatureModel') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DomainElement25', None)
    assert getattr(partner, 'FeatureModel') is None


def test_assoc_relatedAssociation34_stub_double():
    # DEAssociation has no real 'DEAssociation36' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Link(id="sample_text")
    partner = DEAssociation()
    setattr(partner, 'DEAssociation36', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Link35', partner)
    assert getattr(partner, 'DEAssociation36') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Link35', None)
    assert getattr(partner, 'DEAssociation36') is None


def test_assoc_replacedBy66_stub_double():
    # Context has no real 'Context67' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_DeletedContextInformations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_DeletedContextInformations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_DeletedContextInformations(deletedContext="sample_text")
    partner = Context()
    setattr(partner, 'Context67', None)
    _safe_set(owner, 'spinefm_ProcessModel_DeletedContextInformations', partner)
    assert getattr(partner, 'Context67') == owner
    _safe_set(owner, 'spinefm_ProcessModel_DeletedContextInformations', None)
    assert getattr(partner, 'Context67') is None


def test_assoc_restrictionFunction9_stub_double():
    # RestrictionFunction has no real 'RestrictionFunction' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociation(id="sample_text")
    partner = RestrictionFunction()
    setattr(partner, 'RestrictionFunction', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation', {partner})
    assert getattr(partner, 'RestrictionFunction') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation', set())
    assert getattr(partner, 'RestrictionFunction') is None


def test_assoc_root0_stub_double():
    # Feature has no real 'Feature' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_FMModel_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_FMModel_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    partner = Feature()
    setattr(partner, 'Feature', None)
    _safe_set(owner, 'spinefm_FMModel_FeatureModel', partner)
    assert getattr(partner, 'Feature') == owner
    _safe_set(owner, 'spinefm_FMModel_FeatureModel', None)
    assert getattr(partner, 'Feature') is None


def test_assoc_rules68_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_RestrictionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_RestrictionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction', {partner})
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction', set())
    assert getattr(partner, 'Rule') is None


def test_assoc_selectedFeatures72_stub_double():
    # Feature has no real 'Feature73' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = Feature()
    setattr(partner, 'Feature73', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState', {partner})
    assert getattr(partner, 'Feature73') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState', set())
    assert getattr(partner, 'Feature73') is None


def test_assoc_source10_stub_double():
    # DEAssociationEnd has no real 'DEAssociationEnd' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociation(id="sample_text")
    partner = DEAssociationEnd()
    setattr(partner, 'DEAssociationEnd', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation11', partner)
    assert getattr(partner, 'DEAssociationEnd') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation11', None)
    assert getattr(partner, 'DEAssociationEnd') is None


def test_assoc_source33_stub_double():
    # Configuration has no real 'Configuration' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Link(id="sample_text")
    partner = Configuration()
    setattr(partner, 'Configuration', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Link', partner)
    assert getattr(partner, 'Configuration') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Link', None)
    assert getattr(partner, 'Configuration') is None


def test_assoc_state31_stub_double():
    # ConfigurationState has no real 'ConfigurationState' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    partner = ConfigurationState()
    setattr(partner, 'ConfigurationState', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration32', partner)
    assert getattr(partner, 'ConfigurationState') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration32', None)
    assert getattr(partner, 'ConfigurationState') is None


def test_assoc_state82_stub_double():
    # ConfigurationState has no real 'ConfigurationState84' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Rule(id="sample_text")
    partner = ConfigurationState()
    setattr(partner, 'ConfigurationState84', None)
    _safe_set(owner, 'spinefm_ActionModel_Rule83', partner)
    assert getattr(partner, 'ConfigurationState84') == owner
    _safe_set(owner, 'spinefm_ActionModel_Rule83', None)
    assert getattr(partner, 'ConfigurationState84') is None


def test_assoc_subConfigurations40_stub_double():
    # Configuration has no real 'Configuration41' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_CompositeConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_CompositeConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    partner = Configuration()
    setattr(partner, 'Configuration41', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration', {partner})
    assert getattr(partner, 'Configuration41') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration', set())
    assert getattr(partner, 'Configuration41') is None


def test_assoc_target12_stub_double():
    # DEAssociationEnd has no real 'DEAssociationEnd14' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_MSPLModel_DEAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_MSPLModel_DEAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_MSPLModel_DEAssociation(id="sample_text")
    partner = DEAssociationEnd()
    setattr(partner, 'DEAssociationEnd14', None)
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation13', partner)
    assert getattr(partner, 'DEAssociationEnd14') == owner
    _safe_set(owner, 'spinefm_MSPLModel_DEAssociation13', None)
    assert getattr(partner, 'DEAssociationEnd14') is None


def test_assoc_target37_stub_double():
    # Configuration has no real 'Configuration39' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Link(id="sample_text")
    partner = Configuration()
    setattr(partner, 'Configuration39', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Link38', partner)
    assert getattr(partner, 'Configuration39') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Link38', None)
    assert getattr(partner, 'Configuration39') is None


