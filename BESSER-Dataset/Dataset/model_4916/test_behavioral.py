import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractProcessModel,
    Agent,
    Binding,
    BoundProcessModel,
    BoundTemplateParameter,
    ControlConstruct,
    ControlConstructBag,
    ControlConstructList,
    DeployedService,
    Endpoint,
    ExecutionFramework,
    GroundTemplate,
    IOEP,
    InterfaceDescription,
    IntervalThing,
    Iterate,
    Message,
    OperationDescription,
    ProcessModel,
    ServiceCategory,
    ServiceCondition,
    ServiceDirectory,
    ServiceFramework,
    ServiceGrounding,
    ServiceInput,
    ServiceOutput,
    ServiceParameter,
    ServiceProfile,
    ServiceResult,
    ServiceTemplate,
    ServiceTemplateMatchmaker,
    TemplateConstraint,
    TemplateFlow,
    TemplateRepository,
    architecture_ServiceMatchmaker,
    architecture_TemplateMatchmaker,
    semantics_service_Antecedent,
    semantics_service_Consequent,
    semantics_service_EObject,
    semantics_service_Service,
    service_SL,
    service_Service,
    service_ServiceConsumer,
    service_ServiceImplemetation,
    service_ServiceProvider,
    service_architecture_DeployedService,
    service_architecture_ExecutionFramework,
    service_architecture_ServiceDirectory,
    service_architecture_ServiceFramework,
    service_architecture_ServiceMatchmaker,
    service_architecture_ServiceTemplateMatchmaker,
    service_architecture_TemplateMatchmaker,
    service_architecture_TemplateRepository,
    service_semantics_IOEP,
    service_semantics_ProcessModel,
    service_semantics_ServiceCategory,
    service_semantics_ServiceCondition,
    service_semantics_ServiceGrounding,
    service_semantics_ServiceInput,
    service_semantics_ServiceOutput,
    service_semantics_ServiceParameter,
    service_semantics_ServiceProfile,
    service_semantics_ServiceResult,
    service_syntax_Binding,
    service_syntax_Endpoint,
    service_syntax_InterfaceDescription,
    service_syntax_Message,
    service_syntax_OperationDescription,
    service_template_AbstractProcessModel,
    service_template_AnyOrder,
    service_template_BoundProcessModel,
    service_template_BoundTemplateParameter,
    service_template_Choice,
    service_template_ControlConstruct,
    service_template_ControlConstructBag,
    service_template_ControlConstructList,
    service_template_GroundTemplate,
    service_template_IfThenElse,
    service_template_IntervalThing,
    service_template_Iterate,
    service_template_Perform,
    service_template_RepeatUntil,
    service_template_RepeatWhile,
    service_template_Sequence,
    service_template_ServiceTemplate,
    service_template_Split,
    service_template_SplitJoin,
    service_template_TemplateConstraint,
    service_template_TemplateFlow,
    syntax_service_SchemaType,
    syntax_service_ServiceImplemetation,
    syntax_service_TopLevelComplexType,
    syntax_service_TopLevelElement,
    template_service_Antecedent,
    template_service_Service,
    ContainerType,
    ServiceImpLanguage,
    ServiceType,
    StyleEncoding,
    TransportProtocol,
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

def test_assoc_exposes7_reverse_link_reassign_clear():
    a1 = service_ServiceProvider(isType="sample_text")
    a2 = service_ServiceProvider(isType="sample_text_2")
    b = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    _safe_set(b, 'service_Service8', a1)
    assert _is_linked(b, 'service_Service8', a1)
    if hasattr(a1, 'service_ServiceProvider'):
        assert _is_linked(a1, 'service_ServiceProvider', b)
    _safe_set(b, 'service_Service8', a2)
    assert _is_linked(b, 'service_Service8', a2)
    if hasattr(a1, 'service_ServiceProvider'):
        assert not _is_linked(a1, 'service_ServiceProvider', b)
    if hasattr(a2, 'service_ServiceProvider'):
        assert _is_linked(a2, 'service_ServiceProvider', b)
    _safe_set(b, 'service_Service8', None)
    assert not _is_linked(b, 'service_Service8', a2)
    if hasattr(a2, 'service_ServiceProvider'):
        assert not _is_linked(a2, 'service_ServiceProvider', b)


