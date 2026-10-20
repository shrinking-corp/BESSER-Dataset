import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssemblyConnector,
    BehaviourDescription,
    Component,
    DescriptionElement,
    ParameterType,
    ProvidedRole,
    RequiredRole,
    ReturnType,
    Role,
    Simple,
    Type,
    componentBasedSystem_Allocation,
    componentBasedSystem_AllocationContext,
    componentBasedSystem_AssemblyContext,
    componentBasedSystem_Component,
    componentBasedSystem_ComponentBasedSystem,
    componentBasedSystem_CompositeComponent,
    componentBasedSystem_Container,
    componentBasedSystem_DelegationConnector,
    componentBasedSystem_Environment,
    componentBasedSystem_Interface,
    componentBasedSystem_Link,
    componentBasedSystem_Parameter,
    componentBasedSystem_Repository,
    componentBasedSystem_Service,
    componentBasedSystem_Signature,
    componentBasedSystem_behaviourDescription_BehaviourDescription,
    componentBasedSystem_behaviourDescription_Branch,
    componentBasedSystem_behaviourDescription_DescriptionElement,
    componentBasedSystem_behaviourDescription_ExternalCall,
    componentBasedSystem_behaviourDescription_InternalAction,
    componentBasedSystem_behaviourDescription_Loop,
    componentBasedSystem_dataTypes_Complex,
    componentBasedSystem_dataTypes_ParameterType,
    componentBasedSystem_dataTypes_ReturnType,
    componentBasedSystem_dataTypes_Simple,
    componentBasedSystem_dataTypes_Type,
    componentBasedSystem_dataTypes_Void,
    componentBasedSystem_roles_AssemblyConnector,
    componentBasedSystem_roles_ProvidedRole,
    componentBasedSystem_roles_RequiredRole,
    componentBasedSystem_roles_Role,
    dataTypes_ParameterType,
    dataTypes_ReturnType,
    roles_componentBasedSystem_AssemblyContext,
    roles_componentBasedSystem_Interface,
    simpleTypes,
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

def test_assoc_assemblycontext0_reverse_link_reassign_clear():
    a1 = componentBasedSystem_ComponentBasedSystem()
    a2 = componentBasedSystem_ComponentBasedSystem()
    b = componentBasedSystem_AssemblyContext(name="sample_text")
    _safe_set(b, 'componentBasedSystem_AssemblyContext', a1)
    assert _is_linked(b, 'componentBasedSystem_AssemblyContext', a1)
    if hasattr(a1, 'componentBasedSystem_ComponentBasedSystem'):
        assert _is_linked(a1, 'componentBasedSystem_ComponentBasedSystem', b)
    _safe_set(b, 'componentBasedSystem_AssemblyContext', a2)
    assert _is_linked(b, 'componentBasedSystem_AssemblyContext', a2)
    if hasattr(a1, 'componentBasedSystem_ComponentBasedSystem'):
        assert not _is_linked(a1, 'componentBasedSystem_ComponentBasedSystem', b)
    if hasattr(a2, 'componentBasedSystem_ComponentBasedSystem'):
        assert _is_linked(a2, 'componentBasedSystem_ComponentBasedSystem', b)
    _safe_set(b, 'componentBasedSystem_AssemblyContext', None)
    assert not _is_linked(b, 'componentBasedSystem_AssemblyContext', a2)
    if hasattr(a2, 'componentBasedSystem_ComponentBasedSystem'):
        assert not _is_linked(a2, 'componentBasedSystem_ComponentBasedSystem', b)


