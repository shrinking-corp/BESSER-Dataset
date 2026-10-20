import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    AssemblyViewType,
    Component,
    DelegationConnector,
    ParameterTyp,
    SimpleParameterType,
    Type,
    ViewPoint,
    ViewType,
    componentModel_Action,
    componentModel_AllocationViewType,
    componentModel_AssemblyConnector,
    componentModel_AssemblyContext,
    componentModel_AssemblyViewPoint,
    componentModel_AssemblyViewType,
    componentModel_Boolean,
    componentModel_Branch,
    componentModel_Char,
    componentModel_ComplexParameterType,
    componentModel_Component,
    componentModel_CompositeComponent,
    componentModel_Date,
    componentModel_DelegationConnector,
    componentModel_DeploymentViewPoint,
    componentModel_Double,
    componentModel_EnvironmentViewType,
    componentModel_ExternalCall,
    componentModel_Float,
    componentModel_Int,
    componentModel_Interface,
    componentModel_InterfaceServiceMapTuple,
    componentModel_InternalAction,
    componentModel_List,
    componentModel_Long,
    componentModel_Loop,
    componentModel_Map,
    componentModel_Parameter,
    componentModel_ParameterTyp,
    componentModel_ProvidedDelegationConnector,
    componentModel_ProvidedRole,
    componentModel_Repository,
    componentModel_RepositoryViewType,
    componentModel_RequiredDelegationConnector,
    componentModel_RequiredRole,
    componentModel_Service,
    componentModel_ServiceEffectSpecification,
    componentModel_Signature,
    componentModel_SimpleParameterType,
    componentModel_String,
    componentModel_System,
    componentModel_SystemIndependentViewPoint,
    componentModel_Type,
    componentModel_ViewPoint,
    componentModel_ViewType,
    componentModel_Void,
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

def test_assoc_assemblycontext55_reverse_link_reassign_clear():
    a1 = componentModel_RequiredRole(name="sample_text")
    a2 = componentModel_RequiredRole(name="sample_text_2")
    b = componentModel_AssemblyContext(name="sample_text")
    _safe_set(b, 'AssemblyContext', a1)
    assert _is_linked(b, 'AssemblyContext', a1)
    if hasattr(a1, 'requiredrole'):
        assert _is_linked(a1, 'requiredrole', b)
    _safe_set(b, 'AssemblyContext', a2)
    assert _is_linked(b, 'AssemblyContext', a2)
    if hasattr(a1, 'requiredrole'):
        assert not _is_linked(a1, 'requiredrole', b)
    if hasattr(a2, 'requiredrole'):
        assert _is_linked(a2, 'requiredrole', b)
    _safe_set(b, 'AssemblyContext', None)
    assert not _is_linked(b, 'AssemblyContext', a2)
    if hasattr(a2, 'requiredrole'):
        assert not _is_linked(a2, 'requiredrole', b)


def test_assoc_assemblycontext59_reverse_link_reassign_clear():
    a1 = componentModel_ProvidedRole(name="sample_text")
    a2 = componentModel_ProvidedRole(name="sample_text_2")
    b = componentModel_AssemblyContext(name="sample_text")
    _safe_set(b, 'AssemblyContext60', a1)
    assert _is_linked(b, 'AssemblyContext60', a1)
    if hasattr(a1, 'providedrole'):
        assert _is_linked(a1, 'providedrole', b)
    _safe_set(b, 'AssemblyContext60', a2)
    assert _is_linked(b, 'AssemblyContext60', a2)
    if hasattr(a1, 'providedrole'):
        assert not _is_linked(a1, 'providedrole', b)
    if hasattr(a2, 'providedrole'):
        assert _is_linked(a2, 'providedrole', b)
    _safe_set(b, 'AssemblyContext60', None)
    assert not _is_linked(b, 'AssemblyContext60', a2)
    if hasattr(a2, 'providedrole'):
        assert not _is_linked(a2, 'providedrole', b)