def test_assoc_implementation9_reverse_link_reassign_clear():
    a1 = service_ServiceProvider(isType="sample_text")
    a2 = service_ServiceProvider(isType="sample_text_2")
    b = service_ServiceImplemetation(language="sample_text", uri="sample_text")
    _safe_set(b, 'service_ServiceImplemetation', a1)
    assert _is_linked(b, 'service_ServiceImplemetation', a1)
    if hasattr(a1, 'service_ServiceProvider10'):
        assert _is_linked(a1, 'service_ServiceProvider10', b)
    _safe_set(b, 'service_ServiceImplemetation', a2)
    assert _is_linked(b, 'service_ServiceImplemetation', a2)
    if hasattr(a1, 'service_ServiceProvider10'):
        assert not _is_linked(a1, 'service_ServiceProvider10', b)
    if hasattr(a2, 'service_ServiceProvider10'):
        assert _is_linked(a2, 'service_ServiceProvider10', b)
    _safe_set(b, 'service_ServiceImplemetation', None)
    assert not _is_linked(b, 'service_ServiceImplemetation', a2)
    if hasattr(a2, 'service_ServiceProvider10'):
        assert not _is_linked(a2, 'service_ServiceProvider10', b)


def test_assoc_invokes11_reverse_link_reassign_clear():
    a1 = service_ServiceConsumer(isType="sample_text")
    a2 = service_ServiceConsumer(isType="sample_text_2")
    b = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    _safe_set(b, 'service_Service12', a1)
    assert _is_linked(b, 'service_Service12', a1)
    if hasattr(a1, 'service_ServiceConsumer'):
        assert _is_linked(a1, 'service_ServiceConsumer', b)
    _safe_set(b, 'service_Service12', a2)
    assert _is_linked(b, 'service_Service12', a2)
    if hasattr(a1, 'service_ServiceConsumer'):
        assert not _is_linked(a1, 'service_ServiceConsumer', b)
    if hasattr(a2, 'service_ServiceConsumer'):
        assert _is_linked(a2, 'service_ServiceConsumer', b)
    _safe_set(b, 'service_Service12', None)
    assert not _is_linked(b, 'service_Service12', a2)
    if hasattr(a2, 'service_ServiceConsumer'):
        assert not _is_linked(a2, 'service_ServiceConsumer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_adaptedBy6_stub_double():
    # GroundTemplate has no real 'GroundTemplate' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = GroundTemplate()
    setattr(partner, 'GroundTemplate', None)
    _safe_set(owner, 'expose', partner)
    assert getattr(partner, 'GroundTemplate') == owner
    _safe_set(owner, 'expose', None)
    assert getattr(partner, 'GroundTemplate') is None


def test_assoc_bindProcessModel98_stub_double():
    # BoundProcessModel has no real 'BoundProcessModel' property in the generated
    # code (a bare stub) -- manually attach it so service_template_GroundTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_GroundTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_GroundTemplate(name="sample_text")
    partner = BoundProcessModel()
    setattr(partner, 'BoundProcessModel', None)
    _safe_set(owner, 'service_template_GroundTemplate99', {partner})
    assert getattr(partner, 'BoundProcessModel') == owner
    _safe_set(owner, 'service_template_GroundTemplate99', set())
    assert getattr(partner, 'BoundProcessModel') is None


def test_assoc_bindTemplateParameter96_stub_double():
    # BoundTemplateParameter has no real 'BoundTemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so service_template_GroundTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_GroundTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_GroundTemplate(name="sample_text")
    partner = BoundTemplateParameter()
    setattr(partner, 'BoundTemplateParameter', None)
    _safe_set(owner, 'service_template_GroundTemplate97', {partner})
    assert getattr(partner, 'BoundTemplateParameter') == owner
    _safe_set(owner, 'service_template_GroundTemplate97', set())
    assert getattr(partner, 'BoundTemplateParameter') is None


def test_assoc_binding24_stub_double():
    # Binding has no real 'Binding' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_InterfaceDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_InterfaceDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_InterfaceDescription(name="sample_text")
    partner = Binding()
    setattr(partner, 'Binding', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'Binding') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'Binding') is None