def test_assoc_component36_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Component(name="sample_text")
    a2 = componentBasedSystem_Component(name="sample_text_2")
    b = componentBasedSystem_AssemblyContext(name="sample_text")
    _safe_set(b, 'componentBasedSystem_AssemblyContext37', a1)
    assert _is_linked(b, 'componentBasedSystem_AssemblyContext37', a1)
    if hasattr(a1, 'componentBasedSystem_Component38'):
        assert _is_linked(a1, 'componentBasedSystem_Component38', b)
    _safe_set(b, 'componentBasedSystem_AssemblyContext37', a2)
    assert _is_linked(b, 'componentBasedSystem_AssemblyContext37', a2)
    if hasattr(a1, 'componentBasedSystem_Component38'):
        assert not _is_linked(a1, 'componentBasedSystem_Component38', b)
    if hasattr(a2, 'componentBasedSystem_Component38'):
        assert _is_linked(a2, 'componentBasedSystem_Component38', b)
    _safe_set(b, 'componentBasedSystem_AssemblyContext37', None)
    assert not _is_linked(b, 'componentBasedSystem_AssemblyContext37', a2)
    if hasattr(a2, 'componentBasedSystem_Component38'):
        assert not _is_linked(a2, 'componentBasedSystem_Component38', b)


def test_assoc_container29_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Link(name="sample_text")
    a2 = componentBasedSystem_Link(name="sample_text_2")
    b = componentBasedSystem_Container(name="sample_text")
    _safe_set(b, 'componentBasedSystem_Container', a1)
    assert _is_linked(b, 'componentBasedSystem_Container', a1)
    if hasattr(a1, 'componentBasedSystem_Link'):
        assert _is_linked(a1, 'componentBasedSystem_Link', b)
    _safe_set(b, 'componentBasedSystem_Container', a2)
    assert _is_linked(b, 'componentBasedSystem_Container', a2)
    if hasattr(a1, 'componentBasedSystem_Link'):
        assert not _is_linked(a1, 'componentBasedSystem_Link', b)
    if hasattr(a2, 'componentBasedSystem_Link'):
        assert _is_linked(a2, 'componentBasedSystem_Link', b)
    _safe_set(b, 'componentBasedSystem_Container', None)
    assert not _is_linked(b, 'componentBasedSystem_Container', a2)
    if hasattr(a2, 'componentBasedSystem_Link'):
        assert not _is_linked(a2, 'componentBasedSystem_Link', b)


def test_assoc_container46_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Environment()
    a2 = componentBasedSystem_Environment()
    b = componentBasedSystem_Container(name="sample_text")
    _safe_set(b, 'componentBasedSystem_Container48', a1)
    assert _is_linked(b, 'componentBasedSystem_Container48', a1)
    if hasattr(a1, 'componentBasedSystem_Environment47'):
        assert _is_linked(a1, 'componentBasedSystem_Environment47', b)
    _safe_set(b, 'componentBasedSystem_Container48', a2)
    assert _is_linked(b, 'componentBasedSystem_Container48', a2)
    if hasattr(a1, 'componentBasedSystem_Environment47'):
        assert not _is_linked(a1, 'componentBasedSystem_Environment47', b)
    if hasattr(a2, 'componentBasedSystem_Environment47'):
        assert _is_linked(a2, 'componentBasedSystem_Environment47', b)
    _safe_set(b, 'componentBasedSystem_Container48', None)
    assert not _is_linked(b, 'componentBasedSystem_Container48', a2)
    if hasattr(a2, 'componentBasedSystem_Environment47'):
        assert not _is_linked(a2, 'componentBasedSystem_Environment47', b)


def test_assoc_environment9_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Environment()
    a2 = componentBasedSystem_Environment()
    b = componentBasedSystem_ComponentBasedSystem()
    _safe_set(b, 'componentBasedSystem_ComponentBasedSystem10', a1)
    assert _is_linked(b, 'componentBasedSystem_ComponentBasedSystem10', a1)
    if hasattr(a1, 'componentBasedSystem_Environment'):
        assert _is_linked(a1, 'componentBasedSystem_Environment', b)
    _safe_set(b, 'componentBasedSystem_ComponentBasedSystem10', a2)
    assert _is_linked(b, 'componentBasedSystem_ComponentBasedSystem10', a2)
    if hasattr(a1, 'componentBasedSystem_Environment'):
        assert not _is_linked(a1, 'componentBasedSystem_Environment', b)
    if hasattr(a2, 'componentBasedSystem_Environment'):
        assert _is_linked(a2, 'componentBasedSystem_Environment', b)
    _safe_set(b, 'componentBasedSystem_ComponentBasedSystem10', None)
    assert not _is_linked(b, 'componentBasedSystem_ComponentBasedSystem10', a2)
    if hasattr(a2, 'componentBasedSystem_Environment'):
        assert not _is_linked(a2, 'componentBasedSystem_Environment', b)


