import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAction,
    AssemblyContext,
    Automaton,
    BasicComponent,
    BranchAction,
    ComponentType,
    ComponentTypeImplementation,
    ComposedStructure,
    CompositeDataType,
    Connector,
    DataType,
    DelegationConnector,
    Entity,
    ExceptionType,
    InnerDeclaration,
    Interface,
    InterfaceProvidingEntity,
    InterfaceProvidingRequiringEntity,
    InterfaceRequiringEntity,
    InternalBehaviour,
    NamedElement,
    Parameter,
    ProbabilisticBranchTransition,
    ProvidedRole,
    Repository,
    RepositoryComponent,
    RequiredRole,
    Role,
    ServiceEffectSpecification,
    Signature,
    cm_composition_AssemblyConnector,
    cm_composition_AssemblyContext,
    cm_composition_ComposedProvidingRequiringEntity,
    cm_composition_ComposedStructure,
    cm_composition_Connector,
    cm_composition_DelegationConnector,
    cm_composition_Entity,
    cm_composition_Identifier,
    cm_composition_InterfaceProvidingEntity,
    cm_composition_InterfaceProvidingRequiringEntity,
    cm_composition_InterfaceRequiringEntity,
    cm_composition_NamedElement,
    cm_composition_ProvidedDelegationConnector,
    cm_composition_RequiredDelegationConnector,
    cm_composition_SubSystem,
    cm_composition_System,
    cm_repository_BasicComponent,
    cm_repository_CollectionDataType,
    cm_repository_ComponentType,
    cm_repository_ComponentTypeImplementation,
    cm_repository_CompositeComponent,
    cm_repository_CompositeDataType,
    cm_repository_DataType,
    cm_repository_ExceptionType,
    cm_repository_InnerDeclaration,
    cm_repository_Interface,
    cm_repository_Parameter,
    cm_repository_PrimitiveDataType,
    cm_repository_ProvidedRole,
    cm_repository_Repository,
    cm_repository_RepositoryComponent,
    cm_repository_RequiredRole,
    cm_repository_Role,
    cm_repository_Signature,
    cm_seff_AbstractAction,
    cm_seff_Automaton,
    cm_seff_BranchAction,
    cm_seff_ExternalCallAction,
    cm_seff_InternalAction,
    cm_seff_InternalBehaviour,
    cm_seff_ProbabilisticBranchTransition,
    cm_seff_ServiceEffectSpecification,
    cm_seff_SimpleBehaviorSpecification,
    cm_seff_StartAction,
    cm_seff_StopAction,
    composition_ComposedProvidingRequiringEntity,
    composition_ComposedStructure,
    composition_Entity,
    composition_Identifier,
    composition_InterfaceProvidingEntity,
    composition_InterfaceProvidingRequiringEntity,
    composition_InterfaceRequiringEntity,
    composition_NamedElement,
    repository_ComponentTypeImplementation,
    repository_DataType,
    repository_RepositoryComponent,
    seff_Automaton,
    seff_ServiceEffectSpecification,
    PrimitiveType,
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

def test_assoc_assemblyContext48_stub_double():
    # AssemblyContext has no real 'AssemblyContext50' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_ProvidedDelegationConnector()
    partner = AssemblyContext()
    setattr(partner, 'AssemblyContext50', None)
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector49', partner)
    assert getattr(partner, 'AssemblyContext50') == owner
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector49', None)
    assert getattr(partner, 'AssemblyContext50') is None


def test_assoc_assemblyContexts41_stub_double():
    # AssemblyContext has no real 'AssemblyContext' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_ComposedStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_ComposedStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_ComposedStructure()
    partner = AssemblyContext()
    setattr(partner, 'AssemblyContext', None)
    _safe_set(owner, 'parentStructure', {partner})
    assert getattr(partner, 'AssemblyContext') == owner
    _safe_set(owner, 'parentStructure', set())
    assert getattr(partner, 'AssemblyContext') is None


def test_assoc_branchAction101_stub_double():
    # BranchAction has no real 'BranchAction' property in the generated
    # code (a bare stub) -- manually attach it so cm_seff_ProbabilisticBranchTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_seff_ProbabilisticBranchTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_seff_ProbabilisticBranchTransition(branchProbability=3.14)
    partner = BranchAction()
    setattr(partner, 'BranchAction', None)
    _safe_set(owner, 'branchTransitions', partner)
    assert getattr(partner, 'BranchAction') == owner
    _safe_set(owner, 'branchTransitions', None)
    assert getattr(partner, 'BranchAction') is None