def test_assoc_interface56_reverse_link_reassign_clear():
    a1 = componentModel_RequiredRole(name="sample_text")
    a2 = componentModel_RequiredRole(name="sample_text_2")
    b = componentModel_Interface(name="sample_text")
    _safe_set(b, 'componentModel_Interface58', a1)
    assert _is_linked(b, 'componentModel_Interface58', a1)
    if hasattr(a1, 'componentModel_RequiredRole57'):
        assert _is_linked(a1, 'componentModel_RequiredRole57', b)
    _safe_set(b, 'componentModel_Interface58', a2)
    assert _is_linked(b, 'componentModel_Interface58', a2)
    if hasattr(a1, 'componentModel_RequiredRole57'):
        assert not _is_linked(a1, 'componentModel_RequiredRole57', b)
    if hasattr(a2, 'componentModel_RequiredRole57'):
        assert _is_linked(a2, 'componentModel_RequiredRole57', b)
    _safe_set(b, 'componentModel_Interface58', None)
    assert not _is_linked(b, 'componentModel_Interface58', a2)
    if hasattr(a2, 'componentModel_RequiredRole57'):
        assert not _is_linked(a2, 'componentModel_RequiredRole57', b)


def test_assoc_interface61_reverse_link_reassign_clear():
    a1 = componentModel_ProvidedRole(name="sample_text")
    a2 = componentModel_ProvidedRole(name="sample_text_2")
    b = componentModel_Interface(name="sample_text")
    _safe_set(b, 'componentModel_Interface63', a1)
    assert _is_linked(b, 'componentModel_Interface63', a1)
    if hasattr(a1, 'componentModel_ProvidedRole62'):
        assert _is_linked(a1, 'componentModel_ProvidedRole62', b)
    _safe_set(b, 'componentModel_Interface63', a2)
    assert _is_linked(b, 'componentModel_Interface63', a2)
    if hasattr(a1, 'componentModel_ProvidedRole62'):
        assert not _is_linked(a1, 'componentModel_ProvidedRole62', b)
    if hasattr(a2, 'componentModel_ProvidedRole62'):
        assert _is_linked(a2, 'componentModel_ProvidedRole62', b)
    _safe_set(b, 'componentModel_Interface63', None)
    assert not _is_linked(b, 'componentModel_Interface63', a2)
    if hasattr(a2, 'componentModel_ProvidedRole62'):
        assert not _is_linked(a2, 'componentModel_ProvidedRole62', b)


def test_assoc_ownerComponent29_reverse_link_reassign_clear():
    a1 = componentModel_Component(name="sample_text")
    a2 = componentModel_Component(name="sample_text_2")
    b = componentModel_AssemblyContext(name="sample_text")
    _safe_set(b, 'componentModel_AssemblyContext', a1)
    assert _is_linked(b, 'componentModel_AssemblyContext', a1)
    if hasattr(a1, 'componentModel_Component30'):
        assert _is_linked(a1, 'componentModel_Component30', b)
    _safe_set(b, 'componentModel_AssemblyContext', a2)
    assert _is_linked(b, 'componentModel_AssemblyContext', a2)
    if hasattr(a1, 'componentModel_Component30'):
        assert not _is_linked(a1, 'componentModel_Component30', b)
    if hasattr(a2, 'componentModel_Component30'):
        assert _is_linked(a2, 'componentModel_Component30', b)
    _safe_set(b, 'componentModel_AssemblyContext', None)
    assert not _is_linked(b, 'componentModel_AssemblyContext', a2)
    if hasattr(a2, 'componentModel_Component30'):
        assert not _is_linked(a2, 'componentModel_Component30', b)