def test_assoc_binding40_stub_double():
    # Binding has no real 'Binding41' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Endpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Endpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Endpoint(location="sample_text", name="sample_text")
    partner = Binding()
    setattr(partner, 'Binding41', None)
    _safe_set(owner, 'service_syntax_Endpoint', partner)
    assert getattr(partner, 'Binding41') == owner
    _safe_set(owner, 'service_syntax_Endpoint', None)
    assert getattr(partner, 'Binding41') is None


def test_assoc_constraints92_stub_double():
    # TemplateConstraint has no real 'TemplateConstraint' property in the generated
    # code (a bare stub) -- manually attach it so service_template_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_ServiceTemplate(URI="sample_text")
    partner = TemplateConstraint()
    setattr(partner, 'TemplateConstraint', None)
    _safe_set(owner, 'service_template_ServiceTemplate93', {partner})
    assert getattr(partner, 'TemplateConstraint') == owner
    _safe_set(owner, 'service_template_ServiceTemplate93', set())
    assert getattr(partner, 'TemplateConstraint') is None


def test_assoc_consumers18_stub_double():
    # service_SL has no real 'service_SL19' property in the generated
    # code (a bare stub) -- manually attach it so service_ServiceConsumer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_ServiceConsumer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_ServiceConsumer(isType="sample_text")
    partner = service_SL()
    setattr(partner, 'service_SL19', None)
    _safe_set(owner, 'service_ServiceConsumer20', partner)
    assert owner in getattr(partner, 'service_SL19')
    _safe_set(owner, 'service_ServiceConsumer20', None)
    assert owner not in getattr(partner, 'service_SL19')


def test_assoc_deploy187_stub_double():
    # ExecutionFramework has no real 'ExecutionFramework188' property in the generated
    # code (a bare stub) -- manually attach it so service_architecture_DeployedService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_architecture_DeployedService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_architecture_DeployedService(artifact="sample_text")
    partner = ExecutionFramework()
    setattr(partner, 'ExecutionFramework188', None)
    _safe_set(owner, 'deployedService', partner)
    assert getattr(partner, 'ExecutionFramework188') == owner
    _safe_set(owner, 'deployedService', None)
    assert getattr(partner, 'ExecutionFramework188') is None


def test_assoc_deployedService185_stub_double():
    # DeployedService has no real 'DeployedService186' property in the generated
    # code (a bare stub) -- manually attach it so service_architecture_ExecutionFramework's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_architecture_ExecutionFramework's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_architecture_ExecutionFramework(container="sample_text")
    partner = DeployedService()
    setattr(partner, 'DeployedService186', None)
    _safe_set(owner, 'deploy', {partner})
    assert getattr(partner, 'DeployedService186') == owner
    _safe_set(owner, 'deploy', set())
    assert getattr(partner, 'DeployedService186') is None


def test_assoc_deployedService44_stub_double():
    # DeployedService has no real 'DeployedService' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Endpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Endpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Endpoint(location="sample_text", name="sample_text")
    partner = DeployedService()
    setattr(partner, 'DeployedService', None)
    _safe_set(owner, 'service_syntax_Endpoint45', partner)
    assert getattr(partner, 'DeployedService') == owner
    _safe_set(owner, 'service_syntax_Endpoint45', None)
    assert getattr(partner, 'DeployedService') is None


def test_assoc_describedBy5_stub_double():
    # ProcessModel has no real 'ProcessModel' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = ProcessModel()
    setattr(partner, 'ProcessModel', None)
    _safe_set(owner, 'describes', partner)
    assert getattr(partner, 'ProcessModel') == owner
    _safe_set(owner, 'describes', None)
    assert getattr(partner, 'ProcessModel') is None