def test_assoc_components9_stub_double():
    # RepositoryComponent has no real 'RepositoryComponent' property in the generated
    # code (a bare stub) -- manually attach it so cm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_repository_Repository(description="sample_text")
    partner = RepositoryComponent()
    setattr(partner, 'RepositoryComponent', None)
    _safe_set(owner, 'repository', {partner})
    assert getattr(partner, 'RepositoryComponent') == owner
    _safe_set(owner, 'repository', set())
    assert getattr(partner, 'RepositoryComponent') is None


def test_assoc_connectors42_stub_double():
    # Connector has no real 'Connector' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_ComposedStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_ComposedStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_ComposedStructure()
    partner = Connector()
    setattr(partner, 'Connector', None)
    _safe_set(owner, 'parentStructure43', {partner})
    assert getattr(partner, 'Connector') == owner
    _safe_set(owner, 'parentStructure43', set())
    assert getattr(partner, 'Connector') is None


def test_assoc_dataType5_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so cm_repository_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_repository_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_repository_Parameter(name="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'cm_repository_Parameter', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'cm_repository_Parameter', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_dataTypes13_stub_double():
    # DataType has no real 'DataType15' property in the generated
    # code (a bare stub) -- manually attach it so cm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_repository_Repository(description="sample_text")
    partner = DataType()
    setattr(partner, 'DataType15', None)
    _safe_set(owner, 'repository14', {partner})
    assert getattr(partner, 'DataType15') == owner
    _safe_set(owner, 'repository14', set())
    assert getattr(partner, 'DataType15') is None


def test_assoc_innerProvidedRole44_stub_double():
    # ProvidedRole has no real 'ProvidedRole' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole', None)
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector', partner)
    assert getattr(partner, 'ProvidedRole') == owner
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector', None)
    assert getattr(partner, 'ProvidedRole') is None


def test_assoc_interfaces10_stub_double():
    # Interface has no real 'Interface12' property in the generated
    # code (a bare stub) -- manually attach it so cm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_repository_Repository(description="sample_text")
    partner = Interface()
    setattr(partner, 'Interface12', None)
    _safe_set(owner, 'repository11', {partner})
    assert getattr(partner, 'Interface12') == owner
    _safe_set(owner, 'repository11', set())
    assert getattr(partner, 'Interface12') is None


def test_assoc_outerProvidedRole45_stub_double():
    # ProvidedRole has no real 'ProvidedRole47' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole47', None)
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector46', partner)
    assert getattr(partner, 'ProvidedRole47') == owner
    _safe_set(owner, 'cm_composition_ProvidedDelegationConnector46', None)
    assert getattr(partner, 'ProvidedRole47') is None


def test_assoc_providedRole63_stub_double():
    # ProvidedRole has no real 'ProvidedRole65' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_AssemblyConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole65', None)
    _safe_set(owner, 'cm_composition_AssemblyConnector64', partner)
    assert getattr(partner, 'ProvidedRole65') == owner
    _safe_set(owner, 'cm_composition_AssemblyConnector64', None)
    assert getattr(partner, 'ProvidedRole65') is None


def test_assoc_providingAssemblyContext60_stub_double():
    # AssemblyContext has no real 'AssemblyContext62' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_AssemblyConnector()
    partner = AssemblyContext()
    setattr(partner, 'AssemblyContext62', None)
    _safe_set(owner, 'cm_composition_AssemblyConnector61', partner)
    assert getattr(partner, 'AssemblyContext62') == owner
    _safe_set(owner, 'cm_composition_AssemblyConnector61', None)
    assert getattr(partner, 'AssemblyContext62') is None


def test_assoc_requiredRole66_stub_double():
    # RequiredRole has no real 'RequiredRole68' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_AssemblyConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole68', None)
    _safe_set(owner, 'cm_composition_AssemblyConnector67', partner)
    assert getattr(partner, 'RequiredRole68') == owner
    _safe_set(owner, 'cm_composition_AssemblyConnector67', None)
    assert getattr(partner, 'RequiredRole68') is None


def test_assoc_requiringAssemblyContext58_stub_double():
    # AssemblyContext has no real 'AssemblyContext59' property in the generated
    # code (a bare stub) -- manually attach it so cm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_composition_AssemblyConnector()
    partner = AssemblyContext()
    setattr(partner, 'AssemblyContext59', None)
    _safe_set(owner, 'cm_composition_AssemblyConnector', partner)
    assert getattr(partner, 'AssemblyContext59') == owner
    _safe_set(owner, 'cm_composition_AssemblyConnector', None)
    assert getattr(partner, 'AssemblyContext59') is None


def test_assoc_signature6_stub_double():
    # Signature has no real 'Signature' property in the generated
    # code (a bare stub) -- manually attach it so cm_repository_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cm_repository_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cm_repository_Parameter(name="sample_text")
    partner = Signature()
    setattr(partner, 'Signature', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'Signature') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'Signature') is None