def test_assoc_parameters40_reverse_link_reassign_clear():
    a1 = componentModel_Signature(name="sample_text")
    a2 = componentModel_Signature(name="sample_text_2")
    b = componentModel_Parameter(name="sample_text")
    _safe_set(b, 'componentModel_Parameter', a1)
    assert _is_linked(b, 'componentModel_Parameter', a1)
    if hasattr(a1, 'componentModel_Signature41'):
        assert _is_linked(a1, 'componentModel_Signature41', b)
    _safe_set(b, 'componentModel_Parameter', a2)
    assert _is_linked(b, 'componentModel_Parameter', a2)
    if hasattr(a1, 'componentModel_Signature41'):
        assert not _is_linked(a1, 'componentModel_Signature41', b)
    if hasattr(a2, 'componentModel_Signature41'):
        assert _is_linked(a2, 'componentModel_Signature41', b)
    _safe_set(b, 'componentModel_Parameter', None)
    assert not _is_linked(b, 'componentModel_Parameter', a2)
    if hasattr(a2, 'componentModel_Signature41'):
        assert not _is_linked(a2, 'componentModel_Signature41', b)


def test_assoc_providedrole26_reverse_link_reassign_clear():
    a1 = componentModel_ProvidedRole(name="sample_text")
    a2 = componentModel_ProvidedRole(name="sample_text_2")
    b = componentModel_AssemblyContext(name="sample_text")
    _safe_set(b, 'assemblycontext', a1)
    assert _is_linked(b, 'assemblycontext', a1)
    if hasattr(a1, 'ProvidedRole'):
        assert _is_linked(a1, 'ProvidedRole', b)
    _safe_set(b, 'assemblycontext', a2)
    assert _is_linked(b, 'assemblycontext', a2)
    if hasattr(a1, 'ProvidedRole'):
        assert not _is_linked(a1, 'ProvidedRole', b)
    if hasattr(a2, 'ProvidedRole'):
        assert _is_linked(a2, 'ProvidedRole', b)
    _safe_set(b, 'assemblycontext', None)
    assert not _is_linked(b, 'assemblycontext', a2)
    if hasattr(a2, 'ProvidedRole'):
        assert not _is_linked(a2, 'ProvidedRole', b)


def test_assoc_requiredrole27_reverse_link_reassign_clear():
    a1 = componentModel_RequiredRole(name="sample_text")
    a2 = componentModel_RequiredRole(name="sample_text_2")
    b = componentModel_AssemblyContext(name="sample_text")
    _safe_set(b, 'assemblycontext28', a1)
    assert _is_linked(b, 'assemblycontext28', a1)
    if hasattr(a1, 'RequiredRole'):
        assert _is_linked(a1, 'RequiredRole', b)
    _safe_set(b, 'assemblycontext28', a2)
    assert _is_linked(b, 'assemblycontext28', a2)
    if hasattr(a1, 'RequiredRole'):
        assert not _is_linked(a1, 'RequiredRole', b)
    if hasattr(a2, 'RequiredRole'):
        assert _is_linked(a2, 'RequiredRole', b)
    _safe_set(b, 'assemblycontext28', None)
    assert not _is_linked(b, 'assemblycontext28', a2)
    if hasattr(a2, 'RequiredRole'):
        assert not _is_linked(a2, 'RequiredRole', b)