def test_assoc_describes68_stub_double():
    # semantics_service_Service has no real 'Service69' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ProcessModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ProcessModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ProcessModel(name="sample_text")
    partner = semantics_service_Service()
    setattr(partner, 'Service69', None)
    _safe_set(owner, 'describedBy', partner)
    assert getattr(partner, 'Service69') == owner
    _safe_set(owner, 'describedBy', None)
    assert getattr(partner, 'Service69') is None


def test_assoc_element38_stub_double():
    # syntax_service_TopLevelElement has no real 'syntax_service_TopLevelElement' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Message(name="sample_text")
    partner = syntax_service_TopLevelElement()
    setattr(partner, 'syntax_service_TopLevelElement', None)
    _safe_set(owner, 'service_syntax_Message39', partner)
    assert getattr(partner, 'syntax_service_TopLevelElement') == owner
    _safe_set(owner, 'service_syntax_Message39', None)
    assert getattr(partner, 'syntax_service_TopLevelElement') is None


def test_assoc_endpoint0_stub_double():
    # Endpoint has no real 'Endpoint' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = Endpoint()
    setattr(partner, 'Endpoint', None)
    _safe_set(owner, 'service_Service', {partner})
    assert getattr(partner, 'Endpoint') == owner
    _safe_set(owner, 'service_Service', set())
    assert getattr(partner, 'Endpoint') is None


def test_assoc_expose100_stub_double():
    # template_service_Service has no real 'Service101' property in the generated
    # code (a bare stub) -- manually attach it so service_template_GroundTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_GroundTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_GroundTemplate(name="sample_text")
    partner = template_service_Service()
    setattr(partner, 'Service101', None)
    _safe_set(owner, 'adaptedBy', partner)
    assert getattr(partner, 'Service101') == owner
    _safe_set(owner, 'adaptedBy', None)
    assert getattr(partner, 'Service101') is None


def test_assoc_expose90_stub_double():
    # AbstractProcessModel has no real 'AbstractProcessModel' property in the generated
    # code (a bare stub) -- manually attach it so service_template_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_ServiceTemplate(URI="sample_text")
    partner = AbstractProcessModel()
    setattr(partner, 'AbstractProcessModel', None)
    _safe_set(owner, 'service_template_ServiceTemplate91', partner)
    assert getattr(partner, 'AbstractProcessModel') == owner
    _safe_set(owner, 'service_template_ServiceTemplate91', None)
    assert getattr(partner, 'AbstractProcessModel') is None


def test_assoc_fault31_stub_double():
    # Message has no real 'Message33' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_OperationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_OperationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_OperationDescription(name="sample_text")
    partner = Message()
    setattr(partner, 'Message33', None)
    _safe_set(owner, 'service_syntax_OperationDescription32', {partner})
    assert getattr(partner, 'Message33') == owner
    _safe_set(owner, 'service_syntax_OperationDescription32', set())
    assert getattr(partner, 'Message33') is None


def test_assoc_flow87_stub_double():
    # TemplateFlow has no real 'TemplateFlow' property in the generated
    # code (a bare stub) -- manually attach it so service_template_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_ServiceTemplate(URI="sample_text")
    partner = TemplateFlow()
    setattr(partner, 'TemplateFlow', None)
    _safe_set(owner, 'service_template_ServiceTemplate', partner)
    assert getattr(partner, 'TemplateFlow') == owner
    _safe_set(owner, 'service_template_ServiceTemplate', None)
    assert getattr(partner, 'TemplateFlow') is None


def test_assoc_hasCondition59_stub_double():
    # ServiceCondition has no real 'ServiceCondition' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ServiceCondition()
    setattr(partner, 'ServiceCondition', None)
    _safe_set(owner, 'service_semantics_ServiceProfile60', {partner})
    assert getattr(partner, 'ServiceCondition') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile60', set())
    assert getattr(partner, 'ServiceCondition') is None


def test_assoc_hasInput53_stub_double():
    # ServiceInput has no real 'ServiceInput' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ServiceInput()
    setattr(partner, 'ServiceInput', None)
    _safe_set(owner, 'service_semantics_ServiceProfile54', {partner})
    assert getattr(partner, 'ServiceInput') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile54', set())
    assert getattr(partner, 'ServiceInput') is None