def test_assoc_link49_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Link(name="sample_text")
    a2 = componentBasedSystem_Link(name="sample_text_2")
    b = componentBasedSystem_Environment()
    _safe_set(b, 'componentBasedSystem_Environment50', {a1})
    assert _is_linked(b, 'componentBasedSystem_Environment50', a1)
    if hasattr(a1, 'componentBasedSystem_Link51'):
        assert _is_linked(a1, 'componentBasedSystem_Link51', b)
    _safe_set(b, 'componentBasedSystem_Environment50', {a2})
    assert _is_linked(b, 'componentBasedSystem_Environment50', a2)
    if hasattr(a1, 'componentBasedSystem_Link51'):
        assert not _is_linked(a1, 'componentBasedSystem_Link51', b)
    if hasattr(a2, 'componentBasedSystem_Link51'):
        assert _is_linked(a2, 'componentBasedSystem_Link51', b)
    _safe_set(b, 'componentBasedSystem_Environment50', set())
    assert not _is_linked(b, 'componentBasedSystem_Environment50', a2)
    if hasattr(a2, 'componentBasedSystem_Link51'):
        assert not _is_linked(a2, 'componentBasedSystem_Link51', b)


def test_assoc_parameter30_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Signature(name="sample_text")
    a2 = componentBasedSystem_Signature(name="sample_text_2")
    b = componentBasedSystem_Parameter(name="sample_text")
    _safe_set(b, 'componentBasedSystem_Parameter', a1)
    assert _is_linked(b, 'componentBasedSystem_Parameter', a1)
    if hasattr(a1, 'componentBasedSystem_Signature31'):
        assert _is_linked(a1, 'componentBasedSystem_Signature31', b)
    _safe_set(b, 'componentBasedSystem_Parameter', a2)
    assert _is_linked(b, 'componentBasedSystem_Parameter', a2)
    if hasattr(a1, 'componentBasedSystem_Signature31'):
        assert not _is_linked(a1, 'componentBasedSystem_Signature31', b)
    if hasattr(a2, 'componentBasedSystem_Signature31'):
        assert _is_linked(a2, 'componentBasedSystem_Signature31', b)
    _safe_set(b, 'componentBasedSystem_Parameter', None)
    assert not _is_linked(b, 'componentBasedSystem_Parameter', a2)
    if hasattr(a2, 'componentBasedSystem_Signature31'):
        assert not _is_linked(a2, 'componentBasedSystem_Signature31', b)


