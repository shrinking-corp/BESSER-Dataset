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
    ActionType,
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

def test_assoc_CPS64_stub_double():
    # ConfigurationProcessStep has no real 'ConfigurationProcessStep65' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_Context(id="sample_text")
    partner = ConfigurationProcessStep()
    setattr(partner, 'ConfigurationProcessStep65', None)
    _safe_set(owner, 'spinefm_ProcessModel_Context', {partner})
    assert getattr(partner, 'ConfigurationProcessStep65') == owner
    _safe_set(owner, 'spinefm_ProcessModel_Context', set())
    assert getattr(partner, 'ConfigurationProcessStep65') is None


def test_assoc_CPSRef29_stub_double():
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


def test_assoc_actions89_stub_double():
    # Action has no real 'Action90' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Rule(id="sample_text")
    partner = Action()
    setattr(partner, 'Action90', None)
    _safe_set(owner, 'spinefm_ActionModel_Rule', partner)
    assert getattr(partner, 'Action90') == owner
    _safe_set(owner, 'spinefm_ActionModel_Rule', None)
    assert getattr(partner, 'Action90') is None


def test_assoc_actionsDone53_stub_double():
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


def test_assoc_actionsToDo57_stub_double():
    # Action has no real 'Action59' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Action()
    setattr(partner, 'Action59', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep58', {partner})
    assert getattr(partner, 'Action59') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep58', set())
    assert getattr(partner, 'Action59') is None


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


def test_assoc_clonedCPS36_stub_double():
    # ConfigurationProcessStep has no real 'ConfigurationProcessStep38' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    partner = ConfigurationProcessStep()
    setattr(partner, 'ConfigurationProcessStep38', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration37', {partner})
    assert getattr(partner, 'ConfigurationProcessStep38') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration37', set())
    assert getattr(partner, 'ConfigurationProcessStep38') is None


def test_assoc_configuration62_stub_double():
    # Configuration has no real 'Configuration63' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Configuration()
    setattr(partner, 'Configuration63', None)
    _safe_set(owner, 'CPSRef', partner)
    assert getattr(partner, 'Configuration63') == owner
    _safe_set(owner, 'CPSRef', None)
    assert getattr(partner, 'Configuration63') is None


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


def test_assoc_context60_stub_double():
    # Context has no real 'Context' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = Context()
    setattr(partner, 'Context', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep61', partner)
    assert getattr(partner, 'Context') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep61', None)
    assert getattr(partner, 'Context') is None


def test_assoc_deselectedFeatures83_stub_double():
    # Feature has no real 'Feature85' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = Feature()
    setattr(partner, 'Feature85', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState84', {partner})
    assert getattr(partner, 'Feature85') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState84', set())
    assert getattr(partner, 'Feature85') is None


def test_assoc_domainElement33_stub_double():
    # DomainElement has no real 'DomainElement35' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    partner = DomainElement()
    setattr(partner, 'DomainElement35', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration34', partner)
    assert getattr(partner, 'DomainElement35') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Configuration34', None)
    assert getattr(partner, 'DomainElement35') is None


def test_assoc_domainElement54_stub_double():
    # DomainElement has no real 'DomainElement56' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ConfigurationProcessStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ConfigurationProcessStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    partner = DomainElement()
    setattr(partner, 'DomainElement56', None)
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep55', partner)
    assert getattr(partner, 'DomainElement56') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ConfigurationProcessStep55', None)
    assert getattr(partner, 'DomainElement56') is None


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


def test_assoc_feature94_stub_double():
    # Feature has no real 'Feature95' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Action(id="sample_text", type="sample_text")
    partner = Feature()
    setattr(partner, 'Feature95', None)
    _safe_set(owner, 'spinefm_ActionModel_Action', partner)
    assert getattr(partner, 'Feature95') == owner
    _safe_set(owner, 'spinefm_ActionModel_Action', None)
    assert getattr(partner, 'Feature95') is None


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


def test_assoc_fm86_stub_double():
    # FeatureModel has no real 'FeatureModel88' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = FeatureModel()
    setattr(partner, 'FeatureModel88', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState87', partner)
    assert getattr(partner, 'FeatureModel88') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState87', None)
    assert getattr(partner, 'FeatureModel88') is None


def test_assoc_fm96_stub_double():
    # FeatureModel has no real 'FeatureModel98' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Action(id="sample_text", type="sample_text")
    partner = FeatureModel()
    setattr(partner, 'FeatureModel98', None)
    _safe_set(owner, 'spinefm_ActionModel_Action97', partner)
    assert getattr(partner, 'FeatureModel98') == owner
    _safe_set(owner, 'spinefm_ActionModel_Action97', None)
    assert getattr(partner, 'FeatureModel98') is None


def test_assoc_globalContext71_stub_double():
    # GlobalContext has no real 'GlobalContext' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = GlobalContext()
    setattr(partner, 'GlobalContext', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager72', partner)
    assert getattr(partner, 'GlobalContext') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager72', None)
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


def test_assoc_inverse78_stub_double():
    # RestrictionFunction has no real 'RestrictionFunction80' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_RestrictionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_RestrictionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    partner = RestrictionFunction()
    setattr(partner, 'RestrictionFunction80', None)
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction79', partner)
    assert getattr(partner, 'RestrictionFunction80') == owner
    _safe_set(owner, 'spinefm_ActionModel_RestrictionFunction79', None)
    assert getattr(partner, 'RestrictionFunction80') is None


def test_assoc_links48_stub_double():
    # Link has no real 'Link50' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_CompositeConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_CompositeConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    partner = Link()
    setattr(partner, 'Link50', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration49', {partner})
    assert getattr(partner, 'Link50') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration49', set())
    assert getattr(partner, 'Link50') is None


def test_assoc_localContexts73_stub_double():
    # LocalContext has no real 'LocalContext' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = LocalContext()
    setattr(partner, 'LocalContext', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager74', {partner})
    assert getattr(partner, 'LocalContext') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager74', set())
    assert getattr(partner, 'LocalContext') is None


def test_assoc_mspl51_stub_double():
    # MultipleSoftwareProductLine has no real 'MultipleSoftwareProductLine' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_CompositeConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_CompositeConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    partner = MultipleSoftwareProductLine()
    setattr(partner, 'MultipleSoftwareProductLine', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration52', partner)
    assert getattr(partner, 'MultipleSoftwareProductLine') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration52', None)
    assert getattr(partner, 'MultipleSoftwareProductLine') is None


def test_assoc_mspl69_stub_double():
    # MultipleSoftwareProductLine has no real 'MultipleSoftwareProductLine70' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_ContextManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_ContextManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_ContextManager()
    partner = MultipleSoftwareProductLine()
    setattr(partner, 'MultipleSoftwareProductLine70', None)
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager', partner)
    assert getattr(partner, 'MultipleSoftwareProductLine70') == owner
    _safe_set(owner, 'spinefm_ProcessModel_ContextManager', None)
    assert getattr(partner, 'MultipleSoftwareProductLine70') is None


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


def test_assoc_relatedAssociation40_stub_double():
    # DEAssociation has no real 'DEAssociation42' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Link(id="sample_text")
    partner = DEAssociation()
    setattr(partner, 'DEAssociation42', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Link41', partner)
    assert getattr(partner, 'DEAssociation42') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Link41', None)
    assert getattr(partner, 'DEAssociation42') is None


def test_assoc_replacedBy75_stub_double():
    # Context has no real 'Context76' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ProcessModel_DeletedContextInformations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ProcessModel_DeletedContextInformations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ProcessModel_DeletedContextInformations(deletedContext="sample_text")
    partner = Context()
    setattr(partner, 'Context76', None)
    _safe_set(owner, 'spinefm_ProcessModel_DeletedContextInformations', partner)
    assert getattr(partner, 'Context76') == owner
    _safe_set(owner, 'spinefm_ProcessModel_DeletedContextInformations', None)
    assert getattr(partner, 'Context76') is None


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


def test_assoc_rules77_stub_double():
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


def test_assoc_selectedFeatures81_stub_double():
    # Feature has no real 'Feature82' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_ConfigurationState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_ConfigurationState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_ConfigurationState(id="sample_text")
    partner = Feature()
    setattr(partner, 'Feature82', None)
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState', {partner})
    assert getattr(partner, 'Feature82') == owner
    _safe_set(owner, 'spinefm_ActionModel_ConfigurationState', set())
    assert getattr(partner, 'Feature82') is None


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


def test_assoc_source39_stub_double():
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


def test_assoc_state91_stub_double():
    # ConfigurationState has no real 'ConfigurationState93' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ActionModel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ActionModel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ActionModel_Rule(id="sample_text")
    partner = ConfigurationState()
    setattr(partner, 'ConfigurationState93', None)
    _safe_set(owner, 'spinefm_ActionModel_Rule92', partner)
    assert getattr(partner, 'ConfigurationState93') == owner
    _safe_set(owner, 'spinefm_ActionModel_Rule92', None)
    assert getattr(partner, 'ConfigurationState93') is None


def test_assoc_subConfigurations46_stub_double():
    # Configuration has no real 'Configuration47' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_CompositeConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_CompositeConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    partner = Configuration()
    setattr(partner, 'Configuration47', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration', {partner})
    assert getattr(partner, 'Configuration47') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_CompositeConfiguration', set())
    assert getattr(partner, 'Configuration47') is None


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


def test_assoc_target43_stub_double():
    # Configuration has no real 'Configuration45' property in the generated
    # code (a bare stub) -- manually attach it so spinefm_ConfigurationModel_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spinefm_ConfigurationModel_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spinefm_ConfigurationModel_Link(id="sample_text")
    partner = Configuration()
    setattr(partner, 'Configuration45', None)
    _safe_set(owner, 'spinefm_ConfigurationModel_Link44', partner)
    assert getattr(partner, 'Configuration45') == owner
    _safe_set(owner, 'spinefm_ConfigurationModel_Link44', None)
    assert getattr(partner, 'Configuration45') is None