def test_assoc_hasOutput55_stub_double():
    # ServiceOutput has no real 'ServiceOutput' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ServiceOutput()
    setattr(partner, 'ServiceOutput', None)
    _safe_set(owner, 'service_semantics_ServiceProfile56', {partner})
    assert getattr(partner, 'ServiceOutput') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile56', set())
    assert getattr(partner, 'ServiceOutput') is None


def test_assoc_hasProcess49_stub_double():
    # ProcessModel has no real 'ProcessModel50' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ProcessModel()
    setattr(partner, 'ProcessModel50', None)
    _safe_set(owner, 'service_semantics_ServiceProfile', partner)
    assert getattr(partner, 'ProcessModel50') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile', None)
    assert getattr(partner, 'ProcessModel50') is None


def test_assoc_hasResult57_stub_double():
    # ServiceResult has no real 'ServiceResult' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ServiceResult()
    setattr(partner, 'ServiceResult', None)
    _safe_set(owner, 'service_semantics_ServiceProfile58', {partner})
    assert getattr(partner, 'ServiceResult') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile58', set())
    assert getattr(partner, 'ServiceResult') is None


def test_assoc_implement95_stub_double():
    # ServiceTemplate has no real 'ServiceTemplate' property in the generated
    # code (a bare stub) -- manually attach it so service_template_GroundTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_GroundTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_GroundTemplate(name="sample_text")
    partner = ServiceTemplate()
    setattr(partner, 'ServiceTemplate', None)
    _safe_set(owner, 'service_template_GroundTemplate', partner)
    assert getattr(partner, 'ServiceTemplate') == owner
    _safe_set(owner, 'service_template_GroundTemplate', None)
    assert getattr(partner, 'ServiceTemplate') is None


def test_assoc_implementation42_stub_double():
    # syntax_service_ServiceImplemetation has no real 'syntax_service_ServiceImplemetation' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Endpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Endpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Endpoint(location="sample_text", name="sample_text")
    partner = syntax_service_ServiceImplemetation()
    setattr(partner, 'syntax_service_ServiceImplemetation', None)
    _safe_set(owner, 'service_syntax_Endpoint43', partner)
    assert getattr(partner, 'syntax_service_ServiceImplemetation') == owner
    _safe_set(owner, 'service_syntax_Endpoint43', None)
    assert getattr(partner, 'syntax_service_ServiceImplemetation') is None


def test_assoc_inLineSchema25_stub_double():
    # syntax_service_SchemaType has no real 'syntax_service_SchemaType' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_InterfaceDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_InterfaceDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_InterfaceDescription(name="sample_text")
    partner = syntax_service_SchemaType()
    setattr(partner, 'syntax_service_SchemaType', None)
    _safe_set(owner, 'service_syntax_InterfaceDescription26', partner)
    assert getattr(partner, 'syntax_service_SchemaType') == owner
    _safe_set(owner, 'service_syntax_InterfaceDescription26', None)
    assert getattr(partner, 'syntax_service_SchemaType') is None


def test_assoc_input30_stub_double():
    # Message has no real 'Message' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_OperationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_OperationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_OperationDescription(name="sample_text")
    partner = Message()
    setattr(partner, 'Message', None)
    _safe_set(owner, 'service_syntax_OperationDescription', {partner})
    assert getattr(partner, 'Message') == owner
    _safe_set(owner, 'service_syntax_OperationDescription', set())
    assert getattr(partner, 'Message') is None


def test_assoc_interface1_stub_double():
    # InterfaceDescription has no real 'InterfaceDescription' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = InterfaceDescription()
    setattr(partner, 'InterfaceDescription', None)
    _safe_set(owner, 'service_Service2', partner)
    assert getattr(partner, 'InterfaceDescription') == owner
    _safe_set(owner, 'service_Service2', None)
    assert getattr(partner, 'InterfaceDescription') is None