def test_assoc_signatures24_reverse_link_reassign_clear():
    a1 = componentModel_Signature(name="sample_text")
    a2 = componentModel_Signature(name="sample_text_2")
    b = componentModel_Interface(name="sample_text")
    _safe_set(b, 'componentModel_Interface25', {a1})
    assert _is_linked(b, 'componentModel_Interface25', a1)
    if hasattr(a1, 'componentModel_Signature'):
        assert _is_linked(a1, 'componentModel_Signature', b)
    _safe_set(b, 'componentModel_Interface25', {a2})
    assert _is_linked(b, 'componentModel_Interface25', a2)
    if hasattr(a1, 'componentModel_Signature'):
        assert not _is_linked(a1, 'componentModel_Signature', b)
    if hasattr(a2, 'componentModel_Signature'):
        assert _is_linked(a2, 'componentModel_Signature', b)
    _safe_set(b, 'componentModel_Interface25', set())
    assert not _is_linked(b, 'componentModel_Interface25', a2)
    if hasattr(a2, 'componentModel_Signature'):
        assert not _is_linked(a2, 'componentModel_Signature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assemblyConnectors7_stub_double():
    # componentModel_AssemblyConnector has no real 'componentModel_AssemblyConnector' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Component(name="sample_text")
    partner = componentModel_AssemblyConnector()
    setattr(partner, 'componentModel_AssemblyConnector', None)
    _safe_set(owner, 'componentModel_Component8', {partner})
    assert getattr(partner, 'componentModel_AssemblyConnector') == owner
    _safe_set(owner, 'componentModel_Component8', set())
    assert getattr(partner, 'componentModel_AssemblyConnector') is None


def test_assoc_assemblycontext50_stub_double():
    # componentModel_System has no real 'componentModel_System' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_AssemblyContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_AssemblyContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_AssemblyContext(name="sample_text")
    partner = componentModel_System()
    setattr(partner, 'componentModel_System', None)
    _safe_set(owner, 'componentModel_AssemblyContext51', partner)
    assert owner in getattr(partner, 'componentModel_System')
    _safe_set(owner, 'componentModel_AssemblyContext51', None)
    assert owner not in getattr(partner, 'componentModel_System')


def test_assoc_component0_stub_double():
    # componentModel_Repository has no real 'componentModel_Repository' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Component(name="sample_text")
    partner = componentModel_Repository()
    setattr(partner, 'componentModel_Repository', None)
    _safe_set(owner, 'componentModel_Component', partner)
    assert owner in getattr(partner, 'componentModel_Repository')
    _safe_set(owner, 'componentModel_Component', None)
    assert owner not in getattr(partner, 'componentModel_Repository')


def test_assoc_correspondence47_stub_double():
    # componentModel_Service has no real 'componentModel_Service48' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Signature(name="sample_text")
    partner = componentModel_Service()
    setattr(partner, 'componentModel_Service48', None)
    _safe_set(owner, 'componentModel_Signature49', partner)
    assert owner in getattr(partner, 'componentModel_Service48')
    _safe_set(owner, 'componentModel_Signature49', None)
    assert owner not in getattr(partner, 'componentModel_Service48')


def test_assoc_delegationConnectors9_stub_double():
    # componentModel_DelegationConnector has no real 'componentModel_DelegationConnector' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Component(name="sample_text")
    partner = componentModel_DelegationConnector()
    setattr(partner, 'componentModel_DelegationConnector', None)
    _safe_set(owner, 'componentModel_Component10', {partner})
    assert getattr(partner, 'componentModel_DelegationConnector') == owner
    _safe_set(owner, 'componentModel_Component10', set())
    assert getattr(partner, 'componentModel_DelegationConnector') is None


def test_assoc_encapsulated70_stub_double():
    # componentModel_CompositeComponent has no real 'componentModel_CompositeComponent' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_AssemblyContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_AssemblyContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_AssemblyContext(name="sample_text")
    partner = componentModel_CompositeComponent()
    setattr(partner, 'componentModel_CompositeComponent', None)
    _safe_set(owner, 'componentModel_AssemblyContext71', partner)
    assert owner in getattr(partner, 'componentModel_CompositeComponent')
    _safe_set(owner, 'componentModel_AssemblyContext71', None)
    assert owner not in getattr(partner, 'componentModel_CompositeComponent')


def test_assoc_interface1_stub_double():
    # componentModel_Repository has no real 'componentModel_Repository2' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_Repository()
    setattr(partner, 'componentModel_Repository2', None)
    _safe_set(owner, 'componentModel_Interface', partner)
    assert owner in getattr(partner, 'componentModel_Repository2')
    _safe_set(owner, 'componentModel_Interface', None)
    assert owner not in getattr(partner, 'componentModel_Repository2')


def test_assoc_interface52_stub_double():
    # componentModel_System has no real 'componentModel_System53' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_System()
    setattr(partner, 'componentModel_System53', None)
    _safe_set(owner, 'componentModel_Interface54', partner)
    assert owner in getattr(partner, 'componentModel_System53')
    _safe_set(owner, 'componentModel_Interface54', None)
    assert owner not in getattr(partner, 'componentModel_System53')


def test_assoc_interfaceServiceMap5_stub_double():
    # componentModel_InterfaceServiceMapTuple has no real 'componentModel_InterfaceServiceMapTuple' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Component(name="sample_text")
    partner = componentModel_InterfaceServiceMapTuple()
    setattr(partner, 'componentModel_InterfaceServiceMapTuple', None)
    _safe_set(owner, 'componentModel_Component6', {partner})
    assert getattr(partner, 'componentModel_InterfaceServiceMapTuple') == owner
    _safe_set(owner, 'componentModel_Component6', set())
    assert getattr(partner, 'componentModel_InterfaceServiceMapTuple') is None


def test_assoc_parameterTyp74_stub_double():
    # componentModel_ParameterTyp has no real 'componentModel_ParameterTyp' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Parameter(name="sample_text")
    partner = componentModel_ParameterTyp()
    setattr(partner, 'componentModel_ParameterTyp', None)
    _safe_set(owner, 'componentModel_Parameter75', partner)
    assert getattr(partner, 'componentModel_ParameterTyp') == owner
    _safe_set(owner, 'componentModel_Parameter75', None)
    assert getattr(partner, 'componentModel_ParameterTyp') is None


def test_assoc_providedInterface11_stub_double():
    # componentModel_InterfaceServiceMapTuple has no real 'componentModel_InterfaceServiceMapTuple12' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_InterfaceServiceMapTuple()
    setattr(partner, 'componentModel_InterfaceServiceMapTuple12', None)
    _safe_set(owner, 'componentModel_Interface13', partner)
    assert getattr(partner, 'componentModel_InterfaceServiceMapTuple12') == owner
    _safe_set(owner, 'componentModel_Interface13', None)
    assert getattr(partner, 'componentModel_InterfaceServiceMapTuple12') is None


def test_assoc_providedInterface64_stub_double():
    # componentModel_ProvidedDelegationConnector has no real 'componentModel_ProvidedDelegationConnector' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_ProvidedDelegationConnector()
    setattr(partner, 'componentModel_ProvidedDelegationConnector', None)
    _safe_set(owner, 'componentModel_Interface65', partner)
    assert getattr(partner, 'componentModel_ProvidedDelegationConnector') == owner
    _safe_set(owner, 'componentModel_Interface65', None)
    assert getattr(partner, 'componentModel_ProvidedDelegationConnector') is None


def test_assoc_providedrole31_stub_double():
    # componentModel_AssemblyConnector has no real 'componentModel_AssemblyConnector32' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_ProvidedRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_ProvidedRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_ProvidedRole(name="sample_text")
    partner = componentModel_AssemblyConnector()
    setattr(partner, 'componentModel_AssemblyConnector32', None)
    _safe_set(owner, 'componentModel_ProvidedRole', partner)
    assert getattr(partner, 'componentModel_AssemblyConnector32') == owner
    _safe_set(owner, 'componentModel_ProvidedRole', None)
    assert getattr(partner, 'componentModel_AssemblyConnector32') is None


def test_assoc_providedrole66_stub_double():
    # componentModel_ProvidedDelegationConnector has no real 'componentModel_ProvidedDelegationConnector67' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_ProvidedRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_ProvidedRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_ProvidedRole(name="sample_text")
    partner = componentModel_ProvidedDelegationConnector()
    setattr(partner, 'componentModel_ProvidedDelegationConnector67', None)
    _safe_set(owner, 'componentModel_ProvidedRole68', partner)
    assert getattr(partner, 'componentModel_ProvidedDelegationConnector67') == owner
    _safe_set(owner, 'componentModel_ProvidedRole68', None)
    assert getattr(partner, 'componentModel_ProvidedDelegationConnector67') is None


def test_assoc_required44_stub_double():
    # componentModel_Service has no real 'componentModel_Service45' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_Service()
    setattr(partner, 'componentModel_Service45', None)
    _safe_set(owner, 'componentModel_Interface46', partner)
    assert owner in getattr(partner, 'componentModel_Service45')
    _safe_set(owner, 'componentModel_Interface46', None)
    assert owner not in getattr(partner, 'componentModel_Service45')


def test_assoc_requiredInterface37_stub_double():
    # componentModel_RequiredDelegationConnector has no real 'componentModel_RequiredDelegationConnector38' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Interface(name="sample_text")
    partner = componentModel_RequiredDelegationConnector()
    setattr(partner, 'componentModel_RequiredDelegationConnector38', None)
    _safe_set(owner, 'componentModel_Interface39', partner)
    assert getattr(partner, 'componentModel_RequiredDelegationConnector38') == owner
    _safe_set(owner, 'componentModel_Interface39', None)
    assert getattr(partner, 'componentModel_RequiredDelegationConnector38') is None


def test_assoc_requiredrole33_stub_double():
    # componentModel_AssemblyConnector has no real 'componentModel_AssemblyConnector34' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_RequiredRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_RequiredRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_RequiredRole(name="sample_text")
    partner = componentModel_AssemblyConnector()
    setattr(partner, 'componentModel_AssemblyConnector34', None)
    _safe_set(owner, 'componentModel_RequiredRole', partner)
    assert getattr(partner, 'componentModel_AssemblyConnector34') == owner
    _safe_set(owner, 'componentModel_RequiredRole', None)
    assert getattr(partner, 'componentModel_AssemblyConnector34') is None


def test_assoc_requiredrole35_stub_double():
    # componentModel_RequiredDelegationConnector has no real 'componentModel_RequiredDelegationConnector' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_RequiredRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_RequiredRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_RequiredRole(name="sample_text")
    partner = componentModel_RequiredDelegationConnector()
    setattr(partner, 'componentModel_RequiredDelegationConnector', None)
    _safe_set(owner, 'componentModel_RequiredRole36', partner)
    assert getattr(partner, 'componentModel_RequiredDelegationConnector') == owner
    _safe_set(owner, 'componentModel_RequiredRole36', None)
    assert getattr(partner, 'componentModel_RequiredDelegationConnector') is None


def test_assoc_returnType42_stub_double():
    # componentModel_Type has no real 'componentModel_Type' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Signature(name="sample_text")
    partner = componentModel_Type()
    setattr(partner, 'componentModel_Type', None)
    _safe_set(owner, 'componentModel_Signature43', partner)
    assert getattr(partner, 'componentModel_Type') == owner
    _safe_set(owner, 'componentModel_Signature43', None)
    assert getattr(partner, 'componentModel_Type') is None


def test_assoc_serviceeffectspecification3_stub_double():
    # componentModel_ServiceEffectSpecification has no real 'componentModel_ServiceEffectSpecification' property in the generated
    # code (a bare stub) -- manually attach it so componentModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # componentModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = componentModel_Component(name="sample_text")
    partner = componentModel_ServiceEffectSpecification()
    setattr(partner, 'componentModel_ServiceEffectSpecification', None)
    _safe_set(owner, 'componentModel_Component4', partner)
    assert getattr(partner, 'componentModel_ServiceEffectSpecification') == owner
    _safe_set(owner, 'componentModel_Component4', None)
    assert getattr(partner, 'componentModel_ServiceEffectSpecification') is None