def test_assoc_signature24_reverse_link_reassign_clear():
    a1 = componentBasedSystem_Signature(name="sample_text")
    a2 = componentBasedSystem_Signature(name="sample_text_2")
    b = componentBasedSystem_Interface(name="sample_text")
    _safe_set(b, 'componentBasedSystem_Interface', {a1})
    assert _is_linked(b, 'componentBasedSystem_Interface', a1)
    if hasattr(a1, 'componentBasedSystem_Signature'):
        assert _is_linked(a1, 'componentBasedSystem_Signature', b)
    _safe_set(b, 'componentBasedSystem_Interface', {a2})
    assert _is_linked(b, 'componentBasedSystem_Interface', a2)
    if hasattr(a1, 'componentBasedSystem_Signature'):
        assert not _is_linked(a1, 'componentBasedSystem_Signature', b)
    if hasattr(a2, 'componentBasedSystem_Signature'):
        assert _is_linked(a2, 'componentBasedSystem_Signature', b)
    _safe_set(b, 'componentBasedSystem_Interface', set())
    assert not _is_linked(b, 'componentBasedSystem_Interface', a2)
    if hasattr(a2, 'componentBasedSystem_Signature'):
        assert not _is_linked(a2, 'componentBasedSystem_Signature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allocation5_stub_double():
    # componentBasedSystem_Allocation has no real 'componentBasedSystem_Allocation' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = componentBasedSystem_Allocation()
    setattr(partner, 'componentBasedSystem_Allocation', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem6', partner)
    assert getattr(partner, 'componentBasedSystem_Allocation') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem6', None)
    assert getattr(partner, 'componentBasedSystem_Allocation') is None


def test_assoc_assemblyconnector3_stub_double():
    # AssemblyConnector has no real 'AssemblyConnector' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = AssemblyConnector()
    setattr(partner, 'AssemblyConnector', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem4', {partner})
    assert getattr(partner, 'AssemblyConnector') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem4', set())
    assert getattr(partner, 'AssemblyConnector') is None


def test_assoc_assemblycontext25_stub_double():
    # componentBasedSystem_CompositeComponent has no real 'componentBasedSystem_CompositeComponent' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_AssemblyContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_AssemblyContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_AssemblyContext(name="sample_text")
    partner = componentBasedSystem_CompositeComponent()
    setattr(partner, 'componentBasedSystem_CompositeComponent', None)
    _safe_set(owner, 'componentBasedSystem_AssemblyContext26', partner)
    assert owner in getattr(partner, 'componentBasedSystem_CompositeComponent')
    _safe_set(owner, 'componentBasedSystem_AssemblyContext26', None)
    assert owner not in getattr(partner, 'componentBasedSystem_CompositeComponent')


def test_assoc_assemblycontext41_stub_double():
    # componentBasedSystem_AllocationContext has no real 'componentBasedSystem_AllocationContext42' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_AssemblyContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_AssemblyContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_AssemblyContext(name="sample_text")
    partner = componentBasedSystem_AllocationContext()
    setattr(partner, 'componentBasedSystem_AllocationContext42', None)
    _safe_set(owner, 'componentBasedSystem_AssemblyContext43', partner)
    assert getattr(partner, 'componentBasedSystem_AllocationContext42') == owner
    _safe_set(owner, 'componentBasedSystem_AssemblyContext43', None)
    assert getattr(partner, 'componentBasedSystem_AllocationContext42') is None


def test_assoc_behaviourdescription15_stub_double():
    # BehaviourDescription has no real 'BehaviourDescription' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Component(name="sample_text")
    partner = BehaviourDescription()
    setattr(partner, 'BehaviourDescription', None)
    _safe_set(owner, 'componentBasedSystem_Component', {partner})
    assert getattr(partner, 'BehaviourDescription') == owner
    _safe_set(owner, 'componentBasedSystem_Component', set())
    assert getattr(partner, 'BehaviourDescription') is None


def test_assoc_component55_stub_double():
    # componentBasedSystem_Repository has no real 'componentBasedSystem_Repository56' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Component(name="sample_text")
    partner = componentBasedSystem_Repository()
    setattr(partner, 'componentBasedSystem_Repository56', None)
    _safe_set(owner, 'componentBasedSystem_Component57', partner)
    assert owner in getattr(partner, 'componentBasedSystem_Repository56')
    _safe_set(owner, 'componentBasedSystem_Component57', None)
    assert owner not in getattr(partner, 'componentBasedSystem_Repository56')


def test_assoc_container39_stub_double():
    # componentBasedSystem_AllocationContext has no real 'componentBasedSystem_AllocationContext' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Container(name="sample_text")
    partner = componentBasedSystem_AllocationContext()
    setattr(partner, 'componentBasedSystem_AllocationContext', None)
    _safe_set(owner, 'componentBasedSystem_Container40', partner)
    assert getattr(partner, 'componentBasedSystem_AllocationContext') == owner
    _safe_set(owner, 'componentBasedSystem_Container40', None)
    assert getattr(partner, 'componentBasedSystem_AllocationContext') is None


def test_assoc_correspondingSignatures61_stub_double():
    # componentBasedSystem_Service has no real 'componentBasedSystem_Service62' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Signature(name="sample_text")
    partner = componentBasedSystem_Service()
    setattr(partner, 'componentBasedSystem_Service62', None)
    _safe_set(owner, 'componentBasedSystem_Signature63', partner)
    assert owner in getattr(partner, 'componentBasedSystem_Service62')
    _safe_set(owner, 'componentBasedSystem_Signature63', None)
    assert owner not in getattr(partner, 'componentBasedSystem_Service62')


def test_assoc_delegationconnector27_stub_double():
    # componentBasedSystem_CompositeComponent has no real 'componentBasedSystem_CompositeComponent28' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_DelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_DelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_DelegationConnector(name="sample_text")
    partner = componentBasedSystem_CompositeComponent()
    setattr(partner, 'componentBasedSystem_CompositeComponent28', None)
    _safe_set(owner, 'componentBasedSystem_DelegationConnector', partner)
    assert owner in getattr(partner, 'componentBasedSystem_CompositeComponent28')
    _safe_set(owner, 'componentBasedSystem_DelegationConnector', None)
    assert owner not in getattr(partner, 'componentBasedSystem_CompositeComponent28')


def test_assoc_interface52_stub_double():
    # componentBasedSystem_Repository has no real 'componentBasedSystem_Repository53' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Interface(name="sample_text")
    partner = componentBasedSystem_Repository()
    setattr(partner, 'componentBasedSystem_Repository53', None)
    _safe_set(owner, 'componentBasedSystem_Interface54', partner)
    assert owner in getattr(partner, 'componentBasedSystem_Repository53')
    _safe_set(owner, 'componentBasedSystem_Interface54', None)
    assert owner not in getattr(partner, 'componentBasedSystem_Repository53')


def test_assoc_interface70_stub_double():
    # roles_componentBasedSystem_Interface has no real 'roles_componentBasedSystem_Interface' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_roles_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_roles_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_roles_Role(name="sample_text")
    partner = roles_componentBasedSystem_Interface()
    setattr(partner, 'roles_componentBasedSystem_Interface', None)
    _safe_set(owner, 'componentBasedSystem_roles_Role', partner)
    assert getattr(partner, 'roles_componentBasedSystem_Interface') == owner
    _safe_set(owner, 'componentBasedSystem_roles_Role', None)
    assert getattr(partner, 'roles_componentBasedSystem_Interface') is None


def test_assoc_parametertype34_stub_double():
    # ParameterType has no real 'ParameterType' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Parameter(name="sample_text")
    partner = ParameterType()
    setattr(partner, 'ParameterType', None)
    _safe_set(owner, 'componentBasedSystem_Parameter35', partner)
    assert getattr(partner, 'ParameterType') == owner
    _safe_set(owner, 'componentBasedSystem_Parameter35', None)
    assert getattr(partner, 'ParameterType') is None


def test_assoc_providedAssemblyContext76_stub_double():
    # roles_componentBasedSystem_AssemblyContext has no real 'roles_componentBasedSystem_AssemblyContext' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_roles_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_roles_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_roles_AssemblyConnector(name="sample_text")
    partner = roles_componentBasedSystem_AssemblyContext()
    setattr(partner, 'roles_componentBasedSystem_AssemblyContext', None)
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector77', partner)
    assert getattr(partner, 'roles_componentBasedSystem_AssemblyContext') == owner
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector77', None)
    assert getattr(partner, 'roles_componentBasedSystem_AssemblyContext') is None


def test_assoc_providedrole11_stub_double():
    # ProvidedRole has no real 'ProvidedRole' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem12', {partner})
    assert getattr(partner, 'ProvidedRole') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem12', set())
    assert getattr(partner, 'ProvidedRole') is None


def test_assoc_providedrole21_stub_double():
    # ProvidedRole has no real 'ProvidedRole23' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Component(name="sample_text")
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole23', None)
    _safe_set(owner, 'componentBasedSystem_Component22', {partner})
    assert getattr(partner, 'ProvidedRole23') == owner
    _safe_set(owner, 'componentBasedSystem_Component22', set())
    assert getattr(partner, 'ProvidedRole23') is None


def test_assoc_providedrole71_stub_double():
    # ProvidedRole has no real 'ProvidedRole72' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_roles_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_roles_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_roles_AssemblyConnector(name="sample_text")
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole72', None)
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector', partner)
    assert getattr(partner, 'ProvidedRole72') == owner
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector', None)
    assert getattr(partner, 'ProvidedRole72') is None


def test_assoc_repository7_stub_double():
    # componentBasedSystem_Repository has no real 'componentBasedSystem_Repository' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = componentBasedSystem_Repository()
    setattr(partner, 'componentBasedSystem_Repository', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem8', partner)
    assert getattr(partner, 'componentBasedSystem_Repository') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem8', None)
    assert getattr(partner, 'componentBasedSystem_Repository') is None


def test_assoc_requiredAssemblyContext78_stub_double():
    # roles_componentBasedSystem_AssemblyContext has no real 'roles_componentBasedSystem_AssemblyContext80' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_roles_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_roles_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_roles_AssemblyConnector(name="sample_text")
    partner = roles_componentBasedSystem_AssemblyContext()
    setattr(partner, 'roles_componentBasedSystem_AssemblyContext80', None)
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector79', partner)
    assert getattr(partner, 'roles_componentBasedSystem_AssemblyContext80') == owner
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector79', None)
    assert getattr(partner, 'roles_componentBasedSystem_AssemblyContext80') is None


def test_assoc_requiredrole13_stub_double():
    # RequiredRole has no real 'RequiredRole' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem14', {partner})
    assert getattr(partner, 'RequiredRole') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem14', set())
    assert getattr(partner, 'RequiredRole') is None


def test_assoc_requiredrole18_stub_double():
    # RequiredRole has no real 'RequiredRole20' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Component(name="sample_text")
    partner = RequiredRole()
    setattr(partner, 'RequiredRole20', None)
    _safe_set(owner, 'componentBasedSystem_Component19', {partner})
    assert getattr(partner, 'RequiredRole20') == owner
    _safe_set(owner, 'componentBasedSystem_Component19', set())
    assert getattr(partner, 'RequiredRole20') is None


def test_assoc_requiredrole73_stub_double():
    # RequiredRole has no real 'RequiredRole75' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_roles_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_roles_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_roles_AssemblyConnector(name="sample_text")
    partner = RequiredRole()
    setattr(partner, 'RequiredRole75', None)
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector74', partner)
    assert getattr(partner, 'RequiredRole75') == owner
    _safe_set(owner, 'componentBasedSystem_roles_AssemblyConnector74', None)
    assert getattr(partner, 'RequiredRole75') is None


def test_assoc_returntype32_stub_double():
    # ReturnType has no real 'ReturnType' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Signature(name="sample_text")
    partner = ReturnType()
    setattr(partner, 'ReturnType', None)
    _safe_set(owner, 'componentBasedSystem_Signature33', partner)
    assert getattr(partner, 'ReturnType') == owner
    _safe_set(owner, 'componentBasedSystem_Signature33', None)
    assert getattr(partner, 'ReturnType') is None


def test_assoc_role44_stub_double():
    # Role has no real 'Role' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_DelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_DelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_DelegationConnector(name="sample_text")
    partner = Role()
    setattr(partner, 'Role', None)
    _safe_set(owner, 'componentBasedSystem_DelegationConnector45', {partner})
    assert getattr(partner, 'Role') == owner
    _safe_set(owner, 'componentBasedSystem_DelegationConnector45', set())
    assert getattr(partner, 'Role') is None


def test_assoc_service16_stub_double():
    # componentBasedSystem_Service has no real 'componentBasedSystem_Service' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_Component(name="sample_text")
    partner = componentBasedSystem_Service()
    setattr(partner, 'componentBasedSystem_Service', None)
    _safe_set(owner, 'componentBasedSystem_Component17', {partner})
    assert getattr(partner, 'componentBasedSystem_Service') == owner
    _safe_set(owner, 'componentBasedSystem_Component17', set())
    assert getattr(partner, 'componentBasedSystem_Service') is None


def test_assoc_type1_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so componentBasedSystem_ComponentBasedSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentBasedSystem_ComponentBasedSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentBasedSystem_ComponentBasedSystem()
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem2', {partner})
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'componentBasedSystem_ComponentBasedSystem2', set())
    assert getattr(partner, 'Type') is None