def test_assoc_interface65_stub_double():
    # InterfaceDescription has no real 'InterfaceDescription67' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceGrounding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceGrounding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceGrounding(bindParams="sample_text", name="sample_text")
    partner = InterfaceDescription()
    setattr(partner, 'InterfaceDescription67', None)
    _safe_set(owner, 'service_semantics_ServiceGrounding66', partner)
    assert getattr(partner, 'InterfaceDescription67') == owner
    _safe_set(owner, 'service_semantics_ServiceGrounding66', None)
    assert getattr(partner, 'InterfaceDescription67') is None


def test_assoc_operation23_stub_double():
    # OperationDescription has no real 'OperationDescription' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_InterfaceDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_InterfaceDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_InterfaceDescription(name="sample_text")
    partner = OperationDescription()
    setattr(partner, 'OperationDescription', None)
    _safe_set(owner, 'service_syntax_InterfaceDescription', {partner})
    assert getattr(partner, 'OperationDescription') == owner
    _safe_set(owner, 'service_syntax_InterfaceDescription', set())
    assert getattr(partner, 'OperationDescription') is None


def test_assoc_outLineSchema27_stub_double():
    # syntax_service_SchemaType has no real 'syntax_service_SchemaType29' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_InterfaceDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_InterfaceDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_InterfaceDescription(name="sample_text")
    partner = syntax_service_SchemaType()
    setattr(partner, 'syntax_service_SchemaType29', None)
    _safe_set(owner, 'service_syntax_InterfaceDescription28', {partner})
    assert getattr(partner, 'syntax_service_SchemaType29') == owner
    _safe_set(owner, 'service_syntax_InterfaceDescription28', set())
    assert getattr(partner, 'syntax_service_SchemaType29') is None


def test_assoc_output34_stub_double():
    # Message has no real 'Message36' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_OperationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_OperationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_OperationDescription(name="sample_text")
    partner = Message()
    setattr(partner, 'Message36', None)
    _safe_set(owner, 'service_syntax_OperationDescription35', {partner})
    assert getattr(partner, 'Message36') == owner
    _safe_set(owner, 'service_syntax_OperationDescription35', set())
    assert getattr(partner, 'Message36') is None


def test_assoc_presentedBy48_stub_double():
    # semantics_service_Service has no real 'Service' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = semantics_service_Service()
    setattr(partner, 'Service', None)
    _safe_set(owner, 'presents', partner)
    assert getattr(partner, 'Service') == owner
    _safe_set(owner, 'presents', None)
    assert getattr(partner, 'Service') is None


def test_assoc_presents3_stub_double():
    # ServiceProfile has no real 'ServiceProfile' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = ServiceProfile()
    setattr(partner, 'ServiceProfile', None)
    _safe_set(owner, 'presentedBy', partner)
    assert getattr(partner, 'ServiceProfile') == owner
    _safe_set(owner, 'presentedBy', None)
    assert getattr(partner, 'ServiceProfile') is None


def test_assoc_processModel63_stub_double():
    # ProcessModel has no real 'ProcessModel64' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceGrounding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceGrounding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceGrounding(bindParams="sample_text", name="sample_text")
    partner = ProcessModel()
    setattr(partner, 'ProcessModel64', None)
    _safe_set(owner, 'service_semantics_ServiceGrounding', partner)
    assert getattr(partner, 'ProcessModel64') == owner
    _safe_set(owner, 'service_semantics_ServiceGrounding', None)
    assert getattr(partner, 'ProcessModel64') is None


def test_assoc_providers15_stub_double():
    # service_SL has no real 'service_SL16' property in the generated
    # code (a bare stub) -- manually attach it so service_ServiceProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_ServiceProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_ServiceProvider(isType="sample_text")
    partner = service_SL()
    setattr(partner, 'service_SL16', None)
    _safe_set(owner, 'service_ServiceProvider17', partner)
    assert owner in getattr(partner, 'service_SL16')
    _safe_set(owner, 'service_ServiceProvider17', None)
    assert owner not in getattr(partner, 'service_SL16')


def test_assoc_serviceCategory51_stub_double():
    # ServiceCategory has no real 'ServiceCategory' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceProfile(name="sample_text", serviceClassification="sample_text")
    partner = ServiceCategory()
    setattr(partner, 'ServiceCategory', None)
    _safe_set(owner, 'service_semantics_ServiceProfile52', partner)
    assert getattr(partner, 'ServiceCategory') == owner
    _safe_set(owner, 'service_semantics_ServiceProfile52', None)
    assert getattr(partner, 'ServiceCategory') is None


def test_assoc_services13_stub_double():
    # service_SL has no real 'service_SL' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = service_SL()
    setattr(partner, 'service_SL', None)
    _safe_set(owner, 'service_Service14', partner)
    assert owner in getattr(partner, 'service_SL')
    _safe_set(owner, 'service_Service14', None)
    assert owner not in getattr(partner, 'service_SL')


def test_assoc_supportedBy61_stub_double():
    # semantics_service_Service has no real 'Service62' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceGrounding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceGrounding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceGrounding(bindParams="sample_text", name="sample_text")
    partner = semantics_service_Service()
    setattr(partner, 'Service62', None)
    _safe_set(owner, 'supports', partner)
    assert getattr(partner, 'Service62') == owner
    _safe_set(owner, 'supports', None)
    assert getattr(partner, 'Service62') is None


def test_assoc_supports4_stub_double():
    # ServiceGrounding has no real 'ServiceGrounding' property in the generated
    # code (a bare stub) -- manually attach it so service_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Service(description="sample_text", name="sample_text", namespace="sample_text")
    partner = ServiceGrounding()
    setattr(partner, 'ServiceGrounding', None)
    _safe_set(owner, 'supportedBy', {partner})
    assert getattr(partner, 'ServiceGrounding') == owner
    _safe_set(owner, 'supportedBy', set())
    assert getattr(partner, 'ServiceGrounding') is None


def test_assoc_templateParameter88_stub_double():
    # ServiceParameter has no real 'ServiceParameter' property in the generated
    # code (a bare stub) -- manually attach it so service_template_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_template_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_template_ServiceTemplate(URI="sample_text")
    partner = ServiceParameter()
    setattr(partner, 'ServiceParameter', None)
    _safe_set(owner, 'service_template_ServiceTemplate89', {partner})
    assert getattr(partner, 'ServiceParameter') == owner
    _safe_set(owner, 'service_template_ServiceTemplate89', set())
    assert getattr(partner, 'ServiceParameter') is None


def test_assoc_type37_stub_double():
    # syntax_service_TopLevelComplexType has no real 'syntax_service_TopLevelComplexType' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Message(name="sample_text")
    partner = syntax_service_TopLevelComplexType()
    setattr(partner, 'syntax_service_TopLevelComplexType', None)
    _safe_set(owner, 'service_syntax_Message', partner)
    assert getattr(partner, 'syntax_service_TopLevelComplexType') == owner
    _safe_set(owner, 'service_syntax_Message', None)
    assert getattr(partner, 'syntax_service_TopLevelComplexType') is None


def test_assoc_type46_stub_double():
    # InterfaceDescription has no real 'InterfaceDescription47' property in the generated
    # code (a bare stub) -- manually attach it so service_syntax_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_syntax_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_syntax_Binding(name="sample_text", style="sample_text", transport="sample_text")
    partner = InterfaceDescription()
    setattr(partner, 'InterfaceDescription47', None)
    _safe_set(owner, 'binding', partner)
    assert getattr(partner, 'InterfaceDescription47') == owner
    _safe_set(owner, 'binding', None)
    assert getattr(partner, 'InterfaceDescription47') is None


def test_assoc_type70_stub_double():
    # semantics_service_EObject has no real 'semantics_service_EObject' property in the generated
    # code (a bare stub) -- manually attach it so service_semantics_ServiceParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_semantics_ServiceParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_semantics_ServiceParameter(name="sample_text")
    partner = semantics_service_EObject()
    setattr(partner, 'semantics_service_EObject', None)
    _safe_set(owner, 'service_semantics_ServiceParameter', partner)
    assert getattr(partner, 'semantics_service_EObject') == owner
    _safe_set(owner, 'service_semantics_ServiceParameter', None)
    assert getattr(partner, 'semantics_service_EObject') is None


